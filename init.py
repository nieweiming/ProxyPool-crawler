# -*- coding: utf-8 -*-
# @Desc: 数据库的初始化

from models.models import Base, engine


def create_tables():
    """数据库初始化"""

    Base.metadata.create_all(engine)


if __name__ == '__main__':
    create_tables()
