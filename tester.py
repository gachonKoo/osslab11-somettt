from geo import calculate_square_area, calculate_rectangle_area, calculate_circle_area

def test_square_area():
    assert calculate_square_area(4) == 16
    print("Square area test passed!")

def test_rectangle_area():
    assert calculate_rectangle_area(5, 3) == 15
    print("Rectangle area test passed!")

def test_circle_area():
    assert round(calculate_circle_area(3), 2) == 28.27
    print("Circle area test passed!")

if __name__ == "__main__":
    test_square_area()
    test_rectangle_area()
    test_circle_area()
