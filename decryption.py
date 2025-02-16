import cv2


img = cv2.imread("encryptedImage.png")


c = {i: chr(i) for i in range(255)}


retrieved_password_length = img[0, 0, 0]


retrieved_password = ""
for i in range(retrieved_password_length):
    retrieved_password += c[img[0, i + 1, 0]]


pas = input("Enter passcode for Decryption: ")


if retrieved_password == pas:
    
    retrieved_msg_length = img[1, 0, 0]

  
    message = ""
    n, m, z = 1, 1, 0  
    for i in range(retrieved_msg_length):
        message += c[img[n, m, z]]
        m += 1
        if m >= img.shape[1]:
            
            m = 0
            n += 1

    print("Decryption message:", message)
else:
    print("YOU ARE NOT AUTHORIZED")
