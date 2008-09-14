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
#from Console.Console import oas_console


class oas_client:
	def oas_remoteClient(self,port):
		chk=1
		
		while chk==1:
			input_command=raw_input ("OpenAssembler:").strip()
				
			if input_command=="exit":
				sys.exit(0)
				chk=0
			elif input_command=="server halt":
				chk_socket=socket(AF_INET, SOCK_STREAM)
				chk_socket.connect((gethostbyname(gethostname()),port))
				rec=chk_socket.send("server halt")
				chk=0
			elif input_command=="":
				pass
			else:
				errchk=1
				while errchk==1:
					try:
						
						chk_socket=socket(AF_INET, SOCK_STREAM)
						chk_socket.connect((gethostbyname(gethostname()),port))
						chk_socket.recv(2048)
						chk_socket.send(input_command)
						rec=chk_socket.recv(2048)
						print rec
						errchk=0
					except:
						time.sleep(1)
						errchk=1
				chk=1
