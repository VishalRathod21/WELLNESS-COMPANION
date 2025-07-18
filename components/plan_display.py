import streamlit as st

def display_plan(title, plan_data, main_section, tips_section=None):
    """Display a plan section with consistent styling.
    
    Args:
        title (str): The title of the plan section
        plan_data (dict): Dictionary containing the plan data
        main_section (dict): Configuration for the main content section
        tips_section (dict, optional): Configuration for the tips section
    """
    with st.container():
        st.markdown(f"### {title}")
        
        # Main content section
        if main_section.get('key') in plan_data:
            st.markdown(f"#### {main_section.get('title', '')}")
            st.markdown(plan_data[main_section['key']])
            
        # Plan details section
        if main_section.get('plan_key') in plan_data:
            st.markdown(f"#### {main_section.get('plan_title', '')}")
            st.markdown(plan_data[main_section['plan_key']])
        
        # Tips section if provided
        if tips_section and tips_section.get('key') in plan_data:
            st.markdown("---")
            st.markdown(f"#### {tips_section.get('title', '')}")
            st.markdown(plan_data[tips_section['key']])

def render_qa_history(qa_pairs):
    """Render the Q&A history section."""
    if not qa_pairs:
        return
        
    st.markdown("### 💬 Q&A History")
    
    for i, (question, answer) in enumerate(qa_pairs):
        with st.container():
            st.markdown(
                f"""
                <div class="card" style="margin-bottom: 1.5rem;">
                    <div style="margin-bottom: 1rem;">
                        <div style="
                            display: flex;
                            align-items: center;
                            margin-bottom: 0.5rem;
                            color: var(--text-primary);
                            font-weight: 600;
                        ">
                            <span style="
                                background: linear-gradient(90deg, #8A2BE2, #00BFFF);
                                width: 24px;
                                height: 24px;
                                border-radius: 50%;
                                display: flex;
                                align-items: center;
                                justify-content: center;
                                margin-right: 0.75rem;
                                flex-shrink: 0;
                                font-size: 0.8em;
                                color: white;
                            ">Q</span>
                            {question}
                        </div>
                        <div style="
                            display: flex;
                            align-items: flex-start;
                            background: rgba(0, 191, 255, 0.05);
                            padding: 1rem 1.25rem 1rem 2.5rem;
                            border-radius: 12px;
                            border-left: 3px solid #00BFFF;
                            margin-left: 0.75rem;
                        ">
                            <span style="
                                color: #00BFFF;
                                margin-right: 0.5rem;
                                margin-top: 2px;
                            ">→</span>
                            <div style="flex: 1;">
                                {answer}
                            </div>
                        </div>
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )
            
            if i < len(qa_pairs) - 1:
                st.markdown(
                    "<div style='height: 1px; background: rgba(255, 255, 255, 0.05); margin: 1.5rem 0;'></div>",
                    unsafe_allow_html=True
                )
