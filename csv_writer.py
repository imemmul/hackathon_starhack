import csv
#csv_columns_car = ['order_id', 'order_type', 'latitude', 'longtitude']
#csv_columns_store = ['name', 'latitude', 'longtitude', 'duration']
#dict_car = [{'order_id': 1, 'order_type': 'food', 'latitude': 10, 'longtitude': 20}]
#dict_store = [{'name':'Starbucks', 'latitude':30.5, 'longtitude':50.5, 'duration':0.5}, {'name':'Burger', 'latitude':20.5, 'longtitude':35.5, 'duration':35}]


def write_csv(filename):
    csv_file = filename
    try:
        with open(csv_file, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns_store)
            writer.writeheader()
            for data in dict_store:
                writer.writerow(data)
    except IOError:
        print("I/O error")


if __name__ == "__main__":
    write_csv()
