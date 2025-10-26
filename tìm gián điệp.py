from guizero import App, Text, Box, Picture, PushButton, info
from random import randint
so_lan_con_lai = 5
column_random = randint(0,4)
row_random = randint(0,4)
print(column_random)
print(row_random)
app = App(title = "Tìm gián điệp", width = 1000, height = 675)
name = Text(app, text = "Đi tìm gián điệp", size = 15, color = "blue")
box_content = Box(app, width = 1000, height = 605, layout = "grid", border = True)
info("Xin chào", "Bạn có 5 lượt để đoán gián điệp ở đâu")
def gian_diep(column, row):
    global so_lan_con_lai, column_random, row_random
    if column == column_random and row == row_random and so_lan_con_lai > 1:
        Picture(box_content, image = "gián điệp.png", grid = [column_random, row_random])
        info("Thông báo", "Bạn đã tìm được gián điệp!")
        reset_button = PushButton(app, text = "Chơi lại", width = 25, height = 6, command = reset)
        return reset_button
    else:
        if so_lan_con_lai > 1:
            info("Thông báo", "Sai rồi, hãy tìm lại!")
            so_lan_con_lai -= 1
        elif so_lan_con_lai == 1:
            reset_button = PushButton(app, text = "Chơi lại", width = 25, height = 6, command = reset)
            return reset_button
def reset():
    info("Thông báo", "Đã reset thành công")
    global so_lan_con_lai, column_random, row_random
    so_lan_con_lai = 5
    column_random = randint(0,4)
    row_random = randint(0,4)
    for column in range(0,5):
        for row in range(0,5):
            button = PushButton(box_content, grid = [column, row], text = "?", width = 25, height = 6, command = gian_diep, args = [column, row])
            return button
for column in range(0,5):
    for row in range(0,5):
        button = PushButton(box_content, grid = [column, row], text = "?", width = 25, height = 6, command = gian_diep, args = [column, row])

app.display()