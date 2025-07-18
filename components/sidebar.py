import streamlit as st

def render_sidebar():
    """Render the sidebar with user profile and tips."""
    with st.sidebar:
        st.markdown(
            """
            <div style="
                background: linear-gradient(135deg, rgba(138, 43, 226, 0.1) 0%, rgba(0, 191, 255, 0.1) 100%);
                padding: 1.5rem;
                border-radius: 16px;
                margin-bottom: 1.5rem;
                border: 1px solid rgba(255, 255, 255, 0.1);
            ">
                <h3 style="margin: 0 0 1rem 0; color: #FFFFFF; display: flex; align-items: center; gap: 0.5rem;">
                    <span style="background: linear-gradient(90deg, #8A2BE2, #00BFFF);
                              -webkit-background-clip: text;
                              -webkit-text-fill-color: transparent;">👤</span> 
                    Your Profile
                </h3>
                <p style="margin: 0; color: rgba(255, 255, 255, 0.7); font-size: 0.9rem;">
                    Fill in your details to get personalized recommendations
                </p>
            </div>
            
            <div style="
                background: rgba(30, 30, 30, 0.5);
                padding: 1rem;
                border-radius: 12px;
                margin: 1.5rem 0;
                border: 1px solid rgba(255, 255, 255, 0.05);
            ">
                <div class="tips-container">
                    <h4 class="tips-title">
                        <span>💡</span> Essential Tips
                    </h4>
                    <div class="tips-list">
                        <div class="tip-card tip-card--purple">
                            <p class="tip-text">Stay consistent with 3-4 weekly workouts</p>
                        </div>
                        <div class="tip-card tip-card--blue">
                            <p class="tip-text">Hydrate well throughout the day</p>
                        </div>
                        <div class="tip-card tip-card--green">
                            <p class="tip-text">Prioritize 7-8 hours of sleep</p>
                        </div>
                    </div>
                </div>
            </div>
            <style>
                .tips-container {
                    background: rgba(255, 255, 255, 0.03);
                    border-radius: 10px;
                    padding: 1.25rem;
                    margin-bottom: 1.5rem;
                }
                .tips-title {
                    color: #FFFFFF;
                    margin-top: 0;
                    margin-bottom: 1rem;
                    font-size: 1rem;
                    display: flex;
                    align-items: center;
                    gap: 0.5rem;
                }
                .tips-list {
                    display: flex;
                    flex-direction: column;
                    gap: 0.75rem;
                }
                .tip-card {
                    background: rgba(255, 255, 255, 0.03);
                    padding: 0.75rem;
                    border-radius: 8px;
                    margin-bottom: 0.5rem;
                }
                .tip-card--purple {
                    border-left: 3px solid #7B2CBF;
                }
                .tip-card--blue {
                    border-left: 3px solid #00B4D8;
                }
                .tip-card--green {
                    border-left: 3px solid #2ED573;
                }
                .tip-text {
                    color: #FFFFFF;
                    font-size: 0.85rem;
                    font-weight: 500;
                    line-height: 1.4;
                    margin: 0;
                }
            </style>
            """,
            unsafe_allow_html=True
        )
        

        with st.expander("📋 Personal Information", expanded=True):
            col1, col2 = st.columns(2)
            with col1:
                age = st.number_input("Age", min_value=10, max_value=100, step=1, 
                                   help="Your current age in years")
                height = st.number_input("Height (cm)", min_value=100.0, max_value=250.0, step=0.1,
                                      help="Your height in centimeters")
                activity_level = st.selectbox(
                    "Activity Level", 
                    ["Sedentary", "Lightly Active", "Moderately Active", "Very Active", "Extremely Active"],
                    help="How active you are in your daily life"
                )
                dietary_preferences = st.selectbox(
                    "Dietary Preferences", 
                    ["None", "Vegetarian", "Vegan", "Keto", "Paleo", "Gluten Free", "Dairy Free", "Pescatarian", "Low Carb", "Other"],
                    help="Your dietary restrictions or preferences"
                )
            with col2:
                weight = st.number_input("Weight (kg)", min_value=20.0, max_value=300.0, step=0.1,
                                      help="Your current weight in kilograms")
                sex = st.selectbox("Sex", ["Male", "Female", "Other"],
                                help="Your biological sex for accurate calculations")
                fitness_goals = st.selectbox(
                    "Fitness Goals", 
                    ["Lose Weight", "Gain Muscle", "Improve Endurance", "Maintain Fitness", "Strength Training", "General Health"],
                    help="What you want to achieve with your fitness plan"
                )
                work_type = st.selectbox(
                    "Work Type", 
                    ["Student", "Desk Job", "Field Work", "Remote Work", "Manual Labor", "Healthcare", "Retail", "Other"],
                    help="Your typical work environment"
                )
                country = st.text_input("Country", placeholder="e.g., United States",
                                     help="Your country for region-specific recommendations")
        
        with st.expander("🎯 Additional Preferences", expanded=False):
            additional_input = st.text_area(
                "Tell us more about your goals, challenges, or preferences", 
                placeholder="E.g., I have a knee injury, I prefer home workouts, I'm allergic to nuts...",
                help="Any additional information that can help us personalize your plan"
            )
            
            st.markdown("#### 🏆 Weekly Goal")
            goal_intensity = st.slider(
                "How intense do you want your plan to be?", 
                1, 5, 3,
                help="1 = Very Light, 5 = Very Intense",
                key="goal_intensity"
            )
            
            st.markdown("#### ⏰ Available Time")
            available_time = st.slider(
                "How much time can you dedicate daily? (minutes)", 
                15, 180, 60, 15,
                help="Your daily time commitment for the plan",
                key="available_time"
            )
    
    # Return all the collected data
    return {
        'age': age,
        'height': height,
        'weight': weight,
        'sex': sex,
        'activity_level': activity_level,
        'dietary_preferences': dietary_preferences,
        'fitness_goals': fitness_goals,
        'work_type': work_type,
        'country': country,
        'additional_input': additional_input,
        'goal_intensity': goal_intensity,
        'available_time': available_time
    }
