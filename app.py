 #jesus
import streamlit as st
import random
import time

# --- CONFIGURACIÓN ---
st.set_page_config(page_title="Trivia TDA", page_icon="🎓", layout="centered")

# --- ESTILO ERGONÓMICO ---
st.markdown("""
<style>

    .stApp {
        background-color: #1e1e1e;
    }

    /* Texto general */
    html, body, [class*="css"]  {
        color: #e0e0e0;
        font-family: 'Segoe UI', sans-serif;
    }

    h1 {
        text-align: center;
        font-weight: 500;
        color: #f0f0f0;
    }

    h3 {
        color: #cccccc;
        font-weight: 400;
    }

    /* Botones suaves */
    div.stButton > button {
        background-color: #2a2a2a;
        color: #e0e0e0;
        border: 1px solid #3a3a3a;
        border-radius: 10px;
        padding: 12px;
        font-size: 16px;
        transition: 0.2s;
    }

    div.stButton > button:hover {
        background-color: #3a3a3a;
        color: #ffffff;
    }

    /* Contenedor centrado */
    .block-container {
        max-width: 750px;
        margin: auto;
        padding-top: 2rem;
    }

</style>
""", unsafe_allow_html=True)

# --- MÚSICA SUAVE DE FONDO ---
st.markdown("""
<audio autoplay loop>
  <source src="https://www.soundhelix.com/examples/mp3/SoundHelix-Song-2.mp3" type="audio/mp3">
</audio>
""", unsafe_allow_html=True)

# --- PREGUNTAS ---
if 'pool_preguntas' not in st.session_state:
    st.session_state.pool_preguntas = [
        {"p": "¿Cuál es la capital de Venezuela?", "o": ["Maracaibo", "Caracas", "Valencia", "Coro"], "c": "Caracas"},
        {"p": "¿Cuántos bits tiene un byte?", "o": ["4", "16", "32", "8"], "c": "8"},
        {"p": "¿Qué planeta es conocido como el Planeta Rojo?", "o": ["Venus", "Marte", "Júpiter", "Saturno"], "c": "Marte"},
        {"p": "¿Qué elemento químico tiene el símbolo 'O'?", "o": ["Oro", "Osmio", "Oxígeno", "Hierro"], "c": "Oxígeno"},
        {"p": "¿Cuál es el lenguaje de programación de esta App?", "o": ["Java", "C++", "Python", "PHP"], "c": "Python"}
    ]
    random.shuffle(st.session_state.pool_preguntas)

# --- ESTADO ---
if 'indice' not in st.session_state:
    st.session_state.indice = 0
    st.session_state.puntos = 0
    st.session_state.juego_terminado = False

# --- INTERFAZ ---
st.title("Trivia Interactiva TDA")
st.divider()

if not st.session_state.juego_terminado:

    pregunta = st.session_state.pool_preguntas[st.session_state.indice]
    st.subheader(f"Pregunta {st.session_state.indice + 1}")
    st.write(f"### {pregunta['p']}")

    opciones = pregunta['o']
    col1, col2 = st.columns(2)

    with col1:
        btn1 = st.button(opciones[0], use_container_width=True)
        btn2 = st.button(opciones[1], use_container_width=True)
    with col2:
        btn3 = st.button(opciones[2], use_container_width=True)
        btn4 = st.button(opciones[3], use_container_width=True)

    seleccion = None
    if btn1: seleccion = opciones[0]
    if btn2: seleccion = opciones[1]
    if btn3: seleccion = opciones[2]
    if btn4: seleccion = opciones[3]

    if seleccion:
        if seleccion == pregunta['c']:
            st.success("Respuesta correcta")
            st.session_state.puntos += 2
        else:
            st.error(f"Incorrecto. Respuesta: {pregunta['c']}")
        
        time.sleep(1)

        if st.session_state.indice < len(st.session_state.pool_preguntas) - 1:
            st.session_state.indice += 1
            st.rerun()
        else:
            st.session_state.juego_terminado = True
            st.rerun()

else:
    st.header("Fin del juego")
    st.metric("Puntuación Final", f"{st.session_state.puntos}")

    if st.button("Reiniciar"):
        st.session_state.indice = 0
        st.session_state.puntos = 0
        st.session_state.juego_terminado = False
        random.shuffle(st.session_state.pool_preguntas)
        st.rerun()
