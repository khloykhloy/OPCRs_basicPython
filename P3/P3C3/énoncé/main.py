import csv

def extract (filename="input.csv"):
    data = []
    with open(filename, "r") as file :
        csv_reader = csv.DictReader(file)
        for line in csv_reader :
            data.append(line)
    return data

def transform(data_to_transform):
    data_to_load = []
    for data in data_to_transform :
        transformed_data = {}
        transformed_data["nom"] = data["nom"]
        transformed_data["salaire"] = int(data["heures_travaillees"]) * 15
        data_to_load.append(transformed_data)
    return data_to_load

def load(data_to_load, filename="output.csv"):
    with open(filename, "w", newline="") as file :
        fieldnames = ["nom", "salaire"]
        writer = csv.DictWriter(file, fieldnames)
        writer.writeheader()
        for data in data_to_load :
            writer.writerow(data)

def main ():
    data_to_transformed = extract("input.csv")
    data_to_load = transform(data_to_transformed)
    load(data_to_load, "output.csv")

if __name__ == "__main__":
    main()
