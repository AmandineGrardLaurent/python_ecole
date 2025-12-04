# -*- coding: utf-8 -*-

"""
Classe Dao[Address]
"""
import pymysql

from daos.dao import Dao
from dataclasses import dataclass
from typing import Optional

from models.address import Address


@dataclass
class AddressDao(Dao[Address]):

    def create(self, address: Address) -> int:

        return 0

    def read(self, id_address: int) -> Optional[Address]:
        """
            Renvoit une adresse dont via l'id_address
        """
        address: Optional[Address]

        with Dao.connection.cursor(pymysql.cursors.DictCursor) as cursor:
            sql = """
                SELECT a.street, a.postal_code, a.city
                FROM address AS a
                WHERE a.id_address = %s;
            """
            cursor.execute(sql, (id_address,))
            record = cursor.fetchone()
        if record is not None:
            address = Address(record['street'],
                              record['postal_code'],
                              record['city'])
        else:
            address = None

        return address

    def read_all(self) -> list[Address]:
        """
            Renvoit toutes les adresses sous forme de liste
            (ou un tableau vide s'il n'a pas d'étudiant)
        """
        all_address: list[Address] = []

        with Dao.connection.cursor(pymysql.cursors.DictCursor) as cursor:
            sql = """
                SELECT a.street, a.postal_code, a.city
                FROM address AS a
            """
            cursor.execute(sql)
            records = cursor.fetchall()

        if not records:
            return []
        else:
            for record in records:
                address = Address(record['street'],
                                  record['postal_code'],
                                  record['city'])

                all_address.append(address)
            return all_address

    def update(self, address: Address) -> bool:
        ...
        return True

    def delete(self, address: Address) -> bool:
        ...
        return True
