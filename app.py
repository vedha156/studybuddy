import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load trained model
model = joblib.load('student_scheduler_model.pkl')

# Title
st.title("Student Task Scheduling System")

# User input
st.header("Enter Your Study Details")
time_spent = st.slider("Time Spent Per Topic (minutes)", 20, 120, 60)
quiz_score = st.slider("Recent Quiz Score", 50, 100, 75)
past_performance = st.slider("Past Performance Score", 40, 100, 70)
study_frequency = st.slider("Study Frequency (sessions per week)", 1, 7, 3)
preferred_study_time = st.selectbox("Preferred Study Time", ['morning', 'afternoon', 'evening'])
difficulty_level = st.selectbox("Current Topic Difficulty", ['easy', 'medium', 'hard'])

# Encode categorical inputs
study_time_map = {'morning': 0, 'afternoon': 1, 'evening': 2}
difficulty_map = {'easy': 0, 'medium': 1, 'hard': 2}

preferred_study_time = study_time_map[preferred_study_time]
difficulty_level = difficulty_map[difficulty_level]

# Make prediction
input_data = np.array([[time_spent, quiz_score, past_performance, study_frequency, preferred_study_time, difficulty_level]])
prediction = model.predict(input_data)[0]

# Output prediction
st.subheader("Prediction Result")
if prediction == 1:
    st.warning("⚠️ You might be weak in this area. Allocate more study time!")
else:
    st.success("✅ You are doing well in this area. Keep up the good work!")
