while True:
    user = input("You: ").lower()
    if "hello" in user or "hi" in user:
        print("Bot: Hello!")
    elif "bye" in user or "goodbye" in user:
        print("Bot: Bye!")
        break
    else:
        print("Bot: I don't understand.")