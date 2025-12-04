#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Application de gestion d'une école
"""
from typing import Optional

from business.school import School
from models.teacher import Teacher

def display_teacher(school: School, teacher: Optional[Teacher]) -> None:
    if teacher is None or teacher.id is None:
        print("\nLe professeur à cet ID n'existe pas.")
        return
    display_item(teacher, f"Affichage du prof {teacher.first_name} {teacher.last_name}")
    display_list(school.get_teacher_courses(teacher.id), f"Affichage des cours de {teacher.first_name} {teacher.last_name}")

def display_list(items: list, title: str) -> None:
    print(f"\n{title}")
    print("-" * 60)
    if items is not []:
        for item in items:
            print(item)
    else:
        print("Aucun")

def display_item(item, title: str) -> None:
    print(f"\n======== {title} ========")

    if item is not None:
        print(item)
    else:
        print("ID inexistant")

    print("=" * (len(title) + 18))

def main() -> None:
    """Programme principal."""
    print("""\
--------------------------
Bienvenue dans notre école
--------------------------""")

    school: School = School()

    # initialisation d'un ensemble de cours, enseignants et élèves composant l'école
    # school.init_static()
    # affichage de la liste des cours, leur enseignant et leurs élèves
    # school.display_courses_list()

    # suppressions ------------------------------------------------------------------------
    #school.delete_course(school.get_all_courses()[0])
    #school.delete_teacher(school.get_all_teachers()[0])

    # affichage d'un cours ----------------------------------------------------------------
    display_item(school.get_course_by_id(1), "Affichage d'un cours")

    # affichage de la liste complète des cours --------------------------------------------
    display_list(school.get_all_courses(), "Affichage de la liste complète des cours")

    # affichage d'un étudiant -------------------------------------------------------------
    display_item(school.get_student_by_id(4), "Affichage d'un étudiant")

    # affichage de la liste complète des étudiants ----------------------------------------
    display_list(school.get_all_students(), "Affichage de la liste complète des étudiants")

    # affichage d'une adresse -------------------------------------------------------------
    display_item(school.get_address_by_id(2), "Affichage d'une adresse")

    # affichage de la liste complète des étudiants ----------------------------------------
    display_list(school.get_all_address(), "Affichage de la liste complète des adresses")

    # affichage d'un prof
    teacher = school.get_teacher_by_id(6)
    display_teacher(school, teacher)

    # affichage de la liste complète des profs ---------------------------------------------
    display_list(school.get_all_teachers(), "Affichage de la liste complète des profs")


if __name__ == '__main__':
    main()
