from easypipe.source import Video
from easypipe.face import TrackFace


def test_face_tracking():
    webcam = Video()
    face = TrackFace()

    for data, image in face.process(webcam.stream):
        print(data, image)
