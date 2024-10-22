from typing import Optional, List, Dict, Literal
from ..geojson import Point
from datetime import date

from ..readings import AssetReadings, AssetSensors
from .base import BaseAsset

# Constants and types for JunctionGroups
JunctionGroups = {
  "Hydrant": "hydrant",
  "CustomerPoint": "customerPoint",
  "Junction": "junction"
}
JunctionGroupType = Literal["hydrant", "customerPoint", "junction"]

# JunctionSimulation type
class JunctionSimulation():
  pressure: float
  demand: float
  isSupplied: bool
  waterAge: Optional[float]

# Junction type
class Junction(BaseAsset["Junction"]):
  demand: Optional[float]
  description: Optional[str]
  elevation: float
  emitter: Optional[float]
  geometry: Point
  group: JunctionGroupType
  readings: AssetReadings
  sensors: AssetSensors
  simulation: Optional[JunctionSimulation]
  warningThresholdMax: Optional[float]
  warningThresholdMin: Optional[float]
  zones: List[str]

  def get_period_simulation(self) -> List[Dict[str, JunctionSimulation]]:
    """
    Function that returns an array of the simulation values for the whole simulation period with its dates.

    Returns:
        List[Dict[str, JunctionSimulation]]: List of simulation results with dates.
    """
    return [{"date": date.today(), "results": JunctionSimulation()}]