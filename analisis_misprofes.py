import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel


def clean_text(author):
    result = str(author).lower()
    return(result.replace(' ',''))

def main():
    # Cargar el archivo CSV
    data = pd.read_csv('MisProfesores.csv')

    def clean_text(author):
        result = str(author).lower()
        return result.replace(' ', '')

    data['professor_id'] = data['professor_id'].apply(clean_text)
    data['professor_id'] = data['professor_id'].astype(str).str.lower()
    data['professor_id'] = data['professor_id'].astype(str).str.lower()

    # Ejemplo de lista de stop words en español
    stop_words_espanol = [
        'y', 'o', 'un', 'una', 'con', 'en'
    ]

    # Inicialización del TfidfVectorizer con stop words en español
    tfidf_espanol = TfidfVectorizer(stop_words=stop_words_espanol)
    data['personal_comment'] = data['personal_comment'].fillna('')

    overview_matrix = tfidf_espanol.fit_transform(data['personal_comment'])
    print(overview_matrix.shape)

    similarity_matrix = linear_kernel(overview_matrix, overview_matrix)
    print(similarity_matrix)

if __name__ == "__main__":
    main()