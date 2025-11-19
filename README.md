# Customer Loyalty Reward Evaluation Algorithm (CLREA)

## Overview
This project implements a Customer Loyalty Reward Evaluation Algorithm that calculates loyalty points based on purchase amounts and determines customer tier upgrades.

## Description
The CLREA system manages a three-tier customer loyalty program:
- **Bronze** → **Silver** → **Gold**

Customers earn points based on their purchases, with multipliers applied according to their current status. When accumulated points reach certain thresholds, customers are automatically upgraded to higher tiers.

## Features
- Points calculation based on purchase amount and current status
- Automatic tier upgrade system
- Points multiplier system:
  - Gold: 2.0x multiplier
  - Silver: 1.5x multiplier
  - Bronze/Other: 1.0x multiplier
- Status upgrade thresholds:
  - Bronze: 500+ points
  - Silver: 2000+ points
  - Gold: 5000+ points

## Requirements
- Python 3.x

## Installation
No external dependencies required. Simply clone or download the repository.

```bash
git clone <repository-url>
cd SQE
```

## Usage

### Running the Program
```bash
python loyalty_program.py
```

### Function Signature
```python
calculate_loyalty(current_status, purchase_amount, current_points)
```

#### Parameters:
- `current_status` (str): Current customer status ('Gold', 'Silver', 'Bronze', or other)
- `purchase_amount` (float): Purchase amount in currency units
- `current_points` (int): Current accumulated loyalty points

#### Returns:
- `new_status` (str): Updated customer status after purchase
- `new_points` (int): Total accumulated points after purchase
- `message` (str): Congratulatory or informational message

### Example Usage
```python
from loyalty_program import calculate_loyalty

# Example: Gold customer making a $100 purchase with 5100 existing points
status, points, message = calculate_loyalty("Gold", 100.0, 5100)
print(f"Status: {status}, Points: {points}")
print(message)
```

## Test Cases
The program includes 6 test cases demonstrating various scenarios:

1. **TC1**: Gold status customer maintaining Gold tier
2. **TC2**: Silver customer upgrading to Gold
3. **TC3**: Bronze customer upgrading to Gold with large purchase
4. **TC4**: Bronze customer maintaining Bronze status
5. **TC5**: New customer ("Newbie") starting their loyalty journey
6. **TC6**: Unranked customer making a large purchase and upgrading

## Algorithm Logic

### Points Calculation
```
points_earned = purchase_amount × points_multiplier
new_points = current_points + points_earned
```

### Status Upgrade Logic
1. If `new_points >= 5000` and not already Gold → Upgrade to Gold
2. Else if `new_points >= 2000` and not Silver or Gold → Upgrade to Silver
3. Else if `new_points >= 500` and not Bronze, Silver, or Gold → Upgrade to Bronze

## Project Structure
```
SQE/
├── loyalty_program.py    # Main program file
└── README.md            # This file
```

## License
This project is created for educational purposes.

## Author
Software Quality Engineering Assignment

## Date
November 2025
