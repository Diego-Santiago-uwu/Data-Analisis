import csv
import random

def main():
    materias_permitidas = [
        "Sistemas Operativos",
        "Recursos de la construcción",
        "Lab.Mecánica de fluidos",
        "Algebra lineal",
        "CyGA",
        "Geología Estructural",
        "Geología de Yacimientos",
        "Cálculo Integral",
        "Fundamentos de Metalurgia Extractiva",
        "Diseño de Operaciones Metalúrgicas",
        "Lab. Teoría Electromagnética",
        "Lab de CD",
        "Lab Comunicaciones Digitales",
        "Máquinas",
        "Máquinas Eléctricas",
        "Teoría Electromagnética",
        "Ecuaciones diferenciales",
        "Probabilidad",
        "Análisis de sistemas eléctricos",
        "Matemáticas para las Ciencias de la Tierra III",
        "Física",
        "python",
        "EDA 2"
    ]

    opiniones_estudiantes = []
    for _ in range(50):
        opinion = {
            "materia": random.choice(materias_permitidas),
            "calidad": random.randint(1, 5),
            "metodo_ensenanza": random.randint(1, 5),
            "interes": random.randint(1, 5),
            "calificacion_general": random.randint(1, 5)
        }
        opiniones_estudiantes.append(opinion)

    nombre_archivo = "opiniones_estudiantes_50.csv"

    with open(nombre_archivo, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["materia", "calidad", "metodo_ensenanza", "interes",
                                                  "calificacion_general"])

        writer.writeheader()
        for opinion in opiniones_estudiantes:
            writer.writerow(opinion)

if __name__ == "__main__":
    main()