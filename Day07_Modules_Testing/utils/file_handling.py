import json 

def write_txt(filename,content):
    with open(filename, 'w') as file:
        file.write(content)

def read_txt(filename):
    with open(filename, 'r') as file:
        return file.read()

def write_json(filename,content):
    with open(filename, 'w') as file:
        json.dump(content, file, indent=4)
        #writes a dict cleanly to a JSON file 
    
def read_json(filename):
    with open(filename, 'r') as file:
        return json.load(file)