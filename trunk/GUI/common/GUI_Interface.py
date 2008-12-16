######################################################################################
#
#  OpenAssembler V2
#  Owner: Laszlo Mates
#  Email: laszlo.mates@gmail.com
#  Date: 2008.08.21
#
######################################################################################

from socket import *
import sys, time

class GUI_Interface_client:
	def oas_gui_interface_client(self,port,message):
		chk=1
		input_command=message
		errchk=1
		rec=""
		while errchk==1:
			try:
				
				chk_socket=socket(AF_INET, SOCK_STREAM)
				chk_socket.connect((gethostbyname(gethostname()),port))
				chk_socket.recv(2048)
				chk_socket.send(input_command)
				rec=chk_socket.recv(2048)
				errchk=0
			except:
				time.sleep(1)
				errchk=1		
		return rec
		
class GUI_Interface_server:
	def oas_gui_interface_server(self,port,llock):
		llock.acquire()
		oas_socket=socket(AF_INET, SOCK_STREAM)
		senddata="gui_server:"
		llock.release()
		local_ip=gethostbyname(gethostname())
		errchk=1
		while errchk==1:
			try:
				oas_socket.bind((local_ip,port))
				errchk=0
			except:
				time.sleep(1)
				errchk=1
		oas_socket.listen(1)
		e=True
		while e==True:
				(clientSocket, address) = oas_socket.accept()
				clientSocket.send("GUI_server-->")
				buff = clientSocket.recv(2048)
				if buff.strip() == "server halt":
			     		clientSocket.close()
					try:
						oas_socket.shutdown(2)
					except:
						pass
					e=False
				if buff.strip() == "chk":
					clientSocket.send("1")
					clientSocket.close()
				else:
					self.old_gui_do(buff)
					clientSocket.close()

