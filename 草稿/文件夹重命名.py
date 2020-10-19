# -*- coding:utf-8 -*-
import os
path = r""
old_name = os.listdir(path)
for one_name in old_name:
    new_name = ''
    os.rename(os.path.join(path, old_name), os.path.join(path, new_name))
