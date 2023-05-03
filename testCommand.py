# Python program to find the first
# repeated character in a string
def firstRepeatedChar(str):
 
    h = {} # Create empty hash
 
    # Traverse each characters in string
    # in lower case order
    for ch in str:
 
        # If character is already present
        # in hash, return char
        if ch in h:
            return ch;
 
        # Add ch to hash
        else:
            h[ch] = 0
            print(h)
# Driver code
print(firstRepeatedChar("gegeksforgeeks"))