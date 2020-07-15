# # 8.充值
# import pytest
#
# from tools.api import request_tool
# from tools.data import excel_tool
#
# data = excel_tool.get_test_case("test_case/users/充值测试2.xls")
# @pytest.mark.parametrize("yl_ming,cz_jin,expect",data[1],ids=data[0])
# def test_acc_recharge(pub_data,yl_ming,cz_jin,expect):
#     pub_data["yl_ming"] = yl_ming
#     pub_data["cz_jin"] = cz_jin
#     method = "POST"  #请求方法，全部大写
#     feature = "用户模块"  # allure报告中一级分类
#     story = '用户充值'  # allure报告中二级分类
#     uri = "/acc/recharge"  # 接口地址
#     # headers ={}
#     # post请求json数据，注意数据格式为字典或者为json串 为空写None
#     json_data = '''
# {
#   "accountName": "${yl_ming}",
#   "changeMoney": "${cz_jin}
# }
#     '''
#     status_code = 200  # 响应状态码
#     expect = expect  # 预期结果
#     # --------------------分界线，下边的不要修改-----------------------------------------
#     # method,pub_data和url为必传字段
#     r = request_tool.request(method=method,url=uri,pub_data=pub_data,json_data=json_data,status_code=status_code,expect=expect,feature=feature,story=story)

'''
自动生成 数字 20,80   #生成20到80之间的数字 例：56
自动生成 字符串 5 中文数字字母特殊字符 xuepl        #生成以xuepl开头加上长度2到5位包含中文数字字母特殊字符的字符串，例子：xuepl我1
自动生成 地址
自动生成 姓名
自动生成 手机号
自动生成 邮箱
自动生成 身份证号
'''
from tools.api import request_tool
#1. 注册
def test_signup(pub_data):
    pub_data["phone"] = "自动生成 手机号"
    pub_data["userName"] = "自动生成 字符串 5 数字 cby"
    method = "POST"  #请求方法，全部大写
    feature = "用户模块"  # allure报告中一级分类
    story = '用户登录'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/signup"  # 接口地址
    # post请求json数据，注意数据格式为字典或者为json串 为空写None
    json_data = '''
{
  "phone": "${phone}",
  "pwd": "123123c",
  "rePwd": "123123c",
  "userName": "${userName}"
}
    '''
    status_code = 200  # 响应状态码
    expect = "2000"  # 预期结果
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    request_tool.request(method=method,url=uri,pub_data=pub_data,json_data=json_data,status_code=status_code,expect=expect,feature=feature,story=story,title=title)
#2. 登录
def test_login(pub_data):
    method = "POST"  #请求方法，全部大写
    feature = "用户模块"  # allure报告中一级分类
    story = '用户登录'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/login"  # 接口地址
    # post请求json数据，注意数据格式为字典或者为json串 为空写None
    json_data = '''
    {
  "pwd": "123123c",
  "userName": "${userName}"
}
    '''
    status_code = 200  # 响应状态码
    expect = "2000"  # 预期结果
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    request_tool.request(method=method,url=uri,pub_data=pub_data,json_data=json_data,status_code=status_code,expect=expect,feature=feature,story=story,title=title)
#3. 增加商品
def test_product_addProd(pub_data):
    pub_data["productCode"] = "自动生成 字符串 5 数字字母"
    method = "POST"  #请求方法，全部大写
    feature = "商品模块"  # allure报告中一级分类
    story = '增加商品'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/product/addProd"  # 接口地址
    headers = {
        "token" :pub_data["token"]
    }
    # post请求json数据，注意数据格式为字典或者为json串 为空写None
    json_data = '''
{
  "brand": "匡威",
  "colors": [
    "黑色"
  ],
  "price": 100,
  "productCode": "${productCode}",
  "productName": "经典黑",
  "sizes": [
    "36"
  ],
  "type": "服装"
}
    '''
    status_code = 200  # 响应状态码
    expect = "2000"  # 预期结果
    # json path，参数类型为列表 根据jsonpath提取响应正文中的数据
    json_path = [{"productCode": '$.data.productCode'}]
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    request_tool.request(json_path=json_path,method=method,url=uri,pub_data=pub_data,json_data=json_data,status_code=status_code,expect=expect,feature=feature,story=story,title=title,headers=headers)
#4. 查询商品
def test_product_getSkuByProdCode(pub_data):
    method = "GET"  #请求方法，全部大写
    feature = "商品模块"  # allure报告中一级分类
    story = '查询单个用户'  # allure报告中二级分类
    title = "查询单个用户_全字段正常流_1"  # allure报告中用例名字
    uri = "/product/getSkuByProdCode"  # 接口地址
    # post请求json数据，注意数据格式为字典或者为json串 为空写None
    params = {"prodCode":"${productCode}"}
    headers={"token":pub_data["token"]}
    status_code = 200  # 响应状态码
    expect = "2000"  # 预期结果
    # json path，参数类型为列表 根据jsonpath提取响应正文中的数据
    json_path = [{"skuCode": '$.data[0].skuCode'}]
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    request_tool.request(json_path=json_path,method=method,url=uri,pub_data=pub_data,params=params,status_code=status_code,expect=expect,feature=feature,story=story,title=title,headers=headers)
#5. 修改商品价格
def test_product_changePrice(pub_data):
    method = "POST"  #请求方法，全部大写
    feature = "商品模块"  # allure报告中一级分类
    story = '修改商品价格'  # allure报告中二级分类
    title = "修改商品价格_全字段正常流_1"  # allure报告中用例名字
    uri = "/product/changePrice"  # 接口地址
    # post请求json数据，注意数据格式为字典或者为json串 为空写None
    data = {"SKU":'${skuCode}',"price":"150"}
    header={"token":pub_data["token"]}
    status_code = 200  # 响应状态码
    expect = "2000"  # 预期结果
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    request_tool.request(method=method,url=uri,pub_data=pub_data,data=data,status_code=status_code,expect=expect,feature=feature,story=story,title=title,headers=header)
#6. 查询商品验证
def test_product_getSkuByProdCode2(pub_data):
    method = "GET"  #请求方法，全部大写
    feature = "商品模块"  # allure报告中一级分类
    story = '查询单个用户'  # allure报告中二级分类
    title = "查询单个用户_全字段正常流_1"  # allure报告中用例名字
    uri = "/product/getSkuByProdCode"
    # post请求json数据，注意数据格式为字典或者为json串 为空写None
    params = {"prodCode":"${productCode}"}
    headers={"token":pub_data["token"]}
    status_code = 200  # 响应状态码
    expect = "2000"  # 预期结果
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    request_tool.request(method=method,url=uri,pub_data=pub_data,params=params,status_code=status_code,expect=expect,feature=feature,story=story,title=title,headers=headers)
#7. 根据产品编码批量修改商品价格
def test_product_changePriceByProdCode(pub_data):
    method = "POST"  #请求方法，全部大写
    feature = "商品模块"  # allure报告中一级分类
    story = '根据产品编码批量修改商品价格'  # allure报告中二级分类
    title = "根据产品编码批量修改商品价格_全字段正常流_1"  # allure报告中用例名字
    uri = "/product/changePriceByProdCode"  # 接口地址
    # post请求json数据，注意数据格式为字典或者为json串 为空写None
    data = {"price":'555',"prodCode":"${productCode}"}
    headers={"token":pub_data["token"]}
    status_code = 200  # 响应状态码
    expect = "2000"  # 预期结果
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    request_tool.request(method=method,url=uri,pub_data=pub_data,data=data,status_code=status_code,expect=expect,feature=feature,story=story,title=title,headers=headers)
#8. 修改产品的状态测试下架
def test_product_soldOut(pub_data):
    method = "POST"  #请求方法，全部大写
    feature = "商品模块"  # allure报告中一级分类
    story = '下架'  # allure报告中二级分类
    title = "下架_全字段正常流_1"  # allure报告中用例名字
    uri = "/product/soldOut"  # 接口地址
    # post请求json数据，注意数据格式为字典或者为json串 为空写None
    data = {"productCode":'${productCode}'}
    headers={"token":pub_data["token"]}
    status_code = 200  # 响应状态码
    expect = "2000"  # 预期结果
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    request_tool.request(method=method,url=uri,pub_data=pub_data,data=data,status_code=status_code,expect=expect,feature=feature,story=story,title=title,headers=headers)
#9. 修改产品的状态测试预售
def test_product_toPreSale(pub_data):
    method = "POST"  #请求方法，全部大写
    feature = "商品模块"  # allure报告中一级分类
    story = '预售'  # allure报告中二级分类
    title = "预售_全字段正常流_1"  # allure报告中用例名字
    uri = "/product/toPreSale"  # 接口地址
    # post请求json数据，注意数据格式为字典或者为json串 为空写None
    data = {"productCode":'${productCode}'}
    headers={"token":pub_data["token"]}
    status_code = 200  # 响应状态码
    expect = "2000"  # 预期结果
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    request_tool.request(method=method,url=uri,pub_data=pub_data,data=data,status_code=status_code,expect=expect,feature=feature,story=story,title=title,headers=headers)




