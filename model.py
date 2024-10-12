import os
import json
from pathlib import Path

from PIL import Image

import pandas as pd

import google.generativeai as genai

from prompt import PROMPT

ATTRIBUTE_LIST = ["Occasion", "Shape", "Neck", "Pattern", "Length", "Sleeve length", "Knit or woven", "Hemline", "Pattern Type", "Surface Styling", "Sleeve Styling", "Transparency", "Lining", "Closure", "Add ons"]

class GarmentAttribute:
    
    def __init__(self, api_key, model_name="flash") -> None:
        
        self.api_key = api_key
        genai.configure(api_key=api_key)
        
        self.model_name = model_name
        
        model = genai.GenerativeModel(model_name=f"gemini-1.5-flash-001")
        self.model = model
        
        generation_config = {
                            "max_output_tokens": 8192,
                            "temperature": 0.0,
                            "top_p": 0.95
                            }    
        self.generation_config = generation_config
    
    def predict_attribute(self, image_data):
        
        response = self.model.generate_content([image_data, PROMPT],
                                                generation_config=self.generation_config,
                                            )
        refined_response = self.refine_response(response)
        for res_key in refined_response.keys():
            refined_response[res_key] = refined_response[res_key][0] if isinstance(refined_response[res_key], list) else refined_response[res_key] 
        
        return refined_response
    
    def refine_response(self, res):
        
        answer = ""
        for response in res:
            answer = answer + response.text
        
        if 'json' in answer:
            answer = answer.replace('json', '')
        if '`' in answer:
            answer = answer.replace('`', '')
        
        answer = answer.replace(',}','}')
        answer = answer.replace(',\n}','}')
        
        if "null" in answer:
            if "\"null\"" not in answer:            
                answer = answer.replace("null", "\"null\"")
        
        answer = json.loads(answer)
        
        return answer   
    
    
    def predict(self, img):
        
        genai.configure(api_key=self.api_key)
        
        try:
            attribute_pred_temp = self.predict_attribute(img) 
            attribute_pred = {k: attribute_pred_temp[k] for k in ATTRIBUTE_LIST}
            
        except:
            attribute_pred = {k: None for k in ATTRIBUTE_LIST}
        
        return attribute_pred

if __name__ == "__main__":
    
    api_key = "AIzaSyDgv-OYRoCOE4JazlCRFOhJ3qhHXvSyPK8"
    
    model = GarmentAttribute(api_key=api_key)    
    
    path_to_image = "1.jpg"
    
    img = Image.open(path_to_image)
    pred_attribute = model.predict(img)

    print(pred_attribute)