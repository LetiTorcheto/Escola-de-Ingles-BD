import psycopg2


tables = {'CURSO' :(
    """CREATE TABLE CURSO (
    id_curso Integer PRIMARY KEY,
    nome_curso VARCHAR(100),
    faixa_etaria VARCHAR(50),
    nivel VARCHAR(50),
    valor_curso FLOAT);"""),
    
    'RESPONSAVEL':(
    """CREATE TABLE RESPONSAVEL (
    forma_pagamento VARCHAR(100),
    validade_cartao DATE,
    vinculo VARCHAR(20),
    nome_responsavel VARCHAR(100),
    email_responsavel VARCHAR(100),
    fone_responsavel VARCHAR(20),
    id_responsavel INTEGER PRIMARY KEY
    );"""),

'TURMA' :(
    """CREATE TABLE TURMA (
    id_turma INTEGER PRIMARY KEY,
    horario VARCHAR(10),
    sala VARCHAR(10),
    dias_semana VARCHAR(50),
    CURSO_id_curso INTEGER,
    FOREIGN KEY (CURSO_id_curso) REFERENCES CURSO (id_curso)
    );"""),

'INSCRICAO': (
    """CREATE TABLE INSCRICAO (
    id_inscricao INTEGER PRIMARY KEY,
    FK_LEAD_id_lead INTEGER,
    FK_USUARIO_id_usuario INTEGER
);
"""),

'ALUNO':(
    """ CREATE TABLE ALUNO (
    id_conta Integer PRIMARY KEY,
    nome VARCHAR(100),
    telefone VARCHAR(20),
    email VARCHAR(100),
    ativo Boolean,
    idade Int,
    FK_TURMA_id_turma integer,
    FK_RESPONSAVEL_id_responsavel INTEGER,
    aluno_responsavel Boolean,
    FK_INSCRICAO_id_inscricao integer
);
"""),

'LEAD' :(
    """CREATE TABLE LEAD (
    id_lead INTEGER PRIMARY KEY,
    nome_lead VARCHAR(100),
    telefone_lead VARCHAR(20),
    email_lead VARCHAR(100),
    status_lead VARCHAR(100),
    idade INT,
    FK_CAMPANHA_id_campanha INTEGER
);
"""),

'PLACEMENT_TEST': (
    """CREATE TABLE PLACEMENT_TEST (
    id_placement INTEGER PRIMARY KEY,
    score FLOAT,
    descricao_placement VARCHAR(255),
    FK_LEAD_id_lead INTEGER);
"""),

'USUARIO':(
    """CREATE TABLE USUARIO (
    nome_usuario VARCHAR(100),
    id_usuario INTEGER PRIMARY KEY,
    email_usuario VARCHAR(100),
    fone_usuario VARCHAR(20),
    salario FLOAT,
    especializacao VARCHAR(100),
    funcao VARCHAR(100),
    USUARIO_TIPO INT
);
"""),

'CAMPANHA' :(
    """CREATE TABLE CAMPANHA (
    id_campanha INTEGER PRIMARY KEY,
    data_campanha DATE
    );"""),

'MATERIAL_DIDATICO' : (
    """CREATE TABLE MATERIAL_DIDATICO (
    id_md INTEGER PRIMARY KEY,
    qtd_md INTEGER,
    valor_md FLOAT,
    acessorios VARCHAR(100),
    CURSO_id_curso INTEGER,
    FOREIGN KEY (CURSO_id_curso) REFERENCES CURSO (id_curso)
    );"""),

'MENSALIDADE': (
    """CREATE TABLE MENSALIDADE (
    id_mensalidade INTEGER PRIMARY KEY,
    valor_total FLOAT,
    CURSO_id_curso INTEGER,
    FOREIGN KEY (CURSO_id_curso) REFERENCES CURSO (id_curso)
    );"""),



'PROFESSOR_TURMA' : (
    """CREATE TABLE PROFESSOR_TURMA (
    USUARIO_id_usuario INTEGER,
    TURMA_id_turma INTEGER,
    id_professor INTEGER PRIMARY KEY,
    monitor BOOLEAN,
    FOREIGN KEY (USUARIO_id_usuario) REFERENCES USUARIO (id_usuario),
    FOREIGN KEY (TURMA_id_turma) REFERENCES TURMA (id_turma)
    );"""),

'RECIBO_MD' :(
    """CREATE TABLE RECIBO_MD (
    FK_MATERIAL_DIDATICO_id_md INTEGER,
    FK_INSCRICAO_id_inscricao INTEGER,
    desconto_md FLOAT,
    id_recibo_md INTEGER PRIMARY KEY
);
"""),

'RECIBO' :(
    """CREATE TABLE RECIBO (
    FK_RESPONSAVEL_id_responsavel INTEGER,
    FK_MENSALIDADE_id_mensalidade INTEGER,
    id_recibo INTEGER PRIMARY KEY,
    data DATE,
    desc_recibo VARCHAR(255)
);"""),


}

inserts = {
    'CURSO': (
        """insert into CURSO (id_curso, nome_curso, faixa_etaria, nivel, valor_curso) VALUES
    (1, 'Paddy The Jelly 1', '3 a 5 anos', 'Básico para Crianças', 200.00),
    (2, 'Paddy The Jelly 2', '3 a 5 anos', 'Básico para Crianças', 200.00),
    (3, 'Green House 1', '6 a 8 anos', 'Básico para Crianças', 250.00),
    (4, 'Green House 2', '6 a 8 anos', 'Básico para Crianças', 250.00),
    (5, 'Magic Links 1', '9 e 10 anos', 'Básico para Crianças', 230.00),
    (6, 'Magic Links 2', '9 e 10 anos', 'Básico para Crianças', 230.00),
    (7, 'YTEEN 1', '11 a 14 anos', 'Pré intermediário', 220.00),
    (8, 'YTEEN 2', '11 a 14 anos', 'Pré intermediário', 220.00),
    (9, 'YTEEN 3', '11 a 14 anos', 'Pré intermediário', 220.00),
    (10, 'YTEEN 4', '11 a 14 anos', 'Pré intermediário', 220.00),
    (11, 'Discover the New', 'A partir de 15 anos', 'A1', 210.00),
    (12, 'Move your Life', 'A partir de 15 anos', 'A2', 215.00),
    (13, 'Make your Point', 'A partir de 15 anos', 'B1 E B2', 220.00);"""
    ),

    'RESPONSAVEL': (
        """insert into RESPONSAVEL (forma_pagamento, validade_cartao, vinculo, nome_responsavel, email_responsavel, fone_responsavel, id_responsavel) values
    ('Crédito 10 parcelas', '2025-04-01', 'Aluno', 'Hélio Faria Quintana', 'hqf@gmail.com', '(48) 9 9108-0609',1),
    ('Débito', '10-06-2027', 'Avó','Olívia Bittencourt', 'bittencourt@hotmail.com', '(48) 9 9100-0609',2),
    ('Crédito', '01-12-2027', 'Mãe', 'Eliane Barros Cordeiro', 'cordeiro@yahoo.com', '(48) 9 9166-4249',3),
    ('Crédito', '01-12-2029', 'Pai', 'Antônio Denis Fernandes Pai', 'denis@gmail.com', '(48) 9 9166-4849',4),
    ('Debito','01-12-2027','aluno','Gustavo Joaquim Barros Cordeiro','gustavojbc@yahoo.com','(48) 9 9166-4249',5),
    ('pix','25-03-2026', 'aluno','Antônio Denis Fernandes Filho','denis@gmail.com','(48) 9 9166-4849', 6),
    ('Crédito 10 parcelas','08-10-2029','aluno', 'Danilo Noah Souza', 'danilo.noah.souza@julietavinhas.fot.br','(48) 99614-6958', 7);"""
    ),

    'MATERIAL_DIDATICO': (
        """insert into MATERIAL_DIDATICO (id_md , qtd_md , valor_md , acessorios , CURSO_id_curso ) values
    (1, 5, 110.00, 'Mochila e magic pen', 1),
    (2, 4, 110.00, 'Mochila e magic pen', 2),
    (3, 4, 120.00, 'Mochila e magic pen', 3),
    (4, 6, 120.00, 'Mochila e magic pen', 4),
    (5, 2, 120.00, 'Mochila e magic pen', 5),
    (6, 1, 120.00, 'Mochila e magic pen', 6),
    (7, 4, 150.00, 'Mochila', 7),
    (8, 1, 150.00, 'Mochila', 8),
    (9, 3, 150.00, 'Mochila', 9),
    (10, 2, 150.00, 'Mochila', 10),
    (11, 5, 200.00, 'Mochila', 11),
    (12, 1, 200.00, 'Mochila', 12),
    (13, 2, 200.00, 'Mochila', 13);"""
    ),

    'TURMA': (
        """insert into TURMA(id_turma, horario, sala, dias_semana, curso_id_curso) values
    (1,'13:00', 'B','Seg/Qua',8 ),
    (2,'17:00', 'A','Seg/Qua',10),
    (3,'18:00', 'C','Ter/Qui',11),
    (4,'08:00', 'B', 'Ter/Qui',12);"""
    ),

    'CAMPANHA': (
        """insert into CAMPANHA(id_campanha, data_campanha) values
    (1, '06-09-2022'),
    (2, '10-07-2023'),
    (3, '20-11-2023');"""
    ),

        'USUARIO':(
             """insert into USUARIO(nome_usuario, id_usuario, email_usuario, fone_usuario, salario, especializacao, funcao, usuario_tipo) values
        ('Eloá Kamilly da Mota', 1, 'hqf@gmail.com', '(48) 9 9108-0609', 5000.00, 'professor', 'professor', 1),
        ('Igor Miguel Lorenzo Assunção', 2, 'ibis@hotmail.com', '(48) 9 9166-0609', 4500.00, 'administração', 'gerente', 2),
        ('Yuri Fábio Yuri Assis', 3, 'rbc@gmail.com', '(48) 9 9166-0049', 6000.00, 'consultor', 'vendedor', 3),
        ('Breno Yuri Lima', 4, 'gustavojbc@yahoo.com', '(48) 9 9166-4249', 7000.00, 'consultor', 'vendedor', 3),
        ('Thomas Benjamin Ian Teixeira', 5, 'denis@gmail.com', '(48) 9 9166-4849', 5500.00, 'professor', 'professor', 1);"""
        ),

        'ALUNO': ("""insert into ALUNO (id_conta, nome,  telefone, email, ativo, idade, FK_TURMA_id_turma, FK_RESPONSAVEL_id_responsavel ,aluno_responsavel, fk_inscricao_id_inscricao) values
        (1,'Hélio Faria Quintana','(48) 9 9108-0609','hqf@gmail.com',True,56, 3,1,True,1),
        (2,'Ísis Bittencourt','(48) 9 9166-0609','ibis@hotmail.com',True,13, 2,2,False,2 ),
        (3,'Rafaela Barros Cordeiro','(48) 9 9166-0049','rbc@gmail.com',True,17,2,3,False,3),
        (4,'Gustavo Joaquim Barros Cordeiro','(48) 9 9166-4249','gustavojbc@yahoo.com',True,31,1,5,False,3),
        (5,'Antônio Denis Fernandes Filho','(48) 9 9166-4849','denis@gmail.com', True,22,1,4,False,4),
        (6, 'Danilo Noah Souza', '(48) 99614-6958','danilo.noah.souza@julietavinhas.fot.br', True,22,2,7,True,5),
        (7,'Eloá Alessandra Nogueira','(48) 99262-1496','eloa-nogueira91@ruizonline.com.br', False,25,2,6,True,6),
        (8,'Luiz Mário Martins','(48) 99937-2056','luiz_mario_martins@gmail.com.br', True,12,1,7,False,7),
        (9,'Luiz Pietro Martins','(48) 99937-2056','luiz_pietro_martins@gmail.com.br',True,12,1,7,False,7),
        (10,'Josefa Isabelle Barbosa','(48) 98375-9223','josefa_isabelle_barbosa@credendio.com.br',False,46,3,5,True,8);
        """

    ),
        'MENSALIDADE':(
            """insert into MENSALIDADE(id_mensalidade, valor_total, curso_id_curso) values
            (1, 300.00, 8),
            (2, 500.50, 10),
            (3, 555.75, 11),
            (4, 790.25, 12);
            """
        ),

        'LEAD': ("""
    insert into LEAD (id_lead , nome_lead , telefone_lead ,  email_lead , status_lead, idade, fk_campanha_id_campanha) values

        (1,'Hélio Faria Quintana','(48) 9 9108-0609','hqf@gmail.com','Convertido',56,1),
        (2,'Ísis Bittencourt','(48) 9 9166-0609','ibis@hotmail.com','Convertido',13,1),
        (3,'Eliane Barros Cordeiro','(48) 9 9166-4249','cordeiro@yahoo.com','Convertido',11,1),
        (4,'Antônio Denis Fernandes', '(48) 9 9166-4849','denis@gmail.com', 'Convertido',12,1),
        (5,'Melissa Patrícia Figueiredo','(81) 98785-3071','melissa_patricia_figueiredo@yahoo.com.br','Recontatar',13,  1),
        (6,'Sophia Daniela Manuela Rezende','(81) 98785-3071','Sophia@digitalsj.com.br','Interessado', 42, 1),
        (7,'Antônio Denis Fernandes Filho','(48) 9 9166-4849','denis@gmail.com', 'Convertido',12,1),
        (8,'Renato Márcio Vicente Silveira','(48) 98278-0650','renato.marcio.silveira@lctour.com.br','Perdido',19,1),
        (9,'Danilo Noah Souza', '(48) 99614-6958','danilo.noah.souza@julietavinhas.fot.br','Convertido',22,1),
        (10,'Cauê Manuel Aragão','(48) 98214-7369','caue_aragao@yahoo.com.br','Recontatar',17,1),
        (11,'Anderson Jorge Martins','(48) 99553-1082','anderson.jorge.martins@facebook.com.br','Interessado',64,1),
        (12,'Eloá Alessandra Nogueira','(48) 99262-1496','eloa-nogueira91@ruizonline.com.br','Convertido',25,1),
        (13,'Aline Martins','(48) 99937-2056','alinemartins@julietavinhas.fot.br','Convertido',12,1),
        (14,'Lucas Márcio Yago Monteiro','(48) 98920-1542','lucas.marcio.monteiro@technicolor.com','Aguardando Agendamento',34,1),
        (15,'Josefa Isabelle Barbosa','(48) 98375-9223','josefa_isabelle_barbosa@credendio.com.br','Convertido',46,1),
        (16,'John Doe', '(48) 99937-2056', 'john.doe@example.com','Convertido',15,2);
        """),

        'INSCRICAO':("""  insert into INSCRICAO (id_inscricao  , FK_LEAD_id_lead  , FK_USUARIO_id_usuario) values
            (1,1,3),
            (2,2,3),
            (3,3,3),
            (4,3,4),
            (5,7,4),
            (6,9,3),
            (7,12,4),
            (8,13,4),
            (9,13,4),
            (10,15,4);
                     """),

        'PROFESSOR_TURMA':("""
            insert into PROFESSOR_TURMA (usuario_id_usuario, turma_id_turma, id_professor, monitor) values
            (1,1,1, True),
		   (1,2,2,False),
		   (5,3,3,False),
		   (5,4,4,True);"""),
        
        'RECIBO_MD': ("""
            insert into RECIBO_MD (fk_material_didatico_id_md, fk_inscricao_id_inscricao, desconto_md, id_recibo_md) values
                    (11, 3, 0, 1),
		            (10, 2, 0,2),
		            (8, 1, 0 , 3),
		            (7, 2,0,4),
		            (2,3,0,5),
		            (5,2,0,6),
		            (8,3,0,7);
                      """),
        'RECIBO':("""
            insert into RECIBO (fk_responsavel_id_responsavel, fk_mensalidade_id_mensalidade, id_recibo, data, desc_recibo) values
                (5,3,1,'10-10-2024','pago em dia'),
			    (6,2,2,'05-11-2024', 'pago em dia'),
			    (5,3,3,'12-11-2024', 'pago com 2 dias de atraso'),
			    (1,1,4,'15-11-2024', 'pago em dia'),
			    (2,4,5,'15-11-2024', 'pago em dia'),
			    (4,3,6,'16-11-2024',' pago com 1 dia de atraso'),
                (5,3,7,'20-11-2024', 'pago em dia'),
                (4,3,8,'30-11-2024','pago em dia' ),
                (1,1,9,'01-12-2024','pago em dia');
                  """),

        'PLACEMENT_TEST':("""  insert into PLACEMENT_TEST(id_placement, score, descricao_placement, fk_lead_id_lead) values
                (1,7.2,null,1),
                (2,null,'Conversa com a Ísis e responsavel',2),
                (3,5.4,'Teste com Rafaela e possibilidade de matricula Gustavo',3),
                (4,6.4,'Colocar na turma com devido horario',9),
                (5,5.8,null,12),
                (6,8.0,'Apresenta bom domínio da linguagem, pode ser matriculada em turma avançada',15);
                          """)



}

drop = {
'RECIBO' : ('DROP TABLE IF EXISTS RECIBO;'),
'RECIBO_MD' : ('DROP TABLE IF EXISTS RECIBO_MD;'),
'MATERIAL_DIDATICO' : ('DROP TABLE IF EXISTS MATERIAL_DIDATICO;'),
'PROFESSOR_TURMA' : ('DROP TABLE IF EXISTS PROFESSOR_TURMA;'),
'TURMA' : ('DROP TABLE IF EXISTS TURMA;'),
'PLACEMENT_TEST' : ('DROP TABLE IF EXISTS PLACEMENT_TEST;'),
'MENSALIDADE' : ('DROP TABLE IF EXISTS MENSALIDADE;'),
'CAMPANHA' : ('DROP TABLE IF EXISTS CAMPANHA;'),
'USUARIO' : ('DROP TABLE IF EXISTS USUARIO;'),
'ALUNO' : ('DROP TABLE IF EXISTS ALUNO;'),
'LEAD' : ('DROP TABLE IF EXISTS LEAD;'),
'INSCRICAO' :(' DROP TABLE IF EXISTS INSCRICAO;'),
'CURSO': ('DROP TABLE IF EXISTS CURSO;'),
'RESPONSAVEL' : ('DROP TABLE IF EXISTS RESPONSAVEL;'),
}

update = { 'RESPONSAVEL':
          ("""UPDATE RESPONSAVEL
          SET forma_pagamento = 'Boleto', validade_cartao = '2026-12-01', vinculo = 'Pai', nome_responsavel = 'New Name', email_responsavel = 'newemail@example.com', fone_responsavel = '(48) 9 9123-4567'
          WHERE id_responsavel = 1"""),

          'USUARIO':
          ("""UPDATE USUARIO
          SET nome_usuario = 'New User Name', email_usuario = 'newuser@example.com', fone_usuario = '(48) 9 9876-5432', salario = 6000.00, especializacao = 'Senior Instructor', funcao = null, USUARIO_TIPO = 2
          WHERE id_usuario = 1"""),

          'ALUNO':
          ("""UPDATE ALUNO
          SET nome = 'New Student Name', telefone = '(48) 9 8765-4321', email = 'newstudent@example.com', ativo = False, idade = 12, FK_TURMA_id_turma = 2, FK_RESPONSAVEL_id_responsavel = 2, aluno_responsavel = False, FK_INSCRICAO_id_inscricao = 2
          WHERE id_conta = 1"""),
           

}

delete = {
    'INSCRICAO':
    ("""DELETE FROM INSCRICAO
    WHERE id_inscricao = 1 """),

    'LEAD':
    ("""DELETE FROM LEAD 
     WHERE id_lead = 1 """)
}

def conecta_banco():
    try:
        connection_params = {
            'host': 'localhost',
            'database': 'TrabalhoFinal',
            'user': 'postgres',
            'password': 'ramos3001',
            'port':'5432',
        }

        cnx = psycopg2.connect(**connection_params)

        if cnx:
            print("Connected to the PostgreSQL database.")

            with cnx.cursor() as cursor:
                cursor.execute("SELECT version();")
                db_info = cursor.fetchone()
                print("PostgreSQL database version:", db_info)

    except Exception as e:
        print("Error: Unable to connect to the PostgreSQL database.")
        print(e)
        cnx = None

    return cnx

def drop_all_tables(connect):
    print("\n---DROP DB---")
    # Esvazia o Banco de Dados
    cursor = connect.cursor()
    for drop_name in drop:
        drop_description = drop[drop_name]
        try:
            print("Deletando {}: ".format(drop_name), end='')
            cursor.execute(drop_description)
        except (Exception, psycopg2.Error) as err:
            print(err)
        else:
            print("OK")
    connect.commit()
    cursor.close()
    

def create_all_tables(connect):
        print("\n---CREATE ALL TABLES---")
        # Criação das tabelas
        cursor = connect.cursor()
        for table_name in tables:
            table_description = tables[table_name]
            try:
                print("Criando tabela {}: ".format(table_name), end='')
                cursor.execute(table_description)
            except (Exception, psycopg2.Error) as err:
                if err.errno == err.ER_TABLE_EXISTS_ERROR:
                    print("Tabela já existe.")
                else:
                    print(err.msg)
            else:
                print("OK")
        connect.commit()
        cursor.close()
    
def show_table(connect):
    print("\n---SELECIONAR TABELA---")
    # Criação das tabelas
    cursor = connect.cursor()
    for table_name in tables:
        print("Nome: {}".format(table_name))
    try:
        name = input(str("\nDigite o nome da tabela que deseja consultar. ")).upper()
        select = "select * from " + name
        cursor.execute(select)
    except (Exception, psycopg2.Error) as err:

        print(err.msg)
    else:
        print("TABELA {}".format(name))
        myresult = cursor.fetchall()
        for x in myresult:
            print(x)
    cursor.close()
    
def update_value(connect):
    print("\n---SELECIONAR TABELA PARA ATUALIZAÇÃO---")
    # Criação das tabelas
    cursor = connect.cursor()
    for table_name in tables:
        print("Nome: {}".format(table_name))
    try:
        name = input(str("\nDigite o nome da tabela que deseja consultar. ")).upper()
        for table_name in tables:
            table_description = tables[table_name]
            if table_name == name:
                print("Para criar a tabela: {}, foi utilizado o seguinte código {}".format(table_name,
                                                                                           table_description))
        atributo = input("Digite o atributo a ser alterado: ")
        valor = input("Digite o valor a ser atribuido: ")
        codigo_f = input("Digite a variavel primaria: ")
        codigo = input("Digite o codigo numerico: ")
        query = ['UPDATE ', name, ' SET ', atributo, ' = ', valor, ' WHERE ', codigo_f, '= ', codigo]
        sql = ''.join(query)
        cursor.execute(sql)
    except (Exception, psycopg2.Error) as err:

        print(err.msg)
    else:
        print("Atributo atualizado")
    connect.commit()
    cursor.close()
    
def insert_test(connect):
    print("\n---INSERT TEST---")
    # Inserção dos valores nas tabelas
    cursor = connect.cursor()
    for insert_name in inserts:
        insert_description = inserts[insert_name]
        try:
            print("Inserindo valores para {}: ".format(insert_name), end='')
            cursor.execute(insert_description)
        except (Exception, psycopg2.Error) as err:
            print(err)
            
        else:
            print("OK")
    connect.commit()
    cursor.close()
    
def update_test(connect):
    print("\n---UPDATE TEST---")
    # Inesrsão dos valores nas tabelas
    cursor = connect.cursor()
    for update_name in update:
        update_description = update[update_name]
        try:
            print("Teste de atualização de valores para {}: ".format(update_name), end='')
            cursor.execute(update_description)
        except psycopg2.connector.Error as err:
            print(err.msg)
        else:
            print("OK")
    connect.commit()
    cursor.close()
    


def delete_test(connect):
    print("\n---DELETE TEST---")
    # Inesrsão dos valores nas tabelas
    cursor = connect.cursor()
    for delete_name in delete:
        delete_description = delete[delete_name]
        try:
            print("Teste de atualização de valores para {}: ".format(delete_name), end='')
            cursor.execute(delete_description)
        except (Exception, psycopg2.Error) as err:
            print(err)
        else:
            print("OK")
    connect.commit()
    cursor.close()
    
def consulta1(connect):
    select_query = """
    SELECT
    LEAD.id_lead,
    LEAD.nome_lead,
    LEAD.telefone_lead,
    LEAD.email_lead,
    USUARIO.nome_usuario AS nome_consultor,
    CAMPANHA.id_campanha
    FROM LEAD
    JOIN INSCRICAO ON LEAD.id_lead = INSCRICAO.FK_LEAD_id_lead
    JOIN USUARIO ON INSCRICAO.FK_USUARIO_id_usuario = USUARIO.id_usuario
    LEFT JOIN CAMPANHA ON LEAD.FK_CAMPANHA_id_campanha = CAMPANHA.id_campanha
    ORDER BY LEAD.nome_lead
    """
    print("\nPrimeira Consulta: Encontrar todos os leads coletados que se tornaram clientes e realizaram sua inscrição apresentando o nome do consultor e o número da campanha")
    cursor = connect.cursor()
    cursor.execute(select_query)
    myresult = cursor.fetchall()
    for x in myresult:
        print(x)
        
def consulta2(connect):
    select_query = """
   SELECT
    RESPONSAVEL.nome_responsavel,
    CURSO.nome_curso,
    COUNT(RECIBO.id_recibo) AS total_pagamentos
FROM RECIBO
JOIN RESPONSAVEL ON RECIBO.FK_RESPONSAVEL_id_responsavel = RESPONSAVEL.id_responsavel
JOIN MENSALIDADE ON RECIBO.FK_MENSALIDADE_id_mensalidade = MENSALIDADE.id_mensalidade
JOIN CURSO ON MENSALIDADE.CURSO_id_curso = CURSO.id_curso
GROUP BY RESPONSAVEL.nome_responsavel, CURSO.nome_curso;

    """
    print("\nSegunda Consulta: Selecionar quantos pagamentos de mensalidade cada responsável realizou e o total que foi pago, além de mostrar a última data que o último pagamento foi realizado")
    cursor = connect.cursor()
    cursor.execute(select_query)
    myresult = cursor.fetchall()
    for x in myresult:
        print(x)
        
def consulta3(connect):
    select_query = """
 SELECT
    ALUNO.nome AS nome_aluno,
    CURSO.nome_curso,
    AVG(PLACEMENT_TEST.score) AS media_score
FROM ALUNO
JOIN TURMA ON ALUNO.FK_TURMA_id_turma = TURMA.id_turma
JOIN CURSO ON TURMA.CURSO_id_curso = CURSO.id_curso
LEFT JOIN PLACEMENT_TEST ON ALUNO.id_conta = PLACEMENT_TEST.FK_LEAD_id_lead
WHERE PLACEMENT_TEST.score IS NOT NULL
GROUP BY ALUNO.nome, CURSO.nome_curso;


    """
    print("\nTerceira Consulta: Os alunos que ainda não retiraram seu material didático")
    cursor = connect.cursor()
    cursor.execute(select_query)
    myresult = cursor.fetchall()
    for x in myresult:
        print(x)
        
def exit_db(connect):
    print("\n---EXIT DB---")
    connect.close()
    print("Conexão ao MySQL foi encerrada")

def crud_resgatocao(connect):
    drop_all_tables(connect)
    create_all_tables(connect)
    insert_test(connect)

    print("\n---CONSULTAS BEFORE---")
    consulta1(connect)
    consulta2(connect)
    consulta3(connect)


    update_test(connect)
    delete_test(connect)

    print("\n---CONSULTAS AFTER---")
    consulta1(connect)
    consulta2(connect)
    consulta3(connect)
    
try:
    # Estabelece Conexão com o DB
    con = conecta_banco()

    power_up = 1
    while power_up == 1:
        interface = """\n       ---MENU---
        1.  CRUD 
        2.  Criar
        3.  Inserir valores
        4.  Update
        5.  Delete
        6.  CONSULTA 01
        7.  CONSULTA 02
        8.  CONSULTA 03
        9.  Show Table
        10. Update Value
        11. CLEAR ALL 
        0.  Disconnect DB\n """
        print(interface)

        choice = int(input("Opção: "))
        if choice < 0 or choice > 12:
            print("Erro tente novamente")
            choice = int(input())

        if choice == 0:
            if con.is_connected():
                exit_db(con)
                print("Muito obrigado.")
                break
            else:
                break

        if choice == 1:
            crud_resgatocao(con)

        if choice == 2:
            create_all_tables(con)

        if choice == 3:
            insert_test(con)

        if choice == 4:
            update_test(con)

        if choice == 5:
            delete_test(con)

        if choice == 6:
            consulta1(con)

        if choice == 7:
            consulta2(con)

        if choice == 8:
            consulta3(con)

        if choice == 9:
            show_table(con)

        if choice == 10:
            update_value(con)

        if choice == 11:
            drop_all_tables(con)

except (Exception, psycopg2.Error) as error:
    print("Erro na conexão com o PostgreSQL:", error)
    

    
    