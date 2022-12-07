# -*- coding: utf-8 -*-
import boto3
import io
from PIL import Image
import time
import cv2
import openpyxl

def face_reco():
    person = None
    t1 = time.time()
    # Tạo workbook để lưu file excel
    wb = openpyxl.Workbook()
    activesheet = wb.active
    activesheet.title ="Sheet"
    wb.create_sheet()
    sheet = wb['Sheet']
    # Kết nối đến sever AWS
    rekognition = boto3.client('rekognition', region_name='ap-southeast-1')
    dynamodb = boto3.client('dynamodb', region_name='ap-southeast-1')
    t2 = time.time()
    # Lấy ảnh từ thu mục và chuyển về ảnh nhị phân
    img_name = "./image_face_0.jpg"
    # image_name_1 = cv2.imread(img_name)
    image = Image.open(img_name)
    stream = io.BytesIO()
    image.save(stream,format="JPEG")
    image_binary = stream.getvalue()
    # cam = cv2.VideoCapture(0)
    # frame = cam.read()
    # img_name = frame
    # image = Image.open(img_name)
    # stream = io.BytesIO()
    # image.save(stream,format="JPG")
    # image_binary = stream.getvalue()
    # Detect face by rekognition
    response = rekognition.detect_faces(Image={'Bytes':image_binary})
    all_faces = response['FaceDetails']
    t3 = time.time()
    if all_faces == []:
        return
    else:
        # Tạo list khuôn mặt
        boxes = []
        # Lấy size ảnh
        image_width = image.size[0]
        image_height = image.size[1]
        # Cắt mặt detect được
        for face in all_faces:
            box = face['BoundingBox']
            x1 = int(box['Left'] * image_width) * 0.9
            y1 = int(box['Top'] * image_height) * 0.9
            x2 = int(box['Left'] * image_width + box['Width'] * image_width) * 1.10
            y2 = int(box['Top'] * image_height + box['Height']  * image_height) * 1.10
            image_crop = image.crop((x1,y1,x2,y2))
            # Chuyển về ảnh nhị phân
            stream = io.BytesIO()
            image_crop.save(stream,format="JPEG")
            image_crop_binary = stream.getvalue()
            # Gửi hình ảnh được cắt riêng lẻ lên Amazon Rekognition
            response = rekognition.search_faces_by_image(
                    FaceMatchThreshold=98,
                    MaxFaces=10,
                    CollectionId='faceRecoSingv1',
                    Image={'Bytes':image_crop_binary}                                       
                    )
            if len(response['FaceMatches']) > 0:
                # Return results
                for match in response['FaceMatches']:
                    face = dynamodb.get_item(
                        TableName='faceRecoSingt1',               
                        Key={'RekognitionId': {'S': match['Face']['FaceId']}})
                    if 'Item' in face:
                        person = face['Item']['FullName']['S']
                        # Save person-reco
                        numFace=1
                        if person != sheet["A{}".format(numFace)]:
                            sheet["A{}".format(numFace)] = person
                            sheet["A{}".format(numFace)].value
                            wb.save('excelCreate.xlsx')
                            numFace += 1
                        else:
                            sheet["A{}".format(numFace)] = person
                            sheet["A{}".format(numFace)].value
                            wb.save('excelCreate.xlsx')
                    else:
                        person = 'no match found'
        t4 = time.time()               
        print("Thời gian nhận dạng mặt: ",t4-t1)
        print(person)
if __name__ == "__main__":
    face_reco()
        # k = cv2.waitKey(1)
        # if k%256 == 27:
        # # ESC pressed
        #     print("closing")
        #     break










