def game():
        start()
        scene1()
        scene2()

def start():
    print("Hello, welcome to my game... muhhahaha")
    print("My name is Danielle, Danielle from MLH and I prepared a beginner text based adventure for you all!")
    print("Use this to learn how text based adventures work and to inspire yours!")
    
    start = "false"
    while start != "yes":
        start = input("Are you ready to begin? ").lower()
        if start in ["y", "true", "yeah"]:
            start = "yes"
    
    print("Excellent!")

def scene1():
    print("You wake up in your room.")
    print("In text based adventures you can use commands like: Type l to look around and type x [item name] to examine an item.")
    print("Other common key works include (but are not limited to) push, pull, open, read, and take")
    sceneDone = "false"
    while sceneDone == "false":
        action = input("What do you want to do? ").lower()
        if action == "l":
            print("You look around the room. You see a door and a mirror.")
        if action == "x door":
            print("It is just your bedroom door")
        if action == "x mirror":
            print("You look in the mirror, you see your long neck, and brown spots on your yellow fur. You look at the sparkly colors fluctuate around your body. You are... Gene the Glitchy Giraffe")
        if action == "open door":
            sceneDone = "true"

def scene2():
    print("You are now in the woods outside your house.")


game()