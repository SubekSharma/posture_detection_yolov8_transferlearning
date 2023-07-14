from ultralytics import YOLO 

#Load a model 
model = YOLO('yolo8m.pt')

#Train the model 
model.train(data='custom_data.yaml',epochs=100,imgsz=640,batch=8,name='yolov8m_custom')