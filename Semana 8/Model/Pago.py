#!/usr/bin/python
#-*- coding: utf-8 -*-
from enum import Enum

class MeodoPago(Enum):
    EFECTIVO = 1
    TARJETA_CREDITO = 2
    TARJETA_DEBITO = 3
    CHEQUE = 4
    OTRO = 5
    def __init__(self ):
        self.tipo = None

