# __init__.py

from g4f.client import Client

class TurboTalk:
    def __init__(self):
        self.client = Client()
        self.response_content = ""

    def give_response(self, company_name, bot_name, behaviour, user_message):
        messages = [{
            "role": "user",
            "content": (
                user_message + " and to ans me behave very very strongly just like " + behaviour + 
                " as I am a/an " + behaviour + " type person. And if asked any questions in which you have to say anything like who are you or have to give your identity and info then you have to tell me about yourself and introduce yourself as " + 
                bot_name + " by " + company_name + " and is in a learning or developing stage also give a little explanation about it like company name how powerful it will be in future but it is still in developing stage right now and all those things."
            )
        }]

        try:
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=messages,
            )
            self.response_content = response.choices[0].message.content

        except Exception as e:
            self.response_content = f"An error occurred: {e}"

    def get_response(self):
        return self.response_content

turbo_talk_instance = TurboTalk()
 
