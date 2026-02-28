 #jesus
import streamlit as st
import random
import time

# --- CONFIGURACIÓN ---
st.set_page_config(
    page_title="Trivia Telecom",
    page_icon="📡",
    layout="centered"
)

# --- ESTILO TELECOM + UNIVERSO ANIMADO ---
st.markdown("""
<style>

.stApp {
    background: radial-gradient(circle at center, #0b1120, #020617);
    overflow: hidden;
}

/* GRID TELECOM EN MOVIMIENTO */
.stApp::before {
    content: "";
    position: fixed;
    width: 200%;
    height: 200%;
    background-image:
        linear-gradient(rgba(56,189,248,0.08) 1px, transparent 1px),
        linear-gradient(90deg, rgba(56,189,248,0.08) 1px, transparent 1px);
    background-size: 60px 60px;
    animation: moveGrid 40s linear infinite;
    z-index: 0;
}

@keyframes moveGrid {
    from { transform: translate(0,0); }
    to { transform: translate(-60px,-60px); }
}

/* NODOS PULSANTES */
.stApp::after {
    content: "";
    position: fixed;
    width: 100%;
    height: 100%;
    background-image:
        radial-gradient(circle at 20% 30%, rgba(56,189,248,0.25) 3px, transparent 4px),
        radial-gradient(circle at 70% 60%, rgba(56,189,248,0.2) 2px, transparent 3px),
        radial-gradient(circle at 40% 80%, rgba(56,189,248,0.2) 2px, transparent 3px),
        radial-gradient(circle at 80% 20%, rgba(56,189,248,0.2) 3px, transparent 4px);
    animation: pulseNodes 6s ease-in-out infinite alternate;
    z-index: 0;
}

@keyframes pulseNodes {
    from { opacity: 0.4; }
    to { opacity: 0.8; }
}

/* CONTENIDO ENCIMA DEL FONDO */
.block-container {
    position: relative;
    z-index: 1;
    max-width: 750px;
    margin: auto;
    padding-top: 2rem;
}

/* TEXTO */
html, body {
    color: #cbd5e1;
    font-family: 'Segoe UI', sans-serif;
}

h1 {
    text-align: center;
    font-weight: 400;
    color: #e2e8f0;
}

/* BOTONES ESTILO TELECOM */
div.stButton > button {
    background-color: rgba(15,23,42,0.85);
    color: #38bdf8;
    border: 1px solid #0ea5e9;
    border-radius: 14px;
    padding: 12px;
    font-size: 16px;
    transition: 0.3s;
}

div.stButton > button:hover {
    background-color: #0ea5e9;
    color: #020617;
}

</style>
""", unsafe_allow_html=True)

# --- MÚSICA AMBIENTAL SUAVE ---
st.markdown("""
<audio autoplay loop>
  <source src="https://www.soundhelix.com/examples/mp3/SoundHelix-Song-8.mp3" type="audio/mp3">
</audio>
""", unsafe_allow_html=True)

# --- BASE DE PREGUNTAS ---
if 'pool_preguntas' not in st.session_state:
    st.session_state.pool_preguntas = [
        {"p": "¿Cuál es la capital de Venezuela?", 
         "o": ["Maracaibo", "Caracas", "Valencia", "Coro"], 
         "c": "Caracas"},

        {"p": "¿Qué planeta es conocido como el Planeta Rojo?", 
         "o": ["Venus", "Marte", "Júpiter", "Saturno"], 
         "c": "Marte"},

        {"p": "¿Cuántos bits tiene un byte?", 
         "o": ["4", "16", "32", "8"], 
         "c": "8"},

        {"p": "¿Qué elemento químico tiene el símbolo 'O'?", 
         "o": ["Oro", "Osmio", "Oxígeno", "Hierro"], 
         "c": "Oxígeno"},

        {"p": "¿Cuál es el lenguaje de programación de esta App?", 
         "o": ["Java", "C++", "Python", "PHP"], 
         "c": "Python"}
    ]
    random.shuffle(st.session_state.pool_preguntas)

# --- ESTADO DEL JUEGO ---
if 'indice' not in st.session_state:
    st.session_state.indice = 0
    st.session_state.puntos = 0
    st.session_state.juego_terminado = False

# --- INTERFAZ PRINCIPAL ---
st.title("📡 Trivia Telecom Interactiva")
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
            st.success("✔ Transmisión Correcta")
            st.session_state.puntos += 2
        else:
            st.error(f"✘ Error de señal. Respuesta: {pregunta['c']}")

        time.sleep(1)

        if st.session_state.indice < len(st.session_state.pool_preguntas) - 1:
            st.session_state.indice += 1
            st.rerun()
        else:
            st.session_state.juego_terminado = True
            st.rerun()

else:
    st.header("🛰️ Sesión Finalizada")
    st.metric("Puntuación Final", f"{st.session_state.puntos}")

    if st.button("🔄 Reiniciar Red"):
        st.session_state.indice = 0
        st.session_state.puntos = 0
        st.session_state.juego_terminado = False
        random.shuffle(st.session_state.pool_preguntas)
        st.rerun()
