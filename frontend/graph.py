from flask import Flask, request, render_template
from flask_pymongo import PyMongo
# from isodate import ISODate
import datetime

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://exceed_user:1q2w3e4r@158.108.182.0:2277/exceed_backend'
mongo = PyMongo(app)

myCollection = mongo.db.g13

# print("hello test")

@app.route('/',methods=['GET'])
def funct1():
    return render_template("graph.html")


# @app.route('/find_all', methods=['GET'])
# def find():
#     #flit = {"author": "PNon"}
#     #flit = {}
#     myName = request.args.get('name')
#     flit = {"author": myName}

#     query = myCollection.find(flit)
#     output = []

#     for ele in query:
#         output.append({
#                 "author": ele["author"],
#                 "content1": ele["content1"],
#                 "content2": ele["content2"]
#                 })

#     return { "result": output }

# Park History
# {
#     "slotNo": x,
#     "startDateTime": "some time format",
#     "endDateTime": "some time format",
# }

# Slot Realtime
# {
#     "slotInfo": [x,x,x,x],
#     "dateTime": "some time format"
# }

# @app.route('/create', methods=['POST'])
# def insert_one():
#     data = request.json
#     myInsert = {
#             "slotNo": data["slotNo"],
#             "startDateTime": data["startDateTime"],
#             "endDateTime": data["endDateTime"],
#             }
#     myCollection.insert_one(myInsert)
#     return {'result': 'Created successfully'}

@app.route('/create_many', methods=['GET'])
def insert_many():
    data = request.json
    myInsert = [
        {"slotNo": "1", "startDateTime": datetime.datetime(2021,2,13,13,0,0), "endDateTime": datetime.datetime(2021,2,13,13,30,0)},
        {"slotNo": "1", "startDateTime": datetime.datetime(2021,2,13,13,40,0), "endDateTime": datetime.datetime(2021,2,13,13,59,0)},
        {"slotNo": "1", "startDateTime": datetime.datetime(2021,2,13,14,0,0), "endDateTime": datetime.datetime(2021,2,13,14,10,0)},
        {"slotNo": "1", "startDateTime": datetime.datetime(2021,2,13,14,23,0), "endDateTime": datetime.datetime(2021,2,13,14,41,0)},
        {"slotNo": "1", "startDateTime": datetime.datetime(2021,2,13,16,0,0), "endDateTime": datetime.datetime(2021,2,13,16,15,0)},
        {"slotNo": "1", "startDateTime": datetime.datetime(2021,2,13,17,0,0), "endDateTime": datetime.datetime(2021,2,13,21,7,0)}
    ]
    myCollection.insert_many(myInsert)
    return {'result': 'Created successfully'}

@app.route('/search', methods=['POST'])
def search_time():
    data = request.json
    d=datetime.datetime.now();
    # d=datetime.datetime.fromtimestamp(data["startDateTime"])
    filt = {"startDateTime": {"$gte": d}}

    result = myCollection.find(filt)
    output = []
    for e in result:
        output.append({
        "slotNo": e["slotNo"],
        "startDateTime": e["startDateTime"],
        "endDateTime": e["endDateTime"]
        })

    return {"result": output}

# @app.route('/search_me', methods=['GET'])
# def search_time():
#     # myDate = request.args.get('myDate')
#     # filt = {"startDateTime": {"$lt": data["startDateTime"]}}
#     # filt = {"startDateTime": data["startDateTime"]}
#     filt = {"startDateTime":  dateutil.parser.parse("2021-02-13T14:00:00.000Z")}
#     # {'$match': {'timestamp': {'$gte': start, '$lte': end}}}

#     result = myCollection.find(filt)
#     output = []
#     for e in result:
#         output.append(e)

#     return {"result": output}


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='50003', debug=True)