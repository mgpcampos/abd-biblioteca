from flask import Flask, render_template, request, redirect, url_for, flash, session
from supabase import create_client, Client, StorageException
from PIL import Image
import os
import io
import requests


FLASK_SECRET_KEY = os.environ.get("FLASK_SECRET_KEY")

app = Flask(__name__)
app.secret_key = FLASK_SECRET_KEY

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)


@app.route('/', methods=['GET', 'POST'])
def index():
    username = session.get('username')  # Obtém o nome de usuário da sessão
    is_admin = False

    if not username:  # Se não houver um usuário logado
        flash('Você precisa estar logado para visualizar os livros.', 'danger')
        return redirect(url_for('login'))  # Redireciona para a página de login
    else:
        # Verificar se o usuário é administrador
        response = supabase.table('users').select('isAdmin').eq('username', username).execute()
        if response.data:
            is_admin = response.data[0]['isAdmin']
    
    # Se o usuário estiver logado, busca os livros no banco de dados
    books = supabase.table('books').select('*').order('popularity', desc=True).execute().data
    
    return render_template('index.html', username=username, books=books, is_admin=is_admin)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        role = request.form['role']

        is_admin = True if role == 'admin' else False

        response = supabase.table('users').insert({
            'username': username,
            'email': email,
            'password': password,
            'isAdmin': is_admin
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

@app.route('/book/<int:book_id>', methods=['GET', 'POST'])
def book_detail(book_id):
    username = session.get('username')  # Obtém o nome de usuário da sessão
    is_admin = False

    if username:
        # Verificar se o usuário é administrador
        response = supabase.table('users').select('isAdmin').eq('username', username).execute()
        if response.data:
            is_admin = response.data[0]['isAdmin']
    # Incrementar o contador de acessos usando RPC
    supabase.rpc('increment_popularity', {'book_id': book_id}).execute()
    # Obter detalhes do livro
    response = supabase.table('books').select('*').eq('id', book_id).execute()
    if response.data:
        book = response.data[0]
        return render_template('book_detail.html', username=username, is_admin=is_admin, book=book)
    else:
        flash('Livro não encontrado.', 'danger')
        return redirect(url_for('index'))

@app.route('/add_book', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        synopsis = request.form['synopsis']
        image_url = ''
        image_option = request.form.get('image_option')

        if image_option == 'url':
            image_url_input = request.form['image_url']

            # Download e redimensionar a imagem
            try:
                response = requests.get(image_url_input)
                response.raise_for_status()
                image = Image.open(io.BytesIO(response.content))
                image = image.resize((300, 450))  # Redimensionar para a resolução desejada

                # Determinar o formato da imagem
                image_format = image.format
                if not image_format:
                    # Tentar inferir o formato a partir do Content-Type
                    content_type = response.headers.get('Content-Type', '').lower()
                    if 'jpeg' in content_type or 'jpg' in content_type:
                        image_format = 'JPEG'
                    elif 'png' in content_type:
                        image_format = 'PNG'
                    elif 'gif' in content_type:
                        image_format = 'GIF'
                    elif 'webp' in content_type:
                        image_format = 'WEBP'
                    else:
                        # Definir como 'JPEG' se não for possível determinar o formato
                        image_format = 'JPEG'

                # Salvar a imagem em um objeto BytesIO no formato identificado
                buffered = io.BytesIO()
                image.save(buffered, format=image_format)
                buffered.seek(0)

                # Gerar o nome do arquivo
                file_extension = image_format.lower()
                file_name = f"{title.replace(' ', '_')}.{file_extension}"

                # Fazer upload da imagem para o Supabase Storage
                supabase.storage.from_('book-covers').upload(file_name, buffered.read())

                # Obter a URL pública
                image_url = supabase.storage.from_('book-covers').get_public_url(file_name)
            except Exception as e:
                print(f'Erro ao processar a imagem via URL: {e}')
                return redirect(url_for('add_book'))

        elif image_option == 'upload':
            if 'image_file' in request.files:
                image_file = request.files['image_file']
                if image_file.filename != '':
                    try:
                        # Abrir a imagem, converter para WebP e redimensionar
                        image = Image.open(image_file)
                        image = image.resize((300, 450))  # Redimensionar para a resolução desejada

                        # Salvar a imagem em um objeto BytesIO no formato WebP
                        buffered = io.BytesIO()
                        image.save(buffered, format="WEBP")
                        buffered.seek(0)

                        # Fazer upload da imagem para o Supabase Storage
                        file_name = f"{title.replace(' ', '_')}.webp"
                        supabase.storage.from_('book-covers').upload(file_name, buffered.read())

                        # Obter a URL pública
                        image_url = supabase.storage.from_('book-covers').get_public_url(file_name)
                    except Exception as e:
                        print(f'Erro ao processar a imagem via UPLOAD: {e}')
                        return redirect(url_for('add_book'))
                else:
                    flash('Nenhum arquivo de imagem selecionado.', 'danger')
                    return redirect(url_for('add_book'))
            else:
                flash('Nenhum arquivo de imagem enviado.', 'danger')
                return redirect(url_for('add_book'))

        # Inserir os dados no banco
        response = supabase.table('books').insert({
            'title': title,
            'author': author,
            'synopsis': synopsis,
            'image_url': image_url
        }).execute()

        if response.data:
            flash('Sucesso ao adicionar livro.', 'success')
            return redirect(url_for('index'))
        else:
            flash('Erro ao adicionar livro.', 'danger')
            return redirect(url_for('add_book'))

    return render_template('add_book.html')

@app.route('/update_book/<int:book_id>', methods=['GET', 'POST'])
def update_book(book_id):
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        synopsis = request.form['synopsis']

        response = supabase.table('books').update({
            'title': title,
            'author': author,
            'synopsis': synopsis
        }).eq('id', book_id).execute()

        if response.data:
            flash('Sucesso ao atualizar livro.', 'success')
            return redirect(url_for('index'))
        else:
            flash('Erro ao atualizar livro.', 'danger')
    
    book = supabase.table('books').select('*').eq('id', book_id).execute().data[0]
    return render_template('update_book.html', book=book)

@app.route('/remove_book/<int:book_id>', methods=['GET', 'POST'])
def remove_book(book_id):
    response = supabase.table('books').delete().eq('id', book_id).execute()

    if response.data:
        flash('Sucesso ao remover livro do catálogo.', 'success')
    else:
        flash('Erro ao remover livro do catálogo.', 'danger')
    
    return redirect(url_for('index'))


if __name__=='__main__':
   app.run()