import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
import time
from time import asctime


#gett radar library


 
fromaddr = 'equineVision@gmail.com'
toaddr = 'eugenio.parker3@gmail.com'
msg = MIMEMultipart()
msg['FROM'] = fromaddr
msg['TO'] = toaddr
msg['Subject'] = "Monitoring System"


#Radar distance message = radar_distance
msg.attach(MIMEText(message, 'plain'))


server = smtplib.SMTP('smtp.gmail.com', 25)
server.starttls()
server.login(fromaddr, "")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()
  
