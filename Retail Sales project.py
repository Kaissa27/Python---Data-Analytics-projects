def sales_analytics():
    # Format: (Item_Name, Category, Price) 
    transactions = [
        ("Laptop", "Electronics", 1200),
        ("Bread", "Grocery", 3),
        ("Smartphone", "Electronics", 800),
        ("Milk", "Grocery", 4),
        ("Headphones", "Electronics", 150),
        ("Apples", "Grocery", 5)
    ]

    # 1. Split data by category 
    electronics = [t for t in transactions if t[1] == "Electronics"]
    groceries = [t for t in transactions if t[1] == "Grocery"]

    # 2. Calculate Metrics 
    elec_revenue = sum(t[2] for t in electronics)
    groc_revenue = sum(t[2] for t in groceries)

    # 3. Identify Outliers (High Value Items)
    threshold = 500 
    big_ticket_items = [t[0] for t in transactions if t[2] >= threshold]

    print(f"Electronics Revenue: ${elec_revenue}")
    print(f"Grocery Revenue:     ${groc_revenue}")
    print(f"Items over ${threshold}: {', '.join(big_ticket_items)}")

sales_analytics()
