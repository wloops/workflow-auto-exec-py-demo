import json
from base import login, common_operate

with open('publish.json', 'r', encoding='utf-8') as file:
    publish_params = json.load(file)
with open('main_view_list.json', 'r', encoding='utf-8') as file:
    main_view_list = json.load(file)


def reach_path(page, this_page):
    page.locator('#开发工作管理二级菜单组').click()
    page.locator('#功能组件设计管理二级菜单组').click()
    page.locator('#界面设计入口界面').click()
    page.locator('#界面设计入口界面~ul a[title="配管界面目录"]').click()
    page.locator('#progressBar').wait_for(state='hidden')


def find_element_index(lst, element):
    try:
        return lst.index(element)
    except ValueError:
        return -1  # 或者你可以返回None，表示元素不存在于列表中


def search_view(page, this_page, origin_view_name, model_name):
    this_page.locator('.subBar .buttonContent').get_by_text('重置').click()
    this_page.locator('td #compName').fill(origin_view_name)
    this_page.locator('.subBar .buttonContent').get_by_text('精确查询').click()
    page.locator('#progressBar').wait_for(state='hidden')
    tr_rows = this_page.locator('.gridScroller .sortable tr').all()  # 定位到表格的行
    table_rows_text = []
    model_list = []
    for row in tr_rows:
        cells = row.locator('td').all()  # 在每一行中定位到单元格
        cell_values = []
        for i, cell in enumerate(cells):
            print(i, cell)
            if cell.get_attribute('title'):
                cell_values.append(cell.locator('div').inner_text())
                if i == 1:
                    model_list.append(cell.locator('div').inner_text())

        # cell_values = [cell.inner_text() for cell in cells]  # 获取每个单元格的文本
        # print(cell_values)  # 在终端中打印单元格的值
        table_rows_text.append(cell_values)

    print('table_rows_text', table_rows_text)
    print('model_list', model_list)
    row_index = find_element_index(model_list, model_name)
    print('row_index', row_index)
    if row_index == -1:
        print('未找到该型号的记录。即将复制一份。。。')
        this_page.locator('#isMyProductItems_ENUMREMARK').click()
        page.locator('#progressBar').wait_for(state='hidden')
        page.locator('#suggest').get_by_text('是').click()
        this_page.locator('.subBar .buttonContent').get_by_text('精确查询').click()
        page.locator('#progressBar').wait_for(state='hidden')
        tr_rows = this_page.locator('.gridScroller .sortable tr').all()  # 定位到表格的行
        tr_rows[0].click()
        copy_view_button(page, this_page)
        return
    # else:
    #     tr_rows[row_index].click()


def copy_view_button(page, this_page):
    this_page.locator('#dataCM td a').get_by_text('记录管理').click()
    page.locator('#progressBar').wait_for(state='hidden')
    page.locator('#groupingMenu').get_by_text('复制', exact=True).click()
    fill_inputs(page, this_page)


def fill_inputs(page, this_page):
    model_name = publish_params['project_model']['value']  # 型号
    business_type = publish_params['business_type']['value']  # 设计界面业务类型
    business_name = publish_params['business_name']['value']  # 设计界面的业务
    it_unit_type = publish_params['it_unit_type']['value']  # 设计界面组件类型
    it_unit_abbr = publish_params['it_unit_abbr']['value']  # 设计界面组件别名
    it_unit_name = publish_params['it_unit_name']['value']  # 设计界面的IT组件

    common_operate.dialog_search(page, model_name, 'srlID')
    # 设计界面业务类型
    page.locator('input[name="desObjBusiCate_ENUMREMARK"]').click()
    page.locator('#progressBar').wait_for(state='hidden')
    page.locator('#suggest').get_by_text(business_type).click()
    common_operate.dialog_search(page, business_name, 'desObjBusi')
    common_operate.dialog_search(page, it_unit_type, 'compAppLevel')
    common_operate.dialog_search(page, it_unit_abbr, 'compAttrValue5')
    common_operate.dialog_search(page, it_unit_name, 'compMiniAppLevel')
    # 本产品开发 --》否
    page.locator('#suggestFrom input[name=\"isMyProductItems_ENUMREMARK\"]').click()
    page.locator('#progressBar').wait_for(state='hidden')
    page.locator('#suggest').get_by_text('否').click()

    # 新增一条
    # page.locator('.formBar').get_by_text('增加').click()
    # page.locator('#progressBar').wait_for(state='hidden')

    # 关闭所有弹窗
    dialog_tabs = page.locator('#taskbar .taskbarContent')

    if dialog_tabs.is_visible():
        # 右键点击 关闭所有弹出窗口
        dialog_tabs.click(button='right')
        page.locator('#dialogCM li[rel="closeAll"]').click()

    # input('====')


def __main_run():
    page, this_page, p = login.get_login()
    reach_path(page, this_page)
    loop_list = []
    for view in main_view_list:
        view_button_group = view.get('view_button_group')
        view_record_select_group = view.get('view_record_select_group')
        loop_list_string = ''
        if view_button_group and view_record_select_group:
            loop_list_string = view_button_group + ',' + view_record_select_group
        # print('loop_list_string:', loop_list_string)
        if loop_list_string:
            for name in loop_list_string.split(','):
                loop_list.append(name)
    loop_set_list = list(set(loop_list))
    print('loop_set_list:', loop_set_list)

    for view_name in loop_set_list:
        origin_view_name = view_name
        model_name = publish_params['project_model']['value']
        search_view(page, this_page, origin_view_name, model_name)
    input('###')


__main_run()
