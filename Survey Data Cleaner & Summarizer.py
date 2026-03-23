def analyze_survey():
    # Raw data: [Name, Favorite Color, Age]
    raw_responses = [
        ["alice ", "BLUE", "25"],
        ["  BOB", "red", " 30"],
        ["Charlie", " blue ", "22"],
        ["david", "Red", "35"],
        ["Eve", "blue", "28"]
    ]

    # 1. Cleaning Phase (Standardization)
    cleaned_data = []
    for resp in raw_responses:
        name = resp[0].strip().title()
        color = resp[1].strip().lower()
        age = int(resp[2].strip())
        cleaned_data.append({"name": name, "color": color, "age": age})

    # 2. Aggregation Phase (Counting Favorites)
    color_counts = {}
    for person in cleaned_data:
        color = person['color']
        color_counts[color] = color_counts.get(color, 0) + 1

    # 3. Insight Phase (Average Age)
    avg_age = sum(p['age'] for p in cleaned_data) / len(cleaned_data)

    print(f"Total Participants: {len(cleaned_data)}")
    print(f"Favorite Colors: {color_counts}")
    print(f"Average Participant Age: {avg_age:.1f}")

analyze_survey()
