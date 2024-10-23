from os import environ
from typing import TYPE_CHECKING
from sqlite3 import Cursor, connect

if TYPE_CHECKING:
    from pidentity import Contract


from pidentity.database import initialize_sql
from pidentity.guard import Guard


class Control(object):
    def __init__(self, engine: str, connection = None):
        self._contracts = []  # ['post:@:/v1/customers/:id', 'get:@:/v1/customers/id']
        self._pool = connection

    @staticmethod
    def _evaluate(conditions: dict):
        # check if dict key starts with ? or &
        # TODO: remove if unused which appears to be the case
        for key in conditions:
            char = key[0]
            {'?': 'OR', '&': 'AND'}.get(char)

    def add(self, *contracts: 'Contract') -> 'Control':
        for contract in contracts:
            if not contract._on:
                raise ValueError('Every contract must have a valid action and destination before being added to a control')
            for action in contract._on:
                payload = contract._payload
                payload['on'] = action
                self._contracts.append(payload)
        return self

    def guard(self, action: str) -> 'Guard':
        """
        If someone tries to evaluate with a can and to and a
        valid contract does not exist then raise an error
        """
        return Guard(self)

    async def init(self):
        async with self._pool.acquire() as conn:
            await initialize_sql(conn)

    def save(self) -> 'Control':...

    async def resync(self) -> 'Control':
        """fetch contracts from database async and save to _contracts"""
        pass

    def resync(self) -> 'Control':
        """fetch contracts from database and save to _contracts"""
        pass
