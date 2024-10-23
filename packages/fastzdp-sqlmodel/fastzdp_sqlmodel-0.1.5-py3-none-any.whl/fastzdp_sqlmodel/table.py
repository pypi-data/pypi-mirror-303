from sqlalchemy import Engine

from sqlmodel import SQLModel


def init_table(engine: Engine):
    """初始化表格"""
    SQLModel.metadata.drop_all(engine)  # 删除所有表
    SQLModel.metadata.create_all(engine)  # 创建所有表


def create_table(engine: Engine):
    """创建表格"""
    SQLModel.metadata.create_all(engine)  # 创建所有表


def clear_table(engine: Engine):
    """清除表格"""
    SQLModel.metadata.drop_all(engine)
