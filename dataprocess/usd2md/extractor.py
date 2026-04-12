from pxr import Usd, UsdGeom, UsdShade, UsdPhysics, UsdLux, Sdf, Gf

_VEC_TYPES = ( 
            Gf.Vec2f, 
            Gf.Vec3f, 
            Gf.Vec4f, 
            Gf.Vec2d, 
            Gf.Vec3d, 
            Gf.Vec4d, 
            Gf.Vec2h, 
            Gf.Vec3h, 
            Gf.Vec4h, 
            )

def _format_vec(vec):
    return "(" + ", ".join(f"{component:.3f}" for component in vec) + ")"

def _format_value(value):
    if value is None:
        return None
    if isinstance(value, Sdf.AssetPath):
        return value.path or value.resolvedPath or ""
    if isinstance(value, _VEC_TYPES):
        return _format_vec(value)
    if isinstance(value, (float,)):
        return f"{value:.6f}".rstrip("0").rstrip(".")
    if isinstance(value, (tuple, list)) and len(value) in (2, 3, 4):
        try:
            return _format_vec(value)
        except TypeError:
            pass
        return str(value)

def _is_numeric_value(value):
    if isinstance(value, (int, float)):
        return True
    if isinstance(value, _VEC_TYPES):
        return True
    if isinstance(value, (tuple, list)):
        try:
            return all(isinstance(component, (int, float)) for component in value)
        except TypeError:
            return False
    return False

def _asset_path_to_str(value):
    if isinstance(value, Sdf.AssetPath):
        return value.path or value.resolvedPath or ""
    return None
    
def _extract_texture_assets_from_shader(shader: UsdShade.Shader):
    assets = set()
    for shader_input in shader.GetInputs():
        attr = shader_input.GetAttr()
        if attr and attr.HasAuthoredValueOpinion():
            asset_path = _asset_path_to_str(shader_input.Get())
            if asset_path:
                assets.add(asset_path)
    return sorted(assets)

def _describe_shader_input(shader_input: UsdShade.Input):
    info = {
        "name": shader_input.GetBaseName(),
        "type": str(shader_input.GetTypeName()),
    }
    attr = shader_input.GetAttr()
    if attr and attr.HasAuthoredValueOpinion():
        raw_value = shader_input.Get()
        info["value"] = _format_value(raw_value)
        info["value_numeric"] = _is_numeric_value(raw_value)

    connections = []
    upstream_shaders = []
    stage = shader_input.GetPrim().GetStage()
    for path in shader_input.GetRawConnectedSourcePaths():
        conn_info = {"attribute": str(path)}
        prim_path = path.GetPrimPath()
        if prim_path:
            conn_info["prim_path"] = str(prim_path)
            prim = stage.GetPrimAtPath(prim_path)
            if prim and prim.IsA(UsdShade.Shader):
                shader = UsdShade.Shader(prim)
                upstream_shaders.append(shader)
                conn_info["shader_id"] = shader.GetIdAttr().Get()
                textures = _extract_texture_assets_from_shader(shader)
                if textures:
                    conn_info["texture_assets"] = textures
        connections.append(conn_info)

    if connections:
        info["connections"] = connections

    if not info.get("value") and not connections:
        return None, upstream_shaders
    return info, upstream_shaders

def _describe_composition_item(item, source_kind: str):
    info = {"source_kind": source_kind}
    asset_path = getattr(item, "assetPath", None)
    if asset_path:
        info["asset_path"] = asset_path
    prim_path = getattr(item, "primPath", None)
    if prim_path:
        info["prim_path"] = str(prim_path)
    identifier = getattr(item, "identifier", None)
    if identifier:
        info["identifier"] = identifier
    layer_offset = getattr(item, "layerOffset", None)
    if layer_offset and not layer_offset.IsIdentity():
        info["time_offset"] = layer_offset.timeOffset
        info["time_scale"] = layer_offset.timeScale
    custom_data = getattr(item, "customData", None)
    if custom_data:
        info["custom_data"] = dict(custom_data)
    reference_type = getattr(item, "referenceType", None)
    if reference_type:
        info["reference_type"] = str(reference_type)
    return info

def get_shader_details(shader: UsdShade.Shader):
    details = {
        "path": str(shader.GetPath()),
        "shader_id": shader.GetIdAttr().Get(),
        "implementation_source": shader.GetImplementationSourceAttr().Get(),
        "source_assets": [],
        "texture_assets": _extract_texture_assets_from_shader(shader),
        "inputs": [],
    }
    
    source_types = shader.GetSourceTypes()
    if source_types:
        for source_type in source_types:
            asset = shader.GetSourceAsset(source_type)
            asset_path = _asset_path_to_str(asset)
            if asset_path:
                details["source_assets"].append({
                    "type": source_type,
                    "asset_path": asset_path,
                    "resolved_path": asset.resolvedPath if isinstance(asset, Sdf.AssetPath) else None,
                    "sub_identifier": shader.GetSourceAssetSubIdentifier(source_type) or None,
                })

    upstream_shaders = []
    for shader_input in shader.GetInputs():
        input_info, upstream = _describe_shader_input(shader_input)
        if input_info:
            details["inputs"].append(input_info)
        upstream_shaders.extend(upstream)

    return details, upstream_shaders

def get_scene_metadata(stage: Usd.Stage):
    # 提取场景的全局元数据。
    up_axis = UsdGeom.GetStageUpAxis(stage)
    meters_per_unit = UsdGeom.GetStageMetersPerUnit(stage)
    default_prim = stage.GetDefaultPrim().GetName() if stage.GetDefaultPrim() else "Not Set"

    return {
        "up_axis": up_axis,
        "meters_per_unit": meters_per_unit,
        "default_prim": default_prim,
    }


def get_prim_transform(prim: Usd.Prim):
    # 提取Prim的变换信息。
    if not prim or not prim.IsValid():
        return None

    xformable = UsdGeom.Xformable(prim)
    if not xformable:
        return None

    xform_api = UsdGeom.XformCommonAPI(prim)
    if not xform_api:
        return None

    try:
        translate, rotate, scale, _, _ = xform_api.GetXformVectors(Usd.TimeCode.Default())
    except Exception:
        return None

    return {
        "translate": _format_vec(translate),
        "rotate_xyz": _format_vec(rotate),
        "scale": _format_vec(scale),
    }


def get_mesh_details(prim: Usd.Prim):
    #如果Prim是Mesh,提取其几何信息。
    if not prim.IsA(UsdGeom.Mesh):
        return None

    mesh = UsdGeom.Mesh(prim)
    details = {}

    points_attr = mesh.GetPointsAttr()
    if points_attr and points_attr.HasValue():
        details["vertex_count"] = len(points_attr.Get())

    face_counts_attr = mesh.GetFaceVertexCountsAttr()
    if face_counts_attr and face_counts_attr.HasValue():
        details["face_count"] = len(face_counts_attr.Get())

    extent_attr = mesh.GetExtentAttr()
    if extent_attr and extent_attr.HasValue():
        extent = extent_attr.Get()
        min_pt, max_pt = extent[0], extent[1]
        size = max_pt - min_pt
        details["bounding_box_size"] = f"({size[0]:.3f}, {size[1]:.3f}, {size[2]:.3f})"

    return details if details else None

def get_material_details(prim: Usd.Prim):
    #如果Prim是Material, 提取其着色器信息。
    if not prim.IsA(UsdShade.Material):
        return None

    material = UsdShade.Material(prim)

    outputs = material.GetSurfaceOutputs()
    if not outputs:
        default_output = material.GetSurfaceOutput()
        if default_output:
            outputs = [default_output]

    surface_outputs = []
    shader_map = {}

    def enqueue_shader(shader_obj: UsdShade.Shader):
        if not shader_obj:
            return
        shader_path = str(shader_obj.GetPath())
        if shader_path in shader_map:
            return
        details, upstream = get_shader_details(shader_obj)
        shader_map[shader_path] = details
        for upstream_shader in upstream:
            enqueue_shader(upstream_shader)

    for output in outputs or []:
        if not output:
            continue
        output_info = {
            "name": output.GetFullName(),
            "type": str(output.GetTypeName()),
        }
        attr = output.GetAttr()
        if attr:
            doc = attr.GetDocumentation()
            if doc:
                output_info["doc"] = doc

        if output.HasConnectedSource():
            connectable_api, attr_name, attr_type = output.GetConnectedSource()
            prim = connectable_api.GetPrim() if connectable_api else None
            
            if prim:
                output_info["connected_prim"] = str(prim.GetPath())
                if prim.IsA(UsdShade.Shader):
                    shader = UsdShade.Shader(prim)
                    output_info["shader_path"] = str(prim.GetPath())
                    output_info["shader_id"] = shader.GetIdAttr().Get()
                    enqueue_shader(shader)
            output_info["connection"] = {
                "attribute": attr_name,
                "type": str(attr_type)
            }

        surface_outputs.append(output_info)

    if not surface_outputs and not shader_map:
        return None

    return{
        "surface_outputs":surface_outputs,
        "shaders":list(shader_map.values()),
    }


def get_physics_details(prim: Usd.Prim):
    # 提取Prim的物理属性。
    details = {}
    
    if prim.HasAPI(UsdPhysics.RigidBodyAPI):
        rb_api = UsdPhysics.RigidBodyAPI(prim)
        details["rigid_body"] = True
        mass_attr = rb_api.GetMassAttr()
        if mass_attr and mass_attr.HasValue():
            details["mass"] = mass_attr.Get()

    if prim.HasAPI(UsdPhysics.CollisionAPI):
        details["collider"] = True
        
    return details if details else None

def get_light_details(prim: Usd.Prim):
    # 提取灯光参数。
    light = UsdLux.LightAPI(prim)
    if not light:
        return None

    details = {}

    intensity_attr = light.GetIntensityAttr()
    if intensity_attr and intensity_attr.HasValue():
        details["intensity"] = intensity_attr.Get()

    color_attr = light.GetColorAttr()
    if color_attr and color_attr.HasValue():
        color = color_attr.Get()
        details["color"] = f"({color[0]:.3f}, {color[1]:.3f}, {color[2]:.3f})"

    # Add more light-specific attributes if needed
    return details if details else None

def _get_list_op_items(prim: Usd.Prim, field: str):
    list_op = prim.GetMetadata(field)
    if not list_op:
        return []
    try:
        return list_op.GetAddedOrExplicitItems()
    except Exception:
        items = []
        for attr in ("explicitItems", "addedItems", "prependedItems", "appendedItems"):
            values = getattr(list_op, attr, None)
            if values:
                items.extend(list(values))
    return items

def get_xform_reference_details(prim: Usd.Prim):
    "提取Xform引用的USD文件信息。"
    if not prim.IsA(UsdGeom.Xform):
        return None

    ref_details = []
    reference_items = _get_list_op_items(prim, "references")
    for ref in reference_items:
        ref_details.append(_describe_composition_item(ref, "reference"))

    payload_items = _get_list_op_items(prim, "payload")
    for payload in payload_items:
        ref_details.append(_describe_composition_item(payload, "payload"))

    return ref_details or None

def get_prim_data(prim: Usd.Prim):
    """为单个Prim提取所有相关信息。"""
    if not prim.IsValid():
        return None

    data = {
        "path": str(prim.GetPath()),
        "type": prim.GetTypeName(),
        "is_active": prim.IsActive(),
        "transform": get_prim_transform(prim)
    }

    # Type specific details
    if prim.IsA(UsdGeom.Mesh):
        data["geometry"] = get_mesh_details(prim)
    if prim.IsA(UsdShade.Material):
        material_details = get_material_details(prim)
        if material_details:
            data["material"] = material_details
    light_details = get_light_details(prim)
    if light_details:
        data["light"] = light_details
    data["physics"] = get_physics_details(prim)
    
    #Material binding

    binding_api = UsdShade.MaterialBindingAPI(prim)
    if binding_api:
        direct_binding = binding_api.GetDirectBinding()
        if direct_binding:
            material = direct_binding.GetMaterial()
            if material:
                data["material_binding"]=str(material.GetPath())

    xform_refs = get_xform_reference_details(prim)
    if xform_refs:
        data["xform_references"]=xform_refs
        
    return data
