

#no anglemode
class Face:
    def __init__(self):
        self.x=400/2
        self.y=400/2
        self.xSpeed=random(1,4)
        self.ySpeed=random(1, 3)
        self.happy=True;
      
face=Face()
#print(face.x)
nextSmile=0
siz = 50  
def setup():
  size(400, 400);
  #angleMode(DEGREES);


def draw():
  global face, nextSmile, siz
  background(220)
  #print(siz)
  # Face
  if face.happy==True:
    print("happy")
    fill(255, 201, 58)
  else: 
    fill(200, 0, 0)
    
  stroke_weight(2);
  ellipse(face.x, face.y, siz, siz);
  print(face.y)
  # Eyes
  stroke_weight(siz / 7);
  point(face.x - siz / 6, face.y - siz / 8);
  point(face.x + siz / 6, face.y - siz / 8);

  #mouth depends on happy value
  stroke_weight(3);
  if face.happy:
    # Smile
    arc(face.x, face.y + 0.1 * siz, 0.4 * siz, 0.4 * siz, radians(30), radians(150));
  else:
    # Frown
    arc(face.x, face.y + 0.3 * siz, 0.4 * siz, 0.4 * siz, 3.67, 5.76);

    # Angry brow
    line(
      face.x - 0.15 * siz,
      face.y - 0.2 * siz,
      face.x - 0.3 * siz,
      face.y - 0.25 * siz
    )
    line(
      face.x + 0.15 * siz,
      face.y - 0.2 * siz,
      face.x + 0.3 * siz,
      face.y - 0.25 * siz
    )
  # Move the face
  face.x += face.xSpeed
  face.y += face.ySpeed

  # Is it time to be happy?
  if frame_count == nextSmile:
    face.happy = True

  #Check for collision with sides
  if face.x < siz / 2 or face.x > width - siz / 2:
    face.xSpeed *= -1
    face.happy = False
    nextSmile = frame_count + 40

  # Check for collision with top and bottom
  if face.y < siz / 2 or face.y > height - siz / 2:
    face.ySpeed *= -1
    face.happy = False
    nextSmile = frame_count + 40