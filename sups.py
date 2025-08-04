"""
-------------------------------------------------------
Turning each supplement into a Supplement Class for each search.
-------------------------------------------------------
Author:  Zineb Aourid
__updated__ = "2025-08-03"
-------------------------------------------------------
"""

#imports
from supplement_class import Supplement
import json

with open("supplements.json", "r") as f:
    data = json.load(f)

supplements = []
for item in data:
    sup = Supplement(
        id=item["id"],
        name=item["name"],
        symptoms=item["deficiency_symptoms"],
        recs=item["recommendation"]
    )
    supplements.append(sup)

print(supplements)