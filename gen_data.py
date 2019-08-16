import csv
import json

game_data = {}

def items_data():
    def get_data(data):
        ret = {}
        for key in data:
            ret[key] = data[key]
        return ret
    # Generate item data
    items_data = {}
    with open('items.csv') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        for row in reader:
            if row['位置'] not in items_data:
                items_data[row['位置']] = []
            items_data[row['位置']].append(row)
    return items_data

game_data['items'] = items_data()

with open('game_data.js', 'w', encoding = 'utf-8') as f:
    f.write("const game_data = ")
    json.dump(game_data, f, ensure_ascii = False, indent=4)


