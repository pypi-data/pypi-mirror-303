from ldkex.archive import Metadata
from ldkex.utils import read_coordinate, read_int, get_metadata_version


class Location:
    def __init__(self, file, version):
        self.size = read_int(file)
        current_location = file.tell()
        self.longitude = read_coordinate(file)
        self.latitude = read_coordinate(file)
        file.seek(current_location + self.size)


class Locations:
    def __init__(self, file, version):
        self.locations_count = read_int(file)
        self.locations = []

        for i in range(self.locations_count):
            try:
                self.locations.append(Location(file, version))
            except Exception as e:
                print("Location content does not meet doc specification")
                break


class AreaPolygon:
    def __init__(self, file, version):
        self.metadata = Metadata(file, get_metadata_version(version, "are"))
        self.locations = Locations(file, version)
        self.number_of_holes = read_int(file)
        self.holes = []

        for _ in range(self.number_of_holes):
            try:
                self.holes.append(Locations(file, version))
            except Exception as e:
                print("Locations content does not meet doc specification")
                break


class AreaPolygons:
    def __init__(self, file, version):
        self.polygons_count = read_int(file)
        self.polygons = []

        for _ in range(self.polygons_count):
            try:
                self.polygons.append(AreaPolygon(file, version))
            except Exception as e:
                print("AreaPolygon content does not meet doc specification")
                break


class AreaFile:
    def __init__(self, file, file_metadata_map):
        self.file_metadata_map = file_metadata_map
        self.magic_number = read_int(file)
        file_magic = (self.magic_number >> 8) & 0xFFFFFF  # Shift right by 8 bits and mask with 0xFFFFFF
        version = self.magic_number & 0xFF  # Mask with 0xFF

        if (self.magic_number & 0x50500000) == 0x50500000:
            version = (self.magic_number & 0xFF) + 100

        if file_magic != 0x50500D:
            print(f"Area file magic: {file_magic} version: {version}")

        self.header_size = read_int(file)

        if version < 100:
            file.seek(file.tell() + self.header_size)
        else:
            _ = Metadata(file, get_metadata_version(version, "are"))

        self.metadata = Metadata(file, get_metadata_version(version, "are"))
        self.polygons = AreaPolygons(file, version)


class Waypoint:
    def __init__(self, file, version, file_type):
        self.metadata = Metadata(file, get_metadata_version(version, file_type))
        self.location = Location(file, version)


class Waypoints:
    def __init__(self, file, version, file_type):
        self.waypoints_count = read_int(file)
        self.waypoints = []

        for _ in range(self.waypoints_count):
            try:
                self.waypoints.append(Waypoint(file, version, file_type))
            except Exception as e:
                print("Waypoint content does not meet doc specification")
                break


class RouteFile:
    def __init__(self, file, file_metadata_map):
        self.file_metadata_map = file_metadata_map
        self.magic_number = read_int(file)
        file_magic = (self.magic_number >> 8) & 0xFFFFFF  # Shift right by 8 bits and mask with 0xFFFFFF
        version = self.magic_number & 0xFF  # Mask with 0xFF

        if (self.magic_number & 0x50500000) == 0x50500000:
            version = (self.magic_number & 0xFF) + 100

        if file_magic != 0x50500C:
            print(f"Route file magic: {file_magic} version: {version}")

        self.header_size = read_int(file)

        if version < 100:
            file.seek(file.tell() + self.header_size)
        else:
            _ = Metadata(file, get_metadata_version(version, "rte"))

        self.metadata = Metadata(file, get_metadata_version(version, "rte"))
        self.waypoints = Waypoints(file, version, "rte")


class TrackSegment:
    def __init__(self, file, version, file_type):
        if version >= 3:
            self.metadata = Metadata(file, get_metadata_version(version, "trk"))
        else:
            read_int(file)
        self.locations = Locations(file, version)


class TrackSegments:
    def __init__(self, file, version, file_type):
        try:
            self.segments_count = read_int(file)
        except Exception as e:
            print("TrackSegments content does not meet doc specification")
            self.segments_count = 0
        self.segments = []

        for _ in range(self.segments_count):
            try:
                self.segments.append(TrackSegment(file, version, file_type))
            except Exception as e:
                print("TrackSegment content does not meet doc specification")
                break


class TrackFile:
    def __init__(self, file, file_metadata_map):
        self.file_metadata_map = file_metadata_map
        self.magic_number = read_int(file)
        file_magic = (self.magic_number >> 8) & 0xFFFFFF  # Shift right by 8 bits and mask with 0xFFFFFF
        version = self.magic_number & 0xFF  # Mask with 0xFF

        if (self.magic_number & 0x50500000) == 0x50500000:
            version = (self.magic_number & 0xFF) + 100

        if file_magic != 0x50500E:
            print(f"Track file magic: {file_magic} version: {version}")

        self.header_size = read_int(file)

        if version < 100:
            file.seek(file.tell() + self.header_size)
        else:
            _ = Metadata(file, get_metadata_version(version, "trk"))

        self.metadata = Metadata(file, get_metadata_version(version, "trk"))
        self.waypoints = Waypoints(file, version, "trk")
        self.track_segments = TrackSegments(file, version, "set")


class WaypointFile:
    def __init__(self, file, file_metadata_map):
        self.file_metadata_map = file_metadata_map
        self.magic_number = read_int(file)
        file_magic = (self.magic_number >> 8) & 0xFFFFFF  # Shift right by 8 bits and mask with 0xFFFFFF
        version = self.magic_number & 0xFF  # Mask with 0xFF

        if (self.magic_number & 0x50500000) == 0x50500000:
            version = (self.magic_number & 0xFF) + 100

        if file_magic != 0x50500A:
            print(f"Wpt file magic: {file_magic} version: {version}")

        self.header_size = read_int(file)
        file.seek(file.tell() + self.header_size)
        self.waypoint = Waypoint(file, version, "wpt")


class PointsSet:
    def __init__(self, file):
        self.magicNumber = read_int(file)
        fileMagic = (self.magicNumber >> 8) & 0xFFFFFF
        version = self.magicNumber & 0xFF
        if (self.magicNumber & 0x50500000) == 0x50500000:
            version = (self.magicNumber & 0xFF) + 100

        if fileMagic != 0x50500B:
            print(f"Set file magic: {fileMagic} version: {version}")

        self.headerSize = read_int(file)

        if version < 100:
            file.seek(file.tell() + self.headerSize)
        else:
            Metadata(file, get_metadata_version(version, "set"))

        self.metadata = Metadata(file, get_metadata_version(version, "set"))
        self.waypoints = Waypoints(file, version, "set")


class PointsSetFile:
    def __init__(self, file, file_metadata_map):
        self.file_metadata_map = file_metadata_map
        self.magicNumber = read_int(file)
        fileMagic = (self.magicNumber >> 8) & 0xFFFFFF
        version = self.magicNumber & 0xFF
        if (self.magicNumber & 0x50500000) == 0x50500000:
            version = (self.magicNumber & 0xFF) + 100

        if fileMagic != 0x50500B:
            print(f"Set file magic: {fileMagic} version: {version}")

        self.headerSize = read_int(file)

        if version < 100:
            file.seek(file.tell() + self.headerSize)
        else:
            Metadata(file, get_metadata_version(version, "set"))

        self.metadata = Metadata(file, get_metadata_version(version, "set"))
        self.waypoints = Waypoints(file, version, "set")
