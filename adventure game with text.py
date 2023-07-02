### Print a welcome message
print("Welcome to Iroko Estate!")
print("You are giving an opportunity to enter any house, and eat good meals")
print("As a new visitor, you decide to visit Iroko Estate.")
print("The estate is, moldy, rough, and grasses around. You pass through the Main gate.")
print("Do you want to enter Moses house or David house?")

### prompt user for a choice
houseChoice = input("> ")

if (houseChoice == "Moses house"): 
    print("you enter Moses house.") 
    print("As you walk in, you see a dull Baby blocking some money.") 
    print("Do you want to steal the money behind the dull Baby?") 
    
    dullBabyChoice=input("> ")

    if(houseChoice == "Yes"):
        print("You attempt to steal the money, but it electricute and dry you to death.")
        print("you are now dead.")
    elif(houseChoice == "No"):
        print("You decide not to steal the money.")
        print("You turn around and leave the house safely.")
    else: 
        print("invalid choice.  please enter Yes or No.")
elif(houseChoice == "David house"):
    print("You chose to go into David house.")
    print("As you walk in, you see a shiny vase on the table.")
    print("Do you want to open the vase?")

    vaseChoice = input("> ")

    if(vaseChoice == "Yes"):
       print("You open the vase and find some food cans!") 
    elif(vaseChoice == "No"):
        print("You decide not to open the shiny vase.")
        print("As you turn to leave, you hear a sound of flood coming from the corner.")
        print("A white gaint figure with glowing red eyes launches at you, knocking you unconcious")
        print("You wake up in your bed. It was all a dream.")
    else:
      print("invalid choice.  please enter Yes or No.")
else: 
    print("invalid choice.  please enter Moses house or David house.")