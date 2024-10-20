#!/usr/bin/python3
# coding=utf-8
###################################################################
#           ____     _     _ __  __                 
#          / __/__  (_)___(_) /_/ /  ___  ___  ___ _
#         _\ \/ _ \/ / __/ / __/ /__/ _ \/ _ \/ _ `/
#        /___/ .__/_/_/ /_/\__/____/\___/_//_/\_, / 
#           /_/                              /___/  
# Copyright (c) 2024 Chongqing Spiritlong Technology Co., Ltd.
# All rights reserved.  
# @author	arthuryang
# @brief	字符串相关工具
#
###################################################################  

import	datetime
import	re
import	os

## 判断一个字符串是不是浮点数
def is_float(s):
	try:
		float(s)
		# 浮点数
		return True
	except ValueError:
		pass

# 调试/测试代码
if __name__ == '__main__':
	pass

