#!/usr/bin/env python3
from sqlmodel import CheckConstraint, Field, SQLModel, UniqueConstraint


class Host(SQLModel, table=True):
    id: str = Field(primary_key=True)
    platform: str = Field(
        sa_column_args=[CheckConstraint("platform IN ('win32', 'linux')")]
    )


class Path(SQLModel, table=True):
    id: int = Field(primary_key=True)
    host_id: str = Field(foreign_key="host.id", ondelete="CASCADE")
    app_id: str
    dotfile_name: str
    path: str
    private: bool = False
    datetime: str

    __table_args__ = (UniqueConstraint('host_id', 'path', name='uq_host_id_path'),)


# For testing
# This won't break the exist database
if __name__ == '__main__':
    from sqlmodel import create_engine

    engine = create_engine("sqlite:///:memory:", echo=True)
    SQLModel.metadata.create_all(engine)
