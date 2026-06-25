while True:
    user = input("You: ").lower()
    def greeting():
        import random
        greetings = ["Hello!", "Hi!", "What's up?", "Hey!"]
        print(f"Bot: {random.choice(greetings)}")

    def joke():
        print("Bot: Would You like me to tell you a joke?")
        ans1 = input("You: ").lower()
        if "yes" in ans1:
            print("Bot: Why can't you play hide and seek with leopards?")
            ans1_1 = input("You: ").lower()
            if "why" in ans1_1:
                print("Bot: Because they are always spotted.")
        elif "no" in ans1:
            print("How could I help you?")

    if "hello" in user or "hi" in user or "hey" in user:
        greeting()

    elif "joke" in user:
        joke()    

    elif "bye" in user or "goodbye" in user:
        print("Bot: Bye!")
        break

    else:
        print("Bot: I don't understand.")