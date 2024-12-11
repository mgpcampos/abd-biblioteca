<h1 aling="center"> Biblioteca Comunitária </h1>
<p aling="center">Felipe Oliveira, Kauê Miranda, Mateus Gomes, Miguel Luís, Ray Guilherme</p>
<br>
<p aling="center">
<img loading="lazy" src="http://img.shields.io/static/v1?label=STATUS&message=EM%20DESENVOLVIMENTO&color=GREEN&style=for-the-badge"/>

<h1>👨‍🏫 Professores responsáveis</h1> 

-  Carlos Eduardo Duque Polito
-  Olavo Olimpo de Matos Junior

<h1>Introdução ao projeto</h1>

<h2>Objetivo</h2>
A aplicação é destinada ao gerenciamento de livros e reservas em bibliotecas. O principal objetivo é facilitar a interação entre usuários e bibliotecas, permitindo que os leitores busquem, reservem e gerenciem livros de maneira simples e intuitiva.

<h2>O que não é o objetivo do projeto</h2>

A integração com redes sociais para login ou o compartilhamento; 
A disponibilidade de recursos de avaliações ou comentários sobre os livros;
Não haverá métodos de pagamento pois não é o objetivo do projeto arrecadar dinheiro;
A escalabilidade. É um projeto pequeno e não queremos complica-lo.

<h2>Público-alvo</h2>
Todos que se interassam por livros. Seja para aquele que trabalha com isso ou para aquele que consome isso.

<h1>Requisitos do sistema</h1>

<h2>Requisitos funcionais:</h2>
A aplicação será dividida em dois tipos de usuários: o administrador e o usuário comum. O administrador será capaz de cadastrar livros, gerenciar estoques e visualizar reservas. O usuário comum, por sua vez, terá a capacidade de buscar por livros, consultar os detalhes de um livro, reservar os livros que desejarem e verificar o seu histórico de reservas.

<h2>Requisitos não funcionais:</h2>
O grupo não é capaz de garantir que, em um primeiro momento, a aplicação irá apresentar um bom desempenho geral, uma segurança relevante e uma fácil escalabilidade.

<h1>Funcionalidades do projeto</h2>

- `Desenvolver texto`

<h1>Instruções para operar aplicação</h1>

- `Informar instruções`

<h1>Matriz de Requisitos</h1>

- `Elaborar nossa própria matriz de requisitos`

<img src="https://github.com/user-attachments/assets/2743c732-f86c-4b2d-82a0-d9670abd84e6" width=1000> 

<h1>Modelagem do Banco de Dados</h1>

- `Elaborar nossa própria modelagem de banco de dados`
<img src="https://github.com/user-attachments/assets/f478260d-83f6-4f89-89a6-bb44cc65bb63" width=1000> 
<img src="https://github.com/user-attachments/assets/01773011-fe08-4dcf-ba66-b3a0956053bc" width=1000> 

<h1>Dicionário de Dados</h1>

- `Elaborar nosso próprio dicionário de dados`
<h2>Entidade Usuário</h2>
 Essa entidade é necessária para cadastrar o cliente (quem realiza a reserva) e seus dados, possuindo os campos id, email, nome, telefone e senha. 
 <br><br>
 
- `idUsuário`: É um atributo do tipo INT. É o responsável por criar um **Id único** para o usuário, que no caso é o cliente que fará a reserva (**CHAVE PRIMÁRIA**).
- `email`: É um atributo do tipo VARCHAR com um tamanho de 45 caracteres. É o responsável por armazenar o e-mail que o usuário cadastrou.
- `nome`: É um atributo do tipo VARCHAR com um tamanho de 45 caracteres. É o responsável por armazenar o nome do usuário.
- `telefone`: É um atributo do tipo VARCHAR com um tamanho de 45 caracteres. É o responsável por armazenar o número de telefone do usuário.
- `senha`: É um atributo do tipo VARCHAR com um tamanho de 45 caracteres. É o responsável por armazenar a senha que o usuário cadastrou.
- `created_at`: É um atributodo tipo DATE. É o responsável por armazenar a data em que o usuário realizou o cadastro.
  
<h2>Entidade Quarto</h2>
Essa entidade é responsável por armazenar as características dos quartos, contendo campos relacionados ao id, capacidade de ocupação do quarto, o preço da diária e a disponibilidade do mesmo.
<br><br>

- `idQuartos`: É um atributo do tipo INT. É o responsável por criar um **Id único** (**CHAVE PRIMÁRIA**).
- `capacidade`: É um atributo do tipo INT. É o responsável por armazenar a capacidade máxima de pessoas em um quarto.
- `preco_diaria`: É um atributo do tipo FLOAT. É o responsável por armazenar o preço de uma diária do quarto.
- `nome`: É um atributo do tipo VARCHAR com um tamanho de 45 caracteres. É o responsável por armazenar o nome do quarto.
- `Disponibilidade`: É um atributo do tipo INT. É o responsável por armazenar a disponibilidade do quarto, se for igual a 1 significa que o quarto esta disponível, se for igual a zero significa que esta indisponível.
- `imagem`: É um atributo do tipo VARCHAR com um tamanho de 45 caracteres. é o responsável por armazear o relative path da imagem específica do quarto.

<h2>Entidade Reserva</h2>
Essa entidade é a responsável por fazer a relação entre as outras demais tabelas, onde possui os campos id, checkin, checkout, preco_total, e os id's da tabela quarto e usuário. 
<br><br>

- `IdReserva`: É um atributo do tipo INT. É o responsável por criar um **Id único** (**CHAVE PRIMÁRIA**).
- `checkin`: É um atributo do tipo DATE. É o responsável por armazenar a data em que o usuário irá começar sua estadia no hotel.
- `checkout`: É um atributo do tipo DATE. É o responsável por armazenar a data em que o usuário irá terminar sua estadia no hotel.
- `preco_total`:  É um atributo do tipo FLOAT. É o responsável por armazenar o preço total de uma reserva, ou seja, o número de dias da estadia vezes o preco da diária.
- `Usuário_IdUsuário`: É um atributo do tipo INT. É o responsável por relacionar a tabela Reversa com a tabela Usuário através do id (**CHAVE ESTRANGEIRA**).
- `Quartos_IdQuartos`: É um atributo do tipo INT. É o responsável por relacionar a tabela Reversa com a tabela Quartos através do id (**CHAVE ESTRANGEIRA**).
- `data_reserva`: É um atributo do tipo DATE. É o responsável por armazenar a data em que o usuário efetuou a reserva.

<h2>Entidade Reserva Expirada</h2>
Essa entidade é a responsável por armazenar todas as reservas em que a data de check-out é mais velha que a data atual, ou seja, reservas que já acabaram. Os atributos da entidade possuem tipos e funções iguais a da entidade Reserva.



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

<h1>🏗️ Arquitetura da Aplicação</h1> 
<h2>Arquitetura do Software</h2>
<img src="https://github.com/user-attachments/assets/49e11b13-c231-4ae7-ae38-222c95d66f3e" width=1000> 

# Desenvolvedores responsáveis

| [<img loading="lazy" src="" width=115><br><sub>Felipe Oliveira</sub>]() |  [<img loading="lazy" src="" width=115><br><sub>Mateus Gomes</sub>]() |  [<img loading="lazy" src="" width=115><br><sub>Ray Guilherme</sub>]() |
| :---: | :---: | :---: |
