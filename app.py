#Jesus R
## ELCA :D###
import streamlit as st
import random
import time

# ---------------- CONFIGURACIÓN ----------------
st.set_page_config(
    page_title="Trivia Telecom Orbital",
    page_icon="🌍",
    layout="wide"
)

# ---------------- FONDO Y ESTILO GLOBAL ----------------
st.markdown("""
<style>

/* FONDO UNIVERSO */
.stApp {
    background: radial-gradient(circle at center, #0b1120, #020617);
    overflow: hidden;
}

/* GRID TELECOM ANIMADO */
.stApp::before {
    content: "";
    position: fixed;
    width: 200%;
    height: 200%;
    background-image:
        linear-gradient(rgba(56,189,248,0.05) 1px, transparent 1px),
        linear-gradient(90deg, rgba(56,189,248,0.05) 1px, transparent 1px);
    background-size: 80px 80px;
    animation: moveGrid 80s linear infinite;
    z-index: 0;
}

@keyframes moveGrid {
    from { transform: translate(0,0); }
    to { transform: translate(-80px,-80px); }
}

/* SISTEMA ORBITAL */
.orbit-container {
    position: fixed;
    top: 50%;
    left: 50%;
    width: 300px;
    height: 300px;
    margin-top: -150px;
    margin-left: -150px;
    pointer-events: none;
    z-index: 0;
    opacity: 0.35;
}

.earth {
    position: absolute;
    width: 100px;
    height: 100px;
    background: radial-gradient(circle at 30% 30%, #38bdf8, #0ea5e9 40%, #1e293b 70%);
    border-radius: 50%;
    top: 50%;
    left: 50%;
    margin-top: -50px;
    margin-left: -50px;
    box-shadow: 0 0 20px rgba(56,189,248,0.4);
}

.orbit {
    position: absolute;
    width: 280px;
    height: 280px;
    border: 1px dashed rgba(56,189,248,0.2);
    border-radius: 50%;
    top: 10px;
    left: 10px;
    animation: rotateOrbit 40s linear infinite;
}

.satellite-wrapper {
    position: absolute;
    top: -18px;
    left: 50%;
    transform: translateX(-50%);
}

.satellite {
    font-size: 28px;
    animation: counterRotate 40s linear infinite;
}

@keyframes rotateOrbit {
    from { transform: rotate(0deg); }
    to { transform: rotate(360deg); }
}

@keyframes counterRotate {
    from { transform: rotate(0deg); }
    to { transform: rotate(-360deg); }
}

/* PROTEGER CONTENIDO */
.block-container {
    position: relative;
    z-index: 1;
}

</style>

<div class="orbit-container">
    <div class="earth"></div>
    <div class="orbit">
        <div class="satellite-wrapper">
            <div class="satellite">🛰️</div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# ---------------- ESTADOS ----------------
if "ranking" not in st.session_state:
    st.session_state.ranking = []

if "app_iniciada" not in st.session_state:
    st.session_state.app_iniciada = False

# ---------------- PANTALLA DE CARGA ----------------
if not st.session_state.app_iniciada:
    st.markdown("<h1 style='text-align:center;color:#38bdf8;'>🛰️ Estableciendo Enlace Satelital...</h1>", unsafe_allow_html=True)
    barra = st.progress(0)
    for i in range(101):
        time.sleep(0.02)
        barra.progress(i)
    st.session_state.app_iniciada = True
    st.rerun()

# ---------------- MUSICA ----------------
st.markdown("""
<audio autoplay loop id="bg-music">
  <source src="https://www.soundhelix.com/examples/mp3/SoundHelix-Song-8.mp3" type="audio/mp3">
</audio>
<script>
var audio = document.getElementById("bg-music");
audio.volume = 0.35;
</script>
""", unsafe_allow_html=True)

# ---------------- COLUMNAS ----------------
contenido, ranking_col = st.columns([3,1])

# ---------------- RANKING ----------------
with ranking_col:
    st.markdown("## 🏆 Ranking Orbital")

    if st.session_state.ranking:
        ranking_ordenado = sorted(
            st.session_state.ranking,
            key=lambda x: (-x["aciertos"], x["tiempo"])
        )
        for i, jugador in enumerate(ranking_ordenado, start=1):
            st.markdown(f"""
            <div style="
                background: rgba(15,23,42,0.7);
                padding:12px;
                margin-bottom:10px;
                border-radius:14px;
                border:1px solid rgba(56,189,248,0.3);
            ">
                <b>{i}. {jugador['nombre']}</b><br>
                ⏱️ {jugador['tiempo']:.2f} seg<br>
                📊 {jugador['aciertos']} / {jugador['total']}
            </div>
            """, unsafe_allow_html=True)
    else:
        st.info("Sin registros aún.")

# ---------------- CONTENIDO PRINCIPAL ----------------
with contenido:

    st.title("🌍 Trivia Telecom Orbital")
    st.divider()

    if "nombre_usuario" not in st.session_state:

        nombre = st.text_input("👤 Ingrese su nombre")

        if st.button("🚀 Iniciar Misión"):
            if nombre.strip():
                st.session_state.nombre_usuario = nombre
                st.session_state.inicio_tiempo = time.time()
                st.session_state.indice = 0
                st.session_state.aciertos = 0
                st.session_state.juego_terminado = False

                st.session_state.pool_preguntas = [
                    {"p":"¿Cuál es el estándar oficial adoptado en Venezuela para TDA?",
                     "o":["DVB-T2","ATSC 3.0","ISDB-Tb","DTMB"],
                     "c":"ISDB-Tb"},

                    {"p":"¿Qué técnica de modulación utiliza ISDB-Tb?",
                     "o":["AM-VSB","OFDM segmentado","QAM analógico","FM digital"],
                     "c":"OFDM segmentado"},

                    {"p":"¿Qué ancho de banda ocupa un canal NTSC en Venezuela?",
                     "o":["5 MHz","6 MHz","7 MHz","8 MHz"],
                     "c":"6 MHz"},

                    {"p":"¿Qué códec de video usa la TDA venezolana?",
                     "o":["MPEG-2","H.264/AVC","HEVC","VP9"],
                     "c":"H.264/AVC"},

                    {"p":"¿Qué códec de audio usa ISDB-Tb?",
                     "o":["MP3","Dolby Digital","HE-AAC","PCM"],
                     "c":"HE-AAC"},

                    {"p":"¿Qué permite transmitir varios programas en un mismo canal RF?",
                     "o":["Multiplexación","Intermodulación","AM","Barrido"],
                     "c":"Multiplexación"},

                    {"p":"El efecto 'cliff' en TV digital significa:",
                     "o":["Mejora progresiva","Pérdida abrupta bajo umbral","Más ruido","Cambio frecuencia"],
                     "c":"Pérdida abrupta bajo umbral"},

                    {"p":"¿Qué ventaja móvil ofrece ISDB-Tb?",
                     "o":["FM extra","One-Seg","Más potencia","Sin ruido"],
                     "c":"One-Seg"},

                    {"p":"En NTSC el color se transmite mediante:",
                     "o":["Subportadora de crominancia","OFDM","QPSK","Binaria"],
                     "c":"Subportadora de crominancia"},

                    {"p":"Ventaja espectral de TV digital frente a analógica:",
                     "o":["Más ancho banda","Multiprogramación en 6 MHz","Más interferencia","Sin compresión"],
                     "c":"Multiprogramación en 6 MHz"},
                ]

                random.shuffle(st.session_state.pool_preguntas)
                st.rerun()

    else:

        if not st.session_state.juego_terminado:

            pregunta = st.session_state.pool_preguntas[st.session_state.indice]
            st.subheader(f"Pregunta {st.session_state.indice+1}")
            st.write(f"### {pregunta['p']}")

            col1,col2 = st.columns(2)
            with col1:
                b1 = st.button(pregunta['o'][0], use_container_width=True)
                b2 = st.button(pregunta['o'][1], use_container_width=True)
            with col2:
                b3 = st.button(pregunta['o'][2], use_container_width=True)
                b4 = st.button(pregunta['o'][3], use_container_width=True)

            seleccion = None
            if b1: seleccion = pregunta['o'][0]
            if b2: seleccion = pregunta['o'][1]
            if b3: seleccion = pregunta['o'][2]
            if b4: seleccion = pregunta['o'][3]

            if seleccion:
                if seleccion == pregunta['c']:
                    st.success("✔ Correcto")
                    st.session_state.aciertos += 1
                else:
                    st.error(f"✘ Incorrecto. Respuesta: {pregunta['c']}")

                time.sleep(0.5)

                if st.session_state.indice < len(st.session_state.pool_preguntas)-1:
                    st.session_state.indice += 1
                    st.rerun()
                else:
                    st.session_state.juego_terminado = True
                    st.rerun()

        else:
            tiempo_final = time.time() - st.session_state.inicio_tiempo
            total = len(st.session_state.pool_preguntas)

            if "registrado" not in st.session_state:
                st.session_state.ranking.append({
                    "nombre": st.session_state.nombre_usuario,
                    "tiempo": tiempo_final,
                    "aciertos": st.session_state.aciertos,
                    "total": total
                })
                st.session_state.registrado = True

            st.success("🛰️ Misión completada")
            st.metric("⏱️ Tiempo Total", f"{tiempo_final:.2f} seg")
            st.metric("📊 Resultado Final", f"{st.session_state.aciertos} / {total}")

            if st.button("🔄 Nueva Misión"):
                for key in ["nombre_usuario","registrado"]:
                    if key in st.session_state:
                        del st.session_state[key]
                st.rerun()


          
