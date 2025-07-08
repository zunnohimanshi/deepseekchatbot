import streamlit as st
import requests

# Title and input
st.set_page_config(page_title="Ask Anything", page_icon="🤖")
st.header("DeepSeek-based Q&A Chatbot")

user_input = st.text_input("Type your question below:")

if st.button("Submit"):
    if user_input.strip() == "":
        st.warning("Please enter a question first.")
    else:
        st.info("Fetching response...")

        url = "https://openrouter.ai/api/v1/chat/completions"
        headers = {
            "Authorization": "Bearer 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",
            "HTTP-Referer": "https://deepseek.com",
            "Content-Type": "application/json"
        }
        payload = {
            "model": "openchat/openchat-7b"
            "messages": [{"role": "user", "content": user_input}]
        }

        try:
            response = requests.post(url, headers=headers, json=payload)
            if response.status_code == 200:
                output = response.json()["choices"][0]["message"]["content"]
                st.success("Response:")
                st.write(output)
            else:
                st.error("Something went wrong. Try again later.")
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
            else:
    st.error(f"Error {response.status_code}: {response.text}")

