import re
import google.generativeai as genai
from datetime import datetime

class RuleBasedChatbot:
    def __init__(self, api_key):
        self.greetings = [re.compile(r"hi|hello|hey")]
        self.self_intro = [re.compile(r"what is your name"), re.compile(r"(.*) your name")]
        self.user_wellbeing = [re.compile(r"how are you")]
        self.time_and_weather = [re.compile(r"what is the weather like"), re.compile(r"what time is it")]
        self.hunger = [re.compile(r"(.*) (hungry|food)")]
        self.boredom = [re.compile(r"(.*) (bored|boring)")]
        self.calculations = {
            re.compile(r"add (\d+) and (\d+)"): self.add_numbers,
            re.compile(r"subtract (\d+) from (\d+)"): self.subtract_numbers,
            re.compile(r"multiply (\d+) and (\d+)"): self.multiply_numbers,
            re.compile(r"divide (\d+) by (\d+)"): self.divide_numbers,
        }
        
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-pro')

    def respond(self, user_input):
        user_input = user_input.lower()
        
        if any(pattern.match(user_input) for pattern in self.greetings):
            return self.format_response("Hello! How can I be of service today?")
        
        if any(pattern.match(user_input) for pattern in self.self_intro):
            return self.format_response("I'm a rule-based chatbot, created by uday. What's your name?")
        
        if any(pattern.match(user_input) for pattern in self.user_wellbeing):
            return self.format_response("I'm doing well, thanks for asking! How are you doing?")
        
        if any(pattern.match(user_input) for pattern in self.time_and_weather):
            if "time" in user_input:
                return self.format_response(self.get_current_time())
            elif "weather" in user_input:
                return self.format_response("I'm sorry, I don't have access to real-time weather information. You might want to check a weather app or website for the most up-to-date weather in your area.")
        
        if any(pattern.match(user_input) for pattern in self.hunger):
            return self.format_response("Feeling peckish, huh? How about a tasty sandwich or some refreshing fruit?")
        
        if any(pattern.match(user_input) for pattern in self.boredom):
            return self.format_response("Let's chase away the boredom! You could try reading a book, watching a movie, or taking a walk in nature.")
        
        for pattern, func in self.calculations.items():
            match = pattern.match(user_input)
            if match:
                return self.format_response(func(match))
        
        return self.format_response(self.respond_with_gemini(user_input))

    def format_response(self, response):
        lines = response.split('**')
        formatted_response = ""
        for i, line in enumerate(lines):
            if line.strip():
                if i % 2 == 1:  # Odd indexes are between ** and should be bold
                    formatted_response += f"<br><b>{line.strip()}</b><br>"
                else:
                    formatted_response += line.strip() + " "  # Add space to separate non-bold text
        return formatted_response.strip()  # Remove trailing space

    def respond_with_gemini(self, user_input):
        prompt = f"Respond to the following user input in a comprehensive and informative way: '{user_input}'. If the query involves current events, time, or other real-time information, provide a disclaimer that your knowledge cutoff is April 2024 and the information may not be up to date."
        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            return f"An error occurred while generating a response: {str(e)}"

    def get_current_time(self):
        now = datetime.now()
        return f"The current date and time is: {now.strftime('%Y-%m-%d %H:%M:%S')}"

    def add_numbers(self, match):
        num1, num2 = int(match.group(1)), int(match.group(2))
        return f"The sum of {num1} and {num2} is {num1 + num2}."

    def subtract_numbers(self, match):
        num1, num2 = int(match.group(2)), int(match.group(1))
        return f"The difference between {num2} and {num1} is {num2 - num1}."

    def multiply_numbers(self, match):
        num1, num2 = int(match.group(1)), int(match.group(2))
        return f"The product of {num1} and {num2} is {num1 * num2}."

    def divide_numbers(self, match):
        num1, num2 = int(match.group(1)), int(match.group(2))
        if num2 == 0:
            return "Division by zero is not possible."
        return f"{num1} divided by {num2} is {num1 / num2}."

# Note: The API key should be passed when initializing the chatbot in your main application file.