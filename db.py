# db.py

from neo4j import GraphDatabase
from flask import current_app

#neo4j db
class Database:
    def __init__(self):
        self._uri = current_app.config['NEO4J_URI']
        self._user = current_app.config['NEO4J_USER']
        self._password = current_app.config['NEO4J_PASSWORD']
        self._driver = None

    def connect(self):
        self._driver = GraphDatabase.driver(self._uri, auth=(self._user, self._password))

    def close(self):
        if self._driver is not None:
            self._driver.close()
