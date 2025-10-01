import random
from config import names, nouns, config, char_substitutions  # 導入配置和字符替換映射

def truncate_word(word):
    """根據配置選項截斷單詞"""
    if not config["truncate_words"]:
        return word
    
    # 決定是否截斷開頭、結尾或兩者
    truncate_type = random.choice(['none', 'start', 'end', 'both'])
    
    if truncate_type == 'none' or len(word) <= 3:
        return word
    elif truncate_type == 'start':
        return word[random.randint(1, len(word)//2):]
    elif truncate_type == 'end':
        return word[:random.randint(len(word)//2, len(word)-1)]
    else:  # both
        start = random.randint(1, len(word)//3)
        end = random.randint(len(word)-len(word)//3, len(word)-1)
        return word[start:end]

def substitute_characters(word):
    """根據配置選項替換字符"""
    if not config["use_character_substitution"] or random.random() > 0.3:  # 30% 的機率進行替換
        return word
    
    result = ""
    for char in word:
        lower_char = char.lower()
        if lower_char in char_substitutions and random.random() > 0.5:  # 50% 的機率替換符合條件的字符
            result += char_substitutions[lower_char]
        else:
            result += char
    
    return result

def add_underscores(text):
    """根據配置選項添加底線"""
    if not config["add_underscores"] or random.random() > 0.2:  # 20% 的機率添加底線
        return text
    
    if len(text) <= 2:
        return text
    
    position = random.randint(1, len(text) - 1)
    
    # 只添加單一底線
    return text[:position] + '_' + text[position:]

def apply_case_style(text):
    """根據配置選項應用大小寫樣式"""
    if config["case_style"] == "lowercase":
        return text.lower()
    elif config["case_style"] == "capitalize":
        # 如果文字中包含數字或底線，需要特別處理
        parts = []
        current_part = ""
        
        for char in text:
            if char.isalpha() or char.isdigit():
                current_part += char
            else:  # 遇到特殊字符（如底線）
                if current_part:
                    parts.append(current_part)
                    current_part = ""
                parts.append(char)
        
        if current_part:
            parts.append(current_part)
        
        # 處理每個部分
        result = ""
        for i, part in enumerate(parts):
            if i == 0 or parts[i-1] in ['_', '__']:  # 如果是第一個部分或前面是底線
                result += part.capitalize()
            else:
                result += part
        
        return result
    
    return text  # 如果沒有指定樣式，保持原樣

def generate_random_id():
    # 隨機選擇組合類型
    combination_type = random.choice(['name_noun', 'noun_name', 'noun_noun'])
    
    # 獲取並處理單詞
    if combination_type == 'name_noun':
        word1 = truncate_word(random.choice(names))
        word2 = truncate_word(random.choice(nouns))
    elif combination_type == 'noun_name':
        word1 = truncate_word(random.choice(nouns))
        word2 = truncate_word(random.choice(names))
    else:  # noun_noun
        word1 = truncate_word(random.choice(nouns))
        word2 = truncate_word(random.choice(nouns))
    
    # 應用字符替換
    word1 = substitute_characters(word1)
    word2 = substitute_characters(word2)
    
    # 決定數字的位置
    number_position = random.choice(['none', 'middle', 'end'])
    
    # 生成數字
    number_type = random.choice(['two_digits', 'four_digits', 'year'])
    
    if number_type == 'two_digits':
        number = random.randint(10, 99)
    elif number_type == 'four_digits':
        number = random.randint(1000, 9999)
    else:  # year
        number = random.randint(1980, 2010)
    
    # 組合 ID
    if number_position == 'none':
        result = word1 + word2
    elif number_position == 'middle' and config["add_numbers_between_words"]:
        result = word1 + str(number) + word2
    else:  # end 或 當 add_numbers_between_words 為 False 時
        result = word1 + word2 + str(number)
    
    # 添加底線
    result = add_underscores(result)
    
    # 應用大小寫樣式
    result = apply_case_style(result)
    
    return result

def save_ids_to_file(filename, count):
    with open(filename, 'w') as file:
        for _ in range(count):
            file.write(generate_random_id() + '\n')

# 使用範例
if __name__ == "__main__":
    save_ids_to_file("random_id.txt", 1000)  # 生成 1000 個隨機帳號 ID
    
    # 顯示一些範例
    print("生成的隨機 ID 範例:")
    for _ in range(10):
        print(generate_random_id())