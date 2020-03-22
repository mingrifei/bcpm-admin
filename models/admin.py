#!/usr/bin/env python
# -*-coding:utf-8-*-
"""
author : shenshuo
date   : 2018年10月23日
desc   : 管理后台数据库
"""


from sqlalchemy import Column, String, Integer, DateTime, Text,JSON,Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import class_mapper
import sqlalchemy
from datetime import date,datetime
Base = declarative_base()


def o_model_to_dict(model):
    model_dict = {}
    for key, column in class_mapper(model.__class__).c.items():
        model_dict[column.name] = getattr(model, key, None)
    return model_dict


def _model_to_dict(self):
    _dict = {}
    if self!=None:
        #table = class_mapper(self.__class__).mapped_table
        #for col in table.c:
        for col in self._fields:
            val = getattr(self, col,None)
            if type(val)==datetime:
                val = val.isoformat()

            _dict[col] = val
    return _dict
def model_to_dict(model):
    model_dict = {}
    for key, column in class_mapper(model.__class__).c.items():
        val=getattr(model, key, None)
        if type(val)==datetime:
            val=val.isoformat()
        model_dict[column.name] = val
    return model_dict

class OperationRecord(Base):
    __tablename__ = 'operation_record'

    ### 操作记录
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    username = Column('username', String(50))
    nickname = Column('nickname', String(50))
    login_ip = Column('login_ip', String(20))
    method = Column('method', String(10))
    uri = Column('uri', String(150))
    data = Column('data', Text())
    ctime = Column('ctime', DateTime(), default=datetime.now, onupdate=datetime.now)



class Users(Base):
    __tablename__ = 'mg_users'

    ### 用户表
    user_id = Column('user_id', Integer, primary_key=True, autoincrement=True)
    username = Column('username', String(50), unique=True)
    password = Column('password', String(100))
    nickname = Column('nickname', String(100))
    email = Column('email', String(80), unique=True)  ### 邮箱
    tel = Column('tel', String(11))  ### 手机号
    wechat = Column('wechat', String(50))  ### 微信号
    no = Column('no', String(50))  ### 工号
    department = Column('department', String(50))  ### 部门
    google_key = Column('google_key', String(80))  ### 谷歌认证秘钥
    superuser = Column('superuser', String(5), default='10')  ### 超级用户  0代表超级用户
    status = Column('status', String(5), default='0')
    last_ip = Column('last_ip', String(20), default='')
    last_login = Column('last_login', DateTime(), default=datetime.now, onupdate=datetime.now)
    ctime = Column('ctime', DateTime(), default=datetime.now)


class Roles(Base):
    __tablename__ = 'mg_roles'

    ### 角色表
    role_id = Column('role_id', Integer, primary_key=True, autoincrement=True)
    role_name = Column('role_name', String(30))
    status = Column('status', String(5), default='0')
    ctime = Column('ctime', DateTime(), default=datetime.now, onupdate=datetime.now)


class UserRoles(Base):
    __tablename__ = 'mg_user_roles'

    ### 用户角色关联表
    user_role_id = Column('user_role_id', Integer, primary_key=True, autoincrement=True)
    role_id = Column('role_id', String(11))
    user_id = Column('user_id', String(11))
    status = Column('status', String(5), default='0')
    utime = Column('utime', DateTime(), default=datetime.now, onupdate=datetime.now)
    ctime = Column('ctime', DateTime(), default=datetime.now)


class Components(Base):
    __tablename__ = 'mg_components'

    ### 组件表
    comp_id = Column('comp_id', Integer, primary_key=True, autoincrement=True)
    component_name = Column('component_name', String(60))
    status = Column('status', String(5), default='0')


class RolesComponents(Base):
    __tablename__ = 'mg_roles_components'

    ### 角色与前端组件关联表
    role_comp_id = Column('role_comp_id', Integer, primary_key=True, autoincrement=True)
    role_id = Column('role_id', String(11))
    comp_id = Column('comp_id', String(11))
    status = Column('status', String(5), default='0')


class Menus(Base):
    __tablename__ = 'mg_menus'

    ### 前端路由权限
    menu_id = Column('menu_id', Integer, primary_key=True, autoincrement=True)
    menu_name = Column('menu_name', String(60))
    status = Column('status', String(5), default='0')

class RoleMenus(Base):
    __tablename__ = 'mg_role_menus'

    ### 角色与前端路由关联
    role_menu_id = Column('role_menu_id', Integer, primary_key=True, autoincrement=True)
    role_id = Column('role_id', String(11))
    menu_id = Column('menu_id', String(11))
    status = Column('status', String(5), default='0')

class Functions(Base):
    __tablename__ = 'mg_functions'

    ### 权限表
    func_id = Column('func_id', Integer, primary_key=True, autoincrement=True)
    func_name = Column('func_name', String(60))
    uri = Column('uri', String(300))
    method_type = Column('method_type', String(10))
    status = Column('status', String(5), default='0')
    utime = Column('utime', DateTime(), default=datetime.now, onupdate=datetime.now)
    ctime = Column('ctime', DateTime(), default=datetime.now)


class RoleFunctions(Base):
    __tablename__ = 'mg_role_functions'

    ### 角色权限关联表
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    role_id = Column('role_id', String(11))
    func_id = Column('func_id', String(11))
    status = Column('status', String(5), default='0')
class projectmanger(Base):
    __tablename__ = 'mg_project_application'

    ### 项目申请表
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    applysno = Column('applysno', String(64))
    projectsno = Column('projectsno', String(64))#项目号
    contract_sno = Column('contractsno', String(2000))#合同号
    applytype = Column('applytype', String(32))#申请类型 立项申请
    applytitle = Column('applytitle', String(4000))#申请事项
    customername = Column('customername', String(255))#客户名称
    customerid = Column('customerid', String(255))#客户代码
    contractcurrency = Column('contractcurrency', String(255))#币种
    projecttype = Column('projecttype', String(32))#项目类型 研发、研发工程、战略项目、维护、外包
    projectname = Column('projectname', String(4000))#项目名称
    projectmanager = Column('projectmanager', String(255))#项目经理
    projectmanagerid = Column('projectmanagerid', String(255))#项目经理id
    plancost= Column('plancost', Float,default=0)#项目成本
    plannedstart = Column('plannedstart', DateTime(), default=datetime.now, onupdate=datetime.now)#项目预计开始时间
    plannedend = Column('plannedend', DateTime(), default=datetime.now, onupdate=datetime.now)#项目结束时间
    applysubmiter = Column('applysubmiter', String(200))#项目提交者
    contractbudget = Column('contractbudget', Float)#合同预算额
    projectprogress = Column('projectprogress', Float,default=0)#合同预算额
    applydata = Column('applydata',JSON)
    applyreviewdate = Column('applyreviewdate', DateTime(), default=datetime.now, onupdate=datetime.now)#项目预计评审时间
    reviewdoc = Column('reviewdoc', Text)#项目预计评审时间
    reviewcount = Column('reviewcount', String(2))#项目预计评审时间
    applytime = Column('applytime', DateTime(), default=datetime.now, onupdate=datetime.now)
    status = Column('status', String(5), default='0')
class projectreview(Base):
    __tablename__ = 'mg_project_review'

    ### 项目申请表
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    applysno = Column('applysno', String(64))
    applytitle = Column('applytitle', String(255))
    reviewrecordtime = Column('reviewrecordtime', String(255))
    reviewprojectname = Column('reviewprojectname', String(255))
    reviewpanel = Column('reviewpanel', String(2000))
    reviewstatus = Column('reviewstatus', String(255))
    reviewprojectno = Column('reviewprojectno', String(255))
    reviewprojectmanage = Column('reviewprojectmanage', String(255))
    reviewmanday = Column('reviewmanday', String(255))
    reviewprojectstart = Column('reviewprojectstart', DateTime(), default=datetime.now, onupdate=datetime.now)
    reviewprojectend = Column('reviewprojectend', DateTime(), default=datetime.now, onupdate=datetime.now)
    reviewprojectcost = Column('reviewprojectcost',Float, default=0)
    reviewprojectrecord = Column('reviewprojectrecord', Text)
    reviewrecorddate = Column('reviewrecorddate', DateTime(), default=datetime.now, onupdate=datetime.now)
    submiter = Column('applysubmiter', String(50))
    applydata = Column('applydata',JSON)
    status = Column('status', String(5), default='0')
