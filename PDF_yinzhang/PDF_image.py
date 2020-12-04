# -*- coding: utf-8 -*-#
# -----------------------
# Date:2020-11-27
# -----------------------
from fpdf import FPDF
class PDF(FPDF):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_margins(left=5, top=10, right=5)
        self.add_page()

    def set_title(self, text):
        self.set_font("Arial", "B", 16)
        self.cell(0, 0, text, 0, 1, "C")
        self.ln(8)

    def set_logo(self, src=r'C:\Users\65680\Desktop\extract_img.png', *args, **kwargs):
        self.image(src, *args, **kwargs)

    def set_footer(self, text):
        self.ln(20)
        self.set_font("Arial", "", 9)
        self.cell(30, 0, text, 0, 1, "L")

    def add_line(self, text1, text2):
        self.set_font("Arial", "B", 11)
        self.cell(25, 6, text1, 0, 0, "L")
        self.set_font("Arial", "", 11)
        self.cell(20, 6, text2, 0, 1, "L")


WIDTH = 80
HEIGHT = 100

pdf = PDF(format=(WIDTH, HEIGHT))
pdf.set_logo(x=65, y=0, w=15, h=14)
pdf.set_title("EB Company")
pdf.add_line("Name: ", "Eneudy Báez")
pdf.add_line("Date: ", "12/Nov/2020 10:40am")
pdf.add_line("Description: ", "This is a test")
pdf.set_footer("** Stay focus **")
pdf.output("ticket.pdf", "F")  # Generate pdf file