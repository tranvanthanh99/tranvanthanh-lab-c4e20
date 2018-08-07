from pymongo import MongoClient

mongo_uri = 'mongodb://admin:vantran297@ds151180.mlab.com:51180/c4e20-lab'

# 1. connect to database
client = MongoClient(mongo_uri)

# 2. get database
db = client.get_default_database()

# 3. Create a collection
games = db['games']

# # 4. create a document
# new_game = {
#     "title": "Hứng bia",
#     "description": "best game ever"
# }

# # 5. insert doc into collection
# games.insert_one(new_game)

# 6. Read all documents
all_game = games.find()
first_game = all_game[0]
print(first_game['description'])