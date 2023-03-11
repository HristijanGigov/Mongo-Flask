from flask import Flask, request, jsonify
import sqlite3
import pymongo


app = Flask(__name__)



@app.route("/", methods = ["GET"]) 
def read():
    db = sqlite3.connect("data.db")
    mycursor = db.cursor()
    mycursor.execute("SELECT * FROM companies LIMIT 10") 
    companies = []
    for x in mycursor.fetchall():
        y = {
            "id":   x[0],
            "name": x[1],
            "country_iso": x[2],
            "city": x[3],
            "nace": x[4],
            "website": x[5]
        }
        companies.append(y) 
    mycursor.close()
    db.close()
    return jsonify({"companies": companies})




@app.route("/", methods=["POST"])
def add():
    client = pymongo.MongoClient("mongodb://localhost:27017/")  
    db = client["mydb"] 
    lista = db["cleaned_companies"] 
    get_data = request.get_json()
    append = lista.insert_one(get_data)

    
    if append == True:
        return "success" 
    else:
        return "failed"
 


if __name__ == "__main__": 
    app.run(debug=True)