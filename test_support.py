from support import find_answer
POLICIES = [
    {"topic": "refund", "keywords": ["refund", "money back"], "answer": "REFUND_ANSWER"},
    {"topic": "delivery", "keywords": ["delivery"], "answer": "DELIVERY_ANSWER"},
    {"topic": "cancel ", "keywords":["cancel"],"answer":"Cancellation initiated."},
]
def test_find_refund_ignores_case():
    assert find_answer("I want a refund", POLICIES) == "REFUND_ANSWER"
def test_finds_by_second_keyword():
    assert find_answer("give me my money back", POLICIES) == "REFUND_ANSWER"
def test_returns_none_when_unknown():
    assert find_answer("hello there", POLICIES) is None
def test_find_cancel():
    assert find_answer("cancel the order", POLICIES) == "Cancellation initiated."



