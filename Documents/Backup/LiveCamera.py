import cv2

def liveCam1():
    # define a video capture object
    cam = cv2.VideoCapture(0)
    cv2.namedWindow("test1")
    while(True):
        # Capture the video frame by frame
        ret, frame = cam.read()
        # Display the resulting frame
        cv2.imshow('frame', frame)
        # the 'q' button is set as the quitting
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    # After the loop release the cap object
    cam.release()
    # Destroy all the windows
    cv2.destroyAllWindows()

def liveCam2():
    cam = cv2.VideoCapture(0)
    cv2.namedWindow("test2")
    img_counter = 0
    while True:
        ret, frame = cam.read()
        if not ret:
            print("failed to grab frame")
            break
        cv2.imshow("test", frame)
        k = cv2.waitKey(1)
        if k%256 == 27:
            # ESC pressed
            print("closing")
            break
        elif k%256 == 32:
            # SPACE pressed
            img_name = "opencv_frame_{}.png".format(img_counter)
            cv2.imwrite(img_name, frame)
            print("{} written!".format(img_name))
            img_counter += 1
    cam.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    liveCam1()

