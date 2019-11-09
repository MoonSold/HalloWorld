from sqlite3 import *  

MY_BASE = connect("ALL_USERS_PASSWORD.db") 

CURSOR = MY_BASE.cursor()   

LIST = []

L = None

while L != "":
	
	NAMES = input("Введите имя, пароль и мэйл(через запятую): ") 
	print("Если хотите выйти нажмиите ENTER при пустом вводе")    
	PERSON = NAMES.split(",")  
	LIST.append(PERSON) 
	
	if NAMES == "":  
		
		L = ""

R = LIST.pop()
R = None

print(LIST)




CURSOR.execute("""CREATE TABLE users(SNP TEXT,PASSWORD TEXT,MAIL TEXT)""") 


for PER in LIST:
	CURSOR.execute("""INSERT INTO users (SNP,PASSWORD,MAIL) VALUES (?,?,? )""",PER)

 
print("Введено неправильно")


MY_BASE.commit() 
MY_BASE.close()