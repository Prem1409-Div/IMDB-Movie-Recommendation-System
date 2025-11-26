# IMDb Movie Recommendation System 🎬

A content-based movie recommendation system that suggests movies based on their storylines. This project scrapes data from IMDb (2024 releases), processes the text using NLP techniques (TF-IDF), and provides recommendations via an interactive Streamlit web application.

## 🚀 Features

- **Data Scraping**: Automated scraping of movie titles and storylines from IMDb using Selenium.
- **NLP Powered**: Uses TF-IDF (Term Frequency-Inverse Document Frequency) and Cosine Similarity to find similar movies.
- **Interactive UI**: Premium dark-mode interface built with Streamlit for a modern user experience.
- **Custom Queries**: Users can input any plot description to get relevant movie suggestions.

## 🛠️ Tech Stack

- **Python**: Core programming language.
- **Selenium**: For web scraping IMDb data.
- **Pandas**: For data manipulation and storage.
- **Scikit-learn**: For TF-IDF vectorization and cosine similarity calculation.
- **Streamlit**: For the web application interface.

## 📂 Project Structure

```
├── app.py                  # Streamlit web application
├── recommender.py          # Recommendation engine logic
├── scraper.py              # Selenium script to scrape IMDb
├── imdb_2024_movies.csv    # Dataset (scraped movies)
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
```

## ⚙️ Installation

1.  **Clone the repository**:
    ```bash
    git clone <repository-url>
    cd <repository-folder>
    ```

2.  **Create a virtual environment** (optional but recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

## 🏃‍♂️ Usage

### 1. Run the Web App
To start the recommendation system:
```bash
streamlit run app.py
```
The app will open in your browser at `http://localhost:8501`.

### 2. (Optional) Scrape New Data
If you want to update the dataset with the latest movies:
```bash
python scraper.py
```
*Note: This requires Chrome browser installed.*

## 📊 How It Works

1.  **Input**: You enter a storyline (e.g., "A detective solves a murder mystery").
2.  **Processing**: The system converts your text into a numerical vector using TF-IDF.
3.  **Matching**: It calculates the cosine similarity between your input and the storylines of 2000+ movies in the database.
4.  **Output**: The top 5 most similar movies are displayed.

## 📸 Screenshots

![IMDb Recommender UI](refined_ui_grid_1764166179768.png)

## 📝 License

This project is for educational purposes. Data is sourced from IMDb.
