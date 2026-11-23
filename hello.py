def greet(name):
    return f"Hello , {name}! Welcome to supportPilot!."
def route(message):
    if "refund" in message.lower():
        return "refund_team"
    elif "order" in message.lower() or "delivery" in message.lower():
        return "order_team"
    else:
        return "general_support_team"
if __name__=="__main__":
    name = input("what is your name?")
    print(greet(name))
    message = input("what is your query?")
    print(route(message))