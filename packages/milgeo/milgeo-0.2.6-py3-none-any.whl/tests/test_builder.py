from xml.etree.ElementTree import fromstring

import pytest
from milgeo.geometry import Point, Line, Polygon
from milgeo.builder import FeatureBuilder, PlacemarkBuilder


@pytest.fixture
def sample_polygon_geometry():
    return Polygon(
        name="Geometry",
        coordinates=[[[10.0, 20.0], [10.0, 20.0], [10.0, 20.0], [10.0, 20.0]]],
        sidc="12345678901234567890",
        outline_color="#ff0000",
        fill_color="#00ff00",
        fill_opacity="0.5",
        comments=["Comment 1", "Comment 2"]
    )


def test_featurebuilder_basic_elements(sample_polygon_geometry):
    builder = FeatureBuilder(sample_polygon_geometry)
    builder.add_basic_elements()
    feature = builder.build()
    assert feature["properties"]["name"] == "Geometry"
    assert feature["properties"]["sidc"] == "12345678901234567890"
    assert feature["properties"]["comments"] == []


def test_featurebuilder_optional_properties(sample_polygon_geometry):
    sample_polygon_geometry.observation_datetime = "2024-01-01T00:00:00"
    sample_polygon_geometry.quantity = "5"
    builder = FeatureBuilder(sample_polygon_geometry)
    builder.add_optional_properties()
    feature = builder.build()
    assert feature["properties"]["observation_datetime"] == "2024-01-01T00:00:00"
    assert feature["properties"]["quantity"] == "5"
    assert feature["properties"]["comments"] == ["Comment 1", "Comment 2"]


def test_featurebuilder_geometry(sample_polygon_geometry):
    builder = FeatureBuilder(sample_polygon_geometry)
    builder.add_geometry()
    feature = builder.build()
    assert feature["geometry"]["type"] == sample_polygon_geometry.geometry_type
    assert feature["geometry"]["coordinates"] == sample_polygon_geometry.coordinates


def test_placemarkbuilder_basic_elements(sample_polygon_geometry):
    builder = PlacemarkBuilder(sample_polygon_geometry)
    builder.add_basic_elements()
    placemark = builder.build()
    placemark_xml = fromstring(placemark)
    assert placemark_xml.find('name').text == "Geometry"


def test_placemarkbuilder_optional_properties(sample_polygon_geometry):
    builder = PlacemarkBuilder(sample_polygon_geometry)
    builder.add_optional_properties()
    placemark = builder.build()
    placemark_xml = fromstring(placemark)
    assert placemark_xml.find('.//LineStyle/color').text == "#ff0000"


def test_placemarkbuilder_point_geometry(sample_polygon_geometry):
    sample_geometry = Point(
        name="Point",
        coordinates=[10.0, 20.0]
    )
    builder = PlacemarkBuilder(sample_geometry)
    builder.add_geometry()
    placemark = builder.build()
    placemark_xml = fromstring(placemark)
    assert placemark_xml.find('.//Point/coordinates').text == "10.0,20.0"


def test_placemarkbuilder_linestring_geometry():
    sample_geometry = Line(
        name="Line",
        coordinates=[[10.0, 20.0], [30.0, 40.0]]
    )
    builder = PlacemarkBuilder(sample_geometry)
    builder.add_geometry()
    placemark = builder.build()
    placemark_xml = fromstring(placemark)
    assert placemark_xml.find('.//LineString/coordinates').text == "10.0,20.0 30.0,40.0"


def test_placemarkbuilder_polygon_geometry():
    sample_geometry = Polygon(
        name="Polygon",
        coordinates=[[[10.0, 20.0], [30.0, 40.0], [50.0, 60.0], [10.0, 20.0]]]
    )
    builder = PlacemarkBuilder(sample_geometry)
    builder.add_geometry()
    placemark = builder.build()
    placemark_xml = fromstring(placemark)
    assert placemark_xml.find('.//Polygon/outerBoundaryIs/LinearRing/coordinates').text == "10.0,20.0 30.0,40.0 50.0,60.0 10.0,20.0"
