import json
from datetime import datetime

from sqlalchemy import Engine
from sqlmodel import Field, Session, SQLModel

from mtmai.mtlibs import mtutils


class MtmKvBase(SQLModel, table=True):
    """用postgresql 数据库表作为  kv 存储"""

    id: str = Field(default_factory=mtutils.gen_orm_id_key, primary_key=True)
    key: str = Field(unique=True, index=True, max_length=255)
    value: str = Field(default=None)
    value_type: str = Field(
        max_length=50
    )  # 存储值的类型，如 'str', 'int', 'float', 'json' 等
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(
        default_factory=datetime.utcnow, sa_column_kwargs={"onupdate": datetime.utcnow}
    )

    class Config:
        table_name = "mtm_kv_store"


class MtmKvStore:
    """KV 数据操作"""

    def __init__(self, db_engine: Engine):
        self.session = Session(db_engine)
        # self.engine = db_engine
        # self.session = db_session

    async def get(self, key: str):
        item = await self.session.query(MtmKvBase).filter(MtmKvBase.key == key).first()
        if item:
            return self._parse_value(item.value, item.value_type)
        return None

    async def set(self, key: str, value: any):
        value_type = type(value).__name__
        serialized_value = self._serialize_value(value)
        item = await self.session.query(MtmKvBase).filter(MtmKvBase.key == key).first()
        if item:
            item.value = serialized_value
            item.value_type = value_type
            item.updated_at = datetime.utcnow()
        else:
            new_item = MtmKvBase(key=key, value=serialized_value, value_type=value_type)
            self.session.add(new_item)
        await self.session.commit()

    async def delete(self, key: str):
        await self.session.query(MtmKvBase).filter(MtmKvBase.key == key).delete()
        await self.session.commit()

    async def exists(self, key: str) -> bool:
        result = (
            await self.session.query(MtmKvBase).filter(MtmKvBase.key == key).first()
        )
        return result is not None

    def _serialize_value(self, value: any) -> str:
        if isinstance(value, (str, int, float, bool)):
            return str(value)
        return json.dumps(value)

    def _parse_value(self, value: str, value_type: str):
        if value_type == "str":
            return value
        elif value_type == "int":
            return int(value)
        elif value_type == "float":
            return float(value)
        elif value_type == "bool":
            return value.lower() == "true"
        elif value_type == "json":
            return json.loads(value)
        return value
