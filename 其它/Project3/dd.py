import os

import shutil

# defaultencoding = 'utf-8'
# if sys.getdefaultencoding() != defaultencoding:
#     reload(sys)
#     sys.setdefaultencoding(defaultencoding)
# start_time = time.clock()

old_path = "C:/Users/Administrator/Desktop/曙光镇 玉龙坝  化作乡 居仁街道  左鸠嘎乡  打证数据"  # 数据原来的路径
new_path = "C:/Users/Administrator/Desktop/NYQQ"    # 存储路径
for root, dirs, files in os.walk(old_path):
    for one_files in files:
        old_path_name = os.path.join(root, one_files)
        new_path_name = os.path.join(new_path, one_files)
        shutil.copyfile(old_path_name, new_path_name)
        print(old_path_name)
        print(new_path_name)




# old_path = 'E:\\台账数据\\纳雍县台账数据\\纳雍县\\曙光镇 玉龙坝  化作乡 居仁街道  左鸠嘎乡  打证数据'
# new_path = 'C:\\Users\\Administrator\\Desktop\\ccc'
# path_list = os.listdir(old_path)
# for i in path_list:
#     path1 = os.path.join(old_path, i)
#     for roots, dirs, files in os.walk(path1):
#         for onefile in files:
#             old_path_name = os.path.join(roots, onefile)
#             new_path_name = os.path.join(new_path, onefile)
#             shutil.copyfile(old_path_name, new_path_name)

#
# print(__file__)
# path = "C:\\Users\\Administrator\\Desktop\\开阳县分乡镇措施表"
#
# old_names = os.listdir(path)
# for one_old_names in old_names:
#     file_path = os.path.join(path, one_old_names)
#     print(one_old_names)
#     # print(file_path)
#     old_names_list = os.listdir(file_path)
#     for cha in old_names_list:
#         new_cha = cha[len(one_old_names):]
#         print(new_cha)
#         os.rename(os.path.join(file_path, cha), os.path.join(file_path, new_cha))