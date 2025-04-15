# 🎬 IMDb Movie Recommendation System Using Storylines

This project is an intelligent movie recommender system that suggests movies based on storyline similarity. It scrapes 2024 movie data from IMDb using Selenium and applies Natural Language Processing (NLP) techniques like **TF-IDF** and **Cosine Similarity** to recommend top 5 similar movies. The app comes with a user-friendly **Streamlit** interface.

---

## 🚀 Features

- 🔍 Scrapes 2024 movie names and storylines from IMDb
- 🧹 Cleans and pre-processes movie storylines using NLP
- 📊 Converts storylines into numerical vectors using TF-IDF
- 🤝 Uses Cosine Similarity to compute storyline similarity
- 🎯 Recommends top 5 movies based on user-input storyline
- 🌐 Interactive and simple UI built with Streamlit

---

## 📁 Project Structure

\`\`\`
imdb_movie_recommender/
│
├── data/
│   └── imdb_2024_movies.csv          # Scraped movie data
│
├── scripts/
│   ├── scraper.py                    # Selenium-based IMDb scraper
│   ├── preprocessing.py              # Text cleaning and TF-IDF vectorization
│   ├── recommender.py                # Cosine similarity recommendation logic
│   └── utils.py                      # (Optional) Helper functions
│
├── app/
│   └── streamlit_app.py              # Streamlit UI
│
├── requirements.txt                  # Required libraries
└── README.md                         # Project overview
\`\`\`

---

## 🧠 Skills You Will Learn

- Web Scraping with Selenium  
- Natural Language Processing (NLP)  
- TF-IDF, Cosine Similarity  
- Data Cleaning and Preprocessing  
- Data Analysis and Recommendation Systems  
- Streamlit Web App Development  
- Python Best Practices & Modularity  

---

## 📦 Installation

1. **Clone this repository**
\`\`\`bash
git clone https://github.com/yourusername/imdb-movie-recommender.git
cd imdb-movie-recommender
\`\`\`

2. **Create and activate a virtual environment (optional but recommended)**
\`\`\`bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
\`\`\`

3. **Install dependencies**
\`\`\`bash
pip install -r requirements.txt
\`\`\`

---

## 🛠 How to Run

### Step 1: Scrape IMDb Movies (2024)
\`\`\`bash
python scripts/scraper.py
\`\`\`

This saves the data to `data/imdb_2024_movies.csv`.

### Step 2: Run Streamlit App
\`\`\`bash
streamlit run app/streamlit_app.py
\`\`\`

Now open your browser to `http://localhost:8501` to interact with the recommender system.

---

## ✨ Example Use Case

**Input:**
> "A young wizard begins his journey at a magical school where he makes friends and enemies, facing dark forces along the way."

**Output:**
1. The Wizard’s Journey  
2. The Magic Academy  
3. The Dark Sorcerer  
4. Mystic Trials  
5. Shadow of the Realm

---

## 📊 Technologies Used

- **Languages:** Python  
- **Web Scraping:** Selenium  
- **NLP:** NLTK, Scikit-learn  
- **Recommendation Logic:** TF-IDF, Cosine Similarity  
- **Frontend:** Streamlit  
- **Visualization:** Streamlit, Seaborn (optional)  
- **IDE:** VS Code  

---

## 📂 Dataset

Scraped live from IMDb 2024 using Selenium.  
**Columns:** `Movie Name`, `Storyline`  
**Format:** CSV

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).



