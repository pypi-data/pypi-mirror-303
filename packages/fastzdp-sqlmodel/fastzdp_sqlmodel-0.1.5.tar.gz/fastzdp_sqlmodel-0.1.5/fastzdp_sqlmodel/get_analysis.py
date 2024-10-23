from sqlmodel import Session, select, func


def get_sum(
        engine,
        model,
        column,
        query_dict=None,
        in_dict=None,
):
    """
    获取求和结果
    :param engine 引擎对象
    :param model 模型对象
    :param column 要求和的列明
    :param query_dict 等值查询条件, 比如 {class_id:14}
    :param in_dict in查询条件, 比如 {id:[1,2,3]}
    """
    if not hasattr(model, column):
        return 0
    total = 0
    with Session(engine) as session:
        query = select(func.sum(getattr(model, column)))
        # 等值查询
        if isinstance(query_dict, dict):
            for k, v in query_dict.items():
                if hasattr(model, k):
                    query = query.where(getattr(model, k) == v)
        # in 查询
        if isinstance(in_dict, dict):
            for k, v in in_dict.items():
                if hasattr(model, k):
                    query = query.where(getattr(model, k).in_(v))
        # 执行SQL
        result = session.exec(query).one()
        total = float(result) if result else 0
    return total
