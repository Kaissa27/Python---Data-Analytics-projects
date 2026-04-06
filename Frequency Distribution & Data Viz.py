def visualize_test_scores():
    # Raw Data: Unordered test scores from a class
    scores = [88, 92, 75, 81, 65, 70, 95, 82, 45, 99, 87, 78, 62, 91, 84, 76]

    # 1. Define our "Bins" (Ranges)
    # We create a dictionary to hold the counts for each grade bracket
    distribution = {
        "90-100 (A)": 0,
        "80-89  (B)": 0,
        "70-79  (C)": 0,
        "60-69  (D)": 0,
        "< 60   (F)": 0
    }

    # 2. Categorization Logic
    for s in scores:
        if s >= 90: distribution["90-100 (A)"] += 1
        elif s >= 80: distribution["80-89  (B)"] += 1
        elif s >= 70: distribution["70-79  (C)"] += 1
        elif s >= 60: distribution["60-69  (D)"] += 1
        else: distribution["< 60   (F)"] += 1

    print("--- Class Performance Distribution ---")
    print(f"Total Students: {len(scores)}\n")

    # 3. Text-Based Visualization
    # We use a special character to build the bars
    for bracket, count in distribution.items():
        bar = "■" * count  # Multiplies the character by the number of students
        percentage = (count / len(scores)) * 100
        print(f"{bracket} | {bar:<10} ({count} students | {percentage:.1f}%)")

    # 4. Statistical Summary
    avg = sum(scores) / len(scores)
    print("-" * 45)
    print(f"Class Average: {avg:.1f}%")
    print(f"Highest Score: {max(scores)}% | Lowest Score: {min(scores)}%")

if __name__ == "__main__":
    visualize_test_scores()