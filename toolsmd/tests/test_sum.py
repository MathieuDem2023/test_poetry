from ..whisper.sum import (sum, moyenne_liste)


def test_sum():
    assert sum(2, 3) == 5
    assert sum('a', 'b') == 'ab'
    print("test_sum passed")


def test_moyenne_liste():
    assert moyenne_liste([1, 2, 3]) == 2
    assert moyenne_liste([1, 2, 3, 4, 5]) == 3
    assert moyenne_liste([1, 2, 3, 4, 5, 6]) == 3.5
    print("test_moyenne_liste passed")


if __name__ == '__main__':
    test_sum()
    test_moyenne_liste()
    print("Everything passed")
