import smtplib
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login("poojitha202@gmail.com","shiva143")
msg = "hlo!!!!!!!!!!!"
server.sendmail("poojitha202@gamil.com","pthilothy@gmail.com",msg)
print("msg sent")
server.quit()