#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""通过argparse获取python脚本的使用方法，传递位置变量"""
'''
import argparse

# 这行代码就生成了一个命令行参数的对象，之后就可以给对象添加一些参数属性，最后只需要从属性中提取传入的参数进行使用即可
parser = argparse.ArgumentParser(description='传递时间参数')
parser.add_argument('--start-time', '--start-time', help='start_time 开始时间，必要参数', required=True)
parser.add_argument('--end-time', '--end-time', help='end_time 截止时间，必要参数', required=True)
args = parser.parse_args()

def print_time(start_time,end_time):
    print(start_time,end_time)

if __name__ == '__main__':
    print_time(args.start_time,args.end_time)
'''

"""ConfigParser模块配置文件读取参数"""

'''
import ConfigParser

conf = ConfigParser.ConfigParser()
# read file and get information of mysql
conf_path = os.path.dirname(os.path.realpath(__file__)) + "/" + "backup_mysql.ini"
conf.read(conf_path)
host=conf.get('mysql','host')
port=conf.getint('mysql','port')
user=conf.get('mysql','user')
password=conf.get('mysql','password')
database=conf.get('mysql','database')
'''

"""定义class类"""
'''

class GetPrintTime:
    def __init__(self,start_time,end_time):
        self.start_time = start_time
        self.end_time = end_time

    def print_time(self):
        print("开始时间",self.start_time,"结束时间",self.end_time)


if __name__ == '__main__':
    p = GetPrintTime('2020','2021')
    p.print_time()
'''


