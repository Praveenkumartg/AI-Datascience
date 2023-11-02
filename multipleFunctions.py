class multipleFunctions():
    def Numbers():
        n=int(input("Enter any number: "))
        if(n>0):
            print("Number is positive.")
            message="Number is positive."
        elif(n<0):
            print("Number is negative.")
            message="Number is negative."
        else:
            print(n, "is zero")
            message="is zero"
            return message
    def oddEven():
        num=int(input("Enter the number:"))
        if((num%2)==1):
            print("odd number")
            message="odd Number"
        else:
            print("Even number")
            message="Even number"
            return message
    def number():
        num =("1", "2", "3", "4", "5", "6", "7", "8", "9", "10")
        print ("value:",len(num))
        if (len(num) == 10):
            print ("Correct")
        message="Correct"
    def Eligibility():
        Gender=input("Enter the Gender(Male,Female):")
        Age=int(input("Enter the age:"))
        print ("Eligible" if((Age>=18 and Gender=='Female')or(Age>=21 and Gender=='Male')) else "Not eligible")
    def BMI():
        BMI=int(input("Enter the BMI INdex:"))
        if(BMI<18.5):
            print("Underweight")
            message="Underweight"
        elif(BMI<24.9):
            print("Normal")
            message="Normal"
        elif(BMI<29.9):
            print("Overweight")
            message="Overweight"
        else:
            print("Very Overweight")
            message="Very OVerweight"
        return message