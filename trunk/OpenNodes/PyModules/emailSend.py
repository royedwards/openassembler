###OpenAssembler Node python file###

'''
define
{
	name emailSend
	tags pymod
	input string send_from "" ""
	input array1D send_to "[]" ""
	input string subject "" ""
	input string text "" ""
	input array1D files "[]" ""
	input string server "localhost" ""
	output any result "" ""

}
'''

import smtplib
import os,sys
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email.Utils import COMMASPACE, formatdate
from email import Encoders

class emailSend():
	def emailSend_main(self, **connections):
		try:
			send_from=str(connections["send_from"])
		except:
			send_from=""
		try:
			send_to=connections["send_to"]
		except:
			send_to=[]
		try:
			subject=str(connections["subject"])
		except:
			subject=""
		try:
			text=str(connections["text"])
		except:
			text=""
		try:
			server=str(connections["server"])
		except:
			server=""		
		try:
			files=connections["files"]
		except:
			files=[]

		assert type(send_to)==list
		assert type(files)==list

		msg = MIMEMultipart()
		msg['From'] = send_from
		msg['To'] = COMMASPACE.join(send_to)
		msg['Date'] = formatdate(localtime=True)
		msg['Subject'] = subject

		msg.attach( MIMEText(text) )

		for f in files:
			part = MIMEBase('application', "octet-stream")
			part.set_payload( open(f,"rb").read() )
			Encoders.encode_base64(part)
			part.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(f))
			msg.attach(part)

		smtp = smtplib.SMTP(server)
		smtp.sendmail(send_from, send_to, msg.as_string())
		smtp.close()


if __name__ == "__main__":
	args=sys.argv[1:]
	emailSend().emailSend_main(send_from=args[0],send_to=[args[1]],subject=args[2], text="Render is ready please check your sequence!",server=args[3],files=[])

