from models.groq_model import GroqModel

class DietaryAgent:
    def __init__(self, model):
        self.model = model
        self.system_prompt = """You are a Dietary Expert that provides personalized meal plans based on user profiles and goals. 
        Focus on creating practical, healthy meal suggestions that align with the user's dietary preferences and restrictions."""
    
    def generate_plan(self, user_profile, additional_input):
        prompt = f"""{self.system_prompt}
        
        User Profile:
        {user_profile}
        
        Additional Input:
        {additional_input}
        
        Please provide a detailed meal plan including breakfast, lunch, dinner, and snacks.
        Explain the nutritional benefits and how this plan aligns with the user's goals."""
        
        return self.model.generate(prompt)
