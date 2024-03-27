import cv2

video_path = r'C:\Users\aram_\Downloads\videos to test tracking\humanwalking.mp4'

cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Error: Could not open video file")
    exit()

ret, frame = cap.read()

if not ret:
    print("Error: Could not read first frame")
    exit()

bbox = cv2.selectROI("Select object", frame)

cv2.destroyWindow("Select object")

tracker = cv2.TrackerCSRT_create()

tracker.init(frame, bbox)

while True:
    ret, frame = cap.read()

    if not ret:
        print("No more frames to read")
        break

    success, bbox = tracker.update(frame)

    if success:
        x, y, w, h = bbox

        centroid_x = x + w // 2
        centroid_y = y + h // 2

        cross_size = 10
        cv2.line(frame, (centroid_x - cross_size, centroid_y), (centroid_x + cross_size, centroid_y), (0, 0, 255), 1)
        cv2.line(frame, (centroid_x, centroid_y - cross_size), (centroid_x, centroid_y + cross_size), (0, 0, 255), 1)

    cv2.imshow('Tracking', frame)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

print("Tracking complete!")

# cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 1)
