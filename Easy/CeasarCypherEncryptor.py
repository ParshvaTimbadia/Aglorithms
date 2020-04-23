***
The Caesar Cipher technique is one of the earliest and simplest method of encryption technique. It’s simply a type of substitution cipher, i.e., each letter of a given text is replaced by a letter some fixed number of positions down the alphabet. For example with a shift of 1, A would be replaced by B, B would become C, and so on. The method is apparently named after Julius Caesar, who apparently used it to communicate with his officials.

Thus to cipher a given text we need an integer value, known as shift which indicates the number of position each letter of the text has been moved down.

The encryption can be represented using modular arithmetic by first transforming the letters into numbers, according to the scheme, A = 0, B = 1,…, Z = 25. Encryption of a letter by a shift n can be described mathematically as.


In this problem we are converting xyz==> zab
So bascially we are only using lower cases. 
Please have a look at the solution. 
Also Note: ord function in python gives us ASCII value of an character and chr function in python gives back the character from the ASCII number.


***

def caesarCipher(s, k):

    newLetters=[]
    newkey = k % 26
    
    #Newkey is generated incase if the key value exceed more than 26.

    for letter in s:
        newLetters.append(getnewLetter(letter, newkey))
    
    return "".join(newLetters)

def getnewLetter(letter, newKey):
    newLetterCode= ord(letter)+newKey

    if newLetterCode <= 122:
        return chr(newLetterCode)
    else:
        return chr(96+ (newLetterCode%122))
