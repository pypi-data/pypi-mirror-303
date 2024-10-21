from openai import OpenAI


class Wrapper:
    def __init__(self):
        self.client = OpenAI(api_key="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")

    
    def moderate(self, message):
        """
        Moderate some text

        message: str        """
        response = self.client.moderations.create(
            model="omni-moderation-latest",
            input=message
        )
        response_dict = response.model_dump()
        results = response_dict['results'][0]

        flagged_categories = await main.get_flagged_categories(text=message.content)
        return flagged_categories
    

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
