'''
total = 0
for number in range(1, 10 + 1):
    print(number)
    total = total + number
print(total)
'''
'''
def add_numbers():
   total = 0
   for number in range(1, 10 + 1):
      print(number)
      total = total + number
   return(total)
answer=add_numbers()
print(answer)
'''
'''
def my_function(x,y):
    if x == 3:
        #print(x)
        return x
    else:
        return y
        #print(y)
my_function(12,3)
#print(x)
'''

def add_numbers(start,end):
    total=0
    for number in range(start,end+1):
        print(number)
        total=total+number
    return(total)
test1=add_numbers(1,100)
print(test1)
        
        
        
    

