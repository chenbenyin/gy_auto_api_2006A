import random

import allure
import requests

from config.conf import API_URL
@allure.feature("用户管理")
@allure.story("充值提现模块")
@allure.title("扣款接口-账户余额不足")
def test_recharge(pub_data,db):
    with allure.step("第一步、执行请求数据"):
        res = db.select_execute("SELECT account_name FROM `t_cst_account` WHERE `status` =0 AND `account_name`IS NOT NULL;")
    with allure.step("第二步、从查询结果中随机获取一条，去第一条数据"):
        account_name = random.choice(res)[0]
    with allure.step("第三步、准备请求数据"):
        data ={
        "accountName":account_name,
        "changeMoney":100
        }
    with allure.step("第四步、发送请求数据"):
        r = requests.post(API_URL+"/acc/charge",json=data)
    with allure.step("第五步、获取请求内容"):
        allure.attach(r.request.method,"请求方法",allure.attachment_type.TEXT)
        allure.attach(r.request.url,"请求url",allure.attachment_type.TEXT)
        allure.attach(str(r.request.headers),"请求头",allure.attachment_type.TEXT)
        allure.attach(r.request.body,"请求正文",allure.attachment_type.TEXT)
    with allure.step("第六步、获取响应内容"):
        allure.attach(str(r.status_code),"响应状态码",allure.attachment_type.TEXT)
        allure.attach(str(r.headers),"响应头",allure.attachment_type.TEXT)
        allure.attach(r.text,"响应正文",allure.attachment_type.TEXT)
    with allure.step("第七步、断言"):
        allure.attach(r.text,"实际结果",allure.attachment_type.TEXT)
        allure.attach("账户余额不足","预期结果",allure.attachment_type.TEXT)
        assert "账户余额不足"in r.text






