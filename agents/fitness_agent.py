from models.groq_model import GroqModel

class FitnessAgent:
    def __init__(self, model):
        self.model = model
        self.system_prompt = """You are a Fitness Expert that creates personalized workout routines. 
        Design effective exercise plans based on the user's fitness level, goals, and available equipment."""
    
    def generate_plan(self, user_profile, additional_input):
        prompt = f"""{self.system_prompt}
        
        User Profile:
        {user_profile}
        
        Additional Input:
        {additional_input}
        
        Please create a detailed workout plan including warm-up, main exercises, and cool-down.
        Include sets, reps, and rest periods. Explain the benefits of each exercise."""
        
        return self.model.generate(prompt)
