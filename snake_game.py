import math
import random
import cv2
import cvzone
import numpy as np
import time
from cvzone.HandTrackingModule import HandDetector

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

detector = HandDetector(detectionCon=0.8, maxHands=1)


class SnakeGame:
    def __init__(self, foodPath):
        self.foodImg = cv2.imread(foodPath, cv2.IMREAD_UNCHANGED)
        self.foodImg = cv2.resize(self.foodImg, (20, 20))
        self.hFood, self.wFood, _ = self.foodImg.shape
        self.reset()

    def reset(self):
        self.points = []
        self.lengths = []
        self.currentLength = 0
        self.allowedLength = 150
        self.prevHead = None
        self.score = 0
        self.gameOver = False
        self.startTime = time.time()
        self.foods = [self.randomFood() for _ in range(5)]

    def randomFood(self):
        return random.randint(100, 1180), random.randint(100, 620)

    def update(self, img, head):

        if self.gameOver:
            cvzone.putTextRect(img, "GAME OVER", (420, 300), scale=4, thickness=4)
            cvzone.putTextRect(img, f"Score: {self.score}", (480, 380), scale=3)
            cvzone.putTextRect(img, "Press R", (520, 460), scale=2)
            return img

        if self.prevHead is None:
            self.prevHead = head
            return img

        cx, cy = head
        px, py = self.prevHead

        if abs(cx - px) > 80 or abs(cy - py) > 80:
            self.prevHead = head
            return img

        self.points.append((cx, cy))
        dist = math.hypot(cx - px, cy - py)
        self.lengths.append(dist)
        self.currentLength += dist
        self.prevHead = (cx, cy)

        while self.currentLength > self.allowedLength:
            self.currentLength -= self.lengths[0]
            self.lengths.pop(0)
            self.points.pop(0)

        for i, (fx, fy) in enumerate(self.foods):
            if fx - self.wFood < cx < fx + self.wFood and fy - self.hFood < cy < fy + self.hFood:
                self.foods[i] = self.randomFood()
                self.allowedLength += 40
                self.score += 1

        for i in range(1, len(self.points)):
            cv2.line(img, self.points[i - 1], self.points[i], (0, 0, 255), 15)

        if self.points:
            cv2.circle(img, self.points[-1], 15, (0, 255, 0), cv2.FILLED)

        for fx, fy in self.foods:
            img = cvzone.overlayPNG(img, self.foodImg, (fx - 10, fy - 10))

        cvzone.putTextRect(img, f"Score: {self.score}", (40, 70), scale=2)

        if time.time() - self.startTime > 1.5 and len(self.points) > 25:
            pts = np.array(self.points[:-10], np.int32)
            pts = pts.reshape((-1, 1, 2))
            if cv2.pointPolygonTest(pts, (cx, cy), True) > -10:
                self.gameOver = True

        return img


game = SnakeGame("Donut.png")


while True:
    success, img = cap.read()
    if not success:
        break

    img = cv2.flip(img, 1)
    hands, img = detector.findHands(img)

    if hands:
        finger = hands[0]["lmList"][8][:2]
        img = game.update(img, finger)

    cv2.imshow("Snake Game", img)

    key = cv2.waitKey(1) & 0xFF

    if key == ord('r'):
        game.reset()

    elif key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

        


