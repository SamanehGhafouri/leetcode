"""
You are given coordinates, a string that represents the coordinates of a square of the chessboard.
Below is a chessboard for your reference.

Return true if the square is white, and false if the square is black.

The coordinate will always represent a valid chessboard square.
The coordinate will always have the letter first, and the number second.
"""


def square_is_white(coordinates: str) -> bool:
    nums = ['1', '2', '3', '4', '5', '6', '7', '8']
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    if letters.index(coordinates[0]) % 2 == 0 and nums.index(coordinates[1]) % 2 != 0 or letters.index(
            coordinates[0]) % 2 != 0 and nums.index(coordinates[1]) % 2 == 0:
        return True
    return False


if __name__ == '__main__':
    co = "c7"
    print(square_is_white(co))
