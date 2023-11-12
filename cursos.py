from bs4 import BeautifulSoup
import requests
import pandas as pd

def auto_Scrapper_Class(html_soup, course_case, professor_id):
    rows = html_soup.find_all('tr')[1:]  # Saltar el encabezado de la tabla

    for row in rows:
        # Extraer los elementos de cada fila
        date = row.find('div', class_='date').get_text(strip=True) if row.find('div', class_='date') else ''
        rating = row.find('div', class_='rating-block').get_text(strip=True) if row.find('div', class_='rating-block') else ''
        class_name = row.find('span', class_='response').get_text(strip=True) if row.find('span', class_='response') else ''
        comments = row.find('p', class_='commentsParagraph').get_text(strip=True) if row.find('p', class_='commentsParagraph') else ''

        # Agregar al dataset
        course_case.append({
            'professor_id': professor_id,
            'date': date,
            'rating': rating,
            'class': class_name,
            'comment': comments
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