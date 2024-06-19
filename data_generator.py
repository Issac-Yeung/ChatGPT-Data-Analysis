import pandas as pd
import random
from faker import Faker

fake = Faker()

# Function to generate a random Canadian postal code
def generate_canadian_postal_code():
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numbers = '0123456789'
    return f"{random.choice(letters)}{random.choice(numbers)}{random.choice(letters)} {random.choice(numbers)}{random.choice(letters)}{random.choice(numbers)}"

# Function to generate a random gender
def generate_gender():
    return random.choice(["Male", "Female"])

# Generate sample data
data = {
    "Membership ID": [i for i in range(1001, 1101)],
    "First Name": [fake.first_name() for _ in range(100)],
    "Last Name": [fake.last_name() for _ in range(100)],
    "Email": [fake.email() for _ in range(100)],
    "Phone Number": [fake.phone_number() for _ in range(100)],
    "Address": [fake.street_address() for _ in range(100)],
    "City": ["Winnipeg" for _ in range(100)],
    "State/Province": ["MB" for _ in range(100)],
    "Postal Code": [generate_canadian_postal_code() for _ in range(100)],
    "Join Date": [fake.date_between(start_date='-3y', end_date='today') for _ in range(100)],
    "Membership Type": [random.choice(["Regular", "Premium"]) for _ in range(100)],
    "Date of Birth": [fake.date_of_birth(minimum_age=18, maximum_age=90) for _ in range(100)],
    "Gender": [generate_gender() for _ in range(100)]
}

# Create DataFrame
df = pd.DataFrame(data)

# Save to Excel in the current working directory
file_path = "membership_records_large.xlsx"
df.to_excel(file_path, index=False)

# Output the path of the generated file
print(f"Membership records have been saved to {file_path}")
