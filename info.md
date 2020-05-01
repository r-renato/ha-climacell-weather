# Climacell weather service provider integration
### ... is a custom component (sensor) for Home Assistant.<br>

The `climacell` platform uses the <a href="https://www.climacell.co/weather-api/docs/" target="_blank">Climacell API</a> as a source for meteorological data for your location.

[![hacs_badge](https://img.shields.io/badge/HACS-Default-orange.svg)](https://github.com/custom-components/hacs)

[![License][license-shield]](LICENSE.md)

[![BuyMeCoffee][buymecoffeebadge]][buymecoffee]

_To use this component you must obtain an API key. Visit the the <a href="https://www.climacell.co/weather-api" target="_blank">Climacell</a> site to known how to obtain one._

## Manual installation

1. Using the tool of choice, open the directory (folder) of your HA configuration (there you can find `configuration.yaml`).
2. If you do not have a `custom_components` directory (folder) there, you need to create one.
3. In the `custom_components` directory (folder) create a new folder called `climacell`.
4. Download _all_ the files from this repository.
5. Place the content of the `custom_components/climacell/` directory (folder) in the new directory (folder) you created.

## Configuration
To use the `climacell` custom component you must first obtain a <a href="https://www.climacell.co/weather-api/pricing/">API key</a>. 

### Sensor variables

**api_key**
>(string)(Required)<br>

**name**
>(string)(Optional)<br>

**latitude**
>*(float)(Optional)*<br>
>Latitude coordinate to monitor weather of (required if longitude is specified).
>                      
>Default value:<br>
>coordinates from the Home Assistant configuration

**longitude**
>*(float)(Optional)*<br>
>Longitude coordinate to monitor weather of (required if latitude is specified).
> 
>Default value:<br>
>coordinates from the Home Assistant configuration

**units**
>(string)(Optional)<br>
>Specify the unit system. Valid options are us, si.
>
>Default value:
>si or us, based on the temperature preference in Home Assistant.

**monitored_conditions**
>*(list)(Required)*<br>
>Conditions to display in the frontend.
>
>>**forecast_observations**<br>
>>*(integer)(Optional)*<br>
>>Number of days for which you would like to receive forecast. The valid values are numbers starting from 1 to 7.
>>Any condition from monitored_conditions (forecast) will generate a sensor with entity_id <condition>_<day>d. 
>>
>>Default value: 4
>> 
>>**realtime**<br>
>>*(list)(Required)*<br>
>>
>>- *weather_condition*<br>
A textual field that conveys the weather conditions. Possible values are freezing_rain_heavy, freezing_rain,
freezing_rain_light, freezing_drizzle, ice_pellets_heavy, ice_pellets, ice_pellets_light, snow_heavy, snow, 
snow_light, flurries, tstorm, rain_heavy, rain, rain_light, drizzle, fog_light, fog, cloudy, mostly_cloudy, 
partly_cloudy, mostly_clear, clear
>>- *temperature*<br>
Temperature
>>- *humidity*<br>
Percent relative humidity from 0 - 100 %
>>- *visibility*<br>
Visibility distance
>>- *cloud_cover*<br>
Fraction of the sky obscured by clouds
>>- *precipitation*<br>
Precipitation intensity
>>- *precipitation_type*<br>
Types are: none, rain, snow, ice pellets, and freezing rain
>>- *pressure*<br>
Barometric pressure (at surface)
>>- *wind_speed*<br>
Wind speed
>>- *wind_direction*<br>
Wind direction in polar degrees 0-360 where 0 = North
>>- *wind_gust*<br>
Wind gust speed
>>- *moon_phase*<br>
This field is available in hourly and daily endpoints. Available values include new_moon, waxing_crescent,
first_quarter, waxing_gibbous, full, waning_gibbous, third_quarter, waning_crescent
>>- *sunset*<br>
Provides the times of sunset based on location
>>- *sunrise*<br>
Provides the times of sunrise based on location
>>- *pm25*<br>
Particulate Matter < 2.5 μm
>>- *pm10*<br>
Particulate Matter < 10 μm
>>- *o3*<br>
Ozone
>>- *no2*<br>
Nitrogen Dioxide
>>- *co*<br>
Carbon Monoxide
>>- *so2*<br>
Sulfur Dioxide
>>- *epa_aqi*<br>
Air quality index per US EPA standard
>>- *epa_primary_pollutant*<br>
Air quality index of primary pollutant per US EPA standard
>>- *epa_health_concern*<br>
Health concern level based on EPA standard: Good, Moderate, Unhealthy for sensitive groups, Unhealthy, Very Unhealthy, Hazardous
>>- *pollen_tree*<br>
ClimaCell pollen index for trees (or null if not in season)
>>- *pollen_weed*<br>
ClimaCell pollen index for weeds (or null if not in season)
>>- *pollen_grass*<br>
ClimaCell pollen index for grass (or null if not in season)
>>- *fire_index*<br>
ClimaCell fire hazard index
>>
>>**forecast**<br>
>>*(list)(Optional)*<br>
>>
>>- *weather_condition*<br>
A textual field that conveys the weather conditions. Possible values are freezing_rain_heavy, freezing_rain,
freezing_rain_light, freezing_drizzle, ice_pellets_heavy, ice_pellets, ice_pellets_light, snow_heavy, snow, 
snow_light, flurries, tstorm, rain_heavy, rain, rain_light, drizzle, fog_light, fog, cloudy, mostly_cloudy, 
partly_cloudy, mostly_clear, clear
>>- *temperature*<br>
Temperature
>>- *precipitation*<br>
Precipitation intensity
>>- *precipitation_probability*<br>
The chance that precipitation will occur at the forecast time within the hour or day

**scan_interval**
>*(time)(Optional)*<br>
>Minimum time interval between updates.
>>
>>**days**
>>*(integer)(Optional)*
>>
>>**hours**
>>*(integer)(Optional)*
>>
>>**minutes**
>>*(integer)(Optional)*
>>
>>**seconds**
>>*(integer)(Optional)*
>>
>>**milliseconds**
>>*(integer)(Optional)*

## Integration Examples

```yaml
sensor:
## Weather climatecell.co
  - platform: climacell
    api_key: !secret climacell_api_key
    name: cc
    latitude: !secret gps_geo_home_lt
    longitude: !secret gps_geo_home_ln
    monitored_conditions:
      realtime:
        - weather_condition
        - temperature
        - humidity
        - visibility
        - cloud_cover
        - precipitation
        - precipitation_type
        - pressure
        - wind_speed
        - wind_direction
        - wind_gust
        - moon_phase
        - sunset
        - sunrise
      forecast:
        - weather_condition
        - temperature
        - precipitation
        - precipitation_probability
    scan_interval:
      # At least one of these must be specified:
      days: 0
      hours: 1
      minutes: 0
      seconds: 0
      milliseconds: 0
```

The `climacell` custom component exposes a sensor for each monitored condition.
An example of data provided by a `climacell` sensor is the following:

| **Sensor name** | **State** | **Sensor attributes** | **Value**                |
|-----------------|-----------|-----------------------|--------------------------|
| temperature     | 13        | attribution           | Powered by Climacell     |
|                 |           | unit_of_measurement   | C                        |
|                 |           | observation_time      | 2020-04-30T02:40:47.390Z |
|                 |           | friendly_name         | Temperature              |
|                 |           | icon                  | mdi:thermometer          |


[license-shield]:https://img.shields.io/github/license/r-renato/ha-climacell-weather
[buymecoffee]: https://www.buymeacoffee.com/0D3WbkKrn
[buymecoffeebadge]: https://img.shields.io/badge/buy%20me%20a%20coffee-donate-yellow?style=for-the-badge