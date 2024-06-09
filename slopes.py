def calculate_skiers_snowboarders(total_visitors, skier_percentage):
    
    skiers = int(total_visitors * skier_percentage)
    snowboarders = total_visitors - skiers
    return skiers, snowboarders

def calculate_first_aid_needs(total_visitors, first_aid_percentage):
    
    first_aid_needed = int(total_visitors * first_aid_percentage)
    return first_aid_needed

# Example usage
total_visitors = 500  # Replace with the actual total number of visitors
skier_percentage = 0.6  # Assume 60% are skiers
first_aid_percentage = 0.05  # Assume 5% might need first-aid treatment

skiers, snowboarders = calculate_skiers_snowboarders(total_visitors, skier_percentage)
first_aid_needed = calculate_first_aid_needs(total_visitors, first_aid_percentage)

print(f"Number of skiers: {skiers}")
print(f"Number of snowboarders: {snowboarders}")
print(f"Number of riders needing first-aid treatment: {first_aid_needed}")
