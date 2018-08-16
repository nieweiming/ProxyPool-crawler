# -*- coding: utf-8 -*-
"""
数据库模型定义
"""
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from conf import setting

#declarative_base() 创建了一个 BaseModel类，这个类的子类可以自动与一个表关联
Base = declarative_base()
engine = create_engine(setting.DATABASE_URI)

#通过sessionmaker方法创建了一个Session工厂函数
DBSession = sessionmaker(bind=engine)


class ProxyPool(Base):
    """
    定义proxypool表Model
    """
    __tablename__ = 'proxypool'
    id = sqlalchemy.Column(sqlalchemy.INT, nullable=False, primary_key=True, autoincrement=True)
    ip = sqlalchemy.Column(sqlalchemy.VARCHAR(20), unique=True, nullable=False)
    ip_port = sqlalchemy.Column(sqlalchemy.VARCHAR(6), nullable=False)
    utime = sqlalchemy.Column(sqlalchemy.Integer, default=0)
    ctime = sqlalchemy.Column(sqlalchemy.Integer, default=0)

    def __init__(self, values):
        self.set_attributes(values)

    def set_attributes(self, values):
        """
        设置各属性的值
        :param values:
        :return:
        """
        for key in values:
            if hasattr(self, key):
                setattr(self, key, values[key])

    def __repr__(self):
        """
        :return:
        """
        return '<IP %r>' % (self.ip)

    def to_dict(self):
        """
        :return:  转为字典存放
        """
        return dict([(col.name, getattr(self, col.name)) for col in self.__table__.columns])
