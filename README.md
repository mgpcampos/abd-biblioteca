<h1 aling="center"> Biblioteca Comunitária </h1>
<p aling="center">Felipe Oliveira, Mateus Gomes, Miguel Luís, Ray Guilherme</p>
<br>
<p aling="center">


<h1> Professores responsáveis </h1> 

-  Carlos Eduardo Duque Polito
-  Olavo Olimpo de Matos Junior

<h1>Introdução ao projeto</h1>

<h2>Objetivo</h2>
A aplicação é destinada ao gerenciamento de livros em bibliotecas. O principal objetivo é facilitar a interação entre usuários e bibliotecas e o gerenciamento de livros de maneira simples.

<h2>O que não é o objetivo do projeto</h2>

A integração com redes sociais para login ou o compartilhamento; 
A disponibilidade de recursos de avaliações ou comentários sobre os livros;
Não haverá métodos de pagamento pois não é o objetivo do projeto arrecadar dinheiro;
A escalabilidade. É um projeto pequeno e não queremos complica-lo.
Não haverá reservas. Nosso site será usado mais para a averiguar os livros disponíveis na biblioteca local e sua popularidade. Se não haver mais o livro nós o removeremos.

<h2>Público-alvo</h2>
Todos que se interassam por livros. Seja para aquele que trabalha com isso ou para aquele que consome isso.

<h1>Requisitos do sistema</h1>

<h2>Requisitos funcionais:</h2>
A aplicação será dividida em dois tipos de usuários: o administrador e o usuário comum. O administrador será capaz de cadastrar livros, gerenciar estoques e visualizar reservas. O usuário comum, por sua vez, terá a capacidade de buscar por livros, consultar os detalhes de um livro, reservar os livros que desejarem e verificar o seu histórico de reservas.

<h2>Requisitos não funcionais:</h2>
O grupo não é capaz de garantir que, em um primeiro momento, a aplicação irá apresentar um bom desempenho geral, uma segurança relevante e uma fácil escalabilidade.

<h1>Funcionalidades do projeto</h2>
A aplicação de gerenciamento de livros em bibliotecas será uma ferramenta intuitiva e prática, dividida entre dois tipos de usuários: administradores e usuários comuns.

<h3>Funcionalidades para o Administrador:</h3>

- `Cadastro de livros`: Possibilidade de inserir novos títulos, incluindo informações como nome, autor, gênero, quantidade disponível, entre outros.

<h3>Funcionalidades para o Usuário Comum:</h3>

- `Consulta por detalhes`: Visualização de informações detalhadas sobre os livros disponíveis.

<h1>Instruções para operar a aplicação</h1>

#### 1. Clonar o Repositório
```bash
git clone https://github.com/mgpcampos/abd-biblioteca
```
#### 2. Navegar até o Diretório do Projeto
```bash
cd abd-biblioteca
```
#### 3. Criar e Ativar um Ambiente Virtual
```bash
python -m venv .venv
```
#### • Windows
```bash
.venv\Scripts\activate
```
#### • Linux/macOS
```bash
source venv/bin/activate
```
#### 4. Instalar as Dependências
```bash
pip install -r requirements.txt
```
#### 5. Configurar Variáveis de Ambiente
#### Crie um arquivo .env na raiz do projeto e adicione as seguintes linhas:
```
FLASK_SECRET_KEY=SuaChaveSecreta
SUPABASE_URL=SuaURLdoSupabase
SUPABASE_KEY=SuaChaveDoSupabase
```
#### 6. Executar a Aplicação
```bash
flask run
```
Para executar em modo de desenvolvimento com recarregamento automático, execute:
```bash
flask run --debug
```
Caso obtenha sucesso, acesse 127.0.0.1:5000/


<h3>Administradores:</h3>

1. Acesse o sistema e crie uma conta como administrador.
2. Faça login com seu e-mail e senha cadastrados.
3. Acesse o painel administrativo para:
    - Cadastrar novos livros.
    - Atualizar os livros conforme for necessário.

<h3>Usuário Comum:</h3>

1. Acesse o sistema e crie uma conta como Usuário Comum (se ainda não tiver).
2. Faça login com seu e-mail e senha cadastrados.
3. Consulte os detalhes de um livro de seu interesse para verificar informações sobre ele.


<h1>Matriz de Requisitos</h1>

<img src="https://github.com/user-attachments/assets/ce9936ef-0c1d-497c-9963-4213440f7146"> 

<h1>Modelagem do Banco de Dados</h1>

<img src="https://github.com/user-attachments/assets/d92c13f3-df83-4f39-8058-c87b2a14353e"> 


<h1>Dicionário de Dados</h1>
Esse projeto contará com as seguintes Entidades e atributos

<h2>Entidade usuários</h2>
 Essa entidade é necessária para cadastrar tanto o usuário comum quanto o administrador, possuindo os campos: id, nome, email, senha e ISadmin. 
<br><br>
 
- `idUsuário`: É um atributo do tipo INT. É o responsável por criar um **Id único** para o usuário, que no caso é o usuário comum ou o administrador (**CHAVE PRIMÁRIA**).
- `ISadmin`: É um atributo do tipo BOOL. ISAdmin só armazena valores TRUE ou FALSE. Se no caso de um usuário A, o valor for TRUE, então esse usuário é um administrador. Se for false, é um usuário comum.
- `nome`: É um atributo do tipo VARCHAR com um tamanho de 45 caracteres. É o responsável por armazenar o nome do usuário.
- `senha`: É um atributo do tipo VARCHAR com um tamanho de 45 caracteres. É o responsável por armazenar a senha que o usuário cadastrou.

<h2>Entidade books</h2>
 Essa entidade é necessária para cadastrar todas as informações do livro registrado, possuindo os campos: id, título, autor, sinopse, capa, popularidade.
 <br><br>

`idBook`: É um atributo do tipo INT. É o responsável por criar um **Id único** para o livro registrado (**CHAVE PRIMÁRIA**).
- `título `: É um atributo do tipo VARCHAR com um tamanho de 45 caracteres. É o responsável por armazenar o título do livro.
- `autor`: É um atributo do tipo VARCHAR com um tamanho de 45 caracteres. É o responsável por armazenar o nome do autor.
- `imagem_url`: É um atributo do tipo VARCHAR com um tamanho de 45 caracteres. É o responsável por armazenar a capa do livro.
- `sinopse`: É um atributo do tipo VARCHAR com um tamanho de 45 caracteres. É o responsável por armazenar a sinopse do livro.
- `popularidade ` É um atributo do tipo INT. Serve pra contagem de quantos clicks um livro recebeu. Por que o index mostra os livros de modo decrescente de acordo com a contagem de clicks.

<h1>Tecnologias utilizadas</h1> 

`Front-end`:
<br><br>
<img src="https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white">
<img src="https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white">
<img src="https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E">

`Back-end`:
<br><br>
<img src="https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white">

`Banco de Dados`:
<br><br>
<img src="https://img.shields.io/badge/supabase-%2300C4B7.svg?style=for-the-badge&logo=supabase&logoColor=white">

<h1>Arquitetura da Aplicação</h1> 
<h2>Arquitetura do Software</h2>
<img src="https://github.com/user-attachments/assets/49e11b13-c231-4ae7-ae38-222c95d66f3e" width=1000>