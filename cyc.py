import xlwt
import sys
ezxf = xlwt.easyxf
# 生成excel文件
# data:数据
# encoding:编码
# sheet:工作表名称
# path:保存路径
# filename:文件名
# protect:是否开启保护
# password:保护密码
xlwt.easyxf("protection: cell_locked false;")


def save_excel(data, encoding, sheet, path, filename, protect, password):
    try:
        # 创建一个workbook 设置编码
        workbook = xlwt.Workbook(encoding=encoding)
        # 创建一个worksheet
        worksheet = workbook.add_sheet(sheet)
        worksheet.protect = protect  # 設置保護
        worksheet.password = password  # 設置密碼
        # 可编辑,horz center:水平居中,vert center:垂直居中,还可以在这里设置其他样式,颜色,边框等
        editable = ezxf("protection: cell_locked false;align: horz center,vert center;")
        # 不可編輯,horz center:水平居中,vert center:垂直居中,还可以在这里设置其他样式,颜色,边框等
        read_only = ezxf("protection: cell_locked true;align: horz center,vert center;")
        row = 0  # 行
        col = 0  # 列
        for item in data:
            for k, v in item.items():
                # 写入excel
                # 参数对应 行, 列, 值
                if k == "id" or k == "name" or k == "field_id" or k == "field_name":
                    worksheet.write(row, col, label=v, style=read_only)  # 不可编辑
                else:
                    worksheet.write(row, col, label=v, style=editable)  # 可以编辑
                col += 1
            col = 0
            row += 1
        # 保存
        workbook.save("{path}{filename}".format(path=path, filename=filename))
    except Exception as e:
        print("[ERROR]: {error}".format(error=e))
    else:
        print("[SUCCESS]: {path}{filename}".format(path=path, filename=filename))


if __name__ == '__main__':
    data = [
        {"id": "1", "name": "小明", "field_id": "005", "field_name": "005", "date": "2019-7-20", "morning_to_work": "10:00", "morning_off_work": "13:00", "afternoon_to_work": "14:00",
         "afternoon_off_work": "19:00", "to_overtime": "20:00", "off_overtime": "22:00", "overtime_hours": "3"},
        {"id": "2", "name": "小红", "field_id": "006", "field_name": "006", "date": "2019-7-21", "morning_to_work": "10:00", "morning_off_work": "13:00", "afternoon_to_work": "14:00",
         "afternoon_off_work": "19:00", "to_overtime": "20:00", "off_overtime": "22:00", "overtime_hours": "3"},
    ]
    save_excel(data=data, encoding="UTF-8", sheet="Sheet1", path="C:\\Users\\65680\\Desktop\\test", filename='test.xls', protect=True, password="123")