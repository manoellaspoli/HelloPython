import cv2

cap = cv2.VideoCapture(0)

# Check if the webcam is opened correctly
if not cap.isOpened():
    raise IOError("Cannot open webcam")

while True:
    ret, frame = cap.read()
    #frame = cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    img = cv2.GaussianBlur(frame,(3,3),0)
    laplacian = cv2.Laplacian(img,cv2.CV_64F)

    cv2.imshow('image Original', frame)
    cv2.imshow('imagem Cinza', gray)

    cv2.imshow('imagem Gaussian', img)
    cv2.imshow('imagem Laplacian', laplacian)

    c = cv2.waitKey(1)
    if c == 27:
        break

cap.release()
cv2.destroyAllWindows()