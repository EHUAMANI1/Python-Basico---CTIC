# -*- coding: utf-8 -*-
"""
Created on Fri Mar 14 12:19:48 2025

@author: Gatito
"""

# Simulación de matrícula en cursos

class MatriculaUni:
    def __init__(self):
        self.cursos = [
            "Evaluación Social de Proyectos",
            "Derivados Financieros",
            "Política Económica",
            "Actuarial",
            "Análisis y Gestión de Riesgo Financieros"
        ]
        self.matriculados = []

    def mostrar_cursos(self):
        print("Cursos disponibles para matrícula:")
        for idx, curso in enumerate(self.cursos, start=1):
            print(f"{idx}. {curso}")

    def matricular(self, curso_id):
        if 1 <= curso_id <= len(self.cursos):
            curso = self.cursos[curso_id - 1]
            if curso not in self.matriculados:
                self.matriculados.append(curso)
                print(f"¡Te has matriculado en el curso: {curso}!")
            else:
                print(f"Ya estás matriculado en el curso: {curso}")
        else:
            print("ID de curso inválido. Intenta de nuevo.")

    def mostrar_matriculas(self):
        if self.matriculados:
            print("\nCursos en los que estás matriculado:")
            for curso in self.matriculados:
                print(f"- {curso}")
        else:
            print("No estás matriculado en ningún curso.")

def main():
    matricula = MatriculaUni()
    while True:
        print("\nBienvenido al sistema de matrícula 'Matricula Uni'.")
        matricula.mostrar_cursos()
        try:
            opcion = int(input("\nSelecciona el número del curso para matricularte (0 para salir): "))
            if opcion == 0:
                print("¡Gracias por usar el sistema de matrícula!")
                break
            matricula.matricular(opcion)
            matricula.mostrar_matriculas()
        except ValueError:
            print("Por favor, ingresa un número válido.")

if __name__ == "__main__":
    main()
    