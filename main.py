import streamlit as st
from profiles import create_profile, get_notes, get_profile
from form_submit import update_personal_data, add_note, delete_note
from AI import get_macros

st.title("Personal Fitness Tool")

@st.fragment
def personal_data_form(): 
    with st.form ("personal_data_form"):
        st.write("Please fill out the following information:")
        st.header("Personal Information")
        
        profile = st.session_state.profile
        
        name  = st.text_input("Name", value=profile["general"]["name"])
        age  = st.number_input("Age", min_value=1, max_value=120 , step=1, value=profile["general"]["age"])
        weight = st.number_input("Weight (kg)", min_value=0.0, max_value=300.0, step=0.1, value=float(profile["general"]["weight"]))
        height = st.number_input("Height (cm)", min_value=0.0 ,max_value=250.0, step = 0.1, value=float(profile["general"]["height"]))
        genders = ["Male", "Female"]
        gender = st.radio('Gender', genders, genders.index(profile["general"].get("gender", "Male")))
        activities_level = ["Sedentary", "Lightly Active", "Moderately Active", "Very Active", "Extra Active"]
        activities = st.selectbox("Activity Level", activities_level , index= activities_level.index(profile["general"].get("Activity Level", "Lightly Active")))     
        
        personal_data_submit = st.form_submit_button("Submit")
        
        if personal_data_submit:
            if all([name, age, weight, height, gender, activities]):
                with st.spinner("Saving your data..."):
                    # Save data to database
                    st.session_state.profile = update_personal_data(profile, "general", name = name , weight = weight, height = height , gender = gender, activity = activities, age = age)
                    st.success("Data saved successfully!")
            else:
                st.warning("Please fill out all fields")
                               
#goals form 
@st.fragment
def goals_form():
    profile = st.session_state.profile
    with st.form("goals_form"):
        st.header("Goals")
        goals = st.multiselect("Select your goals", ["Muscle Gain", "Fat Loss", "Weight Loss", "Maintain Weight"], default=profile.get("goals", "Muscle Gain"))
        
        goals_submit = st.form_submit_button("Submit")
        if goals_submit:
            with st.spinner("Saving your goal..."):
                st.session_state.profile = update_personal_data(profile, "goals", goals = goals)
                st.success("Goals saved successfully!")
        else: 
            st.warning("Please select at least one goal")

@st.fragment
def macros(): 
    profile = st.session_state.profile
    nutrition = st.container(border=True)
    nutrition.header("Nutrition")
    if nutrition.button("Generate  with AI"): 
        result = get_macros(profile.get("general"), profile.get("goals"))
        profile["nutrition"] = result
        nutrition.success("Macros generated successfully!")
        
    with nutrition.form("nutrition_form", border=False):
        col1, col2, col3, col4 = st.columns(4)
        with col1:
           calories =  st.number_input("Calories",min_value=0 , step=1 , value=profile["nutrition"].get("calories", 0))
        with col2:
            protein = st.number_input("Protein (g)", min_value=0, step=1, value=profile["nutrition"].get("protein", 0))
        with col3:
            carbs = st.number_input("Carbs (g)", min_value=0, step=1, value=profile["nutrition"].get("carbs", 0))
        with col4:
            fat = st.number_input("Fat (g)", min_value=0, step=1, value=profile["nutrition"].get("fat", 0))
            
        if st.form_submit_button("Submit"):
            with st.spinner("Saving your data..."):
                st.session_state.profile = update_personal_data(profile, "nutrition", calories = calories, protein = protein, carbs = carbs, fat = fat)
                st.success("Information saved successfully!")
               
def forms(): 
    #checking if profile_id exists in the session state
    if "profile_id" not in st.session_state:
        profile_id = 1 
        profile = get_profile(profile_id)
        #checking if profile exists or in the database then create a new profile
        if not profile:
            profile_id, profile = create_profile(profile_id)
        
        st.session_state.profile_id = profile_id
        st.session_state.profile = profile
        
    if "notes" not in st.session_state:
        notes = get_notes(st.session_state.profile_id)
        st.session_state.notes = notes
        
    personal_data_form()
    goals_form()
    macros()
    
if __name__ == "__main__":
    forms()