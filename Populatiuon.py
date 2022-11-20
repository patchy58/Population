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
Questions = [["Enter Number of generations: ", ""],
             ["Enter number of Juvivniles: ", ""],
             ["Enter number of Adults: ", ""],
             ["Enter Number of Seniles: ", ""],
             ["Enter Birth Rate: ", ""] ]           

Values = [["Generations"],
          ["juviniles"],
          ["Adults"],
          ["Seniles"],
          ["Birth Rate"]]

birthrate = int(Values[4][1])
oldJuvi = int(Values[1][1])
oldAdults = int(Values[2][1])
oldSeniles = int(Values[3][1])

Menu()
# Infinite Loop using While True
while True: 
    # Asks the questions and recieves answers and stores them
    if input1 == 1:
        print(Questions[0][0])
        Gens = int(input())
        Values[0].append(Gens)
        
        print(Questions[1][0])
        Juviniles = int(input())
        Values[1].append(Juviniles)

        print(Questions[2][0])
        Adults = int(input())
        Values[2].append(Adults)

        print(Questions[3][0])
        Seniles = int(input())
        Values[3].append(Seniles)

        print(Questions[4][0])
        BirthRate = int(input())
        Values[4].append(BirthRate)
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
        
        
         
        while Values[0][1] > 0:
            newAdult = oldJuvi
            newJuvi = oldAdults * birthrate
            newAdult = oldAdults * 0.75 
            oldSeniles = oldSeniles * 0.3 
            newSenile = oldSeniles + newAdult

            print(newAdult)
            print(newSenile)
            print(newJuvi)
            

            Values[0][1] -= 1 




    # Exits the program
    if input1 == 9:
        quit()
    




       
    
