# #####################################################################################
#
#  OpenAssembler V3
#  Owner: Laszlo Mates
#  Email: laszlo.mates@gmail.com
#  Date: 2009.06.04
#
# #####################################################################################

from PyQt4 import QtCore, QtGui
from Core.Gateway.Gateway import oas_gateway

import os,sys

class timelineMain():
	def timeline_start(self):
		range=self.oas_show(mode="silent",showtype="framerange")
		self.oas_sframe_spin.setValue(int(range[0]))
		self.oas_eframe_spin.setValue(int(range[1]))
		self.oas_time_slider.setMinimum(int(range[0]))
		self.oas_time_slider.setMaximum(int(range[1]))
		frame=self.oas_show(mode="silent",showtype="frame")
		self.oas_cframe_spin.setValue(int(frame[0]))
		self.oas_time_slider.setValue(int(frame[0]))

	def setFramerange(self):
		ret=self.oas_framerange(mode="silent",firstframe=int(self.oas_sframe_spin.value()),endframe=int(self.oas_eframe_spin.value()))
		self.timeline_start()

	def setFrame(self):
		ret=self.oas_frame(mode="silent",frame=int(self.oas_cframe_spin.value()))
		self.timeline_start()

	def setToFirstFrame(self):
		self.oas_frame(mode="silent",frame=int(self.oas_sframe_spin.value()))
		self.timeline_start()

	def setToLastFrame(self):
		self.oas_frame(mode="silent",frame=int(self.oas_eframe_spin.value()))
		self.timeline_start()
