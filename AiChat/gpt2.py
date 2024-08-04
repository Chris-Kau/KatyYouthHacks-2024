import os
from dotenv import load_dotenv, dotenv_values
load_dotenv()
key = os.getenv("OPENAIKEY")
import openai
openai.api_key = key
from datetime import datetime


class GPT():
    def __init__(self):
        super().__init__()
        time = x = datetime.today()
        day = x.strftime("%A")
        self.conversation_history = [{"role": "assistant", "content": f"Today's year: {x.year}, Today's day: {day}, Today's day of the month: {x.day}, Today's month: {x.month}"}]
        print("AHHHHHHHHHHHHHHH", self.conversation_history)
    def MakeSchedule(self, prompt):
        response = openai.ChatCompletion.create(
                model = "gpt-3.5-turbo",
                messages= self.conversation_history + [{"role": "user", "content": prompt},
                        {"role": "system", "content": "You are to help the user with organizing their events into their weekly schedule so everything is not crammed.Preferrably, you should not have the same or similar event on the same day if that event is more than 3 hours, unless told otherwise by the user. The week starts on Sundays and ends on Saturdays. Your only output should be in the format: (Today's Date, StartTime - EndTime, Event, Event Description). The Calendar Date should be in the format: (Today's Year/Today's Month/Name of today's day/Today's day of the month) Do not say anything else other than the given format."}]
            )
        return response.choices[0].message.content.strip()

    def chat_with_bot(self, prompt):
        self.conversation_history.append({"role": "user", "content": prompt})
        response = openai.ChatCompletion.create(
                model = "gpt-3.5-turbo",
                messages= self.conversation_history + [{"role": "user", "content": prompt},
                        {"role": "system", "content": "You are to help the user with organizing their events into their weekly schedule so everything is not crammed.Preferrably, you should not have the same or similar event on the same day if that event is more than 3 hours, unless told otherwise by the user. The week starts on Sundays and ends on Saturdays. Be friendly and try not to go off topic. If the user asks to recall something from the past, you have the conversation history"}]
            )
        self.conversation_history.append({"role": "assistant", "content": response.choices[0].message.content.strip()})
        return response.choices[0].message.content.strip()


# if __name__ == "__main__":
#     gpt = GPT()
#     while True:
#         user_input = input("You: ")
#         if user_input.lower() in ["quit", "exit"]:
#             break
#         response = gpt.MakeSchedule(user_input)
#         print("Chat bot:", response)