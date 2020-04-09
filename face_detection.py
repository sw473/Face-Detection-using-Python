# import required packages

import PIL.Image
import PIL.ImageDraw
import face_recognition


image_file = face_recognition.load_image_file("image.jpg")   # To convert jpg file into numpy array


face_locator = face_recognition.face_locations(image_file)   # Locate all the faces in the given image

Number_of_faces = len(face_locator)
print("Found {} face in the given image.".format(Number_of_faces))


image_pil = PIL.Image.fromarray(image_file)   # To convert the image into a Python Image Library object so that we can draw shapes on it and display it

for i in face_locator:

    # To print the location of the images.
    top, right, bottom, left = i
    print("Found faces  at the following pixel locations Top: {}, Left: {}, Bottom: {}, Right: {}".format(top, left, bottom, right))

    # To draw a rectangle around the face
    draw_rectangle = PIL.ImageDraw.Draw(image_pil)
    draw_rectangle.rectangle([left, top, right, bottom], outline="black", width=3)


image_pil.show()   # For displaying the image on screen
