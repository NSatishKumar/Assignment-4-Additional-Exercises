# Palindrome function 
 
def isPalindrome(stg): 
    rev = stg[::-1]       # Reversing the string
    if (stg == rev):      # Checking the strings
        return "It is a Palindrome"
    return "It is not a Palindrome"
