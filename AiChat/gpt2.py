import os
from dotenv import load_dotenv, dotenv_values
load_dotenv()
key = os.getenv("OPENAIKEY")
import openai
openai.api_key = key

def chat_with_gpt(prompt):
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt},
                  {"role": "system", "content": "You are to help the user with organizing their events into their weekly schedule so everything is not crammed.Preferrably, you should not have the same or similar event on the same day if that event is more than 3 hours, unless told otherwise by the user. The week starts on Sundays and ends on Saturdays. Your only output should be in the format: (Day, StartTime - EndTime, Event, Event Description). Do not say anything else other than the given format."}]
    )

    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit"]:
            break
        response = chat_with_gpt(user_input)
        print("Chat bot:", response)