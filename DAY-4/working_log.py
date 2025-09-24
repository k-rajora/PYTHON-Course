import re

logfile = "access.log"

pattern = re.compile(r'(?P<ip>\d+\.\d+\.\d+\.\d+) - - .* "(?P<method>GET|POST) (?P<url>\S+)')

with open(logfile, "r") as f:
    for line in f:
        match = pattern.search(line)
        if match:
            print(f"IP: {match['ip']} | Method: {match['method']} | URL: {match['url']}")
