import streamlit as st
from .profiles import create_profile, get_notes, get_profile

st.title("Personal Fitness Tool")

@st.fragment
def personal_data_form(): 
    with st.form ("personal_data_form"):
        st.write("Please fill out the following information:")
        st.header("Personal Information")
        
        profile = st.session_state.profile
        
        name  = st.text_input("Name", value=profile["general"]["name"])
        age  = st.number_input("Age", min_value=1, max_value=120 , step=1, value=profile["general"]["age"])
        weight = st.number_input("Weight (kg)", min_value=0.0, max_value=300.0, step=0.1, value=profile["general"]["weight"])
        height = st.number_input("Height (cm)", min_value=0.0 ,max_value=250.0, step = 0.1, value=profile["general"]["height"])
        genders = ["Male", "Female"]
        gender = st.radio('Gender', genders, genders.index(profile["general"].get("gender", "Male")))
        activities = st.selectbox("Activity Level", ["Sedentary", "Lightly Active", "Moderately Active", "Very Active", "Super Active"] , index=profile["general"].get("activity", 0))     
        
        personal_data_submit = st.form_submit_button("Submit")
        
        if personal_data_submit:
            if all([name, age, weight, height, gender, activities]):
                with st.spinner("Saving your data..."):
                    # Save data to database
                    
                    st.success("Data saved successfully!")
            else:
                st.warning("Please fill out all fields")
               
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
    
if __name__ == "__main__":
    forms()