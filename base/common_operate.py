def dblclick_tb(page, dialog, name):
    page.locator('#progressBar').wait_for(state='hidden')
    page.wait_for_timeout(500)
    table = dialog.locator('#anyid >> visible=true')
    tds = table.locator('tbody tr td').get_by_text(name, exact=True).first
    tds.dblclick()


# 点击右侧放大镜(属性lookupgroup=factory)选择
def dialog_search(page, name, lookup_group=''):
    if lookup_group != '':
        page.locator('.pageFormContent  p').locator('a[lookupgroup="' + lookup_group + '"]').click()
        page.locator('#progressBar').wait_for(state='hidden')
    dialog = page.locator('.dialog >> visible=true')
    dialog_input = dialog.locator('.pageHeader p input')
    page.locator('.dialog .pageHeader .subBar .buttonContent button').get_by_text('重置').click()
    dialog_input.fill(name)
    page.wait_for_timeout(500)
    dialog_input.press('Enter')
    dblclick_tb(page, dialog, name)


# 穿梭框选择
def dialog_transfer_search(page, name_list):
    dialog = page.locator('.dialog >> visible=true')
    dialog.locator('#formButton').get_by_text('全选右边').click()
    dialog.locator('#formButton button').nth(3).click()
    name_list = name_list.split(',')
    for name in name_list:
        dialog.locator('#leftSelDiv').get_by_text(name).dblclick()
    dialog.locator('.subBar').get_by_text('确定').click()
