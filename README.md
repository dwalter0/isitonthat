# isitonthat

### Installation
It uses one non-standard library.
`pip3 install ipaddress`
Recommend using a venv.

### Usage

Few scripts to check if a list of IP Addresses are in various cloud providers

The ref_locs.txt document shows URLs where the public listings of the IP ranges of the cloud providers are.

All four of the scripts are run like
`python3 isiton_x_.py <file from public listing for provider> <file with ips to check 1 per line>`

<br/>

`python3 isitondo.py google.csv ips.txt`
`python3 isitonazure.py ServiceTags_Public_20230814.json ips.txt`
`python3 isitonaws.py ipranges.json ips.txt`
`python3 isitongcp.py cloud.json ips.txt`
