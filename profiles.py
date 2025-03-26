from db import personal_data_collection, notes_collection

def get_values(_id):
    return {
        "id": _id,
        "general":{
            "name": "John Doe",
            "age": 25,
            "weight": 70,
            "height": 170,
            "activity": "Lightly Active",
            "gender": "Male"
        },
        "goals": ["Muscle Gain"],
        "nutrition": {
            "calories": 2000,
            "protein": 100,
            "carbs": 200,
            "fat": 50
        },
    }
    
    
def create_profile(_id):
    profile = get_values(_id)
    inserted_id = personal_data_collection.insert_one(profile)
    return inserted_id, profile

def get_profile(_id):
    return personal_data_collection.find_one({"id": {"$eq": _id}})

def get_notes(_id):
    return list(notes_collection.find({"user_id": {"$eq": _id}}))