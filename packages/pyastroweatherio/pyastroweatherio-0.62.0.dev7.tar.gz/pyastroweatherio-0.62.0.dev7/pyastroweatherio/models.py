from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, ConfigDict, Field

from pyastroweatherio.const import (
    DEFAULT_ELEVATION,
    DEFAULT_LATITUDE,
    DEFAULT_LONGITUDE,
    DEFAULT_TIMEZONE,
)


class GeoLocationDataModel(BaseModel):
    """Model for the location"""

    model_config = ConfigDict(from_attributes=True)

    latitude: float = Field(default=DEFAULT_LATITUDE)
    longitude: float = Field(default=DEFAULT_LONGITUDE)
    elevation: float = Field(default=DEFAULT_ELEVATION)
    timezone_info: str = Field(default=DEFAULT_TIMEZONE)


class ConditionDataModel(BaseModel):
    """Model for weather conditions"""

    model_config = ConfigDict(from_attributes=True)

    cloudcover: float
    cloud_area_fraction: float
    cloud_area_fraction_high: float
    cloud_area_fraction_low: float
    cloud_area_fraction_medium: float
    fog_area_fraction: float
    seeing: float
    transparency: float
    lifted_index: float
    condition_percentage: int
    rh2m: float
    wind_speed: float
    wind_from_direction: float
    temp2m: float
    dewpoint2m: float
    weather: str
    weather6: str
    precipitation_amount: float
    precipitation_amount6: float


class AtmosphereDataModel(BaseModel):
    """Model for atmosperic conditions"""

    model_config = ConfigDict(from_attributes=True)

    seeing: float
    transparency: float
    lifted_index: float


class SunDataModel(BaseModel):
    """Model for Sun data"""

    model_config = ConfigDict(from_attributes=True)

    altitude: float
    azimuth: float
    next_rising_astro: datetime
    next_rising_civil: datetime
    next_rising_nautical: datetime
    next_setting_astro: datetime
    next_setting_civil: datetime
    next_setting_nautical: datetime
    previous_rising_astro: datetime
    previous_setting_astro: datetime


class MoonDataModel(BaseModel):
    """Model for Moon data"""

    model_config = ConfigDict(from_attributes=True)

    altitude: float
    angular_size: float
    avg_angular_size: float
    avg_distance_km: float
    azimuth: float
    distance: float
    distance_km: float
    next_full_moon: datetime
    next_new_moon: datetime
    next_rising: datetime
    next_setting: datetime
    phase: float
    previous_rising: datetime
    previous_setting: datetime
    relative_distance: float
    relative_size: float


class DarknessDataModel(BaseModel):
    """Model for deep sky darkness"""

    model_config = ConfigDict(from_attributes=True)

    deep_sky_darkness_moon_rises: bool
    deep_sky_darkness_moon_sets: bool
    deep_sky_darkness_moon_always_up: bool
    deep_sky_darkness_moon_always_down: bool
    deep_sky_darkness: float


class TimeDataModel(BaseModel):
    """Model for time data"""

    model_config = ConfigDict(from_attributes=True)

    seventimer_init: datetime
    seventimer_timepoint: int
    forecast_time: datetime


class LocationDataModel(BaseModel):
    """Model for location conditions data"""

    model_config = ConfigDict(from_attributes=True)

    time_data: TimeDataModel
    time_shift: int
    forecast_length: int
    location_data: GeoLocationDataModel
    sun_data: SunDataModel
    moon_data: MoonDataModel
    darkness_data: DarknessDataModel
    night_duration_astronomical: float
    deepsky_forecast: list
    condition_data: ConditionDataModel
    uptonight: list
    uptonight_bodies: list
    uptonight_comets: list


class ForecastDataModel(BaseModel):
    """Model for forecast data"""

    model_config = ConfigDict(from_attributes=True)

    time_data: TimeDataModel
    hour: int
    condition_data: ConditionDataModel


class NightlyConditionsDataModel(BaseModel):
    """Model for nightly conditions data"""

    model_config = ConfigDict(from_attributes=True)

    seventimer_init: datetime
    dayname: str
    hour: int
    nightly_conditions: list
    weather: str
    precipitation_amount6: float


class UpTonightDSODataModel(BaseModel):
    """Model for DSO objects"""

    model_config = ConfigDict(from_attributes=True)

    id: str
    target_name: str
    type: str
    constellation: str
    size: float
    visual_magnitude: float
    meridian_transit: datetime | str
    meridian_antitransit: datetime | str
    foto: float


class UpTonightBodiesDataModel(BaseModel):
    """Model for bodies"""

    model_config = ConfigDict(from_attributes=True)

    target_name: str
    max_altitude: float
    azimuth: float
    max_altitude_time: datetime
    visual_magnitude: float
    meridian_transit: datetime | str
    foto: float


class UpTonightCometsDataModel(BaseModel):
    """Model for comets"""

    model_config = ConfigDict(from_attributes=True)

    designation: str
    distance_au_earth: float
    distance_au_sun: float
    absolute_magnitude: float
    visual_magnitude: float
    altitude: float
    azimuth: float
    rise_time: datetime
    set_time: datetime
