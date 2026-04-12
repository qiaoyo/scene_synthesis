# usda2md/formatter.py

def format_section_title(title:str,level:int =1)->str:
    #格式化章节标题。
    return f"{'#' * level} {title}"

def format_metadata(metadata:dict) -> str:
    #格式化元数据部分。
    content=[format_section_title("1.场景元数据(Scene Metadata)",2)]
    content.append(f"*  **USDA文件路径(USDA File Path):**[将在主脚本中填写]")
    content.append(f"*  **默认Prim (Default Prim):**'{metadata.get('default_prim','N/A')}'")
    content.append(f"*  **单位与坐标系 (Units & Coordinate System):**")
    content.append(f"   *   **米(Meters Per Unit):**{metadata.get('meters_per_unit','N/A')}")
    content.append(f"   *   **Up Axis:**{metadata.get('up_axis','N/A')}")
    return "\n".join(content)

def format_hierarchy(stage)->str:
#格式化场景层级树
    content=[format_section_title("2.场景对象层级(Scene Hierarchy)",2)]
    pseudo_root = stage.GetPseudoRoot()
    for prim in stage.Traverse():
        if prim == pseudo_root:
            continue
        path = str(prim.GetPath())
        depth = len([part for part in path.split("/") if part])
        indent = "    " * max(depth - 1, 0)
        prefix = "*   "
        prim_type = prim.GetTypeName() or "Prim"
        content.append(f"{indent}{prefix}{prim.GetName()} ({prim_type})")
    return "\n".join(content)

def format_prim_details(prim_data:dict)->str:
    #格式化单个Prim的详细信息。
    if not prim_data:
        return
    
    path = prim_data['path']
    prim_type = prim_data['type']
    
    content = [format_section_title(f"{path}",3)]
    content.append(f"*  **Prim路径 (Prim Path):**{path}")
    content.append(f"*  **Prim类型 (Prim Type):**{prim_type}")
    if not prim_data.get('is_active',True):
        content.append(f"*  **状态(Status):**Inactive")

    # Transform
    transform = prim_data.get('transform')
    if transform:
        content.append(f"*  **变换信息 (Transform):**")
        content.append(f"   *   **平移 (Translate):**'{transform['translate']}'")
        content.append(f"   *   **旋转 (Rotate XYZ, Degrees):**'{transform['rotate_xyz']}'")
        content.append(f"   *   **缩放 (Scale):**'{transform['scale']}'")

    references = prim_data.get("xform_references")
    if references:
        content.append(f"*  **外部引用 (Referenced USD Files):**")
        for idx, ref in enumerate(references, 1):
            source_kind = ref.get("source kind", "reference")
            fallback = f"{source_kind.title()} {idx}"
            label = ref.get("asset_path") or ref.get("identifier") or fallback
            content.append(f"       *   [{source_kind}] '{label}'")
            if ref.get("prim_path"):
                content.append(f"       *   Prim Path: '{ref['prim_path']}'")
            if ref.get("time_offset") is not None or ref.get("time_scale")is not None:
                content.append(f"       *   Layer offset: offset={ref.get('time offset', 0)}, scale={ref.get('time scale', 1)}")
            if ref.get("identifier"):
                content.append(f"       *   Identifier: '{ref['identifier']}'")
            if ref.get("reference type"):
                content.append(f"       *   Type: '{ref['reference type']}'")
            if ref.get("custom_data"):
                content.append(f"       *   Custom Data: '{ref['custom_data']}'")
                
    bbox_world = prim_data.get("bbox_world")
    if bbox_world:
        content.append(f"*  **世界包围盒 (World BBox):**")
        size = bbox_world.get("size")
        center = bbox_world.get("center")
        if size:
            content.append(f"   *   Size: '{size}'")
        if center:
            content.append(f"   *   Center: '{center}'")

    # Geometry
    geometry = prim_data.get('geometry')
    if geometry:
        content.append(f"*  **几何信息 (Geometry):**")
        for key, val in geometry.items():
            content.append(f"   *   **{key.replace('_', ' ').title()}:** {val}")
            
    # Physics
    physics = prim_data.get('physics')
    if physics:
        content.append(f"*  **物理属性 (Physics):**")
        for key, val in physics.items():
            content.append(f"   *   **{key.replace('_', ' ').title()}:** {val}")

    # Light
    light = prim_data.get('light')
    if light:
        content.append(f"*  **灯光参数 (Light Parameters):**")
        for key, val in light.items():
            content.append(f"   *   **{key.replace('_', ' ').title()}:** {val}")
            
    # Material Binding
    binding = prim_data.get('material_binding')
    if binding:
        content.append(f"*  **材质绑定 (Material Binding):** {binding}")

    # Material Details
    material = prim_data.get('material')
    surface_outputs = material.get('surface_outputs') if material else None
    shader_nodes = material.get('shaders') if material else None
    if material and (surface_outputs or shader_nodes):
        content.append(f"*  **材质网络 (Material & Shader Details):**")
        if surface_outputs:
            content.append(f"   *   **Surface Outputs:**")
            for output in surface_outputs:
                line = f"       *   '{output.get('name','outputs:surface')}'"
                if output.get('shader_path'):
                    line += f" -> '{output['shader_path']}'"
                content.append(line)
                if output.get('shader_id'):
                    content.append(f"       *   Shader ID: '{output['shader_id']}'")
                connection = output.get('connection')
                if connection:
                    content.append(f"       *   Connection: '{connection.get('attribute')}' ({connection.get('type')})'")
                if output.get('doc'):
                    content.append(f"       *   Doc: {output['doc']}")
        if shader_nodes:
            content.append(f"   *   **Shader 节点 (Shader Nodes):**")
            for shader in shader_nodes:
                header = f"       *   '{shader.get('path')}'"
                if shader.get('shader_id'):
                    header += f" (ID: '{shader['shader_id']}')"
                content.append(header)
                if shader.get('implementation_source'):
                    content.append(f"       *   Implementation: '{shader['implementation_source']}'")
                source_assets = shader.get('source_assets')
                if source_assets:
                    content.append(f"       *   Source Assets:")
                    for asset in source_assets:
                        line = f"           *   [{asset.get('type')}] '{asset.get('asset_path')}'"
                        if asset.get('sub_identifier'):
                            line += f" (Sub Id: '{asset['sub_identifier']}')"
                        if asset.get('resolved_path'):
                            line += f"  | Resolved: '{asset['resolved_path']}'"
                        content.append(line)
                textures = shader.get('texture_assets')
                if textures:
                    content.append(f"       *   纹理引用 (Texture Assets):")
                    for tex in textures:
                        content.append(f"           *   '{tex}'")
                inputs = shader.get('inputs')
                if inputs:
                    content.append(f"       *   Inputs:")
                    for shader_input in inputs:
                        input_line = f"           *   '{shader_input.get('name')}' [{shader_input.get('type','N/A')}]"
                        value = shader_input.get('value')
                        if value is not None:
                            input_line += f" = '{value}'"
                        content.append(input_line)
                        for connection in shader_input.get('connections', []):
                            conn_line = f"               *   Connected: '{connection.get('attribute')}'"
                            if connection.get('prim_path'):
                                conn_line += f" @ '{connection['prim_path']}'"
                            content.append(conn_line)
                            if connection.get('shader_id'):
                                content.append(f"                   *   Shader ID: '{connection['shader_id']}'")
                            for tex in connection.get('texture_assets', []):
                                content.append(f"                   *   Texture: '{tex}'")
    return "\n".join(content)
