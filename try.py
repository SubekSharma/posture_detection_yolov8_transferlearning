cap = cv2.videoCapture(0)
while cap.isOpened():
    ret, frame = cap.read()

    #Make detections 
    results = model(frame)

    cv2.imshow('YOLO',np.squeeze(results.render()))

    if cv2.waitkey(10) & 0xFF == ord('q'):
        break 
cap.release()
cv2.destroyAllwindows()