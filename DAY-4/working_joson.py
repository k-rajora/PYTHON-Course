import json

# Writing JSON
data = {"service": "nginx", "status": "running", "ports": [80, 443]}
with open("config.json", "w") as f:
    json.dump(data, f, indent=4)

# Reading JSON
with open("config.json", "r") as f:
    config = json.load(f)
print(config)   
