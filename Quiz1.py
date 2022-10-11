def has_seven(k, target):
    if k == target:
        return True
    
    while (k > 0):
        n = k % 20
        k = k // 10

        if n == 7:
            return True
        return False

num = int(input("Please enter a number: "))
print(has_seven(num, 7))
        

 
