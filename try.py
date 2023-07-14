import cv2
import numpy as np 
import torch 

model = torch.load(path= "best.pt",force_reload=True)
model.evaluate('train\images\IMG_20230714_104442.jpg')


# cap = cv2.VideoCapture(0)
# while cap.isOpened():
#     ret, frame = cap.read()
    
#     # Make detections 
#     results = model(frame)
    
#     cv2.imshow('Detections', np.squeeze(results.render()))
    
#     if cv2.waitKey(10) & 0xFF == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()

# yolo task=detect mode=predict model=best.pt show=True conf=0.5 source=0 line_thickness=1