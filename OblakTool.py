import os
import socket
os.system("clear")

print(" _____   _____   _           ___   _   _   V1.0  ")  
print("/  _  \ |  _  \ | |         /   | | | / / ") 
print("| | | | | |_| | | |        / /| | | |/ /   ")
print("| | | | |  _  { | |       / / | | | |\ \   ")
print("| |_| | | |_| | | |___   / /_ | | | | | \   ")
print("\_____/ |_____/ |_____| /_/   |_| |_|  \_\ ")
print("")
print("")
print(".....WELCOME TO OBLAK SCRIPT......")
print("")
print("")
name = input("type your name here: ")
print("")
print("")
print("hello: "+name)
print("")
print("")
password = input ("type the password here: ")
import os
os.system("clear")
#Tools
if password == "r2020" :
    import os
    os.system('clear')
    print("")
    print(" _____   _____   _           ___   _   _ ")  
    print("/  _  \ |  _  \ | |         /   | | | / / ") 
    print("| | | | | |_| | | |        / /| | | |/ /   ")
    print("| | | | |  _  { | |       / / | | | |\ \   ")
    print("| |_| | | |_| | | |___   / /_ | | | | | \   ")
    print("\_____/ |_____/ |_____| /_/   |_| |_|  \_\ ")
    print("")
    print("")
    print("")
    print("Correct Password")
    print("")
    print("")
    print("#########################")
    print("1- START Facebook TOOL  #")
    print("                        #")
    print("2- START Findingg IPs   #")      
    print("                        #") 
    print("3- Start E-Mail Tool    #")
    print("                        #")
    print("4- EXIT TOOL            #")
    print("                        #")
    print("#########################")
    select = input("type a number--> ")
#######################################     
if select == "1" :
   os.system("clear")
   print(" ==> Welcome To Facebook Tool <==")
   print("")
   print("")
   print("")
   print("")
   site = "https://m.facebook.com/login/?locale=ar_AR"
   name = input("Please Type The Your target ==> ")
   print("")
   print("")
   passwfile = input("Please Type The Password File ==> ")
   passwfile = open(passwfile, "r")
   for x in passwfile:
            print(x)
   website =site+x 
   if website == name :
        print("Password found ==> ",x)
   else :
    print("Soory Password Not found ")
    print("Please Try Adiffrent Password File")
#############Find ip tool#############
if select == '2' :
    os.system("clear")
    import socket
    if __name__ == '__main__' :
        print("")
        hostname = input("Enter your Target ==> ")
        print("")
        addr = socket.gethostbyname(hostname)
        print("the ip {} address is ==> {}".format(hostname,addr))
######################E-MailTool ########  
if select == '3' :
    os.system("clear")
    print("")
    print("")
    print("====[ Welcome To E-mail Tool ]====")
    print("")
    print("")
    print("")
    print("")
    select2 = input(" Type The Target ==> ")
    print("")
    print("")
    pass2   = input("Enter The Password File ==> ")
    pass2   = open(pass2, "r")
    for z in pass2 :
        print(z)
    site2   = "https://accounts.google.com/signin/chrome/sync/identifier?ssp=1&continue=https%3A%2F%2Fwww.google.com%2F&flowName=GlifDesktopChromeSync"
    if site2 == select2+z :
        print("")
        print("Pssword Found ==> ", z)
    else:
        print("")
        print("Soory Password Not Found..!")
###########EXIT TOOL#############
if select == '4' :
    print("")
    print("Bey Bey ..")
    os.system("exit")
###########################