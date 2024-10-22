from typing import TypedDict, Dict, List, Any, Literal


class RobotCloudNamedItemData(TypedDict):
    id: str
    name: str


class RobotCloudDescribedItemData(RobotCloudNamedItemData):
    description: str


class RobotCloudServiceInstance(RobotCloudNamedItemData):
    service: str


class RobotCloudDeviceDetails(RobotCloudDescribedItemData):
    location: str
    address: Dict[str, int]
    type: int
    configuration_type: str
    tags: List[str]


class RobotCloudProjectDetails(RobotCloudDescribedItemData):
    version: int
    organization: str
    access_level: str
    app_access_level: str
    country: str
    timezone: str
    longitude: float
    latitude: float
    image_url: str
    application_enabled: bool


class RobotCloudServiceInstanceMeasurement(TypedDict):
    instance: str
    time_mark: str
    status: str
    value: Dict[str, Any]


HistoricAggregateFunction = Literal["count", "increase", "mean", "first", "last", "max", "min",
                                    "amax", "amin", "pmax", "pmin", "nmax", "nmin"]