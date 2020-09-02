# coding: utf-8
import xlsxwriter
import json
import sys


# 生成保存excel文件
def save_excel(data, path, filename):
    try:
        workbook = xlsxwriter.Workbook(path + filename)
        worksheet = workbook.add_worksheet("Sheet1")

        # 页眉页脚
        worksheet.set_header("", {'margin': 0.1})
        worksheet.set_footer("", {'margin': 0.1})
        # 列宽
        worksheet.set_column('A:J', 4.67)
        # 页边距
        worksheet.set_margins(left=0.3, right=0.3, top=0.61, bottom=0.37)
        # 水平对中打印页面
        worksheet.center_horizontally()
        # 设置纸张大小
        worksheet.set_paper(11)
        # 样式1
        style1 = workbook.add_format(
            {'bold': True, 'font_size': 15, 'font_name': '黑体', 'border': 1, 'border_color': 'black'})
        style1.set_align('center')  # 水平对齐
        style1.set_align('vcenter')  # 垂直对齐
        style1.set_text_wrap()  # 内容换行
        # 样式2
        style2 = workbook.add_format(
            {'bold': True, 'font_size': 8, 'font_name': 'Arial', 'border': 1, 'border_color': 'black'})
        style2.set_align('center')  # 水平对齐
        style2.set_align('vcenter')  # 垂直对齐
        style2.set_text_wrap()  # 内容换行
        # 样式3
        style3 = workbook.add_format(
            {'bold': True, 'font_size': 7, 'font_name': '黑体', 'border': 1, 'border_color': 'black'})
        style3.set_align('center')  # 水平对齐
        style3.set_align('vcenter')  # 垂直对齐
        style3.set_text_wrap()  # 内容换行
        # 样式4
        style4 = workbook.add_format(
            {'bold': False, 'font_size': 8, 'font_name': 'Arial', 'border': 1, 'border_color': 'black'})
        style4.set_align('vcenter')  # 垂直对齐
        style4.set_text_wrap()  # 内容换行
        # 样式5
        style5 = workbook.add_format(
            {'bold': False, 'font_size': 7, 'font_name': '黑体', 'border': 1, 'border_color': 'black'})
        style5.set_align('center')  # 水平对齐
        style5.set_align('vcenter')  # 垂直对齐
        style5.set_text_wrap()  # 内容换行
        # 样式6
        style6 = workbook.add_format(
            {'bold': False, 'font_size': 6, 'font_name': '黑体', 'border': 1, 'border_color': 'black',
             'bg_color': 'yellow'})
        style6.set_align('center')  # 水平对齐
        style6.set_align('vcenter')  # 垂直对齐
        style6.set_text_wrap()  # 内容换行

        row_pre_page = 27  # 定义一页有多少行
        for page in range(len(data)):
            offset = page * row_pre_page  # 计算偏移量
            # 行高
            for row in range(0, 9):
                # print(row + offset)
                worksheet.set_row(row + offset, 23)

            # 合并单元格
            worksheet.merge_range('A{}:J{}'.format(1 + offset, 1 + offset),
                                  "{company}  TEL: {tel}".format(company=data[page]['company'], tel=data[page]['tel']),
                                  style1)
            worksheet.merge_range('A{}:B{}'.format(2 + offset, 2 + offset), "日期:", style2)
            worksheet.merge_range('C{}:E{}'.format(2 + offset, 2 + offset),
                                  "{stage}期 {month}月 {year}年".format(stage=data[page]['stage'],
                                                                     month=data[page]['month'],
                                                                     year=data[page]['year']), style4)
            worksheet.merge_range('F{}:G{}'.format(2 + offset, 2 + offset), "姓名\nName:", style2)
            worksheet.merge_range('H{}:J{}'.format(2 + offset, 2 + offset), data[page]['username'], style4)

            worksheet.merge_range('A{}:B{}'.format(3 + offset, 3 + offset), "所屬部門:", style2)
            worksheet.merge_range('C{}:E{}'.format(3 + offset, 3 + offset), data[page]['department'], style4)
            worksheet.merge_range('F{}:G{}'.format(3 + offset, 3 + offset), "號碼\nNo:", style2)
            worksheet.merge_range('H{}:J{}'.format(3 + offset, 3 + offset), data[page]['number'], style4)

            worksheet.merge_range('A{}:B{}'.format(4 + offset, 4 + offset), "工作時日數\nReg Hrs:", style2)
            worksheet.merge_range('C{}:D{}'.format(4 + offset, 4 + offset), "", style4)
            worksheet.merge_range('E{}:F{}'.format(4 + offset, 4 + offset), "資率\nRate:", style2)
            worksheet.write('G{}'.format(4 + offset), "", style4)
            worksheet.merge_range('H{}:I{}'.format(4 + offset, 4 + offset), "總數\nTotal:", style2)
            worksheet.write('J{}'.format(4 + offset), "", style4)

            worksheet.merge_range('A{}:B{}'.format(5 + offset, 5 + offset), "加工時日數\nExtra Hrs:", style2)
            worksheet.merge_range('C{}:D{}'.format(5 + offset, 5 + offset), "", style4)
            worksheet.merge_range('E{}:F{}'.format(5 + offset, 5 + offset), "資率\nRate:", style2)
            worksheet.write('G{}'.format(5 + offset), "", style4)
            worksheet.merge_range('H{}:I{}'.format(5 + offset, 5 + offset), "總數\nTotal:", style2)
            worksheet.write('J{}'.format(5 + offset), data[page]['total'], style4)

            worksheet.merge_range('A{}:B{}'.format(6 + offset, 6 + offset), "告假時日數\nAbsence Hrs:", style2)
            worksheet.merge_range('C{}:D{}'.format(6 + offset, 6 + offset), "", style4)
            worksheet.merge_range('E{}:F{}'.format(6 + offset, 6 + offset), "資率\nRate:", style2)
            worksheet.write('G{}'.format(6 + offset), "", style4)
            worksheet.merge_range('H{}:I{}'.format(6 + offset, 6 + offset), "扣除\nDeduction:", style2)
            worksheet.write('J{}'.format(6 + offset), data[page]['deduction'], style4)

            worksheet.merge_range('A{}:B{}'.format(7 + offset, 7 + offset), "工作時間\nPay Ending:", style2)
            worksheet.merge_range('C{}:F{}'.format(7 + offset, 7 + offset), "", style4)
            worksheet.merge_range('G{}:H{}'.format(7 + offset, 7 + offset), "實得工資\nBalance Due:", style2)
            worksheet.merge_range('I{}:J{}'.format(7 + offset, 7 + offset), "", style4)

            worksheet.merge_range('A{}:B{}'.format(8 + offset, 9 + offset), "日期\nDate", style2)
            worksheet.merge_range('C{}:D{}'.format(8 + offset, 8 + offset), "Before Noon 上午", style3)
            worksheet.merge_range('E{}:F{}'.format(8 + offset, 8 + offset), "After Noon 下午", style3)
            worksheet.merge_range('G{}:H{}'.format(8 + offset, 8 + offset), "Overtime 加工", style3)
            worksheet.merge_range('I{}:J{}'.format(8 + offset, 9 + offset), "共計\nTotal", style2)

            worksheet.write('C{}'.format(9 + offset, 9 + offset), "In 入", style3)
            worksheet.write('D{}'.format(9 + offset, 9 + offset), "Out 出", style3)
            worksheet.write('E{}'.format(9 + offset, 9 + offset), "In 入", style3)
            worksheet.write('F{}'.format(9 + offset, 9 + offset), "Out 出", style3)
            worksheet.write('G{}'.format(9 + offset, 9 + offset), "In 入", style3)
            worksheet.write('H{}'.format(9 + offset, 9 + offset), "Out 出", style3)

            # 打卡记录
            index = 1
            for i in range(10 + offset, (len(data[page]['records']) + 10) + offset):
                # print(i - 1)
                worksheet.set_row(i - 1, 16)  # 行高
                worksheet.merge_range('A{}:B{}'.format(i, i), data[page]['records'][str(index)]['date'], style5)
                if data[page]['records'][str(index)]['vacation'] == "fullday":
                    # worksheet.merge_range('C{}:J{}'.format(i, i), data[page]['records'][str(index)][
                    # 'vacation_name'], style6)
                    worksheet.merge_range('C{}:J{}'.format(i, i), "全天休假", style6)
                elif data[page]['records'][str(index)]['vacation'] == "morning":
                    # worksheet.merge_range('C{}:D{}'.format(i, i), data[page]['records'][str(index)][
                    # 'vacation_name'], style6)
                    worksheet.merge_range('C{}:D{}'.format(i, i), "上午休假", style6)
                    worksheet.write('E{}'.format(i), data[page]['records'][str(index)]['afternoon_to_work'], style5)
                    worksheet.write('F{}'.format(i), data[page]['records'][str(index)]['afternoon_off_work'], style5)
                    worksheet.write('G{}'.format(i), data[page]['records'][str(index)]['to_overtime'], style5)
                    worksheet.write('H{}'.format(i), data[page]['records'][str(index)]['off_overtime'], style5)
                    worksheet.merge_range('I{}:J{}'.format(i, i), data[page]['records'][str(index)]['overtime_hours'],
                                          style5)
                elif data[page]['records'][str(index)]['vacation'] == "afternoon":
                    worksheet.write('C{}'.format(i), data[page]['records'][str(index)]['morning_to_work'], style5)
                    worksheet.write('D{}'.format(i), data[page]['records'][str(index)]['morning_off_work'], style5)
                    # worksheet.merge_range('E{}:F{}'.format(i, i), data[page]['records'][str(index)][
                    # 'vacation_name'], style6)
                    worksheet.merge_range('E{}:F{}'.format(i, i), "下午休假", style6)
                    worksheet.write('G{}'.format(i), data[page]['records'][str(index)]['to_overtime'], style5)
                    worksheet.write('H{}'.format(i), data[page]['records'][str(index)]['off_overtime'], style5)
                    worksheet.merge_range('I{}:J{}'.format(i, i), data[page]['records'][str(index)]['overtime_hours'],
                                          style5)
                else:
                    worksheet.write('C{}'.format(i), data[page]['records'][str(index)]['morning_to_work'], style5)
                    worksheet.write('D{}'.format(i), data[page]['records'][str(index)]['morning_off_work'], style5)
                    worksheet.write('E{}'.format(i), data[page]['records'][str(index)]['afternoon_to_work'], style5)
                    worksheet.write('F{}'.format(i), data[page]['records'][str(index)]['afternoon_off_work'], style5)
                    worksheet.write('G{}'.format(i), data[page]['records'][str(index)]['to_overtime'], style5)
                    worksheet.write('H{}'.format(i), data[page]['records'][str(index)]['off_overtime'], style5)
                    worksheet.merge_range('I{}:J{}'.format(i, i), data[page]['records'][str(index)]['overtime_hours'],
                                          style5)

                if i + 1 == (len(data[page]['records']) + 10) + offset:
                    worksheet.set_row(i, 24)
                    worksheet.merge_range('A{}:J{}'.format(i + 1, i + 1),
                                          "Balance due shown above is correct and receipt is acknowledged.\n收 到 上 列 工 "
                                          "資 數 額 無 訛",
                                          style5)
                    worksheet.set_row(i + 1, 24)
                    worksheet.merge_range('A{}:B{}'.format(i + 2, i + 2), "工人簽字\nSignature:", style2)
                    worksheet.merge_range('C{}:E{}'.format(i + 2, i + 2), "", style5)
                    worksheet.merge_range('F{}:G{}'.format(i + 2, i + 2), "管工簽字\nSignature:", style2)
                    worksheet.merge_range('H{}:J{}'.format(i + 2, i + 2), "", style5)
                index += 1
        workbook.close()
    except Exception as e:
        print("[ERROR -1]: {error}".format(error=e))


# 讀取txt json 作為參數使用
def get_txt_json(path):
    try:
        fo = open(path, "r", encoding="UTF-8")
        txt = fo.read()
        fo.close()
        return txt
    except Exception as e:
        print("[ERROR -2]: {error}".format(error=e))


def main():
    try:
        txt_json = get_txt_json("/Users/davis/python_prduction/weather/txt_json.txt")
        json_data = json.loads(txt_json)

        save_excel(data=json_data, path="/Users/davis/Downloads/", filename="save_excel_xlsxwriter.xlsx")

    except Exception as e:
        print("[ERROR -3]: {error}".format(error=e))


if __name__ == '__main__':
    main()
