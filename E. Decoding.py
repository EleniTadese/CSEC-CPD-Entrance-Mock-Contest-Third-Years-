def decode_encoded_word(n, s):
    result = []
    
    # We will rebuild the original word from the encoded string
    for i in range(n):
        if i % 2 == 0:  # For even indices, add to the front
            result.insert(0, s[i])
        else:           # For odd indices, add to the back
            result.append(s[i])
    
    return ''.join(result)

# Read inputs
n = int(input().strip())
s = input().strip()

# Decode the word
decoded_word = decode_encoded_word(n, s)

# Output the result
print(decoded_word)