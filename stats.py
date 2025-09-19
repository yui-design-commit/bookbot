def get_num_words(text):
    words = text.split()
    return len(words)

def get_char_dict(text):
    char_dict = {} # empty char dict
    char_name_list = [] # saves "name" from each dict
    # no split() here. it ignores whitespaces

    for char in text.lower(): # can include whitespaces
        #prints every single char in contents
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1

    for key in char_dict:
        each_char_dict = {}
        each_char_dict["name"] = key
        each_char_dict["num"] = char_dict[key]
        char_name_list.append(each_char_dict)

    def sort_on(items):
        return items["num"]
    
    char_name_list.sort(reverse=True, key=sort_on)

    for item in char_name_list:
        if item["name"].isalpha() != True:
            continue

        print(f'{item["name"]}: {item["num"]} \n')

    return char_name_list



                
                  
            

      

