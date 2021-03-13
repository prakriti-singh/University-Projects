#author: Prakriti Singh
import math
import matplotlib.pyplot as plt
pi = math.pi
e = math.e
h = 7640 
drag_coeff = 1.15 #taking average of given values in the question
rho = 1.2 #given in question
A = 0.45 #cross sectional area of a person given that their height is 1.5m and width is 0.3 m
gravity = 9.81
#function for analytical height calculation
def y_calculation(time,k,mass):
    yo = 1000
    coshval = math.cosh((math.sqrt((k*gravity)/mass))*time)
    y = yo - ((mass/k) * (math.log(coshval, e)))
    return y
#function for analytical velocity calculation  
def Vy_calculation (time,k,mass):
    Vy = -(math.sqrt((mass*gravity)/k)) * math.tanh((math.sqrt((k*gravity)/mass))*time)
    return Vy
#function for plotting for part a       
def plotting(time,k,mass):
     plot_y = []
     plot_Vy = []
     t = 0.000
     plot_time = []
     plot_Vy.append(Vy_calculation(0,k,mass))
     plot_y.append(y_calculation(0,k,mass))
     plot_time.append(0.0)
      
     while t <= time:
        t = t + 0.5
        plot_time.append(t)
        plot_Vy.append(Vy_calculation(t,k,mass))
        plot_y.append(y_calculation(t,k,mass))
     
     plt.figure(1)
     plt.plot(plot_time,plot_y)
     plt.xlabel("Time (s)")
     plt.ylabel("Height (m)")
     plt.grid()
     plt.figure(2)
     plt.plot(plot_time,plot_Vy)
     plt.xlabel("Time (s)")
     plt.ylabel("velocity (m/s)")  
     plt.grid()
     plt.show()         
#function for calculation of velocity and height and plotting graphs for both parts c and d
def c_and_d(time, mass, area, yo, Cd, rho):
    euler_y = []
    euler_Vy = []
    plot_time = []
    euler_y.insert(0,yo)
    euler_Vy.append(0)
    sound_barrier = []
    sound_barrier.append(-343)
    rhoy = 0
    ky = 0
    ran  = int(time/0.01)
    i = 0
    while i <= ran:
        rhoy = rho * (math.exp((-euler_y[i]/h)))
        ky = (Cd * rhoy * A)/2.00
        i = i + 1
        euler_Vy.append((euler_Vy[i-1]) - (0.01*(gravity + ((ky/mass)*abs(euler_Vy[i-1])*euler_Vy[i-1]))))
        euler_y.append(euler_y[i-1] + ((0.01)*euler_Vy[i-1]))
        sound_barrier.append(-343) #making a list for sound barrier to plot
        
    print ("y = ", euler_y[i], " m and final Vy = ", euler_Vy[i],"m/s and maximum velocity reached is ", abs(min(euler_Vy)), " m/s")
     
    plot_y = euler_y
    plot_Vy = euler_Vy
    t = 0.000
    plot_time.append(t)
    while t <= time:
        t = t + 0.01
        t = round(t,3)
        plot_time.append(t)
    
    plt.figure(7)
    plt.ylim(0,yo)
    plt.plot(plot_time,plot_y)
    plt.xlabel("Time (s)")
    plt.ylabel("Height (m)")
    plt.grid()
    plt.figure(8)
    plt.plot(plot_time,plot_Vy, label = "Velocity")
    plt.plot(plot_time, sound_barrier, label = "Sound barrier")
    plt.xlabel("Time (s)")
    plt.ylabel("velocity (m/s)")
    plt.legend()
    plt.grid()
    plt.show() 

MyInput = '0'
while MyInput != 'q':
    plt.close()
    plt.clf()
    print ("a = analytical calculation of y and Vy , b = y and Vy calculation using Euler method , c = calculation of Vy and y using variable air density, d = playing around with different jump parameters , q = quit")
    MyInput = input('Enter a choice, "a", "b", "c", "d" or "q" to quit: ')

    if MyInput == 'a':
        mass = 75
        time = input("Please enter time in seconds: ")
        time = float(time)
        k = (drag_coeff * rho * A)/2
        print ("y = ", y_calculation(time,k,mass), "and Vy = ", Vy_calculation(time,k,mass))
        
        plotting(time,k,mass)
        k=0.000
        time = 0.0000    
        
    elif MyInput == 'b':
        k = (drag_coeff * rho * A)/2
        mass = 75 
        t = 0.000
        time = 0.0000 
        euler_y = []
        euler_Vy = []   
        plot_time = []
        analytical_y = []
        analytical_Vy = []
        analytical_y = []
        plot_time.append(0)
        
        time = input("Please enter time in seconds: ")
        time = float(time)
        step_time = input("Please enter step time in seconds: ")
        step_time = float(step_time)
        
        euler_y.insert(0,1000)
        euler_Vy.append(0)
        analytical_Vy.append(0)
        analytical_y.insert(0,1000)
        ran = (int(time/step_time)) + 1 #range for the 'for loop' for Eulers method
        
        while t < time:
            t = t + step_time
            t = round(t,3)
            plot_time.append(t)
    
        for i in range(1, ran): # Eulers method calculation
            euler_Vy.append((euler_Vy[i-1]) - (step_time*(gravity + ((k/mass)*abs(euler_Vy[i-1])*euler_Vy[i-1]))))
            euler_y.append(euler_y[i-1] + (step_time*euler_Vy[i-1]))
            analytical_Vy.append(Vy_calculation(plot_time[i],k,mass))
            analytical_y.append(y_calculation(plot_time[i],k,mass))
            
        plot_y = euler_y
        plot_Vy = euler_Vy
        
        plt.figure(3)
        plt.ylim(0,1000) #limits plot to 0m (ground)
        plt.plot(plot_time,plot_y, label = "Eulers Method")
        plt.plot(plot_time, analytical_y, label = "Analytical method")
        plt.xlabel("Time (s)")
        plt.ylabel("Height (m)")
        plt.legend()
        plt.grid()
        plt.figure(4)
        plt.plot(plot_time,plot_Vy, label = "Eulers Method")
        plt.plot(plot_time, analytical_Vy, label = "Analytical method")
        plt.xlabel("Time (s)")
        plt.ylabel("velocity (m/s)")
        plt.grid()
        plt.legend()
        plt.show() 
        plt.clf()
        if euler_y[ran-1] > 0.0:
            print ("Using Eulers method y = ", euler_y[ran-1], " m and Vy = ", euler_Vy[ran-1], " m/s")
        else:
            print ("Using Eulers method y = 0 m and Vy = ", euler_Vy[ran-1], " m/s")
        
        print ("Using analytical method y = ", y_calculation(time,k,mass), "and Vy = ", Vy_calculation(time,k,mass))
        print ("If only one plot is seen that means Euler values are very similar to Analytical values due to small step time")
        #Taking in user mass to vary k/m to see how it would affect velocity and height
        user_mass = input ("Please enter a mass in kg: ") 
        user_mass = float(user_mass)
    
        euler_y = []
        euler_Vy = []
        euler_y.insert(0,1000)
        euler_Vy.append(0)
        for i in range(1, ran):
            euler_Vy.append((euler_Vy[i-1]) - (step_time*(gravity + ((k/user_mass)*abs(euler_Vy[i-1])*euler_Vy[i-1]))))
            euler_y.append(euler_y[i-1] + (step_time*euler_Vy[i-1]))
        plot_y = euler_y
        plot_Vy = euler_Vy
        
        plt.figure(5)
        plt.ylim(0,1000) #limits plot to 0m
        plt.plot(plot_time,plot_y)
        plt.xlabel("Time (s)")
        plt.ylabel("Height (m)")
        plt.grid()
        plt.figure(6)
        plt.plot(plot_time,plot_Vy)
        plt.xlabel("Time (s)")
        plt.ylabel("velocity (m/s)")
        plt.grid()
        plt.show() 
        
        if euler_y[ran-1] > 0.0:
            print ("Using Eulers method y = ", euler_y[ran-1], " m and Vy = ", euler_Vy[ran-1], " m/s")
        else:
            print ("Using Eulers method y = 0 m and Vy = ", euler_Vy[ran-1], " m/s")
        
    elif MyInput == 'c':
        time = input("Please enter time in seconds: ")
        time = float(time)
        mass = 118 #Felix's mass (73kg) + mass of his suit (45kg)
        area = 0.51 #Approximation of Felix's surface area
        yo = 39045 # height Felix jumped from
        c_and_d(time, mass, area, yo, drag_coeff, rho)
         
    elif MyInput == 'd':
        time = input("Please enter time in seconds: ")
        time = float(time)
        user_mass2 = input("Please enter mass in kgs: ")
        user_mass2 = float(user_mass2)
        surface_area = input("Please enter surface_area: ")
        surface_area = float(surface_area)
        initial_height = input("Please enter initial height in meters: ")
        initial_height = float(initial_height)
        Cd = input("Please enter drag coefficient: ")
        Cd = float(Cd)
        density = input("Please enter air density: ")
        density = float(density)
        
        c_and_d(time, user_mass2, surface_area, initial_height, Cd, density)
                
    elif MyInput != 'q':
        print('This is an invalid choice')

print('Program terminated')