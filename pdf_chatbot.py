import streamlit as st
import pdfplumber
import openai

# Set up OpenAI API
openai.api_key = "Open_AI_Apikey"

# Function to extract text from PDF
def extract_text_from_pdf(pdf_file):
    with pdfplumber.open(pdf_file) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text()
    return text

# Function to generate response using OpenAI API
def generate_response(prompt, text):
    try:
        response = openai.Completion.create(
            engine="gpt-3.5-turbo",  
            prompt=prompt,
            max_tokens=100,
            temperature=0.7,
            stop=["\n"]
        )
        return response.choices[0].text.strip()
    except openai.error.RateLimitError:
        st.error("Rate limit exceeded. Please try again later.")
        return None

# Main function
def main():
    st.title("Conversational PDF Chatbot")

    # File upload
    st.sidebar.header("Upload PDF File")
    pdf_file = st.sidebar.file_uploader("Upload", type=["pdf"])

    if pdf_file is not None:
        st.sidebar.success("PDF file uploaded successfully!")

        # Extract text from PDF
        text = extract_text_from_pdf(pdf_file)

        # Chat interface
        st.subheader("Chat with PDF Contents")
        conversation_history = st.empty()
        user_input = st.text_input("You:", "")

        if st.button("Send"):
            conversation_history.write(f"You: {user_input}")
            response = generate_response(user_input, text)
            if response:
                conversation_history.write(f"Bot: {response}")

if __name__ == "__main__":
    main()
