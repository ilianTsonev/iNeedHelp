import random

print("Hello!")
tips = [
    "DirectX? What's taht? Bill Gates new way to pump money?",
    "Bash is the best thing to know, yet i am coding this in python.",
    "If you like older OS like Trusty Tahr (14.04) you can use ubuntu pro for extended security and few more years compatibillity!",
    "That snap may be the best for Ubuntu",
    "Wine, they say. Wine is just WSL for windows, but vice-versa",
    "Apt is the main way to download (sudo apt instal) and manage (sudo apt update & sudo apt upgrade) apts!",
    "cp is the best tool to copy cp! (HAANK! HAANK! DO NOT ABREVIATE CYBERPUNK!!!)",
    "With cat you cannot play with a cat, but rather see a what a file have in it without having to open it!"
]

# Select a random tip. Use `len(tips) - 1` to avoid IndexError
selected_tip = tips[random.randint(0, len(tips) - 1)]

print(f"Tip of the day: {selected_tip}")
