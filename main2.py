
from base import login

login_url = 'http://work.paytunnel.cn:19060/gms-v4/selectSystem?key=developmentServerTest121'
login_username = 'lwl'
login_password = 'lwl123'
page, this_page = login.login(login_url, login_username, login_password)

this_page.locator('.muenButtonContent a[title="编辑本视图"]').click()

origin_view_name = '平台级的密钥操作-审批申请界面'

this_page.locator('td #viewName').fill(origin_view_name)
this_page.locator('.subBar .buttonContent').get_by_text('精确查询').click()
page.wait_for_timeout(2000)
tr_rows = this_page.locator('.gridScroller .sortable #anyid tr').all()  # 定位到表格的行
print(len(tr_rows))
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

# form_inputs = this_page.locator('.suggestFrom')  # 定位到表格的行
input_factory = this_page.locator('.pageFormContent  p').locator('#factory_QUERYREMARK').click()
alais = this_page.locator('//*[@id="alais"]').all()
print(len(alais))
# print(input_factory.input_value())
page.wait_for_timeout(500)
suggest_li = page.locator('//*[@id="suggest"]/ul/li').get_by_text('软件开发解决方案').click()
input('暂停---')

# 点击右侧放大镜(属性lookupgroup=factory)选择
this_page.locator('.pageFormContent  p').locator('a[lookupgroup="factory"]').click()

page.wait_for_timeout(1000)
# 等待弹出层出现
popup_selector = ".dialog"  # 根据弹出层的类名或其他特征修改选择器
this_page.waitForSelector(popup_selector)
dialog = this_page.locator('.dialog').all()
print('dialog', len(dialog))
# this_page.locator('close').click()
# dialog_search_input = this_page.locator('.searchContent table tbody tr td p input[name="productType_REMARKFLD"]')
# print('dialog_search_input', dialog_search_input.input_value())
# dialog_search_input.clear()
# this_page.locator('.subBar').get_by_text('重置').click()

tr_rows2 = this_page.locator('.pageContent .gridScroller .sortable tr').all()  # 定位到表格的行
print(len(tr_rows2))
table_rows_text2 = []
for row in tr_rows2:
    cells = row.locator('td').all()  # 在每一行中定位到单元格
    cell_values = []
    for cell in cells:
        if cell.get_attribute('title'):
            cell_values.append(cell.locator('div').inner_text())

    # cell_values = [cell.inner_text() for cell in cells]  # 获取每个单元格的文本
    print(cell_values)  # 在终端中打印单元格的值
    table_rows_text2.append(cell_values)

print('table_rows_text2', table_rows_text2)

input('暂停---')

# # 关闭浏览器
# browser.close()
# # 关闭 playwright driver 进程
# p.stop()
