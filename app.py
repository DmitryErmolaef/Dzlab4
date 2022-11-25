import requests
from flask import Flask, render_template, request
import psycopg2


app = Flask(__name__)

conn = psycopg2.connect(database="service_db", user="postgres", password="Ermollaef32", host="localhost", port="5432")

cursor = conn.cursor()

@app.route('/login/', methods=['GET'])
def index():
    return render_template('login.html')

@app.route('/login/', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    cursor.execute("SELECT * FROM service.users WHERE login=%s and password=%s", (str(username), str(password)))
    records = list(cursor.fetchall())
    print(records)
    if len(username) == 0 and len(password) == 0: return render_template('account.html', full_name = 'вы ввели не корректные данные')
    
    elif len(records) == 0: return render_template('account.html', full_name = 'вы не зарегистрировались в нашем приложении')

    else: return render_template('account.html', full_name=f'{records[0][1]}. Ваш Login: {str(username)}, Password: {str(password)}')

if __name__ == "__main__":
    app.run()
