from sqlmodel import Session
from .get import get


def delete(engine, model_obj):
    """
    根据模型删除数据
    :param engine: 连接数据库的引擎对象
    :param model_obj: 模型对象
    :return: None
    """
    with Session(engine) as session:
        session.delete(model_obj)
        session.commit()


def delete_id(engine, model, id):
    """
    根据模型删除数据
    :param engine: 连接数据库的引擎对象
    :param model: 模型类
    :param id: 要删除的ID
    :return: None
    """
    # 查询
    model_obj = get(engine, model, id)
    if not model_obj:
        return
    # 删除
    delete(engine, model_obj)
