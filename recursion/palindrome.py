# def checkPalindrome(string,n):
#     if n == 0:
#         return string[n]
#     return string[n]+checkPalindrome(string,n-1)


# string = "geeks"
# print(checkPalindrome(string,len(string)-1))
# if string==checkPalindrome(string,len(string)-1):
#     print("yes")
# else:
#     print("no")

def checkPalindrome(string,s,e):
    if s>=e:
        return True
    return string[s] == string[e] and checkPalindrome(string,s+1,e-1)
    

print("yes" if checkPalindrome("abb",0,2) else "no")