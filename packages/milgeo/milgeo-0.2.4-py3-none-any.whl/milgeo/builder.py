from enum import Enum
from typing import Dict, Any
from xml.etree.ElementTree import Element, SubElement, tostring


class FeatureBuilder:
    def __init__(self, geometry):
        self.geometry = geometry
        self.feature = {
            "type": "Feature",
            "properties": {},
            "geometry": {}
        }

    def add_basic_elements(self):
        self.feature["properties"]["name"] = self.geometry.name
        self.feature["properties"]["sidc"] = self.geometry.sidc \
            if self.geometry.sidc is not None \
            else self.geometry.default_sidc
        self.feature["properties"]["comments"] = []

    def add_optional_properties(self):
        properties = [
            "observation_datetime",
            "reliability_credibility",
            "staff_comments",
            "platform_type",
            "quantity",
            "direction",
            "speed",
            "outline-color",
            "fill_color",
            "fill_opacity",
            "comments"
        ]
        for prop in properties:
            if prop == "outline-color":
                attr_name = "outline_color"
            else:
                attr_name = prop
            value = getattr(self.geometry, attr_name, None)
            if value is not None:
                if isinstance(value, Enum):
                    value = value.name
                self.feature["properties"][prop] = value

    def add_geometry(self):
        self.feature["geometry"] = dict(type=self.geometry.geometry_type, coordinates=self.geometry.coordinates)

    def build(self) -> Dict[str, Any]:
        return self.feature


class PlacemarkBuilder:
    def __init__(self, geometry):
        self.geometry = geometry
        self.placemark = Element("Placemark")

    def add_basic_elements(self):
        name = SubElement(self.placemark, "name")
        name.text = self.geometry.name

    def add_optional_properties(self):
        if self.geometry.outline_color:
            style = SubElement(self.placemark, "Style")
            line_style = SubElement(style, "LineStyle")
            color = SubElement(line_style, "color")
            color.text = self.geometry.outline_color

    def add_geometry(self):
        if self.geometry.geometry_type == "Point":
            self._add_point()
        elif self.geometry.geometry_type == "LineString":
            self._add_line_string()
        elif self.geometry.geometry_type == "Polygon":
            self._add_polygon()

    def _add_point(self):
        geometry_element = SubElement(self.placemark, "Point")
        coordinates = SubElement(geometry_element, "coordinates")
        coordinates.text = f"{self.geometry.coordinates[0]},{self.geometry.coordinates[1]}"

    def _add_line_string(self):
        geometry_element = SubElement(self.placemark, "LineString")
        coordinates = SubElement(geometry_element, "coordinates")
        coordinates.text = " ".join([f"{coord[0]},{coord[1]}" for coord in self.geometry.coordinates])

    def _add_polygon(self):
        geometry_element = SubElement(self.placemark, "Polygon")
        outer_boundary_is = SubElement(geometry_element, "outerBoundaryIs")
        linear_ring = SubElement(outer_boundary_is, "LinearRing")
        coordinates = SubElement(linear_ring, "coordinates")
        coordinates.text = " ".join([f"{coord[0]},{coord[1]}" for ring in self.geometry.coordinates for coord in ring])

    def build(self):
        return tostring(self.placemark)