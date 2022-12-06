from paddleocr import PaddleOCR

ocr = PaddleOCR(lang='ch',det='True',rec='True')

img_path = '/home/pll/datasets/pic_tem/images/test/1.png'

result = ocr.ocr(img_path)

for line in result:
    for i in line:
        print(i)

# import cv2
# img_path = r'/home/pll/datasets/pic_tem/images/test/1.png'
# img=cv2.imread(img_path)
# cv2.imshow('img',img)
# cv2.waitKey(0)
