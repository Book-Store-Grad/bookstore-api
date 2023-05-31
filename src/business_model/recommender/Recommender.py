from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from src.business_model.recommender.BookLoader import BookLoader


class Recommender:
    # Preprocess text features
    tfidf = TfidfVectorizer(stop_words='english')

    def __init__(self, books: BookLoader):
        self.books = books.get_books()
        self.book_features = self.tfidf.fit_transform(self.books['b_description'])

        # Calculate cosine similarity matrix
        self.cosine_sim_matrix = cosine_similarity(self.book_features, self.book_features)

    def run(self, book_index, top_n=5):
        # Get the similarity scores for the given book
        similarity_scores = self.cosine_sim_matrix[book_index]

        # Get the indices of top-N similar books (excluding the given book itself)
        top_indices = similarity_scores.argsort()[::-1][1:top_n+1]

        # Get the recommended book titles
        recommended_books = self.books.loc[top_indices, 'b_name']

        recommended_books = recommended_books.to_list()

        return recommended_books

