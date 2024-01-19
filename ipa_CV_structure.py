#takes user input of english text and converts it to ipa then prints ipa conversion and CV structure

def main():
  
  #import english to ipa package
  import eng_to_ipa
  
  
  ipaVowel = {'ɪ', 'ʊ', 'ə', 'e', 'ɒ', 'ʌ', 'æ', 'i', 'u', 'ɑ', 'ɔ', 'ɜ', 'o', 'ɛ'} #create a set of ipa vowels
  userText = input("Enter English text for IPA conversion and CV structure: ") #request user input of english text
  
  #convert text to ipa and print
  userText = eng_to_ipa.convert(userText)
  print("IPA conversion: ", end= "")
  print(userText)
  
  #construct CV structure for text and print
  print("CV structure: ", end="")
  for character in userText:
    if character == "ˈ":
      pass
    elif character == " ":
      print(" ", end= "")
    elif character in ipaVowel:
        print("V", end="")
    else:
     print("C", end="")



# boilerplate
if __name__ == "__main__":
  main()
else:
  print("Script can only run as a stand-alone.")