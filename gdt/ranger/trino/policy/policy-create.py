import json
import yaml

# Load YAML data from a file
with open('policy-0001.yaml', 'r') as yaml_file:
    yaml_data = yaml.safe_load(yaml_file)

# Convert YAML to JSON
json_data = json.dumps(yaml_data, indent=2)

# Print the JSON data or save it to a file
print(json_data)

