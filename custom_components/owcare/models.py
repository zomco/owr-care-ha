"""Models for Owcare."""
from homeassistant.helpers.device_registry import CONNECTION_NETWORK_MAC, DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .const import DOMAIN
from .coordinator import OwcareDataUpdateCoordinator


class OwcareEntity(CoordinatorEntity[OwcareDataUpdateCoordinator]):
    """Defines a base Owcare entity."""

    _attr_has_entity_name = True

    @property
    def device_info(self) -> DeviceInfo:
        """Return device information about this Owcare device."""
        # print(json.dumps(self.coordinator.data.__dict__, indent=4))
        return DeviceInfo(
            connections={
                (CONNECTION_NETWORK_MAC, self.coordinator.data.info.mac_addr)
            },
            identifiers={(DOMAIN, self.coordinator.data.info.mac_addr)},
            name=self.coordinator.data.info.name,
            manufacturer=self.coordinator.data.info.brand,
            model=self.coordinator.data.info.product,
            sw_version=str(self.coordinator.data.info.version),
            hw_version=self.coordinator.data.info.architecture,
            configuration_url=f"http://{self.coordinator.client.host}",
        )
