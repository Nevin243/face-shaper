from camera import capture_face
from shape import face_shape

def main():
    face = capture_face()

    if(face == {}):
        print("No face detected")
        exit(1)

    face_shape(face)

if __name__ == "__main__":
    main()