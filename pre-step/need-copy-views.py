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
    page, this_page, p = login.login(login_url, login_username, login_password)
    return page, this_page, p


# def does_not_contain_any_substrings(main_string, substrings):
#     return all(substring not in main_string for substring in substrings)


all_views_count = 0
main_view_count = 0
entrance_views_count = 0
all_rank_list = []
main_view_list = []
entrance_view_list = []


def get_need_copy_views(_data, page, this_page, p):
    global main_view_count
    global entrance_views_count
    global main_view_list
    for view in _data:
        if view['meta']:
            base_view_name_abbr = view['meta']['title']
            base_view_name = view['meta']['tblAlias']
            if view['meta']['resId'] != 990 and base_view_name != 'viewDef':
                factory, object_name, db_name = CopiedBase.get_copied_base_message(page, this_page, base_view_name)
                main_view_list.append({
                    'base_view_name': base_view_name,
                    'base_view_name_abbr': base_view_name_abbr,
                    'factory': factory,
                    'object_name': object_name,
                    'db_name': db_name
                })
                print(base_view_name_abbr + ':' + '基础开发方案 factory:', factory, '基础数据对象 objectName:',
                      object_name, '对应的数据库表:', db_name)
                main_view_count += 1
                # p.stop()
                page.locator('#taskSetting').click()
                page.wait_for_timeout(1000)
            elif view['meta']['resId'] == 990:
                print('[入口菜单项]', base_view_name_abbr, base_view_name)
                entrance_views_count += 1
                entrance_view_list.append({
                    'base_view_name': base_view_name,
                    'base_view_name_abbr': base_view_name_abbr
                })
                if not view['children']:
                    get_need_copy_views(view['children'], page, this_page, p)
        if view['children']:
            get_need_copy_views(view['children'], page, this_page, p)
    return


def get_need_copy_views_one(origin):
    page, this_page, p = get_login()
    for _data in origin:
        get_need_copy_views(_data['children'], page, this_page, p)
        # print(_data)


get_need_copy_views_one(data)

print('main_view_list:', main_view_list)
print('entrance_view_list:', entrance_view_list)

print('main界面数 views_count:', main_view_count)
print('入口数 views_count:', entrance_views_count)
all_views_count = main_view_count + entrance_views_count
print('总数 views_count:', all_views_count)
