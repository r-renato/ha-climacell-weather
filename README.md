# Climacell weather service provider integration
### ... is a custom component (sensor) for Home Assistant.<br>

The `climacell` platform uses the <a href="https://www.climacell.co/weather-api/docs/" target="_blank">Climacell API</a> as a source for meteorological data for your location.

[![hacs_badge](https://img.shields.io/badge/HACS-Default-orange.svg)](https://github.com/custom-components/hacs)

[![License][license-shield]](LICENSE.md)

[![BuyMeCoffee][buymecoffeebadge]][buymecoffee]

_To use this component you must obtain an API key. Visit the the <a href="https://www.climacell.co/weather-api" target="_blank">Climacell</a> site to known how to obtain one._

## **WARNING**
Realtime, nowcast, hourly and daily are different services, so they consume 1 API call each one.

## Manual installation

1. Using the tool of choice, open the directory (folder) of your HA configuration (there you can find `configuration.yaml`).
2. If you do not have a `custom_components` directory (folder) there, you need to create one.
3. In the `custom_components` directory (folder) create a new folder called `climacell`.
4. Download _all_ the files from this repository.
5. Place the content of the `custom_components/climacell/` directory (folder) in the new directory (folder) you created.

## Configuration
To use the `climacell` custom component you must first obtain a <a href="https://www.climacell.co/weather-api/pricing/">API key</a>. 

### Sensor variables

<dl>
  <dt>api_key</dt>
  <dd>(string)(Required)<br>Your API key.</dd>
  
  <dt>name</dt>
  <dd>(string)(Optional)</dd>
  <dd>Additional name for the sensors.</dd>
  <dd>_Default value:_</dd>
  <dd>Climacell</dd>
</dl>

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
>*(objects)(Required)*<br>
>Conditions to display in the frontend.
>
>>**realtime**<br>
>>*(objects)(Required)*<br>
>>
>>>**conditions**<br>
>>>*(list)(Required)*<br>
>>>>See the available conditions<br>
>>>>
>>>>**scan_interval**
>>>>*(time)(Optional)*<br>
>>>>Minimum time interval between updates.
>>>>
>>>>>**days**
>>>>>*(integer)(Optional)*
>>>>>
>>>>>**hours**
>>>>>*(integer)(Optional)*
>>>>>
>>>>>**minutes**
>>>>>*(integer)(Optional)*
>>>>>
>>>>>**seconds**
>>>>>*(integer)(Optional)*
>>>>>
>>>>>**milliseconds**
>>>>>*(integer)(Optional)*
>>>>
>>>>**exclude_interval**
>>>>*(object)(Optional)*<br>
>>>>Intervals without inquiry.
>>>>>**(object list)(Required)**
>>>>>>**Hour:Minute**
>>>>>>*(string)(Required)*
>
>>**daily**<br>
>>*(objects)(Required)*<br>
>>
>>**forecast_observations**<br>
>>*(integer)(Optional)*<br>
>>Number of days for which you would like to receive forecast. The valid values are numbers starting from 1 to 7.
>>Any condition from monitored_conditions (forecast) will generate a sensor with entity_id <condition>_<day>d. 
>>
>>Default value: 5
>> 
>>>**conditions**<br>
>>>*(list)(Required)*<br>
>>>>See the available conditions<br>
>>>>
>>>>**scan_interval**
>>>>*(time)(Optional)*<br>
>>>>Minimum time interval between updates.
>>>>
>>>>>**days**
>>>>>*(integer)(Optional)*
>>>>>
>>>>>**hours**
>>>>>*(integer)(Optional)*
>>>>>
>>>>>**minutes**
>>>>>*(integer)(Optional)*
>>>>>
>>>>>**seconds**
>>>>>*(integer)(Optional)*
>>>>>
>>>>>**milliseconds**
>>>>>*(integer)(Optional)*
>>>>
>>>>**exclude_interval**
>>>>*(object)(Optional)*<br>
>>>>Intervals without inquiry.
>>>>>**(object list)(Required)**
>>>>>>**Hour:Minute**
>>>>>>*(string)(Required)*
>
>>**hourly**<br>
>>*(objects)(Required)*<br>
>>
>>**forecast_observations**<br>
>>*(integer)(Optional)*<br>
>>Number of days for which you would like to receive forecast. The valid values are numbers starting from 1 to 7.
>>Any condition from monitored_conditions (forecast) will generate a sensor with entity_id <condition>_<day>d. 
>>
>>Default value: 5
>> 
>>>**conditions**<br>
>>>*(list)(Required)*<br>
>>>>See the available conditions<br>
>>>>
>>>>**scan_interval**
>>>>*(time)(Optional)*<br>
>>>>Minimum time interval between updates.
>>>>
>>>>>**days**
>>>>>*(integer)(Optional)*
>>>>>
>>>>>**hours**
>>>>>*(integer)(Optional)*
>>>>>
>>>>>**minutes**
>>>>>*(integer)(Optional)*
>>>>>
>>>>>**seconds**
>>>>>*(integer)(Optional)*
>>>>>
>>>>>**milliseconds**
>>>>>*(integer)(Optional)*
>>>>
>>>>**exclude_interval**
>>>>*(object)(Optional)*<br>
>>>>Intervals without inquiry.
>>>>>**(object list)(Required)**
>>>>>>**Hour:Minute**
>>>>>>*(string)(Required)*
>
>>**nowcast**<br>
>>*(objects)(Required)*<br>
>>
>>**timestep**<br>
>>*(integer)(Optional)*<br>
>>Number of minutes 1/60
>>
>>Default value: 5
>> 
>>**forecast_observations**<br>
>>*(integer)(Optional)*<br>
>>Number of days for which you would like to receive forecast. The valid values are numbers starting from 1 to 7.
>>Any condition from monitored_conditions (forecast) will generate a sensor with entity_id <condition>_<day>d. 
>>
>>Default value: 5
>> 
>>>**conditions**<br>
>>>*(list)(Required)*<br>
>>>>See the available conditions<br>
>>>>
>>>>**scan_interval**
>>>>*(time)(Optional)*<br>
>>>>Minimum time interval between updates.
>>>>
>>>>>**days**
>>>>>*(integer)(Optional)*
>>>>>
>>>>>**hours**
>>>>>*(integer)(Optional)*
>>>>>
>>>>>**minutes**
>>>>>*(integer)(Optional)*
>>>>>
>>>>>**seconds**
>>>>>*(integer)(Optional)*
>>>>>
>>>>>**milliseconds**
>>>>>*(integer)(Optional)*
>>>>
>>>>**exclude_interval**
>>>>*(object)(Optional)*<br>
>>>>Intervals without inquiry.
>>>>>**(object list)(Required)**
>>>>>>**Hour:Minute**
>>>>>>*(string)(Required)*


### Condition information

|        **Condition**        |           **Services**           |             **Description**         |
|-----------------------------|----------------------------------|-------------------------------------|
| temperature                 | realtime, nowcast, hourly, daily | Temperature             |
| feels_like                  | realtime, nowcast, hourly, daily | Wind chill and heat window based on season             |
| dewpoint                    | realtime, nowcast, hourly        | Temperature of the dew point             |
| humidity                    | realtime, nowcast, hourly, daily | Percent relative humidity from 0 - 100%             |
| wind_speed                  | realtime, nowcast, hourly, daily | Wind speed             |
| wind_direction              | realtime, nowcast, hourly, daily | Wind direction in polar degrees 0-360 where 0 is North             |
| wind_gust                   | realtime, nowcast, hourly        | Wind gust speed             |
| pressure                    | realtime, nowcast, hourly, daily | Barometric pressure (at surface)             |
| precipitation               | realtime, nowcast, hourly, daily | Precipitation intensity             |
| precipitation_type          | realtime, nowcast, hourly        | The type of precipitation: none, rain, snow, ice pellets, and freezing rain             |
| precipitation_probability   | hourly, daily                    | The chance that precipitation will occur at the forecast time within the hour or day             |
| precipitation_accumulation  | hourly, daily                    | The accumulated amount of precipitation in the selected timestep             |
| sunset                      | realtime, nowcast, hourly, daily | The times sunset based on location             |
| sunrise                     | realtime, nowcast, hourly, daily | The times sunrise based on location             |
| visibility                  | realtime, nowcast, hourly, daily | Visibility distance             |
| cloud_cover                 | realtime, nowcast, hourly        | Fraction of the sky obscured by clouds             |
| cloud_base                  | realtime, nowcast, hourly        | The lowest level at which the air contains a perceptible quantity of cloud particles: NULL (when there are no clouds)             |
| cloud_ceiling               | realtime, nowcast, hourly        | The height of the lowest layer of clouds which covers more than half of the sky: NULL (when there are no clouds)             |
| satellite_cloud             |                                  | Fraction of the sky obscured by clouds, as observed by satellites             |
| surface_shortwave_radiation | realtime, nowcast, hourly        | Solar radiation reaching the surface             |
| moon_phase                  | realtime, hourly                 | The shape of the directly sunlit portion of the Moon: new, waxing_crescent, first_quarter, waxing_gibbous, full, waning_gibbous, third_quarter, waning_crescent             |
| weather_condition           | realtime, nowcast, hourly, daily | A textual field that conveys the weather conditions: freezing_rain_heavy, freezing_rain, freezing_rain_light, freezing_drizzle, ice_pellets_heavy, ice_pellets, ice_pellets_light, snow_heavy, snow, snow_light, flurries, tstorm, rain_heavy, rain, rain_light, drizzle, fog_light, fog, cloudy, mostly_cloudy, partly_cloudy, mostly_clear, clear            |
| weather_groups              |                                  | All weather elements that convey the weather conditions             |
| pm25                        | realtime, nowcast, hourly        | Particulate Matter < 2.5 μm             |
| pm10                        | realtime, nowcast, hourly        | Particulate Matter < 10 μm             |
| o3                          | realtime, nowcast, hourly        | Ozone             |
| no2                         | realtime, nowcast, hourly        | Nitrogen Dioxide             |
| co                          | realtime, nowcast, hourly        | Carbon Monoxide             |
| so2                         | realtime, nowcast, hourly        | Sulfur Dioxide             |
| epa_aqi                     | realtime, nowcast, hourly        | Air quality index per US EPA standard             |
| epa_primary_pollutant       | realtime, nowcast, hourly        | Air quality index of primary pollutant per US EPA standard              |
| epa_health_concern          | realtime, nowcast, hourly        | Health concern level based on EPA standard: Good, Moderate, Unhealthy for sensitive groups, Unhealthy, Very Unhealthy, Hazardous             |
| china_aqi                   | realtime, nowcast, hourly        | Air quality index per China MEP standard             |
| china_primary_pollutant     | realtime, nowcast, hourly        | Air quality index of primary pollutant per China MEP standard             |
| china_health_concern        | realtime, nowcast, hourly        | Health concern level based on China MEP standard             |
| pollen_tree                 | realtime, nowcast, hourly        | ClimaCell pollen index for trees             |
| pollen_weed                 | realtime, nowcast, hourly        | ClimaCell pollen index for weeds             |
| pollen_grass                | realtime, nowcast, hourly        | ClimaCell pollen index for grass             |
| road_risk_score             | realtime, nowcast, hourly        | ClimaCell road risk (EU and US only): Low risk, Low-moderate risk, Moderate risk, High risk, Extreme risk             |
| road_risk                   | realtime, nowcast, hourly        | The deprecated version of the above-mentioned: low_risk, moderate_risk, mod_hi_risk, high_risk, extreme_risk             |
| road_risk_confidence        | realtime, nowcast, hourly        | An integer between 1 and 100 that is indicative of how confident we are in our road risk prediction (EU and US only)             |
| road_risk_conditions        | realtime, nowcast, hourly        | Main weather conditions that are impacting the road risk score (EU and US only)             |
| fire_index                  | realtime                         | ClimaCell fire hazard index             |

## Integration Examples

```yaml
sensor:
## Weather climatecell.co
  - platform: climacell
    api_key: !secret climacell_api_key
    name: example
    latitude: !secret gps_geo_home_lt
    longitude: !secret gps_geo_home_ln
    monitored_conditions:
      realtime:
        conditions:
          - temperature
          - feels_like
          - dewpoint
          - humidity
          - wind_speed
          - wind_direction
          - wind_gust
          - pressure
          - precipitation
          - precipitation_type
#          - precipitation_probability
#          - precipitation_accumulation
          - sunset
          - sunrise
          - visibility
          - cloud_cover
          - cloud_base
          - cloud_ceiling
#          - satellite_cloud
          - surface_shortwave_radiation
          - moon_phase
          - weather_condition
#          - weather_groups
          - pm25
          - pm10
          - o3
          - no2
          - co
          - so2
          - epa_aqi
          - epa_primary_pollutant
          - epa_health_concern
#          - china_aqi
#          - china_primary_pollutant
#          - china_health_concern
          - pollen_tree
          - pollen_weed
          - pollen_grass
          - road_risk_score
#          - road_risk
          - road_risk_confidence
          - road_risk_conditions
          - fire_index
        update: auto
        scan_interval:
          # At least one of these must be specified:
          days: 0
          hours: 0
          minutes: 30
          seconds: 0
          milliseconds: 0
        exclude_interval:
          1:
            - "23:30"
            - "06:00"
      daily:
        forecast_observations: 1
        conditions:
          - temperature
          - feels_like
#          - dewpoint
          - humidity
          - wind_speed
          - wind_direction
#          - wind_gust
          - pressure
          - precipitation
#          - precipitation_type
          - precipitation_probability
          - precipitation_accumulation
          - sunset
          - sunrise
          - visibility
#          - cloud_cover
#          - cloud_base
#          - cloud_ceiling
#          - satellite_cloud
#          - surface_shortwave_radiation
#          - moon_phase
          - weather_condition
#          - weather_groups
#          - pm25
#          - pm10
#          - o3
#          - no2
#          - co
#          - so2
#          - epa_aqi
#          - epa_primary_pollutant
#          - epa_health_concern
#          - china_aqi
#          - china_primary_pollutant
#          - china_health_concern
#          - pollen_tree
#          - pollen_weed
#          - pollen_grass
#          - road_risk_score
#          - road_risk
#          - road_risk_confidence
#          - road_risk_conditions
#          - fire_index
        scan_interval:
          # At least one of these must be specified:
          days: 0
          hours: 3
          minutes: 0
          seconds: 0
          milliseconds: 0
        exclude_interval:
          1:
            - "10:00"
            - "12:00"
          2:
            - "00:00"
            - "06:30"
      hourly:
        forecast_observations: 1
        conditions:
          - temperature
          - feels_like
          - dewpoint
          - humidity
          - wind_speed
          - wind_direction
          - wind_gust
          - pressure
          - precipitation
          - precipitation_type
          - precipitation_probability
#          - precipitation_accumulation
          - sunset
          - sunrise
          - visibility
          - cloud_cover
          - cloud_base
          - cloud_ceiling
#          - satellite_cloud
          - surface_shortwave_radiation
          - moon_phase
          - weather_condition
#          - weather_groups
          - pm25
          - pm10
          - o3
          - no2
          - co
          - so2
          - epa_aqi
          - epa_primary_pollutant
          - epa_health_concern
#          - china_aqi
#          - china_primary_pollutant
#          - china_health_concern
          - pollen_tree
          - pollen_weed
          - pollen_grass
          - road_risk_score
#          - road_risk
          - road_risk_confidence
          - road_risk_conditions
#          - fire_index
        scan_interval:
          # At least one of these must be specified:
          days: 0
          hours: 1
          minutes: 0
          seconds: 0
          milliseconds: 0
        exclude_interval:
          1:
            - "01:00"
            - "05:00"
      nowcast:
        timestep: 5
        forecast_observations: 1
        conditions:
          - temperature
          - feels_like
          - dewpoint
          - humidity
          - wind_speed
          - wind_direction
          - wind_gust
          - pressure
          - precipitation
          - precipitation_type
#          - precipitation_probability
#          - precipitation_accumulation
          - sunset
          - sunrise
          - visibility
          - cloud_cover
          - cloud_base
          - cloud_ceiling
#          - satellite_cloud
          - surface_shortwave_radiation
#          - moon_phase
          - weather_condition
#          - weather_groups
          - pm25
          - pm10
          - o3
          - no2
          - co
          - so2
          - epa_aqi
          - epa_primary_pollutant
          - epa_health_concern
#          - china_aqi
#          - china_primary_pollutant
#          - china_health_concern
          - pollen_tree
          - pollen_weed
          - pollen_grass
          - road_risk_score
#          - road_risk
          - road_risk_confidence
          - road_risk_conditions
#          - fire_index
        scan_interval:
          # At least one of these must be specified:
          days: 0
          hours: 0
          minutes: 5
          seconds: 0
          milliseconds: 0
        exclude_interval:
          1:
            - "09:00"
            - "10:00"
          2:
            - "13:00"
            - "14:00"
          3:
            - "18:00"
            - "07:00"
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