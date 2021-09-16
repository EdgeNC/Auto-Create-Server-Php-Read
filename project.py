import os

os.system("title EDGE TOOLS")
File = "server_data.php"
print("ARIF TOOLS")
os.system("CLS || clear")
e = open(File, 'w') 
IPGTPS = input("[+] masukan ip mu :  ") 
e.write(f"""server|{IPGTPS}
port|17091
type|1
#maint|Your Maintenance Message -- Remove '#' If You Want Enable Maintenace Mode :)

beta_server|127.0.0.1
beta_port|17091

beta_type|1
meta|localhost
RTENDMARKERBS1001
""")
e.close()
print("server_data.php success di buat")
print("THANKS FOR USING ARIF TOOLS")

