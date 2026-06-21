def message():
    print("Type encrypt for encryption or decrypt for description")
    user = str(input("Enter your choice :"))
    opt = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", 
        "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z" ]
    enc = ""
    if user=="encrypt":
        send=str(input("Enter your message that you want to send:"))
        shift=int(input("Enter your shift number:"))
        encrypted=""
        for i in range(len(send)):
            if send[i] in opt:
                ind=(ord(send[i])-ord('a'))
                encryption=(ind+shift) % 26
                encrypted+=opt[encryption]
            else:
                encrypted += send[i]
        print(f"Here is the encrypted result {encrypted}")
    
    x = str(input(("Type yes if you want to go again , otherwise no :")))
 
    if x=="yes":
       y=str(input(("Type encrypt for encryption or decrypt for description :"))) 
       if y == "encrypt":
            send=str(input("Enter your message that you want to send:"))
            shift=int(input("Enter your shift number:"))
            encrypted=""
            for i in range(len(send)):
                if send[i] in opt:
                   ind=(ord(send[i])-ord('a'))
                   encryption=(ind+shift) % 26
                   encrypted+=opt[encryption]
                else:
                   encrypted += send[i]
            print(f"Here is the encrypted result {encrypted}")
           
       elif y == "decrypt":
            print("Enter the recieved decrypted message here to know message")
            receive=str(input("Enter your received message to know correct text :")) 
            shift=int(input("Enter the shift value :"))
            decrypted=""
            for i in range(len(receive)):
                if receive[i] in opt:
                   ind=(ord(receive[i])-ord('a'))
                   decryption=(ind-shift)
                   if decryption < 0:
                      decryption+=26
                   decryption_1=decryption % 26
                   decrypted+=opt[decryption_1]
                else:
                    decrypted += receive[i]
                
            print(f"The decrypted message is  {decrypted}" )
    else:
        print("You have choosen {x}")                    
    print("Thank you , for choosing us ")
                                                    
message()          
            
        
        