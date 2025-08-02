from sorter import sort

def run_tests():
    test_cases = [
        (100, 100, 100, 10, "SPECIAL"),
        (140, 140, 140, 25, "REJECTED"),
        (120, 100, 100, 15, "STANDARD"),
        (150, 80, 50, 10, "SPECIAL"),
        (50, 50, 50, 21, "SPECIAL"),
        (200, 200, 200, 30, "REJECTED"),
        (10, 10, 10, 1, "STANDARD")
    ]

    for i, (w, h, l, m, expected) in enumerate(test_cases):
        result = sort(w, h, l, m)
        assert result == expected, f"Test case {i+1} failed: expected {expected}, got {result}"
        print(f"Test case {i+1} passed.")

if __name__ == "__main__":
    run_tests()
