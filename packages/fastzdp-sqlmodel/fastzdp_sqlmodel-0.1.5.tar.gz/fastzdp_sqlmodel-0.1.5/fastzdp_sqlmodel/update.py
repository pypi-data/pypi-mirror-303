from sqlmodel import Session
from .get import get


def update(engine, model_obj, update_dict):
    """
    修改数据
    :param engine: 连接数据库的引擎对象
    :param model_obj: 模型对象
    :param update_dict: 更新字典
    :return:
    """
    with Session(engine) as session:
        if not isinstance(update_dict, dict):
            return
        for k, v in update_dict.items():
            if hasattr(model_obj, k):
                setattr(model_obj, k, v)
        session.add(model_obj)
        session.commit()
        session.refresh(model_obj)
        return model_obj


def update_id(engine, model, id, update_dict):
    """
    修改数据
    :param engine: 连接数据库的引擎对象
    :param model: 模型类
    :param id: 要修改的ID
    :param update_dict: 更新字典
    :return:
    """
    # 查询
    model_obj = get(engine, model, id)
    if not model_obj:
        return

    # 修改
    return update(engine, model_obj, update_dict)
