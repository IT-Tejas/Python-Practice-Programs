def diff(a,b):
    result=[]
    for i in a:
        if i not in b:
            result.append(i)
    return result
