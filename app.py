from pymongo import MongoClient
from flask import Flask,request

client=MongoClient('mongodb+srv://parvathanenimadhu:XXXXXXX@cluster0.yaaw6.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')

db=client['makeskilled'] 
collection=db['students'] 

# students - collection
# rollno, name, branch
# db.students.insert({'rollno':'10211A0478','name':'Madhu','branch':'ECE'});
# db.students.find();
# db.students.update({'rollno':'10211A0478'},{'$set':{'branch':'CSE'}})
# db.students.delete({'rollno':'10211A0478'})

app=Flask(__name__)

@app.route('/')
def home():
    return 'API Server is Online'

@app.route('/insert',methods=['GET'])
def insert():
    rollno=request.args.get('rollno')
    name=request.args.get('name')
    branch=request.args.get('branch')
    doc={
        'rollno':rollno,
        'name': name,
        'branch': branch
    }
    collection.insert_one(doc)
    return 'Inserted'

@app.route('/read')
def read():
    docList=[] # empty list 
    for i in collection.find():
        docList.append(i) # one document at time - docList (insert)
    return str(docList)

@app.route('/update',methods=['GET'])
def update():
    filter=request.args.get('filter') # '10211A0478'
    query=request.args.get('query') # 'branch'
    value=request.args.get('value') # 'CSE'
    new_query={'rollno':filter} # {'rollno':10211A0478}
    new_values={query:value} # {'branch':'CSE'}
    collection.update_one(
        new_query,{'$set':new_values}
    )
    return 'Updated'

@app.route('/delete',methods=['GET'])
def delete():
    filter=request.args.get('filter') # '10211A0478'
    new_query={'rollno':filter} # {'rollno':'10211A0478'}
    collection.delete_one(new_query)
    return 'deleted'

if (__name__=="__main__"):
    app.run(
        host='0.0.0.0',
        port=2000,
        debug=True
    )
