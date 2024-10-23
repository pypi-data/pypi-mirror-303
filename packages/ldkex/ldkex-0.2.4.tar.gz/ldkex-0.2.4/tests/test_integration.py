import os

import pytest

from ldkex import LdkExtractor


@pytest.fixture
def setup_extractor():
    extractor = LdkExtractor()
    return extractor


@pytest.mark.parametrize("file_path, "
                         "expected_geometries, "
                         "expected_geometries_no_duplicates, "
                         "expected_points, "
                         "expected_lines, "
                         "expected_polygons, "
                         "expected_points_no_duplicates, "
                         "expected_lines_no_duplicates, "
                         "expected_polygons_no_duplicates", [
                             ('test_data-01.ldk', 242830, 17762, 234713, 6183, 1934, 15620, 1798, 344),
                             ('test_data-02.ldk', 30932, 27215, 28258, 2368, 306, 24715, 2194, 306),
                             ('test_data-03.trk', 1, 1, 0, 1, 0, 0, 1, 0),
                             ('test_data-04.ldk', 205, 205, 205, 0, 0, 205, 0, 0),
                             ('test_data-05.ldk', 7830, 7444, 6793, 864, 173, 6437, 836, 171),
                         ])
def test_extract_file(setup_extractor, file_path, expected_geometries, expected_geometries_no_duplicates,
                      expected_points, expected_lines, expected_polygons, expected_points_no_duplicates,
                      expected_lines_no_duplicates, expected_polygons_no_duplicates):

    test_dir = os.path.dirname(__file__)
    full_file_path = os.path.join(test_dir, 'data', file_path)

    extractor = setup_extractor
    with open(full_file_path, 'rb') as file:
        extractor.extract(file)

    geometries = extractor.geometries

    assert len(geometries) == expected_geometries
    assert len(geometries.get_points()) == expected_points
    assert len(geometries.get_lines()) == expected_lines
    assert len(geometries.get_polygons()) == expected_polygons

    geometries.remove_duplicates(fields=['name', 'coordinates', 'outline_color'])
    assert len(geometries) == expected_geometries_no_duplicates
    assert len(geometries.get_points()) == expected_points_no_duplicates
    assert len(geometries.get_lines()) == expected_lines_no_duplicates
    assert len(geometries.get_polygons()) == expected_polygons_no_duplicates
