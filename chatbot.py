import random
username = None

def greeting():
        greetings = ["Hello!", "Hi!", "What's up?", "Hey!"]
        if username:
            print(f"Bot: {random.choice(greetings)} {username}!")
        else:
            print(f"Bot: {random.choice(greetings)}")

def joke():
    print("Bot: Would You like me to tell you a joke?")
    ans1 = input("You: ").lower()
    if "yes" in ans1 or "yea" in ans1 or "yeah" in ans1 or "sure" in ans1 or "absolutely" in ans1:
        print("Bot: Why can't you play hide and seek with leopards?")
        ans1_1 = input("You: ").lower()
        if "why" in ans1_1:
            print("Bot: Because they are always spotted.")
        ans1_2 = input("You: ").lower()
        if "haha" in ans1_2 or "lol" in ans1_2 or "lmao" in ans1_2 or "lmfao" in ans1_2 or "funny" in ans1_2 or "oh" in ans1_2:
            if username:
                print(f"Bot: I'm glad I made you laugh, {username}.")
            else:
                print("Bot: I'm glad I made you laugh.")

    else:
        print("Bot: No problem! How could I help you?")

print("Bot: Hey, I am your ChatBot!")

while True:
    user = input("You: ").lower()

    if "hello" in user or "hi" in user or "hey" in user:
        greeting()

    elif "my name is" in user:
        username = user.replace("my name is", "").strip().title()
        name_response = ["That's a nice name", "You have a lovely name", "That's a cool name"]
        print(f"Bot: {random.choice(name_response)}, {username}")
    
    elif "i am" in user:
        username = user.replace("i am", "").strip().title()
        name_response = ["That's a nice name", "You have a lovely name", "That's a cool name"]
        print(f"Bot: {random.choice(name_response)}, {username}")

    elif "what is my name" in user or "what's my name" in user:
        if username:
            print(f"Your name is {username}.")
        else:
            print("Bot: I don't know your name yet.")

    elif "joke" in user:
        joke()

    elif "thanks" in user or "thank you" in user:
        if username:
            print(f"Bot: You are welcome, {username}!")
        else:
            print("Bot: You are welcome!")

    elif "bye" in user or "goodbye" in user or "exit" in user or "kill" in user:
        if username:
            print(f"Bot: Bye, {username}!")
        else:
            print("Bot: Bye!")
        break

    else:
        print("Bot: I don't understand.")