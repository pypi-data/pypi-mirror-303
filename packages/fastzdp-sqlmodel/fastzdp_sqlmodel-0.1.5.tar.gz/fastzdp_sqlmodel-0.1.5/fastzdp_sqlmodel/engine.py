from sqlalchemy import create_engine, Engine
from urllib.parse import quote_plus as urlquote


def get_engine(
        username: str = "root",
        password: str = "root",
        ip: str = "127.0.0.1",
        port: int = 3306,
        database: str = "test",
        echo: bool = False,
) -> Engine:
    """获取引擎对象"""
    sqlite_url = f"mysql+pymysql://{username}:{urlquote(password)}@{ip}:{port}/{database}?charset=utf8mb4"
    return create_engine(sqlite_url, echo=echo)
