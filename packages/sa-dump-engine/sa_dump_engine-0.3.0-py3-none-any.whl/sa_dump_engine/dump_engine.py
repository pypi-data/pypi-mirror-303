import io
import sys

from sqlalchemy import (
    create_mock_engine,
    Engine,
    URL,
)


class Executor:

    def __init__(self, dialect_cls, output=sys.stdout, suffix=";", literal_binds=False):
        self.dialect_cls = dialect_cls
        self.output = output
        self.suffix = suffix
        self.literal_binds = literal_binds

    def dump(self, sql, *multiparams, **params):
        """dump SQL statement to output stream.
        """
        print(
            str(
                sql.compile(
                    dialect=self.dialect_cls(),
                    compile_kwargs={
                        "literal_binds": self.literal_binds,
                    },
                )
            ).strip(),
            file=self.output,
        )
        print(self.suffix, file=self.output)


def create_dump_engine(
        dialect_name: str,
        output: io.TextIOBase = sys.stdout,
        suffix: str = ";",
        literal_binds: bool = False) -> Engine:
    """create mock-engine, which dumps SQL statements to output.

    Args:
    - dialect_name: str: SQL dialect name. e.g. 'sqlite', 'mysql', 'postgresql'
    - output: io.TextIOBase: output stream to dump SQL statements
    - suffix: str: suffix to add to each SQL statement
    - literal_binds: bool: if True, bind parameters are rendered inline within the statement
    """
    url = URL.create(
        drivername=dialect_name,  # dialect name only. drivername is not required to output SQL statements
    )
    executor = Executor(
        dialect_cls=url.get_dialect(),
        output=output,
        suffix=suffix,
        literal_binds=literal_binds,
    )
    return create_mock_engine(url, executor=executor.dump)
