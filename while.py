def spaced(input_string):
    i = 0
    while i < len(input_string):
        print(input_string[i], end=" ")
        i += 1
    print()



spaced("abcdefghijklmnop")

def spaced_reverse(input_string):
    i = len(input_string) - 1
    while i >= 0:
        print(input_string[i], end=" ")
        i -= 1
    print()

s1 = "abcdefghijklmnop"
print(len(s1))

spaced_reverse("abcdefghijklmnop")
