import random
import os
import pandas as pd
import numpy as np
from .monitors import ModelManager
from tensorflow.keras.callbacks import EarlyStopping

class ModelTuner ():
    """
    A class to tune machine learning models over multiple hyperparameter configurations and trials.

    This class facilitates the process of hyperparameter tuning by testing multiple configurations of 
    hyperparameters on a provided model architecture over a series of trials. Each configuration is evaluated
    with a rolling window over the data, and the results are cleaned and returned as structured data.

    Attributes:
    -----------
    post_transformation_pipeline : object
        A transformation pipeline to be applied after the main transformations.
        
    transformation_pipeline : object
        A transformation pipeline used to preprocess the original data before model training.
        
    transformed_df : pd.DataFrame
        The transformed DataFrame used for training the models.
        
    recovered_df : pd.DataFrame
        The original DataFrame recovered by applying the inverse transformation to `transformed_df`.
        
    building_func : callable
        A function that builds and returns a machine learning model based on hyperparameters.
        
    directory : str
        Directory path where model weights will be stored after training.

    Methods:
    --------
    search(hyperparameters, X, Y, epochs, num_trials, roll_size, callbacks, verbose=0, batch_size=32, data_freq='D', state='transformed'):
        Performs hyperparameter tuning by iterating over different hyperparameter configurations and trials.
        
    _construct_model_(hps_configuration, X, Y, epochs, batch_size, callbacks, verbose, weights_path=False):
        Builds and trains a model based on a hyperparameter configuration and optionally loads pre-trained weights.
        
    _is_iterable_(obj):
        Helper method to check if the provided object is iterable.
        
    _clean_evaluation_(evaluation):
        Cleans and structures the model evaluation results into a dictionary of dataframes where each key is 
        a metric and each dataframe contains trial results for that metric.
    """
    def __init__ (self, post_transformation_pipeline, transformation_pipeline, transformed_df, building_func, directory):
        """
        Initializes the ModelTuner object with transformation pipelines, data, and model-building function.
        
        Parameters:
        -----------
        post_transformation_pipeline : object
            The pipeline that will be applied to the data after the model predictions.
        
        transformation_pipeline : object
            The pipeline used to transform the input data before training.
        
        transformed_df : pd.DataFrame
            The DataFrame containing the transformed data.
        
        building_func : callable
            A function that takes a hyperparameters object and returns a model.
        
        directory : str
            Path where model weights and logs will be stored.
        """
        self.post_transformation_pipeline=post_transformation_pipeline
        self.transformation_pipeline=transformation_pipeline
        self.transformed_df=transformed_df
        self.recovered_df=transformation_pipeline.inverse_transform(transformed_df)
        self.building_func=building_func
        self.directory=directory
    def search (self, hyperparameters, X, Y, validation_data, epochs, num_trials, roll_size, callbacks, verbose=0, batch_size=32, data_freq='D', state='transformed'):
        """
        Searches over a set of hyperparameter configurations and evaluates models across multiple trials.
        
        Parameters:
        -----------
        hyperparameters : iterable
            A collection of hyperparameter configurations to be tested.
            
        X : np.array or pd.DataFrame
            Input features for training the model.
            
        Y : np.array or pd.DataFrame
            Target values for training the model.

        validation_vata : tuple
            Validation_data
            
        epochs : int
            Number of epochs to train each model.
            
        num_trials : int
            Number of trials for each hyperparameter configuration.
            
        roll_size : int
            Size of the rolling window to use when evaluating model performance.
            
        callbacks : list
            List of callback functions to be used during model training.
            
        verbose : int, optional (default=0)
            Verbosity mode for model training.
            
        batch_size : int, optional (default=32)
            Batch size to use during model training.
            
        data_freq : str, optional (default='D')
            Frequency of the data used for the model.
            
        state : str, optional (default='transformed')
            Indicates whether the state of the data is 'transformed' or 'raw'.
            
        Returns:
        --------
        dict
            A dictionary containing the cleaned evaluation metrics for each hyperparameter configuration and trial.
        """
        if not isinstance(hyperparameters, list):
            raise ValueError(f'hyperparameters parameter must be a list')
        if not all (isinstance(element, dict) for element in hyperparameters):
            raise ValueError(f'hyperparametrs parameter must contain only dictionaries')
        evaluations = {}
        os.makedirs(self.directory, exist_ok=True)
        for hps_idx, hps_configuration in enumerate(hyperparameters):
            print (f'searching configuration: {hps_idx}')
            model_evaluations = {}
            for trial in range (num_trials):
                print (f'trial: {trial}')
                current_callbacks = []
                for callback in callbacks:
                    if isinstance(callback, EarlyStopping):
                        # Crear una nueva instancia de EarlyStopping para este trial
                        new_early_stopping = EarlyStopping(monitor=callback.monitor,
                                                           patience=callback.patience,
                                                           mode=callback.mode,
                                                           restore_best_weights=callback.restore_best_weights)
                        current_callbacks.append(new_early_stopping)
                    else:
                        current_callbacks.append(callback)
                trial_weights_path = f'{self.directory}/{hps_idx}_{trial}.weights.h5'
                if os.path.exists(trial_weights_path):
                    model = self._construct_model_(hps_configuration=hps_configuration,
                                                   X=X,
                                                   Y=Y,
                                                   validation_data=validation_data,
                                                   epochs=epochs,
                                                   batch_size=batch_size,
                                                   callbacks=current_callbacks,
                                                   verbose=verbose,
                                                   weights_path=trial_weights_path
                                                   )
                else:
                    model = self._construct_model_(hps_configuration=hps_configuration,
                                                   X=X,
                                                   Y=Y,
                                                   validation_data=validation_data,
                                                   epochs=epochs,
                                                   batch_size=batch_size,
                                                   callbacks=current_callbacks,
                                                   verbose=verbose
                                                   )
                    model.save_weights(filepath=trial_weights_path)
                manager = ModelManager(post_transformation_pipeline=self.post_transformation_pipeline,
                                       transformation_pipeline=self.transformation_pipeline,
                                       transformed_df=self.transformed_df, model=model)
                evaluation = manager.evaluate(roll_size=roll_size, state=state).iloc[:-1, :]
                model_evaluations[trial] = evaluation
            evaluations[hps_idx] = model_evaluations
        cleaned_evaluations = self._clean_evaluation_(evaluation=evaluations)
        return cleaned_evaluations
    def _construct_model_(self, hps_configuration, X, Y, validation_data, epochs, batch_size, callbacks, verbose, weights_path=False):
        """
        Constructs and trains a model based on the provided hyperparameter configuration.
        
        Parameters:
        -----------
        hps_configuration : dict
            Hyperparameter configuration for the model.
            
        X : np.array or pd.DataFrame
            Input features for training.
            
        Y : np.array or pd.DataFrame
            Target values for training.
            
        validation_vata : tuple
            Validation_data
            
        epochs : int
            Number of epochs to train the model.
            
        batch_size : int
            Batch size to use during training.
            
        callbacks : list
            List of callback functions to be used during training.
            
        verbose : int
            Verbosity mode for model training.
            
        weights_path : str, optional (default=False)
            Path to pre-trained weights. If provided, the model will load these weights before training.
            
        Returns:
        --------
        model
            The constructed and trained machine learning model.
        """
        hp_object = HyperparametersSelector(hps_configuration = hps_configuration)
        model = self.building_func(hp_object)
        if weights_path:
            model.load_weights(filepath=weights_path)
            return model
        model.fit(x=X, y=Y, validation_data=validation_data, epochs=epochs, batch_size=batch_size, callbacks=callbacks, verbose=verbose)
        return model
    def _clean_evaluation_ (self, evaluation):
        """
        Cleans and organizes evaluation results into a structured format.
        
        Parameters:
        -----------
        evaluation : dict
            The raw evaluation data, where keys are hyperparameter configurations and values are dictionaries
            of trial results.
            
        Returns:
        --------
        dict
            A dictionary of DataFrames where each key is a metric and each DataFrame contains results for 
            that metric across different hyperparameter configurations and trials.
        """
        metrics_dict = {}
        for hps_config, trials in evaluation.items():
            for trial, df in trials.items():
                for metric in df.columns:
                    if metric not in metrics_dict:
                        metrics_dict[metric] = pd.DataFrame(columns=['Hps_config', 'trial'] + df.index.tolist())
                    new_row = pd.Series([hps_config, trial] + df[metric].tolist(), index=metrics_dict[metric].columns)
                    metrics_dict[metric] = pd.concat([metrics_dict[metric], new_row.to_frame().T], ignore_index=True)
        return metrics_dict


class HyperparametersSelector:
    """
    A class for selecting hyperparameters based on given configurations.

    Attributes:
        hps (dict): A dictionary to store hyperparameter names and their selected values.

    Methods:
        Int(name, min_value, max_value, step): Returns an integer hyperparameter.
        Float(name, min_value, max_value, step): Returns a floating-point hyperparameter.
        Choice(name, values): Returns a choice from given possible values.
        _get_values_(): Returns the dictionary of all hyperparameter values.
    """

    def __init__(self, hps_configuration=None):
        """
        Initializes the HyperparametersSelection with an optional hyperparameters configuration.

        Args:
            hps_configuration (dict, optional): A pre-defined dictionary of hyperparameters. Defaults to None.
        """
        self.hps = {} if hps_configuration is None else hps_configuration

    def Int(self, name, min_value, max_value, step):
        """
        Generates or retrieves an integer hyperparameter within the specified range, using the specified step.

        Args:
            name (str): The name of the hyperparameter.
            min_value (int): The minimum value of the range.
            max_value (int): The maximum value of the range.
            step (int): The step between possible values within the range.

        Returns:
            int: The chosen or retrieved integer value for the hyperparameter.

        Raises:
            ValueError: If min_value is greater than max_value or if step is not positive.
        """
        if name in self.hps:
            return self.hps[name]
        if min_value > max_value:
            raise ValueError("min_val must be less than or equal to max_val")
        if step <= 0:
            raise ValueError("step must be a positive number")
        number = random.choice(range(min_value, max_value + 1, step))
        self.hps[name] = number
        return number

    def Float(self, name, min_value, max_value, step):
        """
        Generates or retrieves a floating-point hyperparameter within the specified range, using the specified step.

        Args:
            name (str): The name of the hyperparameter.
            min_value (float): The minimum value of the range.
            max_value (float): The maximum value of the range.
            step (float): The step between possible values within the range.

        Returns:
            float: The chosen or retrieved floating-point value for the hyperparameter.

        Raises:
            ValueError: If min_value is greater than max_value or if step is not positive.
        """
        if name in self.hps:
            return self.hps[name]
        if min_value > max_value:
            raise ValueError("min_val must be less than or equal to max_val")
        if step <= 0:
            raise ValueError("step must be a positive number")
        number = random.choice([min_value + i * step for i in range(int((max_value - min_value) / step) + 1)])
        self.hps[name] = number
        return number

    def Choice(self, name, values):
        """
        Chooses or retrieves a value from a list of possible values for a hyperparameter.

        Args:
            name (str): The name of the hyperparameter.
            values (list): A list of possible values from which to choose.

        Returns:
            Any: The chosen or retrieved value from the list.

        Raises:
            ValueError: If the list of possible values is empty.
        """
        if name in self.hps:
            return self.hps[name]
        if isinstance(values, list):
            if not values:
                raise ValueError("list cannot be empty")
        elif isinstance(values, np.ndarray):
            if values.size == 0:
                raise ValueError("array cannot be empty")
        election = random.choice(values)
        self.hps[name] = election
        return election

    def _get_values_(self):
        """
        Retrieves the dictionary containing all hyperparameter names and their selected values.

        Returns:
            dict: The dictionary of hyperparameter names and values.
        """
        return self.hps


class RandomSearch():
    """
    Clase RandomSearch para realizar una búsqueda aleatoria de hiperparámetros para un modelo de aprendizaje profundo.

    Atributos:
    ----------
    buildin_func : function
        Función que recibe un objeto de hiperparámetros y devuelve un modelo configurado.
    objective : str
        Métrica de validación que se utilizará para optimizar los hiperparámetros. Debe ser una de las siguientes: 
        ['val_loss', 'val_mae', 'val_mse', 'val_mape', 'val_r2'].
    max_trials : int
        Número máximo de configuraciones de hiperparámetros a probar.
    executions_per_trial : int
        Número de veces que se ejecutará el entrenamiento para cada configuración de hiperparámetros.
    results : dict
        Diccionario que almacena los resultados de las configuraciones probadas. Las keys son los números de los trials, 
        y los valores son una tupla con la configuración de hiperparámetros y el valor promedio de la métrica objetivo.

    Métodos:
    --------
    __init__(self, buildin_func, objective, max_trials, executions_per_trial):
        Inicializa la clase RandomSearch con la función de construcción de modelos, el objetivo a optimizar, 
        el número máximo de configuraciones (trials) y las ejecuciones por trial.

    search(self, X, Y, epochs, batch_size, validation_data, callbacks, verbose=1):
        Ejecuta la búsqueda de hiperparámetros. Entrena varios modelos con configuraciones de hiperparámetros aleatorios y
        selecciona el mejor basado en la métrica objetivo.
        
        Parámetros:
        -----------
        X : array-like
            Datos de entrada para el entrenamiento.
        Y : array-like
            Etiquetas o valores objetivo para el entrenamiento.
        epochs : int
            Número de épocas para entrenar cada modelo.
        batch_size : int
            Tamaño del lote utilizado durante el entrenamiento.
        validation_data : tuple
            Datos de validación en forma de (X_val, Y_val) para calcular la métrica objetivo.
        callbacks : list
            Lista de callbacks a utilizar durante el entrenamiento.
        verbose : int, opcional
            Nivel de verbosidad (1 por defecto). Determina qué tan detallada será la salida impresa.

    _generator_(self):
        Genera una nueva configuración de hiperparámetros utilizando la función de construcción y un objeto de selección de hiperparámetros.
        
        Retorna:
        --------
        hps_configuration : dict
            Diccionario que contiene los valores de la configuración de hiperparámetros generados.
        hps_object : object
            Objeto que contiene la información de los hiperparámetros seleccionados.
    """

    def __init__(self, building_func, objective, max_trials, executions_per_trial):
        self.building_func = building_func
        valid_objectives = ['val_loss', 'val_mae', 'val_mse', 'val_mape', 'val_r2']
        if objective not in valid_objectives:
            raise ValueError(f"'{objective}' is not a valid mode. Choose from {valid_objectives}.")
        self.objective = objective
        self.max_trials = max_trials
        self.executions_per_trial = executions_per_trial

    def search(self, X, Y, epochs, batch_size, validation_data, callbacks, verbose=1):
        """
        Realiza la búsqueda de hiperparámetros probando varias configuraciones de modelos.

        Parámetros:
        -----------
        X : array-like
            Conjunto de datos de entrada para el entrenamiento del modelo.
        Y : array-like
            Conjunto de etiquetas o valores objetivo para el entrenamiento.
        epochs : int
            Número de épocas para entrenar cada modelo.
        batch_size : int
            Tamaño del batch utilizado durante el entrenamiento.
        validation_data : tuple
            Conjunto de datos de validación en la forma (X_val, Y_val).
        callbacks : list
            Lista de callbacks a utilizar durante el entrenamiento.
        verbose : int, opcional
            Nivel de verbosidad del proceso de entrenamiento, por defecto es 1.

        Retorna:
        --------
        None
        """
        print('Searching: \n')
        results = {}
        for trial in range(self.max_trials):
            print(f'Searching model: {trial}')
            trial_results = []
            current_hps_configuration, current_hp_object = self._generator_()
            for model_trial in range(self.executions_per_trial):
                print(f'model trial: {model_trial}')
                model = self.building_func(current_hp_object)
                current_callbacks = []
                for callback in callbacks:
                    if isinstance(callback, EarlyStopping):
                        # Crear una nueva instancia de EarlyStopping para este trial
                        new_early_stopping = EarlyStopping(monitor=callback.monitor,
                                                           patience=callback.patience,
                                                           mode=callback.mode,
                                                           restore_best_weights=callback.restore_best_weights)
                        current_callbacks.append(new_early_stopping)
                    else:
                        current_callbacks.append(callback)
                history = model.fit(x=X, y=Y, batch_size=batch_size, epochs=epochs, verbose=verbose, 
                                    callbacks=current_callbacks, validation_data=validation_data)

                # Seleccionar la métrica según el objetivo
                if self.objective == 'val_loss':
                    score = history.history['val_loss'][-1]
                    self.reverse = False
                elif self.objective == 'val_mae':
                    score = history.history['val_mae'][-1]
                    self.reverse = False
                elif self.objective == 'val_mse':
                    score = history.history['val_mse'][-1]
                    self.reverse = False
                elif self.objective == 'val_mape':
                    score = history.history['val_mape'][-1]
                    self.reverse = False
                elif self.objective == 'val_r2':
                    score = history.history['val_r2'][-1]
                    self.reverse = True

                trial_results.append(score)

            results[trial] = (current_hps_configuration, sum(trial_results) / len(trial_results))

        # Ordenar los resultados según la métrica objetivo
        results = {k: v for k, v in sorted(results.items(), key=lambda item: item[1][1], reverse=self.reverse)}
        results = {i: v for i, v in enumerate(results.values())}
        return results
    def _generator_(self):
        """
        Genera una nueva configuración de hiperparámetros aleatoria.

        Retorna:
        --------
        hps_configuration : dict
            Configuración generada de los hiperparámetros.
        hps_object : object
            Objeto que contiene los hiperparámetros seleccionados.
        """
        hps_object = HyperparametersSelector()
        _ = self.building_func(hps_object)
        hps_configuration = hps_object._get_values_()
        return hps_configuration, hps_object