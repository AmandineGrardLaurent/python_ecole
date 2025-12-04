# -*- coding: utf-8 -*-

"""
Classe Dao[Student]
"""
import pymysql

from daos.dao import Dao
from dataclasses import dataclass
from typing import Optional

from models.address import Address
from models.student import Student


@dataclass
class StudentDao(Dao[Student]):

    def create(self, student: Student) -> int:

        return 0

    def read(self, id_student: int) -> Optional[Student]:
        """
            Renvoit l'étudiant correspondant dont l'id_person est id_student
        """
        student: Optional[Student]

        with Dao.connection.cursor(pymysql.cursors.DictCursor) as cursor:
            sql = """
                SELECT p.first_name, p.last_name, p.age, s.student_nbr, a.street, a.postal_code, a.city
                FROM student AS s
                JOIN person AS p
                ON s.id_person=p.id_person
                JOIN address AS a
                ON a.id_address = p.id_address
                WHERE p.id_person = %s;
            """
            cursor.execute(sql, (id_student,))
            record = cursor.fetchone()
        if record is not None:
            student = Student(record['first_name'],
                              record['last_name'],
                              record['age'])
            student.student_nbr = record['student_nbr']
            student.address = Address(record['street'],
                                      record['postal_code'],
                                      record['city'])
        else:
            student = None

        return student

    def read_all(self) -> list[Student]:
        """
            Renvoit tous les étudiants sous forme de liste
            (ou un tableau vide s'il n'a pas d'étudiant)
        """
        students: list[Student] = []

        with Dao.connection.cursor(pymysql.cursors.DictCursor) as cursor:
            sql = """
                SELECT p.first_name, p.last_name, p.age, s.student_nbr, a.street, a.postal_code, a.city
                FROM student AS s
                JOIN person AS p
                ON s.id_person=p.id_person
                JOIN address AS a
                ON a.id_address = p.id_address
            """
            cursor.execute(sql)
            records = cursor.fetchall()

        if not records:
            return []
        else:
            for record in records:
                student = Student(record['first_name'],
                                  record['last_name'],
                                  record['age'])
                student.student_nbr = record['student_nbr']
                student.address = Address(record['street'],
                                          record['postal_code'],
                                          record['city'])

                students.append(student)
            return students

    def update(self, student: Student) -> bool:
        ...
        return True

    def delete(self, student: Student) -> bool:
        ...
        return True
