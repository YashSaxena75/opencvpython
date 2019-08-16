import cv2
img=cv2.imread('lena.jpg',0)  # 0 or 1 or -1 flags
#print(img) #this will display the image matrix
cv2.imshow('image',img)
k=cv2.waitKey(0)
#print(k)
if k==27:
    exit(0)
elif k==ord('s'):
    print("Saving your image.......")
    cv2.imwrite('lena_copy.jpg',img)
cv2.destroyAllWindows()