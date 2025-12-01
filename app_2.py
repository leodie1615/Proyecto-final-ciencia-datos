# ========================================================================
# Archivo: app.py
# Propósito: Prototipo funcional de Producto de Datos usando Streamlit
# ========================================================================

import streamlit as st
import pandas as pd
import joblib
import numpy as np

# ----------------- 1. CONFIGURACIÓN E IMPORTACIÓN DEL MODELO -----------------

CAT_COLS = ['estado', 'oferta', 'fuente']
NUM_COLS = ['cantidad_tareas', 'num_seguimientos', 'duracion_planeada_total_projecto', 'duracion_meses_team']

@st.cache_resource
def load_resources():
    """Carga el modelo y los transformadores necesarios."""
    try:
        model = joblib.load('model/rf.joblib')
        ohe = joblib.load('model/one_hot_encoder.joblib')
        scaler = joblib.load('model/standard_scaler.joblib')
        final_columns = joblib.load('model/final_columns.joblib')
        return model, ohe, scaler, final_columns
    except FileNotFoundError as e:
        st.error(f"Error: No se encontró el archivo de recurso: {e.filename}. Asegúrate de haber guardado 'rf.joblib', 'one_hot_encoder.joblib', 'standard_scaler.joblib', y 'final_columns.joblib'.")
        st.stop()

model, ohe, scaler, FINAL_COLS = load_resources()

# ----------------- 2. INTERFAZ DE USUARIO (UI) -----------------

st.set_page_config(page_title="Prototipo de Producto de Datos", layout="centered")

st.title('Herramienta Predicción')
st.markdown('---')
st.subheader('Ingrese los datos:')

col1, col2 = st.columns(2)

with col1:
    
    estado_options = ['active', 'disabled', 'pending', 'trialing']
    estado_raw = st.selectbox('1. Estado del Proyecto:', 
                          options=estado_options)

    oferta_options = ['budget', 'time', 'freemium']
    oferta_raw = st.selectbox('2. Oferta del Proyecto:', 
                          options=oferta_options) 

    fuente_options = ['bot', 'app', 'import', 'papi']
    fuente_raw = st.selectbox('5. Fuente de Origen:', 
                          options=fuente_options)

    cantidad_tareas = st.slider('3. Cantidad de Tareas:', 
                            min_value=0, max_value=30, value=15)

with col2:

    num_seguimientos = st.number_input('4. Número de Seguimientos/Reuniones:', 
                                   min_value=0, max_value=30, value=5)

    duracion_planeada_total_projecto = st.number_input('6. Duración Planeada Total (en días/semanas):', 
                                                    min_value=1, value=100)

    duracion_meses_team = st.number_input('7. Duración Equipo (en meses):', 
                                       min_value=0, value=100)

st.markdown('---')

# ----------------- 3. FUNCIÓN DE PREDICCIÓN Y PREPROCESAMIENTO -----------------

def preprocess_and_predict(input_values, ml_model, ohe, scaler, final_cols):
    
    # Crear DataFrame crudo
    raw_data = {
        'estado': [input_values['estado']],
        'oferta': [input_values['oferta']],
        'fuente': [input_values['fuente']],
        'cantidad_tareas': [input_values['cantidad_tareas']],
        'num_seguimientos': [input_values['num_seguimientos']],
        'duracion_planeada_total_projecto': [input_values['duracion_planeada_total_projecto']],
        'duracion_meses_team': [input_values['duracion_meses_team']]
    }
    input_df = pd.DataFrame(raw_data)
    
    df_cat = input_df[CAT_COLS]
    df_num = input_df[NUM_COLS]
    
    df_cat_encoded = pd.DataFrame(
        ohe.transform(df_cat),
        columns=ohe.get_feature_names_out(CAT_COLS),
        index=input_df.index
    )
    
    df_num_scaled = pd.DataFrame(
        scaler.transform(df_num),
        columns=NUM_COLS,
        index=input_df.index
    )
    
    df_final = pd.concat([df_num_scaled, df_cat_encoded], axis=1)
    
    for col in final_cols:
        if col not in df_final.columns:
            df_final[col] = 0
            
    final_input_df = df_final[final_cols]
    
    #Predicción
    try:
        prediction = ml_model.predict(final_input_df)
        st.sidebar.write(f"Predicción generada: {prediction[0]}")
        return prediction[0]
    except Exception as e:
        st.error(f"Error en la predicción. Revise las columnas. Error: {e}")
        return None


# ----------------- 4. EJECUCIÓN DEL PROTOTIPO -----------------

if st.button('Obtener Predicción', type="primary"):
    
    input_values = {
        'estado': estado_raw,
        'oferta': oferta_raw,
        'fuente': fuente_raw,
        'cantidad_tareas': cantidad_tareas,
        'num_seguimientos': num_seguimientos,
        'duracion_planeada_total_projecto': duracion_planeada_total_projecto,
        'duracion_meses_team': duracion_meses_team
    }
    
    with st.spinner('Calculando...'):
        prediction_result = preprocess_and_predict(
            input_values, 
            model, 
            ohe, 
            scaler, 
            FINAL_COLS
        )

        