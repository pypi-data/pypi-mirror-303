import datetime

from typing import List, Tuple, Union, Any

from dateutil.parser import parse

from geodesic.bases import _APIObject
from geodesic.utils import datetime_to_utc
from geodesic.descriptors import (
    _ListDescr,
    _StringDescr,
    _DictDescr,
)
from geodesic.boson.asset_bands import AssetBands

# Middleware types
SEARCH_FILTER_CQL2 = "cql2"
SEARCH_FILTER_SPATIAL = "spatial"
SEARCH_FILTER_DATETIME = "datetime"
SEARCH_TRANSFORM_RENAME_FIELDS = "rename-fields"
SEARCH_TRANSFORM_GEOMETRY = "transform-geometry"
SEARCH_TRANSFORM_COMBINE_FIELDS = "combine-fields"
SEARCH_TRANSFORM_DEFAULT_DATETIME_RANGE = "default-datetime-range"
SEARCH_TRANSFORM_S2 = "s2"
SEARCH_TRANSFORM_H3 = "h3"
SEARCH_TRANSFORM_CALCULATE_FIELD = "calculate-field"
SEARCH_TRANSFORM_COMPUTE_ID = "compute-id"
PIXELS_TRANSFORM_COLORMAP = "colormap"
PIXELS_TRANSFORM_DEFAULT_ASSET_BANDS = "default_asset_bands"
PIXELS_TRANSFORM_RASTERIZE = "rasterize"
PIXELS_TRANSFORM_RESCALE_SHIFT = "rescale-shift"
PIXELS_TRANSFORM_DEFAULT_DATETIME_RANGE = "default-datetime-range"
PIXELS_TRANSFORM_BAND_ARITHMETIC = "band-arithmetic"
PIXELS_TRANSFORM_INVERSE_DISTANCE_WEIGHTING = "inverse-distance-weighting"
PIXELS_TRANSFORM_DATETIME_DIFFERENCE = "datetime-difference"


def parsedate(dt):
    try:
        return parse(dt)
    except TypeError:
        return dt


class _Middleware(_APIObject):
    _limit_setitem = ("type", "properties")
    type = _StringDescr(
        doc="type of middleware to apply to a provider",
        one_of=[
            SEARCH_FILTER_DATETIME,
            SEARCH_FILTER_CQL2,
            SEARCH_FILTER_SPATIAL,
            SEARCH_TRANSFORM_RENAME_FIELDS,
            SEARCH_TRANSFORM_COMBINE_FIELDS,
            SEARCH_TRANSFORM_GEOMETRY,
            SEARCH_TRANSFORM_DEFAULT_DATETIME_RANGE,
            SEARCH_TRANSFORM_S2,
            SEARCH_TRANSFORM_H3,
            SEARCH_TRANSFORM_CALCULATE_FIELD,
            SEARCH_TRANSFORM_COMPUTE_ID,
            PIXELS_TRANSFORM_COLORMAP,
            PIXELS_TRANSFORM_DEFAULT_ASSET_BANDS,
            PIXELS_TRANSFORM_RASTERIZE,
            PIXELS_TRANSFORM_RESCALE_SHIFT,
            PIXELS_TRANSFORM_DEFAULT_DATETIME_RANGE,
            PIXELS_TRANSFORM_BAND_ARITHMETIC,
            PIXELS_TRANSFORM_INVERSE_DISTANCE_WEIGHTING,
            PIXELS_TRANSFORM_DATETIME_DIFFERENCE,
        ],
    )
    properties = _DictDescr(doc="properties (if any) to configure the middleware")


class SearchFilter(_Middleware):
    @staticmethod
    def cql2_filter() -> "SearchFilter":
        """Adds CQL filtering to a provider that may not implement it natively."""
        return SearchFilter(type=SEARCH_FILTER_CQL2)

    @staticmethod
    def spatial() -> "SearchFilter":
        """Adds spatial filtering to a provider that may not implement it natively."""
        return SearchFilter(type=SEARCH_FILTER_SPATIAL)

    @staticmethod
    def datetime(field: str) -> "SearchFilter":
        """Adds datetime filtering to a provider that may not implement it natively."""
        return SearchFilter(type=SEARCH_FILTER_DATETIME, properties={"datetime_field": field})


class SearchTransform(_Middleware):
    @staticmethod
    def rename_fields(case=None, field_map={}) -> "SearchTransform":
        """Rename fields in the `properties` of a search response.

        Args:
            case (str, optional): case to apply to the field names. Defaults to None.
                One of ["upper", "lower"]
            field_map (dict, optional): mapping of old field names to new field names.
                Defaults to {}.

        Examples:
            >>> # Rename the field "old_field" to "new_field"
            >>> transform = SearchTransform.rename_fields(field_map={"old_field": "new_field"})

            >>> # Rename the field "old_field" to "new_field" and make it uppercase
            >>> transform = SearchTransform.rename_fields(case="upper", field_map={"old_field": "new_field"})
        """  # noqa: E501
        properties = {"field_map": field_map}
        if case is not None and case in ["upper", "lower"]:
            properties["case"] = case
        elif case is not None:
            raise ValueError(f"case must be one of ['upper', 'lower'], got {case}")

        return SearchTransform(type=SEARCH_TRANSFORM_RENAME_FIELDS, properties=properties)

    @staticmethod
    def combine_fields(
        new_field: str, fields: List[str], separator: str = "", sprintf: str = ""
    ) -> "SearchTransform":
        """Combine fields in the `properties` of a search response.

        Args:
            new_field (str): name of the new field to create
            fields (List[str]): fields to combine
            separator (str, optional): separator to use when combining fields. Defaults to " ".
            sprintf (str, optional): sprintf format to use when combining fields. This uses golang
            format strings to format the fields into one combined string field. For instance,
            "%d.2 %s" would print "2.00 dollars" if the field values were 2 and "dollars".
            For more information about the formatting see https://pkg.go.dev/fmt.
            All fields must have values for the sprintf to be executed. Defaults to "".

        Examples:
            >>> # Combine the fields STATE_FIPS and COUNTY_FIPS into a new field called FIPS
            >>> transform = SearchTransform.combine_fields(
            ...     new_field="FIPS",
            ...     fields=["STATE_FIPS", "COUNTY_FIPS"],
            ...     separator=""
            ... )

            >>> # Combine the fields STATE_FIPS and COUNTY_FIPS into a new field called FIPS
            >>> transform = SearchTransform.combine_fields(
            ...     new_field="FIPS",
            ...     fields=["STATE_FIPS", "COUNTY_FIPS"],
            ...     sprintf="%02d%03d"
            ... )
        """
        return SearchTransform(
            type="combine-fields",
            properties={
                "new_field": new_field,
                "fields": fields,
                "separator": separator,
                "sprintf": sprintf,
            },
        )

    @staticmethod
    def centroid() -> "SearchTransform":
        """Calculate the centroid of the queried geometry.

        This middleware will calculate the centroid of the geometry and return it in a new
        collection called "centroid". In the case of multi-geometries, the centroid of the entire
        geometry will be calculated.

        When creating this middleware, most of the time you will want to apply it after
        any filtering happens, so that the centroid is calculated on the filtered geometry. This is
        done by adding it to the `search_transforms_after` list in the `MiddlewareConfig`. See the
        below example.

        Returns:
            SearchTransform: middleware to calculate the centroid of the queried geometry

        Examples:
            >>> # Add the centroid middleware to a dataset view
            >>> ds_with_centroid = ds.view(
            ...     middleware=[
            ...         SearchTransform.centroid()
            ...     ]
            ... )
        """
        return SearchTransform(
            type="transform-geometry",
            properties={
                "transform": "centroid",
                "parameters": {},
            },
        )

    @staticmethod
    def convex_hull() -> "SearchTransform":
        """Calculate the convex hull of the queried geometry.

        This middleware will calculate the convex hull of the geometry and return it in a new
        collection called "convex_hull". The convex hull is the smallest convex polygon that
        encloses the geometry.  In the case of multi-geometries, the convex hull of the entire
        geometry will be calculated.

        When creating this middleware, most of the time you will want to apply it after
        any filtering happens, so that the centroid is calculated on the filtered geometry. This is
        done by adding it to the `search_transforms_after` list in the `MiddlewareConfig`. See the
        below example.

        Returns:
            SearchTransform: middleware to calculate the convex hull of the queried geometry

        Examples:
            >>> # Add the convex_hull middleware to a dataset view
            >>> ds_with_convex_hull = ds.view(
            ...     middleware=[
            ...         SearchTransform.convex_hull()
            ...     ]
            ... )
        """
        return SearchTransform(
            type="transform-geometry",
            properties={
                "transform": "convex_hull",
                "parameters": {},
            },
        )

    @staticmethod
    def bounds() -> "SearchTransform":
        """Calculate the bounds of the queried geometry.

        This middleware will calculate the bounds of the geometry and return it in a new collection
        called "bounds". The bounds in this case are a rectangle that encloses the geometry.
        In the case of multi-geometries, the bounds of the entire geometry will be calculated.

        When creating this middleware, most of the time you will want to apply it after
        any filtering happens, so that the centroid is calculated on the filtered geometry. This is
        done by adding it to the `search_transforms_after` list in the `MiddlewareConfig`. See the
        below example.

        Returns:
            SearchTransform: middleware to calculate the bounds of the queried geometry

        Examples:
            >>> # Add the bounds middleware to a dataset view
            >>> ds_with_bounds = ds.view(
            ...     middleware=[
            ...         SearchTransform.bounds()
            ...     ]
            ... )
        """
        return SearchTransform(
            type="transform-geometry",
            properties={
                "transform": "bounds",
                "parameters": {},
            },
        )

    @staticmethod
    def simplify(threshold: float, stride: int = 2) -> "SearchTransform":
        """Simplify the queried geometry.

        This middleware will simplify the geometry by removing points according to the
        `Ramer-Douglas-Peucker Algorithm<https://en.wikipedia.org/wiki/Ramer%E2%80%93Douglas%E2%80%93Peucker_algorithm>`_.
        This is useful for reducing the size of the geometry for visualization or other purposes.
        The threshold is approximately the scale at which points will be removed. A smaller
        threshold will cause more points of the original geometry to be kept, and larger will cause
        more to be thrown away. The stride parameter controls how many points are checked against
        the threshold when simplifying. A larger stride will simplify the geometry faster but may
        result in a less accurate simplification. If you are not familiar with this algorithm, it
        is recommended that you leave stride at the default value of 2.

        When creating this middleware, most of the time you will want to apply it after
        any filtering happens, so that the centroid is calculated on the filtered geometry. This is
        done by adding it to the `search_transforms_after` list in the `MiddlewareConfig`. See the
        below example.

        .. note::
            The units of the threshold are the same as the units of the spatial reference of the
            geometry. For instance, if the geometry is in EPSG:4326, the threshold will be in degrees.

        Args:
            threshold (float): distance between points that will be removed
            stride (int, optional): number of points to skip when simplifying. Defaults to 2.

        Returns:
            SearchTransform: middleware to simplify the queried geometry

        Examples:
            >>> # Add the simplify middleware to a dataset view
            >>> simplified_ds = ds.view(
            ...     middleware=[
            ...         SearchTransform.simplify(threshold=0.01, stride=3)
            ...     ]
            ... )
        """  # noqa: E501
        if threshold < 0:
            raise ValueError("threshold must be greater than or equal to 0")

        if stride < 1:
            raise ValueError("stride must be greater than or equal to 1")

        return SearchTransform(
            type="transform-geometry",
            properties={
                "transform": "simplify",
                "parameters": {"threshold": threshold, "stride": stride},
            },
        )

    @staticmethod
    def buffer(
        distance: float = None, distance_field: str = None, segments: int = 10
    ) -> "SearchTransform":
        """Buffer the queried geometry.

        This middleware will buffer the geometry by a given distance. The distance is the distance
        to buffer the geometry in the units of the spatial reference of the geometry. For instance,
        if the geometry is in EPSG:4326, the distance will be in degrees. The segments parameter
        controls the number of segments to use when approximating the buffer. A larger number of
        segments will result in a smoother buffer but will result in larger geometries.

        This middleware is especially useful when combined with the rasterize middleware to create
        a buffer around points. When rasterizing points with the buffer middleware, the buffer will
        ensure that the points do not become incredibly small when a high rasterization resolution
        is used.

        Args:
            distance (float): distance to buffer the geometry
            distance_field (str): field in the properties of the feature that contains the distance
                to buffer the geometry
            segments (int, optional): number of segments to use when approximating the buffer.
                Defaults to 10.

        Returns:
            SearchTransform: middleware to buffer the queried geometry

        Examples:
            >>> # Add the buffer middleware to a dataset view
            >>> buffered_ds = ds.view(
            ...     name="buffered-ds",
            ...     middleware=[
            ...         SearchTransform.buffer(distance=0.01, segments=32)
            ...     ]
            ... )
        """
        if distance is None and distance_field is None:
            raise ValueError("Must provide either a distance or a distance_field")

        if distance is not None and distance <= 0:
            raise ValueError("distance must be greater than 0")

        properties = {"type": "transform-geometry"}
        if distance is not None:
            properties["properties"] = {
                "transform": "buffer",
                "parameters": {"distance": distance, "segments": segments},
            }
        else:
            properties["properties"] = {
                "transform": "buffer",
                "parameters": {"distance_field": distance_field, "segments": segments},
            }

        return SearchTransform(**properties)

    @staticmethod
    def default_datetime_range(
        start: Union[datetime.datetime, str] = None,
        end: Union[datetime.datetime, str] = None,
        before_now: datetime.timedelta = None,
    ) -> "SearchTransform":
        """Sets the default datetime range in a search request on a Dataset.

        This is useful for when you are creating a dataset that points to a very long time history,
        but by default wish to show a specific time range. This can be useful for things like
        showing the last 24 hours of data.

        Parameters:
            start: start of the default datetime range. Defaults to None.
            end: end of the default datetime range. Defaults to None.
            before_now: time delta before now to set the start of the default datetime range. If
                provided, will be used instead of start/end and will dynamically be used based on
                the current time whenever there is a new request. Defaults to None.

        Example:
            >>> # Set the default datetime range to be the last 24 hours
            >>> default_datetime_transform = SearchTransform.default_datetime_range(before_now=datetime.timedelta(days=1))

            >>> # Set the default datetime range to be from 2021-01-01 to 2021-01-02
            >>> default_datetime_transform = SearchTransform.default_datetime_range(start="2021-01-01", end="2021-01-02")
        """  # noqa: E501
        properties = _default_datetime_range_props(start, end, before_now)
        return SearchTransform(type="default-datetime-range", properties=properties)

    @staticmethod
    def s2(level: int, return_all: bool = False) -> "SearchTransform":
        """Adds the S2 cell to properties.

        See http://s2geometry.io/devguide/s2cell_hierarchy.html for more details.

        Defaults to returning the S2 cell of the centroid of the geometry

        If return_all is set to True, will return a list of the S2 cells that cover the geometry

        Adds a property to the feature properties called "s2_[level]" where [level] is the level of
        the S2 cell.

        If return_all is set to True, will return a list of the S2 cells that cover the geometry,
        in a property called "s2_[level]_all".

        Args:
            level: S2 level. Must be between 0 and 30
            return_all: whether to return all S2 cells that cover the geometry. Defaults to False

        Returns:
            SearchTransform: middleware to add S2 cell to feature properties

        Examples:
            >>> # Add the S2 cell to the properties of the search response
            >>> transform = SearchTransform.s2(level=10)
        """
        if level < 0 or level > 30:
            raise ValueError("S2 level must be between 0 and 30")

        return SearchTransform(
            type=SEARCH_TRANSFORM_S2,
            properties={"level": level, "return_all": return_all},
        )

    @staticmethod
    def h3(resolution: int, return_all: bool = False) -> "SearchTransform":
        """Adds the H3 cell to properties.

        See https://h3geo.org/ for more details.

        Defaults to returning the H3 cell of the centroid of the geometry

        If return_all is set to True, will return a list of the H3 that are enclosed by the geometry

        Adds a property to the feature properties called "h3_[resolution]" where [resolution] is the
        level of the S2 cell.

        If return_all is set to True, will return a list of the H3 cells that cover the geometry,
        in a property called "h3_[resolution]_all".

        Args:
            resolution: H3 resolution. Must be between 0 and 15
            return_all: whether to return all H3 cells that cover the geometry. Defaults to False

        Returns:
            SearchTransform: middleware to add H3 cell to feature properties

        Examples:
            >>> # Add the H3 cell to the properties of the search response
            >>> transform = SearchTransform.h3(resolution=10)
        """
        if resolution < 0 or resolution > 15:
            raise ValueError("H3 resolution must be between 0 and 15")

        return SearchTransform(
            type=SEARCH_TRANSFORM_H3,
            properties={"resolution": resolution, "return_all": return_all},
        )

    @staticmethod
    def calculate_field(
        new_field: str,
        expression: str,
        skip_if_null: bool = False,
        fill_value: float = None,
    ) -> "SearchTransform":
        """Creates a new field in the search response based on an expression.

        The fields in the expression must be numeric fields.

        Args:
            new_field: name of the new field to create
            expression: expression to calculate the new field
            skip_if_null: whether to skip the calculation if any of the fields in the expression do
                not exist.  Useful when not every feature contains a property used in the
                expression. Defaults to False.
            fill_value: value to fill the new field with if the expression is not calculated.
                Defaults to None.

        Returns:
            SearchTransform: middleware to calculate a new field in the search response

        Examples:
            >>> # Calculate a new field called "sum" that is the sum of "field_1" and "field_2"
            >>> transform = SearchTransform.calculate_field(
            ...     new_field="sum",
            ...     expression="field_1 + field_2"
            ... )

            >>> # Calculate a new field called "plus_one" that is "field_1" + 1
            >>> transform = SearchTransform.calculate_field(
            ...     new_field="plus_one",
            ...     expression="field_1 + 1"
            ... )

            >>> # Calculate a new field called "div" that is "(field_1 + 5) / field_2"
            >>> transform = SearchTransform.calculate_field(
            ...     new_field="div",
            ...     expression="(field_1 + 5) / field_2",
            ...     skip_if_null=True
            ... )
        """
        properties = {
            "new_field": new_field,
            "expression": expression,
            "skip_if_null": skip_if_null,
        }

        if fill_value is not None:
            properties["fill_value"] = fill_value

        return SearchTransform(
            type="calculate-field",
            properties=properties,
        )

    @staticmethod
    def compute_id() -> "SearchTransform":
        """Compute an ID for each feature in the search response.

        This middleware will compute an ID for each feature in the search response. The ID is
        computed by hashing the properties and geometry of the feature. This is useful for when you
        want to uniquely identify each feature in the search response when the features do not have
        an existing ID.

        Returns:
            SearchTransform: middleware to compute an ID for each feature in the search response

        Examples:
            >>> # Compute an ID for each feature in the search response
            >>> transform = SearchTransform.compute_id()
        """
        return SearchTransform(type=SEARCH_TRANSFORM_COMPUTE_ID)


class PixelsTransform(_Middleware):
    @staticmethod
    def colormap(
        *,
        asset: str,
        band: Union[int, str],
        colormap_name: str = "magma",
        lookup_table: List[List[int]] = None,
        min: float = None,
        max: float = None,
        rescale: bool = False,
        no_data_value: float = None,
        asset_name: str = "colormap",
    ) -> "PixelsTransform":
        """Apply a colormap to the pixels data from an existing asset in the dataset.

        Args:
            asset: asset to apply the colormap to
            band: band to apply the colormap to
            colormap_name: name of the colormap to apply. Defaults to "magma".
            lookup_table: lookup table to apply. Defaults to None. This can be used to provide a
                custom colormap via a lookup table. In this case, this should be a list of lists
                where each sublist is a color, including the alpha channel. For instance,
                [[0, 0, 0, 255], [255, 255, 255, 255]] would create a colormap that goes from black
                to white in two steps, splitting values below 0,5 to black and above to white.
            min: minimum value of the colormap. Valid only if rescale is True. Defaults to None.
            max: maximum value of the colormap. Valid only if rescale is True. Defaults to None.
            rescale: whether to rescale the colormap to the min and max values. If min/max are None,
                statistics of the dataset (if available) will be used, otherwise the values of the
                current response will be used.  Defaults to False.
            no_data_value: value to use for pixels with no data. These values will be transparent.
                Defaults to None.
            asset_name: name of the asset to create. Defaults to "colormap".

        Examples:
            >>> # Apply the magma colormap to the rasterized band of the asset "rasterized"
            >>> colormap_transform = PixelsTransform.colormap(asset="rasterized", band="rasterized", min=0, max=1000)
        """  # noqa: E501
        properties = {
            "asset": asset,
            "band": band,
            "colormap_name": colormap_name,
            "rescale": rescale,
            "asset_name": asset_name,
        }
        if lookup_table is not None:
            properties.pop("colormap_name")
            properties["lookup_table"] = lookup_table
        if min is not None:
            properties["min"] = min
        if max is not None:
            properties["max"] = max
        if no_data_value is not None:
            properties["no_data_value"] = no_data_value

        return PixelsTransform(type=PIXELS_TRANSFORM_COLORMAP, properties=properties)

    @staticmethod
    def rescale_shift(
        asset: str,
        bands: List[Union[int, str]] = None,
        scale: List[float] = None,
        shift: List[float] = None,
        clamp: List[float] = None,
        asset_name: str = "rescaled",
    ) -> "PixelsTransform":
        """Rescale the pixel values of an asset in a dataset.

        Rescales the pixel values of an asset in a dataset by subtracting a shift from the pixel
        values and then dividing by a scale. This is useful for things like normalizing the pixel
        values of an image to be between 0 and 1 or 0 and 255, or recalibration pixels values under
        a linear transformation.

        If scale/shift is not specified, will rescale by the local min/max of the pixel values
        across all bands. Do not use this with tiled services as each tile will be rescaled based on
        its min/max and the result will be a checkerboard pattern. Instead, use the scale/shift
        parameters to rescale the entire image tile set.

        Args:
            asset: asset to rescale/shift
            bands: bands to rescale/shift. If not specified, will use all bands for the
                specified asset.
            scale: scale values for each band. This will divide the shifted pixel values by this
                value.
            shift: shift values for each band. This will subtract this value from the pixel values
                prior to scaling.
            clamp: If specified, must be 2 numbers to clamp the values between ranges. Values less
                than clamp[0] will be set to clamp[0] and values greater than clamp[1] will be set
                to clamp[1].  Defaults to None (no clamping)
            asset_name: name of the asset to create. Defaults to "rescaled".

        Examples:
            >>> # Rescale the pixel values of an asset with values in uint8 to be between 0 and 1
            >>> transform = PixelsTransform.rescale_shift(
            ... asset="my_asset",
            ... bands=[0, 1, 2],
            ... scale=[255],
            ... shift=[0],
            ... asset_name="rescaled"
            ... )

            >>> # Rescale all bands for "my_asset" to be between 0 and 255
            >>> transform = PixelsTransform.rescale_shift(
            ... asset="my_asset",
            ... asset_name="rescaled"
            ... )

            >>> # Rescale "red", "green", and "blue" bands for "image" to be between 0 and 1
            >>> # using a known min/max
            >>> transform = PixelsTransform.rescale_shift(
            ... asset="image",
            ... bands=["red", "green", "blue"],
            ... scale=[12345, 12345, 12345],
            ... shift=[123, 456, 789],
            ... asset_name="rescaled-rgb"
            ... )
        """
        properties = {
            "asset": asset,
            "asset_name": asset_name,
        }
        if bands is not None:
            properties["bands"] = bands
        if scale is not None and shift is None:
            raise ValueError("Must provide a shift if providing a scale")
        if shift is not None and scale is None:
            raise ValueError("Must provide a scale if providing a shift")
        if scale is not None and shift is not None and len(scale) != len(shift):
            raise ValueError("Scale and shift must be the same length")
        if clamp is not None and len(clamp) != 2:
            raise ValueError("Clamp must be a list of 2 numbers")
        if scale is not None:
            properties["scale"] = scale
        if shift is not None:
            properties["shift"] = shift
        if clamp is not None:
            properties["clamp"] = clamp

        return PixelsTransform(
            type=PIXELS_TRANSFORM_RESCALE_SHIFT,
            properties=properties,
        )

    @staticmethod
    def default_asset_bands(default_asset_bands: List[AssetBands]) -> "PixelsTransform":
        """Sets the default value of asset_bands in a pixels request on a Dataset.

        This is useful for when you are creating a static dataset and want to set the default bands
        that will be used in the pixels request or for when you have a dataset that has multiple
        bands and you want to set the default bands that will be used in the pixels request.

        Parameters:
            default_asset_bands: list of AssetBands objects that will be used as the default bands
            in the pixels request

        Example:
            >>> # Set the default asset bands to be the first band of the rasterized asset
            >>> default_asset_transform = PixelsTransform.default_asset_bands(
            ...     [AssetBands(asset="rasterized", bands=[0])]
            ... )
        """
        return PixelsTransform(
            type=PIXELS_TRANSFORM_DEFAULT_ASSET_BANDS,
            properties={"asset_bands": default_asset_bands},
        )

    @staticmethod
    def default_datetime_range(
        start: Union[datetime.datetime, str] = None,
        end: Union[datetime.datetime, str] = None,
        before_now: datetime.timedelta = None,
    ) -> "PixelsTransform":
        """Sets the default datetime range in a pixels request on a Dataset.

        This is useful for when you are creating a dataset that points to a very long time history,
        but by default wish to show a specific time range. This can be useful for things like
        showing the last 24 hours of data.

        Parameters:
            start: start of the default datetime range. Defaults to None.
            end: end of the default datetime range. Defaults to None.
            before_now: time delta before now to set the start of the default datetime range. If
                provided, will be used instead of start/end and will dynamically be used based on
                the current time whenever there is a new request. Defaults to None.

        Example:
            >>> # Set the default datetime range to be the last 24 hours
            >>> default_datetime_transform = PixelsTransform.default_datetime_range(
            ...     before_now=datetime.timedelta(days=1)
            ... )

            >>> # Set the default datetime range to be from 2021-01-01 to 2021-01-02
            >>> default_datetime_transform = PixelsTransform.default_datetime_range(
            ...     start="2021-01-01", end="2021-01-02"
            ... )
        """
        properties = _default_datetime_range_props(start, end, before_now)
        return PixelsTransform(type="default-datetime-range", properties=properties)

    @staticmethod
    def rasterize(
        attribute_name: str = None,
        value: Any = None,
        use_z: bool = False,
        initialize_value: Any = None,
        invert: bool = False,
        all_touched: bool = False,
        add: bool = False,
        collections: List[str] = [],
        asset_name: str = "rasterized",
        band_name: str = "rasterized",
        feature_limit: int = 25000,
    ) -> "PixelsTransform":
        """Creates a rasterized image from a feature collection as a new raster asset.

        Rasterize middleware is useful for performing simple aggregations on a feature collection.
        This can be useful for things like creating a population density raster from a feature
        collection of population counts or creating a binary raster from a feature collection of
        labels in a segmentation task.

        Args:
            attribute_name: attribute name to rasterize. Defaults to None.
            value: value to rasterize. Defaults to None.
            use_z: whether to use the z value of the feature. Defaults to False.
            initialize_value: value to initialize the raster with. Defaults to None.
            invert: invert which pixels are rasterize. Defaults to False.
            all_touched: whether to rasterize all pixels touched by the feature. Defaults to False.
            add: whether to add the raster to the asset. Defaults to False.
            collections: collections to rasterize. Defaults to [] (all collections).
            asset_name: name of the asset to create. Defaults to "rasterized".
            band_name: name of the band to create. Defaults to "rasterized".
            feature_limit: maximum number of features to rasterize. Defaults to 25000.

        Examples:
            >>> # Rasterize the population attribute by summing the values in the attribute for each pixel
            >>> transform = PixelsTransform.rasterize(
            ... attribute_name="population",
            ... add=True,
            ... asset_name="population_raster",
            ... band_name="population"
            ... )

            >>> # Rasterize by object by setting the value to 1 wherever there is an object
            >>> transform = PixelsTransform.rasterize(
            ... value=1
            ... )

            >>> # Rasterize by object by setting the value to 1 wherever there is NOT an object
            >>> transform = PixelsTransform.rasterize(
            ... value=1,
            ... invert=True
            ... )

        """  # noqa: E501
        if (value is None and attribute_name is None) and (not use_z):
            raise ValueError(
                "Must provide either a value or an attribute_name or use_z must be True."
            )

        return PixelsTransform(
            type=PIXELS_TRANSFORM_RASTERIZE,
            properties={
                "value": value,
                "initialize_value": initialize_value,
                "attribute_name": attribute_name,
                "invert": invert,
                "all_touched": all_touched,
                "use_z": use_z,
                "add": add,
                "collections": collections,
                "asset_name": asset_name,
                "band_name": band_name,
                "feature_limit": feature_limit,
            },
        )

    @staticmethod
    def inverse_distance_weighting(
        attribute_name: str,
        max_distance: float,
        asset_name: str = "idw",
        collections: List[str] = [],
        no_data_value: float = 0,
        power: int = 2,
        max_points: int = 25,
        feature_limit: int = 1000,
    ) -> "PixelsTransform":
        """Creates an interpolated image from a feature collection using inverse distance weighting.

        Inverse distance weighting is a method for interpolating values from a set of points to a raster. This
        method is useful for interpolating values like temperature, precipitation, or other continuous variables
        from a set of point measurements.

        If the features are not points (e.g. polygons), the centroid of the feature will be used as the point
        to interpolate from.

        Inverse distance weighting takes the k nearest points to a pixel and calculates the value at that pixel
        as the weighted average of the values of the k nearest points. The weight of each point is calculated
        as 1 / distance^power, where power is a parameter that controls the rate at which the weight decreases.


        The max distance (meters) parameter controls the maximum distance to interpolate to. If there are no points within
        this distance, the pixel will be set to the `no_data_value`.

        Increasing the feature limit will increase the number of features that are interpolated, but will also increase
        the time it takes to interpolate the image. There is a hard limit of 10,000 features that can be interpolated.

        Args:
            attribute_name: attribute name to interpolate. This is the field in the properties of each feature that will be interpolated.
            asset_name: name of the asset to create.
            max_distance: maximum distance to interpolate in meters.
            collections: collections to interpolate. Defaults to [] (all collections).
            no_data_value: value to use for pixels with no data. Defaults to 0.
            power: power to use in the interpolation. Defaults to 2.
            max_points: maximum number of points to use in the interpolation. Defaults to 25.
            feature_limit: maximum number of features to interpolate. Defaults to 1000.

        Examples:
            >>> # Interpolate the temperature attribute using inverse distance weighting
            >>> transform = PixelsTransform.inverse_distance_weighting(
            ...     attribute_name="temperature",
            ...     asset_name="temperature_interpolated",
            ...     max_distance=100
            ... )
        """  # noqa: E501
        if power <= 0:
            raise ValueError("power must be greater than 0")

        if max_points <= 0:
            raise ValueError("max_points must be greater than 0")

        if feature_limit <= 0:
            raise ValueError("feature_limit must be greater than 0")

        if max_distance <= 0:
            raise ValueError("max_distance must be greater than 0")

        return PixelsTransform(
            type=PIXELS_TRANSFORM_INVERSE_DISTANCE_WEIGHTING,
            properties={
                "power": power,
                "max_points": max_points,
                "feature_limit": feature_limit,
                "attribute_name": attribute_name,
                "asset_name": asset_name,
                "collections": collections,
                "max_distance": max_distance,
                "no_data_value": no_data_value,
            },
        )

    @staticmethod
    def band_arithmetic(expression: str, asset_name: str) -> "PixelsTransform":
        """Creates a new asset by applying a band arithmetic expression to an existing asset.

        Asset bands are represented using the following syntax:

        - `{"band_name": band_index}`: asset band from band index
        - `{"asset_name": "band_name"}`: asset band from band name

        Addition, subtraction, multiplication, and division are supported.

        Functions and exponentiation are not yet supported.

        Args:
            expression: band arithmetic expression to apply
            asset_name: name of the asset to create

        Returns:
            PixelsTransform: middleware to apply band arithmetic to an asset

        Examples:
            >>> # Create a new asset by adding the "red" and "nir" bands together
            >>> transform = PixelsTransform.band_arithmetic(
            ...     expression='{"red": 0} + {"nir": 0}',
            ...     asset_name="red_nir_sum"
            ... )

            >>> # Create a new asset by adding 10 to the "red" band
            >>> transform = PixelsTransform.band_arithmetic(
            ...     expression='{"image": "red"} + 10',
            ...     asset_name="red_plus_10"
            ... )
        """
        # some validation on the expression to catch common mistakes

        expression = expression.replace("'", '"')

        if expression.count("(") != expression.count(")"):
            raise ValueError(
                "Expression must have an equal number of opening and closing parentheses"
            )

        if expression.count("{") != expression.count("}"):
            raise ValueError(
                "Expression must have an equal number of opening and closing curly braces"
            )

        if expression.count('"') % 2 != 0:
            raise ValueError("Expression must have an even number of double quotes")

        return PixelsTransform(
            type=PIXELS_TRANSFORM_BAND_ARITHMETIC,
            properties={
                "expression": expression,
                "asset_name": asset_name,
            },
        )

    @staticmethod
    def normalized_difference(
        asset_band_1: AssetBands, asset_band_2: AssetBands, asset_name: str
    ) -> "PixelsTransform":
        """Creates a new asset by calculating the normalized difference between two bands.

        The normalized difference is calculated as (band_1 - band_2) / (band_1 + band_2).

        A common index, NDVI, is calculated by: `(NIR - Red) / (NIR + Red)`

        Args:
            asset_band_1: asset band for the first band
            asset_band_2: asset band for the second band
            asset_name: name of the asset to create

        Returns:
            PixelsTransform: middleware to calculate the normalized difference between two bands

        Examples:
            >>> # Calculate NDVI using band names
            >>> transform = PixelsTransform.normalized_difference(
            ...     asset_band_1=AssetBands(asset="image", bands=["nir"]),
            ...     asset_band_2=AssetBands(asset="image", bands=["red"]),
            ...     asset_name="ndvi"
            ... )

            >>> # Calculate NDVI using band IDs
            >>> transform = PixelsTransform.normalized_difference(
            ...     asset_band_1=AssetBands(asset="nir", bands=[0]),
            ...     asset_band_2=AssetBands(asset="red", bands=[0]),
            ...     asset_name="ndvi"
            ... )
        """
        if isinstance(asset_band_1, dict):
            asset_band_1 = AssetBands(**asset_band_1)
        if isinstance(asset_band_2, dict):
            asset_band_2 = AssetBands(**asset_band_2)

        a1 = asset_band_1.asset
        if a1 is None:
            raise ValueError("Asset band 1 must have an asset")
        b1 = asset_band_1.bands
        if len(b1) != 1:
            raise ValueError("Asset band 1 must have exactly one band")
        b1 = b1[0]
        if isinstance(b1, str):
            b1 = f'"{b1}"'

        a2 = asset_band_2.asset
        if a2 is None:
            raise ValueError("Asset band 2 must have an asset")
        b2 = asset_band_2.bands
        if len(b2) != 1:
            raise ValueError("Asset band 2 must have exactly one band")
        b2 = b2[0]
        if isinstance(b2, str):
            b2 = f'"{b2}"'

        expression = (
            f'({{"{a1}": {b1}}} - {{"{a2}": {b2}}}) / ({{"{a1}": {b1}}} + {{"{a2}": {b2}}})'
        )

        return PixelsTransform.band_arithmetic(expression, asset_name)

    @staticmethod
    def datetime_difference(
        datetime1: Union[List[Union[datetime.datetime, str]], Tuple[Union[datetime.datetime, str]]],
        datetime2: Union[List[Union[datetime.datetime, str]], Tuple[Union[datetime.datetime, str]]],
        asset: str,
        band: Union[int, str],
        asset_name: str,
    ) -> "PixelsTransform":
        """Creates a new asset by calculating the difference between two datetime bands.

        The difference is calculated as (datetime1 - datetime2)

        Note: This middleware will override the datetime field in any request to the new asset.

        Args:
            datetime1: first datetime range
            datetime2: second datetime range
            asset: asset to apply the difference to
            band: band to apply the difference to
            asset_name: name of the asset to create

        Returns:
            PixelsTransform: middleware to calculate the difference between two datetime bands

        Examples:
            >>> # Calculate the difference on the B8 (red) band between January 2021 and 2022
            >>> transform = PixelsTransform.datetime_difference(
            ...     datetime1=[datetime.datetime(2021, 1, 1), datetime.datetime(2021, 1, 31)],
            ...     datetime2=[datetime.datetime(2022, 1, 1), datetime.datetime(2022, 1, 31)],
            ...     asset="B8",
            ...     band=0,
            ...     asset_name="datetime_difference",
            ... )
        """
        if not datetime1 or not datetime2:
            raise ValueError("Must provide two datetime ranges")
        if len(datetime1) != 2 or len(datetime2) != 2:
            raise ValueError("Datetime ranges must have exactly two bounds")
        dt1 = [datetime_to_utc(parsedate(dt)).isoformat() for dt in datetime1]
        dt2 = [datetime_to_utc(parsedate(dt)).isoformat() for dt in datetime2]

        return PixelsTransform(
            type=PIXELS_TRANSFORM_DATETIME_DIFFERENCE,
            properties={
                "datetime1": dt1,
                "datetime2": dt2,
                "asset_name": asset_name,
                "asset": asset,
                "band": band,
            },
        )


class MiddlewareConfig(_APIObject):
    """Configures the Middleware for a Dataset.

    Middleware can be applied to a dataset to perform actions on the data before it is returned to the user, but
    without influencing the underlying data. This can be useful for things like filtering, transforming, or
    enhancing the data in some way. Middleware can be applied to the search and pixels handlers of a dataset.

    Middleware is broken into a few different pieces:

    - Search Filters: These are filters that are applied to the search results of a dataset. They can be used to
        filter the results of a search based on some criteria. These should ONLY be applied to providers that
        don't offer filtering themselves. When in doubt DON'T apply filters. Most providers have them implemented
        and this is generally not needed. If you've implemented a remote provider with a relatively small number
        of features, this can be useful since implementing filtering on the provider side can be difficult.
    - Search Transforms: These are transforms that are applied to the search results of a dataset. They can be used
        to rename fields, combine fields, or otherwise modify the results of a search. These can be applied either
        before or after search filters. In the former case, set `search_transforms_before` and in the latter case,
        set `search_transforms_after`.
    - Pixels Transforms: These are transforms that are applied to the pixels handler of a dataset. They can be used
        to apply colormaps, rescale pixel values, or otherwise modify the pixels data. Many of them can create new
        assets in the dataset while some may modifiy existing assets.

    All of these middleware types can be applied to a dataset by adding them to the `middleware` field of a
    `MiddlewareConfig` object. The order of these operations is important. The first item in `middleware`
    will be applied to the response first, and so on until the last item. Middleware that alters the request
    must be added after any middleware that alters the response. That is, the responses will be altered by the
    middleware in a first to last order, and requests will be modified in a last to first order. Filters must
    be applied AFTER any transforms that they depend on.

    """  # noqa: E501

    middleware = _ListDescr(
        item_type=(SearchFilter, SearchTransform, PixelsTransform, dict),
        coerce_items=True,
        doc="Middleware to apply to a dataset. This can include search filters, search transforms, "
        "and pixels transforms.",
    )
    search_filters = _ListDescr(
        item_type=(SearchFilter, dict),
        coerce_items=True,
        doc="(DEPRECATED) Which filter actions to perform applied to the result of a dataset.",
    )
    search_transforms_before = _ListDescr(
        item_type=(SearchTransform, dict),
        coerce_items=True,
        doc="(DEPRECATED) transforms to be applied to each feature/item in a search response. "
        "This is applied BEFORE any filtering takes place",
    )
    search_transforms_after = _ListDescr(
        item_type=(SearchTransform, dict),
        coerce_items=True,
        doc="(DEPRECATED) transforms to be applied to each feature/item in a search response. "
        "This is applied AFTER any filtering takes place",
    )
    pixels_transforms = _ListDescr(
        item_type=(PixelsTransform, dict),
        coerce_items=True,
        doc="(DEPRECATED) transforms the request/response of a pixels handler. Useful for "
        "things like applying colormaps or more complex transformations on the pixels data.",
    )


def _default_datetime_range_props(
    start: Union[datetime.datetime, str] = None,
    end: Union[datetime.datetime, str] = None,
    before_now: datetime.timedelta = None,
) -> dict:
    if all([start is None, end is None, before_now is None]):
        raise ValueError("Must provide at least a start, end, or before_now")

    datetime_specified = start is not None or end is not None
    before_now_specified = before_now is not None

    if datetime_specified and before_now_specified:
        raise ValueError("Cannot provide both a before_now and a start/end")

    if before_now_specified:
        return {"seconds_before_now": before_now.total_seconds()}

    start = datetime_to_utc(parsedate(start)).isoformat()
    end = datetime_to_utc(parsedate(end)).isoformat()

    return {"datetime": [start, end]}
