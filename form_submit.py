from datetime import datetime
from db import personal_data_collection, notes_collection

def update_personal_data(existing, update_type, **kwargs):
    if update_type == "goals":
        existing["goals"] = kwargs.get("goles",[])
        update_field = {"goals": existing["goals"]}
    else: 
        existing[update_type] = kwargs 
        update_field = {update_type: existing[update_type]}
        
    personal_data_collection.update_one({"_id": existing["_id"]}, {"$set": update_field})
    return existing


def add_note(note, profile_id):
    new_note = {"user_id": profile_id, 
                "text": note, 
                "$vectorize": note, 
                "metatdata": {"injested": datetime.now()},
                }
    result = notes_collection.insert_one(new_note)
    new_note["_id"] = result.inserted_id
    return new_note

def delete_note(note_id):
    return notes_collection.delete_one({"_id": note_id})