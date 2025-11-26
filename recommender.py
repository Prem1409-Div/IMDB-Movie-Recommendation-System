import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import re
import sys

# Force UTF-8 output for Windows terminals
sys.stdout.reconfigure(encoding='utf-8')

class MovieRecommender:
    def __init__(self, data_path="imdb_2024_movies.csv"):
        """
        Initialize the recommender with the movie dataset.
        """
        self.data_path = data_path
        self.df = None
        self.tfidf_vectorizer = None
        self.tfidf_matrix = None
        
    def load_data(self):
        """
        Load data from CSV and perform basic preprocessing.
        """
        try:
            self.df = pd.read_csv(self.data_path)
            print(f"✅ Loaded {len(self.df)} movies from {self.data_path}")
            
            # Basic cleaning
            self.df['Storyline'] = self.df['Storyline'].fillna('')
            self.df['Title'] = self.df['Title'].fillna('Unknown Title')
            
            # Preprocess storylines (simple cleaning)
            self.df['clean_storyline'] = self.df['Storyline'].apply(self._preprocess_text)
            
            return True
        except FileNotFoundError:
            print(f"❌ File not found: {self.data_path}")
            return False
        except Exception as e:
            print(f"❌ Error loading data: {e}")
            return False

    def _preprocess_text(self, text):
        """
        Clean text: lowercase, remove punctuation.
        """
        text = str(text).lower()
        text = re.sub(r'[^\w\s]', '', text)
        return text
            
    def train(self):
        """
        Build the TF-IDF matrix.
        """
        if self.df is None:
            print("❌ Data not loaded. Call load_data() first.")
            return

        print("🔄 Training recommender model...")
        
        # Initialize TF-IDF Vectorizer with English stop words
        self.tfidf_vectorizer = TfidfVectorizer(stop_words='english')
        
        # Fit and transform the processed storylines
        self.tfidf_matrix = self.tfidf_vectorizer.fit_transform(self.df['clean_storyline'])
        
        print("✅ Model trained successfully!")

    def get_recommendations(self, query_text, n_recommendations=5):
        """
        Get movie recommendations based on a text query (storyline).
        """
        if self.tfidf_matrix is None:
            print("❌ Model not trained. Call train() first.")
            return []

        # Preprocess the query
        clean_query = self._preprocess_text(query_text)
        
        # Transform the query to a vector
        query_vec = self.tfidf_vectorizer.transform([clean_query])
        
        # Calculate cosine similarity between query and all movies
        # cosine_similarity returns a shape of (1, n_movies)
        similarity_scores = cosine_similarity(query_vec, self.tfidf_matrix).flatten()
        
        # Get indices of top matches (sorted descending)
        # We use argsort which sorts ascending, so we take the last n items and reverse
        top_indices = similarity_scores.argsort()[-n_recommendations:][::-1]
        
        results = []
        for idx in top_indices:
            # Only include if similarity is somewhat relevant (optional, but good practice)
            # For now, we return top 5 regardless of score, but we could filter > 0
            if similarity_scores[idx] > 0:
                results.append({
                    "Title": self.df.iloc[idx]['Title'],
                    "Storyline": self.df.iloc[idx]['Storyline'],
                    "Score": float(similarity_scores[idx])
                })
        
        return results

if __name__ == "__main__":
    # Example usage
    recommender = MovieRecommender()
    if recommender.load_data():
        recommender.train()
        
        test_query = "A young wizard goes to a magic school."
        print(f"\n🔍 Query: {test_query}")
        recs = recommender.get_recommendations(test_query)
        
        for i, movie in enumerate(recs, 1):
            print(f"{i}. {movie['Title']} (Score: {movie['Score']:.2f})")
