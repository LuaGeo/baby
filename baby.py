from random import choice

questions = ["Do you know what came first, the egg or the chicken?",
             "Why is the sky blue?", "Where are all the dinosaurs?"]

question = choice(questions)

answer2 = input(question).strip().lower()

while (answer2) != "just because":
    answer2 = input("Why?").strip().lower()

print("Oh... Okay")

answer2 = input(question).strip().lower()

while (answer2) != "just because":
    answer2 = input("Why?").strip().lower()

print("Oh... Okay")