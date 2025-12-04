#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Application de gestion d'une école
"""

from business.school import School


def main() -> None:
    """Programme principal."""
    print("""\
--------------------------
Bienvenue dans notre école
--------------------------""")

    school: School = School()

    # initialisation d'un ensemble de cours, enseignants et élèves composant l'école
    school.init_static()

    # affichage de la liste des cours, leur enseignant et leurs élèves
    # school.display_courses_list()

    # affichage d'un cours
    print(school.get_course_by_id(1))
    print(school.get_course_by_id(2))
    print(school.get_course_by_id(5))
    print(school.get_course_by_id(9))

    # affichage de la liste complète des cours
    courses = school.get_all_courses()
    for course in courses:
        print(course)

    #school.delete_course(courses[8])

    # affichage d'un étudiant
    print("-"*20)
    print(school.get_student_by_id(1))

    # affichage de la liste complète des étudiants
    students = school.get_all_students()
    for student in students:
        print(student)

    # affichage d'une adresse
    print("-"*20)
    print(school.get_address_by_id(1))

    # affichage de la liste complète des étudiants
    all_address = school.get_all_address()
    for address in all_address:
        print(address)


if __name__ == '__main__':
    main()
