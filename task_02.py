#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Contains expectations."""


import inquisition

START_LOC = inquisition.SPANISH.index('Spanish')
PRE_STRING = inquisition.SPANISH[0:START_LOC]
STR_LEN = len(inquisition.SPANISH)
POST_STRING = inquisition.SPANISH[START_LOC + len('Spanish'):STR_LEN]
FLEMISH = PRE_STRING + 'Flemish' + POST_STRING

print FLEMISH
