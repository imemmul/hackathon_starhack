import csv
csv_columns = ['order_id', 'order_type', 'latitude', 'longtitude']

dict_data = [{'order_id': 1, 'order_type': 'food', 'latitude': 10, 'longtitude': 20}]

csv_file = "data.csv"
try:
    with open(csv_file, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()
        for data in dict_data:
            writer.writerow(data)
except IOError:
    print("I/O error")
