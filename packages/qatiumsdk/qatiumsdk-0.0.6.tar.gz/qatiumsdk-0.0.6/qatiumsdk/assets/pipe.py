from typing import Optional, List, Union, Literal, Dict
from ..geojson import LineString, MultiLineString
from datetime import date
from ..readings import AssetReadings, AssetSensors
from .base import BaseAsset

# PipeStatus type
PipeStatus = Literal["OPEN", "CLOSED"]

# PipeGroups type
PipeGroups = {
  "Main": "main",
  "Lateral": "lateral"
}
PipeGroupType = Literal["main", "lateral"]

# PipeSimulation type
class PipeSimulation():
  status: PipeStatus
  flow: float
  velocity: float
  unitaryHeadloss: float
  isSupplied: bool

# Pipe type
class Pipe(BaseAsset["Pipe"]):
  description: Optional[str]
  geometry: Union[LineString, MultiLineString]
  diameter: float
  length: float
  roughness: float
  minorLoss: float
  status: PipeStatus
  group: PipeGroupType
  isCV: bool
  material: Optional[str]
  installationDate: Optional[date]
  simulation: Optional[PipeSimulation]
  readings: AssetReadings
  sensors: AssetSensors
  zones: List[str]
  warningThresholdMin: Optional[float]
  warningThresholdMax: Optional[float]

  def get_period_simulation(self) -> List[Dict[str, PipeSimulation]]:
    """
    Function that returns an array of the simulation values for the whole simulation period with its dates.

    Returns:
        List[Dict[str, PipeSimulation]]: List of simulation results with dates.
    """
    return [{"date": date.today(), "results": PipeSimulation()}]
