import json

def read_json_file():
    file_path = "data/sales.json"

    with open(file_path, "r") as file:
        data = json.load(file)

    print("JSON Loaded Successfully\n")
    print(data)

if __name__ == "__main__":
    read_json_file()