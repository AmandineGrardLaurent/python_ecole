#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Application de gestion d'une école
"""

from business.school import School
from models.teacher import Teacher


def display_list(items: list, title: str) -> None:
    print(f"\n{title}")
    print("-" * 40)
    for item in items:
        print(item)

def display_item(item, title: str) -> None:
    print(f"\n=== {title} ===")
    print(item)
    print("=" * (len(title) + 8))

def main() -> None:
    """Programme principal."""
    print("""\
--------------------------
Bienvenue dans notre école
--------------------------""")

    school: School = School()

    # initialisation d'un ensemble de cours, enseignants et élèves composant l'école
    #school.init_static()

    # affichage de la liste des cours, leur enseignant et leurs élèves
    # school.display_courses_list()

    #school.delete_course(school.get_all_courses()[0])
    #school.delete_teacher(school.get_all_teachers()[0])

    # affichage d'un cours ----------------------------------------------------------------
    display_item(school.get_course_by_id(4), "Affichage d'un cours")

    # affichage de la liste complète des cours --------------------------------------------
    display_list(school.get_all_courses(), "Affichage de la liste complète des cours")

    # affichage d'un étudiant -------------------------------------------------------------
    display_item(school.get_student_by_id(2), "Affichage d'un étudiant")

    # affichage de la liste complète des étudiants ----------------------------------------
    display_list(school.get_all_students(), "Affichage de la liste complète des étudiants")

    # affichage d'une adresse -------------------------------------------------------------
    display_item(school.get_address_by_id(2), "Affichage d'une adresse")

    # affichage de la liste complète des étudiants
    display_list(school.get_all_address(), "Affichage de la liste complète des adresses")

    # affichage d'un prof
    display_item(school.get_teacher_by_id(5), "Affichage d'un prof")

    # affichage de la liste complète des profs
    display_list(school.get_all_teachers(), "Affichage de la liste complète des profs")


if __name__ == '__main__':
    main()
