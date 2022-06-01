#print number of each charaters present in given statement

def count_letter(statement):
    result={}
    for item in statement:
        if item not in result:
            result[item] = 0
        result[item] +=1
    return result

print(count_letter("avinash"))
    
