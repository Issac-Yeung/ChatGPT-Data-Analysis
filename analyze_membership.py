import pandas as pd
import os
from openai import OpenAI

# Load the Excel file
file_path = "membership_records_large.xlsx"
df = pd.read_excel(file_path)

# Convert DataFrame to CSV string
data_str = df.to_csv(index=False)

# Define the prompt
prompt = f"""
The following is a dataset of membership records. Please analyze the data and provide a summary including:
1. Total number of members
2. Number of members by membership type
3. Average join date by membership type
4. Distribution of members by gender
5. Any other relevant insights

Dataset:
{data_str}
"""

client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("OPENAI_API_KEY"),
)

# Define the messages for the chat completion
messages = [
    {
        "role": "user",
        "content": prompt
    }
]
chat_completion = client.chat.completions.create(
    messages=messages,
    model="gpt-3.5-turbo"
)
# Print the entire response for debugging
print(chat_completion)

# Attempt to access the message content correctly
try:
    message_content = chat_completion.choices[0].message.content.strip()
    print(message_content)
except Exception as e:
    print(f"Error accessing message content: {e}")
