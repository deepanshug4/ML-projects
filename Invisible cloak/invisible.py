import cv2
import numpy as np

cap = cv2.VideoCapture(0)
back = cv2.imread('./back.jpg')

while cap.isOpened():
    ret, frame = cap.read()

    if ret:
        # hsv: Hue Saturation Value. The way human eyes perceive colors
        # hue --> the color
        # saturation --> the ratio with white color
        # value --> the ratio with black color
        hsv = cv2.cvtColor(frame,  cv2.COLOR_BGR2HSV)
        # cv2.imshow("hsv", hsv)
        rgb = np.uint8([[[0,0,255]]])
        hsv_red = cv2.cvtColor(rgb, cv2.COLOR_BGR2HSV)
        # print(hsv_red)
        # threshold only red color to pick it up.
        # range lower = hue-10, 100, 100; upper = hue + 10, 255, 255
        l_red = np.array([0, 100, 100])
        u_red = np.array([10, 255, 255])
        mask = cv2.inRange(hsv, l_red, u_red)
        # cv2.imshow("mask", mask)
        # part1 is all the parts that are red.
        part1 = cv2.bitwise_and(back, back, mask=mask)
        # cv2.imshow("part1", part1)

        # part2 is for everything except red
        mask = cv2.bitwise_not(mask)
        part2 = cv2.bitwise_and(frame, frame, mask=mask)
        # cv2.imshow("part2", part2)

        cv2.imshow("final cloak", part1+part2)
        if cv2.waitKey(30) == ord("q"):
            break

cap.release()
cv2.destroyAllWindows()