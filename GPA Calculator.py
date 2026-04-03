print("Hello")
x = 1
while x == 1:
    number_of_degrees = int(input("Enter your number of degrees:"))
    the_degees_and_courses = {}
    for i in range(number_of_degrees):
       the_key = input("Enter the name of the course:")
       the_value = int(input("Enter your degree:"))
       if 100 <the_value < 0:
           print("this not right")
           break
       the_degees_and_courses.update({the_key :the_value})
    y = 1
    for key, value in the_degees_and_courses.items():
        print(y,"-",key,":",value)
        y +=1
    the_totle = sum(the_degees_and_courses.values())
    the_rate = the_totle / len(the_degees_and_courses)
    print("your totale:",the_totle)
    print("your rate:",the_rate)
    exit
        

    
    