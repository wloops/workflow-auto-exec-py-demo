# 被复制的基础视图

from base import login


def get_copied_base_message(page, this_page, view_name):
    origin_view_name = view_name

    this_page.locator('td #viewName').fill(origin_view_name)
    this_page.locator('.subBar .buttonContent').get_by_text('精确查询').click()
    page.wait_for_timeout(2000)
    tr_rows = this_page.locator('.gridScroller .sortable tr').all()  # 定位到表格的行
    table_rows_text = []
    for row in tr_rows:
        cells = row.locator('td').all()  # 在每一行中定位到单元格
        cell_values = []
        for cell in cells:
            if cell.get_attribute('title'):
                cell_values.append(cell.locator('div').inner_text())

        # cell_values = [cell.inner_text() for cell in cells]  # 获取每个单元格的文本
        print(cell_values)  # 在终端中打印单元格的值
        table_rows_text.append(cell_values)

    print('table_rows_text', table_rows_text)
    # input('选中一行进行下一步操作：')
    print(table_rows_text[0])
    # 点击该行进行操作
    tr_rows[0].click()
    this_page.locator('#dataCM td a').get_by_text('设计来源对象').click()

    this_page.locator('.displayFirstClass').click()

    # this_page.locator('.displayFirstClass').click(button="right")
    # page.wait_for_timeout(500)
    # page.locator('#设计对象组件').hover()
    # page.wait_for_timeout(300)
    # page.locator('#从基础对象创建本对象-复制数据字典并创建界面').click()
    # page.locator('.formBar').get_by_text('确定').click()
    # page.wait_for_timeout(300)
    # page.locator('.formBar').get_by_text('确定').click()
    # page.wait_for_timeout(100)
    # page.locator('.toolBar').get_by_text('确定').click()

    # form_inputs = this_page.locator('.suggestFrom')  # 定位到表格的行
    factory = this_page.locator('//*[@id="factory"]').input_value()
    object_name = this_page.locator('//*[@id="objectName"]').input_value()
    db_name = this_page.locator('//*[@id="mngObject"]').input_value()

    return factory, object_name, db_name
    input('暂停---')
#
