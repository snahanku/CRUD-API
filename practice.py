


app.routes("/create" methods=['POST'])
def user():
    _json=request.json
    name= _json['name']
    email=_json['email']
    phone =_json['phone']

    if name  and email and phone and request.method=="POST":
        id =mongo.db.table name .insert_one( mongo code )
        resp=jsonify("user added sucessfully ")
        resp.status_code=200
        return resp
    



    
app.routes("/read" methods=["GET"])
def read():
    users= mongo.db.user.find()
    response=dumps(users)
    return response






app.route("/read/<id>" methods=["GET"])
def getuserId(id):
    users=mongo.db.user.find_one({_"id": objectid(id)})
    resp= dumps(users)
    return resp 







app.route.("/read/<email>" methods=["GET"])
def getemail(email):
    users=mongo.db.user.find_one({"email": Object_email(email)})
    resp=dumps(users)
    return resp


app.route ("/update/<id>" methods=["PUT"])
def update(id):
    _id=id
    _json= request.json
    name=_json["name"]
    email=_json["email"]
    phone= _json["phone"]

    if name and email and phone and  request.method=="PUT":
        mongo.db.update_one()
        response= jsonify({"usr updated successfully"})
        return response
    else:
        return not_found()







app.route("/delete/<id>" methods=["GET" ,"POST"])
def getdelete(id):
    users=mongo.db.user.delete_one({"_id:" Object_id(id)})
    resp=jsonify{"user deleted sucessfully "}
    return resp












