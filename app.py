 #jesus
import streamlit as st
import random
import time

# --- CONFIGURACIÓN ---
st.set_page_config(page_title="Trivia Cósmica", page_icon="🌌", layout="centered")

# --- ESTILO UNIVERSO SUAVE ---
st.markdown("""
<style>

.stApp {
    background: linear-gradient(to bottom, #0f172a, #1e293b);
    color: #e2e8f0;
    overflow: hidden;
}

/* Capa de estrellas */
.stApp::before {
    content: "";
    position: fixed;
    top: 0;
    left: 0;
    width: 200%;
    height: 200%;
    background-image:
        radial-gradient(2px 2px at 20% 30%, rgba(255,255,255,0.4), transparent),
        radial-gradient(1.5px 1.5px at 70% 80%, rgba(255,255,255,0.3), transparent),
        radial-gradient(1px 1px at 40% 60%, rgba(255,255,255,0.2), transparent),
        radial-gradient(2px 2px at 90% 20%, rgba(255,255,255,0.3), transparent);
    background-repeat: repeat;
    animation: moveStars 120s linear infinite;
    z-index: 0;
}

/* Animación lenta */
@keyframes moveStars {
    from { transform: translate(0, 0); }
    to { transform: translate(-25%, -25%); }
}

/* Contenido por encima */
.block-container {
    position: relative;
    z-index: 1;
    max-width: 750px;
    margin: auto;
    padding-top: 2rem;
}

/* Título */
h1 {
    text-align: center;
    font-weight: 400;
    color: #f1f5f9;
}

/* Botones suaves */
div.stButton > button {
    background-color: #1e293b;
    color: #e2e8f0;
    border: 1px solid #334155;
    border-radius: 12px;
    padding: 12px;
    font-size: 16px;
    transition: 0.3s;
}

div.stButton > button:hover {
    background-color: #334155;
    color: #ffffff;
}

</style>
""", unsafe_allow_html=True)

# --- MÚSICA AMBIENTAL ESPACIAL ---
st.markdown("""
<audio autoplay loop>
  <source src="https://www.soundhelix.com/examples/mp3/SoundHelix-Song-8.mp3" type="audio/mp3">
</audio>
""", unsafe_allow_html=True)

# --- PREGUNTAS ---
if 'pool_preguntas' not in st.session_state:
    st.session_state.pool_preguntas = [
        {"p": "¿Cuál es la capital de Venezuela?", "o": ["Maracaibo", "Caracas", "Valencia", "Coro"], "c": "Caracas"},
        {"p": "¿Qué planeta es conocido como el Planeta Rojo?", "o": ["Venus", "Marte", "Júpiter", "Saturno"], "c": "Marte"},
        {"p": "¿Cuántos bits tiene un byte?", "o": ["4", "16", "32", "8"], "c": "8"},
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
st.title("🌌 Trivia Cósmica TDA")
st.divider()

if not st.session_state.juego_terminado:

    pregunta = st.session_state.pool_preguntas[st.session_state.indice]
    st.subheader(f"Pregunta {st.session_state.indice + 1}")
    st.write(f"### {pregunta['p']}")

    opciones = pregunta['o']
    col1, col2 = st.columns(2)

    with col1:
        b1 = st.button(opciones[0], use_container_width=True)
        b2 = st.button(opciones[1], use_container_width=True)
    with col2:
        b3 = st.button(opciones[2], use_container_width=True)
        b4 = st.button(opciones[3], use_container_width=True)

    seleccion = None
    if b1: seleccion = opciones[0]
    if b2: seleccion = opciones[1]
    if b3: seleccion = opciones[2]
    if b4: seleccion = opciones[3]

    if seleccion:
        if seleccion == pregunta['c']:
            st.success("Respuesta correcta ✨")
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
    st.header("🚀 Misión Finalizada")
    st.metric("Puntuación Final", f"{st.session_state.puntos}")

    if st.button("Reiniciar Misión"):
        st.session_state.indice = 0
        st.session_state.puntos = 0
        st.session_state.juego_terminado = False
        random.shuffle(st.session_state.pool_preguntas)
        st.rerun()
