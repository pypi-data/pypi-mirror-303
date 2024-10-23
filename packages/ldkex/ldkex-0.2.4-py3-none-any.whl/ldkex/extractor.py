import copy
from collections import defaultdict
from io import BytesIO
from typing import List
from milgeo import Point, Line, Polygon, GeometriesList

from ldkex.archive import LdkFile
from ldkex.geodata import TrackFile, WaypointFile, AreaFile, RouteFile, PointsSetFile


class LdkExtractor:
    def __init__(self):
        self.geometries = GeometriesList()

    def extract(self, file) -> GeometriesList:
        file_extension = file.name.split('.')[-1]

        file_type_map = {
            "set": (PointsSetFile, self._extract_points_from_set_file),
            "trk": (TrackFile, self._extract_lines_from_track_file),
            "wpt": (WaypointFile, self._extract_points_from_waypoint_file),
            "are": (AreaFile, self._extract_polygons_from_area_file),
            "rte": (RouteFile, self._extract_lines_from_route_file)
        }

        if file_extension in file_type_map:
            file_class, extraction_method = file_type_map[file_extension]
            file_data = file.read()
            file_instance = file_class(BytesIO(file_data), file_metadata_map={})
            extraction_method([file_instance])
        else:
            ldk_file = LdkFile(file)
            nodes = ldk_file.data_nodes

            for node in nodes:
                node_file_type = node.file_type
                if node_file_type in file_type_map:
                    file_class, extraction_method = file_type_map[node_file_type]
                    file_instance = file_class(BytesIO(node.total_byte_array_with_additional_blocks),
                                               node.file_metadata_map)
                    extraction_method([file_instance])

        return self.geometries

    def _extract_points_from_waypoint_file(self, waypoints: List[WaypointFile]):
        for waypoint in waypoints:
            file_level_metadata = defaultdict(list)
            for entry in waypoint.waypoint.metadata.main_content.entries:
                file_level_metadata[entry.entry_name].append(str(entry.data))

            self._create_geometry(geometry_type=Point,
                                  name=file_level_metadata["name"][-1] if file_level_metadata["name"] else None,
                                  coordinates=[waypoint.waypoint.location.longitude,
                                               waypoint.waypoint.location.latitude],
                                  metadata=file_level_metadata,
                                  color_string=file_level_metadata["color"][-1] if
                                  file_level_metadata["color"] else '#663399')

    def _extract_lines_from_route_file(self, routes: List[RouteFile]):
        if not routes:
            return
        for route in routes:
            metadata = self._extract_file_level_metadata(route)
            point_metadata = self._extract_waypoint_metadata(route.waypoints.waypoints[0],
                                                             copy.deepcopy(metadata))  # TODO: Check if this is correct
            self._create_geometry(geometry_type=Line,
                                  name=point_metadata["name"][-1] if point_metadata["name"] else None,
                                  coordinates=[[wp.location.longitude, wp.location.latitude] for wp in
                                               route.waypoints.waypoints],
                                  metadata=point_metadata,
                                  color_string=point_metadata["color"][-1]
                                  if point_metadata["color"] else None)

    def _extract_lines_from_track_file(self, tracks: List[TrackFile]):
        if not tracks:
            return
        for track in tracks:
            metadata = self._extract_file_level_metadata(track)
            for wp in track.waypoints.waypoints:
                point_metadata = self._extract_waypoint_metadata(wp, copy.deepcopy(metadata))
                self._create_geometry(geometry_type=Point,
                                      name=point_metadata["name"][-1] if point_metadata["name"] else None,
                                      coordinates=[wp.location.longitude, wp.location.latitude],
                                      metadata=point_metadata,
                                      color_string=point_metadata["color"][-1] if
                                      point_metadata["color"] else '#663399')
            for segment in track.track_segments.segments:
                segment_metadata = self._extract_waypoint_metadata(segment, copy.deepcopy(metadata))
                self._create_geometry(geometry_type=Line,
                                      name=segment_metadata["name"][-1] if segment_metadata["name"] else None,
                                      coordinates=[[loc.longitude, loc.latitude] for loc in
                                                   segment.locations.locations],
                                      metadata=segment_metadata,
                                      color_string=segment_metadata["color"][-1] if
                                      segment_metadata["color"] else None)

    def _extract_polygons_from_area_file(self, areas: List[AreaFile]):
        if not areas:
            return
        for area in areas:
            metadata = self._extract_file_level_metadata(area)
            for polygon in area.polygons.polygons:
                polygon_metadata = self._extract_waypoint_metadata(polygon, copy.deepcopy(metadata))
                self._create_geometry(geometry_type=Polygon,
                                      name=polygon_metadata["name"][-1] if polygon_metadata["name"] else None,
                                      coordinates=[[[loc.longitude, loc.latitude] for loc in
                                                    polygon.locations.locations]],
                                      metadata=polygon_metadata,
                                      color_string=polygon_metadata["color"][-1] if
                                      polygon_metadata["color"] else None)

    def _extract_points_from_set_file(self, point_sets: List[PointsSetFile]):
        if not point_sets:
            return
        for point_set in point_sets:
            metadata = self._extract_file_level_metadata(point_set)
            for wp in point_set.waypoints.waypoints:
                point_metadata = self._extract_waypoint_metadata(wp, copy.deepcopy(metadata))
                self._create_geometry(geometry_type=Point,
                                      name=point_metadata["name"][-1] if point_metadata["name"] else None,
                                      coordinates=[wp.location.longitude, wp.location.latitude],
                                      metadata=point_metadata,
                                      color_string=point_metadata["color"][-1] if
                                      point_metadata["color"] else '#663399')

    def _create_geometry(self, geometry_type, name, coordinates, metadata, color_string, iterations=0):
        try:
            geometry = geometry_type(name=name, coordinates=coordinates, metadata=metadata)
            geometry.find_outline_color(string=color_string)
            geometry.find_sidc()
            self.geometries.add_geometry(geometry)
        except ValueError:
            if iterations < 3:
                self._handle_geometry_creation_error(geometry_type=geometry_type, coordinates=coordinates, name=name,
                                                     metadata=metadata, color_string=color_string,
                                                     iterations=iterations)

    def _handle_geometry_creation_error(self, geometry_type, coordinates, name, metadata, color_string, iterations):
        if geometry_type == Polygon:
            coordinates[0].append(coordinates[0][0])
        if geometry_type == Line:
            coordinates.append(coordinates[0])
        self._create_geometry(geometry_type=geometry_type, name=name, coordinates=coordinates,
                              metadata=metadata, color_string=color_string, iterations=iterations + 1)

    @staticmethod
    def _extract_file_level_metadata(file):
        file_level_metadata = defaultdict(list)
        for key, value in file.file_metadata_map.items():
            file_level_metadata[key].append(value)
        for entry in file.metadata.main_content.entries:
            file_level_metadata[entry.entry_name].append(str(entry.data))
        return file_level_metadata

    @staticmethod
    def _extract_waypoint_metadata(waypoint, base_metadata=None):
        if base_metadata is None:
            base_metadata = defaultdict(list)
        for entry in waypoint.metadata.main_content.entries:
            base_metadata[entry.entry_name].append(str(entry.data))
        return base_metadata
