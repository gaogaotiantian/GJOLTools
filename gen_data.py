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

game_data['items'] = items_data()
game_data['enchantment'] = enchantment_data()

with open('game_data.js', 'w', encoding = 'utf-8') as f:
    f.write("const game_data = ")
    json.dump(game_data, f, ensure_ascii = False, indent=4)


