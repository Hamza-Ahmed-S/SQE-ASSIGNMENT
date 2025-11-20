def calculate_loyalty(current_status, purchase_amount, current_points):
    """
    Customer Loyalty Reward Evaluation Algorithm (CLREA)
    Calculates loyalty points based on purchase value and determines
    if the customer qualifies for a tier upgrade:
    Bronze → Silver → Gold.
    """
    # (1)
    points_multiplier = 0
    new_points = current_points
    new_status = current_status
    status_change = False
    # (2)
    # Determine multiplier based on status
    if current_status == 'Gold':
        points_multiplier = 2.0
    elif current_status == 'Silver':
        points_multiplier = 1.5
    else:
        points_multiplier = 1.0

     # (3)
    # Calculate and add points
    points_earned = int(purchase_amount * points_multiplier)
    new_points += points_earned

     # (4)
    # Status upgrade conditions
    if new_points >= 5000:
        # (5)
        if current_status != 'Gold':
            new_status = 'Gold'
            status_change = True
    elif new_points >= 2000:
        # (6)
        if current_status not in ('Silver', 'Gold'):
            new_status = 'Silver'
            status_change = True
    elif new_points >= 500:
         # (7)
        if current_status not in ('Bronze', 'Silver', 'Gold'):
            new_status = 'Bronze'
            status_change = True
    # (8)
    if status_change:
        message = f"Congratulations! You earned {points_earned} points and were upgraded to {new_status} status."
    else:
        message = f"You earned {points_earned} points. Your status remains {new_status}."
    # (9)
    return new_status, new_points, message
if __name__ == "__main__":
    print("TC1:", calculate_loyalty("Gold", 100.0, 5100))
    print("TC2:", calculate_loyalty("Silver", 3500.0, 3000))
    print("TC3:", calculate_loyalty("Bronze", 2100.0, 0))
    print("TC4:", calculate_loyalty("Bronze", 100.0, 600))
    print("TC5:", calculate_loyalty("Newbie", 100.0, 0))
    print("TC6:", calculate_loyalty("Unranked", 5000.0, 0))
