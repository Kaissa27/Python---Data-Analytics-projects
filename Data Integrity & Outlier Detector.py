def validate_sensor_data():
    # Raw Data: [Reading_ID, Temperature_Celsius]
    # Note: Some readings are clearly errors (999) or missing (None)
    raw_data = [
        ["ID_01", 22.5], ["ID_02", 23.1], ["ID_03", 999.0], 
        ["ID_04", 21.8], ["ID_05", None], ["ID_06", -50.0], 
        ["ID_07", 22.9], ["ID_08", 24.2]
    ]

    clean_readings = []
    errors = []

    print("--- Data Integrity Check ---")

    for record in raw_data:
        id_tag, value = record

        # 1. Null Check (Handling missing data)
        if value is None:
            errors.append(f"{id_tag}: Missing Value")
            continue

        # 2. Range Check (Logic: Room temp shouldn't be > 50 or < 0)
        if value > 50 or value < 0:
            errors.append(f"{id_tag}: Out of Range ({value})")
            continue

        # 3. Data is valid 
        clean_readings.append(value)

    # 4. Final Analysis on VALID data only
    if clean_readings:
        avg_temp = sum(clean_readings) / len(clean_readings)
        max_temp = max(clean_readings)
        min_temp = min(clean_readings)

        print(f"Valid Records:   {len(clean_readings)}")
        print(f"Average Temp:    {avg_temp:.2f}°C")
        print(f"Min/Max Range:   {min_temp}°C - {max_temp}°C")
    
    # 5. Error Reporting
    print("\n[!] Data Quality Alerts:")
    for err in errors:
        print(f" - {err}")

validate_sensor_data()