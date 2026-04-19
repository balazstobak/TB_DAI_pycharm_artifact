from artifact import Artifact, Painting, Sculpture, give_name_artifact
from renaissance import renaissance_painting, renaissance_sculpture, renaissance_building


def give_name_main():
    return f"main name: {__name__}"


if __name__ == "__main__":
    a1 = Artifact("a1", 1598)
    a2 = Artifact("a2", 1958)
    a3 = Artifact("a3", 1002)

    p1 = Painting("p1", 1587, "art1", "oil")
    p2 = Painting("p2", 902, "art2", "pastel")
    p3 = Painting("p3", 1877, "art3", "crayon")

    s1 = Sculpture("s1", 1950, "marble", 15)
    s2 = Sculpture("s2", 1801, "bronze", 100)

    print(f"{s1.is_old(10)=}")
    print(give_name_artifact())
    print(give_name_main())
    print(__name__)

    print("\n--- Renaissance objects ---")
    print(renaissance_painting)
    print(f"name: {renaissance_painting.name}")
    print(f"date: {renaissance_painting.date}")
    print(f"artist: {renaissance_painting.artist}")
    print(f"medium: {renaissance_painting.medium}")

    print()

    print(renaissance_sculpture)
    print(f"name: {renaissance_sculpture.name}")
    print(f"date: {renaissance_sculpture.date}")
    print(f"material: {renaissance_sculpture.material}")
    print(f"size: {renaissance_sculpture.size}")

    print()

    print(renaissance_building)
    print(f"name: {renaissance_building.name}")
    print(f"date: {renaissance_building.date}")
    print(f"architect: {renaissance_building.architect}")
    print(f"location: {renaissance_building.location}")