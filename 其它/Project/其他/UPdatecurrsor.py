# coding: utf-8
import arcpy
import arcpy.da
import sys

defaultencoding = 'utf-8'

if sys.getdefaultencoding() != defaultencoding:
    reload(sys)
    sys.setdefaultencoding(defaultencoding)
# 成果数据所在位置
layersdata = ur"C:/T面积统计王贵/分类清单数据保存.gdb/耕地数据_行政村_单元_PROJECT"

# 创建游标遍历图层
with arcpy.da.UpdateCursor(layersdata,
                           ['As_CLASS', 'As_FZCLASS', 'Hg_CLASS', 'Hg_FZCLASS', 'Cr_CLASS', 'Cr_FZCLASS', 'Pb_CLASS',
                            'Pb_FZCLASS', 'Cd_CLASS', 'Cd_FZCLASS', 'ZH_CLASS', 'ZH_FZCLASS', 'ZZNZW', 'ZZNZW_1', '省',
                            '市（州）', '县（市_区）', '乡镇（街道）', '类别编码', '地理位置', '面积', '常年主载农作物', '土壤目标污染物', '质量类别',
                            'XH']) as cursor:
# with arcpy.da.UpdateCursor(layersdata,
#                            ['As_CLASS', 'As_FZCLASS', 'Hg_CLASS', 'Hg_FZCLASS', 'Cr_CLASS', 'Cr_FZCLASS',
#                             'Pb_CLASS','Pb_FZCLASS', 'Cd_CLASS', 'Cd_FZCLASS', 'ZH_CLASS', 'ZH_FZCLASS', ]) as cursor:
    # 创建空列表接受信息
    for row in cursor:
        for _i in range(0, 12):
            if row[_i] == 0:
                row[_i] = 1
        row[14] = "贵州省"   # 省
        row[15] = "遵义市"   # 市
        row[16] = "湄潭县"   # 县

        # row[17] = "湄潭县"   # 乡镇
        #
        # row[18] = ''   # 类别编码
        #
        # row[19] = ''   # 地理位置
        #
        # row[20] = ''   # 面积
        #
        # row[21] = ''   # 常年主载农作物
        #
        # row[22] = ''   # 土壤目标污染物
        #
        # row[23] = ''   # 质量类别

        cursor.updateRow(row)
