

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
# @brief	excel工具集
#
###################################################################  

import	platform

# excel
from SpiritLong_excel.excel import	cell_font
from SpiritLong_excel.excel import	cell_fill
from SpiritLong_excel.excel import	cell_border
from SpiritLong_excel.excel import	alignment_center
from SpiritLong_excel.excel import	alignment_left
from SpiritLong_excel.excel import	alignment_right
from SpiritLong_excel.excel import	style_title
from SpiritLong_excel.excel import	open_xlsx
from SpiritLong_excel.excel import	set_cell
from SpiritLong_excel.excel import	get_records_with_title
from SpiritLong_excel.excel import	adjust_column_width
from SpiritLong_excel.excel import	adjust_all_column_width
from SpiritLong_excel.excel import	cell_coordinate
from SpiritLong_excel.excel import	cell_code
from SpiritLong_excel.excel import	records_to_excel
from SpiritLong_excel.excel import	csv_save_as_xlsx
if platform.system()=="Windows":
	from SpiritLong_excel.excel import xls_save_as_xlsx
