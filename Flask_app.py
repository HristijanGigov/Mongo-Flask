from flask import Flask, request, jsonify
import sqlite3
import pymongo

#creating flask app
app = Flask(__name__)


#forming a route with get method 
@app.route("/", methods = ["GET"]) 
def read():
    db = sqlite3.connect("data.db") #connection to data base 
    mycursor = db.cursor()
    mycursor.execute("SELECT * FROM companies LIMIT 10") #read 10 companies 
    companies = []
    for x in mycursor.fetchall():#looping through the information
        y = {
            "id":   x[0],
            "name": x[1],
            "country_iso": x[2],
            "city": x[3],
            "nace": x[4],
            "website": x[5]
        }
        companies.append(y) #appending the looped companies
    mycursor.close() 
    db.close()
    return jsonify({"companies": companies})



# route with post method on mongo db
@app.route("/", methods=["POST"])
def add():
    client = pymongo.MongoClient("mongodb://localhost:27017/")  #connection throught local host
    db = client["mydb"] 
    lista = db["cleaned_companies"] #forming a new db 
    get_data = request.get_json()
    append = lista.insert_one(get_data)  #appending the data in the new formed db

    #returns failure if the program has errors
    if append == True:
        return "success" 
    else:
        return "failed"
 

#activating the debugger on flask
if __name__ == "__main__": 
    app.run(debug=True)
