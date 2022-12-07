# -*- coding: utf-8 -*-
from gtts import gTTS
from playsound import playsound
import openpyxl as xl
from pathlib import Path

def text2speech():
    # Tạo danh sách tên theo ID tương ứng
    list_face = ['Tổng Bí Thư',
                'Chủ Tịch Nước',
                'Thủ Tướng',
                'Chủ Tịch Quốc Hội',
                'Võ Văn Thưởng',
                'Trương Thị Mai',
                'Phạm Bình Minh',
                'Nguyễn Văn Nên',
                'Tô Lâm',
                'Phan Đình Trạc',
                'Trần Thanh Mẫn',
                'Trần Tuấn Anh',
                'Trần Cẩm Tú',
                'Phan Văn Giang',
                'Nguyễn Hòa Bình',
                'Nguyễn Xuân Thắng',
                'Lương Cường',
                'Trần Tuấn Anh',
                'Đinh Tiến Dũng',
                'Vũ Đức Đam',
                'Thống Đốc Ngân Hàng',
                'Trần Sỹ Thanh',
                'Hồ Hùng Anh',
                'Đỗ Quang Hiển',
                'Đỗ Minh Phú',
                'Thái Hương',
                'Võ Quốc Thắng',
                'Nguyễn Thị Nga',
                'Đỗ Anh Tuấn', 
                'Tổng Giám Đốc',
                'Chị Ngoãn',
                'Trung Hiếu',
                'Quốc Anh',
                'Văn Thành',
                'Thanh Phong',
                'Hiếu T2', 
                'Phú',
                'Huyền',
                ]
    # Mở wb đã lưu ID nhận dạng được
    wb = xl.load_workbook('./excelCreate.xlsx')
    activeSheet = wb.active
    sheet = wb['Sheet']
    list_1 = list(sheet.columns)[0]
    cell = 0
    face = []
    for cellObj in list_1:
        # Chỉ đến cột A và thêm giá trị vào face[]
        cell_Ai = sheet["A{}".format(cell+1)]
        print(type(int( cell_Ai.value)))
        add = int(cell_Ai.value)
        face.append(add)
        cell +=1
        # print(face)
    # Sắp xếp ID để nhận diện khách VIP
    lenth = len(face)
    for i in range(0,lenth-1):
        for j in range(i+1,lenth):
            if (face[i]>face[j]):
                # Hoán đổi vị trí
                tmp = face[i]
                face[i] = face[j]
                face[j] = tmp
    # Trả về speech
    for ID in face:         
        speech = list_face[ID]
        text = 'Xin chào: ' + speech
        output = gTTS(text, lang="vi", slow=False)
        output.save("output.mp3")
        audio = Path().cwd() / "output.mp3"
        playsound(audio)
        # playsound.playsound('output.mp3', True)

if __name__ == '__main__':
    text2speech()