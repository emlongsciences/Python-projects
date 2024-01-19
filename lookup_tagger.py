# this script reads in a training file which contains words and their parts of speech by
# extracting word pairs for the file and then compares the end of the file with the rest of the file
# by requesting a word from the user and returns TRUE if the pos in the training and test dictionaries for that word match

# import PACKAGE 
import pickle as pickle

def main ():
   # makes two objects for the file to be dealt with by either the training or test dictionary
   conllu_file_object = open("en_gum-ud-train.conllu", "r", encoding= "utf-8")
   conllu_file_object2 = open("en_gum-ud-train.conllu", "r", encoding= "utf-8")
   # extract words and their pos for file and creates training and test dictionaries
   pos_dict_train = extract_word_pos_pairs_train(conllu_file_object)
   pos_dict_test = testing(conllu_file_object2)
   # saves dictionaries to files
   save_dct_to_file(pos_dict_train)
   save_dct_to_file(pos_dict_test)
   #compares pos for a given term between training and test dictionaries
   query_pos(pos_dict_train, pos_dict_test)
   
   
   
   

# create dictionary of words and their pos for first two thirds of file
def extract_word_pos_pairs_train(conllu_file_object):
  pos_dict_train = dict()
  line_count = 0
  for line in conllu_file_object:
    line_count = line_count + 1
  for line in conllu_file_object:
     line_elements = line.split("\t")
     c = c + 1
     if len(line_elements) > 3:
        if c < (.8 * line_count):
          word = line_elements[1]
          pos = line_elements[3]
          pos_dict_train[word] = pos
  return(pos_dict_train)

# create dictionary of words and their pos for last third of file  
def testing(conllu_file_object2):
  pos_dict_test = dict()
  c = 0
  for line in conllu_file_object2:
     line_elements = line.split("\t")
     c = c + 1
     if len(line_elements) > 3:
        if c > 125000:
          word = line_elements[1]
          pos = line_elements[3]
          pos_dict_test[word] = pos
  return(pos_dict_test)

#save training dictionary to file using pickle dump
def save_dct_to_file(pos_dict_train):
  with open('posdict.pkl', 'wb') as fp:
    pickle.dump(pos_dict_train, fp)
  fp.close

#save test dictionary to file using pickle dump
def save_dct_to_file(pos_dict_test):
  with open('posdict.pkl', 'wb') as fp:
    pickle.dump(pos_dict_test, fp)
  fp.close

#returns logical statement of a match between pos in training and test dictionary for word input by user
def query_pos(pos_dict_train, pos_dict_test):
  term = input("enter word")
  print(pos_dict_train[term] == pos_dict_test[term])


#biolerplate
if __name__ == "__main__":
  main()
else:
  print("Script can only run as a stand-alone.")