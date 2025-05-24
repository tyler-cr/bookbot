
def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

def get_num_words(file_path):
    return len(get_book_text(file_path).split())

def get_num_chars(file_path):

    ret_dict = {}

    lower_book = get_book_text(file_path).lower()

    for char in lower_book:
        if char in ret_dict:
            ret_dict[char] += 1
        else:
            ret_dict[char] = 1
    
    return ret_dict

def get_sorted_list(dict):
    ret_list = []

    for key, value in dict.items():
        if key.isalpha():
            ret_list.append({"name": key, "num": value})

    ret_list.sort(reverse=True, key = sort_on)

    return ret_list

def sort_on(dict):
    return dict["num"]
