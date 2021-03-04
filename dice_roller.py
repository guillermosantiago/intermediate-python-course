import random

def main():
  num_dices = 2
  sum_dices = 0
  for i in range(0,num_dices):
      roll = random.randint(1,6)
      sum_dices += roll
      print(f'You rolled a {roll}')
      pass

  print(f'So the sum is {sum_dices}')

if __name__== "__main__":
  main()
