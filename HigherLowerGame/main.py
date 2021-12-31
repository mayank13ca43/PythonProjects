from game_data import data
from art import logo,vs
from os import system
import random


shouldContinue = True
score = 0
while shouldContinue:
  print(logo)
  A = random.choice(data)
  B = random.choice(data)
  if(A == B):
    B = random.choice(data)
  print(f"Compare A: {A['name']}, a {A['description']}, from {A['country']}.")
  print(vs)
  #print(f"Followers = A : {A['follower_count']} , B : {B['follower_count']}")
  print(f"Against B: {B['name']}, a {B['description']}, from {B['country']}.")
  guess = input("Who has more followers ? Type 'A' or 'B': ")
  if guess == 'A' and A['follower_count'] >= B['follower_count']:
    score += 1
    system('clear')
    print(f"You're right! Current score: {score}")
  elif guess == 'B' and A['follower_count'] <= B['follower_count']:
    score += 1
    system('clear')
    print(f"You're right! Current score: {score}")
  else:
    print(f"Sorry, that's wrong. Final score : {score}")
    shouldContinue = False

