from base import login

page, this_page, p = login.get_login()


page.locator('#我的工作管理二级菜单').click()
page.locator('#我的工作任务管理入口').click()
page.locator('#我的工作任务管理入口~ul a[title="我安排的未完任务"]').click()
this_page.locator('table thead #topcheckbox').click()
this_page.locator('#调整负责人').click()
page.locator('#改由本人负责任务').click()
page.locator('.toolBar').get_by_text('取消').click()
page.locator('#taskSetting').click()
page.wait_for_timeout(500)
this_page.get_by_role("cell", name="任务名称:").get_by_label("").fill('审批数据视图设计申请')
this_page.locator("#exeStatus_ENUMREMARK").click()
page.wait_for_timeout(300)
page.locator('#suggest').get_by_text('批准').click()
this_page.locator('.subBar .buttonContent').get_by_text('精确查询').click()
page.locator('#progressBar').wait_for(state='hidden')
this_page.locator('.panelBar .combox').select_option('500')
page.locator('#progressBar').wait_for(state='hidden')
this_page.locator('table thead #topcheckbox').click()
this_page.locator('#dataCM').locator('#执行任务').click()
page.locator('#完成本轮任务').click()
page.locator('.toolBar').get_by_text('取消').click()

# page.wait_for_timeout(1000)
# this_page.get_by_role("cell", name="任务名称:").get_by_label("").fill('创建指定数据视图组件')
# this_page.get_by_role("cell", name="工作对象简称:").get_by_label("").fill('低性能端口模板')
# this_page.locator('.subBar .buttonContent').get_by_text('精确查询').click()

input('~~~')
