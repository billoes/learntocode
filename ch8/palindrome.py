def is_palidrome(word):
    if len(word) <= 1:
        return True
    else:
        if word[0] == word[-1]:
            return is_palidrome(word[1:-1])
        else:
            return False


check = is_palidrome('radar')
print(check)

