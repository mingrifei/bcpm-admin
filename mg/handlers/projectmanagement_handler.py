#!/usr/bin/env python
# -*-coding:utf-8-*-
"""
author : shenshuo
date   : 2017年11月20日15:52:07
role   : 缓存权限
"""

import json,time
from tornado.web import RequestHandler
from libs.my_verify import MyVerify
from settings import settings as my_settings
from websdk.db_context import DBContext
from models.admin import projectmanger,model_to_dict,projectreview,Users,_model_to_dict
from websdk.utils import SendMail
from websdk.consts import const
from sqlalchemy import and_,or_


class addprojecthandler(RequestHandler):
    '''
    applytype: "立项申请"
    applysubmiter: "刘松"
    applytitle: "申请对长江证券投资者报送产品销售项目立项评审"
    projectname: "长江证券投保基金报送平台V2.0"
    customername: "长江证券股份有限公司"
    customerid: "GD098889989898"
    projecttype: "A-gc"
    contractcurrency: "rmb"
    contractbudget: 1000000
    plancost: 10000
    projectmanager: "张三"
    reviewcount: "1"
    reviewdoc: "<table width="869"> <tbody> <tr> <td colspan="4" width="624">工作量估算表</td> <td width="244">人员预估</td> </tr> <tr> <td rowspan="2">里程碑</td> <td colspan="2" rowspan="2">工作描述</td> <td>工作量估算（人/日）</td> <td>&nbsp;</td> </tr> <tr> <td>最小工作量</td> <td>&nbsp;</td> </tr> <tr> <td rowspan="5">项目管理</td> <td colspan="2">软件开发计划</td> <td>0</td> <td>&nbsp;</td> </tr> <tr> <td colspan="2">配置管理计划</td> <td>0</td> <td>&nbsp;</td> </tr> <tr> <td colspan="2">软件测试计划</td> <td>0</td> <td>&nbsp;</td> </tr> <tr> <td colspan="2">质量保证计划</td> <td>0</td> <td>&nbsp;</td> </tr> <tr> <td colspan="2">项目实施计划</td> <td>1.5</td> <td>&nbsp;</td> </tr> <tr> <td rowspan="4">需求分析</td> <td colspan="2">需求调查</td> <td>2</td> <td>&nbsp;</td> </tr> <tr> <td colspan="2">需求分析</td> <td>1</td> <td>&nbsp;</td> </tr> <tr> <td colspan="2">需求文档</td> <td>5</td> <td>&nbsp;</td> </tr> <tr> <td colspan="2">需求确认</td> <td>1</td> <td>&nbsp;</td> </tr> <tr> <td rowspan="5">系统设计</td> <td colspan="2">体系结构设计</td> <td>5</td> <td>&nbsp;</td> </tr> <tr> <td colspan="2">数据模型设计</td> <td>0</td> <td>&nbsp;</td> </tr> <tr> <td colspan="2">系统原型设计</td> <td>1</td> <td>&nbsp;</td> </tr> <tr> <td colspan="2">模块详细设计</td> <td>17.5</td> <td>&nbsp;</td> </tr> <tr> <td colspan="2">设计评审</td> <td>0</td> <td>&nbsp;</td> </tr> <tr> <td rowspan="5">项目开发</td> <td colspan="2" width="287">效果设计</td> <td>1</td> <td>&nbsp;</td> </tr> <tr> <td colspan="2" width="287">UI功能开发</td> <td>44</td> <td>2人*1月</td> </tr> <tr> <td colspan="2" width="287">服务层开发</td> <td>110</td> <td>前期开发5人*1月&nbsp;+开源改造数据库需求未确定，需求明确后再评估</td> </tr> <tr> <td colspan="2" width="287">系统整合</td> <td>0</td> <td>&nbsp;</td> </tr> <tr> <td colspan="2" width="287">代码评审</td> <td>0</td> <td>&nbsp;</td> </tr> <tr> <td rowspan="8">系统测试</td> <td colspan="2">准备测试用例</td> <td>15</td> <td>&nbsp;</td> </tr> <tr> <td colspan="2">测试用例评审</td> <td>5</td> <td>&nbsp;</td> </tr> <tr> <td colspan="2">系统集成测试</td> <td>30</td> <td>系统测试 3人*2周</td> </tr> <tr> <td colspan="2">测试结果修改</td> <td>0</td> <td>&nbsp;</td> </tr> <tr> <td colspan="2">测试方案</td> <td>0</td> <td>&nbsp;</td> </tr> <tr> <td colspan="2">性能测试</td> <td>1</td> <td>&nbsp;</td> </tr> <tr> <td colspan="2">安全测试</td> <td>0</td> <td>&nbsp;</td> </tr> <tr> <td colspan="2">测试报告</td> <td>0.5</td> <td>&nbsp;</td> </tr> <tr> <td rowspan="10">工程实施</td> <td colspan="2">系统部署</td> <td>10</td> <td>&nbsp;</td> </tr> <tr> <td colspan="2">取数口径确认</td> <td>30</td> <td>3人*2周</td> </tr> <tr> <td colspan="2">现场开发</td> <td>&nbsp;</td> <td>开源改造数据库需求未确定，需求明确后再评估</td> </tr> <tr> <td colspan="2">现场测试</td> <td>&nbsp;</td> <td>开源改造数据库需求未确定，需求明确后再评估</td> </tr> <tr> <td colspan="2">工程实施方案</td> <td>1</td> <td>&nbsp;</td> </tr> <tr> <td colspan="2">工程上线方案</td> <td>1</td> <td>&nbsp;</td> </tr> <tr> <td colspan="2">运维方案</td> <td>0.5</td> <td>&nbsp;</td> </tr> <tr> <td colspan="2">应急方案</td> <td>0.5</td> <td>&nbsp;</td> </tr> <tr> <td colspan="2">培训</td> <td>3</td> <td>&nbsp;</td> </tr> <tr> <td colspan="2">实施人员驻场</td> <td>264</td> <td>12月16日正常运维一年</td> </tr> <tr> <td>一年维护</td> <td colspan="2">&nbsp;</td> <td>&nbsp;</td> <td>1人月</td> </tr> <tr> <td colspan="3">工作量总计（人/日）</td> <td>550.5</td> <td>&nbsp;</td> </tr> <tr> <td colspan="3">工作量总计（人/月）</td> <td>25</td> <td>&nbsp;</td> </tr> <tr> <td colspan="3">人力成本单价(元)</td> <td>￥25,000.00&nbsp;</td> <td>&nbsp;</td> </tr> <tr> <td colspan="3">人力总成本(元)</td> <td>￥625,000.00&nbsp;</td> <td>&nbsp;</td> </tr> <tr> <td colspan="2" rowspan="4">其它投入估算（元）</td> <td>交通费用</td> <td>0</td> <td>&nbsp;</td> </tr> <tr> <td>会务费+商务费</td> <td>0</td> <td>&nbsp;</td> </tr> <tr> <td>差旅费用</td> <td>0</td> <td>&nbsp;</td> </tr> <tr> <td>其它费用</td> <td>0</td> <td>&nbsp;</td> </tr> <tr> <td colspan="3">成本预估（元）</td> <td>￥625,000.00&nbsp;</td> <td>&nbsp;</td> </tr> </tbody> </table>"
    plannedstart: "2020-02-03"
    plannedend: "2020-02-25"
    applyreviewdate: "2020-02-26"
    '''
    def post(self, *args, **kwargs):
        data = json.loads(self.request.body.decode("utf-8"))
        applytype = data.get('applytype', None)
        applysubmiter = data.get('applysubmiter', None)
        applytitle = data.get('applytitle', None)
        projectname = data.get('projectname', None)
        customername = data.get('customername', None)
        customerid = data.get('customerid', None)
        projecttype = data.get('projecttype', None)
        contractcurrency = data.get('contractcurrency', None)
        contractbudget = data.get('contractbudget', None)
        plancost = data.get('plancost', None)
        projectmanager = data.get('projectmanager', None)
        reviewcount = data.get('reviewcount', None)
        reviewdoc = data.get('reviewdoc', None)
        plannedstart = data.get('plannedstart', None)
        plannedend = data.get('plannedend', None)
        applyreviewdate = data.get('applyreviewdate', None)
        applydata=data
        applysno=time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))


        if applytype == None:
            return self.write(dict(code=-1, msg='信息有误，拒绝您的申请'))
        else:
            with DBContext('w', None, True) as session:
                session.add(projectmanger(applysno=applysno,applytype=applytype, applytitle=applytitle, applysubmiter=applysubmiter,applydata=applydata,projectname=projectname,customername=customername,customerid=customerid,
                                          projecttype=projecttype,contractcurrency=contractcurrency,contractbudget=contractbudget,plancost=plancost,projectmanager=projectmanager,reviewcount=reviewcount,
                                          reviewdoc=reviewdoc,plannedstart=plannedstart,plannedend=plannedend,applyreviewdate=applyreviewdate))

            return self.write(dict(code=0, msg='项目信息提交成功',data=''))


class importprojecthandler(RequestHandler):

    def post(self, *args, **kwargs):
        data = json.loads(self.request.body.decode("utf-8"))
        with DBContext('w', None, True) as session:
                result_apply=session.execute("INSERT INTO mg_project_application(applysno,projectsno,contractsno,applytype,applytitle,customername,contractcurrency,projecttype,projectname,projectmanager,plancost,contractbudget,projectprogress,status)VALUES(uuid(),:projectsno,:contract_sno,'立项申请',:applytitle,:customername,:contractcurrency,:projecttype,:projectname,:projectmanager,:plancost,:contractbudget,:projectprogress,:status)", data)

        return self.write(dict(code=0, msg='导入数据共'+str(result_apply.rowcount)+'条',data=str(result_apply.rowcount)))



class updateprojectreviewhandler(RequestHandler):

    def post(self, *args, **kwargs):
        data = json.loads(self.request.body.decode("utf-8"))
        applysno = data.get('applysno', None)
        applytitle = data.get('applytitle', None)
        reviewrecordtime = data.get('reviewrecordtime', None)
        reviewprojectname = data.get('reviewprojectname', None)
        reviewpanel = data.get('reviewpanel', None)
        reviewstatus = data.get('reviewstatus', None)
        reviewprojectno = data.get('reviewprojectno', None)
        reviewprojectmanage = data.get('reviewprojectmanage', None)
        reviewmanday = data.get('reviewmanday', None)
        reviewprojectstart = data.get('reviewprojectstart', None)
        reviewprojectend = data.get('reviewprojectend', None)
        reviewprojectcost = data.get('reviewprojectcost', None)
        reviewprojectrecord = data.get('reviewprojectrecord', None)
        reviewrecorddate = data.get('reviewrecorddate', None)
        submiter = data.get('submiter', None)
        applydata = data.get('applydata', None)

        if applysno == None:
            return self.write(dict(code=-1, msg='信息有误，拒绝您的申请'))
        else:
            with DBContext('w', None, True) as session:
                with DBContext('w', None, True) as session:
                    session.query(projectreview).filter(projectreview.applysno == applysno).delete()
                    session.commit()
                    session.add(projectreview(applysno=applysno,applytitle=applytitle, reviewrecordtime=reviewrecordtime, reviewprojectname=reviewprojectname,reviewpanel=reviewpanel,
                                              reviewstatus=reviewstatus,reviewprojectno=reviewprojectno,reviewprojectmanage=reviewprojectmanage,reviewmanday=reviewmanday,reviewprojectstart=reviewprojectstart,
                                              reviewprojectend=reviewprojectend,reviewprojectcost=reviewprojectcost,reviewprojectrecord=reviewprojectrecord,reviewrecorddate=reviewrecorddate,
                                              submiter=submiter,applydata=applydata))
                    session.commit()
                    if reviewstatus!=None:
                        session.query(projectmanger).filter(projectmanger.applysno == applysno).update({projectmanger.status:reviewstatus})
                    session.commit()


            with DBContext('r') as session:
                result_review=session.query(projectreview).filter(projectreview.applysno==applysno).first()
            return self.write(dict(code=0, msg="更新完成",appsno=result_review.applysno,applytitle=applytitle))

class projectreviewdetailhandler(RequestHandler):

      def post(self, *args, **kwargs):
        applysno = self.request.body.decode("utf-8")
        with DBContext('r') as session:
            _result=session.query(projectreview).filter(projectreview.applysno == applysno).first()
            if _result is not None:
                _result = model_to_dict(_result)
        return self.write(dict(code=0, msg='查询成功',data=_result))
class deleteprojecthandler(RequestHandler):

      def post(self, *args, **kwargs):
        applysno = json.loads(self.request.body.decode("utf-8"))
        if len(applysno)<6:
            return self.write(dict(code=-1, msg='信息有误，拒绝您的申请'))
        else:
            with DBContext('w') as session:
                _result=session.query(projectreview).filter(projectreview.applysno == applysno).delete()
                session.commit()
                _result=session.query(projectmanger).filter(projectmanger.applysno == applysno).delete()
                session.commit()
                if _result>0:
                    return self.write(dict(code=0, msg='删除成功'))
                else:
                    return self.write(dict(code='-4', msg='系统异常，删除失败'))


class projectdetailhandler(RequestHandler):

      def post(self, *args, **kwargs):
        data = json.loads(self.request.body.decode("utf-8"))
        applysno = str(data)

        if applysno == '0':
            return self.write(dict(code=-1, msg='信息有误，拒绝您的申请'))
        else:
            with DBContext('r') as session:
                result_apply=session.query(projectmanger).filter(projectmanger.apply_sno==applysno).first()
                rs_apply = model_to_dict(result_apply)
            return self.write(dict(code=0, msg='查询成功',data=rs_apply,appsno=result_apply.apply_sno))
class userlisthandler(RequestHandler):
    def get(self):
        return  self.write(dict(code=0, msg='请使用POST请求'))
    def post(self, *args, **kwargs):


        if len(self.request.body)>0:
            data = json.loads(self.request.body.decode("utf-8"))
            print(data)
            searchname = str(data)
            with DBContext('r') as session:
                result=session.query(Users.user_id,Users.nickname,Users.username,Users.email).filter(Users.nickname==searchname).all()
        else:
            with DBContext('r') as session:
                result=session.query(Users.user_id,Users.nickname,Users.username,Users.email).all()
        return self.write(dict(code=0, msg='查询成功',data=result))


class projectreviewlisthandler(RequestHandler):

    def post(self, *args, **kwargs):
        data = json.loads(self.request.body.decode("utf-8"))
        projecttype = data.get('projecttype', None)
        applytype = data.get('applytype', None)
        applytitle = data.get('applytitle', None)
        applysubmiter = data.get('applysubmiter', None)
        pageIndex = data.get('pageIndex', None)
        pageSize = data.get('pageSize', None)

        if projecttype ==None:
            return self.write(dict(code=-1, msg='信息有误，拒绝您的申请'))
        else:
            with DBContext('r') as session:
                if applytitle!='' or applysubmiter!='':
                    count=session.query(projectmanger,Users.nickname).join(Users,projectmanger.applysubmiter==Users.user_id).filter(projectmanger.applytitle.like ('%'+applytitle+'%'),projectmanger.applysubmiter.like ('%'+applysubmiter+'%')).count()
                    result_applyorder=session.query(projectmanger,Users.nickname).join(Users,projectmanger.applysubmiter==Users.user_id).filter(projectmanger.applytitle.like ('%'+applytitle+'%'),projectmanger.applysubmiter.like ('%'+applysubmiter+'%')).order_by((projectmanger.id).desc()).limit(pageSize).offset((pageIndex-1)*pageSize)
                else:
                    count=session.query(projectmanger).count()
                    #result_applyorder=session.query(projectmanger.id,projectmanger.applysubmiter,projectmanger.status,projectmanger.applytitle,projectmanger.applysno,projectmanger.applydata,projectmanger.applytime,projectmanger.applytype,Users.nickname).outerjoin(Users,projectmanger.applysubmiter==Users.user_id).order_by((projectmanger.id).desc()).limit(pageSize).offset((pageIndex-1)*pageSize)
                    result_applyorder=session.query(projectmanger.id,projectmanger.projectsno,projectmanger.applysubmiter,projectmanger.status,projectmanger.applytitle,projectmanger.applysno,projectmanger.applydata,projectmanger.applytime,projectmanger.applytype,projectmanger.projectmanager,projectmanger.projecttype,projectmanger.contractbudget,projectmanger.projectprogress).order_by((projectmanger.id).desc()).limit(pageSize).offset((pageIndex-1)*pageSize)
            rs_apply=[]
        for msg in result_applyorder:
                apply_dict={}
                apply_dict=_model_to_dict(msg)
                '''
                apply_dict['id']=msg.id
                apply_dict['apply_submiter']=msg.apply_submiter
                apply_dict['status']=msg.status
                apply_dict['apply_title']=msg.apply_title
                apply_dict['apply_sno']=msg.apply_sno
                apply_dict['apply_data']=msg.apply_data
                apply_dict['apply_time']=msg.apply_time
                apply_dict['apply_type']=msg.apply_type
                apply_dict['nickname']=msg.nickname
                '''
                rs_apply.append(apply_dict)

        return self.write(dict(code=0, msg='查询成功',data=rs_apply,pageTotal=count))

class sendprojectemailhandler(RequestHandler):

    def post(self, *args, **kwargs):
        applysno=time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
        data = json.loads(self.request.body.decode("utf-8"))
        emailaddress = data.get('emailaddress', None)
        ccaddress = data.get('ccaddress', None)
        emailtitle = applysno+data.get('emailtitle', None)
        emailcontent = data.get('emailcontent', None)

        if emailaddress == None:
            return self.write(dict(code=-1, msg='信息有误，拒绝您的申请'))
        else:
            EMAIL_HOST='smtp.163.com'
            EMAIL_PORT='25'
            EMAIL_HOST_USER='grkjxmgl@163.com'
            EMAIL_HOST_PASSWORD='kingdom88'
            EMAIL_USE_SSL=0
            MAIL_USE_TLS=0
            try:
                obj = SendMail(mail_host=EMAIL_HOST,
                               mail_port=EMAIL_PORT,
                               mail_user=EMAIL_HOST_USER,
                               mail_password=EMAIL_HOST_PASSWORD,
                               mail_ssl=False,
                               mail_tls=False)

                obj.send_mail(emailaddress, emailtitle,emailcontent, subtype='html')
                return self.write(dict(code=0, msg='邮件已经发送成功'))
            except Exception as e:
                return dict(code=-1, msg='邮件发送失败 {}'.format(str(e)))


projectmanagement_urls = [
    (r"/api/v1/pm/addproject/", addprojecthandler),
    (r"/api/v1/pm/importproject/", importprojecthandler),
    (r"/api/v1/pm/projectdetail/", projectdetailhandler),
    (r"/api/v1/pm/sendprojectemail/", sendprojectemailhandler),
    (r"/api/v1/pm/projectreviewlist/", projectreviewlisthandler),
    (r"/api/v1/pm/updateprojectreview/", updateprojectreviewhandler),
    (r"/api/v1/pm/projectreviewdetail/", projectreviewdetailhandler),
    (r"/api/v1/pm/deleteproject/", deleteprojecthandler),
    (r"/api/v1/pm/userlist/", userlisthandler),
]

if __name__ == "__main__":
    pass
