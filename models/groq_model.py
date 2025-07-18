from groq import Groq

class GroqModel:
    def __init__(self, api_key, model_name="llama3-70b-8192"):
        self.client = Groq(api_key=api_key)
        self.model_name = model_name
    
    def generate(self, prompt, temperature=0.4):
        try:
            completion = self.client.chat.completions.create(
                messages=[{"role": "user", "content": prompt}],
                model=self.model_name,
                temperature=temperature
            )
            return completion.choices[0].message.content
        except Exception as e:
            raise Exception(f"Groq API error: {e}")
