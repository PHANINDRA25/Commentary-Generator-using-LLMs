import numpy as np
import pickle
import pandas as pd
#from flasgger import Swagger
import streamlit as st 

from PIL import Image

#app=Flask(__name__)
#Swagger(app)

pickle_in = open("response1.pkl","rb")
classifier=pickle.load(pickle_in)

#@app.route('/')
def welcome():
    return "Welcome All"

#@app.route('/predict',methods=["Get"])
def predict_note_authentication(bowler, batsman, delivery_outcome, bowler_action, batsman_action, bowler_outcome, batsmen_outcome):
    
    
   
    prediction=classifier.predict([[bowler,batsman,bowler_action,batsman_action]])
    print(prediction)
    return prediction



def main():
    st.title("Bank Authenticator")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Bank Authenticator ML App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    bowler = st.text_input("bowler","Type Here")
    batsman = st.text_input("batsman","Type Here")
    bowler_action = st.text_input("bowler_action","Type Here")
    bowler_outcome = st.text_input("bowler_outcome","Type Here")
    batsman_action = st.text_input("batsman_action","Type Here")
    batsmen_outcome = st.text_input("batsmen_outcome","Type Here")
    delivery_outcome = st.text_input("delivery_outcome","Type Here")
    result=""
    if st.button("Predict"):
        result=predict_note_authentication(over,bowler, batsman, delivery_outcome, bowler_action, batsman_action, bowler_outcome, batsmen_outcome)
    st.success('The output is {}'.format(result))
    if st.button("About"):
        st.text("Lets LEarn")
        st.text("Built with Streamlit")

if __name__=='__main__':
    main()
    
    
    