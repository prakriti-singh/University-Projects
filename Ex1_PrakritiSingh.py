import math
pi = math.pi
def MyArcTan(x,N):  #Function to calculate arctan
        n= 0
        sum = 0
        while n <= N:
                sum += ((((-1)**n) * (x**((2*n)+1))) / ((2*n) + 1)) 
                n+=1    
        return sum 
def  FinalAnswer(x,N): #Funtion to calculate arctan for different values of x
    if abs(x) <= 1:
            final = (MyArcTan(x,N)) 
    elif abs(x) > 1:
        if x>0:
            final = ((pi/2) - MyArcTan((1/x),N)) 
        elif x<0:
            final = (-(pi/2) - MyArcTan((1/x),N))
    return final
        
MyInput = '0'
while MyInput != 'q':
   
    MyInput = input('Enter a choice, "a", "b" or "q" to quit: ')
    print('You entered the choice: ',MyInput)

    if MyInput == 'a':
        print('You have chosen part (a)')
        Input_x = input('Enter a value for x (floating point number): ')
        x = float(Input_x)
        #Next piece of code makes sure user enters an Integer and a positive value
        while True:
            Input_N = input('Enter a value for N (positive integer): ')
            if Input_N.isdigit():
                N = int(Input_N)
                break
        print ('Arctan(', x, ') = ', FinalAnswer(x,N))    
  
    elif MyInput == 'b':
        print('You have chosen part (b)')
        x=2
        #Next piece of code makes sure user enters an Integer and a positive value
        while True: 
            Input_N = input('Enter a value for N (positive integer): ')
            if Input_N.isdigit(): 
            #isdigit() checks if all the characters in the string are digits, a negative sign and a decimal point are considered non-digits
                N = int(Input_N)
                break
        print (' x    | MyArctan function ans | Arctan funtion ans    | Difference')
        while x <= 2 and x>=(-2):
                difference = abs(FinalAnswer(x,N) - math.atan(x))
                print (x, " "*(4-len(str(x))),'|',(FinalAnswer(x,N))," "*(20-len(str(FinalAnswer(x,N)))),'|', math.atan(x)," "*(20-len(str(math.atan(x)))),'|', difference, " "*(20-len(str(difference))))
                x-=0.1 #decreases the value of x by 0.1
                x = round(x,1) #rounds the float value of x to one digit
                
    elif MyInput != 'q':
        print('This is not a valid choice')

print('You have chosen to finish - goodbye.')