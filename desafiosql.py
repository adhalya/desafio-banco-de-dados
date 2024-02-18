import sqlite3

# Conectando com o banco de dados
desafiosql = sqlite3.connect('Desafio')
cursor = desafiosql.cursor()

# 1. Crie uma tabela chamada "alunos" com os seguintes campos: id (inteiro), nome (texto), idade (inteiro) e curso (texto).

#desafiosql.execute('CREATE TABLE alunos(id INT, nome VARCHAR(100), idade INT, curso VARCHAR(100))')


# 2.Insira pelo menos 5 registros de alunos na tabela que você criou no exercício anterior.

#cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(1, "Adhalya Intchala", 26, "Arquitetura")')
#cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(2, "Emilly Sousa", 32, "Engenharia Civil")')
#cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(3, "Oliver Castro", 29, "Biologia")')
#cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(4, "Franci Costa", 22, "Física")')
#cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(5, "Roberto Lima", 24, "Geografia")')


# 3.CONSULTAS BÁSICAS
    # a) Selecionar todos os registros da tabela "alunos".
    
#dados = cursor.execute('SELECT * FROM alunos')

    # b) Selecionar o nome e a idade dos alunos com mais de 20 anos.
    
#dados = cursor.execute('SELECT * FROM alunos WHERE idade>20')  

    # c) Selecionar os alunos do curso de engenharia em ordem alfabética.
    
#dados = cursor.execute('SELECT * FROM alunos WHERE curso="Engenharia Civil" ORDER BY nome')

    # d) Contar o número total de alunos na tabela

#dados = cursor.execute('SELECT COUNT(*) AS total_alunos FROM alunos')


# 4. ATUALIZAÇÃO E REMOÇÃO
    # a) Atualize a idade de um aluno específico na tabela.

#dados = cursor.execute('UPDATE alunos SET idade=27 WHERE nome="Emilly Sousa"')

    # b) Remova um aluno pelo seu ID.
    
#dados = cursor.execute('DELETE FROM alunos WHERE id=5')

# 5. CRIAR UMA TABELA E INSERIR DADOS
"""Crie uma tabela chamada "clientes" com os campos: id (chave
primária), nome (texto), idade (inteiro) e saldo (float). Insira alguns
registros de clientes na tabela."""

#dados = cursor.execute('CREATE TABLE clientes(id INT PRIMARY KEY, nome TEXT, idade INT, saldo FLOAT)')
#dados = cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES(1, "Adhalya", 26, "1000.50")')    
#dados = cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES(2, "Lorena", 32, "1500.75")') 
#dados = cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES(3, "Pedro", 40, "2000.00")') 
#dados = cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES(4, "Maria", 30, "1200.90")') 
#dados = cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES(5, "Ana", 35, "1800.25")') 


# 6. CONSULTAS E FUNÇÕES AGREGADAS
    # a) Selecione o nome e a idade dos clientes com idade superior a 30 anos.

#dados = cursor.execute('SELECT nome, idade FROM clientes WHERE idade>30')


    # b) Calcule o saldo médio dos clientes.
    
#dados = cursor.execute('SELECT AVG(saldo) AS saldo_medio FROM clientes')


    # c) Encontre o cliente com o saldo máximo.

#dados = cursor.execute('SELECT * FROM clientes ORDER BY saldo DESC LIMIT 1')


    # d) Conte quantos clientes têm saldo acima de 1000.
    
# dados = cursor.execute('SELECT COUNT(saldo>1000) AS saldo_superior_100 FROM clientes')


# 7. ATUALIZAÇÃO E REMOÇÃO COM CONDIÇÕES
    # a) Atualize o saldo de um cliente específico.

#dados = cursor.execute('UPDATE clientes SET saldo="890.50" WHERE nome="Adhalya"')


    # b) Remova um cliente pelo seu ID.

#dados = cursor.execute('DELETE FROM clientes WHERE id=4')
    
    
# 8. JUNÇÃO DE TABELAS
"""Crie uma segunda tabela chamada "compras" com os campos: id
(chave primária), cliente_id (chave estrangeira referenciando o id
da tabela "clientes"), produto (texto) e valor (real). Insira algumas
compras associadas a clientes existentes na tabela "clientes".
Escreva uma consulta para exibir o nome do cliente, o produto e o
valor de cada compra."""

#dados = cursor.execute('CREATE TABLE compras(id INT PRIMARY KEY, cliente_id INT, produto TEXT, valor REAL, FOREIGN KEY (cliente_id) REFERENCES clientes(id))')
#dados = cursor.execute('INSERT INTO compras(id, cliente_id, produto, valor) VALUES(1, 1, "Blusa", 25.99)')
#dados = cursor.execute('INSERT INTO compras(id, cliente_id, produto, valor) VALUES(2, 3, "Calça", 39.99)')
#dados = cursor.execute('INSERT INTO compras(id, cliente_id, produto, valor) VALUES(3, 2, "Tênis", 79.99)')
#dados = cursor.execute('INSERT INTO compras(id, cliente_id, produto, valor) VALUES(4, 5, "Meias", 9.99)')
dados = cursor.execute('SELECT c.id, cl.nome AS nome_cliente, c.produto, c.valor FROM compras c INNER JOIN clientes cl ON c.cliente_id = cl.id;')

for alunos in cursor:
    print(alunos) 

# Comitando no banco de dados
desafiosql.commit()
# Finalizando conexão com o banco de dados
desafiosql.close()