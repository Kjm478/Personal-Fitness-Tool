import streamlit as st

st.title("Personal Fitness Tool")

@st.fragment
def personal_data_form(): 
    with st.form ("personal_data_form"):
        st.write("Please fill out the following information:")
        st.header("Personal Information")
        name  = st.text_input("Name")
        age  = st.number_input("Age", min_value=1, max_value=120 , step=1)
        weight = st.number_input("Weight (kg)", min_value=0.0, max_value=300.0, step=0.1)
        height = st.number_input("Height (cm)", min_value=0.0 ,max_value=250.0, step = 0.1)
        gender = st.radio('Gender', ["Male", "Female"])
        activities = st.selectbox("Activity Level", ["Sedentary", "Lightly Active", "Moderately Active", "Very Active", "Super Active"])  
        
        personal_data_submit = st.form_submit_button("Submit")
        
        if personal_data_submit:
            if all([name, age, weight, height, gender, activities]):
                with st.spinner("Saving your data..."):
                    # Save data to database
                    st.success("Data saved successfully!")
            else:
                st.warning("Please fill out all fields")
               
def forms(): 
    personal_data_form()
    
if __name__ == "__main__":
    forms()