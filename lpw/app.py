from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from flask import jsonify

client = MongoClient('mongodb://localhost:27017/')
db = client['mydb']
collection = db['books']

app = Flask(__name__)

@app.route('/home', methods=['GET'])
def hello():
    return 'Welcome to library management system!'


# CREATE
# api for adding books
@app.route('/addbook', methods=['POST'])
def addbook():
    book = request.json
    print(book)
    collection.insert_one(book)
    return 'book inserted!!'

# READ
# api for show books
@app.route('/show_books', methods=['GET'])
def show_books():
    books = collection.find()
    return jsonify(books)


# UPDATE
# api for updating books
@app.route('/update_book', methods=['PUT'])
def updatebook():
    book_id = request.json['id']
    new_book = request.json
    old_book = collection.find_one({'id': book_id})
    collection.update_one(old_book, {"$set": new_book})
    return 'Update book having id: ' + str(book_id); 

# DELETE
# api for delete books
@app.route('/delete_book', methods=['DELETE'])
def delete_book():
    book_id = request.json['id']
    collection.delete_one({'id': book_id})
    return 'Deleted book ' + str(book_id) + ' Successfully!!'
    

if __name__ == '__main__':
    app.run(debug=True, port=5000)
