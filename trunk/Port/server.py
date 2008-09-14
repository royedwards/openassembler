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
from Console.Console import oas_console
import thread

######################################################################################
# this file is for the port communication
######################################################################################

class oas_server(oas_console):
	def oas_port_server(self,port,lock):
		lock.acquire()
		oas_socket=socket(AF_INET, SOCK_STREAM)
		senddata="oas_server:"
		local_ip=gethostbyname(gethostname())
		errchk=1
		while errchk==1:
			try:
				oas_socket.bind((local_ip,port))
				print "\nOpenAssembler Server started at "+str(local_ip)+":"+str(port)+" !"
				errchk=0
			except:
				time.sleep(1)
				errchk=1
		oas_socket.listen(1)
		lock.release()
		e=True
		while e==True:
				(clientSocket, address) = oas_socket.accept()
				clientSocket.send("OpenAssembler_server-->")
				buff = clientSocket.recv(2048)
				if buff.strip() == "server halt":
			     		print "OpenAssembler Server stopping......."
			     		clientSocket.close()
					oas_socket.shutdown(2)
					e=False
				else:
			     		ret=self.oas_Console(imput_to_parse=str(buff.strip()),mode="silent")
					clientSocket.send(str(ret))
			     		clientSocket.close()
					e=True



class oas_common_port_communication:
	def oas_server_halt(self,port):
		try:
			chk_socket=socket(AF_INET, SOCK_STREAM)
			chk_socket.connect((gethostbyname(gethostname()),port))
			chk_socket.send("server halt")
			chk_socket.close()
		except:
			pass
