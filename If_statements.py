

#Use "or"

x=10
if x>5 or x<5:
  print("hello world")


x=42
if x>1:
 print ("more than one")
if x<100:
 print ("less than 100")
 print ("all done")


#if statement with "value"
S = 80
K = 50

if S>K:
   value = S-K
   print("The value of the asset is" + str(value))
else:
   value=0
   print("The value of the asset is" + str(value))

#result and print result
x, y = 100, 100
if x < y:
        result = "x is less than y"
elif x == y:        #use elif for additional condition
        result = "x is the sam as y"        
else:               #this is for everything else
        result = "x is greater than y"
        print (result)

#if in the result

x, y = 110, 100
result = "x is less than y" if x < y else "x is greater or equal to y"
print (result)

x, y = 110, 100
print("x is less than y" if x<y else "x is greater or equal to y")