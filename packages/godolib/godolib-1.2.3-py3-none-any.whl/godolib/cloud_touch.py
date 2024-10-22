import boto3
import os
import json
import pandas as pd
import numpy as np
from io import BytesIO, StringIO
import pickle
import h5py
import requests
from concurrent.futures import ThreadPoolExecutor
from datetime import date
import time

class DataExtractor():
    """
    Clase para extraer datos históricos de precios utilizando la API de EODHD.
    
    Atributos:
    ----------
    eod_token : str
        Token de acceso para la API de EODHD.
    """

    def __init__(self, eod_token):
        """
        Inicializa la clase con el token de la API.

        Parámetros:
        -----------
        eod_token : str
            Token para la autenticación en la API de EODHD.
        """
        self.eod_token = eod_token
    def eod_extract(self, symbol, freq, start_date=None, end_date=None, exchange='US', fmt='csv', intraday_spot=['Close'], historical_spot=['Adjusted_close']):
        """
        Extrae datos históricos o intradía de un símbolo financiero utilizando la API de EOD Historical Data.
    
        Parámetros:
        -----------
        symbol : str
            El ticker del activo financiero (e.g., 'AAPL' para Apple).
        freq : str
            La frecuencia de los datos a extraer. Valores permitidos: ['m', 'w', 'd', '1h', '5m', '1m'].
            'm' - mensual, 'w' - semanal, 'd' - diario, '1h' - cada hora, '5m' - cada 5 minutos, '1m' - cada minuto.
        start_date : int, opcional
            Timestamp de inicio para la extracción de datos en formato UNIX. Si no se especifica, calcula automáticamente
            basado en la máxima duración permitida por la frecuencia elegida.
        end_date : int, opcional
            Timestamp de fin para la extracción de datos en formato UNIX. Si no se especifica, se usa el timestamp actual.
        exchange : str, opcional
            El código del mercado de valores en el que se negocia el símbolo, por defecto es 'US'.
        fmt : str, opcional
            El formato de salida de los datos. Valores permitidos: 'csv' (por defecto), 'json'.
        intraday_spot : list, opcional
            Las columnas específicas a retornar para datos intradía. Por defecto es ['Close'].
        historical_spot : list, opcional
            Las columnas específicas a retornar para datos históricos. Por defecto es ['Adjusted_close'].
    
        Retorna:
        --------
        pd.DataFrame
            Un DataFrame de pandas con las columnas especificadas, indexado por la fecha y hora de los datos.
            Para datos intradía, el índice será 'Datetime' y para datos históricos, será 'Date'.
    
        Levanta:
        --------
        ValueError
            Si la 'freq' no está en las frecuencias válidas o si los periodos entre 'start_date' y 'end_date'
            exceden los máximos permitidos para la frecuencia especificada.
    
        Ejemplo:
        --------
        >>> data_extractor = DataExtractor(eod_token='your_api_token')
        >>> aapl_data = data_extractor.eod_extract_('AAPL', '1h', exchange='US', fmt='csv')
        >>> print(aapl_data.head())
        """
        valid_frequencies = ['m', 'w', 'd', '1h', '5m', '1m']
        if freq not in valid_frequencies:
            raise ValueError(f"freq parameter must be one of: {valid_frequencies}")
        if freq in ['1h', '5m', '1m']:
            if not end_date:
                end_date = int(time.time())
            if not start_date:
                start_date = end_date - 120 * 24 * 60 * 60
            if ((end_date - start_date) / (24 * 3600) > 120) & (freq == '1m'):
                raise ValueError('maximum periods between dates are 120 days for 1-minute frequency')
            elif ((end_date - start_date) / (24 * 3600) > 600) & (freq == '5m'):
                raise ValueError('maximum periods between dates are 600 days for 5-minute frequency')
            elif ((end_date - start_date) / (24 * 3600) > 7200) & (freq == '1h'):
                raise ValueError('maximum periods between dates are 7200 days for 1-hour frequency')
            url = f'https://eodhd.com/api/intraday/{symbol}.{exchange}?from={start_date}&to={end_date}&interval={freq}&api_token={self.eod_token}&fmt={fmt}'
            data = requests.get(url).content
            df = self._decode_(data)
            df['Datetime'] = pd.to_datetime(df['Datetime'])
            df.set_index('Datetime', inplace=True)
            return df[intraday_spot]
        else:
            if not end_date:
                end_date = self._today_date_()
            if not start_date:
                start_date = '1900-01-01'
            url = f'https://eodhd.com/api/eod/{symbol}.{exchange}?from={start_date}&to={end_date}&period={freq}&api_token={self.eod_token}&fmt={fmt}'
            data = requests.get(url).content
            df = self._decode_(data)
            df['Date'] = pd.to_datetime(df['Date'])
            df.set_index('Date', inplace=True)
            return df[historical_spot]

    def extract_multiple(self, symbols, freq='d', start_date=None, end_date=None, exchange='US', fmt='csv', intraday_spot=['Close'], historical_spot=['Adjusted_close'], max_workers=5):
        """
        Extrae datos históricos o intradía para múltiples símbolos de forma paralela.
    
        Parámetros:
        -----------
        symbols : list
            Lista de símbolos de los activos financieros.
        freq : str, opcional
            Frecuencia de los datos ('m', 'w', 'd', '1h', '5m', '1m'). Por defecto es 'd' para datos diarios.
        start_date : int, opcional
            Timestamp de inicio para la extracción de datos en formato UNIX. Si no se especifica, se calcula automáticamente.
        end_date : int, opcional
            Timestamp de fin para la extracción de datos en formato UNIX. Si no se especifica, se utiliza el timestamp actual.
        exchange : str, opcional
            Código del mercado de valores. Por defecto es 'US'.
        fmt : str, opcional
            Formato de los datos recibidos (‘json’ o ‘csv’). Por defecto es 'csv'.
        intraday_spot : list, opcional
            Columnas que se devolverán para datos intradía. Por defecto es ['Close'].
        historical_spot : list, opcional
            Columnas que se devolverán para datos históricos. Por defecto es ['Adjusted_close'].
        max_workers : int, opcional
            Número máximo de hilos de ejecución en paralelo. Por defecto es 5.
    
        Retorna:
        --------
        pd.DataFrame
            DataFrame con los datos históricos o intradía de los símbolos, con las columnas nombradas directamente por los tickers.
        """
    
        def task(symbol):
            return symbol, self.eod_extract(symbol, freq, start_date, end_date, exchange, fmt, intraday_spot, historical_spot)
    
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            results = list(executor.map(task, symbols))

        combined_df = pd.concat([df for _, df in results], axis=1)
        combined_df.columns = symbols
    
        return combined_df

    def _decode_(self, data):
        """
        Decodifica el contenido recibido en formato CSV y lo convierte en un DataFrame.

        Parámetros:
        -----------
        data : bytes
            Datos en formato binario (CSV codificado en bytes).

        Retorna:
        --------
        pd.DataFrame
            DataFrame con los datos decodificados.
        """
        df = pd.read_csv(StringIO(data.decode('utf-8')))
        return df

    def _today_date_(self):
        """
        Obtiene la fecha de hoy en formato 'YYYY-MM-DD'.

        Retorna:
        --------
        str
            Fecha actual en formato 'YYYY-MM-DD'.
        """
        return date.today().strftime("%Y-%m-%d")

class S3Touch():
    """
    Clase S3Touch para interactuar con Amazon S3. Permite subir archivos o directorios completos a un bucket de S3
    y leer archivos desde S3 en diferentes formatos como JSON, CSV y Numpy (.npy).

    Atributos:
    ----------
    bucket_name : str
        El nombre del bucket de S3 con el cual se desea interactuar.
    
    s3 : boto3.client
        El cliente de boto3 que permite realizar operaciones con S3.

    Métodos:
    --------
    __init__(bucket_name, access_key, secret_access_key, region_name):
        Inicializa la clase con las credenciales y la configuración para interactuar con S3.
    
    _upload_file(file_path, s3_folder=None):
        Sube un archivo único desde el sistema local a un bucket de S3.
    
    _upload_folder(folder_path, s3_folder=None):
        Sube un directorio completo de archivos desde el sistema local a un bucket de S3.
    
    write(path, s3_folder=None):
        Detecta si el path es un archivo o directorio y llama a los métodos correspondientes para subirlos a S3.
    
    read(s3_key, local_path=None):
        Lee un archivo de S3 y lo procesa en base a su extensión (JSON, CSV, Numpy).
    """
    
    def __init__(self, bucket_name, access_key, secret_access_key, region_name):
        """
        Inicializa la clase S3Touch con las credenciales y configuraciones necesarias para interactuar con S3.
        
        Parámetros:
        -----------
        bucket_name : str
            El nombre del bucket de S3 al que se subirán o leerán archivos.
        
        access_key : str
            Clave de acceso (AWS Access Key) para autenticar el cliente S3.
        
        secret_access_key : str
            Clave secreta (AWS Secret Access Key) asociada al acceso S3.
        
        region_name : str
            Región de AWS en la que se encuentra el bucket de S3.
        """
        self.bucket_name = bucket_name
        self.s3 = boto3.client('s3',
                               aws_access_key_id=access_key,
                               aws_secret_access_key=secret_access_key,
                               region_name=region_name)

    def _upload_file(self, file_path, s3_folder=None):
        """
        Sube un archivo único al bucket de S3.

        Parámetros:
        -----------
        file_path : str
            Ruta completa del archivo en el sistema local que se va a subir.
        
        s3_folder : str, opcional
            Carpeta dentro del bucket de S3 donde se guardará el archivo. Si no se especifica, se sube a la raíz del bucket.
        
        Excepciones:
        ------------
        Podría generar excepciones relacionadas con permisos o accesos a S3 si el cliente no tiene acceso adecuado.
        """
        s3_key = f"{s3_folder}/{os.path.basename(file_path)}" if s3_folder else os.path.basename(file_path)
        s3_key = s3_key.lstrip('/')  # Elimina barra inicial si existe
        self.s3.upload_file(file_path, self.bucket_name, s3_key)

    def _upload_folder(self, folder_path, s3_folder=None):
        """
        Sube todos los archivos dentro de un directorio al bucket de S3, manteniendo la estructura de subcarpetas.

        Parámetros:
        -----------
        folder_path : str
            Ruta del directorio en el sistema local que se va a subir.
        
        s3_folder : str, opcional
            Carpeta dentro del bucket de S3 donde se guardará la estructura de archivos. Si no se especifica, se suben a la raíz del bucket.
        
        Excepciones:
        ------------
        Podría generar excepciones si no tiene acceso a S3 o si hay problemas con los permisos.
        """
        if not s3_folder:
            s3_folder = f'{os.path.basename(folder_path)}/'
        else:
            s3_folder = f'{s3_folder}/'
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                relative_path = os.path.relpath(file_path, folder_path)
                s3_key = os.path.join(s3_folder, relative_path).replace("\\", "/")
                self.s3.upload_file(file_path, self.bucket_name, s3_key)
                print (f'{file} succesfully wrote')

    def write(self, path, s3_folder=None):
        """
        Sube un archivo o directorio al bucket de S3. Si la ruta proporcionada es un archivo, lo sube. Si es un directorio, sube todo su contenido.

        Parámetros:
        -----------
        path : str
            Ruta del archivo o directorio que se desea subir.
        
        s3_folder : str, opcional
            Carpeta dentro del bucket de S3 donde se subirá el archivo o directorio. Si no se especifica, se sube a la raíz del bucket.
        
        Excepciones:
        ------------
        ValueError: Si la ruta proporcionada no es ni un archivo ni un directorio.
        """
        if os.path.isfile(path):
            self._upload_file(path, s3_folder)
        elif os.path.isdir(path):
            self._upload_folder(path, s3_folder)
        else:
            raise ValueError("La ruta proporcionada no es válida. Debe ser un archivo o un directorio.")
            
    def read(self, s3_key, local_path=None):
        """
        Lee un archivo desde el bucket de S3 y lo procesa según su tipo de archivo.
    
        Parámetros:
        -----------
        s3_key : str
            Clave (ruta) del archivo dentro del bucket de S3.
        
        local_path : str, opcional
            Ruta local donde se desea descargar el archivo. Si se especifica, el archivo se guardará localmente en lugar de solo procesarlo.
        
        Retorno:
        --------
        El archivo procesado, que puede ser:
        - Un diccionario (para archivos JSON).
        - Un array de Numpy (para archivos .npy).
        - Un DataFrame de pandas (para archivos .csv).
        - Un objeto Python (para archivos .pkl).
        - Un objeto h5py.File (para archivos .h5).
        
        Excepciones:
        ------------
        ValueError: Si el formato del archivo no es soportado.
        """
        try:
            response = self.s3.get_object(Bucket=self.bucket_name, Key=s3_key)
            file_content = response['Body'].read()
    
            if s3_key.endswith('.json'):
                file = json.loads(file_content.decode('utf-8'))
            elif s3_key.endswith('.npy'):
                file = np.load(BytesIO(file_content), allow_pickle=True)
            elif s3_key.endswith('.csv'):
                file = pd.read_csv(StringIO(file_content.decode('utf-8')))
            elif s3_key.endswith('.pkl'):
                file = pickle.loads(file_content)
            elif s3_key.endswith('.h5'):
                # Crear un archivo temporal para poder abrirlo con h5py
                with open('temp_model.h5', 'wb') as f:
                    f.write(file_content)
                file = h5py.File('temp_model.h5', 'r')
            else:
                raise ValueError(f"Formato de archivo no soportado: {s3_key}")
    
            if local_path:
                with open(local_path, 'wb') as f:
                    f.write(file_content)
            
            return file
    
        except Exception as e:
            print(f"Error al procesar el archivo: {e}")
            raise e
    def download_folder (self, s3_folder, local_path):
        """
        Download an entire folder from an S3 bucket to a local directory.
    
        This method downloads all the files located in a specified folder in S3 to a local directory. 
        It checks if the folder path on S3 ends with a '/' and adjusts it if necessary. It then lists all
        objects in the specified S3 folder. If the folder contains any files (not just subdirectories),
        each file is downloaded to the corresponding local path.
    
        Parameters:
        - s3_folder (str): The folder path in the S3 bucket. Must not be an empty string.
        - local_path (str): The local directory path where the files will be downloaded.
    
        Notes:
        - This function assumes that 'self.s3' is an initialized boto3 S3 client and 'self.bucket_name'
          is the name of the S3 bucket.
        - The function creates any necessary local directories if they do not exist.
        - Files are saved in the local directory maintaining their relative path as in S3.
    
        """
        if not s3_folder.endswith('/'):
            s3_folder += '/'
        response = self.s3.list_objects_v2(Bucket=self.bucket_name, Prefix=s3_folder)
        if 'Contents' in response:
            for file in response['Contents']:
                file_name = file['Key']
                if not file_name.endswith('/'):
                    local_file_path = os.path.join(local_path, os.path.relpath(file_name, s3_folder))
                    os.makedirs(os.path.dirname(local_file_path), exist_ok=True)
                    self.s3.download_file(self.bucket_name, file_name, local_file_path)
                    print(f"Downloaded {file_name} to {local_file_path}")

def invoke_lambda_to_stop_instance(access_key, secret_access_key, region_name, instance_id):
    """
    Invoca una función Lambda de AWS para detener una instancia EC2 específica.

    Esta función utiliza las credenciales de AWS y los parámetros proporcionados para invocar 
    una función Lambda que está configurada para detener una instancia EC2. La invocación 
    se realiza de manera asíncrona (InvocationType='Event').

    Parámetros:
    -----------
    access_key : str
        Clave de acceso de AWS (AWS access key) necesaria para autenticarse en los servicios de AWS.
    
    secret_access_key : str
        Clave secreta de AWS (AWS secret access key) asociada al acceso.
    
    region_name : str
        Nombre de la región de AWS en la que se encuentra la función Lambda y la instancia EC2.
    
    instance_id : str
        ID de la instancia EC2 que se desea detener mediante la función Lambda.

    Retorna:
    --------
    response : dict
        Respuesta del cliente de Lambda de AWS, que contiene información sobre el resultado de la invocación.
    """
    lambda_client = boto3.client(
        'lambda',
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_access_key,
        region_name=region_name
    )

    payload = {
        'instance_id': instance_id
    }

    response = lambda_client.invoke(
        FunctionName='stop_instance_after_executed',  # Nombre de la función Lambda que detiene la instancia.
        InvocationType='Event',  # 'Event' significa que la invocación es asíncrona.
        Payload=json.dumps(payload)  # Cargar el ID de la instancia como un JSON.
    )
    print ('lambda invoked')
    return response

