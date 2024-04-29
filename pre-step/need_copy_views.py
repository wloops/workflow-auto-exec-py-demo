# 获取需要复制的原视图列表
import json
import time
from base import copied_base
from base import login

# 读取 JSON 文件
with open('data.json', 'r', encoding='utf-8') as file:
    data = json.load(file)


def get_login():
    login_url = 'http://work.paytunnel.cn:19060/gms-v4/selectSystem?key=developmentServerTest121'
    login_username = 'lwl'
    login_password = 'lwl123'
    headless = False
    page, this_page, p = login.login(login_url, login_username, login_password, headless)
    return page, this_page, p


# def does_not_contain_any_substrings(main_string, substrings):
#     return all(substring not in main_string for substring in substrings)

start_time = time.time()
all_views_count = 0
main_view_count = 0
entrance_views_count = 0
all_rank_list = []
main_view_list = []
entrance_view_list = []


def get_need_copy_views(_data, page, this_page, p, classify=''):
    global main_view_count
    global entrance_views_count
    global main_view_list
    for view in _data:
        if view['meta']:
            base_view_name_abbr = view['meta']['title']
            base_view_name = view['meta']['tblAlias']
            if view['meta']['resId'] != 990 and base_view_name != 'viewDef':
                factory, object_name, db_name, view_button, view_record_select_group, view_button_group, operate_button = (
                    copied_base.get_copied_base_message(page, this_page, base_view_name))
                main_view_list.append({
                    'base_view_name': base_view_name,
                    'base_view_name_abbr': base_view_name_abbr,
                    'factory': factory,
                    'object_name': object_name,
                    'db_name': db_name,
                    'classify': classify if classify != '' else '',
                    'view_record_select_group': view_record_select_group,
                    'view_button_group': view_button_group,
                    'view_button': view_button,
                    'operate_button': operate_button
                })
                print(base_view_name_abbr + ':' + '基础开发方案 factory:', factory, '基础数据对象 objectName:',
                      object_name, '对应的数据库表:', db_name, '界面-缺省操作:', view_button, '界面-记录操作:', view_record_select_group,
                      '界面操作：', view_button_group, '操作按钮：', operate_button)
                main_view_count += 1
                # p.stop()
                page.locator('#taskSetting').click()
                page.wait_for_timeout(1000)
            elif view['meta']['resId'] == 990:
                entrance_views_count += 1
                origin_children_view_list, operate_button = copied_base.get_entrance_view_base_message(page, this_page, base_view_name)
                page.locator('#taskSetting').click()
                page.wait_for_timeout(1000)
                entrance_view_list.append({
                    'base_view_name': base_view_name,
                    'base_view_name_abbr': base_view_name_abbr,
                    'classify': classify if classify != '' else '',
                    'origin_children_view_list': origin_children_view_list,
                    'operate_button': operate_button
                })
                print('[入口菜单项]', base_view_name_abbr, base_view_name, '子界面列表：', origin_children_view_list,
                      '入口的按钮：', operate_button)
                if not view['children']:
                    # classify_join_entrance = classify + '/' + base_view_name_abbr + ':' + base_view_name
                    get_need_copy_views(view['children'], page, this_page, p)
        if view['children']:
            # classify_join_entrance = classify + '/' + view['meta']['title'] + ':' + view['meta']['tblAlias']
            get_need_copy_views(view['children'], page, this_page, p, classify)
    return


def __main__run(origin):
    page, this_page, p = get_login()
    for _data in origin:
        classify = _data['meta']['title'] + ':' + _data['meta']['tblAlias']
        get_need_copy_views(_data['children'], page, this_page, p, classify)
        # print(_data)


__main__run(data)

print('main_view_list:', main_view_list)
print('entrance_view_list:', entrance_view_list)

print('main界面数 views_count:', main_view_count)
print('入口数 views_count:', entrance_views_count)
all_views_count = main_view_count + entrance_views_count
print('总数 views_count:', all_views_count)
end_time = time.time()
print(f"获取需要复制的原数据对象的列表和关键属性。运行时间: {end_time - start_time}秒")
# 使用json.dump()将数据写入文件，并设置缩进和排序参数
with open('main_view_list.json', 'w', encoding='utf-8') as file:
    json.dump(main_view_list, file, ensure_ascii=False, indent=4, sort_keys=True)

with open('entrance_view_list.json', 'w', encoding='utf-8') as file:
    json.dump(entrance_view_list, file, ensure_ascii=False, indent=4, sort_keys=True)
