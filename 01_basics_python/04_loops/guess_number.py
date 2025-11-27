import random

secret = random.randint(1, 20)

attempts_left = input("Сколько попыток ты хочешь потратить (по умолчанию 5)? ")
attempts_left = int(attempts_left) if attempts_left.strip() else 5

if attempts_left <= 0:
    print("Возьмём стандартные 5 попыток, иначе будет нечестно.")
    attempts_left = 5

print("Я загадала число от 1 до 20. Попробуй угадать его за выбранное число попыток!")

attempts_start = attempts_left
guessed = False

while attempts_left > 0:
    guess = int(input("Твой вариант: "))
    attempts_left -= 1

    if guess == secret:
        used_attempts = attempts_start - attempts_left
        print(f"Поздравляю! Ты угадал число {secret} с {used_attempts}-й попытки!")
        guessed = True
        break
    elif guess < secret:
        print("Моё число больше.")
    else:
        print("Моё число меньше.")

    if attempts_left > 0:
        print(f"Осталось попыток: {attempts_left}")

if not guessed:
    print(f"Попытки закончились. Я загадала число {secret}. Попробуй ещё раз!")