from bson import ObjectId
from src.models.database import db, collection
from src.models.model import TraineeModel, TraineeUpdateModel

#helper es una funcion usada para tareas especificas 
#-> sirve para señalar un diccionario
def helper_trainee(trainee) -> dict:
    return {
        "id": str(trainee["_id"]),
        "document": str(trainee["document"]),
        "firstname": trainee["firstname"],
        "lastname": str(trainee["lastname"]),
        "email": trainee["email"],
        "age": trainee["age"],
        "program": trainee["program"],
        "record_number": trainee["record_number"]
    }