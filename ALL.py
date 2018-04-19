
import getpass
import sys
import telnetlib

HOST = ("192.168.79.137", "192.168.79.138", "192.168.79.140")
user = raw_input("Enter your username: ")
password = getpass.getpass()

for i in HOST:
    if i is "192.168.79.137":
        tn = telnetlib.Telnet(HOST[0], timeout = 5)
        tn.read_until("Username: ")
        tn.write(user + "\n")
        if password:
            tn.read_until("Password:")
            tn.write(password + "\n")
        tn.write("en \n")
        tn.write("conf t\n")
        tn.write("int lo 0\n")
        tn.write("ip add 1.1.1.1 255.255.255.255\n" )
        tn.write("no shut\n")
        tn.write("end\n")
        tn.write("exit\n")
        print tn.read_all()

    elif i is "192.168.79.138":
        tn = telnetlib.Telnet(HOST[1], timeout = 5)
        tn.read_until("Username: ")
        tn.write(user + "\n")
        if password:
            tn.read_until("Password:")
            tn.write(password + "\n")
        tn.write("en \n")
        tn.write("conf t\n")
        tn.write("int lo 0\n")
        tn.write("ip add 1.1.1.1 255.255.255.255\n")
        tn.write("no shut\n")
        tn.write("end\n")
        tn.write("exit\n")
        print tn.read_all()

    elif i is "192.168.79.140":
        tn = telnetlib.Telnet(HOST[2], timeout = 15)
        tn.read_until("login: ")
        tn.write(user + "\n")
        if password:
            tn.read_until("Password:")
            tn.write(password + "\n")
        tn.write("configure\n")
        tn.write("set interfaces lo0 unit 0 family inet address 1.1.1.1/32\n")
        tn.write("commit and-quit\n")
        tn.write("exit\n")
        print tn.read_all()
