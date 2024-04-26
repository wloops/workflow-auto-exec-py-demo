# 点击右侧放大镜(属性lookupgroup=factory)选择
def dialog_search(page, name, lookupgroup=''):
    if lookupgroup != '':
        page.locator('.pageFormContent  p').locator('a[lookupgroup="'+lookupgroup+'"]').click()
    dialog = page.locator('.dialog >> visible=true')
    dialog_input = dialog.locator('.pageHeader p input')
    dialog_input.fill(name)
    dialog_input.press('Enter')
    table = dialog.locator('#anyid >> visible=true')
    tds = table.locator('tbody tr td').get_by_text(name, exact=True).first
    tds.dblclick()


# 穿梭框选择
def dialog_transfer_search(page, name_list):
    dialog = page.locator('.dialog >> visible=true')
    dialog.locator('#formButton').get_by_text('全选右边').click()
    dialog.locator('#formButton button').nth(3).click()
    name_list = name_list.split(',')
    for name in name_list:
        dialog.locator('#leftSelDiv').get_by_text(name).dblclick()
    dialog.locator('.subBar').get_by_text('确定').click()
