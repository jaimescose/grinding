TEST_CASES = [
    (("anagram", "nagaram"), True),
    (("rat", "car"), False),
    (("care", "race"), True),
    (("cars", "car"), True),
]

def main(s: str, t: str) -> bool:
    
    if len(s) != len(t):
        return False
    
    for c1, c2 in zip(s, t)
