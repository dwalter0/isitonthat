import sys
import json
import ipaddress

file_path = sys.argv[1]  # Replace with the actual file path
with open(file_path, 'r') as jsonfile:
    json_data = json.load(jsonfile)

file_path = sys.argv[2]  # Replace with the actual file path
with open(file_path, 'r') as ipfile:
    ips = ipfile.readlines()


address_prefixes = [entry["properties"]["addressPrefixes"] for entry in json_data["values"]]
none = True
for ip in ips:
    ip = ip.strip("\n")
    ipinarange = False
    for prefix_group in address_prefixes:
        for prefix in prefix_group:
            network = ipaddress.ip_network(prefix, strict=False)
            ip_address = ipaddress.ip_address(ip)
            if ip_address in network:
                ipinarange = True
                none = False
    if ipinarange:
        print(f"IP {ip} is in azure.")
    else:
        print(f"IP {ip} is not in azure.")
if none:
    print("I don't think any of them are in azure.")
