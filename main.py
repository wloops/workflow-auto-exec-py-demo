from base import copied_base

#  获取基础开发方案
base_view_name = '密码服务端口模板-HSM无关界面-部署'
base_view_name_abbr = '低性能端口模板'
# CopiedBase.get_copied_base_message(base_view_name)
factory, object_name, db_name = copied_base.get_copied_base_message(base_view_name)
print('基础开发方案 factory:', factory, '基础数据对象 object_name:', object_name, '对应的数据库表:', db_name)


# 发布：参数
