# Background Image. We are using this to record the background image.
import cv2
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, back = cap.read()  # ret means that the camera is working. So if it is working then 1.
    if ret:
        cv2.imshow("image", back)
        if cv2.waitKey(30) == ord("q"):
            # waitkey is basically waiting for any change or cmd for the given amount of time and 
            # then if nothing happens another pic is clicked. ord is giving unicode of q.
            cv2.imwrite("back.jpg", back)
            break

cap.release()
cv2.destroyAllWindows()