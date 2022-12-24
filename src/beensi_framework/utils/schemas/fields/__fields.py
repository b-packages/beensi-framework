from . import (
    BaseField,
    NumericField,
    IntegerField,
    PositiveIntegerField,
    NegativeIntegerField,
    FloatField,
    PositiveFloatField,
    NegativeFloatField,
    StringField,
)
from beensi_framework.utils.macros import (
    NUMERIC,
    BASE,
    INTEGER,
    POSITIVE_INTEGER,
    NEGATIVE_INTEGER,
    FLOAT,
    POSITIVE_FLOAT,
    NEGATIVE_FLOAT,
    STRING,
    EMAIL,
    PASSWORD,
    GENDER,
    URL,
    LIST,
    DICTIONARY,
    TUPLE,
    SET,
    BOOLEAN,
    USERNAME,
)

Fields = {
    BASE: BaseField,
    NUMERIC: NumericField,
    INTEGER: IntegerField,
    POSITIVE_INTEGER: PositiveIntegerField,
    NEGATIVE_INTEGER: NegativeIntegerField,
    FLOAT: FloatField,
    POSITIVE_FLOAT: PositiveFloatField,
    NEGATIVE_FLOAT: NegativeFloatField,
    STRING: StringField,

    EMAIL: BaseField,
    PASSWORD: BaseField,
    GENDER: BaseField,
    URL: BaseField,
    LIST: BaseField,
    DICTIONARY: BaseField,
    TUPLE: BaseField,
    SET: BaseField,
    BOOLEAN: BaseField,
    USERNAME: BaseField,
}
