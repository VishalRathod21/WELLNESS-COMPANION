from models.groq_model import GroqModel

class ActivityAgent:
    def __init__(self, model):
        self.model = model
        self.system_prompt = """You are an Activity Planner that suggests lifestyle activities for overall well-being.
        Recommend activities that promote physical, mental, and emotional health based on the user's preferences and location."""
    
    def generate_plan(self, user_profile, additional_input):
        prompt = f"""{self.system_prompt}
        
        User Profile:
        {user_profile}
        
        Additional Input:
        {additional_input}
        
        Please suggest a variety of activities that would benefit this user.
        Include both indoor and outdoor options, and explain the benefits of each activity."""
        
        return self.model.generate(prompt)
