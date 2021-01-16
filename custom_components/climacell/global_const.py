import voluptuous as vol
from homeassistant.helpers import config_validation as cv

from homeassistant.components.weather import (
    ATTR_WEATHER_TEMPERATURE,
    ATTR_WEATHER_VISIBILITY,
    ATTR_WEATHER_HUMIDITY,
    ATTR_WEATHER_PRESSURE,
    ATTR_WEATHER_WIND_SPEED,
    ATTR_FORECAST_PRECIPITATION,
    ATTR_FORECAST_PRECIPITATION_PROBABILITY,
)

from homeassistant.const import (
    ATTR_NAME,
    ATTR_ICON,
    SUN_EVENT_SUNSET,
    SUN_EVENT_SUNRISE,
    ATTR_UNIT_OF_MEASUREMENT,
)

ATTRIBUTION = "Powered by Climacell"
ATTR_OBSERVATION_TIME = "observation_time"

CONF_UNITS = "units"
CONF_ALLOWED_UNITS = ["metric", "imperial"]
CONF_LEGACY_UNITS = ["si", "us"]

PERCENTAGE = "%"
DEGREES = "degrees"
SECONDS = "s"

CONF_CONDITIONS = "conditions"
CONF_SOURCES = "sources"
CONF_FORECAST_OBSERVATIONS = "forecast_observations"
CONF_TIMESTEP = "timestep"
CONF_EXCLUDE_INTERVAL = "exclude_interval"
CONF_TIMELINES = "timelines"
CONF_FIELDS = "fields"
CONF_START_TIME = "start_time"

TIMESTEP_VALUES = ["1m", "5m", "15m", "30m", "1h", "1d"]

CONF_UPDATE = "update"
ATTR_AUTO = "auto"
ATTR_MANUAL = "manual"

ATTR_FIELD = "field"

ATTR_WEATHER_FEELS_LIKE = "feels_like"
ATTR_WEATHER_DEWPOINT = "dewpoint"

ATTR_WEATHER_WIND_DIRECTION = "wind_direction"
ATTR_WEATHER_WIND_GUST = "wind_gust"
ATTR_FORECAST_PRECIPITATION_TYPE = "precipitation_type"
ATTR_FORECAST_PRECIPITATION_ACCUMULATION = "precipitation_accumulation"
ATTR_WEATHER_CLOUD_COVER = "cloud_cover"
ATTR_WEATHER_CLOUD_BASE = "cloud_base"
ATTR_WEATHER_CLOUD_CEILING = "cloud_ceiling"
ATTR_WEATHER_CONDITION = "weather_condition"
ATTR_WEATHER_SURFACE_SHORTWAVE_RADIATION = "surface_shortwave_radiation"
ATTR_MOON_PHASE = "moon_phase"
ATTR_WEATHER_GROUP = "weather_groups"
ATTR_WEATHER_PRESSURE_SEALEVEL = "sealevel_pressure"
ATTR_WEATHER_SOLAR_GHI = "solar_ghi"

ATTR_POLLEN_TREE = "pollen_tree"
ATTR_POLLEN_WEED = "pollen_weed"
ATTR_POLLEN_GRASS = "pollen_grass"

ATTR_AIR_QUALITY_PM25 = "pm25"
ATTR_AIR_QUALITY_PM10 = "pm10"
ATTR_AIR_QUALITY_O3 = "o3"
ATTR_AIR_QUALITY_NO2 = "no2"
ATTR_AIR_QUALITY_CO = "co"
ATTR_AIR_QUALITY_SO2 = "so2"
ATTR_AIR_QUALITY_EPA_AQI = "epa_aqi"
ATTR_AIR_QUALITY_EPA_PRIM = "epa_primary_pollutant"
ATTR_AIR_QUALITY_EPA_HEALTH = "epa_health_concern"
ATTR_AIR_QUALITY_CHINA_AQI = "china_aqi"
ATTR_AIR_QUALITY_CHINA_PRIMARY_POLLUTANT = "china_primary_pollutant"
ATTR_AIR_QUALITY_CHINA_HEALTH_CONCERN = "china_health_concern"

ATTR_ROAD_RISK_SCORE = "road_risk_score"
ATTR_ROAD_RISK = "road_risk"
ATTR_ROAD_RISK_CONFIDENCE = "road_risk_confidence"
ATTR_ROAD_RISK_CONDITIONS = "road_risk_conditions"

ATTR_FIRE_INDEX = "fire_index"

UPDATE_MODES = {
    ATTR_AUTO,
    ATTR_MANUAL,
}

ATTR_API_SUFFIX = "api_suffix"
ATTR_SUFFIX_NAME = "suffix_name"
ATTR_CONDITION = "condition"

SUFFIXES = {
    "min": {ATTR_API_SUFFIX: "Min", ATTR_SUFFIX_NAME: "Minimum"},
    "max": {ATTR_API_SUFFIX: "Max", ATTR_SUFFIX_NAME: "Maximum"},
    "avg": {ATTR_API_SUFFIX: "Avg", ATTR_SUFFIX_NAME: "Average"},
    "mintime": {ATTR_API_SUFFIX: "MinTime", ATTR_SUFFIX_NAME: "Time of minium"},
    "maxtime": {
        ATTR_API_SUFFIX: "MaxTime",
        ATTR_SUFFIX_NAME: "Time of maximum",
    },
}

CLIMACELL_DATA_CONDITIONS = {
    ATTR_WEATHER_TEMPERATURE: {
        ATTR_FIELD: "temperature",
        ATTR_NAME: "Temperature",
        ATTR_ICON: "mdi:thermometer",
    },
    ATTR_WEATHER_FEELS_LIKE: {
        ATTR_FIELD: "temperatureApparent",
        ATTR_NAME: "Feels Like",
        ATTR_ICON: "mdi:thermometer",
    },
    ATTR_WEATHER_DEWPOINT: {
        ATTR_FIELD: "dewPoint",
        ATTR_NAME: "Dewpoint",
        ATTR_ICON: "mdi:thermometer",
    },
    ATTR_WEATHER_HUMIDITY: {
        ATTR_FIELD: "humidity",
        ATTR_NAME: "Humidity Percentage",
        ATTR_ICON: "mdi:water-percent",
    },
    ATTR_WEATHER_WIND_SPEED: {
        ATTR_FIELD: "windSpeed",
        ATTR_NAME: "Wind speed",
        ATTR_ICON: "mdi:weather-windy",
    },
    ATTR_WEATHER_WIND_DIRECTION: {
        ATTR_FIELD: "windDirection",
        ATTR_NAME: "Wind Direction",
        ATTR_ICON: "mdi:compass",
    },
    ATTR_WEATHER_WIND_GUST: {
        ATTR_FIELD: "windGust",
        ATTR_NAME: "Wind Gust",
        ATTR_ICON: "mdi:weather-windy-variant",
    },
    ATTR_WEATHER_PRESSURE: {
        ATTR_FIELD: "pressureSurfaceLevel",
        ATTR_NAME: "Barometric pressure",
        ATTR_ICON: "mdi:gauge",
    },
    ATTR_WEATHER_PRESSURE_SEALEVEL: {
        ATTR_FIELD: "pressureSeaLevel",
        ATTR_NAME: "Barometric pressure at sea level",
        ATTR_ICON: "mdi:gauge",
    },
    ATTR_FORECAST_PRECIPITATION_TYPE: {
        ATTR_FIELD: "precipitationType",
        ATTR_NAME: "Precipitation Type",
        ATTR_ICON: "mdi:weather-pouring",
    },
    ATTR_FORECAST_PRECIPITATION: {
        ATTR_FIELD: "precipitationIntensity",
        ATTR_NAME: "Precipitation",
        ATTR_ICON: "mdi:weather-rainy",
    },
    ATTR_FORECAST_PRECIPITATION_PROBABILITY: {
        ATTR_FIELD: "precipitationProbability",
        ATTR_NAME: "precipitation Probability",
        ATTR_ICON: "mdi:weather-rainy",
    },
    SUN_EVENT_SUNRISE: {
        ATTR_FIELD: "sunriseTime",
        ATTR_NAME: "Sunrise",
        ATTR_ICON: "mdi:white-balance-sunny",
    },
    SUN_EVENT_SUNSET: {
        ATTR_FIELD: "sunsetTime",
        ATTR_NAME: "Sunset",
        ATTR_ICON: "mdi:weather-night",
    },
    ATTR_WEATHER_SOLAR_GHI: {
        ATTR_FIELD: "solarGHI",
        ATTR_NAME: "Solar GHI",
        ATTR_ICON: "mdi:white-balance-sunny",
    },
    ATTR_WEATHER_VISIBILITY: {
        ATTR_FIELD: "visibility",
        ATTR_NAME: "Visibility",
        ATTR_ICON: "mdi:eye",
    },
    ATTR_WEATHER_CLOUD_COVER: {
        ATTR_FIELD: "cloudCover",
        ATTR_NAME: "Cloud Cover",
        ATTR_ICON: "mdi:weather-partly-cloudy",
    },
    ATTR_WEATHER_CLOUD_BASE: {
        ATTR_FIELD: "cloudBase",
        ATTR_NAME: "Cloud Base",
        ATTR_ICON: "mdi:weather-partly-cloudy",
    },
    ATTR_WEATHER_CLOUD_CEILING: {
        ATTR_FIELD: "cloudCeiling",
        ATTR_NAME: "Cloud Ceiling",
        ATTR_ICON: "mdi:weather-partly-cloudy",
    },
    ATTR_MOON_PHASE: {
        ATTR_FIELD: "moonPhase",
        ATTR_NAME: "Moon Phase",
        ATTR_ICON: "mdi:weather-night",
    },
    ATTR_WEATHER_CONDITION: {
        ATTR_FIELD: "weatherCode",
        ATTR_NAME: "Weather Condition",
        ATTR_ICON: "mdi:thermometer",
    },
    #
    # Air Quality
    #
    ATTR_AIR_QUALITY_PM25: {
        ATTR_FIELD: "particulateMatter25",
        ATTR_NAME: "pm25",
        ATTR_ICON: "mdi:eye",
    },
    ATTR_AIR_QUALITY_PM10: {
        ATTR_FIELD: "particulateMatter10",
        ATTR_NAME: "pm10",
        ATTR_ICON: "mdi:eye",
    },
    ATTR_AIR_QUALITY_O3: {
        ATTR_FIELD: "pollutantO3",
        ATTR_NAME: "o3",
        ATTR_ICON: "mdi:eye",
    },
    ATTR_AIR_QUALITY_NO2: {
        ATTR_FIELD: "pollutantNO2",
        ATTR_NAME: "no2",
        ATTR_ICON: "mdi:eye",
    },
    ATTR_AIR_QUALITY_CO: {
        ATTR_FIELD: "pollutantCO",
        ATTR_NAME: "co",
        ATTR_ICON: "mdi:eye",
    },
    ATTR_AIR_QUALITY_SO2: {
        ATTR_FIELD: "pollutantSO2",
        ATTR_NAME: "so2",
        ATTR_ICON: "mdi:eye",
    },
    ATTR_AIR_QUALITY_EPA_AQI: {
        ATTR_FIELD: "epaIndex",
        ATTR_NAME: "EPA AQI",
        ATTR_ICON: "mdi:eye",
    },
    ATTR_AIR_QUALITY_EPA_PRIM: {
        ATTR_FIELD: "epaPrimaryPollutant",
        ATTR_NAME: "EPA Primary Pollutant",
        ATTR_ICON: "mdi:eye",
    },
    ATTR_AIR_QUALITY_EPA_HEALTH: {
        ATTR_FIELD: "epaHealthConcern",
        ATTR_NAME: "EPA Health Concern",
        ATTR_ICON: "mdi:eye",
    },
    ATTR_AIR_QUALITY_CHINA_AQI: {
        ATTR_FIELD: "mepIndex",
        ATTR_NAME: "China AQI",
        ATTR_ICON: "mdi:eye",
    },
    ATTR_AIR_QUALITY_CHINA_PRIMARY_POLLUTANT: {
        ATTR_FIELD: "mepPrimaryPollutant",
        ATTR_NAME: "China Primary Pollutant",
        ATTR_ICON: "mdi:eye",
    },
    ATTR_AIR_QUALITY_CHINA_HEALTH_CONCERN: {
        ATTR_FIELD: "mepHealthConcern",
        ATTR_NAME: "China Health Concern",
        ATTR_ICON: "mdi:eye",
    },
    #
    # Pollen
    #
    ATTR_POLLEN_TREE: {
        ATTR_FIELD: "treeIndex",
        ATTR_NAME: "Pollen Tree",
        ATTR_ICON: "mdi:tree",
    },
    ATTR_POLLEN_WEED: {
        ATTR_FIELD: "grassIndex",
        ATTR_NAME: "Pollen Weed",
        ATTR_ICON: "mdi:sprout",
    },
    ATTR_POLLEN_GRASS: {
        ATTR_FIELD: "weedIndex",
        ATTR_NAME: "Pollen Grass",
        ATTR_ICON: "mdi:flower",
    },
    #
    # Road Risk
    #
    ATTR_ROAD_RISK_SCORE: {
        ATTR_FIELD: "roadRiskScore",
        ATTR_NAME: "Road Risk Score",
        ATTR_ICON: "",
    },
    ATTR_ROAD_RISK: {
        ATTR_FIELD: "roadRisk",
        ATTR_NAME: "Road Risk",
        ATTR_ICON: "",
    },
    ATTR_ROAD_RISK_CONFIDENCE: {
        ATTR_FIELD: "roadRiskConfidence",
        ATTR_NAME: "Road Risk Confidence",
        ATTR_ICON: "",
    },
    ATTR_ROAD_RISK_CONDITIONS: {
        ATTR_FIELD: "roadRiskConditions",
        ATTR_NAME: "Road Risk Conditions",
        ATTR_ICON: "",
    },
    #
    # Fire Index
    #
    ATTR_FIRE_INDEX: {
        ATTR_FIELD: "fireIndex",
        ATTR_NAME: "Fire Index",
        ATTR_ICON: "mdi:pine-tree-fire",
    },
}

SCHEMA_EXCLUDE_INTERVAL = vol.Schema(
    {
        vol.All(vol.Coerce(int), vol.Range(min=1, max=20)): vol.All(
            cv.ensure_list, [cv.string]
        ),
    }
)

# From https://docs.climacell.co/reference/data-layers-overview
METRIC_UNITS = {
    "cloudBase": "km",
    "cloudCeiling": "km",
    "cloudCover": "%",
    "dewPoint": "Celcius",
    "epaHealthConcern": {
        "0": "Good",
        "1": "Moderate",
        "2": "Unhealthy for Sensitive Groups",
        "3": "Unhealthy",
        "4": "Very Unhealthy",
        "5": "Hazardous",
    },
    "epaIndex": "EPA AQI",
    "epaPrimaryPollutant": {
        "0": "PM2.5",
        "1": "PM10",
        "2": "O3",
        "3": "NO2",
        "4": "CO",
        "5": "SO2",
    },
    "fireIndex": "FWI",
    "grassGrassIndex": {
        "0": "None",
        "1": "Very Low",
        "2": "Low",
        "3": "Medium",
        "4": "High",
        "5": "Very High",
    },
    "grassIndex": {
        "0": "None",
        "1": "Very Low",
        "2": "Low",
        "3": "Medium",
        "4": "High",
        "5": "Very High",
    },
    "hailBinary": "Binary Prediction",
    "humidity": "%",
    "mepHealthConcern": {
        "0": "Good",
        "1": "Moderate",
        "2": "Unhealthy for Sensitive Groups",
        "3": "Unhealthy",
        "4": "Very Unhealthy",
        "5": "Hazardous",
    },
    "mepIndex": "MEP AQI",
    "mepPrimaryPollutant": {
        "0": "PM2.5",
        "1": "PM10",
        "2": "O3",
        "3": "NO2",
        "4": "CO",
        "5": "SO2",
    },
    "moonPhase": {
        "0": "New",
        "1": "Waxing Crescent",
        "2": "First Quarter",
        "3": "Waxing Gibbous",
        "4": "Full",
        "5": "Waning Gibbous",
        "6": "Third Quarter",
        "7": "Waning Crescen",
    },
    "particulateMatter10": "μg/m^3",
    "particulateMatter25": "μg/m^3",
    "pollutantCO": "ppb",
    "pollutantNO2": "ppb",
    "pollutantO3": "ppb",
    "pollutantSO2": "ppb",
    "precipitationIntensity": "mm/hr",
    "precipitationProbability": "%",
    "precipitationType": {
        "0": "N/A",
        "1": "Rain",
        "2": "Snow",
        "3": "Freezing Rain",
        "4": "Ice Pellets",
    },
    "pressureSeaLevel": "hPa",
    "pressureSurfaceLevel": "hPa",
    "solarDIF": "W/m^2",
    "solarDIR": "W/m^2",
    "solarGHI": "W/m^2",
    "temperature": "Celcius",
    "temperatureApparent": "Celcius",
    "treeAcacia": {
        "0": "None",
        "1": "Very Low",
        "2": "Low",
        "3": "Medium",
        "4": "High",
        "5": "Very High",
    },
    "treeAsh": {
        "0": "None",
        "1": "Very Low",
        "2": "Low",
        "3": "Medium",
        "4": "High",
        "5": "Very High",
    },
    "treeBeech": {
        "0": "None",
        "1": "Very Low",
        "2": "Low",
        "3": "Medium",
        "4": "High",
        "5": "Very High",
    },
    "treeBirch": {
        "0": "None",
        "1": "Very Low",
        "2": "Low",
        "3": "Medium",
        "4": "High",
        "5": "Very High",
    },
    "treeCedar": {
        "0": "None",
        "1": "Very Low",
        "2": "Low",
        "3": "Medium",
        "4": "High",
        "5": "Very High",
    },
    "treeCottonwood": {
        "0": "None",
        "1": "Very Low",
        "2": "Low",
        "3": "Medium",
        "4": "High",
        "5": "Very High",
    },
    "treeCypress": {
        "0": "None",
        "1": "Very Low",
        "2": "Low",
        "3": "Medium",
        "4": "High",
        "5": "Very High",
    },
    "treeElder": {
        "0": "None",
        "1": "Very Low",
        "2": "Low",
        "3": "Medium",
        "4": "High",
        "5": "Very High",
    },
    "treeElm": {
        "0": "None",
        "1": "Very Low",
        "2": "Low",
        "3": "Medium",
        "4": "High",
        "5": "Very High",
    },
    "treeHemlock": {
        "0": "None",
        "1": "Very Low",
        "2": "Low",
        "3": "Medium",
        "4": "High",
        "5": "Very High",
    },
    "treeHickory": {
        "0": "None",
        "1": "Very Low",
        "2": "Low",
        "3": "Medium",
        "4": "High",
        "5": "Very High",
    },
    "treeIndex": {
        "0": "None",
        "1": "Very Low",
        "2": "Low",
        "3": "Medium",
        "4": "High",
        "5": "Very High",
    },
    "treeJuniper": {
        "0": "None",
        "1": "Very Low",
        "2": "Low",
        "3": "Medium",
        "4": "High",
        "5": "Very High",
    },
    "treeMahagony": {
        "0": "None",
        "1": "Very Low",
        "2": "Low",
        "3": "Medium",
        "4": "High",
        "5": "Very High",
    },
    "treeMaple": {
        "0": "None",
        "1": "Very Low",
        "2": "Low",
        "3": "Medium",
        "4": "High",
        "5": "Very High",
    },
    "treeMulberry": {
        "0": "None",
        "1": "Very Low",
        "2": "Low",
        "3": "Medium",
        "4": "High",
        "5": "Very High",
    },
    "treeOak": {
        "0": "None",
        "1": "Very Low",
        "2": "Low",
        "3": "Medium",
        "4": "High",
        "5": "Very High",
    },
    "treePine": {
        "0": "None",
        "1": "Very Low",
        "2": "Low",
        "3": "Medium",
        "4": "High",
        "5": "Very High",
    },
    "treeSpruce": {
        "0": "None",
        "1": "Very Low",
        "2": "Low",
        "3": "Medium",
        "4": "High",
        "5": "Very High",
    },
    "treeSycamore": {
        "0": "None",
        "1": "Very Low",
        "2": "Low",
        "3": "Medium",
        "4": "High",
        "5": "Very High",
    },
    "treeWalnut": {
        "0": "None",
        "1": "Very Low",
        "2": "Low",
        "3": "Medium",
        "4": "High",
        "5": "Very High",
    },
    "treeWillow": {
        "0": "None",
        "1": "Very Low",
        "2": "Low",
        "3": "Medium",
        "4": "High",
        "5": "Very High",
    },
    "visibility": "km",
    "weatherCode": {
        "0": "Unknown",
        "1000": "Clear",
        "1001": "Cloudy",
        "1100": "Mostly Clear",
        "1101": "Partly Cloudy",
        "1102": "Mostly Cloudy",
        "2000": "Fog",
        "2100": "Light Fog",
        "3000": "Light Wind",
        "3001": "Wind",
        "3002": "Strong Wind",
        "4000": "Drizzle",
        "4001": "Rain",
        "4200": "Light Rain",
        "4201": "Heavy Rain",
        "5000": "Snow",
        "5001": "Flurries",
        "5100": "Light Snow",
        "5101": "Heavy Snow",
        "6000": "Freezing Drizzle",
        "6001": "Freezing Rain",
        "6200": "Light Freezing Rain",
        "6201": "Heavy Freezing Rain",
        "7000": "Ice Pellets",
        "7101": "Heavy Ice Pellets",
        "7102": "Light Ice Pellets",
        "8000": "Thunderstorm",
    },
    "weedGrassweedIndex": {
        "0": "None",
        "1": "Very Low",
        "2": "Low",
        "3": "Medium",
        "4": "High",
        "5": "Very High",
    },
    "weedIndex": {
        "0": "None",
        "1": "Very Low",
        "2": "Low",
        "3": "Medium",
        "4": "High",
        "5": "Very High",
    },
    "windDirection": "degrees",
    "windGust": "m/s",
    "windSpeed": "m/s",
}

IMPERIAL_UNITS = {
    "cloudBase": "mi",
    "cloudCeiling": "mi",
    "cloudCover": "%",
    "dewPoint": "Fahrenheit",
    "epaHealthConcern": {
        "0": "Good",
        "1": "Moderate",
        "2": "Unhealthy for Sensitive Groups",
        "3": "Unhealthy",
        "4": "Very Unhealthy",
        "5": "Hazardous",
    },
    "epaIndex": "EPA AQI",
    "epaPrimaryPollutant": {
        "0": "PM2.5",
        "1": "PM10",
        "2": "O3",
        "3": "NO2",
        "4": "CO",
        "5": "SO2",
    },
    "fireIndex": "FWI",
    "grassGrassIndex": {
        "0": "None",
        "1": "Very Low",
        "2": "Low",
        "3": "Medium",
        "4": "High",
        "5": "Very High",
    },
    "grassIndex": {
        "0": "None",
        "1": "Very Low",
        "2": "Low",
        "3": "Medium",
        "4": "High",
        "5": "Very High",
    },
    "hailBinary": "Binary Prediction",
    "humidity": "%",
    "mepHealthConcern": {
        "0": "Good",
        "1": "Moderate",
        "2": "Unhealthy for Sensitive Groups",
        "3": "Unhealthy",
        "4": "Very Unhealthy",
        "5": "Hazardous",
    },
    "mepIndex": "MEP AQI",
    "mepPrimaryPollutant": {
        "0": "PM2.5",
        "1": "PM10",
        "2": "O3",
        "3": "NO2",
        "4": "CO",
        "5": "SO2",
    },
    "moonPhase": {
        "0": "New",
        "1": "Waxing Crescent",
        "2": "First Quarter",
        "3": "Waxing Gibbous",
        "4": "Full",
        "5": "Waning Gibbous",
        "6": "Third Quarter",
        "7": "Waning Crescen",
    },
    "particulateMatter10": "μg/ft^3",
    "particulateMatter25": "μg/ft^3",
    "pollutantCO": "ppb",
    "pollutantNO2": "ppb",
    "pollutantO3": "ppb",
    "pollutantSO2": "ppb",
    "precipitationIntensity": "in/hr",
    "precipitationProbability": "%",
    "precipitationType": {
        "0": "N/A",
        "1": "Rain",
        "2": "Snow",
        "3": "Freezing Rain",
        "4": "Ice Pellets",
    },
    "pressureSeaLevel": "inHg",
    "pressureSurfaceLevel": "inHg",
    "solarDIF": "Btu/ft^2",
    "solarDIR": "Btu/ft^2",
    "solarGHI": "Btu/ft^2",
    "temperature": "Fahrenheit",
    "temperatureApparent": "Fahrenheit",
    "treeAcacia": {
        "0": "None",
        "1": "Very Low",
        "2": "Low",
        "3": "Medium",
        "4": "High",
        "5": "Very High",
    },
    "treeAsh": {
        "0": "None",
        "1": "Very Low",
        "2": "Low",
        "3": "Medium",
        "4": "High",
        "5": "Very High",
    },
    "treeBeech": {
        "0": "None",
        "1": "Very Low",
        "2": "Low",
        "3": "Medium",
        "4": "High",
        "5": "Very High",
    },
    "treeBirch": {
        "0": "None",
        "1": "Very Low",
        "2": "Low",
        "3": "Medium",
        "4": "High",
        "5": "Very High",
    },
    "treeCedar": {
        "0": "None",
        "1": "Very Low",
        "2": "Low",
        "3": "Medium",
        "4": "High",
        "5": "Very High",
    },
    "treeCottonwood": {
        "0": "None",
        "1": "Very Low",
        "2": "Low",
        "3": "Medium",
        "4": "High",
        "5": "Very High",
    },
    "treeCypress": {
        "0": "None",
        "1": "Very Low",
        "2": "Low",
        "3": "Medium",
        "4": "High",
        "5": "Very High",
    },
    "treeElder": {
        "0": "None",
        "1": "Very Low",
        "2": "Low",
        "3": "Medium",
        "4": "High",
        "5": "Very High",
    },
    "treeElm": {
        "0": "None",
        "1": "Very Low",
        "2": "Low",
        "3": "Medium",
        "4": "High",
        "5": "Very High",
    },
    "treeHemlock": {
        "0": "None",
        "1": "Very Low",
        "2": "Low",
        "3": "Medium",
        "4": "High",
        "5": "Very High",
    },
    "treeHickory": {
        "0": "None",
        "1": "Very Low",
        "2": "Low",
        "3": "Medium",
        "4": "High",
        "5": "Very High",
    },
    "treeIndex": {
        "0": "None",
        "1": "Very Low",
        "2": "Low",
        "3": "Medium",
        "4": "High",
        "5": "Very High",
    },
    "treeJuniper": {
        "0": "None",
        "1": "Very Low",
        "2": "Low",
        "3": "Medium",
        "4": "High",
        "5": "Very High",
    },
    "treeMahagony": {
        "0": "None",
        "1": "Very Low",
        "2": "Low",
        "3": "Medium",
        "4": "High",
        "5": "Very High",
    },
    "treeMaple": {
        "0": "None",
        "1": "Very Low",
        "2": "Low",
        "3": "Medium",
        "4": "High",
        "5": "Very High",
    },
    "treeMulberry": {
        "0": "None",
        "1": "Very Low",
        "2": "Low",
        "3": "Medium",
        "4": "High",
        "5": "Very High",
    },
    "treeOak": {
        "0": "None",
        "1": "Very Low",
        "2": "Low",
        "3": "Medium",
        "4": "High",
        "5": "Very High",
    },
    "treePine": {
        "0": "None",
        "1": "Very Low",
        "2": "Low",
        "3": "Medium",
        "4": "High",
        "5": "Very High",
    },
    "treeSpruce": {
        "0": "None",
        "1": "Very Low",
        "2": "Low",
        "3": "Medium",
        "4": "High",
        "5": "Very High",
    },
    "treeSycamore": {
        "0": "None",
        "1": "Very Low",
        "2": "Low",
        "3": "Medium",
        "4": "High",
        "5": "Very High",
    },
    "treeWalnut": {
        "0": "None",
        "1": "Very Low",
        "2": "Low",
        "3": "Medium",
        "4": "High",
        "5": "Very High",
    },
    "treeWillow": {
        "0": "None",
        "1": "Very Low",
        "2": "Low",
        "3": "Medium",
        "4": "High",
        "5": "Very High",
    },
    "visibility": "mi",
    "weatherCode": {
        "0": "Unknown",
        "1000": "Clear",
        "1001": "Cloudy",
        "1100": "Mostly Clear",
        "1101": "Partly Cloudy",
        "1102": "Mostly Cloudy",
        "2000": "Fog",
        "2100": "Light Fog",
        "3000": "Light Wind",
        "3001": "Wind",
        "3002": "Strong Wind",
        "4000": "Drizzle",
        "4001": "Rain",
        "4200": "Light Rain",
        "4201": "Heavy Rain",
        "5000": "Snow",
        "5001": "Flurries",
        "5100": "Light Snow",
        "5101": "Heavy Snow",
        "6000": "Freezing Drizzle",
        "6001": "Freezing Rain",
        "6200": "Light Freezing Rain",
        "6201": "Heavy Freezing Rain",
        "7000": "Ice Pellets",
        "7101": "Heavy Ice Pellets",
        "7102": "Light Ice Pellets",
        "8000": "Thunderstorm",
    },
    "weedGrassweedIndex": {
        "0": "None",
        "1": "Very Low",
        "2": "Low",
        "3": "Medium",
        "4": "High",
        "5": "Very High",
    },
    "weedIndex": {
        "0": "None",
        "1": "Very Low",
        "2": "Low",
        "3": "Medium",
        "4": "High",
        "5": "Very High",
    },
    "windDirection": "degrees",
    "windGust": "mph",
    "windSpeed": "mph",
}

UNITS = {
    CONF_ALLOWED_UNITS[0]: METRIC_UNITS,
    CONF_ALLOWED_UNITS[1]: IMPERIAL_UNITS,
}
