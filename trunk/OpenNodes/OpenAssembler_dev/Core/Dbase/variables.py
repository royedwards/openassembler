# #####################################################################################
#
#  OpenAssembler V3
#  Owner: Laszlo Mates
#  Email: laszlo.mates@gmail.com
#  Date: 2009.06.08
#
# #####################################################################################

class oas_variablechecker:

	def oas_variable(self,variabletype,value):
		if len(value)==0:
			return value
		if str(value)[0]=="=" or str(value)[0]=="$":
			value=value
		elif variabletype.find("vector")>-1 or variabletype.find("point")>-1 or variabletype.find("color")>-1:
			if len(value.split())>1:
				value=str(value.split()[0])+","+str(value.split()[1])+","+str(value.split()[2])
			elif len(value.split(","))>1:
				value=str(value.split(",")[0])+","+str(value.split(",")[1])+","+str(value.split(",")[2])
			else:
				value="0;0;0"					
		elif variabletype.find("matrix")>-1:
			if len(value.split())>1:
				value=str(value.split(" ")[0])+","+str(value.split(" ")[1])+","+str(value.split(" ")[2])+","+str(value.split(" ")[3])+","+str(value.split(" ")[4])+","+str(value.split(" ")[5])+","+str(value.split(" ")[6])+","+str(value.split(" ")[7])+","+str(value.split(" ")[8])+","+str(value.split(" ")[9])+","+str(value.split(" ")[10])+","+str(value.split(" ")[11])+","+str(value.split(" ")[12])+","+str(value.split(" ")[13])+","+str(value.split(" ")[14])+","+str(value.split(" ")[15])
			elif len(value.split(","))>1:
				value=str(value.split(",")[0])+","+str(value.split(",")[1])+","+str(value.split(",")[2])+","+str(value.split(",")[3])+","+str(value.split(",")[4])+","+str(value.split(",")[5])+","+str(value.split(",")[6])+","+str(value.split(",")[7])+","+str(value.split(",")[8])+","+str(value.split(",")[9])+","+str(value.split(",")[10])+","+str(value.split(",")[11])+","+str(value.split(",")[12])+","+str(value.split(",")[13])+","+str(value.split(",")[14])+","+str(value.split(",")[15])
			elif len(value.split("_"))>1:
				value=str(value.split("_")[0])+","+str(value.split("_")[1])+","+str(value.split("_")[2])+","+str(value.split("_")[3])+","+str(value.split("_")[4])+","+str(value.split("_")[5])+","+str(value.split("_")[6])+","+str(value.split("_")[7])+","+str(value.split("_")[8])+","+str(value.split("_")[9])+","+str(value.split("_")[10])+","+str(value.split("_")[11])+","+str(value.split("_")[12])+","+str(value.split("_")[13])+","+str(value.split("_")[14])+","+str(value.split("_")[15])
			else:
				value="0;0;0;0;0;0;0;0;0;0;0;0;0;0;0;0"
		elif variabletype.find("int")>-1:
			try:
				value=int(value)
			except:
				value=0
		elif variabletype.find("float")>-1 or variabletype.find("bool")>-1:
			try:
				value=float(value)
			except:
				value=0	
		else:
			pass
		return value
