import streamlit as st

def display_plan(title, content, key_details, tips=None):
    """
    Display a plan section with modern dark theme styling
    
    Args:
        title (str): Section title
        content (dict): Dictionary containing the plan content
        key_details (dict): Configuration for the main content display
        tips (dict, optional): Configuration for the tips section
    """
    with st.container():
        # Header with gradient text
        st.markdown(f"""
        <h2 style="
            background: linear-gradient(90deg, #8A2BE2, #00BFFF);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin: 0 0 1.5rem 0;
            font-weight: 700;
            display: flex;
            align-items: center;
            gap: 0.5rem;
        ">
            {title.split(' ')[0]}
            <span style="background: linear-gradient(90deg, #00BFFF, #8A2BE2);
                      -webkit-background-clip: text;
                      -webkit-text-fill-color: transparent;">
                {' '.join(title.split(' ')[1:])}
            </span>
        </h2>
        """, unsafe_allow_html=True)
        
        # Main content area
        with st.container():
            cols = st.columns([3, 1] if tips else [1], gap="large")
            
            # Left column - Main content
            with cols[0]:
                # Why this plan works section
                with st.expander(f"🔍 {key_details['title']}", expanded=True):
                    info_content = content.get(key_details['key'], 'No information available')
                    st.markdown(
                        f"""
                        <div style="
                            padding: 1.5rem;
                            border-radius: 16px;
                            background: rgba(255, 255, 255, 0.03);
                            border-left: 4px solid #8A2BE2;
                            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.2);
                            backdrop-filter: blur(10px);
                            margin: 1rem 0;
                        ">
                            {info_content}
                        </div>
                        """,
                        unsafe_allow_html=True
                    )
                
                # Plan details section
                st.markdown(f"#### 📋 {key_details['plan_title']}")
                plan_content = content.get(key_details['plan_key'], 'Plan details not available')
                st.markdown(
                    f"""
                    <div style="
                        padding: 1.75rem;
                        margin: 1.5rem 0;
                        background: rgba(255, 255, 255, 0.03);
                        border: 1px solid rgba(255, 255, 255, 0.1);
                        border-radius: 16px;
                        box-shadow: 0 4px 25px rgba(0, 0, 0, 0.2);
                        backdrop-filter: blur(10px);
                    ">
                        {plan_content}
                    </div>
                    """,
                    unsafe_allow_html=True
                )
            
            # Right column - Tips (if provided)
            if tips and len(cols) > 1:
                with cols[1]:
                    st.markdown(f"#### 💡 {tips['title']}")
                    tips_content = content.get(tips['key'], '')
                    if tips_content:
                        tip_items = [t.strip() for t in tips_content.split('\n') if t.strip()]
                        for i, tip in enumerate(tip_items):
                            st.markdown(
                                f"""
                                <div style="
                                    padding: 1.25rem;
                                    margin-bottom: 1rem;
                                    background: rgba(0, 180, 255, 0.08);
                                    border-left: 3px solid #00B4D8;
                                    border-radius: 12px;
                                    transition: transform 0.2s, box-shadow 0.2s;
                                    &:hover {{
                                        transform: translateY(-2px);
                                        box-shadow: 0 6px 15px rgba(0, 0, 0, 0.15);
                                    }}
                                ">
                                    <div style="display: flex; align-items: flex-start;">
                                        <span style="
                                            background: #00B4D8;
                                            width: 24px;
                                            height: 24px;
                                            border-radius: 50%;
                                            display: flex;
                                            align-items: center;
                                            justify-content: center;
                                            margin-right: 0.75rem;
                                            flex-shrink: 0;
                                            color: #0a1929;
                                            font-weight: bold;
                                            font-size: 0.8em;
                                        ">{i+1}</span>
                                        <span style="flex: 1;">{tip}</span>
                                    </div>
                                </div>
                                """,
                                unsafe_allow_html=True
                            )
                    else:
                        st.markdown(
                            """
                            <div style="
                                padding: 1.25rem;
                                background: rgba(255, 255, 255, 0.03);
                                border: 1px dashed rgba(255, 255, 255, 0.2);
                                border-radius: 12px;
                                color: rgba(255, 255, 255, 0.6);
                                text-align: center;
                            ">
                                No tips available for this section.
                            </div>
                            """,
                            unsafe_allow_html=True
                        )
        
        # Additional considerations (if any)
        if 'important_considerations' in content and content['important_considerations']:
            with st.expander("📌 Important Considerations", expanded=False):
                considerations = content['important_considerations']
                st.markdown(
                    f"""
                    <div style="
                        background: rgba(255, 193, 7, 0.08);
                        padding: 1.5rem;
                        border-radius: 12px;
                        border-left: 4px solid #FFC107;
                        margin: 1rem 0;
                    ">
                        {considerations}
                    </div>
                    """,
                    unsafe_allow_html=True
                )
        
        st.markdown(
            """
            <div style="
                height: 1px;
                background: linear-gradient(90deg, transparent, rgba(255,255,255,0.1), transparent);
                margin: 2rem 0;
            "></div>
            """,
            unsafe_allow_html=True
        )

def setup_page():
    """Configure the page settings and load global styles with dark theme"""
    st.set_page_config(
        page_title="Wellness360 | Your AI Health & Lifestyle Planner",
        page_icon="✨",
        layout="wide",
        initial_sidebar_state="expanded",
        menu_items={
            'Get Help': 'https://github.com/yourusername/vitalis-ai',
            'Report a bug': 'https://github.com/yourusername/vitalis-ai/issues',
            'About': "### Vitalis AI\nYour intelligent health and wellness companion."
        }
    )
    
    # Load Google Fonts and set global styles
    st.markdown("""
    <link href='https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap' rel='stylesheet'>
    <style>
        :root {
            --primary: #6C63FF;
            --primary-dark: #5A4DFF;
            --secondary: #00B4D8;
            --success: #06D6A0;
            --warning: #FFD166;
            --danger: #EF476F;
            --light: #F8F9FA;
            --dark: #212529;
            --gray: #6C757D;
            --light-gray: #E9ECEF;
            --border-radius: 12px;
            --box-shadow: 0 4px 20px rgba(0, 0, 0, 0.05);
            --transition: all 0.3s ease;
        }
        
        /* Base Styles */
        * {
            font-family: 'Inter', sans-serif;
            box-sizing: border-box;
        }
        
        body {
            color: var(--dark);
            background-color: #F8FAFF;
            line-height: 1.6;
        }
        
        /* Main Container */
        .main {
            max-width: 1400px;
            padding: 2rem 3rem !important;
            margin: 0 auto;
        }
        
        /* Typography */
        h1, h2, h3, h4, h5, h6 {
            color: var(--dark);
            font-weight: 700;
            line-height: 1.3;
            margin-bottom: 1rem;
        }
        
        h1 { font-size: 2.5rem; }
        h2 { font-size: 2rem; }
        h3 { font-size: 1.75rem; }
        h4 { font-size: 1.5rem; }
        h5 { font-size: 1.25rem; }
        h6 { font-size: 1rem; }
        
        p {
            margin-bottom: 1rem;
            color: var(--gray);
        }
        
        /* Sidebar */
        .css-1d391kg {
            background-color: #FFFFFF !important;
            border-right: 1px solid var(--light-gray) !important;
            padding: 1.5rem !important;
        }
        
        /* Buttons */
        .stButton > button {
            background: linear-gradient(135deg, var(--primary) 0%, var(--primary-dark) 100%) !important;
            border: none !important;
            color: white !important;
            font-weight: 600 !important;
            border-radius: var(--border-radius) !important;
            padding: 0.75rem 1.5rem !important;
            transition: var(--transition) !important;
            box-shadow: 0 4px 6px rgba(108, 99, 255, 0.2) !important;
            width: 100% !important;
            text-transform: none !important;
            font-size: 1rem !important;
        }
        
        .stButton > button:hover {
            transform: translateY(-2px) !important;
            box-shadow: 0 6px 12px rgba(108, 99, 255, 0.25) !important;
        }
        
        /* Form Elements */
        .stTextInput > div > div > input,
        .stNumberInput > div > div > input,
        .stSelectbox > div > div,
        .stTextArea > div > div > textarea {
            border-radius: var(--border-radius) !important;
            border: 1px solid var(--light-gray) !important;
            padding: 0.75rem 1rem !important;
            transition: var(--transition) !important;
            font-size: 0.95rem !important;
        }
        
        .stTextInput > div > div > input:focus,
        .stNumberInput > div > div > input:focus,
        .stSelectbox > div > div:focus,
        .stTextArea > div > div > textarea:focus {
            border-color: var(--primary) !important;
            box-shadow: 0 0 0 3px rgba(108, 99, 255, 0.1) !important;
            outline: none !important;
        }
        
        /* Cards */
        .card {
            background: white;
            border-radius: var(--border-radius);
            padding: 1.5rem;
            box-shadow: var(--box-shadow);
            border: 1px solid var(--light-gray);
            transition: var(--transition);
            margin-bottom: 1.5rem;
        }
        
        .card:hover {
            transform: translateY(-4px);
            box-shadow: 0 8px 30px rgba(0, 0, 0, 0.1);
        }
        
        /* Tabs */
        .stTabs [data-baseweb="tab-list"] {
            gap: 8px;
            margin-bottom: 1.5rem;
        }
        
        .stTabs [data-baseweb="tab"] {
            padding: 0.75rem 1.5rem;
            border-radius: var(--border-radius);
            margin: 0 2px;
            transition: var(--transition);
            font-weight: 500;
            color: var(--gray);
        }
        
        .stTabs [aria-selected="true"] {
            background-color: var(--primary) !important;
            color: white !important;
            font-weight: 600;
        }
        
        /* Expanders */
        .stExpander {
            margin-bottom: 1.5rem;
        }
        
        .stExpander > div > div[data-testid="stExpanderContentInner"] {
            padding: 1.5rem 0;
        }
        
        /* Progress Bars */
        .stProgress > div > div > div > div {
            background: linear-gradient(90deg, var(--primary), var(--secondary)) !important;
            border-radius: 4px;
        }
        
        /* Responsive Design */
        @media (max-width: 768px) {
            .main {
                padding: 1rem !important;
            }
            
            .stButton > button {
                margin: 0.5rem 0;
            }
        }
    </style>
    """, unsafe_allow_html=True)
