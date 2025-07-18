import streamlit as st

def render_hero():
    """Render the hero section of the application."""
    # Create the hero content
    st.markdown(
        """
        <div class="hero-container">
            <div class="hero-content">
                <div class="hero-badge">
                    🚀 YOUR PERSONAL WELLNESS COMPANION
                </div>
                <h1 class="hero-title">
                    Elevate Your Health with <span class="highlight">AI-Powered</span> Wellness
                </h1>
                <p class="hero-description">
                    Experience a new standard in health and wellness with our intelligent platform 
                    that crafts <span class="highlight">personalized plans</span> tailored to your unique needs, 
                    helping you achieve your wellness goals effectively.
                </p>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    # Create the features grid using Streamlit columns for better control
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown(
            """
            <div class="feature-card">
                <div class="feature-icon" style="color: #7B2CBF;">🧠</div>
                <h3>Smart Recommendations</h3>
                <p>Get personalized suggestions that evolve with your progress and feedback for better results.</p>
            </div>
            """,
            unsafe_allow_html=True
        )
    
    with col2:
        st.markdown(
            """
            <div class="feature-card">
                <div class="feature-icon" style="color: #00B4D8;">🔒</div>
                <h3>Your Privacy, Our Priority</h3>
                <p>We value your trust. Your data stays secure with end-to-end encryption and strict privacy controls.</p>
            </div>
            """,
            unsafe_allow_html=True
        )
    
    with col3:
        st.markdown(
            """
            <div class="feature-card">
                <div class="feature-icon" style="color: #00C897;">🌐</div>
                <h3>Comprehensive Wellness</h3>
                <p>Benefit from a holistic approach that considers all aspects of your health and lifestyle.</p>
            </div>
            """,
            unsafe_allow_html=True
        )
    
    # Add gradient circles
    st.markdown(
        """
        <div class="gradient-circle top-right"></div>
        <div class="gradient-circle bottom-right"></div>
        """,
        unsafe_allow_html=True
    )
    
    # Add the CSS styles
    st.markdown(
        """
        <style>
            .hero-container {
                position: relative;
                padding: 2rem 0;
                overflow: hidden;
            }
            
            .hero-content {
                position: relative;
                z-index: 2;
                max-width: 1200px;
                margin: 0 auto;
                padding: 0 1.5rem;
            }
            
            .hero-badge {
                display: inline-block;
                background: rgba(123, 44, 191, 0.1);
                color: #7B2CBF;
                padding: 0.5rem 1rem;
                border-radius: 50px;
                font-size: 0.8rem;
                font-weight: 600;
                margin-bottom: 1.5rem;
                letter-spacing: 1px;
            }
            
            .hero-title {
                font-size: 3rem;
                font-weight: 800;
                line-height: 1.2;
                margin: 0 0 1.5rem 0;
                background: linear-gradient(90deg, #FFFFFF, #A0A0A0);
                -webkit-background-clip: text;
                background-clip: text;
                -webkit-text-fill-color: transparent;
            }
            
            .hero-description {
                font-size: 1.25rem;
                line-height: 1.6;
                color: rgba(255, 255, 255, 0.8);
                margin-bottom: 3rem;
                max-width: 800px;
            }
            
            .highlight {
                background: linear-gradient(90deg, #7B2CBF, #00B4D8);
                -webkit-background-clip: text;
                background-clip: text;
                -webkit-text-fill-color: transparent;
                font-weight: 700;
            }
            
            .features-grid {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
                gap: 1.5rem;
                margin: 2rem 0;
            }
            
            .feature-card {
                background: rgba(255, 255, 255, 0.03);
                border: 1px solid rgba(255, 255, 255, 0.05);
                border-radius: 12px;
                padding: 1.5rem;
                transition: transform 0.3s ease, box-shadow 0.3s ease;
            }
            
            .feature-card:hover {
                transform: translateY(-5px);
                box-shadow: 0 10px 20px rgba(0, 0, 0, 0.2);
            }
            
            .feature-icon {
                font-size: 2rem;
                margin-bottom: 1rem;
                display: inline-block;
            }
            
            .feature-card h3 {
                color: #FFFFFF;
                margin: 0 0 0.75rem 0;
                font-size: 1.25rem;
            }
            
            .feature-card p {
                color: rgba(255, 255, 255, 0.7);
                margin: 0;
                font-size: 0.95rem;
                line-height: 1.6;
            }
            
            .gradient-circle {
                position: absolute;
                border-radius: 50%;
                filter: blur(60px);
                opacity: 0.4;
                z-index: 1;
            }
            
            .gradient-circle.top-right {
                width: 400px;
                height: 400px;
                top: -200px;
                right: -200px;
                background: radial-gradient(circle, rgba(0, 180, 216, 0.5) 0%, rgba(0, 180, 216, 0) 70%);
            }
            
            .gradient-circle.bottom-right {
                width: 600px;
                height: 600px;
                bottom: -300px;
                right: -300px;
                background: radial-gradient(circle, rgba(123, 44, 191, 0.5) 0%, rgba(123, 44, 191, 0) 70%);
            }
            
            @media (max-width: 768px) {
                .hero-title {
                    font-size: 2rem;
                }
                
                .hero-description {
                    font-size: 1.1rem;
                }
                
                .features-grid {
                    grid-template-columns: 1fr;
                }
            }
        </style>
        """,
        unsafe_allow_html=True
    )

def render_generate_button():
    """Render the generate plan button."""
    return st.button(
        "✨ Generate My Personalized Plan",
        key="generate_btn",
        use_container_width=True,
        help="Click to create your customized health and wellness plan"
    )
