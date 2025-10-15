import os

print("""Choose one color of them:
          blue, red, green, yellow """)

x = input("Enter color: ")

def change_color(color):
    
    if color == "red":
        os.system('color 4f')
    elif color == "blue":
        os.system('color 1f')
    elif color == "yellow":
        os.system('color 6f')
    elif color == "green":
        os.system('color 2f')
    else:
        print("Enter true color!!!")
        change_color(x)

change_color(x)