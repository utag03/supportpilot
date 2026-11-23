import json

def load_policies(path = "policies.json"):
    with open(path) as f:
        return json.load(f)
def find_answer(message,policies):
    text = message.strip().lower()
    for policy in policies:
        for keyword in policy["keywords"]:
            if keyword in text:
                return policy["answer"]
    return None