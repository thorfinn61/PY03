import math


def calculate_distance(point1: int, point2: int):
    return math.sqrt(
        (point2[0] - point1[0])**2 +
        (point2[1] - point1[1])**2 +
        (point2[2] - point1[2])**2
    )


if __name__ == "__main__":
    print("=== Game Coordinate System ===\n")
    p1 = (10, 20, 5)
    p2 = (0, 0, 0)
    distance = calculate_distance(p1, p2)
    print(f"Position created: {p1}")
    print(f"Distance Between (0, 0, 0) and {p1}: {distance:.2f}")
    coordinates = "3, 4, 0"
    print(f'\nParsing coordinates: "{coordinates}"')
    parsed_coordinates = tuple(int(x) for x in coordinates.split(","))
    print(f"Parsed position: {parsed_coordinates}")
    new_distance = calculate_distance(parsed_coordinates, p2)
    print(
        f"Distance between (0, 0, 0) and {parsed_coordinates}: "
        f"{new_distance:.1f}"
    )
    invalid = "abc,def,ghi"
    print(f'\nParsing invalid coordinates: "{invalid}"')
    try:
        parse = tuple(int(x) for x in invalid.split(","))
    except ValueError as e:
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type: {type(e).__name__}, Args: {e.args}")
    print("\nUnpacking demonstration:")
    x, y, z = parsed_coordinates
    print(f"Player at x={x}, y={y}, z={z}")
    print(f"Coordinates: X={x}, Y={y}, Z={z}")
