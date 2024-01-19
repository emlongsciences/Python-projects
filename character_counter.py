def main():
    #open and read file as string
    with open("lorem.txt") as file:
        text = file.read()
    #loop through string to count character frequencies and print them
    word = text.split(text)
    for word in text:
        char_freq_pair = word + " " + str(text.count(word))
        print(char_freq_pair)    

if __name__ == "__main__":
    main()






