# -*- coding: utf-8 -*-
import time
import cv2

cascade_src = "xml_file/cars.xml"
# video_src = "dataset/lightest_traffic_1.mp4"
# video_src = "dataset/lightest_traffic_2.mp4"
video_src = "dataset/lightest_traffic_4.mp4"

# video_src =  "dataset/heavier_traffic_1.mp4"
# video_src = "dataset/heavier_traffic_2.mp4"
# video_src = "dataset/heavier_traffic_3.mp4"
# video_src = "dataset/heavier_traffic_5.mp4"


# video_src = "dataset/heaviest_traffic_1.mp4"
# video_src = "dataset/heaviest_traffic_2.mp4"
# video_src = "dataset/heaviest_traffic_3.mp4"
# video_src = "dataset/heaviest_traffic_4.mp4"
# video_src = "dataset/heaviest_traffic_5.mp4"

cap = cv2.VideoCapture(video_src)
car_cascade = cv2.CascadeClassifier(cascade_src)

def rescaleFrame(frame, scale=6):
  # works for images, video, and live video
  width = int (frame.shape[1] *scale)
  height = int(frame.shape[0] *scale)
  dimensions = (width, height)

  return cv2.resize(frame, dimensions, interpolation=cv2.INTER_AREA)

while True:
    start_time = time.time()  # Start timer
    ret, car_video = cap.read()
    if (type(car_video) == type(None)):
        break
    
    gray = cv2.cvtColor(car_video, cv2.COLOR_BGR2GRAY)
    
    cars = car_cascade.detectMultiScale(gray, 1.1, 2)

    # draw rectangles around detected cars
    for (x,y,w,h) in cars:
        cv2.rectangle(car_video,(x,y),(x+w,y+h),(0,0,255),2)      
        
    # Display the number of cars detected
    car_count = len(cars)
    cv2.putText(car_video, f'Cars detected: {car_count}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

    # Resize the frames for display
    frame_resized = rescaleFrame(car_video, scale=.2)

    # Show the original processed video
    cv2.imshow('Processed Video', frame_resized)
    
 
    # Calculate processing time
    end_time = time.time()
    print(f'Frame processing time: {end_time - start_time:.2f} seconds')

    # close window when escape key is pressed
    if cv2.waitKey(33) == 27:
        break

cv2.destroyAllWindows()
print(car_count)