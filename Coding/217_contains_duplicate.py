TEST_CASES = [
    (([1, 2, 3, 1], ), True),
    (([1, 2, 3, 4], ), False),
    (([1, 1, 1, 3, 3, 4, 3, 2, 4, 2], ), True),
]
]

def main(numbers_list: list[int]) -> bool:
    numbers = set()

    for n in numbers_list:
        if n in numbers:
            return True
        numbers.add(n)
    
    return False
