from mlproject.distance import haversine


def test_distance():
    distance = haversine(2.380009, 48.865070, 2.4, 49.)

    assert type(distance) == float
    assert distance == 15.074432154120332
