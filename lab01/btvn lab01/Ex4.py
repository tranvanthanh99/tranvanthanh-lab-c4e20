import matplotlib
matplotlib.use("TKAgg")
from matplotlib import pyplot

from pymongo import MongoClient

mongo_uri = 'mongodb://admin:admin@ds021182.mlab.com:21182/c4e'

client = MongoClient(mongo_uri)
db = client.get_default_database()

customers = db['customers']

event = 0
wom = 0
ads = 0
all_customers = customers.find()

for i in all_customers:
    
    if i['ref'] == "events":
        event +=1
    elif i['ref'] == "wom":
        wom +=1
    elif i['ref'] == "ads":
        ads +=1

print("event: {}, wom: {}, ads: {}".format(event,wom,ads))

labels = ["events","wom","ads"]
values = [event,wom,ads]
color = ["yellow","orange","gold"]
explode = [0,0.15,0.1]

pyplot.pie(
    values,
    labels=labels,
    colors=color,
    explode=explode
    )
pyplot.axis('equal')

pyplot.show()