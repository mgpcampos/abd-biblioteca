from flask import Flask, render_template, request, redirect, url_for, flash, session
from supabase import create_client, Client
import os

FLASK_SECRET_KEY = os.environ.get("FLASK_SECRET_KEY")

app = Flask(__name__)
app.secret_key = FLASK_SECRET_KEY

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)


@app.route('/')
def index():
    response = supabase.table('books').select('*').execute()
    books = response.data if response.data else []
    username = session.get('username')
    return render_template('index.html', books=books, username=username)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        response = supabase.table('users').insert({
            'username': username,
            'email': email,
            'password': password
        }).execute()

        if response.data:
            flash('Sucesso ao registrar usuário.', 'success')
            return redirect(url_for('login'))
        else:
            flash('Erro ao registrar usuário.', 'danger')
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        response = supabase.table('users').select('*').eq('email', email).eq('password', password).execute()
        if response.data:
            session['username'] = response.data[0]['username']
            return redirect(url_for('index'))
        else:
            flash('E-mail ou senha inválido(s).', 'danger')
            return redirect(url_for('login'))
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    flash('Você saiu de sua conta.', 'success')
    return redirect(url_for('index'))


if __name__=='__main__':
   app.run()