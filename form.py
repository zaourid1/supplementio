"""
-------------------------------------------------------
Form to ask and answer what supplement is best reccomeneded
-------------------------------------------------------
Author:  Zineb Aourid
__updated__ = "2025-08-03"
-------------------------------------------------------
"""
#imports
from sups import supplements

# Gather all unique symptoms from the supplements list
all_symptoms = set()
for s in supplements:
    for symptom in s.symptoms:
        all_symptoms.add(symptom)

# Display intro
print("Hello and welcome to supplement recommender.")
print("Here I will recommend the best supplement based on your symptoms.\n")
print("---------------------")
print("What symptoms do you currently have? Pick from the following:\n")

for i in all_symptoms:
    print(i)
print('--------------------')

# User input
symptoms_input = input("Enter symptoms (comma-separated): ").lower()
user_symptoms = [s.strip() for s in symptoms_input.split(",")]

# Matching supplements
print("\nRecommended Supplements:")
found = False
for sup in supplements:
    if any(symptom in sup.symptoms for symptom in user_symptoms):
        print(f"- {sup.name} → {sup.recs}")
        print(f"----> symptoms: {user_symptoms}")
        print()
        found = True

if not found:
    print("No supplements matched your symptoms. Try different keywords.")
