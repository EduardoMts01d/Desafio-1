import mysql.connector
from mysql.connector import Error
cont = 0
prof=[]
alunos = []
soma = 0
Talunos = 0
#mostrar a quantidade de alunos
#mostrar a teachingability
#mostrar o total de cursos


try:
    con = mysql.connector.connect(host='relational.fit.cvut.cz',database='university',user='guest',password='relational',port='3306') #conexão com o banco de dados 

    #consulta na tabela professores 
    consulta_prof = "select * from prof" 
    cursor = con.cursor()
    cursor.execute(consulta_prof) #executa o comando informado na var consulta_prof
    linhas = cursor.fetchall() #percorre todas as linhas 
    
    print("\nMostrando")
    for coluna in linhas:  
        print("Id_Professor: ", coluna[0]) #printa o primeiro professor 
        prof.append(coluna[0]) #armazena dentro do professor 
        
        for i in prof: #para cada professor do primeiro até o ultimo
            consulta_RA = "select student_id from RA where prof_id = " + str(i) #consulta a tabela RA e passa o id por cada elemento do vetor prof   
            cursor = con.cursor()
            cursor.execute(consulta_RA)#executa o comando informado na var consulta_RA
            linhasR = cursor.fetchall()#percorre todas as linhas da tabela  
            Talunos += cursor.rowcount # conta quanto alunos cada professor tem por meio de quantas linhas a tabela tem.
            
            for j in linhasR: #para cada aluno do primeiro até o ultimo
                consulta_cursos = "select course_id from registration where student_id = " + str(j[0]) #consulta a tabela registration e passa o id por cada elemento que é _  
                # o conteúdo de cada linha. da tabela RA consultada pelo id de cada professor 
                
                cursor = con.cursor()
                cursor.execute(consulta_cursos) #executa o comando 
                colunass = cursor.fetchall()
                soma += cursor.rowcount #conta a quantidade de cursos por cada aluno, ou seja, através do id de cada aluno na tabela registration. 
       
        print("teachingability:",coluna[2])
        print("Alunos: ",Talunos)
        print("Número total de cursos: ", soma)
        soma = 0 #soma é a contagem de cursos por cada aluno 
           
        coluna = 0 #coluna é o id de cada professor por isso tenho que zerar. 
        print("\nPox Prof \n\n")

except Error as e:
    print("Erro ao acessar tabela MySQL",e)

finally:
    if (con.is_connected()):
        con.close()
        cursor.close()
        print("Conexão ao MySQL encerrada")
#nova conexão
#con = mysql.connector.connect(host='relational.fit.cvut.cz',database='university',user='guest',password='relational',port='3306')
#CRIA TABELA
#comando= """
#CREATE TABLE resultado(
#prof_id int(4) AUTO_INCREMENT,
#student_id int NOT NULL,
#teachingability int,
#PRIMARY KEY (prof_id)
#);
#"""

#cursor = con.cursor()
#cursor.execute(consulta_prof)
#con.commit()
    
