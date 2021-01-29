# py3

def RLE(input):
    return recursive(input, len(input))
        
        
def recursive(input, str_len, curr_char=0, next_char=1, count=1):
    if str_len == 0:
        return input
    if input[curr_char] == input[next_char]:
        return recursive(input, str_len, curr_char, next_char+1,  count+1)
    else:
        new_str = input[next_char:] + input[curr_char] + str(count)
        return recursive(new_str, str_len-count, 0, 1, 1)
            
            
print(RLE("AAABBBCCCDDXZ"))

# expected output: A3B3C3D2X1Z1
