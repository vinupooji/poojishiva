import smtplib
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login("poojitha202@gmail.com","password")
msg = "hlo!!!!!!!!!!!"
server.sendmail("poojitha202@gamil.com","pthilothy@gmail.com",msg)
server.quit()