import sys
import json
import ipaddress

file_path = sys.argv[1]  # Replace with the actual file path
with open(file_path, 'r') as jsonfile:
    json_data = json.load(jsonfile)

file_path = sys.argv[2]  # Replace with the actual file path
with open(file_path, 'r') as ipfile:
    ips = ipfile.readlines()

address_prefixes = []
for entry in json_data["prefixes"]:
    if "ip_prefix" in entry:
        address_prefixes.append(entry["ip_prefix"])
    if "ipv6_prefix" in entry:
        address_prefixes.append(entry["ipv6_prefix"])
        
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
        print(f"IP {ip} is in AWS.")
    else:
        print(f"IP {ip} is not in AWS.")
if none:
    print("I don't think any of them are in AWS.")
