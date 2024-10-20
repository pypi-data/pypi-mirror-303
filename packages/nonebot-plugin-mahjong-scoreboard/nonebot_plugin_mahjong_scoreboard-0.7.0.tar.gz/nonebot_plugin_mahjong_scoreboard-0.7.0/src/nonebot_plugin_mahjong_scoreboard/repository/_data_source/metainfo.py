from sqlalchemy import JSON, inspect, select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Mapped, mapped_column

from .data_source import data_source

APP_DB_VERSION = 4


@data_source.registry.mapped
class MetaInfoOrm:
    __tablename__ = 'metainfo'

    key: Mapped[str] = mapped_column(primary_key=True)
    value: Mapped[any] = mapped_column(JSON)


async def get_metainfo(key: str) -> any:
    async with AsyncSession(data_source.engine) as session:
        record = await session.get(MetaInfoOrm, key)
        return record.value


async def set_metainfo(key: str, value: any):
    async with AsyncSession(data_source.engine) as session:
        record = await session.get(MetaInfoOrm, key)
        if record is None:
            record = MetaInfoOrm(key=key, value=value)
            session.add(record)

        record.value = value
        await session.commit()


@data_source.on_engine_created
async def initialize_metainfo():
    async with data_source.engine.begin() as conn:
        await conn.run_sync(lambda conn: MetaInfoOrm.__table__.create(conn, checkfirst=True))

    async with data_source.engine.begin() as conn:
        async with AsyncSession(data_source.engine, expire_on_commit=False) as session:
            # 判断是否初次建库
            blank_database = not await conn.run_sync(lambda conn: inspect(conn).has_table("games"))
            if blank_database:
                insert_db_version = APP_DB_VERSION
            else:
                insert_db_version = 1

            stmt = select(MetaInfoOrm).where(MetaInfoOrm.key == "db_version")
            result = (await session.execute(stmt)).scalar_one_or_none()
            if result is None:
                result = MetaInfoOrm(key="db_version", value=insert_db_version)
                session.add(result)
                await session.commit()

        await conn.commit()
