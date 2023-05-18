QUESTIONS:-1. Create one variable containing following type of data.
(i) string.
(ii) list.
(iii) float.
(iv) tuple.

(i) string
a = "Rohit Raj"
print(a)
print(type(a))


(ii) list
b = [2,3,4,5,6,"Rohit",34.1415,True,]
print(b)
print(type(b))


(iii) float
c = 34.1415
print(c)
print(type(c))


(iv) Tuple
d = (20,'Rohit',35.75,[30,60,90])
print(d)
print(type(d))



QUESTION:-2. Given are some following variables containing data.
(i) var1=''
(ii) var2='[DS,ML,Python]'
(iii) var3=['DS','ML','Python']
(iv) var4=1.
What will be the data type of the above given variable.


(i) var1 =''
print(type(var1))
print(var1)


(ii) var2='[DS,ML,Python]'
print(type(var2))
print(var2)


(iii) var3=['DS','ML','Python']
print(type(var3))
print(var3)


(iv) var4=1
print(type(var4))
print(var4)




QUESTION:-3. Explain the use of the following operators using an example.
(i) /
(ii) %
(iii) //
(iv) **


(i) / - Division sign.
This operator is used to divide two values and define to float value.
print(10/5)
print(int(10/5))


(ii) % - Modulus sign.
This operator is used to modulus divide two values.
print(10%3)
print(float(10%3))



(iii) // - Floor division sign.
This operator is used to divide two values and define to integer value.
print(10//5)



(iv) ** - Exponentiation sign.
This operator is used to define power of the two values.
print(5**3) # 5 ka power 3 is called 125.
print(2**3) # 2 ka power 3 is called 8.




QUESTION:-4. Create a list of length 10 of your choice containing multiple types of data. using for loop print the element and its data type.
l = [2,3,4,5,6,'Rohit Raj',"pwskills",34.1415,True,[1,2,3,4,5]]
for i in l :
     print(l)
     print(type(i))




QUESTION:-5. Using a while loop, verify if the number A is purely divisible by number B and if so then how many times it can be divisible.
A = int(input("Enter A:"))
B = int(input("Enter B:"))
count = 0

while A % B == 0:
    count += 1
    A //= B

    if count > 0:
        print(f"{A} is divisible by {B} exactly {count} times.")
    else: 
        print(f"{A} is not divisible by {B}.")    




QUESTION:-6. Create a list containing 25 int type data. using for loop and if-else condition print if the element is divisible by 3 or not.

l = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
for i in l :
    if(i%3==0):
        print("The number is divisible by 3")
        print(i)
    else: 
         print("The number is not divisible by 3")    
         print(i)





QUESTION:-7. What do you understand about mutable and immutable data types?give examples for both showing this property.


Mutable Data Types:- The ability of objects to change their values.
Example:-
l = [2,3,4,5,6,'Rohit',"pwskills",True,34.1415,False]
l[0] = 200
l[1] = 300
l[2] = 400
l[3] = 500
l[4] = 600
l[5] = "Raj"
l[6] = 'skill'
l[7] = False
l[8] = 3.13
l[9] = True
print(l)


Immutable Data Types:- The ability of objects do not change their values.
Example:-
s = "Rohit"
s[0] = "t"
print(s)
