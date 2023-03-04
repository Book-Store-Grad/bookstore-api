from enum import Enum


class DataType(Enum):
    CHARACTER_VARYING = "character varying"
    INTEGER = "integer"
    TIMESTAMP = "timestamp"
    BOOLEAN = "boolean"
    SERIAL = "serial"
    TIMESTAMPTZ = "timestamptz"
    BINARY = "bytea"

