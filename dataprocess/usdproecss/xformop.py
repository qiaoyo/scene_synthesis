from core.simple_base import USDProcessingContext, USDProcessor
from pxr import Gf, Usd, UsdGeom
from utils.utils_prim_info import decompose_matrix_to_trs, decompose_matrix_to_tos


class XformOpChecker(USDProcessor):
    def __init__(self):
        super().__init__(name="XformOpChecker", description="check the xform op order of the prim")

    def process(self, context: USDProcessingContext) -> bool:
        stage = context.stage
        print("xformOpChecker process")
        for prim in stage.Traverse():
            if prim.IsPseudoRoot():
                continue

            if prim.IsA(UsdGeom.Xform):
                self._normalize_xform_prim(prim)
            elif prim.IsA(UsdGeom.Mesh):
                self._normalize_mesh_prim(prim)
        return True

    def _normalize_xform_prim(self, prim: Usd.Prim) -> None:
        """Ensure Xform prims author translate/rotate/scale ops with correct values."""
        xformable = UsdGeom.Xformable(prim)
        local_matrix = self._get_local_matrix(xformable)
        translation, rotation, scale = decompose_matrix_to_trs(local_matrix)
        translation, orientation, scale = decompose_matrix_to_tos(local_matrix)
        self._clear_existing_ops(prim, xformable)

        # print(f"prim.GetAttribute('xformOp:orient').Get(): {prim.GetAttribute('xformOp:orient').Get()}")
        # print(f"prim.GetAttribute('xformOp:scale').Get(): {prim.GetAttribute('xformOp:scale').Get()}")
        # print(f"prim.GetAttribute('xformOp:translate').Get(): {prim.GetAttribute('xformOp:translate').Get()}")
        # print(f"prim.GetAttribute('xformOp:transform').Get(): {prim.GetAttribute('xformOp:transform').Get()}")
        # print(f"prim.GetAttribute('xformOpOrder').Get(): {prim.GetAttribute('xformOpOrder').Get()}")

        translate_op = xformable.AddTranslateOp()
        orient_op = xformable.AddOrientOp()
        # rotatezyx_op = xformable.AddRotateZYXOp()
        scale_op = xformable.AddScaleOp()

        translate_op.Set(translation, Usd.TimeCode.Default())
        # rotatezyx_op.Set(rotation, Usd.TimeCode.Default())
        orient_op.Set(orientation, Usd.TimeCode.Default())
        scale_op.Set(scale, Usd.TimeCode.Default())

    def _normalize_mesh_prim(self, prim: Usd.Prim) -> None:
        """Author a single transform op on Mesh prims using their local matrix."""
        # print(prim)
        xformable = UsdGeom.Xformable(prim)
        local_matrix = self._get_local_matrix(xformable)

        self._clear_existing_ops(prim, xformable)

        transform_op = xformable.AddTransformOp(UsdGeom.XformOp.PrecisionDouble, "transform")
        transform_op.Set(local_matrix, Usd.TimeCode.Default())

    def _get_local_matrix(self, xformable: UsdGeom.Xformable) -> Gf.Matrix4d:
        """Return only the matrix part from GetLocalTransformation."""
        result = xformable.GetLocalTransformation(Usd.TimeCode.Default())
        if isinstance(result, tuple):
            return result[0]
        return result

    def _clear_existing_ops(self, prim: Usd.Prim, xformable: UsdGeom.Xformable) -> None:
        # for op in xformable.GetOrderedXformOps():
        xform_op_order = prim.GetAttribute("xformOpOrder")
        if not xform_op_order.Get():
            return
        for xform_op in xform_op_order.Get():
            prim.RemoveProperty(xform_op)

        xform_op_transform = prim.GetAttribute("xformOp:transform")
        if xform_op_transform.Get():
            prim.RemoveProperty("xformOp:transform")
        xformable.ClearXformOpOrder()
