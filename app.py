import streamlit as st
from dotenv import load_dotenv
from src.rag import load_rag_chain

load_dotenv()


st.set_page_config(page_title="News Research Chatbot", page_icon="📰")
st.title("📰 News Research Chatbot")

# Get URLs from user input
urls = st.text_area(
    "Enter one or more news URLs (comma separated):",
    placeholder="https://www.bbc.com/news, https://www.cnn.com"
)

# Button to load knowledge base
if st.button("Load Knowledge Base"):
    if urls.strip():
        with st.spinner("Loading knowledge base..."):
            try:
                st.session_state.rag_chain = load_rag_chain(urls)
                st.session_state.chat_history = []
                st.success("Knowledge base loaded! You can now chat.")
            except Exception as e:
                st.error(f"Failed to load knowledge base: {e}")
    else:
        st.warning("Please enter at least one URL.")

# Only proceed if RAG chain is loaded
if "rag_chain" in st.session_state:
    rag_chain = st.session_state.rag_chain

    def get_response(user_input):
        response = rag_chain.invoke({"input": user_input})
        return response["answer"] if "answer" in response else str(response)

    st.markdown("Ask me anything about the latest news from the provided URLs!")

    user_input = st.text_input("You:", key="input")
    if st.button("Send") and user_input:
        with st.spinner("Thinking..."):
            answer = get_response(user_input)
            st.session_state.chat_history.append(("You", user_input))
            st.session_state.chat_history.append(("Bot", answer))

    for sender, message in st.session_state.chat_history:
        if sender == "You":
            st.markdown(f"**You:** {message}")
        else:
            st.markdown(f"**Bot:** {message}")
else:
    st.info("Please enter URLs and load the knowledge base to start chatting.")