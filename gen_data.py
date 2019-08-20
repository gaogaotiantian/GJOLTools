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

def enchantment_data():
    ret = {
        "头饰": {
            "专注": [24, 36, 51, 68]
        },
        "武器": {
            "攻击": [8, 10, 26, 34]
        }, 
        "上装": {
            "术": [8, 12, 20, 27]
        }, 
        "下装": {
            "术": [8, 12, 20, 27]
        }, 
        "护手": {
            "强度": [24, 36, 51, 68],
            "专精": [24, 36, 51, 68],
            "专注": [24, 36, 51, 68],
        },
        "腰带": {
            "专精": [24, 36, 51, 68],
            "会心": [24, 36, 51, 68],
            "急速": [24, 36, 51, 68],
        }, 
        "鞋子": {
            "急速": [24, 46, 51, 68],
        }
    }
    return ret

def gem_data():
    def get_data(row):
        ret = {}
        for key in row:
            try:
                val = int(row[key])
                if val == 2:
                    ret[key] = list(range(6, 22, 2))
                elif val == 6:
                    ret[key] = list(range(6, 51, 6))
            except:
                pass
        return ret

    gem_data = {}
    with open('gem.csv') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        for row in reader:
            for place in row["位置"].split():
                if place not in gem_data:
                    gem_data[place] = {}

                gem_data[place][row["名称"]] = get_data(row)
    return gem_data

game_data['items'] = items_data()
game_data['enchantment'] = enchantment_data()
game_data['gem'] = gem_data()

with open('game_data.js', 'w', encoding = 'utf-8') as f:
    f.write("const game_data = ")
    json.dump(game_data, f, ensure_ascii = False, indent=4)


