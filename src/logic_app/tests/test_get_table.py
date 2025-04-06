# from __future__ import annotations
# import sys
# from pathlib import Path
# from sqlalchemy import create_engine
# from sqlalchemy import MetaData
# from sqlalchemy import Table
# sys.path.append(str(Path(__file__).parent.parent))  # type: ignore
# from common.utils import get_settings  # type: ignore # noqa
# settings = get_settings()  # type: ignore
# engine = create_engine(
#     f'postgresql+psycopg://{settings.postgres.username}:{settings.postgres.password}@{settings.postgres.host}/{settings.postgres.db}',
# )
# def get_table(engine):
#     """get table
#     Args:
#         engine (Engine): A instance of the database engine
#     """
#     connection = engine.connect()
#     metadata = MetaData()
#     metadata.reflect(bind=engine)
#     # Print value in each column
#     for table_name in metadata.tables:
#         table = Table(table_name, metadata, autoload_with=engine)
#         print(f'Contents of table {table_name}:')
#         result = connection.execute(table.select()).fetchall()
#         for row in result:
#             print(row)
#         print('\n')
# get_table(engine)
from __future__ import annotations
