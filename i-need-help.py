import random
import time
import os

 f = open("longlist.txt", "r")

print("Hello!")
tips = [
    "DirectX? What's that? Bill Gates' new way to pump money?",
    "Bash is the best thing to know, yet I am coding this in Python.",
    "If you like older OS like Trusty Tahr (14.04), you can use Ubuntu Pro for extended security and a few more years of compatibility!",
    "That snap may be the best for Ubuntu.",
    "Wine, they say. Wine is just WSL for Windows, but vice-versa.",
    "Apt is the main way to download (sudo apt install) and manage (sudo apt update & sudo apt upgrade) packages!",
    "cp is the best tool to copy! (HAANK! HAANK! DO NOT ABREVIATE CYBERPUNK!!!)",
    "With cat, you cannot play with a cat, but rather see what a file has in it without having to open it!",
    "I wanted this snap to be called iNeedHelp, not i-need-help. Snapcraft hates caps."
]

# Select a random tip
selected_tip = tips[random.randint(0, len(tips) - 1)]
time.sleep(10)  # Changed from 10000 to 10 for a more reasonable wait time
os.system("clear")  # Clear the terminal screen
print(f"Tip of the day: {selected_tip}")

while True:  # Changed `true` to `True`
    e = input("What do you wanna do? \n1. Learn Bash\n2. I Need Help\n3. I WANNA CONTACT YOU!\nQ, E, mmm. Escape, Quit\n")
    if e == "1":
        print("Bash is quite easy.")
        time.sleep(2)  # Changed from 1000 to 2 for a more reasonable wait time
        print("Here is the full list of commands in Bash, the clear Bash:")
        time.sleep(5)
    elif e == "2" or e.lower() == "ineedhelp" or e == "HELP":  # Fixed the method call
        print("Sure, Here is a list of most known issues or questions for bash")
        print(f.readline())
        print(f.readline()) 
        print(f.readline())
        print(f.readline()) 
    elif e == "3":
        print("Sure. My email is pools.stock-0q@icloud.com\nIf you want a fast and cool way, my Discord is .memelian4 with the dot.")
    elif e == "q" or e == "Q" or e == "E" or e == "mmm":  # Removed the comment from this line
        print("Exiting the program. Goodbye!")
        break  # Changed `brak` to `break`
    else:
        break #buddy, whatelsedoido
