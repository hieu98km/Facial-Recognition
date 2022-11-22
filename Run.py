from __future__ import print_function
import boto3
import io
from PIL import Image, ImageDraw, ExifTags, ImageColor
import time
import cv2
import openpyxl
from TTS import text2speech


if __name__ == "__main__":
    # Tạo workbook để lưu file excel 
    wb = openpyxl.Workbook()
    activesheet = wb.active
    activesheet.title ="Sheet new"
    wb.create_sheet()
    sheet = wb['Sheet new']
    # Kết nối đến aws
    t0 = time.time()
    rekognition = boto3.client('rekognition', region_name='ap-southeast-1')
    dynamodb = boto3.client('dynamodb', region_name='ap-southeast-1')
    t1 = time.time()
    # Khởi tạo camera
    img_counter = 0
    person = None
    while True:
        cam = cv2.VideoCapture(0)
        numFace = 1
        t2 = time.time()
        ret, frame = cam.read()
        if not ret:
            print("lấy ảnh lỗi")
            break
        # Lưu ảnh và convert chuẩn bị cho rekognition
        img_name = "image_face_{}.png".format(img_counter)
        cv2.imwrite(img_name, frame)
        image_path0 = cv2.imread(img_name)
        image = Image.open(img_name)
        stream = io.BytesIO()
        image.save(stream,format="JPEG")
        image_binary = stream.getvalue()
        t3 = time.time()
        # Detect face by rekognition
        response = rekognition.detect_faces(Image={'Bytes':image_binary})
        all_faces = response['FaceDetails']
        # Tạo list khuôn mặt
        boxes = []
        # Lấy size ảnh
        image_width = image.size[0]
        image_height = image.size[1]
        # Khởi tạo vẽ trên ảnh
        # draw = ImageDraw.Draw(image)
        # Cắt mặt detect được
        for face in all_faces:
            box = face['BoundingBox']
            x1 = int(box['Left'] * image_width) * 0.9
            y1 = int(box['Top'] * image_height) * 0.9
            x2 = int(box['Left'] * image_width + box['Width'] * image_width) * 1.10
            y2 = int(box['Top'] * image_height + box['Height']  * image_height) * 1.10
            image_crop = image.crop((x1,y1,x2,y2))
            # Lấy ra vị trí để vẽ hcn
            left = image_width * box['Left']
            top = image_height * box['Top']
            width = image_width * box['Width']
            height = image_height * box['Height']
            # Tọa độ hcn
            points = (
                (left,top),
                (left + width, top),
                (left + width, top + height),
                (left , top + height),
                (left, top)
            )
            # draw.line(points, fill='#00d400', width=2)
            stream = io.BytesIO()
            image_crop.save(stream,format="JPEG")
            image_crop_binary = stream.getvalue()
            t4 = time.time()
            # Gửi hình ảnh được cắt riêng lẻ lên Amazon Rekognition
            response = rekognition.search_faces_by_image(
                    FaceMatchThreshold=95,
                    MaxFaces=256,
                    CollectionId='faceRecoSing',
                    Image={'Bytes':image_crop_binary}                                       
                    )
            if len(response['FaceMatches']) > 0:
                # Return results
                # print ('Tọa độ: ', box)
                for match in response['FaceMatches']:
                    face = dynamodb.get_item(
                        TableName='faceRecoSing1',               
                        Key={'RekognitionId': {'S': match['Face']['FaceId']}}
                        )
                    if 'Item' in face:
                        person = face['Item']['FullName']['S']
                        # font = ImageFont.truetype(r'/home/hieu98/Documents/FaceReco1/font-times-new-roman.ttf', 9)
                        # text = "Person:"+ person
                        # draw.multiline_text((left,top-10), text, font = font, stroke_width = 3, fill ="red")
                        # draw.multiline_text((left,top), "Person: "+ person, stroke_width = 3, fill=(255, 0, 0))
                        # image.show()
                        draw_rect = cv2.rectangle(img=image_path0,
                                                    pt1=(int(left), int(top)),
                                                    pt2=(int(left+width), int(top+height)),
                                                    color=[0, 0, 255],
                                                    thickness=1,
                                                    lineType=cv2.LINE_AA,
                                                    shift=0)
                        # # Save person-reco
                        # if person != sheet["A{}".format(numFace)]:
                        #     sheet["A{}".format(numFace)] = person
                        #     sheet["A{}".format(numFace)].value
                        #     wb.save('excelCreate.xlsx')
                        #     numFace += 1
                        # else:
                        #     sheet["A{}".format(numFace)] = person
                        #     sheet["A{}".format(numFace)].value
                        #     wb.save('excelCreate.xlsx')
                    else:
                        person = None
                    if person == None:
                            sheet["A{}".format(numFace)] = person
                            sheet["A{}".format(numFace)].value
                            wb.save('excelCreate.xlsx')
                            
                    elif person != sheet["A{}".format(numFace)]:
                        sheet["A{}".format(numFace)] = person
                        sheet["A{}".format(numFace)].value
                        wb.save('excelCreate.xlsx')
                        numFace += 1
                    else:
                        sheet["A{}".format(numFace)] = person
                        sheet["A{}".format(numFace)].value
                        wb.save('excelCreate.xlsx')

                    t5 = time.time()
                    print ("Độ tin cậy: ",match['Face']['Confidence'],"\nPerson:", person)
                    print("Time xử lý: ", t5-t2)
        # Sử dụng file để speech
        text2speech()
        cv2.imshow("face-recognition", image_path0)
        cam.release()
        k = cv2.waitKey(1)
        if k%256 == 27:
        # ESC pressed
            print("closing")
            break
    cam.release()
    cv2.destroyAllWindows()













    

    