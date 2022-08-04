def disemvowel(string_):
    new_string = str(string_)
    for letter in str(string_):
        if letter in 'aeiouAEIOU':
            new_string = new_string.replace(letter, '')
            # print(new_string)
        else:    
            # print('not: ', letter)
            pass
    # print(string_)
    return new_string

disemvowel('is letter')