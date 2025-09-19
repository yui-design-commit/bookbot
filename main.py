import sys
from stats import get_num_words, get_char_dict

def main():

  if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
  else:
     book_path = sys.argv[1]



  
  book_text = get_book_text(book_path)
  char_dict = get_char_dict(book_text)
  num_words = get_num_words(book_text)

  #print(char_dict['t'])
  #print(char_dict['p'])
  #print(char_dict['c'])

  print("============ BOOKBOT ============")
  print(f'Analyzing book found at {book_path}...')
  print("----------- Word Count ----------")
  print(f'Found {num_words} total words')
  print("--------- Character Count -------")
  for item in char_dict:
        if item["name"].isalpha() != True:
            continue
        print(f'{item["name"]}: {item["num"]} \n')

def get_book_text(book_path):
    with open(book_path) as f:
      return f.read()

main()