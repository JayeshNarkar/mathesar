from sqlalchemy import DECIMAL as sa_decimal
from db.types import email, money, uri
from db.types.base import PostgresType


CUSTOM_TYPE_DICT = {
    # For some reason, SQLAlchemy doesn't add DECIMAL to the default
    # ischema_names supported by a PostgreSQL engine
    PostgresType.DECIMAL.value: sa_decimal,
    email.DB_TYPE: email.Email,
    money.DB_TYPE: money.Money,
    uri.DB_TYPE: uri.URI
}
