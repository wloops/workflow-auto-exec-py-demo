import json
import time
from base import login
from base import common_operate

start_time = time.time()


def add_data_objects(page, this_page, dialog, object_name_abbr, object_name, db_id, current_classify):
    object_name = '密码服务中间件::' + object_name.rstrip('界面')
    design_plan = '密码服务中间件'
    # 填写参数，批量增加
    dialog.locator('#compName').fill(object_name)
    dialog.locator('#serviceAddr').fill(object_name_abbr)

    # 点击右侧放大镜(属性lookupgroup=factory)选择
    page.locator('.pageFormContent  p').locator('a[lookupgroup="数据对象管理界面.factory"]').click()
    common_operate.dialog_search(page, design_plan)
    page.locator('.pageFormContent  p').locator('a[lookupgroup="数据对象管理界面.compSrlID"]').click()
    common_operate.dialog_search(page, db_id)

    # 新增一条
    page.locator('.formBar').get_by_text('增加').click()
    page.locator('#progressBar').wait_for(state='hidden')

    error_box = page.locator('.formMsgError')
    error_box_is_visible = error_box.is_visible()
    print('error_box_is_visible：', error_box_is_visible)
    if error_box_is_visible:
        print('报错', error_box.inner_text())
        error_box.wait_for(state='hidden')
    else:
        closes = page.locator('.formBar').get_by_text('闭').all()
        for close in closes:
            close.click()

    # page.wait_for_timeout(500)
    # 全部新增完成后，申请任务
    # 返回一组工作任务简称
    # input('暂停 ~~~')


def reach_classify(page, this_page, p, business_name, project_model):
    page.locator('#开发工作管理二级菜单组').click()
    page.locator('#软件产品设计管理二级菜单组').click()
    page.locator('#软件产品设计管理二级菜单组~ul a[title="公司产品型号"]').click()
    page.locator('#progressBar').wait_for(state='hidden')
    this_page.locator('tr td[title="' + project_model + '"]').click()
    this_page.locator('#业务框架').click()
    page.locator('#设计业务方案').click()
    this_page.locator('.displayFirstClass').click()
    this_page.get_by_text('业务-按名称排序').click()
    # 先写死
    # this_page.locator('//*[@id="firstTree"]/li/ul/li[1]/ul/li[26]/div/a').click()
    this_page.locator('li.selected div a').get_by_text(business_name).click()
    this_page.locator('li.selected div').get_by_text('功能分类').click()
    print('已打开相应的功能分类')

    return True


# 创建视图任务
def create_view_plan(page, this_page, p, classify, last_one=False):
    if last_one:
        page.locator('.formBar').get_by_text('取消').click()
        # 创建新的入口视图
        # create_entrance_view(page, this_page, p, classify)
        this_page.locator('li.selected div').get_by_text('功能分类').click(button='right')
        page.locator('#dataCM').get_by_text('刷新该节点').click()
    classify_link = this_page.locator('li.selected ul li')
    classify_son_link = classify_link.get_by_text(classify)
    classify_son_link.click()
    classify_link.get_by_text('设计的数据对象-名称索引').click(button='right')

    # 创建视图任务 逻辑
    classify_link.get_by_text('设计的数据对象-名称索引').click()
    id_class = classify_link.get_by_text('设计的数据对象-名称索引').get_attribute('class')
    id_class = id_class.split()[0]
    children_list_class = 'abcdefg' + str(int(id_class.split('g')[1]) + 1)
    child_list = this_page.locator('.' + children_list_class).all()
    print(f'将要为【{classify}】分类下的{len(child_list)}个数据对象，创建视图任务')
    for child in child_list:
        child.click(button='right')
        page.locator('#dataCM').locator('li#任务管理').hover()
        page.locator('#showTreeNode').locator('li#数据视图任务').hover()
        page.locator('#showTreeNode').locator('li#只创建初始任务').click()
        page.locator('.toolBar').get_by_text('确定').click()
        page.locator('#progressBar').wait_for(state='hidden')
        error_box = page.locator('.alertInner h1').get_by_text('错误提示')
        error_box_is_visible = error_box.is_visible()
        if error_box_is_visible:
            print('任务创建报错。跳出循环')
            page.locator('.toolBar').get_by_text('确定').click()
        else:
            page.locator('.formBar').get_by_text('闭').click()

    this_page.locator('li.selected div').get_by_text('功能分类').click(button='right')
    page.locator('#dataCM').get_by_text('刷新该节点').click()


def open_add_view(page, this_page, p, classify, old_classify='', close_old=False):
    if close_old:
        page.locator('.formBar').get_by_text('取消').click()
        this_page.locator('li.selected div').get_by_text('功能分类').click(button='right')
        page.locator('#dataCM').get_by_text('刷新该节点').click()
        create_view_plan(page, this_page, p, old_classify)
    classify_link = this_page.locator('li.selected ul li')
    classify_son_link = classify_link.get_by_text(classify)
    classify_son_link.click()
    classify_link.get_by_text('设计的数据对象-名称索引').click(button='right')
    page.locator('#dataCM').locator('#新增').click()
    page.wait_for_timeout(500)

    return True


# 读取 JSON 文件
with open('main_view_list.json', 'r', encoding='utf-8') as file:
    main_view_list = json.load(file)
with open('publish.json', 'r', encoding='utf-8') as file:
    publish_params = json.load(file)


def __main__run():
    page, this_page, p = login.get_login()
    current_classify = main_view_list[0].get('classify').split(':')[0]
    business_name = publish_params['business_name']['value']
    project_model = publish_params['project_model']['value']
    reach_classify_end = reach_classify(page, this_page, p, business_name, project_model)
    open_add_view(page, this_page, p, current_classify)
    if reach_classify_end:
        for obj in main_view_list:
            name = obj.get('base_view_name')
            abbr = obj.get('base_view_name_abbr')
            classify = obj.get('classify').split(':')[0]
            db_name = obj.get('db_name')
            object_name = obj.get('object_name')
            print(name, abbr, classify, db_name, object_name)
            if current_classify != classify:
                old_classify = current_classify
                current_classify = classify
                open_add_view(page, this_page, p, current_classify, old_classify, True)
            page.wait_for_timeout(300)
            dialog = page.locator('.dialog')
            add_data_objects(page, this_page, dialog, abbr, name, db_name, current_classify)

    # 跑完后，给最后一个分类创建视图任务
    create_view_plan(page, this_page, p, current_classify, True)


__main__run()

end_time = time.time()
print(f"创建视图对象及任务。运行时间: {end_time - start_time}秒")
