import getpass
import telnetlib

user = raw_input("Enter your username: ")
password = getpass.getpass()

HOST = ("192.168.79.140", "192.168.79.138", "192.168.79.137")

for i in HOST:
    print("\n\nconnecting to " + i)
    tn = telnetlib.Telnet(i, timeout = 15)
    if i is "192.168.79.140":
        tn.read_until("login: ")
        tn.write(user + "\n")
        if password:
            tn.read_until("Password:")
            tn.write(password + "\n")
        tn.write("sh configuration | display set\n")
        tn.write("exit\n")
        print(tn.read_all())

    elif i is "192.168.79.138":
        tn.read_until("Username: ")
        tn.write(user + "\n")
        if password:
            tn.read_until("Password:")
            tn.write(password + "\n")
        tn.write("terminal length 0\n")
        tn.write("sh run\n")
        tn.write("exit\n")
        print(tn.read_all())

    elif i is "192.168.79.137":
        tn.read_until("Username: ")
        tn.write(user + "\n")
        if password:
            tn.read_until("Password:")
            tn.write(password + "\n")
        tn.write("en\n")
        tn.write("terminal length 0\n")
        tn.write("sh run\n\n")
        tn.write("exit\n\n")
        print(tn.read_all())
    readall = tn.read_all()
    File = open("File"+ str(i), "w")
    File.write(readall)
    File.write("\n")
    File.close()
    print("Backup of "+i+" completed")

