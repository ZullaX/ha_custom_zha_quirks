"""Custom quirk: Tuya NDIR CO2 _TZE204_3ejwxpmu (TS0601)."""

from typing import Any

from zhaquirks.tuya.builder import (
    TuyaQuirkBuilder,
    TuyaTemperatureMeasurement,
)


def tuya_air_quality_temperature_converter(value: Any) -> int:
    """Temperature from Tuya DP payload -> centidegrees."""
    return int.from_bytes(value.serialize()[2:4], byteorder="big", signed=True) * 10


(
    TuyaQuirkBuilder("_TZE204_3ejwxpmu", "TS0601")
    .tuya_co2(dp_id=2)
    .tuya_dp(
        dp_id=18,
        ep_attribute=TuyaTemperatureMeasurement.ep_attribute,
        attribute_name=TuyaTemperatureMeasurement.AttributeDefs.measured_value.name,
        converter=tuya_air_quality_temperature_converter,  
    )
    .adds(TuyaTemperatureMeasurement)
    .tuya_humidity(dp_id=19, scale=10)
    .skip_configuration()
    .add_to_registry()
)