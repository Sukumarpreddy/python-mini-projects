import json

with open('data.json',"r") as f:
    data = json.load(f)
    print("Original Data:")
    print(data)

data["status"] = "processed"

with open("udapted_data.json", "w") as f:
    json.dump(data, f ,indent=4)

print("\nUpdated JSON saved! ")