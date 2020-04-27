from math import sqrt, isclose

PERCISION = 0.05
SQUARE = 2
FULL_JAW = 2

# Internal Printer  
def __print_shape(shape):
    print("Face Shape: " + shape)

def face_shape(data):

    # Bound Height and Width
    face_length = data['Length']
    face_width = data['Width']

    # Get relative sizes
    cheekbone_width = data['upperJawlineRight']['X'] - data['upperJawlineLeft']['X']
    forehead_width = data['rightEyeBrowRight']['X'] - data['leftEyeBrowLeft']['X']
    jawline = (data['midJawlineRight']['X'], data['chinBottom']['Y'])
    chin = (data['chinBottom']['X'], data['chinBottom']['Y'])
    
    # Euclidean distance
    jaw_length = sqrt(sum([(a - b) ** SQUARE for a, b in zip(jawline, chin)]))
    # x2 for full face
    jaw_length = jaw_length * FULL_JAW

    # Show user some sizing -> handwaving
    print("Relative shape sizing:")
    print("Cheekbone Width: " + str(cheekbone_width))
    print("Forehead Width: " + str(forehead_width))
    print("Face Length: " + str(face_length))
    print("Jawline Length: " + str(jaw_length))

    # TODO Fix this condition ELIF Nightmare
    # TODO Revist shape logic - is it right?
    # Forehead Width > Cheekbone Width > Jawline [Pointed Chin] == heart
    if((forehead_width > cheekbone_width) and (cheekbone_width > jaw_length)):
        __print_shape("Heart")

    # Face Length > (Cheekbone Width ≈ Forehead Width ≈ Jawline) == oblong
    elif((face_length > jaw_length) and (isclose(cheekbone_width, forehead_width, abs_tol=PERCISION)) and (isclose(jaw_length, forehead_width, abs_tol=PERCISION))):
        __print_shape("Oblong")

     # Face Length > Cheekbone Width > Forehead Width > Jawline == diamond
    elif((face_length > cheekbone_width) and (cheekbone_width > forehead_width) and (forehead_width > jaw_length)):
        __print_shape("Diamond")

    # Face Length > Cheekbone Width & Forehead Width > Jawline == oval
    elif((face_length > cheekbone_width) and (isclose(cheekbone_width, forehead_width, abs_tol=PERCISION)) and (cheekbone_width > jaw_length)):
        __print_shape("Oval")

    # (Face Length ≈ Cheekbone Width) > (Forehead Width ≈ Jawline) [Rounded Jaw] == round
    elif((isclose(face_length, cheekbone_width, abs_tol=PERCISION)) and (cheekbone_width > forehead_width) and (isclose(forehead_width, jaw_length, abs_tol=PERCISION))):
        __print_shape("Round")

    # Face Length ≈ Cheekbone Width ≈ Forehead Witch ≈ Jawline [Hard Jawed] == square
    elif((isclose(cheekbone_width, face_length, abs_tol=PERCISION)) and (isclose(cheekbone_width, forehead_width, abs_tol=PERCISION)) and (isclose(jaw_length, forehead_width, abs_tol=PERCISION))):
        __print_shape("Square")

    # Jawline > Cheekbone Width > Forehead Width == triage
    elif((jaw_length > cheekbone_width) and  (cheekbone_width > forehead_width)):
        __print_shape("Triangle")
 
    # Base case - All else fails?
    else:
        __print_shape("Not sure! Try staying centre frame!")