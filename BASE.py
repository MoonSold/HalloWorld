from sqlite3 import *

MY_BASE = connect("ALL_USERS_PASSWORD.db")

CURSOR = MY_BASE.cursor()

LIST = []


while True:

	print("Если хотите выйти нажмиите ENTER при пустом вводе")

	INP = input("Введите имя, пароль и мэйл(через запятую): ")

	PERSON = INP.split(",")

	if len(PERSON) == 3 and len(PERSON[0].split(" ")) == 3 and "@" in PERSON[2]:
		LIST.append(PERSON)

	elif INP == "":
		break



R = LIST.pop()

R = None




try:
	CURSOR.execute("""CREATE TABLE users(SNP TEXT,PASSWORD TEXT,MAIL TEXT)""")

	for PER in LIST:
		CURSOR.execute("""INSERT INTO users (SNP,PASSWORD,MAIL) VALUES (?,?,? )""",PER)

except:
	print("\t\t\t\tБАЗА ДАННЫХ УЖЕ СУЩЕСТВУЕТ\t\t\t\t")


MY_BASE.commit()
MY_BASE.close()
