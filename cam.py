import cv2
import time

# Replace with your IP camera URL
# Example: "http://192.168.1.10:8080/video"
url = "HERE_IS_YOUR_IP"

cap = cv2.VideoCapture(url)

if not cap.isOpened():
    print("❌ Error: Cannot connect to IP Camera")
    exit()

prev_time = 0

while True:
    ret, frame = cap.read()

    if not ret or frame is None:
        print("⚠ Frame not received")
        break

    # FPS calculation
    curr_time = time.time()
    fps = 1 / (curr_time - prev_time) if prev_time != 0 else 0
    prev_time = curr_time

    cv2.putText(
        frame,
        f"FPS: {int(fps)}",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2
    )

    cv2.imshow("IP Camera Stream", frame)

    key = cv2.waitKey(1) & 0xFF

    if key == ord('q'):
        break

    elif key == ord('s'):
        filename = f"screenshot_{int(time.time())}.jpg"
        cv2.imwrite(filename, frame)
        print(f"📸 Screenshot saved: {filename}")

cap.release()
cv2.destroyAllWindows()
