# USDA场景描述文档:assembly1.usda

## 1.场景元数据(Scene Metadata)

* **USDA文件路径(USDA File Path):**`/media/simple/another_Documents/isaacsim_assets/scenedata/assembly1.usda`
* **默认Prim (Default Prim):**'Not Set'
* **单位与坐标系 (Units & Coordinate System):**
  * **米(Meters Per Unit):**1.0
  * **Up Axis:**Z
* **场景描述(Scene Describe):** 该生产车间采用矩阵式模块化布局，由多条平行的蓝色高架输送线与成排的机器人作业单元构成。核心区域分布着至少六组标准化的协作工作站，每组均在黄色木质工作台上配备了一台白色协作机器人与一台橙色工业机器人，用于对半圆弧形工件进行精密加工。黑色输送带负责工件的长程流转，而多台黄色AGV则载着周转箱在工位间穿梭，实现柔性物料补给。整体规划采用“分布式单元+集中式输送”的架构，将固定输送与柔性物流深度融合，展现了智能工厂高扩展性与高效率的柔性制造特征。
* **设备数量(Device Number):**
  * **Scene: 1**
  * **IndustrialRobot: 14**
  * **Workbench: 21**
  * **Conveyor: 28**
  * **AGV: 6**
  * **Forklift: 0**
  * **Box: 6**
  * **Rack: 0**
  * **Pallet: 0**
  * **Part: 138**
  * **Decoration: 0**

## 2.场景对象层级(Scene Hierarchy)

* Render (Prim)
  * OmniverseKit (Prim)
    * HydraTextures (Prim)
      * omni_kit_widget_viewport_ViewportTexture_0 (RenderProduct)
  * OmniverseGlobalRenderSettings (RenderSettings)
  * Vars (Prim)
    * LdrColor (RenderVar)
* World (Prim)
  * DomeLight (DomeLight)
  * SunLight (DistantLight)
  * IndoorLight (SphereLight)
  * Environment (Xform)
    * Materials (Scope)
      * industrialWindow_Small (Material)
        * pbr_shader (Shader)
        * uvset0 (Shader)
        * tex_base (Shader)
        * tex_metallic (Shader)
        * tex_roughness (Shader)
        * tex_normal (Shader)
      * industrialDoor (Material)
        * pbr_shader (Shader)
        * uvset0 (Shader)
        * tex_base (Shader)
        * tex_metallic (Shader)
        * tex_roughness (Shader)
        * tex_normal (Shader)
      * Atlas_2048x2048_01 (Material)
        * pbr_shader (Shader)
        * uvset0 (Shader)
        * tex_base (Shader)
        * tex_metallic (Shader)
        * tex_roughness (Shader)
        * tex_normal (Shader)
      * decalMoss01 (Material)
        * pbr_shader (Shader)
        * uvset0 (Shader)
        * tex_base (Shader)
      * woodenFence (Material)
        * pbr_shader (Shader)
        * uvset0 (Shader)
        * tex_base (Shader)
        * tex_metallic (Shader)
        * tex_roughness (Shader)
        * tex_normal (Shader)
      * eletricBox_001 (Material)
        * pbr_shader (Shader)
        * uvset0 (Shader)
        * tex_base (Shader)
        * tex_metallic (Shader)
        * tex_roughness (Shader)
        * tex_normal (Shader)
      * air_conditioning_001 (Material)
        * pbr_shader (Shader)
        * uvset0 (Shader)
        * tex_base (Shader)
        * tex_metallic (Shader)
        * tex_roughness (Shader)
        * tex_normal (Shader)
      * vents (Material)
        * pbr_shader (Shader)
        * uvset0 (Shader)
        * tex_base (Shader)
        * tex_metallic (Shader)
        * tex_roughness (Shader)
      * roofingSheets (Material)
        * pbr_shader (Shader)
        * uvset0 (Shader)
        * tex_base (Shader)
        * tex_metallic (Shader)
        * tex_roughness (Shader)
        * tex_normal (Shader)
      * emptyBillboard (Material)
        * pbr_shader (Shader)
        * uvset0 (Shader)
        * tex_base (Shader)
    * Meshes (Xform)
      * Sketchfab_model (Xform)
        * b63827acdd174d9a8e1e6ab96b34b9f7_fbx (Xform)
          * RootNode (Xform)
            * industrialWindow_Small (Xform)
              * industrialWindow_Small_industrialWindow_Small_0 (Xform)
                * industrialWindow_Small_industrialWindow_Small_0 (Mesh)
            * industrialWindow_Small_001 (Xform)
              * industrialWindow_Small_001_industrialWindow_Small_0 (Xform)
                * industrialWindow_Small_001_industrialWindow_Small_0 (Mesh)
            * industrialWindow_Small_002 (Xform)
              * industrialWindow_Small_002_industrialWindow_Small_0 (Xform)
                * industrialWindow_Small_002_industrialWindow_Small_0 (Mesh)
            * industrialWindow_Small_003 (Xform)
              * industrialWindow_Small_003_industrialWindow_Small_0 (Xform)
                * industrialWindow_Small_003_industrialWindow_Small_0 (Mesh)
            * industrialWindow_Small_004 (Xform)
              * industrialWindow_Small_004_industrialWindow_Small_0 (Xform)
                * industrialWindow_Small_004_industrialWindow_Small_0 (Mesh)
            * industrialWindow_Small_005 (Xform)
              * industrialWindow_Small_005_industrialWindow_Small_0 (Xform)
                * industrialWindow_Small_005_industrialWindow_Small_0 (Mesh)
            * industrialWindow_Small_006 (Xform)
              * industrialWindow_Small_006_industrialWindow_Small_0 (Xform)
                * industrialWindow_Small_006_industrialWindow_Small_0 (Mesh)
            * industrialWindow_Small_007 (Xform)
              * industrialWindow_Small_007_industrialWindow_Small_0 (Xform)
                * industrialWindow_Small_007_industrialWindow_Small_0 (Mesh)
            * industrialWindow_Small_008 (Xform)
              * industrialWindow_Small_008_industrialWindow_Small_0 (Xform)
                * industrialWindow_Small_008_industrialWindow_Small_0 (Mesh)
            * industrialWindow_Small_009 (Xform)
              * industrialWindow_Small_009_industrialWindow_Small_0 (Xform)
                * industrialWindow_Small_009_industrialWindow_Small_0 (Mesh)
            * industrialWindow_Small_010 (Xform)
              * industrialWindow_Small_010_industrialWindow_Small_0 (Xform)
                * industrialWindow_Small_010_industrialWindow_Small_0 (Mesh)
            * industrialWindow_Small_011 (Xform)
              * industrialWindow_Small_011_industrialWindow_Small_0 (Xform)
                * industrialWindow_Small_011_industrialWindow_Small_0 (Mesh)
            * industrialWindow_Small_012 (Xform)
              * industrialWindow_Small_012_industrialWindow_Small_0 (Xform)
                * industrialWindow_Small_012_industrialWindow_Small_0 (Mesh)
            * industrialWindow_Small_013 (Xform)
              * industrialWindow_Small_013_industrialWindow_Small_0 (Xform)
                * industrialWindow_Small_013_industrialWindow_Small_0 (Mesh)
            * industrialWindow_Small_014 (Xform)
              * industrialWindow_Small_014_industrialWindow_Small_0 (Xform)
                * industrialWindow_Small_014_industrialWindow_Small_0 (Mesh)
            * industrialDoor (Xform)
              * industrialDoor_industrialDoor_0 (Xform)
                * industrialDoor_industrialDoor_0 (Mesh)
            * concreteStairs (Xform)
              * concreteStairs_Atlas_2048x2048_01_0 (Xform)
                * concreteStairs_Atlas_2048x2048_01_0 (Mesh)
            * buildingMainwalls (Xform)
              * buildingMainwalls_Atlas_2048x2048_01_0 (Xform)
                * buildingMainwalls_Atlas_2048x2048_01_0 (Mesh)
            * wallbaseboard (Xform)
              * wallbaseboard_Atlas_2048x2048_01_0 (Xform)
                * wallbaseboard_Atlas_2048x2048_01_0 (Mesh)
            * metalFrame (Xform)
              * metalFrame_Atlas_2048x2048_01_0 (Xform)
                * metalFrame_Atlas_2048x2048_01_0 (Mesh)
            * mossDecal (Xform)
              * mossDecal_decalMoss01_0 (Xform)
                * mossDecal_decalMoss01_0 (Mesh)
            * building_Roof (Xform)
              * building_Roof_Atlas_2048x2048_01_0 (Xform)
                * building_Roof_Atlas_2048x2048_01_0 (Mesh)
            * woodenFenceType_02 (Xform)
              * woodenFenceType_02_woodenFence_0 (Xform)
                * woodenFenceType_02_woodenFence_0 (Mesh)
            * woodenFenceType_01 (Xform)
              * woodenFenceType_01_woodenFence_0 (Xform)
                * woodenFenceType_01_woodenFence_0 (Mesh)
            * woodenFenceType_02_001 (Xform)
              * woodenFenceType_02_001_woodenFence_0 (Xform)
                * woodenFenceType_02_001_woodenFence_0 (Mesh)
            * eletricBox_Low_001 (Xform)
              * eletricBox_Low_001_eletricBox_001_0 (Xform)
                * eletricBox_Low_001_eletricBox_001_0 (Mesh)
            * eletricBox_Low_002 (Xform)
              * eletricBox_Low_002_eletricBox_001_0 (Xform)
                * eletricBox_Low_002_eletricBox_001_0 (Mesh)
            * airconditioning_Low_002 (Xform)
              * airconditioning_Low_002_air_conditioning_001_0 (Xform)
                * airconditioning_Low_002_air_conditioning_001_0 (Mesh)
            * airconditioningBraket_002 (Xform)
              * airconditioningBraket_002_air_conditioning_001_0 (Xform)
                * airconditioningBraket_002_air_conditioning_001_0 (Mesh)
            * airconditioning_Low_003 (Xform)
              * airconditioning_Low_003_air_conditioning_001_0 (Xform)
                * airconditioning_Low_003_air_conditioning_001_0 (Mesh)
            * airconditioningBraket_003 (Xform)
              * airconditioningBraket_003_air_conditioning_001_0 (Xform)
                * airconditioningBraket_003_air_conditioning_001_0 (Mesh)
            * vents (Xform)
              * vents_vents_0 (Xform)
                * vents_vents_0 (Mesh)
            * vents_001 (Xform)
              * vents_001_vents_0 (Xform)
                * vents_001_vents_0 (Mesh)
            * vents_002 (Xform)
              * vents_002_vents_0 (Xform)
                * vents_002_vents_0 (Mesh)
            * metalBeams (Xform)
              * metalBeams_roofingSheets_0 (Xform)
                * metalBeams_roofingSheets_0 (Mesh)
            * metalSheet (Xform)
              * metalSheet_roofingSheets_0 (Xform)
                * metalSheet_roofingSheets_0 (Mesh)
            * metalSheet_001 (Xform)
              * metalSheet_001_roofingSheets_0 (Xform)
                * metalSheet_001_roofingSheets_0 (Mesh)
            * metalSheet_002 (Xform)
              * metalSheet_002_roofingSheets_0 (Xform)
                * metalSheet_002_roofingSheets_0 (Mesh)
            * metalSheet_003 (Xform)
              * metalSheet_003_roofingSheets_0 (Xform)
                * metalSheet_003_roofingSheets_0 (Mesh)
            * emptyBillboard (Xform)
              * emptyBillboard_emptyBillboard_0 (Xform)
                * emptyBillboard_emptyBillboard_0 (Mesh)
            * emptyBillboard_001 (Xform)
              * emptyBillboard_001_emptyBillboard_0 (Xform)
                * emptyBillboard_001_emptyBillboard_0 (Mesh)
  * Workbench_1 (Xform)
    * SM_MetalWorktable_A12_01 (Mesh)
      * M_MetalWorktable_A01_Body (GeomSubset)
      * M_MetalWorktable_A01_BoltsRailsLosk (GeomSubset)
      * M_MetalWorktable_A01_Legs (GeomSubset)
      * M_MetalWorktable_A01_Table (GeomSubset)
      * SM_MetalWorktable_A12_Locker_01 (Mesh)
        * M_MetalWorktable_A01_Body (GeomSubset)
        * M_MetalWorktable_A01_BoltsRailsLosk (GeomSubset)
    * Looks (Scope)
      * Metal_Glossy_A_MetalWorktable_A (Material)
        * Shader (Shader)
      * MetalPainted_Gray_Glossy_A_MetalWorktable_A (Material)
        * Shader (Shader)
      * Plastic_Black_A_MetalWorktable_A (Material)
        * Shader (Shader)
      * Wood_Maple_MetalWorktable_A (Material)
        * Shader (Shader)
  * Workbench_2 (Xform)
    * SM_MetalWorktable_A12_01 (Mesh)
      * M_MetalWorktable_A01_Body (GeomSubset)
      * M_MetalWorktable_A01_BoltsRailsLosk (GeomSubset)
      * M_MetalWorktable_A01_Legs (GeomSubset)
      * M_MetalWorktable_A01_Table (GeomSubset)
      * SM_MetalWorktable_A12_Locker_01 (Mesh)
        * M_MetalWorktable_A01_Body (GeomSubset)
        * M_MetalWorktable_A01_BoltsRailsLosk (GeomSubset)
    * Looks (Scope)
      * Metal_Glossy_A_MetalWorktable_A (Material)
        * Shader (Shader)
      * MetalPainted_Gray_Glossy_A_MetalWorktable_A (Material)
        * Shader (Shader)
      * Plastic_Black_A_MetalWorktable_A (Material)
        * Shader (Shader)
      * Wood_Maple_MetalWorktable_A (Material)
        * Shader (Shader)
  * Workbench_3 (Xform)
    * SM_MetalWorktable_A12_01 (Mesh)
      * M_MetalWorktable_A01_Body (GeomSubset)
      * M_MetalWorktable_A01_BoltsRailsLosk (GeomSubset)
      * M_MetalWorktable_A01_Legs (GeomSubset)
      * M_MetalWorktable_A01_Table (GeomSubset)
      * SM_MetalWorktable_A12_Locker_01 (Mesh)
        * M_MetalWorktable_A01_Body (GeomSubset)
        * M_MetalWorktable_A01_BoltsRailsLosk (GeomSubset)
    * Looks (Scope)
      * Metal_Glossy_A_MetalWorktable_A (Material)
        * Shader (Shader)
      * MetalPainted_Gray_Glossy_A_MetalWorktable_A (Material)
        * Shader (Shader)
      * Plastic_Black_A_MetalWorktable_A (Material)
        * Shader (Shader)
      * Wood_Maple_MetalWorktable_A (Material)
        * Shader (Shader)
  * Workbench_4 (Xform)
    * SM_MetalWorktable_A12_01 (Mesh)
      * M_MetalWorktable_A01_Body (GeomSubset)
      * M_MetalWorktable_A01_BoltsRailsLosk (GeomSubset)
      * M_MetalWorktable_A01_Legs (GeomSubset)
      * M_MetalWorktable_A01_Table (GeomSubset)
      * SM_MetalWorktable_A12_Locker_01 (Mesh)
        * M_MetalWorktable_A01_Body (GeomSubset)
        * M_MetalWorktable_A01_BoltsRailsLosk (GeomSubset)
    * Looks (Scope)
      * Metal_Glossy_A_MetalWorktable_A (Material)
        * Shader (Shader)
      * MetalPainted_Gray_Glossy_A_MetalWorktable_A (Material)
        * Shader (Shader)
      * Plastic_Black_A_MetalWorktable_A (Material)
        * Shader (Shader)
      * Wood_Maple_MetalWorktable_A (Material)
        * Shader (Shader)
  * Workbench_5 (Xform)
    * SM_MetalWorktable_A12_01 (Mesh)
      * M_MetalWorktable_A01_Body (GeomSubset)
      * M_MetalWorktable_A01_BoltsRailsLosk (GeomSubset)
      * M_MetalWorktable_A01_Legs (GeomSubset)
      * M_MetalWorktable_A01_Table (GeomSubset)
      * SM_MetalWorktable_A12_Locker_01 (Mesh)
        * M_MetalWorktable_A01_Body (GeomSubset)
        * M_MetalWorktable_A01_BoltsRailsLosk (GeomSubset)
    * Looks (Scope)
      * Metal_Glossy_A_MetalWorktable_A (Material)
        * Shader (Shader)
      * MetalPainted_Gray_Glossy_A_MetalWorktable_A (Material)
        * Shader (Shader)
      * Plastic_Black_A_MetalWorktable_A (Material)
        * Shader (Shader)
      * Wood_Maple_MetalWorktable_A (Material)
        * Shader (Shader)
  * Workbench_6 (Xform)
    * SM_MetalWorktable_A12_01 (Mesh)
      * M_MetalWorktable_A01_Body (GeomSubset)
      * M_MetalWorktable_A01_BoltsRailsLosk (GeomSubset)
      * M_MetalWorktable_A01_Legs (GeomSubset)
      * M_MetalWorktable_A01_Table (GeomSubset)
      * SM_MetalWorktable_A12_Locker_01 (Mesh)
        * M_MetalWorktable_A01_Body (GeomSubset)
        * M_MetalWorktable_A01_BoltsRailsLosk (GeomSubset)
    * Looks (Scope)
      * Metal_Glossy_A_MetalWorktable_A (Material)
        * Shader (Shader)
      * MetalPainted_Gray_Glossy_A_MetalWorktable_A (Material)
        * Shader (Shader)
      * Plastic_Black_A_MetalWorktable_A (Material)
        * Shader (Shader)
      * Wood_Maple_MetalWorktable_A (Material)
        * Shader (Shader)
  * Workbench_7 (Xform)
    * SM_MetalWorktable_A12_01 (Mesh)
      * M_MetalWorktable_A01_Body (GeomSubset)
      * M_MetalWorktable_A01_BoltsRailsLosk (GeomSubset)
      * M_MetalWorktable_A01_Legs (GeomSubset)
      * M_MetalWorktable_A01_Table (GeomSubset)
      * SM_MetalWorktable_A12_Locker_01 (Mesh)
        * M_MetalWorktable_A01_Body (GeomSubset)
        * M_MetalWorktable_A01_BoltsRailsLosk (GeomSubset)
    * Looks (Scope)
      * Metal_Glossy_A_MetalWorktable_A (Material)
        * Shader (Shader)
      * MetalPainted_Gray_Glossy_A_MetalWorktable_A (Material)
        * Shader (Shader)
      * Plastic_Black_A_MetalWorktable_A (Material)
        * Shader (Shader)
      * Wood_Maple_MetalWorktable_A (Material)
        * Shader (Shader)
  * Conveyor_1 (Xform)
    * Looks (Scope)
      * Acrylic_Clear_Glossy_A (Material)
        * Shader (Shader)
      * M_ConveyorBelt_A01_Belt (Material)
        * Shader (Shader)
      * M_ConveyorBelt_A01_Decal (Material)
        * Shader (Shader)
      * Metal_Rough_A (Material)
        * Shader (Shader)
      * MetalPainted_Black_Glossy_A (Material)
        * Shader (Shader)
      * MetalPainted_Blue_Glossy_A (Material)
        * Shader (Shader)
      * Plastic_Orange_A (Material)
        * Shader (Shader)
      * Plastic_Red_A (Material)
        * Shader (Shader)
      * Plastic_Rough_Black_A (Material)
        * Shader (Shader)
      * Steel_A (Material)
        * Shader (Shader)
    * SM_ConveyorBelt_A09_02 (Mesh)
      * M_ConveyorBelt_A01_Body_01 (GeomSubset)
      * M_ConveyorBelt_A01_Bolts_01 (GeomSubset)
      * M_ConveyorBelt_A01_Box_01 (GeomSubset)
      * M_ConveyorBelt_A01_Caps_01 (GeomSubset)
      * M_ConveyorBelt_A01_Engine_01 (GeomSubset)
      * M_ConveyorBelt_A01_FixBody_01 (GeomSubset)
      * M_ConveyorBelt_A01_Plate01_01 (GeomSubset)
      * M_ConveyorBelt_A01_Plate02_01 (GeomSubset)
      * M_ConveyorBelt_A01_Sheets_01 (GeomSubset)
      * M_ConveyorBelt_A01_WirePipes_01 (GeomSubset)
    * SM_ConveyorBelt_A09_Decal_02 (Mesh)
    * Belt (Xform)
      * SM_ConveyorBelt_A09_Belt_02 (Mesh)
    * Anchorpoint (Xform)
  * Conveyor_2 (Xform)
    * Looks (Scope)
      * Acrylic_Clear_Glossy_A (Material)
        * Shader (Shader)
      * M_ConveyorBelt_A01_Belt (Material)
        * Shader (Shader)
      * M_ConveyorBelt_A01_Decal (Material)
        * Shader (Shader)
      * Metal_Rough_A (Material)
        * Shader (Shader)
      * MetalPainted_Black_Glossy_A (Material)
        * Shader (Shader)
      * MetalPainted_Blue_Glossy_A (Material)
        * Shader (Shader)
      * Plastic_Orange_A (Material)
        * Shader (Shader)
      * Plastic_Red_A (Material)
        * Shader (Shader)
      * Plastic_Rough_Black_A (Material)
        * Shader (Shader)
      * Steel_A (Material)
        * Shader (Shader)
    * SM_ConveyorBelt_A09_02 (Mesh)
      * M_ConveyorBelt_A01_Body_01 (GeomSubset)
      * M_ConveyorBelt_A01_Bolts_01 (GeomSubset)
      * M_ConveyorBelt_A01_Box_01 (GeomSubset)
      * M_ConveyorBelt_A01_Caps_01 (GeomSubset)
      * M_ConveyorBelt_A01_Engine_01 (GeomSubset)
      * M_ConveyorBelt_A01_FixBody_01 (GeomSubset)
      * M_ConveyorBelt_A01_Plate01_01 (GeomSubset)
      * M_ConveyorBelt_A01_Plate02_01 (GeomSubset)
      * M_ConveyorBelt_A01_Sheets_01 (GeomSubset)
      * M_ConveyorBelt_A01_WirePipes_01 (GeomSubset)
    * SM_ConveyorBelt_A09_Decal_02 (Mesh)
    * Belt (Xform)
      * SM_ConveyorBelt_A09_Belt_02 (Mesh)
    * Anchorpoint (Xform)
  * Conveyor_3 (Xform)
    * Looks (Scope)
      * Acrylic_Clear_Glossy_A (Material)
        * Shader (Shader)
      * M_ConveyorBelt_A01_Belt (Material)
        * Shader (Shader)
      * M_ConveyorBelt_A01_Decal (Material)
        * Shader (Shader)
      * Metal_Rough_A (Material)
        * Shader (Shader)
      * MetalPainted_Black_Glossy_A (Material)
        * Shader (Shader)
      * MetalPainted_Blue_Glossy_A (Material)
        * Shader (Shader)
      * Plastic_Orange_A (Material)
        * Shader (Shader)
      * Plastic_Red_A (Material)
        * Shader (Shader)
      * Plastic_Rough_Black_A (Material)
        * Shader (Shader)
      * Steel_A (Material)
        * Shader (Shader)
    * SM_ConveyorBelt_A09_02 (Mesh)
      * M_ConveyorBelt_A01_Body_01 (GeomSubset)
      * M_ConveyorBelt_A01_Bolts_01 (GeomSubset)
      * M_ConveyorBelt_A01_Box_01 (GeomSubset)
      * M_ConveyorBelt_A01_Caps_01 (GeomSubset)
      * M_ConveyorBelt_A01_Engine_01 (GeomSubset)
      * M_ConveyorBelt_A01_FixBody_01 (GeomSubset)
      * M_ConveyorBelt_A01_Plate01_01 (GeomSubset)
      * M_ConveyorBelt_A01_Plate02_01 (GeomSubset)
      * M_ConveyorBelt_A01_Sheets_01 (GeomSubset)
      * M_ConveyorBelt_A01_WirePipes_01 (GeomSubset)
    * SM_ConveyorBelt_A09_Decal_02 (Mesh)
    * Belt (Xform)
      * SM_ConveyorBelt_A09_Belt_02 (Mesh)
    * Anchorpoint (Xform)
  * Conveyor_4 (Xform)
    * Looks (Scope)
      * Acrylic_Clear_Glossy_A (Material)
        * Shader (Shader)
      * M_ConveyorBelt_A01_Belt (Material)
        * Shader (Shader)
      * M_ConveyorBelt_A01_Decal (Material)
        * Shader (Shader)
      * Metal_Rough_A (Material)
        * Shader (Shader)
      * MetalPainted_Black_Glossy_A (Material)
        * Shader (Shader)
      * MetalPainted_Blue_Glossy_A (Material)
        * Shader (Shader)
      * Plastic_Orange_A (Material)
        * Shader (Shader)
      * Plastic_Red_A (Material)
        * Shader (Shader)
      * Plastic_Rough_Black_A (Material)
        * Shader (Shader)
      * Steel_A (Material)
        * Shader (Shader)
    * SM_ConveyorBelt_A09_02 (Mesh)
      * M_ConveyorBelt_A01_Body_01 (GeomSubset)
      * M_ConveyorBelt_A01_Bolts_01 (GeomSubset)
      * M_ConveyorBelt_A01_Box_01 (GeomSubset)
      * M_ConveyorBelt_A01_Caps_01 (GeomSubset)
      * M_ConveyorBelt_A01_Engine_01 (GeomSubset)
      * M_ConveyorBelt_A01_FixBody_01 (GeomSubset)
      * M_ConveyorBelt_A01_Plate01_01 (GeomSubset)
      * M_ConveyorBelt_A01_Plate02_01 (GeomSubset)
      * M_ConveyorBelt_A01_Sheets_01 (GeomSubset)
      * M_ConveyorBelt_A01_WirePipes_01 (GeomSubset)
    * SM_ConveyorBelt_A09_Decal_02 (Mesh)
    * Belt (Xform)
      * SM_ConveyorBelt_A09_Belt_02 (Mesh)
    * Anchorpoint (Xform)
  * Conveyor_5 (Xform)
    * Looks (Scope)
      * Acrylic_Clear_Glossy_A (Material)
        * Shader (Shader)
      * M_ConveyorBelt_A01_Belt (Material)
        * Shader (Shader)
      * M_ConveyorBelt_A01_Decal (Material)
        * Shader (Shader)
      * Metal_Rough_A (Material)
        * Shader (Shader)
      * MetalPainted_Black_Glossy_A (Material)
        * Shader (Shader)
      * MetalPainted_Blue_Glossy_A (Material)
        * Shader (Shader)
      * Plastic_Orange_A (Material)
        * Shader (Shader)
      * Plastic_Red_A (Material)
        * Shader (Shader)
      * Plastic_Rough_Black_A (Material)
        * Shader (Shader)
      * Steel_A (Material)
        * Shader (Shader)
    * SM_ConveyorBelt_A09_02 (Mesh)
      * M_ConveyorBelt_A01_Body_01 (GeomSubset)
      * M_ConveyorBelt_A01_Bolts_01 (GeomSubset)
      * M_ConveyorBelt_A01_Box_01 (GeomSubset)
      * M_ConveyorBelt_A01_Caps_01 (GeomSubset)
      * M_ConveyorBelt_A01_Engine_01 (GeomSubset)
      * M_ConveyorBelt_A01_FixBody_01 (GeomSubset)
      * M_ConveyorBelt_A01_Plate01_01 (GeomSubset)
      * M_ConveyorBelt_A01_Plate02_01 (GeomSubset)
      * M_ConveyorBelt_A01_Sheets_01 (GeomSubset)
      * M_ConveyorBelt_A01_WirePipes_01 (GeomSubset)
    * SM_ConveyorBelt_A09_Decal_02 (Mesh)
    * Belt (Xform)
      * SM_ConveyorBelt_A09_Belt_02 (Mesh)
    * Anchorpoint (Xform)
  * Conveyor_6 (Xform)
    * Looks (Scope)
      * Acrylic_Clear_Glossy_A (Material)
        * Shader (Shader)
      * M_ConveyorBelt_A01_Belt (Material)
        * Shader (Shader)
      * M_ConveyorBelt_A01_Decal (Material)
        * Shader (Shader)
      * Metal_Rough_A (Material)
        * Shader (Shader)
      * MetalPainted_Black_Glossy_A (Material)
        * Shader (Shader)
      * MetalPainted_Blue_Glossy_A (Material)
        * Shader (Shader)
      * Plastic_Orange_A (Material)
        * Shader (Shader)
      * Plastic_Red_A (Material)
        * Shader (Shader)
      * Plastic_Rough_Black_A (Material)
        * Shader (Shader)
      * Steel_A (Material)
        * Shader (Shader)
    * SM_ConveyorBelt_A09_02 (Mesh)
      * M_ConveyorBelt_A01_Body_01 (GeomSubset)
      * M_ConveyorBelt_A01_Bolts_01 (GeomSubset)
      * M_ConveyorBelt_A01_Box_01 (GeomSubset)
      * M_ConveyorBelt_A01_Caps_01 (GeomSubset)
      * M_ConveyorBelt_A01_Engine_01 (GeomSubset)
      * M_ConveyorBelt_A01_FixBody_01 (GeomSubset)
      * M_ConveyorBelt_A01_Plate01_01 (GeomSubset)
      * M_ConveyorBelt_A01_Plate02_01 (GeomSubset)
      * M_ConveyorBelt_A01_Sheets_01 (GeomSubset)
      * M_ConveyorBelt_A01_WirePipes_01 (GeomSubset)
    * SM_ConveyorBelt_A09_Decal_02 (Mesh)
    * Belt (Xform)
      * SM_ConveyorBelt_A09_Belt_02 (Mesh)
    * Anchorpoint (Xform)
  * Conveyor_7 (Xform)
    * Looks (Scope)
      * Acrylic_Clear_Glossy_A (Material)
        * Shader (Shader)
      * M_ConveyorBelt_A01_Belt (Material)
        * Shader (Shader)
      * M_ConveyorBelt_A01_Decal (Material)
        * Shader (Shader)
      * Metal_Rough_A (Material)
        * Shader (Shader)
      * MetalPainted_Black_Glossy_A (Material)
        * Shader (Shader)
      * MetalPainted_Blue_Glossy_A (Material)
        * Shader (Shader)
      * Plastic_Orange_A (Material)
        * Shader (Shader)
      * Plastic_Red_A (Material)
        * Shader (Shader)
      * Plastic_Rough_Black_A (Material)
        * Shader (Shader)
      * Steel_A (Material)
        * Shader (Shader)
    * SM_ConveyorBelt_A09_02 (Mesh)
      * M_ConveyorBelt_A01_Body_01 (GeomSubset)
      * M_ConveyorBelt_A01_Bolts_01 (GeomSubset)
      * M_ConveyorBelt_A01_Box_01 (GeomSubset)
      * M_ConveyorBelt_A01_Caps_01 (GeomSubset)
      * M_ConveyorBelt_A01_Engine_01 (GeomSubset)
      * M_ConveyorBelt_A01_FixBody_01 (GeomSubset)
      * M_ConveyorBelt_A01_Plate01_01 (GeomSubset)
      * M_ConveyorBelt_A01_Plate02_01 (GeomSubset)
      * M_ConveyorBelt_A01_Sheets_01 (GeomSubset)
      * M_ConveyorBelt_A01_WirePipes_01 (GeomSubset)
    * SM_ConveyorBelt_A09_Decal_02 (Mesh)
    * Belt (Xform)
      * SM_ConveyorBelt_A09_Belt_02 (Mesh)
    * Anchorpoint (Xform)
  * Conveyor_8 (Xform)
    * Looks (Scope)
      * Acrylic_Clear_Glossy_A (Material)
        * Shader (Shader)
      * M_ConveyorBelt_A01_Belt (Material)
        * Shader (Shader)
      * M_ConveyorBelt_A01_Decal (Material)
        * Shader (Shader)
      * Metal_Rough_A (Material)
        * Shader (Shader)
      * MetalPainted_Black_Glossy_A (Material)
        * Shader (Shader)
      * MetalPainted_Blue_Glossy_A (Material)
        * Shader (Shader)
      * Plastic_Orange_A (Material)
        * Shader (Shader)
      * Plastic_Red_A (Material)
        * Shader (Shader)
      * Plastic_Rough_Black_A (Material)
        * Shader (Shader)
      * Steel_A (Material)
        * Shader (Shader)
    * SM_ConveyorBelt_A09_02 (Mesh)
      * M_ConveyorBelt_A01_Body_01 (GeomSubset)
      * M_ConveyorBelt_A01_Bolts_01 (GeomSubset)
      * M_ConveyorBelt_A01_Box_01 (GeomSubset)
      * M_ConveyorBelt_A01_Caps_01 (GeomSubset)
      * M_ConveyorBelt_A01_Engine_01 (GeomSubset)
      * M_ConveyorBelt_A01_FixBody_01 (GeomSubset)
      * M_ConveyorBelt_A01_Plate01_01 (GeomSubset)
      * M_ConveyorBelt_A01_Plate02_01 (GeomSubset)
      * M_ConveyorBelt_A01_Sheets_01 (GeomSubset)
      * M_ConveyorBelt_A01_WirePipes_01 (GeomSubset)
    * SM_ConveyorBelt_A09_Decal_02 (Mesh)
    * Belt (Xform)
      * SM_ConveyorBelt_A09_Belt_02 (Mesh)
    * Anchorpoint (Xform)
  * Conveyor_9 (Xform)
    * Looks (Scope)
      * Acrylic_Clear_Glossy_A (Material)
        * Shader (Shader)
      * M_ConveyorBelt_A01_Belt (Material)
        * Shader (Shader)
      * M_ConveyorBelt_A01_Decal (Material)
        * Shader (Shader)
      * Metal_Rough_A (Material)
        * Shader (Shader)
      * MetalPainted_Black_Glossy_A (Material)
        * Shader (Shader)
      * MetalPainted_Blue_Glossy_A (Material)
        * Shader (Shader)
      * Plastic_Orange_A (Material)
        * Shader (Shader)
      * Plastic_Red_A (Material)
        * Shader (Shader)
      * Plastic_Rough_Black_A (Material)
        * Shader (Shader)
      * Steel_A (Material)
        * Shader (Shader)
    * SM_ConveyorBelt_A09_02 (Mesh)
      * M_ConveyorBelt_A01_Body_01 (GeomSubset)
      * M_ConveyorBelt_A01_Bolts_01 (GeomSubset)
      * M_ConveyorBelt_A01_Box_01 (GeomSubset)
      * M_ConveyorBelt_A01_Caps_01 (GeomSubset)
      * M_ConveyorBelt_A01_Engine_01 (GeomSubset)
      * M_ConveyorBelt_A01_FixBody_01 (GeomSubset)
      * M_ConveyorBelt_A01_Plate01_01 (GeomSubset)
      * M_ConveyorBelt_A01_Plate02_01 (GeomSubset)
      * M_ConveyorBelt_A01_Sheets_01 (GeomSubset)
      * M_ConveyorBelt_A01_WirePipes_01 (GeomSubset)
    * SM_ConveyorBelt_A09_Decal_02 (Mesh)
    * Belt (Xform)
      * SM_ConveyorBelt_A09_Belt_02 (Mesh)
    * Anchorpoint (Xform)
  * Conveyor_10 (Xform)
    * Looks (Scope)
      * Acrylic_Clear_Glossy_A (Material)
        * Shader (Shader)
      * M_ConveyorBelt_A01_Belt (Material)
        * Shader (Shader)
      * M_ConveyorBelt_A01_Decal (Material)
        * Shader (Shader)
      * Metal_Rough_A (Material)
        * Shader (Shader)
      * MetalPainted_Black_Glossy_A (Material)
        * Shader (Shader)
      * MetalPainted_Blue_Glossy_A (Material)
        * Shader (Shader)
      * Plastic_Orange_A (Material)
        * Shader (Shader)
      * Plastic_Red_A (Material)
        * Shader (Shader)
      * Plastic_Rough_Black_A (Material)
        * Shader (Shader)
      * Steel_A (Material)
        * Shader (Shader)
    * SM_ConveyorBelt_A09_02 (Mesh)
      * M_ConveyorBelt_A01_Body_01 (GeomSubset)
      * M_ConveyorBelt_A01_Bolts_01 (GeomSubset)
      * M_ConveyorBelt_A01_Box_01 (GeomSubset)
      * M_ConveyorBelt_A01_Caps_01 (GeomSubset)
      * M_ConveyorBelt_A01_Engine_01 (GeomSubset)
      * M_ConveyorBelt_A01_FixBody_01 (GeomSubset)
      * M_ConveyorBelt_A01_Plate01_01 (GeomSubset)
      * M_ConveyorBelt_A01_Plate02_01 (GeomSubset)
      * M_ConveyorBelt_A01_Sheets_01 (GeomSubset)
      * M_ConveyorBelt_A01_WirePipes_01 (GeomSubset)
    * SM_ConveyorBelt_A09_Decal_02 (Mesh)
    * Belt (Xform)
      * SM_ConveyorBelt_A09_Belt_02 (Mesh)
    * Anchorpoint (Xform)
  * Conveyor_11 (Xform)
    * Looks (Scope)
      * Acrylic_Clear_Glossy_A (Material)
        * Shader (Shader)
      * M_ConveyorBelt_A01_Belt (Material)
        * Shader (Shader)
      * M_ConveyorBelt_A01_Decal (Material)
        * Shader (Shader)
      * Metal_Rough_A (Material)
        * Shader (Shader)
      * MetalPainted_Black_Glossy_A (Material)
        * Shader (Shader)
      * MetalPainted_Blue_Glossy_A (Material)
        * Shader (Shader)
      * Plastic_Orange_A (Material)
        * Shader (Shader)
      * Plastic_Red_A (Material)
        * Shader (Shader)
      * Plastic_Rough_Black_A (Material)
        * Shader (Shader)
      * Steel_A (Material)
        * Shader (Shader)
    * SM_ConveyorBelt_A09_02 (Mesh)
      * M_ConveyorBelt_A01_Body_01 (GeomSubset)
      * M_ConveyorBelt_A01_Bolts_01 (GeomSubset)
      * M_ConveyorBelt_A01_Box_01 (GeomSubset)
      * M_ConveyorBelt_A01_Caps_01 (GeomSubset)
      * M_ConveyorBelt_A01_Engine_01 (GeomSubset)
      * M_ConveyorBelt_A01_FixBody_01 (GeomSubset)
      * M_ConveyorBelt_A01_Plate01_01 (GeomSubset)
      * M_ConveyorBelt_A01_Plate02_01 (GeomSubset)
      * M_ConveyorBelt_A01_Sheets_01 (GeomSubset)
      * M_ConveyorBelt_A01_WirePipes_01 (GeomSubset)
    * SM_ConveyorBelt_A09_Decal_02 (Mesh)
    * Belt (Xform)
      * SM_ConveyorBelt_A09_Belt_02 (Mesh)
    * Anchorpoint (Xform)
  * Conveyor_12 (Xform)
    * Looks (Scope)
      * Acrylic_Clear_Glossy_A (Material)
        * Shader (Shader)
      * M_ConveyorBelt_A01_Belt (Material)
        * Shader (Shader)
      * M_ConveyorBelt_A01_Decal (Material)
        * Shader (Shader)
      * Metal_Rough_A (Material)
        * Shader (Shader)
      * MetalPainted_Black_Glossy_A (Material)
        * Shader (Shader)
      * MetalPainted_Blue_Glossy_A (Material)
        * Shader (Shader)
      * Plastic_Orange_A (Material)
        * Shader (Shader)
      * Plastic_Red_A (Material)
        * Shader (Shader)
      * Plastic_Rough_Black_A (Material)
        * Shader (Shader)
      * Steel_A (Material)
        * Shader (Shader)
    * SM_ConveyorBelt_A09_02 (Mesh)
      * M_ConveyorBelt_A01_Body_01 (GeomSubset)
      * M_ConveyorBelt_A01_Bolts_01 (GeomSubset)
      * M_ConveyorBelt_A01_Box_01 (GeomSubset)
      * M_ConveyorBelt_A01_Caps_01 (GeomSubset)
      * M_ConveyorBelt_A01_Engine_01 (GeomSubset)
      * M_ConveyorBelt_A01_FixBody_01 (GeomSubset)
      * M_ConveyorBelt_A01_Plate01_01 (GeomSubset)
      * M_ConveyorBelt_A01_Plate02_01 (GeomSubset)
      * M_ConveyorBelt_A01_Sheets_01 (GeomSubset)
      * M_ConveyorBelt_A01_WirePipes_01 (GeomSubset)
    * SM_ConveyorBelt_A09_Decal_02 (Mesh)
    * Belt (Xform)
      * SM_ConveyorBelt_A09_Belt_02 (Mesh)
    * Anchorpoint (Xform)
  * Conveyor_13 (Xform)
    * Looks (Scope)
      * Acrylic_Clear_Glossy_A (Material)
        * Shader (Shader)
      * M_ConveyorBelt_A01_Belt (Material)
        * Shader (Shader)
      * M_ConveyorBelt_A01_Decal (Material)
        * Shader (Shader)
      * Metal_Rough_A (Material)
        * Shader (Shader)
      * MetalPainted_Black_Glossy_A (Material)
        * Shader (Shader)
      * MetalPainted_Blue_Glossy_A (Material)
        * Shader (Shader)
      * Plastic_Orange_A (Material)
        * Shader (Shader)
      * Plastic_Red_A (Material)
        * Shader (Shader)
      * Plastic_Rough_Black_A (Material)
        * Shader (Shader)
      * Steel_A (Material)
        * Shader (Shader)
    * SM_ConveyorBelt_A09_02 (Mesh)
      * M_ConveyorBelt_A01_Body_01 (GeomSubset)
      * M_ConveyorBelt_A01_Bolts_01 (GeomSubset)
      * M_ConveyorBelt_A01_Box_01 (GeomSubset)
      * M_ConveyorBelt_A01_Caps_01 (GeomSubset)
      * M_ConveyorBelt_A01_Engine_01 (GeomSubset)
      * M_ConveyorBelt_A01_FixBody_01 (GeomSubset)
      * M_ConveyorBelt_A01_Plate01_01 (GeomSubset)
      * M_ConveyorBelt_A01_Plate02_01 (GeomSubset)
      * M_ConveyorBelt_A01_Sheets_01 (GeomSubset)
      * M_ConveyorBelt_A01_WirePipes_01 (GeomSubset)
    * SM_ConveyorBelt_A09_Decal_02 (Mesh)
    * Belt (Xform)
      * SM_ConveyorBelt_A09_Belt_02 (Mesh)
    * Anchorpoint (Xform)
  * Conveyor_14 (Xform)
    * Looks (Scope)
      * Acrylic_Clear_Glossy_A (Material)
        * Shader (Shader)
      * M_ConveyorBelt_A01_Belt (Material)
        * Shader (Shader)
      * M_ConveyorBelt_A01_Decal (Material)
        * Shader (Shader)
      * Metal_Rough_A (Material)
        * Shader (Shader)
      * MetalPainted_Black_Glossy_A (Material)
        * Shader (Shader)
      * MetalPainted_Blue_Glossy_A (Material)
        * Shader (Shader)
      * Plastic_Orange_A (Material)
        * Shader (Shader)
      * Plastic_Red_A (Material)
        * Shader (Shader)
      * Plastic_Rough_Black_A (Material)
        * Shader (Shader)
      * Steel_A (Material)
        * Shader (Shader)
    * SM_ConveyorBelt_A09_02 (Mesh)
      * M_ConveyorBelt_A01_Body_01 (GeomSubset)
      * M_ConveyorBelt_A01_Bolts_01 (GeomSubset)
      * M_ConveyorBelt_A01_Box_01 (GeomSubset)
      * M_ConveyorBelt_A01_Caps_01 (GeomSubset)
      * M_ConveyorBelt_A01_Engine_01 (GeomSubset)
      * M_ConveyorBelt_A01_FixBody_01 (GeomSubset)
      * M_ConveyorBelt_A01_Plate01_01 (GeomSubset)
      * M_ConveyorBelt_A01_Plate02_01 (GeomSubset)
      * M_ConveyorBelt_A01_Sheets_01 (GeomSubset)
      * M_ConveyorBelt_A01_WirePipes_01 (GeomSubset)
    * SM_ConveyorBelt_A09_Decal_02 (Mesh)
    * Belt (Xform)
      * SM_ConveyorBelt_A09_Belt_02 (Mesh)
    * Anchorpoint (Xform)
  * Conveyor_15 (Xform)
    * Looks (Scope)
      * Acrylic_Clear_Glossy_A (Material)
        * Shader (Shader)
      * M_ConveyorBelt_A01_Belt (Material)
        * Shader (Shader)
      * M_ConveyorBelt_A01_Decal (Material)
        * Shader (Shader)
      * Metal_Rough_A (Material)
        * Shader (Shader)
      * MetalPainted_Black_Glossy_A (Material)
        * Shader (Shader)
      * MetalPainted_Blue_Glossy_A (Material)
        * Shader (Shader)
      * Plastic_Orange_A (Material)
        * Shader (Shader)
      * Plastic_Red_A (Material)
        * Shader (Shader)
      * Plastic_Rough_Black_A (Material)
        * Shader (Shader)
      * Steel_A (Material)
        * Shader (Shader)
    * SM_ConveyorBelt_A09_02 (Mesh)
      * M_ConveyorBelt_A01_Body_01 (GeomSubset)
      * M_ConveyorBelt_A01_Bolts_01 (GeomSubset)
      * M_ConveyorBelt_A01_Box_01 (GeomSubset)
      * M_ConveyorBelt_A01_Caps_01 (GeomSubset)
      * M_ConveyorBelt_A01_Engine_01 (GeomSubset)
      * M_ConveyorBelt_A01_FixBody_01 (GeomSubset)
      * M_ConveyorBelt_A01_Plate01_01 (GeomSubset)
      * M_ConveyorBelt_A01_Plate02_01 (GeomSubset)
      * M_ConveyorBelt_A01_Sheets_01 (GeomSubset)
      * M_ConveyorBelt_A01_WirePipes_01 (GeomSubset)
    * SM_ConveyorBelt_A09_Decal_02 (Mesh)
    * Belt (Xform)
      * SM_ConveyorBelt_A09_Belt_02 (Mesh)
    * Anchorpoint (Xform)
  * Conveyor_16 (Xform)
    * Looks (Scope)
      * Acrylic_Clear_Glossy_A (Material)
        * Shader (Shader)
      * M_ConveyorBelt_A01_Belt (Material)
        * Shader (Shader)
      * M_ConveyorBelt_A01_Decal (Material)
        * Shader (Shader)
      * Metal_Rough_A (Material)
        * Shader (Shader)
      * MetalPainted_Black_Glossy_A (Material)
        * Shader (Shader)
      * MetalPainted_Blue_Glossy_A (Material)
        * Shader (Shader)
      * Plastic_Orange_A (Material)
        * Shader (Shader)
      * Plastic_Red_A (Material)
        * Shader (Shader)
      * Plastic_Rough_Black_A (Material)
        * Shader (Shader)
      * Steel_A (Material)
        * Shader (Shader)
    * SM_ConveyorBelt_A09_02 (Mesh)
      * M_ConveyorBelt_A01_Body_01 (GeomSubset)
      * M_ConveyorBelt_A01_Bolts_01 (GeomSubset)
      * M_ConveyorBelt_A01_Box_01 (GeomSubset)
      * M_ConveyorBelt_A01_Caps_01 (GeomSubset)
      * M_ConveyorBelt_A01_Engine_01 (GeomSubset)
      * M_ConveyorBelt_A01_FixBody_01 (GeomSubset)
      * M_ConveyorBelt_A01_Plate01_01 (GeomSubset)
      * M_ConveyorBelt_A01_Plate02_01 (GeomSubset)
      * M_ConveyorBelt_A01_Sheets_01 (GeomSubset)
      * M_ConveyorBelt_A01_WirePipes_01 (GeomSubset)
    * SM_ConveyorBelt_A09_Decal_02 (Mesh)
    * Belt (Xform)
      * SM_ConveyorBelt_A09_Belt_02 (Mesh)
    * Anchorpoint (Xform)
  * Conveyor_17 (Xform)
    * Looks (Scope)
      * Acrylic_Clear_Glossy_A (Material)
        * Shader (Shader)
      * M_ConveyorBelt_A01_Belt (Material)
        * Shader (Shader)
      * M_ConveyorBelt_A01_Decal (Material)
        * Shader (Shader)
      * Metal_Rough_A (Material)
        * Shader (Shader)
      * MetalPainted_Black_Glossy_A (Material)
        * Shader (Shader)
      * MetalPainted_Blue_Glossy_A (Material)
        * Shader (Shader)
      * Plastic_Orange_A (Material)
        * Shader (Shader)
      * Plastic_Red_A (Material)
        * Shader (Shader)
      * Plastic_Rough_Black_A (Material)
        * Shader (Shader)
      * Steel_A (Material)
        * Shader (Shader)
    * SM_ConveyorBelt_A09_02 (Mesh)
      * M_ConveyorBelt_A01_Body_01 (GeomSubset)
      * M_ConveyorBelt_A01_Bolts_01 (GeomSubset)
      * M_ConveyorBelt_A01_Box_01 (GeomSubset)
      * M_ConveyorBelt_A01_Caps_01 (GeomSubset)
      * M_ConveyorBelt_A01_Engine_01 (GeomSubset)
      * M_ConveyorBelt_A01_FixBody_01 (GeomSubset)
      * M_ConveyorBelt_A01_Plate01_01 (GeomSubset)
      * M_ConveyorBelt_A01_Plate02_01 (GeomSubset)
      * M_ConveyorBelt_A01_Sheets_01 (GeomSubset)
      * M_ConveyorBelt_A01_WirePipes_01 (GeomSubset)
    * SM_ConveyorBelt_A09_Decal_02 (Mesh)
    * Belt (Xform)
      * SM_ConveyorBelt_A09_Belt_02 (Mesh)
    * Anchorpoint (Xform)
  * Conveyor_18 (Xform)
    * Looks (Scope)
      * Acrylic_Clear_Glossy_A (Material)
        * Shader (Shader)
      * M_ConveyorBelt_A01_Belt (Material)
        * Shader (Shader)
      * M_ConveyorBelt_A01_Decal (Material)
        * Shader (Shader)
      * Metal_Rough_A (Material)
        * Shader (Shader)
      * MetalPainted_Black_Glossy_A (Material)
        * Shader (Shader)
      * MetalPainted_Blue_Glossy_A (Material)
        * Shader (Shader)
      * Plastic_Orange_A (Material)
        * Shader (Shader)
      * Plastic_Red_A (Material)
        * Shader (Shader)
      * Plastic_Rough_Black_A (Material)
        * Shader (Shader)
      * Steel_A (Material)
        * Shader (Shader)
    * SM_ConveyorBelt_A09_02 (Mesh)
      * M_ConveyorBelt_A01_Body_01 (GeomSubset)
      * M_ConveyorBelt_A01_Bolts_01 (GeomSubset)
      * M_ConveyorBelt_A01_Box_01 (GeomSubset)
      * M_ConveyorBelt_A01_Caps_01 (GeomSubset)
      * M_ConveyorBelt_A01_Engine_01 (GeomSubset)
      * M_ConveyorBelt_A01_FixBody_01 (GeomSubset)
      * M_ConveyorBelt_A01_Plate01_01 (GeomSubset)
      * M_ConveyorBelt_A01_Plate02_01 (GeomSubset)
      * M_ConveyorBelt_A01_Sheets_01 (GeomSubset)
      * M_ConveyorBelt_A01_WirePipes_01 (GeomSubset)
    * SM_ConveyorBelt_A09_Decal_02 (Mesh)
    * Belt (Xform)
      * SM_ConveyorBelt_A09_Belt_02 (Mesh)
    * Anchorpoint (Xform)
  * Conveyor_19 (Xform)
    * Looks (Scope)
      * Acrylic_Clear_Glossy_A (Material)
        * Shader (Shader)
      * M_ConveyorBelt_A01_Belt (Material)
        * Shader (Shader)
      * M_ConveyorBelt_A01_Decal (Material)
        * Shader (Shader)
      * Metal_Rough_A (Material)
        * Shader (Shader)
      * MetalPainted_Black_Glossy_A (Material)
        * Shader (Shader)
      * MetalPainted_Blue_Glossy_A (Material)
        * Shader (Shader)
      * Plastic_Orange_A (Material)
        * Shader (Shader)
      * Plastic_Red_A (Material)
        * Shader (Shader)
      * Plastic_Rough_Black_A (Material)
        * Shader (Shader)
      * Steel_A (Material)
        * Shader (Shader)
    * SM_ConveyorBelt_A09_02 (Mesh)
      * M_ConveyorBelt_A01_Body_01 (GeomSubset)
      * M_ConveyorBelt_A01_Bolts_01 (GeomSubset)
      * M_ConveyorBelt_A01_Box_01 (GeomSubset)
      * M_ConveyorBelt_A01_Caps_01 (GeomSubset)
      * M_ConveyorBelt_A01_Engine_01 (GeomSubset)
      * M_ConveyorBelt_A01_FixBody_01 (GeomSubset)
      * M_ConveyorBelt_A01_Plate01_01 (GeomSubset)
      * M_ConveyorBelt_A01_Plate02_01 (GeomSubset)
      * M_ConveyorBelt_A01_Sheets_01 (GeomSubset)
      * M_ConveyorBelt_A01_WirePipes_01 (GeomSubset)
    * SM_ConveyorBelt_A09_Decal_02 (Mesh)
    * Belt (Xform)
      * SM_ConveyorBelt_A09_Belt_02 (Mesh)
    * Anchorpoint (Xform)
  * Conveyor_20 (Xform)
    * Looks (Scope)
      * Acrylic_Clear_Glossy_A (Material)
        * Shader (Shader)
      * M_ConveyorBelt_A01_Belt (Material)
        * Shader (Shader)
      * M_ConveyorBelt_A01_Decal (Material)
        * Shader (Shader)
      * Metal_Rough_A (Material)
        * Shader (Shader)
      * MetalPainted_Black_Glossy_A (Material)
        * Shader (Shader)
      * MetalPainted_Blue_Glossy_A (Material)
        * Shader (Shader)
      * Plastic_Orange_A (Material)
        * Shader (Shader)
      * Plastic_Red_A (Material)
        * Shader (Shader)
      * Plastic_Rough_Black_A (Material)
        * Shader (Shader)
      * Steel_A (Material)
        * Shader (Shader)
    * SM_ConveyorBelt_A09_02 (Mesh)
      * M_ConveyorBelt_A01_Body_01 (GeomSubset)
      * M_ConveyorBelt_A01_Bolts_01 (GeomSubset)
      * M_ConveyorBelt_A01_Box_01 (GeomSubset)
      * M_ConveyorBelt_A01_Caps_01 (GeomSubset)
      * M_ConveyorBelt_A01_Engine_01 (GeomSubset)
      * M_ConveyorBelt_A01_FixBody_01 (GeomSubset)
      * M_ConveyorBelt_A01_Plate01_01 (GeomSubset)
      * M_ConveyorBelt_A01_Plate02_01 (GeomSubset)
      * M_ConveyorBelt_A01_Sheets_01 (GeomSubset)
      * M_ConveyorBelt_A01_WirePipes_01 (GeomSubset)
    * SM_ConveyorBelt_A09_Decal_02 (Mesh)
    * Belt (Xform)
      * SM_ConveyorBelt_A09_Belt_02 (Mesh)
    * Anchorpoint (Xform)
  * Conveyor_21 (Xform)
    * Looks (Scope)
      * Acrylic_Clear_Glossy_A (Material)
        * Shader (Shader)
      * M_ConveyorBelt_A01_Belt (Material)
        * Shader (Shader)
      * M_ConveyorBelt_A01_Decal (Material)
        * Shader (Shader)
      * Metal_Rough_A (Material)
        * Shader (Shader)
      * MetalPainted_Black_Glossy_A (Material)
        * Shader (Shader)
      * MetalPainted_Blue_Glossy_A (Material)
        * Shader (Shader)
      * Plastic_Orange_A (Material)
        * Shader (Shader)
      * Plastic_Red_A (Material)
        * Shader (Shader)
      * Plastic_Rough_Black_A (Material)
        * Shader (Shader)
      * Steel_A (Material)
        * Shader (Shader)
    * SM_ConveyorBelt_A09_02 (Mesh)
      * M_ConveyorBelt_A01_Body_01 (GeomSubset)
      * M_ConveyorBelt_A01_Bolts_01 (GeomSubset)
      * M_ConveyorBelt_A01_Box_01 (GeomSubset)
      * M_ConveyorBelt_A01_Caps_01 (GeomSubset)
      * M_ConveyorBelt_A01_Engine_01 (GeomSubset)
      * M_ConveyorBelt_A01_FixBody_01 (GeomSubset)
      * M_ConveyorBelt_A01_Plate01_01 (GeomSubset)
      * M_ConveyorBelt_A01_Plate02_01 (GeomSubset)
      * M_ConveyorBelt_A01_Sheets_01 (GeomSubset)
      * M_ConveyorBelt_A01_WirePipes_01 (GeomSubset)
    * SM_ConveyorBelt_A09_Decal_02 (Mesh)
    * Belt (Xform)
      * SM_ConveyorBelt_A09_Belt_02 (Mesh)
    * Anchorpoint (Xform)
  * Conveyor_22 (Xform)
    * Looks (Scope)
      * Acrylic_Clear_Glossy_A (Material)
        * Shader (Shader)
      * M_ConveyorBelt_A01_Belt (Material)
        * Shader (Shader)
      * M_ConveyorBelt_A01_Decal (Material)
        * Shader (Shader)
      * Metal_Rough_A (Material)
        * Shader (Shader)
      * MetalPainted_Black_Glossy_A (Material)
        * Shader (Shader)
      * MetalPainted_Blue_Glossy_A (Material)
        * Shader (Shader)
      * Plastic_Orange_A (Material)
        * Shader (Shader)
      * Plastic_Red_A (Material)
        * Shader (Shader)
      * Plastic_Rough_Black_A (Material)
        * Shader (Shader)
      * Steel_A (Material)
        * Shader (Shader)
    * SM_ConveyorBelt_A09_02 (Mesh)
      * M_ConveyorBelt_A01_Body_01 (GeomSubset)
      * M_ConveyorBelt_A01_Bolts_01 (GeomSubset)
      * M_ConveyorBelt_A01_Box_01 (GeomSubset)
      * M_ConveyorBelt_A01_Caps_01 (GeomSubset)
      * M_ConveyorBelt_A01_Engine_01 (GeomSubset)
      * M_ConveyorBelt_A01_FixBody_01 (GeomSubset)
      * M_ConveyorBelt_A01_Plate01_01 (GeomSubset)
      * M_ConveyorBelt_A01_Plate02_01 (GeomSubset)
      * M_ConveyorBelt_A01_Sheets_01 (GeomSubset)
      * M_ConveyorBelt_A01_WirePipes_01 (GeomSubset)
    * SM_ConveyorBelt_A09_Decal_02 (Mesh)
    * Belt (Xform)
      * SM_ConveyorBelt_A09_Belt_02 (Mesh)
    * Anchorpoint (Xform)
  * Conveyor_23 (Xform)
    * Looks (Scope)
      * Acrylic_Clear_Glossy_A (Material)
        * Shader (Shader)
      * M_ConveyorBelt_A01_Belt (Material)
        * Shader (Shader)
      * M_ConveyorBelt_A01_Decal (Material)
        * Shader (Shader)
      * Metal_Rough_A (Material)
        * Shader (Shader)
      * MetalPainted_Black_Glossy_A (Material)
        * Shader (Shader)
      * MetalPainted_Blue_Glossy_A (Material)
        * Shader (Shader)
      * Plastic_Orange_A (Material)
        * Shader (Shader)
      * Plastic_Red_A (Material)
        * Shader (Shader)
      * Plastic_Rough_Black_A (Material)
        * Shader (Shader)
      * Steel_A (Material)
        * Shader (Shader)
    * SM_ConveyorBelt_A09_02 (Mesh)
      * M_ConveyorBelt_A01_Body_01 (GeomSubset)
      * M_ConveyorBelt_A01_Bolts_01 (GeomSubset)
      * M_ConveyorBelt_A01_Box_01 (GeomSubset)
      * M_ConveyorBelt_A01_Caps_01 (GeomSubset)
      * M_ConveyorBelt_A01_Engine_01 (GeomSubset)
      * M_ConveyorBelt_A01_FixBody_01 (GeomSubset)
      * M_ConveyorBelt_A01_Plate01_01 (GeomSubset)
      * M_ConveyorBelt_A01_Plate02_01 (GeomSubset)
      * M_ConveyorBelt_A01_Sheets_01 (GeomSubset)
      * M_ConveyorBelt_A01_WirePipes_01 (GeomSubset)
    * SM_ConveyorBelt_A09_Decal_02 (Mesh)
    * Belt (Xform)
      * SM_ConveyorBelt_A09_Belt_02 (Mesh)
    * Anchorpoint (Xform)
  * Conveyor_24 (Xform)
    * Looks (Scope)
      * Acrylic_Clear_Glossy_A (Material)
        * Shader (Shader)
      * M_ConveyorBelt_A01_Belt (Material)
        * Shader (Shader)
      * M_ConveyorBelt_A01_Decal (Material)
        * Shader (Shader)
      * Metal_Rough_A (Material)
        * Shader (Shader)
      * MetalPainted_Black_Glossy_A (Material)
        * Shader (Shader)
      * MetalPainted_Blue_Glossy_A (Material)
        * Shader (Shader)
      * Plastic_Orange_A (Material)
        * Shader (Shader)
      * Plastic_Red_A (Material)
        * Shader (Shader)
      * Plastic_Rough_Black_A (Material)
        * Shader (Shader)
      * Steel_A (Material)
        * Shader (Shader)
    * SM_ConveyorBelt_A09_02 (Mesh)
      * M_ConveyorBelt_A01_Body_01 (GeomSubset)
      * M_ConveyorBelt_A01_Bolts_01 (GeomSubset)
      * M_ConveyorBelt_A01_Box_01 (GeomSubset)
      * M_ConveyorBelt_A01_Caps_01 (GeomSubset)
      * M_ConveyorBelt_A01_Engine_01 (GeomSubset)
      * M_ConveyorBelt_A01_FixBody_01 (GeomSubset)
      * M_ConveyorBelt_A01_Plate01_01 (GeomSubset)
      * M_ConveyorBelt_A01_Plate02_01 (GeomSubset)
      * M_ConveyorBelt_A01_Sheets_01 (GeomSubset)
      * M_ConveyorBelt_A01_WirePipes_01 (GeomSubset)
    * SM_ConveyorBelt_A09_Decal_02 (Mesh)
    * Belt (Xform)
      * SM_ConveyorBelt_A09_Belt_02 (Mesh)
    * Anchorpoint (Xform)
  * Conveyor_25 (Xform)
    * Looks (Scope)
      * Acrylic_Clear_Glossy_A (Material)
        * Shader (Shader)
      * M_ConveyorBelt_A01_Belt (Material)
        * Shader (Shader)
      * M_ConveyorBelt_A01_Decal (Material)
        * Shader (Shader)
      * Metal_Rough_A (Material)
        * Shader (Shader)
      * MetalPainted_Black_Glossy_A (Material)
        * Shader (Shader)
      * MetalPainted_Blue_Glossy_A (Material)
        * Shader (Shader)
      * Plastic_Orange_A (Material)
        * Shader (Shader)
      * Plastic_Red_A (Material)
        * Shader (Shader)
      * Plastic_Rough_Black_A (Material)
        * Shader (Shader)
      * Steel_A (Material)
        * Shader (Shader)
    * SM_ConveyorBelt_A09_02 (Mesh)
      * M_ConveyorBelt_A01_Body_01 (GeomSubset)
      * M_ConveyorBelt_A01_Bolts_01 (GeomSubset)
      * M_ConveyorBelt_A01_Box_01 (GeomSubset)
      * M_ConveyorBelt_A01_Caps_01 (GeomSubset)
      * M_ConveyorBelt_A01_Engine_01 (GeomSubset)
      * M_ConveyorBelt_A01_FixBody_01 (GeomSubset)
      * M_ConveyorBelt_A01_Plate01_01 (GeomSubset)
      * M_ConveyorBelt_A01_Plate02_01 (GeomSubset)
      * M_ConveyorBelt_A01_Sheets_01 (GeomSubset)
      * M_ConveyorBelt_A01_WirePipes_01 (GeomSubset)
    * SM_ConveyorBelt_A09_Decal_02 (Mesh)
    * Belt (Xform)
      * SM_ConveyorBelt_A09_Belt_02 (Mesh)
    * Anchorpoint (Xform)
  * Conveyor_26 (Xform)
    * Looks (Scope)
      * Acrylic_Clear_Glossy_A (Material)
        * Shader (Shader)
      * M_ConveyorBelt_A01_Belt (Material)
        * Shader (Shader)
      * M_ConveyorBelt_A01_Decal (Material)
        * Shader (Shader)
      * Metal_Rough_A (Material)
        * Shader (Shader)
      * MetalPainted_Black_Glossy_A (Material)
        * Shader (Shader)
      * MetalPainted_Blue_Glossy_A (Material)
        * Shader (Shader)
      * Plastic_Orange_A (Material)
        * Shader (Shader)
      * Plastic_Red_A (Material)
        * Shader (Shader)
      * Plastic_Rough_Black_A (Material)
        * Shader (Shader)
      * Steel_A (Material)
        * Shader (Shader)
    * SM_ConveyorBelt_A09_02 (Mesh)
      * M_ConveyorBelt_A01_Body_01 (GeomSubset)
      * M_ConveyorBelt_A01_Bolts_01 (GeomSubset)
      * M_ConveyorBelt_A01_Box_01 (GeomSubset)
      * M_ConveyorBelt_A01_Caps_01 (GeomSubset)
      * M_ConveyorBelt_A01_Engine_01 (GeomSubset)
      * M_ConveyorBelt_A01_FixBody_01 (GeomSubset)
      * M_ConveyorBelt_A01_Plate01_01 (GeomSubset)
      * M_ConveyorBelt_A01_Plate02_01 (GeomSubset)
      * M_ConveyorBelt_A01_Sheets_01 (GeomSubset)
      * M_ConveyorBelt_A01_WirePipes_01 (GeomSubset)
    * SM_ConveyorBelt_A09_Decal_02 (Mesh)
    * Belt (Xform)
      * SM_ConveyorBelt_A09_Belt_02 (Mesh)
    * Anchorpoint (Xform)
  * Conveyor_27 (Xform)
    * Looks (Scope)
      * Acrylic_Clear_Glossy_A (Material)
        * Shader (Shader)
      * M_ConveyorBelt_A01_Belt (Material)
        * Shader (Shader)
      * M_ConveyorBelt_A01_Decal (Material)
        * Shader (Shader)
      * Metal_Rough_A (Material)
        * Shader (Shader)
      * MetalPainted_Black_Glossy_A (Material)
        * Shader (Shader)
      * MetalPainted_Blue_Glossy_A (Material)
        * Shader (Shader)
      * Plastic_Orange_A (Material)
        * Shader (Shader)
      * Plastic_Red_A (Material)
        * Shader (Shader)
      * Plastic_Rough_Black_A (Material)
        * Shader (Shader)
      * Steel_A (Material)
        * Shader (Shader)
    * SM_ConveyorBelt_A09_02 (Mesh)
      * M_ConveyorBelt_A01_Body_01 (GeomSubset)
      * M_ConveyorBelt_A01_Bolts_01 (GeomSubset)
      * M_ConveyorBelt_A01_Box_01 (GeomSubset)
      * M_ConveyorBelt_A01_Caps_01 (GeomSubset)
      * M_ConveyorBelt_A01_Engine_01 (GeomSubset)
      * M_ConveyorBelt_A01_FixBody_01 (GeomSubset)
      * M_ConveyorBelt_A01_Plate01_01 (GeomSubset)
      * M_ConveyorBelt_A01_Plate02_01 (GeomSubset)
      * M_ConveyorBelt_A01_Sheets_01 (GeomSubset)
      * M_ConveyorBelt_A01_WirePipes_01 (GeomSubset)
    * SM_ConveyorBelt_A09_Decal_02 (Mesh)
    * Belt (Xform)
      * SM_ConveyorBelt_A09_Belt_02 (Mesh)
    * Anchorpoint (Xform)
  * Conveyor_28 (Xform)
    * Looks (Scope)
      * Acrylic_Clear_Glossy_A (Material)
        * Shader (Shader)
      * M_ConveyorBelt_A01_Belt (Material)
        * Shader (Shader)
      * M_ConveyorBelt_A01_Decal (Material)
        * Shader (Shader)
      * Metal_Rough_A (Material)
        * Shader (Shader)
      * MetalPainted_Black_Glossy_A (Material)
        * Shader (Shader)
      * MetalPainted_Blue_Glossy_A (Material)
        * Shader (Shader)
      * Plastic_Orange_A (Material)
        * Shader (Shader)
      * Plastic_Red_A (Material)
        * Shader (Shader)
      * Plastic_Rough_Black_A (Material)
        * Shader (Shader)
      * Steel_A (Material)
        * Shader (Shader)
    * SM_ConveyorBelt_A09_02 (Mesh)
      * M_ConveyorBelt_A01_Body_01 (GeomSubset)
      * M_ConveyorBelt_A01_Bolts_01 (GeomSubset)
      * M_ConveyorBelt_A01_Box_01 (GeomSubset)
      * M_ConveyorBelt_A01_Caps_01 (GeomSubset)
      * M_ConveyorBelt_A01_Engine_01 (GeomSubset)
      * M_ConveyorBelt_A01_FixBody_01 (GeomSubset)
      * M_ConveyorBelt_A01_Plate01_01 (GeomSubset)
      * M_ConveyorBelt_A01_Plate02_01 (GeomSubset)
      * M_ConveyorBelt_A01_Sheets_01 (GeomSubset)
      * M_ConveyorBelt_A01_WirePipes_01 (GeomSubset)
    * SM_ConveyorBelt_A09_Decal_02 (Mesh)
    * Belt (Xform)
      * SM_ConveyorBelt_A09_Belt_02 (Mesh)
    * Anchorpoint (Xform)
  * PartA_OnBelt_1 (Xform)
    * node__Size_1_0x1_4x4_SUPPRESSION_Default (Xform)
      * geometry_1 (Mesh)
  * PartA_OnBelt_2 (Xform)
    * node__Size_1_0x1_4x4_SUPPRESSION_Default (Xform)
      * geometry_1 (Mesh)
  * PartA_OnBelt_3 (Xform)
    * node__Size_1_0x1_4x4_SUPPRESSION_Default (Xform)
      * geometry_1 (Mesh)
  * PartA_OnBelt_4 (Xform)
    * node__Size_1_0x1_4x4_SUPPRESSION_Default (Xform)
      * geometry_1 (Mesh)
  * PartA_OnBelt_5 (Xform)
    * node__Size_1_0x1_4x4_SUPPRESSION_Default (Xform)
      * geometry_1 (Mesh)
  * PartA_OnBelt_6 (Xform)
    * node__Size_1_0x1_4x4_SUPPRESSION_Default (Xform)
      * geometry_1 (Mesh)
  * PartA_OnBelt_7 (Xform)
    * node__Size_1_0x1_4x4_SUPPRESSION_Default (Xform)
      * geometry_1 (Mesh)
  * PartA_OnBelt_8 (Xform)
    * node__Size_1_0x1_4x4_SUPPRESSION_Default (Xform)
      * geometry_1 (Mesh)
  * PartA_OnBelt_9 (Xform)
    * node__Size_1_0x1_4x4_SUPPRESSION_Default (Xform)
      * geometry_1 (Mesh)
  * PartA_OnBelt_10 (Xform)
    * node__Size_1_0x1_4x4_SUPPRESSION_Default (Xform)
      * geometry_1 (Mesh)
  * PartA_OnBelt_11 (Xform)
    * node__Size_1_0x1_4x4_SUPPRESSION_Default (Xform)
      * geometry_1 (Mesh)
  * PartA_OnBelt_12 (Xform)
    * node__Size_1_0x1_4x4_SUPPRESSION_Default (Xform)
      * geometry_1 (Mesh)
  * PartA_OnBelt_13 (Xform)
    * node__Size_1_0x1_4x4_SUPPRESSION_Default (Xform)
      * geometry_1 (Mesh)
  * PartA_OnBelt_14 (Xform)
    * node__Size_1_0x1_4x4_SUPPRESSION_Default (Xform)
      * geometry_1 (Mesh)
  * PartA_OnBelt_15 (Xform)
    * node__Size_1_0x1_4x4_SUPPRESSION_Default (Xform)
      * geometry_1 (Mesh)
  * PartA_OnBelt_16 (Xform)
    * node__Size_1_0x1_4x4_SUPPRESSION_Default (Xform)
      * geometry_1 (Mesh)
  * PartA_OnBelt_17 (Xform)
    * node__Size_1_0x1_4x4_SUPPRESSION_Default (Xform)
      * geometry_1 (Mesh)
  * PartA_OnBelt_18 (Xform)
    * node__Size_1_0x1_4x4_SUPPRESSION_Default (Xform)
      * geometry_1 (Mesh)
  * PartA_OnBelt_19 (Xform)
    * node__Size_1_0x1_4x4_SUPPRESSION_Default (Xform)
      * geometry_1 (Mesh)
  * PartA_OnBelt_20 (Xform)
    * node__Size_1_0x1_4x4_SUPPRESSION_Default (Xform)
      * geometry_1 (Mesh)
  * PartA_OnBelt_21 (Xform)
    * node__Size_1_0x1_4x4_SUPPRESSION_Default (Xform)
      * geometry_1 (Mesh)
  * PartA_OnBelt_22 (Xform)
    * node__Size_1_0x1_4x4_SUPPRESSION_Default (Xform)
      * geometry_1 (Mesh)
  * PartA_OnBelt_23 (Xform)
    * node__Size_1_0x1_4x4_SUPPRESSION_Default (Xform)
      * geometry_1 (Mesh)
  * PartA_OnBelt_24 (Xform)
    * node__Size_1_0x1_4x4_SUPPRESSION_Default (Xform)
      * geometry_1 (Mesh)
  * PartA_OnBelt_25 (Xform)
    * node__Size_1_0x1_4x4_SUPPRESSION_Default (Xform)
      * geometry_1 (Mesh)
  * PartA_OnBelt_26 (Xform)
    * node__Size_1_0x1_4x4_SUPPRESSION_Default (Xform)
      * geometry_1 (Mesh)
  * PartA_OnBelt_27 (Xform)
    * node__Size_1_0x1_4x4_SUPPRESSION_Default (Xform)
      * geometry_1 (Mesh)
  * PartA_OnBelt_28 (Xform)
    * node__Size_1_0x1_4x4_SUPPRESSION_Default (Xform)
      * geometry_1 (Mesh)
  * PartA_OnBelt_29 (Xform)
    * node__Size_1_0x1_4x4_SUPPRESSION_Default (Xform)
      * geometry_1 (Mesh)
  * PartA_OnBelt_30 (Xform)
    * node__Size_1_0x1_4x4_SUPPRESSION_Default (Xform)
      * geometry_1 (Mesh)
  * PartA_OnBelt_31 (Xform)
    * node__Size_1_0x1_4x4_SUPPRESSION_Default (Xform)
      * geometry_1 (Mesh)
  * PartA_OnBelt_32 (Xform)
    * node__Size_1_0x1_4x4_SUPPRESSION_Default (Xform)
      * geometry_1 (Mesh)
  * PartA_OnBelt_33 (Xform)
    * node__Size_1_0x1_4x4_SUPPRESSION_Default (Xform)
      * geometry_1 (Mesh)
  * PartA_OnBelt_34 (Xform)
    * node__Size_1_0x1_4x4_SUPPRESSION_Default (Xform)
      * geometry_1 (Mesh)
  * PartA_OnBelt_35 (Xform)
    * node__Size_1_0x1_4x4_SUPPRESSION_Default (Xform)
      * geometry_1 (Mesh)
  * PartA_OnBelt_36 (Xform)
    * node__Size_1_0x1_4x4_SUPPRESSION_Default (Xform)
      * geometry_1 (Mesh)
  * PartA_OnBelt_37 (Xform)
    * node__Size_1_0x1_4x4_SUPPRESSION_Default (Xform)
      * geometry_1 (Mesh)
  * PartA_OnBelt_38 (Xform)
    * node__Size_1_0x1_4x4_SUPPRESSION_Default (Xform)
      * geometry_1 (Mesh)
  * PartA_OnBelt_39 (Xform)
    * node__Size_1_0x1_4x4_SUPPRESSION_Default (Xform)
      * geometry_1 (Mesh)
  * PartA_OnBelt_40 (Xform)
    * node__Size_1_0x1_4x4_SUPPRESSION_Default (Xform)
      * geometry_1 (Mesh)
  * PartA_OnBelt_41 (Xform)
    * node__Size_1_0x1_4x4_SUPPRESSION_Default (Xform)
      * geometry_1 (Mesh)
  * PartA_OnBelt_42 (Xform)
    * node__Size_1_0x1_4x4_SUPPRESSION_Default (Xform)
      * geometry_1 (Mesh)
  * PartA_OnBelt_43 (Xform)
    * node__Size_1_0x1_4x4_SUPPRESSION_Default (Xform)
      * geometry_1 (Mesh)
  * PartA_OnBelt_44 (Xform)
    * node__Size_1_0x1_4x4_SUPPRESSION_Default (Xform)
      * geometry_1 (Mesh)
  * PartA_OnBelt_45 (Xform)
    * node__Size_1_0x1_4x4_SUPPRESSION_Default (Xform)
      * geometry_1 (Mesh)
  * PartA_OnBelt_46 (Xform)
    * node__Size_1_0x1_4x4_SUPPRESSION_Default (Xform)
      * geometry_1 (Mesh)
  * PartA_OnBelt_47 (Xform)
    * node__Size_1_0x1_4x4_SUPPRESSION_Default (Xform)
      * geometry_1 (Mesh)
  * PartA_OnBelt_48 (Xform)
    * node__Size_1_0x1_4x4_SUPPRESSION_Default (Xform)
      * geometry_1 (Mesh)
  * PartA_OnBelt_49 (Xform)
    * node__Size_1_0x1_4x4_SUPPRESSION_Default (Xform)
      * geometry_1 (Mesh)
  * PartA_OnBelt_50 (Xform)
    * node__Size_1_0x1_4x4_SUPPRESSION_Default (Xform)
      * geometry_1 (Mesh)
  * PartA_OnBelt_51 (Xform)
    * node__Size_1_0x1_4x4_SUPPRESSION_Default (Xform)
      * geometry_1 (Mesh)
  * PartA_OnBelt_52 (Xform)
    * node__Size_1_0x1_4x4_SUPPRESSION_Default (Xform)
      * geometry_1 (Mesh)
  * PartA_OnBelt_53 (Xform)
    * node__Size_1_0x1_4x4_SUPPRESSION_Default (Xform)
      * geometry_1 (Mesh)
  * PartA_OnBelt_54 (Xform)
    * node__Size_1_0x1_4x4_SUPPRESSION_Default (Xform)
      * geometry_1 (Mesh)
  * PartA_OnBelt_55 (Xform)
    * node__Size_1_0x1_4x4_SUPPRESSION_Default (Xform)
      * geometry_1 (Mesh)
  * PartA_OnBelt_56 (Xform)
    * node__Size_1_0x1_4x4_SUPPRESSION_Default (Xform)
      * geometry_1 (Mesh)
  * PartA_OnBelt_57 (Xform)
    * node__Size_1_0x1_4x4_SUPPRESSION_Default (Xform)
      * geometry_1 (Mesh)
  * PartA_OnBelt_58 (Xform)
    * node__Size_1_0x1_4x4_SUPPRESSION_Default (Xform)
      * geometry_1 (Mesh)
  * PartA_OnBelt_59 (Xform)
    * node__Size_1_0x1_4x4_SUPPRESSION_Default (Xform)
      * geometry_1 (Mesh)
  * PartA_OnBelt_60 (Xform)
    * node__Size_1_0x1_4x4_SUPPRESSION_Default (Xform)
      * geometry_1 (Mesh)
  * PartA_OnBelt_61 (Xform)
    * node__Size_1_0x1_4x4_SUPPRESSION_Default (Xform)
      * geometry_1 (Mesh)
  * PartA_OnBelt_62 (Xform)
    * node__Size_1_0x1_4x4_SUPPRESSION_Default (Xform)
      * geometry_1 (Mesh)
  * PartA_OnBelt_63 (Xform)
    * node__Size_1_0x1_4x4_SUPPRESSION_Default (Xform)
      * geometry_1 (Mesh)
  * PartB_OnBelt_1 (Xform)
    * node__Size_8_Length_28_SUPPRESSION_A_Simplified (Xform)
      * geometry_1 (Mesh)
  * PartB_OnBelt_2 (Xform)
    * node__Size_8_Length_28_SUPPRESSION_A_Simplified (Xform)
      * geometry_1 (Mesh)
  * PartB_OnBelt_3 (Xform)
    * node__Size_8_Length_28_SUPPRESSION_A_Simplified (Xform)
      * geometry_1 (Mesh)
  * PartB_OnBelt_4 (Xform)
    * node__Size_8_Length_28_SUPPRESSION_A_Simplified (Xform)
      * geometry_1 (Mesh)
  * PartB_OnBelt_5 (Xform)
    * node__Size_8_Length_28_SUPPRESSION_A_Simplified (Xform)
      * geometry_1 (Mesh)
  * PartB_OnBelt_6 (Xform)
    * node__Size_8_Length_28_SUPPRESSION_A_Simplified (Xform)
      * geometry_1 (Mesh)
  * PartB_OnBelt_7 (Xform)
    * node__Size_8_Length_28_SUPPRESSION_A_Simplified (Xform)
      * geometry_1 (Mesh)
  * PartB_OnBelt_8 (Xform)
    * node__Size_8_Length_28_SUPPRESSION_A_Simplified (Xform)
      * geometry_1 (Mesh)
  * PartB_OnBelt_9 (Xform)
    * node__Size_8_Length_28_SUPPRESSION_A_Simplified (Xform)
      * geometry_1 (Mesh)
  * PartB_OnBelt_10 (Xform)
    * node__Size_8_Length_28_SUPPRESSION_A_Simplified (Xform)
      * geometry_1 (Mesh)
  * PartB_OnBelt_11 (Xform)
    * node__Size_8_Length_28_SUPPRESSION_A_Simplified (Xform)
      * geometry_1 (Mesh)
  * PartB_OnBelt_12 (Xform)
    * node__Size_8_Length_28_SUPPRESSION_A_Simplified (Xform)
      * geometry_1 (Mesh)
  * PartB_OnBelt_13 (Xform)
    * node__Size_8_Length_28_SUPPRESSION_A_Simplified (Xform)
      * geometry_1 (Mesh)
  * PartB_OnBelt_14 (Xform)
    * node__Size_8_Length_28_SUPPRESSION_A_Simplified (Xform)
      * geometry_1 (Mesh)
  * PartB_OnBelt_15 (Xform)
    * node__Size_8_Length_28_SUPPRESSION_A_Simplified (Xform)
      * geometry_1 (Mesh)
  * PartB_OnBelt_16 (Xform)
    * node__Size_8_Length_28_SUPPRESSION_A_Simplified (Xform)
      * geometry_1 (Mesh)
  * PartB_OnBelt_17 (Xform)
    * node__Size_8_Length_28_SUPPRESSION_A_Simplified (Xform)
      * geometry_1 (Mesh)
  * PartB_OnBelt_18 (Xform)
    * node__Size_8_Length_28_SUPPRESSION_A_Simplified (Xform)
      * geometry_1 (Mesh)
  * PartB_OnBelt_19 (Xform)
    * node__Size_8_Length_28_SUPPRESSION_A_Simplified (Xform)
      * geometry_1 (Mesh)
  * PartB_OnBelt_20 (Xform)
    * node__Size_8_Length_28_SUPPRESSION_A_Simplified (Xform)
      * geometry_1 (Mesh)
  * PartB_OnBelt_21 (Xform)
    * node__Size_8_Length_28_SUPPRESSION_A_Simplified (Xform)
      * geometry_1 (Mesh)
  * PartB_OnBelt_22 (Xform)
    * node__Size_8_Length_28_SUPPRESSION_A_Simplified (Xform)
      * geometry_1 (Mesh)
  * PartB_OnBelt_23 (Xform)
    * node__Size_8_Length_28_SUPPRESSION_A_Simplified (Xform)
      * geometry_1 (Mesh)
  * PartB_OnBelt_24 (Xform)
    * node__Size_8_Length_28_SUPPRESSION_A_Simplified (Xform)
      * geometry_1 (Mesh)
  * PartB_OnBelt_25 (Xform)
    * node__Size_8_Length_28_SUPPRESSION_A_Simplified (Xform)
      * geometry_1 (Mesh)
  * PartB_OnBelt_26 (Xform)
    * node__Size_8_Length_28_SUPPRESSION_A_Simplified (Xform)
      * geometry_1 (Mesh)
  * PartB_OnBelt_27 (Xform)
    * node__Size_8_Length_28_SUPPRESSION_A_Simplified (Xform)
      * geometry_1 (Mesh)
  * PartB_OnBelt_28 (Xform)
    * node__Size_8_Length_28_SUPPRESSION_A_Simplified (Xform)
      * geometry_1 (Mesh)
  * PartB_OnBelt_29 (Xform)
    * node__Size_8_Length_28_SUPPRESSION_A_Simplified (Xform)
      * geometry_1 (Mesh)
  * PartB_OnBelt_30 (Xform)
    * node__Size_8_Length_28_SUPPRESSION_A_Simplified (Xform)
      * geometry_1 (Mesh)
  * PartB_OnBelt_31 (Xform)
    * node__Size_8_Length_28_SUPPRESSION_A_Simplified (Xform)
      * geometry_1 (Mesh)
  * PartB_OnBelt_32 (Xform)
    * node__Size_8_Length_28_SUPPRESSION_A_Simplified (Xform)
      * geometry_1 (Mesh)
  * PartB_OnBelt_33 (Xform)
    * node__Size_8_Length_28_SUPPRESSION_A_Simplified (Xform)
      * geometry_1 (Mesh)
  * PartB_OnBelt_34 (Xform)
    * node__Size_8_Length_28_SUPPRESSION_A_Simplified (Xform)
      * geometry_1 (Mesh)
  * PartB_OnBelt_35 (Xform)
    * node__Size_8_Length_28_SUPPRESSION_A_Simplified (Xform)
      * geometry_1 (Mesh)
  * PartB_OnBelt_36 (Xform)
    * node__Size_8_Length_28_SUPPRESSION_A_Simplified (Xform)
      * geometry_1 (Mesh)
  * PartB_OnBelt_37 (Xform)
    * node__Size_8_Length_28_SUPPRESSION_A_Simplified (Xform)
      * geometry_1 (Mesh)
  * PartB_OnBelt_38 (Xform)
    * node__Size_8_Length_28_SUPPRESSION_A_Simplified (Xform)
      * geometry_1 (Mesh)
  * PartB_OnBelt_39 (Xform)
    * node__Size_8_Length_28_SUPPRESSION_A_Simplified (Xform)
      * geometry_1 (Mesh)
  * PartB_OnBelt_40 (Xform)
    * node__Size_8_Length_28_SUPPRESSION_A_Simplified (Xform)
      * geometry_1 (Mesh)
  * PartB_OnBelt_41 (Xform)
    * node__Size_8_Length_28_SUPPRESSION_A_Simplified (Xform)
      * geometry_1 (Mesh)
  * PartB_OnBelt_42 (Xform)
    * node__Size_8_Length_28_SUPPRESSION_A_Simplified (Xform)
      * geometry_1 (Mesh)
  * PartB_OnBelt_43 (Xform)
    * node__Size_8_Length_28_SUPPRESSION_A_Simplified (Xform)
      * geometry_1 (Mesh)
  * PartB_OnBelt_44 (Xform)
    * node__Size_8_Length_28_SUPPRESSION_A_Simplified (Xform)
      * geometry_1 (Mesh)
  * PartB_OnBelt_45 (Xform)
    * node__Size_8_Length_28_SUPPRESSION_A_Simplified (Xform)
      * geometry_1 (Mesh)
  * PartB_OnBelt_46 (Xform)
    * node__Size_8_Length_28_SUPPRESSION_A_Simplified (Xform)
      * geometry_1 (Mesh)
  * PartB_OnBelt_47 (Xform)
    * node__Size_8_Length_28_SUPPRESSION_A_Simplified (Xform)
      * geometry_1 (Mesh)
  * PartB_OnBelt_48 (Xform)
    * node__Size_8_Length_28_SUPPRESSION_A_Simplified (Xform)
      * geometry_1 (Mesh)
  * PartB_OnBelt_49 (Xform)
    * node__Size_8_Length_28_SUPPRESSION_A_Simplified (Xform)
      * geometry_1 (Mesh)
  * PartB_OnBelt_50 (Xform)
    * node__Size_8_Length_28_SUPPRESSION_A_Simplified (Xform)
      * geometry_1 (Mesh)
  * PartB_OnBelt_51 (Xform)
    * node__Size_8_Length_28_SUPPRESSION_A_Simplified (Xform)
      * geometry_1 (Mesh)
  * PartB_OnBelt_52 (Xform)
    * node__Size_8_Length_28_SUPPRESSION_A_Simplified (Xform)
      * geometry_1 (Mesh)
  * PartB_OnBelt_53 (Xform)
    * node__Size_8_Length_28_SUPPRESSION_A_Simplified (Xform)
      * geometry_1 (Mesh)
  * PartB_OnBelt_54 (Xform)
    * node__Size_8_Length_28_SUPPRESSION_A_Simplified (Xform)
      * geometry_1 (Mesh)
  * PartB_OnBelt_55 (Xform)
    * node__Size_8_Length_28_SUPPRESSION_A_Simplified (Xform)
      * geometry_1 (Mesh)
  * PartB_OnBelt_56 (Xform)
    * node__Size_8_Length_28_SUPPRESSION_A_Simplified (Xform)
      * geometry_1 (Mesh)
  * PartB_OnBelt_57 (Xform)
    * node__Size_8_Length_28_SUPPRESSION_A_Simplified (Xform)
      * geometry_1 (Mesh)
  * PartB_OnBelt_58 (Xform)
    * node__Size_8_Length_28_SUPPRESSION_A_Simplified (Xform)
      * geometry_1 (Mesh)
  * PartB_OnBelt_59 (Xform)
    * node__Size_8_Length_28_SUPPRESSION_A_Simplified (Xform)
      * geometry_1 (Mesh)
  * PartB_OnBelt_60 (Xform)
    * node__Size_8_Length_28_SUPPRESSION_A_Simplified (Xform)
      * geometry_1 (Mesh)
  * PartB_OnBelt_61 (Xform)
    * node__Size_8_Length_28_SUPPRESSION_A_Simplified (Xform)
      * geometry_1 (Mesh)
  * PartB_OnBelt_62 (Xform)
    * node__Size_8_Length_28_SUPPRESSION_A_Simplified (Xform)
      * geometry_1 (Mesh)
  * PartB_OnBelt_63 (Xform)
    * node__Size_8_Length_28_SUPPRESSION_A_Simplified (Xform)
      * geometry_1 (Mesh)
  * PartA_OnWorkbench_1 (Xform)
    * node__Size_1_0x1_4x4_SUPPRESSION_Default (Xform)
      * geometry_1 (Mesh)
  * PartA_OnWorkbench_2 (Xform)
    * node__Size_1_0x1_4x4_SUPPRESSION_Default (Xform)
      * geometry_1 (Mesh)
  * PartA_OnWorkbench_3 (Xform)
    * node__Size_1_0x1_4x4_SUPPRESSION_Default (Xform)
      * geometry_1 (Mesh)
  * PartA_OnWorkbench_4 (Xform)
    * node__Size_1_0x1_4x4_SUPPRESSION_Default (Xform)
      * geometry_1 (Mesh)
  * PartA_OnWorkbench_5 (Xform)
    * node__Size_1_0x1_4x4_SUPPRESSION_Default (Xform)
      * geometry_1 (Mesh)
  * PartA_OnWorkbench_6 (Xform)
    * node__Size_1_0x1_4x4_SUPPRESSION_Default (Xform)
      * geometry_1 (Mesh)
  * PartB_OnWorkbench_1 (Xform)
    * node__Size_8_Length_28_SUPPRESSION_A_Simplified (Xform)
      * geometry_1 (Mesh)
  * PartB_OnWorkbench_2 (Xform)
    * node__Size_8_Length_28_SUPPRESSION_A_Simplified (Xform)
      * geometry_1 (Mesh)
  * PartB_OnWorkbench_3 (Xform)
    * node__Size_8_Length_28_SUPPRESSION_A_Simplified (Xform)
      * geometry_1 (Mesh)
  * PartB_OnWorkbench_4 (Xform)
    * node__Size_8_Length_28_SUPPRESSION_A_Simplified (Xform)
      * geometry_1 (Mesh)
  * PartB_OnWorkbench_5 (Xform)
    * node__Size_8_Length_28_SUPPRESSION_A_Simplified (Xform)
      * geometry_1 (Mesh)
  * PartB_OnWorkbench_6 (Xform)
    * node__Size_8_Length_28_SUPPRESSION_A_Simplified (Xform)
      * geometry_1 (Mesh)
  * agv_1 (Xform)
    * Materials (Scope)
      * ASELSAN_CATS_04 (Material)
        * pbr_shader (Shader)
      * ASELSAN_CATS_04_2 (Material)
        * pbr_shader (Shader)
      * ASELSAN_CATS_13 (Material)
        * pbr_shader (Shader)
      * Color_000 (Material)
        * pbr_shader (Shader)
      * Color_A05 (Material)
        * pbr_shader (Shader)
      * Color_A06 (Material)
        * pbr_shader (Shader)
      * Color_B05 (Material)
        * pbr_shader (Shader)
      * Color_E02 (Material)
        * pbr_shader (Shader)
      * Color_E05 (Material)
        * pbr_shader (Shader)
      * Color_F06 (Material)
        * pbr_shader (Shader)
      * Color_G03 (Material)
        * pbr_shader (Shader)
      * Color_M02 (Material)
        * pbr_shader (Shader)
      * Color_M03 (Material)
        * pbr_shader (Shader)
      * Mtl39 (Material)
        * pbr_shader (Shader)
      * Mtl6 (Material)
        * pbr_shader (Shader)
        * uvset0 (Shader)
        * tex_base (Shader)
      * Mtl9 (Material)
        * pbr_shader (Shader)
      * Silver (Material)
        * pbr_shader (Shader)
      * material (Material)
        * pbr_shader (Shader)
        * uvset0 (Shader)
        * tex_base (Shader)
      * cash_register_keys (Material)
        * pbr_shader (Shader)
      * Chris_Shoe_Sole (Material)
        * pbr_shader (Shader)
      * Color_002 (Material)
        * pbr_shader (Shader)
      * Color_005 (Material)
        * pbr_shader (Shader)
      * Color_006 (Material)
        * pbr_shader (Shader)
      * Color_008 (Material)
        * pbr_shader (Shader)
      * Color_A01 (Material)
        * pbr_shader (Shader)
      * Color_A11 (Material)
        * pbr_shader (Shader)
      * Color_M04 (Material)
        * pbr_shader (Shader)
      * Color_M05 (Material)
        * pbr_shader (Shader)
      * Color_M06 (Material)
        * pbr_shader (Shader)
      * Color_M07 (Material)
        * pbr_shader (Shader)
      * Color_M09 (Material)
        * pbr_shader (Shader)
      * FCP_Charcoal_v2 (Material)
        * pbr_shader (Shader)
      * FrontColor (Material)
        * pbr_shader (Shader)
      * Light_Blue (Material)
        * pbr_shader (Shader)
      * M_0011_Seashell (Material)
        * pbr_shader (Shader)
      * M_0131_Silver (Material)
        * pbr_shader (Shader)
      * M_0134_DimGray (Material)
        * pbr_shader (Shader)
      * M_0135_DarkGray (Material)
        * pbr_shader (Shader)
      * Metal_Silver (Material)
        * pbr_shader (Shader)
      * Mtl1 (Material)
        * pbr_shader (Shader)
      * Mtl10 (Material)
        * pbr_shader (Shader)
      * Mtl11 (Material)
        * pbr_shader (Shader)
      * Mtl12 (Material)
        * pbr_shader (Shader)
      * Mtl13 (Material)
        * pbr_shader (Shader)
      * Mtl14 (Material)
        * pbr_shader (Shader)
      * Mtl15 (Material)
        * pbr_shader (Shader)
      * Mtl16 (Material)
        * pbr_shader (Shader)
      * Mtl17 (Material)
        * pbr_shader (Shader)
      * Mtl3 (Material)
        * pbr_shader (Shader)
      * Mtl35 (Material)
        * pbr_shader (Shader)
      * Mtl36 (Material)
        * pbr_shader (Shader)
      * Mtl37 (Material)
        * pbr_shader (Shader)
      * Mtl3a (Material)
        * pbr_shader (Shader)
      * Mtl3b (Material)
        * pbr_shader (Shader)
      * Mtl5 (Material)
        * pbr_shader (Shader)
      * Mtl7 (Material)
        * pbr_shader (Shader)
      * Mtl8 (Material)
        * pbr_shader (Shader)
      * Mtla (Material)
        * pbr_shader (Shader)
      * Mtlb1 (Material)
        * pbr_shader (Shader)
      * Stainless_Steel (Material)
        * pbr_shader (Shader)
      * Metal_Aluminum_Anodized_1 (Material)
        * pbr_shader (Shader)
      * Metal_Aluminum_Anodized_2 (Material)
        * pbr_shader (Shader)
      * basic_gray_plastic (Material)
        * pbr_shader (Shader)
      * texture (Material)
        * pbr_shader (Shader)
    * Meshes (Xform)
      * Sketchfab_model (Xform)
        * AGV_ready_1_obj_cleaner_materialmerger_gles (Xform)
          * Object_2 (Xform)
            * Object_0 (Mesh)
          * Object_3 (Xform)
            * Object_1 (Mesh)
          * Object_4 (Xform)
            * Object_2 (Mesh)
          * Object_5 (Xform)
            * Object_3 (Mesh)
          * Object_6 (Xform)
            * Object_4 (Mesh)
          * Object_7 (Xform)
            * Object_5 (Mesh)
          * Object_8 (Xform)
            * Object_6 (Mesh)
          * Object_9 (Xform)
            * Object_7 (Mesh)
          * Object_10 (Xform)
            * Object_8 (Mesh)
          * Object_11 (Xform)
            * Object_9 (Mesh)
          * Object_12 (Xform)
            * Object_10 (Mesh)
          * Object_13 (Xform)
            * Object_11 (Mesh)
          * Object_14 (Xform)
            * Object_12 (Mesh)
          * Object_15 (Xform)
            * Object_13 (Mesh)
          * Object_16 (Xform)
            * Object_14 (Mesh)
          * Object_17 (Xform)
            * Object_15 (Mesh)
          * Object_18 (Xform)
            * Object_16 (Mesh)
          * Object_19 (Xform)
            * Object_17 (Mesh)
          * Object_20 (Xform)
            * Object_18 (Mesh)
          * Object_21 (Xform)
            * Object_19 (Mesh)
          * Object_22 (Xform)
            * Object_20 (Mesh)
          * Object_23 (Xform)
            * Object_21 (Mesh)
          * Object_24 (Xform)
            * Object_22 (Mesh)
          * Object_25 (Xform)
            * Object_23 (Mesh)
          * Object_26 (Xform)
            * Object_24 (Mesh)
          * Object_27 (Xform)
            * Object_25 (Mesh)
          * Object_28 (Xform)
            * Object_26 (Mesh)
          * Object_29 (Xform)
            * Object_27 (Mesh)
          * Object_30 (Xform)
            * Object_28 (Mesh)
          * Object_31 (Xform)
            * Object_29 (Mesh)
          * Object_32 (Xform)
            * Object_30 (Mesh)
          * Object_33 (Xform)
            * Object_31 (Mesh)
          * Object_34 (Xform)
            * Object_32 (Mesh)
          * Object_35 (Xform)
            * Object_33 (Mesh)
          * Object_36 (Xform)
            * Object_34 (Mesh)
          * Object_37 (Xform)
            * Object_35 (Mesh)
          * Object_38 (Xform)
            * Object_36 (Mesh)
          * Object_39 (Xform)
            * Object_37 (Mesh)
          * Object_40 (Xform)
            * Object_38 (Mesh)
          * Object_41 (Xform)
            * Object_39 (Mesh)
          * Object_42 (Xform)
            * Object_40 (Mesh)
          * Object_43 (Xform)
            * Object_41 (Mesh)
          * Object_44 (Xform)
            * Object_42 (Mesh)
          * Object_45 (Xform)
            * Object_43 (Mesh)
          * Object_46 (Xform)
            * Object_44 (Mesh)
          * Object_47 (Xform)
            * Object_45 (Mesh)
          * Object_48 (Xform)
            * Object_46 (Mesh)
          * Object_49 (Xform)
            * Object_47 (Mesh)
          * Object_50 (Xform)
            * Object_48 (Mesh)
          * Object_51 (Xform)
            * Object_49 (Mesh)
          * Object_52 (Xform)
            * Object_50 (Mesh)
          * Object_53 (Xform)
            * Object_51 (Mesh)
          * Object_54 (Xform)
            * Object_52 (Mesh)
          * Object_55 (Xform)
            * Object_53 (Mesh)
          * Object_56 (Xform)
            * Object_54 (Mesh)
          * Object_57 (Xform)
            * Object_55 (Mesh)
          * Object_58 (Xform)
            * Object_56 (Mesh)
          * Object_59 (Xform)
            * Object_57 (Mesh)
          * Object_60 (Xform)
            * Object_58 (Mesh)
          * Object_61 (Xform)
            * Object_59 (Mesh)
          * Object_62 (Xform)
            * Object_60 (Mesh)
          * Object_63 (Xform)
            * Object_61 (Mesh)
          * Object_64 (Xform)
            * Object_62 (Mesh)
          * Object_65 (Xform)
            * Object_63 (Mesh)
          * Object_66 (Xform)
            * Object_64 (Mesh)
          * Object_67 (Xform)
            * Object_65 (Mesh)
          * Object_68 (Xform)
            * Object_66 (Mesh)
          * Object_69 (Xform)
            * Object_67 (Mesh)
          * Object_70 (Xform)
            * Object_68 (Mesh)
          * Object_71 (Xform)
            * Object_69 (Mesh)
          * Object_72 (Xform)
            * Object_70 (Mesh)
          * Object_73 (Xform)
            * Object_71 (Mesh)
          * Object_74 (Xform)
            * Object_72 (Mesh)
          * Object_75 (Xform)
            * Object_73 (Mesh)
          * Object_76 (Xform)
            * Object_74 (Mesh)
          * Object_77 (Xform)
            * Object_75 (Mesh)
          * Object_78 (Xform)
            * Object_76 (Mesh)
          * Object_79 (Xform)
            * Object_77 (Mesh)
          * Object_80 (Xform)
            * Object_78 (Mesh)
          * Object_81 (Xform)
            * Object_79 (Mesh)
          * Object_82 (Xform)
            * Object_80 (Mesh)
          * Object_83 (Xform)
            * Object_81 (Mesh)
          * Object_84 (Xform)
            * Object_82 (Mesh)
          * Object_85 (Xform)
            * Object_83 (Mesh)
          * Object_86 (Xform)
            * Object_84 (Mesh)
          * Object_87 (Xform)
            * Object_85 (Mesh)
          * Object_88 (Xform)
            * Object_86 (Mesh)
          * Object_89 (Xform)
            * Object_87 (Mesh)
          * Object_90 (Xform)
            * Object_88 (Mesh)
          * Object_91 (Xform)
            * Object_89 (Mesh)
          * Object_92 (Xform)
            * Object_90 (Mesh)
          * Object_93 (Xform)
            * Object_91 (Mesh)
          * Object_94 (Xform)
            * Object_92 (Mesh)
          * Object_95 (Xform)
            * Object_93 (Mesh)
          * Object_96 (Xform)
            * Object_94 (Mesh)
          * Object_97 (Xform)
            * Object_95 (Mesh)
          * Object_98 (Xform)
            * Object_96 (Mesh)
          * Object_99 (Xform)
            * Object_97 (Mesh)
          * Object_100 (Xform)
            * Object_98 (Mesh)
          * Object_101 (Xform)
            * Object_99 (Mesh)
          * Object_102 (Xform)
            * Object_100 (Mesh)
          * Object_103 (Xform)
            * Object_101 (Mesh)
          * Object_104 (Xform)
            * Object_102 (Mesh)
          * Object_105 (Xform)
            * Object_103 (Mesh)
          * Object_106 (Xform)
            * Object_104 (Mesh)
          * Object_107 (Xform)
            * Object_105 (Mesh)
          * Object_108 (Xform)
            * Object_106 (Mesh)
          * Object_109 (Xform)
            * Object_107 (Mesh)
          * Object_110 (Xform)
            * Object_108 (Mesh)
          * Object_111 (Xform)
            * Object_109 (Mesh)
          * Object_112 (Xform)
            * Object_110 (Mesh)
          * Object_113 (Xform)
            * Object_111 (Mesh)
          * Object_114 (Xform)
            * Object_112 (Mesh)
          * Object_115 (Xform)
            * Object_113 (Mesh)
          * Object_116 (Xform)
            * Object_114 (Mesh)
          * Object_117 (Xform)
            * Object_115 (Mesh)
          * Object_118 (Xform)
            * Object_116 (Mesh)
          * Object_119 (Xform)
            * Object_117 (Mesh)
          * Object_120 (Xform)
            * Object_118 (Mesh)
          * Object_121 (Xform)
            * Object_119 (Mesh)
          * Object_122 (Xform)
            * Object_120 (Mesh)
          * Object_123 (Xform)
            * Object_121 (Mesh)
          * Object_124 (Xform)
            * Object_122 (Mesh)
          * Object_125 (Xform)
            * Object_123 (Mesh)
          * Object_126 (Xform)
            * Object_124 (Mesh)
          * Object_127 (Xform)
            * Object_125 (Mesh)
          * Object_128 (Xform)
            * Object_126 (Mesh)
          * Object_129 (Xform)
            * Object_127 (Mesh)
          * Object_130 (Xform)
            * Object_128 (Mesh)
          * Object_131 (Xform)
            * Object_129 (Mesh)
          * Object_132 (Xform)
            * Object_130 (Mesh)
          * Object_133 (Xform)
            * Object_131 (Mesh)
          * Object_134 (Xform)
            * Object_132 (Mesh)
          * Object_135 (Xform)
            * Object_133 (Mesh)
          * Object_136 (Xform)
            * Object_134 (Mesh)
          * Object_137 (Xform)
            * Object_135 (Mesh)
          * Object_138 (Xform)
            * Object_136 (Mesh)
          * Object_139 (Xform)
            * Object_137 (Mesh)
          * Object_140 (Xform)
            * Object_138 (Mesh)
          * Object_141 (Xform)
            * Object_139 (Mesh)
          * Object_142 (Xform)
            * Object_140 (Mesh)
          * Object_143 (Xform)
            * Object_141 (Mesh)
          * Object_144 (Xform)
            * Object_142 (Mesh)
          * Object_145 (Xform)
            * Object_143 (Mesh)
          * Object_146 (Xform)
            * Object_144 (Mesh)
          * Object_147 (Xform)
            * Object_145 (Mesh)
          * Object_148 (Xform)
            * Object_146 (Mesh)
          * Object_149 (Xform)
            * Object_147 (Mesh)
          * Object_150 (Xform)
            * Object_148 (Mesh)
          * Object_151 (Xform)
            * Object_149 (Mesh)
          * Object_152 (Xform)
            * Object_150 (Mesh)
          * Object_153 (Xform)
            * Object_151 (Mesh)
          * Object_154 (Xform)
            * Object_152 (Mesh)
          * Object_155 (Xform)
            * Object_153 (Mesh)
          * Object_156 (Xform)
            * Object_154 (Mesh)
          * Object_157 (Xform)
            * Object_155 (Mesh)
          * Object_158 (Xform)
            * Object_156 (Mesh)
          * Object_159 (Xform)
            * Object_157 (Mesh)
          * Object_160 (Xform)
            * Object_158 (Mesh)
          * Object_161 (Xform)
            * Object_159 (Mesh)
          * Object_162 (Xform)
            * Object_160 (Mesh)
          * Object_163 (Xform)
            * Object_161 (Mesh)
          * Object_164 (Xform)
            * Object_162 (Mesh)
          * Object_165 (Xform)
            * Object_163 (Mesh)
          * Object_166 (Xform)
            * Object_164 (Mesh)
          * Object_167 (Xform)
            * Object_165 (Mesh)
          * Object_168 (Xform)
            * Object_166 (Mesh)
          * Object_169 (Xform)
            * Object_167 (Mesh)
          * Object_170 (Xform)
            * Object_168 (Mesh)
          * Object_171 (Xform)
            * Object_169 (Mesh)
          * Object_172 (Xform)
            * Object_170 (Mesh)
  * agv_2 (Xform)
    * Materials (Scope)
      * ASELSAN_CATS_04 (Material)
        * pbr_shader (Shader)
      * ASELSAN_CATS_04_2 (Material)
        * pbr_shader (Shader)
      * ASELSAN_CATS_13 (Material)
        * pbr_shader (Shader)
      * Color_000 (Material)
        * pbr_shader (Shader)
      * Color_A05 (Material)
        * pbr_shader (Shader)
      * Color_A06 (Material)
        * pbr_shader (Shader)
      * Color_B05 (Material)
        * pbr_shader (Shader)
      * Color_E02 (Material)
        * pbr_shader (Shader)
      * Color_E05 (Material)
        * pbr_shader (Shader)
      * Color_F06 (Material)
        * pbr_shader (Shader)
      * Color_G03 (Material)
        * pbr_shader (Shader)
      * Color_M02 (Material)
        * pbr_shader (Shader)
      * Color_M03 (Material)
        * pbr_shader (Shader)
      * Mtl39 (Material)
        * pbr_shader (Shader)
      * Mtl6 (Material)
        * pbr_shader (Shader)
        * uvset0 (Shader)
        * tex_base (Shader)
      * Mtl9 (Material)
        * pbr_shader (Shader)
      * Silver (Material)
        * pbr_shader (Shader)
      * material (Material)
        * pbr_shader (Shader)
        * uvset0 (Shader)
        * tex_base (Shader)
      * cash_register_keys (Material)
        * pbr_shader (Shader)
      * Chris_Shoe_Sole (Material)
        * pbr_shader (Shader)
      * Color_002 (Material)
        * pbr_shader (Shader)
      * Color_005 (Material)
        * pbr_shader (Shader)
      * Color_006 (Material)
        * pbr_shader (Shader)
      * Color_008 (Material)
        * pbr_shader (Shader)
      * Color_A01 (Material)
        * pbr_shader (Shader)
      * Color_A11 (Material)
        * pbr_shader (Shader)
      * Color_M04 (Material)
        * pbr_shader (Shader)
      * Color_M05 (Material)
        * pbr_shader (Shader)
      * Color_M06 (Material)
        * pbr_shader (Shader)
      * Color_M07 (Material)
        * pbr_shader (Shader)
      * Color_M09 (Material)
        * pbr_shader (Shader)
      * FCP_Charcoal_v2 (Material)
        * pbr_shader (Shader)
      * FrontColor (Material)
        * pbr_shader (Shader)
      * Light_Blue (Material)
        * pbr_shader (Shader)
      * M_0011_Seashell (Material)
        * pbr_shader (Shader)
      * M_0131_Silver (Material)
        * pbr_shader (Shader)
      * M_0134_DimGray (Material)
        * pbr_shader (Shader)
      * M_0135_DarkGray (Material)
        * pbr_shader (Shader)
      * Metal_Silver (Material)
        * pbr_shader (Shader)
      * Mtl1 (Material)
        * pbr_shader (Shader)
      * Mtl10 (Material)
        * pbr_shader (Shader)
      * Mtl11 (Material)
        * pbr_shader (Shader)
      * Mtl12 (Material)
        * pbr_shader (Shader)
      * Mtl13 (Material)
        * pbr_shader (Shader)
      * Mtl14 (Material)
        * pbr_shader (Shader)
      * Mtl15 (Material)
        * pbr_shader (Shader)
      * Mtl16 (Material)
        * pbr_shader (Shader)
      * Mtl17 (Material)
        * pbr_shader (Shader)
      * Mtl3 (Material)
        * pbr_shader (Shader)
      * Mtl35 (Material)
        * pbr_shader (Shader)
      * Mtl36 (Material)
        * pbr_shader (Shader)
      * Mtl37 (Material)
        * pbr_shader (Shader)
      * Mtl3a (Material)
        * pbr_shader (Shader)
      * Mtl3b (Material)
        * pbr_shader (Shader)
      * Mtl5 (Material)
        * pbr_shader (Shader)
      * Mtl7 (Material)
        * pbr_shader (Shader)
      * Mtl8 (Material)
        * pbr_shader (Shader)
      * Mtla (Material)
        * pbr_shader (Shader)
      * Mtlb1 (Material)
        * pbr_shader (Shader)
      * Stainless_Steel (Material)
        * pbr_shader (Shader)
      * Metal_Aluminum_Anodized_1 (Material)
        * pbr_shader (Shader)
      * Metal_Aluminum_Anodized_2 (Material)
        * pbr_shader (Shader)
      * basic_gray_plastic (Material)
        * pbr_shader (Shader)
      * texture (Material)
        * pbr_shader (Shader)
    * Meshes (Xform)
      * Sketchfab_model (Xform)
        * AGV_ready_1_obj_cleaner_materialmerger_gles (Xform)
          * Object_2 (Xform)
            * Object_0 (Mesh)
          * Object_3 (Xform)
            * Object_1 (Mesh)
          * Object_4 (Xform)
            * Object_2 (Mesh)
          * Object_5 (Xform)
            * Object_3 (Mesh)
          * Object_6 (Xform)
            * Object_4 (Mesh)
          * Object_7 (Xform)
            * Object_5 (Mesh)
          * Object_8 (Xform)
            * Object_6 (Mesh)
          * Object_9 (Xform)
            * Object_7 (Mesh)
          * Object_10 (Xform)
            * Object_8 (Mesh)
          * Object_11 (Xform)
            * Object_9 (Mesh)
          * Object_12 (Xform)
            * Object_10 (Mesh)
          * Object_13 (Xform)
            * Object_11 (Mesh)
          * Object_14 (Xform)
            * Object_12 (Mesh)
          * Object_15 (Xform)
            * Object_13 (Mesh)
          * Object_16 (Xform)
            * Object_14 (Mesh)
          * Object_17 (Xform)
            * Object_15 (Mesh)
          * Object_18 (Xform)
            * Object_16 (Mesh)
          * Object_19 (Xform)
            * Object_17 (Mesh)
          * Object_20 (Xform)
            * Object_18 (Mesh)
          * Object_21 (Xform)
            * Object_19 (Mesh)
          * Object_22 (Xform)
            * Object_20 (Mesh)
          * Object_23 (Xform)
            * Object_21 (Mesh)
          * Object_24 (Xform)
            * Object_22 (Mesh)
          * Object_25 (Xform)
            * Object_23 (Mesh)
          * Object_26 (Xform)
            * Object_24 (Mesh)
          * Object_27 (Xform)
            * Object_25 (Mesh)
          * Object_28 (Xform)
            * Object_26 (Mesh)
          * Object_29 (Xform)
            * Object_27 (Mesh)
          * Object_30 (Xform)
            * Object_28 (Mesh)
          * Object_31 (Xform)
            * Object_29 (Mesh)
          * Object_32 (Xform)
            * Object_30 (Mesh)
          * Object_33 (Xform)
            * Object_31 (Mesh)
          * Object_34 (Xform)
            * Object_32 (Mesh)
          * Object_35 (Xform)
            * Object_33 (Mesh)
          * Object_36 (Xform)
            * Object_34 (Mesh)
          * Object_37 (Xform)
            * Object_35 (Mesh)
          * Object_38 (Xform)
            * Object_36 (Mesh)
          * Object_39 (Xform)
            * Object_37 (Mesh)
          * Object_40 (Xform)
            * Object_38 (Mesh)
          * Object_41 (Xform)
            * Object_39 (Mesh)
          * Object_42 (Xform)
            * Object_40 (Mesh)
          * Object_43 (Xform)
            * Object_41 (Mesh)
          * Object_44 (Xform)
            * Object_42 (Mesh)
          * Object_45 (Xform)
            * Object_43 (Mesh)
          * Object_46 (Xform)
            * Object_44 (Mesh)
          * Object_47 (Xform)
            * Object_45 (Mesh)
          * Object_48 (Xform)
            * Object_46 (Mesh)
          * Object_49 (Xform)
            * Object_47 (Mesh)
          * Object_50 (Xform)
            * Object_48 (Mesh)
          * Object_51 (Xform)
            * Object_49 (Mesh)
          * Object_52 (Xform)
            * Object_50 (Mesh)
          * Object_53 (Xform)
            * Object_51 (Mesh)
          * Object_54 (Xform)
            * Object_52 (Mesh)
          * Object_55 (Xform)
            * Object_53 (Mesh)
          * Object_56 (Xform)
            * Object_54 (Mesh)
          * Object_57 (Xform)
            * Object_55 (Mesh)
          * Object_58 (Xform)
            * Object_56 (Mesh)
          * Object_59 (Xform)
            * Object_57 (Mesh)
          * Object_60 (Xform)
            * Object_58 (Mesh)
          * Object_61 (Xform)
            * Object_59 (Mesh)
          * Object_62 (Xform)
            * Object_60 (Mesh)
          * Object_63 (Xform)
            * Object_61 (Mesh)
          * Object_64 (Xform)
            * Object_62 (Mesh)
          * Object_65 (Xform)
            * Object_63 (Mesh)
          * Object_66 (Xform)
            * Object_64 (Mesh)
          * Object_67 (Xform)
            * Object_65 (Mesh)
          * Object_68 (Xform)
            * Object_66 (Mesh)
          * Object_69 (Xform)
            * Object_67 (Mesh)
          * Object_70 (Xform)
            * Object_68 (Mesh)
          * Object_71 (Xform)
            * Object_69 (Mesh)
          * Object_72 (Xform)
            * Object_70 (Mesh)
          * Object_73 (Xform)
            * Object_71 (Mesh)
          * Object_74 (Xform)
            * Object_72 (Mesh)
          * Object_75 (Xform)
            * Object_73 (Mesh)
          * Object_76 (Xform)
            * Object_74 (Mesh)
          * Object_77 (Xform)
            * Object_75 (Mesh)
          * Object_78 (Xform)
            * Object_76 (Mesh)
          * Object_79 (Xform)
            * Object_77 (Mesh)
          * Object_80 (Xform)
            * Object_78 (Mesh)
          * Object_81 (Xform)
            * Object_79 (Mesh)
          * Object_82 (Xform)
            * Object_80 (Mesh)
          * Object_83 (Xform)
            * Object_81 (Mesh)
          * Object_84 (Xform)
            * Object_82 (Mesh)
          * Object_85 (Xform)
            * Object_83 (Mesh)
          * Object_86 (Xform)
            * Object_84 (Mesh)
          * Object_87 (Xform)
            * Object_85 (Mesh)
          * Object_88 (Xform)
            * Object_86 (Mesh)
          * Object_89 (Xform)
            * Object_87 (Mesh)
          * Object_90 (Xform)
            * Object_88 (Mesh)
          * Object_91 (Xform)
            * Object_89 (Mesh)
          * Object_92 (Xform)
            * Object_90 (Mesh)
          * Object_93 (Xform)
            * Object_91 (Mesh)
          * Object_94 (Xform)
            * Object_92 (Mesh)
          * Object_95 (Xform)
            * Object_93 (Mesh)
          * Object_96 (Xform)
            * Object_94 (Mesh)
          * Object_97 (Xform)
            * Object_95 (Mesh)
          * Object_98 (Xform)
            * Object_96 (Mesh)
          * Object_99 (Xform)
            * Object_97 (Mesh)
          * Object_100 (Xform)
            * Object_98 (Mesh)
          * Object_101 (Xform)
            * Object_99 (Mesh)
          * Object_102 (Xform)
            * Object_100 (Mesh)
          * Object_103 (Xform)
            * Object_101 (Mesh)
          * Object_104 (Xform)
            * Object_102 (Mesh)
          * Object_105 (Xform)
            * Object_103 (Mesh)
          * Object_106 (Xform)
            * Object_104 (Mesh)
          * Object_107 (Xform)
            * Object_105 (Mesh)
          * Object_108 (Xform)
            * Object_106 (Mesh)
          * Object_109 (Xform)
            * Object_107 (Mesh)
          * Object_110 (Xform)
            * Object_108 (Mesh)
          * Object_111 (Xform)
            * Object_109 (Mesh)
          * Object_112 (Xform)
            * Object_110 (Mesh)
          * Object_113 (Xform)
            * Object_111 (Mesh)
          * Object_114 (Xform)
            * Object_112 (Mesh)
          * Object_115 (Xform)
            * Object_113 (Mesh)
          * Object_116 (Xform)
            * Object_114 (Mesh)
          * Object_117 (Xform)
            * Object_115 (Mesh)
          * Object_118 (Xform)
            * Object_116 (Mesh)
          * Object_119 (Xform)
            * Object_117 (Mesh)
          * Object_120 (Xform)
            * Object_118 (Mesh)
          * Object_121 (Xform)
            * Object_119 (Mesh)
          * Object_122 (Xform)
            * Object_120 (Mesh)
          * Object_123 (Xform)
            * Object_121 (Mesh)
          * Object_124 (Xform)
            * Object_122 (Mesh)
          * Object_125 (Xform)
            * Object_123 (Mesh)
          * Object_126 (Xform)
            * Object_124 (Mesh)
          * Object_127 (Xform)
            * Object_125 (Mesh)
          * Object_128 (Xform)
            * Object_126 (Mesh)
          * Object_129 (Xform)
            * Object_127 (Mesh)
          * Object_130 (Xform)
            * Object_128 (Mesh)
          * Object_131 (Xform)
            * Object_129 (Mesh)
          * Object_132 (Xform)
            * Object_130 (Mesh)
          * Object_133 (Xform)
            * Object_131 (Mesh)
          * Object_134 (Xform)
            * Object_132 (Mesh)
          * Object_135 (Xform)
            * Object_133 (Mesh)
          * Object_136 (Xform)
            * Object_134 (Mesh)
          * Object_137 (Xform)
            * Object_135 (Mesh)
          * Object_138 (Xform)
            * Object_136 (Mesh)
          * Object_139 (Xform)
            * Object_137 (Mesh)
          * Object_140 (Xform)
            * Object_138 (Mesh)
          * Object_141 (Xform)
            * Object_139 (Mesh)
          * Object_142 (Xform)
            * Object_140 (Mesh)
          * Object_143 (Xform)
            * Object_141 (Mesh)
          * Object_144 (Xform)
            * Object_142 (Mesh)
          * Object_145 (Xform)
            * Object_143 (Mesh)
          * Object_146 (Xform)
            * Object_144 (Mesh)
          * Object_147 (Xform)
            * Object_145 (Mesh)
          * Object_148 (Xform)
            * Object_146 (Mesh)
          * Object_149 (Xform)
            * Object_147 (Mesh)
          * Object_150 (Xform)
            * Object_148 (Mesh)
          * Object_151 (Xform)
            * Object_149 (Mesh)
          * Object_152 (Xform)
            * Object_150 (Mesh)
          * Object_153 (Xform)
            * Object_151 (Mesh)
          * Object_154 (Xform)
            * Object_152 (Mesh)
          * Object_155 (Xform)
            * Object_153 (Mesh)
          * Object_156 (Xform)
            * Object_154 (Mesh)
          * Object_157 (Xform)
            * Object_155 (Mesh)
          * Object_158 (Xform)
            * Object_156 (Mesh)
          * Object_159 (Xform)
            * Object_157 (Mesh)
          * Object_160 (Xform)
            * Object_158 (Mesh)
          * Object_161 (Xform)
            * Object_159 (Mesh)
          * Object_162 (Xform)
            * Object_160 (Mesh)
          * Object_163 (Xform)
            * Object_161 (Mesh)
          * Object_164 (Xform)
            * Object_162 (Mesh)
          * Object_165 (Xform)
            * Object_163 (Mesh)
          * Object_166 (Xform)
            * Object_164 (Mesh)
          * Object_167 (Xform)
            * Object_165 (Mesh)
          * Object_168 (Xform)
            * Object_166 (Mesh)
          * Object_169 (Xform)
            * Object_167 (Mesh)
          * Object_170 (Xform)
            * Object_168 (Mesh)
          * Object_171 (Xform)
            * Object_169 (Mesh)
          * Object_172 (Xform)
            * Object_170 (Mesh)
  * agv_3 (Xform)
    * Materials (Scope)
      * ASELSAN_CATS_04 (Material)
        * pbr_shader (Shader)
      * ASELSAN_CATS_04_2 (Material)
        * pbr_shader (Shader)
      * ASELSAN_CATS_13 (Material)
        * pbr_shader (Shader)
      * Color_000 (Material)
        * pbr_shader (Shader)
      * Color_A05 (Material)
        * pbr_shader (Shader)
      * Color_A06 (Material)
        * pbr_shader (Shader)
      * Color_B05 (Material)
        * pbr_shader (Shader)
      * Color_E02 (Material)
        * pbr_shader (Shader)
      * Color_E05 (Material)
        * pbr_shader (Shader)
      * Color_F06 (Material)
        * pbr_shader (Shader)
      * Color_G03 (Material)
        * pbr_shader (Shader)
      * Color_M02 (Material)
        * pbr_shader (Shader)
      * Color_M03 (Material)
        * pbr_shader (Shader)
      * Mtl39 (Material)
        * pbr_shader (Shader)
      * Mtl6 (Material)
        * pbr_shader (Shader)
        * uvset0 (Shader)
        * tex_base (Shader)
      * Mtl9 (Material)
        * pbr_shader (Shader)
      * Silver (Material)
        * pbr_shader (Shader)
      * material (Material)
        * pbr_shader (Shader)
        * uvset0 (Shader)
        * tex_base (Shader)
      * cash_register_keys (Material)
        * pbr_shader (Shader)
      * Chris_Shoe_Sole (Material)
        * pbr_shader (Shader)
      * Color_002 (Material)
        * pbr_shader (Shader)
      * Color_005 (Material)
        * pbr_shader (Shader)
      * Color_006 (Material)
        * pbr_shader (Shader)
      * Color_008 (Material)
        * pbr_shader (Shader)
      * Color_A01 (Material)
        * pbr_shader (Shader)
      * Color_A11 (Material)
        * pbr_shader (Shader)
      * Color_M04 (Material)
        * pbr_shader (Shader)
      * Color_M05 (Material)
        * pbr_shader (Shader)
      * Color_M06 (Material)
        * pbr_shader (Shader)
      * Color_M07 (Material)
        * pbr_shader (Shader)
      * Color_M09 (Material)
        * pbr_shader (Shader)
      * FCP_Charcoal_v2 (Material)
        * pbr_shader (Shader)
      * FrontColor (Material)
        * pbr_shader (Shader)
      * Light_Blue (Material)
        * pbr_shader (Shader)
      * M_0011_Seashell (Material)
        * pbr_shader (Shader)
      * M_0131_Silver (Material)
        * pbr_shader (Shader)
      * M_0134_DimGray (Material)
        * pbr_shader (Shader)
      * M_0135_DarkGray (Material)
        * pbr_shader (Shader)
      * Metal_Silver (Material)
        * pbr_shader (Shader)
      * Mtl1 (Material)
        * pbr_shader (Shader)
      * Mtl10 (Material)
        * pbr_shader (Shader)
      * Mtl11 (Material)
        * pbr_shader (Shader)
      * Mtl12 (Material)
        * pbr_shader (Shader)
      * Mtl13 (Material)
        * pbr_shader (Shader)
      * Mtl14 (Material)
        * pbr_shader (Shader)
      * Mtl15 (Material)
        * pbr_shader (Shader)
      * Mtl16 (Material)
        * pbr_shader (Shader)
      * Mtl17 (Material)
        * pbr_shader (Shader)
      * Mtl3 (Material)
        * pbr_shader (Shader)
      * Mtl35 (Material)
        * pbr_shader (Shader)
      * Mtl36 (Material)
        * pbr_shader (Shader)
      * Mtl37 (Material)
        * pbr_shader (Shader)
      * Mtl3a (Material)
        * pbr_shader (Shader)
      * Mtl3b (Material)
        * pbr_shader (Shader)
      * Mtl5 (Material)
        * pbr_shader (Shader)
      * Mtl7 (Material)
        * pbr_shader (Shader)
      * Mtl8 (Material)
        * pbr_shader (Shader)
      * Mtla (Material)
        * pbr_shader (Shader)
      * Mtlb1 (Material)
        * pbr_shader (Shader)
      * Stainless_Steel (Material)
        * pbr_shader (Shader)
      * Metal_Aluminum_Anodized_1 (Material)
        * pbr_shader (Shader)
      * Metal_Aluminum_Anodized_2 (Material)
        * pbr_shader (Shader)
      * basic_gray_plastic (Material)
        * pbr_shader (Shader)
      * texture (Material)
        * pbr_shader (Shader)
    * Meshes (Xform)
      * Sketchfab_model (Xform)
        * AGV_ready_1_obj_cleaner_materialmerger_gles (Xform)
          * Object_2 (Xform)
            * Object_0 (Mesh)
          * Object_3 (Xform)
            * Object_1 (Mesh)
          * Object_4 (Xform)
            * Object_2 (Mesh)
          * Object_5 (Xform)
            * Object_3 (Mesh)
          * Object_6 (Xform)
            * Object_4 (Mesh)
          * Object_7 (Xform)
            * Object_5 (Mesh)
          * Object_8 (Xform)
            * Object_6 (Mesh)
          * Object_9 (Xform)
            * Object_7 (Mesh)
          * Object_10 (Xform)
            * Object_8 (Mesh)
          * Object_11 (Xform)
            * Object_9 (Mesh)
          * Object_12 (Xform)
            * Object_10 (Mesh)
          * Object_13 (Xform)
            * Object_11 (Mesh)
          * Object_14 (Xform)
            * Object_12 (Mesh)
          * Object_15 (Xform)
            * Object_13 (Mesh)
          * Object_16 (Xform)
            * Object_14 (Mesh)
          * Object_17 (Xform)
            * Object_15 (Mesh)
          * Object_18 (Xform)
            * Object_16 (Mesh)
          * Object_19 (Xform)
            * Object_17 (Mesh)
          * Object_20 (Xform)
            * Object_18 (Mesh)
          * Object_21 (Xform)
            * Object_19 (Mesh)
          * Object_22 (Xform)
            * Object_20 (Mesh)
          * Object_23 (Xform)
            * Object_21 (Mesh)
          * Object_24 (Xform)
            * Object_22 (Mesh)
          * Object_25 (Xform)
            * Object_23 (Mesh)
          * Object_26 (Xform)
            * Object_24 (Mesh)
          * Object_27 (Xform)
            * Object_25 (Mesh)
          * Object_28 (Xform)
            * Object_26 (Mesh)
          * Object_29 (Xform)
            * Object_27 (Mesh)
          * Object_30 (Xform)
            * Object_28 (Mesh)
          * Object_31 (Xform)
            * Object_29 (Mesh)
          * Object_32 (Xform)
            * Object_30 (Mesh)
          * Object_33 (Xform)
            * Object_31 (Mesh)
          * Object_34 (Xform)
            * Object_32 (Mesh)
          * Object_35 (Xform)
            * Object_33 (Mesh)
          * Object_36 (Xform)
            * Object_34 (Mesh)
          * Object_37 (Xform)
            * Object_35 (Mesh)
          * Object_38 (Xform)
            * Object_36 (Mesh)
          * Object_39 (Xform)
            * Object_37 (Mesh)
          * Object_40 (Xform)
            * Object_38 (Mesh)
          * Object_41 (Xform)
            * Object_39 (Mesh)
          * Object_42 (Xform)
            * Object_40 (Mesh)
          * Object_43 (Xform)
            * Object_41 (Mesh)
          * Object_44 (Xform)
            * Object_42 (Mesh)
          * Object_45 (Xform)
            * Object_43 (Mesh)
          * Object_46 (Xform)
            * Object_44 (Mesh)
          * Object_47 (Xform)
            * Object_45 (Mesh)
          * Object_48 (Xform)
            * Object_46 (Mesh)
          * Object_49 (Xform)
            * Object_47 (Mesh)
          * Object_50 (Xform)
            * Object_48 (Mesh)
          * Object_51 (Xform)
            * Object_49 (Mesh)
          * Object_52 (Xform)
            * Object_50 (Mesh)
          * Object_53 (Xform)
            * Object_51 (Mesh)
          * Object_54 (Xform)
            * Object_52 (Mesh)
          * Object_55 (Xform)
            * Object_53 (Mesh)
          * Object_56 (Xform)
            * Object_54 (Mesh)
          * Object_57 (Xform)
            * Object_55 (Mesh)
          * Object_58 (Xform)
            * Object_56 (Mesh)
          * Object_59 (Xform)
            * Object_57 (Mesh)
          * Object_60 (Xform)
            * Object_58 (Mesh)
          * Object_61 (Xform)
            * Object_59 (Mesh)
          * Object_62 (Xform)
            * Object_60 (Mesh)
          * Object_63 (Xform)
            * Object_61 (Mesh)
          * Object_64 (Xform)
            * Object_62 (Mesh)
          * Object_65 (Xform)
            * Object_63 (Mesh)
          * Object_66 (Xform)
            * Object_64 (Mesh)
          * Object_67 (Xform)
            * Object_65 (Mesh)
          * Object_68 (Xform)
            * Object_66 (Mesh)
          * Object_69 (Xform)
            * Object_67 (Mesh)
          * Object_70 (Xform)
            * Object_68 (Mesh)
          * Object_71 (Xform)
            * Object_69 (Mesh)
          * Object_72 (Xform)
            * Object_70 (Mesh)
          * Object_73 (Xform)
            * Object_71 (Mesh)
          * Object_74 (Xform)
            * Object_72 (Mesh)
          * Object_75 (Xform)
            * Object_73 (Mesh)
          * Object_76 (Xform)
            * Object_74 (Mesh)
          * Object_77 (Xform)
            * Object_75 (Mesh)
          * Object_78 (Xform)
            * Object_76 (Mesh)
          * Object_79 (Xform)
            * Object_77 (Mesh)
          * Object_80 (Xform)
            * Object_78 (Mesh)
          * Object_81 (Xform)
            * Object_79 (Mesh)
          * Object_82 (Xform)
            * Object_80 (Mesh)
          * Object_83 (Xform)
            * Object_81 (Mesh)
          * Object_84 (Xform)
            * Object_82 (Mesh)
          * Object_85 (Xform)
            * Object_83 (Mesh)
          * Object_86 (Xform)
            * Object_84 (Mesh)
          * Object_87 (Xform)
            * Object_85 (Mesh)
          * Object_88 (Xform)
            * Object_86 (Mesh)
          * Object_89 (Xform)
            * Object_87 (Mesh)
          * Object_90 (Xform)
            * Object_88 (Mesh)
          * Object_91 (Xform)
            * Object_89 (Mesh)
          * Object_92 (Xform)
            * Object_90 (Mesh)
          * Object_93 (Xform)
            * Object_91 (Mesh)
          * Object_94 (Xform)
            * Object_92 (Mesh)
          * Object_95 (Xform)
            * Object_93 (Mesh)
          * Object_96 (Xform)
            * Object_94 (Mesh)
          * Object_97 (Xform)
            * Object_95 (Mesh)
          * Object_98 (Xform)
            * Object_96 (Mesh)
          * Object_99 (Xform)
            * Object_97 (Mesh)
          * Object_100 (Xform)
            * Object_98 (Mesh)
          * Object_101 (Xform)
            * Object_99 (Mesh)
          * Object_102 (Xform)
            * Object_100 (Mesh)
          * Object_103 (Xform)
            * Object_101 (Mesh)
          * Object_104 (Xform)
            * Object_102 (Mesh)
          * Object_105 (Xform)
            * Object_103 (Mesh)
          * Object_106 (Xform)
            * Object_104 (Mesh)
          * Object_107 (Xform)
            * Object_105 (Mesh)
          * Object_108 (Xform)
            * Object_106 (Mesh)
          * Object_109 (Xform)
            * Object_107 (Mesh)
          * Object_110 (Xform)
            * Object_108 (Mesh)
          * Object_111 (Xform)
            * Object_109 (Mesh)
          * Object_112 (Xform)
            * Object_110 (Mesh)
          * Object_113 (Xform)
            * Object_111 (Mesh)
          * Object_114 (Xform)
            * Object_112 (Mesh)
          * Object_115 (Xform)
            * Object_113 (Mesh)
          * Object_116 (Xform)
            * Object_114 (Mesh)
          * Object_117 (Xform)
            * Object_115 (Mesh)
          * Object_118 (Xform)
            * Object_116 (Mesh)
          * Object_119 (Xform)
            * Object_117 (Mesh)
          * Object_120 (Xform)
            * Object_118 (Mesh)
          * Object_121 (Xform)
            * Object_119 (Mesh)
          * Object_122 (Xform)
            * Object_120 (Mesh)
          * Object_123 (Xform)
            * Object_121 (Mesh)
          * Object_124 (Xform)
            * Object_122 (Mesh)
          * Object_125 (Xform)
            * Object_123 (Mesh)
          * Object_126 (Xform)
            * Object_124 (Mesh)
          * Object_127 (Xform)
            * Object_125 (Mesh)
          * Object_128 (Xform)
            * Object_126 (Mesh)
          * Object_129 (Xform)
            * Object_127 (Mesh)
          * Object_130 (Xform)
            * Object_128 (Mesh)
          * Object_131 (Xform)
            * Object_129 (Mesh)
          * Object_132 (Xform)
            * Object_130 (Mesh)
          * Object_133 (Xform)
            * Object_131 (Mesh)
          * Object_134 (Xform)
            * Object_132 (Mesh)
          * Object_135 (Xform)
            * Object_133 (Mesh)
          * Object_136 (Xform)
            * Object_134 (Mesh)
          * Object_137 (Xform)
            * Object_135 (Mesh)
          * Object_138 (Xform)
            * Object_136 (Mesh)
          * Object_139 (Xform)
            * Object_137 (Mesh)
          * Object_140 (Xform)
            * Object_138 (Mesh)
          * Object_141 (Xform)
            * Object_139 (Mesh)
          * Object_142 (Xform)
            * Object_140 (Mesh)
          * Object_143 (Xform)
            * Object_141 (Mesh)
          * Object_144 (Xform)
            * Object_142 (Mesh)
          * Object_145 (Xform)
            * Object_143 (Mesh)
          * Object_146 (Xform)
            * Object_144 (Mesh)
          * Object_147 (Xform)
            * Object_145 (Mesh)
          * Object_148 (Xform)
            * Object_146 (Mesh)
          * Object_149 (Xform)
            * Object_147 (Mesh)
          * Object_150 (Xform)
            * Object_148 (Mesh)
          * Object_151 (Xform)
            * Object_149 (Mesh)
          * Object_152 (Xform)
            * Object_150 (Mesh)
          * Object_153 (Xform)
            * Object_151 (Mesh)
          * Object_154 (Xform)
            * Object_152 (Mesh)
          * Object_155 (Xform)
            * Object_153 (Mesh)
          * Object_156 (Xform)
            * Object_154 (Mesh)
          * Object_157 (Xform)
            * Object_155 (Mesh)
          * Object_158 (Xform)
            * Object_156 (Mesh)
          * Object_159 (Xform)
            * Object_157 (Mesh)
          * Object_160 (Xform)
            * Object_158 (Mesh)
          * Object_161 (Xform)
            * Object_159 (Mesh)
          * Object_162 (Xform)
            * Object_160 (Mesh)
          * Object_163 (Xform)
            * Object_161 (Mesh)
          * Object_164 (Xform)
            * Object_162 (Mesh)
          * Object_165 (Xform)
            * Object_163 (Mesh)
          * Object_166 (Xform)
            * Object_164 (Mesh)
          * Object_167 (Xform)
            * Object_165 (Mesh)
          * Object_168 (Xform)
            * Object_166 (Mesh)
          * Object_169 (Xform)
            * Object_167 (Mesh)
          * Object_170 (Xform)
            * Object_168 (Mesh)
          * Object_171 (Xform)
            * Object_169 (Mesh)
          * Object_172 (Xform)
            * Object_170 (Mesh)
  * agv_4 (Xform)
    * Materials (Scope)
      * ASELSAN_CATS_04 (Material)
        * pbr_shader (Shader)
      * ASELSAN_CATS_04_2 (Material)
        * pbr_shader (Shader)
      * ASELSAN_CATS_13 (Material)
        * pbr_shader (Shader)
      * Color_000 (Material)
        * pbr_shader (Shader)
      * Color_A05 (Material)
        * pbr_shader (Shader)
      * Color_A06 (Material)
        * pbr_shader (Shader)
      * Color_B05 (Material)
        * pbr_shader (Shader)
      * Color_E02 (Material)
        * pbr_shader (Shader)
      * Color_E05 (Material)
        * pbr_shader (Shader)
      * Color_F06 (Material)
        * pbr_shader (Shader)
      * Color_G03 (Material)
        * pbr_shader (Shader)
      * Color_M02 (Material)
        * pbr_shader (Shader)
      * Color_M03 (Material)
        * pbr_shader (Shader)
      * Mtl39 (Material)
        * pbr_shader (Shader)
      * Mtl6 (Material)
        * pbr_shader (Shader)
        * uvset0 (Shader)
        * tex_base (Shader)
      * Mtl9 (Material)
        * pbr_shader (Shader)
      * Silver (Material)
        * pbr_shader (Shader)
      * material (Material)
        * pbr_shader (Shader)
        * uvset0 (Shader)
        * tex_base (Shader)
      * cash_register_keys (Material)
        * pbr_shader (Shader)
      * Chris_Shoe_Sole (Material)
        * pbr_shader (Shader)
      * Color_002 (Material)
        * pbr_shader (Shader)
      * Color_005 (Material)
        * pbr_shader (Shader)
      * Color_006 (Material)
        * pbr_shader (Shader)
      * Color_008 (Material)
        * pbr_shader (Shader)
      * Color_A01 (Material)
        * pbr_shader (Shader)
      * Color_A11 (Material)
        * pbr_shader (Shader)
      * Color_M04 (Material)
        * pbr_shader (Shader)
      * Color_M05 (Material)
        * pbr_shader (Shader)
      * Color_M06 (Material)
        * pbr_shader (Shader)
      * Color_M07 (Material)
        * pbr_shader (Shader)
      * Color_M09 (Material)
        * pbr_shader (Shader)
      * FCP_Charcoal_v2 (Material)
        * pbr_shader (Shader)
      * FrontColor (Material)
        * pbr_shader (Shader)
      * Light_Blue (Material)
        * pbr_shader (Shader)
      * M_0011_Seashell (Material)
        * pbr_shader (Shader)
      * M_0131_Silver (Material)
        * pbr_shader (Shader)
      * M_0134_DimGray (Material)
        * pbr_shader (Shader)
      * M_0135_DarkGray (Material)
        * pbr_shader (Shader)
      * Metal_Silver (Material)
        * pbr_shader (Shader)
      * Mtl1 (Material)
        * pbr_shader (Shader)
      * Mtl10 (Material)
        * pbr_shader (Shader)
      * Mtl11 (Material)
        * pbr_shader (Shader)
      * Mtl12 (Material)
        * pbr_shader (Shader)
      * Mtl13 (Material)
        * pbr_shader (Shader)
      * Mtl14 (Material)
        * pbr_shader (Shader)
      * Mtl15 (Material)
        * pbr_shader (Shader)
      * Mtl16 (Material)
        * pbr_shader (Shader)
      * Mtl17 (Material)
        * pbr_shader (Shader)
      * Mtl3 (Material)
        * pbr_shader (Shader)
      * Mtl35 (Material)
        * pbr_shader (Shader)
      * Mtl36 (Material)
        * pbr_shader (Shader)
      * Mtl37 (Material)
        * pbr_shader (Shader)
      * Mtl3a (Material)
        * pbr_shader (Shader)
      * Mtl3b (Material)
        * pbr_shader (Shader)
      * Mtl5 (Material)
        * pbr_shader (Shader)
      * Mtl7 (Material)
        * pbr_shader (Shader)
      * Mtl8 (Material)
        * pbr_shader (Shader)
      * Mtla (Material)
        * pbr_shader (Shader)
      * Mtlb1 (Material)
        * pbr_shader (Shader)
      * Stainless_Steel (Material)
        * pbr_shader (Shader)
      * Metal_Aluminum_Anodized_1 (Material)
        * pbr_shader (Shader)
      * Metal_Aluminum_Anodized_2 (Material)
        * pbr_shader (Shader)
      * basic_gray_plastic (Material)
        * pbr_shader (Shader)
      * texture (Material)
        * pbr_shader (Shader)
    * Meshes (Xform)
      * Sketchfab_model (Xform)
        * AGV_ready_1_obj_cleaner_materialmerger_gles (Xform)
          * Object_2 (Xform)
            * Object_0 (Mesh)
          * Object_3 (Xform)
            * Object_1 (Mesh)
          * Object_4 (Xform)
            * Object_2 (Mesh)
          * Object_5 (Xform)
            * Object_3 (Mesh)
          * Object_6 (Xform)
            * Object_4 (Mesh)
          * Object_7 (Xform)
            * Object_5 (Mesh)
          * Object_8 (Xform)
            * Object_6 (Mesh)
          * Object_9 (Xform)
            * Object_7 (Mesh)
          * Object_10 (Xform)
            * Object_8 (Mesh)
          * Object_11 (Xform)
            * Object_9 (Mesh)
          * Object_12 (Xform)
            * Object_10 (Mesh)
          * Object_13 (Xform)
            * Object_11 (Mesh)
          * Object_14 (Xform)
            * Object_12 (Mesh)
          * Object_15 (Xform)
            * Object_13 (Mesh)
          * Object_16 (Xform)
            * Object_14 (Mesh)
          * Object_17 (Xform)
            * Object_15 (Mesh)
          * Object_18 (Xform)
            * Object_16 (Mesh)
          * Object_19 (Xform)
            * Object_17 (Mesh)
          * Object_20 (Xform)
            * Object_18 (Mesh)
          * Object_21 (Xform)
            * Object_19 (Mesh)
          * Object_22 (Xform)
            * Object_20 (Mesh)
          * Object_23 (Xform)
            * Object_21 (Mesh)
          * Object_24 (Xform)
            * Object_22 (Mesh)
          * Object_25 (Xform)
            * Object_23 (Mesh)
          * Object_26 (Xform)
            * Object_24 (Mesh)
          * Object_27 (Xform)
            * Object_25 (Mesh)
          * Object_28 (Xform)
            * Object_26 (Mesh)
          * Object_29 (Xform)
            * Object_27 (Mesh)
          * Object_30 (Xform)
            * Object_28 (Mesh)
          * Object_31 (Xform)
            * Object_29 (Mesh)
          * Object_32 (Xform)
            * Object_30 (Mesh)
          * Object_33 (Xform)
            * Object_31 (Mesh)
          * Object_34 (Xform)
            * Object_32 (Mesh)
          * Object_35 (Xform)
            * Object_33 (Mesh)
          * Object_36 (Xform)
            * Object_34 (Mesh)
          * Object_37 (Xform)
            * Object_35 (Mesh)
          * Object_38 (Xform)
            * Object_36 (Mesh)
          * Object_39 (Xform)
            * Object_37 (Mesh)
          * Object_40 (Xform)
            * Object_38 (Mesh)
          * Object_41 (Xform)
            * Object_39 (Mesh)
          * Object_42 (Xform)
            * Object_40 (Mesh)
          * Object_43 (Xform)
            * Object_41 (Mesh)
          * Object_44 (Xform)
            * Object_42 (Mesh)
          * Object_45 (Xform)
            * Object_43 (Mesh)
          * Object_46 (Xform)
            * Object_44 (Mesh)
          * Object_47 (Xform)
            * Object_45 (Mesh)
          * Object_48 (Xform)
            * Object_46 (Mesh)
          * Object_49 (Xform)
            * Object_47 (Mesh)
          * Object_50 (Xform)
            * Object_48 (Mesh)
          * Object_51 (Xform)
            * Object_49 (Mesh)
          * Object_52 (Xform)
            * Object_50 (Mesh)
          * Object_53 (Xform)
            * Object_51 (Mesh)
          * Object_54 (Xform)
            * Object_52 (Mesh)
          * Object_55 (Xform)
            * Object_53 (Mesh)
          * Object_56 (Xform)
            * Object_54 (Mesh)
          * Object_57 (Xform)
            * Object_55 (Mesh)
          * Object_58 (Xform)
            * Object_56 (Mesh)
          * Object_59 (Xform)
            * Object_57 (Mesh)
          * Object_60 (Xform)
            * Object_58 (Mesh)
          * Object_61 (Xform)
            * Object_59 (Mesh)
          * Object_62 (Xform)
            * Object_60 (Mesh)
          * Object_63 (Xform)
            * Object_61 (Mesh)
          * Object_64 (Xform)
            * Object_62 (Mesh)
          * Object_65 (Xform)
            * Object_63 (Mesh)
          * Object_66 (Xform)
            * Object_64 (Mesh)
          * Object_67 (Xform)
            * Object_65 (Mesh)
          * Object_68 (Xform)
            * Object_66 (Mesh)
          * Object_69 (Xform)
            * Object_67 (Mesh)
          * Object_70 (Xform)
            * Object_68 (Mesh)
          * Object_71 (Xform)
            * Object_69 (Mesh)
          * Object_72 (Xform)
            * Object_70 (Mesh)
          * Object_73 (Xform)
            * Object_71 (Mesh)
          * Object_74 (Xform)
            * Object_72 (Mesh)
          * Object_75 (Xform)
            * Object_73 (Mesh)
          * Object_76 (Xform)
            * Object_74 (Mesh)
          * Object_77 (Xform)
            * Object_75 (Mesh)
          * Object_78 (Xform)
            * Object_76 (Mesh)
          * Object_79 (Xform)
            * Object_77 (Mesh)
          * Object_80 (Xform)
            * Object_78 (Mesh)
          * Object_81 (Xform)
            * Object_79 (Mesh)
          * Object_82 (Xform)
            * Object_80 (Mesh)
          * Object_83 (Xform)
            * Object_81 (Mesh)
          * Object_84 (Xform)
            * Object_82 (Mesh)
          * Object_85 (Xform)
            * Object_83 (Mesh)
          * Object_86 (Xform)
            * Object_84 (Mesh)
          * Object_87 (Xform)
            * Object_85 (Mesh)
          * Object_88 (Xform)
            * Object_86 (Mesh)
          * Object_89 (Xform)
            * Object_87 (Mesh)
          * Object_90 (Xform)
            * Object_88 (Mesh)
          * Object_91 (Xform)
            * Object_89 (Mesh)
          * Object_92 (Xform)
            * Object_90 (Mesh)
          * Object_93 (Xform)
            * Object_91 (Mesh)
          * Object_94 (Xform)
            * Object_92 (Mesh)
          * Object_95 (Xform)
            * Object_93 (Mesh)
          * Object_96 (Xform)
            * Object_94 (Mesh)
          * Object_97 (Xform)
            * Object_95 (Mesh)
          * Object_98 (Xform)
            * Object_96 (Mesh)
          * Object_99 (Xform)
            * Object_97 (Mesh)
          * Object_100 (Xform)
            * Object_98 (Mesh)
          * Object_101 (Xform)
            * Object_99 (Mesh)
          * Object_102 (Xform)
            * Object_100 (Mesh)
          * Object_103 (Xform)
            * Object_101 (Mesh)
          * Object_104 (Xform)
            * Object_102 (Mesh)
          * Object_105 (Xform)
            * Object_103 (Mesh)
          * Object_106 (Xform)
            * Object_104 (Mesh)
          * Object_107 (Xform)
            * Object_105 (Mesh)
          * Object_108 (Xform)
            * Object_106 (Mesh)
          * Object_109 (Xform)
            * Object_107 (Mesh)
          * Object_110 (Xform)
            * Object_108 (Mesh)
          * Object_111 (Xform)
            * Object_109 (Mesh)
          * Object_112 (Xform)
            * Object_110 (Mesh)
          * Object_113 (Xform)
            * Object_111 (Mesh)
          * Object_114 (Xform)
            * Object_112 (Mesh)
          * Object_115 (Xform)
            * Object_113 (Mesh)
          * Object_116 (Xform)
            * Object_114 (Mesh)
          * Object_117 (Xform)
            * Object_115 (Mesh)
          * Object_118 (Xform)
            * Object_116 (Mesh)
          * Object_119 (Xform)
            * Object_117 (Mesh)
          * Object_120 (Xform)
            * Object_118 (Mesh)
          * Object_121 (Xform)
            * Object_119 (Mesh)
          * Object_122 (Xform)
            * Object_120 (Mesh)
          * Object_123 (Xform)
            * Object_121 (Mesh)
          * Object_124 (Xform)
            * Object_122 (Mesh)
          * Object_125 (Xform)
            * Object_123 (Mesh)
          * Object_126 (Xform)
            * Object_124 (Mesh)
          * Object_127 (Xform)
            * Object_125 (Mesh)
          * Object_128 (Xform)
            * Object_126 (Mesh)
          * Object_129 (Xform)
            * Object_127 (Mesh)
          * Object_130 (Xform)
            * Object_128 (Mesh)
          * Object_131 (Xform)
            * Object_129 (Mesh)
          * Object_132 (Xform)
            * Object_130 (Mesh)
          * Object_133 (Xform)
            * Object_131 (Mesh)
          * Object_134 (Xform)
            * Object_132 (Mesh)
          * Object_135 (Xform)
            * Object_133 (Mesh)
          * Object_136 (Xform)
            * Object_134 (Mesh)
          * Object_137 (Xform)
            * Object_135 (Mesh)
          * Object_138 (Xform)
            * Object_136 (Mesh)
          * Object_139 (Xform)
            * Object_137 (Mesh)
          * Object_140 (Xform)
            * Object_138 (Mesh)
          * Object_141 (Xform)
            * Object_139 (Mesh)
          * Object_142 (Xform)
            * Object_140 (Mesh)
          * Object_143 (Xform)
            * Object_141 (Mesh)
          * Object_144 (Xform)
            * Object_142 (Mesh)
          * Object_145 (Xform)
            * Object_143 (Mesh)
          * Object_146 (Xform)
            * Object_144 (Mesh)
          * Object_147 (Xform)
            * Object_145 (Mesh)
          * Object_148 (Xform)
            * Object_146 (Mesh)
          * Object_149 (Xform)
            * Object_147 (Mesh)
          * Object_150 (Xform)
            * Object_148 (Mesh)
          * Object_151 (Xform)
            * Object_149 (Mesh)
          * Object_152 (Xform)
            * Object_150 (Mesh)
          * Object_153 (Xform)
            * Object_151 (Mesh)
          * Object_154 (Xform)
            * Object_152 (Mesh)
          * Object_155 (Xform)
            * Object_153 (Mesh)
          * Object_156 (Xform)
            * Object_154 (Mesh)
          * Object_157 (Xform)
            * Object_155 (Mesh)
          * Object_158 (Xform)
            * Object_156 (Mesh)
          * Object_159 (Xform)
            * Object_157 (Mesh)
          * Object_160 (Xform)
            * Object_158 (Mesh)
          * Object_161 (Xform)
            * Object_159 (Mesh)
          * Object_162 (Xform)
            * Object_160 (Mesh)
          * Object_163 (Xform)
            * Object_161 (Mesh)
          * Object_164 (Xform)
            * Object_162 (Mesh)
          * Object_165 (Xform)
            * Object_163 (Mesh)
          * Object_166 (Xform)
            * Object_164 (Mesh)
          * Object_167 (Xform)
            * Object_165 (Mesh)
          * Object_168 (Xform)
            * Object_166 (Mesh)
          * Object_169 (Xform)
            * Object_167 (Mesh)
          * Object_170 (Xform)
            * Object_168 (Mesh)
          * Object_171 (Xform)
            * Object_169 (Mesh)
          * Object_172 (Xform)
            * Object_170 (Mesh)
  * agv_5 (Xform)
    * Materials (Scope)
      * ASELSAN_CATS_04 (Material)
        * pbr_shader (Shader)
      * ASELSAN_CATS_04_2 (Material)
        * pbr_shader (Shader)
      * ASELSAN_CATS_13 (Material)
        * pbr_shader (Shader)
      * Color_000 (Material)
        * pbr_shader (Shader)
      * Color_A05 (Material)
        * pbr_shader (Shader)
      * Color_A06 (Material)
        * pbr_shader (Shader)
      * Color_B05 (Material)
        * pbr_shader (Shader)
      * Color_E02 (Material)
        * pbr_shader (Shader)
      * Color_E05 (Material)
        * pbr_shader (Shader)
      * Color_F06 (Material)
        * pbr_shader (Shader)
      * Color_G03 (Material)
        * pbr_shader (Shader)
      * Color_M02 (Material)
        * pbr_shader (Shader)
      * Color_M03 (Material)
        * pbr_shader (Shader)
      * Mtl39 (Material)
        * pbr_shader (Shader)
      * Mtl6 (Material)
        * pbr_shader (Shader)
        * uvset0 (Shader)
        * tex_base (Shader)
      * Mtl9 (Material)
        * pbr_shader (Shader)
      * Silver (Material)
        * pbr_shader (Shader)
      * material (Material)
        * pbr_shader (Shader)
        * uvset0 (Shader)
        * tex_base (Shader)
      * cash_register_keys (Material)
        * pbr_shader (Shader)
      * Chris_Shoe_Sole (Material)
        * pbr_shader (Shader)
      * Color_002 (Material)
        * pbr_shader (Shader)
      * Color_005 (Material)
        * pbr_shader (Shader)
      * Color_006 (Material)
        * pbr_shader (Shader)
      * Color_008 (Material)
        * pbr_shader (Shader)
      * Color_A01 (Material)
        * pbr_shader (Shader)
      * Color_A11 (Material)
        * pbr_shader (Shader)
      * Color_M04 (Material)
        * pbr_shader (Shader)
      * Color_M05 (Material)
        * pbr_shader (Shader)
      * Color_M06 (Material)
        * pbr_shader (Shader)
      * Color_M07 (Material)
        * pbr_shader (Shader)
      * Color_M09 (Material)
        * pbr_shader (Shader)
      * FCP_Charcoal_v2 (Material)
        * pbr_shader (Shader)
      * FrontColor (Material)
        * pbr_shader (Shader)
      * Light_Blue (Material)
        * pbr_shader (Shader)
      * M_0011_Seashell (Material)
        * pbr_shader (Shader)
      * M_0131_Silver (Material)
        * pbr_shader (Shader)
      * M_0134_DimGray (Material)
        * pbr_shader (Shader)
      * M_0135_DarkGray (Material)
        * pbr_shader (Shader)
      * Metal_Silver (Material)
        * pbr_shader (Shader)
      * Mtl1 (Material)
        * pbr_shader (Shader)
      * Mtl10 (Material)
        * pbr_shader (Shader)
      * Mtl11 (Material)
        * pbr_shader (Shader)
      * Mtl12 (Material)
        * pbr_shader (Shader)
      * Mtl13 (Material)
        * pbr_shader (Shader)
      * Mtl14 (Material)
        * pbr_shader (Shader)
      * Mtl15 (Material)
        * pbr_shader (Shader)
      * Mtl16 (Material)
        * pbr_shader (Shader)
      * Mtl17 (Material)
        * pbr_shader (Shader)
      * Mtl3 (Material)
        * pbr_shader (Shader)
      * Mtl35 (Material)
        * pbr_shader (Shader)
      * Mtl36 (Material)
        * pbr_shader (Shader)
      * Mtl37 (Material)
        * pbr_shader (Shader)
      * Mtl3a (Material)
        * pbr_shader (Shader)
      * Mtl3b (Material)
        * pbr_shader (Shader)
      * Mtl5 (Material)
        * pbr_shader (Shader)
      * Mtl7 (Material)
        * pbr_shader (Shader)
      * Mtl8 (Material)
        * pbr_shader (Shader)
      * Mtla (Material)
        * pbr_shader (Shader)
      * Mtlb1 (Material)
        * pbr_shader (Shader)
      * Stainless_Steel (Material)
        * pbr_shader (Shader)
      * Metal_Aluminum_Anodized_1 (Material)
        * pbr_shader (Shader)
      * Metal_Aluminum_Anodized_2 (Material)
        * pbr_shader (Shader)
      * basic_gray_plastic (Material)
        * pbr_shader (Shader)
      * texture (Material)
        * pbr_shader (Shader)
    * Meshes (Xform)
      * Sketchfab_model (Xform)
        * AGV_ready_1_obj_cleaner_materialmerger_gles (Xform)
          * Object_2 (Xform)
            * Object_0 (Mesh)
          * Object_3 (Xform)
            * Object_1 (Mesh)
          * Object_4 (Xform)
            * Object_2 (Mesh)
          * Object_5 (Xform)
            * Object_3 (Mesh)
          * Object_6 (Xform)
            * Object_4 (Mesh)
          * Object_7 (Xform)
            * Object_5 (Mesh)
          * Object_8 (Xform)
            * Object_6 (Mesh)
          * Object_9 (Xform)
            * Object_7 (Mesh)
          * Object_10 (Xform)
            * Object_8 (Mesh)
          * Object_11 (Xform)
            * Object_9 (Mesh)
          * Object_12 (Xform)
            * Object_10 (Mesh)
          * Object_13 (Xform)
            * Object_11 (Mesh)
          * Object_14 (Xform)
            * Object_12 (Mesh)
          * Object_15 (Xform)
            * Object_13 (Mesh)
          * Object_16 (Xform)
            * Object_14 (Mesh)
          * Object_17 (Xform)
            * Object_15 (Mesh)
          * Object_18 (Xform)
            * Object_16 (Mesh)
          * Object_19 (Xform)
            * Object_17 (Mesh)
          * Object_20 (Xform)
            * Object_18 (Mesh)
          * Object_21 (Xform)
            * Object_19 (Mesh)
          * Object_22 (Xform)
            * Object_20 (Mesh)
          * Object_23 (Xform)
            * Object_21 (Mesh)
          * Object_24 (Xform)
            * Object_22 (Mesh)
          * Object_25 (Xform)
            * Object_23 (Mesh)
          * Object_26 (Xform)
            * Object_24 (Mesh)
          * Object_27 (Xform)
            * Object_25 (Mesh)
          * Object_28 (Xform)
            * Object_26 (Mesh)
          * Object_29 (Xform)
            * Object_27 (Mesh)
          * Object_30 (Xform)
            * Object_28 (Mesh)
          * Object_31 (Xform)
            * Object_29 (Mesh)
          * Object_32 (Xform)
            * Object_30 (Mesh)
          * Object_33 (Xform)
            * Object_31 (Mesh)
          * Object_34 (Xform)
            * Object_32 (Mesh)
          * Object_35 (Xform)
            * Object_33 (Mesh)
          * Object_36 (Xform)
            * Object_34 (Mesh)
          * Object_37 (Xform)
            * Object_35 (Mesh)
          * Object_38 (Xform)
            * Object_36 (Mesh)
          * Object_39 (Xform)
            * Object_37 (Mesh)
          * Object_40 (Xform)
            * Object_38 (Mesh)
          * Object_41 (Xform)
            * Object_39 (Mesh)
          * Object_42 (Xform)
            * Object_40 (Mesh)
          * Object_43 (Xform)
            * Object_41 (Mesh)
          * Object_44 (Xform)
            * Object_42 (Mesh)
          * Object_45 (Xform)
            * Object_43 (Mesh)
          * Object_46 (Xform)
            * Object_44 (Mesh)
          * Object_47 (Xform)
            * Object_45 (Mesh)
          * Object_48 (Xform)
            * Object_46 (Mesh)
          * Object_49 (Xform)
            * Object_47 (Mesh)
          * Object_50 (Xform)
            * Object_48 (Mesh)
          * Object_51 (Xform)
            * Object_49 (Mesh)
          * Object_52 (Xform)
            * Object_50 (Mesh)
          * Object_53 (Xform)
            * Object_51 (Mesh)
          * Object_54 (Xform)
            * Object_52 (Mesh)
          * Object_55 (Xform)
            * Object_53 (Mesh)
          * Object_56 (Xform)
            * Object_54 (Mesh)
          * Object_57 (Xform)
            * Object_55 (Mesh)
          * Object_58 (Xform)
            * Object_56 (Mesh)
          * Object_59 (Xform)
            * Object_57 (Mesh)
          * Object_60 (Xform)
            * Object_58 (Mesh)
          * Object_61 (Xform)
            * Object_59 (Mesh)
          * Object_62 (Xform)
            * Object_60 (Mesh)
          * Object_63 (Xform)
            * Object_61 (Mesh)
          * Object_64 (Xform)
            * Object_62 (Mesh)
          * Object_65 (Xform)
            * Object_63 (Mesh)
          * Object_66 (Xform)
            * Object_64 (Mesh)
          * Object_67 (Xform)
            * Object_65 (Mesh)
          * Object_68 (Xform)
            * Object_66 (Mesh)
          * Object_69 (Xform)
            * Object_67 (Mesh)
          * Object_70 (Xform)
            * Object_68 (Mesh)
          * Object_71 (Xform)
            * Object_69 (Mesh)
          * Object_72 (Xform)
            * Object_70 (Mesh)
          * Object_73 (Xform)
            * Object_71 (Mesh)
          * Object_74 (Xform)
            * Object_72 (Mesh)
          * Object_75 (Xform)
            * Object_73 (Mesh)
          * Object_76 (Xform)
            * Object_74 (Mesh)
          * Object_77 (Xform)
            * Object_75 (Mesh)
          * Object_78 (Xform)
            * Object_76 (Mesh)
          * Object_79 (Xform)
            * Object_77 (Mesh)
          * Object_80 (Xform)
            * Object_78 (Mesh)
          * Object_81 (Xform)
            * Object_79 (Mesh)
          * Object_82 (Xform)
            * Object_80 (Mesh)
          * Object_83 (Xform)
            * Object_81 (Mesh)
          * Object_84 (Xform)
            * Object_82 (Mesh)
          * Object_85 (Xform)
            * Object_83 (Mesh)
          * Object_86 (Xform)
            * Object_84 (Mesh)
          * Object_87 (Xform)
            * Object_85 (Mesh)
          * Object_88 (Xform)
            * Object_86 (Mesh)
          * Object_89 (Xform)
            * Object_87 (Mesh)
          * Object_90 (Xform)
            * Object_88 (Mesh)
          * Object_91 (Xform)
            * Object_89 (Mesh)
          * Object_92 (Xform)
            * Object_90 (Mesh)
          * Object_93 (Xform)
            * Object_91 (Mesh)
          * Object_94 (Xform)
            * Object_92 (Mesh)
          * Object_95 (Xform)
            * Object_93 (Mesh)
          * Object_96 (Xform)
            * Object_94 (Mesh)
          * Object_97 (Xform)
            * Object_95 (Mesh)
          * Object_98 (Xform)
            * Object_96 (Mesh)
          * Object_99 (Xform)
            * Object_97 (Mesh)
          * Object_100 (Xform)
            * Object_98 (Mesh)
          * Object_101 (Xform)
            * Object_99 (Mesh)
          * Object_102 (Xform)
            * Object_100 (Mesh)
          * Object_103 (Xform)
            * Object_101 (Mesh)
          * Object_104 (Xform)
            * Object_102 (Mesh)
          * Object_105 (Xform)
            * Object_103 (Mesh)
          * Object_106 (Xform)
            * Object_104 (Mesh)
          * Object_107 (Xform)
            * Object_105 (Mesh)
          * Object_108 (Xform)
            * Object_106 (Mesh)
          * Object_109 (Xform)
            * Object_107 (Mesh)
          * Object_110 (Xform)
            * Object_108 (Mesh)
          * Object_111 (Xform)
            * Object_109 (Mesh)
          * Object_112 (Xform)
            * Object_110 (Mesh)
          * Object_113 (Xform)
            * Object_111 (Mesh)
          * Object_114 (Xform)
            * Object_112 (Mesh)
          * Object_115 (Xform)
            * Object_113 (Mesh)
          * Object_116 (Xform)
            * Object_114 (Mesh)
          * Object_117 (Xform)
            * Object_115 (Mesh)
          * Object_118 (Xform)
            * Object_116 (Mesh)
          * Object_119 (Xform)
            * Object_117 (Mesh)
          * Object_120 (Xform)
            * Object_118 (Mesh)
          * Object_121 (Xform)
            * Object_119 (Mesh)
          * Object_122 (Xform)
            * Object_120 (Mesh)
          * Object_123 (Xform)
            * Object_121 (Mesh)
          * Object_124 (Xform)
            * Object_122 (Mesh)
          * Object_125 (Xform)
            * Object_123 (Mesh)
          * Object_126 (Xform)
            * Object_124 (Mesh)
          * Object_127 (Xform)
            * Object_125 (Mesh)
          * Object_128 (Xform)
            * Object_126 (Mesh)
          * Object_129 (Xform)
            * Object_127 (Mesh)
          * Object_130 (Xform)
            * Object_128 (Mesh)
          * Object_131 (Xform)
            * Object_129 (Mesh)
          * Object_132 (Xform)
            * Object_130 (Mesh)
          * Object_133 (Xform)
            * Object_131 (Mesh)
          * Object_134 (Xform)
            * Object_132 (Mesh)
          * Object_135 (Xform)
            * Object_133 (Mesh)
          * Object_136 (Xform)
            * Object_134 (Mesh)
          * Object_137 (Xform)
            * Object_135 (Mesh)
          * Object_138 (Xform)
            * Object_136 (Mesh)
          * Object_139 (Xform)
            * Object_137 (Mesh)
          * Object_140 (Xform)
            * Object_138 (Mesh)
          * Object_141 (Xform)
            * Object_139 (Mesh)
          * Object_142 (Xform)
            * Object_140 (Mesh)
          * Object_143 (Xform)
            * Object_141 (Mesh)
          * Object_144 (Xform)
            * Object_142 (Mesh)
          * Object_145 (Xform)
            * Object_143 (Mesh)
          * Object_146 (Xform)
            * Object_144 (Mesh)
          * Object_147 (Xform)
            * Object_145 (Mesh)
          * Object_148 (Xform)
            * Object_146 (Mesh)
          * Object_149 (Xform)
            * Object_147 (Mesh)
          * Object_150 (Xform)
            * Object_148 (Mesh)
          * Object_151 (Xform)
            * Object_149 (Mesh)
          * Object_152 (Xform)
            * Object_150 (Mesh)
          * Object_153 (Xform)
            * Object_151 (Mesh)
          * Object_154 (Xform)
            * Object_152 (Mesh)
          * Object_155 (Xform)
            * Object_153 (Mesh)
          * Object_156 (Xform)
            * Object_154 (Mesh)
          * Object_157 (Xform)
            * Object_155 (Mesh)
          * Object_158 (Xform)
            * Object_156 (Mesh)
          * Object_159 (Xform)
            * Object_157 (Mesh)
          * Object_160 (Xform)
            * Object_158 (Mesh)
          * Object_161 (Xform)
            * Object_159 (Mesh)
          * Object_162 (Xform)
            * Object_160 (Mesh)
          * Object_163 (Xform)
            * Object_161 (Mesh)
          * Object_164 (Xform)
            * Object_162 (Mesh)
          * Object_165 (Xform)
            * Object_163 (Mesh)
          * Object_166 (Xform)
            * Object_164 (Mesh)
          * Object_167 (Xform)
            * Object_165 (Mesh)
          * Object_168 (Xform)
            * Object_166 (Mesh)
          * Object_169 (Xform)
            * Object_167 (Mesh)
          * Object_170 (Xform)
            * Object_168 (Mesh)
          * Object_171 (Xform)
            * Object_169 (Mesh)
          * Object_172 (Xform)
            * Object_170 (Mesh)
  * agv_6 (Xform)
    * Materials (Scope)
      * ASELSAN_CATS_04 (Material)
        * pbr_shader (Shader)
      * ASELSAN_CATS_04_2 (Material)
        * pbr_shader (Shader)
      * ASELSAN_CATS_13 (Material)
        * pbr_shader (Shader)
      * Color_000 (Material)
        * pbr_shader (Shader)
      * Color_A05 (Material)
        * pbr_shader (Shader)
      * Color_A06 (Material)
        * pbr_shader (Shader)
      * Color_B05 (Material)
        * pbr_shader (Shader)
      * Color_E02 (Material)
        * pbr_shader (Shader)
      * Color_E05 (Material)
        * pbr_shader (Shader)
      * Color_F06 (Material)
        * pbr_shader (Shader)
      * Color_G03 (Material)
        * pbr_shader (Shader)
      * Color_M02 (Material)
        * pbr_shader (Shader)
      * Color_M03 (Material)
        * pbr_shader (Shader)
      * Mtl39 (Material)
        * pbr_shader (Shader)
      * Mtl6 (Material)
        * pbr_shader (Shader)
        * uvset0 (Shader)
        * tex_base (Shader)
      * Mtl9 (Material)
        * pbr_shader (Shader)
      * Silver (Material)
        * pbr_shader (Shader)
      * material (Material)
        * pbr_shader (Shader)
        * uvset0 (Shader)
        * tex_base (Shader)
      * cash_register_keys (Material)
        * pbr_shader (Shader)
      * Chris_Shoe_Sole (Material)
        * pbr_shader (Shader)
      * Color_002 (Material)
        * pbr_shader (Shader)
      * Color_005 (Material)
        * pbr_shader (Shader)
      * Color_006 (Material)
        * pbr_shader (Shader)
      * Color_008 (Material)
        * pbr_shader (Shader)
      * Color_A01 (Material)
        * pbr_shader (Shader)
      * Color_A11 (Material)
        * pbr_shader (Shader)
      * Color_M04 (Material)
        * pbr_shader (Shader)
      * Color_M05 (Material)
        * pbr_shader (Shader)
      * Color_M06 (Material)
        * pbr_shader (Shader)
      * Color_M07 (Material)
        * pbr_shader (Shader)
      * Color_M09 (Material)
        * pbr_shader (Shader)
      * FCP_Charcoal_v2 (Material)
        * pbr_shader (Shader)
      * FrontColor (Material)
        * pbr_shader (Shader)
      * Light_Blue (Material)
        * pbr_shader (Shader)
      * M_0011_Seashell (Material)
        * pbr_shader (Shader)
      * M_0131_Silver (Material)
        * pbr_shader (Shader)
      * M_0134_DimGray (Material)
        * pbr_shader (Shader)
      * M_0135_DarkGray (Material)
        * pbr_shader (Shader)
      * Metal_Silver (Material)
        * pbr_shader (Shader)
      * Mtl1 (Material)
        * pbr_shader (Shader)
      * Mtl10 (Material)
        * pbr_shader (Shader)
      * Mtl11 (Material)
        * pbr_shader (Shader)
      * Mtl12 (Material)
        * pbr_shader (Shader)
      * Mtl13 (Material)
        * pbr_shader (Shader)
      * Mtl14 (Material)
        * pbr_shader (Shader)
      * Mtl15 (Material)
        * pbr_shader (Shader)
      * Mtl16 (Material)
        * pbr_shader (Shader)
      * Mtl17 (Material)
        * pbr_shader (Shader)
      * Mtl3 (Material)
        * pbr_shader (Shader)
      * Mtl35 (Material)
        * pbr_shader (Shader)
      * Mtl36 (Material)
        * pbr_shader (Shader)
      * Mtl37 (Material)
        * pbr_shader (Shader)
      * Mtl3a (Material)
        * pbr_shader (Shader)
      * Mtl3b (Material)
        * pbr_shader (Shader)
      * Mtl5 (Material)
        * pbr_shader (Shader)
      * Mtl7 (Material)
        * pbr_shader (Shader)
      * Mtl8 (Material)
        * pbr_shader (Shader)
      * Mtla (Material)
        * pbr_shader (Shader)
      * Mtlb1 (Material)
        * pbr_shader (Shader)
      * Stainless_Steel (Material)
        * pbr_shader (Shader)
      * Metal_Aluminum_Anodized_1 (Material)
        * pbr_shader (Shader)
      * Metal_Aluminum_Anodized_2 (Material)
        * pbr_shader (Shader)
      * basic_gray_plastic (Material)
        * pbr_shader (Shader)
      * texture (Material)
        * pbr_shader (Shader)
    * Meshes (Xform)
      * Sketchfab_model (Xform)
        * AGV_ready_1_obj_cleaner_materialmerger_gles (Xform)
          * Object_2 (Xform)
            * Object_0 (Mesh)
          * Object_3 (Xform)
            * Object_1 (Mesh)
          * Object_4 (Xform)
            * Object_2 (Mesh)
          * Object_5 (Xform)
            * Object_3 (Mesh)
          * Object_6 (Xform)
            * Object_4 (Mesh)
          * Object_7 (Xform)
            * Object_5 (Mesh)
          * Object_8 (Xform)
            * Object_6 (Mesh)
          * Object_9 (Xform)
            * Object_7 (Mesh)
          * Object_10 (Xform)
            * Object_8 (Mesh)
          * Object_11 (Xform)
            * Object_9 (Mesh)
          * Object_12 (Xform)
            * Object_10 (Mesh)
          * Object_13 (Xform)
            * Object_11 (Mesh)
          * Object_14 (Xform)
            * Object_12 (Mesh)
          * Object_15 (Xform)
            * Object_13 (Mesh)
          * Object_16 (Xform)
            * Object_14 (Mesh)
          * Object_17 (Xform)
            * Object_15 (Mesh)
          * Object_18 (Xform)
            * Object_16 (Mesh)
          * Object_19 (Xform)
            * Object_17 (Mesh)
          * Object_20 (Xform)
            * Object_18 (Mesh)
          * Object_21 (Xform)
            * Object_19 (Mesh)
          * Object_22 (Xform)
            * Object_20 (Mesh)
          * Object_23 (Xform)
            * Object_21 (Mesh)
          * Object_24 (Xform)
            * Object_22 (Mesh)
          * Object_25 (Xform)
            * Object_23 (Mesh)
          * Object_26 (Xform)
            * Object_24 (Mesh)
          * Object_27 (Xform)
            * Object_25 (Mesh)
          * Object_28 (Xform)
            * Object_26 (Mesh)
          * Object_29 (Xform)
            * Object_27 (Mesh)
          * Object_30 (Xform)
            * Object_28 (Mesh)
          * Object_31 (Xform)
            * Object_29 (Mesh)
          * Object_32 (Xform)
            * Object_30 (Mesh)
          * Object_33 (Xform)
            * Object_31 (Mesh)
          * Object_34 (Xform)
            * Object_32 (Mesh)
          * Object_35 (Xform)
            * Object_33 (Mesh)
          * Object_36 (Xform)
            * Object_34 (Mesh)
          * Object_37 (Xform)
            * Object_35 (Mesh)
          * Object_38 (Xform)
            * Object_36 (Mesh)
          * Object_39 (Xform)
            * Object_37 (Mesh)
          * Object_40 (Xform)
            * Object_38 (Mesh)
          * Object_41 (Xform)
            * Object_39 (Mesh)
          * Object_42 (Xform)
            * Object_40 (Mesh)
          * Object_43 (Xform)
            * Object_41 (Mesh)
          * Object_44 (Xform)
            * Object_42 (Mesh)
          * Object_45 (Xform)
            * Object_43 (Mesh)
          * Object_46 (Xform)
            * Object_44 (Mesh)
          * Object_47 (Xform)
            * Object_45 (Mesh)
          * Object_48 (Xform)
            * Object_46 (Mesh)
          * Object_49 (Xform)
            * Object_47 (Mesh)
          * Object_50 (Xform)
            * Object_48 (Mesh)
          * Object_51 (Xform)
            * Object_49 (Mesh)
          * Object_52 (Xform)
            * Object_50 (Mesh)
          * Object_53 (Xform)
            * Object_51 (Mesh)
          * Object_54 (Xform)
            * Object_52 (Mesh)
          * Object_55 (Xform)
            * Object_53 (Mesh)
          * Object_56 (Xform)
            * Object_54 (Mesh)
          * Object_57 (Xform)
            * Object_55 (Mesh)
          * Object_58 (Xform)
            * Object_56 (Mesh)
          * Object_59 (Xform)
            * Object_57 (Mesh)
          * Object_60 (Xform)
            * Object_58 (Mesh)
          * Object_61 (Xform)
            * Object_59 (Mesh)
          * Object_62 (Xform)
            * Object_60 (Mesh)
          * Object_63 (Xform)
            * Object_61 (Mesh)
          * Object_64 (Xform)
            * Object_62 (Mesh)
          * Object_65 (Xform)
            * Object_63 (Mesh)
          * Object_66 (Xform)
            * Object_64 (Mesh)
          * Object_67 (Xform)
            * Object_65 (Mesh)
          * Object_68 (Xform)
            * Object_66 (Mesh)
          * Object_69 (Xform)
            * Object_67 (Mesh)
          * Object_70 (Xform)
            * Object_68 (Mesh)
          * Object_71 (Xform)
            * Object_69 (Mesh)
          * Object_72 (Xform)
            * Object_70 (Mesh)
          * Object_73 (Xform)
            * Object_71 (Mesh)
          * Object_74 (Xform)
            * Object_72 (Mesh)
          * Object_75 (Xform)
            * Object_73 (Mesh)
          * Object_76 (Xform)
            * Object_74 (Mesh)
          * Object_77 (Xform)
            * Object_75 (Mesh)
          * Object_78 (Xform)
            * Object_76 (Mesh)
          * Object_79 (Xform)
            * Object_77 (Mesh)
          * Object_80 (Xform)
            * Object_78 (Mesh)
          * Object_81 (Xform)
            * Object_79 (Mesh)
          * Object_82 (Xform)
            * Object_80 (Mesh)
          * Object_83 (Xform)
            * Object_81 (Mesh)
          * Object_84 (Xform)
            * Object_82 (Mesh)
          * Object_85 (Xform)
            * Object_83 (Mesh)
          * Object_86 (Xform)
            * Object_84 (Mesh)
          * Object_87 (Xform)
            * Object_85 (Mesh)
          * Object_88 (Xform)
            * Object_86 (Mesh)
          * Object_89 (Xform)
            * Object_87 (Mesh)
          * Object_90 (Xform)
            * Object_88 (Mesh)
          * Object_91 (Xform)
            * Object_89 (Mesh)
          * Object_92 (Xform)
            * Object_90 (Mesh)
          * Object_93 (Xform)
            * Object_91 (Mesh)
          * Object_94 (Xform)
            * Object_92 (Mesh)
          * Object_95 (Xform)
            * Object_93 (Mesh)
          * Object_96 (Xform)
            * Object_94 (Mesh)
          * Object_97 (Xform)
            * Object_95 (Mesh)
          * Object_98 (Xform)
            * Object_96 (Mesh)
          * Object_99 (Xform)
            * Object_97 (Mesh)
          * Object_100 (Xform)
            * Object_98 (Mesh)
          * Object_101 (Xform)
            * Object_99 (Mesh)
          * Object_102 (Xform)
            * Object_100 (Mesh)
          * Object_103 (Xform)
            * Object_101 (Mesh)
          * Object_104 (Xform)
            * Object_102 (Mesh)
          * Object_105 (Xform)
            * Object_103 (Mesh)
          * Object_106 (Xform)
            * Object_104 (Mesh)
          * Object_107 (Xform)
            * Object_105 (Mesh)
          * Object_108 (Xform)
            * Object_106 (Mesh)
          * Object_109 (Xform)
            * Object_107 (Mesh)
          * Object_110 (Xform)
            * Object_108 (Mesh)
          * Object_111 (Xform)
            * Object_109 (Mesh)
          * Object_112 (Xform)
            * Object_110 (Mesh)
          * Object_113 (Xform)
            * Object_111 (Mesh)
          * Object_114 (Xform)
            * Object_112 (Mesh)
          * Object_115 (Xform)
            * Object_113 (Mesh)
          * Object_116 (Xform)
            * Object_114 (Mesh)
          * Object_117 (Xform)
            * Object_115 (Mesh)
          * Object_118 (Xform)
            * Object_116 (Mesh)
          * Object_119 (Xform)
            * Object_117 (Mesh)
          * Object_120 (Xform)
            * Object_118 (Mesh)
          * Object_121 (Xform)
            * Object_119 (Mesh)
          * Object_122 (Xform)
            * Object_120 (Mesh)
          * Object_123 (Xform)
            * Object_121 (Mesh)
          * Object_124 (Xform)
            * Object_122 (Mesh)
          * Object_125 (Xform)
            * Object_123 (Mesh)
          * Object_126 (Xform)
            * Object_124 (Mesh)
          * Object_127 (Xform)
            * Object_125 (Mesh)
          * Object_128 (Xform)
            * Object_126 (Mesh)
          * Object_129 (Xform)
            * Object_127 (Mesh)
          * Object_130 (Xform)
            * Object_128 (Mesh)
          * Object_131 (Xform)
            * Object_129 (Mesh)
          * Object_132 (Xform)
            * Object_130 (Mesh)
          * Object_133 (Xform)
            * Object_131 (Mesh)
          * Object_134 (Xform)
            * Object_132 (Mesh)
          * Object_135 (Xform)
            * Object_133 (Mesh)
          * Object_136 (Xform)
            * Object_134 (Mesh)
          * Object_137 (Xform)
            * Object_135 (Mesh)
          * Object_138 (Xform)
            * Object_136 (Mesh)
          * Object_139 (Xform)
            * Object_137 (Mesh)
          * Object_140 (Xform)
            * Object_138 (Mesh)
          * Object_141 (Xform)
            * Object_139 (Mesh)
          * Object_142 (Xform)
            * Object_140 (Mesh)
          * Object_143 (Xform)
            * Object_141 (Mesh)
          * Object_144 (Xform)
            * Object_142 (Mesh)
          * Object_145 (Xform)
            * Object_143 (Mesh)
          * Object_146 (Xform)
            * Object_144 (Mesh)
          * Object_147 (Xform)
            * Object_145 (Mesh)
          * Object_148 (Xform)
            * Object_146 (Mesh)
          * Object_149 (Xform)
            * Object_147 (Mesh)
          * Object_150 (Xform)
            * Object_148 (Mesh)
          * Object_151 (Xform)
            * Object_149 (Mesh)
          * Object_152 (Xform)
            * Object_150 (Mesh)
          * Object_153 (Xform)
            * Object_151 (Mesh)
          * Object_154 (Xform)
            * Object_152 (Mesh)
          * Object_155 (Xform)
            * Object_153 (Mesh)
          * Object_156 (Xform)
            * Object_154 (Mesh)
          * Object_157 (Xform)
            * Object_155 (Mesh)
          * Object_158 (Xform)
            * Object_156 (Mesh)
          * Object_159 (Xform)
            * Object_157 (Mesh)
          * Object_160 (Xform)
            * Object_158 (Mesh)
          * Object_161 (Xform)
            * Object_159 (Mesh)
          * Object_162 (Xform)
            * Object_160 (Mesh)
          * Object_163 (Xform)
            * Object_161 (Mesh)
          * Object_164 (Xform)
            * Object_162 (Mesh)
          * Object_165 (Xform)
            * Object_163 (Mesh)
          * Object_166 (Xform)
            * Object_164 (Mesh)
          * Object_167 (Xform)
            * Object_165 (Mesh)
          * Object_168 (Xform)
            * Object_166 (Mesh)
          * Object_169 (Xform)
            * Object_167 (Mesh)
          * Object_170 (Xform)
            * Object_168 (Mesh)
          * Object_171 (Xform)
            * Object_169 (Mesh)
          * Object_172 (Xform)
            * Object_170 (Mesh)
  * StackedCarton_1 (Xform)
    * Materials (Scope)
      * Material_1 (Material)
        * pbr_shader (Shader)
        * uvset0 (Shader)
        * tex_base (Shader)
    * Meshes (Xform)
      * Sketchfab_model (Xform)
        * Plastic_Crate_FBX (Xform)
          * RootNode (Xform)
            * Box003 (Xform)
              * Object_4 (Xform)
                * Box003_Material__1_0 (Xform)
                  * Box003_Material__1_0 (Mesh)
  * StackedCarton_2 (Xform)
    * Materials (Scope)
      * Material_1 (Material)
        * pbr_shader (Shader)
        * uvset0 (Shader)
        * tex_base (Shader)
    * Meshes (Xform)
      * Sketchfab_model (Xform)
        * Plastic_Crate_FBX (Xform)
          * RootNode (Xform)
            * Box003 (Xform)
              * Object_4 (Xform)
                * Box003_Material__1_0 (Xform)
                  * Box003_Material__1_0 (Mesh)
  * StackedCarton_3 (Xform)
    * Materials (Scope)
      * Material_1 (Material)
        * pbr_shader (Shader)
        * uvset0 (Shader)
        * tex_base (Shader)
    * Meshes (Xform)
      * Sketchfab_model (Xform)
        * Plastic_Crate_FBX (Xform)
          * RootNode (Xform)
            * Box003 (Xform)
              * Object_4 (Xform)
                * Box003_Material__1_0 (Xform)
                  * Box003_Material__1_0 (Mesh)
  * StackedCarton_4 (Xform)
    * Materials (Scope)
      * Material_1 (Material)
        * pbr_shader (Shader)
        * uvset0 (Shader)
        * tex_base (Shader)
    * Meshes (Xform)
      * Sketchfab_model (Xform)
        * Plastic_Crate_FBX (Xform)
          * RootNode (Xform)
            * Box003 (Xform)
              * Object_4 (Xform)
                * Box003_Material__1_0 (Xform)
                  * Box003_Material__1_0 (Mesh)
  * StackedCarton_5 (Xform)
    * Materials (Scope)
      * Material_1 (Material)
        * pbr_shader (Shader)
        * uvset0 (Shader)
        * tex_base (Shader)
    * Meshes (Xform)
      * Sketchfab_model (Xform)
        * Plastic_Crate_FBX (Xform)
          * RootNode (Xform)
            * Box003 (Xform)
              * Object_4 (Xform)
                * Box003_Material__1_0 (Xform)
                  * Box003_Material__1_0 (Mesh)
  * StackedCarton_6 (Xform)
    * Materials (Scope)
      * Material_1 (Material)
        * pbr_shader (Shader)
        * uvset0 (Shader)
        * tex_base (Shader)
    * Meshes (Xform)
      * Sketchfab_model (Xform)
        * Plastic_Crate_FBX (Xform)
          * RootNode (Xform)
            * Box003 (Xform)
              * Object_4 (Xform)
                * Box003_Material__1_0 (Xform)
                  * Box003_Material__1_0 (Mesh)
  * Workbench_02 (Xform)
  * Workbench_03 (Xform)
  * Workbench_04 (Xform)
  * Workbench_05 (Xform)
  * Workbench_06 (Xform)
  * Workbench_07 (Xform)
  * Workbench_08 (Xform)
  * Workbench_09 (Xform)
  * Workbench_10 (Xform)
  * Workbench_11 (Xform)
  * Workbench_12 (Xform)
  * Workbench_13 (Xform)
  * Workbench_14 (Xform)
  * Workbench_15 (Xform)
  * Black_Honey___Robotic_Arm (Xform)
    * Materials (Scope)
      * robo_arm (Material)
        * pbr_shader (Shader)
        * uvset0 (Shader)
        * tex_base (Shader)
        * tex_metallic (Shader)
        * tex_roughness (Shader)
        * tex_normal (Shader)
        * tex_emissive (Shader)
      * robot_base (Material)
        * pbr_shader (Shader)
        * uvset0 (Shader)
        * tex_base (Shader)
        * tex_metallic (Shader)
        * tex_roughness (Shader)
        * tex_normal (Shader)
        * tex_emissive (Shader)
    * Meshes (Xform)
      * Sketchfab_model (Xform)
        * root (Xform)
          * GLTF_SceneRootNode (Xform)
            * roboarm_001_low_0 (Xform)
              * Object_4 (Xform)
                * Object_0 (Mesh)
            * roboarm_002_low_1 (Xform)
              * Object_6 (Xform)
                * Object_1 (Mesh)
            * roboarm_003_low_2 (Xform)
              * Object_8 (Xform)
                * Object_2 (Mesh)
            * roboarm_004_low_3 (Xform)
              * Object_10 (Xform)
                * Object_3 (Mesh)
            * roboarm_005_low_4 (Xform)
              * Object_12 (Xform)
                * Object_4 (Mesh)
            * roboarm_006_low_5 (Xform)
              * Object_14 (Xform)
                * Object_5 (Mesh)
            * roboarm_007_low_6 (Xform)
              * Object_16 (Xform)
                * Object_6 (Mesh)
            * roboarm_008_low_7 (Xform)
              * Object_18 (Xform)
                * Object_7 (Mesh)
            * roboarm_009_low_8 (Xform)
              * Object_20 (Xform)
                * Object_8 (Mesh)
            * roboarm_010_low_9 (Xform)
              * Object_22 (Xform)
                * Object_9 (Mesh)
            * roboarm_011_low_10 (Xform)
              * Object_24 (Xform)
                * Object_10 (Mesh)
            * roboarm_012_low_11 (Xform)
              * Object_26 (Xform)
                * Object_11 (Mesh)
            * roboarm_013_low_12 (Xform)
              * Object_28 (Xform)
                * Object_12 (Mesh)
            * roboarm_014_low_13 (Xform)
              * Object_30 (Xform)
                * Object_13 (Mesh)
            * roboarm_015_low_14 (Xform)
              * Object_32 (Xform)
                * Object_14 (Mesh)
            * roboarm_016_low_15 (Xform)
              * Object_34 (Xform)
                * Object_15 (Mesh)
            * roboarm_017_low_16 (Xform)
              * Object_36 (Xform)
                * Object_16 (Mesh)
            * roboarm_018_low_17 (Xform)
              * Object_38 (Xform)
                * Object_17 (Mesh)
            * roboarm_019_low_18 (Xform)
              * Object_40 (Xform)
                * Object_18 (Mesh)
            * roboarm_020_low_19 (Xform)
              * Object_42 (Xform)
                * Object_19 (Mesh)
            * roboarm_021_low_20 (Xform)
              * Object_44 (Xform)
                * Object_20 (Mesh)
            * roboarm_022_low_21 (Xform)
              * Object_46 (Xform)
                * Object_21 (Mesh)
            * roboarm_023_low_22 (Xform)
              * Object_48 (Xform)
                * Object_22 (Mesh)
            * roboarm_024_low_23 (Xform)
              * Object_50 (Xform)
                * Object_23 (Mesh)
            * roboarm_025_low_24 (Xform)
              * Object_52 (Xform)
                * Object_24 (Mesh)
            * roboarm_026_low_25 (Xform)
              * Object_54 (Xform)
                * Object_25 (Mesh)
            * roboarm_027_low_26 (Xform)
              * Object_56 (Xform)
                * Object_26 (Mesh)
            * roboarm_028_low_27 (Xform)
              * Object_58 (Xform)
                * Object_27 (Mesh)
            * roboarm_low_28 (Xform)
              * Object_60 (Xform)
                * Object_28 (Mesh)
            * robot_base_010_low_29 (Xform)
              * Object_62 (Xform)
                * Object_29 (Mesh)
            * robot_base_001_low_30 (Xform)
              * Object_64 (Xform)
                * Object_30 (Mesh)
            * robot_base_002_low_31 (Xform)
              * Object_66 (Xform)
                * Object_31 (Mesh)
            * robot_base_003_low_32 (Xform)
              * Object_68 (Xform)
                * Object_32 (Mesh)
            * robot_base_004_low_33 (Xform)
              * Object_70 (Xform)
                * Object_33 (Mesh)
            * robot_base_005_low_34 (Xform)
              * Object_72 (Xform)
                * Object_34 (Mesh)
            * robot_base_006_low_35 (Xform)
              * Object_74 (Xform)
                * Object_35 (Mesh)
            * robot_base_008_low_36 (Xform)
              * Object_76 (Xform)
                * Object_36 (Mesh)
            * robot_base_009_low_37 (Xform)
              * Object_78 (Xform)
                * Object_37 (Mesh)
            * robot_base_018_low_38 (Xform)
              * Object_80 (Xform)
                * Object_38 (Mesh)
            * robot_base_011_low_39 (Xform)
              * Object_82 (Xform)
                * Object_39 (Mesh)
            * robot_base_012_low_40 (Xform)
              * Object_84 (Xform)
                * Object_40 (Mesh)
            * robot_base_013_low_41 (Xform)
              * Object_86 (Xform)
                * Object_41 (Mesh)
            * robot_base_014_low_42 (Xform)
              * Object_88 (Xform)
                * Object_42 (Mesh)
            * robot_base_015_low_43 (Xform)
              * Object_90 (Xform)
                * Object_43 (Mesh)
            * robot_base_016_low_44 (Xform)
              * Object_92 (Xform)
                * Object_44 (Mesh)
            * robot_base_017_low_45 (Xform)
              * Object_94 (Xform)
                * Object_45 (Mesh)
            * robot_base_020_low_46 (Xform)
              * Object_96 (Xform)
                * Object_46 (Mesh)
            * robot_base_019_low_47 (Xform)
              * Object_98 (Xform)
                * Object_47 (Mesh)
            * robot_base_021_low_48 (Xform)
              * Object_100 (Xform)
                * Object_48 (Mesh)
            * robot_base_022_low_49 (Xform)
              * Object_102 (Xform)
                * Object_49 (Mesh)
            * robot_base_023_low_50 (Xform)
              * Object_104 (Xform)
                * Object_50 (Mesh)
            * robot_base_low_51 (Xform)
              * Object_106 (Xform)
                * Object_51 (Mesh)
            * robot_base_024_low_52 (Xform)
              * Object_108 (Xform)
                * Object_52 (Mesh)
            * robot_base_025_low_53 (Xform)
              * Object_110 (Xform)
                * Object_53 (Mesh)
            * robot_base_026_low_54 (Xform)
              * Object_112 (Xform)
                * Object_54 (Mesh)
            * robot_base_027_low_55 (Xform)
              * Object_114 (Xform)
                * Object_55 (Mesh)
            * robot_base_028_low_56 (Xform)
              * Object_116 (Xform)
                * Object_56 (Mesh)
            * robot_base_029_low_57 (Xform)
              * Object_118 (Xform)
                * Object_57 (Mesh)
            * robot_base_030_low_58 (Xform)
              * Object_120 (Xform)
                * Object_58 (Mesh)
            * robot_base_031_low_59 (Xform)
              * Object_122 (Xform)
                * Object_59 (Mesh)
            * robot_base_032_low_60 (Xform)
              * Object_124 (Xform)
                * Object_60 (Mesh)
            * robot_base_007_low_61 (Xform)
              * Object_126 (Xform)
                * Object_61 (Mesh)
            * robot_base_033_low_62 (Xform)
              * Object_128 (Xform)
                * Object_62 (Mesh)
            * robot_base_035_low_63 (Xform)
              * Object_130 (Xform)
                * Object_63 (Mesh)
  * rs007l_onrobot_rg2 (Xform)
    * world (Xform)
      * world2base (PhysicsFixedJoint)
    * root_joint (PhysicsFixedJoint)
    * base_link (Xform)
      * joint1 (PhysicsRevoluteJoint)
      * visuals (Mesh)
      * collisions (Mesh)
    * link1 (Xform)
      * joint2 (PhysicsRevoluteJoint)
      * visuals (Mesh)
      * collisions (Mesh)
    * link2 (Xform)
      * joint3 (PhysicsRevoluteJoint)
      * visuals (Mesh)
      * collisions (Mesh)
    * link3 (Xform)
      * joint4 (PhysicsRevoluteJoint)
      * visuals (Mesh)
      * collisions (Mesh)
    * link4 (Xform)
      * joint5 (PhysicsRevoluteJoint)
      * visuals (Mesh)
      * collisions (Mesh)
    * link5 (Xform)
      * joint6 (PhysicsRevoluteJoint)
      * visuals (Mesh)
      * collisions (Mesh)
    * link6 (Xform)
      * rs007l2rg2 (PhysicsFixedJoint)
      * visuals (Mesh)
      * collisions (Mesh)
    * onrobot_rg2_base_link (Xform)
      * finger_joint (PhysicsRevoluteJoint)
      * gripper_center_joint (PhysicsFixedJoint)
      * left_inner_knuckle_joint (PhysicsRevoluteJoint)
      * right_inner_knuckle_joint (PhysicsRevoluteJoint)
      * right_outer_knuckle_joint (PhysicsRevoluteJoint)
      * visuals (Mesh)
      * collisions (Mesh)
    * left_outer_knuckle (Xform)
      * left_inner_finger_joint (PhysicsRevoluteJoint)
      * visuals (Mesh)
      * collisions (Mesh)
    * left_inner_finger (Xform)
      * visuals (Mesh)
      * collisions (Mesh)
    * gripper_center (Xform)
    * left_inner_knuckle (Xform)
      * visuals (Mesh)
      * collisions (Mesh)
    * right_inner_knuckle (Xform)
      * visuals (Mesh)
      * collisions (Mesh)
    * right_outer_knuckle (Xform)
      * right_inner_finger_joint (PhysicsRevoluteJoint)
      * visuals (Mesh)
      * collisions (Mesh)
    * right_inner_finger (Xform)
      * visuals (Mesh)
      * collisions (Mesh)
    * Looks (Scope)
      * material_Black (Material)
        * Shader (Shader)
      * material_White (Material)
        * Shader (Shader)
      * material_CCCCCC (Material)
        * Shader (Shader)
      * material_191919 (Material)
        * Shader (Shader)
  * Black_Honey___Robotic_Arm_01 (Prim)
  * rs007l_onrobot_rg2_01 (Prim)
  * Black_Honey___Robotic_Arm_02 (Prim)
  * rs007l_onrobot_rg2_02 (Prim)
  * Black_Honey___Robotic_Arm_03 (Prim)
  * rs007l_onrobot_rg2_03 (Prim)
  * Black_Honey___Robotic_Arm_04 (Prim)
  * Black_Honey___Robotic_Arm_05 (Prim)
  * rs007l_onrobot_rg2_04 (Prim)
  * rs007l_onrobot_rg2_05 (Prim)
  * Black_Honey___Robotic_Arm_06 (Prim)
  * rs007l_onrobot_rg2_06 (Prim)

## 3. 外部引用Xform简报(Referenced Xforms)

### '/World/Environment' (Xform)

* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/Urban_Building.usdz
* BBox (world): size=(1138.488, 300.000, 524.538), center=(-3.808, 2.648, 14.475)
* 几何统计: Mesh=41, Vertices=16932, Faces=16720
* 子Mesh材质: /World/Environment/Meshes/Sketchfab_model/b63827acdd174d9a8e1e6ab96b34b9f7_fbx/RootNode/industrialWindow_Small/industrialWindow_Small_industrialWindow_Small_0/industrialWindow_Small_industrialWindow_Small_0 -> 未绑定, /World/Environment/Meshes/Sketchfab_model/b63827acdd174d9a8e1e6ab96b34b9f7_fbx/RootNode/industrialWindow_Small_001/industrialWindow_Small_001_industrialWindow_Small_0/industrialWindow_Small_001_industrialWindow_Small_0 -> 未绑定, /World/Environment/Meshes/Sketchfab_model/b63827acdd174d9a8e1e6ab96b34b9f7_fbx/RootNode/industrialWindow_Small_002/industrialWindow_Small_002_industrialWindow_Small_0/industrialWindow_Small_002_industrialWindow_Small_0 -> 未绑定, /World/Environment/Meshes/Sketchfab_model/b63827acdd174d9a8e1e6ab96b34b9f7_fbx/RootNode/industrialWindow_Small_003/industrialWindow_Small_003_industrialWindow_Small_0/industrialWindow_Small_003_industrialWindow_Small_0 -> 未绑定, /World/Environment/Meshes/Sketchfab_model/b63827acdd174d9a8e1e6ab96b34b9f7_fbx/RootNode/industrialWindow_Small_004/industrialWindow_Small_004_industrialWindow_Small_0/industrialWindow_Small_004_industrialWindow_Small_0 -> 未绑定, /World/Environment/Meshes/Sketchfab_model/b63827acdd174d9a8e1e6ab96b34b9f7_fbx/RootNode/industrialWindow_Small_005/industrialWindow_Small_005_industrialWindow_Small_0/industrialWindow_Small_005_industrialWindow_Small_0 -> 未绑定, /World/Environment/Meshes/Sketchfab_model/b63827acdd174d9a8e1e6ab96b34b9f7_fbx/RootNode/industrialWindow_Small_006/industrialWindow_Small_006_industrialWindow_Small_0/industrialWindow_Small_006_industrialWindow_Small_0 -> 未绑定, /World/Environment/Meshes/Sketchfab_model/b63827acdd174d9a8e1e6ab96b34b9f7_fbx/RootNode/industrialWindow_Small_007/industrialWindow_Small_007_industrialWindow_Small_0/industrialWindow_Small_007_industrialWindow_Small_0 -> 未绑定, /World/Environment/Meshes/Sketchfab_model/b63827acdd174d9a8e1e6ab96b34b9f7_fbx/RootNode/industrialWindow_Small_008/industrialWindow_Small_008_industrialWindow_Small_0/industrialWindow_Small_008_industrialWindow_Small_0 -> 未绑定, /World/Environment/Meshes/Sketchfab_model/b63827acdd174d9a8e1e6ab96b34b9f7_fbx/RootNode/industrialWindow_Small_009/industrialWindow_Small_009_industrialWindow_Small_0/industrialWindow_Small_009_industrialWindow_Small_0 -> 未绑定, /World/Environment/Meshes/Sketchfab_model/b63827acdd174d9a8e1e6ab96b34b9f7_fbx/RootNode/industrialWindow_Small_010/industrialWindow_Small_010_industrialWindow_Small_0/industrialWindow_Small_010_industrialWindow_Small_0 -> 未绑定, /World/Environment/Meshes/Sketchfab_model/b63827acdd174d9a8e1e6ab96b34b9f7_fbx/RootNode/industrialWindow_Small_011/industrialWindow_Small_011_industrialWindow_Small_0/industrialWindow_Small_011_industrialWindow_Small_0 -> 未绑定, /World/Environment/Meshes/Sketchfab_model/b63827acdd174d9a8e1e6ab96b34b9f7_fbx/RootNode/industrialWindow_Small_012/industrialWindow_Small_012_industrialWindow_Small_0/industrialWindow_Small_012_industrialWindow_Small_0 -> 未绑定, /World/Environment/Meshes/Sketchfab_model/b63827acdd174d9a8e1e6ab96b34b9f7_fbx/RootNode/industrialWindow_Small_013/industrialWindow_Small_013_industrialWindow_Small_0/industrialWindow_Small_013_industrialWindow_Small_0 -> 未绑定, /World/Environment/Meshes/Sketchfab_model/b63827acdd174d9a8e1e6ab96b34b9f7_fbx/RootNode/industrialWindow_Small_014/industrialWindow_Small_014_industrialWindow_Small_0/industrialWindow_Small_014_industrialWindow_Small_0 -> 未绑定, /World/Environment/Meshes/Sketchfab_model/b63827acdd174d9a8e1e6ab96b34b9f7_fbx/RootNode/industrialDoor/industrialDoor_industrialDoor_0/industrialDoor_industrialDoor_0 -> 未绑定, /World/Environment/Meshes/Sketchfab_model/b63827acdd174d9a8e1e6ab96b34b9f7_fbx/RootNode/concreteStairs/concreteStairs_Atlas_2048x2048_01_0/concreteStairs_Atlas_2048x2048_01_0 -> 未绑定, /World/Environment/Meshes/Sketchfab_model/b63827acdd174d9a8e1e6ab96b34b9f7_fbx/RootNode/buildingMainwalls/buildingMainwalls_Atlas_2048x2048_01_0/buildingMainwalls_Atlas_2048x2048_01_0 -> 未绑定, /World/Environment/Meshes/Sketchfab_model/b63827acdd174d9a8e1e6ab96b34b9f7_fbx/RootNode/wallbaseboard/wallbaseboard_Atlas_2048x2048_01_0/wallbaseboard_Atlas_2048x2048_01_0 -> 未绑定, /World/Environment/Meshes/Sketchfab_model/b63827acdd174d9a8e1e6ab96b34b9f7_fbx/RootNode/metalFrame/metalFrame_Atlas_2048x2048_01_0/metalFrame_Atlas_2048x2048_01_0 -> 未绑定, /World/Environment/Meshes/Sketchfab_model/b63827acdd174d9a8e1e6ab96b34b9f7_fbx/RootNode/mossDecal/mossDecal_decalMoss01_0/mossDecal_decalMoss01_0 -> 未绑定, /World/Environment/Meshes/Sketchfab_model/b63827acdd174d9a8e1e6ab96b34b9f7_fbx/RootNode/building_Roof/building_Roof_Atlas_2048x2048_01_0/building_Roof_Atlas_2048x2048_01_0 -> 未绑定, /World/Environment/Meshes/Sketchfab_model/b63827acdd174d9a8e1e6ab96b34b9f7_fbx/RootNode/woodenFenceType_02/woodenFenceType_02_woodenFence_0/woodenFenceType_02_woodenFence_0 -> 未绑定, /World/Environment/Meshes/Sketchfab_model/b63827acdd174d9a8e1e6ab96b34b9f7_fbx/RootNode/woodenFenceType_01/woodenFenceType_01_woodenFence_0/woodenFenceType_01_woodenFence_0 -> 未绑定, /World/Environment/Meshes/Sketchfab_model/b63827acdd174d9a8e1e6ab96b34b9f7_fbx/RootNode/woodenFenceType_02_001/woodenFenceType_02_001_woodenFence_0/woodenFenceType_02_001_woodenFence_0 -> 未绑定, /World/Environment/Meshes/Sketchfab_model/b63827acdd174d9a8e1e6ab96b34b9f7_fbx/RootNode/eletricBox_Low_001/eletricBox_Low_001_eletricBox_001_0/eletricBox_Low_001_eletricBox_001_0 -> 未绑定, /World/Environment/Meshes/Sketchfab_model/b63827acdd174d9a8e1e6ab96b34b9f7_fbx/RootNode/eletricBox_Low_002/eletricBox_Low_002_eletricBox_001_0/eletricBox_Low_002_eletricBox_001_0 -> 未绑定, /World/Environment/Meshes/Sketchfab_model/b63827acdd174d9a8e1e6ab96b34b9f7_fbx/RootNode/airconditioning_Low_002/airconditioning_Low_002_air_conditioning_001_0/airconditioning_Low_002_air_conditioning_001_0 -> 未绑定, /World/Environment/Meshes/Sketchfab_model/b63827acdd174d9a8e1e6ab96b34b9f7_fbx/RootNode/airconditioningBraket_002/airconditioningBraket_002_air_conditioning_001_0/airconditioningBraket_002_air_conditioning_001_0 -> 未绑定, /World/Environment/Meshes/Sketchfab_model/b63827acdd174d9a8e1e6ab96b34b9f7_fbx/RootNode/airconditioning_Low_003/airconditioning_Low_003_air_conditioning_001_0/airconditioning_Low_003_air_conditioning_001_0 -> 未绑定, /World/Environment/Meshes/Sketchfab_model/b63827acdd174d9a8e1e6ab96b34b9f7_fbx/RootNode/airconditioningBraket_003/airconditioningBraket_003_air_conditioning_001_0/airconditioningBraket_003_air_conditioning_001_0 -> 未绑定, /World/Environment/Meshes/Sketchfab_model/b63827acdd174d9a8e1e6ab96b34b9f7_fbx/RootNode/vents/vents_vents_0/vents_vents_0 -> 未绑定, /World/Environment/Meshes/Sketchfab_model/b63827acdd174d9a8e1e6ab96b34b9f7_fbx/RootNode/vents_001/vents_001_vents_0/vents_001_vents_0 -> 未绑定, /World/Environment/Meshes/Sketchfab_model/b63827acdd174d9a8e1e6ab96b34b9f7_fbx/RootNode/vents_002/vents_002_vents_0/vents_002_vents_0 -> 未绑定, /World/Environment/Meshes/Sketchfab_model/b63827acdd174d9a8e1e6ab96b34b9f7_fbx/RootNode/metalBeams/metalBeams_roofingSheets_0/metalBeams_roofingSheets_0 -> 未绑定, /World/Environment/Meshes/Sketchfab_model/b63827acdd174d9a8e1e6ab96b34b9f7_fbx/RootNode/metalSheet/metalSheet_roofingSheets_0/metalSheet_roofingSheets_0 -> 未绑定, /World/Environment/Meshes/Sketchfab_model/b63827acdd174d9a8e1e6ab96b34b9f7_fbx/RootNode/metalSheet_001/metalSheet_001_roofingSheets_0/metalSheet_001_roofingSheets_0 -> 未绑定, /World/Environment/Meshes/Sketchfab_model/b63827acdd174d9a8e1e6ab96b34b9f7_fbx/RootNode/metalSheet_002/metalSheet_002_roofingSheets_0/metalSheet_002_roofingSheets_0 -> 未绑定, /World/Environment/Meshes/Sketchfab_model/b63827acdd174d9a8e1e6ab96b34b9f7_fbx/RootNode/metalSheet_003/metalSheet_003_roofingSheets_0/metalSheet_003_roofingSheets_0 -> 未绑定, /World/Environment/Meshes/Sketchfab_model/b63827acdd174d9a8e1e6ab96b34b9f7_fbx/RootNode/emptyBillboard/emptyBillboard_emptyBillboard_0/emptyBillboard_emptyBillboard_0 -> 未绑定, /World/Environment/Meshes/Sketchfab_model/b63827acdd174d9a8e1e6ab96b34b9f7_fbx/RootNode/emptyBillboard_001/emptyBillboard_001_emptyBillboard_0/emptyBillboard_001_emptyBillboard_0 -> 未绑定

---

### '/World/Workbench_1' (Xform)

* 引用: reference:/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/5.0/NVIDIA/Assets/DigitalTwin/Assets/Warehouse/Furnishing/Workbenches/MetalWorktable_A/MetalWorktable_A12_01.usd
* BBox (world): size=(200.000, 70.000, 84.000), center=(-0.000, -15.000, 0.420)
* 几何统计: Mesh=2, Vertices=9819, Faces=11939
* 子Mesh材质: /World/Workbench_1/SM_MetalWorktable_A12_01 -> 未绑定, /World/Workbench_1/SM_MetalWorktable_A12_01/SM_MetalWorktable_A12_Locker_01 -> 未绑定

---

### '/World/Workbench_2' (Xform)

* 引用: reference:/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/5.0/NVIDIA/Assets/DigitalTwin/Assets/Warehouse/Furnishing/Workbenches/MetalWorktable_A/MetalWorktable_A12_01.usd
* BBox (world): size=(200.000, 70.000, 84.000), center=(-0.000, -10.000, 0.420)
* 几何统计: Mesh=2, Vertices=9819, Faces=11939
* 子Mesh材质: /World/Workbench_2/SM_MetalWorktable_A12_01 -> 未绑定, /World/Workbench_2/SM_MetalWorktable_A12_01/SM_MetalWorktable_A12_Locker_01 -> 未绑定

---

### '/World/Workbench_3' (Xform)

* 引用: reference:/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/5.0/NVIDIA/Assets/DigitalTwin/Assets/Warehouse/Furnishing/Workbenches/MetalWorktable_A/MetalWorktable_A12_01.usd
* BBox (world): size=(200.000, 70.000, 84.000), center=(-0.000, -5.000, 0.420)
* 几何统计: Mesh=2, Vertices=9819, Faces=11939
* 子Mesh材质: /World/Workbench_3/SM_MetalWorktable_A12_01 -> 未绑定, /World/Workbench_3/SM_MetalWorktable_A12_01/SM_MetalWorktable_A12_Locker_01 -> 未绑定

---

### '/World/Workbench_4' (Xform)

* 引用: reference:/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/5.0/NVIDIA/Assets/DigitalTwin/Assets/Warehouse/Furnishing/Workbenches/MetalWorktable_A/MetalWorktable_A12_01.usd
* BBox (world): size=(200.000, 70.000, 84.000), center=(-0.000, -0.000, 0.420)
* 几何统计: Mesh=2, Vertices=9819, Faces=11939
* 子Mesh材质: /World/Workbench_4/SM_MetalWorktable_A12_01 -> 未绑定, /World/Workbench_4/SM_MetalWorktable_A12_01/SM_MetalWorktable_A12_Locker_01 -> 未绑定

---

### '/World/Workbench_5' (Xform)

* 引用: reference:/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/5.0/NVIDIA/Assets/DigitalTwin/Assets/Warehouse/Furnishing/Workbenches/MetalWorktable_A/MetalWorktable_A12_01.usd
* BBox (world): size=(200.000, 70.000, 84.000), center=(-0.000, 5.000, 0.420)
* 几何统计: Mesh=2, Vertices=9819, Faces=11939
* 子Mesh材质: /World/Workbench_5/SM_MetalWorktable_A12_01 -> 未绑定, /World/Workbench_5/SM_MetalWorktable_A12_01/SM_MetalWorktable_A12_Locker_01 -> 未绑定

---

### '/World/Workbench_6' (Xform)

* 引用: reference:/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/5.0/NVIDIA/Assets/DigitalTwin/Assets/Warehouse/Furnishing/Workbenches/MetalWorktable_A/MetalWorktable_A12_01.usd
* BBox (world): size=(200.000, 70.000, 84.000), center=(-0.000, 10.000, 0.420)
* 几何统计: Mesh=2, Vertices=9819, Faces=11939
* 子Mesh材质: /World/Workbench_6/SM_MetalWorktable_A12_01 -> 未绑定, /World/Workbench_6/SM_MetalWorktable_A12_01/SM_MetalWorktable_A12_Locker_01 -> 未绑定

---

### '/World/Workbench_7' (Xform)

* 引用: reference:/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/5.0/NVIDIA/Assets/DigitalTwin/Assets/Warehouse/Furnishing/Workbenches/MetalWorktable_A/MetalWorktable_A12_01.usd
* BBox (world): size=(200.000, 70.000, 84.000), center=(-0.000, 15.000, 0.420)
* 几何统计: Mesh=2, Vertices=9819, Faces=11939
* 子Mesh材质: /World/Workbench_7/SM_MetalWorktable_A12_01 -> 未绑定, /World/Workbench_7/SM_MetalWorktable_A12_01/SM_MetalWorktable_A12_Locker_01 -> 未绑定

---

### '/World/Conveyor_1' (Xform)

* 引用: reference:/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/ConveyorBelt_A09.usd
* BBox (world): size=(4.003, 1.177, 2.311), center=(-3.001, -15.013, 1.155)
* 几何统计: Mesh=3, Vertices=361700, Faces=388719
* 子Mesh材质: /World/Conveyor_1/SM_ConveyorBelt_A09_02 -> 未绑定, /World/Conveyor_1/SM_ConveyorBelt_A09_Decal_02 -> /World/Conveyor_1/Looks/M_ConveyorBelt_A01_Decal, /World/Conveyor_1/Belt/SM_ConveyorBelt_A09_Belt_02 -> /World/Conveyor_1/Looks/M_ConveyorBelt_A01_Belt
* 材质摘要:
* /World/Conveyor_1/Looks/M_ConveyorBelt_A01_Belt -> Inputs: 'reflection_roughness_texture_influence=1', 'metallic_texture_influence=1', Textures: './T_ConveyorBelt_A01_Belt_Albedo.png', './T_ConveyorBelt_A01_Belt_Normal.png', './T_ConveyorBelt_A01_Belt_ORM.png'
* /World/Conveyor_1/Looks/M_ConveyorBelt_A01_Decal -> Inputs: 'reflection_roughness_texture_influence=1', 'metallic_texture_influence=1', Textures: './T_ConveyorsBelt_A01_Decal_Albedo.png', './T_ConveyorsBelt_A01_Decal_Alpha.png', './T_ConveyorsBelt_A01_Decal_ORM.png'

---

### '/World/Conveyor_2' (Xform)

* 引用: reference:/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/ConveyorBelt_A09.usd
* BBox (world): size=(4.003, 1.177, 2.311), center=(-7.013, -15.013, 1.155)
* 几何统计: Mesh=3, Vertices=361700, Faces=388719
* 子Mesh材质: /World/Conveyor_2/SM_ConveyorBelt_A09_02 -> 未绑定, /World/Conveyor_2/SM_ConveyorBelt_A09_Decal_02 -> /World/Conveyor_2/Looks/M_ConveyorBelt_A01_Decal, /World/Conveyor_2/Belt/SM_ConveyorBelt_A09_Belt_02 -> /World/Conveyor_2/Looks/M_ConveyorBelt_A01_Belt
* 材质摘要:
* /World/Conveyor_2/Looks/M_ConveyorBelt_A01_Belt -> Inputs: 'reflection_roughness_texture_influence=1', 'metallic_texture_influence=1', Textures: './T_ConveyorBelt_A01_Belt_Albedo.png', './T_ConveyorBelt_A01_Belt_Normal.png', './T_ConveyorBelt_A01_Belt_ORM.png'
* /World/Conveyor_2/Looks/M_ConveyorBelt_A01_Decal -> Inputs: 'reflection_roughness_texture_influence=1', 'metallic_texture_influence=1', Textures: './T_ConveyorsBelt_A01_Decal_Albedo.png', './T_ConveyorsBelt_A01_Decal_Alpha.png', './T_ConveyorsBelt_A01_Decal_ORM.png'

---

### '/World/Conveyor_3' (Xform)

* 引用: reference:/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/ConveyorBelt_A09.usd
* BBox (world): size=(4.003, 1.177, 2.311), center=(-11.025, -15.013, 1.155)
* 几何统计: Mesh=3, Vertices=361700, Faces=388719
* 子Mesh材质: /World/Conveyor_3/SM_ConveyorBelt_A09_02 -> 未绑定, /World/Conveyor_3/SM_ConveyorBelt_A09_Decal_02 -> /World/Conveyor_3/Looks/M_ConveyorBelt_A01_Decal, /World/Conveyor_3/Belt/SM_ConveyorBelt_A09_Belt_02 -> /World/Conveyor_3/Looks/M_ConveyorBelt_A01_Belt
* 材质摘要:
* /World/Conveyor_3/Looks/M_ConveyorBelt_A01_Belt -> Inputs: 'reflection_roughness_texture_influence=1', 'metallic_texture_influence=1', Textures: './T_ConveyorBelt_A01_Belt_Albedo.png', './T_ConveyorBelt_A01_Belt_Normal.png', './T_ConveyorBelt_A01_Belt_ORM.png'
* /World/Conveyor_3/Looks/M_ConveyorBelt_A01_Decal -> Inputs: 'reflection_roughness_texture_influence=1', 'metallic_texture_influence=1', Textures: './T_ConveyorsBelt_A01_Decal_Albedo.png', './T_ConveyorsBelt_A01_Decal_Alpha.png', './T_ConveyorsBelt_A01_Decal_ORM.png'

---

### '/World/Conveyor_4' (Xform)

* 引用: reference:/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/ConveyorBelt_A09.usd
* BBox (world): size=(4.003, 1.177, 2.311), center=(-15.037, -15.013, 1.155)
* 几何统计: Mesh=3, Vertices=361700, Faces=388719
* 子Mesh材质: /World/Conveyor_4/SM_ConveyorBelt_A09_02 -> 未绑定, /World/Conveyor_4/SM_ConveyorBelt_A09_Decal_02 -> /World/Conveyor_4/Looks/M_ConveyorBelt_A01_Decal, /World/Conveyor_4/Belt/SM_ConveyorBelt_A09_Belt_02 -> /World/Conveyor_4/Looks/M_ConveyorBelt_A01_Belt
* 材质摘要:
* /World/Conveyor_4/Looks/M_ConveyorBelt_A01_Belt -> Inputs: 'reflection_roughness_texture_influence=1', 'metallic_texture_influence=1', Textures: './T_ConveyorBelt_A01_Belt_Albedo.png', './T_ConveyorBelt_A01_Belt_Normal.png', './T_ConveyorBelt_A01_Belt_ORM.png'
* /World/Conveyor_4/Looks/M_ConveyorBelt_A01_Decal -> Inputs: 'reflection_roughness_texture_influence=1', 'metallic_texture_influence=1', Textures: './T_ConveyorsBelt_A01_Decal_Albedo.png', './T_ConveyorsBelt_A01_Decal_Alpha.png', './T_ConveyorsBelt_A01_Decal_ORM.png'

---

### '/World/Conveyor_5' (Xform)

* 引用: reference:/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/ConveyorBelt_A09.usd
* BBox (world): size=(4.003, 1.177, 2.311), center=(-3.001, -10.013, 1.155)
* 几何统计: Mesh=3, Vertices=361700, Faces=388719
* 子Mesh材质: /World/Conveyor_5/SM_ConveyorBelt_A09_02 -> 未绑定, /World/Conveyor_5/SM_ConveyorBelt_A09_Decal_02 -> /World/Conveyor_5/Looks/M_ConveyorBelt_A01_Decal, /World/Conveyor_5/Belt/SM_ConveyorBelt_A09_Belt_02 -> /World/Conveyor_5/Looks/M_ConveyorBelt_A01_Belt
* 材质摘要:
* /World/Conveyor_5/Looks/M_ConveyorBelt_A01_Belt -> Inputs: 'reflection_roughness_texture_influence=1', 'metallic_texture_influence=1', Textures: './T_ConveyorBelt_A01_Belt_Albedo.png', './T_ConveyorBelt_A01_Belt_Normal.png', './T_ConveyorBelt_A01_Belt_ORM.png'
* /World/Conveyor_5/Looks/M_ConveyorBelt_A01_Decal -> Inputs: 'reflection_roughness_texture_influence=1', 'metallic_texture_influence=1', Textures: './T_ConveyorsBelt_A01_Decal_Albedo.png', './T_ConveyorsBelt_A01_Decal_Alpha.png', './T_ConveyorsBelt_A01_Decal_ORM.png'

---

### '/World/Conveyor_6' (Xform)

* 引用: reference:/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/ConveyorBelt_A09.usd
* BBox (world): size=(4.003, 1.177, 2.311), center=(-7.013, -10.013, 1.155)
* 几何统计: Mesh=3, Vertices=361700, Faces=388719
* 子Mesh材质: /World/Conveyor_6/SM_ConveyorBelt_A09_02 -> 未绑定, /World/Conveyor_6/SM_ConveyorBelt_A09_Decal_02 -> /World/Conveyor_6/Looks/M_ConveyorBelt_A01_Decal, /World/Conveyor_6/Belt/SM_ConveyorBelt_A09_Belt_02 -> /World/Conveyor_6/Looks/M_ConveyorBelt_A01_Belt
* 材质摘要:
* /World/Conveyor_6/Looks/M_ConveyorBelt_A01_Belt -> Inputs: 'reflection_roughness_texture_influence=1', 'metallic_texture_influence=1', Textures: './T_ConveyorBelt_A01_Belt_Albedo.png', './T_ConveyorBelt_A01_Belt_Normal.png', './T_ConveyorBelt_A01_Belt_ORM.png'
* /World/Conveyor_6/Looks/M_ConveyorBelt_A01_Decal -> Inputs: 'reflection_roughness_texture_influence=1', 'metallic_texture_influence=1', Textures: './T_ConveyorsBelt_A01_Decal_Albedo.png', './T_ConveyorsBelt_A01_Decal_Alpha.png', './T_ConveyorsBelt_A01_Decal_ORM.png'

---

### '/World/Conveyor_7' (Xform)

* 引用: reference:/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/ConveyorBelt_A09.usd
* BBox (world): size=(4.003, 1.177, 2.311), center=(-11.025, -10.013, 1.155)
* 几何统计: Mesh=3, Vertices=361700, Faces=388719
* 子Mesh材质: /World/Conveyor_7/SM_ConveyorBelt_A09_02 -> 未绑定, /World/Conveyor_7/SM_ConveyorBelt_A09_Decal_02 -> /World/Conveyor_7/Looks/M_ConveyorBelt_A01_Decal, /World/Conveyor_7/Belt/SM_ConveyorBelt_A09_Belt_02 -> /World/Conveyor_7/Looks/M_ConveyorBelt_A01_Belt
* 材质摘要:
* /World/Conveyor_7/Looks/M_ConveyorBelt_A01_Belt -> Inputs: 'reflection_roughness_texture_influence=1', 'metallic_texture_influence=1', Textures: './T_ConveyorBelt_A01_Belt_Albedo.png', './T_ConveyorBelt_A01_Belt_Normal.png', './T_ConveyorBelt_A01_Belt_ORM.png'
* /World/Conveyor_7/Looks/M_ConveyorBelt_A01_Decal -> Inputs: 'reflection_roughness_texture_influence=1', 'metallic_texture_influence=1', Textures: './T_ConveyorsBelt_A01_Decal_Albedo.png', './T_ConveyorsBelt_A01_Decal_Alpha.png', './T_ConveyorsBelt_A01_Decal_ORM.png'

---

### '/World/Conveyor_8' (Xform)

* 引用: reference:/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/ConveyorBelt_A09.usd
* BBox (world): size=(4.003, 1.177, 2.311), center=(-15.037, -10.013, 1.155)
* 几何统计: Mesh=3, Vertices=361700, Faces=388719
* 子Mesh材质: /World/Conveyor_8/SM_ConveyorBelt_A09_02 -> 未绑定, /World/Conveyor_8/SM_ConveyorBelt_A09_Decal_02 -> /World/Conveyor_8/Looks/M_ConveyorBelt_A01_Decal, /World/Conveyor_8/Belt/SM_ConveyorBelt_A09_Belt_02 -> /World/Conveyor_8/Looks/M_ConveyorBelt_A01_Belt
* 材质摘要:
* /World/Conveyor_8/Looks/M_ConveyorBelt_A01_Belt -> Inputs: 'reflection_roughness_texture_influence=1', 'metallic_texture_influence=1', Textures: './T_ConveyorBelt_A01_Belt_Albedo.png', './T_ConveyorBelt_A01_Belt_Normal.png', './T_ConveyorBelt_A01_Belt_ORM.png'
* /World/Conveyor_8/Looks/M_ConveyorBelt_A01_Decal -> Inputs: 'reflection_roughness_texture_influence=1', 'metallic_texture_influence=1', Textures: './T_ConveyorsBelt_A01_Decal_Albedo.png', './T_ConveyorsBelt_A01_Decal_Alpha.png', './T_ConveyorsBelt_A01_Decal_ORM.png'

---

### '/World/Conveyor_9' (Xform)

* 引用: reference:/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/ConveyorBelt_A09.usd
* BBox (world): size=(4.003, 1.177, 2.311), center=(-3.001, -5.013, 1.155)
* 几何统计: Mesh=3, Vertices=361700, Faces=388719
* 子Mesh材质: /World/Conveyor_9/SM_ConveyorBelt_A09_02 -> 未绑定, /World/Conveyor_9/SM_ConveyorBelt_A09_Decal_02 -> /World/Conveyor_9/Looks/M_ConveyorBelt_A01_Decal, /World/Conveyor_9/Belt/SM_ConveyorBelt_A09_Belt_02 -> /World/Conveyor_9/Looks/M_ConveyorBelt_A01_Belt
* 材质摘要:
* /World/Conveyor_9/Looks/M_ConveyorBelt_A01_Belt -> Inputs: 'reflection_roughness_texture_influence=1', 'metallic_texture_influence=1', Textures: './T_ConveyorBelt_A01_Belt_Albedo.png', './T_ConveyorBelt_A01_Belt_Normal.png', './T_ConveyorBelt_A01_Belt_ORM.png'
* /World/Conveyor_9/Looks/M_ConveyorBelt_A01_Decal -> Inputs: 'reflection_roughness_texture_influence=1', 'metallic_texture_influence=1', Textures: './T_ConveyorsBelt_A01_Decal_Albedo.png', './T_ConveyorsBelt_A01_Decal_Alpha.png', './T_ConveyorsBelt_A01_Decal_ORM.png'

---

### '/World/Conveyor_10' (Xform)

* 引用: reference:/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/ConveyorBelt_A09.usd
* BBox (world): size=(4.003, 1.177, 2.311), center=(-7.013, -5.013, 1.155)
* 几何统计: Mesh=3, Vertices=361700, Faces=388719
* 子Mesh材质: /World/Conveyor_10/SM_ConveyorBelt_A09_02 -> 未绑定, /World/Conveyor_10/SM_ConveyorBelt_A09_Decal_02 -> /World/Conveyor_10/Looks/M_ConveyorBelt_A01_Decal, /World/Conveyor_10/Belt/SM_ConveyorBelt_A09_Belt_02 -> /World/Conveyor_10/Looks/M_ConveyorBelt_A01_Belt
* 材质摘要:
* /World/Conveyor_10/Looks/M_ConveyorBelt_A01_Belt -> Inputs: 'reflection_roughness_texture_influence=1', 'metallic_texture_influence=1', Textures: './T_ConveyorBelt_A01_Belt_Albedo.png', './T_ConveyorBelt_A01_Belt_Normal.png', './T_ConveyorBelt_A01_Belt_ORM.png'
* /World/Conveyor_10/Looks/M_ConveyorBelt_A01_Decal -> Inputs: 'reflection_roughness_texture_influence=1', 'metallic_texture_influence=1', Textures: './T_ConveyorsBelt_A01_Decal_Albedo.png', './T_ConveyorsBelt_A01_Decal_Alpha.png', './T_ConveyorsBelt_A01_Decal_ORM.png'

---

### '/World/Conveyor_11' (Xform)

* 引用: reference:/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/ConveyorBelt_A09.usd
* BBox (world): size=(4.003, 1.177, 2.311), center=(-11.025, -5.013, 1.155)
* 几何统计: Mesh=3, Vertices=361700, Faces=388719
* 子Mesh材质: /World/Conveyor_11/SM_ConveyorBelt_A09_02 -> 未绑定, /World/Conveyor_11/SM_ConveyorBelt_A09_Decal_02 -> /World/Conveyor_11/Looks/M_ConveyorBelt_A01_Decal, /World/Conveyor_11/Belt/SM_ConveyorBelt_A09_Belt_02 -> /World/Conveyor_11/Looks/M_ConveyorBelt_A01_Belt
* 材质摘要:
* /World/Conveyor_11/Looks/M_ConveyorBelt_A01_Belt -> Inputs: 'reflection_roughness_texture_influence=1', 'metallic_texture_influence=1', Textures: './T_ConveyorBelt_A01_Belt_Albedo.png', './T_ConveyorBelt_A01_Belt_Normal.png', './T_ConveyorBelt_A01_Belt_ORM.png'
* /World/Conveyor_11/Looks/M_ConveyorBelt_A01_Decal -> Inputs: 'reflection_roughness_texture_influence=1', 'metallic_texture_influence=1', Textures: './T_ConveyorsBelt_A01_Decal_Albedo.png', './T_ConveyorsBelt_A01_Decal_Alpha.png', './T_ConveyorsBelt_A01_Decal_ORM.png'

---

### '/World/Conveyor_12' (Xform)

* 引用: reference:/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/ConveyorBelt_A09.usd
* BBox (world): size=(4.003, 1.177, 2.311), center=(-15.037, -5.013, 1.155)
* 几何统计: Mesh=3, Vertices=361700, Faces=388719
* 子Mesh材质: /World/Conveyor_12/SM_ConveyorBelt_A09_02 -> 未绑定, /World/Conveyor_12/SM_ConveyorBelt_A09_Decal_02 -> /World/Conveyor_12/Looks/M_ConveyorBelt_A01_Decal, /World/Conveyor_12/Belt/SM_ConveyorBelt_A09_Belt_02 -> /World/Conveyor_12/Looks/M_ConveyorBelt_A01_Belt
* 材质摘要:
* /World/Conveyor_12/Looks/M_ConveyorBelt_A01_Belt -> Inputs: 'reflection_roughness_texture_influence=1', 'metallic_texture_influence=1', Textures: './T_ConveyorBelt_A01_Belt_Albedo.png', './T_ConveyorBelt_A01_Belt_Normal.png', './T_ConveyorBelt_A01_Belt_ORM.png'
* /World/Conveyor_12/Looks/M_ConveyorBelt_A01_Decal -> Inputs: 'reflection_roughness_texture_influence=1', 'metallic_texture_influence=1', Textures: './T_ConveyorsBelt_A01_Decal_Albedo.png', './T_ConveyorsBelt_A01_Decal_Alpha.png', './T_ConveyorsBelt_A01_Decal_ORM.png'

---

### '/World/Conveyor_13' (Xform)

* 引用: reference:/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/ConveyorBelt_A09.usd
* BBox (world): size=(4.003, 1.177, 2.311), center=(-3.001, -0.013, 1.155)
* 几何统计: Mesh=3, Vertices=361700, Faces=388719
* 子Mesh材质: /World/Conveyor_13/SM_ConveyorBelt_A09_02 -> 未绑定, /World/Conveyor_13/SM_ConveyorBelt_A09_Decal_02 -> /World/Conveyor_13/Looks/M_ConveyorBelt_A01_Decal, /World/Conveyor_13/Belt/SM_ConveyorBelt_A09_Belt_02 -> /World/Conveyor_13/Looks/M_ConveyorBelt_A01_Belt
* 材质摘要:
* /World/Conveyor_13/Looks/M_ConveyorBelt_A01_Belt -> Inputs: 'reflection_roughness_texture_influence=1', 'metallic_texture_influence=1', Textures: './T_ConveyorBelt_A01_Belt_Albedo.png', './T_ConveyorBelt_A01_Belt_Normal.png', './T_ConveyorBelt_A01_Belt_ORM.png'
* /World/Conveyor_13/Looks/M_ConveyorBelt_A01_Decal -> Inputs: 'reflection_roughness_texture_influence=1', 'metallic_texture_influence=1', Textures: './T_ConveyorsBelt_A01_Decal_Albedo.png', './T_ConveyorsBelt_A01_Decal_Alpha.png', './T_ConveyorsBelt_A01_Decal_ORM.png'

---

### '/World/Conveyor_14' (Xform)

* 引用: reference:/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/ConveyorBelt_A09.usd
* BBox (world): size=(4.003, 1.177, 2.311), center=(-7.013, -0.013, 1.155)
* 几何统计: Mesh=3, Vertices=361700, Faces=388719
* 子Mesh材质: /World/Conveyor_14/SM_ConveyorBelt_A09_02 -> 未绑定, /World/Conveyor_14/SM_ConveyorBelt_A09_Decal_02 -> /World/Conveyor_14/Looks/M_ConveyorBelt_A01_Decal, /World/Conveyor_14/Belt/SM_ConveyorBelt_A09_Belt_02 -> /World/Conveyor_14/Looks/M_ConveyorBelt_A01_Belt
* 材质摘要:
* /World/Conveyor_14/Looks/M_ConveyorBelt_A01_Belt -> Inputs: 'reflection_roughness_texture_influence=1', 'metallic_texture_influence=1', Textures: './T_ConveyorBelt_A01_Belt_Albedo.png', './T_ConveyorBelt_A01_Belt_Normal.png', './T_ConveyorBelt_A01_Belt_ORM.png'
* /World/Conveyor_14/Looks/M_ConveyorBelt_A01_Decal -> Inputs: 'reflection_roughness_texture_influence=1', 'metallic_texture_influence=1', Textures: './T_ConveyorsBelt_A01_Decal_Albedo.png', './T_ConveyorsBelt_A01_Decal_Alpha.png', './T_ConveyorsBelt_A01_Decal_ORM.png'

---

### '/World/Conveyor_15' (Xform)

* 引用: reference:/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/ConveyorBelt_A09.usd
* BBox (world): size=(4.003, 1.177, 2.311), center=(-11.025, -0.013, 1.155)
* 几何统计: Mesh=3, Vertices=361700, Faces=388719
* 子Mesh材质: /World/Conveyor_15/SM_ConveyorBelt_A09_02 -> 未绑定, /World/Conveyor_15/SM_ConveyorBelt_A09_Decal_02 -> /World/Conveyor_15/Looks/M_ConveyorBelt_A01_Decal, /World/Conveyor_15/Belt/SM_ConveyorBelt_A09_Belt_02 -> /World/Conveyor_15/Looks/M_ConveyorBelt_A01_Belt
* 材质摘要:
* /World/Conveyor_15/Looks/M_ConveyorBelt_A01_Belt -> Inputs: 'reflection_roughness_texture_influence=1', 'metallic_texture_influence=1', Textures: './T_ConveyorBelt_A01_Belt_Albedo.png', './T_ConveyorBelt_A01_Belt_Normal.png', './T_ConveyorBelt_A01_Belt_ORM.png'
* /World/Conveyor_15/Looks/M_ConveyorBelt_A01_Decal -> Inputs: 'reflection_roughness_texture_influence=1', 'metallic_texture_influence=1', Textures: './T_ConveyorsBelt_A01_Decal_Albedo.png', './T_ConveyorsBelt_A01_Decal_Alpha.png', './T_ConveyorsBelt_A01_Decal_ORM.png'

---

### '/World/Conveyor_16' (Xform)

* 引用: reference:/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/ConveyorBelt_A09.usd
* BBox (world): size=(4.003, 1.177, 2.311), center=(-15.037, -0.013, 1.155)
* 几何统计: Mesh=3, Vertices=361700, Faces=388719
* 子Mesh材质: /World/Conveyor_16/SM_ConveyorBelt_A09_02 -> 未绑定, /World/Conveyor_16/SM_ConveyorBelt_A09_Decal_02 -> /World/Conveyor_16/Looks/M_ConveyorBelt_A01_Decal, /World/Conveyor_16/Belt/SM_ConveyorBelt_A09_Belt_02 -> /World/Conveyor_16/Looks/M_ConveyorBelt_A01_Belt
* 材质摘要:
* /World/Conveyor_16/Looks/M_ConveyorBelt_A01_Belt -> Inputs: 'reflection_roughness_texture_influence=1', 'metallic_texture_influence=1', Textures: './T_ConveyorBelt_A01_Belt_Albedo.png', './T_ConveyorBelt_A01_Belt_Normal.png', './T_ConveyorBelt_A01_Belt_ORM.png'
* /World/Conveyor_16/Looks/M_ConveyorBelt_A01_Decal -> Inputs: 'reflection_roughness_texture_influence=1', 'metallic_texture_influence=1', Textures: './T_ConveyorsBelt_A01_Decal_Albedo.png', './T_ConveyorsBelt_A01_Decal_Alpha.png', './T_ConveyorsBelt_A01_Decal_ORM.png'

---

### '/World/Conveyor_17' (Xform)

* 引用: reference:/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/ConveyorBelt_A09.usd
* BBox (world): size=(4.003, 1.177, 2.311), center=(-3.001, 4.987, 1.155)
* 几何统计: Mesh=3, Vertices=361700, Faces=388719
* 子Mesh材质: /World/Conveyor_17/SM_ConveyorBelt_A09_02 -> 未绑定, /World/Conveyor_17/SM_ConveyorBelt_A09_Decal_02 -> /World/Conveyor_17/Looks/M_ConveyorBelt_A01_Decal, /World/Conveyor_17/Belt/SM_ConveyorBelt_A09_Belt_02 -> /World/Conveyor_17/Looks/M_ConveyorBelt_A01_Belt
* 材质摘要:
* /World/Conveyor_17/Looks/M_ConveyorBelt_A01_Belt -> Inputs: 'reflection_roughness_texture_influence=1', 'metallic_texture_influence=1', Textures: './T_ConveyorBelt_A01_Belt_Albedo.png', './T_ConveyorBelt_A01_Belt_Normal.png', './T_ConveyorBelt_A01_Belt_ORM.png'
* /World/Conveyor_17/Looks/M_ConveyorBelt_A01_Decal -> Inputs: 'reflection_roughness_texture_influence=1', 'metallic_texture_influence=1', Textures: './T_ConveyorsBelt_A01_Decal_Albedo.png', './T_ConveyorsBelt_A01_Decal_Alpha.png', './T_ConveyorsBelt_A01_Decal_ORM.png'

---

### '/World/Conveyor_18' (Xform)

* 引用: reference:/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/ConveyorBelt_A09.usd
* BBox (world): size=(4.003, 1.177, 2.311), center=(-7.013, 4.987, 1.155)
* 几何统计: Mesh=3, Vertices=361700, Faces=388719
* 子Mesh材质: /World/Conveyor_18/SM_ConveyorBelt_A09_02 -> 未绑定, /World/Conveyor_18/SM_ConveyorBelt_A09_Decal_02 -> /World/Conveyor_18/Looks/M_ConveyorBelt_A01_Decal, /World/Conveyor_18/Belt/SM_ConveyorBelt_A09_Belt_02 -> /World/Conveyor_18/Looks/M_ConveyorBelt_A01_Belt
* 材质摘要:
* /World/Conveyor_18/Looks/M_ConveyorBelt_A01_Belt -> Inputs: 'reflection_roughness_texture_influence=1', 'metallic_texture_influence=1', Textures: './T_ConveyorBelt_A01_Belt_Albedo.png', './T_ConveyorBelt_A01_Belt_Normal.png', './T_ConveyorBelt_A01_Belt_ORM.png'
* /World/Conveyor_18/Looks/M_ConveyorBelt_A01_Decal -> Inputs: 'reflection_roughness_texture_influence=1', 'metallic_texture_influence=1', Textures: './T_ConveyorsBelt_A01_Decal_Albedo.png', './T_ConveyorsBelt_A01_Decal_Alpha.png', './T_ConveyorsBelt_A01_Decal_ORM.png'

---

### '/World/Conveyor_19' (Xform)

* 引用: reference:/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/ConveyorBelt_A09.usd
* BBox (world): size=(4.003, 1.177, 2.311), center=(-11.025, 4.987, 1.155)
* 几何统计: Mesh=3, Vertices=361700, Faces=388719
* 子Mesh材质: /World/Conveyor_19/SM_ConveyorBelt_A09_02 -> 未绑定, /World/Conveyor_19/SM_ConveyorBelt_A09_Decal_02 -> /World/Conveyor_19/Looks/M_ConveyorBelt_A01_Decal, /World/Conveyor_19/Belt/SM_ConveyorBelt_A09_Belt_02 -> /World/Conveyor_19/Looks/M_ConveyorBelt_A01_Belt
* 材质摘要:
* /World/Conveyor_19/Looks/M_ConveyorBelt_A01_Belt -> Inputs: 'reflection_roughness_texture_influence=1', 'metallic_texture_influence=1', Textures: './T_ConveyorBelt_A01_Belt_Albedo.png', './T_ConveyorBelt_A01_Belt_Normal.png', './T_ConveyorBelt_A01_Belt_ORM.png'
* /World/Conveyor_19/Looks/M_ConveyorBelt_A01_Decal -> Inputs: 'reflection_roughness_texture_influence=1', 'metallic_texture_influence=1', Textures: './T_ConveyorsBelt_A01_Decal_Albedo.png', './T_ConveyorsBelt_A01_Decal_Alpha.png', './T_ConveyorsBelt_A01_Decal_ORM.png'

---

### '/World/Conveyor_20' (Xform)

* 引用: reference:/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/ConveyorBelt_A09.usd
* BBox (world): size=(4.003, 1.177, 2.311), center=(-15.037, 4.987, 1.155)
* 几何统计: Mesh=3, Vertices=361700, Faces=388719
* 子Mesh材质: /World/Conveyor_20/SM_ConveyorBelt_A09_02 -> 未绑定, /World/Conveyor_20/SM_ConveyorBelt_A09_Decal_02 -> /World/Conveyor_20/Looks/M_ConveyorBelt_A01_Decal, /World/Conveyor_20/Belt/SM_ConveyorBelt_A09_Belt_02 -> /World/Conveyor_20/Looks/M_ConveyorBelt_A01_Belt
* 材质摘要:
* /World/Conveyor_20/Looks/M_ConveyorBelt_A01_Belt -> Inputs: 'reflection_roughness_texture_influence=1', 'metallic_texture_influence=1', Textures: './T_ConveyorBelt_A01_Belt_Albedo.png', './T_ConveyorBelt_A01_Belt_Normal.png', './T_ConveyorBelt_A01_Belt_ORM.png'
* /World/Conveyor_20/Looks/M_ConveyorBelt_A01_Decal -> Inputs: 'reflection_roughness_texture_influence=1', 'metallic_texture_influence=1', Textures: './T_ConveyorsBelt_A01_Decal_Albedo.png', './T_ConveyorsBelt_A01_Decal_Alpha.png', './T_ConveyorsBelt_A01_Decal_ORM.png'

---

### '/World/Conveyor_21' (Xform)

* 引用: reference:/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/ConveyorBelt_A09.usd
* BBox (world): size=(4.003, 1.177, 2.311), center=(-3.001, 9.987, 1.155)
* 几何统计: Mesh=3, Vertices=361700, Faces=388719
* 子Mesh材质: /World/Conveyor_21/SM_ConveyorBelt_A09_02 -> 未绑定, /World/Conveyor_21/SM_ConveyorBelt_A09_Decal_02 -> /World/Conveyor_21/Looks/M_ConveyorBelt_A01_Decal, /World/Conveyor_21/Belt/SM_ConveyorBelt_A09_Belt_02 -> /World/Conveyor_21/Looks/M_ConveyorBelt_A01_Belt
* 材质摘要:
* /World/Conveyor_21/Looks/M_ConveyorBelt_A01_Belt -> Inputs: 'reflection_roughness_texture_influence=1', 'metallic_texture_influence=1', Textures: './T_ConveyorBelt_A01_Belt_Albedo.png', './T_ConveyorBelt_A01_Belt_Normal.png', './T_ConveyorBelt_A01_Belt_ORM.png'
* /World/Conveyor_21/Looks/M_ConveyorBelt_A01_Decal -> Inputs: 'reflection_roughness_texture_influence=1', 'metallic_texture_influence=1', Textures: './T_ConveyorsBelt_A01_Decal_Albedo.png', './T_ConveyorsBelt_A01_Decal_Alpha.png', './T_ConveyorsBelt_A01_Decal_ORM.png'

---

### '/World/Conveyor_22' (Xform)

* 引用: reference:/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/ConveyorBelt_A09.usd
* BBox (world): size=(4.003, 1.177, 2.311), center=(-7.013, 9.987, 1.155)
* 几何统计: Mesh=3, Vertices=361700, Faces=388719
* 子Mesh材质: /World/Conveyor_22/SM_ConveyorBelt_A09_02 -> 未绑定, /World/Conveyor_22/SM_ConveyorBelt_A09_Decal_02 -> /World/Conveyor_22/Looks/M_ConveyorBelt_A01_Decal, /World/Conveyor_22/Belt/SM_ConveyorBelt_A09_Belt_02 -> /World/Conveyor_22/Looks/M_ConveyorBelt_A01_Belt
* 材质摘要:
* /World/Conveyor_22/Looks/M_ConveyorBelt_A01_Belt -> Inputs: 'reflection_roughness_texture_influence=1', 'metallic_texture_influence=1', Textures: './T_ConveyorBelt_A01_Belt_Albedo.png', './T_ConveyorBelt_A01_Belt_Normal.png', './T_ConveyorBelt_A01_Belt_ORM.png'
* /World/Conveyor_22/Looks/M_ConveyorBelt_A01_Decal -> Inputs: 'reflection_roughness_texture_influence=1', 'metallic_texture_influence=1', Textures: './T_ConveyorsBelt_A01_Decal_Albedo.png', './T_ConveyorsBelt_A01_Decal_Alpha.png', './T_ConveyorsBelt_A01_Decal_ORM.png'

---

### '/World/Conveyor_23' (Xform)

* 引用: reference:/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/ConveyorBelt_A09.usd
* BBox (world): size=(4.003, 1.177, 2.311), center=(-11.025, 9.987, 1.155)
* 几何统计: Mesh=3, Vertices=361700, Faces=388719
* 子Mesh材质: /World/Conveyor_23/SM_ConveyorBelt_A09_02 -> 未绑定, /World/Conveyor_23/SM_ConveyorBelt_A09_Decal_02 -> /World/Conveyor_23/Looks/M_ConveyorBelt_A01_Decal, /World/Conveyor_23/Belt/SM_ConveyorBelt_A09_Belt_02 -> /World/Conveyor_23/Looks/M_ConveyorBelt_A01_Belt
* 材质摘要:
* /World/Conveyor_23/Looks/M_ConveyorBelt_A01_Belt -> Inputs: 'reflection_roughness_texture_influence=1', 'metallic_texture_influence=1', Textures: './T_ConveyorBelt_A01_Belt_Albedo.png', './T_ConveyorBelt_A01_Belt_Normal.png', './T_ConveyorBelt_A01_Belt_ORM.png'
* /World/Conveyor_23/Looks/M_ConveyorBelt_A01_Decal -> Inputs: 'reflection_roughness_texture_influence=1', 'metallic_texture_influence=1', Textures: './T_ConveyorsBelt_A01_Decal_Albedo.png', './T_ConveyorsBelt_A01_Decal_Alpha.png', './T_ConveyorsBelt_A01_Decal_ORM.png'

---

### '/World/Conveyor_24' (Xform)

* 引用: reference:/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/ConveyorBelt_A09.usd
* BBox (world): size=(4.003, 1.177, 2.311), center=(-15.037, 9.987, 1.155)
* 几何统计: Mesh=3, Vertices=361700, Faces=388719
* 子Mesh材质: /World/Conveyor_24/SM_ConveyorBelt_A09_02 -> 未绑定, /World/Conveyor_24/SM_ConveyorBelt_A09_Decal_02 -> /World/Conveyor_24/Looks/M_ConveyorBelt_A01_Decal, /World/Conveyor_24/Belt/SM_ConveyorBelt_A09_Belt_02 -> /World/Conveyor_24/Looks/M_ConveyorBelt_A01_Belt
* 材质摘要:
* /World/Conveyor_24/Looks/M_ConveyorBelt_A01_Belt -> Inputs: 'reflection_roughness_texture_influence=1', 'metallic_texture_influence=1', Textures: './T_ConveyorBelt_A01_Belt_Albedo.png', './T_ConveyorBelt_A01_Belt_Normal.png', './T_ConveyorBelt_A01_Belt_ORM.png'
* /World/Conveyor_24/Looks/M_ConveyorBelt_A01_Decal -> Inputs: 'reflection_roughness_texture_influence=1', 'metallic_texture_influence=1', Textures: './T_ConveyorsBelt_A01_Decal_Albedo.png', './T_ConveyorsBelt_A01_Decal_Alpha.png', './T_ConveyorsBelt_A01_Decal_ORM.png'

---

### '/World/Conveyor_25' (Xform)

* 引用: reference:/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/ConveyorBelt_A09.usd
* BBox (world): size=(4.003, 1.177, 2.311), center=(-3.001, 14.987, 1.155)
* 几何统计: Mesh=3, Vertices=361700, Faces=388719
* 子Mesh材质: /World/Conveyor_25/SM_ConveyorBelt_A09_02 -> 未绑定, /World/Conveyor_25/SM_ConveyorBelt_A09_Decal_02 -> /World/Conveyor_25/Looks/M_ConveyorBelt_A01_Decal, /World/Conveyor_25/Belt/SM_ConveyorBelt_A09_Belt_02 -> /World/Conveyor_25/Looks/M_ConveyorBelt_A01_Belt
* 材质摘要:
* /World/Conveyor_25/Looks/M_ConveyorBelt_A01_Belt -> Inputs: 'reflection_roughness_texture_influence=1', 'metallic_texture_influence=1', Textures: './T_ConveyorBelt_A01_Belt_Albedo.png', './T_ConveyorBelt_A01_Belt_Normal.png', './T_ConveyorBelt_A01_Belt_ORM.png'
* /World/Conveyor_25/Looks/M_ConveyorBelt_A01_Decal -> Inputs: 'reflection_roughness_texture_influence=1', 'metallic_texture_influence=1', Textures: './T_ConveyorsBelt_A01_Decal_Albedo.png', './T_ConveyorsBelt_A01_Decal_Alpha.png', './T_ConveyorsBelt_A01_Decal_ORM.png'

---

### '/World/Conveyor_26' (Xform)

* 引用: reference:/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/ConveyorBelt_A09.usd
* BBox (world): size=(4.003, 1.177, 2.311), center=(-7.013, 14.987, 1.155)
* 几何统计: Mesh=3, Vertices=361700, Faces=388719
* 子Mesh材质: /World/Conveyor_26/SM_ConveyorBelt_A09_02 -> 未绑定, /World/Conveyor_26/SM_ConveyorBelt_A09_Decal_02 -> /World/Conveyor_26/Looks/M_ConveyorBelt_A01_Decal, /World/Conveyor_26/Belt/SM_ConveyorBelt_A09_Belt_02 -> /World/Conveyor_26/Looks/M_ConveyorBelt_A01_Belt
* 材质摘要:
* /World/Conveyor_26/Looks/M_ConveyorBelt_A01_Belt -> Inputs: 'reflection_roughness_texture_influence=1', 'metallic_texture_influence=1', Textures: './T_ConveyorBelt_A01_Belt_Albedo.png', './T_ConveyorBelt_A01_Belt_Normal.png', './T_ConveyorBelt_A01_Belt_ORM.png'
* /World/Conveyor_26/Looks/M_ConveyorBelt_A01_Decal -> Inputs: 'reflection_roughness_texture_influence=1', 'metallic_texture_influence=1', Textures: './T_ConveyorsBelt_A01_Decal_Albedo.png', './T_ConveyorsBelt_A01_Decal_Alpha.png', './T_ConveyorsBelt_A01_Decal_ORM.png'

---

### '/World/Conveyor_27' (Xform)

* 引用: reference:/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/ConveyorBelt_A09.usd
* BBox (world): size=(4.003, 1.177, 2.311), center=(-11.025, 14.987, 1.155)
* 几何统计: Mesh=3, Vertices=361700, Faces=388719
* 子Mesh材质: /World/Conveyor_27/SM_ConveyorBelt_A09_02 -> 未绑定, /World/Conveyor_27/SM_ConveyorBelt_A09_Decal_02 -> /World/Conveyor_27/Looks/M_ConveyorBelt_A01_Decal, /World/Conveyor_27/Belt/SM_ConveyorBelt_A09_Belt_02 -> /World/Conveyor_27/Looks/M_ConveyorBelt_A01_Belt
* 材质摘要:
* /World/Conveyor_27/Looks/M_ConveyorBelt_A01_Belt -> Inputs: 'reflection_roughness_texture_influence=1', 'metallic_texture_influence=1', Textures: './T_ConveyorBelt_A01_Belt_Albedo.png', './T_ConveyorBelt_A01_Belt_Normal.png', './T_ConveyorBelt_A01_Belt_ORM.png'
* /World/Conveyor_27/Looks/M_ConveyorBelt_A01_Decal -> Inputs: 'reflection_roughness_texture_influence=1', 'metallic_texture_influence=1', Textures: './T_ConveyorsBelt_A01_Decal_Albedo.png', './T_ConveyorsBelt_A01_Decal_Alpha.png', './T_ConveyorsBelt_A01_Decal_ORM.png'

---

### '/World/Conveyor_28' (Xform)

* 引用: reference:/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/ConveyorBelt_A09.usd
* BBox (world): size=(4.003, 1.177, 2.311), center=(-15.037, 14.987, 1.155)
* 几何统计: Mesh=3, Vertices=361700, Faces=388719
* 子Mesh材质: /World/Conveyor_28/SM_ConveyorBelt_A09_02 -> 未绑定, /World/Conveyor_28/SM_ConveyorBelt_A09_Decal_02 -> /World/Conveyor_28/Looks/M_ConveyorBelt_A01_Decal, /World/Conveyor_28/Belt/SM_ConveyorBelt_A09_Belt_02 -> /World/Conveyor_28/Looks/M_ConveyorBelt_A01_Belt
* 材质摘要:
* /World/Conveyor_28/Looks/M_ConveyorBelt_A01_Belt -> Inputs: 'reflection_roughness_texture_influence=1', 'metallic_texture_influence=1', Textures: './T_ConveyorBelt_A01_Belt_Albedo.png', './T_ConveyorBelt_A01_Belt_Normal.png', './T_ConveyorBelt_A01_Belt_ORM.png'
* /World/Conveyor_28/Looks/M_ConveyorBelt_A01_Decal -> Inputs: 'reflection_roughness_texture_influence=1', 'metallic_texture_influence=1', Textures: './T_ConveyorsBelt_A01_Decal_Albedo.png', './T_ConveyorsBelt_A01_Decal_Alpha.png', './T_ConveyorsBelt_A01_Decal_ORM.png'

---

### '/World/PartA_OnBelt_1' (Xform)

* 引用: reference:/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ban_Yuan_Jian/Woodruff keys GB_converted/0;Size=1.0x1.4x4;SUPPRESSION=Default.usd
* BBox (world): size=(3.816, 1.400, 1.000), center=(-1.400, -14.870, 1.830)
* 几何统计: Mesh=1, Vertices=414, Faces=824
* 子Mesh材质: /World/PartA_OnBelt_1/node__Size_1_0x1_4x4_SUPPRESSION_Default/geometry_1 -> 未绑定

---

### '/World/PartA_OnBelt_2' (Xform)

* 引用: reference:/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ban_Yuan_Jian/Woodruff keys GB_converted/0;Size=1.0x1.4x4;SUPPRESSION=Default.usd
* BBox (world): size=(3.816, 1.400, 1.000), center=(-3.200, -14.870, 1.830)
* 几何统计: Mesh=1, Vertices=414, Faces=824
* 子Mesh材质: /World/PartA_OnBelt_2/node__Size_1_0x1_4x4_SUPPRESSION_Default/geometry_1 -> 未绑定

---

### '/World/PartA_OnBelt_3' (Xform)

* 引用: reference:/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ban_Yuan_Jian/Woodruff keys GB_converted/0;Size=1.0x1.4x4;SUPPRESSION=Default.usd
* BBox (world): size=(3.816, 1.400, 1.000), center=(-5.000, -14.870, 1.830)
* 几何统计: Mesh=1, Vertices=414, Faces=824
* 子Mesh材质: /World/PartA_OnBelt_3/node__Size_1_0x1_4x4_SUPPRESSION_Default/geometry_1 -> 未绑定

---

### '/World/PartA_OnBelt_4' (Xform)

* 引用: reference:/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ban_Yuan_Jian/Woodruff keys GB_converted/0;Size=1.0x1.4x4;SUPPRESSION=Default.usd
* BBox (world): size=(3.816, 1.400, 1.000), center=(-6.800, -14.870, 1.830)
* 几何统计: Mesh=1, Vertices=414, Faces=824
* 子Mesh材质: /World/PartA_OnBelt_4/node__Size_1_0x1_4x4_SUPPRESSION_Default/geometry_1 -> 未绑定

---

### '/World/PartA_OnBelt_5' (Xform)

* 引用: reference:/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ban_Yuan_Jian/Woodruff keys GB_converted/0;Size=1.0x1.4x4;SUPPRESSION=Default.usd
* BBox (world): size=(3.816, 1.400, 1.000), center=(-8.600, -14.870, 1.830)
* 几何统计: Mesh=1, Vertices=414, Faces=824
* 子Mesh材质: /World/PartA_OnBelt_5/node__Size_1_0x1_4x4_SUPPRESSION_Default/geometry_1 -> 未绑定

---

### '/World/PartA_OnBelt_6' (Xform)

* 引用: reference:/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ban_Yuan_Jian/Woodruff keys GB_converted/0;Size=1.0x1.4x4;SUPPRESSION=Default.usd
* BBox (world): size=(3.816, 1.400, 1.000), center=(-10.400, -14.870, 1.830)
* 几何统计: Mesh=1, Vertices=414, Faces=824
* 子Mesh材质: /World/PartA_OnBelt_6/node__Size_1_0x1_4x4_SUPPRESSION_Default/geometry_1 -> 未绑定

---

### '/World/PartA_OnBelt_7' (Xform)

* 引用: reference:/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ban_Yuan_Jian/Woodruff keys GB_converted/0;Size=1.0x1.4x4;SUPPRESSION=Default.usd
* BBox (world): size=(3.816, 1.400, 1.000), center=(-12.200, -14.870, 1.830)
* 几何统计: Mesh=1, Vertices=414, Faces=824
* 子Mesh材质: /World/PartA_OnBelt_7/node__Size_1_0x1_4x4_SUPPRESSION_Default/geometry_1 -> 未绑定

---

### '/World/PartA_OnBelt_8' (Xform)

* 引用: reference:/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ban_Yuan_Jian/Woodruff keys GB_converted/0;Size=1.0x1.4x4;SUPPRESSION=Default.usd
* BBox (world): size=(3.816, 1.400, 1.000), center=(-14.000, -14.870, 1.830)
* 几何统计: Mesh=1, Vertices=414, Faces=824
* 子Mesh材质: /World/PartA_OnBelt_8/node__Size_1_0x1_4x4_SUPPRESSION_Default/geometry_1 -> 未绑定

---

### '/World/PartA_OnBelt_9' (Xform)

* 引用: reference:/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ban_Yuan_Jian/Woodruff keys GB_converted/0;Size=1.0x1.4x4;SUPPRESSION=Default.usd
* BBox (world): size=(3.816, 1.400, 1.000), center=(-15.800, -14.870, 1.830)
* 几何统计: Mesh=1, Vertices=414, Faces=824
* 子Mesh材质: /World/PartA_OnBelt_9/node__Size_1_0x1_4x4_SUPPRESSION_Default/geometry_1 -> 未绑定

---

### '/World/PartA_OnBelt_10' (Xform)

* 引用: reference:/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ban_Yuan_Jian/Woodruff keys GB_converted/0;Size=1.0x1.4x4;SUPPRESSION=Default.usd
* BBox (world): size=(3.816, 1.400, 1.000), center=(-1.400, -9.870, 1.830)
* 几何统计: Mesh=1, Vertices=414, Faces=824
* 子Mesh材质: /World/PartA_OnBelt_10/node__Size_1_0x1_4x4_SUPPRESSION_Default/geometry_1 -> 未绑定

---

### '/World/PartA_OnBelt_11' (Xform)

* 引用: reference:/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ban_Yuan_Jian/Woodruff keys GB_converted/0;Size=1.0x1.4x4;SUPPRESSION=Default.usd
* BBox (world): size=(3.816, 1.400, 1.000), center=(-3.200, -9.870, 1.830)
* 几何统计: Mesh=1, Vertices=414, Faces=824
* 子Mesh材质: /World/PartA_OnBelt_11/node__Size_1_0x1_4x4_SUPPRESSION_Default/geometry_1 -> 未绑定

---

### '/World/PartA_OnBelt_12' (Xform)

* 引用: reference:/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ban_Yuan_Jian/Woodruff keys GB_converted/0;Size=1.0x1.4x4;SUPPRESSION=Default.usd
* BBox (world): size=(3.816, 1.400, 1.000), center=(-5.000, -9.870, 1.830)
* 几何统计: Mesh=1, Vertices=414, Faces=824
* 子Mesh材质: /World/PartA_OnBelt_12/node__Size_1_0x1_4x4_SUPPRESSION_Default/geometry_1 -> 未绑定

---

### '/World/PartA_OnBelt_13' (Xform)

* 引用: reference:/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ban_Yuan_Jian/Woodruff keys GB_converted/0;Size=1.0x1.4x4;SUPPRESSION=Default.usd
* BBox (world): size=(3.816, 1.400, 1.000), center=(-6.800, -9.870, 1.830)
* 几何统计: Mesh=1, Vertices=414, Faces=824
* 子Mesh材质: /World/PartA_OnBelt_13/node__Size_1_0x1_4x4_SUPPRESSION_Default/geometry_1 -> 未绑定

---

### '/World/PartA_OnBelt_14' (Xform)

* 引用: reference:/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ban_Yuan_Jian/Woodruff keys GB_converted/0;Size=1.0x1.4x4;SUPPRESSION=Default.usd
* BBox (world): size=(3.816, 1.400, 1.000), center=(-8.600, -9.870, 1.830)
* 几何统计: Mesh=1, Vertices=414, Faces=824
* 子Mesh材质: /World/PartA_OnBelt_14/node__Size_1_0x1_4x4_SUPPRESSION_Default/geometry_1 -> 未绑定

---

### '/World/PartA_OnBelt_15' (Xform)

* 引用: reference:/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ban_Yuan_Jian/Woodruff keys GB_converted/0;Size=1.0x1.4x4;SUPPRESSION=Default.usd
* BBox (world): size=(3.816, 1.400, 1.000), center=(-10.400, -9.870, 1.830)
* 几何统计: Mesh=1, Vertices=414, Faces=824
* 子Mesh材质: /World/PartA_OnBelt_15/node__Size_1_0x1_4x4_SUPPRESSION_Default/geometry_1 -> 未绑定

---

### '/World/PartA_OnBelt_16' (Xform)

* 引用: reference:/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ban_Yuan_Jian/Woodruff keys GB_converted/0;Size=1.0x1.4x4;SUPPRESSION=Default.usd
* BBox (world): size=(3.816, 1.400, 1.000), center=(-12.200, -9.870, 1.830)
* 几何统计: Mesh=1, Vertices=414, Faces=824
* 子Mesh材质: /World/PartA_OnBelt_16/node__Size_1_0x1_4x4_SUPPRESSION_Default/geometry_1 -> 未绑定

---

### '/World/PartA_OnBelt_17' (Xform)

* 引用: reference:/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ban_Yuan_Jian/Woodruff keys GB_converted/0;Size=1.0x1.4x4;SUPPRESSION=Default.usd
* BBox (world): size=(3.816, 1.400, 1.000), center=(-14.000, -9.870, 1.830)
* 几何统计: Mesh=1, Vertices=414, Faces=824
* 子Mesh材质: /World/PartA_OnBelt_17/node__Size_1_0x1_4x4_SUPPRESSION_Default/geometry_1 -> 未绑定

---

### '/World/PartA_OnBelt_18' (Xform)

* 引用: reference:/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ban_Yuan_Jian/Woodruff keys GB_converted/0;Size=1.0x1.4x4;SUPPRESSION=Default.usd
* BBox (world): size=(3.816, 1.400, 1.000), center=(-15.800, -9.870, 1.830)
* 几何统计: Mesh=1, Vertices=414, Faces=824
* 子Mesh材质: /World/PartA_OnBelt_18/node__Size_1_0x1_4x4_SUPPRESSION_Default/geometry_1 -> 未绑定

---

### '/World/PartA_OnBelt_19' (Xform)

* 引用: reference:/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ban_Yuan_Jian/Woodruff keys GB_converted/0;Size=1.0x1.4x4;SUPPRESSION=Default.usd
* BBox (world): size=(3.816, 1.400, 1.000), center=(-1.400, -4.870, 1.830)
* 几何统计: Mesh=1, Vertices=414, Faces=824
* 子Mesh材质: /World/PartA_OnBelt_19/node__Size_1_0x1_4x4_SUPPRESSION_Default/geometry_1 -> 未绑定

---

### '/World/PartA_OnBelt_20' (Xform)

* 引用: reference:/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ban_Yuan_Jian/Woodruff keys GB_converted/0;Size=1.0x1.4x4;SUPPRESSION=Default.usd
* BBox (world): size=(3.816, 1.400, 1.000), center=(-3.200, -4.870, 1.830)
* 几何统计: Mesh=1, Vertices=414, Faces=824
* 子Mesh材质: /World/PartA_OnBelt_20/node__Size_1_0x1_4x4_SUPPRESSION_Default/geometry_1 -> 未绑定

---

### '/World/PartA_OnBelt_21' (Xform)

* 引用: reference:/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ban_Yuan_Jian/Woodruff keys GB_converted/0;Size=1.0x1.4x4;SUPPRESSION=Default.usd
* BBox (world): size=(3.816, 1.400, 1.000), center=(-5.000, -4.870, 1.830)
* 几何统计: Mesh=1, Vertices=414, Faces=824
* 子Mesh材质: /World/PartA_OnBelt_21/node__Size_1_0x1_4x4_SUPPRESSION_Default/geometry_1 -> 未绑定

---

### '/World/PartA_OnBelt_22' (Xform)

* 引用: reference:/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ban_Yuan_Jian/Woodruff keys GB_converted/0;Size=1.0x1.4x4;SUPPRESSION=Default.usd
* BBox (world): size=(3.816, 1.400, 1.000), center=(-6.800, -4.870, 1.830)
* 几何统计: Mesh=1, Vertices=414, Faces=824
* 子Mesh材质: /World/PartA_OnBelt_22/node__Size_1_0x1_4x4_SUPPRESSION_Default/geometry_1 -> 未绑定

---

### '/World/PartA_OnBelt_23' (Xform)

* 引用: reference:/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ban_Yuan_Jian/Woodruff keys GB_converted/0;Size=1.0x1.4x4;SUPPRESSION=Default.usd
* BBox (world): size=(3.816, 1.400, 1.000), center=(-8.600, -4.870, 1.830)
* 几何统计: Mesh=1, Vertices=414, Faces=824
* 子Mesh材质: /World/PartA_OnBelt_23/node__Size_1_0x1_4x4_SUPPRESSION_Default/geometry_1 -> 未绑定

---

### '/World/PartA_OnBelt_24' (Xform)

* 引用: reference:/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ban_Yuan_Jian/Woodruff keys GB_converted/0;Size=1.0x1.4x4;SUPPRESSION=Default.usd
* BBox (world): size=(3.816, 1.400, 1.000), center=(-10.400, -4.870, 1.830)
* 几何统计: Mesh=1, Vertices=414, Faces=824
* 子Mesh材质: /World/PartA_OnBelt_24/node__Size_1_0x1_4x4_SUPPRESSION_Default/geometry_1 -> 未绑定

---

### '/World/PartA_OnBelt_25' (Xform)

* 引用: reference:/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ban_Yuan_Jian/Woodruff keys GB_converted/0;Size=1.0x1.4x4;SUPPRESSION=Default.usd
* BBox (world): size=(3.816, 1.400, 1.000), center=(-12.200, -4.870, 1.830)
* 几何统计: Mesh=1, Vertices=414, Faces=824
* 子Mesh材质: /World/PartA_OnBelt_25/node__Size_1_0x1_4x4_SUPPRESSION_Default/geometry_1 -> 未绑定

---

### '/World/PartA_OnBelt_26' (Xform)

* 引用: reference:/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ban_Yuan_Jian/Woodruff keys GB_converted/0;Size=1.0x1.4x4;SUPPRESSION=Default.usd
* BBox (world): size=(3.816, 1.400, 1.000), center=(-14.000, -4.870, 1.830)
* 几何统计: Mesh=1, Vertices=414, Faces=824
* 子Mesh材质: /World/PartA_OnBelt_26/node__Size_1_0x1_4x4_SUPPRESSION_Default/geometry_1 -> 未绑定

---

### '/World/PartA_OnBelt_27' (Xform)

* 引用: reference:/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ban_Yuan_Jian/Woodruff keys GB_converted/0;Size=1.0x1.4x4;SUPPRESSION=Default.usd
* BBox (world): size=(3.816, 1.400, 1.000), center=(-15.800, -4.870, 1.830)
* 几何统计: Mesh=1, Vertices=414, Faces=824
* 子Mesh材质: /World/PartA_OnBelt_27/node__Size_1_0x1_4x4_SUPPRESSION_Default/geometry_1 -> 未绑定

---

### '/World/PartA_OnBelt_28' (Xform)

* 引用: reference:/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ban_Yuan_Jian/Woodruff keys GB_converted/0;Size=1.0x1.4x4;SUPPRESSION=Default.usd
* BBox (world): size=(3.816, 1.400, 1.000), center=(-1.400, 0.130, 1.830)
* 几何统计: Mesh=1, Vertices=414, Faces=824
* 子Mesh材质: /World/PartA_OnBelt_28/node__Size_1_0x1_4x4_SUPPRESSION_Default/geometry_1 -> 未绑定

---

### '/World/PartA_OnBelt_29' (Xform)

* 引用: reference:/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ban_Yuan_Jian/Woodruff keys GB_converted/0;Size=1.0x1.4x4;SUPPRESSION=Default.usd
* BBox (world): size=(3.816, 1.400, 1.000), center=(-3.200, 0.130, 1.830)
* 几何统计: Mesh=1, Vertices=414, Faces=824
* 子Mesh材质: /World/PartA_OnBelt_29/node__Size_1_0x1_4x4_SUPPRESSION_Default/geometry_1 -> 未绑定

---

### '/World/PartA_OnBelt_30' (Xform)

* 引用: reference:/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ban_Yuan_Jian/Woodruff keys GB_converted/0;Size=1.0x1.4x4;SUPPRESSION=Default.usd
* BBox (world): size=(3.816, 1.400, 1.000), center=(-5.000, 0.130, 1.830)
* 几何统计: Mesh=1, Vertices=414, Faces=824
* 子Mesh材质: /World/PartA_OnBelt_30/node__Size_1_0x1_4x4_SUPPRESSION_Default/geometry_1 -> 未绑定

---

### '/World/PartA_OnBelt_31' (Xform)

* 引用: reference:/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ban_Yuan_Jian/Woodruff keys GB_converted/0;Size=1.0x1.4x4;SUPPRESSION=Default.usd
* BBox (world): size=(3.816, 1.400, 1.000), center=(-6.800, 0.130, 1.830)
* 几何统计: Mesh=1, Vertices=414, Faces=824
* 子Mesh材质: /World/PartA_OnBelt_31/node__Size_1_0x1_4x4_SUPPRESSION_Default/geometry_1 -> 未绑定

---

### '/World/PartA_OnBelt_32' (Xform)

* 引用: reference:/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ban_Yuan_Jian/Woodruff keys GB_converted/0;Size=1.0x1.4x4;SUPPRESSION=Default.usd
* BBox (world): size=(3.816, 1.400, 1.000), center=(-8.600, 0.130, 1.830)
* 几何统计: Mesh=1, Vertices=414, Faces=824
* 子Mesh材质: /World/PartA_OnBelt_32/node__Size_1_0x1_4x4_SUPPRESSION_Default/geometry_1 -> 未绑定

---

### '/World/PartA_OnBelt_33' (Xform)

* 引用: reference:/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ban_Yuan_Jian/Woodruff keys GB_converted/0;Size=1.0x1.4x4;SUPPRESSION=Default.usd
* BBox (world): size=(3.816, 1.400, 1.000), center=(-10.400, 0.130, 1.830)
* 几何统计: Mesh=1, Vertices=414, Faces=824
* 子Mesh材质: /World/PartA_OnBelt_33/node__Size_1_0x1_4x4_SUPPRESSION_Default/geometry_1 -> 未绑定

---

### '/World/PartA_OnBelt_34' (Xform)

* 引用: reference:/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ban_Yuan_Jian/Woodruff keys GB_converted/0;Size=1.0x1.4x4;SUPPRESSION=Default.usd
* BBox (world): size=(3.816, 1.400, 1.000), center=(-12.200, 0.130, 1.830)
* 几何统计: Mesh=1, Vertices=414, Faces=824
* 子Mesh材质: /World/PartA_OnBelt_34/node__Size_1_0x1_4x4_SUPPRESSION_Default/geometry_1 -> 未绑定

---

### '/World/PartA_OnBelt_35' (Xform)

* 引用: reference:/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ban_Yuan_Jian/Woodruff keys GB_converted/0;Size=1.0x1.4x4;SUPPRESSION=Default.usd
* BBox (world): size=(3.816, 1.400, 1.000), center=(-14.000, 0.130, 1.830)
* 几何统计: Mesh=1, Vertices=414, Faces=824
* 子Mesh材质: /World/PartA_OnBelt_35/node__Size_1_0x1_4x4_SUPPRESSION_Default/geometry_1 -> 未绑定

---

### '/World/PartA_OnBelt_36' (Xform)

* 引用: reference:/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ban_Yuan_Jian/Woodruff keys GB_converted/0;Size=1.0x1.4x4;SUPPRESSION=Default.usd
* BBox (world): size=(3.816, 1.400, 1.000), center=(-15.800, 0.130, 1.830)
* 几何统计: Mesh=1, Vertices=414, Faces=824
* 子Mesh材质: /World/PartA_OnBelt_36/node__Size_1_0x1_4x4_SUPPRESSION_Default/geometry_1 -> 未绑定

---

### '/World/PartA_OnBelt_37' (Xform)

* 引用: reference:/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ban_Yuan_Jian/Woodruff keys GB_converted/0;Size=1.0x1.4x4;SUPPRESSION=Default.usd
* BBox (world): size=(3.816, 1.400, 1.000), center=(-1.400, 5.130, 1.830)
* 几何统计: Mesh=1, Vertices=414, Faces=824
* 子Mesh材质: /World/PartA_OnBelt_37/node__Size_1_0x1_4x4_SUPPRESSION_Default/geometry_1 -> 未绑定

---

### '/World/PartA_OnBelt_38' (Xform)

* 引用: reference:/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ban_Yuan_Jian/Woodruff keys GB_converted/0;Size=1.0x1.4x4;SUPPRESSION=Default.usd
* BBox (world): size=(3.816, 1.400, 1.000), center=(-3.200, 5.130, 1.830)
* 几何统计: Mesh=1, Vertices=414, Faces=824
* 子Mesh材质: /World/PartA_OnBelt_38/node__Size_1_0x1_4x4_SUPPRESSION_Default/geometry_1 -> 未绑定

---

### '/World/PartA_OnBelt_39' (Xform)

* 引用: reference:/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ban_Yuan_Jian/Woodruff keys GB_converted/0;Size=1.0x1.4x4;SUPPRESSION=Default.usd
* BBox (world): size=(3.816, 1.400, 1.000), center=(-5.000, 5.130, 1.830)
* 几何统计: Mesh=1, Vertices=414, Faces=824
* 子Mesh材质: /World/PartA_OnBelt_39/node__Size_1_0x1_4x4_SUPPRESSION_Default/geometry_1 -> 未绑定

---

### '/World/PartA_OnBelt_40' (Xform)

* 引用: reference:/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ban_Yuan_Jian/Woodruff keys GB_converted/0;Size=1.0x1.4x4;SUPPRESSION=Default.usd
* BBox (world): size=(3.816, 1.400, 1.000), center=(-6.800, 5.130, 1.830)
* 几何统计: Mesh=1, Vertices=414, Faces=824
* 子Mesh材质: /World/PartA_OnBelt_40/node__Size_1_0x1_4x4_SUPPRESSION_Default/geometry_1 -> 未绑定

---

### '/World/PartA_OnBelt_41' (Xform)

* 引用: reference:/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ban_Yuan_Jian/Woodruff keys GB_converted/0;Size=1.0x1.4x4;SUPPRESSION=Default.usd
* BBox (world): size=(3.816, 1.400, 1.000), center=(-8.600, 5.130, 1.830)
* 几何统计: Mesh=1, Vertices=414, Faces=824
* 子Mesh材质: /World/PartA_OnBelt_41/node__Size_1_0x1_4x4_SUPPRESSION_Default/geometry_1 -> 未绑定

---

### '/World/PartA_OnBelt_42' (Xform)

* 引用: reference:/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ban_Yuan_Jian/Woodruff keys GB_converted/0;Size=1.0x1.4x4;SUPPRESSION=Default.usd
* BBox (world): size=(3.816, 1.400, 1.000), center=(-10.400, 5.130, 1.830)
* 几何统计: Mesh=1, Vertices=414, Faces=824
* 子Mesh材质: /World/PartA_OnBelt_42/node__Size_1_0x1_4x4_SUPPRESSION_Default/geometry_1 -> 未绑定

---

### '/World/PartA_OnBelt_43' (Xform)

* 引用: reference:/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ban_Yuan_Jian/Woodruff keys GB_converted/0;Size=1.0x1.4x4;SUPPRESSION=Default.usd
* BBox (world): size=(3.816, 1.400, 1.000), center=(-12.200, 5.130, 1.830)
* 几何统计: Mesh=1, Vertices=414, Faces=824
* 子Mesh材质: /World/PartA_OnBelt_43/node__Size_1_0x1_4x4_SUPPRESSION_Default/geometry_1 -> 未绑定

---

### '/World/PartA_OnBelt_44' (Xform)

* 引用: reference:/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ban_Yuan_Jian/Woodruff keys GB_converted/0;Size=1.0x1.4x4;SUPPRESSION=Default.usd
* BBox (world): size=(3.816, 1.400, 1.000), center=(-14.000, 5.130, 1.830)
* 几何统计: Mesh=1, Vertices=414, Faces=824
* 子Mesh材质: /World/PartA_OnBelt_44/node__Size_1_0x1_4x4_SUPPRESSION_Default/geometry_1 -> 未绑定

---

### '/World/PartA_OnBelt_45' (Xform)

* 引用: reference:/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ban_Yuan_Jian/Woodruff keys GB_converted/0;Size=1.0x1.4x4;SUPPRESSION=Default.usd
* BBox (world): size=(3.816, 1.400, 1.000), center=(-15.800, 5.130, 1.830)
* 几何统计: Mesh=1, Vertices=414, Faces=824
* 子Mesh材质: /World/PartA_OnBelt_45/node__Size_1_0x1_4x4_SUPPRESSION_Default/geometry_1 -> 未绑定

---

### '/World/PartA_OnBelt_46' (Xform)

* 引用: reference:/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ban_Yuan_Jian/Woodruff keys GB_converted/0;Size=1.0x1.4x4;SUPPRESSION=Default.usd
* BBox (world): size=(3.816, 1.400, 1.000), center=(-1.400, 10.130, 1.830)
* 几何统计: Mesh=1, Vertices=414, Faces=824
* 子Mesh材质: /World/PartA_OnBelt_46/node__Size_1_0x1_4x4_SUPPRESSION_Default/geometry_1 -> 未绑定

---

### '/World/PartA_OnBelt_47' (Xform)

* 引用: reference:/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ban_Yuan_Jian/Woodruff keys GB_converted/0;Size=1.0x1.4x4;SUPPRESSION=Default.usd
* BBox (world): size=(3.816, 1.400, 1.000), center=(-3.200, 10.130, 1.830)
* 几何统计: Mesh=1, Vertices=414, Faces=824
* 子Mesh材质: /World/PartA_OnBelt_47/node__Size_1_0x1_4x4_SUPPRESSION_Default/geometry_1 -> 未绑定

---

### '/World/PartA_OnBelt_48' (Xform)

* 引用: reference:/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ban_Yuan_Jian/Woodruff keys GB_converted/0;Size=1.0x1.4x4;SUPPRESSION=Default.usd
* BBox (world): size=(3.816, 1.400, 1.000), center=(-5.000, 10.130, 1.830)
* 几何统计: Mesh=1, Vertices=414, Faces=824
* 子Mesh材质: /World/PartA_OnBelt_48/node__Size_1_0x1_4x4_SUPPRESSION_Default/geometry_1 -> 未绑定

---

### '/World/PartA_OnBelt_49' (Xform)

* 引用: reference:/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ban_Yuan_Jian/Woodruff keys GB_converted/0;Size=1.0x1.4x4;SUPPRESSION=Default.usd
* BBox (world): size=(3.816, 1.400, 1.000), center=(-6.800, 10.130, 1.830)
* 几何统计: Mesh=1, Vertices=414, Faces=824
* 子Mesh材质: /World/PartA_OnBelt_49/node__Size_1_0x1_4x4_SUPPRESSION_Default/geometry_1 -> 未绑定

---

### '/World/PartA_OnBelt_50' (Xform)

* 引用: reference:/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ban_Yuan_Jian/Woodruff keys GB_converted/0;Size=1.0x1.4x4;SUPPRESSION=Default.usd
* BBox (world): size=(3.816, 1.400, 1.000), center=(-8.600, 10.130, 1.830)
* 几何统计: Mesh=1, Vertices=414, Faces=824
* 子Mesh材质: /World/PartA_OnBelt_50/node__Size_1_0x1_4x4_SUPPRESSION_Default/geometry_1 -> 未绑定

---

### '/World/PartA_OnBelt_51' (Xform)

* 引用: reference:/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ban_Yuan_Jian/Woodruff keys GB_converted/0;Size=1.0x1.4x4;SUPPRESSION=Default.usd
* BBox (world): size=(3.816, 1.400, 1.000), center=(-10.400, 10.130, 1.830)
* 几何统计: Mesh=1, Vertices=414, Faces=824
* 子Mesh材质: /World/PartA_OnBelt_51/node__Size_1_0x1_4x4_SUPPRESSION_Default/geometry_1 -> 未绑定

---

### '/World/PartA_OnBelt_52' (Xform)

* 引用: reference:/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ban_Yuan_Jian/Woodruff keys GB_converted/0;Size=1.0x1.4x4;SUPPRESSION=Default.usd
* BBox (world): size=(3.816, 1.400, 1.000), center=(-12.200, 10.130, 1.830)
* 几何统计: Mesh=1, Vertices=414, Faces=824
* 子Mesh材质: /World/PartA_OnBelt_52/node__Size_1_0x1_4x4_SUPPRESSION_Default/geometry_1 -> 未绑定

---

### '/World/PartA_OnBelt_53' (Xform)

* 引用: reference:/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ban_Yuan_Jian/Woodruff keys GB_converted/0;Size=1.0x1.4x4;SUPPRESSION=Default.usd
* BBox (world): size=(3.816, 1.400, 1.000), center=(-14.000, 10.130, 1.830)
* 几何统计: Mesh=1, Vertices=414, Faces=824
* 子Mesh材质: /World/PartA_OnBelt_53/node__Size_1_0x1_4x4_SUPPRESSION_Default/geometry_1 -> 未绑定

---

### '/World/PartA_OnBelt_54' (Xform)

* 引用: reference:/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ban_Yuan_Jian/Woodruff keys GB_converted/0;Size=1.0x1.4x4;SUPPRESSION=Default.usd
* BBox (world): size=(3.816, 1.400, 1.000), center=(-15.800, 10.130, 1.830)
* 几何统计: Mesh=1, Vertices=414, Faces=824
* 子Mesh材质: /World/PartA_OnBelt_54/node__Size_1_0x1_4x4_SUPPRESSION_Default/geometry_1 -> 未绑定

---

### '/World/PartA_OnBelt_55' (Xform)

* 引用: reference:/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ban_Yuan_Jian/Woodruff keys GB_converted/0;Size=1.0x1.4x4;SUPPRESSION=Default.usd
* BBox (world): size=(3.816, 1.400, 1.000), center=(-1.400, 15.130, 1.830)
* 几何统计: Mesh=1, Vertices=414, Faces=824
* 子Mesh材质: /World/PartA_OnBelt_55/node__Size_1_0x1_4x4_SUPPRESSION_Default/geometry_1 -> 未绑定

---

### '/World/PartA_OnBelt_56' (Xform)

* 引用: reference:/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ban_Yuan_Jian/Woodruff keys GB_converted/0;Size=1.0x1.4x4;SUPPRESSION=Default.usd
* BBox (world): size=(3.816, 1.400, 1.000), center=(-3.200, 15.130, 1.830)
* 几何统计: Mesh=1, Vertices=414, Faces=824
* 子Mesh材质: /World/PartA_OnBelt_56/node__Size_1_0x1_4x4_SUPPRESSION_Default/geometry_1 -> 未绑定

---

### '/World/PartA_OnBelt_57' (Xform)

* 引用: reference:/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ban_Yuan_Jian/Woodruff keys GB_converted/0;Size=1.0x1.4x4;SUPPRESSION=Default.usd
* BBox (world): size=(3.816, 1.400, 1.000), center=(-5.000, 15.130, 1.830)
* 几何统计: Mesh=1, Vertices=414, Faces=824
* 子Mesh材质: /World/PartA_OnBelt_57/node__Size_1_0x1_4x4_SUPPRESSION_Default/geometry_1 -> 未绑定

---

### '/World/PartA_OnBelt_58' (Xform)

* 引用: reference:/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ban_Yuan_Jian/Woodruff keys GB_converted/0;Size=1.0x1.4x4;SUPPRESSION=Default.usd
* BBox (world): size=(3.816, 1.400, 1.000), center=(-6.800, 15.130, 1.830)
* 几何统计: Mesh=1, Vertices=414, Faces=824
* 子Mesh材质: /World/PartA_OnBelt_58/node__Size_1_0x1_4x4_SUPPRESSION_Default/geometry_1 -> 未绑定

---

### '/World/PartA_OnBelt_59' (Xform)

* 引用: reference:/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ban_Yuan_Jian/Woodruff keys GB_converted/0;Size=1.0x1.4x4;SUPPRESSION=Default.usd
* BBox (world): size=(3.816, 1.400, 1.000), center=(-8.600, 15.130, 1.830)
* 几何统计: Mesh=1, Vertices=414, Faces=824
* 子Mesh材质: /World/PartA_OnBelt_59/node__Size_1_0x1_4x4_SUPPRESSION_Default/geometry_1 -> 未绑定

---

### '/World/PartA_OnBelt_60' (Xform)

* 引用: reference:/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ban_Yuan_Jian/Woodruff keys GB_converted/0;Size=1.0x1.4x4;SUPPRESSION=Default.usd
* BBox (world): size=(3.816, 1.400, 1.000), center=(-10.400, 15.130, 1.830)
* 几何统计: Mesh=1, Vertices=414, Faces=824
* 子Mesh材质: /World/PartA_OnBelt_60/node__Size_1_0x1_4x4_SUPPRESSION_Default/geometry_1 -> 未绑定

---

### '/World/PartA_OnBelt_61' (Xform)

* 引用: reference:/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ban_Yuan_Jian/Woodruff keys GB_converted/0;Size=1.0x1.4x4;SUPPRESSION=Default.usd
* BBox (world): size=(3.816, 1.400, 1.000), center=(-12.200, 15.130, 1.830)
* 几何统计: Mesh=1, Vertices=414, Faces=824
* 子Mesh材质: /World/PartA_OnBelt_61/node__Size_1_0x1_4x4_SUPPRESSION_Default/geometry_1 -> 未绑定

---

### '/World/PartA_OnBelt_62' (Xform)

* 引用: reference:/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ban_Yuan_Jian/Woodruff keys GB_converted/0;Size=1.0x1.4x4;SUPPRESSION=Default.usd
* BBox (world): size=(3.816, 1.400, 1.000), center=(-14.000, 15.130, 1.830)
* 几何统计: Mesh=1, Vertices=414, Faces=824
* 子Mesh材质: /World/PartA_OnBelt_62/node__Size_1_0x1_4x4_SUPPRESSION_Default/geometry_1 -> 未绑定

---

### '/World/PartA_OnBelt_63' (Xform)

* 引用: reference:/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ban_Yuan_Jian/Woodruff keys GB_converted/0;Size=1.0x1.4x4;SUPPRESSION=Default.usd
* BBox (world): size=(3.816, 1.400, 1.000), center=(-15.800, 15.130, 1.830)
* 几何统计: Mesh=1, Vertices=414, Faces=824
* 子Mesh材质: /World/PartA_OnBelt_63/node__Size_1_0x1_4x4_SUPPRESSION_Default/geometry_1 -> 未绑定

---

### '/World/PartB_OnBelt_1' (Xform)

* 引用: reference:/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ping_Jian/Feather keys GB_converted/6;Size=8;Length=28;SUPPRESSION=A,Simplified.usd
* BBox (world): size=(28.000, 8.000, 7.000), center=(-2.400, -15.000, 1.830)
* 几何统计: Mesh=1, Vertices=2310, Faces=4628
* 子Mesh材质: /World/PartB_OnBelt_1/node__Size_8_Length_28_SUPPRESSION_A_Simplified/geometry_1 -> 未绑定

---

### '/World/PartB_OnBelt_2' (Xform)

* 引用: reference:/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ping_Jian/Feather keys GB_converted/6;Size=8;Length=28;SUPPRESSION=A,Simplified.usd
* BBox (world): size=(28.000, 8.000, 7.000), center=(-4.200, -15.000, 1.830)
* 几何统计: Mesh=1, Vertices=2310, Faces=4628
* 子Mesh材质: /World/PartB_OnBelt_2/node__Size_8_Length_28_SUPPRESSION_A_Simplified/geometry_1 -> 未绑定

---

### '/World/PartB_OnBelt_3' (Xform)

* 引用: reference:/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ping_Jian/Feather keys GB_converted/6;Size=8;Length=28;SUPPRESSION=A,Simplified.usd
* BBox (world): size=(28.000, 8.000, 7.000), center=(-6.000, -15.000, 1.830)
* 几何统计: Mesh=1, Vertices=2310, Faces=4628
* 子Mesh材质: /World/PartB_OnBelt_3/node__Size_8_Length_28_SUPPRESSION_A_Simplified/geometry_1 -> 未绑定

---

### '/World/PartB_OnBelt_4' (Xform)

* 引用: reference:/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ping_Jian/Feather keys GB_converted/6;Size=8;Length=28;SUPPRESSION=A,Simplified.usd
* BBox (world): size=(28.000, 8.000, 7.000), center=(-7.800, -15.000, 1.830)
* 几何统计: Mesh=1, Vertices=2310, Faces=4628
* 子Mesh材质: /World/PartB_OnBelt_4/node__Size_8_Length_28_SUPPRESSION_A_Simplified/geometry_1 -> 未绑定

---

### '/World/PartB_OnBelt_5' (Xform)

* 引用: reference:/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ping_Jian/Feather keys GB_converted/6;Size=8;Length=28;SUPPRESSION=A,Simplified.usd
* BBox (world): size=(28.000, 8.000, 7.000), center=(-9.600, -15.000, 1.830)
* 几何统计: Mesh=1, Vertices=2310, Faces=4628
* 子Mesh材质: /World/PartB_OnBelt_5/node__Size_8_Length_28_SUPPRESSION_A_Simplified/geometry_1 -> 未绑定

---

### '/World/PartB_OnBelt_6' (Xform)

* 引用: reference:/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ping_Jian/Feather keys GB_converted/6;Size=8;Length=28;SUPPRESSION=A,Simplified.usd
* BBox (world): size=(28.000, 8.000, 7.000), center=(-11.400, -15.000, 1.830)
* 几何统计: Mesh=1, Vertices=2310, Faces=4628
* 子Mesh材质: /World/PartB_OnBelt_6/node__Size_8_Length_28_SUPPRESSION_A_Simplified/geometry_1 -> 未绑定

---

### '/World/PartB_OnBelt_7' (Xform)

* 引用: reference:/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ping_Jian/Feather keys GB_converted/6;Size=8;Length=28;SUPPRESSION=A,Simplified.usd
* BBox (world): size=(28.000, 8.000, 7.000), center=(-13.200, -15.000, 1.830)
* 几何统计: Mesh=1, Vertices=2310, Faces=4628
* 子Mesh材质: /World/PartB_OnBelt_7/node__Size_8_Length_28_SUPPRESSION_A_Simplified/geometry_1 -> 未绑定

---

### '/World/PartB_OnBelt_8' (Xform)

* 引用: reference:/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ping_Jian/Feather keys GB_converted/6;Size=8;Length=28;SUPPRESSION=A,Simplified.usd
* BBox (world): size=(28.000, 8.000, 7.000), center=(-15.000, -15.000, 1.830)
* 几何统计: Mesh=1, Vertices=2310, Faces=4628
* 子Mesh材质: /World/PartB_OnBelt_8/node__Size_8_Length_28_SUPPRESSION_A_Simplified/geometry_1 -> 未绑定

---

### '/World/PartB_OnBelt_9' (Xform)

* 引用: reference:/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ping_Jian/Feather keys GB_converted/6;Size=8;Length=28;SUPPRESSION=A,Simplified.usd
* BBox (world): size=(28.000, 8.000, 7.000), center=(-16.800, -15.000, 1.830)
* 几何统计: Mesh=1, Vertices=2310, Faces=4628
* 子Mesh材质: /World/PartB_OnBelt_9/node__Size_8_Length_28_SUPPRESSION_A_Simplified/geometry_1 -> 未绑定

---

### '/World/PartB_OnBelt_10' (Xform)

* 引用: reference:/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ping_Jian/Feather keys GB_converted/6;Size=8;Length=28;SUPPRESSION=A,Simplified.usd
* BBox (world): size=(28.000, 8.000, 7.000), center=(-2.400, -10.000, 1.830)
* 几何统计: Mesh=1, Vertices=2310, Faces=4628
* 子Mesh材质: /World/PartB_OnBelt_10/node__Size_8_Length_28_SUPPRESSION_A_Simplified/geometry_1 -> 未绑定

---

### '/World/PartB_OnBelt_11' (Xform)

* 引用: reference:/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ping_Jian/Feather keys GB_converted/6;Size=8;Length=28;SUPPRESSION=A,Simplified.usd
* BBox (world): size=(28.000, 8.000, 7.000), center=(-4.200, -10.000, 1.830)
* 几何统计: Mesh=1, Vertices=2310, Faces=4628
* 子Mesh材质: /World/PartB_OnBelt_11/node__Size_8_Length_28_SUPPRESSION_A_Simplified/geometry_1 -> 未绑定

---

### '/World/PartB_OnBelt_12' (Xform)

* 引用: reference:/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ping_Jian/Feather keys GB_converted/6;Size=8;Length=28;SUPPRESSION=A,Simplified.usd
* BBox (world): size=(28.000, 8.000, 7.000), center=(-6.000, -10.000, 1.830)
* 几何统计: Mesh=1, Vertices=2310, Faces=4628
* 子Mesh材质: /World/PartB_OnBelt_12/node__Size_8_Length_28_SUPPRESSION_A_Simplified/geometry_1 -> 未绑定

---

### '/World/PartB_OnBelt_13' (Xform)

* 引用: reference:/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ping_Jian/Feather keys GB_converted/6;Size=8;Length=28;SUPPRESSION=A,Simplified.usd
* BBox (world): size=(28.000, 8.000, 7.000), center=(-7.800, -10.000, 1.830)
* 几何统计: Mesh=1, Vertices=2310, Faces=4628
* 子Mesh材质: /World/PartB_OnBelt_13/node__Size_8_Length_28_SUPPRESSION_A_Simplified/geometry_1 -> 未绑定

---

### '/World/PartB_OnBelt_14' (Xform)

* 引用: reference:/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ping_Jian/Feather keys GB_converted/6;Size=8;Length=28;SUPPRESSION=A,Simplified.usd
* BBox (world): size=(28.000, 8.000, 7.000), center=(-9.600, -10.000, 1.830)
* 几何统计: Mesh=1, Vertices=2310, Faces=4628
* 子Mesh材质: /World/PartB_OnBelt_14/node__Size_8_Length_28_SUPPRESSION_A_Simplified/geometry_1 -> 未绑定

---

### '/World/PartB_OnBelt_15' (Xform)

* 引用: reference:/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ping_Jian/Feather keys GB_converted/6;Size=8;Length=28;SUPPRESSION=A,Simplified.usd
* BBox (world): size=(28.000, 8.000, 7.000), center=(-11.400, -10.000, 1.830)
* 几何统计: Mesh=1, Vertices=2310, Faces=4628
* 子Mesh材质: /World/PartB_OnBelt_15/node__Size_8_Length_28_SUPPRESSION_A_Simplified/geometry_1 -> 未绑定

---

### '/World/PartB_OnBelt_16' (Xform)

* 引用: reference:/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ping_Jian/Feather keys GB_converted/6;Size=8;Length=28;SUPPRESSION=A,Simplified.usd
* BBox (world): size=(28.000, 8.000, 7.000), center=(-13.200, -10.000, 1.830)
* 几何统计: Mesh=1, Vertices=2310, Faces=4628
* 子Mesh材质: /World/PartB_OnBelt_16/node__Size_8_Length_28_SUPPRESSION_A_Simplified/geometry_1 -> 未绑定

---

### '/World/PartB_OnBelt_17' (Xform)

* 引用: reference:/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ping_Jian/Feather keys GB_converted/6;Size=8;Length=28;SUPPRESSION=A,Simplified.usd
* BBox (world): size=(28.000, 8.000, 7.000), center=(-15.000, -10.000, 1.830)
* 几何统计: Mesh=1, Vertices=2310, Faces=4628
* 子Mesh材质: /World/PartB_OnBelt_17/node__Size_8_Length_28_SUPPRESSION_A_Simplified/geometry_1 -> 未绑定

---

### '/World/PartB_OnBelt_18' (Xform)

* 引用: reference:/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ping_Jian/Feather keys GB_converted/6;Size=8;Length=28;SUPPRESSION=A,Simplified.usd
* BBox (world): size=(28.000, 8.000, 7.000), center=(-16.800, -10.000, 1.830)
* 几何统计: Mesh=1, Vertices=2310, Faces=4628
* 子Mesh材质: /World/PartB_OnBelt_18/node__Size_8_Length_28_SUPPRESSION_A_Simplified/geometry_1 -> 未绑定

---

### '/World/PartB_OnBelt_19' (Xform)

* 引用: reference:/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ping_Jian/Feather keys GB_converted/6;Size=8;Length=28;SUPPRESSION=A,Simplified.usd
* BBox (world): size=(28.000, 8.000, 7.000), center=(-2.400, -5.000, 1.830)
* 几何统计: Mesh=1, Vertices=2310, Faces=4628
* 子Mesh材质: /World/PartB_OnBelt_19/node__Size_8_Length_28_SUPPRESSION_A_Simplified/geometry_1 -> 未绑定

---

### '/World/PartB_OnBelt_20' (Xform)

* 引用: reference:/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ping_Jian/Feather keys GB_converted/6;Size=8;Length=28;SUPPRESSION=A,Simplified.usd
* BBox (world): size=(28.000, 8.000, 7.000), center=(-4.200, -5.000, 1.830)
* 几何统计: Mesh=1, Vertices=2310, Faces=4628
* 子Mesh材质: /World/PartB_OnBelt_20/node__Size_8_Length_28_SUPPRESSION_A_Simplified/geometry_1 -> 未绑定

---

### '/World/PartB_OnBelt_21' (Xform)

* 引用: reference:/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ping_Jian/Feather keys GB_converted/6;Size=8;Length=28;SUPPRESSION=A,Simplified.usd
* BBox (world): size=(28.000, 8.000, 7.000), center=(-6.000, -5.000, 1.830)
* 几何统计: Mesh=1, Vertices=2310, Faces=4628
* 子Mesh材质: /World/PartB_OnBelt_21/node__Size_8_Length_28_SUPPRESSION_A_Simplified/geometry_1 -> 未绑定

---

### '/World/PartB_OnBelt_22' (Xform)

* 引用: reference:/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ping_Jian/Feather keys GB_converted/6;Size=8;Length=28;SUPPRESSION=A,Simplified.usd
* BBox (world): size=(28.000, 8.000, 7.000), center=(-7.800, -5.000, 1.830)
* 几何统计: Mesh=1, Vertices=2310, Faces=4628
* 子Mesh材质: /World/PartB_OnBelt_22/node__Size_8_Length_28_SUPPRESSION_A_Simplified/geometry_1 -> 未绑定

---

### '/World/PartB_OnBelt_23' (Xform)

* 引用: reference:/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ping_Jian/Feather keys GB_converted/6;Size=8;Length=28;SUPPRESSION=A,Simplified.usd
* BBox (world): size=(28.000, 8.000, 7.000), center=(-9.600, -5.000, 1.830)
* 几何统计: Mesh=1, Vertices=2310, Faces=4628
* 子Mesh材质: /World/PartB_OnBelt_23/node__Size_8_Length_28_SUPPRESSION_A_Simplified/geometry_1 -> 未绑定

---

### '/World/PartB_OnBelt_24' (Xform)

* 引用: reference:/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ping_Jian/Feather keys GB_converted/6;Size=8;Length=28;SUPPRESSION=A,Simplified.usd
* BBox (world): size=(28.000, 8.000, 7.000), center=(-11.400, -5.000, 1.830)
* 几何统计: Mesh=1, Vertices=2310, Faces=4628
* 子Mesh材质: /World/PartB_OnBelt_24/node__Size_8_Length_28_SUPPRESSION_A_Simplified/geometry_1 -> 未绑定

---

### '/World/PartB_OnBelt_25' (Xform)

* 引用: reference:/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ping_Jian/Feather keys GB_converted/6;Size=8;Length=28;SUPPRESSION=A,Simplified.usd
* BBox (world): size=(28.000, 8.000, 7.000), center=(-13.200, -5.000, 1.830)
* 几何统计: Mesh=1, Vertices=2310, Faces=4628
* 子Mesh材质: /World/PartB_OnBelt_25/node__Size_8_Length_28_SUPPRESSION_A_Simplified/geometry_1 -> 未绑定

---

### '/World/PartB_OnBelt_26' (Xform)

* 引用: reference:/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ping_Jian/Feather keys GB_converted/6;Size=8;Length=28;SUPPRESSION=A,Simplified.usd
* BBox (world): size=(28.000, 8.000, 7.000), center=(-15.000, -5.000, 1.830)
* 几何统计: Mesh=1, Vertices=2310, Faces=4628
* 子Mesh材质: /World/PartB_OnBelt_26/node__Size_8_Length_28_SUPPRESSION_A_Simplified/geometry_1 -> 未绑定

---

### '/World/PartB_OnBelt_27' (Xform)

* 引用: reference:/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ping_Jian/Feather keys GB_converted/6;Size=8;Length=28;SUPPRESSION=A,Simplified.usd
* BBox (world): size=(28.000, 8.000, 7.000), center=(-16.800, -5.000, 1.830)
* 几何统计: Mesh=1, Vertices=2310, Faces=4628
* 子Mesh材质: /World/PartB_OnBelt_27/node__Size_8_Length_28_SUPPRESSION_A_Simplified/geometry_1 -> 未绑定

---

### '/World/PartB_OnBelt_28' (Xform)

* 引用: reference:/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ping_Jian/Feather keys GB_converted/6;Size=8;Length=28;SUPPRESSION=A,Simplified.usd
* BBox (world): size=(28.000, 8.000, 7.000), center=(-2.400, 0.000, 1.830)
* 几何统计: Mesh=1, Vertices=2310, Faces=4628
* 子Mesh材质: /World/PartB_OnBelt_28/node__Size_8_Length_28_SUPPRESSION_A_Simplified/geometry_1 -> 未绑定

---

### '/World/PartB_OnBelt_29' (Xform)

* 引用: reference:/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ping_Jian/Feather keys GB_converted/6;Size=8;Length=28;SUPPRESSION=A,Simplified.usd
* BBox (world): size=(28.000, 8.000, 7.000), center=(-4.200, 0.000, 1.830)
* 几何统计: Mesh=1, Vertices=2310, Faces=4628
* 子Mesh材质: /World/PartB_OnBelt_29/node__Size_8_Length_28_SUPPRESSION_A_Simplified/geometry_1 -> 未绑定

---

### '/World/PartB_OnBelt_30' (Xform)

* 引用: reference:/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ping_Jian/Feather keys GB_converted/6;Size=8;Length=28;SUPPRESSION=A,Simplified.usd
* BBox (world): size=(28.000, 8.000, 7.000), center=(-6.000, 0.000, 1.830)
* 几何统计: Mesh=1, Vertices=2310, Faces=4628
* 子Mesh材质: /World/PartB_OnBelt_30/node__Size_8_Length_28_SUPPRESSION_A_Simplified/geometry_1 -> 未绑定

---

### '/World/PartB_OnBelt_31' (Xform)

* 引用: reference:/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ping_Jian/Feather keys GB_converted/6;Size=8;Length=28;SUPPRESSION=A,Simplified.usd
* BBox (world): size=(28.000, 8.000, 7.000), center=(-7.800, 0.000, 1.830)
* 几何统计: Mesh=1, Vertices=2310, Faces=4628
* 子Mesh材质: /World/PartB_OnBelt_31/node__Size_8_Length_28_SUPPRESSION_A_Simplified/geometry_1 -> 未绑定

---

### '/World/PartB_OnBelt_32' (Xform)

* 引用: reference:/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ping_Jian/Feather keys GB_converted/6;Size=8;Length=28;SUPPRESSION=A,Simplified.usd
* BBox (world): size=(28.000, 8.000, 7.000), center=(-9.600, 0.000, 1.830)
* 几何统计: Mesh=1, Vertices=2310, Faces=4628
* 子Mesh材质: /World/PartB_OnBelt_32/node__Size_8_Length_28_SUPPRESSION_A_Simplified/geometry_1 -> 未绑定

---

### '/World/PartB_OnBelt_33' (Xform)

* 引用: reference:/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ping_Jian/Feather keys GB_converted/6;Size=8;Length=28;SUPPRESSION=A,Simplified.usd
* BBox (world): size=(28.000, 8.000, 7.000), center=(-11.400, 0.000, 1.830)
* 几何统计: Mesh=1, Vertices=2310, Faces=4628
* 子Mesh材质: /World/PartB_OnBelt_33/node__Size_8_Length_28_SUPPRESSION_A_Simplified/geometry_1 -> 未绑定

---

### '/World/PartB_OnBelt_34' (Xform)

* 引用: reference:/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ping_Jian/Feather keys GB_converted/6;Size=8;Length=28;SUPPRESSION=A,Simplified.usd
* BBox (world): size=(28.000, 8.000, 7.000), center=(-13.200, 0.000, 1.830)
* 几何统计: Mesh=1, Vertices=2310, Faces=4628
* 子Mesh材质: /World/PartB_OnBelt_34/node__Size_8_Length_28_SUPPRESSION_A_Simplified/geometry_1 -> 未绑定

---

### '/World/PartB_OnBelt_35' (Xform)

* 引用: reference:/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ping_Jian/Feather keys GB_converted/6;Size=8;Length=28;SUPPRESSION=A,Simplified.usd
* BBox (world): size=(28.000, 8.000, 7.000), center=(-15.000, 0.000, 1.830)
* 几何统计: Mesh=1, Vertices=2310, Faces=4628
* 子Mesh材质: /World/PartB_OnBelt_35/node__Size_8_Length_28_SUPPRESSION_A_Simplified/geometry_1 -> 未绑定

---

### '/World/PartB_OnBelt_36' (Xform)

* 引用: reference:/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ping_Jian/Feather keys GB_converted/6;Size=8;Length=28;SUPPRESSION=A,Simplified.usd
* BBox (world): size=(28.000, 8.000, 7.000), center=(-16.800, 0.000, 1.830)
* 几何统计: Mesh=1, Vertices=2310, Faces=4628
* 子Mesh材质: /World/PartB_OnBelt_36/node__Size_8_Length_28_SUPPRESSION_A_Simplified/geometry_1 -> 未绑定

---

### '/World/PartB_OnBelt_37' (Xform)

* 引用: reference:/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ping_Jian/Feather keys GB_converted/6;Size=8;Length=28;SUPPRESSION=A,Simplified.usd
* BBox (world): size=(28.000, 8.000, 7.000), center=(-2.400, 5.000, 1.830)
* 几何统计: Mesh=1, Vertices=2310, Faces=4628
* 子Mesh材质: /World/PartB_OnBelt_37/node__Size_8_Length_28_SUPPRESSION_A_Simplified/geometry_1 -> 未绑定

---

### '/World/PartB_OnBelt_38' (Xform)

* 引用: reference:/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ping_Jian/Feather keys GB_converted/6;Size=8;Length=28;SUPPRESSION=A,Simplified.usd
* BBox (world): size=(28.000, 8.000, 7.000), center=(-4.200, 5.000, 1.830)
* 几何统计: Mesh=1, Vertices=2310, Faces=4628
* 子Mesh材质: /World/PartB_OnBelt_38/node__Size_8_Length_28_SUPPRESSION_A_Simplified/geometry_1 -> 未绑定

---

### '/World/PartB_OnBelt_39' (Xform)

* 引用: reference:/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ping_Jian/Feather keys GB_converted/6;Size=8;Length=28;SUPPRESSION=A,Simplified.usd
* BBox (world): size=(28.000, 8.000, 7.000), center=(-6.000, 5.000, 1.830)
* 几何统计: Mesh=1, Vertices=2310, Faces=4628
* 子Mesh材质: /World/PartB_OnBelt_39/node__Size_8_Length_28_SUPPRESSION_A_Simplified/geometry_1 -> 未绑定

---

### '/World/PartB_OnBelt_40' (Xform)

* 引用: reference:/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ping_Jian/Feather keys GB_converted/6;Size=8;Length=28;SUPPRESSION=A,Simplified.usd
* BBox (world): size=(28.000, 8.000, 7.000), center=(-7.800, 5.000, 1.830)
* 几何统计: Mesh=1, Vertices=2310, Faces=4628
* 子Mesh材质: /World/PartB_OnBelt_40/node__Size_8_Length_28_SUPPRESSION_A_Simplified/geometry_1 -> 未绑定

---

### '/World/PartB_OnBelt_41' (Xform)

* 引用: reference:/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ping_Jian/Feather keys GB_converted/6;Size=8;Length=28;SUPPRESSION=A,Simplified.usd
* BBox (world): size=(28.000, 8.000, 7.000), center=(-9.600, 5.000, 1.830)
* 几何统计: Mesh=1, Vertices=2310, Faces=4628
* 子Mesh材质: /World/PartB_OnBelt_41/node__Size_8_Length_28_SUPPRESSION_A_Simplified/geometry_1 -> 未绑定

---

### '/World/PartB_OnBelt_42' (Xform)

* 引用: reference:/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ping_Jian/Feather keys GB_converted/6;Size=8;Length=28;SUPPRESSION=A,Simplified.usd
* BBox (world): size=(28.000, 8.000, 7.000), center=(-11.400, 5.000, 1.830)
* 几何统计: Mesh=1, Vertices=2310, Faces=4628
* 子Mesh材质: /World/PartB_OnBelt_42/node__Size_8_Length_28_SUPPRESSION_A_Simplified/geometry_1 -> 未绑定

---

### '/World/PartB_OnBelt_43' (Xform)

* 引用: reference:/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ping_Jian/Feather keys GB_converted/6;Size=8;Length=28;SUPPRESSION=A,Simplified.usd
* BBox (world): size=(28.000, 8.000, 7.000), center=(-13.200, 5.000, 1.830)
* 几何统计: Mesh=1, Vertices=2310, Faces=4628
* 子Mesh材质: /World/PartB_OnBelt_43/node__Size_8_Length_28_SUPPRESSION_A_Simplified/geometry_1 -> 未绑定

---

### '/World/PartB_OnBelt_44' (Xform)

* 引用: reference:/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ping_Jian/Feather keys GB_converted/6;Size=8;Length=28;SUPPRESSION=A,Simplified.usd
* BBox (world): size=(28.000, 8.000, 7.000), center=(-15.000, 5.000, 1.830)
* 几何统计: Mesh=1, Vertices=2310, Faces=4628
* 子Mesh材质: /World/PartB_OnBelt_44/node__Size_8_Length_28_SUPPRESSION_A_Simplified/geometry_1 -> 未绑定

---

### '/World/PartB_OnBelt_45' (Xform)

* 引用: reference:/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ping_Jian/Feather keys GB_converted/6;Size=8;Length=28;SUPPRESSION=A,Simplified.usd
* BBox (world): size=(28.000, 8.000, 7.000), center=(-16.800, 5.000, 1.830)
* 几何统计: Mesh=1, Vertices=2310, Faces=4628
* 子Mesh材质: /World/PartB_OnBelt_45/node__Size_8_Length_28_SUPPRESSION_A_Simplified/geometry_1 -> 未绑定

---

### '/World/PartB_OnBelt_46' (Xform)

* 引用: reference:/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ping_Jian/Feather keys GB_converted/6;Size=8;Length=28;SUPPRESSION=A,Simplified.usd
* BBox (world): size=(28.000, 8.000, 7.000), center=(-2.400, 10.000, 1.830)
* 几何统计: Mesh=1, Vertices=2310, Faces=4628
* 子Mesh材质: /World/PartB_OnBelt_46/node__Size_8_Length_28_SUPPRESSION_A_Simplified/geometry_1 -> 未绑定

---

### '/World/PartB_OnBelt_47' (Xform)

* 引用: reference:/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ping_Jian/Feather keys GB_converted/6;Size=8;Length=28;SUPPRESSION=A,Simplified.usd
* BBox (world): size=(28.000, 8.000, 7.000), center=(-4.200, 10.000, 1.830)
* 几何统计: Mesh=1, Vertices=2310, Faces=4628
* 子Mesh材质: /World/PartB_OnBelt_47/node__Size_8_Length_28_SUPPRESSION_A_Simplified/geometry_1 -> 未绑定

---

### '/World/PartB_OnBelt_48' (Xform)

* 引用: reference:/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ping_Jian/Feather keys GB_converted/6;Size=8;Length=28;SUPPRESSION=A,Simplified.usd
* BBox (world): size=(28.000, 8.000, 7.000), center=(-6.000, 10.000, 1.830)
* 几何统计: Mesh=1, Vertices=2310, Faces=4628
* 子Mesh材质: /World/PartB_OnBelt_48/node__Size_8_Length_28_SUPPRESSION_A_Simplified/geometry_1 -> 未绑定

---

### '/World/PartB_OnBelt_49' (Xform)

* 引用: reference:/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ping_Jian/Feather keys GB_converted/6;Size=8;Length=28;SUPPRESSION=A,Simplified.usd
* BBox (world): size=(28.000, 8.000, 7.000), center=(-7.800, 10.000, 1.830)
* 几何统计: Mesh=1, Vertices=2310, Faces=4628
* 子Mesh材质: /World/PartB_OnBelt_49/node__Size_8_Length_28_SUPPRESSION_A_Simplified/geometry_1 -> 未绑定

---

### '/World/PartB_OnBelt_50' (Xform)

* 引用: reference:/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ping_Jian/Feather keys GB_converted/6;Size=8;Length=28;SUPPRESSION=A,Simplified.usd
* BBox (world): size=(28.000, 8.000, 7.000), center=(-9.600, 10.000, 1.830)
* 几何统计: Mesh=1, Vertices=2310, Faces=4628
* 子Mesh材质: /World/PartB_OnBelt_50/node__Size_8_Length_28_SUPPRESSION_A_Simplified/geometry_1 -> 未绑定

---

### '/World/PartB_OnBelt_51' (Xform)

* 引用: reference:/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ping_Jian/Feather keys GB_converted/6;Size=8;Length=28;SUPPRESSION=A,Simplified.usd
* BBox (world): size=(28.000, 8.000, 7.000), center=(-11.400, 10.000, 1.830)
* 几何统计: Mesh=1, Vertices=2310, Faces=4628
* 子Mesh材质: /World/PartB_OnBelt_51/node__Size_8_Length_28_SUPPRESSION_A_Simplified/geometry_1 -> 未绑定

---

### '/World/PartB_OnBelt_52' (Xform)

* 引用: reference:/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ping_Jian/Feather keys GB_converted/6;Size=8;Length=28;SUPPRESSION=A,Simplified.usd
* BBox (world): size=(28.000, 8.000, 7.000), center=(-13.200, 10.000, 1.830)
* 几何统计: Mesh=1, Vertices=2310, Faces=4628
* 子Mesh材质: /World/PartB_OnBelt_52/node__Size_8_Length_28_SUPPRESSION_A_Simplified/geometry_1 -> 未绑定

---

### '/World/PartB_OnBelt_53' (Xform)

* 引用: reference:/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ping_Jian/Feather keys GB_converted/6;Size=8;Length=28;SUPPRESSION=A,Simplified.usd
* BBox (world): size=(28.000, 8.000, 7.000), center=(-15.000, 10.000, 1.830)
* 几何统计: Mesh=1, Vertices=2310, Faces=4628
* 子Mesh材质: /World/PartB_OnBelt_53/node__Size_8_Length_28_SUPPRESSION_A_Simplified/geometry_1 -> 未绑定

---

### '/World/PartB_OnBelt_54' (Xform)

* 引用: reference:/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ping_Jian/Feather keys GB_converted/6;Size=8;Length=28;SUPPRESSION=A,Simplified.usd
* BBox (world): size=(28.000, 8.000, 7.000), center=(-16.800, 10.000, 1.830)
* 几何统计: Mesh=1, Vertices=2310, Faces=4628
* 子Mesh材质: /World/PartB_OnBelt_54/node__Size_8_Length_28_SUPPRESSION_A_Simplified/geometry_1 -> 未绑定

---

### '/World/PartB_OnBelt_55' (Xform)

* 引用: reference:/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ping_Jian/Feather keys GB_converted/6;Size=8;Length=28;SUPPRESSION=A,Simplified.usd
* BBox (world): size=(28.000, 8.000, 7.000), center=(-2.400, 15.000, 1.830)
* 几何统计: Mesh=1, Vertices=2310, Faces=4628
* 子Mesh材质: /World/PartB_OnBelt_55/node__Size_8_Length_28_SUPPRESSION_A_Simplified/geometry_1 -> 未绑定

---

### '/World/PartB_OnBelt_56' (Xform)

* 引用: reference:/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ping_Jian/Feather keys GB_converted/6;Size=8;Length=28;SUPPRESSION=A,Simplified.usd
* BBox (world): size=(28.000, 8.000, 7.000), center=(-4.200, 15.000, 1.830)
* 几何统计: Mesh=1, Vertices=2310, Faces=4628
* 子Mesh材质: /World/PartB_OnBelt_56/node__Size_8_Length_28_SUPPRESSION_A_Simplified/geometry_1 -> 未绑定

---

### '/World/PartB_OnBelt_57' (Xform)

* 引用: reference:/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ping_Jian/Feather keys GB_converted/6;Size=8;Length=28;SUPPRESSION=A,Simplified.usd
* BBox (world): size=(28.000, 8.000, 7.000), center=(-6.000, 15.000, 1.830)
* 几何统计: Mesh=1, Vertices=2310, Faces=4628
* 子Mesh材质: /World/PartB_OnBelt_57/node__Size_8_Length_28_SUPPRESSION_A_Simplified/geometry_1 -> 未绑定

---

### '/World/PartB_OnBelt_58' (Xform)

* 引用: reference:/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ping_Jian/Feather keys GB_converted/6;Size=8;Length=28;SUPPRESSION=A,Simplified.usd
* BBox (world): size=(28.000, 8.000, 7.000), center=(-7.800, 15.000, 1.830)
* 几何统计: Mesh=1, Vertices=2310, Faces=4628
* 子Mesh材质: /World/PartB_OnBelt_58/node__Size_8_Length_28_SUPPRESSION_A_Simplified/geometry_1 -> 未绑定

---

### '/World/PartB_OnBelt_59' (Xform)

* 引用: reference:/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ping_Jian/Feather keys GB_converted/6;Size=8;Length=28;SUPPRESSION=A,Simplified.usd
* BBox (world): size=(28.000, 8.000, 7.000), center=(-9.600, 15.000, 1.830)
* 几何统计: Mesh=1, Vertices=2310, Faces=4628
* 子Mesh材质: /World/PartB_OnBelt_59/node__Size_8_Length_28_SUPPRESSION_A_Simplified/geometry_1 -> 未绑定

---

### '/World/PartB_OnBelt_60' (Xform)

* 引用: reference:/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ping_Jian/Feather keys GB_converted/6;Size=8;Length=28;SUPPRESSION=A,Simplified.usd
* BBox (world): size=(28.000, 8.000, 7.000), center=(-11.400, 15.000, 1.830)
* 几何统计: Mesh=1, Vertices=2310, Faces=4628
* 子Mesh材质: /World/PartB_OnBelt_60/node__Size_8_Length_28_SUPPRESSION_A_Simplified/geometry_1 -> 未绑定

---

### '/World/PartB_OnBelt_61' (Xform)

* 引用: reference:/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ping_Jian/Feather keys GB_converted/6;Size=8;Length=28;SUPPRESSION=A,Simplified.usd
* BBox (world): size=(28.000, 8.000, 7.000), center=(-13.200, 15.000, 1.830)
* 几何统计: Mesh=1, Vertices=2310, Faces=4628
* 子Mesh材质: /World/PartB_OnBelt_61/node__Size_8_Length_28_SUPPRESSION_A_Simplified/geometry_1 -> 未绑定

---

### '/World/PartB_OnBelt_62' (Xform)

* 引用: reference:/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ping_Jian/Feather keys GB_converted/6;Size=8;Length=28;SUPPRESSION=A,Simplified.usd
* BBox (world): size=(28.000, 8.000, 7.000), center=(-15.000, 15.000, 1.830)
* 几何统计: Mesh=1, Vertices=2310, Faces=4628
* 子Mesh材质: /World/PartB_OnBelt_62/node__Size_8_Length_28_SUPPRESSION_A_Simplified/geometry_1 -> 未绑定

---

### '/World/PartB_OnBelt_63' (Xform)

* 引用: reference:/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ping_Jian/Feather keys GB_converted/6;Size=8;Length=28;SUPPRESSION=A,Simplified.usd
* BBox (world): size=(28.000, 8.000, 7.000), center=(-16.800, 15.000, 1.830)
* 几何统计: Mesh=1, Vertices=2310, Faces=4628
* 子Mesh材质: /World/PartB_OnBelt_63/node__Size_8_Length_28_SUPPRESSION_A_Simplified/geometry_1 -> 未绑定

---

### '/World/PartA_OnWorkbench_1' (Xform)

* 引用: reference:/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ban_Yuan_Jian/Woodruff keys GB_converted/0;Size=1.0x1.4x4;SUPPRESSION=Default.usd
* BBox (world): size=(3.816, 1.400, 1.000), center=(0.000, -15.248, 0.892)
* 几何统计: Mesh=1, Vertices=414, Faces=824
* 子Mesh材质: /World/PartA_OnWorkbench_1/node__Size_1_0x1_4x4_SUPPRESSION_Default/geometry_1 -> 未绑定

---

### '/World/PartA_OnWorkbench_2' (Xform)

* 引用: reference:/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ban_Yuan_Jian/Woodruff keys GB_converted/0;Size=1.0x1.4x4;SUPPRESSION=Default.usd
* BBox (world): size=(3.816, 1.400, 1.000), center=(0.000, -10.248, 0.892)
* 几何统计: Mesh=1, Vertices=414, Faces=824
* 子Mesh材质: /World/PartA_OnWorkbench_2/node__Size_1_0x1_4x4_SUPPRESSION_Default/geometry_1 -> 未绑定

---

### '/World/PartA_OnWorkbench_3' (Xform)

* 引用: reference:/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ban_Yuan_Jian/Woodruff keys GB_converted/0;Size=1.0x1.4x4;SUPPRESSION=Default.usd
* BBox (world): size=(3.816, 1.400, 1.000), center=(0.000, -5.248, 0.892)
* 几何统计: Mesh=1, Vertices=414, Faces=824
* 子Mesh材质: /World/PartA_OnWorkbench_3/node__Size_1_0x1_4x4_SUPPRESSION_Default/geometry_1 -> 未绑定

---

### '/World/PartA_OnWorkbench_4' (Xform)

* 引用: reference:/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ban_Yuan_Jian/Woodruff keys GB_converted/0;Size=1.0x1.4x4;SUPPRESSION=Default.usd
* BBox (world): size=(3.816, 1.400, 1.000), center=(0.000, -0.248, 0.892)
* 几何统计: Mesh=1, Vertices=414, Faces=824
* 子Mesh材质: /World/PartA_OnWorkbench_4/node__Size_1_0x1_4x4_SUPPRESSION_Default/geometry_1 -> 未绑定

---

### '/World/PartA_OnWorkbench_5' (Xform)

* 引用: reference:/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ban_Yuan_Jian/Woodruff keys GB_converted/0;Size=1.0x1.4x4;SUPPRESSION=Default.usd
* BBox (world): size=(3.816, 1.400, 1.000), center=(0.000, 4.752, 0.892)
* 几何统计: Mesh=1, Vertices=414, Faces=824
* 子Mesh材质: /World/PartA_OnWorkbench_5/node__Size_1_0x1_4x4_SUPPRESSION_Default/geometry_1 -> 未绑定

---

### '/World/PartA_OnWorkbench_6' (Xform)

* 引用: reference:/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ban_Yuan_Jian/Woodruff keys GB_converted/0;Size=1.0x1.4x4;SUPPRESSION=Default.usd
* BBox (world): size=(3.816, 1.400, 1.000), center=(0.000, 9.752, 0.892)
* 几何统计: Mesh=1, Vertices=414, Faces=824
* 子Mesh材质: /World/PartA_OnWorkbench_6/node__Size_1_0x1_4x4_SUPPRESSION_Default/geometry_1 -> 未绑定

---

### '/World/PartB_OnWorkbench_1' (Xform)

* 引用: reference:/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ping_Jian/Feather keys GB_converted/6;Size=8;Length=28;SUPPRESSION=A,Simplified.usd
* BBox (world): size=(28.000, 8.000, 7.000), center=(0.000, -14.708, 0.892)
* 几何统计: Mesh=1, Vertices=2310, Faces=4628
* 子Mesh材质: /World/PartB_OnWorkbench_1/node__Size_8_Length_28_SUPPRESSION_A_Simplified/geometry_1 -> 未绑定

---

### '/World/PartB_OnWorkbench_2' (Xform)

* 引用: reference:/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ping_Jian/Feather keys GB_converted/6;Size=8;Length=28;SUPPRESSION=A,Simplified.usd
* BBox (world): size=(28.000, 8.000, 7.000), center=(0.000, -9.708, 0.892)
* 几何统计: Mesh=1, Vertices=2310, Faces=4628
* 子Mesh材质: /World/PartB_OnWorkbench_2/node__Size_8_Length_28_SUPPRESSION_A_Simplified/geometry_1 -> 未绑定

---

### '/World/PartB_OnWorkbench_3' (Xform)

* 引用: reference:/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ping_Jian/Feather keys GB_converted/6;Size=8;Length=28;SUPPRESSION=A,Simplified.usd
* BBox (world): size=(28.000, 8.000, 7.000), center=(0.000, -4.708, 0.892)
* 几何统计: Mesh=1, Vertices=2310, Faces=4628
* 子Mesh材质: /World/PartB_OnWorkbench_3/node__Size_8_Length_28_SUPPRESSION_A_Simplified/geometry_1 -> 未绑定

---

### '/World/PartB_OnWorkbench_4' (Xform)

* 引用: reference:/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ping_Jian/Feather keys GB_converted/6;Size=8;Length=28;SUPPRESSION=A,Simplified.usd
* BBox (world): size=(28.000, 8.000, 7.000), center=(0.000, 0.292, 0.892)
* 几何统计: Mesh=1, Vertices=2310, Faces=4628
* 子Mesh材质: /World/PartB_OnWorkbench_4/node__Size_8_Length_28_SUPPRESSION_A_Simplified/geometry_1 -> 未绑定

---

### '/World/PartB_OnWorkbench_5' (Xform)

* 引用: reference:/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ping_Jian/Feather keys GB_converted/6;Size=8;Length=28;SUPPRESSION=A,Simplified.usd
* BBox (world): size=(28.000, 8.000, 7.000), center=(0.000, 5.292, 0.892)
* 几何统计: Mesh=1, Vertices=2310, Faces=4628
* 子Mesh材质: /World/PartB_OnWorkbench_5/node__Size_8_Length_28_SUPPRESSION_A_Simplified/geometry_1 -> 未绑定

---

### '/World/PartB_OnWorkbench_6' (Xform)

* 引用: reference:/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ping_Jian/Feather keys GB_converted/6;Size=8;Length=28;SUPPRESSION=A,Simplified.usd
* BBox (world): size=(28.000, 8.000, 7.000), center=(0.000, 10.292, 0.892)
* 几何统计: Mesh=1, Vertices=2310, Faces=4628
* 子Mesh材质: /World/PartB_OnWorkbench_6/node__Size_8_Length_28_SUPPRESSION_A_Simplified/geometry_1 -> 未绑定

---

### '/World/agv_1' (Xform)

* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/AGV_ready_1/AGV_ready_1.usdc
* BBox (world): size=(1.457, 0.340, 0.669), center=(2.098, -14.286, 0.059)
* 几何统计: Mesh=171, Vertices=1634024, Faces=683203
* 子Mesh材质: /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_2/Object_0 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_3/Object_1 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_4/Object_2 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_5/Object_3 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_6/Object_4 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_7/Object_5 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_8/Object_6 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_9/Object_7 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_10/Object_8 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_11/Object_9 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_12/Object_10 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_13/Object_11 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_14/Object_12 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_15/Object_13 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_16/Object_14 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_17/Object_15 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_18/Object_16 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_19/Object_17 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_20/Object_18 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_21/Object_19 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_22/Object_20 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_23/Object_21 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_24/Object_22 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_25/Object_23 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_26/Object_24 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_27/Object_25 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_28/Object_26 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_29/Object_27 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_30/Object_28 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_31/Object_29 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_32/Object_30 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_33/Object_31 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_34/Object_32 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_35/Object_33 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_36/Object_34 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_37/Object_35 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_38/Object_36 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_39/Object_37 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_40/Object_38 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_41/Object_39 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_42/Object_40 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_43/Object_41 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_44/Object_42 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_45/Object_43 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_46/Object_44 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_47/Object_45 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_48/Object_46 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_49/Object_47 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_50/Object_48 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_51/Object_49 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_52/Object_50 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_53/Object_51 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_54/Object_52 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_55/Object_53 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_56/Object_54 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_57/Object_55 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_58/Object_56 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_59/Object_57 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_60/Object_58 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_61/Object_59 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_62/Object_60 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_63/Object_61 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_64/Object_62 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_65/Object_63 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_66/Object_64 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_67/Object_65 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_68/Object_66 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_69/Object_67 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_70/Object_68 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_71/Object_69 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_72/Object_70 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_73/Object_71 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_74/Object_72 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_75/Object_73 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_76/Object_74 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_77/Object_75 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_78/Object_76 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_79/Object_77 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_80/Object_78 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_81/Object_79 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_82/Object_80 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_83/Object_81 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_84/Object_82 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_85/Object_83 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_86/Object_84 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_87/Object_85 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_88/Object_86 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_89/Object_87 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_90/Object_88 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_91/Object_89 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_92/Object_90 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_93/Object_91 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_94/Object_92 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_95/Object_93 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_96/Object_94 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_97/Object_95 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_98/Object_96 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_99/Object_97 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_100/Object_98 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_101/Object_99 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_102/Object_100 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_103/Object_101 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_104/Object_102 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_105/Object_103 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_106/Object_104 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_107/Object_105 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_108/Object_106 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_109/Object_107 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_110/Object_108 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_111/Object_109 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_112/Object_110 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_113/Object_111 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_114/Object_112 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_115/Object_113 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_116/Object_114 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_117/Object_115 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_118/Object_116 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_119/Object_117 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_120/Object_118 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_121/Object_119 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_122/Object_120 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_123/Object_121 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_124/Object_122 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_125/Object_123 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_126/Object_124 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_127/Object_125 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_128/Object_126 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_129/Object_127 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_130/Object_128 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_131/Object_129 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_132/Object_130 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_133/Object_131 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_134/Object_132 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_135/Object_133 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_136/Object_134 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_137/Object_135 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_138/Object_136 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_139/Object_137 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_140/Object_138 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_141/Object_139 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_142/Object_140 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_143/Object_141 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_144/Object_142 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_145/Object_143 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_146/Object_144 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_147/Object_145 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_148/Object_146 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_149/Object_147 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_150/Object_148 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_151/Object_149 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_152/Object_150 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_153/Object_151 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_154/Object_152 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_155/Object_153 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_156/Object_154 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_157/Object_155 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_158/Object_156 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_159/Object_157 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_160/Object_158 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_161/Object_159 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_162/Object_160 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_163/Object_161 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_164/Object_162 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_165/Object_163 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_166/Object_164 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_167/Object_165 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_168/Object_166 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_169/Object_167 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_170/Object_168 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_171/Object_169 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_172/Object_170 -> 未绑定

---

### '/World/agv_2' (Xform)

* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/AGV_ready_1/AGV_ready_1.usdc
* BBox (world): size=(1.457, 0.340, 0.669), center=(2.098, -9.286, 0.059)
* 几何统计: Mesh=171, Vertices=1634024, Faces=683203
* 子Mesh材质: /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_2/Object_0 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_3/Object_1 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_4/Object_2 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_5/Object_3 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_6/Object_4 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_7/Object_5 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_8/Object_6 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_9/Object_7 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_10/Object_8 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_11/Object_9 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_12/Object_10 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_13/Object_11 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_14/Object_12 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_15/Object_13 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_16/Object_14 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_17/Object_15 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_18/Object_16 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_19/Object_17 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_20/Object_18 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_21/Object_19 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_22/Object_20 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_23/Object_21 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_24/Object_22 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_25/Object_23 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_26/Object_24 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_27/Object_25 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_28/Object_26 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_29/Object_27 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_30/Object_28 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_31/Object_29 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_32/Object_30 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_33/Object_31 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_34/Object_32 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_35/Object_33 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_36/Object_34 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_37/Object_35 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_38/Object_36 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_39/Object_37 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_40/Object_38 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_41/Object_39 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_42/Object_40 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_43/Object_41 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_44/Object_42 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_45/Object_43 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_46/Object_44 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_47/Object_45 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_48/Object_46 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_49/Object_47 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_50/Object_48 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_51/Object_49 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_52/Object_50 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_53/Object_51 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_54/Object_52 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_55/Object_53 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_56/Object_54 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_57/Object_55 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_58/Object_56 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_59/Object_57 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_60/Object_58 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_61/Object_59 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_62/Object_60 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_63/Object_61 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_64/Object_62 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_65/Object_63 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_66/Object_64 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_67/Object_65 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_68/Object_66 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_69/Object_67 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_70/Object_68 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_71/Object_69 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_72/Object_70 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_73/Object_71 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_74/Object_72 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_75/Object_73 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_76/Object_74 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_77/Object_75 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_78/Object_76 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_79/Object_77 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_80/Object_78 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_81/Object_79 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_82/Object_80 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_83/Object_81 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_84/Object_82 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_85/Object_83 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_86/Object_84 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_87/Object_85 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_88/Object_86 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_89/Object_87 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_90/Object_88 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_91/Object_89 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_92/Object_90 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_93/Object_91 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_94/Object_92 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_95/Object_93 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_96/Object_94 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_97/Object_95 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_98/Object_96 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_99/Object_97 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_100/Object_98 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_101/Object_99 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_102/Object_100 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_103/Object_101 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_104/Object_102 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_105/Object_103 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_106/Object_104 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_107/Object_105 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_108/Object_106 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_109/Object_107 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_110/Object_108 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_111/Object_109 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_112/Object_110 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_113/Object_111 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_114/Object_112 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_115/Object_113 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_116/Object_114 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_117/Object_115 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_118/Object_116 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_119/Object_117 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_120/Object_118 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_121/Object_119 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_122/Object_120 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_123/Object_121 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_124/Object_122 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_125/Object_123 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_126/Object_124 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_127/Object_125 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_128/Object_126 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_129/Object_127 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_130/Object_128 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_131/Object_129 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_132/Object_130 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_133/Object_131 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_134/Object_132 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_135/Object_133 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_136/Object_134 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_137/Object_135 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_138/Object_136 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_139/Object_137 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_140/Object_138 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_141/Object_139 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_142/Object_140 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_143/Object_141 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_144/Object_142 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_145/Object_143 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_146/Object_144 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_147/Object_145 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_148/Object_146 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_149/Object_147 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_150/Object_148 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_151/Object_149 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_152/Object_150 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_153/Object_151 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_154/Object_152 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_155/Object_153 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_156/Object_154 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_157/Object_155 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_158/Object_156 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_159/Object_157 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_160/Object_158 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_161/Object_159 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_162/Object_160 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_163/Object_161 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_164/Object_162 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_165/Object_163 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_166/Object_164 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_167/Object_165 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_168/Object_166 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_169/Object_167 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_170/Object_168 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_171/Object_169 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_172/Object_170 -> 未绑定

---

### '/World/agv_3' (Xform)

* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/AGV_ready_1/AGV_ready_1.usdc
* BBox (world): size=(1.457, 0.340, 0.669), center=(2.098, -4.286, 0.059)
* 几何统计: Mesh=171, Vertices=1634024, Faces=683203
* 子Mesh材质: /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_2/Object_0 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_3/Object_1 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_4/Object_2 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_5/Object_3 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_6/Object_4 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_7/Object_5 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_8/Object_6 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_9/Object_7 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_10/Object_8 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_11/Object_9 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_12/Object_10 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_13/Object_11 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_14/Object_12 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_15/Object_13 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_16/Object_14 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_17/Object_15 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_18/Object_16 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_19/Object_17 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_20/Object_18 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_21/Object_19 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_22/Object_20 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_23/Object_21 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_24/Object_22 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_25/Object_23 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_26/Object_24 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_27/Object_25 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_28/Object_26 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_29/Object_27 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_30/Object_28 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_31/Object_29 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_32/Object_30 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_33/Object_31 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_34/Object_32 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_35/Object_33 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_36/Object_34 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_37/Object_35 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_38/Object_36 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_39/Object_37 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_40/Object_38 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_41/Object_39 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_42/Object_40 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_43/Object_41 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_44/Object_42 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_45/Object_43 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_46/Object_44 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_47/Object_45 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_48/Object_46 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_49/Object_47 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_50/Object_48 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_51/Object_49 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_52/Object_50 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_53/Object_51 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_54/Object_52 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_55/Object_53 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_56/Object_54 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_57/Object_55 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_58/Object_56 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_59/Object_57 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_60/Object_58 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_61/Object_59 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_62/Object_60 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_63/Object_61 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_64/Object_62 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_65/Object_63 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_66/Object_64 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_67/Object_65 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_68/Object_66 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_69/Object_67 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_70/Object_68 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_71/Object_69 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_72/Object_70 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_73/Object_71 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_74/Object_72 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_75/Object_73 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_76/Object_74 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_77/Object_75 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_78/Object_76 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_79/Object_77 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_80/Object_78 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_81/Object_79 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_82/Object_80 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_83/Object_81 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_84/Object_82 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_85/Object_83 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_86/Object_84 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_87/Object_85 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_88/Object_86 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_89/Object_87 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_90/Object_88 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_91/Object_89 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_92/Object_90 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_93/Object_91 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_94/Object_92 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_95/Object_93 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_96/Object_94 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_97/Object_95 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_98/Object_96 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_99/Object_97 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_100/Object_98 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_101/Object_99 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_102/Object_100 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_103/Object_101 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_104/Object_102 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_105/Object_103 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_106/Object_104 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_107/Object_105 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_108/Object_106 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_109/Object_107 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_110/Object_108 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_111/Object_109 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_112/Object_110 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_113/Object_111 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_114/Object_112 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_115/Object_113 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_116/Object_114 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_117/Object_115 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_118/Object_116 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_119/Object_117 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_120/Object_118 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_121/Object_119 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_122/Object_120 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_123/Object_121 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_124/Object_122 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_125/Object_123 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_126/Object_124 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_127/Object_125 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_128/Object_126 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_129/Object_127 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_130/Object_128 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_131/Object_129 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_132/Object_130 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_133/Object_131 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_134/Object_132 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_135/Object_133 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_136/Object_134 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_137/Object_135 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_138/Object_136 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_139/Object_137 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_140/Object_138 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_141/Object_139 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_142/Object_140 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_143/Object_141 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_144/Object_142 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_145/Object_143 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_146/Object_144 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_147/Object_145 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_148/Object_146 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_149/Object_147 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_150/Object_148 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_151/Object_149 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_152/Object_150 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_153/Object_151 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_154/Object_152 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_155/Object_153 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_156/Object_154 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_157/Object_155 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_158/Object_156 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_159/Object_157 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_160/Object_158 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_161/Object_159 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_162/Object_160 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_163/Object_161 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_164/Object_162 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_165/Object_163 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_166/Object_164 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_167/Object_165 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_168/Object_166 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_169/Object_167 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_170/Object_168 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_171/Object_169 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_172/Object_170 -> 未绑定

---

### '/World/agv_4' (Xform)

* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/AGV_ready_1/AGV_ready_1.usdc
* BBox (world): size=(1.457, 0.340, 0.669), center=(2.098, 0.714, 0.059)
* 几何统计: Mesh=171, Vertices=1634024, Faces=683203
* 子Mesh材质: /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_2/Object_0 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_3/Object_1 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_4/Object_2 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_5/Object_3 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_6/Object_4 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_7/Object_5 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_8/Object_6 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_9/Object_7 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_10/Object_8 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_11/Object_9 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_12/Object_10 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_13/Object_11 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_14/Object_12 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_15/Object_13 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_16/Object_14 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_17/Object_15 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_18/Object_16 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_19/Object_17 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_20/Object_18 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_21/Object_19 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_22/Object_20 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_23/Object_21 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_24/Object_22 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_25/Object_23 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_26/Object_24 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_27/Object_25 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_28/Object_26 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_29/Object_27 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_30/Object_28 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_31/Object_29 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_32/Object_30 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_33/Object_31 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_34/Object_32 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_35/Object_33 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_36/Object_34 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_37/Object_35 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_38/Object_36 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_39/Object_37 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_40/Object_38 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_41/Object_39 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_42/Object_40 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_43/Object_41 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_44/Object_42 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_45/Object_43 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_46/Object_44 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_47/Object_45 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_48/Object_46 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_49/Object_47 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_50/Object_48 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_51/Object_49 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_52/Object_50 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_53/Object_51 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_54/Object_52 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_55/Object_53 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_56/Object_54 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_57/Object_55 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_58/Object_56 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_59/Object_57 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_60/Object_58 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_61/Object_59 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_62/Object_60 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_63/Object_61 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_64/Object_62 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_65/Object_63 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_66/Object_64 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_67/Object_65 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_68/Object_66 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_69/Object_67 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_70/Object_68 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_71/Object_69 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_72/Object_70 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_73/Object_71 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_74/Object_72 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_75/Object_73 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_76/Object_74 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_77/Object_75 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_78/Object_76 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_79/Object_77 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_80/Object_78 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_81/Object_79 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_82/Object_80 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_83/Object_81 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_84/Object_82 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_85/Object_83 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_86/Object_84 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_87/Object_85 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_88/Object_86 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_89/Object_87 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_90/Object_88 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_91/Object_89 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_92/Object_90 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_93/Object_91 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_94/Object_92 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_95/Object_93 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_96/Object_94 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_97/Object_95 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_98/Object_96 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_99/Object_97 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_100/Object_98 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_101/Object_99 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_102/Object_100 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_103/Object_101 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_104/Object_102 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_105/Object_103 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_106/Object_104 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_107/Object_105 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_108/Object_106 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_109/Object_107 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_110/Object_108 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_111/Object_109 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_112/Object_110 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_113/Object_111 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_114/Object_112 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_115/Object_113 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_116/Object_114 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_117/Object_115 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_118/Object_116 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_119/Object_117 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_120/Object_118 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_121/Object_119 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_122/Object_120 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_123/Object_121 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_124/Object_122 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_125/Object_123 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_126/Object_124 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_127/Object_125 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_128/Object_126 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_129/Object_127 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_130/Object_128 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_131/Object_129 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_132/Object_130 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_133/Object_131 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_134/Object_132 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_135/Object_133 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_136/Object_134 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_137/Object_135 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_138/Object_136 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_139/Object_137 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_140/Object_138 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_141/Object_139 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_142/Object_140 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_143/Object_141 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_144/Object_142 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_145/Object_143 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_146/Object_144 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_147/Object_145 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_148/Object_146 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_149/Object_147 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_150/Object_148 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_151/Object_149 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_152/Object_150 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_153/Object_151 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_154/Object_152 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_155/Object_153 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_156/Object_154 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_157/Object_155 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_158/Object_156 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_159/Object_157 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_160/Object_158 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_161/Object_159 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_162/Object_160 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_163/Object_161 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_164/Object_162 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_165/Object_163 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_166/Object_164 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_167/Object_165 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_168/Object_166 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_169/Object_167 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_170/Object_168 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_171/Object_169 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_172/Object_170 -> 未绑定

---

### '/World/agv_5' (Xform)

* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/AGV_ready_1/AGV_ready_1.usdc
* BBox (world): size=(1.457, 0.340, 0.669), center=(2.098, 5.714, 0.059)
* 几何统计: Mesh=171, Vertices=1634024, Faces=683203
* 子Mesh材质: /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_2/Object_0 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_3/Object_1 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_4/Object_2 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_5/Object_3 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_6/Object_4 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_7/Object_5 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_8/Object_6 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_9/Object_7 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_10/Object_8 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_11/Object_9 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_12/Object_10 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_13/Object_11 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_14/Object_12 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_15/Object_13 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_16/Object_14 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_17/Object_15 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_18/Object_16 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_19/Object_17 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_20/Object_18 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_21/Object_19 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_22/Object_20 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_23/Object_21 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_24/Object_22 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_25/Object_23 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_26/Object_24 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_27/Object_25 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_28/Object_26 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_29/Object_27 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_30/Object_28 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_31/Object_29 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_32/Object_30 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_33/Object_31 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_34/Object_32 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_35/Object_33 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_36/Object_34 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_37/Object_35 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_38/Object_36 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_39/Object_37 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_40/Object_38 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_41/Object_39 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_42/Object_40 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_43/Object_41 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_44/Object_42 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_45/Object_43 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_46/Object_44 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_47/Object_45 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_48/Object_46 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_49/Object_47 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_50/Object_48 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_51/Object_49 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_52/Object_50 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_53/Object_51 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_54/Object_52 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_55/Object_53 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_56/Object_54 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_57/Object_55 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_58/Object_56 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_59/Object_57 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_60/Object_58 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_61/Object_59 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_62/Object_60 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_63/Object_61 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_64/Object_62 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_65/Object_63 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_66/Object_64 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_67/Object_65 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_68/Object_66 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_69/Object_67 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_70/Object_68 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_71/Object_69 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_72/Object_70 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_73/Object_71 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_74/Object_72 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_75/Object_73 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_76/Object_74 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_77/Object_75 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_78/Object_76 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_79/Object_77 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_80/Object_78 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_81/Object_79 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_82/Object_80 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_83/Object_81 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_84/Object_82 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_85/Object_83 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_86/Object_84 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_87/Object_85 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_88/Object_86 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_89/Object_87 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_90/Object_88 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_91/Object_89 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_92/Object_90 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_93/Object_91 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_94/Object_92 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_95/Object_93 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_96/Object_94 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_97/Object_95 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_98/Object_96 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_99/Object_97 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_100/Object_98 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_101/Object_99 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_102/Object_100 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_103/Object_101 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_104/Object_102 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_105/Object_103 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_106/Object_104 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_107/Object_105 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_108/Object_106 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_109/Object_107 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_110/Object_108 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_111/Object_109 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_112/Object_110 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_113/Object_111 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_114/Object_112 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_115/Object_113 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_116/Object_114 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_117/Object_115 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_118/Object_116 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_119/Object_117 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_120/Object_118 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_121/Object_119 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_122/Object_120 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_123/Object_121 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_124/Object_122 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_125/Object_123 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_126/Object_124 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_127/Object_125 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_128/Object_126 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_129/Object_127 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_130/Object_128 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_131/Object_129 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_132/Object_130 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_133/Object_131 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_134/Object_132 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_135/Object_133 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_136/Object_134 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_137/Object_135 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_138/Object_136 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_139/Object_137 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_140/Object_138 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_141/Object_139 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_142/Object_140 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_143/Object_141 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_144/Object_142 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_145/Object_143 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_146/Object_144 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_147/Object_145 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_148/Object_146 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_149/Object_147 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_150/Object_148 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_151/Object_149 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_152/Object_150 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_153/Object_151 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_154/Object_152 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_155/Object_153 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_156/Object_154 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_157/Object_155 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_158/Object_156 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_159/Object_157 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_160/Object_158 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_161/Object_159 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_162/Object_160 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_163/Object_161 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_164/Object_162 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_165/Object_163 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_166/Object_164 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_167/Object_165 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_168/Object_166 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_169/Object_167 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_170/Object_168 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_171/Object_169 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_172/Object_170 -> 未绑定

---

### '/World/agv_6' (Xform)

* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/AGV_ready_1/AGV_ready_1.usdc
* BBox (world): size=(1.457, 0.340, 0.669), center=(2.098, 10.714, 0.059)
* 几何统计: Mesh=171, Vertices=1634024, Faces=683203
* 子Mesh材质: /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_2/Object_0 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_3/Object_1 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_4/Object_2 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_5/Object_3 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_6/Object_4 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_7/Object_5 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_8/Object_6 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_9/Object_7 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_10/Object_8 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_11/Object_9 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_12/Object_10 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_13/Object_11 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_14/Object_12 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_15/Object_13 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_16/Object_14 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_17/Object_15 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_18/Object_16 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_19/Object_17 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_20/Object_18 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_21/Object_19 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_22/Object_20 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_23/Object_21 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_24/Object_22 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_25/Object_23 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_26/Object_24 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_27/Object_25 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_28/Object_26 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_29/Object_27 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_30/Object_28 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_31/Object_29 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_32/Object_30 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_33/Object_31 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_34/Object_32 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_35/Object_33 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_36/Object_34 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_37/Object_35 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_38/Object_36 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_39/Object_37 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_40/Object_38 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_41/Object_39 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_42/Object_40 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_43/Object_41 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_44/Object_42 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_45/Object_43 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_46/Object_44 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_47/Object_45 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_48/Object_46 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_49/Object_47 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_50/Object_48 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_51/Object_49 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_52/Object_50 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_53/Object_51 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_54/Object_52 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_55/Object_53 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_56/Object_54 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_57/Object_55 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_58/Object_56 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_59/Object_57 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_60/Object_58 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_61/Object_59 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_62/Object_60 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_63/Object_61 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_64/Object_62 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_65/Object_63 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_66/Object_64 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_67/Object_65 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_68/Object_66 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_69/Object_67 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_70/Object_68 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_71/Object_69 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_72/Object_70 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_73/Object_71 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_74/Object_72 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_75/Object_73 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_76/Object_74 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_77/Object_75 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_78/Object_76 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_79/Object_77 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_80/Object_78 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_81/Object_79 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_82/Object_80 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_83/Object_81 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_84/Object_82 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_85/Object_83 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_86/Object_84 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_87/Object_85 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_88/Object_86 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_89/Object_87 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_90/Object_88 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_91/Object_89 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_92/Object_90 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_93/Object_91 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_94/Object_92 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_95/Object_93 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_96/Object_94 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_97/Object_95 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_98/Object_96 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_99/Object_97 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_100/Object_98 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_101/Object_99 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_102/Object_100 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_103/Object_101 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_104/Object_102 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_105/Object_103 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_106/Object_104 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_107/Object_105 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_108/Object_106 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_109/Object_107 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_110/Object_108 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_111/Object_109 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_112/Object_110 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_113/Object_111 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_114/Object_112 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_115/Object_113 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_116/Object_114 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_117/Object_115 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_118/Object_116 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_119/Object_117 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_120/Object_118 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_121/Object_119 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_122/Object_120 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_123/Object_121 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_124/Object_122 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_125/Object_123 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_126/Object_124 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_127/Object_125 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_128/Object_126 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_129/Object_127 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_130/Object_128 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_131/Object_129 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_132/Object_130 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_133/Object_131 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_134/Object_132 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_135/Object_133 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_136/Object_134 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_137/Object_135 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_138/Object_136 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_139/Object_137 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_140/Object_138 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_141/Object_139 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_142/Object_140 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_143/Object_141 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_144/Object_142 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_145/Object_143 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_146/Object_144 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_147/Object_145 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_148/Object_146 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_149/Object_147 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_150/Object_148 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_151/Object_149 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_152/Object_150 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_153/Object_151 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_154/Object_152 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_155/Object_153 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_156/Object_154 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_157/Object_155 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_158/Object_156 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_159/Object_157 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_160/Object_158 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_161/Object_159 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_162/Object_160 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_163/Object_161 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_164/Object_162 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_165/Object_163 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_166/Object_164 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_167/Object_165 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_168/Object_166 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_169/Object_167 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_170/Object_168 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_171/Object_169 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_172/Object_170 -> 未绑定

---

### '/World/StackedCarton_1' (Xform)

* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/Plastic_Crate(1)/Plastic_Crate.usdc
* BBox (world): size=(0.424, 0.365, 0.421), center=(2.093, -14.473, 0.404)
* 几何统计: Mesh=1, Vertices=490, Faces=528
* 子Mesh材质: /World/StackedCarton_1/Meshes/Sketchfab_model/Plastic_Crate_FBX/RootNode/Box003/Object_4/Box003_Material__1_0/Box003_Material__1_0 -> 未绑定

---

### '/World/StackedCarton_2' (Xform)

* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/Plastic_Crate(1)/Plastic_Crate.usdc
* BBox (world): size=(0.424, 0.365, 0.421), center=(2.093, -9.473, 0.404)
* 几何统计: Mesh=1, Vertices=490, Faces=528
* 子Mesh材质: /World/StackedCarton_2/Meshes/Sketchfab_model/Plastic_Crate_FBX/RootNode/Box003/Object_4/Box003_Material__1_0/Box003_Material__1_0 -> 未绑定

---

### '/World/StackedCarton_3' (Xform)

* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/Plastic_Crate(1)/Plastic_Crate.usdc
* BBox (world): size=(0.424, 0.365, 0.421), center=(2.093, -4.473, 0.404)
* 几何统计: Mesh=1, Vertices=490, Faces=528
* 子Mesh材质: /World/StackedCarton_3/Meshes/Sketchfab_model/Plastic_Crate_FBX/RootNode/Box003/Object_4/Box003_Material__1_0/Box003_Material__1_0 -> 未绑定

---

### '/World/StackedCarton_4' (Xform)

* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/Plastic_Crate(1)/Plastic_Crate.usdc
* BBox (world): size=(0.424, 0.365, 0.421), center=(2.093, 0.527, 0.404)
* 几何统计: Mesh=1, Vertices=490, Faces=528
* 子Mesh材质: /World/StackedCarton_4/Meshes/Sketchfab_model/Plastic_Crate_FBX/RootNode/Box003/Object_4/Box003_Material__1_0/Box003_Material__1_0 -> 未绑定

---

### '/World/StackedCarton_5' (Xform)

* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/Plastic_Crate(1)/Plastic_Crate.usdc
* BBox (world): size=(0.424, 0.365, 0.421), center=(2.093, 5.527, 0.404)
* 几何统计: Mesh=1, Vertices=490, Faces=528
* 子Mesh材质: /World/StackedCarton_5/Meshes/Sketchfab_model/Plastic_Crate_FBX/RootNode/Box003/Object_4/Box003_Material__1_0/Box003_Material__1_0 -> 未绑定

---

### '/World/StackedCarton_6' (Xform)

* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/Plastic_Crate(1)/Plastic_Crate.usdc
* BBox (world): size=(0.424, 0.365, 0.421), center=(2.093, 10.527, 0.404)
* 几何统计: Mesh=1, Vertices=490, Faces=528
* 子Mesh材质: /World/StackedCarton_6/Meshes/Sketchfab_model/Plastic_Crate_FBX/RootNode/Box003/Object_4/Box003_Material__1_0/Box003_Material__1_0 -> 未绑定

---

### '/World/Workbench_02' (Xform)

* 引用: reference:file:/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/5.0/NVIDIA/Assets/DigitalTwin/Assets/Warehouse/Furnishing/Workbenches/MetalWorktable_A/MetalWorktable_A12_01.usd
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(0.000, 0.000, 0.000)
* 几何统计: Mesh=0, Vertices=0, Faces=0

---

### '/World/Workbench_03' (Xform)

* 引用: reference:file:/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/5.0/NVIDIA/Assets/DigitalTwin/Assets/Warehouse/Furnishing/Workbenches/MetalWorktable_A/MetalWorktable_A12_01.usd
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(0.000, 0.000, 0.000)
* 几何统计: Mesh=0, Vertices=0, Faces=0

---

### '/World/Workbench_04' (Xform)

* 引用: reference:file:/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/5.0/NVIDIA/Assets/DigitalTwin/Assets/Warehouse/Furnishing/Workbenches/MetalWorktable_A/MetalWorktable_A12_01.usd
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(0.000, 0.000, 0.000)
* 几何统计: Mesh=0, Vertices=0, Faces=0

---

### '/World/Workbench_05' (Xform)

* 引用: reference:file:/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/5.0/NVIDIA/Assets/DigitalTwin/Assets/Warehouse/Furnishing/Workbenches/MetalWorktable_A/MetalWorktable_A12_01.usd
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(0.000, 0.000, 0.000)
* 几何统计: Mesh=0, Vertices=0, Faces=0

---

### '/World/Workbench_06' (Xform)

* 引用: reference:file:/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/5.0/NVIDIA/Assets/DigitalTwin/Assets/Warehouse/Furnishing/Workbenches/MetalWorktable_A/MetalWorktable_A12_01.usd
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(0.000, 0.000, 0.000)
* 几何统计: Mesh=0, Vertices=0, Faces=0

---

### '/World/Workbench_07' (Xform)

* 引用: reference:file:/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/5.0/NVIDIA/Assets/DigitalTwin/Assets/Warehouse/Furnishing/Workbenches/MetalWorktable_A/MetalWorktable_A12_01.usd
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(0.000, 0.000, 0.000)
* 几何统计: Mesh=0, Vertices=0, Faces=0

---

### '/World/Workbench_08' (Xform)

* 引用: reference:file:/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/5.0/NVIDIA/Assets/DigitalTwin/Assets/Warehouse/Furnishing/Workbenches/MetalWorktable_A/MetalWorktable_A12_01.usd
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(0.000, 0.000, 0.000)
* 几何统计: Mesh=0, Vertices=0, Faces=0

---

### '/World/Workbench_09' (Xform)

* 引用: reference:file:/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/5.0/NVIDIA/Assets/DigitalTwin/Assets/Warehouse/Furnishing/Workbenches/MetalWorktable_A/MetalWorktable_A12_01.usd
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(0.000, 0.000, 0.000)
* 几何统计: Mesh=0, Vertices=0, Faces=0

---

### '/World/Workbench_10' (Xform)

* 引用: reference:file:/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/5.0/NVIDIA/Assets/DigitalTwin/Assets/Warehouse/Furnishing/Workbenches/MetalWorktable_A/MetalWorktable_A12_01.usd
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(0.000, 0.000, 0.000)
* 几何统计: Mesh=0, Vertices=0, Faces=0

---

### '/World/Workbench_11' (Xform)

* 引用: reference:file:/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/5.0/NVIDIA/Assets/DigitalTwin/Assets/Warehouse/Furnishing/Workbenches/MetalWorktable_A/MetalWorktable_A12_01.usd
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(0.000, 0.000, 0.000)
* 几何统计: Mesh=0, Vertices=0, Faces=0

---

### '/World/Workbench_12' (Xform)

* 引用: reference:file:/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/5.0/NVIDIA/Assets/DigitalTwin/Assets/Warehouse/Furnishing/Workbenches/MetalWorktable_A/MetalWorktable_A12_01.usd
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(0.000, 0.000, 0.000)
* 几何统计: Mesh=0, Vertices=0, Faces=0

---

### '/World/Workbench_13' (Xform)

* 引用: reference:file:/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/5.0/NVIDIA/Assets/DigitalTwin/Assets/Warehouse/Furnishing/Workbenches/MetalWorktable_A/MetalWorktable_A12_01.usd
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(0.000, 0.000, 0.000)
* 几何统计: Mesh=0, Vertices=0, Faces=0

---

### '/World/Workbench_14' (Xform)

* 引用: reference:file:/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/5.0/NVIDIA/Assets/DigitalTwin/Assets/Warehouse/Furnishing/Workbenches/MetalWorktable_A/MetalWorktable_A12_01.usd
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(0.000, 0.000, 0.000)
* 几何统计: Mesh=0, Vertices=0, Faces=0

---

### '/World/Workbench_15' (Xform)

* 引用: reference:file:/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/5.0/NVIDIA/Assets/DigitalTwin/Assets/Warehouse/Furnishing/Workbenches/MetalWorktable_A/MetalWorktable_A12_01.usd
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(0.000, 0.000, 0.000)
* 几何统计: Mesh=0, Vertices=0, Faces=0

---

### '/World/Black_Honey___Robotic_Arm' (Xform)

* 引用: payload:../device_data/usdz/IndustrialRobot/Black_Honey_-_Robotic_Arm.usdz
* BBox (world): size=(80.801, 227.335, 36.268), center=(-0.800, -15.705, 1.863)
* 几何统计: Mesh=64, Vertices=57172, Faces=72957
* 子Mesh材质: /World/Black_Honey___Robotic_Arm/Meshes/Sketchfab_model/root/GLTF_SceneRootNode/roboarm_001_low_0/Object_4/Object_0 -> 未绑定, /World/Black_Honey___Robotic_Arm/Meshes/Sketchfab_model/root/GLTF_SceneRootNode/roboarm_002_low_1/Object_6/Object_1 -> 未绑定, /World/Black_Honey___Robotic_Arm/Meshes/Sketchfab_model/root/GLTF_SceneRootNode/roboarm_003_low_2/Object_8/Object_2 -> 未绑定, /World/Black_Honey___Robotic_Arm/Meshes/Sketchfab_model/root/GLTF_SceneRootNode/roboarm_004_low_3/Object_10/Object_3 -> 未绑定, /World/Black_Honey___Robotic_Arm/Meshes/Sketchfab_model/root/GLTF_SceneRootNode/roboarm_005_low_4/Object_12/Object_4 -> 未绑定, /World/Black_Honey___Robotic_Arm/Meshes/Sketchfab_model/root/GLTF_SceneRootNode/roboarm_006_low_5/Object_14/Object_5 -> 未绑定, /World/Black_Honey___Robotic_Arm/Meshes/Sketchfab_model/root/GLTF_SceneRootNode/roboarm_007_low_6/Object_16/Object_6 -> 未绑定, /World/Black_Honey___Robotic_Arm/Meshes/Sketchfab_model/root/GLTF_SceneRootNode/roboarm_008_low_7/Object_18/Object_7 -> 未绑定, /World/Black_Honey___Robotic_Arm/Meshes/Sketchfab_model/root/GLTF_SceneRootNode/roboarm_009_low_8/Object_20/Object_8 -> 未绑定, /World/Black_Honey___Robotic_Arm/Meshes/Sketchfab_model/root/GLTF_SceneRootNode/roboarm_010_low_9/Object_22/Object_9 -> 未绑定, /World/Black_Honey___Robotic_Arm/Meshes/Sketchfab_model/root/GLTF_SceneRootNode/roboarm_011_low_10/Object_24/Object_10 -> 未绑定, /World/Black_Honey___Robotic_Arm/Meshes/Sketchfab_model/root/GLTF_SceneRootNode/roboarm_012_low_11/Object_26/Object_11 -> 未绑定, /World/Black_Honey___Robotic_Arm/Meshes/Sketchfab_model/root/GLTF_SceneRootNode/roboarm_013_low_12/Object_28/Object_12 -> 未绑定, /World/Black_Honey___Robotic_Arm/Meshes/Sketchfab_model/root/GLTF_SceneRootNode/roboarm_014_low_13/Object_30/Object_13 -> 未绑定, /World/Black_Honey___Robotic_Arm/Meshes/Sketchfab_model/root/GLTF_SceneRootNode/roboarm_015_low_14/Object_32/Object_14 -> 未绑定, /World/Black_Honey___Robotic_Arm/Meshes/Sketchfab_model/root/GLTF_SceneRootNode/roboarm_016_low_15/Object_34/Object_15 -> 未绑定, /World/Black_Honey___Robotic_Arm/Meshes/Sketchfab_model/root/GLTF_SceneRootNode/roboarm_017_low_16/Object_36/Object_16 -> 未绑定, /World/Black_Honey___Robotic_Arm/Meshes/Sketchfab_model/root/GLTF_SceneRootNode/roboarm_018_low_17/Object_38/Object_17 -> 未绑定, /World/Black_Honey___Robotic_Arm/Meshes/Sketchfab_model/root/GLTF_SceneRootNode/roboarm_019_low_18/Object_40/Object_18 -> 未绑定, /World/Black_Honey___Robotic_Arm/Meshes/Sketchfab_model/root/GLTF_SceneRootNode/roboarm_020_low_19/Object_42/Object_19 -> 未绑定, /World/Black_Honey___Robotic_Arm/Meshes/Sketchfab_model/root/GLTF_SceneRootNode/roboarm_021_low_20/Object_44/Object_20 -> 未绑定, /World/Black_Honey___Robotic_Arm/Meshes/Sketchfab_model/root/GLTF_SceneRootNode/roboarm_022_low_21/Object_46/Object_21 -> 未绑定, /World/Black_Honey___Robotic_Arm/Meshes/Sketchfab_model/root/GLTF_SceneRootNode/roboarm_023_low_22/Object_48/Object_22 -> 未绑定, /World/Black_Honey___Robotic_Arm/Meshes/Sketchfab_model/root/GLTF_SceneRootNode/roboarm_024_low_23/Object_50/Object_23 -> 未绑定, /World/Black_Honey___Robotic_Arm/Meshes/Sketchfab_model/root/GLTF_SceneRootNode/roboarm_025_low_24/Object_52/Object_24 -> 未绑定, /World/Black_Honey___Robotic_Arm/Meshes/Sketchfab_model/root/GLTF_SceneRootNode/roboarm_026_low_25/Object_54/Object_25 -> 未绑定, /World/Black_Honey___Robotic_Arm/Meshes/Sketchfab_model/root/GLTF_SceneRootNode/roboarm_027_low_26/Object_56/Object_26 -> 未绑定, /World/Black_Honey___Robotic_Arm/Meshes/Sketchfab_model/root/GLTF_SceneRootNode/roboarm_028_low_27/Object_58/Object_27 -> 未绑定, /World/Black_Honey___Robotic_Arm/Meshes/Sketchfab_model/root/GLTF_SceneRootNode/roboarm_low_28/Object_60/Object_28 -> 未绑定, /World/Black_Honey___Robotic_Arm/Meshes/Sketchfab_model/root/GLTF_SceneRootNode/robot_base_010_low_29/Object_62/Object_29 -> 未绑定, /World/Black_Honey___Robotic_Arm/Meshes/Sketchfab_model/root/GLTF_SceneRootNode/robot_base_001_low_30/Object_64/Object_30 -> 未绑定, /World/Black_Honey___Robotic_Arm/Meshes/Sketchfab_model/root/GLTF_SceneRootNode/robot_base_002_low_31/Object_66/Object_31 -> 未绑定, /World/Black_Honey___Robotic_Arm/Meshes/Sketchfab_model/root/GLTF_SceneRootNode/robot_base_003_low_32/Object_68/Object_32 -> 未绑定, /World/Black_Honey___Robotic_Arm/Meshes/Sketchfab_model/root/GLTF_SceneRootNode/robot_base_004_low_33/Object_70/Object_33 -> 未绑定, /World/Black_Honey___Robotic_Arm/Meshes/Sketchfab_model/root/GLTF_SceneRootNode/robot_base_005_low_34/Object_72/Object_34 -> 未绑定, /World/Black_Honey___Robotic_Arm/Meshes/Sketchfab_model/root/GLTF_SceneRootNode/robot_base_006_low_35/Object_74/Object_35 -> 未绑定, /World/Black_Honey___Robotic_Arm/Meshes/Sketchfab_model/root/GLTF_SceneRootNode/robot_base_008_low_36/Object_76/Object_36 -> 未绑定, /World/Black_Honey___Robotic_Arm/Meshes/Sketchfab_model/root/GLTF_SceneRootNode/robot_base_009_low_37/Object_78/Object_37 -> 未绑定, /World/Black_Honey___Robotic_Arm/Meshes/Sketchfab_model/root/GLTF_SceneRootNode/robot_base_018_low_38/Object_80/Object_38 -> 未绑定, /World/Black_Honey___Robotic_Arm/Meshes/Sketchfab_model/root/GLTF_SceneRootNode/robot_base_011_low_39/Object_82/Object_39 -> 未绑定, /World/Black_Honey___Robotic_Arm/Meshes/Sketchfab_model/root/GLTF_SceneRootNode/robot_base_012_low_40/Object_84/Object_40 -> 未绑定, /World/Black_Honey___Robotic_Arm/Meshes/Sketchfab_model/root/GLTF_SceneRootNode/robot_base_013_low_41/Object_86/Object_41 -> 未绑定, /World/Black_Honey___Robotic_Arm/Meshes/Sketchfab_model/root/GLTF_SceneRootNode/robot_base_014_low_42/Object_88/Object_42 -> 未绑定, /World/Black_Honey___Robotic_Arm/Meshes/Sketchfab_model/root/GLTF_SceneRootNode/robot_base_015_low_43/Object_90/Object_43 -> 未绑定, /World/Black_Honey___Robotic_Arm/Meshes/Sketchfab_model/root/GLTF_SceneRootNode/robot_base_016_low_44/Object_92/Object_44 -> 未绑定, /World/Black_Honey___Robotic_Arm/Meshes/Sketchfab_model/root/GLTF_SceneRootNode/robot_base_017_low_45/Object_94/Object_45 -> 未绑定, /World/Black_Honey___Robotic_Arm/Meshes/Sketchfab_model/root/GLTF_SceneRootNode/robot_base_020_low_46/Object_96/Object_46 -> 未绑定, /World/Black_Honey___Robotic_Arm/Meshes/Sketchfab_model/root/GLTF_SceneRootNode/robot_base_019_low_47/Object_98/Object_47 -> 未绑定, /World/Black_Honey___Robotic_Arm/Meshes/Sketchfab_model/root/GLTF_SceneRootNode/robot_base_021_low_48/Object_100/Object_48 -> 未绑定, /World/Black_Honey___Robotic_Arm/Meshes/Sketchfab_model/root/GLTF_SceneRootNode/robot_base_022_low_49/Object_102/Object_49 -> 未绑定, /World/Black_Honey___Robotic_Arm/Meshes/Sketchfab_model/root/GLTF_SceneRootNode/robot_base_023_low_50/Object_104/Object_50 -> 未绑定, /World/Black_Honey___Robotic_Arm/Meshes/Sketchfab_model/root/GLTF_SceneRootNode/robot_base_low_51/Object_106/Object_51 -> 未绑定, /World/Black_Honey___Robotic_Arm/Meshes/Sketchfab_model/root/GLTF_SceneRootNode/robot_base_024_low_52/Object_108/Object_52 -> 未绑定, /World/Black_Honey___Robotic_Arm/Meshes/Sketchfab_model/root/GLTF_SceneRootNode/robot_base_025_low_53/Object_110/Object_53 -> 未绑定, /World/Black_Honey___Robotic_Arm/Meshes/Sketchfab_model/root/GLTF_SceneRootNode/robot_base_026_low_54/Object_112/Object_54 -> 未绑定, /World/Black_Honey___Robotic_Arm/Meshes/Sketchfab_model/root/GLTF_SceneRootNode/robot_base_027_low_55/Object_114/Object_55 -> 未绑定, /World/Black_Honey___Robotic_Arm/Meshes/Sketchfab_model/root/GLTF_SceneRootNode/robot_base_028_low_56/Object_116/Object_56 -> 未绑定, /World/Black_Honey___Robotic_Arm/Meshes/Sketchfab_model/root/GLTF_SceneRootNode/robot_base_029_low_57/Object_118/Object_57 -> 未绑定, /World/Black_Honey___Robotic_Arm/Meshes/Sketchfab_model/root/GLTF_SceneRootNode/robot_base_030_low_58/Object_120/Object_58 -> 未绑定, /World/Black_Honey___Robotic_Arm/Meshes/Sketchfab_model/root/GLTF_SceneRootNode/robot_base_031_low_59/Object_122/Object_59 -> 未绑定, /World/Black_Honey___Robotic_Arm/Meshes/Sketchfab_model/root/GLTF_SceneRootNode/robot_base_032_low_60/Object_124/Object_60 -> 未绑定, /World/Black_Honey___Robotic_Arm/Meshes/Sketchfab_model/root/GLTF_SceneRootNode/robot_base_007_low_61/Object_126/Object_61 -> 未绑定, /World/Black_Honey___Robotic_Arm/Meshes/Sketchfab_model/root/GLTF_SceneRootNode/robot_base_033_low_62/Object_128/Object_62 -> 未绑定, /World/Black_Honey___Robotic_Arm/Meshes/Sketchfab_model/root/GLTF_SceneRootNode/robot_base_035_low_63/Object_130/Object_63 -> 未绑定

---

### '/World/rs007l_onrobot_rg2' (Xform)

* 引用: payload:../device_data/usdz/IndustrialRobot/rs007l_onrobot_rg2.usdz
* BBox (world): size=(0.381, 0.319, 1.585), center=(0.691, -14.327, 1.632)
* 几何统计: Mesh=28, Vertices=383850, Faces=127950
* 子Mesh材质: /World/rs007l_onrobot_rg2/base_link/visuals -> /World/rs007l_onrobot_rg2/Looks/material_White, /World/rs007l_onrobot_rg2/base_link/collisions -> 未绑定, /World/rs007l_onrobot_rg2/link1/visuals -> /World/rs007l_onrobot_rg2/Looks/material_White, /World/rs007l_onrobot_rg2/link1/collisions -> 未绑定, /World/rs007l_onrobot_rg2/link2/visuals -> /World/rs007l_onrobot_rg2/Looks/material_White, /World/rs007l_onrobot_rg2/link2/collisions -> 未绑定, /World/rs007l_onrobot_rg2/link3/visuals -> /World/rs007l_onrobot_rg2/Looks/material_White, /World/rs007l_onrobot_rg2/link3/collisions -> 未绑定, /World/rs007l_onrobot_rg2/link4/visuals -> /World/rs007l_onrobot_rg2/Looks/material_White, /World/rs007l_onrobot_rg2/link4/collisions -> 未绑定, /World/rs007l_onrobot_rg2/link5/visuals -> /World/rs007l_onrobot_rg2/Looks/material_White, /World/rs007l_onrobot_rg2/link5/collisions -> 未绑定, /World/rs007l_onrobot_rg2/link6/visuals -> /World/rs007l_onrobot_rg2/Looks/material_Black, /World/rs007l_onrobot_rg2/link6/collisions -> 未绑定, /World/rs007l_onrobot_rg2/onrobot_rg2_base_link/visuals -> /World/rs007l_onrobot_rg2/Looks/material_CCCCCC, /World/rs007l_onrobot_rg2/onrobot_rg2_base_link/collisions -> 未绑定, /World/rs007l_onrobot_rg2/left_outer_knuckle/visuals -> /World/rs007l_onrobot_rg2/Looks/material_CCCCCC, /World/rs007l_onrobot_rg2/left_outer_knuckle/collisions -> 未绑定, /World/rs007l_onrobot_rg2/left_inner_finger/visuals -> /World/rs007l_onrobot_rg2/Looks/material_191919, /World/rs007l_onrobot_rg2/left_inner_finger/collisions -> 未绑定, /World/rs007l_onrobot_rg2/left_inner_knuckle/visuals -> /World/rs007l_onrobot_rg2/Looks/material_CCCCCC, /World/rs007l_onrobot_rg2/left_inner_knuckle/collisions -> 未绑定, /World/rs007l_onrobot_rg2/right_inner_knuckle/visuals -> /World/rs007l_onrobot_rg2/Looks/material_CCCCCC, /World/rs007l_onrobot_rg2/right_inner_knuckle/collisions -> 未绑定, /World/rs007l_onrobot_rg2/right_outer_knuckle/visuals -> /World/rs007l_onrobot_rg2/Looks/material_CCCCCC, /World/rs007l_onrobot_rg2/right_outer_knuckle/collisions -> 未绑定, /World/rs007l_onrobot_rg2/right_inner_finger/visuals -> /World/rs007l_onrobot_rg2/Looks/material_191919, /World/rs007l_onrobot_rg2/right_inner_finger/collisions -> 未绑定
* 材质摘要:
* /World/rs007l_onrobot_rg2/Looks/material_191919 -> Inputs: 'diffuse_color_constant=(0.100, 0.100, 0.100)'
* /World/rs007l_onrobot_rg2/Looks/material_Black -> Inputs: 'diffuse_color_constant=(0.000, 0.000, 0.000)'
* /World/rs007l_onrobot_rg2/Looks/material_CCCCCC -> Inputs: 'diffuse_color_constant=(0.800, 0.800, 0.800)'
* /World/rs007l_onrobot_rg2/Looks/material_White -> Inputs: 'diffuse_color_constant=(1.000, 1.000, 1.000)'

---
