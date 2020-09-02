# -*- coding: utf-8 -*-
import time

cc = time.clock()
print(cc)
import arcpy
import sys

print(time.clock())

defaultencoding = 'utf-8'

if sys.getdefaultencoding() != defaultencoding:
    reload(sys)
    sys.setdefaultencoding(defaultencoding)

SJK_MC = 'C:/Users/Administrator/Desktop/sjk'
MC_K = '52贵州省xxx县矢量数据库'

# Process: 创建文件地理数据库
LUJING = arcpy.CreateFileGDB_management(SJK_MC, MC_K, "10.0")

# Process: 创建要素数据集
DT_SJ = arcpy.CreateFeatureDataset_management(LUJING, "底图数据", "")

# Process: 创建要素类 (3)
CX_ZQ = arcpy.CreateFeatureclass_management(DT_SJ, "CXZQ", "POLYGON", "", "DISABLED", "DISABLED", "", "", "0", "0", "0")

# Process: 添加字段 (32)
arcpy.AddField_management(CX_ZQ, "BSM", "LONG", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (31)
arcpy.AddField_management(CX_ZQ, "PXZQDM", "TEXT", "", "", "255", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (30)
arcpy.AddField_management(CX_ZQ, "PXZQMC", "TEXT", "", "", "255", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (22)
arcpy.AddField_management(CX_ZQ, "CXZQDM", "TEXT", "", "", "255", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (21)
arcpy.AddField_management(CX_ZQ, "CXZQMC", "TEXT", "", "", "255", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 创建要素类 (2)
PX_ZQ = arcpy.CreateFeatureclass_management(DT_SJ, "PXZQ", "POLYGON", "", "DISABLED", "DISABLED", "", "", "0", "0", "0")

# Process: 添加字段 (25)
arcpy.AddField_management(PX_ZQ, "BSM", "LONG", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (24)
arcpy.AddField_management(PX_ZQ, "PXZQDM", "TEXT", "", "", "255", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (23)
arcpy.AddField_management(PX_ZQ, "PXZQMC", "TEXT", "", "", "255", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 创建要素类
DL_TB = arcpy.CreateFeatureclass_management(DT_SJ, "DLTB", "POLYGON", "", "DISABLED", "DISABLED", "", "", "0", "0", "0")

# Process: 添加字段
arcpy.AddField_management(DL_TB, "BSM", "LONG", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (2)
arcpy.AddField_management(DL_TB, "YSDM", "TEXT", "", "", "255", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (6)
arcpy.AddField_management(DL_TB, "TBYBH", "TEXT", "", "", "255", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (7)
arcpy.AddField_management(DL_TB, "TBBH", "TEXT", "", "", "255", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (12)
arcpy.AddField_management(DL_TB, "DLBM", "TEXT", "", "", "255", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (11)
arcpy.AddField_management(DL_TB, "DLMC", "TEXT", "", "", "255", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (10)
arcpy.AddField_management(DL_TB, "QSXZ", "TEXT", "", "", "255", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (9)
arcpy.AddField_management(DL_TB, "QSDWDM", "TEXT", "", "", "255", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (8)
arcpy.AddField_management(DL_TB, "QSDWMC", "TEXT", "", "", "255", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (5)
arcpy.AddField_management(DL_TB, "ZLDWDM", "TEXT", "", "", "255", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (4)
arcpy.AddField_management(DL_TB, "ZLDWMC", "TEXT", "", "", "255", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (3)
arcpy.AddField_management(DL_TB, "GDLX", "TEXT", "", "", "255", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (13)
arcpy.AddField_management(DL_TB, "KCLX", "TEXT", "", "", "255", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (14)
arcpy.AddField_management(DL_TB, "KCDLBM", "TEXT", "", "", "255", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (15)
arcpy.AddField_management(DL_TB, "TKXS", "DOUBLE", "", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (16)
arcpy.AddField_management(DL_TB, "TBMJ", "DOUBLE", "", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (17)
arcpy.AddField_management(DL_TB, "XZDWMJ", "DOUBLE", "", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (18)
arcpy.AddField_management(DL_TB, "LXDWMJ", "DOUBLE", "", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (19)
arcpy.AddField_management(DL_TB, "TKMJ", "DOUBLE", "", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (20)
arcpy.AddField_management(DL_TB, "TBDLMJ", "DOUBLE", "", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (28)
arcpy.AddField_management(DL_TB, "PZWH", "TEXT", "", "", "255", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (27)
arcpy.AddField_management(DL_TB, "BGJLH", "TEXT", "", "", "255", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (26)
arcpy.AddField_management(DL_TB, "BGRQ", "DATE", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 创建要素类 (4)
FXZQ = arcpy.CreateFeatureclass_management(DT_SJ, "FXZQ", "POLYGON", "", "DISABLED", "DISABLED", "", "", "0", "0", "0")

# Process: 添加字段 (38)
arcpy.AddField_management(FXZQ, "BSM", "LONG", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (37)
arcpy.AddField_management(FXZQ, "PXZQDM", "TEXT", "", "", "255", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (36)
arcpy.AddField_management(FXZQ, "PXZQMC", "TEXT", "", "", "255", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (35)
arcpy.AddField_management(FXZQ, "CXZQDM", "TEXT", "", "", "255", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (34)
arcpy.AddField_management(FXZQ, "CXZQMC", "TEXT", "", "", "255", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (29)
arcpy.AddField_management(FXZQ, "FXZQDM", "TEXT", "", "", "255", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (33)
arcpy.AddField_management(FXZQ, "FXZQMC", "TEXT", "", "", "255", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 创建要素类 (5)
TX_ZQ = arcpy.CreateFeatureclass_management(DT_SJ, "TXZQ", "POLYGON", "", "DISABLED", "DISABLED", "", "", "0", "0", "0")

# Process: 添加字段 (45)
arcpy.AddField_management(TX_ZQ, "BSM", "LONG", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (44)
arcpy.AddField_management(TX_ZQ, "PXZQDM", "TEXT", "", "", "255", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (43)
arcpy.AddField_management(TX_ZQ, "PXZQMC", "TEXT", "", "", "255", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (42)
arcpy.AddField_management(TX_ZQ, "CXZQDM", "TEXT", "", "", "255", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (41)
arcpy.AddField_management(TX_ZQ, "CXZQMC", "TEXT", "", "", "255", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (39)
arcpy.AddField_management(TX_ZQ, "FXZQDM", "TEXT", "", "", "255", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (40)
arcpy.AddField_management(TX_ZQ, "FXZQMC", "TEXT", "", "", "255", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (53)
arcpy.AddField_management(TX_ZQ, "TXZQDM", "TEXT", "", "", "255", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (54)
arcpy.AddField_management(TX_ZQ, "TXZQMC", "TEXT", "", "", "255", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 创建要素类 (6)
XZQ = arcpy.CreateFeatureclass_management(DT_SJ, "XZQ", "POLYGON", "", "DISABLED", "DISABLED", "", "", "0", "0", "0")

# Process: 添加字段 (52)
arcpy.AddField_management(XZQ, "BSM", "LONG", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (51)
arcpy.AddField_management(XZQ, "PXZQDM", "TEXT", "", "", "255", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (50)
arcpy.AddField_management(XZQ, "PXZQMC", "TEXT", "", "", "255", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (49)
arcpy.AddField_management(XZQ, "CXZQDM", "TEXT", "", "", "255", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (48)
arcpy.AddField_management(XZQ, "CXZQMC", "TEXT", "", "", "255", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (46)
arcpy.AddField_management(XZQ, "FXZQDM", "TEXT", "", "", "255", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (47)
arcpy.AddField_management(XZQ, "FXZQMC", "TEXT", "", "", "255", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (55)
arcpy.AddField_management(XZQ, "TXZQDM", "TEXT", "", "", "255", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (56)
arcpy.AddField_management(XZQ, "TXZQMC", "TEXT", "", "", "255", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (57)
arcpy.AddField_management(XZQ, "XZQDM", "TEXT", "", "", "255", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (58)
arcpy.AddField_management(XZQ, "XZQMC", "TEXT", "", "", "255", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 创建要素数据集 (2)
XC_SJ = arcpy.CreateFeatureDataset_management(LUJING, "详查数据", "")

# Process: 创建要素类 (9)
XCP_JDY = arcpy.CreateFeatureclass_management(XC_SJ, "XCPJDY", "POLYGON", "", "DISABLED", "DISABLED", "", "", "0", "0",
                                              "0")

# Process: 添加字段 (85)
arcpy.AddField_management(XCP_JDY, "BSM", "LONG", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (84)
arcpy.AddField_management(XCP_JDY, "PXZQDM", "TEXT", "", "", "255", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (83)
arcpy.AddField_management(XCP_JDY, "PXZQMC", "TEXT", "", "", "255", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (82)
arcpy.AddField_management(XCP_JDY, "CXZQDM", "TEXT", "", "", "255", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (81)
arcpy.AddField_management(XCP_JDY, "CXZQMC", "TEXT", "", "", "255", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (92)
arcpy.AddField_management(XCP_JDY, "ZH5_CLASS", "SHORT", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (93)
arcpy.AddField_management(XCP_JDY, "SUM_NYDTBMJ", "DOUBLE", "", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (94)
arcpy.AddField_management(XCP_JDY, "XCDYBM", "TEXT", "", "", "255", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 创建要素类 (7)
XCT = arcpy.CreateFeatureclass_management(XC_SJ, "XCT", "POINT", "", "DISABLED", "DISABLED", "", "", "0", "0", "0")

# Process: 添加字段 (65)
arcpy.AddField_management(XCT, "BSM", "LONG", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (64)
arcpy.AddField_management(XCT, "PXZQDM", "TEXT", "", "", "255", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (63)
arcpy.AddField_management(XCT, "PXZQMC", "TEXT", "", "", "255", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (62)
arcpy.AddField_management(XCT, "CXZQDM", "TEXT", "", "", "255", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (61)
arcpy.AddField_management(XCT, "CXZQMC", "TEXT", "", "", "255", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (59)
arcpy.AddField_management(XCT, "FXZQDM", "TEXT", "", "", "255", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (60)
arcpy.AddField_management(XCT, "FXZQMC", "TEXT", "", "", "255", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (66)
arcpy.AddField_management(XCT, "TXZQDM", "TEXT", "", "", "255", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (67)
arcpy.AddField_management(XCT, "TXZQMC", "TEXT", "", "", "255", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (68)
arcpy.AddField_management(XCT, "XZQDM", "TEXT", "", "", "255", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (69)
arcpy.AddField_management(XCT, "XZQMC", "TEXT", "", "", "255", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (86)
arcpy.AddField_management(XCT, "LON", "DOUBLE", "", "6", "", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (87)
arcpy.AddField_management(XCT, "LAT", "DOUBLE", "", "6", "", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (88)
arcpy.AddField_management(XCT, "YDBM", "TEXT", "", "", "255", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (89)
arcpy.AddField_management(XCT, "XCDYBM", "TEXT", "", "", "255", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (90)
arcpy.AddField_management(XCT, "NYDLX", "TEXT", "", "", "255", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (91)
arcpy.AddField_management(XCT, "Cd", "DOUBLE", "", "4", "", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (104)
arcpy.AddField_management(XCT, "Hg", "DOUBLE", "", "4", "", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (105)
arcpy.AddField_management(XCT, "As", "DOUBLE", "", "4", "", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (106)
arcpy.AddField_management(XCT, "Pb", "DOUBLE", "", "4", "", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (107)
arcpy.AddField_management(XCT, "Cr", "DOUBLE", "", "4", "", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (108)
arcpy.AddField_management(XCT, "pH", "DOUBLE", "", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (109)
arcpy.AddField_management(XCT, "Cd_CLASS", "SHORT", "", "4", "", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (110)
arcpy.AddField_management(XCT, "Hg_CLASS", "SHORT", "", "4", "", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (111)
arcpy.AddField_management(XCT, "As_CLASS", "SHORT", "", "4", "", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (112)
arcpy.AddField_management(XCT, "Pb_CLASS", "SHORT", "", "4", "", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (113)
arcpy.AddField_management(XCT, "Cr_CLASS", "SHORT", "", "4", "", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (114)
arcpy.AddField_management(XCT, "ZH_CLASS", "SHORT", "", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 创建要素类 (8)
XCN = arcpy.CreateFeatureclass_management(XC_SJ, "XCN", "POINT", "", "DISABLED", "DISABLED", "", "", "0", "0", "0")

# Process: 添加字段 (76)
arcpy.AddField_management(XCN, "BSM", "LONG", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (75)
arcpy.AddField_management(XCN, "PXZQDM", "TEXT", "", "", "255", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (74)
arcpy.AddField_management(XCN, "PXZQMC", "TEXT", "", "", "255", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (73)
arcpy.AddField_management(XCN, "CXZQDM", "TEXT", "", "", "255", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (72)
arcpy.AddField_management(XCN, "CXZQMC", "TEXT", "", "", "255", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (70)
arcpy.AddField_management(XCN, "FXZQDM", "TEXT", "", "", "255", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (71)
arcpy.AddField_management(XCN, "FXZQMC", "TEXT", "", "", "255", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (77)
arcpy.AddField_management(XCN, "TXZQDM", "TEXT", "", "", "255", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (78)
arcpy.AddField_management(XCN, "TXZQMC", "TEXT", "", "", "255", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (79)
arcpy.AddField_management(XCN, "XZQDM", "TEXT", "", "", "255", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (80)
arcpy.AddField_management(XCN, "XZQMC", "TEXT", "", "", "255", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (103)
arcpy.AddField_management(XCN, "LON", "DOUBLE", "", "6", "", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (115)
arcpy.AddField_management(XCN, "LAT", "DOUBLE", "", "6", "", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (116)
arcpy.AddField_management(XCN, "YDBM", "TEXT", "", "", "255", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (117)
arcpy.AddField_management(XCN, "XCDYBM", "TEXT", "", "", "255", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (118)
arcpy.AddField_management(XCN, "NCPLX", "TEXT", "", "", "255", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (119)
arcpy.AddField_management(XCN, "CdN", "DOUBLE", "", "4", "", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (120)
arcpy.AddField_management(XCN, "HgN", "DOUBLE", "", "4", "", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (121)
arcpy.AddField_management(XCN, "AsN", "DOUBLE", "", "4", "", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (122)
arcpy.AddField_management(XCN, "PbN", "DOUBLE", "", "4", "", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (123)
arcpy.AddField_management(XCN, "CrN", "DOUBLE", "", "4", "", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (125)
arcpy.AddField_management(XCN, "CdN_CLASS", "SHORT", "", "4", "", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (126)
arcpy.AddField_management(XCN, "HgN_CLASS", "SHORT", "", "4", "", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (127)
arcpy.AddField_management(XCN, "AsN_CLASS", "SHORT", "", "4", "", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (128)
arcpy.AddField_management(XCN, "PbN_CLASS", "SHORT", "", "4", "", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (129)
arcpy.AddField_management(XCN, "CrN_CLASS", "SHORT", "", "4", "", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (130)
arcpy.AddField_management(XCN, "ZHN_CLASS", "SHORT", "", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 创建要素数据集 (4)
LBHFCGSJ = arcpy.CreateFeatureDataset_management(LUJING, "类别划分成果数据", "")

# Process: 创建要素类 (12)
LBHF = arcpy.CreateFeatureclass_management(LBHFCGSJ, "LBHF", "POLYGON", "", "DISABLED", "DISABLED", "", "", "0", "0",
                                           "0")

# Process: 添加字段 (101)
arcpy.AddField_management(LBHF, "BSM", "LONG", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (100)
arcpy.AddField_management(LBHF, "PXZQDM", "TEXT", "", "", "255", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (99)
arcpy.AddField_management(LBHF, "PXZQMC", "TEXT", "", "", "255", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (98)
arcpy.AddField_management(LBHF, "CXZQDM", "TEXT", "", "", "255", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (97)
arcpy.AddField_management(LBHF, "CXZQMC", "TEXT", "", "", "255", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (95)
arcpy.AddField_management(LBHF, "FXZQDM", "TEXT", "", "", "255", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (96)
arcpy.AddField_management(LBHF, "FXZQMC", "TEXT", "", "", "255", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (102)
arcpy.AddField_management(LBHF, "TXZQDM", "TEXT", "", "", "255", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (124)
arcpy.AddField_management(LBHF, "TXZQMC", "TEXT", "", "", "255", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (139)
arcpy.AddField_management(LBHF, "QSDWDM", "TEXT", "", "", "255", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (138)
arcpy.AddField_management(LBHF, "QSDWMC", "TEXT", "", "", "255", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (142)
arcpy.AddField_management(LBHF, "DLBM", "TEXT", "", "", "255", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (141)
arcpy.AddField_management(LBHF, "DLMC", "TEXT", "", "", "255", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (150)
arcpy.AddField_management(LBHF, "TBDLMJ", "DOUBLE", "", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (131)
arcpy.AddField_management(LBHF, "Cd_CLASS", "SHORT", "", "4", "", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (132)
arcpy.AddField_management(LBHF, "Hg_CLASS", "SHORT", "", "4", "", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (133)
arcpy.AddField_management(LBHF, "As_CLASS", "SHORT", "", "4", "", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (134)
arcpy.AddField_management(LBHF, "Pb_CLASS", "SHORT", "", "4", "", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (135)
arcpy.AddField_management(LBHF, "Cr_CLASS", "SHORT", "", "4", "", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (136)
arcpy.AddField_management(LBHF, "ZH_CLASS", "SHORT", "", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (137)
arcpy.AddField_management(LBHF, "LBBM", "TEXT", "", "2", "255", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (140)
arcpy.AddField_management(LBHF, "DLWZ", "TEXT", "", "4", "255", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (143)
arcpy.AddField_management(LBHF, "MJ_MU", "TEXT", "", "4", "255", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (144)
arcpy.AddField_management(LBHF, "CNZZNZW", "TEXT", "", "4", "255", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (145)
arcpy.AddField_management(LBHF, "TRMBWRW", "TEXT", "", "4", "255", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (146)
arcpy.AddField_management(LBHF, "ZLLB", "TEXT", "", "4", "255", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (147)
arcpy.AddField_management(LBHF, "XCWFNY", "TEXT", "", "2", "255", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 创建要素数据集 (3)
QTSJ = arcpy.CreateFeatureDataset_management(LUJING, "其他数据", "")

# Process: 创建要素类 (10)
PCT = arcpy.CreateFeatureclass_management(QTSJ, "PCT", "POINT", "", "DISABLED", "DISABLED", "", "", "0", "0", "0")

# Process: 添加字段 (155)
arcpy.AddField_management(PCT, "BSM", "LONG", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (154)
arcpy.AddField_management(PCT, "PXZQDM", "TEXT", "", "", "255", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (153)
arcpy.AddField_management(PCT, "PXZQMC", "TEXT", "", "", "255", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (152)
arcpy.AddField_management(PCT, "CXZQDM", "TEXT", "", "", "255", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (151)
arcpy.AddField_management(PCT, "CXZQMC", "TEXT", "", "", "255", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (148)
arcpy.AddField_management(PCT, "FXZQDM", "TEXT", "", "", "255", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (149)
arcpy.AddField_management(PCT, "FXZQMC", "TEXT", "", "", "255", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (156)
arcpy.AddField_management(PCT, "TXZQDM", "TEXT", "", "", "255", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (157)
arcpy.AddField_management(PCT, "TXZQMC", "TEXT", "", "", "255", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (158)
arcpy.AddField_management(PCT, "XZQDM", "TEXT", "", "", "255", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (159)
arcpy.AddField_management(PCT, "XZQMC", "TEXT", "", "", "255", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (160)
arcpy.AddField_management(PCT, "LON", "DOUBLE", "", "6", "", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (161)
arcpy.AddField_management(PCT, "LAT", "DOUBLE", "", "6", "", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (162)
arcpy.AddField_management(PCT, "YDBM", "TEXT", "", "", "255", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (164)
arcpy.AddField_management(PCT, "NYDLX", "TEXT", "", "", "255", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (165)
arcpy.AddField_management(PCT, "Cd", "DOUBLE", "", "4", "", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (166)
arcpy.AddField_management(PCT, "Hg", "DOUBLE", "", "4", "", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (167)
arcpy.AddField_management(PCT, "As", "DOUBLE", "", "4", "", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (168)
arcpy.AddField_management(PCT, "Pb", "DOUBLE", "", "4", "", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (169)
arcpy.AddField_management(PCT, "Cr", "DOUBLE", "", "4", "", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (170)
arcpy.AddField_management(PCT, "pH", "DOUBLE", "", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (171)
arcpy.AddField_management(PCT, "Cd_CLASS", "SHORT", "", "4", "", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (172)
arcpy.AddField_management(PCT, "Hg_CLASS", "SHORT", "", "4", "", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (173)
arcpy.AddField_management(PCT, "As_CLASS", "SHORT", "", "4", "", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (174)
arcpy.AddField_management(PCT, "Pb_CLASS", "SHORT", "", "4", "", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (175)
arcpy.AddField_management(PCT, "Cr_CLASS", "SHORT", "", "4", "", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (176)
arcpy.AddField_management(PCT, "ZH_CLASS", "SHORT", "", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (163)
arcpy.AddField_management(PCT, "XMMC", "TEXT", "", "", "255", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 创建要素类 (16)
JCN = arcpy.CreateFeatureclass_management(QTSJ, "JCN", "POINT", "", "DISABLED", "DISABLED", "", "", "0", "0", "0")

# Process: 添加字段 (183)
arcpy.AddField_management(JCN, "BSM", "LONG", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (182)
arcpy.AddField_management(JCN, "PXZQDM", "TEXT", "", "", "255", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (181)
arcpy.AddField_management(JCN, "PXZQMC", "TEXT", "", "", "255", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (180)
arcpy.AddField_management(JCN, "CXZQDM", "TEXT", "", "", "255", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (179)
arcpy.AddField_management(JCN, "CXZQMC", "TEXT", "", "", "255", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (177)
arcpy.AddField_management(JCN, "FXZQDM", "TEXT", "", "", "255", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (178)
arcpy.AddField_management(JCN, "FXZQMC", "TEXT", "", "", "255", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (184)
arcpy.AddField_management(JCN, "TXZQDM", "TEXT", "", "", "255", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (185)
arcpy.AddField_management(JCN, "TXZQMC", "TEXT", "", "", "255", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (186)
arcpy.AddField_management(JCN, "XZQDM", "TEXT", "", "", "255", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (187)
arcpy.AddField_management(JCN, "XZQMC", "TEXT", "", "", "255", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (188)
arcpy.AddField_management(JCN, "LON", "DOUBLE", "", "6", "", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (189)
arcpy.AddField_management(JCN, "LAT", "DOUBLE", "", "6", "", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (190)
arcpy.AddField_management(JCN, "YDBM", "TEXT", "", "", "255", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (192)
arcpy.AddField_management(JCN, "NCPLX", "TEXT", "", "", "255", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (193)
arcpy.AddField_management(JCN, "CdN", "DOUBLE", "", "4", "", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (194)
arcpy.AddField_management(JCN, "HgN", "DOUBLE", "", "4", "", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (195)
arcpy.AddField_management(JCN, "AsN", "DOUBLE", "", "4", "", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (196)
arcpy.AddField_management(JCN, "PbN", "DOUBLE", "", "4", "", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (197)
arcpy.AddField_management(JCN, "CrN", "DOUBLE", "", "4", "", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (198)
arcpy.AddField_management(JCN, "CdN_CLASS", "SHORT", "", "4", "", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (199)
arcpy.AddField_management(JCN, "HgN_CLASS", "SHORT", "", "4", "", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (200)
arcpy.AddField_management(JCN, "AsN_CLASS", "SHORT", "", "4", "", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (201)
arcpy.AddField_management(JCN, "PbN_CLASS", "SHORT", "", "4", "", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (202)
arcpy.AddField_management(JCN, "CrN_CLASS", "SHORT", "", "4", "", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (203)
arcpy.AddField_management(JCN, "ZHN_CLASS", "SHORT", "", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (204)
arcpy.AddField_management(JCN, "XMMC", "TEXT", "", "", "255", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 创建要素类 (11)
PCN = arcpy.CreateFeatureclass_management(QTSJ, "PCN", "POINT", "", "DISABLED", "DISABLED", "", "", "0", "0", "0")

# Process: 添加字段 (210)
arcpy.AddField_management(PCN, "BSM", "LONG", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (209)
arcpy.AddField_management(PCN, "PXZQDM", "TEXT", "", "", "255", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (208)
arcpy.AddField_management(PCN, "PXZQMC", "TEXT", "", "", "255", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (207)
arcpy.AddField_management(PCN, "CXZQDM", "TEXT", "", "", "255", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (206)
arcpy.AddField_management(PCN, "CXZQMC", "TEXT", "", "", "255", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (191)
arcpy.AddField_management(PCN, "FXZQDM", "TEXT", "", "", "255", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (205)
arcpy.AddField_management(PCN, "FXZQMC", "TEXT", "", "", "255", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (211)
arcpy.AddField_management(PCN, "TXZQDM", "TEXT", "", "", "255", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (212)
arcpy.AddField_management(PCN, "TXZQMC", "TEXT", "", "", "255", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (213)
arcpy.AddField_management(PCN, "XZQDM", "TEXT", "", "", "255", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (214)
arcpy.AddField_management(PCN, "XZQMC", "TEXT", "", "", "255", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (215)
arcpy.AddField_management(PCN, "LON", "DOUBLE", "", "6", "", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (216)
arcpy.AddField_management(PCN, "LAT", "DOUBLE", "", "6", "", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (217)
arcpy.AddField_management(PCN, "YDBM", "TEXT", "", "", "255", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (218)
arcpy.AddField_management(PCN, "NCPLX", "TEXT", "", "", "255", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (219)
arcpy.AddField_management(PCN, "CdN", "DOUBLE", "", "4", "", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (220)
arcpy.AddField_management(PCN, "HgN", "DOUBLE", "", "4", "", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (221)
arcpy.AddField_management(PCN, "AsN", "DOUBLE", "", "4", "", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (222)
arcpy.AddField_management(PCN, "PbN", "DOUBLE", "", "4", "", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (223)
arcpy.AddField_management(PCN, "CrN", "DOUBLE", "", "4", "", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (224)
arcpy.AddField_management(PCN, "CdN_CLASS", "SHORT", "", "4", "", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (225)
arcpy.AddField_management(PCN, "HgN_CLASS", "SHORT", "", "4", "", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (226)
arcpy.AddField_management(PCN, "AsN_CLASS", "SHORT", "", "4", "", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (227)
arcpy.AddField_management(PCN, "PbN_CLASS", "SHORT", "", "4", "", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (228)
arcpy.AddField_management(PCN, "CrN_CLASS", "SHORT", "", "4", "", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (229)
arcpy.AddField_management(PCN, "ZHN_CLASS", "SHORT", "", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (230)
arcpy.AddField_management(PCN, "XMMC", "TEXT", "", "", "255", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 创建要素类 (17)
QTN = arcpy.CreateFeatureclass_management(QTSJ, "QTN", "POINT", "", "DISABLED", "DISABLED", "", "", "0", "0", "0")

# Process: 添加字段 (237)
arcpy.AddField_management(QTN, "BSM", "LONG", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (236)
arcpy.AddField_management(QTN, "PXZQDM", "TEXT", "", "", "255", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (235)
arcpy.AddField_management(QTN, "PXZQMC", "TEXT", "", "", "255", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (234)
arcpy.AddField_management(QTN, "CXZQDM", "TEXT", "", "", "255", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (233)
arcpy.AddField_management(QTN, "CXZQMC", "TEXT", "", "", "255", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (231)
arcpy.AddField_management(QTN, "FXZQDM", "TEXT", "", "", "255", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (232)
arcpy.AddField_management(QTN, "FXZQMC", "TEXT", "", "", "255", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (238)
arcpy.AddField_management(QTN, "TXZQDM", "TEXT", "", "", "255", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (239)
arcpy.AddField_management(QTN, "TXZQMC", "TEXT", "", "", "255", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (240)
arcpy.AddField_management(QTN, "XZQDM", "TEXT", "", "", "255", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (241)
arcpy.AddField_management(QTN, "XZQMC", "TEXT", "", "", "255", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (242)
arcpy.AddField_management(QTN, "LON", "DOUBLE", "", "6", "", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (243)
arcpy.AddField_management(QTN, "LAT", "DOUBLE", "", "6", "", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (244)
arcpy.AddField_management(QTN, "YDBM", "TEXT", "", "", "255", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (245)
arcpy.AddField_management(QTN, "NCPLX", "TEXT", "", "", "255", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (246)
arcpy.AddField_management(QTN, "CdN", "DOUBLE", "", "4", "", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (247)
arcpy.AddField_management(QTN, "HgN", "DOUBLE", "", "4", "", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (248)
arcpy.AddField_management(QTN, "AsN", "DOUBLE", "", "4", "", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (249)
arcpy.AddField_management(QTN, "PbN", "DOUBLE", "", "4", "", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (250)
arcpy.AddField_management(QTN, "CrN", "DOUBLE", "", "4", "", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (251)
arcpy.AddField_management(QTN, "CdN_CLASS", "SHORT", "", "4", "", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (252)
arcpy.AddField_management(QTN, "HgN_CLASS", "SHORT", "", "4", "", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (253)
arcpy.AddField_management(QTN, "AsN_CLASS", "SHORT", "", "4", "", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (254)
arcpy.AddField_management(QTN, "PbN_CLASS", "SHORT", "", "4", "", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (255)
arcpy.AddField_management(QTN, "CrN_CLASS", "SHORT", "", "4", "", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (256)
arcpy.AddField_management(QTN, "ZHN_CLASS", "SHORT", "", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (257)
arcpy.AddField_management(QTN, "XMMC", "TEXT", "", "", "255", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 创建要素类 (14)
DMBT = arcpy.CreateFeatureclass_management(QTSJ, "DMBT", "POINT", "", "DISABLED", "DISABLED", "", "", "0", "0", "0")

# Process: 添加字段 (264)
arcpy.AddField_management(DMBT, "BSM", "LONG", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (263)
arcpy.AddField_management(DMBT, "PXZQDM", "TEXT", "", "", "255", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (262)
arcpy.AddField_management(DMBT, "PXZQMC", "TEXT", "", "", "255", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (261)
arcpy.AddField_management(DMBT, "CXZQDM", "TEXT", "", "", "255", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (260)
arcpy.AddField_management(DMBT, "CXZQMC", "TEXT", "", "", "255", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (258)
arcpy.AddField_management(DMBT, "FXZQDM", "TEXT", "", "", "255", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (259)
arcpy.AddField_management(DMBT, "FXZQMC", "TEXT", "", "", "255", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (265)
arcpy.AddField_management(DMBT, "TXZQDM", "TEXT", "", "", "255", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (266)
arcpy.AddField_management(DMBT, "TXZQMC", "TEXT", "", "", "255", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (267)
arcpy.AddField_management(DMBT, "XZQDM", "TEXT", "", "", "255", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (268)
arcpy.AddField_management(DMBT, "XZQMC", "TEXT", "", "", "255", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (269)
arcpy.AddField_management(DMBT, "LON", "DOUBLE", "", "6", "", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (270)
arcpy.AddField_management(DMBT, "LAT", "DOUBLE", "", "6", "", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (271)
arcpy.AddField_management(DMBT, "YDBM", "TEXT", "", "", "255", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (273)
arcpy.AddField_management(DMBT, "NYDLX", "TEXT", "", "", "255", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (274)
arcpy.AddField_management(DMBT, "Cd", "DOUBLE", "", "4", "", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (275)
arcpy.AddField_management(DMBT, "Hg", "DOUBLE", "", "4", "", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (276)
arcpy.AddField_management(DMBT, "As", "DOUBLE", "", "4", "", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (277)
arcpy.AddField_management(DMBT, "Pb", "DOUBLE", "", "4", "", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (278)
arcpy.AddField_management(DMBT, "Cr", "DOUBLE", "", "4", "", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (279)
arcpy.AddField_management(DMBT, "pH", "DOUBLE", "", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (280)
arcpy.AddField_management(DMBT, "Cd_CLASS", "SHORT", "", "4", "", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (281)
arcpy.AddField_management(DMBT, "Hg_CLASS", "SHORT", "", "4", "", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (282)
arcpy.AddField_management(DMBT, "As_CLASS", "SHORT", "", "4", "", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (283)
arcpy.AddField_management(DMBT, "Pb_CLASS", "SHORT", "", "4", "", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (284)
arcpy.AddField_management(DMBT, "Cr_CLASS", "SHORT", "", "4", "", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (285)
arcpy.AddField_management(DMBT, "ZH_CLASS", "SHORT", "", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (272)
arcpy.AddField_management(DMBT, "XMMC", "TEXT", "", "", "255", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 创建要素类 (15)
QTT = arcpy.CreateFeatureclass_management(QTSJ, "QTT", "POINT", "", "DISABLED", "DISABLED", "", "", "0", "0", "0")

# Process: 添加字段 (292)
arcpy.AddField_management(QTT, "BSM", "LONG", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (291)
arcpy.AddField_management(QTT, "PXZQDM", "TEXT", "", "", "255", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (290)
arcpy.AddField_management(QTT, "PXZQMC", "TEXT", "", "", "255", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (289)
arcpy.AddField_management(QTT, "CXZQDM", "TEXT", "", "", "255", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (288)
arcpy.AddField_management(QTT, "CXZQMC", "TEXT", "", "", "255", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (286)
arcpy.AddField_management(QTT, "FXZQDM", "TEXT", "", "", "255", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (287)
arcpy.AddField_management(QTT, "FXZQMC", "TEXT", "", "", "255", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (293)
arcpy.AddField_management(QTT, "TXZQDM", "TEXT", "", "", "255", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (294)
arcpy.AddField_management(QTT, "TXZQMC", "TEXT", "", "", "255", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (295)
arcpy.AddField_management(QTT, "XZQDM", "TEXT", "", "", "255", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (296)
arcpy.AddField_management(QTT, "XZQMC", "TEXT", "", "", "255", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (297)
arcpy.AddField_management(QTT, "LON", "DOUBLE", "", "6", "", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (298)
arcpy.AddField_management(QTT, "LAT", "DOUBLE", "", "6", "", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (299)
arcpy.AddField_management(QTT, "YDBM", "TEXT", "", "", "255", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (301)
arcpy.AddField_management(QTT, "NYDLX", "TEXT", "", "", "255", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (302)
arcpy.AddField_management(QTT, "Cd", "DOUBLE", "", "4", "", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (303)
arcpy.AddField_management(QTT, "Hg", "DOUBLE", "", "4", "", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (304)
arcpy.AddField_management(QTT, "As", "DOUBLE", "", "4", "", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (305)
arcpy.AddField_management(QTT, "Pb", "DOUBLE", "", "4", "", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (306)
arcpy.AddField_management(QTT, "Cr", "DOUBLE", "", "4", "", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (307)
arcpy.AddField_management(QTT, "pH", "DOUBLE", "", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (308)
arcpy.AddField_management(QTT, "Cd_CLASS", "SHORT", "", "4", "", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (309)
arcpy.AddField_management(QTT, "Hg_CLASS", "SHORT", "", "4", "", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (310)
arcpy.AddField_management(QTT, "As_CLASS", "SHORT", "", "4", "", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (311)
arcpy.AddField_management(QTT, "Pb_CLASS", "SHORT", "", "4", "", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (312)
arcpy.AddField_management(QTT, "Cr_CLASS", "SHORT", "", "4", "", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (313)
arcpy.AddField_management(QTT, "ZH_CLASS", "SHORT", "", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (300)
arcpy.AddField_management(QTT, "XMMC", "TEXT", "", "", "255", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 创建要素类 (13)
JCT = arcpy.CreateFeatureclass_management(QTSJ, "JCT", "POINT", "", "DISABLED", "DISABLED", "", "", "0", "0", "0")

# Process: 添加字段 (320)
arcpy.AddField_management(JCT, "BSM", "LONG", "", "", "", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (319)
arcpy.AddField_management(JCT, "PXZQDM", "TEXT", "", "", "255", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (318)
arcpy.AddField_management(JCT, "PXZQMC", "TEXT", "", "", "255", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (317)
arcpy.AddField_management(JCT, "CXZQDM", "TEXT", "", "", "255", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (316)
arcpy.AddField_management(JCT, "CXZQMC", "TEXT", "", "", "255", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (314)
arcpy.AddField_management(JCT, "FXZQDM", "TEXT", "", "", "255", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (315)
arcpy.AddField_management(JCT, "FXZQMC", "TEXT", "", "", "255", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (321)
arcpy.AddField_management(JCT, "TXZQDM", "TEXT", "", "", "255", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (322)
arcpy.AddField_management(JCT, "TXZQMC", "TEXT", "", "", "255", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (323)
arcpy.AddField_management(JCT, "XZQDM", "TEXT", "", "", "255", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (324)
arcpy.AddField_management(JCT, "XZQMC", "TEXT", "", "", "255", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (325)
arcpy.AddField_management(JCT, "LON", "DOUBLE", "", "6", "", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (326)
arcpy.AddField_management(JCT, "LAT", "DOUBLE", "", "6", "", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (327)
arcpy.AddField_management(JCT, "YDBM", "TEXT", "", "", "255", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (329)
arcpy.AddField_management(JCT, "NYDLX", "TEXT", "", "", "255", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (330)
arcpy.AddField_management(JCT, "Cd", "DOUBLE", "", "4", "", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (331)
arcpy.AddField_management(JCT, "Hg", "DOUBLE", "", "4", "", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (332)
arcpy.AddField_management(JCT, "As", "DOUBLE", "", "4", "", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (333)
arcpy.AddField_management(JCT, "Pb", "DOUBLE", "", "4", "", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (334)
arcpy.AddField_management(JCT, "Cr", "DOUBLE", "", "4", "", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (335)
arcpy.AddField_management(JCT, "pH", "DOUBLE", "", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (336)
arcpy.AddField_management(JCT, "Cd_CLASS", "SHORT", "", "4", "", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (337)
arcpy.AddField_management(JCT, "Hg_CLASS", "SHORT", "", "4", "", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (338)
arcpy.AddField_management(JCT, "As_CLASS", "SHORT", "", "4", "", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (339)
arcpy.AddField_management(JCT, "Pb_CLASS", "SHORT", "", "4", "", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (340)
arcpy.AddField_management(JCT, "Cr_CLASS", "SHORT", "", "4", "", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (341)
arcpy.AddField_management(JCT, "ZH_CLASS", "SHORT", "", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

# Process: 添加字段 (328)
arcpy.AddField_management(JCT, "XMMC", "TEXT", "", "", "255", "", "NULLABLE", "NON_REQUIRED", "")

print(time.clock())













