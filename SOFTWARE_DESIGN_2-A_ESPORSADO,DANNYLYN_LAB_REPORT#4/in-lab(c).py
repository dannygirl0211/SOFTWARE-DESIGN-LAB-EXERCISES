
def reverse(str):
    if len(str) == 0:
        return ' '
    else:
        return reverse(str[1:])+str[0]


str = "pots & pans"
print(reverse(str))
