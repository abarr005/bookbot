
def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read() # read file into the variable
        return file_contents # print the contents

def count_words(book):
    word_list = book.split()
    return len(word_list)

def count_char(book_words):
    count_dict = {} # our new dictionary
    lower_case = book_words.lower() # convert to lower case
    unique_list = list((set(lower_case))) # unique list of characters
    for item in unique_list:
        if item.isalpha():
            count_dict[item] = lower_case.count(item)
    return count_dict

full_text = main()
word_count = count_words(full_text)
char_list = count_char(full_text)

print("--- Begin report of books/frankenstein.txt ---")
print(f'{word_count} words found in the document\n')

sorted_char = sorted(char_list.items(), key=lambda item: item[1], reverse=True)

for key, value in sorted_char:
    print(f"The '{key}' character was found {value} times")

print("--- End report ---")

