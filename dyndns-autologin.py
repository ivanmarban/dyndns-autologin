import mechanize
import time
import smtplib

#DynDNS account info
username =''
password = ''

#Gmail account info
fromaddr = ''
toaddrs  = ''
gusername = ''
gpassword = ''

counter = 0

#Use mechanize to open url:
br = mechanize.Browser()
r = br.open('https://account.dyn.com')
br.addheaders = [('User-agent', 'Firefox')]

#Search the login form:
for form in br.forms():
    if "submit=Log in" in str(form):
        br.select_form(nr=counter)
    counter += 1

#Now we log in with the correct user/pass:
br.form['username'] = username
br.form['password'] = password
br.submit()

#Print result:
html = br.response().read()
#print html

if "Welcome" in str(html):
	#print "Login succesful, waiting 5 seconds to logout..."
	time.sleep(5)
	r = br.open("https://account.dyn.com/entrance/?__logout=1")
	#print br.response().read()
else:
    #print "ERROR: Unable to login"
	server = smtplib.SMTP('smtp.gmail.com:587')
	server.starttls()
	server.login(gusername,gpassword)
	server.sendmail(fromaddr, toaddrs, "ERROR: Unable to login at https://account.dyn.com")
	server.quit()