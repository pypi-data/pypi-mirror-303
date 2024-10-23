"""Defines the Data Classes used."""

import math
from datetime import datetime

from pprint import pprint as pp

from pyastroweatherio.const import (
    CONDITION,
    CONDITION_PLAIN,
    DEEP_SKY_THRESHOLD,
    LIFTED_INDEX_PLAIN,
    LIFTED_INDEX_RANGE,
    LIFTED_INDEX_VALUE,
    MAG_DEGRATION_MAX,
    SEEING_MAX,
    WIND10M_DIRECTON,
    WIND10M_MAX,
    WIND10M_PLAIN,
    WIND10M_RANGE,
    WIND10M_VALUE,
)


class TimeData:
    """A representation of the time data of forecasts."""

    def __init__(self, *, data: dict):
        self.seventimer_init = data["seventimer_init"]
        self.seventimer_timepoint = data["seventimer_timepoint"]
        self.forecast_time = data["forecast_time"]

    # @property
    # def seventimer_timepoint(self) -> datetime:
    #     """Return Forecast Anchor."""

    #     return self.seventimer_timepoint.replace(microsecond=0, tzinfo=timezone.utc)

    # @seventimer_timepoint.setter
    # def seventimer_timepoint(self, timepoint):
    #     self.seventimer_timepoint = timepoint


class GeoLocationData:
    """A representation of the geographic location."""

    def __init__(self, *, data: dict):
        self.latitude = data["latitude"]
        self.longitude = data["longitude"]
        self.elevation = data["elevation"]
        self.timezone_info = data["timezone_info"]


class AtmosphereData:
    """A representation of atmospheric condition base class."""

    def __init__(self, *, data: dict):
        self.seeing = data["seeing"]
        self.transparency = data["transparency"]
        self.lifted_index = data["lifted_index"]


class SunData:
    """A representation of Sun data class."""

    def __init__(self, *, data: dict):
        self.altitude = data["altitude"]
        self.azimuth = data["azimuth"]
        self.next_rising_astro = data["next_rising_astro"]
        self.next_rising_civil = data["next_rising_civil"]
        self.next_rising_nautical = data["next_rising_nautical"]
        self.next_setting_astro = data["next_setting_astro"]
        self.next_setting_civil = data["next_setting_civil"]
        self.next_setting_nautical = data["next_setting_nautical"]
        self.previous_rising_astro = data["previous_rising_astro"]
        self.previous_setting_astro = data["previous_setting_astro"]


class MoonData:
    """A representation of Moon data class."""

    def __init__(self, *, data: dict):
        self.altitude = data["altitude"]
        self.angular_size = data["angular_size"]
        self.avg_angular_size = data["avg_angular_size"]
        self.avg_distance_km = data["avg_distance_km"]
        self.azimuth = data["azimuth"]
        self.distance = data["distance"]
        self.distance_km = data["distance_km"]
        self.next_full_moon = data["next_full_moon"]
        self.next_new_moon = data["next_new_moon"]
        self.next_rising = data["next_rising"]
        self.next_setting = data["next_setting"]
        self.phase = data["phase"]
        self.previous_rising = data["previous_rising"]
        self.previous_setting = data["previous_setting"]
        self.relative_distance = data["relative_distance"]
        self.relative_size = data["relative_size"]


class DarknessData:
    """A representation of darkness data class."""

    def __init__(self, *, data: dict):
        self.deep_sky_darkness_moon_rises = data["deep_sky_darkness_moon_rises"]
        self.deep_sky_darkness_moon_sets = data["deep_sky_darkness_moon_sets"]
        self.deep_sky_darkness_moon_always_up = data["deep_sky_darkness_moon_always_up"]
        self.deep_sky_darkness_moon_always_down = data["deep_sky_darkness_moon_always_down"]
        self.deep_sky_darkness = data["deep_sky_darkness"]


class ConditionData:
    """A representation of the condition base class."""

    def __init__(self, *, data: dict):
        self.cloudcover = data["cloudcover"]
        self.cloud_area_fraction = data["cloud_area_fraction"]
        self.cloud_area_fraction_high = data["cloud_area_fraction_high"]
        self.cloud_area_fraction_low = data["cloud_area_fraction_low"]
        self.cloud_area_fraction_medium = data["cloud_area_fraction_medium"]
        self.fog_area_fraction = data["fog_area_fraction"]
        self._seeing = data["seeing"]
        self._transparency = data["transparency"]
        self._lifted_index = data["lifted_index"]
        self.condition_percentage = data["condition_percentage"]
        self.rh2m = data["rh2m"]
        self.wind_speed = data["wind_speed"]
        self.wind_from_direction = data["wind_from_direction"]
        self.temp2m = data["temp2m"]
        self._dewpoint2m = data["dewpoint2m"]
        self._weather = data["weather"]
        self._weather6 = data["weather6"]
        self.precipitation_amount = data["precipitation_amount"]
        self.precipitation_amount6 = data["precipitation_amount6"]

    # #########################################################################
    # Condition
    # #########################################################################
    @property
    def cloudcover_percentage(self) -> int:
        """Return Cloud Cover Percentage."""

        return self.cloudcover

    @property
    def cloudless_percentage(self) -> int:
        """Return Cloudless Percentage."""

        return 100 - int(self.cloudcover)

    @property
    def cloud_area_fraction_percentage(self) -> int:
        """Return Cloud Cover Percentage."""

        return int(self.cloud_area_fraction)

    @property
    def cloud_area_fraction_high_percentage(self) -> int:
        """Return Cloud Cover Percentage."""

        return int(self.cloud_area_fraction_high)

    @property
    def cloud_area_fraction_medium_percentage(self) -> int:
        """Return Cloud Cover Percentage."""

        return int(self.cloud_area_fraction_medium)

    @property
    def cloud_area_fraction_low_percentage(self) -> int:
        """Return Cloud Cover Percentage."""

        return int(self.cloud_area_fraction_low)

    @property
    def fog_area_fraction_percentage(self) -> int:
        """Return Fog Area Percentage."""

        return int(self.fog_area_fraction)

    @property
    def seeing(self) -> float:
        """Return Seeing."""

        return round(self._seeing, 2)

    @seeing.setter
    def seeing(self, new_value: float):
        self._seeing = new_value

    @property
    def seeing_percentage(self) -> int:
        """Return Seeing Percentage."""

        return int(100 - self._seeing * 100 / SEEING_MAX)

    @property
    def transparency(self) -> float:
        """Return Transparency."""

        return round(self._transparency, 2)

    @transparency.setter
    def transparency(self, new_value: float):
        self._transparency = new_value

    @property
    def transparency_percentage(self) -> int:
        """Return Transparency."""

        return int(100 - self._transparency * 100 / MAG_DEGRATION_MAX)

    @property
    def lifted_index(self) -> float:
        """Return Lifted Index."""

        return round(self._lifted_index, 2)

    @lifted_index.setter
    def lifted_index(self, new_value: float):
        self._lifted_index = new_value

    @property
    def wind10m_speed(self) -> float:
        """Return 10m Wind Speed."""

        return self.wind_speed

    @property
    def calm_percentage(self) -> int:
        """Return 10m Wind Speed."""

        return int(100 - self.wind_speed * (100 / WIND10M_MAX))

    @property
    def wind10m_direction(self) -> str:
        """Return 10m Wind Direction."""

        direction = self.wind_from_direction
        direction += 22.5
        direction = direction % 360
        direction = int(direction / 45)  # values 0 to 7
        return WIND10M_DIRECTON[max(0, min(7, direction))]

    @property
    def dewpoint2m(self) -> float:
        """Return 2m Dew Point."""

        return round(self._dewpoint2m, 1)

    @dewpoint2m.setter
    def dewpoint2m(self, new_value: float):
        self._dewpoint2m = new_value

    @property
    def weather(self) -> str:
        """Return Current Weather."""

        return self._weather.replace("_", " ").capitalize()

    @weather.setter
    def weather(self, new_value: float):
        self._weather = new_value

    @property
    def weather6(self) -> str:
        """Return Current Weather."""

        return self._weather6.replace("_", " ").capitalize()

    @weather6.setter
    def weather6(self, new_value: float):
        self._weather6 = new_value


class UpTonightDSOData:
    """A representation of uptonight DSO."""

    # def __init__(self, data):
    def __init__(self, *, data: dict):
        self.id = data["id"]
        self.target_name = data["target_name"]
        self.type = data["type"]
        self.constellation = data["constellation"]
        self.size = data["size"]
        self.visual_magnitude = data["visual_magnitude"]
        self.meridian_transit = data["meridian_transit"]
        self.meridian_antitransit = data["meridian_antitransit"]
        self.foto = data["foto"]


class UpTonightBodiesData:
    """A representation of uptonight bodies."""

    # def __init__(self, data):
    def __init__(self, *, data: dict):
        self.target_name = data["target_name"]
        self.max_altitude = data["max_altitude"]
        self.azimuth = data["azimuth"]
        self.max_altitude_time = data["max_altitude_time"]
        self.visual_magnitude = data["visual_magnitude"]
        self.meridian_transit = data["meridian_transit"]
        self.foto = data["foto"]


class UpTonightCometsData:
    """A representation of uptonight comets."""

    # def __init__(self, data):
    def __init__(self, *, data: dict):
        self.designation = data["designation"]
        self.distance_au_earth = data["distance_au_earth"]
        self.distance_au_sun = data["distance_au_sun"]
        self.absolute_magnitude = data["absolute_magnitude"]
        self.visual_magnitude = data["visual_magnitude"]
        self.altitude = data["altitude"]
        self.azimuth = data["azimuth"]
        self.rise_time = data["rise_time"]
        self.set_time = data["set_time"]


class LocationData:
    """A representation of the Location AstroWeather Data."""

    # def __init__(self, data):
    def __init__(self, *, data: dict):
        self.time_data = data["time_data"]
        self.time_shift = data["time_shift"]
        self.forecast_length = data["forecast_length"]
        self.location_data = data["location_data"]
        self.sun_data = data["sun_data"]
        self.moon_data = data["moon_data"]
        self.darkness_data = data["darkness_data"]
        self.night_duration_astronomical = data["night_duration_astronomical"]
        self.deepsky_forecast = data["deepsky_forecast"]
        self.condition_data = data["condition_data"]
        self.uptonight = data["uptonight"]
        self.uptonight_bodies = data["uptonight_bodies"]
        self.uptonight_comets = data["uptonight_comets"]

    # #########################################################################
    # Time data
    # #########################################################################
    @property
    def seventimer_init(self) -> datetime:
        return self.time_data.seventimer_init

    @property
    def seventimer_timepoint(self) -> int:
        return self.time_data.seventimer_timepoint

    @property
    def forecast_time(self) -> datetime:
        return self.time_data.forecast_time

    # #########################################################################
    # Location
    # #########################################################################
    @property
    def latitude(self) -> float:
        """Return Latitude."""

        return self.location_data.latitude

    @property
    def longitude(self) -> float:
        """Return Longitude."""

        return self.location_data.longitude

    @property
    def elevation(self) -> float:
        """Return Elevation."""

        return self.location_data.elevation

    # #########################################################################
    # Condition
    # #########################################################################
    @property
    def wind10m_speed_plain(self) -> str:
        """Return wind speed plain."""

        wind_speed_value = 0
        for (start, end), derate in zip(WIND10M_RANGE, WIND10M_VALUE):
            if start <= self.condition_data.wind_speed <= end:
                wind_speed_value = derate

        return WIND10M_PLAIN[max(0, min(7, wind_speed_value - 1))]

    @property
    def lifted_index_plain(self) -> str:
        """Return Lifted Index plain."""

        lifted_index_value = 0
        for (start, end), derate in zip(LIFTED_INDEX_RANGE, LIFTED_INDEX_VALUE):
            if start <= self.condition_data.lifted_index <= end:
                lifted_index_value = derate

        return LIFTED_INDEX_PLAIN[max(0, min(7, lifted_index_value - 1))]

    @property
    def deep_sky_view(self) -> bool:
        """Return True if Deep Sky should be possible."""

        if self.condition_percentage >= DEEP_SKY_THRESHOLD:
            return True
        return False

    @property
    def condition_plain(self) -> str:
        """Return Current View Conditions."""

        if self.condition_percentage > 80:
            return CONDITION_PLAIN[0].capitalize()
        if self.condition_percentage > 60:
            return CONDITION_PLAIN[1].capitalize()
        if self.condition_percentage > 40:
            return CONDITION_PLAIN[2].capitalize()
        if self.condition_percentage > 20:
            return CONDITION_PLAIN[3].capitalize()
        return CONDITION_PLAIN[4].capitalize()

    @property
    def condition_percentage(self) -> int:
        return self.condition_data.condition_percentage

    @property
    def cloudcover_percentage(self) -> int:
        return self.condition_data.cloudcover_percentage

    @property
    def cloudless_percentage(self) -> int:
        return self.condition_data.cloudless_percentage

    @property
    def cloud_area_fraction_percentage(self) -> int:
        return self.condition_data.cloud_area_fraction_percentage

    @property
    def cloud_area_fraction_high_percentage(self) -> int:
        return self.condition_data.cloud_area_fraction_high_percentage

    @property
    def cloud_area_fraction_medium_percentage(self) -> int:
        return self.condition_data.cloud_area_fraction_medium_percentage

    @property
    def cloud_area_fraction_low_percentage(self) -> int:
        return self.condition_data.cloud_area_fraction_low_percentage

    @property
    def seeing(self) -> float:
        return self.condition_data.seeing

    @property
    def seeing_percentage(self) -> int:
        return self.condition_data.seeing_percentage

    @property
    def transparency(self) -> float:
        return self.condition_data.transparency

    @property
    def transparency_percentage(self) -> int:
        return self.condition_data.transparency_percentage

    @property
    def lifted_index(self) -> float:
        return self.condition_data.lifted_index

    @property
    def calm_percentage(self) -> int:
        return self.condition_data.calm_percentage

    @property
    def wind10m_direction(self) -> float:
        return self.condition_data.wind10m_direction

    @property
    def wind10m_speed(self) -> float:
        return self.condition_data.wind10m_speed

    @property
    def temp2m(self) -> float:
        return self.condition_data.temp2m

    @property
    def rh2m(self) -> float:
        return self.condition_data.rh2m

    @property
    def dewpoint2m(self) -> float:
        return self.condition_data.dewpoint2m

    @property
    def weather(self) -> str:
        return self.condition_data.weather

    @property
    def weather6(self) -> str:
        return self.condition_data.weather6

    # #########################################################################
    # Sun
    # #########################################################################
    @property
    def sun_altitude(self) -> float:
        """Return Sun Altitude."""

        return round(self.sun_data.altitude, 3)

    @property
    def sun_azimuth(self) -> float:
        """Return sun Azimuth."""

        return round(self.sun_data.azimuth, 3)

    @property
    def sun_next_rising_astro(self) -> datetime:
        """Return Sun Next Rising Astronomical."""

        return self.sun_data.next_rising_astro

    @property
    def sun_next_rising(self) -> datetime:
        """Return Sun Next Rising Civil."""

        return self.sun_data.next_rising_civil

    @property
    def sun_next_rising_nautical(self) -> datetime:
        """Return Sun Next Rising Nautical."""

        return self.sun_data.next_rising_nautical

    @property
    def sun_next_setting_astro(self) -> datetime:
        """Return Sun Next Setting Astronomical."""

        return self.sun_data.next_setting_astro

    @property
    def sun_next_setting(self) -> datetime:
        """Return Next Setting Civil."""

        return self.sun_data.next_setting_civil

    @property
    def sun_next_setting_nautical(self) -> datetime:
        """Return Sun Next Setting Nautical."""

        return self.sun_data.next_setting_nautical

    # #########################################################################
    # Moon
    # #########################################################################
    @property
    def moon_altitude(self) -> float:
        """Return Moon Altitude."""

        return round(self.moon_data.altitude, 3)

    @property
    def moon_angular_size(self) -> float:
        """Return Moon Angular Size in Minutes."""

        return round(self.moon_data.angular_size, 3)

    @property
    def moon_azimuth(self) -> float:
        """Return Moon Azimuth."""

        return round(self.moon_data.azimuth, 3)

    @property
    def moon_distance_km(self) -> float:
        """Return Moon Distance in km."""

        return round(self.moon_data.distance_km, 0)

    @property
    def moon_next_full_moon(self) -> datetime:
        """Return Moon Next Full Moon."""

        return self.moon_data.next_full_moon

    @property
    def moon_next_new_moon(self) -> datetime:
        """Return Moon Next New Moon."""

        return self.moon_data.next_new_moon

    @property
    def moon_next_rising(self) -> datetime:
        """Return Moon Next Rising."""

        return self.moon_data.next_rising

    @property
    def moon_next_setting(self) -> datetime:
        """Return Moon Next Setting."""

        return self.moon_data.next_setting

    @property
    def moon_phase(self) -> float:
        """Return Moon Phase."""

        return round(self.moon_data.phase, 1)

    @property
    def moon_relative_size(self) -> float:
        """Return Moon Relative Size in %."""

        return round(self.moon_data.relative_size * 100 - 100, 3)

    # #########################################################################
    # Darkness
    # #########################################################################
    @property
    def deep_sky_darkness_moon_rises(self) -> bool:
        """Returns true if moon rises during astronomical night."""

        return self.darkness_data.deep_sky_darkness_moon_rises

    @property
    def deep_sky_darkness_moon_sets(self) -> bool:
        """Returns true if moon sets during astronomical night."""

        return self.darkness_data.deep_sky_darkness_moon_sets

    @property
    def deep_sky_darkness_moon_always_up(self) -> bool:
        """Returns true if moon is up during astronomical night."""

        return self.darkness_data.deep_sky_darkness_moon_always_up

    @property
    def deep_sky_darkness_moon_always_down(self) -> bool:
        """Returns true if moon is down during astronomical night."""

        return self.darkness_data.deep_sky_darkness_moon_always_down

    @property
    def deep_sky_darkness(self) -> float:
        """Returns the remaining timespan of deep sky darkness."""

        return self.darkness_data.deep_sky_darkness

    # #########################################################################
    # Deep Sky Forecast
    # #########################################################################
    @property
    def deepsky_forecast_today(self) -> int:
        """Return Forecas Today in Percent."""

        nightly_condition_sum = 0
        if len(self.deepsky_forecast) > 0:
            for nightly_condition in self.deepsky_forecast[0].nightly_conditions:
                nightly_condition_sum += nightly_condition
            return int(round(nightly_condition_sum / len(self.deepsky_forecast[0].nightly_conditions)))

    @property
    def deepsky_forecast_today_dayname(self):
        """Return Forecast Todays Dayname."""

        if len(self.deepsky_forecast) > 0:
            nightly_conditions = self.deepsky_forecast[0]
            return nightly_conditions.dayname

    @property
    def deepsky_forecast_today_plain(self):
        """Return Forecast Today."""

        out = ""
        if len(self.deepsky_forecast) > 0:
            for nightly_condition in self.deepsky_forecast[0].nightly_conditions:
                out += CONDITION[4 - math.floor(nightly_condition / 20)].capitalize()
        return out

    @property
    def deepsky_forecast_today_desc(self):
        """Return Forecast Today Description."""

        if len(self.deepsky_forecast) > 0:
            nightly_conditions = self.deepsky_forecast[0]
            return nightly_conditions.weather.replace("_", " ").capitalize()

    @property
    def deepsky_forecast_today_precipitation_amount6(self) -> float:
        """Return Forecast Today Precipitation Amount6."""

        if len(self.deepsky_forecast) > 0:
            nightly_conditions = self.deepsky_forecast[0]
            return nightly_conditions.precipitation_amount6

    @property
    def deepsky_forecast_tomorrow(self) -> int:
        """Return Forecas Tomorrow in Percentt."""

        nightly_condition_sum = 0
        if len(self.deepsky_forecast) > 1:
            for nightly_condition in self.deepsky_forecast[1].nightly_conditions:
                nightly_condition_sum += nightly_condition
            return int(round(nightly_condition_sum / len(self.deepsky_forecast[1].nightly_conditions)))

    @property
    def deepsky_forecast_tomorrow_dayname(self):
        """Return Forecast Todays Dayname."""

        if len(self.deepsky_forecast) > 1:
            nightly_conditions = self.deepsky_forecast[1]
            return nightly_conditions.dayname

    @property
    def deepsky_forecast_tomorrow_plain(self):
        """Return Forecast Tomorrow."""

        out = ""
        if len(self.deepsky_forecast) > 1:
            for nightly_condition in self.deepsky_forecast[1].nightly_conditions:
                out += CONDITION[4 - math.floor(nightly_condition / 20)].capitalize()
        return out

    @property
    def deepsky_forecast_tomorrow_desc(self):
        """Return Forecast Tomorrow Description."""

        if len(self.deepsky_forecast) > 1:
            nightly_conditions = self.deepsky_forecast[1]
            return nightly_conditions.weather.replace("_", " ").capitalize()

    @property
    def deepsky_forecast_tomorrow_precipitation_amount6(self) -> float:
        """Return Forecast Today Precipitation Amount6."""

        if len(self.deepsky_forecast) > 0:
            nightly_conditions = self.deepsky_forecast[1]
            return nightly_conditions.precipitation_amount6

    # #########################################################################
    # UpTonight
    # #########################################################################
    # @property
    # def uptonight(self) -> int:
    #     """Return the number of best DSOs for tonight."""

    #     if self.uptonight is not None:
    #         return len(self.uptonight)
    #     return None

    @property
    def uptonight_list(self) -> list[UpTonightDSOData]:
        """Return the list of UpTonight targets."""

        return self.uptonight

    # #########################################################################
    # UpTonight Bodies
    # #########################################################################
    # @property
    # def uptonight_bodies(self) -> int:
    #     """Return the number of best BODIEs for tonight."""

    #     if self.uptonight_bodies is not None:
    #         return len(self.uptonight_bodies)
    #     return None

    @property
    def uptonight_bodies_list(self) -> list[dict]:
        """Return the list of UpTonight bodies."""

        return self.uptonight_bodies

    # #########################################################################
    # UpTonight Comets
    # #########################################################################
    # @property
    # def uptonight_comets(self) -> int:
    #     """Return the number of best comets for tonight."""

    #     if self.uptonight_comets is not None:
    #         return len(self.uptonight_comets)
    #     return None

    @property
    def uptonight_comets_list(self) -> list[dict]:
        """Return the list of UpTonight comets."""

        return self.uptonight_comets


class ForecastData:
    """A representation of 3-Hour Based Forecast AstroWeather Data."""

    def __init__(self, *, data: dict):
        self.time_data = data["time_data"]
        self.hour = data["hour"]
        self.condition_data = data["condition_data"]

    # #########################################################################
    # Time data
    # #########################################################################
    @property
    def seventimer_init(self) -> datetime:
        return self.time_data.seventimer_init

    @property
    def seventimer_timepoint(self) -> int:
        return self.time_data.seventimer_timepoint

    @property
    def forecast_time(self) -> datetime:
        return self.time_data.forecast_time

    # #########################################################################
    # Forecast data
    # #########################################################################
    @property
    def deep_sky_view(self) -> bool:
        """Return True if Deep Sky should be possible."""

        if self.condition_percentage <= DEEP_SKY_THRESHOLD:
            return True
        return False

    @property
    def condition_percentage(self) -> int:
        return self.condition_data.condition_percentage

    @property
    def cloudcover_percentage(self) -> int:
        return self.condition_data.cloudcover_percentage

    @property
    def cloudless_percentage(self) -> int:
        return self.condition_data.cloudless_percentage

    @property
    def cloud_area_fraction_percentage(self) -> int:
        return self.condition_data.cloud_area_fraction_percentage

    @property
    def cloud_area_fraction_high_percentage(self) -> str:
        return self.condition_data.cloud_area_fraction_high_percentage

    @property
    def cloud_area_fraction_medium_percentage(self) -> str:
        return self.condition_data.cloud_area_fraction_medium_percentage

    @property
    def cloud_area_fraction_low_percentage(self) -> str:
        return self.condition_data.cloud_area_fraction_low_percentage

    @property
    def seeing(self) -> float:
        return self.condition_data.seeing

    @property
    def seeing_percentage(self) -> int:
        return self.condition_data.seeing_percentage

    @property
    def transparency(self) -> float:
        return self.condition_data.transparency

    @property
    def transparency_percentage(self) -> int:
        return self.condition_data.transparency_percentage

    @property
    def lifted_index(self) -> float:
        return self.condition_data.lifted_index

    @property
    def calm_percentage(self) -> int:
        return self.condition_data.calm_percentage

    @property
    def wind10m_direction(self) -> float:
        return self.condition_data.wind10m_direction

    @property
    def wind10m_speed(self) -> float:
        return self.condition_data.wind10m_speed

    @property
    def temp2m(self) -> float:
        return self.condition_data.temp2m

    @property
    def rh2m(self) -> float:
        return self.condition_data.rh2m

    @property
    def dewpoint2m(self) -> float:
        return self.condition_data.dewpoint2m

    @property
    def weather(self) -> str:
        return self.condition_data.weather

    @property
    def weather6(self) -> str:
        return self.condition_data.weather6

    @property
    def precipitation_amount(self) -> float:
        return self.condition_data.precipitation_amount

    @property
    def precipitation_amount6(self) -> float:
        return self.condition_data.precipitation_amount6


class NightlyConditionsData:
    """A representation of nights Sky Quality Data."""

    def __init__(self, *, data: dict):
        self.seventimer_init = data["seventimer_init"]
        self.dayname = data["dayname"]
        self.hour = data["hour"]
        self.nightly_conditions = data["nightly_conditions"]
        self._weather = data["weather"]
        self.precipitation_amount6 = data["precipitation_amount6"]

    @property
    def weather(self) -> str:
        """Return Current Weather."""

        return self._weather.replace("_", " ").capitalize()

    @weather.setter
    def weather(self, new_value: str):
        self._weather = new_value
