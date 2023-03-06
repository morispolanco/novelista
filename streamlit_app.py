import openai
import streamlit as st
from dotenv import load_dotenv
import os

# Configurar la conexión a OpenAI
load_dotenv('.env')
openai.api_key = os.getenv('OPENAI_API_KEY')

# Título de la aplicación
st.title('Generador de novelas')

# Caja de texto para que el usuario proporcione la descripción de la escena
scene_description = st.text_input('Descripción de la escena')

# Botón para generar el capítulo
if st.button('Generar capítulo'):
    # Parámetros de la generación del capítulo
    prompt = f"Escena: {scene_description}\n\nEscribe un capítulo de novela basado en la descripción de las escenas. Utiliza diálogos y descripciones ricas. Imita el estilo de Arturo Pérez Reverte\n\n"
    model = "text-davinci-003"
    temperature = 0.5
    max_tokens = 3700

    # Generar el capítulo utilizando GPT-3.5-turbo
    response = openai.Completion.create(
        engine=model,
        prompt=prompt,
        temperature=temperature,
        max_tokens=max_tokens
    )

    # Mostrar el capítulo generado al usuario
    st.write(response.choices[0].text)
