import random
num = 0

def generate_random_number():
   return random.randint(0, 100)

def difference_from_answer(guess, answer):
  if guess == answer:
    return "Correct"
  elif guess < answer:
    return "Too low"
  elif guess > answer:
    return "Too high"
