import streamlit as st
import pandas as pd


# Set the title of the app
st.title("Gender Disparities in HIV Prevalence")

# Input fields for user to enter data
st.write("Please enter the following information:")

# Create a list to store user input data
data = []

# User inputs
num_entries = st.number_input("Enter the number of entries you want to input:", min_value=1, value=1)

for i in range(num_entries):
    st.write(f"Entry {i + 1}:")
    age = st.number_input(f"Age in years (Entry {i + 1}):", min_value=0)
    sex = st.selectbox(f"Sex (Entry {i + 1}):", options=['Male', 'Female'], key=f"sex_{i}")
    hiv_status = st.selectbox(f"HIV Status (Entry {i + 1}):", options=['NEG', 'POS'], key=f"hiv_status_{i}")
    
    data.append({"age in years": age, "sex": sex, "HIV status": hiv_status})

# Create a DataFrame from the input data
df = pd.DataFrame(data)

if not df.empty:
    # Show the first few rows of the dataset
    st.write("Data preview:")
    st.dataframe(df)

    # Encode categorical variables if necessary
    df['sex_encoded'] = df['sex'].apply(lambda x: 0 if x == 'Male' else 1)
    df['hiv_status_encoded'] = df['HIV status'].apply(lambda x: 0 if x == 'NEG' else 1)
    
    # Bar plot: Gender-based HIV prevalence
    st.write("### Gender-based HIV Prevalence")
    gender_hiv = df.groupby(['sex', 'HIV status']).size().unstack()
    st.bar_chart(gender_hiv)

   
