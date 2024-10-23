import datetime
from typing import Union

from geodesic.bases import _APIObject
from geodesic.descriptors import (
    _StringDescr,
    _BoolDescr,
    _ListDescr,
    _DictDescr,
    _IntDescr,
    _BaseDescr,
    _FloatDescr,
    _TypeConstrainedDescr,
)
from geodesic.boson.middleware import MiddlewareConfig
from geodesic.boson.tile_options import TileOptions
from geodesic.boson.servicer_settings import ServicerSettings

# Credential Keys
DEFAULT_CREDENTIAL_KEY = "default"
STORAGE_CREDENTIAL_KEY = "storage"
API_CREDENTIAL_KEY = "api"


class CacheConfig(_APIObject):
    """Cache Configuration.

    This tells Boson how it should cache data from the provider.

    There are two main options that can be controled here:

    `enabled`: whether or not to cache data in the persistent cache. This is typically configured
        to be cloud storage like S3 or GCS. Whether enabled is True or not, Boson will perform some
        level of internal caching, but the cache will not be backed by a persistent store unless
        this is set to True.
    `ttl`: time to live for cached items in seconds. For quickly changing data, this should be set
        to a low value. This defaults to 5 minutes if not set. If this value is greater than the
        default TTL of the internal cache (5 minutes), this TTL will only correspond to the
        persistent cache. If the value is less than the internal cache, the internal cache will use
        a TTL less than or equal to this value. If `enabled` is False and this value is set to a
        value greater than 5 minutes, Boson will cap the TTL at 5 minutes.

    Args:
        enabled (bool): enable/disable persistent caching for a particular provider.
        ttl (Union[datetime.timedelta, int, float]): time to live for cached items in seconds. For
            quickly changing data, this should be set to a low value. Default is 5 minutes
            if not set.

    """

    enabled = _BoolDescr(doc="enable/disable caching for a particular provider")
    ttl_seconds = _FloatDescr(doc="time to live for cached items in seconds")

    def __init__(
        self,
        enabled: bool = False,
        ttl: Union[datetime.timedelta, int, float] = None,
        **kwargs,
    ):
        ttl_seconds = None
        if isinstance(ttl, datetime.timedelta):
            ttl_seconds = int(ttl.total_seconds())
        elif isinstance(ttl, (int, float)):
            ttl_seconds = float(ttl)

        if ttl_seconds is not None:
            kwargs["ttl_seconds"] = ttl_seconds
        super().__init__(enabled=enabled, **kwargs)


class BosonConfig(_APIObject):
    """BosonConfig Provider Configuration.

    This tells Boson how it should access the underlying data.
    """

    provider_name = _StringDescr(doc="the name of the provider this Boson uses")
    url = _StringDescr(doc="the url of the service this refers to (if any)")
    thread_safe = _BoolDescr(doc="is this particular provider implementation thread safe")
    pass_headers = _ListDescr(doc="list of headers that this provider should pass to backend")
    max_page_size = _IntDescr(doc="the max number of records this provider can page through")
    properties = _DictDescr(doc="additional provider-specific properties")
    credentials = _DictDescr(doc="credentials that are needed by this provider")
    middleware = _TypeConstrainedDescr((MiddlewareConfig, dict), doc="user configured middleware")
    cache = _TypeConstrainedDescr((CacheConfig, dict), doc="user configured cache config")
    tile_options = _TypeConstrainedDescr((TileOptions, dict), doc="user configured tile options")
    servicer_settings = _TypeConstrainedDescr(
        (ServicerSettings, dict), doc="user configured servicer settings"
    )
    max_get_pixels_features = _IntDescr(
        doc="max number of input rasters to mosaic in a get_pixels request"
    )


class BosonDescr(_BaseDescr):
    """A Boson Provider Config.

    __get__ returns a BosonConfig object.

    __set__ sets from a dictionary or BosonConfig, coercing to a BosonConfig if needed and stores
        internally to the APIObject dict.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._type = (BosonConfig, dict)

    def _get(self, obj: object, objtype=None) -> dict:
        # Try to get the private attribute by name (e.g. '_boson_config')
        b = getattr(obj, self.private_name, None)
        if b is not None:
            # Return it if it exists
            return b

        try:
            b = self._get_object(obj)
            if isinstance(b, dict):
                b = BosonConfig(**b)
            self._set(obj, b)
            setattr(obj, self.private_name, b)
        except KeyError:
            if self.default is None:
                self._attribute_error(objtype)
            self._set(obj, self.default)
            return self.default
        return b

    def _set(self, obj: object, value: object) -> None:
        # Reset the private attribute (e.g. "_boson_config") to None
        setattr(obj, self.private_name, None)

        if isinstance(value, BosonConfig):
            self._set_object(obj, value)
        elif isinstance(value, dict):
            self._set_object(obj, BosonConfig(**value))
        else:
            raise ValueError(f"invalid value type {type(value)}")

    def _validate(self, obj: object, value: object) -> None:
        if not isinstance(value, (BosonConfig, dict)):
            raise ValueError(f"'{self.public_name}' must be a BosonConfig or a dict")

        try:
            BosonConfig(**value)
        except Exception as e:
            raise ValueError("boson config is invalid") from e
