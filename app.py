#Estudiante Jesus R.

import streamlit as st
import random
import time

# --- CONFIGURACIÓN DE LA PÁGINA ---
st.set_page_config(page_title="Trivia Master IUT", page_icon="💰")
st.markdown("""
<style>
    /* Fondo general */
    .stApp {
        background-color: #f4f4f4;
    }

    /* Título centrado */
    h1 {
        text-align: center;
        color: #222222;
        font-weight: 600;
    }

    /* Pregunta */
    h3 {
        color: #333333;
        font-weight: 500;
    }

    /* Botones minimalistas */
    div.stButton > button {
        background-color: white;
        color: black;
        border: 1px solid #dddddd;
        border-radius: 8px;
        padding: 10px;
        font-size: 16px;
        transition: 0.3s;
    }

    div.stButton > button:hover {
        background-color: #222222;
        color: white;
        border: 1px solid #222222;
    }

    /* Centrar contenido */
    .block-container {
        max-width: 700px;
        margin: auto;
    }
</style>
""", unsafe_allow_html=True)

# --- 1. BASE DE DATOS DE PRUEBA (El "Pool" de 10 preguntas) ---
# Instrucción para el alumno: "Aquí es donde añades tus preguntas de TDA"

if 'pool_preguntas' not in st.session_state:
    st.session_state.pool_preguntas = [
        {"p": "¿Cuál es la capital de Venezuela?", "o": ["Maracaibo", "Caracas", "Valencia", "Coro"], "c": "Caracas"},
        {"p": "¿Qué planeta es conocido como el Planeta Rojo?", "o": ["Venus", "Marte", "Júpiter", "Saturno"], "c": "Marte"},
        {"p": "¿Cuántos bits tiene un byte?", "o": ["4", "16", "32", "8"], "c": "8"},
        {"p": "¿Quién pintó la Mona Lisa?", "o": ["Dali", "Picasso", "Da Vinci", "Van Gogh"], "c": "Da Vinci"},
        {"p": "¿Cuál es el metal más caro del mundo?", "o": ["Oro", "Platino", "Rodio", "Cobre"], "c": "Rodio"},
        {"p": "¿Qué animal es la mascota de Linux?", "o": ["Gato", "Pingüino", "Perro", "Elefante"], "c": "Pingüino"},
        {"p": "¿En qué año llegó el hombre a la Luna?", "o": ["1965", "1972", "1969", "1980"], "c": "1969"},
        {"p": "¿Cuál es el río más largo del mundo?", "o": ["Amazonas", "Nilo", "Orinoco", "Misisipi"], "c": "Amazonas"},
        {"p": "¿Qué elemento químico tiene el símbolo 'O'?", "o": ["Oro", "Osmio", "Oxígeno", "Hierro"], "c": "Oxígeno"},
        {"p": "¿Cuál es el lenguaje de programación de esta App?", "o": ["Java", "C++", "Python", "PHP"], "c": "Python"}
    ]
    # Mezclamos el pool para que no siempre salgan igual
    random.shuffle(st.session_state.pool_preguntas)

# --- 2. GESTIÓN DEL ESTADO DEL JUEGO ---
# Usamos session_state para que la App "recuerde" en qué pregunta vamos

if 'indice' not in st.session_state:
    st.session_state.indice = 0
    st.session_state.puntos = 0
    st.session_state.juego_terminado = False

# --- 3. FUNCIONES DE AUDIO ---
# st.markdown("""
<audio autoplay loop>
  <source src="https://www.youtube.com/watch?v=Zaj44qsZCRc" type="audio/mp3">
</audio>
""", unsafe_allow_html=True)

def reproducir_sonido(url):
    st.markdown(f'<audio src="{url}" autoplay style="display:none"></audio>', unsafe_allow_html=True)

# --- 4. INTERFAZ VISUAL ---

st.title("💰 ¿Quién quiere ser Ingeniero TDA?")
st.divider()

if not st.session_state.juego_terminado:
    # Obtenemos la pregunta actual del pool
    pregunta_actual = st.session_state.pool_preguntas[st.session_state.indice]
    
    st.subheader(f"Pregunta {st.session_state.indice + 1}:")
    st.write(f"### {pregunta_actual['p']}")
    
    # Creamos los botones para las opciones
    opciones = pregunta_actual['o']
    
    # Usamos columnas para que parezca el tablero del programa de TV
    col1, col2 = st.columns(2)
    
    with col1:
        btn_a = st.button(f"A) {opciones[0]}", use_container_width=True)
        btn_b = st.button(f"B) {opciones[1]}", use_container_width=True)
    with col2:
        btn_c = st.button(f"C) {opciones[2]}", use_container_width=True)
        btn_d = st.button(f"D) {opciones[3]}", use_container_width=True)

    # Lógica de respuesta
    seleccion = None
    if btn_a: seleccion = opciones[0]
    if btn_b: seleccion = opciones[1]
    if btn_c: seleccion = opciones[2]
    if btn_d: seleccion = opciones[3]

    if seleccion:
        if seleccion == pregunta_actual['c']:
            st.success("¡CORRECTO! 🌟")
            # reproducir_sonido("URL_DE_SONIDO_CORRECTO")
            st.session_state.puntos += 2
            time.sleep(1)
        else:
            st.error(f"INCORRECTO. La respuesta era: {pregunta_actual['c']} ❌")
            # reproducir_sonido("URL_DE_SONIDO_ERROR")
            time.sleep(1)

        # Avanzamos a la siguiente pregunta
        if st.session_state.indice < 4:
            st.session_state.indice += 1
            st.rerun()
        else:
            st.session_state.juego_terminado = True
            st.rerun()

else:
    # PANTALLA FINAL
    st.header("🏁 ¡Fin del Juego!")
    st.metric("PUNTUACIÓN FINAL", f"{st.session_state.puntos} / 10")
    
    if st.session_state.puntos >= 8:
        st.balloons()
        st.success("¡Eres un experto! Ya puedes trabajar en la cabecera de la TDA.")
    else:
        st.warning("Sigue estudiando, la norma ISDB-Tb te espera.")
    
    if st.button("Reintentar"):
        st.session_state.indice = 0
        st.session_state.puntos = 0
        st.session_state.juego_terminado = False
        random.shuffle(st.session_state.pool_preguntas)
        st.rerun()
