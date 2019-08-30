import csv
import argparse

class Item:
    def __init__(self, raw):
        self.data = {}
        for key in raw:
            self.data[key] = raw[key]

    def render_markdown(self):
        ret = "* **{}** _{}_\n".format(self.data["装备名"], self.render_attribute())
        return ret

    def render_attribute(self):
        attr_list = []
        ret = ""
        for key in self.data:
            if key != "等级":
                try:
                    attr = float(self.data[key])
                    attr_list.append((key, attr))
                except:
                    pass
        attr_list.sort(key = lambda x: x[1], reverse = True)
        ret = " ".join(["{} + {}".format(key, attr) for key, attr in attr_list])
        return ret

    def __getitem__(self, key):
        return self.data[key]
                
class ItemList:
    def __init__(self):
        self.items = {}

    def add_item_raw(self, raw):
        item = Item(raw)
        level = item["等级"]
        position = item["位置"]
        if level not in self.items: 
            self.items[level] = {}
        if position not in self.items[level]:
            self.items[level][position] = []
        self.items[level][position].append(item)

    def render(self):
        ret = ""
        for level in self.items:
            ret += "## {}\n\n".format(level)
            ret += "### 法战 \n\n"
            for position in self.items[level]:
                ret += "#### {}\n\n".format(position)
                items = sorted(self.items[level][position], key = lambda x: x["装备名"])
                for item in items:
                    ret += item.render_markdown()
                ret += "\n"
        return ret

class QqxCombination:
    def __init__(self, raw):
        self.data = {}
        for key in raw:
            self.data[key] = raw[key]

    def render(self):
        ret = "* "
        ret += ", ".join([self.data[key] for key in self.data if key != "分数" and self.data[key]]);
        ret += "： {}".format(self.data["分数"])
        ret += "\n"
        return ret


def do_item():
    item_list = ItemList()
    with open('items.csv') as csvfile:
        reader = csv.DictReader(csvfile, delimiter = ',')
        for row in reader:
            item_list.add_item_raw(row)

    print(item_list.render())

def do_qqx():
    ret = ""
    with open('qqx_combination.csv') as csvfile:
        reader = csv.DictReader(csvfile, delimiter = ',')
        for row in reader:
            comb = QqxCombination(row)
            ret += comb.render()
    print(ret)
        
            


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("file_list", nargs = '*')
    args = parser.parse_args()
    for f in args.file_list:
        if f == "item":
            print("Do Item")
            do_item()
        elif f == "qqx":
            print("Do QQX")
            do_qqx()

