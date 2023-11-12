import analisis_misprofes
import cursos
import estudiantes

def main():
    # Ejecutar el script de web scraping para cursos
    cursos.main()

    # Generar opiniones aleatorias de estudiantes
    estudiantes.main()

    # Ejecutar el análisis de comentarios de profesores
    analisis_misprofes.main()


if __name__ == "__main__":
    main()