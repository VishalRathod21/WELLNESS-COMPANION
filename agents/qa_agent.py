from models.groq_model import GroqModel

class QAAgent:
    def __init__(self, model):
        self.model = model
        self.system_prompt = """You are a helpful assistant that answers questions about health and fitness plans.
        Only use the provided context to answer questions. If you don't know the answer, say so."""
    
    def generate_answer(self, context, question):
        prompt = f"""{self.system_prompt}
        
        Context:
        {context}
        
        Question: {question}
        
        Please provide a clear and concise answer based on the context above."""
        
        return self.model.generate(prompt)
