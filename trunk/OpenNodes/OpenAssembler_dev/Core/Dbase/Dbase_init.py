# #####################################################################################
#
#  OpenAssembler V3
#  Owner: Laszlo Mates
#  Email: laszlo.mates@gmail.com
#  Date: 2009.06.08
#
# #####################################################################################

from Core.Startup.Setup import oas_setup
import sys, os

class dBase_Init(oas_setup):
	def dBase_builder(self):
		self.oas_rt={}
		self.oas_rt_connections={}
		self.oas_scene_setup={'startframe': 100,'frame':100,'endframe':200,'endnode':""}
		self.oas_save_filename=""
		self.oas_variablecategory={}
		self.oas_last_node_created=""
		self.setup_contents=self.oas_load_setup()
		self.manualPath=self.manuPath(self.setup_contents)
		self.oas_node_list=self.oas_collect_nodes_from_dirs(self.oas_collect_node_dirs(self.oas_load_setup()))
		self.oas_menucategories=self.oas_menucategory_settings(self.oas_load_setup())

	def reloadMenucats(self):
		self.setup_contents=self.oas_load_setup()
		self.manualPath=self.manuPath(self.setup_contents)
		self.oas_node_list=self.oas_collect_nodes_from_dirs(self.oas_collect_node_dirs(self.oas_load_setup()))
		self.oas_menucategories=self.oas_menucategory_settings(self.oas_load_setup())		
