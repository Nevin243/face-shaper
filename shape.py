from math import sqrt, isclose

PERCISION = 2
SQUARE = 2
FULL_JAW = 2

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

    # Show user some sizing -> handwave
    print("Relative shape sizing:")
    print("Cheekbone Width: " + str(cheekbone_width))
    print("Forehead Width: " + str(forehead_width))
    print("Face Length: " + str(face_length))
    print("Jawline Length: " + str(jaw_length))

    # TODO Fix this condition ELIF Nightmare
    # Face Length > Cheekbone Width > Forehead Width > Jawline == diamond
    if((face_length > cheekbone_width) and (cheekbone_width > forehead_width) and (forehead_width > jaw_length)):
        print("Diamond")

    # Forehead Width > Cheekbone Width > Jawline [Pointed Chin] == heart
    elif((forehead_width > cheekbone_width) and (cheekbone_width > jaw_length)):
        print("heart")

    # Face Length > (Cheekbone Width ≈ Forehead Width ≈ Jawline) == oblong
    elif((face_length > jaw_length) and (isclose(cheekbone_width, forehead_width, abs_tol=10**-PERCISION)) and (isclose(jaw_length, forehead_width, abs_tol=10**-PERCISION))):
        print("oblong")

    # Face Length > Cheekbone Width & Forehead Width > Jawline == oval
    elif((face_length > cheekbone_width) and (isclose(cheekbone_width, forehead_width, abs_tol=10**-PERCISION)) and (cheekbone_width > jaw_length)):
        print("oval")

    # (Face Length ≈ Cheekbone Width) > (Forehead Width ≈ Jawline) [Rounded Jaw] == round
    elif((isclose(face_length, cheekbone_width, abs_tol=10**-PERCISION)) and (cheekbone_width > forehead_width) and (isclose(forehead_width, jaw_length, abs_tol=10**-PERCISION))):
        print("round")

    # Face Length ≈ Cheekbone Width ≈ Forehead Witch ≈ Jawline [Hard Jawed] == square
    elif((isclose(cheekbone_width, face_length, abs_tol=10**-PERCISION)) and (isclose(cheekbone_width, forehead_width, abs_tol=10**-PERCISION)) and (isclose(jaw_length, forehead_width, abs_tol=10**-PERCISION))):
        print("square")

    # Jawline > Cheekbone Width > Forehead Width == triage
    elif((jaw_length > cheekbone_width) and  (cheekbone_width > forehead_width)):
        print("Triangle")
 
    # Base case - All else fails?
    else:
        print("Not sure! Try staying centre frame!")