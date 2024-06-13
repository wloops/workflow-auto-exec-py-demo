# 点击右侧放大镜(属性lookupgroup=factory)选择
def click_next_button(page, dialog, next_button, name):
    dblclick_tb(page, dialog, name)
    next_button.click()
    page.locator('#progressBar').wait_for(state='hidden')
    page.wait_for_timeout(500)
    new_next_button = dialog.locator('.panelBar .next[href="javascript:;"]').get_by_text('下一页')
    if next_button.is_visible():
        click_next_button(page, dialog, new_next_button, name)
    else:
        dblclick_tb(page, dialog, name)


def dblclick_tb(page, dialog, name):
    page.locator('#progressBar').wait_for(state='hidden')
    page.wait_for_timeout(500)
    table = dialog.locator('#anyid >> visible=true')
    tds = table.locator('tbody tr td').get_by_text(name, exact=True).first
    tds.dblclick()
    # tr_rows = table.locator('.tbody tr').all()  # 定位到表格的行
    # table_rows_text = []
    # model_list = []
    # for row in tr_rows:
    #     cells = row.locator('td').all()  # 在每一行中定位到单元格
    #     cell_values = []
    #     for i, cell in enumerate(cells):
    #         print(i, cell)
    #         cell_values.append(cell.locator('div').inner_text())
    #         if i == 1:
    #             model_list.append(cell.locator('div').inner_text())
    #
    #     # cell_values = [cell.inner_text() for cell in cells]  # 获取每个单元格的文本
    #     # print(cell_values)  # 在终端中打印单元格的值
    #     table_rows_text.append(cell_values)
    # print('table_rows_text', table_rows_text)
    # print('model_list', model_list)

def dialog_search(page, name, lookup_group='', model='Enter'):
    if lookup_group != '':
        page.locator('.pageFormContent  p').locator('a[lookupgroup="' + lookup_group + '"]').click()
        page.locator('#progressBar').wait_for(state='hidden')
    dialog = page.locator('.dialog >> visible=true')
    dialog_input = dialog.locator('.pageHeader p input')
    page.locator('.dialog .pageHeader .subBar .buttonContent button').get_by_text('重置').click()
    dialog_input.fill(name)
    page.wait_for_timeout(500)
    if model == 'Enter':
        dialog_input.press('Enter')
        dblclick_tb(page, dialog, name)
    else:
        next_button = dialog.locator('.panelBar .next[href="javascript:;"]').get_by_text('下一页')
        if next_button.is_visible():
            print('多页')
            click_next_button(page, dialog, next_button, name)


# 穿梭框选择
def dialog_transfer_search(page, name_list):
    dialog = page.locator('.dialog >> visible=true')
    dialog.locator('#formButton').get_by_text('全选右边').click()
    dialog.locator('#formButton button').nth(3).click()
    name_list = name_list.split(',')
    for name in name_list:
        dialog.locator('#leftSelDiv').get_by_text(name).dblclick()
    dialog.locator('.subBar').get_by_text('确定').click()
