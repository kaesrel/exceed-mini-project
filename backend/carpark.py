from flask import Flask, request
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://exceed_user:1q2w3e4r@158.108.182.0:2277/exceed_backend'
mongo =PyMongo(app)

myCollection = mongo.db.g13

@app.route('/create', methods=['POST'])
def insert():
    data = request.json
    myInsert = {
        "carpark": data["carpark"], #string Carpark_{x}
        "status": data["status"], #string {"available","parking","timeout"}
        "timein": data["timein"],  #string {"12.00"}
        "duration": data["duration"]  #int {5} minute
    }
    myCollection.insert_one(myInsert)
    return {"result": "Create succesfully"}

@app.route('/replace', methods=['PUT'])
def replace():
    data = request.json

    filt = {"carpark": data["carpark"]}

    updated_content = {"$set": {
        "carpark": data["carpark"],
        "status": data["status"],
        "timein": data["timein"],
        "duration": data["duration"]
    }}

    myCollection.update_one(filt, updated_content)
    return {"result": "Replace successfully"}

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='50003', debug=True)