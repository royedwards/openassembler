import pg

class oas_connect_to_postgresql:
	def run(self, host="",username="",password="",database=""):
		return pg.connect(dbname=str(database), user=str(username), host=str(host), passwd=str(password))		

class oas_disconnect_from_postgresql:
	def run(self, connection=None,pass_thrue=None):
		connection.close()
		return pass_thrue

class oas_postgresql_query:
	def run(self, connection=None,query=""):
		return connection.query(query).dictresult()		



