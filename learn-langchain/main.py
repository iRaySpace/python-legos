import streamlit as st
from qa_chain import load_qa_chain

@st.cache_resource
def get_qa_chain():
    return load_qa_chain()


def main():
    st.title("🤖 Kotlin Code Assistant")
    st.markdown("Ask questions about `ExpenseLogService.kt`")

    # Init
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    qa_chain = get_qa_chain()

    query = st.chat_input("🔍 What's your question:")
    if query:
        # User message
        st.session_state.chat_history.append({"role": "user", "content": query})
        with st.chat_message("user"):
            st.markdown(query)

        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                response = qa_chain.invoke(query)
                st.markdown(response.get("result"))

        st.session_state.chat_history.append({"role": "assistant", "content": response})

if __name__ == "__main__":
    main()
