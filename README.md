## **Predicción de la Calidad del Vino Tinto mediante Machine Learning**

### **Descripción del proyecto**

Este proyecto desarrolla un sistema de Machine Learning capaz de predecir la calidad de un vino tinto a partir de sus características fisicoquímicas.

El trabajo incluye un análisis exploratorio completo de los datos (EDA), la construcción de distintos modelos predictivos y la selección del modelo con mejor rendimiento para su posterior despliegue mediante una aplicación interactiva desarrollada con Streamlit.

### **Objetivos:**

Analizar las características del conjunto de datos.

Identificar las variables más influyentes en la calidad del vino.

Realizar un análisis exploratorio de datos (EDA).

Construir y comparar diferentes modelos de Machine Learning.

Seleccionar el modelo con mejor capacidad predictiva.

Desarrollar una aplicación interactiva para realizar predicciones.

### **Dataset**

El conjunto de datos utilizado corresponde al dataset "winequality-red".

Cada registro representa un vino tinto portugués caracterizado mediante variables fisicoquímicas.

*Variables independientes:*
- Acidez fija
- Acidez volátil
- Ácido cítrico
- Azúcar residual
- Cloruros
- Dióxido de azufre libre
- Dióxido de azufre total
- Densidad
- pH
- Sulfatos
- Alcohol

*Variable objetivo:*
- Calidad del vino (quality)

Posteriormente se transformó en una clasificación binaria:

0 → Mala calidad (< 6)

1 → Buena calidad (≥ 6)

### **Análisis Exploratorio de Datos (EDA)**

Durante el análisis exploratorio se realizaron:

*Análisis univariable*
- Estadísticos descriptivos
- Histogramas
- Boxplots
- Distribuciones de frecuencia

*Análisis bivariado*
- Matriz de correlación
- Pairplots
- Relación entre calidad y:
    - Alcohol
    - Acidez volátil
    - Sulfatos
    - Ácido cítrico

**Principales conclusiones:**

- El alcohol presenta una relación positiva con la calidad.
- Los sulfatos muestran una influencia positiva.
- La acidez volátil presenta una relación negativa con la calidad.
- Existen variables con valores atípicos y distribuciones asimétricas.

### **Modelo de Regresión Lineal**

Como primer enfoque se abordó el problema como una tarea de regresión.

Resultados obtenidos:
- MAE: 0.4909
- MAPE: 0.0972
- MSE: 0.4113
- RMSE: 0.6413
- R²: 0.3784

#### **Conclusión**

El modelo únicamente explica aproximadamente el 38% de la variabilidad de la calidad, por lo que se decidió reformular el problema como una tarea de clasificación.

### **Modelos de Clasificación**

Se construyó una variable binaria:

- Buena calidad (quality ≥ 6)

- Mala calidad (quality < 6)

Posteriormente se realizaron:

T- rain/Test Split

- Escalado de variables

- Entrenamiento de modelos

*Modelos evaluados:*

- Logistic Regression
- K-Nearest Neighbors (KNN)
- Decision Tree
- Random Forest
- Support Vector Machine (SVM)

### **Comparación de Modelos**

Comparando la accuracy de los modelos estudiados se selecciona la mejor que es para el modelo ->
Support Vector Machine (SVM)

### **Modelo Final**

El modelo SVM obtuvo el mejor rendimiento global.

Métricas principales:

- Accuracy: 75.37%
- Precision: 76%
- Recall: 75%
- F1-Score: 75%

Interpretación:

El modelo clasifica correctamente aproximadamente tres de cada cuatro vinos.

**Variables más influyentes**

*Variables con impacto positivo:*

- Alcohol
- Sulfatos

*Variables con impacto negativo:*

- Acidez volátil
- Dióxido de azufre total
- Cloruros

Estas variables mostraron una mayor relación con la calidad del vino durante el análisis exploratorio y la construcción de modelos.

### **Optimización del Modelo**

Se realizó una búsqueda de hiperparámetros mediante GridSearchCV.

Mejores parámetros encontrados:

{

    'C': 10,

    'gamma': 0.01,

    'kernel': 'rbf'
}

Accuracy media de validación cruzada:

74.42%

Sin embargo, el rendimiento sobre el conjunto de prueba fue inferior al modelo original, por lo que se mantuvo la versión inicial del SVM como modelo final.

### **Aplicación Streamlit**

El modelo es deplegado mediante una aplicación web desarrollada con Streamlit.

Funcionalidades:

- Introducción de variables fisicoquímicas.
- Predicción automática de calidad.
- Interfaz amigable para el usuario.
- Visualización de resultados en tiempo real.

### **Tecnologías utilizadas**

- Python

- Pandas

- NumPy

- Matplotlib

- Seaborn

- Scikit-Learn

- Joblib

- Streamlit

### **Referencias**

- UCI Machine Learning Repository

- Kaggle

- Scikit-Learn Documentation

- Streamlit Documentation

### **Autor**

Proyecto desarrollado como práctica de Machine Learning aplicada a la predicción de la calidad del vino mediante técnicas de análisis de datos y aprendizaje supervisado.