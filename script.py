import os

print("""Choose one color of them:
          blue, red, green, yellow """)



def change_color():
    x = input("Enter color: ")
    if x == "red":
        os.system('color 4f')
    elif x == "blue":
        os.system('color 1f')
    elif x == "yellow":
        os.system('color 6f')
    elif x == "green":
        os.system('color 2f')
    else:
        print("Enter true color!!!")
        change_color()

change_color()
