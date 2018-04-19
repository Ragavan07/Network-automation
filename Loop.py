import getpass
import sys
import telnetlib

HOST = ("192.168.79.137", "192.168.79.138")
user = raw_input("Enter username: ")
password = getpass.getpass()


for i in HOST:
    if i is "192.168.79.137":
        tn = telnetlib.Telnet(HOST[0], timeout = 15)
        tn.read_until("Username: ")
        tn.write(user+ "\n")
        if password:
            tn.read_until("Password:")
            tn.write(password + "\n")
        tn.write("conf t\n")
        for n in range(1,6):
            tn.write("int lo" + str(n) + "\n")
            tn.write("ip add "+str(n)+"."+str(n)+"."+str(n)+"."+str(n)+ " 255.255.255.255 \n")
            tn.write("no shut\n")
            tn.write("exit\n")
        tn.write("exit \n")
        

    elif i is "192.168.79.138":
        tn = telnetlib.Telnet(HOST[1], timeout = 15)
        tn.read_until("Username: ")
        tn.write(user+ "\n")
        if password:
            tn.read_until("Password:")
            tn.write(password + "\n")
        tn.write("en \n")
        tn.write("conf t\n")
        for n in range(1,6):
            tn.write("int lo" + str(n) + "\n")
            tn.write("ip address "+str(n)+"."+str(n)+"."+str(n)+"."+str(n)+ " 255.255.255.255 \n")
            tn.write("no shut\n")
            tn.write("exit\n")
#            print tn.read_all() 
        tn.write("exit \n")
        print (tn.read_all())
