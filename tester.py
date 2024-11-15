import geo.utils as utils

def test_pythagoras():
    a, b = 3, 4
    c = utils.pythagoras(a, b)
    assert c == 5, f"Expected 5, got {c}"
    print("Pythagoras test passed!")

if __name__ == "__main__":
    test_pythagoras()
