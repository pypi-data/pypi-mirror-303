"""Data models for various GTFS tables using pandera library.

The module includes the following classes:

- AgencyTable: Optional. Represents the Agency table in the GTFS dataset.
- WranglerStopsTable: Represents the Stops table in the GTFS dataset.
- RoutesTable: Represents the Routes table in the GTFS dataset.
- WranglerShapesTable: Represents the Shapes table in the GTFS dataset.
- WranglerStopTimesTable: Represents the Stop Times table in the GTFS dataset.
- WranglerTripsTable: Represents the Trips table in the GTFS dataset.

Each table model leverages the Pydantic data models defined in the records module to define the
data model for the corresponding table. The classes also include additional configurations for,
such as uniqueness constraints.

!!! example "Validating a table to the WranglerStopsTable"

    ```python
    from network_wrangler.models.gtfs.tables import WranglerStopsTable
    from network_wrangler.utils.modesl import validate_df_to_model

    validated_stops_df = validate_df_to_model(stops_df, WranglerStopsTable)
    ```
"""

from typing import ClassVar, Optional

import pandas as pd
import pandera as pa
from pandas import Timestamp
from pandera.typing import Category, Series

from ...logger import WranglerLogger
from ...params import DEFAULT_TIMESPAN
from ...utils.time import str_to_time, str_to_time_series
from .._base.db import TableForeignKeys, TablePrimaryKeys
from .._base.types import TimeString
from .table_types import HttpURL
from .types import (
    BikesAllowed,
    DirectionID,
    LocationType,
    PickupDropoffType,
    RouteType,
    TimepointType,
    WheelchairAccessible,
)


class AgenciesTable(pa.DataFrameModel):
    """Represents the Agency table in the GTFS dataset.

    For field definitions, see the GTFS reference: <https://gtfs.org/documentation/schedule/reference/#agencytxt>

    Attributes:
        agency_id (str): The agency_id. Primary key. Required to be unique.
        agency_name (str): The agency name.
        agency_url (str): The agency URL.
        agency_timezone (str): The agency timezone.
        agency_lang (str): The agency language.
        agency_phone (str): The agency phone number.
        agency_fare_url (str): The agency fare URL.
        agency_email (str): The agency email.
    """

    agency_id: Series[str] = pa.Field(coerce=True, nullable=False, unique=True)
    agency_name: Series[str] = pa.Field(coerce=True, nullable=True)
    agency_url: Series[HttpURL] = pa.Field(coerce=True, nullable=True)
    agency_timezone: Series[str] = pa.Field(coerce=True, nullable=True)
    agency_lang: Series[str] = pa.Field(coerce=True, nullable=True)
    agency_phone: Series[str] = pa.Field(coerce=True, nullable=True)
    agency_fare_url: Series[str] = pa.Field(coerce=True, nullable=True)
    agency_email: Series[str] = pa.Field(coerce=True, nullable=True)

    class Config:
        """Config for the AgenciesTable data model."""

        coerce = True
        add_missing_columns = True
        _pk: ClassVar[TablePrimaryKeys] = ["agency_id"]


class StopsTable(pa.DataFrameModel):
    """Represents the Stops table in the GTFS dataset.

    For field definitions, see the GTFS reference: <https://gtfs.org/documentation/schedule/reference/#stopstxt>

    Attributes:
        stop_id (str): The stop_id. Primary key. Required to be unique.
        stop_lat (float): The stop latitude.
        stop_lon (float): The stop longitude.
        wheelchair_boarding (Optional[int]): The wheelchair boarding.
        stop_code (Optional[str]): The stop code.
        stop_name (Optional[str]): The stop name.
        tts_stop_name (Optional[str]): The text-to-speech stop name.
        stop_desc (Optional[str]): The stop description.
        zone_id (Optional[str]): The zone id.
        stop_url (Optional[str]): The stop URL.
        location_type (Optional[LocationType]): The location type. Values can be:
            - 0: stop platform
            - 1: station
            - 2: entrance/exit
            - 3: generic node
            - 4: boarding area
            Default of blank assumes a stop platform.
        parent_station (Optional[str]): The `stop_id` of the parent station.
        stop_timezone (Optional[str]): The stop timezone.
    """

    stop_id: Series[str] = pa.Field(coerce=True, nullable=False, unique=True)
    stop_lat: Series[float] = pa.Field(coerce=True, nullable=False, ge=-90, le=90)
    stop_lon: Series[float] = pa.Field(coerce=True, nullable=False, ge=-180, le=180)

    # Optional Fields
    wheelchair_boarding: Optional[Series[Category]] = pa.Field(
        dtype_kwargs={"categories": WheelchairAccessible}, coerce=True, default=0
    )
    stop_code: Optional[Series[str]] = pa.Field(nullable=True, coerce=True)
    stop_name: Optional[Series[str]] = pa.Field(nullable=True, coerce=True)
    tts_stop_name: Optional[Series[str]] = pa.Field(nullable=True, coerce=True)
    stop_desc: Optional[Series[str]] = pa.Field(nullable=True, coerce=True)
    zone_id: Optional[Series[str]] = pa.Field(nullable=True, coerce=True)
    stop_url: Optional[Series[str]] = pa.Field(nullable=True, coerce=True)
    location_type: Optional[Series[Category]] = pa.Field(
        dtype_kwargs={"categories": LocationType},
        nullable=True,
        coerce=True,
        default=0,
    )
    parent_station: Optional[Series[str]] = pa.Field(nullable=True, coerce=True)
    stop_timezone: Optional[Series[str]] = pa.Field(nullable=True, coerce=True)

    class Config:
        """Config for the StopsTable data model."""

        coerce = True
        add_missing_columns = True
        _pk: ClassVar[TablePrimaryKeys] = ["stop_id"]
        _fk: ClassVar[TableForeignKeys] = {"parent_station": ("stops", "stop_id")}


class WranglerStopsTable(StopsTable):
    """Wrangler flavor of GTFS StopsTable.

    For field definitions, see the GTFS reference: <https://gtfs.org/documentation/schedule/reference/#stopstxt>

    Attributes:
        stop_id (int): The stop_id. Primary key. Required to be unique. **Wrangler assumes that this is a reference to a roadway node and as such must be an integer**
        stop_lat (float): The stop latitude.
        stop_lon (float): The stop longitude.
        wheelchair_boarding (Optional[int]): The wheelchair boarding.
        stop_code (Optional[str]): The stop code.
        stop_name (Optional[str]): The stop name.
        tts_stop_name (Optional[str]): The text-to-speech stop name.
        stop_desc (Optional[str]): The stop description.
        zone_id (Optional[str]): The zone id.
        stop_url (Optional[str]): The stop URL.
        location_type (Optional[LocationType]): The location type. Values can be:
            - 0: stop platform
            - 1: station
            - 2: entrance/exit
            - 3: generic node
            - 4: boarding area
            Default of blank assumes a stop platform.
        parent_station (Optional[int]): The `stop_id` of the parent station. **Since stop_id is an integer in Wrangler, this field is also an integer**
        stop_timezone (Optional[str]): The stop timezone.
        stop_id_GTFS (Optional[str]): The stop_id from the GTFS data.
        projects (str): A comma-separated string value for projects that have been applied to this stop.
    """

    stop_id: Series[int] = pa.Field(
        coerce=True, nullable=False, unique=True, description="The model_node_id."
    )
    stop_id_GTFS: Series[str] = pa.Field(
        coerce=True,
        nullable=True,
        description="The stop_id from the GTFS data",
    )
    stop_lat: Series[float] = pa.Field(coerce=True, nullable=True, ge=-90, le=90)
    stop_lon: Series[float] = pa.Field(coerce=True, nullable=True, ge=-180, le=180)
    projects: Series[str] = pa.Field(coerce=True, default="")


class RoutesTable(pa.DataFrameModel):
    """Represents the Routes table in the GTFS dataset.

    For field definitions, see the GTFS reference: <https://gtfs.org/documentation/schedule/reference/#routestxt>

    Attributes:
        route_id (str): The route_id. Primary key. Required to be unique.
        route_short_name (Optional[str]): The route short name.
        route_long_name (Optional[str]): The route long name.
        route_type (RouteType): The route type. Required. Values can be:
            - 0: Tram, Streetcar, Light rail
            - 1: Subway, Metro
            - 2: Rail
            - 3: Bus
        agency_id (Optional[str]): The agency_id. Foreign key to agency_id in the agencies table.
        route_desc (Optional[str]): The route description.
        route_url (Optional[str]): The route URL.
        route_color (Optional[str]): The route color.
        route_text_color (Optional[str]): The route text color.
    """

    route_id: Series[str] = pa.Field(nullable=False, unique=True, coerce=True)
    route_short_name: Series[str] = pa.Field(nullable=True, coerce=True)
    route_long_name: Series[str] = pa.Field(nullable=True, coerce=True)
    route_type: Series[Category] = pa.Field(
        dtype_kwargs={"categories": RouteType}, coerce=True, nullable=False
    )

    # Optional Fields
    agency_id: Optional[Series[str]] = pa.Field(nullable=True, coerce=True)
    route_desc: Optional[Series[str]] = pa.Field(nullable=True, coerce=True)
    route_url: Optional[Series[str]] = pa.Field(nullable=True, coerce=True)
    route_color: Optional[Series[str]] = pa.Field(nullable=True, coerce=True)
    route_text_color: Optional[Series[str]] = pa.Field(nullable=True, coerce=True)

    class Config:
        """Config for the RoutesTable data model."""

        coerce = True
        add_missing_columns = True
        _pk: ClassVar[TablePrimaryKeys] = ["route_id"]
        _fk: ClassVar[TableForeignKeys] = {"agency_id": ("agencies", "agency_id")}


class ShapesTable(pa.DataFrameModel):
    """Represents the Shapes table in the GTFS dataset.

    For field definitions, see the GTFS reference: <https://gtfs.org/documentation/schedule/reference/#shapestxt>

    Attributes:
        shape_id (str): The shape_id. Primary key. Required to be unique.
        shape_pt_lat (float): The shape point latitude.
        shape_pt_lon (float): The shape point longitude.
        shape_pt_sequence (int): The shape point sequence.
        shape_dist_traveled (Optional[float]): The shape distance traveled.
    """

    shape_id: Series[str] = pa.Field(nullable=False, coerce=True)
    shape_pt_lat: Series[float] = pa.Field(coerce=True, nullable=False, ge=-90, le=90)
    shape_pt_lon: Series[float] = pa.Field(coerce=True, nullable=False, ge=-180, le=180)
    shape_pt_sequence: Series[int] = pa.Field(coerce=True, nullable=False, ge=0)

    # Optional
    shape_dist_traveled: Optional[Series[float]] = pa.Field(coerce=True, nullable=True, ge=0)

    class Config:
        """Config for the ShapesTable data model."""

        coerce = True
        add_missing_columns = True
        _pk: ClassVar[TablePrimaryKeys] = ["shape_id", "shape_pt_sequence"]
        _fk: ClassVar[TableForeignKeys] = {}
        unique: ClassVar[list[str]] = ["shape_id", "shape_pt_sequence"]


class WranglerShapesTable(ShapesTable):
    """Wrangler flavor of GTFS ShapesTable.

     For field definitions, see the GTFS reference: <https://gtfs.org/documentation/schedule/reference/#shapestxt>

    Attributes:
        shape_id (str): The shape_id. Primary key. Required to be unique.
        shape_pt_lat (float): The shape point latitude.
        shape_pt_lon (float): The shape point longitude.
        shape_pt_sequence (int): The shape point sequence.
        shape_dist_traveled (Optional[float]): The shape distance traveled.
        shape_model_node_id (int): The model_node_id of the shape point. Foreign key to the model_node_id in the nodes table.
        projects (str): A comma-separated string value for projects that have been applied to this shape.
    """

    shape_model_node_id: Series[int] = pa.Field(coerce=True, nullable=False)
    projects: Series[str] = pa.Field(coerce=True, default="")


class TripsTable(pa.DataFrameModel):
    """Represents the Trips table in the GTFS dataset.

    For field definitions, see the GTFS reference: <https://gtfs.org/documentation/schedule/reference/#tripstxt>

    Attributes:
        trip_id (str): Primary key. Required to be unique.
        shape_id (str): Foreign key to `shape_id` in the shapes table.
        direction_id (DirectionID): The direction id. Required. Values can be:
            - 0: Outbound
            - 1: Inbound
        service_id (str): The service id.
        route_id (str): The route id. Foreign key to `route_id` in the routes table.
        trip_short_name (Optional[str]): The trip short name.
        trip_headsign (Optional[str]): The trip headsign.
        block_id (Optional[str]): The block id.
        wheelchair_accessible (Optional[int]): The wheelchair accessible. Values can be:
            - 0: No information
            - 1: Allowed
            - 2: Not allowed
        bikes_allowed (Optional[int]): The bikes allowed. Values can be:
            - 0: No information
            - 1: Allowed
            - 2: Not allowed
    """

    trip_id: Series[str] = pa.Field(nullable=False, unique=True, coerce=True)
    shape_id: Series[str] = pa.Field(nullable=False, coerce=True)
    direction_id: Series[Category] = pa.Field(
        dtype_kwargs={"categories": DirectionID}, coerce=True, nullable=False, default=0
    )
    service_id: Series[str] = pa.Field(nullable=False, coerce=True, default="1")
    route_id: Series[str] = pa.Field(nullable=False, coerce=True)

    # Optional Fields
    trip_short_name: Optional[Series[str]] = pa.Field(nullable=True, coerce=True)
    trip_headsign: Optional[Series[str]] = pa.Field(nullable=True, coerce=True)
    block_id: Optional[Series[str]] = pa.Field(nullable=True, coerce=True)
    wheelchair_accessible: Optional[Series[Category]] = pa.Field(
        dtype_kwargs={"categories": WheelchairAccessible}, coerce=True, default=0
    )
    bikes_allowed: Optional[Series[Category]] = pa.Field(
        dtype_kwargs={"categories": BikesAllowed},
        coerce=True,
        default=0,
    )

    class Config:
        """Config for the TripsTable data model."""

        coerce = True
        add_missing_columns = True
        _pk: ClassVar[TablePrimaryKeys] = ["trip_id"]
        _fk: ClassVar[TableForeignKeys] = {"route_id": ("routes", "route_id")}


class WranglerTripsTable(TripsTable):
    """Represents the Trips table in the Wrangler feed, adding projects list.

    For field definitions, see the GTFS reference: <https://gtfs.org/documentation/schedule/reference/#tripstxt>

    Attributes:
        trip_id (str): Primary key. Required to be unique.
        shape_id (str): Foreign key to `shape_id` in the shapes table.
        direction_id (DirectionID): The direction id. Required. Values can be:
            - 0: Outbound
            - 1: Inbound
        service_id (str): The service id.
        route_id (str): The route id. Foreign key to `route_id` in the routes table.
        trip_short_name (Optional[str]): The trip short name.
        trip_headsign (Optional[str]): The trip headsign.
        block_id (Optional[str]): The block id.
        wheelchair_accessible (Optional[int]): The wheelchair accessible. Values can be:
            - 0: No information
            - 1: Allowed
            - 2: Not allowed
        bikes_allowed (Optional[int]): The bikes allowed. Values can be:
            - 0: No information
            - 1: Allowed
            - 2: Not allowed
        projects (str): A comma-separated string value for projects that have been applied to this trip.
    """

    projects: Series[str] = pa.Field(coerce=True, default="")

    class Config:
        """Config for the WranglerTripsTable data model."""

        coerce = True
        add_missing_columns = True
        _pk: ClassVar[TablePrimaryKeys] = ["trip_id"]
        _fk: ClassVar[TableForeignKeys] = {"route_id": ("routes", "route_id")}


class FrequenciesTable(pa.DataFrameModel):
    """Represents the Frequency table in the GTFS dataset.

    For field definitions, see the GTFS reference: <https://gtfs.org/documentation/schedule/reference/#frequenciestxt>

    The primary key of this table is a composite key of `trip_id` and `start_time`.

    Attributes:
        trip_id (str): Foreign key to `trip_id` in the trips table.
        start_time (TimeString): The start time in HH:MM:SS format.
        end_time (TimeString): The end time in HH:MM:SS format.
        headway_secs (int): The headway in seconds.
    """

    trip_id: Series[str] = pa.Field(nullable=False, coerce=True)
    start_time: Series[TimeString] = pa.Field(
        nullable=False, coerce=True, default=DEFAULT_TIMESPAN[0]
    )
    end_time: Series[TimeString] = pa.Field(
        nullable=False, coerce=True, default=DEFAULT_TIMESPAN[1]
    )
    headway_secs: Series[int] = pa.Field(
        coerce=True,
        ge=1,
        nullable=False,
    )

    class Config:
        """Config for the FrequenciesTable data model."""

        coerce = True
        add_missing_columns = True
        unique: ClassVar[list[str]] = ["trip_id", "start_time"]
        _pk: ClassVar[TablePrimaryKeys] = ["trip_id", "start_time"]
        _fk: ClassVar[TableForeignKeys] = {"trip_id": ("trips", "trip_id")}


class WranglerFrequenciesTable(FrequenciesTable):
    """Wrangler flavor of GTFS FrequenciesTable.

    For field definitions, see the GTFS reference: <https://gtfs.org/documentation/schedule/reference/#frequenciestxt>

    The primary key of this table is a composite key of `trip_id` and `start_time`.

    Attributes:
        trip_id (str): Foreign key to `trip_id` in the trips table.
        start_time (datetime.datetime): The start time in datetime format.
        end_time (datetime.datetime): The end time in datetime format.
        headway_secs (int): The headway in seconds.
    """

    projects: Series[str] = pa.Field(coerce=True, default="")
    start_time: Series = pa.Field(
        nullable=False, coerce=True, default=str_to_time(DEFAULT_TIMESPAN[0])
    )
    end_time: Series = pa.Field(
        nullable=False, coerce=True, default=str_to_time(DEFAULT_TIMESPAN[1])
    )

    class Config:
        """Config for the FrequenciesTable data model."""

        coerce = True
        add_missing_columns = True
        unique: ClassVar[list[str]] = ["trip_id", "start_time"]
        _pk: ClassVar[TablePrimaryKeys] = ["trip_id", "start_time"]
        _fk: ClassVar[TableForeignKeys] = {"trip_id": ("trips", "trip_id")}

    @pa.parser("start_time")
    def st_to_timestamp(cls, series: Series) -> Series[Timestamp]:
        """Check that start time is timestamp."""
        series = series.fillna(str_to_time(DEFAULT_TIMESPAN[0]))
        if series.dtype == "datetime64[ns]":
            return series
        series = str_to_time_series(series)
        return series.astype("datetime64[ns]")

    @pa.parser("end_time")
    def et_to_timestamp(cls, series: Series) -> Series[Timestamp]:
        """Check that start time is timestamp."""
        series = series.fillna(str_to_time(DEFAULT_TIMESPAN[1]))
        if series.dtype == "datetime64[ns]":
            return series
        return str_to_time_series(series)


class StopTimesTable(pa.DataFrameModel):
    """Represents the Stop Times table in the GTFS dataset.

    For field definitions, see the GTFS reference: <https://gtfs.org/documentation/schedule/reference/#stop_timestxt>

    The primary key of this table is a composite key of `trip_id` and `stop_sequence`.

    Attributes:
        trip_id (str): Foreign key to `trip_id` in the trips table.
        stop_id (str): Foreign key to `stop_id` in the stops table.
        stop_sequence (int): The stop sequence.
        pickup_type (PickupDropoffType): The pickup type. Values can be:
            - 0: Regularly scheduled pickup
            - 1: No pickup available
            - 2: Must phone agency to arrange pickup
            - 3: Must coordinate with driver to arrange pickup
        drop_off_type (PickupDropoffType): The drop off type. Values can be:
            - 0: Regularly scheduled drop off
            - 1: No drop off available
            - 2: Must phone agency to arrange drop off
            - 3: Must coordinate with driver to arrange drop off
        arrival_time (TimeString): The arrival time in HH:MM:SS format.
        departure_time (TimeString): The departure time in HH:MM:SS format.
        shape_dist_traveled (Optional[float]): The shape distance traveled.
        timepoint (Optional[TimepointType]): The timepoint type. Values can be:
            - 0: The stop is not a timepoint
            - 1: The stop is a timepoint
    """

    trip_id: Series[str] = pa.Field(nullable=False, coerce=True)
    stop_id: Series[str] = pa.Field(nullable=False, coerce=True)
    stop_sequence: Series[int] = pa.Field(nullable=False, coerce=True, ge=0)
    pickup_type: Series[Category] = pa.Field(
        dtype_kwargs={"categories": PickupDropoffType},
        nullable=True,
        coerce=True,
    )
    drop_off_type: Series[Category] = pa.Field(
        dtype_kwargs={"categories": PickupDropoffType},
        nullable=True,
        coerce=True,
    )
    arrival_time: Series[TimeString] = pa.Field(nullable=True, coerce=True)
    departure_time: Series[TimeString] = pa.Field(nullable=True, coerce=True)

    # Optional
    shape_dist_traveled: Optional[Series[float]] = pa.Field(coerce=True, nullable=True, ge=0)
    timepoint: Optional[Series[Category]] = pa.Field(
        dtype_kwargs={"categories": TimepointType}, coerce=True, default=0
    )

    class Config:
        """Config for the StopTimesTable data model."""

        coerce = True
        add_missing_columns = True
        _pk: ClassVar[TablePrimaryKeys] = ["trip_id", "stop_sequence"]
        _fk: ClassVar[TableForeignKeys] = {
            "trip_id": ("trips", "trip_id"),
            "stop_id": ("stops", "stop_id"),
        }

        unique: ClassVar[list[str]] = ["trip_id", "stop_sequence"]


class WranglerStopTimesTable(StopTimesTable):
    """Wrangler flavor of GTFS StopTimesTable.

    For field definitions, see the GTFS reference: <https://gtfs.org/documentation/schedule/reference/#stop_timestxt>

    The primary key of this table is a composite key of `trip_id` and `stop_sequence`.

    Attributes:
        trip_id (str): Foreign key to `trip_id` in the trips table.
        stop_id (int): Foreign key to `stop_id` in the stops table.
        stop_sequence (int): The stop sequence.
        pickup_type (PickupDropoffType): The pickup type. Values can be:
            - 0: Regularly scheduled pickup
            - 1: No pickup available
            - 2: Must phone agency to arrange pickup
            - 3: Must coordinate with driver to arrange pickup
        drop_off_type (PickupDropoffType): The drop off type. Values can be:
            - 0: Regularly scheduled drop off
            - 1: No drop off available
            - 2: Must phone agency to arrange drop off
            - 3: Must coordinate with driver to arrange drop off
        arrival_time (datetime.datetime): The arrival time in datetime format.
        departure_time (datetime.datetime): The departure time in datetime format.
        shape_dist_traveled (Optional[float]): The shape distance traveled.
        timepoint (Optional[TimepointType]): The timepoint type. Values can be:
            - 0: The stop is not a timepoint
            - 1: The stop is a timepoint
        projects (str): A comma-separated string value for projects that have been applied to this stop.
    """

    stop_id: Series[int] = pa.Field(nullable=False, coerce=True, description="The model_node_id.")
    arrival_time: Series[Timestamp] = pa.Field(nullable=True, default=pd.NaT, coerce=False)
    departure_time: Series[Timestamp] = pa.Field(nullable=True, default=pd.NaT, coerce=False)
    projects: Series[str] = pa.Field(coerce=True, default="")

    @pa.dataframe_parser
    def parse_times(cls, df):
        """Parse arrival and departure times.

        - Check that all times are timestamps <24h.
        - Check that arrival_time and departure_time are not both "00:00:00".  If so, set
            them to NaT.

        """
        # if arrival_time and departure_time are not set or are both set to "00:00:00", set them to NaT
        if "arrival_time" not in df.columns:
            df["arrival_time"] = pd.NaT
        if "departure_time" not in df.columns:
            df["departure_time"] = pd.NaT
        msg = f"stop_times before parsing: \n {df[['arrival_time', 'departure_time']]}"
        # WranglerLogger.debug(msg)
        filler_timestrings = (df["arrival_time"] == Timestamp("00:00:00")) & (
            df["departure_time"] == Timestamp("00:00:00")
        )

        df.loc[filler_timestrings, "arrival_time"] = pd.NaT
        df.loc[filler_timestrings, "departure_time"] = pd.NaT
        msg = f"stop_times after filling with NaT: \n {df[['arrival_time', 'departure_time']]}"
        # WranglerLogger.debug(msg)
        df["arrival_time"] = str_to_time_series(df["arrival_time"])
        df["departure_time"] = str_to_time_series(df["departure_time"])
        msg = f"stop_times after parsing: \n{df[['arrival_time', 'departure_time']]}"
        # WranglerLogger.debug(msg)
        return df

    class Config:
        """Config for the StopTimesTable data model."""

        coerce = True
        add_missing_columns = True
        _pk: ClassVar[TablePrimaryKeys] = ["trip_id", "stop_sequence"]
        _fk: ClassVar[TableForeignKeys] = {
            "trip_id": ("trips", "trip_id"),
            "stop_id": ("stops", "stop_id"),
        }

        unique: ClassVar[list[str]] = ["trip_id", "stop_sequence"]
