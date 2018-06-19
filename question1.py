def sortString(s,t):
    split_word = []
    for i in s:
        split_word.append(i)
    num = 0
    new_string = ""
    

    for i in t:
        for ii in s:
            amount = split_word.count
            if i == ii and i not in new_string:
                if amount(i) > 1:
                    new_string = new_string + i*amount(i)
                else:
                    new_string = new_string + i
    print new_string.count('o'), 22
    return new_string


print sortString('autonomy','astrology')


