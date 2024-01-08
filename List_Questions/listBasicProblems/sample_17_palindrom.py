s=121
low=0
is_palindrome=True
upper=len(str(s))-1
for i in range(len(str(s))):
    if str(s)[low]!=str(s)[upper]:
        print("not palindrome")
        is_palindrome=False
        break
    low+=1
    upper-=1
if is_palindrome:
    print("string is palindrome")