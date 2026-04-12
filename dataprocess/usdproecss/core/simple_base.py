from abc import ABC, abstractmethod
from dataclasses import dataclass
from pxr import Usd, UsdGeom, UsdShade, Gf

class USDProcessingContext(ABC):
    def __init__(self,
                 usd_path: str):
        self.usd_path = usd_path
        
        self.stage = Usd.Stage.Open(usd_path)
        
class USDProcessor(ABC):
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
        
    def process(self, context: USDProcessingContext)->bool:
        pass
    