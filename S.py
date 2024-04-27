import streamlit as st
import openai
import os
import json

# Initialize OpenAI with the API key
openai.api_key = ''

def generate_commentary(bowler, batsman, delivery_outcome, bowler_action, batsman_action, bowler_outcome, batsmen_outcome):
    prompt = f"In a critical phase of the game, {bowler} bowls to {batsman}. The delivery is a {bowler_action} and {batsman_action}. The outcome is {delivery_outcome}. {bowler} achieves {bowler_outcome} while {batsman} responds with {batsmen_outcome}. Describe the ball in a crisp way as a real commentator."
    
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a cricket commentator providing live commentary for a match. Don't greet for each and every ball. Keep it simple, don't be too long. Generated sentence structing should not be the same for all. Keep it crisp. Don't start the same way for each ball"},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"An error occurred: {str(e)}"

# Streamlit UI
st.title("Cricket Commentary Generator")

bowler = st.text_input("Bowler's name:")
batsman = st.text_input("Batsman's name:")
bowler_action = st.text_input("Bowler's action:")
bowler_outcome = st.text_input("Bowler's outcome:")
batsman_action = st.text_input("Batsman's action:")
batsmen_outcome = st.text_input("Batsman's outcome:")
delivery_outcome = st.text_input("Delivery outcome:")

if st.button("Generate Commentary"):
    commentary = generate_commentary(bowler, batsman, delivery_outcome, bowler_action, batsman_action, bowler_outcome, batsmen_outcome)
    st.write(commentary)
