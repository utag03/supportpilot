from support import load_policies, find_answer
ESCALATION_WORDS = ["lawyer", "scam", "fraud", "angry"]
turns = 0
escalations=0
policies = load_policies()
print("SupportPilot FAQ bot. Type 'quit' to exit.")
while True:
    message = input("You:").strip().lower()
    if message == "quit":
        break
    turns += 1
    need_humans=False

    for word in ESCALATION_WORDS:
        if word in message:
            need_humans=True
    if need_humans:
        escalations+=1
        print("Bot: I'm connecting you with a human agent.")
    elif message == "":
        print("Bot: Please type a question.")
    else:
        answer = find_answer(message, policies)
        if answer is None:
            print("Bot: Sorry, I don't know that one yet.")
        else:
            print(f"Bot: {answer}")

print(
    f"Goodbye! You sent {turns} messages and had "
    f"{escalations} escalations. Thank you for using SupportPilot FAQ bot."
)