"""App Streamlit: Chat Espejo

El usuario escribe y el chat responde exactamente lo mismo (efecto espejo).
"""

import streamlit as st
from utils.chat import send_message, save_label
from dotenv import load_dotenv

load_dotenv()  # Cargar variables de entorno desde .env


st.set_page_config(page_title="Chat Espejo", page_icon="🪞")
st.title("Chat Espejo — Chat simplificado")
st.write("Este chat responde exactamente con el mismo texto que envías (espejo).")


DEFAULT_PROMPT = "Escribe tu mensaje..."

if "messages" not in st.session_state:
    # Cada elemento: {'role': 'user'|'assistant', 'content': str}
    st.session_state.messages = []

# Mostrar historial al recargar
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# Input del usuario usando st.chat_input (estilo del ejemplo)
prompt = st.chat_input(DEFAULT_PROMPT)
if prompt:
    # Añadir mensaje del usuario inmediatamente
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Obtener respuesta (espejo)
    assistant_text = send_message(prompt)

    # Guardar etiqueta
    save_label(prompt, assistant_text)

    # Stream simulando salida incremental
    with st.chat_message("assistant"):
        placeholder = st.empty()
        text_so_far = ""
        try:
            for token in str(assistant_text).split():
                text_so_far += token + " "
                placeholder.markdown(text_so_far)
        except Exception:
            # Fallback: mostrar todo
            placeholder.markdown(assistant_text)

    # Guardar respuesta en el historial
    st.session_state.messages.append({"role": "assistant", "content": assistant_text})


st.markdown("---")
st.caption("Chat espejo: no se hace ninguna llamada externa, la respuesta es exactamente lo enviado.")
