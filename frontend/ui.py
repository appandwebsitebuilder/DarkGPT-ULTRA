import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="DarkGPT Pro 🌍", layout="wide")
st.title("🌍 DarkGPT Pro: Global Innovation Mesh")

languages = ["English", "Hindi", "Spanish", "French", "Bengali"]
selected_lang = st.sidebar.selectbox("🌐 Select Your Language", languages)
st.sidebar.markdown("---")
st.sidebar.info("Built for World Welfare. Not for Profit.")

tab1, tab2 = st.tabs(["💬 Global Assistant", "💡 Innovation Mesh"])

with tab1:
    st.header(f"Ask Anything (in {selected_lang})")
    if "messages" not in st.session_state:
        st.session_state.messages = []

    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    if user_input := st.chat_input("Write your question here..."):
        st.session_state.messages.append({"role": "user", "content": user_input})
        with st.chat_message("user"):
            st.markdown(user_input)

        with st.chat_message("assistant"):
            with st.spinner("Processing globally..."):
                try:
                    res = requests.post(f"{API_URL}/chat", json={"query": user_input, "language": selected_lang})
                    if res.status_code == 200:
                        reply = res.json()["response"]
                        st.markdown(reply)
                        st.session_state.messages.append({"role": "assistant", "content": reply})
                    else:
                        st.error("Error from backend!")
                except:
                    st.error("Is the FastAPI backend running?")

with tab2:
    st.header("🤝 Global Innovation Dashboard")
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Post an Idea")
        i_title = st.text_input("Idea Title")
        i_desc = st.text_area("Describe your innovation")
        i_auth = st.text_input("Your Name / Country")
        if st.button("Submit to Mesh"):
            if i_title and i_desc:
                requests.post(f"{API_URL}/mesh/add", json={"title": i_title, "description": i_desc, "author": i_auth})
                st.success("Idea Published Globally! 🎉")
    
    with col2:
        st.subheader("Find Collaborators")
        search_q = st.text_input("Search technologies or ideas...")
        if st.button("Search Mesh"):
            res = requests.get(f"{API_URL}/mesh/search", params={"query": search_q})
            if res.status_code == 200:
                matches = res.json()["matches"]
                for m in matches:
                    st.info(f"**{m['title']}** by {m['author']}\n\n{m['idea']}")
