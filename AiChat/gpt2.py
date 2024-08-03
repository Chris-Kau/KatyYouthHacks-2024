import os
from dotenv import load_dotenv, dotenv_values
load_dotenv()
key = os.getenv("OPENAIKEY")
import openai
openai.api_key = key


class GPT():
    def __init__(self):
        super().__init__()
    
    def MakeSchedule(self, prompt):
        response = openai.ChatCompletion.create(
                model = "gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt},
                        {"role": "system", "content": "You are to help the user with organizing their events into their weekly schedule so everything is not crammed.Preferrably, you should not have the same or similar event on the same day if that event is more than 3 hours, unless told otherwise by the user. The week starts on Sundays and ends on Saturdays. Your only output should be in the format: (Day, StartTime - EndTime, Event, Event Description). Do not say anything else other than the given format. If the user does not give events only say 'Please provide me with the time of an event and the event description'"}]
            )
        return response.choices[0].message.content.strip()



if __name__ == "__main__":
    gpt = GPT()
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit"]:
            break
        response = gpt.MakeSchedule(user_input)
        print("Chat bot:", response)