# 获取需要复制的原视图列表
import json
from base import CopiedBase
from base import login
# 读取 JSON 文件
with open('data.json', 'r', encoding='utf-8') as file:
    data = json.load(file)


def get_login():
    login_url = 'http://work.paytunnel.cn:19060/gms-v4/selectSystem?key=developmentServerTest121'
    login_username = 'lwl'
    login_password = 'lwl123'
    page, this_page = login.login(login_url, login_username, login_password)
    return page, this_page


def get_need_copy_views(_data):
    page, this_page = get_login()
    for view in _data:
        if view['meta']:
            base_view_name_abbr = view['meta']['title']
            base_view_name = view['meta']['tblAlias']
            # base_view_name 只对不包含有'二级菜单-'的视图操作
            if '二级菜单' not in base_view_name:
                if '入口' not in base_view_name:
                    factory, object_name, db_name = CopiedBase.get_copied_base_message(page, this_page, base_view_name)
                    print(base_view_name_abbr + ':' + '基础开发方案 factory:', factory, '基础数据对象 objectName:', object_name, '对应的数据库表:', db_name)
                    page.locator('#taskSetting').click()
        if view['children']:
            get_need_copy_views(view['children'])
            return
    return


get_need_copy_views(data)
