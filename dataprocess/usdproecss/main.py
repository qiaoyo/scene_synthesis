from core.simple_base import USDProcessingContext,USDProcessor
from flatten import FlattenXform2MeshJoint
from center import CenterChecker
from xformop import XformOpChecker
from pathlib import Path

from pxr import UsdGeom, Gf,UsdShade
import os,sys

if __name__ == "__main__":
    #usd_path = Path("/media/simple/another_Documents/isaacsim_assets/assets/Workbench_2/Workbench_2.usdc")
    usd_path = Path("/media/simple/another_Documents/isaacsim_assets/device_data/usdz/Part/xiejian.usd")
    usd_dir = usd_path.parent
    usd_name = usd_path.name
    usd_context = USDProcessingContext(str(usd_path))
    
    xformop = XformOpChecker()
    center = CenterChecker()
    flatten = FlattenXform2MeshJoint()
    processors = [xformop,flatten,center]
    
    for processor in processors:
        print(f"Running processor: {processor.name}")
        success = processor.process(usd_context)
        if not success:
            print(f"Processor {processor.name} failed.")
            break
    
    stage = usd_context.stage
    # stage.Save()
    stage.Export(str(usd_dir / f"processed_{usd_name}"))
    