import psutil
import os

def memory_usage():
    """
    Imprime la cantidad de memoria RAM utilizada por el proceso actual en megabytes (MB).

    Esta función utiliza la biblioteca `psutil` para acceder a la información del sistema, 
    específicamente al uso de memoria del proceso que está ejecutando el código. La memoria 
    utilizada se mide en bytes y se convierte a megabytes para una mejor legibilidad.

    Ejemplo:
        >>> obtener_uso_memoria()
        Uso de memoria: 120.35 MB
    """
    proceso = psutil.Process(os.getpid())
    memoria_en_mb = proceso.memory_info().rss / (1024 * 1024)
    print(f"Used Memory: {memoria_en_mb:.2f} MB")