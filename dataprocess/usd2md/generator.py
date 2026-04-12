# usd2md/generator.py

import os
from pxr import Usd, UsdShade, UsdGeom
import extractor
import formatter

class UsdaDocumentGenerator:
    def __init__(self, usda_path: str, mode: str = "verbose"):
        if not os.path.exists(usda_path):
            raise FileNotFoundError(f"USDA file not found at: {usda_path}")
        self.usda_path = usda_path
        self.stage = Usd.Stage.Open(usda_path)
        if not self.stage:
            raise RuntimeError(f"Failed to open USD stage from: {usda_path}")

        mode_normalized = mode.lower()
        if mode_normalized not in {"verbose", "brief"}:
            raise ValueError("mode 必须是 'verbose' 或'brief'")
        self.mode = mode_normalized
        self._bbox_cache = UsdGeom.BBoxCache(Usd.TimeCode.Default(), ["default"])

    def generate(self) -> str:
        """生成Markdown文档字符串。"""
        doc_parts = []

        # 1. Header
        scene_name = os.path.basename(self.usda_path)
        doc_parts.append(formatter.format_section_title(f"USDA场景描述文档:{scene_name}", 1))

        # 2. Metadata
        metadata = extractor.get_scene_metadata(self.stage)
        metadata_str = formatter.format_metadata(metadata)
        metadata_str = metadata_str.replace("[将在主脚本中填写]", f"`{self.usda_path}`")
        doc_parts.append(metadata_str)

        # 3. Hierarchy
        doc_parts.append(formatter.format_hierarchy(self.stage))

        # 4. Detailed Prim Descriptions
        if self.mode == "verbose":
            doc_parts.extend(self._generate_verbose_sections())
        else:
            doc_parts.extend(self._generate_brief_sections())
        return "\n\n".join(doc_parts)
    
    def _generate_verbose_sections(self):
        parts = [formatter.format_section_title("3. 对象详细描述 (Detailed Prim Descriptions)", 2)]
        prims_to_detail, materials = self._collect_verbose_targets()
        for prim in prims_to_detail:
            data = extractor.get_prim_data(prim)
            if data:
                if prim.GetTypeName() == "Xform" and (prim.HasAuthoredReferences() or prim.HasPayload()):
                    bbox_summary = self._compute_bbox_summary(prim)
                    if bbox_summary:
                        data["bbox_world"] = {
                            "size": bbox_summary["size_str"],
                            "center": bbox_summary["center_str"],
                        }
                    parts.append(formatter.format_prim_details(data))
                    parts.append("\n---\n")

        if materials:
            parts.append(formatter.format_section_title("4. 材质库 (Material Library)", 2))
            for prim in materials:
                data = extractor.get_prim_data(prim)
                if data:
                    parts.append(formatter.format_prim_details(data))
                    parts.append("\n---\n")
        return parts

    def _collect_verbose_targets(self):
        prims_to_detail = []
        materials_to_detail = []
        pseudo_root = self.stage.GetPseudoRoot()
        for prim in self.stage.Traverse():
            if prim == pseudo_root:
                continue
            if prim.IsA(UsdShade.Material):
                materials_to_detail.append(prim)
                continue

            type_name = prim.GetTypeName()
            if type_name == "Scope":
                continue
            if type_name == "Xform":
                if prim.HasAuthoredReferences() or prim.HasPayload():
                    prims_to_detail.append(prim)
                continue
            if type_name:
                prims_to_detail.append(prim)
        return prims_to_detail, materials_to_detail

    def _generate_brief_sections(self):
        parts = [formatter.format_section_title("3. 外部引用Xform简报(Referenced Xforms)", 2)]
        xforms = self._collect_referenced_xforms()
        if not xforms:
            parts.append("暂无引用USD的Xform。")
            return parts
    
        for prim in xforms:
            summary = self._format_brief_xform_section(prim)
            if summary:
                parts.append(summary)
                parts.append("\n---\n")
        return parts

    def _collect_referenced_xforms(self):
        pseudo_root = self.stage.GetPseudoRoot()
        xforms = []
        for prim in self.stage.Traverse():
            if prim == pseudo_root:
                continue
            if prim.GetTypeName() == "Xform" and (prim.HasAuthoredReferences() or prim.HasPayload()):
                xforms.append(prim)
        return xforms

    def _collect_child_mesh_data(self, prim: Usd.Prim):
        meshes = []
        for descendant in Usd.PrimRange(prim):
            if descendant == prim:
                continue
            if descendant.IsA(UsdGeom.Mesh):
                mesh_data = extractor.get_prim_data(descendant)
                if mesh_data:
                    meshes.append(mesh_data)
        return meshes
    
    def _compute_bbox_summary(self, prim: Usd.Prim):
        if not prim or not prim.IsValid():
            return None
        try:
            bbox = self._bbox_cache.ComputeWorldBound(prim)
        except Exception:
            return None
        if not bbox:
            return None
        bbox_range = bbox.GetRange()
        size = bbox_range.GetSize()
        center = bbox.ComputeCentroid()
        size_tuple = (size[0], size [1], size [2])
        center_tuple = (center[0], center [1], center [2])
        return {
            "size": size_tuple,
            "center": center_tuple,
            "size_str": self._format_vec(size_tuple),
            "center_str": self._format_vec(center_tuple),
        }
        
    def _summarize_meshes_for_brief(self, mesh_datas):
        entries = []
        materials = set()
        total_vertices = 0
        total_faces = 0
        for data in mesh_datas:
            path = data.get("path")
            binding = data.get("material_binding")
            entries.append({
                "path": path,
                "material_binding": binding or "未绑定"
            })
            if binding:
                materials.add(binding)
            geometry = data.get("geometry") or {}
            total_vertices += geometry.get("vertex_count", 0) or 0
            total_faces += geometry.get("face_count", 0) or 0

        return {
            "entries": entries,
            "material_paths": sorted(materials),
            "count": len(entries),
            "total_vertices": total_vertices,
            "total_faces": total_faces,
        }
        
    def _summarize_material_for_brief(self, material_path: str):
        prim = self.stage.GetPrimAtPath(material_path)
        if not prim or not prim.IsValid():
            return None
        data = extractor.get_prim_data(prim)
        if not data:
            return None
        mat_payload = data.get("material")
        if not mat_payload:
            return None

        mdl_assets = set()
        textures = set()
        numeric_inputs = []

        for shader in mat_payload.get("shaders", []):
            for asset in shader.get("source_assets", []):
                source_type = (asset.get("type") or "").lower()
                if source_type == "mdl" and asset.get("asset path"):
                    mdl_assets.add(asset["asset_path"])
            for tex in shader.get("texture_assets", []):
                if tex:
                    textures.add(tex)
            for shader_input in shader.get("inputs", []):
                if shader_input.get("value") is not None and shader_input.get("value_numeric"):
                    numeric_inputs.append(f"{shader_input.get('name')}={shader_input.get('value')}")
                for conn in shader_input.get("connections", []):
                    for tex in conn.get("texture_assets", []):
                        if tex:
                            textures.add(tex)
        return {
            "path": material_path,
            "mdl_assets": sorted(mdl_assets),
            "numeric_inputs": numeric_inputs,
            "textures": sorted(textures),
        }

    def _format_brief_xform_section(self, prim: Usd.Prim):
        data = extractor.get_prim_data(prim)
        if not data:
            return ""

        meshes = self._collect_child_mesh_data(prim)
        mesh_summary = self._summarize_meshes_for_brief(meshes)
        material_summaries = [
            summary for summary in
            (self._summarize_material_for_brief(path) for path in mesh_summary["material_paths"])
            if summary
        ]
        lines = [formatter.format_section_title(f"'{data['path']}' (Xform)", 3)]

        references = data.get("xform_references") or []
        if references:
            ref_line = "; ".join(self._format_reference_entry(ref) for ref in references)
            lines.append(f"* 引用: {ref_line}")

        transform = data.get("transform")
        if transform:
            translate = transform.get("translate", "N/A")
            rotate = transform.get("rotate_xyz", "N/A")
            scale = transform.get("scale", "N/A")
            lines.append(
                f"* 变换: T={translate}; R={rotate}; S={scale}"
            )

        bbox_summary = self._compute_bbox_summary(prim)
        if bbox_summary:
            lines.append(
                f"* BBox (world): size={bbox_summary['size_str']}, center={bbox_summary['center_str']}"
            )

        lines.append(
            f"* 几何统计: Mesh={mesh_summary['count']}, "
            f"Vertices={mesh_summary['total_vertices']}, Faces={mesh_summary['total_faces']}"
        )

        if mesh_summary["entries"]:
            mesh_pairs = [
                f"{entry['path']} -> {entry['material_binding']}"
                for entry in mesh_summary["entries"]
            ]
            lines.append(f"* 子Mesh材质: {', '.join(mesh_pairs)}")

        if material_summaries:
            lines.append(f"* 材质摘要:")
            for summary in material_summaries:
                parts = []
                if summary["mdl_assets"]:
                    parts.append("MDL: " + ", ".join(f"'{asset}'" for asset in summary["mdl_assets"]))
                if summary["numeric_inputs"]:
                    parts.append("Inputs: " + ", ".join(f"'{item}'" for item in summary["numeric_inputs"]))
                if summary["textures"]:
                    parts.append("Textures: " + ", ".join(f"'{tex}'" for tex in summary["textures"]))
                if parts:
                    lines.append(f" * {summary['path']} -> {', '.join(parts)}")

        return "\n".join(lines)

    @staticmethod
    def _format_reference_entry(ref_info: dict) -> str:
        source_kind = ref_info.get("source_kind", "reference")
        label = ref_info.get("asset_path") or ref_info.get("identifier") or ref_info.get("prim_path") or "_"
        suffix = ref_info.get("prim_path")
        extra = f" @{suffix}" if suffix else ""
        return f"{source_kind}:{label}{extra}"
        
    @staticmethod
    def _format_vec(tuple_vec):
        if not tuple_vec:
            return "N/A"
        return "(" + ", ".join(f"{component:.3f}" for component in tuple_vec) + ")"

    def write_to_file(self, output_path: str):
        """生成文档并写入文件."""
        content = self.generate()
        output_dir = os.path.dirname(output_path)
        if output_dir:
            os.makedirs(output_dir, exist_ok=True)

        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Documentation successfully written to: {output_path}")