# 被复制的基础视图

from base import login


def start_step(page, this_page, view_name):
    origin_view_name = view_name
    this_page.locator('#intermenu .muenBtn').get_by_text('编辑本视图').click()
    page.locator('#progressBar').wait_for(state='hidden')
    this_page.locator('td #viewName').fill(origin_view_name)
    this_page.locator('.subBar .buttonContent').get_by_text('精确查询').click()
    page.locator('#progressBar').wait_for(state='hidden')
    tr_rows = this_page.locator('.gridScroller .sortable tr').all()  # 定位到表格的行
    table_rows_text = []
    for row in tr_rows:
        cells = row.locator('td').all()  # 在每一行中定位到单元格
        cell_values = []
        for cell in cells:
            if cell.get_attribute('title'):
                cell_values.append(cell.locator('div').inner_text())

        # cell_values = [cell.inner_text() for cell in cells]  # 获取每个单元格的文本
        # print(cell_values)  # 在终端中打印单元格的值
        table_rows_text.append(cell_values)

    # print('table_rows_text', table_rows_text)
    # input('选中一行进行下一步操作：')
    # print(table_rows_text[0])
    # 点击该行进行操作
    tr_rows[0].click()


def get_copied_base_message(page, this_page, view_name):
    start_step(page, this_page, view_name)
    this_page.locator('#dataCM td a').get_by_text('设计来源对象').click()
    page.locator('#progressBar').wait_for(state='hidden')
    this_page.locator('.displayFirstClass').click()
    page.locator('#progressBar').wait_for(state='hidden')

    # form_inputs = this_page.locator('.suggestFrom')  # 定位到表格的行
    factory = this_page.locator('#productType').input_value()
    object_name = this_page.locator('#objectName').input_value()
    db_name = this_page.locator('#mngObject').input_value()

    page.locator('.navTab-tab li[tabid=编辑本视图]').click()
    page.locator('#progressBar').wait_for(state='hidden')
    this_page.locator('#dataCM td a').get_by_text('设计来源界面').click()
    page.locator('#progressBar').wait_for(state='hidden')
    this_page.locator('.displayFirstClass').click()
    page.locator('#progressBar').wait_for(state='hidden')
    view_button = this_page.locator('#compAttrValue8').input_value()
    view_record_select_group = this_page.locator('#compAttrValue13').input_value()
    view_button_group = this_page.locator('#compAttrValue14').input_value()

    page.locator('.abcdefg2').get_by_text('操作按钮-按时间排序').click()
    page.locator('#progressBar').wait_for(state='hidden')
    buttons = this_page.locator('.abcdefg3').all()
    operate_button = []
    for button in buttons:
        operate_button.append(button.inner_text())
    print('操作按钮-按时间排序：', operate_button)
    return factory, object_name, db_name, view_button, view_record_select_group, view_button_group, operate_button


def get_entrance_view_base_message(page, this_page, view_name):
    start_step(page, this_page, view_name)
    this_page.locator('#dataCM td a').get_by_text('设计来源界面').click()

    this_page.locator('.displayFirstClass').click()
    page.locator('#progressBar').wait_for(state='hidden')
    origin_children_view_list = this_page.locator('#compAttrValue11').input_value()
    page.locator('.abcdefg2').get_by_text('操作按钮-按时间排序').click()
    page.locator('#progressBar').wait_for(state='hidden')
    buttons = this_page.locator('.abcdefg3').all()
    operate_button = []
    for button in buttons:
        operate_button.append(button.inner_text())
    print('操作按钮-按时间排序：', operate_button)

    return origin_children_view_list, operate_button
