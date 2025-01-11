import streamlit as st
from test import predict, show_image
# from tensorflow.keras.preprocessing import image



#use it at top as it deside page config
st.set_page_config(
    page_title='Analysys app',
    layout='wide',
    initial_sidebar_state='collapsed',
    page_icon='logo.png'
                   )


# Hide Streamlit default header and footer
hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
"""

st.markdown(hide_streamlit_style, unsafe_allow_html=True)


# Streamlit app title
st.title("Select a cat or dog image")
# File uploader
uploaded_file = st.file_uploader("Choose an image", type=["png", "jpg", "jpeg"])
if uploaded_file is not None:
    show_image(uploaded_file, caption=True)    

else:
    st.markdown(
            "<p style='color:red; font-size:20px;'>Please upload only dog or cat image</p>",
            unsafe_allow_html=True
        )

if st.button("Submit"):
    predict(uploaded_file)
    st.balloons()



