import json

# 读取 JSON 文件
with open('entrance_view_list.json', 'r', encoding='utf-8') as file:
    entrance_view_list = json.load(file)
with open('publish.json', 'r', encoding='utf-8') as file:
    publish_params = json.load(file)


# def __main__run():
    #功能分类方式批量创建时，进入操作路径
    # open_operate_path()
    #循环创建每个功能分类下的入口界面
    # for entry in entrance_view_list:
    #创建入口时：选所属的界面

# __main__run()
