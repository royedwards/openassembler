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


class oas_broadcaster:
	def oas_Broadcast(self,port_list,message):
		for port in port_list:
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
		
