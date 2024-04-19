from base import login


# def add_data_object(viewName):
object_name_abbr = '低性能端口模板'
object_name = '密码服务中间件::' + object_name_abbr
business_name = '116-中间件部署管理'
fun_class_list = ['产品配置管理', '平台密钥管理', '产品出厂配置']
fun_class_name = fun_class_list[0]
design_plan = '密码服务中间件'
db_id = 'hisuSocketSvrConf'
print(fun_class_name)

login_url = 'http://work.paytunnel.cn:19060/gms-v4/selectSystem?key=developmentServerTest121'
login_username = 'lwl'
login_password = 'lwl123'
page, this_page = login.login(login_url, login_username, login_password)
page.locator('#开发工作管理二级菜单组').click()
page.locator('#软件产品设计管理二级菜单组').click()
page.locator('a[title="公司产品型号"]').click()
this_page.locator('tr td[title="Splenwise密码服务中间件"]').click()
this_page.locator('#业务框架').click()
page.locator('#设计业务方案').click()
this_page.locator('.displayFirstClass').click()
this_page.get_by_text('业务-按序号排序').click()
# 先写死
# this_page.locator('//*[@id="firstTree"]/li/ul/li[1]/ul/li[26]/div/a').click()
this_page.locator('li.selected div a').get_by_text(business_name).click()
this_page.locator('li.selected div').get_by_text('功能分类').click()
this_page.locator('li.selected div a').get_by_text(fun_class_name).click()
this_page.locator('li.selected div').get_by_text('设计的数据对象-名称索引').click(button='right')
page.locator('#dataCM').locator('#新增').click()

# 填写参数，批量增加
dialog = page.locator('.dialog')
dialog.locator('#compName').fill(object_name)
dialog.locator('#serviceAddr').fill(object_name_abbr)
page.wait_for_timeout(1000)
# 点击右侧放大镜(属性lookupgroup=factory)选择


def dialog_search(page, name):
    dialog_input = page.locator('.pageHeader p input')
    dialog_input.fill(name)
    dialog_input.press('Enter')
    page.locator('.pageContent .gridScroller tr td').get_by_text(name, exact=True).dblclick()


page.locator('.pageFormContent  p').locator('a[lookupgroup="数据对象管理界面.factory"]').click()
dialog_search(page, design_plan)
page.locator('.pageFormContent  p').locator('a[lookupgroup="数据对象管理界面.compSrlID"]').click()
dialog_search(page, db_id)

# 新增一条
# page.locator('.formBar').get_by_text('增加').click()

# 全部新增完成后，申请任务

# 返回一组工作任务简称
input('暂停 ~~~')


