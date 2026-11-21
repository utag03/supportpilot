ESCALATION_WORDS = ["lawyer", "scam", "fraud", "angry"]
turns = 0
print("SupportPilot FAQ bot. Type 'quit' to exit.")
while True:
    message = input("You:").strip().lower()
    if message == "quit":
        break
    turns += 1
    need_humans=False
    escalations=0
    for word in ESCALATION_WORDS:
        if word in message:
            need_humans=True
            escalations+=1
    if need_humans:
        print("Bot: I'm connecting you with a human agent.")
    elif message == "":
        print("Bot: Please type a question.")
    elif "refund" in message:
        print("Bot: Refunds are available within 7 days for damaged items.")
    elif "delivery" in message or "shipping" in message:
        print("Bot: Delivery usually takes 3-5 business days.")
    elif "password" in message :
        print("Bot: You can reset your password using the 'Forgot Password' link.")
    elif "cancel" in message or "return" in message:
        print("Bot: You can cancel or return items within 14 days of purchase.")
    elif "order" in message:
        print("Bot: You can track your order using the tracking number sent to your email.")
    else:
        print("Bot: Sorry, I don't know that one yet.")
print(f"Goodbye! You sent {turns} messages and had escalations {escalations} times. Thank you for using SupportPilot FAQ bot.")