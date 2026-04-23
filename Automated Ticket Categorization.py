import pandas as pd

def automate_support_tags():
    # 1. Incoming "Unstructured" Data
    tickets = [
        "My order #1234 hasn't arrived yet, where is it?",
        "I can't log in to my account, it says password incorrect",
        "Why was I charged twice for my subscription this month?",
        "The package arrived but the item is broken",
        "Reset my password please, I'm locked out",
        "The shipping was supposed to be overnight but it's been 3 days"
    ]

    # 2. Logic-Based Tagging (The Analytics Approach)
    # We define keywords for our business categories
    category_map = {
        'Logistics': ['order', 'shipping', 'arrived', 'package', 'delivery'],
        'Technical': ['log in', 'password', 'account', 'locked', 'error'],
        'Billing': ['charged', 'subscription', 'payment', 'refund', 'price']
    }

    def get_tag(text):
        text = text.lower()
        for category, keywords in category_map.items():
            if any(word in text for word in keywords):
                return category
        return 'General'

    # 3. Create a Report
    df = pd.DataFrame({'Ticket_Text': tickets})
    df['Category'] = df['Ticket_Text'].apply(get_tag)

    # 4. Analytics Summary
    summary = df['Category'].value_counts()
    
    print("--- 🎫 Support Ticket Breakdown ---")
    print(df)
    print("\nTotal Tickets by Department:")
    print(summary)

if __name__ == "__main__":
    automate_support_tags()
