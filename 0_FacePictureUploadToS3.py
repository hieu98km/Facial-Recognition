import boto3
s3 = boto3.resource('s3')
# Get list of objects for indexing
images=[('001.jpg','0'),
      ('002.jpg','1'),
      ('003.jpg','2'),
      ('004.jpg','3'),
      ('005.jpg','4'),
      ('006.jpg','5'),
      ('007.jpg','6'),
      ('008.jpg','7'),
      ('009.jpg','8'),
      ('010.jpg','9'),
      ('011.jpg','10'),
      ('012.jpg','11'),
      ('013.jpg','12'),
      ('014.jpg','13'),
      ('015.jpg','14'),
      ('016.jpg','15'),
      ('017.jpg','16'),
      ('018.jpg','17'),
      ('019.jpg','18'),
      ('020.png','19'),
      ('021.jpg','20'),
      ('022.jpg','21'),
      ('023.jpg','22'),
      ('024.jpg','23'),
      ('025.jpg','24'),
      ('026.jpg','25'),
      ('027.jpg','26'),
      ('028.jpg','27'),
      ('029.jpg','28'),
      ('030.png','29'),
      ('031.jpg','30'),
      ('032.jpg','31'),
      ('033.jpg','32'),
      ('034.jpg','33'),
      ('035.jpg','34'),
      ('036.jpg','35'),
      ('037.jpg','36'),
      ('038.jpg','37'),
      ]
# Iterate through list to upload objects to S3   
for image in images:
    file = open(image[0],'rb')
    object = s3.Object('face-reco-sing','index/'+ image[0])
    ret = object.put(Body=file,
                    Metadata={'FullName':image[1]}
                    )
