from .get import get_by_dict


def is_exists(engine, model, query_dict: dict) -> bool:
    """
    根据查询字典指定的键值对等值查询数据
    :param engine: 引擎对象
    :param model: 模型类
    :param query_dict: 查询字典
    """
    data = get_by_dict(engine, model, query_dict)
    return isinstance(data, list) and len(data) > 0
