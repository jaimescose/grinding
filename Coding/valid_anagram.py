TEST_CASES = [
    (("anagram", "nagaram"), True),
    (("rat", "car"), False),
    (("care", "race"), True),
    (("cars", "car"), False),
]

def main(s: str, t: str) -> bool:
    return optimized_2(s, t)
    

def optimized_2(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    
    s_counter, t_counter = dict(), dict()
    for s_char, t_char in zip(s, t):
        s_counter[s_char] = s_counter.get(s_char, 0) + 1
        t_counter[t_char] = t_counter.get(t_char, 0) + 1
    
    for k, v in s_counter.items():
        if v != t_counter.get(k, 0):
            return False
    
    return True
