# ha_custom_zha_quirks

Custom [ZHA quirks](https://github.com/zigpy/zha-device-handlers) for Zigbee devices in [Home Assistant](https://www.home-assistant.io/) that are not yet supported in the official `zha-device-handlers` package, or need device-specific mappings.

## Installation

1. Copy this repository into a `custom_zha_quirks` folder next to your `configuration.yaml` (for example `/config/custom_zha_quirks/`).
2. Add the quirks path to `configuration.yaml`. If you already have a `zha:` section, add these lines under it:

```yaml
zha:
  enable_quirks: true
  custom_quirks_path: /config/custom_zha_quirks/
```

3. Restart Home Assistant (or reload the ZHA integration).

After pairing, remove and re-pair a device if it was joined before the quirk was added.

## Devices

| Folder | Device |
|--------|--------|
| `co2/` | Tuya NDIR CO₂ `_TZE204_3ejwxpmu` (TS0601) |
