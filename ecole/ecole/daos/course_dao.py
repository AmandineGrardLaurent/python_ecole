# -*- coding: utf-8 -*-

"""
Classe Dao[Course]
"""
import pymysql

from models.course import Course
from daos.dao import Dao
from dataclasses import dataclass
from typing import Optional

from models.teacher import Teacher


@dataclass
class CourseDao(Dao[Course]):
    def create(self, course: Course) -> int:
        """Crée en BD l'entité Course correspondant au cours course

        :param course: à créer sous forme d'entité Course en BD
        :return: l'id de l'entité insérée en BD (0 si la création a échoué).
        """
        ...
        return 0

    def read(self, id_course: int) -> Optional[Course]:
        """Renvoit le cours correspondant à l'entité dont l'id est id_course
           (ou None s'il n'a pu être trouvé)"""
        course: Optional[Course]

        with Dao.connection.cursor(pymysql.cursors.DictCursor) as cursor:
            sql = """
                SELECT c.name, c.start_date, c.end_date, c.id_course, 
                p.first_name, p.last_name, p.age, 
                t.hiring_date, t.id_teacher
                FROM course AS c
                LEFT JOIN teacher AS t
                ON c.id_teacher=t.id_teacher
                LEFT JOIN person AS p
                ON t.id_person=p.id_person
                WHERE id_course = %s
            """
            cursor.execute(sql, (id_course,))
            record = cursor.fetchone()
        if record is None:
            return None
        course = Course(record['name'],
                        record['start_date'],
                        record['end_date'])
        course.id = record['id_course']

        if record['id_teacher'] is not None:
            teacher = Teacher(record['first_name'],
                              record['last_name'],
                              record['age'],
                              record['hiring_date'])
            teacher.id = record['id_teacher']
            course.teacher = teacher
        else:
            course.teacher = None

        return course

    def read_all(self) -> list[Course]:
        """Renvoit l'ensemble des cours sous forme de liste
           (ou un tableau vide s'il n'a pas de cours)"""
        courses: list[Course] = []

        with Dao.connection.cursor(pymysql.cursors.DictCursor) as cursor:
            sql = """
                SELECT c.name, c.start_date, c.end_date, c.id_course, 
                p.first_name, p.last_name, p.age, 
                t.hiring_date, t.id_teacher
                FROM course AS c
                LEFT JOIN teacher AS t
                ON c.id_teacher=t.id_teacher
                LEFT JOIN person AS p
                ON t.id_person=p.id_person
            """
            cursor.execute(sql)
            records = cursor.fetchall()

        if not records:
            return []

        for record in records:
            course = Course(record['name'],
                            record['start_date'],
                            record['end_date'])
            course.id = record['id_course']

            if record['id_teacher'] is not None:
                teacher = Teacher(record['first_name'],
                                  record['last_name'],
                                  record['age'],
                                  record['hiring_date'])
                teacher.id = record['id_teacher']
                course.teacher = teacher
            else:
                course.teacher = None
            courses.append(course)
        return courses

    def update(self, course: Course) -> bool:
        """Met à jour en BD l'entité Course correspondant à course, pour y correspondre

        :param course: cours déjà mis à jour en mémoire
        :return: True si la mise à jour a pu être réalisée
        """
        ...
        return True

    def delete(self, course: Course) -> bool:
        """Supprime en BD l'entité Course correspondant à course

        :param course: cours dont l'entité Course correspondante est à supprimer
        :return: True si la suppression a pu être réalisée
        """

        with Dao.connection.cursor(pymysql.cursors.DictCursor) as cursor:
            sql = "DELETE FROM course WHERE id_course = %s"
            cursor.execute(sql, (course.id,))
            Dao.connection.commit()
            if cursor.rowcount > 0:
                return True
            else:
                return False
