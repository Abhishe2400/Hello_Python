def solve(a, mappings):
    output = ""
    for i in a:
        output += mappings.get(i, '!')+" "

    return output


mapping = {
    "1": "one",
    "2": "two",
    "3": "three"
}

s = input('Enter your string')
print(solve(s, mapping))
