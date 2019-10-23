from socket import * 
from sqlite3 import *

MY_BASE = connect("ALL_BASE_PASSWORD.db") 
CURSOR = MY_BASE.cursor() 


LIST = []

NAME1 = CURSOR.execute("""SELECT * FROM base """)

for i in NAME1: 
	LIST.append(i) 



FIRST,SECOND,THIRD = LIST



NAME1,PASSWORD1,MAIL1 = FIRST
NAME2,PASSWORD2,MAIL2 = SECOND
NAME3,PASSWORD3,MAIL3 = THIRD


TABLE = "<table>\n" + "<style type=\"text/css\">\nTABLE {\nwidth: 100%;\nborder-collapse: collapse;\n}\nTD, TH {\npadding: 3px;\nborder: 1px solid black;\n}\nTH {\nbackground: Yellow;\n}\n</style>\n"+ "<tr><th>FIO</th><th>PASSWORD</th><th>MAIL</th></tr>""<tr><td>" + str(NAME1) + "</td><td>" + str(PASSWORD1) + "</td><td>" + str(MAIL1) + "</td></tr>\n" + "<tr><td>" + str(NAME2) + "</td><td>" + str(PASSWORD2) + "</td><td>" + str(MAIL2) + "</td></tr>\n" + "<tr><td>" + str(NAME3) + "</td><td>" + str(PASSWORD3) + "</td><td>" + str(MAIL3) + "</td></tr>\n" + "</table>"







MY_BASE..close()


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


