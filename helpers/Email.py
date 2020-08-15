# import necessary packages
 
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
 
class Email():
   
       def EnviarEmail(self,titulo, mensaje) :
            # create message object instance
          try:
                  msg = MIMEMultipart()
                  password = "Renovado7173"
                  msg['From'] = "ehidalgoca@gmail.com"
                  msg['To'] = "ehidalgo@stpsantiago.cl"
                  msg['Subject'] = titulo
                  msg.attach(MIMEText(mensaje, 'plain'))
                  #create server
                  server = smtplib.SMTP('smtp.gmail.com: 587')
                  server.starttls()   
                  server.login(msg['From'], password)
                  server.sendmail(msg['From'], msg['To'], msg.as_string())
                  server.quit()
                  return True
          except: 
              return False
           
    
       





 




 


