import random


def encoded(decoded_message):
    vowels = ['a', 'e', 'i', 'o', 'u']
    consonants = [chr(x) for x in range(97, 123) if chr(x) not in vowels]

    def generate_line(vowel_count):
        line = []
        for _ in range(vowel_count):
            line.append(random.choice(vowels))
        while len(line) < 50:
            line.append(random.choice(consonants))
        random.shuffle(line)
        return ''.join(line)

    file_content = ""
    for char in decoded_message:
        if char == ' ':
            file_content += generate_line(0) + "\n"
        elif char.isalpha():
            vowel_count = ord(char.lower()) - 96
            file_content += generate_line(vowel_count) + "\n"

    return file_content.strip()


decoded_message = "This was hard, but I enjoy the course"
file_content = encoded(decoded_message)
print("Reconstructed file content:")
print(file_content)
