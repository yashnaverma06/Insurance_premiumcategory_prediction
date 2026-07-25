from fastapi import FastAPI
from pydantic import BaseModel, Field, computed_field, field_validator
from typing import Annotated, Literal, Optional
import pickle
import pandas as pd
from fastapi.responses import JSONResponse


#import the ml model
with open('insurance_model (1).pkl', 'rb') as f:
    model = pickle.load(f)


app = FastAPI()

tier_1_cities = ["Mumbai", "Delhi", "Bangalore", "Chennai", "Kolkata", "Hyderabad", "Pune"]
tier_2_cities = [
    "Jaipur", "Chandigarh", "Indore", "Lucknow", "Patna", "Ranchi", "Visakhapatnam", "Coimbatore",
    "Bhopal", "Nagpur", "Vadodara", "Surat", "Rajkot", "Jodhpur", "Raipur", "Amritsar", "Varanasi",
    "Agra", "Dehradun", "Mysore", "Jabalpur", "Guwahati", "Thiruvananthapuram", "Ludhiana", "Nashik",
    "Allahabad", "Udaipur", "Aurangabad", "Hubli", "Belgaum", "Salem", "Vijayawada", "Tiruchirappalli",
    "Bhavnagar", "Gwalior", "Dhanbad", "Bareilly", "Aligarh", "Gaya", "Kozhikode", "Warangal",
    "Kolhapur", "Bilaspur", "Jalandhar", "Noida", "Guntur", "Asansol", "Siliguri"
]


Occupation = ['Factory Worker', 'Businessman', 'Sales Manager', 'Banker',
       'Marketing Manager', 'Insurance Agent', 'HR Manager', 'Pharmacist',
       'Teacher', 'Software Engineer', 'Consultant', 'Driver',
       'Shop Owner', 'Nurse', 'Accountant', 'Government Employee',
       'Architect', 'Engineer', 'Real Estate Agent', 'Civil Servant',
       'Plumber', 'Retail Manager', 'Chef', 'Electrician', 'Carpenter',
       'Doctor', 'Lab Technician', 'Data Analyst', 'Lawyer',
       'Content Writer']

#build pydantic model to validate incoming data

class UserInput(BaseModel):
    age: Annotated[int, Field(..., gt=0, lt=120 , description = 'Age of user')]
    weight: Annotated[float, Field(..., gt=0, description = "weight of the user")]
    height: Annotated[float, Field(..., gt=0, description = 'height of user in cm')]
    income_lpa: Annotated[int, Field(..., gt=0, description = 'Income of user in lpa')]
    smoker: Annotated[bool, Field(..., description = 'Is the user a smoker(true/false)')]
    city: Annotated[str, Field(..., description = 'City that the belongs to')]
    occupation: Annotated[str, Field(..., description = 'Occupation of the user')]

    @field_validator("occupation")
    @classmethod
    def validate_occupation(cls, value):
        if value not in Occupation:
            raise ValueError("Invalid occupation")
        return value

    @computed_field
    @property
    def bmi(self) -> float:
            return self.weight/(self.height**2)

    @computed_field
    @property
    def lifestyle_risk(self) -> str:
        if self.smoker and self.bmi > 30:
            return "High"
        elif self.smoker or self.bmi > 25:
            return "Medium"
        else:
            return "Low"

    @computed_field
    @property
    def age_group(self) -> str:
        if self.age < 25:
            return 'Young Adult'
        elif self.age < 45:
            return 'Middle Age'
        else:
            return 'Senior'

    @computed_field
    @property
    def city_tier(self) -> int:
        if self.city in tier_1_cities:
            return 1
        elif self.city in tier_2_cities:
            return 2
        else:
            return 3

@app.post('/predict')
def predict_premium(data: UserInput):

     input_df = pd.DataFrame([{
          'bmi': data.bmi,
          'age_group': data.age_group,
          'lifestyle_risk': data.lifestyle_risk,
          'city_tier': data.city_tier,
          'income_lpa': data.income_lpa,
          'occupation': data.occupation
     }])

     prediction = model.predict(input_df)[0]

     return JSONResponse(status_code = 200, content = {'predicted_category': prediction})