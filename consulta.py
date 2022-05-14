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
    con = mysql.connector.connect(host='relational.fit.cvut.cz',database='university',user='guest',password='relational',port='3306')

    consulta_prof = "select * from prof"
    cursor = con.cursor()
    cursor.execute(consulta_prof)
    linhas = cursor.fetchall()
    
    print("\nMostrando")
    for coluna in linhas:
        print("Id_Professor: ", coluna[0])
        prof.append(coluna[0])
        for i in prof:
            consulta_RA = "select student_id from RA where prof_id = " + str(i)  
            cursor = con.cursor()
            cursor.execute(consulta_RA)
            linhasR = cursor.fetchall()
            Talunos += cursor.rowcount
            for j in linhasR:
         
                consulta_cursos = "select course_id from registration where student_id = " + str(j[0])  
                cursor = con.cursor()
                cursor.execute(consulta_cursos)
                colunass = cursor.fetchall()
         
                soma += cursor.rowcount
       
        print("teachingability:",coluna[2])
        print("Alunos: ",Talunos)
        print("Número total de cursos: ", soma)
        soma = 0
           
        coluna = 0
        print("\nPox Prof \n\n")
#CRIA TABELA

except Error as e:
    print("Erro ao acessar tabela MySQL",e)

finally:
    if (con.is_connected()):
        con.close()
        cursor.close()
        print("Conexão ao MySQL encerrada")
con = mysql.connector.connect(host='relational.fit.cvut.cz',database='university',user='guest',password='relational',port='3306')

comando= """
CREATE TABLE resultado(
prof_id int(4) AUTO_INCREMENT,
student_id int NOT NULL,
teachingability int,
PRIMARY KEY (prof_id)
);
"""

cursor = con.cursor()
cursor.execute(consulta_prof)
con.commit()
    
