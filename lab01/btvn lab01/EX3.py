from pymongo import MongoClient

mongo_uri = 'mongodb://admin:admin@ds021182.mlab.com:21182/c4e'

client = MongoClient(mongo_uri)
db = client.get_default_database()

posts = db['posts']

add_post = {
    'title': 'Quick Math' ,
    'author': 'someone',
    'content': '''1 + 1 = 2
                  2 + 2 = 3
                  wow!!!'''
}

posts.insert_one(add_post)