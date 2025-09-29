# quiz-app.py
questions = [
    {"q":"Capital of France?", "a":"Paris"},
    {"q":"5+7=?", "a":"12"},
    {"q":"Python creator?", "a":"Guido"}
]
score=0
for i, item in enumerate(questions,1):
    ans=input(f"Q{i}: {item['q']} ")
    if ans.strip().lower()==item['a'].lower(): print("Correct!"); score+=1
    else: print(f"Wrong! Answer: {item['a']}")
print(f"Your score: {score}/{len(questions)}")
