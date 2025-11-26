import streamlit as st
from recommender import MovieRecommender
import time

# Page configuration
st.set_page_config(
    page_title="IMDb Movie Recommender",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for premium look
st.markdown("""
    <style>
    /* Main Background with Gradient */
    .stApp {
        background: radial-gradient(circle at top left, #1a1c24, #0e1117);
    }
    
    /* Hide Streamlit elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Typography Colors - High Contrast */
    h1, h2, h3 {
        color: #f5c518 !important; /* IMDb Yellow */
        text-shadow: 0 2px 4px rgba(0,0,0,0.5);
    }
    
    p, label, .stMarkdown {
        color: #e2e8f0 !important; /* Bright White-Grey */
    }
    
    /* Button Styling */
    .stButton>button {
        width: 100%;
        background: linear-gradient(45deg, #f5c518, #e2b616);
        color: #000000 !important;
        font-weight: 800;
        border: none;
        padding: 0.6rem 1rem;
        border-radius: 8px;
        text-transform: uppercase;
        letter-spacing: 1px;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(245, 197, 24, 0.2);
    }
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(245, 197, 24, 0.4);
        color: #000000 !important;
    }
    
    /* Movie Card Styling */
    .movie-card {
        background: rgba(30, 33, 40, 0.8);
        backdrop-filter: blur(10px);
        border-radius: 16px;
        padding: 24px;
        height: 100%;
        border: 1px solid rgba(255, 255, 255, 0.1);
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        position: relative;
        overflow: hidden;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3);
    }
    
    .movie-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 4px;
        background: linear-gradient(90deg, #f5c518, #f7df7c);
        opacity: 0;
        transition: opacity 0.3s ease;
    }
    
    .movie-card:hover {
        transform: translateY(-8px);
        box-shadow: 0 12px 30px rgba(0, 0, 0, 0.5);
        border-color: #f5c518;
    }
    
    .movie-card:hover::before {
        opacity: 1;
    }
    
    .movie-title {
        color: #ffffff !important;
        font-size: 1.4rem;
        font-weight: 700;
        margin-bottom: 12px;
        display: flex;
        align-items: center;
        gap: 10px;
    }
    
    .movie-story {
        color: #cbd5e0 !important;
        font-size: 0.95rem;
        line-height: 1.6;
        margin-bottom: 16px;
        display: -webkit-box;
        -webkit-line-clamp: 4;
        -webkit-box-orient: vertical;
        overflow: hidden;
    }
    
    .meta-tag {
        display: inline-flex;
        align-items: center;
        background: rgba(245, 197, 24, 0.15);
        color: #f5c518 !important;
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 0.85rem;
        font-weight: 600;
        border: 1px solid rgba(245, 197, 24, 0.3);
    }
    
    /* Input Area */
    .stTextArea textarea {
        background-color: rgba(26, 28, 36, 0.8) !important;
        color: #ffffff !important;
        border: 1px solid #4a5568 !important;
        border-radius: 12px;
    }
    .stTextArea textarea:focus {
        border-color: #f5c518 !important;
        box-shadow: 0 0 0 1px #f5c518 !important;
    }
    .stTextArea label {
        color: #f5c518 !important;
        font-weight: 600;
    }
    
    /* Placeholder Color */
    .stTextArea textarea::placeholder {
        color: #a0aec0 !important;
        opacity: 1; /* Firefox */
    }
    </style>
    """, unsafe_allow_html=True)

# Initialize recommender
@st.cache_resource
def get_recommender():
    recommender = MovieRecommender()
    if recommender.load_data():
        recommender.train()
    return recommender

recommender = get_recommender()

# Header Section
col_h1, col_h2 = st.columns([3, 1])
with col_h1:
    st.title("🎬 IMDb NLP Recommender")
    st.markdown("### *Discover movies through the power of AI*")

# Search Section
st.markdown("<br>", unsafe_allow_html=True)
search_col1, search_col2 = st.columns([4, 1])

with search_col1:
    storyline_input = st.text_area(
        "Search Query",
        placeholder="Describe the movie plot you're looking for... (e.g., 'A detective hunting a serial killer in a rainy city')",
        height=80,
        label_visibility="collapsed"
    )

with search_col2:
    st.markdown("<div style='height: 10px'></div>", unsafe_allow_html=True)
    search_button = st.button("Find Movies", type="primary")

# Results Section
if search_button:
    if not storyline_input.strip():
        st.warning("⚠️ Please enter a storyline description first.")
    else:
        if recommender.df is None:
            st.error("❌ Error: Could not load movie data.")
        else:
            with st.spinner("🔍 Analyzing 2000+ storylines..."):
                time.sleep(0.8) # UX delay
                recommendations = recommender.get_recommendations(storyline_input)
            
            if recommendations:
                st.markdown("<br><h3>✨ Recommended for You</h3><br>", unsafe_allow_html=True)
                
                # Grid Layout
                cols = st.columns(2) # 2 columns grid
                
                for idx, movie in enumerate(recommendations):
                    col = cols[idx % 2]
                    with col:
                        match_score = int(movie['Score']*100)
                        st.markdown(f"""
                        <div class="movie-card">
                            <div class="movie-title">
                                <span>{idx + 1}. {movie['Title']}</span>
                            </div>
                            <div class="movie-story">
                                {movie['Storyline']}
                            </div>
                            <div class="meta-tag">
                                🎯 {match_score}% Match
                            </div>
                        </div>
                        <br>
                        """, unsafe_allow_html=True)
            else:
                st.info("No matches found. Try describing the plot differently.")

# Footer
st.markdown("<br><br><br>", unsafe_allow_html=True)
st.markdown(
    """
    <div style='text-align: center; color: #718096; padding: 20px;'>
        <small>Powered by TF-IDF & Cosine Similarity • Data: IMDb 2024</small>
    </div>
    """, 
    unsafe_allow_html=True
)
