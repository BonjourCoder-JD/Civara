countries = [
    {"country": "Canada", "year": 2026, "indicator": "Gender equality", "score": 75.5},
    {"country": "Germany", "year": 2026, "indicator": "Gender equality", "score": 82.3},
    {"country": "Japan", "year": 2026, "indicator": "Gender equality", "score": 68.1},
]

print("Civara Equity Dataset")

for country in countries:
        print(f"{country['country']}: {country['score']}")