import streamlit as st
import pickle
import pandas as pd
from xgboost import XGBClassifier

with open('xgb.pkl', 'rb') as model_file:
    xgb_model = pickle.load(model_file)

feature_names = ['Gender', 'Customer Type', 'Age', 'Type of Travel',
       'Class', 'Flight Distance', 'Inflight wifi service',
       'Departure/Arrival time convenient', 'Ease of Online booking',
       'Gate location', 'Food and drink', 'Online boarding', 'Seat comfort',
       'Inflight entertainment', 'On-board service', 'Leg room service',
       'Baggage handling', 'Checkin service', 'Inflight service',
       'Cleanliness', 'Departure Delay in Minutes', 'Arrival Delay in Minutes']

st.title("Flight Passanger Satisfaction Prediction")
st.write("This model will help you predict the Flight passanger satisfaction.")

select_Gender = st.selectbox("Gender",["Female","Male"])
Gender = 0 if select_Gender == "Female" else 1

select_Customer_Type = st.selectbox("Customer Type",["Loyal Customer","disloyal Customer"])
Customer_Type = 0 if select_Customer_Type == "disloyal Customer" else 1

Age = st.number_input("Age",min_value=1,max_value=90)

select_TypeofTravel = st.selectbox("Travel Type",["Personal Travel","Business travel"])
TypeofTravel = 0 if select_TypeofTravel == "Personal Travel" else 1

select_Class = st.selectbox("Class",["Eco","Eco Plus","Business"])
Class = 0
if  select_Class == "Eco":
    Class = 0
elif select_Class == "Eco Plus":
    Class = 1
else:
    Class = 2

FlightDistance = st.number_input("Flight Travel Distance",min_value=10)
Inflightwifiservice = st.number_input("Inflight wifi service",min_value=0,max_value=5)
DepartureArrivaltimeconvenient = st.number_input("Departure Arrival time convenient",min_value=0,max_value=5)
EaseofOnlinebooking = st.number_input("Ease of Online booking",min_value=0,max_value=5)
Gatelocation = st.number_input("Gate location",min_value=0,max_value=5)
Foodanddrink = st.number_input("Food and drink",min_value=0,max_value=5)
Onlineboarding = st.number_input("Online boarding",min_value=0,max_value=5)
Seatcomfort = st.number_input("Seat comfort",min_value=0,max_value=5)
Inflightentertainment = st.number_input("Inflight Entertainment",min_value=0,max_value=5)
On_boardservice = st.number_input("On_board Service",min_value=0,max_value=5)
Legroomservice = st.number_input("Legroom Service",min_value=0,max_value=5)
Baggagehandling = st.number_input("Baggage Handling",min_value=0,max_value=5)
Checkinservice = st.number_input("Checkin Service",min_value=0,max_value=5)
Inflightservice = st.number_input("Inflight Service",min_value=0,max_value=5)
Cleanliness = st.number_input("Cleanliness",min_value=0,max_value=5)
DepartureDelayinMinutes = st.number_input("Departure Delay in Minutes",min_value=0)
ArrivalDelayinMinutes = st.number_input("Arrival Delay in Minutes",min_value=0)

entered_data = [Gender,Customer_Type,Age,TypeofTravel,Class,FlightDistance,
                           Inflightwifiservice,DepartureArrivaltimeconvenient,EaseofOnlinebooking,
                           Gatelocation,Foodanddrink,Onlineboarding,Seatcomfort,Inflightentertainment,
                           On_boardservice,Legroomservice,Baggagehandling,Checkinservice,Inflightservice,
                           Cleanliness,DepartureDelayinMinutes,ArrivalDelayinMinutes]

input_data = pd.DataFrame([entered_data], columns=feature_names)

if st.button("Predict"):
    prediction = xgb_model.predict(input_data)

    if prediction[0] == 1:
        st.success("Passanger is satisfied during this travel", icon="✅")
    else:
        st.warning("Passanger is not satisfied during this travel.",icon="⚠️")
