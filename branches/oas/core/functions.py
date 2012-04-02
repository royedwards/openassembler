import pickle

class core_functions:
	def save_object(self,object_to_write,path):
		file = open(path, 'w')
		pickle.dump(object_to_write, file)
		file.close()

	def load_object(self,path):
		file = open(path, 'r')
		object_to_load = pickle.load(file)
		file.close()
		return object_to_load

	def paste_network(self):
		pass
