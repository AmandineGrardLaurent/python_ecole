# -*- coding: utf-8 -*-

"""
Classe Dao[Teacher]
"""
import pymysql

from daos.dao import Dao
from dataclasses import dataclass
from typing import Optional

from models.teacher import Teacher


@dataclass
class TeacherDao(Dao[Teacher]):

    def create(self, teacher: Teacher) -> int:

        return 0

    def read(self, id_teacher: int) -> Optional[Teacher]:
        """
            Renvoit l'étudiant correspondant dont l'id_person est id_student
        """
        teacher: Optional[Teacher]

        with Dao.connection.cursor(pymysql.cursors.DictCursor) as cursor:
            sql = """
                SELECT p.first_name, p.last_name, p.age, t.hiring_date
                FROM teacher AS t
                JOIN person AS p
                ON t.id_person=p.id_person
                WHERE t.id_teacher = %s;
            """
            cursor.execute(sql, (id_teacher,))
            record = cursor.fetchone()
        if record is not None:
            teacher = Teacher(record['first_name'],
                              record['last_name'],
                              record['age'],
                              record['hiring_date'])
        else:
            teacher = None

        return teacher

    def read_all(self) -> list[Teacher]:
        """
            Renvoit tous les profs sous forme de liste
            (ou un tableau vide s'il n'y a pas de profs)
        """
        teachers: list[Teacher] = []

        with Dao.connection.cursor(pymysql.cursors.DictCursor) as cursor:
            sql = """
                SELECT p.first_name, p.last_name, p.age, t.hiring_date
                FROM teacher AS t
                JOIN person AS p
                ON t.id_person=p.id_person
            """
            cursor.execute(sql)
            records = cursor.fetchall()

        if not records:
            return []
        else:
            for record in records:
                teacher = Teacher(record['first_name'],
                                  record['last_name'],
                                  record['age'],
                                  record['hiring_date'])


                teachers.append(teacher)
            return teachers

    def update(self, teacher: Teacher) -> bool:
        ...
        return True

    def delete(self, teacher: Teacher) -> bool:
        ...
        return True
