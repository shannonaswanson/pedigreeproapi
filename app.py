from pymongo import MongoClient
from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from DogObjCleaner import DogObjCleaner
from BreedValidator import BreedValidator
from bson import ObjectId
import os

flask_env = os.getenv("FLASK_ENV", "development")
app = Flask(__name__)
cors = CORS(app) # allow CORS for all domains on all routes.
app.config['CORS_HEADERS'] = 'Content-Type'

dbName = "breeder"
# use the .env MONGODB_URI if it exists, otherwise default to localhost
client = MongoClient(os.getenv("MONGODB_URI", "mongodb://localhost:27017/"))
db = client[dbName]
dogCollection = db["dogs"]


dogObjCleaner = DogObjCleaner(BreedValidator())

# create a sample curl command to test the API
# curl -X GET http://localhost:5000/hello

# create GET request called hello
@app.route('/hello', methods=['GET'])
@cross_origin()
def hello():
    print("Received hello request")
    return jsonify({'message': 'Hello, World!'})


# POST request to search for dogs with pagination and sorting support
# Searches by registration number, name (partial match), gender, breed, or whelp date range
# 
# Acceptable JSON input:
# {
#   "registrationNumber": "DN61764904",        // Exact match
#   "name": "Fido",                           // Partial, case-insensitive match
#   "isMale": true,                           // true for male, false for female
#   "breed": "Labrador Retriever",            // Exact match
#   "startWhelpDate": "2023-01-01",           // Start of date range (YYYY-MM-DD)
#   "endWhelpDate": "2023-12-31",             // End of date range (YYYY-MM-DD)
#   "orderBy": "dogName",                     // Sort field: registrationNumber, dogName, whelpDate, breed
#   "orderDirection": "asc",                  // Sort direction: asc or desc
#   "page": 1,                                // Page number (default: 1)
#   "pageSize": 25                            // Results per page (default: 10, max: 1000)
# }
#
# Returns paginated results with metadata:
# {
#   "dogs": [...],                            // Array of dog objects
#   "pagination": {
#     "currentPage": 1,
#     "pageSize": 25,
#     "totalCount": 150,
#     "totalPages": 6,
#     "hasNext": true,
#     "hasPrev": false
#   }
# }
#
# Sample curl command:
# curl -X POST http://localhost:5001/search -H "Content-Type: application/json" -d '{"name": "Moon Fairy", "breed": "Border Collie", "page": 1, "pageSize": 25}'
@app.route('/search', methods=['POST'])
@cross_origin()
def search_dogs():
    default_page_size = 10
    print("Received search request")
    data = request.get_json()
    print(data)
    
    if not data:
        return jsonify({'message': 'Invalid request'}), 400

    # Extract pagination parameters with defaults
    page = data.get('page', 1)
    page_size = data.get('pageSize', default_page_size)

    # Validate pagination parameters
    if page < 1:
        page = 1
    if page_size < 1 or page_size > 1000:  # Cap max page size
        page_size = default_page_size

    query = {}
    if 'registrationNumber' in data:
        query['registrationNumber'] = data['registrationNumber']
    
    if 'name' in data:
        # need to change this to do a contains search, case insensitive
        query['dogName'] = {'$regex': data['name'], '$options': 'i'}

    if 'isMale' in data:
        # sex is either male or female string
        sex = 'female' 
        if data['isMale']:
            sex = 'male'
        query['sex'] = sex

    if 'breed' in data:
        query['breed'] = data['breed']

    if 'startWhelpDate' in data and 'endWhelpDate' in data:
        query['whelpDate'] = {
            '$gte': data['startWhelpDate'],
            '$lte': data['endWhelpDate']
        }
    elif 'startWhelpDate' in data:
        query['whelpDate'] = {'$gte': data['startWhelpDate']}
    elif 'endWhelpDate' in data:
        query['whelpDate'] = {'$lte': data['endWhelpDate']}

    if 'orderBy' in data:
        order_by = data['orderBy']
        if order_by not in ['registrationNumber', 'dogName', 'whelpDate', 'breed']:
            return jsonify({'message': f'Invalid orderBy field: {order_by}'}), 400
    else:
        order_by = 'registrationNumber'

    if 'orderDirection' in data:
        order_direction = data['orderDirection'].lower()
        if order_direction not in ['asc', 'desc']:
            return jsonify({'message': f'Invalid orderDirection: {order_direction}'}), 400
    else:
        order_direction = 'asc'

    # add sorting to the query
    if order_direction == 'asc':
        sort_order = 1
    else:
        sort_order = -1

    print("Query to be executed: ", query)
    
    # Calculate skip value for pagination
    skip = (page - 1) * page_size
    
    # Get total count and paginated results
    total_count = dogCollection.count_documents(query)
    dogs = list(dogCollection.find(query).sort(order_by, sort_order).skip(skip).limit(page_size))

    if not dogs:
        return jsonify({'message': 'No dogs found matching the criteria'}), 404
    
    # Clean up the results
    for dog in dogs:
        dog['_id'] = str(dog.get('_id'))
    
    # Calculate pagination metadata
    total_pages = (total_count + page_size - 1) // page_size  # Ceiling division
    has_next = page < total_pages
    has_prev = page > 1
    
    return jsonify({
        'dogs': dogs,
        'pagination': {
            'currentPage': page,
            'pageSize': page_size,
            'totalCount': total_count,
            'totalPages': total_pages,
            'hasNext': has_next,
            'hasPrev': has_prev
        }
    }), 200


# GET request to retrieve a dog's pedigree tree
# Fetches a dog and its ancestral lineage (sire and dam lines) up to available generations
# 
# Query parameters:
# - _id: MongoDB ObjectId of the dog (required)
#
# Example URL:
# /pedigree?_id=6856cc40f9a8bfcbe4b7b0b3
#
# Returns hierarchical pedigree data:
# [
#   {
#     "id": "dog_nameKey",           // Primary dog (root of tree)
#     "dogName": "Champion Dog",
#     "registrationNumber": "DN123",
#     "parentId": null,              // Root has no parent
#     "sireNameKey": "sire_nameKey",
#     "damNameKey": "dam_nameKey",
#     // ... other dog properties
#   },
#   {
#     "id": "sire_nameKey",          // Sire of primary dog
#     "dogName": "Sire Name",
#     "parentId": "dog_nameKey",     // References primary dog
#     "sex": "male",
#     // ... sire's ancestry continues
#   },
#   {
#     "id": "dam_nameKey",           // Dam of primary dog
#     "dogName": "Dam Name", 
#     "parentId": "dog_nameKey",     // References primary dog
#     "sex": "female",
#     // ... dam's ancestry continues
#   }
#   // ... additional ancestors with parentId references
# ]
#
# Sample curl command:
# curl -X GET "http://localhost:5001/pedigree?_id=6856cc40f9a8bfcbe4b7b0b3"
@app.route('/pedigree', methods=['GET'])
@cross_origin()
def get_dogs():
    if '_id' not in request.args:
        return jsonify({'message': 'Missing id parameter'}), 400
    dogs = []
    query = {}

    try:
        query["_id"] = ObjectId(request.args.get('_id'))
    except Exception as e:
        return jsonify({'message': f'Invalid id format: {e}'}), 400
    
    dog = db["dogs"].find_one(query)
    if not dog:
        return jsonify({'message': 'Dog not found'}), 404

    dog['_id'] = str(dog.get('_id'))
    dog['id'] = dog["nameKey"]
    dog['parentId'] = None

    if 'sire' in dog and dog['sire'] is not None:
        dog['sireNameKey'] = dogObjCleaner.getNameKey(dog["sire"], dog['breed'])
    
    if 'dam' in dog and dog['dam'] is not None:
        dog['damNameKey'] = dogObjCleaner.getNameKey(dog["dam"], dog['breed'])

    dogs.append(dog)

    pedigree = db["pedigrees"].find_one({"nameKey": dog["nameKey"]})
    if not pedigree:
        pedigree = db["pedigrees"].find_one({"registrationNumber": dog["registrationNumber"]})
    if not pedigree:
        print("No pedigree found for dog: ", dog["nameKey"])
        return jsonify(dogs)

    pedigreeMap = {}
    nodeDogObjMap = {}

    def addToPedigreeMap(parent, key):
        dogObj = None
        if key in parent:
            dogObj = db["dogs"].find_one({key: parent[key]})

        if dogObj:
            dogObj['_id'] = str(dogObj.get('_id'))
            dogObj['id'] = dogObj["nameKey"]
            pedigreeMap[dogObj["nameKey"]] = dogObj
            dogObj.pop("nameKey", None)
        else:
            if key in parent:
                nodeDogObjMap[parent[key]] = {'id': parent[key]}


    if pedigree:
        for sireParent in pedigree["sire"]:
            addToPedigreeMap(sireParent, "nameKey")
            addToPedigreeMap(sireParent, "registrationNumber")

        for damParent in pedigree["dam"]:
            addToPedigreeMap(damParent, "nameKey")
            addToPedigreeMap(damParent, "registrationNumber")

        def AddParentId(dogObj, parentId):
            if dogObj is not None:
                dogObj['parentId'] = parentId
                dogs.append(dogObj)
                sireDogObj = None
                damDogObj = None

                if 'sireNameKey' in dogObj and dogObj['sireNameKey'] is not None and dogObj['sireNameKey'] in pedigreeMap:
                    sireDogObj = pedigreeMap[dogObj['sireNameKey']]
                elif 'sireNameKey' in dogObj and dogObj['sireNameKey'] in nodeDogObjMap:
                    sireDogObj = nodeDogObjMap[dogObj['sireNameKey']]
                    sireDogObj['dogName'] = dogObj['sire']
                    sireDogObj['sex'] = 'male'

                if 'id' not in dogObj:
                    print("dogObj: ", dogObj)
                else:
                    AddParentId(sireDogObj, dogObj["id"])

                if 'damNameKey' in dogObj and dogObj['damNameKey'] is not None and dogObj['damNameKey'] in pedigreeMap:
                    damDogObj = pedigreeMap[dogObj['damNameKey']]
                elif 'damNameKey' in dogObj and dogObj['damNameKey'] in nodeDogObjMap:
                    damDogObj = nodeDogObjMap[dogObj['damNameKey']]
                    damDogObj['dogName'] = dogObj['dam']
                    damDogObj['sex'] = 'female'

                if 'id' in dogObj:
                    AddParentId(damDogObj, dogObj["id"])

        # dog is the parent object
        if 'sireNameKey' in dog and dog['sireNameKey'] is not None and dog['sireNameKey'] in pedigreeMap:
            sireDogObj = None
            if dog['sireNameKey'] in pedigreeMap:
                sireDogObj = pedigreeMap[dog['sireNameKey']]
            elif dog['sireNameKey'] in nodeDogObjMap:
                sireDogObj = nodeDogObjMap[dog['sireNameKey']]
                sireDogObj['dogName'] = dog['sire']

            AddParentId(sireDogObj, dog["nameKey"])
        if 'damNameKey' in dog and dog['damNameKey'] is not None and dog['damNameKey'] in pedigreeMap:
            damDogObj = None
            if dog['damNameKey'] in pedigreeMap:
                damDogObj = pedigreeMap[dog['damNameKey']]
            elif dog['damNameKey'] in nodeDogObjMap:
                damDogObj = nodeDogObjMap[dog['damNameKey']]
                damDogObj['dogName'] = dog['dam']

            AddParentId(damDogObj, dog["nameKey"])



    # delete to ObjectId property
    print("Dogs found: ", len(dogs))
    return jsonify(dogs)


if __name__ == '__main__':
    # Respect PORT environment variable (Cloud Run supplies this). Default to 5001 for local dev.
    port = int(os.getenv("PORT", 5001))
    app.run(debug=True, port=port, host="0.0.0.0")