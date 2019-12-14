import cv2

condition = True

try:
    def capture():
        cap = cv2.VideoCapture(0)

        if cap.isOpened()==True:
            ret, frame =cap.read()
            img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            cv2.imwrite('static/image.jpg', img)
            cap.release()
            cv2.destroyAllWindows()
            print('capture complete....')
        else:
            print('cannot load image....')
            globals()['condition'] = False

except:
    condition = False

if __name__=='__main__':
    capture()