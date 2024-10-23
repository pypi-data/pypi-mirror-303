from sqlalchemy import (
    MetaData,
    ForeignKey,
    Table,
    Column,
    Integer,
    String,
    insert,
)
from sa_dump_engine import create_dump_engine


# table examples from https://docs.sqlalchemy.org/en/20/core/metadata.html#creating-and-dropping-database-tables
metadata_obj = MetaData()

user = Table(
    "user",
    metadata_obj,
    Column("user_id", Integer, primary_key=True),
    Column("user_name", String(16), nullable=False),
    Column("email_address", String(60), key="email"),
    Column("nickname", String(50), nullable=False),
)

user_prefs = Table(
    "user_prefs",
    metadata_obj,
    Column("pref_id", Integer, primary_key=True),
    Column("user_id", Integer, ForeignKey("user.user_id"), nullable=False),
    Column("pref_name", String(40), nullable=False),
    Column("pref_value", String(100)),
)


def main(dialect_name: str, **kwargs):
    # create a mock engine to dump SQL statements with dialect_name like 'sqlite', 'mysql', 'postgresql'
    engine = create_dump_engine(dialect_name, literal_binds=False)

    # do some with dump-engine, then you can get SQL statement
    # to get CREATE TABLE statement
    metadata_obj.create_all(engine)

    # to get INSERT Statement
    conn = engine.connect()
    conn.execute(
        insert(user).
        values(user_name="user1", email="user1@example.com", nickname="user1")
    )


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--dialect-name',
        default='sqlite',
        help='dialect name. e.g. sqlite, mysql, postgresql'
    )

    args = parser.parse_args()
    main(**vars(args))
