# -*- coding: utf-8 -*-

"""
Classe Dao[Student]
"""

from daos.dao import Dao
from dataclasses import dataclass
from typing import Optional

from models.student import Student


@dataclass
class StudentDao(Dao[Student]):

    def update(self, student: Student) -> bool:
        """Met à jour en BD l'entité Course correspondant à course, pour y correspondre

        :param course: cours déjà mis à jour en mémoire
        :return: True si la mise à jour a pu être réalisée
        """
        ...
        return True

    def delete(self, student: Student) -> bool:
        """Supprime en BD l'entité Course correspondant à course

        :param course: cours dont l'entité Course correspondante est à supprimer
        :return: True si la suppression a pu être réalisée
        """
        ...
        return True
