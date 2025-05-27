import streamlit as st
import random
from datetime import datetime
from pathlib import Path

# Load quotes
def load_quotes():
    file_path = Path("quotes.txt")
    if file_path.exists():
        with open(file_path, "r", encoding="utf-8") as f:
            return [line.strip() for line in f if line.strip()]
    else:
        return ["Stay strong! Keep going!"]
    
quotes = load_quotes()

# Background styling
def set_background():
    st.markdown(
        """
        <style>
        .stApp {
            background-image: url("https://images.unsplash.com/photo-1506784983877-45594efa4cbe");
            background-size: cover;
            background-repeat: no-repeat;
            background-position: center;
        }
        .quote-box {
            background-color: rgba(255, 255, 255, 0.8);
            padding: 30px;
            border-radius: 15px;
            font-size: 1.5em;
            text-align: center;
            box-shadow: 0 4px 8px rgba(0,0,0,0.2);
        }
        </style>
        """,
        unsafe_allow_html=True
    )

set_background()

# App title
st.title("🌞 Daily Motivation Generator")

# Show today's date
st.markdown(f"**{datetime.now().strftime('%A, %B %d, %Y')}**")

# Button to get a random quote
if st.button("✨ Inspire Me"):
    quote = random.choice(quotes)
    st.markdown(f"<div class= 'quote-box'>{quote}</div>", unsafe_allow_html=True)
else:
    st.markdown("<div class='quote-box'>Click the button to get inspired!</div>", unsafe_allow_html=True)
