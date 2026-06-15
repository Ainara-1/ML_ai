import streamlit as st
import pandas as pd
import joblib

# ==========================
# CONFIGURACIÓN
# ==========================
st.set_page_config(
    page_title="WineQuality AI",
    page_icon="🍷",
    layout="wide"
)

# ==========================
# CARGAR MODELO
# ==========================
modelo = joblib.load("modelo_svm.pkl")
scaler = joblib.load("scaler.pkl")

# ==========================
# MENÚ LATERAL
# ==========================
pagina = st.sidebar.selectbox(
    "Menú",
    ["Portada", "Inicio", "Predicción", "Información", "Conclusiones"]
)

# =====================================================
# PÁGINA PORTADA
# =====================================================
if pagina == "Portada":

    st.title("Inteligencia Artificial para la Evaluación de la Calidad del Vino")
    st.write("")

    col1, col2, col3 = st.columns([1,3,1])

    with col2:
        st.image(
            "IMAGEN_vinos-tinto.jpg",
            caption="WineQuality AI - Machine Learning aplicado al sector vitivinícola",
            width=700
        )

    

# =====================================================
# PÁGINA INICIO
# =====================================================

elif pagina == "Inicio":

    st.title("🍷 WineQuality AI")

    st.subheader(
        "Inteligencia Artificial para la Evaluación de la Calidad del Vino"
    )

    st.write(
        """
        WineQuality AI es una solución basada en Machine Learning
        capaz de estimar la calidad de un vino a partir de sus
        características fisicoquímicas en cuestión de segundos.

        La plataforma está orientada a:

        • Bodegas

        • Laboratorios enológicos

        • Distribuidores

        • Departamentos de control de calidad

        • Empresas exportadoras
        """
    )

    st.divider()

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            label="Precisión del modelo",
            value="75.36%"
        )

    with col2:
        st.metric(
            label="Variables analizadas",
            value="11"
        )

    with col3:
        st.metric(
            label="Tiempo de predicción",
            value="< 1 s"
        )

    st.divider()

    st.subheader("🎯 Objetivo")

    st.write(
        """
        Ayudar a las empresas del sector vitivinícola
        a obtener una estimación rápida de la calidad
        de un vino mediante técnicas de Inteligencia Artificial.
        """
    )

# =====================================================
# PÁGINA PREDICCIÓN
# =====================================================
elif pagina == "Predicción":

    st.title("🔬 Evaluación Inteligente del Vino")

    st.write(
        """
        Introduzca los parámetros obtenidos en el análisis químico
        para estimar la calidad del vino utilizando el modelo
        WineQuality AI.
        """
    )

    st.divider()

    col1, col2, col3 = st.columns(3)

    # ======================
    # COLUMNA 1
    # ======================
    with col1:

        acidez_fija = st.number_input(
            "Acidez fija",
            min_value=0.0,
            value=7.4
        )

        acidez_volatil = st.number_input(
            "Acidez volátil",
            min_value=0.0,
            value=0.70
        )

        acido_citrico = st.number_input(
            "Ácido cítrico",
            min_value=0.0,
            value=0.00
        )

        azucar_resid = st.number_input(
            "Azúcar residual",
            min_value=0.0,
            value=1.90
        )

    # ======================
    # COLUMNA 2
    # ======================
    with col2:

        cloruros = st.number_input(
            "Cloruros",
            min_value=0.0,
            value=0.076
        )

        dioxido_libre = st.number_input(
            "Dióxido azufre libre",
            min_value=0.0,
            value=11.0
        )

        dioxido_total = st.number_input(
            "Dióxido azufre total",
            min_value=0.0,
            value=34.0
        )

        densidad = st.number_input(
            "Densidad",
            min_value=0.0,
            value=0.9978,
            format="%.4f"
        )

    # ======================
    # COLUMNA 3
    # ======================
    with col3:

        ph = st.number_input(
            "pH",
            min_value=0.0,
            value=3.51
        )

        sulfatos = st.number_input(
            "Sulfatos",
            min_value=0.0,
            value=0.56
        )

        alcohol = st.number_input(
            "Alcohol",
            min_value=0.0,
            value=9.40
        )

    st.write("")

    # ======================
    # BOTÓN CENTRADO
    # ======================
    col_btn1, col_btn2, col_btn3 = st.columns([1, 2, 1])

    with col_btn2:
        predecir = st.button(
            "🍷 Analizar vino",
            use_container_width=True
        )

    # ======================
    # PREDICCIÓN
    # ======================
    if predecir:

        datos = pd.DataFrame([[
            acidez_fija,
            acidez_volatil,
            acido_citrico,
            azucar_resid,
            cloruros,
            dioxido_libre,
            dioxido_total,
            densidad,
            ph,
            sulfatos,
            alcohol
        ]], columns=[
            'acidez_fija',
            'acidez_volatil',
            'acido_citrico',
            'azucar_resid',
            'cloruros',
            'dioxido_azufre_libre',
            'dioxido_azufre_total',
            'densidad',
            'pH',
            'sulfatos',
            'alcohol'
        ])

        datos_scaled = scaler.transform(datos)

        prediccion = modelo.predict(datos_scaled)[0]

        if prediccion == 1:

            st.success(
                "🍷 Clasificación Premium\n\n"
                "El sistema estima que el vino pertenece "
                "al grupo de vinos de buena calidad."
            )

        else:

            st.error(
                "🍷 Clasificación Estándar\n\n"
                "El sistema estima que el vino pertenece "
                "al grupo de vinos de calidad inferior."
            )

# =====================================================
# PÁGINA INFORMACIÓN
# =====================================================
elif pagina == "Información":

    st.title("🏢 Acerca de WineQuality AI")

    st.subheader("Tecnología utilizada")

    st.write("""
    • Python

    • Scikit-Learn

    • Streamlit

    • Support Vector Machine (SVM)

    • Machine Learning Supervisado
    """)

    st.divider()

    st.subheader("📈 Rendimiento del modelo")

    st.write("""
    Modelo seleccionado: SVM

    Accuracy: 75.36%

    Clasificación binaria:

    • 0 → Mala calidad (< 6)

    • 1 → Buena calidad (≥ 6)
    """)

# =====================================================
# PÁGINA CONCLUSION
# =====================================================
elif pagina == "Conclusiones":


    #st.divider()

    st.subheader("🔍 Variables más influyentes")

    st.write("""
    Variables que aumentan la calidad:

    ✅ Alcohol

    ✅ Sulfatos

    Variables que reducen la calidad:

    ❌ Acidez volátil

    ❌ Dióxido de azufre total

    ❌ Cloruros
    """)

    st.divider()

    st.subheader("💼 Casos de uso")

    st.info("""
    .🏭 Bodegas:
    Clasificación automática de lotes.

    🧪 Laboratorios:
    Apoyo al análisis químico tradicional.

    📦 Distribuidores:
    Control rápido de calidad.

    🌍 Exportadores:
    Homogeneización de estándares de calidad.
    """)