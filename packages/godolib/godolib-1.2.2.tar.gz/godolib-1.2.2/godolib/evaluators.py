import tensorflow as tf

def r2(y_true, y_pred):
    """
    Calcula el coeficiente de determinación R² para un modelo de regresión. Este coeficiente, también conocido como
    R cuadrado, proporciona una medida de cuán bien los resultados observados son replicados por el modelo, basado
    en la proporción de la variación total de los datos explicada por el modelo.

    Parámetros:
    -----------
    y_true : Tensor
        Tensor que contiene los valores verdaderos. Debe ser de la misma forma que y_pred.
    y_pred : Tensor
        Tensor que contiene los valores predichos por el modelo de machine learning.

    Retorna:
    --------
    r2_score : Tensor
        Un tensor escalar que contiene el valor del coeficiente de determinación R². Un valor de R² de 1 indica
        que el modelo explica perfectamente la variabilidad de los datos de respuesta alrededor de su media,
        mientras que un valor de 0 indica que el modelo no explica nada de la variabilidad.

    Descripción de la función:
    --------------------------
    - ss_res : Suma de cuadrados de los residuos. Se calcula como la suma de los cuadrados de las diferencias
      entre los valores reales y los predichos.
    - ss_tot : Suma total de cuadrados. Es la suma de los cuadrados de las diferencias entre los valores reales
      y la media de esos valores.
    - r2_scores : Tensor que contiene el coeficiente R² calculado para cada característica individualmente,
      ajustado para múltiples dimensiones de salida.
    - r2_score : Valor escalar del R², obtenido como la media de los R² de todas las características, lo cual
      proporciona una única métrica representativa del rendimiento del modelo a lo largo de todas las características
      predichas.

    Nota:
    -----
    La función utiliza `tf.keras.backend.epsilon()` para añadir un pequeño número al denominador en el cálculo
    de R² para evitar divisiones por cero y asegurar la estabilidad numérica del cálculo.
    """
    # Calcula la suma de cuadrados de los residuos
    ss_res = tf.reduce_sum(tf.square(y_true - y_pred), axis=0)
    # Calcula la suma total de cuadrados
    ss_tot = tf.reduce_sum(tf.square(y_true - tf.reduce_mean(y_true, axis=0)), axis=0)
    # Calcula R² para cada salida y promedia sobre todas las salidas
    r2_scores = 1 - ss_res / (ss_tot + tf.keras.backend.epsilon())
    r2_score = tf.reduce_mean(r2_scores)
    
    return r2_score