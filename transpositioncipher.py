block_size = int(input("Enter Blocksize: "))    #gain size of block

print("Please enter correct order of the blocks")
print("Remember that the first character is 0, not 1.")

block_order = [''] * block_size                 #make block order list
for a in range(block_size):      #gain correct order within block
    block_order[a] = int(input(f"Position {a} goes to: "))

ciphertext_s = input("Input Ciphertext: ")
ciphertext = ciphertext_s.replace(" ", "")      #remove all spaces

def transposition_cipher(text, block_size, block_order):
    reordered_text = ""
    
    for b in range(0, len(text), block_size):
        block = text[b:b + block_size]      #get a block of text of block_size length
        block = block.ljust(block_size)     #pad the block with spaces if its not complete
        
        reordered_block = [""] * block_size     #make a blank list with block_size terms
        
        for original_index, new_index in enumerate(block_order):    #reordering block
            reordered_block[new_index] = block[original_index]      
           
        reordered_text += ''.join(reordered_block)  #adds the newest reordered block to the final text
        
    return reordered_text
    
original_text = transposition_cipher(ciphertext, block_size, block_order)
print("Original Text:")
print(original_text)

z = input("Press enter to exit.")