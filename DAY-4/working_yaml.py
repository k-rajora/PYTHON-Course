import yaml

# Writing YAML
data = {"service": "nginx", "replicas": 3, "enabled": True}
with open("config.yaml", "w") as f:
    yaml.dump(data, f)

# Reading YAML
with open("config.yaml", "r") as f:
    config = yaml.safe_load(f)
print(config["service"])   # nginx
