const game_data = {
    "items": {
        "头": [
            {
                "装备名": "装备1", 
                "等级": 180, 
            }
        ], 
        "衣服": [
            {
                "装备名": "身体装备1",
                "术": 12
            },
            {
                "装备名": "身体装备2",
                "术": 14
            }
        ],
        "武器": [
            {
                "装备名": "碧华",
                "等级": 195,
                "攻击": 81.4,
                "专注": 108.5,
                "术": 20.7,
                "急速": 45.2,
                "会心": 32.3
            }
        ],
        "左信物": [
            {
                "装备名": "碧华福器",
                "等级": 195,
                "攻击": 24.8,
                "术": 26.5,
            }
        ]
    }
}

const attribute_header = [
    "术",
    "攻击",
    "强度",
    "专精",
    "会心",
    "专注",
    "急速"
]

const item_positions = Object.keys(game_data["items"]);

const item_header = [
    "位置",
    "装备",
    "强化",
    "等级",
    "术",
    "攻击",
    "强度",
    "专精",
    "会心",
    "专注",
    "急速"
]

function create_attribute_chart() {
    let container = document.getElementById('item-attribute-container');
    let d = document.createElement('div');
    d.className = "d-flex justify-content-around";

    container.appendChild(d);

    for (let i = 0; i < attribute_header.length; i++) {
        let header = attribute_header[i];
        let col = document.createElement('div');
        let attribute_name = document.createElement('p')
        let attribute_data = document.createElement('p')
        let attribute_data_percent = document.createElement('p')
        attribute_name.innerHTML = header
        attribute_data.id = "属性-"+header
        attribute_data.className = "item-cell"
        attribute_data_percent.id = "属性-"+header+"-率"
        attribute_data_percent.className = "item-cell"
        col.appendChild(attribute_name)
        col.appendChild(attribute_data)
        col.appendChild(attribute_data_percent)

        d.appendChild(col);
    }
    
}

function create_item_chart() {
    // Create the whole form first
    let container = document.getElementById('item-choice-container');
    let d = document.createElement('div');
    d.className = "d-flex justify-content-around";
    for (let i = 0; i < item_header.length; i++) {
        let header = item_header[i];
        let col = document.createElement('div');
        col.id = "装备-"+header
        
        let header_div = document.createElement('div');
        header_div.innerHTML = header;
        col.appendChild(header_div);

        // Create cells for each position
        for (let j = 0; j < item_positions.length; j++) {
            let position = item_positions[j];
            let position_div = document.createElement('div');
            position_div.className = "item-cell"
            position_div.id = header + '-' + position;
            if (header == "位置") {
                position_div.innerHTML = position;
            }
            col.appendChild(position_div);
        }

        d.appendChild(col);
    }
    container.appendChild(d);

    // Add selector for the form
    for (let i = 0; i < item_positions.length; i++) {
        let position = item_positions[i];
        if (position in game_data["items"]) {
            // 装备选择
            let name_cell = document.getElementById("装备-"+position);
            let options = []
            let select_id = position + "-select";
            name_cell.innerHTML = "";
            for (let j = 0; j < game_data["items"][position].length; j++) {
                let data = game_data["items"][position][j];
                options.push(data["装备名"]);
            }
            name_cell.appendChild(create_select(select_id, options));

            // 强化选择
            name_cell = document.getElementById("强化-"+position);
            name_cell.innerHTML = "";
            select_id = position + "-强化-select";
            options = [];
            for (let j = 0; j <= 5; j++) {
                options.push(j);
            }
            name_cell.appendChild(create_select(select_id, options));

        }
    }
}

function create_select(select_id, options) {
    let s = document.createElement('select');
    s.className = "form-control";
    s.id = select_id;

    for (let i = 0; i < options.length; i++) {
        let option = document.createElement('option');
        option.value = options[i];
        option.innerHTML = options[i];
        s.appendChild(option);
    }

    return s;
}

function find_item_by_name(name, position = null)
{
    if (position) {
        if (position in game_data["items"]) {
            for (let i = 0; i < game_data["items"][position].length; i++) {
                if (game_data["items"][position][i]["装备名"] == name) {
                    return game_data["items"][position][i];
                }
            }
        }
    } else {
        for (let position in game_data["items"]) {
            for (let i = 0; i < game_data["items"][position].length; i++) {
                if (game_data["items"][position][i]["装备名"] == name) {
                    return game_data["items"][position][i];
                }
            }
        }
    }

    return null;
}

function refresh_item_data() {
    // Update item data based on selected item
    for (let i = 0; i < item_positions.length; i++) {
        let position = item_positions[i];
        let select = document.getElementById(position+"-select");
        if (select) {
            let item_name = select.options[select.selectedIndex].value;
            let data = find_item_by_name(item_name);
            if (data) {
                // Do not change "装备" and "位置"
                for (let j = 3; j < item_header.length; j++) {
                    let header = item_header[j];
                    let cell = document.getElementById(header + '-' + position);
                    if (header in data) {
                        cell.innerHTML = data[header];
                    } else {
                        cell.innerHTML = 0;
                    }
                }
            }
        }
    }

    // Update total attributes based on items
    for (let i = 0; i < attribute_header.length; i++) {
        let attr = attribute_header[i];
        let total_attr_points = attr_base(attr);
        for (let j = 0; j < item_positions.length; j++) {
            let position = item_positions[j];
            total_attr_points += parseFloat(document.getElementById(attr + '-' + position).innerHTML);
        }
        document.getElementById("属性-" + attr).innerHTML = total_attr_points;
        document.getElementById("属性-" + attr + "-率").innerHTML = attr_percent(attr, total_attr_points);
    }
    
}

function attr_base(attr) {
    return 0;
}

function attr_percent(attr, points) {
    return "";
}

$(function() {
    create_attribute_chart();
    create_item_chart();
    refresh_item_data();

    $('body').on('change', 'select', refresh_item_data);
})
