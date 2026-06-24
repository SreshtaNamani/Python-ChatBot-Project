while True:
    user = input("You: ").lower()
    if "hello" in user or "hi" in user:
        print("Bot: Hello!")
    elif "joke" in user:
        print("Bot: Would You like me to tell you a joke?")
        ans1 = input("You: ").lower()
        if "yes" in ans1:
            print("Bot: Why can't you play hide and seek with leopards?")
            ans1_1 = input("You: ").lower()
            if "why" in ans1_1:
                print("Bot: Because they are always spotted.")
        elif "no" in ans1:
            print("How could I help you?")
    elif "bye" in user or "goodbye" in user:
        print("Bot: Bye!")
        break
    else:
        print("Bot: I don't understand.")