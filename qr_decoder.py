
import sys
import os
import cv2


def decode(filename):

    # read the QRCODE image
    image = cv2.imread(filename)
    # initialize the cv2 QRCode detector
    detector = cv2.QRCodeDetector()
    # detect and decode
    data, vertices_array, binary_qrcode = detector.detectAndDecode(image)
    # if there is a QR code
    # print the data
    if vertices_array is not None:
        print("QRCode data:")
        print(data)
    else:
        print("There was some error")


def main():

    if len(sys.argv) > 1:
        f = ''.join(sys.argv[1:])
        if os.path.exists(f) and os.path.isfile(f):
            decode(f)
    else:
        pass


if __name__ == '__main__':
    main()
