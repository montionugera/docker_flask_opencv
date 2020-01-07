import cv2
import numpy
def get_np_array_from_file(request_file_upload):
    filestr = request_file_upload.read()
    # convert string data to numpy array
    npimg = cv2.imdecode(numpy.fromstring(filestr, numpy.uint8), cv2.IMREAD_UNCHANGED)
    return npimg

def de_blur(image_2d, threshold=100):
    lp = cv2.Laplacian(image_2d, cv2.CV_64F).var()
    if lp < threshold:
        kernel = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
        image_2d = cv2.filter2D(image, -1, kernel)
    return image_2d

def de_noise(image_2d):
    gray = cv2.cvtColor(image_2d, cv2.COLOR_BGR2GRAY)
    image_2d = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 199, 55)
    return image_2d