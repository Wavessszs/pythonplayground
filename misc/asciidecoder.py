import string
import random
import time

target = "betlognijcmalaki"
characters = string.ascii_lowercase
result = ""

for target_letter in target:
    while True:
        random_letter = random.choice(characters)
        print("\r" + result + random_letter, end="")  # Overwrite the same line
        if random_letter == target_letter:
            result += random_letter
            break
        time.sleep(.02)

print("\nFinal result: oten"    )

