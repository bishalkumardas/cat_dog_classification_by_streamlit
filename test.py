import numpy as np
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model
import streamlit as st
from PIL import Image




model=load_model('model(0.9345).h5')

@st.dialog('AI has predicted')
def predict(img_path):
    img = image.load_img(img_path, target_size=(256, 256))  # Resize image to match input size

    # Convert the image to a numpy array and normalize it
    img_array = image.img_to_array(img)
    img_array = img_array / 255.0  # Normalize the image (scale pixel values to [0, 1])

    # Add batch dimension (because the model expects a batch of images)
    img_array = np.expand_dims(img_array, axis=0)

    # Make a prediction
    prediction = model.predict(img_array)

    # Output the prediction result
    if prediction[0] > 0.6:
        show_image(img_path)
        st.markdown(
            "<p style='color:green; font-size:20px;'>It is a Dog 🐶</p>",
            unsafe_allow_html=True
        )
        # st.write("")
        st.audio("audio/dog.wav", format="audio/wav", loop=False)
        
    elif prediction[0] < 0.4:
        show_image(img_path)
        st.markdown(
            "<p style='color:green; font-size:20px;'>It is a Cat 🐱</p>",
            unsafe_allow_html=True
        )
        # st.write("")
        st.audio("audio/cat.wav", format="audio/wav", loop=False)
    
    else:
        st.write('Probably this is nighter dog nor cat')

    # Print the predicted probability
    print("Predicted probability: ", prediction[0])

def show_image(uploaded_file, caption=False):
    upoloded_image= Image.open(uploaded_file)
    if caption==True:
        caption=uploaded_file.name
        st.image(upoloded_image,caption=caption, use_container_width=False, width=400 )
    # elif caption==False:
    else:
        st.image(upoloded_image, use_container_width=False, width=400 )
        