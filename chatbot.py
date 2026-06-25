while True:
    user = input("You: ").lower()

    def greeting():
        import random
        greetings = ["Hello!", "Hi!", "What's up?", "Hey!"]
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
                print(f"Bot: I'm glad I made you laugh, {ans_name}")
        else:
            print("How could I help you?")

    if "hello" in user or "hi" in user or "hey" in user:
        greeting()

    elif "name" in user:
        print("Bot: May i know your name please?")
        ans_name = input("You: Name: ")
        import random
        name_response = ["That's a nice name", "You have a lovely name", "That's a cool name"]
        print(f"Bot: {random.choice(name_response)}, {ans_name}")

    elif "thanks" in user or "thank you" in user:
        print(f"Bot: Is there anything else I can do for you, {ans_name}")
        ans2 = input("You: ").lower()
        if "yes" in ans2 or "yea" in ans2 or "yeah" in ans2 or "sure" in ans2 or "absolutely" in ans2:
            continue
        else:
            print(f"Bot: Okay, {ans_name}. Enjoy your day!")

    elif "joke" in user:
        joke()

    elif "bye" in user or "goodbye" in user or "exit" in user or "kill" in user:
        print("Bot: Bye!")
        break

    else:
        print("Bot: I don't understand.")