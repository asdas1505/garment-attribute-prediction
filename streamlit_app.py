import streamlit as st
from PIL import Image
import pandas as pd
from model import GarmentAttribute


API_KEY = "AIzaSyDgv-OYRoCOE4JazlCRFOhJ3qhHXvSyPK8"
model = GarmentAttribute(api_key=API_KEY, model_name="flash")

def main():
    st.title("Garment Attribute Prediction")

    col1, col2 = st.columns(2, gap="large")

    front_uploaded_img = None
    
    # File uploader for multiple images
    uploaded_img = st.file_uploader("Choose front image of product", type=["png", "jpg", "jpeg"])    
    
    if st.button("Submit"):

        img_data = Image.open(uploaded_img)
        
        attributes_pred = model.predict(img_data)
        
        attr_list = [[k, attributes_pred[k]] for k in attributes_pred.keys()]
        
        pred_df = pd.DataFrame(attr_list, columns=["Attribute", "Prediction"])

        with col1:
            st.image(img_data, caption='Uploaded Image')
        
        with col2:
            st.dataframe(
                    pred_df,
                    column_config={
                        "Attribute": "Attribute",
                        "Prediction": "Prediction"
                    },
                hide_index=True,
                height=560
            )
        
if __name__ == '__main__':
    main()
