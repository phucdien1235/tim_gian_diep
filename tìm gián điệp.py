from guizero import App, Text, Box, Picture, PushButton, info
from random import randint
column_random = randint(0,2)
row_random = randint(0,2)
app = App(title = "Tìm gián điệp", width = 1000, height = 675)
name = Text(app, text = "Đi tìm gián điệp", size = 15, color = "blue")
box_content = Box(app, width = 1000, height = 605, layout = "grid", border = True)
def gian_diep(column, row):
    if column == column_random and row == row_random:
        Picture(box_content, image = "gián điệp.png", grid = [column_random, row_random])
        info("Thông báo", "Bạn đã tìm được gián điệp!")
    else:
        info("Thông báo", "Sai rồi, hãy tìm lại!")
for column in range(0,3):
    for row in range(0,3):
        button = PushButton(box_content, grid = [column, row], text = "?", width = 44, height = 12, command = gian_diep, args = [column, row])

app.display()