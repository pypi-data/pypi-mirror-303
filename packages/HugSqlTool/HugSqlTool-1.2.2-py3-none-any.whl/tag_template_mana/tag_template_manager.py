# encoding=utf-8
import os
from service_engine import service_manager as ServiceManager


def deal_item_path():
    # 处理下基础路径
    current_file_path = os.path.abspath(__file__)
    # 获取当前Python文件的父路径
    parent_directory = os.path.dirname(current_file_path)
    # 获取父路径的父路径
    grandparent_directory = os.path.dirname(parent_directory)
    os.chdir(grandparent_directory)


if __name__ == '__main__':
    deal_item_path()
    print('=================================================================')
    print('【帮助文档】\n[当前项目根路径的绝对路径]：{} \n[跳]：请使用回车键'.format(os.getcwd()))
    print('=================================================================')
    ServiceManager.start_constructor_tag_template()
