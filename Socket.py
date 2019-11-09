from socket import * 
from sqlite3 import *

MY_BASE = connect("ALL_USERS_PASSWORD.db") 
CURSOR = MY_BASE.cursor() 


LIST = []

NAME1 = CURSOR.execute("""SELECT * FROM users""")

for i in NAME1: 
	LIST.append(i) 




TABLE = "<table>\n" + "<style type=\"text/css\">\nTABLE {\nwidth: 100%;\nborder-collapse: collapse;\n}\nTD, TH {\npadding: 3px;\nborder: 1px solid black;\n}\nTH {\nbackground: Yellow;\n}\n</style>\n"+ "<tr><th>FIO</th><th>PASSWORD</th><th>MAIL</th></tr>\n"

for NPE in LIST: 
	
	FIO,MAIL,PASSWORD = NPE 

	STR = "<tr><td>" + str(FIO) + "</td><td>" + str(MAIL) + "</td><td>" + str(PASSWORD) + "</td></tr>\n"

	TABLE = TABLE + STR



TABLE = TABLE + "</table>"





MY_BASE.close()
MY_SOCKET = socket(AF_INET,SOCK_STREAM) 
MY_SOCKET.bind(("localhost",5000))
MY_SOCKET.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
MY_SOCKET.listen() 

while True: 
	client_socket,adress = MY_SOCKET.accept() 

	reqest = client_socket.recv(1024)

	ALL = reqest.decode("utf-8").split(" ") 
	try:
		if ALL[1] == "/users": 
			client_socket.sendall(("HTTP/1.1 200 OK\n\n" + TABLE).encode()) 

		else:
			client_socket.sendall(("HTTP/1.1 200 OK\n\n" + "<h1>HALLO WORLD</h1>").encode()) 
	
		client_socket.close()  
	
	except: 
		
		pass


