#jesus
import streamlit as st
import random
import time

# --- CONFIGURACIÓN DE LA PÁGINA ---
st.set_page_config(page_title="Trivia Master IUT", page_icon="🎓", layout="centered")

# --- ESTILO MINIMALISTA ---
st.markdown("""
<style>
    .stApp {
        background-color: #f4f4f4;
    }

    h1 {
        text-align: center;
        color: #222222;
        font-weight: 600;
    }

    h3 {
        color: #333333;
        font-weight: 500;
    }

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

    .block-container {
        max-width: 700px;
        margin: auto;
    }
</style>
""", unsafe_allow_html=True)

# --- MÚSICA DE FONDO ---
st.markdown("""
<audio autoplay loop>
  <source src="https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3" type="audio/mp3">
</audio>
""", unsafe_allow_html=True)

# --- BASE DE DATOS DE PREGUNTAS ---
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
    random.shuffle(st.session_state.pool_preguntas)

# --- ESTADO DEL JUEGO ---
if 'indice' not in st.session_state:
    st.session_state.indice = 0
    st.session_state.puntos = 0
    st.session_state.juego_terminado = False

# --- FUNCIÓN PARA SONIDOS ---
def reproducir_sonido(url):
    st.markdown(f'<audio src="{url}" autoplay></audio>', unsafe_allow_html=True)

# --- INTERFAZ PRINCIPAL ---
st.title("🎓 Trivia Interactiva TDA")
st.divider()

if not st.session_state.juego_terminado:

    pregunta_actual = st.session_state.pool_preguntas[st.session_state.indice]

    st.subheader(f"Pregunta {st.session_state.indice + 1}")
    st.write(f"### {pregunta_actual['p']}")

    opciones = pregunta_actual['o']

    col1, col2 = st.columns(2)

    with col1:
        btn_a = st.button(f"A) {opciones[0]}", use_container_width=True)
        btn_b = st.button(f"B) {opciones[1]}", use_container_width=True)
    with col2:
        btn_c = st.button(f"C) {opciones[2]}", use_container_width=True)
        btn_d = st.button(f"D) {opciones[3]}", use_container_width=True)

    seleccion = None
    if btn_a: seleccion = opciones[0]
    if btn_b: seleccion = opciones[1]
    if btn_c: seleccion = opciones[2]
    if btn_d: seleccion = opciones[3]

    if seleccion:
        if seleccion == pregunta_actual['c']:
            st.success("✔ Respuesta Correcta")
            st.session_state.puntos += 2
            time.sleep(1)
        else:
            st.error(f"✘ Incorrecto. Respuesta correcta: {pregunta_actual['c']}")
            time.sleep(1)

        if st.session_state.indice < 4:
            st.session_state.indice += 1
            st.rerun()
        else:
            st.session_state.juego_terminado = True
            st.rerun()

else:
    st.header("🏁 Fin del Juego")
    st.metric("Puntuación Final", f"{st.session_state.puntos} / 10")

    if st.session_state.puntos >= 8:
        st.balloons()
        st.success("Excelente desempeño 🎉")
    else:
        st.warning("Puedes intentarlo nuevamente 📚")

    if st.button("Reintentar"):
        st.session_state.indice = 0
        st.session_state.puntos = 0
        st.session_state.juego_terminado = False
        random.shuffle(st.session_state.pool_preguntas)
        st.rerun()
