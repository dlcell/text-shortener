from openai import OpenAI
from os import getenv
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()

client = OpenAI(api_key=getenv("OPENAI_API_KEY"))

# Define the text you want summarized via input
print("what text do you want to summarize?")
long_text = input()

# Create a prompt for summarization
prompt = f"Summarize this text in 2-3 sentences:\n\n{long_text}\n\nSummary:"

# Call the OpenAI API
response = client.chat.completions.create(model="gpt-3.5-turbo",
messages=[
    {"role": "user", "content": prompt}
],
temperature=0.5,
max_tokens=100)

# Extract and print the summary
summary = response.choices[0].message.content.strip()
print("\nSummary:", summary)