import json

def write_to_file(dictionary):
    json_object = json.dumps(dictionary, indent=4)
    with open("output/result.json", "w") as outfile:
        outfile.write(json_object)