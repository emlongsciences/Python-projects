def main():
    #Have user enter base 10 number
    numStore = int(input("Enter an integer to convert to another base: "), base = 10)
    #Offer the user options for base conversion
    baseStore = int(input("Select a base (2) (6) (8): "))
    #Convert number based on selection
    if baseStore == 2:
            print(bin(numStore))
    if baseStore == 6:
            print(hex(numStore))
    if baseStore == 8:
            print(oct(numStore))
    
        
      

if __name__ == "__main__":
    main()


 