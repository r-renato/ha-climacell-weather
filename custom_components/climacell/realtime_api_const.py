"""Support for climacell"""
import voluptuous as vol
from homeassistant.helpers import config_validation as cv

from homeassistant.components.weather import (
    ATTR_WEATHER_TEMPERATURE,
    ATTR_WEATHER_HUMIDITY,
    ATTR_WEATHER_VISIBILITY,
    ATTR_WEATHER_PRESSURE,
    ATTR_WEATHER_WIND_SPEED,
)

from homeassistant.const import CONF_SCAN_INTERVAL, SUN_EVENT_SUNSET, SUN_EVENT_SUNRISE

from custom_components.climacell_custom.global_const import (
    ATTR_WEATHER_FEELS_LIKE,
    ATTR_WEATHER_DEWPOINT,
    ATTR_WEATHER_WIND_GUST,
    ATTR_WEATHER_WIND_DIRECTION,
    ATTR_FORECAST_PRECIPITATION,
    ATTR_FORECAST_PRECIPITATION_TYPE,
    ATTR_WEATHER_CLOUD_COVER,
    ATTR_WEATHER_CLOUD_BASE,
    ATTR_WEATHER_CLOUD_CEILING,
    ATTR_WEATHER_SURFACE_SHORTWAVE_RADIATION,
    ATTR_MOON_PHASE,
    ATTR_WEATHER_CONDITION,
    ATTR_AIR_QUALITY_PM25,
    ATTR_AIR_QUALITY_PM10,
    ATTR_AIR_QUALITY_O3,
    ATTR_AIR_QUALITY_NO2,
    ATTR_AIR_QUALITY_CO,
    ATTR_AIR_QUALITY_SO2,
    ATTR_AIR_QUALITY_EPA_AQI,
    ATTR_AIR_QUALITY_EPA_PRIM,
    ATTR_AIR_QUALITY_EPA_HEALTH,
    ATTR_AIR_QUALITY_CHINA_AQI,
    ATTR_AIR_QUALITY_CHINA_PRIMARY_POLLUTANT,
    ATTR_AIR_QUALITY_CHINA_HEALTH_CONCERN,
    ATTR_POLLEN_TREE,
    ATTR_POLLEN_WEED,
    ATTR_POLLEN_GRASS,
    ATTR_ROAD_RISK_SCORE,
    ATTR_ROAD_RISK,
    ATTR_ROAD_RISK_CONFIDENCE,
    ATTR_ROAD_RISK_CONDITIONS,
    ATTR_FIRE_INDEX,
    CONF_EXCLUDE_INTERVAL,
    SCHEMA_EXCLUDE_INTERVAL,
    UPDATE_MODES,
    CONF_UPDATE,
    CONF_CONDITIONS,
)

CONF_REALTIME = "realtime"

REALTIME_CONDITIONS = {
    ATTR_WEATHER_TEMPERATURE,
    ATTR_WEATHER_FEELS_LIKE,
    ATTR_WEATHER_DEWPOINT,
    ATTR_WEATHER_HUMIDITY,
    ATTR_WEATHER_WIND_SPEED,
    ATTR_WEATHER_WIND_DIRECTION,
    ATTR_WEATHER_WIND_GUST,
    ATTR_WEATHER_PRESSURE,
    ATTR_FORECAST_PRECIPITATION,
    ATTR_FORECAST_PRECIPITATION_TYPE,
    # ATTR_FORECAST_PRECIPITATION_PROBABILITY,
    # ATTR_FORECAST_PRECIPITATION_ACCUMULATION,
    SUN_EVENT_SUNSET,
    SUN_EVENT_SUNRISE,
    ATTR_WEATHER_VISIBILITY,
    ATTR_WEATHER_CLOUD_COVER,
    ATTR_WEATHER_CLOUD_BASE,
    ATTR_WEATHER_CLOUD_CEILING,
    # ATTR_WEATHER_SATELLITE_CLOUD,
    ATTR_WEATHER_SURFACE_SHORTWAVE_RADIATION,
    ATTR_MOON_PHASE,
    ATTR_WEATHER_CONDITION,
    # ATTR_WEATHER_GROUP,
    ATTR_AIR_QUALITY_PM25,
    ATTR_AIR_QUALITY_PM10,
    ATTR_AIR_QUALITY_O3,
    ATTR_AIR_QUALITY_NO2,
    ATTR_AIR_QUALITY_CO,
    ATTR_AIR_QUALITY_SO2,
    ATTR_AIR_QUALITY_EPA_AQI,
    ATTR_AIR_QUALITY_EPA_PRIM,
    ATTR_AIR_QUALITY_EPA_HEALTH,
    ATTR_AIR_QUALITY_CHINA_AQI,
    ATTR_AIR_QUALITY_CHINA_PRIMARY_POLLUTANT,
    ATTR_AIR_QUALITY_CHINA_HEALTH_CONCERN,
    ATTR_POLLEN_TREE,
    ATTR_POLLEN_WEED,
    ATTR_POLLEN_GRASS,
    ATTR_ROAD_RISK_SCORE,
    ATTR_ROAD_RISK,
    ATTR_ROAD_RISK_CONFIDENCE,
    ATTR_ROAD_RISK_CONDITIONS,
    ATTR_FIRE_INDEX,
}

SCHEMA_REALTIME_CONDITIONS = vol.Schema(
    {
        vol.Optional(CONF_CONDITIONS): vol.All(
            cv.ensure_list, [vol.In(REALTIME_CONDITIONS)]
        ),
        vol.Optional(CONF_UPDATE): vol.All(cv.ensure_list, [vol.In(UPDATE_MODES)]),
        vol.Optional(CONF_SCAN_INTERVAL): cv.time_period,
        vol.Optional(CONF_EXCLUDE_INTERVAL): vol.All(
            cv.ensure_list, [vol.Schema(SCHEMA_EXCLUDE_INTERVAL)]
        ),
    }
)
