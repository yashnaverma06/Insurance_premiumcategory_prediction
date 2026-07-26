import streamlit as st
import requests

#page configuration

st.set_page_config(
    page_title = 'Insurance Premium Predictor',
    layout = 'centered'
)

st.title('Insurance Premium Predictor')

st.write(
    "Enter your details below to predict your insurance premium category"
)

st.divider()
#user input
age = st.number_input("Age", min_value=0)

weight = st.number_input("Weight (kg)", min_value=0.0)

height = st.number_input("Height (cm)", min_value=0.0)

income_lpa = st.number_input("Annual Income (LPA)", min_value=0.0)

smoker = st.selectbox(
    "Smoker",
    ["No", "Yes"]
)

city = st.selectbox(
    "City",
    ['Agra', 'Allahabad', 'Srinagar', 'Meerut', 'Varanasi', 'Hyderabad',
       'Ahmedabad', 'Chennai', 'Amritsar', 'Vadodara', 'Lucknow',
       'Bhopal', 'Mumbai', 'Ludhiana', 'Rajkot', 'Surat', 'Ghaziabad',
       'Ranchi', 'Pune', 'Kanpur', 'Nagpur', 'Faridabad', 'Bangalore',
       'Jaipur', 'Kolkata', 'Nashik', 'Patna', 'Indore', 'Delhi',
       'Visakhapatnam'
    ]
)

occupation = st.selectbox(
    "Occupation",
    [
        'Factory Worker', 'Businessman', 'Sales Manager', 'Banker',
       'Marketing Manager', 'Insurance Agent', 'HR Manager', 'Pharmacist',
       'Teacher', 'Software Engineer', 'Consultant', 'Driver',
       'Shop Owner', 'Nurse', 'Accountant', 'Government Employee',
       'Architect', 'Engineer', 'Real Estate Agent', 'Civil Servant',
       'Plumber', 'Retail Manager', 'Chef', 'Electrician', 'Carpenter',
       'Doctor', 'Lab Technician', 'Data Analyst', 'Lawyer',
       'Content Writer'
    ]
)

#predict button

if st.button("Predict Premium"):
    data = {
        "age": age,
        "weight": weight,
        "height": height,
        "income_lpa": income_lpa,
        "smoker": smoker == "Yes",
        "city": city,
        "occupation": occupation }

    try:

        response = requests.post(
            "http://127.0.0.1:8000/predict",
            json=data
        )

        if response.status_code == 200:

            prediction = response.json()

            st.success("Prediction Successful!")

            st.subheader("Predicted Premium Category")

            st.write(prediction)

        else:

            st.error("Prediction Failed")

            st.write(response.text)

    except Exception as e:

        st.error("Unable to connect to FastAPI server.")

        st.write(e)
