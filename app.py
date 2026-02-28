import streamlit as st
import random
import time

# ---------------- CONFIGURACIÓN ----------------
st.set_page_config(
    page_title="Trivia Telecom Orbital",
    page_icon="🌍",
    layout="wide"
)

# ---------------- ESTADOS INICIALES ----------------
if "ranking" not in st.session_state:
    st.session_state.ranking = []

if "nombre_usuario" not in st.session_state:
    st.session_state.nombre_usuario = None

if "inicio_tiempo" not in st.session_state:
    st.session_state.inicio_tiempo = None

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

# ---------------- DISEÑO EN COLUMNAS ----------------
contenido, ranking_col = st.columns([3, 1])

# ---------------- PANEL RANKING ----------------
with ranking_col:
    st.markdown("## 🏆 Ranking Orbital")

    if st.session_state.ranking:

        # Ordenar por más aciertos y menor tiempo
        ranking_ordenado = sorted(
            st.session_state.ranking,
            key=lambda x: (-x["aciertos"], x["tiempo"])
        )

        for i, jugador in enumerate(ranking_ordenado, start=1):
            st.markdown(
                f"""
                <div style="
                    background: rgba(15,23,42,0.65);
                    padding:12px;
                    margin-bottom:10px;
                    border-radius:14px;
                    border:1px solid rgba(56,189,248,0.3);
                ">
                    <b>{i}. {jugador['nombre']}</b><br>
                    ⏱️ {jugador['tiempo']:.2f} seg<br>
                    📊 {jugador['aciertos']} / {jugador['total']}
                </div>
                """,
                unsafe_allow_html=True
            )
    else:
        st.info("Sin registros aún.")

# ---------------- CONTENIDO PRINCIPAL ----------------
with contenido:

    st.title("🌍 Trivia Telecom Orbital")
    st.divider()

    # Pedir nombre
    if not st.session_state.nombre_usuario:

        nombre = st.text_input("👤 Ingrese su nombre para iniciar misión")

        if st.button("🚀 Iniciar Misión"):
            if nombre.strip():
                st.session_state.nombre_usuario = nombre
                st.session_state.inicio_tiempo = time.time()
                st.session_state.indice = 0
                st.session_state.juego_terminado = False
                st.session_state.aciertos = 0  # 👈 contador

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
                     "c": "Python"},
                ]

                random.shuffle(st.session_state.pool_preguntas)
                st.rerun()

    else:

        if not st.session_state.get("juego_terminado", False):

            pregunta = st.session_state.pool_preguntas[st.session_state.indice]

            st.subheader(f"Pregunta {st.session_state.indice + 1}")
            st.write(f"### {pregunta['p']}")

            col1, col2 = st.columns(2)

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
                    st.success("✔ Transmisión Correcta")
                    st.session_state.aciertos += 1  # 👈 suma correcta
                else:
                    st.error(f"✘ Error. Respuesta: {pregunta['c']}")

                time.sleep(0.5)

                if st.session_state.indice < len(st.session_state.pool_preguntas) - 1:
                    st.session_state.indice += 1
                    st.rerun()
                else:
                    st.session_state.juego_terminado = True
                    st.rerun()

        else:

            tiempo_final = time.time() - st.session_state.inicio_tiempo
            total_preguntas = len(st.session_state.pool_preguntas)

            # Guardar en ranking una sola vez
            if "registrado" not in st.session_state:
                st.session_state.ranking.append({
                    "nombre": st.session_state.nombre_usuario,
                    "tiempo": tiempo_final,
                    "aciertos": st.session_state.aciertos,
                    "total": total_preguntas
                })
                st.session_state.registrado = True

            st.success("🛰️ Misión completada")
            st.metric("⏱️ Tiempo Total", f"{tiempo_final:.2f} seg")
            st.metric("📊 Resultado", f"{st.session_state.aciertos} / {total_preguntas}")

            if st.button("🔄 Nueva Misión"):
                for key in ["nombre_usuario", "registrado"]:
                    if key in st.session_state:
                        del st.session_state[key]
                st.rerun()
