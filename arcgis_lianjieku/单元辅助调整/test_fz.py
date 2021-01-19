# coding:utf-8
import arcpy
import sys
import os
import time

reload(sys)
sys.setdefaultencoding('utf-8')
arcpy.env.overwriteOutput = True

# 7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
# 单元元素名称
ys = 'Cd'
# ys = arcpy.GetParameterAsText(4)
# 中间数据存放地理数据库
work = r"C:\Users\Administrator\Desktop\source\work.gdb"
# work = arcpy.GetParameterAsText(0)
# 输出的地理数据库
out_path = r'C:\Users\Administrator\Desktop\source\T调整后2018.gdb'
# out_path = arcpy.GetParameterAsText(1)
# 原始单元数据
ysdy = r"C:\Users\Administrator\Desktop\source\T调整前2018.gdb\评价单元_Cd_1"
# ysdy = arcpy.GetParameterAsText(2)
# 农产品数据
ncpsj = r'C:\Users\Administrator\Desktop\source\T农产品数据2020.gdb\QTN2019_2020不重复'
# ncpsj = arcpy.GetParameterAsText(3)
# 单元筛选条件
dy_expression = '备注4 IS NULL'
# dy_expression = arcpy.GetParameterAsText(5)
# 农产品筛选条件
ncp_expression = 'NCPLX IS NOT NULL'
# ncp_expression = arcpy.GetParameterAsText(6)
# 7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
# arcpy.AddMessage("准备单元数据······················")
print("准备单元数据······················")
# Process: 筛选单元数据
arcpy.Select_analysis(ysdy, os.path.join(work, "ysdy_sxh"), dy_expression)
# 筛选后的单元数据
dy_sxh = os.path.join(work, "ysdy_sxh")

# Process: 添加字段_接受1类count
arcpy.AddField_management(dy_sxh, "count_1", "LONG")

# Process: 添加字段_接受2类count
arcpy.AddField_management(dy_sxh, "count_2", "LONG")

# Process: 添加字段_接受3类count
arcpy.AddField_management(dy_sxh, "count_3", "LONG")

# Process: 添加字段_count_sum
arcpy.AddField_management(dy_sxh, "count_sum", "LONG")
# arcpy.AddMessage("准备农产品数据······················")
print("准备农产品数据······················")
# 筛选农产品数据
arcpy.Select_analysis(ncpsj, os.path.join(work, "ncpsj_sxh"), ncp_expression)

# 筛选后的农产品数据
ncp_sxh = os.path.join(work, "ncpsj_sxh")

fields = arcpy.ListFields(ncp_sxh)
for file1 in fields:
    filed_ = file1.name
    if filed_ not in ['ZHN_CLASS', 'OBJECTID', 'Shape', 'Shape_Length', 'Shape_Area']:
        arcpy.DeleteField_management(ncp_sxh, filed_)
# 农产品一类
arcpy.Select_analysis(ncp_sxh, os.path.join(work, "ncp_sxh_1"), 'ZHN_CLASS = 1')
ncp_sxh_1 = os.path.join(work, "ncp_sxh_1")
# 农产品二类
arcpy.Select_analysis(ncp_sxh, os.path.join(work, "ncp_sxh_2"), 'ZHN_CLASS = 2')
ncp_sxh_2 = os.path.join(work, "ncp_sxh_2")
# 农产品三类
arcpy.Select_analysis(ncp_sxh, os.path.join(work, "ncp_sxh_3"), 'ZHN_CLASS = 3')
ncp_sxh_3 = os.path.join(work, "ncp_sxh_3")
# arcpy.AddMessage("正在处理······················")
print("正在处理························")
# Process: 空间连接_sum
arcpy.SpatialJoin_analysis(dy_sxh, ncp_sxh, os.path.join(work, "连接总"), 'JOIN_ONE_TO_ONE', match_option='INTERSECT')
ljz = os.path.join(work, "连接总")
arcpy.CalculateField_management(ljz, 'count_sum', '!Join_Count!', 'PYTHON_9.3')  # 计算字段
arcpy.DeleteField_management(ljz, "Join_Count;ZHN_CLASS;TARGET_FID")  # 删除字段

# Process: 空间连接_1类
arcpy.SpatialJoin_analysis(ljz, ncp_sxh_1, os.path.join(work, "连接总_1"), 'JOIN_ONE_TO_ONE', match_option='INTERSECT')
ljz_1 = os.path.join(work, "连接总_1")
arcpy.CalculateField_management(ljz_1, 'count_1', '!Join_Count!', 'PYTHON_9.3')  # 计算字段
arcpy.DeleteField_management(ljz_1, "Join_Count;ZHN_CLASS;TARGET_FID")  # 删除字段
# Process: 空间连接_2类
arcpy.SpatialJoin_analysis(ljz_1, ncp_sxh_2, os.path.join(work, "连接总_2"), 'JOIN_ONE_TO_ONE', match_option='INTERSECT')
ljz_2 = os.path.join(work, "连接总_2")
arcpy.CalculateField_management(ljz_2, 'count_2', '!Join_Count!', 'PYTHON_9.3')  # 计算字段
arcpy.DeleteField_management(ljz_2, "Join_Count;ZHN_CLASS;TARGET_FID")  # 删除字段
# Process: 空间连接_3类
arcpy.SpatialJoin_analysis(ljz_2, ncp_sxh_3, os.path.join(work, "连接总_3"), 'JOIN_ONE_TO_ONE', match_option='INTERSECT')
ljz_3 = os.path.join(work, "连接总_3")
arcpy.CalculateField_management(ljz_3, 'count_3', '!Join_Count!', 'PYTHON_9.3')  # 计算字段
arcpy.DeleteField_management(ljz_3, "Join_Count;ZHN_CLASS;TARGET_FID")  # 删除字段

# 添加字段（辅助调整后）
calc_field = "%s_fztz" % ys
arcpy.AddField_management(ljz_3, calc_field, "SHORT")
# arcpy.AddMessage("计算最终结果······················")
print("计算最终结果······················")
# 计算字段
arcpy.CalculateField_management(ljz_3, calc_field,
                                "calc( !%s_CLASS! , !count_1! , !count_2! , !count_3! , !count_sum! )" % ys,
                                "PYTHON_9.3",
                                "# coding:utf-8\\nimport sys\\n\\nreload(sys)\\nsys.setdefaultencoding('utf-8')\\n\\n\\n"
                                "def calc(a1, x1, x2, x3, total):\\n"
                                "    a1 = int(a1)\\n"
                                "    x1 = int(x1)\\n    x2 = int(x2)\\n"
                                "    x3 = int(x3)\\n"
                                "    total = int(total)\\n"
                                "    # 判断点位数量是否大于三个\\n"
                                "    level = 0\\n"
                                "    high_sum = 0\\n"
                                "    if total < 3:\\n"
                                "        level = a1\\n"
                                "    else:\\n"
                                "        # 计算原类别为安全利用类的情况\\n\\n"
                                "        if a1 == 2:\\n"
                                "            if a1 == 2 and x2 + x3 == 0:\\n"
                                "                level = 1\\n"
                                "            else:\\n"
                                "                level = 2\\n"
                                "        # 计算原类别为严格管控类的情况\\n"
                                "        if a1 == 3:\\n"
                                "            if (float(x1)/total >= 0.65 and x3 == 0) or (x2 + x3 == 0):\\n"
                                "                level = 2\\n"
                                "            else:\\n"
                                "                level = 3\\n"
                                "        if a1 == 1:\\n"
                                "            level = 1\\n"
                                "    return level")
# 调整后字段整理
arcpy.DeleteField_management(ljz_3, "count_1;count_2;count_3;count_sum")
arcpy.AddField_management(ljz_3, "level_change", "TEXT", field_length=255)
arcpy.CalculateField_management(ljz_3, "level_change", "Abs ([%s_CLASS] <> [%s_fztz])" % (ys, ys))
# 调整后数据存放
fztzh = "%s辅助调整后" % ys
union_ = os.path.join(work, "union_ysdy")  # 原始单元互补面
arcpy.Erase_analysis(ysdy, ljz_3, union_)  # 擦除得到互补面
merge_ysdy = os.path.join(work, "merge_ysdy")  # 合并后的数据
arcpy.Merge_management([ljz_3, union_], merge_ysdy)  # 合并得到更新后的完整面
layer_ = arcpy.MakeFeatureLayer_management(merge_ysdy, "merge_ysdy_layer")  # 创建视图
temp_ = arcpy.SelectLayerByAttribute_management(layer_, "NEW_SELECTION", '%s_fztz IS NULL' % ys)
arcpy.CalculateField_management(temp_, "%s_fztz" % ys, '[%s_CLASS]' % ys)  # 计算字段
arcpy.CalculateField_management(temp_, "level_change", "0")  # 计算字段
arcpy.FeatureClassToFeatureClass_conversion(merge_ysdy, out_path, fztzh)
# arcpy.AddMessage("已调整完成，数据存放于%s" % out_path)
# 清除中间数据
# arcpy.AddMessage("清空缓存············")
print("清空缓存············")
for one_del in [merge_ysdy, ncp_sxh, ncp_sxh_1, ncp_sxh_2, ncp_sxh_3, union_, dy_sxh, ljz, ljz_1, ljz_2, ljz_3]:
    arcpy.Delete_management(one_del)
print("done!")
