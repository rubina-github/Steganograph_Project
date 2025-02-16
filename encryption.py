import cv2
import os


img = cv2.imread("mypic.jpg")  


msg = input("Enter secret message: ")
password = input("Enter a passcode: ")


d = {chr(i): i for i in range(255)}


password_length = len(password)
img[0, 0, 0] = password_length


for i in range(password_length):
    img[0, i + 1, 0] = d[password[i]]


msg_length = len(msg)
img[1, 0, 0] = msg_length


n, m, z = 1, 1, 0  
for i in range(msg_length):
    img[n, m, z] = d[msg[i]]
    m += 1  
    if m >= img.shape[1]:  
        m = 0
        n += 1


cv2.imwrite("encryptedImage.png", img)
os.system("start encryptedImage.png")  

print("Encryption completed! The message is hidden inside encryptedImage.png.")
