from ultralytics import YOLO
import cv2

# Load the model
model = YOLO("my_model.pt")

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        break
    results = model.predict(source=frame, conf=0.3, verbose=False)   
    
    ann = results[0].plot()
 
    cv2.imshow("YOLOv8 Real-Time Detection", ann)

 
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
