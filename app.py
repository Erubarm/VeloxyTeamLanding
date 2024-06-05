from flask import Flask, request, send_from_directory
import sqlite3

app = Flask(__name__, static_url_path='', static_folder='static')

def init_db():
       conn = sqlite3.connect('contacts.db')
       cursor = conn.cursor()
       cursor.execute('''
           CREATE TABLE IF NOT EXISTS Contact (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               first_name TEXT NOT NULL,
               last_name TEXT NOT NULL,
               phone TEXT NOT NULL,
               message TEXT NOT NULL
           )
       ''')
       conn.commit()
       conn.close()

@app.route('/')
def home():
       return send_from_directory('static', 'index.html')

@app.route('/submit_form', methods=['POST'])
def submit_form():
       first_name = request.form['first_name']
       last_name = request.form['last_name']
       phone = request.form['phone']
       message = request.form['message']

       conn = sqlite3.connect('contacts.db')
       cursor = conn.cursor()
       cursor.execute('''
           INSERT INTO Contact (first_name, last_name, phone, message)
           VALUES (?, ?, ?, ?)
       ''', (first_name, last_name, phone, message))
       conn.commit()
       conn.close()
       
       return 'Форма успешно отправлена!'

if __name__ == '__main__':
       init_db()
       app.run(debug=True)