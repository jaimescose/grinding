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
        
        if s_char not in s_counter:
            s_counter[s_char] = 1
        else:
            s_counter[s_char] += 1

        if t_char not in t_counter:
            t_counter[t_char] = 1
        else:
            t_counter[t_char] += 1
    
    for k, v in s_counter.items():
        if v != t_counter.get(k, 0):
            return False
    
    return True

        

