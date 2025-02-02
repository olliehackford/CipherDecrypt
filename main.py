def transposition(text_s, block_size):
    text = text_s.replace(" ", "") 

    block_order = [''] * block_size                 #make block order list
    for a in range(block_size):      #gain correct order within block
        block_order[a] = int(input(f"Position {a} goes to: "))

    reordered_text = ""
    
    for b in range(0, len(text), block_size):
        block = text[b:b + block_size]      #get a block of text of block_size length
        block = block.ljust(block_size)     #pad the block with spaces if its not complete
        
        reordered_block = [""] * block_size     #make a blank list with block_size terms
        
        for original_index, new_index in enumerate(block_order):    #reordering block
            reordered_block[new_index] = block[original_index]      
           
        reordered_text += ''.join(reordered_block)  #adds the newest reordered block to the final text
        
    return reordered_text

###################################################################################################################################################################################

def vigenere(text_s, key_c):
    key = [ord(char.lower()) - ord("a") for char in key_c]
    text = text_s.replace(" ", "")

    reordered_text = ""
    text_list = list(text)
    reordered_block = [""] * len(key)

    for a in range(0, len(text), len(key)):

        for b in range(len(key)):

            if (a + b) < len(text):
                new_letter_number = (ord(text_list[a+b].lower()) - ord("a")) - key[b]   #number of current letter in text - key increment

                if new_letter_number > 25:
                    new_letter_number = new_letter_number - 26          #ensuring number corresponds to letter correctly
                if new_letter_number < 0:
                    new_letter_number = new_letter_number + 26

                reordered_block[b] = chr(new_letter_number + ord("a"))

            else:
                reordered_block[b]= ""

        reordered_text += ''.join(reordered_block)

    reordered_text_u = reordered_text.upper()
    return reordered_text_u

####################################################################################################################################################################################

def start():
    print("1: Transposition Cipher")
    print("2: Vigenere Cipher")
    ans = input("Please select what type of cipher you would like to decrypt: ")

    if ans == "1":
        print("Transposition selected.")
        ciphertext = input("Please input ciphertext: ")
        block_size = int(input("Please enter block size: "))
        print("Transposed text:")
        print(transposition(ciphertext, block_size))

    elif ans == "2":
        print("Vigenere selected.")
        ciphertext = input("Please input ciphertext: ")
        key = input("Enter key: ")
        print("Transposed text:")
        print(vigenere(ciphertext, key))

    else:
        print("Input not recognised, please try again.")
        start()

#####################################################################################################################################################################################

start()
