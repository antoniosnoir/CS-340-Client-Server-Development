from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations Animal collection in MongoDB """
    
    def __init__(self, username, password):
        # Initializing the MongoClient. This helps tohttp://localhost:8891/edit/AntonFiles/animal_shelter.py#
        # access the MongoDB satabases and collections.
        #self.client = MongoClient('mongodb://localhost:55072')
        self.client = MongoClient('mongodb://%s:%s@localhost:55072/?authMechanism=DEFAULT&authSOURCE=AAC'% (username, password))
        self.database = self.client['AAC']
        
# Complete this create method to implement the C in CRUD
    def create(self, data):
        if data is not None:
            self.database.animals.insert(data) # data should be dictionary
            #if insert != 0:
            return True
                #print("True")
            #else:
                #return False
                #print("False")
        else:
            raise Exception("Nothing to save, because data parameter is empty")
            
    def read_all(self, data):
        cursor = self.database.animals.find(data, {'_id':False})
        return cursor

# Create method to implement the R in CRUD
    def read(self, data):
        self.database.animals.find_one(data)
        if data is not None: 
            results = self.database.animals.find(data, {"_id":False, "name":1, "type":1}) #_id False to skip row ID
            return results
        else:
            raise Exception("No results found")
        return data
        
# Method to implement the U in CRUD, Update
    def update(self, data, updatedData):
        if data is not None and updatedData is not None:
            self.database.animals.replace_one(data, {"_id":False}, {"$set":updatedData}, upsert = False)
            self.read(updatedData)
            #return results
        else:
            raise Exception("Data not updated successfully")
            
# Method to implement the D in CRUD, Delete
    def delete(self, data):
        if data is not None:
            results = self.database.animals.find_one(data, {"_id":False, "name":1, "type":1})
            if results is not None:
                remove = self.database.animals.delete_one(data)
                print("Animal has been removed from database")
                return
            else:
                print("No animal found in the database")
                return
        else:
            raise Exception("Error, the animal data is empty, cannot delete")
        