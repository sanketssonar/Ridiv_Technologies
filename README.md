# Conversational PDF Chatbot

This is a simple conversational chatbot that extracts text from a PDF file uploaded by the user and allows them to interact with its contents using OpenAI's GPT-3.5 model. The chatbot is built using Streamlit.

## Getting Started

To run this chatbot locally, follow these steps:

1. Install the required dependencies:

```
pip install streamlit pdfplumber openai
```

2. Obtain an API key from OpenAI. You can sign up and get your API key [here](https://openai.com/signup).

3. Replace `"Open_AI_Apikey"` in the code with your OpenAI API key.

4. Run the Streamlit application:

```
streamlit run app.py
```

## Usage

1. Upload a PDF file using the file uploader in the sidebar.

2. Once the PDF file is uploaded, type your message in the text input box labeled "You:".

3. Click the "Send" button to see the chatbot's response.

4. The chat history will be displayed below the input box.

## Notes

- This chatbot uses OpenAI's GPT-3.5 model for generating responses. Please note that this may incur costs depending on your usage.

- The chatbot's performance may vary depending on the content and quality of the PDF file uploaded.

## Creator

This project was created by Sanket Sonar. You can find more of Sanket's work [here](https://github.com/sanketsonar).

