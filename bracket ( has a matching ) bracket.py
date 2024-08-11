# Q. Write a function matched(s) that takes as input a string s and checks if the brackets "(" and ")" in s are matched: that is, every "(" has a matching ")" after it and every ")" has a matching "(" before it. Your function should ignore all other symbols that appear in s. Your function should return True if s has matched brackets and False if it does not.

# Here are some examples to show how your function should work.

 
# >>> matched("zb%78")
# True
# >>> matched("(7)(a")
# False
# >>> matched("a)*(?")
# False
# >>> matched("((jkl)78(A)&l(8(dd(FJI:),):)?)")
# True


#------MY-SOLUTION------#
def matched(s):
    counter = 0
    for i in range(0, len(s)):
        if s[i] == "(":
            counter += 1
        elif s[i] == ")":
            counter -= 1
            if counter < 0:
                return False
    if counter == 0:
        return True
    else:
        return False
    
print(matched("((jkl)78(A)&l(8(dd(FJI:),):)?)"))