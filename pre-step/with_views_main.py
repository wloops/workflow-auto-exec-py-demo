# 从任务列表界面逐个进行操作
import json
import time
from base import login
from base import common_operate

start_time = time.time()

with open('main_view_list.json', 'r', encoding='utf-8') as file:
    main_view_list = json.load(file)
with open('publish.json', 'r', encoding='utf-8') as file:
    publish_params = json.load(file)


def get_login():
    login_url = 'http://work.paytunnel.cn:19060/gms-v4/selectSystem?key=developmentServerTest121'
    login_username = 'lwl'
    login_password = 'lwl123'
    headless = False
    page, this_page, p = login.login(login_url, login_username, login_password, headless)
    page.locator('#progressBar').wait_for(state='hidden')
    return page, this_page, p


def start_main(page, this_page, p, object_name_abbr, view_button, factory, comp_srl_id):
    # object_name_abbr = '低性能端口模板'
    # view_button = '增加记录,删除记录'
    # 2 根据任务名称和工作对象简称 搜索后确定唯一的一个任务进行操作
    this_page.get_by_role("cell", name="任务名称:").get_by_label("").fill('创建指定数据视图组件')
    this_page.get_by_role("cell", name="工作对象简称:").get_by_label("").fill(object_name_abbr)
    this_page.locator('.subBar .buttonContent').get_by_text('精确查询').click()
    page.locator('#progressBar').wait_for(state='hidden')
    # 2.1 选中目标记录，点击：工作对象菜单->设计数据视图(hover)->创建数据视图组件->(弹窗)点击：确定
    this_page.get_by_role("cell", name=object_name_abbr).first.click()
    this_page.locator('#dataCM').locator('#工作对象菜单').click()
    page.locator('#设计数据视图').hover()
    page.locator('#创建数据视图组件').click()
    page.locator('.toolBar').get_by_text('确定').click()
    page.locator('.formBar').get_by_text('闭').click()
    # 2.2 选中目标记录，点击：工作对象菜单->设计数据视图(hover)->设计数据视图组件
    this_page.get_by_role("cell", name=object_name_abbr).first.click()
    this_page.locator('#dataCM').locator('#工作对象菜单').click()
    page.locator('#设计数据视图').hover()
    page.locator('#设计数据视图组件').click()
    # 在 设计数据视图组件 界面中
    # 3 点击树的第一条记录
    this_page.locator('.displayFirstClass').click()
    # 4 填入 基础开发方案 和 基础组件 等参数
    common_operate.dialog_search(page, factory, 'factory')  # 基础开发方案
    common_operate.dialog_search(page, comp_srl_id, 'compSrlID')  # 基础组件
    # 5 点击右下角 修改
    this_page.locator('.formBar #treeUpdateButton').get_by_text('修改').click()
    page.locator('.toolBar').get_by_text('确定').click()
    page.locator('#progressBar').wait_for(state='hidden')
    # 6 右键点击树的第一条记录  然后->设计对象组件(hover)->从基础对象创建本对象-复制数据字典并创建界面
    this_page.locator('.displayFirstClass').locator('.abcdefg1').click(button='right')
    page.locator('#设计对象组件').hover()
    page.wait_for_timeout(300)
    page.locator('#从基础对象创建本对象-复制数据字典并创建界面').click()
    # 7 三次确定
    page.locator('.formBar').get_by_text('确定').click()
    page.wait_for_timeout(100)
    page.locator('.formBar').get_by_text('确定').click()
    page.wait_for_timeout(100)
    page.locator('.toolBar').get_by_text('确定').click()

    page.locator('#progressBar').wait_for(state='hidden')
    error_box = page.locator('.alertInner h1').get_by_text('错误提示')
    error_box_is_visible = error_box.is_visible()
    # print('error_box_is_visible：', error_box_is_visible, error_box)
    if error_box_is_visible:
        print('创建界面出错')
        page.locator('.toolBar').get_by_text('确定').click()
    else:
        page.locator('.formBar').get_by_text('闭').click()

    # 创建IT组件
    # 点击：创建的操作界面->[界面名称]->使用界面的IT组件(右键)->新增
    this_page.locator('.displayFirstClass').click(button='right')
    page.locator('#dataCM').get_by_text('刷新该节点').click()
    this_page.get_by_text('创建的操作界面').click()
    this_page.locator('.abcdefg3').get_by_text(object_name_abbr).click()
    # print(view_button)
    if bool(view_button):
        this_page.locator('#compAttrValue8~input').click()
        common_operate.dialog_transfer_search(page, view_button)
    # 击右下角 修改
    this_page.locator('.formBar #treeUpdateButton').get_by_text('修改').click()
    page.locator('#progressBar').wait_for(state='hidden')
    page.locator('.toolBar').get_by_text('确定').click()

    this_page.locator('.abcdefg3').get_by_text(object_name_abbr).click(button='right')
    page.locator('#dataCM').get_by_text('刷新该节点').click()
    this_page.get_by_text('使用界面的IT组件').click(button='right')
    page.locator('#dataCM').locator('#新增').click()
    # # 依次选择 型号、IT组件别名、IT组件  -> 点击：增加
    project_model = publish_params['project_model']['value']
    it_unit_abbr = publish_params['it_unit_abbr']['value']
    it_unit_name = publish_params['it_unit_name']['value']
    common_operate.dialog_search(page, project_model, 'IT组件使用的操作界面管理界面.srlID')
    common_operate.dialog_search(page, it_unit_abbr, 'IT组件使用的操作界面管理界面.attr128LenValue9')
    common_operate.dialog_search(page, it_unit_name, 'IT组件使用的操作界面管理界面.compName')
    page.locator('.formBar').get_by_text('增加').click()
    page.locator('#progressBar').wait_for(state='hidden')
    # 关闭操作结果界面和创建IT组件界面
    dialog = page.locator('.dialog >> visible=true')
    error_box = page.locator('.formMsgError')
    error_box_is_visible = error_box.is_visible()
    # print('error_box_is_visible：', error_box_is_visible)
    if error_box_is_visible:
        print('创建IT组件出错：', error_box.inner_text())
        error_box.wait_for(state='hidden')
        dialog.locator('.formBar').get_by_text('取消').click()
        this_page.get_by_text('使用界面的IT组件').click(button='right')
        page.locator('#dataCM').get_by_text('刷新该节点').click()

    else:
        closes = page.locator('.formBar').get_by_text('闭').all()
        for close in closes:
            close.click()
    # 发布
    # [IT组件别名 同名]右键->创建使用的界面(hover)->创建并发布-向{publish.json->dest_env}
    this_page.locator('.abcdefg5').get_by_text(it_unit_abbr).click(button='right')
    # dest_env = '创建并发布-向缺省部署实例'
    dest_env = '创建并发布-向' + publish_params['dest_env']['value']
    page.locator('#创建使用的界面').hover()
    page.locator('#showTreeNode').get_by_text(dest_env).click()
    # 三次确定

    page.locator('.formBar').get_by_text('确定').click()
    page.wait_for_timeout(100)
    page.locator('.formBar').get_by_text('确定').click()
    page.wait_for_timeout(100)
    page.locator('.toolBar').get_by_text('确定').click()
    page.locator('#progressBar').wait_for(state='hidden')
    # 打印或记录响应结果（日志）
    # logs = page.locator('#gms_showinfo li').all()
    # for log in logs:
    #     print(log.inner_text())
    error_box = page.locator('.alertInner h1').get_by_text('错误提示')
    error_box_is_visible = error_box.is_visible()
    # print('error_box_is_visible：', error_box_is_visible, error_box)
    if error_box_is_visible:
        print('创建界面出错')
        page.locator('.toolBar').get_by_text('确定').click()
    else:
        page.locator('.formBar').get_by_text('闭').click()
    dialog = page.locator('.dialog >> visible=true')
    dialog_is_visible = dialog.is_visible()
    if dialog_is_visible:
        dialog.locator('.formBar').get_by_text('取消').click()
    page.wait_for_timeout(300)
    page.locator('#taskSetting').click()
    page.locator('#progressBar').wait_for(state='hidden')
    return


def __main__run():
    page, this_page, p = get_login()
    task_id = 0
    for index, view in enumerate(main_view_list):
        object_name_abbr = view.get('base_view_name_abbr')
        task_id += 1
        print(f'开始执行==>[{task_id}]', object_name_abbr)
        view_button = view.get('view_button')
        factory = view.get('factory')
        comp_srl_id = view.get('object_name')
        # 临时使用，跳过前面的
        # if object_name_abbr == '密码机指令服务':
        start_main(page, this_page, p, object_name_abbr, view_button, factory, comp_srl_id)
        print(object_name_abbr, f'<==执行成功[{task_id}]')


__main__run()

end_time = time.time()
print(f"创建指定数据视图组件及发布。运行时间: {end_time - start_time}秒")
