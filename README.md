# ClimaCell weather service provider integration
### ... is a custom component (sensor) for Home Assistant.<br>

The `ClimaCell` platform uses the <a href="https://www.climacell.co/weather-api/docs/" target="_blank">ClimaCell API</a> as a source for meteorological data for your location.

[![hacs_badge](https://img.shields.io/badge/HACS-Default-orange.svg)](https://github.com/custom-components/hacs)

[![License][license-shield]](LICENSE)

[![BuyMeCoffee][buymecoffeebadge]][buymecoffee]

_To use this component you must obtain an API key. Visit the <a href="https://www.climacell.co/weather-api" target="_blank">ClimaCell</a> site to learn how to obtain one._

## **WARNING**
`Realtime`, `nowcast`, `hourly` and `daily` are different services, so they consume one API call each.

## Manual installation

1. Using the tool of choice, open the directory (folder) of your HA configuration (there you can find `configuration.yaml`).
2. If you do not have a `custom_components` directory (folder) there, you need to create one.
3. In the `custom_components` directory (folder) create a new folder called `climacell`.
4. Download _all_ the files from this repository.
5. Place the content of the `custom_components/climacell/` directory (folder) in the new directory (folder) you created.

## Configuration
To use the `ClimaCell` custom component you must first obtain an <a href="https://www.climacell.co/weather-api/pricing/">API key</a>. 

### Sensor variables

<dl>
  <dt>api_key</dt>
  <dd><i>(string)(Required)</i><br>Your API key.</dd>  
  
  <dt>name</dt>
  <dd><i>(string)(Optional)</i><br>Additional name for the sensors. PS The name of the sensor always starts with the prefix <code>cc</code></dd>
  <dd><i>Default value:</i><br>climacell</dd>
  
  <dt>latitude</dt>
  <dd><i>(float)(Optional)</i><br>Latitude coordinate to monitor weather of (required if longitude is specified).</dd>
  <dd><i>Default value:</i><br>coordinates from the Home Assistant configuration</dd>
  
  <dt>longitude</dt>
  <dd><i>(float)(Optional)</i><br>Longitude coordinate to monitor weather of (required if latitude is specified).</dd>
  <dd><i>Default value:</i><br>Coordinates from the Home Assistant configuration</dd>
  
  <dt>units</dt>
  <dd><i>(string)(Optional)</i><br>Specify the unit system. Valid options are <code>us</code>, <code>si</code>.</dd>
  <dd><i>Default value:</i><br><code>si</code> or <code>us</code>, based on the temperature preference in Home Assistant</dd>   
  
  <dt>timelines</dt>
  <dd><i>(object list)(Required)</i><br>List of timeline specification. Each list item is an object with the following variables.</dd>
  <dd>
    <dl>
      <dt>name</dt>
      <dd><i>(string)(Optional)</i><br>Name of timeline used for naming the sensors.</dd>
      <dd><i>Default value:</i><br>None</dd>
      <dt>fields</dt>
      <dd><i>(string list)(Required)</i><br>Conditions to view. These depend on the type of service, see the section below for more details.</dd>
      <dt>timestep</dt>
      <dd><i>(string)(Optional)</i><br>Step length for observations consisting of an integer value followed by 'm' for minute, 'h' for hour or 'd' for day.</dd>
      <dd><i>Default value:</i><br>1d</dd>
      <dt>forecast_observations</dt>
      <dd><i>(integer)(Optional)</i><br>Number of timesteps for which you would like to receive forecast.</dd>
      <dd><i>Default value:</i><br>5</dd>
      <dt>scan_interval</dt>
      <dd><i>(time)(Optional)</i><br>Minimum time interval between updates.</dd>
      <dd><i>Default value:</i><br>5 minutes</dd>
      <dt>exclude_interval</dt>
      <dd><i>(array of object)(Optional)</i><br>Intervals excluded from the update to use to reduce the number of the API calls. Each interval consists of a pair of values and indicates the start and end of the update exclusion. In particular you can specify from 1 to 20 different ranges.
          <dl>  
            <dt>Example</dt>
            <dd>exclude_interval:</dd> 
            <dd>&emsp;1:&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;# range</dd>
            <dd>&emsp;&emsp;- "23:30"&emsp;# start</dd>
            <dd>&emsp;&emsp;- "06:00"&emsp;# end</dd>
          </dl>  
      </dd>  
      <dd><i>Default value:</i><br>None</dd>
      <dt>start_time</dt>
      <dd><i>(integer)(Optional)</i><br>Number of minutes in future (+) or past (-) from the current time to start the timeline. The availability depends on timestep and requested fields.</dd>
      <dd><i>Default value:</i><br>0</dd>
    </dl>
  </dd>   
</dl>

### Condition information

The available Fields and suffixes can be found in the <a href="https://docs.climacell.co/reference/data-layers-overview" target="_blank">climacell dodumentation</a>. The old field names can still be used.

### Migration from V3 Version

To make the integration API V4 compatible it has been largely restructured. We tried to make it backward compatible regarding configuration and sensor names but there might be some cornercases where the sensornames change when upgrading.

## Integration Examples

```yaml
sensor:
## Weather climatecell.co
  - platform: climacell
    api_key: !secret climacell_api_key
    name: example
    latitude: !secret gps_geo_home_lt
    longitude: !secret gps_geo_home_ln
    units: metric
    timelines:
      - name: "Daily"
        fields:
          - temperature
          - wind_direction
          - precipitation
          - precipitation_type
          - wind_speed
          - wind_direction
          - weather_condition
          - pollen_tree
          - pollen_weed
          - pollen_grass
        start_time: -5
        forecast_observations: 3
        timestep: "1d"
        update: auto
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
| cc_temperature  | 13.2      | attribution           | Powered by Climacell     |
|                 |           | unit_of_measurement   | C                        |
|                 |           | observation_time      | 2020-04-30T02:40:47.390Z |
|                 |           | friendly_name         | Temperature              |
|                 |           | icon                  | mdi:thermometer          |


[license-shield]:https://img.shields.io/github/license/r-renato/ha-climacell-weather
[buymecoffee]: https://www.buymeacoffee.com/0D3WbkKrn
[buymecoffeebadge]: https://img.shields.io/badge/buy%20me%20a%20coffee-donate-yellow?style=for-the-badge
