import json
print("Podaj nazwe pliku")
filename = input()
file = json.load(open(filename+'.json', "r"))

config = open("config.cfg", "w")
for printer in file:

    config.write('''
        define host{
	        use		    generic-printer
	        host_name'''+printer+'''
	        alias
	        address		172.16.205+ip
	        hostgroups	network-printers
	        parents		TYC-PRINT-2
        }''')