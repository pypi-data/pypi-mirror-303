from openai import OpenAI


class Wrapper:
    def __init__(self, api_key):
        self.api_key = api_key
        self.client = OpenAI(api_key=self.api_key)

    
    def moderate(self, message):
        """
        Moderate some text

        message: str        """
        response = self.client.moderations.create(
            model="omni-moderation-latest",
            input=message
        )
        return response
    

    def completion(self, model, message, system_message):
        """
        Get a chat completion

        model: str
        message: str
        system_message: str
        """
        response = self.client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": system_message},
                {"role": "user", "content": message}
                ]
            )
        return response.choices[0].message
    

    def image(self, model, prompt):
        response = self.client.images.generate(
            model=model,
            prompt=prompt,
            size="1024x1024",
            quality="standard",
            n=1
        )
        return response.data[0].url