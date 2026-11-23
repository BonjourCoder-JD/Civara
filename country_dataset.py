countries = [
    {"country": "Canada", "year": 2026, "indicator": "Gender equality", "score": 75.5},
    {"country": "Germany", "year": 2026, "indicator": "Gender equality", "score": 82.3},
    {"country": "Japan", "year": 2026, "indicator": "Gender equality", "score": 68.1},
]

print("Civara Equity Dataset")

for country in countries:
        print(f"{country['country']}: {country['score']}")

total_score = 0

for country in countries:
        total_score += country['score']
print(f"Total score: {total_score}")

def calculate_average_score(countries):
    if len(countries) == 0:
        return 0
    total_score = 0
    for record in countries:
        total_score += record['score']
    return total_score / len(countries)

print(f"Average score: {calculate_average_score(countries)}")
