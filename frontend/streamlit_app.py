import streamlit as st
import requests
import datetime
import os
import time

# --- CONFIGURATION ---
BASE_URL = os.getenv('BACKEND_URL', 'http://localhost:8000')

st.set_page_config(
    page_title='AI Trip Planner | Premium Experience',
    page_icon='🌍',
    layout='wide',
    initial_sidebar_state='expanded'
)

# --- CUSTOM CSS ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    .main {
        background-color: #f8f9fa;
    }

    /* Hero Section */
    .hero-container {
        background: linear-gradient(135deg, #1e3a8a 0%, #3b82f6 100%);
        padding: 3rem;
        border-radius: 1rem;
        color: white;
        margin-bottom: 2rem;
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
    }

    .hero-title {
        font-size: 3rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
    }

    .hero-subtitle {
        font-size: 1.25rem;
        opacity: 0.9;
    }

    /* Custom Cards */
    .stCard {
        background: white;
        padding: 1.5rem;
        border-radius: 0.75rem;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
        border: 1px solid #e5e7eb;
        margin-bottom: 1.5rem;
    }

    /* Buttons */
    .stButton>button {
        background: linear-gradient(135deg, #3b82f6 0%, #2563eb 100%);
        color: white;
        border: none;
        padding: 0.5rem 2rem;
        border-radius: 0.5rem;
        font-weight: 600;
        transition: all 0.3s ease;
        width: 100%;
    }

    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 10px 15px -3px rgba(59, 130, 246, 0.4);
    }

    /* Input Styling */
    .stTextInput>div>div>input {
        border-radius: 0.5rem;
    }

    /* Result Area */
    .result-container {
        background-color: white;
        color: #1f2937 !important;
        padding: 2rem;
        border-radius: 1rem;
        border-left: 5px solid #3b82f6;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
        margin-top: 1rem;
        line-height: 1.6;
    }
    .result-container * {
        color: #1f2937 !important;
    }
    .result-container code {
        background-color: #f1f5f9 !important;
        color: #1e3a8a !important;
        padding: 0.2rem 0.4rem !important;
        border-radius: 0.25rem !important;
        font-family: monospace;
    }
</style>
""", unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    st.image("https://img.icons8.com/clouds/200/airplane-take-off.png", width=150)
    st.title("Settings")
    
    st.markdown("### 🛠 Configuration")
    model_choice = st.selectbox("AI Intelligence", ["Standard", "Pro (Detailed)", "Fast"], index=0)
    budget_level = st.select_slider("Budget Level", options=["Budget", "Moderate", "Luxury"], value="Moderate")
    
    st.divider()
    st.markdown("### ℹ️ About")
    st.info("AI Trip Planner generates personalized travel itineraries using advanced AI agents.")
    st.caption("v2.0.0 | Created by Mehedi Hasan")

# --- MAIN UI ---
# Hero Section
st.markdown("""
<div class="hero-container">
    <div class="hero-title">Plan Your Next Adventure 🌍</div>
    <div class="hero-subtitle">Unlock personalized travel itineraries powered by AI. Just tell us where you're dreaming of!</div>
</div>
""", unsafe_allow_html=True)

# Layout: Two columns for input
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("### 📍 Tell us your plans")
    with st.container():
        user_input = st.text_area("What's on your mind?", 
                                 placeholder="e.g., I want to visit Japan for 10 days in April. Focus on food and historical sites. My budget is moderate.",
                                 height=150)
        
        c1, c2, c3 = st.columns(3)
        with c1:
            dest = st.text_input("Destination (Optional)", placeholder="e.g. Tokyo")
        with c2:
            duration = st.number_input("Duration (Days)", min_value=1, max_value=30, value=7)
        with c3:
            travel_type = st.multiselect("Interests", ["Food", "Nature", "History", "Shopping", "Adventure", "Relaxation"], default=["Food"])

        submit_button = st.button("✨ Generate My Itinerary")

with col2:
    st.markdown("### 💡 Quick Tips")
    st.write("- **Be specific**: Mention interests like 'vegan food' or 'hiking'.")
    st.write("- **Dates matter**: AI can check seasonal events.")
    st.write("- **Group size**: Let us know if you're traveling solo or with family!")
    
    # Placeholder for a beautiful image
    st.image("https://images.unsplash.com/photo-1503220317375-aaad61436b1b?auto=format&fit=crop&q=80&w=1000", caption="Let's Explore the World", width="stretch")

# --- PROCESSING ---
if submit_button:
    if not user_input.strip() and not dest.strip():
        st.warning("Please tell us where you want to go!")
    else:
        # Construct a rich query if specific fields are used
        query = user_input
        if dest or duration:
            query = f"Plan a trip to {dest if dest else 'somewhere amazing'} for {duration} days. "
            if travel_type:
                query += f"Interests include: {', '.join(travel_type)}. "
            query += f"Additional details: {user_input}"

        try:
            with st.status("🏝 Crafting your perfect journey...", expanded=True) as status:
                st.write("Searching for paths...")
                time.sleep(1) # Visual flair
                st.write("Analyzing destinations...")
                
                payload = {'question': query}
                response = requests.post(f'{BASE_URL}/query', json=payload)
                
                if response.status_code == 200:
                    status.update(label="✅ Itinerary Ready!", state="complete", expanded=False)
                    answer = response.json().get('answer', 'No answer returned.')
                    
                    st.divider()
                    st.markdown("## 🎊 Your Personalized Travel Plan")
                    
                    # Using a styled container for the result
                    with st.container():
                        st.markdown(f"""
                        <div class="result-container">
                        {answer}
                        </div>
                        """, unsafe_allow_html=True)
                    
                    st.caption(f"Generated on {datetime.datetime.now().strftime('%Y-%m-%d at %H:%M')}")
                    
                    # Add download button
                    st.download_button(
                        label="📄 Download Plan as Text",
                        data=answer,
                        file_name=f"Trip_Plan_{datetime.datetime.now().strftime('%Y%m%d')}.txt",
                        mime="text/plain"
                    )
                else:
                    status.update(label="❌ Planning Failed", state="error")
                    st.error(f"Error: {response.text}")
        
        except Exception as e:
            st.error(f"An unexpected error occurred: {e}")

# Footer
st.markdown("---")
st.markdown("<p style='text-align: center; color: #6b7280;'>Powered by LangGraph & Groq | Made with ❤️ for Travelers</p>", unsafe_allow_html=True)