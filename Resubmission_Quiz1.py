def has_seven(k,target):  
    if not k:  
        return False 
    else:  
        if( (k % 10 == target) + has_seven(k // 10,target) > 0):
            return True
        return False
        

print(has_seven(7,7))
print(has_seven(123, 7))

