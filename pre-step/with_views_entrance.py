import json
import time

from base import login, common_operate

start_time = time.time()

# 读取 JSON 文件
with open('entrance_view_list.json', 'r', encoding='utf-8') as file:
    entrance_view_list = json.load(file)
with open('main_view_list.json', 'r', encoding='utf-8') as file:
    main_view_list = json.load(file)
with open('publish.json', 'r', encoding='utf-8') as file:
    publish_params = json.load(file)


def get_new_view_name(page, this_page, p, origin_children_view_list):
    origin_list = origin_children_view_list.split(',')
    name_abbr_list = []
    for child in origin_list:
        for view in main_view_list:
            if view['base_view_name'] == child:
                name_abbr_list.append(view['base_view_name_abbr'])
    print('name_abbr_list:', name_abbr_list)
    # 获取当前分类下新的name
    name_abbr = this_page.locator('li.selected div~ul .abcdefg7').all()
    new_need_name_list = []
    for name in name_abbr:
        t_name = name.inner_text().split('--')[1]
        if t_name in name_abbr_list:
            print('new name:', t_name)
            name.click(button='right')
            page.locator('#dataCM').get_by_text('刷新该节点').click()
            page.locator('#progressBar').wait_for(state='hidden')
            input_value = this_page.locator('#suggestFrom #compName').input_value()
            new_need_name_list.append(input_value)
            name.click()
            page.locator('#progressBar').wait_for(state='hidden')
    print('new_need_name_list:', new_need_name_list)
    new_need_name_list_str = ','.join(new_need_name_list)
    print('new_need_name_list_str:', new_need_name_list_str)
    return new_need_name_list_str


def refresh_classify_ul(page, this_page, p, is_refresh=False):
    if is_refresh:
        # page.locator('.formBar').get_by_text('取消').click()
        this_page.locator('li.selected div').get_by_text('功能分类').click(button='right')
        page.locator('#dataCM').get_by_text('刷新该节点').click()


def open_add_view(page, this_page, p, classify, close_old=False):
    if close_old:
        this_page.locator('li.selected div~ul .abcdefg6').get_by_text('设计的操作界面').click(button='right')
        page.locator('#dataCM').get_by_text('刷新该节点').click()
        this_page.locator('li.selected div~ul .abcdefg6').get_by_text('设计的操作界面').click(button='right')
        page.locator('#dataCM').locator('#新增').click()
        return
    #     page.locator('.formBar').get_by_text('取消').click()
    #     this_page.locator('li.selected div').get_by_text('功能分类').click(button='right')
    #     page.locator('#dataCM').get_by_text('刷新该节点').click()
    classify_link = this_page.locator('li.selected ul li div.abcdefg5').get_by_text(classify)
    # classify_son_link = classify_link.get_by_text(classify)
    classify_link.click()

    this_page.locator('li.selected div~ul .abcdefg6').get_by_text('设计的操作界面').click()
    # input('==')
    # this_page.locator('li.selected div~ul .abcdefg6').get_by_text('设计的操作界面').click(button='right')
    # page.locator('#dataCM').locator('#新增').click()
    # page.wait_for_timeout(500)
    # input('~~~~')
    print('已打开设计的操作界面')

    return True


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


def add_entrance_view(page, this_page, dialog, abbr, name, origin_children_view_list, current_classify):
    view_name = '密码服务中间件::' + name
    view_name_abbr = abbr
    it_unit_abbr = publish_params['it_unit_abbr']['value']
    it_unit_name = publish_params['it_unit_name']['value']
    # 填写参数，批量增加
    # dialog.locator('input[name="compAppType_ENUMREMARK"]').click()
    dialog.locator('#compAppType~input[name="compAppType_ENUMREMARK"] >> visible=true').click()
    page.wait_for_timeout(300)
    page.locator('#suggest').get_by_text('操作入口界面').click()
    dialog.locator('#compName').fill(view_name)
    dialog.locator('#serviceAddr').fill(view_name_abbr)
    common_operate.dialog_search(page, it_unit_abbr, '界面目录管理界面.compAttrValue5')  # 设计界面组件别名
    common_operate.dialog_search(page, it_unit_name, '界面目录管理界面.compMiniAppLevel')  # 设计界面组件

    if bool(origin_children_view_list):
        dialog.locator('#suggestFrom div p a').get_by_text('管理的数据界面').click()
        common_operate.dialog_transfer_search(page, origin_children_view_list)

    # 新增一条
    page.locator('.formBar').get_by_text('增加').click()
    page.locator('#progressBar').wait_for(state='hidden')

    error_box = page.locator('.formMsgError')
    error_box_is_visible = error_box.is_visible()
    print('error_box_is_visible：', error_box_is_visible)
    if error_box_is_visible:
        print('报错', error_box.inner_text())
        error_box.wait_for(state='hidden')
        page.locator('.formBar').get_by_text('取消').click()
    else:
        page.locator('.formBar').get_by_text('取消').click()
        closes = page.locator('.formBar').get_by_text('闭').all()
        for close in closes:
            close.click()


def __main__run():
    page, this_page, p = login.get_login()
    current_classify = entrance_view_list[0].get('classify').split(':')[0]
    business_name = publish_params['business_name']['value']
    project_model = publish_params['project_model']['value']
    reach_classify_end = reach_classify(page, this_page, p, business_name, project_model)
    # open_add_view(page, this_page, p, current_classify)
    if reach_classify_end:
        for index, entrance in enumerate(entrance_view_list):
            index += 1
            name = entrance.get('base_view_name')
            abbr = entrance.get('base_view_name_abbr')
            print(f'开始：：{index}--{abbr}')
            classify = entrance.get('classify').split(':')[0]
            origin_children_view_list = entrance.get('origin_children_view_list')
            old_classify = current_classify
            refresh_classify_ul(page, this_page, p, True)
            open_add_view(page, this_page, p, current_classify, False)
            new_need_name_list = get_new_view_name(page, this_page, p, origin_children_view_list)
            open_add_view(page, this_page, p, current_classify, True)
            if current_classify != classify:
                current_classify = classify
                refresh_classify_ul(page, this_page, p, True)
            page.wait_for_timeout(300)
            dialog = page.locator('.dialog >> visible=true')
            add_entrance_view(page, this_page, dialog, abbr, name, new_need_name_list, current_classify)
            print(f'结束：：{index}--{abbr}')
            # input('111')


__main__run()
end_time = time.time()
print(f"创建入口。运行时间: {end_time - start_time}秒")
