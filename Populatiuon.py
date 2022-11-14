# The menu 
def Menu():
    print("Please Select and option")
    print("1. Enter Generation 0 values")
    print("2. See Generation 0 values")
    print("3. Run the model")
    print("4. Save the model to CSV")
    print("9. Exit")
    global input1
    input1 = int(input("Enter: "))
    
# 2d Array to store the question and the answer
Values = [["Enter Number of generations: ", ""],
             ["Enter number of Juvivniles: ", ""],
             ["Enter number of Adults: ", ""],
             ["Enter Number of Seniles: ", ""],
             ["Enter Birth Rate: ", ""] ]           



Menu()
# Infinite Loop using While True
while True: 
    # Asks the questions and recieves answers and stores them
    if input1 == 1:
        print(Values[0][0])
        Values[0][1] = int(input())  

        print(Values[1][0])
        Values[1][1] = int(input())

        print(Values[2][0])
        Values[2][1] = int(input())

        print(Values[3][0])
        Values[3][1] = int(input())

        print(Values[4][0])
        Values[4][1] = int(input())
        Menu()
        
    
    # Tells the user the values entered
    if input1 == 2:
        print("You entered" , Values[0][1] , "Generations")
        print("You entered" , Values[1][1] , "Juviniles")
        print("You entered" , Values[2][1] , "Adults")
        print("You entered" , Values[3][1] , "Seniles")
        print("You entered a Birth Rate of" , Values[4][1])
        Menu()


    # Runs the model
    if input1 == 3:
        birthrate = int(Values[4][1])
        juviniles = int(Values[1][1])
        adults = int(Values[2][1])
        seniles = int(Values[3][1])

        while Values[0][1] > 0:
            newseniles = adults
            newadults = juviniles
            juviniles = 0
            newjuvies = adults * birthrate

            # All seniles die and adults become seniles
            #Values[3][1] = (Values[3][1] * 0) + Values[2][1]
            # All Juvniles become adults
            #Values[2][1] = (Values[2][1] * 0) + Values[1][1]

            

            


            #print(Values[2][1])
            print(newjuvies)
            




            Values[0][1] -= 1 




    # Exits the program
    if input1 == 9:
        quit()
    




       
    
