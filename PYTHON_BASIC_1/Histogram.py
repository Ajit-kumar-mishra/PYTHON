            
   
def histogram(item):
    for n in item:
        result = ''
        num = n
        while(num > 0):
            result = result + '*'
            num = num-1
        print(result)
            
histogram([2,4,6,8,10,8,6,4,2])