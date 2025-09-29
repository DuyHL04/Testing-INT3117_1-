def ticket_cost(age: int, daytype: str):
    if age < 0 or age > 100:
        return "Lỗi age"
    if daytype not in ["Weekday", "Weekend"]:
        return "Lỗi DayType"
    
    if age <= 12: #Child
        return 50000 if daytype == "Weekday" else 60000
    elif age <= 60: #Adult
        return 100000 if daytype == "Weekday" else 120000
    else: #Senior
        return 70000 if daytype == "Weekday" else 80000
    


