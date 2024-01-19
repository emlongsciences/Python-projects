#This script converts Spanish words to IPA by loading a dictionary containing a few spanish words and their ipa conversions.
#It requests text input from the user and converts the text to ipa by referencing the dictionary and 
#printing the converted text

#this script optionally writes a dct file of a small dictionary containing a few spanish words and their ipa conversions
#this can be activated by removing # from the write_dct function


import pickle #imports package for writing and reading dictionary files

def main(): #main function which contains all other functions
 convert() #function that converts words to IPa

def convert():
  #this function converts text input by user into IPA by using text as keys in dictionary to access values of IPA conversion

  #write_dct()
  esp_ipa = load_dct()
  text_input = get_text_input()
  tokens = tokenise(text_input)
  for token in tokens:
    print(esp_ipa[token] + " ")
  
#def write_dct():
  #file = open("espdictionary.dct", "wb")
  #dict_to_file = {"El":"el", "perro":"pero", "corre":"kore", "pero":"peɾo", "la":"la", "gata":"gata", "camina":"kamina"}
  #pickle.dump(dict_to_file, file)
  #file.close()


def load_dct(): #loads .dct file in as dictionary
  with open('espdictionary.dct', 'rb') as read_file:
    data = read_file.read()
  esp_ipa = pickle.loads(data)
  return(esp_ipa)


def get_text_input(): #gets text input from user to look up in IPA dictionary
  text_input = input("Enter text: ")
  return(text_input)


def tokenise(text_input): #splits text input by token
  tokens = text_input.split()
  return(tokens)


if __name__ == "__main__":
  main()
else:  # this is the boilerplate
  print("Script can only run as a package.")
