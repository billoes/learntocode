def is_palidrome(word):
    if len(word) <= 1:
        return True
    else:
        first = word[0]
        last = word[-1]
        middle = word[1:-1]
        if first == last:
            return is_palidrome(middle)
        else:
            return False


check = is_palidrome('radar')
print(check)

