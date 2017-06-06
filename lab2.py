def object_reference():
    s = [0] * 3
    s[0] += 1
    print(s)

s = [''] * 3
s[0] += 'a'
print(s)

s = [[]] * 3
s[0] += [1]
print(s)

def gcd(a, b):
     while b != 0:
          (a, b) = (b, a % b)
    
gcd(10, 25) # => 5
gcd(14, 15) # => 1
gcd(3, 9) # => 3
gcd(1, 1) # => 1

def flip_dict(d):
    
    out = {}
    for key, value in d.items():
        if value not in out:
            out[value] = []
        out[value].append(key)
    return out

def comprehension_read():

    print([x for x in [1, 2, 3, 4]])
    print([n - 2 for n in range(10)])
    print([k % 10 for k in range(41) if k % 3 == 0])
    print([s.lower() for s in ['PythOn', 'iS', 'cOoL'] if s[0] < s[-1]])

    arr = [[3,2,1], ['a','b','c'], [('do',), ['re'], 'mi']]
    print([el.append(el[0] * 4) for el in arr])
    print(arr)

    print([letter for letter in "pYthON" if letter.isupper()])
    print({len(w) for w in ["its", "the", "remix", "to", "ignition"]})

def comprehension_write():
  
    arr = [0, 1, 2, 3]
    print([2 * num + 1 for num in arr])  # [1, 3, 5, 7]

    arr = [3, 5, 9, 8]
    print([num % 3 == 0 for num in arr])  # [True, False, True, False]

    arr = ["TA_sam", "TA_guido", "student_poohbear", "student_htiek"]
    print([name[3:] for name in arr if name.startswith('TA_')])  # ["sam", "guido"]

    arr = ['apple', 'orange', 'pear']
    print([fruit[0].upper() for fruit in arr])  # ['A', 'O', 'P']
    print([fruit for fruit in arr if 'p' in fruit])  # ['apple', 'pear']
    print([(fruit, len(fruit)) for fruit in arr])  # [('apple', 5), ('orange', 6), ('pear', 4)]
    print({fruit:len(fruit) for fruit in arr})  # {'orange': 6, 'apple': 5, 'pear': 4}

def is_cyclone_word(word):
    word = word.upper()
    letters = [None] * len(word)
    half = (len(word) + 1) // 2
    letters[::2] = word[:half]
    letters[1::2] = word[:half - 1:-1]
    return all([left <= right for left, right in zip(letters, letters[1:])])

def is_cyclone_phrase(phrase):
 
    return all([is_cyclone_word(word) for word in phrase.split()])

def generate_pascal_row(row):
   
    if not row: return [1]
    return [left + right for left, right in zip([0] + row, row + [0])]


def is_triangle_number(num):
   
    discrim = 8 * num + 1
    base = int(math.sqrt(discrim))
    return base * base == discrim

def polygon_collision(poly1, poly2):
    pass

if __name__ == '__main__':
   
    fns = [
        (object_reference, (), {}),
        (gcd, (91, 35), {}),
        (flip_dict, ({"CA": "US", "NY": "US", "ON": "CA"},), {}),
        (comprehension_read, (), {}),
        (comprehension_write, (), {}),
        (is_cyclone_phrase, ("all alone at noon",), {}),
        (generate_pascal_row, ([1, 4, 6, 4, 1],), {}),
    
    ]
    for fn, args, kwargs in fns:
        name = fn.__name__
        print("*" * len(name))     # header
        print(name)                # function name
        print(fn.__doc__)          # function docstring
        res = fn(*args, **kwargs)  # variadic argument unpacking - cool stuff! More Week 3.
        if res:
            print(res)
        input("Press [ENTER] to continue...")
    print("Done!")
