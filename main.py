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

def make_a_guess(answer):
  user_guess = int(input("Guess a number\n"))
  return difference_from_answer(user_guess, answer)
