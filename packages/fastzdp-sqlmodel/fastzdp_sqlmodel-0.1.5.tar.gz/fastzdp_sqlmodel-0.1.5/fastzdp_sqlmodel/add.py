from sqlmodel import Session


def add(engine, model_obj):
    """
    新增
    :param engine: 引擎对象
    :param model_obj: 模型实例对象
    """
    with Session(engine) as session:
        session.add(model_obj)
        session.commit()
