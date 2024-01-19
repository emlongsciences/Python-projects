#summary: reads lorem.txt and creates a dictionary of bigram frequencies by counting tuples made from bigrams


def main():
  #open text file and make into string
  with open("lorem.txt") as file:
        text = file.read()
  word_list = text.split() #splits the text
  previous_word = "^" #first counter because no previous word when indexing first word
  bigram_freqs = dict() #create empty dictionary to store bigrams and frequency counts
  #loops through text and makes tuples of bigrams while counting frequencies
  for word in word_list:
     bigram_tuple = (previous_word, word) #bigram
     if bigram_tuple in bigram_freqs:
      bigram_freqs[bigram_tuple] += 1 #adds to frequency count if current bigram is already in dictionary
     else: 
      bigram_freqs[bigram_tuple] = 1 #adds a 1 if current bigram not found in dictionary
     previous_word = word #sets previous word for next loop
  print(bigram_freqs)    #prints dictionary of bigrams with their frequency counts

#biolerplate
if __name__ == "__main__":
  main()
else:
  print("Script can only run as a stand-alone.")


    