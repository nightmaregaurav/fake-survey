import json
import random

TOTAL_ENTRIES_TO_GENERATE = 250

data = {    
    "How often do you code?": [
        ("Daily", 5),
        ("Several times a week", 4),
        ("Once a week", 3),
        ("Rarely", 2),
        ("Never", 1)
    ]
}

def generate_answer(options):
    weighted_options = []
    for option, priority in options:
        weighted_options.extend([option] * priority)
    return random.choice(weighted_options)

questions = list(data.keys())
answers = []
for _ in range(TOTAL_ENTRIES_TO_GENERATE):
    answers.append([generate_answer(options) for _, options in data.items()])

final = {
    "q": questions,
    "a": answers 
}

with open("out.json", "w") as json_file:
    json.dump(final, json_file, indent=4)
