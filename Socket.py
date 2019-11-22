from socket import *
from sqlite3 import *




class SOCKET():

	global MY_BASE
	MY_BASE = connect("ALL_USERS_PASSWORD.db")

	global CURSOR
	CURSOR = MY_BASE.cursor()



	def __init__(self):

		global CHANGE

		CHANGE = False

		global reqest

		reqest = None

		def BEGIN():

			file_BEGIN = open(r"C:\Users\bkv\Desktop\WEB\BEGIN.html","r",encoding="UTF8")

			BEGIN = file_BEGIN.read()

			file_BEGIN.close()

			return BEGIN



		def ADD_NEW_USERS(CHANGE,reqest):

			if CHANGE == True:

				ALL_INF = []

				L = reqest.decode("utf-8").split("\n")

				for i in L:
					i = i.split("&")
					ALL_INF.append(i)

				L = None

				ALL_INF.reverse()

				try:

					FIO = ALL_INF[0][0].split("=")[1]
					PAS = ALL_INF[0][1].split("=")[1]
					MAIL = ALL_INF[0][2].split("=")[1]

					if len(FIO.split(" ")) == 3 and "@" in MAIL and PAS != "":

						CURSOR.execute("""INSERT INTO users (SNP,PASSWORD,MAIL) VALUES (?,?,? )""",(FIO,PAS,MAIL))
						MY_BASE.commit()
						ADD = None
						ALL_INF = None

				except:

					ALL_INF = None


		def NEW_USERS():

			file_reqest = open(r"C:\Users\bkv\Desktop\WEB\REQ.html","r",encoding="UTF8")

			REQ = file_reqest.read()

			file_reqest.close()

			return REQ



		def CREATING_TABLE():

			file_table = open(r"C:\Users\bkv\Desktop\WEB\TABLE.html","r",encoding="UTF8")

			TABLE = file_table.read()

			file_table.close()

			LIST_OF_USERS = []

			STR = ""
			DATA_USERS = CURSOR.execute("""SELECT * FROM users""")

			for data in DATA_USERS:
				LIST_OF_USERS.append(data)

			for FIO_PASS_EMAIL in LIST_OF_USERS:
				FIO,PASSWORD,MAIL = FIO_PASS_EMAIL
				STR = STR + "<tr><td>" + str(FIO) + "</td><td>" + str(PASSWORD) + "</td><td>" + str(MAIL) + "</td></tr>\n"

			BUTTON =  """

			<button onclick="window.location='http://localhost:5000/new_users'">ДОБАВИТЬ НОВЫХ ПОЛЬЗОВАТЕЛЕЙ</button>

			"""

			TABLE = TABLE + STR + "</table>\n\n" + BUTTON  + "</body>" "</html>"

			return TABLE




		MY_SOCKET = socket(AF_INET,SOCK_STREAM)
		MY_SOCKET.bind(("localhost",5000))
		MY_SOCKET.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
		MY_SOCKET.listen()
		print("\t\t\t\tВЫ ПОДНЯЛИ СЕРВАК\t\t\t\t")

		while True:
			try:
				client_socket,adress = MY_SOCKET.accept()

				reqest = client_socket.recv(1024)

				ALL = reqest.decode("utf-8").split(" ")



				if ALL[1] == "/users":

					ADD_NEW_USERS(CHANGE,reqest)

					CHANGE = False

					TABLE = CREATING_TABLE()

					client_socket.sendall(("HTTP/1.1 200 OK\n\n" + TABLE).encode())



				elif ALL[1] == "/new_users":

					REQ = NEW_USERS()

					client_socket.sendall(("HTTP/1.1 200 OK\n\n" + REQ).encode())

					CHANGE = True

				else:

					MAIN = BEGIN()
					client_socket.sendall(("HTTP/1.1 200 OK\n\n" + MAIN).encode())

					client_socket.close()

			except:
				pass


		MY_BASE.close()



SERV = SOCKET()
