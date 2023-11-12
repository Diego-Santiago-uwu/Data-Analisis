from bs4 import BeautifulSoup
import requests
import pandas as pd
import re

def parse_rating(rating_text):
    # Extraer la opinión, puntuación general y facilidad usando expresiones regulares
    match = re.search(r'(\D+)(\d+\.?\d*)Calidad General(\d+\.?\d*)Facilidad', rating_text)
    if match:
        return match.group(1).strip(), match.group(2), match.group(3)
    return '', '', ''

def auto_Scrapper_Class(html_soup, course_case, professor_id):
    rows = html_soup.find_all('tr')[1:]  # Saltar el encabezado de la tabla

    for row in rows:
        date = row.find('div', class_='date').get_text(strip=True) if row.find('div', class_='date') else ''
        rating_block = row.find('div', class_='rating-block')
        rating_text = rating_block.get_text(strip=True) if rating_block else ''
        opinion, general_score, facility = parse_rating(rating_text)
        class_name = row.find('span', class_='response').get_text(strip=True) if row.find('span', class_='response') else ''
        comment_element = row.find('p', class_='commentsParagraph')
        if comment_element:
            comments = comment_element.get_text(strip=True)
            if not comments:  # Si los comentarios están vacíos (cadena vacía)
                comments = None
        else:
            comments = None

        course_case.append({
            'professor_id': professor_id,
            'date': date,
            'opinion': opinion,
            'general_score': general_score,
            'facility': facility,
            'class': class_name,
            'personal_comment': comments
        })
def main():
    data = []
    links = [
        "https://www.misprofesores.com/profesores/Jose-Alonso-Alanis-Rojas_152405",
        "https://www.misprofesores.com/profesores/Rodrigo-Alarcon-flores_164799",
        "https://www.misprofesores.com/profesores/Noe-Andres-Anaya-Badillo_134868",
        "https://www.misprofesores.com/profesores/Jonathan-Abimael-Anaya-Guarneros_132330",
        "https://www.misprofesores.com/profesores/hortencia-caballero-lopez_90459",
        "https://www.misprofesores.com/profesores/Dandy-Calla-Choque_124028",
        "https://www.misprofesores.com/profesores/Jesus-Castelan-Martinez_139025",
        "https://www.misprofesores.com/profesores/MARIA-DEL-CARMEN-ANGELICA-MORENO-ARGUELLO_123987",
        "https://www.misprofesores.com/profesores/Raul-Puente-Mancilla_78555",
        "https://www.misprofesores.com/profesores/MI-Armando-Moises-Perez-Silva_118727",
        "https://www.misprofesores.com/profesores/Luis-Enrique-Quintanar-Cortes_90578",
        "https://www.misprofesores.com/profesores/Brayan-Tellez-Cruz_156865"
    ]

    for index, link in enumerate(links, start=1):
        response = requests.get(link)
        html_soup = BeautifulSoup(response.content, 'html.parser')
        auto_Scrapper_Class(html_soup, data, professor_id=index)

    courses_df = pd.DataFrame(data)
    courses_df.to_csv('MisProfesores.csv', index=False)
    print(courses_df.head())

if __name__ == "__main__":
    main()