from socket import * 





MY_SOCKET = socket(AF_INET,SOCK_STREAM) 
MY_SOCKET.bind(("localhost",5000))
MY_SOCKET.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
MY_SOCKET.listen() 

while True: 
			

	client_socket,adress = MY_SOCKET.accept() 
	client_socket.sendall(("HTTP/1.1 200 OK\n\n" + "<h1>Hallo World</h1>").encode()) 
	client_socket.close()  
