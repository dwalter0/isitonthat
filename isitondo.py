import sys
import csv
import ipaddress


            

file_path = sys.argv[2]  # Replace with the actual file path
with open(file_path, 'r') as ipfile:
    ips = ipfile.readlines()

address_prefixes = []
file_path = sys.argv[1]  # Replace with the actual file path
with open(file_path, 'r') as csvfile:
    csv_reader = csv.reader(csvfile)
    for row in csv_reader:
        if row:
            address_prefixes.append(row[0])
        
none = True
for ip in ips:
    ip = ip.strip("\n")
    ipinarange = False
    for prefix in address_prefixes:
        network = ipaddress.ip_network(prefix, strict=False)
        ip_address = ipaddress.ip_address(ip)
        if ip_address in network:
            ipinarange = True
            none = False
    if ipinarange:
        print(f"IP {ip} is in GCP.")
    else:
        print(f"IP {ip} is not in GCP.")
if none:
    print("I don't think any of them are in GCP.")
