import math

def analyze_user_engagement():
    # Raw Data: { User_ID: [Session_Lengths_In_Minutes] }
    # Each list represents the last 5 times that user logged in.
    user_sessions = {
        "User_001": [45, 30, 60, 15, 50],
        "User_002": [5, 2, 8, 1, 3],
        "User_003": [120, 95, 110, 80, 105],
        "User_004": [20, 25, 20, 30, 15],
        "User_005": [60, 0, 0, 0, 0] # User stopped logging in
    }

    print(f"{'User ID':<10} | {'Avg Session':<12} | {'Stability':<10} | {'Status'}")
    print("-" * 55)

    for user, sessions in user_sessions.items():
        # 1. Basic Metric: Average Session Length
        avg_session = sum(sessions) / len(sessions)
        
        # 2. Advanced Metric: Standard Deviation (Stability)
        # Does the user log in for the same amount of time, or is it random?
        variance = sum((x - avg_session) ** 2 for x in sessions) / len(sessions)
        std_dev = math.sqrt(variance)

        # 3. Categorization Logic (Segmentation)
        if avg_session > 90:
            status = "💎 Power User"
        elif avg_session < 10:
            status = "⚠️ At Risk (Churn)"
        elif sessions.count(0) > 2:
            status = "❌ Inactive"
        else:
            status = "✅ Active"

        print(f"{user:<10} | {avg_session:>8.1f} min | {std_dev:>8.1f}   | {status}")

    # 4. Global Insight: Platform Health
    total_avg = sum(sum(s) for s in user_sessions.values()) / (len(user_sessions) * 5)
    print("-" * 55)
    print(f"Global Average Session: {total_avg:.1f} minutes")

if __name__ == "__main__":
    analyze_user_engagement()