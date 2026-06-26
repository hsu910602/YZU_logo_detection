import cv2
import os

finalCascadeFile = 'classifier/cascade.xml'
cascade_limestone = cv2.CascadeClassifier(finalCascadeFile)

test_dir = 'test'
op_dir = 'op'

if not os.path.exists(op_dir):
    os.makedirs(op_dir)


for filename in os.listdir(test_dir):
    if filename.endswith(".jpg") or filename.endswith(".png") or filename.endswith(".jpeg"):
        img_path = os.path.join(test_dir, filename)
        image = cv2.imread(img_path)               
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        rectangles = cascade_limestone.detectMultiScale(
            gray, 
            scaleFactor=1.05, 
            minNeighbors=15,     
            minSize=(25, 25)     
        )     

        for (x, y, w, h) in rectangles:
            cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)
        output_path = os.path.join(op_dir, filename)
        cv2.imwrite(output_path, image)
        