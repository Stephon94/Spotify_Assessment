##2[d4[f3[ab]]]
##2[d4[f3[g2[ab]]]]

def decodeString(s):
    string = s.replace("]", "").split("[")
    string = "".join(string)
    string = list(string)
    
    for i in range(len(string)-1,-1,-1):
            try:
                    string[i] = int(string[i])
                    string[i] = string[i] * string[i+1]
            except:
                    try:
                            string[i] = string[i] + string[i+1]
                    except:
                            pass
    print s[0]

