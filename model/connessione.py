from dataclasses import dataclass
from model.object import Object

@dataclass
class Connessione:
    o1 : Object
    o2 : Object
    peso : int