import streamlit as st
import requests, json
# from keys import url

url = st.secrets["bedrock_url"]

# Define the Streamlit app
def main():
    st.set_page_config(
        page_title="Flinstones Portal",
        page_icon="dino.jpg",  # page icon logo
        layout="wide",
    )
    # Display the logo at the top
    st.image("header.png", use_column_width=True)

    # Add a title and description
    st.title("Flinstones Portal")
    st.write("Welcome to the Flinstones 'RAG' Portal. This page allows you to interact with AHEAD's document corpus AND Bedrock LLMs!")


    # input text box for the api key
    api_key_input = st.text_input("Enter your user API key for project flinstone:")

    if api_key_input:

        # Create an input box for text
        user_input = st.text_input("Enter your LLM query here:")


        if user_input:
            query = user_input

            # Define the JSON data you want to send
            data = {
                "body": query
            }

            # Set the headers to indicate that you are sending JSON data
            headers = {
                'Content-Type': 'application/json',
                'x-api-key': api_key_input
            }

            # Send the POST request
            response = requests.post(url, data=json.dumps(data), headers=headers)

            # Handle the response
            if response.status_code == 200:
                st.write("Request was successful!")
                st.write("Response:", response.text)
                #st.json(response.json())  # Display response JSON data
            else:
                st.write("Request failed with status code:", response.status_code)
                st.write("Response:", response.text)
                #st.json(response.json())  # Display response JSON data


if __name__ == "__main__":
    main()
