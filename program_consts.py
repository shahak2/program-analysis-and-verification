from enum import StrEnum

class ABSTRACT_DOMAINS(StrEnum):
    parity = "parity"
    summation = "summation"
    combined = "combined"


PROGRAM_DESCRIPTION = "paav.py - A Python script for performing static analysis."

PATH_HELP = "The path to the program code."

DOMAIN_HELP = "Specify the domain (parity, summation, or combined)."

RUN_TESTS_HELP = "Run tests - No need for path or domain."
