import random

while True:
    try:
        reply =int(input("1.Encode\n2.Decode\n3.Exit\nEnter 1,2 or 3 :"))
    # Encryption process

        if reply == 1:
            reply2 = (input("Enter the word to Encrypt :"))
            
            # if the length of encryption word is smaller than 3 then it simply reverse the word  
            
            if len(reply2) < 3:
                print("Your Encrypted word is :",reply2[::-1])   
            
            # if the length of the word is greater than 2 then it will remove the first word and add it to the last
            
            elif((len(reply2)>2)):
                letters = "zxcvbnmlkjhgfdsaqwertyuiop"
                a = random.choice(letters)
                s = random.choice(letters)
                e = random.choice(letters)
                d = random.choice(letters)
                b = random.choice(letters)
                c = random.choice(letters)
                reply3 = reply2[1:] + reply2[0]

                # then it add 3 random digits at first and 3 random digits at last
                
                print("Your Encrypted word is :",a+s+e + reply3 + b+d+c)
    # Decryption process

        elif(reply == 2):
            reply4 = (input("Enter the word to decode :"))

            # if the length of the encrypted word is smaller than 3 than it simply reverse the word
            
            if (len(reply4) < 3):
                print("Your decoded word is :",reply4[::-1])

                # if the length of the word is greater than 3 then it firstly remove 3 digits from first and 3 digits from the last
            
            elif(len(reply4) > 2):
                reply5 = reply4[3:]
                reply6 = reply5[:-3]

                # if the length of the word is greater than 3 then it firstly remove the last word add it to the first
                
                reply7 = reply6[-1] + reply6[:-1]
                print("Your Decoded word is :",reply7)
        
        elif(reply == 3):
            break
    except:
        print("Invalid operation")