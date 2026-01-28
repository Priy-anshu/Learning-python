import cv2

source='priyanshu.jpeg'
destination='newImage.jpeg'
scale_percentage=50

src=cv2.imread(source, cv2.IMREAD_UNCHANGED)

if src is None:
    print("no image found")
else :

    # just want to see the image

    # cv2.imshow("see image" , src)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    # want to resize the image

    new_width=int(src.shape[1] * scale_percentage /100)
    new_height=int(src.shape[0] * scale_percentage /100)
    output=cv2.resize(src,(new_width,new_height))
    # only want to reduce the weidth and height
    cv2.imwrite(destination,output)

    # if want to reduce the disk size too
    # cv2.imwrite(destination,output, [cv2.IMWRITE_JPEG_QUALITY,50])