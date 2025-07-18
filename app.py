import os
import streamlit as st
from dotenv import load_dotenv

# Import components
from components.sidebar import render_sidebar
from components.hero import render_hero, render_generate_button
from components.plan_display import display_plan, render_qa_history

# Import agents
from models.groq_model import GroqModel
from agents.dietary_agent import DietaryAgent
from agents.fitness_agent import FitnessAgent
from agents.activity_agent import ActivityAgent
from agents.qa_agent import QAAgent

# Load environment variables
load_dotenv()

# Set page config
st.set_page_config(
    page_title="Vitalis AI | Your Health Companion",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load CSS
with open("static/css/styles.css") as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

def initialize_agents():
    """Initialize AI agents with API key."""
    groq_api_key = os.getenv("GROQ_API_KEY")
    if not groq_api_key:
        st.error("❌ GROQ_API_KEY not found in environment variables")
        return None
    
    try:
        groq_model = GroqModel(api_key=groq_api_key)
        return {
            'dietary': DietaryAgent(groq_model),
            'fitness': FitnessAgent(groq_model),
            'activity': ActivityAgent(groq_model),
            'qa': QAAgent(groq_model)
        }
    except Exception as e:
        st.error(f"❌ Error initializing AI agents: {e}")
        return None

def generate_plans(agents, user_data):
    """Generate all plans using the AI agents."""
    with st.spinner("🔮 Crafting your perfect health and fitness routine..."):
        user_profile = f"""
        Age: {user_data['age']}, Weight: {user_data['weight']}kg, 
        Height: {user_data['height']}cm, Sex: {user_data['sex']},
        Activity Level: {user_data['activity_level']}, 
        Dietary Preferences: {user_data['dietary_preferences']},
        Fitness Goals: {user_data['fitness_goals']}, 
        Work Type: {user_data['work_type']}, 
        Country: {user_data['country']}
        """

        try:
            # Generate dietary plan
            with st.spinner("🍽️ Generating your personalized dietary plan..."):
                st.session_state.dietary_plan = {
                    "why_this_plan_works": agents['dietary'].generate_plan(user_profile, user_data['additional_input']),
                    "meal_plan": agents['dietary'].generate_plan(user_profile, user_data['additional_input']),
                    "important_considerations": agents['dietary'].generate_plan(user_profile, user_data['additional_input'])
                }

            # Generate fitness plan
            with st.spinner("💪 Creating your fitness routine..."):
                st.session_state.fitness_plan = {
                    "goals": agents['fitness'].generate_plan(user_profile, user_data['additional_input']),
                    "routine": agents['fitness'].generate_plan(user_profile, user_data['additional_input']),
                    "tips": agents['fitness'].generate_plan(user_profile, user_data['additional_input'])
                }

            # Generate activity plan
            with st.spinner("🌟 Planning your activities..."):
                st.session_state.activity_plan = {
                    "suggestions": agents['activity'].generate_plan(user_profile, user_data['additional_input']),
                    "why_these": agents['activity'].generate_plan(user_profile, user_data['additional_input'])
                }

            st.session_state.plans_generated = True
            st.rerun()
            
        except Exception as e:
            st.error(f"❌ An error occurred while generating plans: {e}")

def render_qa_tab(agents):
    """Render the Q&A tab."""
    st.markdown(
        """
        <div class="qa-container">
            <h3 class="qa-title">
                <span>❓ Questions about your plan?</span>
            </h3>
            <p class="qa-description">
                Ask anything about your personalized plan and get instant AI-powered answers.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    # Question input
    question = st.text_input(
        "Your question",
        placeholder="E.g., Can you suggest vegetarian alternatives?",
        label_visibility="collapsed"
    )
    
    if st.button("🔍 Get Answer", use_container_width=True):
        if question:
            with st.spinner("🔍 Finding the best answer for you..."):
                try:
                    context = f"""
                    Dietary Plan: {st.session_state.dietary_plan.get('meal_plan', '')}
                    Fitness Plan: {st.session_state.fitness_plan.get('routine', '')}
                    Activity Plan: {st.session_state.activity_plan.get('suggestions', '')}
                    """
                    answer = agents['qa'].generate_answer(context, question)
                    if 'qa_pairs' not in st.session_state:
                        st.session_state.qa_pairs = []
                    st.session_state.qa_pairs.append((question, answer))
                    st.rerun()
                except Exception as e:
                    st.error(f"❌ An error occurred while getting the answer: {e}")
    
    # Display Q&A history
    if 'qa_pairs' in st.session_state and st.session_state.qa_pairs:
        render_qa_history(st.session_state.qa_pairs)

def main():
    """Main application function."""
    # Initialize session state
    if 'dietary_plan' not in st.session_state:
        st.session_state.dietary_plan = {}
        st.session_state.fitness_plan = {}
        st.session_state.activity_plan = {}
        st.session_state.qa_pairs = []
        st.session_state.plans_generated = False
    
    # Initialize agents
    agents = initialize_agents()
    if not agents:
        return
    
    # Render sidebar and get user data
    user_data = render_sidebar()
    
    # Render hero section
    render_hero()
    
    # Main content area
    col1, _ = st.columns([3, 1], gap="large")
    
    with col1:
        # Generate plan button
        if render_generate_button():
            generate_plans(agents, user_data)
        
        # Display generated plans
        if st.session_state.plans_generated:
            st.markdown("<div style='margin-top: 2rem;'></div>", unsafe_allow_html=True)
            
            # Create tabs for different plan sections
            tab1, tab2, tab3, tab4 = st.tabs([
                "📋 Dietary Plan", 
                "💪 Fitness Plan", 
                "🌟 Activity Plan",
                "❓ Ask Questions"
            ])
            
            with tab1:
                if 'dietary_plan' in st.session_state and st.session_state.dietary_plan:
                    display_plan(
                        "🍽️ Your Personalized Dietary Plan", 
                        st.session_state.dietary_plan,
                        {"title": "Why this plan works", "key": "why_this_plan_works", 
                         "plan_title": "🍽️ Meal Plan", "plan_key": "meal_plan"}
                    )
                else:
                    st.info("No dietary plan generated yet.")
            
            with tab2:
                if 'fitness_plan' in st.session_state and st.session_state.fitness_plan:
                    display_plan(
                        "💪 Your Personalized Fitness Plan", 
                        st.session_state.fitness_plan,
                        {"title": "🎯 Goals", "key": "goals", 
                         "plan_title": "🏋️‍♂️ Exercise Routine", "plan_key": "routine"},
                        {"title": "💡 Pro Tips", "key": "tips"}
                    )
                else:
                    st.info("No fitness plan generated yet.")
            
            with tab3:
                if 'activity_plan' in st.session_state and st.session_state.activity_plan:
                    display_plan(
                        "🌟 Suggested Activities", 
                        st.session_state.activity_plan,
                        {"title": "Why these activities?", "key": "why_these", 
                         "plan_title": "🎉 Activity Suggestions", "plan_key": "suggestions"}
                    )
                else:
                    st.info("No activity plan generated yet.")
                    
            with tab4:
                render_qa_tab(agents)

if __name__ == "__main__":
    main()
