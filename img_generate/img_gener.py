from MukeshAPI import api

image = api.ai_image("python")
with open("image.jpg", "wb") as file:
    file.write(image)

print("Your image is generated")