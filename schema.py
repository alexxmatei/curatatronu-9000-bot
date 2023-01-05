# TODO - Description & Validation for all classes in file
from typing import List

class Tasks:
    def __init__(self, id: int, createdAt: str = None, task: str = None, description: str = None, occurrence: str = None):
        self.id = id
        self.createdAt = createdAt
        self.task = task
        self.description = description
        self.occurrence = occurrence


class Greetings:
    def __init__(self, id: int, createdAt: str = None, greeting: str = None, type: str = None):
        self.id = id
        self.createdAt = createdAt
        self.greeting = greeting
        self.type = type


class Weeks:
    def __init__(self, id: int, createdAt: str = None, responsible: str = None, weekNr: int = None, tasksDone: List[int] = None):
        self.id = id
        self.createdAt = createdAt
        self.responsible = responsible
        self.weekNr = weekNr
        self.tasksDone = tasksDone or []


class Responsabili_curatenie:
    def __init__(self, id: int, createdAt: str = None, nume: str = None, telegramId: str = None, order_nr: int = None):
        self.id = id
        self.createdAt = createdAt
        self.nume = nume
        self.telegramId = telegramId
        self.order_nr = order_nr
