# coding:utf-8
import arcpy

arcpy.env.workspace = r'C:\Users\ols\Desktop\T1105检查\T1106检查.gdb'


# arcpy.AddField_management('地块_polygons', 'A', 'TEXT', '', '', '255')  # 省
# arcpy.AddField_management('地块_polygons', 'B', 'TEXT', '', '', '255')  # 市
# arcpy.AddField_management('地块_polygons', 'C', 'TEXT', '', '', '255')  # 县
# arcpy.AddField_management('地块_polygons', 'D', 'TEXT', '', '', '255')  # 行业类型
# arcpy.AddField_management('地块_polygons', 'E', 'TEXT', '', '', '50')  # 行业代码
# arcpy.AddField_management('地块_polygons', 'F', 'TEXT', '', '', '255')  # 地块类型
# arcpy.AddField_management('地块_polygons', 'G', 'TEXT', '', '', '5')  # 借力类型

# arcpy.CalculateField_management('地块_polygons', '省', expression='!A!')
# arcpy.CalculateField_management('地块_polygons', '市', expression='!B!')
# arcpy.CalculateField_management('地块_polygons', '县', expression='!C!')
# arcpy.CalculateField_management('地块_polygons', '行业类型', expression='!D!')
# arcpy.CalculateField_management('地块_polygons', '行业代码', expression='!E!')
# arcpy.CalculateField_management('地块_polygons', '地块类型', expression='!F!')
# arcpy.CalculateField_management('地块_polygons', '借力类型', expression='!G!')
#
# arcpy.DeleteField_management('地块_polygons', 'A')
# arcpy.DeleteField_management('地块_polygons', 'B')
# arcpy.DeleteField_management('地块_polygons', 'C')
# arcpy.DeleteField_management('地块_polygons', 'D')
# arcpy.DeleteField_management('地块_polygons', 'E')
# arcpy.DeleteField_management('地块_polygons', 'F')
# arcpy.DeleteField_management('地块_polygons', 'G')

# arcpy.AddField_management('地块_polygons', '省', 'TEXT', '', '', '255')  # 省
# arcpy.AddField_management('地块_polygons', '市', 'TEXT', '', '', '255')  # 市
# arcpy.AddField_management('地块_polygons', '县', 'TEXT', '', '', '255')  # 县
# arcpy.AddField_management('地块_polygons', '行业类型', 'TEXT', '', '', '255')  # 行业类型
# arcpy.AddField_management('地块_polygons', '行业代码', 'TEXT', '', '', '50')  # 行业代码
# arcpy.AddField_management('地块_polygons', '地块类型', 'TEXT', '', '', '255')  # 地块类型
# arcpy.AddField_management('地块_polygons', '借力类型', 'TEXT', '', '', '5')  # 借力类型
