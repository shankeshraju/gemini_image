from google.generativeai import GenerativeModel, configure
import google.generativeai as genai
import streamlit as st
from PIL import Image
import os


st.set_page_config(page_title='Gemini Testing', layout='wide')
col1, col2 = st.columns(2)


def gemini_text(query):
    model = GenerativeModel('gemini-pro')
    response = model.generate_content(query)
    st.write(response.text)


def gemini_vision(img, query):
    model = GenerativeModel('gemini-pro-vision')
    response = model.generate_content([img, query])
    response.resolve()
    st.write(response.text)


def main():
    with col1:
        key = st.text_input('OpenAI API key')
        genai.configure(api_key = key)
        image_file = st.file_uploader('Upload the image', type=['jpeg', 'png'])
        image_query = ("""You act as a Interior designer and your job is to suggest how can we improve the interior design more attractive""")
        submit_img = st.button('Generate Story')
        if submit_img:
            st.image(image_file)
            img = Image.open(image_file)
            gemini_vision(img, image_query)

    with col2:
        text_query = st.text_area('Enter the query for the text?')
        submit_txt = st.button('Answer my query')
        if submit_txt:
            gemini_text(text_query)


if __name__ == '__main__':
    main()