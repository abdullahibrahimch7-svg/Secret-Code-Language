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
            
            # If the length of the word is greater than 2, move the first character to the end.            
            
            elif((len(reply2)>2)):
                letters = "zxcvbnmlkjhgfdsaqwertyuiop"
                a = random.choice(letters)
                s = random.choice(letters)
                e = random.choice(letters)
                d = random.choice(letters)
                b = random.choice(letters)
                c = random.choice(letters)
                reply3 = reply2[1:] + reply2[0]

                # Reverse the whole word
                
                replyr = reply3[::-1]

            # Then add 3 random characters at the beginning and 3 at the end.                
                
                print("Your Encrypted word is :",a+s+e + replyr + b+d+c)
    # Decryption process

        elif(reply == 2):
            reply4 = (input("Enter the word to decode :"))

        # Move the last character back to the beginning to restore the original word.            
            
            if (len(reply4) < 3):
                print("Your decoded word is :",reply4[::-1])

        # Move the last character back to the beginning to restore the original word.            
            
            elif(len(reply4) > 2):
                reply5 = reply4[3:]
                reply6 = reply5[:-3]

                # It reverse the word to restore the original word
                
                reply8 = reply6[::-1]
                
            # Move the last character to the beginning to restore the original word.                
                
                reply7 = reply8[-1] + reply8[:-1]
                print("Your Decoded word is :",reply7)
        
        elif(reply == 3):
            break
    except Exception:
        print("Invalid operation.Try again")
