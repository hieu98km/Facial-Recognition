# -*- coding: utf-8 -*-
from gtts import gTTS
import playsound
import openpyxl as xl
import os

def text2speech():
    ListFace = ['Tổng Bí Thư',
                'Chủ Tịch Nước',
                'Thủ Tướng Chính Phủ',
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
                'Thống Đốc Ngân Hàng Nhà Nước Việt Nam',
                'Trần Sỹ Thanh',
                'Hồ Hùng Anh','Đỗ Quang Hiển',
                'Đỗ Minh Phú','Thái Hương',
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
    # Load file xlsx
    wb = xl.load_workbook(f'/home/hieu98/Documents/Backup_22_11_v2/excelCreate.xlsx')
    activeSheet = wb.active
    sheet = wb['Sheet']
    list_1 = list(sheet.columns)[0]
    cell = 0
    listFace =[]
    for cellObj in list_1:
        # Chi den o A1 va in gia tri
        cellA1 = sheet["A{}".format(cell+1)]
        print(type(int(cellA1.value)))
        a = int(cellA1.value)
        listFace.append(a)
        print(listFace)
        cell +=1
    lenth = len(listFace)
    # Lặp từ phần tử đầu đến kế cuối,
    # Vì khi đến phần tử cuối là đã sắp xếp thành công
    for i in range(0, lenth - 1):
        for j in range(i + 1, lenth):
            if (listFace[i] > listFace[j]):
                # Hoán đổi vị trí
                tmp = listFace[i]
                listFace[i] = listFace[j]
                listFace[j] = tmp
    for m in listFace:           
        textSpeech = ListFace[m-1]
        text = 'Xin chào: ' + textSpeech
        output = gTTS(text, lang="vi", slow=False)
        output.save("output.mp3")
        playsound.playsound('output.mp3', True)
        os.system('python2 mp3Co.py')