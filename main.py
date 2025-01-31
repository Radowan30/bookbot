def main():
    book_path = "books/frankenstein.txt"
    with open(book_path) as f:
        file_contents = f.read()
        print_report(file_contents)
    
def print_report(file_contents):
    print("--- Begin report of books/frankenstein.txt ---")
    count = word_count(file_contents)
    print(f"{count} words found in the document")
    print("\n")
    character_count(file_contents)
    print("--- End report ---")


def word_count(file_contents):
    return len(file_contents.split())


def character_count(file_contents):
    lowered_file_contents = file_contents.lower()

    dict_of_chars = {}
    for c in lowered_file_contents:
        if c in dict_of_chars:
            dict_of_chars[c] += 1
        else:
            dict_of_chars[c] = 1
    
    list_of_chars=[]
    for c in dict_of_chars:
        list_of_chars.append({"char":c, "num":dict_of_chars[c]})
    
    list_of_chars.sort(reverse=True, key=sort_on)
    for item in list_of_chars:    
        if(item["char"].isalpha()):
            item_char = item["char"]
            item_num = item["num"]
            print(f"The '{item_char}' character was found {item_num} times")

def sort_on(dict):
    return dict["num"]
        
main()
