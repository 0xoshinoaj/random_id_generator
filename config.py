# config.py

# 名字列表 - 擴展為原來的兩倍
names = [
    "Alice", "Bob", "Charlie", "David", "Eva", "Frank", "Grace", "Hannah", 
    "Ian", "Jack", "Kathy", "Leo", "Mia", "Nina", "Oscar", "Paul", 
    "Quinn", "Rachel", "Sam", "Tina", "Uma", "Vera", "Will", "Xena", 
    "Yara", "Zoe", "Adam", "Bella", "Cathy", "Derek", "Ella", "Fiona", 
    "Gina", "Henry", "Ivy", "Jake", "Kira", "Liam", "Maya", "Nate", 
    "Olivia", "Peter", "Quincy", "Rita", "Steve", "Troy", "Ursula", 
    "Victor", "Wendy", "Xander", "Yvonne", "Zach",
    # 新增名字
    "Aaron", "Brenda", "Carl", "Diana", "Eric", "Felicia", "George", "Heidi",
    "Isaac", "Julia", "Kevin", "Linda", "Mark", "Nancy", "Owen", "Pamela",
    "Quentin", "Rose", "Scott", "Tara", "Ulysses", "Violet", "Walter", "Ximena",
    "Yasmin", "Zachary", "Andrew", "Bianca", "Cameron", "Donna", "Edward", "Faye",
    "Greg", "Holly", "Ivan", "Jessica", "Kyle", "Laura", "Michael", "Natalie",
    "Oliver", "Patricia", "Quinton", "Rebecca", "Simon", "Tiffany", "Umar", "Valerie",
    "William", "Xenia", "Yvette", "Zeke"
]

# 名詞列表 - 擴展為原來的兩倍
nouns = [
    "Tree", "River", "Mountain", "Sky", "Ocean", "Star", "Cloud", "Flower", 
    "Sun", "Moon", "Lake", "Rock", "Wind", "Fire", "Earth", "Grass", 
    "Bird", "Fish", "Insect", "Animal", "Stone", "Leaf", "Root", "Branch", 
    "Wave", "Rain", "Snow", "Thunder", "Lightning", "Desert", "Valley", 
    "Forest", "Field", "Meadow", "Canyon", "Island", "Coast", "Beach", 
    "Hill", "Plain", "Pond", "Stream", "Grove", "Swamp", "Marsh", 
    "Glacier", "Cave", "Cliff", "Dune", "Fjord", "Lagoon", "Tide", 
    "Coral", "Reef", "Geyser", "Volcano", "Crater",
    # 新增名詞
    "Book", "Chair", "Table", "Door", "Window", "House", "Car", "Road",
    "Phone", "Computer", "Keyboard", "Mouse", "Screen", "Lamp", "Pen", "Paper",
    "Bottle", "Cup", "Plate", "Fork", "Knife", "Spoon", "Bowl", "Glass",
    "Shirt", "Pants", "Shoes", "Hat", "Coat", "Glove", "Sock", "Scarf",
    "Watch", "Clock", "Ring", "Necklace", "Bracelet", "Earring", "Wallet", "Bag",
    "Box", "Key", "Lock", "Chain", "Rope", "String", "Thread", "Needle",
    "Brick", "Wood", "Metal", "Glass", "Plastic", "Rubber", "Cotton", "Wool",
    "Nation", "City", "Town", "Village", "Street", "Bridge", "Tower", "Building"
]

# 配置選項
config = {
    # 是否在單詞中間添加數字
    "add_numbers_between_words": True,
    
    # 是否截斷單詞（去頭去尾）
    "truncate_words": True,
    
    # 是否添加底線
    "add_underscores": True,
    
    # 是否使用字符替換（例如：'a' -> '4'）
    "use_character_substitution": False,
    
    # 大小寫設置：'capitalize'（開頭大寫）或 'lowercase'（全小寫）
    "case_style": "lowercase"
}

# 字符替換映射
char_substitutions = {
    'a': '4',
    'e': '3',
    'i': '1',
    'o': '0',
    's': '5',
    't': '7',
    'b': '8',
    'g': '9',
    'l': '1',
    'z': '2'
}