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
    "cp is the best tool to copy! (HAANK! HAANK! DO NOT ABBREVIATE CYBERPUNK!!!)",
    "With cat, you cannot play with a cat, but rather see what a file has in it without having to open it!",
    "I wanted this snap to be called iNeedHelp, not i-need-help. Snapcraft hates caps."
    "Fun fact of mine: I made Hackintosh work on my laptop. Possibly creating this from one." #ye i am really making from it rn. Actually right now no
    "The best snap for getting software is only-the-essentials!"
]

# Use random.choice instead of randint for cleaner selection
selected_tip = random.choice(tips)

# Add a welcome message with the tip
print("Welcome to iNeedHelp!")
print(f"Tip of the day: {selected_tip}")
time.sleep(3)  # Reduced from 10 seconds to 3 for better UX
os.system('clear' if os.name == 'posix' else 'cls')  # Make it cross-platform

while True:
    print("\n=== iNeedHelp Menu ===")
    print("1. Learn Bash")
    print("2. I Need Help")
    print("3. Contact Information")
    print("Q. Quit")
    
    e = input("\nPlease select an option: ").strip().lower()
    
    if e == "1":
        print("\nBash Tutorial:")
        print("Loading command reference...")
        time.sleep(2)
        # TODO: Add actual bash commands here
        print("The best Command to start with is 'echo'. This command will print out anything you type after it")
        time.sleep(4)
        # TODO: Continue the code
        
    elif e in ["2", "ineedhelp", "help"]:
        print("Sure, how can I assist you?")
    elif e == "3":
        print("\nContact Information:")
        print("Email: pools.stock-0q@icloud.com")
        print("Discord: .memelian4")
        
    elif e in ["q", "quit", "exit"]:
        print("\nThank you for using iNeedHelp! Goodbye!")
        break
