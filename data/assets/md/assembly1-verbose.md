# USDA场景描述文档:assembly1.usda

## 1.场景元数据(Scene Metadata)

* **USDA文件路径(USDA File Path):**`/media/simple/another_Documents/isaacsim_assets/scenedata/assembly1.usda`
* **默认Prim (Default Prim):**'Not Set'
* **单位与坐标系 (Units & Coordinate System):**

  * **米(Meters Per Unit):**1.0
  * **Up Axis:**Z
* **场景描述(Scene Describe):** 该工业车间模拟场景呈现出一种矩阵式、模块化且高度重复的现代化生产线布局，整体规划强调空间利用率与多工位并行的作业逻辑。车间地面为纯白色，不仅增强了视觉上的洁净感，也为自动化设备的传感器识别提供了良好的背景。从空间格局上看，整个区域被清晰地划分为两大功能带：纵向排布的物流输送区与横向延伸的机器人加工作业区。输送区由多条平行的蓝色高架输送线组成，这些输送线采用统一的钢性框架支撑，支腿呈淡蓝色，横梁上方安装有黑色橡胶材质的传送带，带面上正输送着大量形状规整的半圆弧形灰色工件。输送线的数量较多，呈等间距矩阵分布，形成了强大的物料流转网络。在输送线的侧翼，平行排列着一系列标准化的机器人作业单元。每个单元的核心是一组拼合式的黄色木质工作台，台面上方集成了一套双机协作系统：一台白色的轻型协作机器人与一台橙黑相间的六轴工业机器人共同部署在同一工作站内。这种“白+橙”的机器人配置出现了至少六组，它们呈直线矩阵排列，每一组都精准对接一条或多条输送线。机器人的机械臂末端安装有精密的抓取或焊接夹具，正处于对台面上散落的工件进行精细化操作的状态。工作台下方设有开放式的多层储物架，便于存放工序所需的零配件或周转工具。在机器人作业区与输送区之间的宽敞通道内，部署了多台黄色的自动导引运输车（AGV）。这些AGV底盘低矮，轮廓圆润，顶部载有一个半透明的周转箱，正按照预设的网格路径在各个机器人工作站之间灵活穿梭，执行零部件的补给或成品转运任务。AGV的数量与机器人工作站的数量相匹配，确保了整个系统在物流层面的高频响应。此外，车间背景处可见一排低矮的仓储式货架，采用深蓝色框架，可能用于原材料的暂存。从整体规划结构来看，该布局采用了典型的“分布式单元+集中式输送”的架构。每一组机器人工作站都是一个独立的加工细胞，而平行的蓝色输送线则构成了贯穿全场的生产大动脉。这种排布方式具有极强的可扩展性，可以根据产能需求灵活增减作业单元。设备间的相互关系极为明确：AGV负责点对点的柔性接驳，机器人负责工位内的精密操作，而输送线则负责跨区域的大规模流转。整个场景中没有冗余的控制柜露出，暗示所有设备可能通过地板下的布线或无线网络实现了高度集成的中央集群控制。
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

## 3. 对象详细描述 (Detailed Prim Descriptions)

### /World/Environment

* **Prim路径 (Prim Path):**/World/Environment
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/assets/Urban_Building.usdz'
* **世界包围盒 (World BBox):**
  * Size: '(1138.488, 300.000, 524.538)'
  * Center: '(-3.808, 2.648, 14.475)'

---

### /World/Workbench_1

* **Prim路径 (Prim Path):**/World/Workbench_1
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/5.0/NVIDIA/Assets/DigitalTwin/Assets/Warehouse/Furnishing/Workbenches/MetalWorktable_A/MetalWorktable_A12_01.usd'
* **世界包围盒 (World BBox):**
  * Size: '(200.000, 70.000, 84.000)'
  * Center: '(-0.000, -15.000, 0.420)'

---

### /World/Workbench_2

* **Prim路径 (Prim Path):**/World/Workbench_2
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/5.0/NVIDIA/Assets/DigitalTwin/Assets/Warehouse/Furnishing/Workbenches/MetalWorktable_A/MetalWorktable_A12_01.usd'
* **世界包围盒 (World BBox):**
  * Size: '(200.000, 70.000, 84.000)'
  * Center: '(-0.000, -10.000, 0.420)'

---

### /World/Workbench_3

* **Prim路径 (Prim Path):**/World/Workbench_3
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/5.0/NVIDIA/Assets/DigitalTwin/Assets/Warehouse/Furnishing/Workbenches/MetalWorktable_A/MetalWorktable_A12_01.usd'
* **世界包围盒 (World BBox):**
  * Size: '(200.000, 70.000, 84.000)'
  * Center: '(-0.000, -5.000, 0.420)'

---

### /World/Workbench_4

* **Prim路径 (Prim Path):**/World/Workbench_4
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/5.0/NVIDIA/Assets/DigitalTwin/Assets/Warehouse/Furnishing/Workbenches/MetalWorktable_A/MetalWorktable_A12_01.usd'
* **世界包围盒 (World BBox):**
  * Size: '(200.000, 70.000, 84.000)'
  * Center: '(-0.000, -0.000, 0.420)'

---

### /World/Workbench_5

* **Prim路径 (Prim Path):**/World/Workbench_5
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/5.0/NVIDIA/Assets/DigitalTwin/Assets/Warehouse/Furnishing/Workbenches/MetalWorktable_A/MetalWorktable_A12_01.usd'
* **世界包围盒 (World BBox):**
  * Size: '(200.000, 70.000, 84.000)'
  * Center: '(-0.000, 5.000, 0.420)'

---

### /World/Workbench_6

* **Prim路径 (Prim Path):**/World/Workbench_6
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/5.0/NVIDIA/Assets/DigitalTwin/Assets/Warehouse/Furnishing/Workbenches/MetalWorktable_A/MetalWorktable_A12_01.usd'
* **世界包围盒 (World BBox):**
  * Size: '(200.000, 70.000, 84.000)'
  * Center: '(-0.000, 10.000, 0.420)'

---

### /World/Workbench_7

* **Prim路径 (Prim Path):**/World/Workbench_7
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/5.0/NVIDIA/Assets/DigitalTwin/Assets/Warehouse/Furnishing/Workbenches/MetalWorktable_A/MetalWorktable_A12_01.usd'
* **世界包围盒 (World BBox):**
  * Size: '(200.000, 70.000, 84.000)'
  * Center: '(-0.000, 15.000, 0.420)'

---

### /World/Conveyor_1

* **Prim路径 (Prim Path):**/World/Conveyor_1
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/ConveyorBelt_A09.usd'
* **世界包围盒 (World BBox):**
  * Size: '(4.003, 1.177, 2.311)'
  * Center: '(-3.001, -15.013, 1.155)'

---

### /World/Conveyor_2

* **Prim路径 (Prim Path):**/World/Conveyor_2
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/ConveyorBelt_A09.usd'
* **世界包围盒 (World BBox):**
  * Size: '(4.003, 1.177, 2.311)'
  * Center: '(-7.013, -15.013, 1.155)'

---

### /World/Conveyor_3

* **Prim路径 (Prim Path):**/World/Conveyor_3
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/ConveyorBelt_A09.usd'
* **世界包围盒 (World BBox):**
  * Size: '(4.003, 1.177, 2.311)'
  * Center: '(-11.025, -15.013, 1.155)'

---

### /World/Conveyor_4

* **Prim路径 (Prim Path):**/World/Conveyor_4
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/ConveyorBelt_A09.usd'
* **世界包围盒 (World BBox):**
  * Size: '(4.003, 1.177, 2.311)'
  * Center: '(-15.037, -15.013, 1.155)'

---

### /World/Conveyor_5

* **Prim路径 (Prim Path):**/World/Conveyor_5
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/ConveyorBelt_A09.usd'
* **世界包围盒 (World BBox):**
  * Size: '(4.003, 1.177, 2.311)'
  * Center: '(-3.001, -10.013, 1.155)'

---

### /World/Conveyor_6

* **Prim路径 (Prim Path):**/World/Conveyor_6
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/ConveyorBelt_A09.usd'
* **世界包围盒 (World BBox):**
  * Size: '(4.003, 1.177, 2.311)'
  * Center: '(-7.013, -10.013, 1.155)'

---

### /World/Conveyor_7

* **Prim路径 (Prim Path):**/World/Conveyor_7
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/ConveyorBelt_A09.usd'
* **世界包围盒 (World BBox):**
  * Size: '(4.003, 1.177, 2.311)'
  * Center: '(-11.025, -10.013, 1.155)'

---

### /World/Conveyor_8

* **Prim路径 (Prim Path):**/World/Conveyor_8
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/ConveyorBelt_A09.usd'
* **世界包围盒 (World BBox):**
  * Size: '(4.003, 1.177, 2.311)'
  * Center: '(-15.037, -10.013, 1.155)'

---

### /World/Conveyor_9

* **Prim路径 (Prim Path):**/World/Conveyor_9
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/ConveyorBelt_A09.usd'
* **世界包围盒 (World BBox):**
  * Size: '(4.003, 1.177, 2.311)'
  * Center: '(-3.001, -5.013, 1.155)'

---

### /World/Conveyor_10

* **Prim路径 (Prim Path):**/World/Conveyor_10
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/ConveyorBelt_A09.usd'
* **世界包围盒 (World BBox):**
  * Size: '(4.003, 1.177, 2.311)'
  * Center: '(-7.013, -5.013, 1.155)'

---

### /World/Conveyor_11

* **Prim路径 (Prim Path):**/World/Conveyor_11
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/ConveyorBelt_A09.usd'
* **世界包围盒 (World BBox):**
  * Size: '(4.003, 1.177, 2.311)'
  * Center: '(-11.025, -5.013, 1.155)'

---

### /World/Conveyor_12

* **Prim路径 (Prim Path):**/World/Conveyor_12
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/ConveyorBelt_A09.usd'
* **世界包围盒 (World BBox):**
  * Size: '(4.003, 1.177, 2.311)'
  * Center: '(-15.037, -5.013, 1.155)'

---

### /World/Conveyor_13

* **Prim路径 (Prim Path):**/World/Conveyor_13
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/ConveyorBelt_A09.usd'
* **世界包围盒 (World BBox):**
  * Size: '(4.003, 1.177, 2.311)'
  * Center: '(-3.001, -0.013, 1.155)'

---

### /World/Conveyor_14

* **Prim路径 (Prim Path):**/World/Conveyor_14
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/ConveyorBelt_A09.usd'
* **世界包围盒 (World BBox):**
  * Size: '(4.003, 1.177, 2.311)'
  * Center: '(-7.013, -0.013, 1.155)'

---

### /World/Conveyor_15

* **Prim路径 (Prim Path):**/World/Conveyor_15
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/ConveyorBelt_A09.usd'
* **世界包围盒 (World BBox):**
  * Size: '(4.003, 1.177, 2.311)'
  * Center: '(-11.025, -0.013, 1.155)'

---

### /World/Conveyor_16

* **Prim路径 (Prim Path):**/World/Conveyor_16
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/ConveyorBelt_A09.usd'
* **世界包围盒 (World BBox):**
  * Size: '(4.003, 1.177, 2.311)'
  * Center: '(-15.037, -0.013, 1.155)'

---

### /World/Conveyor_17

* **Prim路径 (Prim Path):**/World/Conveyor_17
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/ConveyorBelt_A09.usd'
* **世界包围盒 (World BBox):**
  * Size: '(4.003, 1.177, 2.311)'
  * Center: '(-3.001, 4.987, 1.155)'

---

### /World/Conveyor_18

* **Prim路径 (Prim Path):**/World/Conveyor_18
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/ConveyorBelt_A09.usd'
* **世界包围盒 (World BBox):**
  * Size: '(4.003, 1.177, 2.311)'
  * Center: '(-7.013, 4.987, 1.155)'

---

### /World/Conveyor_19

* **Prim路径 (Prim Path):**/World/Conveyor_19
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/ConveyorBelt_A09.usd'
* **世界包围盒 (World BBox):**
  * Size: '(4.003, 1.177, 2.311)'
  * Center: '(-11.025, 4.987, 1.155)'

---

### /World/Conveyor_20

* **Prim路径 (Prim Path):**/World/Conveyor_20
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/ConveyorBelt_A09.usd'
* **世界包围盒 (World BBox):**
  * Size: '(4.003, 1.177, 2.311)'
  * Center: '(-15.037, 4.987, 1.155)'

---

### /World/Conveyor_21

* **Prim路径 (Prim Path):**/World/Conveyor_21
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/ConveyorBelt_A09.usd'
* **世界包围盒 (World BBox):**
  * Size: '(4.003, 1.177, 2.311)'
  * Center: '(-3.001, 9.987, 1.155)'

---

### /World/Conveyor_22

* **Prim路径 (Prim Path):**/World/Conveyor_22
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/ConveyorBelt_A09.usd'
* **世界包围盒 (World BBox):**
  * Size: '(4.003, 1.177, 2.311)'
  * Center: '(-7.013, 9.987, 1.155)'

---

### /World/Conveyor_23

* **Prim路径 (Prim Path):**/World/Conveyor_23
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/ConveyorBelt_A09.usd'
* **世界包围盒 (World BBox):**
  * Size: '(4.003, 1.177, 2.311)'
  * Center: '(-11.025, 9.987, 1.155)'

---

### /World/Conveyor_24

* **Prim路径 (Prim Path):**/World/Conveyor_24
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/ConveyorBelt_A09.usd'
* **世界包围盒 (World BBox):**
  * Size: '(4.003, 1.177, 2.311)'
  * Center: '(-15.037, 9.987, 1.155)'

---

### /World/Conveyor_25

* **Prim路径 (Prim Path):**/World/Conveyor_25
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/ConveyorBelt_A09.usd'
* **世界包围盒 (World BBox):**
  * Size: '(4.003, 1.177, 2.311)'
  * Center: '(-3.001, 14.987, 1.155)'

---

### /World/Conveyor_26

* **Prim路径 (Prim Path):**/World/Conveyor_26
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/ConveyorBelt_A09.usd'
* **世界包围盒 (World BBox):**
  * Size: '(4.003, 1.177, 2.311)'
  * Center: '(-7.013, 14.987, 1.155)'

---

### /World/Conveyor_27

* **Prim路径 (Prim Path):**/World/Conveyor_27
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/ConveyorBelt_A09.usd'
* **世界包围盒 (World BBox):**
  * Size: '(4.003, 1.177, 2.311)'
  * Center: '(-11.025, 14.987, 1.155)'

---

### /World/Conveyor_28

* **Prim路径 (Prim Path):**/World/Conveyor_28
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/ConveyorBelt_A09.usd'
* **世界包围盒 (World BBox):**
  * Size: '(4.003, 1.177, 2.311)'
  * Center: '(-15.037, 14.987, 1.155)'

---

### /World/PartA_OnBelt_1

* **Prim路径 (Prim Path):**/World/PartA_OnBelt_1
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ban_Yuan_Jian/Woodruff keys GB_converted/0;Size=1.0x1.4x4;SUPPRESSION=Default.usd'
* **世界包围盒 (World BBox):**
  * Size: '(3.816, 1.400, 1.000)'
  * Center: '(-1.400, -14.870, 1.830)'

---

### /World/PartA_OnBelt_2

* **Prim路径 (Prim Path):**/World/PartA_OnBelt_2
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ban_Yuan_Jian/Woodruff keys GB_converted/0;Size=1.0x1.4x4;SUPPRESSION=Default.usd'
* **世界包围盒 (World BBox):**
  * Size: '(3.816, 1.400, 1.000)'
  * Center: '(-3.200, -14.870, 1.830)'

---

### /World/PartA_OnBelt_3

* **Prim路径 (Prim Path):**/World/PartA_OnBelt_3
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ban_Yuan_Jian/Woodruff keys GB_converted/0;Size=1.0x1.4x4;SUPPRESSION=Default.usd'
* **世界包围盒 (World BBox):**
  * Size: '(3.816, 1.400, 1.000)'
  * Center: '(-5.000, -14.870, 1.830)'

---

### /World/PartA_OnBelt_4

* **Prim路径 (Prim Path):**/World/PartA_OnBelt_4
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ban_Yuan_Jian/Woodruff keys GB_converted/0;Size=1.0x1.4x4;SUPPRESSION=Default.usd'
* **世界包围盒 (World BBox):**
  * Size: '(3.816, 1.400, 1.000)'
  * Center: '(-6.800, -14.870, 1.830)'

---

### /World/PartA_OnBelt_5

* **Prim路径 (Prim Path):**/World/PartA_OnBelt_5
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ban_Yuan_Jian/Woodruff keys GB_converted/0;Size=1.0x1.4x4;SUPPRESSION=Default.usd'
* **世界包围盒 (World BBox):**
  * Size: '(3.816, 1.400, 1.000)'
  * Center: '(-8.600, -14.870, 1.830)'

---

### /World/PartA_OnBelt_6

* **Prim路径 (Prim Path):**/World/PartA_OnBelt_6
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ban_Yuan_Jian/Woodruff keys GB_converted/0;Size=1.0x1.4x4;SUPPRESSION=Default.usd'
* **世界包围盒 (World BBox):**
  * Size: '(3.816, 1.400, 1.000)'
  * Center: '(-10.400, -14.870, 1.830)'

---

### /World/PartA_OnBelt_7

* **Prim路径 (Prim Path):**/World/PartA_OnBelt_7
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ban_Yuan_Jian/Woodruff keys GB_converted/0;Size=1.0x1.4x4;SUPPRESSION=Default.usd'
* **世界包围盒 (World BBox):**
  * Size: '(3.816, 1.400, 1.000)'
  * Center: '(-12.200, -14.870, 1.830)'

---

### /World/PartA_OnBelt_8

* **Prim路径 (Prim Path):**/World/PartA_OnBelt_8
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ban_Yuan_Jian/Woodruff keys GB_converted/0;Size=1.0x1.4x4;SUPPRESSION=Default.usd'
* **世界包围盒 (World BBox):**
  * Size: '(3.816, 1.400, 1.000)'
  * Center: '(-14.000, -14.870, 1.830)'

---

### /World/PartA_OnBelt_9

* **Prim路径 (Prim Path):**/World/PartA_OnBelt_9
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ban_Yuan_Jian/Woodruff keys GB_converted/0;Size=1.0x1.4x4;SUPPRESSION=Default.usd'
* **世界包围盒 (World BBox):**
  * Size: '(3.816, 1.400, 1.000)'
  * Center: '(-15.800, -14.870, 1.830)'

---

### /World/PartA_OnBelt_10

* **Prim路径 (Prim Path):**/World/PartA_OnBelt_10
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ban_Yuan_Jian/Woodruff keys GB_converted/0;Size=1.0x1.4x4;SUPPRESSION=Default.usd'
* **世界包围盒 (World BBox):**
  * Size: '(3.816, 1.400, 1.000)'
  * Center: '(-1.400, -9.870, 1.830)'

---

### /World/PartA_OnBelt_11

* **Prim路径 (Prim Path):**/World/PartA_OnBelt_11
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ban_Yuan_Jian/Woodruff keys GB_converted/0;Size=1.0x1.4x4;SUPPRESSION=Default.usd'
* **世界包围盒 (World BBox):**
  * Size: '(3.816, 1.400, 1.000)'
  * Center: '(-3.200, -9.870, 1.830)'

---

### /World/PartA_OnBelt_12

* **Prim路径 (Prim Path):**/World/PartA_OnBelt_12
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ban_Yuan_Jian/Woodruff keys GB_converted/0;Size=1.0x1.4x4;SUPPRESSION=Default.usd'
* **世界包围盒 (World BBox):**
  * Size: '(3.816, 1.400, 1.000)'
  * Center: '(-5.000, -9.870, 1.830)'

---

### /World/PartA_OnBelt_13

* **Prim路径 (Prim Path):**/World/PartA_OnBelt_13
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ban_Yuan_Jian/Woodruff keys GB_converted/0;Size=1.0x1.4x4;SUPPRESSION=Default.usd'
* **世界包围盒 (World BBox):**
  * Size: '(3.816, 1.400, 1.000)'
  * Center: '(-6.800, -9.870, 1.830)'

---

### /World/PartA_OnBelt_14

* **Prim路径 (Prim Path):**/World/PartA_OnBelt_14
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ban_Yuan_Jian/Woodruff keys GB_converted/0;Size=1.0x1.4x4;SUPPRESSION=Default.usd'
* **世界包围盒 (World BBox):**
  * Size: '(3.816, 1.400, 1.000)'
  * Center: '(-8.600, -9.870, 1.830)'

---

### /World/PartA_OnBelt_15

* **Prim路径 (Prim Path):**/World/PartA_OnBelt_15
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ban_Yuan_Jian/Woodruff keys GB_converted/0;Size=1.0x1.4x4;SUPPRESSION=Default.usd'
* **世界包围盒 (World BBox):**
  * Size: '(3.816, 1.400, 1.000)'
  * Center: '(-10.400, -9.870, 1.830)'

---

### /World/PartA_OnBelt_16

* **Prim路径 (Prim Path):**/World/PartA_OnBelt_16
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ban_Yuan_Jian/Woodruff keys GB_converted/0;Size=1.0x1.4x4;SUPPRESSION=Default.usd'
* **世界包围盒 (World BBox):**
  * Size: '(3.816, 1.400, 1.000)'
  * Center: '(-12.200, -9.870, 1.830)'

---

### /World/PartA_OnBelt_17

* **Prim路径 (Prim Path):**/World/PartA_OnBelt_17
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ban_Yuan_Jian/Woodruff keys GB_converted/0;Size=1.0x1.4x4;SUPPRESSION=Default.usd'
* **世界包围盒 (World BBox):**
  * Size: '(3.816, 1.400, 1.000)'
  * Center: '(-14.000, -9.870, 1.830)'

---

### /World/PartA_OnBelt_18

* **Prim路径 (Prim Path):**/World/PartA_OnBelt_18
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ban_Yuan_Jian/Woodruff keys GB_converted/0;Size=1.0x1.4x4;SUPPRESSION=Default.usd'
* **世界包围盒 (World BBox):**
  * Size: '(3.816, 1.400, 1.000)'
  * Center: '(-15.800, -9.870, 1.830)'

---

### /World/PartA_OnBelt_19

* **Prim路径 (Prim Path):**/World/PartA_OnBelt_19
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ban_Yuan_Jian/Woodruff keys GB_converted/0;Size=1.0x1.4x4;SUPPRESSION=Default.usd'
* **世界包围盒 (World BBox):**
  * Size: '(3.816, 1.400, 1.000)'
  * Center: '(-1.400, -4.870, 1.830)'

---

### /World/PartA_OnBelt_20

* **Prim路径 (Prim Path):**/World/PartA_OnBelt_20
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ban_Yuan_Jian/Woodruff keys GB_converted/0;Size=1.0x1.4x4;SUPPRESSION=Default.usd'
* **世界包围盒 (World BBox):**
  * Size: '(3.816, 1.400, 1.000)'
  * Center: '(-3.200, -4.870, 1.830)'

---

### /World/PartA_OnBelt_21

* **Prim路径 (Prim Path):**/World/PartA_OnBelt_21
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ban_Yuan_Jian/Woodruff keys GB_converted/0;Size=1.0x1.4x4;SUPPRESSION=Default.usd'
* **世界包围盒 (World BBox):**
  * Size: '(3.816, 1.400, 1.000)'
  * Center: '(-5.000, -4.870, 1.830)'

---

### /World/PartA_OnBelt_22

* **Prim路径 (Prim Path):**/World/PartA_OnBelt_22
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ban_Yuan_Jian/Woodruff keys GB_converted/0;Size=1.0x1.4x4;SUPPRESSION=Default.usd'
* **世界包围盒 (World BBox):**
  * Size: '(3.816, 1.400, 1.000)'
  * Center: '(-6.800, -4.870, 1.830)'

---

### /World/PartA_OnBelt_23

* **Prim路径 (Prim Path):**/World/PartA_OnBelt_23
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ban_Yuan_Jian/Woodruff keys GB_converted/0;Size=1.0x1.4x4;SUPPRESSION=Default.usd'
* **世界包围盒 (World BBox):**
  * Size: '(3.816, 1.400, 1.000)'
  * Center: '(-8.600, -4.870, 1.830)'

---

### /World/PartA_OnBelt_24

* **Prim路径 (Prim Path):**/World/PartA_OnBelt_24
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ban_Yuan_Jian/Woodruff keys GB_converted/0;Size=1.0x1.4x4;SUPPRESSION=Default.usd'
* **世界包围盒 (World BBox):**
  * Size: '(3.816, 1.400, 1.000)'
  * Center: '(-10.400, -4.870, 1.830)'

---

### /World/PartA_OnBelt_25

* **Prim路径 (Prim Path):**/World/PartA_OnBelt_25
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ban_Yuan_Jian/Woodruff keys GB_converted/0;Size=1.0x1.4x4;SUPPRESSION=Default.usd'
* **世界包围盒 (World BBox):**
  * Size: '(3.816, 1.400, 1.000)'
  * Center: '(-12.200, -4.870, 1.830)'

---

### /World/PartA_OnBelt_26

* **Prim路径 (Prim Path):**/World/PartA_OnBelt_26
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ban_Yuan_Jian/Woodruff keys GB_converted/0;Size=1.0x1.4x4;SUPPRESSION=Default.usd'
* **世界包围盒 (World BBox):**
  * Size: '(3.816, 1.400, 1.000)'
  * Center: '(-14.000, -4.870, 1.830)'

---

### /World/PartA_OnBelt_27

* **Prim路径 (Prim Path):**/World/PartA_OnBelt_27
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ban_Yuan_Jian/Woodruff keys GB_converted/0;Size=1.0x1.4x4;SUPPRESSION=Default.usd'
* **世界包围盒 (World BBox):**
  * Size: '(3.816, 1.400, 1.000)'
  * Center: '(-15.800, -4.870, 1.830)'

---

### /World/PartA_OnBelt_28

* **Prim路径 (Prim Path):**/World/PartA_OnBelt_28
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ban_Yuan_Jian/Woodruff keys GB_converted/0;Size=1.0x1.4x4;SUPPRESSION=Default.usd'
* **世界包围盒 (World BBox):**
  * Size: '(3.816, 1.400, 1.000)'
  * Center: '(-1.400, 0.130, 1.830)'

---

### /World/PartA_OnBelt_29

* **Prim路径 (Prim Path):**/World/PartA_OnBelt_29
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ban_Yuan_Jian/Woodruff keys GB_converted/0;Size=1.0x1.4x4;SUPPRESSION=Default.usd'
* **世界包围盒 (World BBox):**
  * Size: '(3.816, 1.400, 1.000)'
  * Center: '(-3.200, 0.130, 1.830)'

---

### /World/PartA_OnBelt_30

* **Prim路径 (Prim Path):**/World/PartA_OnBelt_30
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ban_Yuan_Jian/Woodruff keys GB_converted/0;Size=1.0x1.4x4;SUPPRESSION=Default.usd'
* **世界包围盒 (World BBox):**
  * Size: '(3.816, 1.400, 1.000)'
  * Center: '(-5.000, 0.130, 1.830)'

---

### /World/PartA_OnBelt_31

* **Prim路径 (Prim Path):**/World/PartA_OnBelt_31
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ban_Yuan_Jian/Woodruff keys GB_converted/0;Size=1.0x1.4x4;SUPPRESSION=Default.usd'
* **世界包围盒 (World BBox):**
  * Size: '(3.816, 1.400, 1.000)'
  * Center: '(-6.800, 0.130, 1.830)'

---

### /World/PartA_OnBelt_32

* **Prim路径 (Prim Path):**/World/PartA_OnBelt_32
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ban_Yuan_Jian/Woodruff keys GB_converted/0;Size=1.0x1.4x4;SUPPRESSION=Default.usd'
* **世界包围盒 (World BBox):**
  * Size: '(3.816, 1.400, 1.000)'
  * Center: '(-8.600, 0.130, 1.830)'

---

### /World/PartA_OnBelt_33

* **Prim路径 (Prim Path):**/World/PartA_OnBelt_33
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ban_Yuan_Jian/Woodruff keys GB_converted/0;Size=1.0x1.4x4;SUPPRESSION=Default.usd'
* **世界包围盒 (World BBox):**
  * Size: '(3.816, 1.400, 1.000)'
  * Center: '(-10.400, 0.130, 1.830)'

---

### /World/PartA_OnBelt_34

* **Prim路径 (Prim Path):**/World/PartA_OnBelt_34
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ban_Yuan_Jian/Woodruff keys GB_converted/0;Size=1.0x1.4x4;SUPPRESSION=Default.usd'
* **世界包围盒 (World BBox):**
  * Size: '(3.816, 1.400, 1.000)'
  * Center: '(-12.200, 0.130, 1.830)'

---

### /World/PartA_OnBelt_35

* **Prim路径 (Prim Path):**/World/PartA_OnBelt_35
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ban_Yuan_Jian/Woodruff keys GB_converted/0;Size=1.0x1.4x4;SUPPRESSION=Default.usd'
* **世界包围盒 (World BBox):**
  * Size: '(3.816, 1.400, 1.000)'
  * Center: '(-14.000, 0.130, 1.830)'

---

### /World/PartA_OnBelt_36

* **Prim路径 (Prim Path):**/World/PartA_OnBelt_36
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ban_Yuan_Jian/Woodruff keys GB_converted/0;Size=1.0x1.4x4;SUPPRESSION=Default.usd'
* **世界包围盒 (World BBox):**
  * Size: '(3.816, 1.400, 1.000)'
  * Center: '(-15.800, 0.130, 1.830)'

---

### /World/PartA_OnBelt_37

* **Prim路径 (Prim Path):**/World/PartA_OnBelt_37
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ban_Yuan_Jian/Woodruff keys GB_converted/0;Size=1.0x1.4x4;SUPPRESSION=Default.usd'
* **世界包围盒 (World BBox):**
  * Size: '(3.816, 1.400, 1.000)'
  * Center: '(-1.400, 5.130, 1.830)'

---

### /World/PartA_OnBelt_38

* **Prim路径 (Prim Path):**/World/PartA_OnBelt_38
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ban_Yuan_Jian/Woodruff keys GB_converted/0;Size=1.0x1.4x4;SUPPRESSION=Default.usd'
* **世界包围盒 (World BBox):**
  * Size: '(3.816, 1.400, 1.000)'
  * Center: '(-3.200, 5.130, 1.830)'

---

### /World/PartA_OnBelt_39

* **Prim路径 (Prim Path):**/World/PartA_OnBelt_39
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ban_Yuan_Jian/Woodruff keys GB_converted/0;Size=1.0x1.4x4;SUPPRESSION=Default.usd'
* **世界包围盒 (World BBox):**
  * Size: '(3.816, 1.400, 1.000)'
  * Center: '(-5.000, 5.130, 1.830)'

---

### /World/PartA_OnBelt_40

* **Prim路径 (Prim Path):**/World/PartA_OnBelt_40
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ban_Yuan_Jian/Woodruff keys GB_converted/0;Size=1.0x1.4x4;SUPPRESSION=Default.usd'
* **世界包围盒 (World BBox):**
  * Size: '(3.816, 1.400, 1.000)'
  * Center: '(-6.800, 5.130, 1.830)'

---

### /World/PartA_OnBelt_41

* **Prim路径 (Prim Path):**/World/PartA_OnBelt_41
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ban_Yuan_Jian/Woodruff keys GB_converted/0;Size=1.0x1.4x4;SUPPRESSION=Default.usd'
* **世界包围盒 (World BBox):**
  * Size: '(3.816, 1.400, 1.000)'
  * Center: '(-8.600, 5.130, 1.830)'

---

### /World/PartA_OnBelt_42

* **Prim路径 (Prim Path):**/World/PartA_OnBelt_42
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ban_Yuan_Jian/Woodruff keys GB_converted/0;Size=1.0x1.4x4;SUPPRESSION=Default.usd'
* **世界包围盒 (World BBox):**
  * Size: '(3.816, 1.400, 1.000)'
  * Center: '(-10.400, 5.130, 1.830)'

---

### /World/PartA_OnBelt_43

* **Prim路径 (Prim Path):**/World/PartA_OnBelt_43
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ban_Yuan_Jian/Woodruff keys GB_converted/0;Size=1.0x1.4x4;SUPPRESSION=Default.usd'
* **世界包围盒 (World BBox):**
  * Size: '(3.816, 1.400, 1.000)'
  * Center: '(-12.200, 5.130, 1.830)'

---

### /World/PartA_OnBelt_44

* **Prim路径 (Prim Path):**/World/PartA_OnBelt_44
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ban_Yuan_Jian/Woodruff keys GB_converted/0;Size=1.0x1.4x4;SUPPRESSION=Default.usd'
* **世界包围盒 (World BBox):**
  * Size: '(3.816, 1.400, 1.000)'
  * Center: '(-14.000, 5.130, 1.830)'

---

### /World/PartA_OnBelt_45

* **Prim路径 (Prim Path):**/World/PartA_OnBelt_45
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ban_Yuan_Jian/Woodruff keys GB_converted/0;Size=1.0x1.4x4;SUPPRESSION=Default.usd'
* **世界包围盒 (World BBox):**
  * Size: '(3.816, 1.400, 1.000)'
  * Center: '(-15.800, 5.130, 1.830)'

---

### /World/PartA_OnBelt_46

* **Prim路径 (Prim Path):**/World/PartA_OnBelt_46
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ban_Yuan_Jian/Woodruff keys GB_converted/0;Size=1.0x1.4x4;SUPPRESSION=Default.usd'
* **世界包围盒 (World BBox):**
  * Size: '(3.816, 1.400, 1.000)'
  * Center: '(-1.400, 10.130, 1.830)'

---

### /World/PartA_OnBelt_47

* **Prim路径 (Prim Path):**/World/PartA_OnBelt_47
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ban_Yuan_Jian/Woodruff keys GB_converted/0;Size=1.0x1.4x4;SUPPRESSION=Default.usd'
* **世界包围盒 (World BBox):**
  * Size: '(3.816, 1.400, 1.000)'
  * Center: '(-3.200, 10.130, 1.830)'

---

### /World/PartA_OnBelt_48

* **Prim路径 (Prim Path):**/World/PartA_OnBelt_48
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ban_Yuan_Jian/Woodruff keys GB_converted/0;Size=1.0x1.4x4;SUPPRESSION=Default.usd'
* **世界包围盒 (World BBox):**
  * Size: '(3.816, 1.400, 1.000)'
  * Center: '(-5.000, 10.130, 1.830)'

---

### /World/PartA_OnBelt_49

* **Prim路径 (Prim Path):**/World/PartA_OnBelt_49
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ban_Yuan_Jian/Woodruff keys GB_converted/0;Size=1.0x1.4x4;SUPPRESSION=Default.usd'
* **世界包围盒 (World BBox):**
  * Size: '(3.816, 1.400, 1.000)'
  * Center: '(-6.800, 10.130, 1.830)'

---

### /World/PartA_OnBelt_50

* **Prim路径 (Prim Path):**/World/PartA_OnBelt_50
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ban_Yuan_Jian/Woodruff keys GB_converted/0;Size=1.0x1.4x4;SUPPRESSION=Default.usd'
* **世界包围盒 (World BBox):**
  * Size: '(3.816, 1.400, 1.000)'
  * Center: '(-8.600, 10.130, 1.830)'

---

### /World/PartA_OnBelt_51

* **Prim路径 (Prim Path):**/World/PartA_OnBelt_51
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ban_Yuan_Jian/Woodruff keys GB_converted/0;Size=1.0x1.4x4;SUPPRESSION=Default.usd'
* **世界包围盒 (World BBox):**
  * Size: '(3.816, 1.400, 1.000)'
  * Center: '(-10.400, 10.130, 1.830)'

---

### /World/PartA_OnBelt_52

* **Prim路径 (Prim Path):**/World/PartA_OnBelt_52
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ban_Yuan_Jian/Woodruff keys GB_converted/0;Size=1.0x1.4x4;SUPPRESSION=Default.usd'
* **世界包围盒 (World BBox):**
  * Size: '(3.816, 1.400, 1.000)'
  * Center: '(-12.200, 10.130, 1.830)'

---

### /World/PartA_OnBelt_53

* **Prim路径 (Prim Path):**/World/PartA_OnBelt_53
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ban_Yuan_Jian/Woodruff keys GB_converted/0;Size=1.0x1.4x4;SUPPRESSION=Default.usd'
* **世界包围盒 (World BBox):**
  * Size: '(3.816, 1.400, 1.000)'
  * Center: '(-14.000, 10.130, 1.830)'

---

### /World/PartA_OnBelt_54

* **Prim路径 (Prim Path):**/World/PartA_OnBelt_54
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ban_Yuan_Jian/Woodruff keys GB_converted/0;Size=1.0x1.4x4;SUPPRESSION=Default.usd'
* **世界包围盒 (World BBox):**
  * Size: '(3.816, 1.400, 1.000)'
  * Center: '(-15.800, 10.130, 1.830)'

---

### /World/PartA_OnBelt_55

* **Prim路径 (Prim Path):**/World/PartA_OnBelt_55
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ban_Yuan_Jian/Woodruff keys GB_converted/0;Size=1.0x1.4x4;SUPPRESSION=Default.usd'
* **世界包围盒 (World BBox):**
  * Size: '(3.816, 1.400, 1.000)'
  * Center: '(-1.400, 15.130, 1.830)'

---

### /World/PartA_OnBelt_56

* **Prim路径 (Prim Path):**/World/PartA_OnBelt_56
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ban_Yuan_Jian/Woodruff keys GB_converted/0;Size=1.0x1.4x4;SUPPRESSION=Default.usd'
* **世界包围盒 (World BBox):**
  * Size: '(3.816, 1.400, 1.000)'
  * Center: '(-3.200, 15.130, 1.830)'

---

### /World/PartA_OnBelt_57

* **Prim路径 (Prim Path):**/World/PartA_OnBelt_57
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ban_Yuan_Jian/Woodruff keys GB_converted/0;Size=1.0x1.4x4;SUPPRESSION=Default.usd'
* **世界包围盒 (World BBox):**
  * Size: '(3.816, 1.400, 1.000)'
  * Center: '(-5.000, 15.130, 1.830)'

---

### /World/PartA_OnBelt_58

* **Prim路径 (Prim Path):**/World/PartA_OnBelt_58
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ban_Yuan_Jian/Woodruff keys GB_converted/0;Size=1.0x1.4x4;SUPPRESSION=Default.usd'
* **世界包围盒 (World BBox):**
  * Size: '(3.816, 1.400, 1.000)'
  * Center: '(-6.800, 15.130, 1.830)'

---

### /World/PartA_OnBelt_59

* **Prim路径 (Prim Path):**/World/PartA_OnBelt_59
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ban_Yuan_Jian/Woodruff keys GB_converted/0;Size=1.0x1.4x4;SUPPRESSION=Default.usd'
* **世界包围盒 (World BBox):**
  * Size: '(3.816, 1.400, 1.000)'
  * Center: '(-8.600, 15.130, 1.830)'

---

### /World/PartA_OnBelt_60

* **Prim路径 (Prim Path):**/World/PartA_OnBelt_60
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ban_Yuan_Jian/Woodruff keys GB_converted/0;Size=1.0x1.4x4;SUPPRESSION=Default.usd'
* **世界包围盒 (World BBox):**
  * Size: '(3.816, 1.400, 1.000)'
  * Center: '(-10.400, 15.130, 1.830)'

---

### /World/PartA_OnBelt_61

* **Prim路径 (Prim Path):**/World/PartA_OnBelt_61
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ban_Yuan_Jian/Woodruff keys GB_converted/0;Size=1.0x1.4x4;SUPPRESSION=Default.usd'
* **世界包围盒 (World BBox):**
  * Size: '(3.816, 1.400, 1.000)'
  * Center: '(-12.200, 15.130, 1.830)'

---

### /World/PartA_OnBelt_62

* **Prim路径 (Prim Path):**/World/PartA_OnBelt_62
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ban_Yuan_Jian/Woodruff keys GB_converted/0;Size=1.0x1.4x4;SUPPRESSION=Default.usd'
* **世界包围盒 (World BBox):**
  * Size: '(3.816, 1.400, 1.000)'
  * Center: '(-14.000, 15.130, 1.830)'

---

### /World/PartA_OnBelt_63

* **Prim路径 (Prim Path):**/World/PartA_OnBelt_63
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ban_Yuan_Jian/Woodruff keys GB_converted/0;Size=1.0x1.4x4;SUPPRESSION=Default.usd'
* **世界包围盒 (World BBox):**
  * Size: '(3.816, 1.400, 1.000)'
  * Center: '(-15.800, 15.130, 1.830)'

---

### /World/PartB_OnBelt_1

* **Prim路径 (Prim Path):**/World/PartB_OnBelt_1
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ping_Jian/Feather keys GB_converted/6;Size=8;Length=28;SUPPRESSION=A,Simplified.usd'
* **世界包围盒 (World BBox):**
  * Size: '(28.000, 8.000, 7.000)'
  * Center: '(-2.400, -15.000, 1.830)'

---

### /World/PartB_OnBelt_2

* **Prim路径 (Prim Path):**/World/PartB_OnBelt_2
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ping_Jian/Feather keys GB_converted/6;Size=8;Length=28;SUPPRESSION=A,Simplified.usd'
* **世界包围盒 (World BBox):**
  * Size: '(28.000, 8.000, 7.000)'
  * Center: '(-4.200, -15.000, 1.830)'

---

### /World/PartB_OnBelt_3

* **Prim路径 (Prim Path):**/World/PartB_OnBelt_3
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ping_Jian/Feather keys GB_converted/6;Size=8;Length=28;SUPPRESSION=A,Simplified.usd'
* **世界包围盒 (World BBox):**
  * Size: '(28.000, 8.000, 7.000)'
  * Center: '(-6.000, -15.000, 1.830)'

---

### /World/PartB_OnBelt_4

* **Prim路径 (Prim Path):**/World/PartB_OnBelt_4
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ping_Jian/Feather keys GB_converted/6;Size=8;Length=28;SUPPRESSION=A,Simplified.usd'
* **世界包围盒 (World BBox):**
  * Size: '(28.000, 8.000, 7.000)'
  * Center: '(-7.800, -15.000, 1.830)'

---

### /World/PartB_OnBelt_5

* **Prim路径 (Prim Path):**/World/PartB_OnBelt_5
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ping_Jian/Feather keys GB_converted/6;Size=8;Length=28;SUPPRESSION=A,Simplified.usd'
* **世界包围盒 (World BBox):**
  * Size: '(28.000, 8.000, 7.000)'
  * Center: '(-9.600, -15.000, 1.830)'

---

### /World/PartB_OnBelt_6

* **Prim路径 (Prim Path):**/World/PartB_OnBelt_6
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ping_Jian/Feather keys GB_converted/6;Size=8;Length=28;SUPPRESSION=A,Simplified.usd'
* **世界包围盒 (World BBox):**
  * Size: '(28.000, 8.000, 7.000)'
  * Center: '(-11.400, -15.000, 1.830)'

---

### /World/PartB_OnBelt_7

* **Prim路径 (Prim Path):**/World/PartB_OnBelt_7
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ping_Jian/Feather keys GB_converted/6;Size=8;Length=28;SUPPRESSION=A,Simplified.usd'
* **世界包围盒 (World BBox):**
  * Size: '(28.000, 8.000, 7.000)'
  * Center: '(-13.200, -15.000, 1.830)'

---

### /World/PartB_OnBelt_8

* **Prim路径 (Prim Path):**/World/PartB_OnBelt_8
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ping_Jian/Feather keys GB_converted/6;Size=8;Length=28;SUPPRESSION=A,Simplified.usd'
* **世界包围盒 (World BBox):**
  * Size: '(28.000, 8.000, 7.000)'
  * Center: '(-15.000, -15.000, 1.830)'

---

### /World/PartB_OnBelt_9

* **Prim路径 (Prim Path):**/World/PartB_OnBelt_9
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ping_Jian/Feather keys GB_converted/6;Size=8;Length=28;SUPPRESSION=A,Simplified.usd'
* **世界包围盒 (World BBox):**
  * Size: '(28.000, 8.000, 7.000)'
  * Center: '(-16.800, -15.000, 1.830)'

---

### /World/PartB_OnBelt_10

* **Prim路径 (Prim Path):**/World/PartB_OnBelt_10
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ping_Jian/Feather keys GB_converted/6;Size=8;Length=28;SUPPRESSION=A,Simplified.usd'
* **世界包围盒 (World BBox):**
  * Size: '(28.000, 8.000, 7.000)'
  * Center: '(-2.400, -10.000, 1.830)'

---

### /World/PartB_OnBelt_11

* **Prim路径 (Prim Path):**/World/PartB_OnBelt_11
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ping_Jian/Feather keys GB_converted/6;Size=8;Length=28;SUPPRESSION=A,Simplified.usd'
* **世界包围盒 (World BBox):**
  * Size: '(28.000, 8.000, 7.000)'
  * Center: '(-4.200, -10.000, 1.830)'

---

### /World/PartB_OnBelt_12

* **Prim路径 (Prim Path):**/World/PartB_OnBelt_12
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ping_Jian/Feather keys GB_converted/6;Size=8;Length=28;SUPPRESSION=A,Simplified.usd'
* **世界包围盒 (World BBox):**
  * Size: '(28.000, 8.000, 7.000)'
  * Center: '(-6.000, -10.000, 1.830)'

---

### /World/PartB_OnBelt_13

* **Prim路径 (Prim Path):**/World/PartB_OnBelt_13
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ping_Jian/Feather keys GB_converted/6;Size=8;Length=28;SUPPRESSION=A,Simplified.usd'
* **世界包围盒 (World BBox):**
  * Size: '(28.000, 8.000, 7.000)'
  * Center: '(-7.800, -10.000, 1.830)'

---

### /World/PartB_OnBelt_14

* **Prim路径 (Prim Path):**/World/PartB_OnBelt_14
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ping_Jian/Feather keys GB_converted/6;Size=8;Length=28;SUPPRESSION=A,Simplified.usd'
* **世界包围盒 (World BBox):**
  * Size: '(28.000, 8.000, 7.000)'
  * Center: '(-9.600, -10.000, 1.830)'

---

### /World/PartB_OnBelt_15

* **Prim路径 (Prim Path):**/World/PartB_OnBelt_15
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ping_Jian/Feather keys GB_converted/6;Size=8;Length=28;SUPPRESSION=A,Simplified.usd'
* **世界包围盒 (World BBox):**
  * Size: '(28.000, 8.000, 7.000)'
  * Center: '(-11.400, -10.000, 1.830)'

---

### /World/PartB_OnBelt_16

* **Prim路径 (Prim Path):**/World/PartB_OnBelt_16
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ping_Jian/Feather keys GB_converted/6;Size=8;Length=28;SUPPRESSION=A,Simplified.usd'
* **世界包围盒 (World BBox):**
  * Size: '(28.000, 8.000, 7.000)'
  * Center: '(-13.200, -10.000, 1.830)'

---

### /World/PartB_OnBelt_17

* **Prim路径 (Prim Path):**/World/PartB_OnBelt_17
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ping_Jian/Feather keys GB_converted/6;Size=8;Length=28;SUPPRESSION=A,Simplified.usd'
* **世界包围盒 (World BBox):**
  * Size: '(28.000, 8.000, 7.000)'
  * Center: '(-15.000, -10.000, 1.830)'

---

### /World/PartB_OnBelt_18

* **Prim路径 (Prim Path):**/World/PartB_OnBelt_18
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ping_Jian/Feather keys GB_converted/6;Size=8;Length=28;SUPPRESSION=A,Simplified.usd'
* **世界包围盒 (World BBox):**
  * Size: '(28.000, 8.000, 7.000)'
  * Center: '(-16.800, -10.000, 1.830)'

---

### /World/PartB_OnBelt_19

* **Prim路径 (Prim Path):**/World/PartB_OnBelt_19
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ping_Jian/Feather keys GB_converted/6;Size=8;Length=28;SUPPRESSION=A,Simplified.usd'
* **世界包围盒 (World BBox):**
  * Size: '(28.000, 8.000, 7.000)'
  * Center: '(-2.400, -5.000, 1.830)'

---

### /World/PartB_OnBelt_20

* **Prim路径 (Prim Path):**/World/PartB_OnBelt_20
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ping_Jian/Feather keys GB_converted/6;Size=8;Length=28;SUPPRESSION=A,Simplified.usd'
* **世界包围盒 (World BBox):**
  * Size: '(28.000, 8.000, 7.000)'
  * Center: '(-4.200, -5.000, 1.830)'

---

### /World/PartB_OnBelt_21

* **Prim路径 (Prim Path):**/World/PartB_OnBelt_21
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ping_Jian/Feather keys GB_converted/6;Size=8;Length=28;SUPPRESSION=A,Simplified.usd'
* **世界包围盒 (World BBox):**
  * Size: '(28.000, 8.000, 7.000)'
  * Center: '(-6.000, -5.000, 1.830)'

---

### /World/PartB_OnBelt_22

* **Prim路径 (Prim Path):**/World/PartB_OnBelt_22
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ping_Jian/Feather keys GB_converted/6;Size=8;Length=28;SUPPRESSION=A,Simplified.usd'
* **世界包围盒 (World BBox):**
  * Size: '(28.000, 8.000, 7.000)'
  * Center: '(-7.800, -5.000, 1.830)'

---

### /World/PartB_OnBelt_23

* **Prim路径 (Prim Path):**/World/PartB_OnBelt_23
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ping_Jian/Feather keys GB_converted/6;Size=8;Length=28;SUPPRESSION=A,Simplified.usd'
* **世界包围盒 (World BBox):**
  * Size: '(28.000, 8.000, 7.000)'
  * Center: '(-9.600, -5.000, 1.830)'

---

### /World/PartB_OnBelt_24

* **Prim路径 (Prim Path):**/World/PartB_OnBelt_24
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ping_Jian/Feather keys GB_converted/6;Size=8;Length=28;SUPPRESSION=A,Simplified.usd'
* **世界包围盒 (World BBox):**
  * Size: '(28.000, 8.000, 7.000)'
  * Center: '(-11.400, -5.000, 1.830)'

---

### /World/PartB_OnBelt_25

* **Prim路径 (Prim Path):**/World/PartB_OnBelt_25
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ping_Jian/Feather keys GB_converted/6;Size=8;Length=28;SUPPRESSION=A,Simplified.usd'
* **世界包围盒 (World BBox):**
  * Size: '(28.000, 8.000, 7.000)'
  * Center: '(-13.200, -5.000, 1.830)'

---

### /World/PartB_OnBelt_26

* **Prim路径 (Prim Path):**/World/PartB_OnBelt_26
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ping_Jian/Feather keys GB_converted/6;Size=8;Length=28;SUPPRESSION=A,Simplified.usd'
* **世界包围盒 (World BBox):**
  * Size: '(28.000, 8.000, 7.000)'
  * Center: '(-15.000, -5.000, 1.830)'

---

### /World/PartB_OnBelt_27

* **Prim路径 (Prim Path):**/World/PartB_OnBelt_27
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ping_Jian/Feather keys GB_converted/6;Size=8;Length=28;SUPPRESSION=A,Simplified.usd'
* **世界包围盒 (World BBox):**
  * Size: '(28.000, 8.000, 7.000)'
  * Center: '(-16.800, -5.000, 1.830)'

---

### /World/PartB_OnBelt_28

* **Prim路径 (Prim Path):**/World/PartB_OnBelt_28
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ping_Jian/Feather keys GB_converted/6;Size=8;Length=28;SUPPRESSION=A,Simplified.usd'
* **世界包围盒 (World BBox):**
  * Size: '(28.000, 8.000, 7.000)'
  * Center: '(-2.400, 0.000, 1.830)'

---

### /World/PartB_OnBelt_29

* **Prim路径 (Prim Path):**/World/PartB_OnBelt_29
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ping_Jian/Feather keys GB_converted/6;Size=8;Length=28;SUPPRESSION=A,Simplified.usd'
* **世界包围盒 (World BBox):**
  * Size: '(28.000, 8.000, 7.000)'
  * Center: '(-4.200, 0.000, 1.830)'

---

### /World/PartB_OnBelt_30

* **Prim路径 (Prim Path):**/World/PartB_OnBelt_30
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ping_Jian/Feather keys GB_converted/6;Size=8;Length=28;SUPPRESSION=A,Simplified.usd'
* **世界包围盒 (World BBox):**
  * Size: '(28.000, 8.000, 7.000)'
  * Center: '(-6.000, 0.000, 1.830)'

---

### /World/PartB_OnBelt_31

* **Prim路径 (Prim Path):**/World/PartB_OnBelt_31
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ping_Jian/Feather keys GB_converted/6;Size=8;Length=28;SUPPRESSION=A,Simplified.usd'
* **世界包围盒 (World BBox):**
  * Size: '(28.000, 8.000, 7.000)'
  * Center: '(-7.800, 0.000, 1.830)'

---

### /World/PartB_OnBelt_32

* **Prim路径 (Prim Path):**/World/PartB_OnBelt_32
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ping_Jian/Feather keys GB_converted/6;Size=8;Length=28;SUPPRESSION=A,Simplified.usd'
* **世界包围盒 (World BBox):**
  * Size: '(28.000, 8.000, 7.000)'
  * Center: '(-9.600, 0.000, 1.830)'

---

### /World/PartB_OnBelt_33

* **Prim路径 (Prim Path):**/World/PartB_OnBelt_33
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ping_Jian/Feather keys GB_converted/6;Size=8;Length=28;SUPPRESSION=A,Simplified.usd'
* **世界包围盒 (World BBox):**
  * Size: '(28.000, 8.000, 7.000)'
  * Center: '(-11.400, 0.000, 1.830)'

---

### /World/PartB_OnBelt_34

* **Prim路径 (Prim Path):**/World/PartB_OnBelt_34
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ping_Jian/Feather keys GB_converted/6;Size=8;Length=28;SUPPRESSION=A,Simplified.usd'
* **世界包围盒 (World BBox):**
  * Size: '(28.000, 8.000, 7.000)'
  * Center: '(-13.200, 0.000, 1.830)'

---

### /World/PartB_OnBelt_35

* **Prim路径 (Prim Path):**/World/PartB_OnBelt_35
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ping_Jian/Feather keys GB_converted/6;Size=8;Length=28;SUPPRESSION=A,Simplified.usd'
* **世界包围盒 (World BBox):**
  * Size: '(28.000, 8.000, 7.000)'
  * Center: '(-15.000, 0.000, 1.830)'

---

### /World/PartB_OnBelt_36

* **Prim路径 (Prim Path):**/World/PartB_OnBelt_36
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ping_Jian/Feather keys GB_converted/6;Size=8;Length=28;SUPPRESSION=A,Simplified.usd'
* **世界包围盒 (World BBox):**
  * Size: '(28.000, 8.000, 7.000)'
  * Center: '(-16.800, 0.000, 1.830)'

---

### /World/PartB_OnBelt_37

* **Prim路径 (Prim Path):**/World/PartB_OnBelt_37
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ping_Jian/Feather keys GB_converted/6;Size=8;Length=28;SUPPRESSION=A,Simplified.usd'
* **世界包围盒 (World BBox):**
  * Size: '(28.000, 8.000, 7.000)'
  * Center: '(-2.400, 5.000, 1.830)'

---

### /World/PartB_OnBelt_38

* **Prim路径 (Prim Path):**/World/PartB_OnBelt_38
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ping_Jian/Feather keys GB_converted/6;Size=8;Length=28;SUPPRESSION=A,Simplified.usd'
* **世界包围盒 (World BBox):**
  * Size: '(28.000, 8.000, 7.000)'
  * Center: '(-4.200, 5.000, 1.830)'

---

### /World/PartB_OnBelt_39

* **Prim路径 (Prim Path):**/World/PartB_OnBelt_39
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ping_Jian/Feather keys GB_converted/6;Size=8;Length=28;SUPPRESSION=A,Simplified.usd'
* **世界包围盒 (World BBox):**
  * Size: '(28.000, 8.000, 7.000)'
  * Center: '(-6.000, 5.000, 1.830)'

---

### /World/PartB_OnBelt_40

* **Prim路径 (Prim Path):**/World/PartB_OnBelt_40
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ping_Jian/Feather keys GB_converted/6;Size=8;Length=28;SUPPRESSION=A,Simplified.usd'
* **世界包围盒 (World BBox):**
  * Size: '(28.000, 8.000, 7.000)'
  * Center: '(-7.800, 5.000, 1.830)'

---

### /World/PartB_OnBelt_41

* **Prim路径 (Prim Path):**/World/PartB_OnBelt_41
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ping_Jian/Feather keys GB_converted/6;Size=8;Length=28;SUPPRESSION=A,Simplified.usd'
* **世界包围盒 (World BBox):**
  * Size: '(28.000, 8.000, 7.000)'
  * Center: '(-9.600, 5.000, 1.830)'

---

### /World/PartB_OnBelt_42

* **Prim路径 (Prim Path):**/World/PartB_OnBelt_42
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ping_Jian/Feather keys GB_converted/6;Size=8;Length=28;SUPPRESSION=A,Simplified.usd'
* **世界包围盒 (World BBox):**
  * Size: '(28.000, 8.000, 7.000)'
  * Center: '(-11.400, 5.000, 1.830)'

---

### /World/PartB_OnBelt_43

* **Prim路径 (Prim Path):**/World/PartB_OnBelt_43
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ping_Jian/Feather keys GB_converted/6;Size=8;Length=28;SUPPRESSION=A,Simplified.usd'
* **世界包围盒 (World BBox):**
  * Size: '(28.000, 8.000, 7.000)'
  * Center: '(-13.200, 5.000, 1.830)'

---

### /World/PartB_OnBelt_44

* **Prim路径 (Prim Path):**/World/PartB_OnBelt_44
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ping_Jian/Feather keys GB_converted/6;Size=8;Length=28;SUPPRESSION=A,Simplified.usd'
* **世界包围盒 (World BBox):**
  * Size: '(28.000, 8.000, 7.000)'
  * Center: '(-15.000, 5.000, 1.830)'

---

### /World/PartB_OnBelt_45

* **Prim路径 (Prim Path):**/World/PartB_OnBelt_45
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ping_Jian/Feather keys GB_converted/6;Size=8;Length=28;SUPPRESSION=A,Simplified.usd'
* **世界包围盒 (World BBox):**
  * Size: '(28.000, 8.000, 7.000)'
  * Center: '(-16.800, 5.000, 1.830)'

---

### /World/PartB_OnBelt_46

* **Prim路径 (Prim Path):**/World/PartB_OnBelt_46
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ping_Jian/Feather keys GB_converted/6;Size=8;Length=28;SUPPRESSION=A,Simplified.usd'
* **世界包围盒 (World BBox):**
  * Size: '(28.000, 8.000, 7.000)'
  * Center: '(-2.400, 10.000, 1.830)'

---

### /World/PartB_OnBelt_47

* **Prim路径 (Prim Path):**/World/PartB_OnBelt_47
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ping_Jian/Feather keys GB_converted/6;Size=8;Length=28;SUPPRESSION=A,Simplified.usd'
* **世界包围盒 (World BBox):**
  * Size: '(28.000, 8.000, 7.000)'
  * Center: '(-4.200, 10.000, 1.830)'

---

### /World/PartB_OnBelt_48

* **Prim路径 (Prim Path):**/World/PartB_OnBelt_48
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ping_Jian/Feather keys GB_converted/6;Size=8;Length=28;SUPPRESSION=A,Simplified.usd'
* **世界包围盒 (World BBox):**
  * Size: '(28.000, 8.000, 7.000)'
  * Center: '(-6.000, 10.000, 1.830)'

---

### /World/PartB_OnBelt_49

* **Prim路径 (Prim Path):**/World/PartB_OnBelt_49
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ping_Jian/Feather keys GB_converted/6;Size=8;Length=28;SUPPRESSION=A,Simplified.usd'
* **世界包围盒 (World BBox):**
  * Size: '(28.000, 8.000, 7.000)'
  * Center: '(-7.800, 10.000, 1.830)'

---

### /World/PartB_OnBelt_50

* **Prim路径 (Prim Path):**/World/PartB_OnBelt_50
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ping_Jian/Feather keys GB_converted/6;Size=8;Length=28;SUPPRESSION=A,Simplified.usd'
* **世界包围盒 (World BBox):**
  * Size: '(28.000, 8.000, 7.000)'
  * Center: '(-9.600, 10.000, 1.830)'

---

### /World/PartB_OnBelt_51

* **Prim路径 (Prim Path):**/World/PartB_OnBelt_51
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ping_Jian/Feather keys GB_converted/6;Size=8;Length=28;SUPPRESSION=A,Simplified.usd'
* **世界包围盒 (World BBox):**
  * Size: '(28.000, 8.000, 7.000)'
  * Center: '(-11.400, 10.000, 1.830)'

---

### /World/PartB_OnBelt_52

* **Prim路径 (Prim Path):**/World/PartB_OnBelt_52
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ping_Jian/Feather keys GB_converted/6;Size=8;Length=28;SUPPRESSION=A,Simplified.usd'
* **世界包围盒 (World BBox):**
  * Size: '(28.000, 8.000, 7.000)'
  * Center: '(-13.200, 10.000, 1.830)'

---

### /World/PartB_OnBelt_53

* **Prim路径 (Prim Path):**/World/PartB_OnBelt_53
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ping_Jian/Feather keys GB_converted/6;Size=8;Length=28;SUPPRESSION=A,Simplified.usd'
* **世界包围盒 (World BBox):**
  * Size: '(28.000, 8.000, 7.000)'
  * Center: '(-15.000, 10.000, 1.830)'

---

### /World/PartB_OnBelt_54

* **Prim路径 (Prim Path):**/World/PartB_OnBelt_54
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ping_Jian/Feather keys GB_converted/6;Size=8;Length=28;SUPPRESSION=A,Simplified.usd'
* **世界包围盒 (World BBox):**
  * Size: '(28.000, 8.000, 7.000)'
  * Center: '(-16.800, 10.000, 1.830)'

---

### /World/PartB_OnBelt_55

* **Prim路径 (Prim Path):**/World/PartB_OnBelt_55
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ping_Jian/Feather keys GB_converted/6;Size=8;Length=28;SUPPRESSION=A,Simplified.usd'
* **世界包围盒 (World BBox):**
  * Size: '(28.000, 8.000, 7.000)'
  * Center: '(-2.400, 15.000, 1.830)'

---

### /World/PartB_OnBelt_56

* **Prim路径 (Prim Path):**/World/PartB_OnBelt_56
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ping_Jian/Feather keys GB_converted/6;Size=8;Length=28;SUPPRESSION=A,Simplified.usd'
* **世界包围盒 (World BBox):**
  * Size: '(28.000, 8.000, 7.000)'
  * Center: '(-4.200, 15.000, 1.830)'

---

### /World/PartB_OnBelt_57

* **Prim路径 (Prim Path):**/World/PartB_OnBelt_57
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ping_Jian/Feather keys GB_converted/6;Size=8;Length=28;SUPPRESSION=A,Simplified.usd'
* **世界包围盒 (World BBox):**
  * Size: '(28.000, 8.000, 7.000)'
  * Center: '(-6.000, 15.000, 1.830)'

---

### /World/PartB_OnBelt_58

* **Prim路径 (Prim Path):**/World/PartB_OnBelt_58
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ping_Jian/Feather keys GB_converted/6;Size=8;Length=28;SUPPRESSION=A,Simplified.usd'
* **世界包围盒 (World BBox):**
  * Size: '(28.000, 8.000, 7.000)'
  * Center: '(-7.800, 15.000, 1.830)'

---

### /World/PartB_OnBelt_59

* **Prim路径 (Prim Path):**/World/PartB_OnBelt_59
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ping_Jian/Feather keys GB_converted/6;Size=8;Length=28;SUPPRESSION=A,Simplified.usd'
* **世界包围盒 (World BBox):**
  * Size: '(28.000, 8.000, 7.000)'
  * Center: '(-9.600, 15.000, 1.830)'

---

### /World/PartB_OnBelt_60

* **Prim路径 (Prim Path):**/World/PartB_OnBelt_60
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ping_Jian/Feather keys GB_converted/6;Size=8;Length=28;SUPPRESSION=A,Simplified.usd'
* **世界包围盒 (World BBox):**
  * Size: '(28.000, 8.000, 7.000)'
  * Center: '(-11.400, 15.000, 1.830)'

---

### /World/PartB_OnBelt_61

* **Prim路径 (Prim Path):**/World/PartB_OnBelt_61
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ping_Jian/Feather keys GB_converted/6;Size=8;Length=28;SUPPRESSION=A,Simplified.usd'
* **世界包围盒 (World BBox):**
  * Size: '(28.000, 8.000, 7.000)'
  * Center: '(-13.200, 15.000, 1.830)'

---

### /World/PartB_OnBelt_62

* **Prim路径 (Prim Path):**/World/PartB_OnBelt_62
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ping_Jian/Feather keys GB_converted/6;Size=8;Length=28;SUPPRESSION=A,Simplified.usd'
* **世界包围盒 (World BBox):**
  * Size: '(28.000, 8.000, 7.000)'
  * Center: '(-15.000, 15.000, 1.830)'

---

### /World/PartB_OnBelt_63

* **Prim路径 (Prim Path):**/World/PartB_OnBelt_63
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ping_Jian/Feather keys GB_converted/6;Size=8;Length=28;SUPPRESSION=A,Simplified.usd'
* **世界包围盒 (World BBox):**
  * Size: '(28.000, 8.000, 7.000)'
  * Center: '(-16.800, 15.000, 1.830)'

---

### /World/PartA_OnWorkbench_1

* **Prim路径 (Prim Path):**/World/PartA_OnWorkbench_1
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ban_Yuan_Jian/Woodruff keys GB_converted/0;Size=1.0x1.4x4;SUPPRESSION=Default.usd'
* **世界包围盒 (World BBox):**
  * Size: '(3.816, 1.400, 1.000)'
  * Center: '(0.000, -15.248, 0.892)'

---

### /World/PartA_OnWorkbench_2

* **Prim路径 (Prim Path):**/World/PartA_OnWorkbench_2
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ban_Yuan_Jian/Woodruff keys GB_converted/0;Size=1.0x1.4x4;SUPPRESSION=Default.usd'
* **世界包围盒 (World BBox):**
  * Size: '(3.816, 1.400, 1.000)'
  * Center: '(0.000, -10.248, 0.892)'

---

### /World/PartA_OnWorkbench_3

* **Prim路径 (Prim Path):**/World/PartA_OnWorkbench_3
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ban_Yuan_Jian/Woodruff keys GB_converted/0;Size=1.0x1.4x4;SUPPRESSION=Default.usd'
* **世界包围盒 (World BBox):**
  * Size: '(3.816, 1.400, 1.000)'
  * Center: '(0.000, -5.248, 0.892)'

---

### /World/PartA_OnWorkbench_4

* **Prim路径 (Prim Path):**/World/PartA_OnWorkbench_4
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ban_Yuan_Jian/Woodruff keys GB_converted/0;Size=1.0x1.4x4;SUPPRESSION=Default.usd'
* **世界包围盒 (World BBox):**
  * Size: '(3.816, 1.400, 1.000)'
  * Center: '(0.000, -0.248, 0.892)'

---

### /World/PartA_OnWorkbench_5

* **Prim路径 (Prim Path):**/World/PartA_OnWorkbench_5
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ban_Yuan_Jian/Woodruff keys GB_converted/0;Size=1.0x1.4x4;SUPPRESSION=Default.usd'
* **世界包围盒 (World BBox):**
  * Size: '(3.816, 1.400, 1.000)'
  * Center: '(0.000, 4.752, 0.892)'

---

### /World/PartA_OnWorkbench_6

* **Prim路径 (Prim Path):**/World/PartA_OnWorkbench_6
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ban_Yuan_Jian/Woodruff keys GB_converted/0;Size=1.0x1.4x4;SUPPRESSION=Default.usd'
* **世界包围盒 (World BBox):**
  * Size: '(3.816, 1.400, 1.000)'
  * Center: '(0.000, 9.752, 0.892)'

---

### /World/PartB_OnWorkbench_1

* **Prim路径 (Prim Path):**/World/PartB_OnWorkbench_1
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ping_Jian/Feather keys GB_converted/6;Size=8;Length=28;SUPPRESSION=A,Simplified.usd'
* **世界包围盒 (World BBox):**
  * Size: '(28.000, 8.000, 7.000)'
  * Center: '(0.000, -14.708, 0.892)'

---

### /World/PartB_OnWorkbench_2

* **Prim路径 (Prim Path):**/World/PartB_OnWorkbench_2
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ping_Jian/Feather keys GB_converted/6;Size=8;Length=28;SUPPRESSION=A,Simplified.usd'
* **世界包围盒 (World BBox):**
  * Size: '(28.000, 8.000, 7.000)'
  * Center: '(0.000, -9.708, 0.892)'

---

### /World/PartB_OnWorkbench_3

* **Prim路径 (Prim Path):**/World/PartB_OnWorkbench_3
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ping_Jian/Feather keys GB_converted/6;Size=8;Length=28;SUPPRESSION=A,Simplified.usd'
* **世界包围盒 (World BBox):**
  * Size: '(28.000, 8.000, 7.000)'
  * Center: '(0.000, -4.708, 0.892)'

---

### /World/PartB_OnWorkbench_4

* **Prim路径 (Prim Path):**/World/PartB_OnWorkbench_4
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ping_Jian/Feather keys GB_converted/6;Size=8;Length=28;SUPPRESSION=A,Simplified.usd'
* **世界包围盒 (World BBox):**
  * Size: '(28.000, 8.000, 7.000)'
  * Center: '(0.000, 0.292, 0.892)'

---

### /World/PartB_OnWorkbench_5

* **Prim路径 (Prim Path):**/World/PartB_OnWorkbench_5
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ping_Jian/Feather keys GB_converted/6;Size=8;Length=28;SUPPRESSION=A,Simplified.usd'
* **世界包围盒 (World BBox):**
  * Size: '(28.000, 8.000, 7.000)'
  * Center: '(0.000, 5.292, 0.892)'

---

### /World/PartB_OnWorkbench_6

* **Prim路径 (Prim Path):**/World/PartB_OnWorkbench_6
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ping_Jian/Feather keys GB_converted/6;Size=8;Length=28;SUPPRESSION=A,Simplified.usd'
* **世界包围盒 (World BBox):**
  * Size: '(28.000, 8.000, 7.000)'
  * Center: '(0.000, 10.292, 0.892)'

---

### /World/agv_1

* **Prim路径 (Prim Path):**/World/agv_1
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/assets/AGV_ready_1/AGV_ready_1.usdc'
* **世界包围盒 (World BBox):**
  * Size: '(1.457, 0.340, 0.669)'
  * Center: '(2.098, -14.286, 0.059)'

---

### /World/agv_2

* **Prim路径 (Prim Path):**/World/agv_2
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/assets/AGV_ready_1/AGV_ready_1.usdc'
* **世界包围盒 (World BBox):**
  * Size: '(1.457, 0.340, 0.669)'
  * Center: '(2.098, -9.286, 0.059)'

---

### /World/agv_3

* **Prim路径 (Prim Path):**/World/agv_3
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/assets/AGV_ready_1/AGV_ready_1.usdc'
* **世界包围盒 (World BBox):**
  * Size: '(1.457, 0.340, 0.669)'
  * Center: '(2.098, -4.286, 0.059)'

---

### /World/agv_4

* **Prim路径 (Prim Path):**/World/agv_4
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/assets/AGV_ready_1/AGV_ready_1.usdc'
* **世界包围盒 (World BBox):**
  * Size: '(1.457, 0.340, 0.669)'
  * Center: '(2.098, 0.714, 0.059)'

---

### /World/agv_5

* **Prim路径 (Prim Path):**/World/agv_5
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/assets/AGV_ready_1/AGV_ready_1.usdc'
* **世界包围盒 (World BBox):**
  * Size: '(1.457, 0.340, 0.669)'
  * Center: '(2.098, 5.714, 0.059)'

---

### /World/agv_6

* **Prim路径 (Prim Path):**/World/agv_6
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/assets/AGV_ready_1/AGV_ready_1.usdc'
* **世界包围盒 (World BBox):**
  * Size: '(1.457, 0.340, 0.669)'
  * Center: '(2.098, 10.714, 0.059)'

---

### /World/StackedCarton_1

* **Prim路径 (Prim Path):**/World/StackedCarton_1
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/assets/Plastic_Crate(1)/Plastic_Crate.usdc'
* **世界包围盒 (World BBox):**
  * Size: '(0.424, 0.365, 0.421)'
  * Center: '(2.093, -14.473, 0.404)'

---

### /World/StackedCarton_2

* **Prim路径 (Prim Path):**/World/StackedCarton_2
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/assets/Plastic_Crate(1)/Plastic_Crate.usdc'
* **世界包围盒 (World BBox):**
  * Size: '(0.424, 0.365, 0.421)'
  * Center: '(2.093, -9.473, 0.404)'

---

### /World/StackedCarton_3

* **Prim路径 (Prim Path):**/World/StackedCarton_3
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/assets/Plastic_Crate(1)/Plastic_Crate.usdc'
* **世界包围盒 (World BBox):**
  * Size: '(0.424, 0.365, 0.421)'
  * Center: '(2.093, -4.473, 0.404)'

---

### /World/StackedCarton_4

* **Prim路径 (Prim Path):**/World/StackedCarton_4
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/assets/Plastic_Crate(1)/Plastic_Crate.usdc'
* **世界包围盒 (World BBox):**
  * Size: '(0.424, 0.365, 0.421)'
  * Center: '(2.093, 0.527, 0.404)'

---

### /World/StackedCarton_5

* **Prim路径 (Prim Path):**/World/StackedCarton_5
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/assets/Plastic_Crate(1)/Plastic_Crate.usdc'
* **世界包围盒 (World BBox):**
  * Size: '(0.424, 0.365, 0.421)'
  * Center: '(2.093, 5.527, 0.404)'

---

### /World/StackedCarton_6

* **Prim路径 (Prim Path):**/World/StackedCarton_6
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/assets/Plastic_Crate(1)/Plastic_Crate.usdc'
* **世界包围盒 (World BBox):**
  * Size: '(0.424, 0.365, 0.421)'
  * Center: '(2.093, 10.527, 0.404)'

---

### /World/Workbench_02

* **Prim路径 (Prim Path):**/World/Workbench_02
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] 'file:/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/5.0/NVIDIA/Assets/DigitalTwin/Assets/Warehouse/Furnishing/Workbenches/MetalWorktable_A/MetalWorktable_A12_01.usd'
* **世界包围盒 (World BBox):**
  * Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
  * Center: '(0.000, 0.000, 0.000)'

---

### /World/Workbench_03

* **Prim路径 (Prim Path):**/World/Workbench_03
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] 'file:/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/5.0/NVIDIA/Assets/DigitalTwin/Assets/Warehouse/Furnishing/Workbenches/MetalWorktable_A/MetalWorktable_A12_01.usd'
* **世界包围盒 (World BBox):**
  * Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
  * Center: '(0.000, 0.000, 0.000)'

---

### /World/Workbench_04

* **Prim路径 (Prim Path):**/World/Workbench_04
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] 'file:/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/5.0/NVIDIA/Assets/DigitalTwin/Assets/Warehouse/Furnishing/Workbenches/MetalWorktable_A/MetalWorktable_A12_01.usd'
* **世界包围盒 (World BBox):**
  * Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
  * Center: '(0.000, 0.000, 0.000)'

---

### /World/Workbench_05

* **Prim路径 (Prim Path):**/World/Workbench_05
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] 'file:/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/5.0/NVIDIA/Assets/DigitalTwin/Assets/Warehouse/Furnishing/Workbenches/MetalWorktable_A/MetalWorktable_A12_01.usd'
* **世界包围盒 (World BBox):**
  * Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
  * Center: '(0.000, 0.000, 0.000)'

---

### /World/Workbench_06

* **Prim路径 (Prim Path):**/World/Workbench_06
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] 'file:/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/5.0/NVIDIA/Assets/DigitalTwin/Assets/Warehouse/Furnishing/Workbenches/MetalWorktable_A/MetalWorktable_A12_01.usd'
* **世界包围盒 (World BBox):**
  * Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
  * Center: '(0.000, 0.000, 0.000)'

---

### /World/Workbench_07

* **Prim路径 (Prim Path):**/World/Workbench_07
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] 'file:/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/5.0/NVIDIA/Assets/DigitalTwin/Assets/Warehouse/Furnishing/Workbenches/MetalWorktable_A/MetalWorktable_A12_01.usd'
* **世界包围盒 (World BBox):**
  * Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
  * Center: '(0.000, 0.000, 0.000)'

---

### /World/Workbench_08

* **Prim路径 (Prim Path):**/World/Workbench_08
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] 'file:/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/5.0/NVIDIA/Assets/DigitalTwin/Assets/Warehouse/Furnishing/Workbenches/MetalWorktable_A/MetalWorktable_A12_01.usd'
* **世界包围盒 (World BBox):**
  * Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
  * Center: '(0.000, 0.000, 0.000)'

---

### /World/Workbench_09

* **Prim路径 (Prim Path):**/World/Workbench_09
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] 'file:/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/5.0/NVIDIA/Assets/DigitalTwin/Assets/Warehouse/Furnishing/Workbenches/MetalWorktable_A/MetalWorktable_A12_01.usd'
* **世界包围盒 (World BBox):**
  * Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
  * Center: '(0.000, 0.000, 0.000)'

---

### /World/Workbench_10

* **Prim路径 (Prim Path):**/World/Workbench_10
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] 'file:/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/5.0/NVIDIA/Assets/DigitalTwin/Assets/Warehouse/Furnishing/Workbenches/MetalWorktable_A/MetalWorktable_A12_01.usd'
* **世界包围盒 (World BBox):**
  * Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
  * Center: '(0.000, 0.000, 0.000)'

---

### /World/Workbench_11

* **Prim路径 (Prim Path):**/World/Workbench_11
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] 'file:/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/5.0/NVIDIA/Assets/DigitalTwin/Assets/Warehouse/Furnishing/Workbenches/MetalWorktable_A/MetalWorktable_A12_01.usd'
* **世界包围盒 (World BBox):**
  * Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
  * Center: '(0.000, 0.000, 0.000)'

---

### /World/Workbench_12

* **Prim路径 (Prim Path):**/World/Workbench_12
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] 'file:/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/5.0/NVIDIA/Assets/DigitalTwin/Assets/Warehouse/Furnishing/Workbenches/MetalWorktable_A/MetalWorktable_A12_01.usd'
* **世界包围盒 (World BBox):**
  * Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
  * Center: '(0.000, 0.000, 0.000)'

---

### /World/Workbench_13

* **Prim路径 (Prim Path):**/World/Workbench_13
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] 'file:/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/5.0/NVIDIA/Assets/DigitalTwin/Assets/Warehouse/Furnishing/Workbenches/MetalWorktable_A/MetalWorktable_A12_01.usd'
* **世界包围盒 (World BBox):**
  * Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
  * Center: '(0.000, 0.000, 0.000)'

---

### /World/Workbench_14

* **Prim路径 (Prim Path):**/World/Workbench_14
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] 'file:/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/5.0/NVIDIA/Assets/DigitalTwin/Assets/Warehouse/Furnishing/Workbenches/MetalWorktable_A/MetalWorktable_A12_01.usd'
* **世界包围盒 (World BBox):**
  * Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
  * Center: '(0.000, 0.000, 0.000)'

---

### /World/Workbench_15

* **Prim路径 (Prim Path):**/World/Workbench_15
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] 'file:/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/5.0/NVIDIA/Assets/DigitalTwin/Assets/Warehouse/Furnishing/Workbenches/MetalWorktable_A/MetalWorktable_A12_01.usd'
* **世界包围盒 (World BBox):**
  * Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
  * Center: '(0.000, 0.000, 0.000)'

---

### /World/Black_Honey___Robotic_Arm

* **Prim路径 (Prim Path):**/World/Black_Honey___Robotic_Arm
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '../device_data/usdz/IndustrialRobot/Black_Honey_-_Robotic_Arm.usdz'
* **世界包围盒 (World BBox):**
  * Size: '(80.801, 227.335, 36.268)'
  * Center: '(-0.800, -15.705, 1.863)'

---

### /World/rs007l_onrobot_rg2

* **Prim路径 (Prim Path):**/World/rs007l_onrobot_rg2
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '../device_data/usdz/IndustrialRobot/rs007l_onrobot_rg2.usdz'
* **世界包围盒 (World BBox):**
  * Size: '(0.381, 0.319, 1.585)'
  * Center: '(0.691, -14.327, 1.632)'

---

## 4. 材质库 (Material Library)

### /World/Environment/Materials/industrialWindow_Small

* **Prim路径 (Prim Path):**/World/Environment/Materials/industrialWindow_Small
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/Environment/Materials/industrialWindow_Small/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Environment/Materials/industrialWindow_Small/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f]
        * Connected: '/World/Environment/Materials/industrialWindow_Small/tex_base.outputs:rgb' @ '/World/Environment/Materials/industrialWindow_Small/tex_base'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/industrialWindow-Small_baseColor.jpg'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float]
        * Connected: '/World/Environment/Materials/industrialWindow_Small/tex_metallic.outputs:r' @ '/World/Environment/Materials/industrialWindow_Small/tex_metallic'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/industrialWindow-Small_metallicRoughness_metal_scale0.jpg'
      * 'normal' [normal3f]
        * Connected: '/World/Environment/Materials/industrialWindow_Small/tex_normal.outputs:rgb' @ '/World/Environment/Materials/industrialWindow_Small/tex_normal'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/industrialWindow-Small_normal.jpg'
      * 'occlusion' [float] = '1'
      * 'roughness' [float]
        * Connected: '/World/Environment/Materials/industrialWindow_Small/tex_roughness.outputs:r' @ '/World/Environment/Materials/industrialWindow_Small/tex_roughness'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/industrialWindow-Small_metallicRoughness_rough.jpg'
    * '/World/Environment/Materials/industrialWindow_Small/tex_base' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/industrialWindow-Small_baseColor.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'file' [asset] = '0/industrialWindow-Small_baseColor.jpg'
      * 'st' [float2]
        * Connected: '/World/Environment/Materials/industrialWindow_Small/uvset0.outputs:result' @ '/World/Environment/Materials/industrialWindow_Small/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/Environment/Materials/industrialWindow_Small/uvset0' (ID: 'UsdPrimvarReader_float2')
    * Implementation: 'id'
    * '/World/Environment/Materials/industrialWindow_Small/tex_metallic' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/industrialWindow-Small_metallicRoughness_metal_scale0.jpg'
    * Inputs:
      * 'fallback' [float4] = '(0.000, 0.000, 0.000, 1.000)'
      * 'file' [asset] = '0/industrialWindow-Small_metallicRoughness_metal_scale0.jpg'
      * 'st' [float2]
        * Connected: '/World/Environment/Materials/industrialWindow_Small/uvset0.outputs:result' @ '/World/Environment/Materials/industrialWindow_Small/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/Environment/Materials/industrialWindow_Small/tex_normal' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/industrialWindow-Small_normal.jpg'
    * Inputs:
      * 'bias' [float4] = '(-1.000, -1.000, -1.000, -1.000)'
      * 'fallback' [float4] = '(0.000, 0.000, 1.000, 1.000)'
      * 'file' [asset] = '0/industrialWindow-Small_normal.jpg'
      * 'scale' [float4] = '(2.000, 2.000, 2.000, 2.000)'
      * 'st' [float2]
        * Connected: '/World/Environment/Materials/industrialWindow_Small/uvset0.outputs:result' @ '/World/Environment/Materials/industrialWindow_Small/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/Environment/Materials/industrialWindow_Small/tex_roughness' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/industrialWindow-Small_metallicRoughness_rough.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 0.000, 0.000, 1.000)'
      * 'file' [asset] = '0/industrialWindow-Small_metallicRoughness_rough.jpg'
      * 'st' [float2]
        * Connected: '/World/Environment/Materials/industrialWindow_Small/uvset0.outputs:result' @ '/World/Environment/Materials/industrialWindow_Small/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'

---

### /World/Environment/Materials/industrialDoor

* **Prim路径 (Prim Path):**/World/Environment/Materials/industrialDoor
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/Environment/Materials/industrialDoor/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Environment/Materials/industrialDoor/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f]
        * Connected: '/World/Environment/Materials/industrialDoor/tex_base.outputs:rgb' @ '/World/Environment/Materials/industrialDoor/tex_base'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/industrialDoor_baseColor.jpg'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float]
        * Connected: '/World/Environment/Materials/industrialDoor/tex_metallic.outputs:r' @ '/World/Environment/Materials/industrialDoor/tex_metallic'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/industrialDoor_metallicRoughness_metal_scale0.jpg'
      * 'normal' [normal3f]
        * Connected: '/World/Environment/Materials/industrialDoor/tex_normal.outputs:rgb' @ '/World/Environment/Materials/industrialDoor/tex_normal'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/industrialDoor_normal.jpg'
      * 'occlusion' [float] = '1'
      * 'roughness' [float]
        * Connected: '/World/Environment/Materials/industrialDoor/tex_roughness.outputs:r' @ '/World/Environment/Materials/industrialDoor/tex_roughness'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/industrialDoor_metallicRoughness_rough.jpg'
    * '/World/Environment/Materials/industrialDoor/tex_base' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/industrialDoor_baseColor.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'file' [asset] = '0/industrialDoor_baseColor.jpg'
      * 'st' [float2]
        * Connected: '/World/Environment/Materials/industrialDoor/uvset0.outputs:result' @ '/World/Environment/Materials/industrialDoor/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/Environment/Materials/industrialDoor/uvset0' (ID: 'UsdPrimvarReader_float2')
    * Implementation: 'id'
    * '/World/Environment/Materials/industrialDoor/tex_metallic' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/industrialDoor_metallicRoughness_metal_scale0.jpg'
    * Inputs:
      * 'fallback' [float4] = '(0.000, 0.000, 0.000, 1.000)'
      * 'file' [asset] = '0/industrialDoor_metallicRoughness_metal_scale0.jpg'
      * 'st' [float2]
        * Connected: '/World/Environment/Materials/industrialDoor/uvset0.outputs:result' @ '/World/Environment/Materials/industrialDoor/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/Environment/Materials/industrialDoor/tex_normal' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/industrialDoor_normal.jpg'
    * Inputs:
      * 'bias' [float4] = '(-1.000, -1.000, -1.000, -1.000)'
      * 'fallback' [float4] = '(0.000, 0.000, 1.000, 1.000)'
      * 'file' [asset] = '0/industrialDoor_normal.jpg'
      * 'scale' [float4] = '(2.000, 2.000, 2.000, 2.000)'
      * 'st' [float2]
        * Connected: '/World/Environment/Materials/industrialDoor/uvset0.outputs:result' @ '/World/Environment/Materials/industrialDoor/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/Environment/Materials/industrialDoor/tex_roughness' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/industrialDoor_metallicRoughness_rough.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 0.000, 0.000, 1.000)'
      * 'file' [asset] = '0/industrialDoor_metallicRoughness_rough.jpg'
      * 'st' [float2]
        * Connected: '/World/Environment/Materials/industrialDoor/uvset0.outputs:result' @ '/World/Environment/Materials/industrialDoor/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'

---

### /World/Environment/Materials/Atlas_2048x2048_01

* **Prim路径 (Prim Path):**/World/Environment/Materials/Atlas_2048x2048_01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/Environment/Materials/Atlas_2048x2048_01/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Environment/Materials/Atlas_2048x2048_01/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f]
        * Connected: '/World/Environment/Materials/Atlas_2048x2048_01/tex_base.outputs:rgb' @ '/World/Environment/Materials/Atlas_2048x2048_01/tex_base'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/Atlas_2048x2048_01_baseColor.jpg'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float]
        * Connected: '/World/Environment/Materials/Atlas_2048x2048_01/tex_metallic.outputs:r' @ '/World/Environment/Materials/Atlas_2048x2048_01/tex_metallic'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/Atlas_2048x2048_01_metallicRoughness_metal_scale0.jpg'
      * 'normal' [normal3f]
        * Connected: '/World/Environment/Materials/Atlas_2048x2048_01/tex_normal.outputs:rgb' @ '/World/Environment/Materials/Atlas_2048x2048_01/tex_normal'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/Atlas_2048x2048_01_normal.jpg'
      * 'occlusion' [float] = '1'
      * 'roughness' [float]
        * Connected: '/World/Environment/Materials/Atlas_2048x2048_01/tex_roughness.outputs:r' @ '/World/Environment/Materials/Atlas_2048x2048_01/tex_roughness'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/Atlas_2048x2048_01_metallicRoughness_rough.jpg'
    * '/World/Environment/Materials/Atlas_2048x2048_01/tex_base' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/Atlas_2048x2048_01_baseColor.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'file' [asset] = '0/Atlas_2048x2048_01_baseColor.jpg'
      * 'st' [float2]
        * Connected: '/World/Environment/Materials/Atlas_2048x2048_01/uvset0.outputs:result' @ '/World/Environment/Materials/Atlas_2048x2048_01/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/Environment/Materials/Atlas_2048x2048_01/uvset0' (ID: 'UsdPrimvarReader_float2')
    * Implementation: 'id'
    * '/World/Environment/Materials/Atlas_2048x2048_01/tex_metallic' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/Atlas_2048x2048_01_metallicRoughness_metal_scale0.jpg'
    * Inputs:
      * 'fallback' [float4] = '(0.000, 0.000, 0.000, 1.000)'
      * 'file' [asset] = '0/Atlas_2048x2048_01_metallicRoughness_metal_scale0.jpg'
      * 'st' [float2]
        * Connected: '/World/Environment/Materials/Atlas_2048x2048_01/uvset0.outputs:result' @ '/World/Environment/Materials/Atlas_2048x2048_01/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/Environment/Materials/Atlas_2048x2048_01/tex_normal' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/Atlas_2048x2048_01_normal.jpg'
    * Inputs:
      * 'bias' [float4] = '(-1.000, -1.000, -1.000, -1.000)'
      * 'fallback' [float4] = '(0.000, 0.000, 1.000, 1.000)'
      * 'file' [asset] = '0/Atlas_2048x2048_01_normal.jpg'
      * 'scale' [float4] = '(2.000, 2.000, 2.000, 2.000)'
      * 'st' [float2]
        * Connected: '/World/Environment/Materials/Atlas_2048x2048_01/uvset0.outputs:result' @ '/World/Environment/Materials/Atlas_2048x2048_01/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/Environment/Materials/Atlas_2048x2048_01/tex_roughness' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/Atlas_2048x2048_01_metallicRoughness_rough.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 0.000, 0.000, 1.000)'
      * 'file' [asset] = '0/Atlas_2048x2048_01_metallicRoughness_rough.jpg'
      * 'st' [float2]
        * Connected: '/World/Environment/Materials/Atlas_2048x2048_01/uvset0.outputs:result' @ '/World/Environment/Materials/Atlas_2048x2048_01/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'

---

### /World/Environment/Materials/decalMoss01

* **Prim路径 (Prim Path):**/World/Environment/Materials/decalMoss01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/Environment/Materials/decalMoss01/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Environment/Materials/decalMoss01/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f]
        * Connected: '/World/Environment/Materials/decalMoss01/tex_base.outputs:rgb' @ '/World/Environment/Materials/decalMoss01/tex_base'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/decalMoss01_baseColor.png'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'opacity' [float]
        * Connected: '/World/Environment/Materials/decalMoss01/tex_base.outputs:a' @ '/World/Environment/Materials/decalMoss01/tex_base'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/decalMoss01_baseColor.png'
      * 'roughness' [float] = '0.821115'
    * '/World/Environment/Materials/decalMoss01/tex_base' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/decalMoss01_baseColor.png'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'file' [asset] = '0/decalMoss01_baseColor.png'
      * 'st' [float2]
        * Connected: '/World/Environment/Materials/decalMoss01/uvset0.outputs:result' @ '/World/Environment/Materials/decalMoss01/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/Environment/Materials/decalMoss01/uvset0' (ID: 'UsdPrimvarReader_float2')
    * Implementation: 'id'

---

### /World/Environment/Materials/woodenFence

* **Prim路径 (Prim Path):**/World/Environment/Materials/woodenFence
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/Environment/Materials/woodenFence/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Environment/Materials/woodenFence/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f]
        * Connected: '/World/Environment/Materials/woodenFence/tex_base.outputs:rgb' @ '/World/Environment/Materials/woodenFence/tex_base'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/woodenFence_baseColor.jpg'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float]
        * Connected: '/World/Environment/Materials/woodenFence/tex_metallic.outputs:r' @ '/World/Environment/Materials/woodenFence/tex_metallic'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/woodenFence_metallicRoughness_metal_scale0.jpg'
      * 'normal' [normal3f]
        * Connected: '/World/Environment/Materials/woodenFence/tex_normal.outputs:rgb' @ '/World/Environment/Materials/woodenFence/tex_normal'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/woodenFence_normal.jpg'
      * 'occlusion' [float] = '1'
      * 'roughness' [float]
        * Connected: '/World/Environment/Materials/woodenFence/tex_roughness.outputs:r' @ '/World/Environment/Materials/woodenFence/tex_roughness'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/woodenFence_metallicRoughness_rough.jpg'
    * '/World/Environment/Materials/woodenFence/tex_base' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/woodenFence_baseColor.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'file' [asset] = '0/woodenFence_baseColor.jpg'
      * 'st' [float2]
        * Connected: '/World/Environment/Materials/woodenFence/uvset0.outputs:result' @ '/World/Environment/Materials/woodenFence/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/Environment/Materials/woodenFence/uvset0' (ID: 'UsdPrimvarReader_float2')
    * Implementation: 'id'
    * '/World/Environment/Materials/woodenFence/tex_metallic' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/woodenFence_metallicRoughness_metal_scale0.jpg'
    * Inputs:
      * 'fallback' [float4] = '(0.000, 0.000, 0.000, 1.000)'
      * 'file' [asset] = '0/woodenFence_metallicRoughness_metal_scale0.jpg'
      * 'st' [float2]
        * Connected: '/World/Environment/Materials/woodenFence/uvset0.outputs:result' @ '/World/Environment/Materials/woodenFence/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/Environment/Materials/woodenFence/tex_normal' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/woodenFence_normal.jpg'
    * Inputs:
      * 'bias' [float4] = '(-1.000, -1.000, -1.000, -1.000)'
      * 'fallback' [float4] = '(0.000, 0.000, 1.000, 1.000)'
      * 'file' [asset] = '0/woodenFence_normal.jpg'
      * 'scale' [float4] = '(2.000, 2.000, 2.000, 2.000)'
      * 'st' [float2]
        * Connected: '/World/Environment/Materials/woodenFence/uvset0.outputs:result' @ '/World/Environment/Materials/woodenFence/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/Environment/Materials/woodenFence/tex_roughness' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/woodenFence_metallicRoughness_rough.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 0.000, 0.000, 1.000)'
      * 'file' [asset] = '0/woodenFence_metallicRoughness_rough.jpg'
      * 'st' [float2]
        * Connected: '/World/Environment/Materials/woodenFence/uvset0.outputs:result' @ '/World/Environment/Materials/woodenFence/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'

---

### /World/Environment/Materials/eletricBox_001

* **Prim路径 (Prim Path):**/World/Environment/Materials/eletricBox_001
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/Environment/Materials/eletricBox_001/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Environment/Materials/eletricBox_001/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f]
        * Connected: '/World/Environment/Materials/eletricBox_001/tex_base.outputs:rgb' @ '/World/Environment/Materials/eletricBox_001/tex_base'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/eletricBox.001_baseColor.jpg'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float]
        * Connected: '/World/Environment/Materials/eletricBox_001/tex_metallic.outputs:r' @ '/World/Environment/Materials/eletricBox_001/tex_metallic'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/eletricBox.001_metallicRoughness_metal.jpg'
      * 'normal' [normal3f]
        * Connected: '/World/Environment/Materials/eletricBox_001/tex_normal.outputs:rgb' @ '/World/Environment/Materials/eletricBox_001/tex_normal'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/eletricBox.001_normal.jpg'
      * 'occlusion' [float] = '1'
      * 'roughness' [float]
        * Connected: '/World/Environment/Materials/eletricBox_001/tex_roughness.outputs:r' @ '/World/Environment/Materials/eletricBox_001/tex_roughness'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/eletricBox.001_metallicRoughness_rough.jpg'
    * '/World/Environment/Materials/eletricBox_001/tex_base' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/eletricBox.001_baseColor.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'file' [asset] = '0/eletricBox.001_baseColor.jpg'
      * 'st' [float2]
        * Connected: '/World/Environment/Materials/eletricBox_001/uvset0.outputs:result' @ '/World/Environment/Materials/eletricBox_001/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/Environment/Materials/eletricBox_001/uvset0' (ID: 'UsdPrimvarReader_float2')
    * Implementation: 'id'
    * '/World/Environment/Materials/eletricBox_001/tex_metallic' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/eletricBox.001_metallicRoughness_metal.jpg'
    * Inputs:
      * 'fallback' [float4] = '(0.000, 0.000, 0.000, 1.000)'
      * 'file' [asset] = '0/eletricBox.001_metallicRoughness_metal.jpg'
      * 'st' [float2]
        * Connected: '/World/Environment/Materials/eletricBox_001/uvset0.outputs:result' @ '/World/Environment/Materials/eletricBox_001/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/Environment/Materials/eletricBox_001/tex_normal' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/eletricBox.001_normal.jpg'
    * Inputs:
      * 'bias' [float4] = '(-1.000, -1.000, -1.000, -1.000)'
      * 'fallback' [float4] = '(0.000, 0.000, 1.000, 1.000)'
      * 'file' [asset] = '0/eletricBox.001_normal.jpg'
      * 'scale' [float4] = '(2.000, 2.000, 2.000, 2.000)'
      * 'st' [float2]
        * Connected: '/World/Environment/Materials/eletricBox_001/uvset0.outputs:result' @ '/World/Environment/Materials/eletricBox_001/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/Environment/Materials/eletricBox_001/tex_roughness' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/eletricBox.001_metallicRoughness_rough.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 0.000, 0.000, 1.000)'
      * 'file' [asset] = '0/eletricBox.001_metallicRoughness_rough.jpg'
      * 'st' [float2]
        * Connected: '/World/Environment/Materials/eletricBox_001/uvset0.outputs:result' @ '/World/Environment/Materials/eletricBox_001/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'

---

### /World/Environment/Materials/air_conditioning_001

* **Prim路径 (Prim Path):**/World/Environment/Materials/air_conditioning_001
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/Environment/Materials/air_conditioning_001/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Environment/Materials/air_conditioning_001/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f]
        * Connected: '/World/Environment/Materials/air_conditioning_001/tex_base.outputs:rgb' @ '/World/Environment/Materials/air_conditioning_001/tex_base'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/air_conditioning.001_baseColor.jpg'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float]
        * Connected: '/World/Environment/Materials/air_conditioning_001/tex_metallic.outputs:r' @ '/World/Environment/Materials/air_conditioning_001/tex_metallic'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/air_conditioning.001_metallicRoughness_metal_scale0.jpg'
      * 'normal' [normal3f]
        * Connected: '/World/Environment/Materials/air_conditioning_001/tex_normal.outputs:rgb' @ '/World/Environment/Materials/air_conditioning_001/tex_normal'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/air_conditioning.001_normal.jpg'
      * 'occlusion' [float] = '1'
      * 'roughness' [float]
        * Connected: '/World/Environment/Materials/air_conditioning_001/tex_roughness.outputs:r' @ '/World/Environment/Materials/air_conditioning_001/tex_roughness'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/air_conditioning.001_metallicRoughness_rough.jpg'
    * '/World/Environment/Materials/air_conditioning_001/tex_base' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/air_conditioning.001_baseColor.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'file' [asset] = '0/air_conditioning.001_baseColor.jpg'
      * 'st' [float2]
        * Connected: '/World/Environment/Materials/air_conditioning_001/uvset0.outputs:result' @ '/World/Environment/Materials/air_conditioning_001/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/Environment/Materials/air_conditioning_001/uvset0' (ID: 'UsdPrimvarReader_float2')
    * Implementation: 'id'
    * '/World/Environment/Materials/air_conditioning_001/tex_metallic' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/air_conditioning.001_metallicRoughness_metal_scale0.jpg'
    * Inputs:
      * 'fallback' [float4] = '(0.000, 0.000, 0.000, 1.000)'
      * 'file' [asset] = '0/air_conditioning.001_metallicRoughness_metal_scale0.jpg'
      * 'st' [float2]
        * Connected: '/World/Environment/Materials/air_conditioning_001/uvset0.outputs:result' @ '/World/Environment/Materials/air_conditioning_001/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/Environment/Materials/air_conditioning_001/tex_normal' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/air_conditioning.001_normal.jpg'
    * Inputs:
      * 'bias' [float4] = '(-1.000, -1.000, -1.000, -1.000)'
      * 'fallback' [float4] = '(0.000, 0.000, 1.000, 1.000)'
      * 'file' [asset] = '0/air_conditioning.001_normal.jpg'
      * 'scale' [float4] = '(2.000, 2.000, 2.000, 2.000)'
      * 'st' [float2]
        * Connected: '/World/Environment/Materials/air_conditioning_001/uvset0.outputs:result' @ '/World/Environment/Materials/air_conditioning_001/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/Environment/Materials/air_conditioning_001/tex_roughness' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/air_conditioning.001_metallicRoughness_rough.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 0.000, 0.000, 1.000)'
      * 'file' [asset] = '0/air_conditioning.001_metallicRoughness_rough.jpg'
      * 'st' [float2]
        * Connected: '/World/Environment/Materials/air_conditioning_001/uvset0.outputs:result' @ '/World/Environment/Materials/air_conditioning_001/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'

---

### /World/Environment/Materials/vents

* **Prim路径 (Prim Path):**/World/Environment/Materials/vents
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/Environment/Materials/vents/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Environment/Materials/vents/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f]
        * Connected: '/World/Environment/Materials/vents/tex_base.outputs:rgb' @ '/World/Environment/Materials/vents/tex_base'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/vents_baseColor.jpg'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float]
        * Connected: '/World/Environment/Materials/vents/tex_metallic.outputs:r' @ '/World/Environment/Materials/vents/tex_metallic'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/vents_metallicRoughness_metal_scale0.jpg'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float]
        * Connected: '/World/Environment/Materials/vents/tex_roughness.outputs:r' @ '/World/Environment/Materials/vents/tex_roughness'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/vents_metallicRoughness_rough.jpg'
    * '/World/Environment/Materials/vents/tex_base' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/vents_baseColor.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'file' [asset] = '0/vents_baseColor.jpg'
      * 'st' [float2]
        * Connected: '/World/Environment/Materials/vents/uvset0.outputs:result' @ '/World/Environment/Materials/vents/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/Environment/Materials/vents/uvset0' (ID: 'UsdPrimvarReader_float2')
    * Implementation: 'id'
    * '/World/Environment/Materials/vents/tex_metallic' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/vents_metallicRoughness_metal_scale0.jpg'
    * Inputs:
      * 'fallback' [float4] = '(0.000, 0.000, 0.000, 1.000)'
      * 'file' [asset] = '0/vents_metallicRoughness_metal_scale0.jpg'
      * 'st' [float2]
        * Connected: '/World/Environment/Materials/vents/uvset0.outputs:result' @ '/World/Environment/Materials/vents/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/Environment/Materials/vents/tex_roughness' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/vents_metallicRoughness_rough.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 0.000, 0.000, 1.000)'
      * 'file' [asset] = '0/vents_metallicRoughness_rough.jpg'
      * 'st' [float2]
        * Connected: '/World/Environment/Materials/vents/uvset0.outputs:result' @ '/World/Environment/Materials/vents/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'

---

### /World/Environment/Materials/roofingSheets

* **Prim路径 (Prim Path):**/World/Environment/Materials/roofingSheets
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/Environment/Materials/roofingSheets/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Environment/Materials/roofingSheets/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f]
        * Connected: '/World/Environment/Materials/roofingSheets/tex_base.outputs:rgb' @ '/World/Environment/Materials/roofingSheets/tex_base'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/roofingSheets_baseColor.jpg'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float]
        * Connected: '/World/Environment/Materials/roofingSheets/tex_metallic.outputs:r' @ '/World/Environment/Materials/roofingSheets/tex_metallic'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/roofingSheets_metallicRoughness_metal_scale0.jpg'
      * 'normal' [normal3f]
        * Connected: '/World/Environment/Materials/roofingSheets/tex_normal.outputs:rgb' @ '/World/Environment/Materials/roofingSheets/tex_normal'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/roofingSheets_normal.jpg'
      * 'occlusion' [float] = '1'
      * 'roughness' [float]
        * Connected: '/World/Environment/Materials/roofingSheets/tex_roughness.outputs:r' @ '/World/Environment/Materials/roofingSheets/tex_roughness'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/roofingSheets_metallicRoughness_rough_scale1.jpg'
    * '/World/Environment/Materials/roofingSheets/tex_base' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/roofingSheets_baseColor.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'file' [asset] = '0/roofingSheets_baseColor.jpg'
      * 'st' [float2]
        * Connected: '/World/Environment/Materials/roofingSheets/uvset0.outputs:result' @ '/World/Environment/Materials/roofingSheets/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/Environment/Materials/roofingSheets/uvset0' (ID: 'UsdPrimvarReader_float2')
    * Implementation: 'id'
    * '/World/Environment/Materials/roofingSheets/tex_metallic' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/roofingSheets_metallicRoughness_metal_scale0.jpg'
    * Inputs:
      * 'fallback' [float4] = '(0.000, 0.000, 0.000, 1.000)'
      * 'file' [asset] = '0/roofingSheets_metallicRoughness_metal_scale0.jpg'
      * 'st' [float2]
        * Connected: '/World/Environment/Materials/roofingSheets/uvset0.outputs:result' @ '/World/Environment/Materials/roofingSheets/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/Environment/Materials/roofingSheets/tex_normal' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/roofingSheets_normal.jpg'
    * Inputs:
      * 'bias' [float4] = '(-1.000, -1.000, -1.000, -1.000)'
      * 'fallback' [float4] = '(0.000, 0.000, 1.000, 1.000)'
      * 'file' [asset] = '0/roofingSheets_normal.jpg'
      * 'scale' [float4] = '(2.000, 2.000, 2.000, 2.000)'
      * 'st' [float2]
        * Connected: '/World/Environment/Materials/roofingSheets/uvset0.outputs:result' @ '/World/Environment/Materials/roofingSheets/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/Environment/Materials/roofingSheets/tex_roughness' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/roofingSheets_metallicRoughness_rough_scale1.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 0.000, 0.000, 1.000)'
      * 'file' [asset] = '0/roofingSheets_metallicRoughness_rough_scale1.jpg'
      * 'st' [float2]
        * Connected: '/World/Environment/Materials/roofingSheets/uvset0.outputs:result' @ '/World/Environment/Materials/roofingSheets/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'

---

### /World/Environment/Materials/emptyBillboard

* **Prim路径 (Prim Path):**/World/Environment/Materials/emptyBillboard
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/Environment/Materials/emptyBillboard/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Environment/Materials/emptyBillboard/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f]
        * Connected: '/World/Environment/Materials/emptyBillboard/tex_base.outputs:rgb' @ '/World/Environment/Materials/emptyBillboard/tex_base'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/emptyBillboard_baseColor.jpg'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0.821115'
    * '/World/Environment/Materials/emptyBillboard/tex_base' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/emptyBillboard_baseColor.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'file' [asset] = '0/emptyBillboard_baseColor.jpg'
      * 'st' [float2]
        * Connected: '/World/Environment/Materials/emptyBillboard/uvset0.outputs:result' @ '/World/Environment/Materials/emptyBillboard/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/Environment/Materials/emptyBillboard/uvset0' (ID: 'UsdPrimvarReader_float2')
    * Implementation: 'id'

---

### /World/Workbench_1/Looks/Metal_Glossy_A_MetalWorktable_A

* **Prim路径 (Prim Path):**/World/Workbench_1/Looks/Metal_Glossy_A_MetalWorktable_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Workbench_1/Looks/Metal_Glossy_A_MetalWorktable_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Workbench_1/Looks/Metal_Glossy_A_MetalWorktable_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../../../../../Materials/Base/Metals/Metal_Glossy_A.mdl' (Sub Id: 'Metal_Glossy_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/5.0/NVIDIA/Assets/DigitalTwin/Materials/Base/Metals/Metal_Glossy_A.mdl'

---

### /World/Workbench_1/Looks/MetalPainted_Gray_Glossy_A_MetalWorktable_A

* **Prim路径 (Prim Path):**/World/Workbench_1/Looks/MetalPainted_Gray_Glossy_A_MetalWorktable_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface'

---

### /World/Workbench_1/Looks/Plastic_Black_A_MetalWorktable_A

* **Prim路径 (Prim Path):**/World/Workbench_1/Looks/Plastic_Black_A_MetalWorktable_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Workbench_1/Looks/Plastic_Black_A_MetalWorktable_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Workbench_1/Looks/Plastic_Black_A_MetalWorktable_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../../../../../Materials/Base/Plastics/Plastic_Black_A.mdl' (Sub Id: 'Plastic_Black_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/5.0/NVIDIA/Assets/DigitalTwin/Materials/Base/Plastics/Plastic_Black_A.mdl'

---

### /World/Workbench_1/Looks/Wood_Maple_MetalWorktable_A

* **Prim路径 (Prim Path):**/World/Workbench_1/Looks/Wood_Maple_MetalWorktable_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Workbench_1/Looks/Wood_Maple_MetalWorktable_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Workbench_1/Looks/Wood_Maple_MetalWorktable_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * 纹理引用 (Texture Assets):
      * './materials/T_MetalWorktable_A01_Albedo.png'
      * './materials/T_MetalWorktable_A01_Normal.png'
      * './materials/T_MetalWorktable_A01_ORM.png'
    * Inputs:
      * 'diffuse_texture' [asset] = './materials/T_MetalWorktable_A01_Albedo.png'
      * 'metallic_texture_influence' [float] = '1'
      * 'normalmap_texture' [asset] = './materials/T_MetalWorktable_A01_Normal.png'
      * 'ORM_texture' [asset] = './materials/T_MetalWorktable_A01_ORM.png'
      * 'reflection_roughness_texture_influence' [float] = '1'

---

### /World/Workbench_2/Looks/Metal_Glossy_A_MetalWorktable_A

* **Prim路径 (Prim Path):**/World/Workbench_2/Looks/Metal_Glossy_A_MetalWorktable_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Workbench_2/Looks/Metal_Glossy_A_MetalWorktable_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Workbench_2/Looks/Metal_Glossy_A_MetalWorktable_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../../../../../Materials/Base/Metals/Metal_Glossy_A.mdl' (Sub Id: 'Metal_Glossy_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/5.0/NVIDIA/Assets/DigitalTwin/Materials/Base/Metals/Metal_Glossy_A.mdl'

---

### /World/Workbench_2/Looks/MetalPainted_Gray_Glossy_A_MetalWorktable_A

* **Prim路径 (Prim Path):**/World/Workbench_2/Looks/MetalPainted_Gray_Glossy_A_MetalWorktable_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface'

---

### /World/Workbench_2/Looks/Plastic_Black_A_MetalWorktable_A

* **Prim路径 (Prim Path):**/World/Workbench_2/Looks/Plastic_Black_A_MetalWorktable_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Workbench_2/Looks/Plastic_Black_A_MetalWorktable_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Workbench_2/Looks/Plastic_Black_A_MetalWorktable_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../../../../../Materials/Base/Plastics/Plastic_Black_A.mdl' (Sub Id: 'Plastic_Black_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/5.0/NVIDIA/Assets/DigitalTwin/Materials/Base/Plastics/Plastic_Black_A.mdl'

---

### /World/Workbench_2/Looks/Wood_Maple_MetalWorktable_A

* **Prim路径 (Prim Path):**/World/Workbench_2/Looks/Wood_Maple_MetalWorktable_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Workbench_2/Looks/Wood_Maple_MetalWorktable_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Workbench_2/Looks/Wood_Maple_MetalWorktable_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * 纹理引用 (Texture Assets):
      * './materials/T_MetalWorktable_A01_Albedo.png'
      * './materials/T_MetalWorktable_A01_Normal.png'
      * './materials/T_MetalWorktable_A01_ORM.png'
    * Inputs:
      * 'diffuse_texture' [asset] = './materials/T_MetalWorktable_A01_Albedo.png'
      * 'metallic_texture_influence' [float] = '1'
      * 'normalmap_texture' [asset] = './materials/T_MetalWorktable_A01_Normal.png'
      * 'ORM_texture' [asset] = './materials/T_MetalWorktable_A01_ORM.png'
      * 'reflection_roughness_texture_influence' [float] = '1'

---

### /World/Workbench_3/Looks/Metal_Glossy_A_MetalWorktable_A

* **Prim路径 (Prim Path):**/World/Workbench_3/Looks/Metal_Glossy_A_MetalWorktable_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Workbench_3/Looks/Metal_Glossy_A_MetalWorktable_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Workbench_3/Looks/Metal_Glossy_A_MetalWorktable_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../../../../../Materials/Base/Metals/Metal_Glossy_A.mdl' (Sub Id: 'Metal_Glossy_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/5.0/NVIDIA/Assets/DigitalTwin/Materials/Base/Metals/Metal_Glossy_A.mdl'

---

### /World/Workbench_3/Looks/MetalPainted_Gray_Glossy_A_MetalWorktable_A

* **Prim路径 (Prim Path):**/World/Workbench_3/Looks/MetalPainted_Gray_Glossy_A_MetalWorktable_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface'

---

### /World/Workbench_3/Looks/Plastic_Black_A_MetalWorktable_A

* **Prim路径 (Prim Path):**/World/Workbench_3/Looks/Plastic_Black_A_MetalWorktable_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Workbench_3/Looks/Plastic_Black_A_MetalWorktable_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Workbench_3/Looks/Plastic_Black_A_MetalWorktable_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../../../../../Materials/Base/Plastics/Plastic_Black_A.mdl' (Sub Id: 'Plastic_Black_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/5.0/NVIDIA/Assets/DigitalTwin/Materials/Base/Plastics/Plastic_Black_A.mdl'

---

### /World/Workbench_3/Looks/Wood_Maple_MetalWorktable_A

* **Prim路径 (Prim Path):**/World/Workbench_3/Looks/Wood_Maple_MetalWorktable_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Workbench_3/Looks/Wood_Maple_MetalWorktable_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Workbench_3/Looks/Wood_Maple_MetalWorktable_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * 纹理引用 (Texture Assets):
      * './materials/T_MetalWorktable_A01_Albedo.png'
      * './materials/T_MetalWorktable_A01_Normal.png'
      * './materials/T_MetalWorktable_A01_ORM.png'
    * Inputs:
      * 'diffuse_texture' [asset] = './materials/T_MetalWorktable_A01_Albedo.png'
      * 'metallic_texture_influence' [float] = '1'
      * 'normalmap_texture' [asset] = './materials/T_MetalWorktable_A01_Normal.png'
      * 'ORM_texture' [asset] = './materials/T_MetalWorktable_A01_ORM.png'
      * 'reflection_roughness_texture_influence' [float] = '1'

---

### /World/Workbench_4/Looks/Metal_Glossy_A_MetalWorktable_A

* **Prim路径 (Prim Path):**/World/Workbench_4/Looks/Metal_Glossy_A_MetalWorktable_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Workbench_4/Looks/Metal_Glossy_A_MetalWorktable_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Workbench_4/Looks/Metal_Glossy_A_MetalWorktable_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../../../../../Materials/Base/Metals/Metal_Glossy_A.mdl' (Sub Id: 'Metal_Glossy_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/5.0/NVIDIA/Assets/DigitalTwin/Materials/Base/Metals/Metal_Glossy_A.mdl'

---

### /World/Workbench_4/Looks/MetalPainted_Gray_Glossy_A_MetalWorktable_A

* **Prim路径 (Prim Path):**/World/Workbench_4/Looks/MetalPainted_Gray_Glossy_A_MetalWorktable_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface'

---

### /World/Workbench_4/Looks/Plastic_Black_A_MetalWorktable_A

* **Prim路径 (Prim Path):**/World/Workbench_4/Looks/Plastic_Black_A_MetalWorktable_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Workbench_4/Looks/Plastic_Black_A_MetalWorktable_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Workbench_4/Looks/Plastic_Black_A_MetalWorktable_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../../../../../Materials/Base/Plastics/Plastic_Black_A.mdl' (Sub Id: 'Plastic_Black_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/5.0/NVIDIA/Assets/DigitalTwin/Materials/Base/Plastics/Plastic_Black_A.mdl'

---

### /World/Workbench_4/Looks/Wood_Maple_MetalWorktable_A

* **Prim路径 (Prim Path):**/World/Workbench_4/Looks/Wood_Maple_MetalWorktable_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Workbench_4/Looks/Wood_Maple_MetalWorktable_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Workbench_4/Looks/Wood_Maple_MetalWorktable_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * 纹理引用 (Texture Assets):
      * './materials/T_MetalWorktable_A01_Albedo.png'
      * './materials/T_MetalWorktable_A01_Normal.png'
      * './materials/T_MetalWorktable_A01_ORM.png'
    * Inputs:
      * 'diffuse_texture' [asset] = './materials/T_MetalWorktable_A01_Albedo.png'
      * 'metallic_texture_influence' [float] = '1'
      * 'normalmap_texture' [asset] = './materials/T_MetalWorktable_A01_Normal.png'
      * 'ORM_texture' [asset] = './materials/T_MetalWorktable_A01_ORM.png'
      * 'reflection_roughness_texture_influence' [float] = '1'

---

### /World/Workbench_5/Looks/Metal_Glossy_A_MetalWorktable_A

* **Prim路径 (Prim Path):**/World/Workbench_5/Looks/Metal_Glossy_A_MetalWorktable_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Workbench_5/Looks/Metal_Glossy_A_MetalWorktable_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Workbench_5/Looks/Metal_Glossy_A_MetalWorktable_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../../../../../Materials/Base/Metals/Metal_Glossy_A.mdl' (Sub Id: 'Metal_Glossy_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/5.0/NVIDIA/Assets/DigitalTwin/Materials/Base/Metals/Metal_Glossy_A.mdl'

---

### /World/Workbench_5/Looks/MetalPainted_Gray_Glossy_A_MetalWorktable_A

* **Prim路径 (Prim Path):**/World/Workbench_5/Looks/MetalPainted_Gray_Glossy_A_MetalWorktable_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface'

---

### /World/Workbench_5/Looks/Plastic_Black_A_MetalWorktable_A

* **Prim路径 (Prim Path):**/World/Workbench_5/Looks/Plastic_Black_A_MetalWorktable_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Workbench_5/Looks/Plastic_Black_A_MetalWorktable_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Workbench_5/Looks/Plastic_Black_A_MetalWorktable_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../../../../../Materials/Base/Plastics/Plastic_Black_A.mdl' (Sub Id: 'Plastic_Black_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/5.0/NVIDIA/Assets/DigitalTwin/Materials/Base/Plastics/Plastic_Black_A.mdl'

---

### /World/Workbench_5/Looks/Wood_Maple_MetalWorktable_A

* **Prim路径 (Prim Path):**/World/Workbench_5/Looks/Wood_Maple_MetalWorktable_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Workbench_5/Looks/Wood_Maple_MetalWorktable_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Workbench_5/Looks/Wood_Maple_MetalWorktable_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * 纹理引用 (Texture Assets):
      * './materials/T_MetalWorktable_A01_Albedo.png'
      * './materials/T_MetalWorktable_A01_Normal.png'
      * './materials/T_MetalWorktable_A01_ORM.png'
    * Inputs:
      * 'diffuse_texture' [asset] = './materials/T_MetalWorktable_A01_Albedo.png'
      * 'metallic_texture_influence' [float] = '1'
      * 'normalmap_texture' [asset] = './materials/T_MetalWorktable_A01_Normal.png'
      * 'ORM_texture' [asset] = './materials/T_MetalWorktable_A01_ORM.png'
      * 'reflection_roughness_texture_influence' [float] = '1'

---

### /World/Workbench_6/Looks/Metal_Glossy_A_MetalWorktable_A

* **Prim路径 (Prim Path):**/World/Workbench_6/Looks/Metal_Glossy_A_MetalWorktable_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Workbench_6/Looks/Metal_Glossy_A_MetalWorktable_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Workbench_6/Looks/Metal_Glossy_A_MetalWorktable_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../../../../../Materials/Base/Metals/Metal_Glossy_A.mdl' (Sub Id: 'Metal_Glossy_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/5.0/NVIDIA/Assets/DigitalTwin/Materials/Base/Metals/Metal_Glossy_A.mdl'

---

### /World/Workbench_6/Looks/MetalPainted_Gray_Glossy_A_MetalWorktable_A

* **Prim路径 (Prim Path):**/World/Workbench_6/Looks/MetalPainted_Gray_Glossy_A_MetalWorktable_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface'

---

### /World/Workbench_6/Looks/Plastic_Black_A_MetalWorktable_A

* **Prim路径 (Prim Path):**/World/Workbench_6/Looks/Plastic_Black_A_MetalWorktable_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Workbench_6/Looks/Plastic_Black_A_MetalWorktable_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Workbench_6/Looks/Plastic_Black_A_MetalWorktable_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../../../../../Materials/Base/Plastics/Plastic_Black_A.mdl' (Sub Id: 'Plastic_Black_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/5.0/NVIDIA/Assets/DigitalTwin/Materials/Base/Plastics/Plastic_Black_A.mdl'

---

### /World/Workbench_6/Looks/Wood_Maple_MetalWorktable_A

* **Prim路径 (Prim Path):**/World/Workbench_6/Looks/Wood_Maple_MetalWorktable_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Workbench_6/Looks/Wood_Maple_MetalWorktable_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Workbench_6/Looks/Wood_Maple_MetalWorktable_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * 纹理引用 (Texture Assets):
      * './materials/T_MetalWorktable_A01_Albedo.png'
      * './materials/T_MetalWorktable_A01_Normal.png'
      * './materials/T_MetalWorktable_A01_ORM.png'
    * Inputs:
      * 'diffuse_texture' [asset] = './materials/T_MetalWorktable_A01_Albedo.png'
      * 'metallic_texture_influence' [float] = '1'
      * 'normalmap_texture' [asset] = './materials/T_MetalWorktable_A01_Normal.png'
      * 'ORM_texture' [asset] = './materials/T_MetalWorktable_A01_ORM.png'
      * 'reflection_roughness_texture_influence' [float] = '1'

---

### /World/Workbench_7/Looks/Metal_Glossy_A_MetalWorktable_A

* **Prim路径 (Prim Path):**/World/Workbench_7/Looks/Metal_Glossy_A_MetalWorktable_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Workbench_7/Looks/Metal_Glossy_A_MetalWorktable_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Workbench_7/Looks/Metal_Glossy_A_MetalWorktable_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../../../../../Materials/Base/Metals/Metal_Glossy_A.mdl' (Sub Id: 'Metal_Glossy_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/5.0/NVIDIA/Assets/DigitalTwin/Materials/Base/Metals/Metal_Glossy_A.mdl'

---

### /World/Workbench_7/Looks/MetalPainted_Gray_Glossy_A_MetalWorktable_A

* **Prim路径 (Prim Path):**/World/Workbench_7/Looks/MetalPainted_Gray_Glossy_A_MetalWorktable_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface'

---

### /World/Workbench_7/Looks/Plastic_Black_A_MetalWorktable_A

* **Prim路径 (Prim Path):**/World/Workbench_7/Looks/Plastic_Black_A_MetalWorktable_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Workbench_7/Looks/Plastic_Black_A_MetalWorktable_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Workbench_7/Looks/Plastic_Black_A_MetalWorktable_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../../../../../Materials/Base/Plastics/Plastic_Black_A.mdl' (Sub Id: 'Plastic_Black_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/5.0/NVIDIA/Assets/DigitalTwin/Materials/Base/Plastics/Plastic_Black_A.mdl'

---

### /World/Workbench_7/Looks/Wood_Maple_MetalWorktable_A

* **Prim路径 (Prim Path):**/World/Workbench_7/Looks/Wood_Maple_MetalWorktable_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Workbench_7/Looks/Wood_Maple_MetalWorktable_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Workbench_7/Looks/Wood_Maple_MetalWorktable_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * 纹理引用 (Texture Assets):
      * './materials/T_MetalWorktable_A01_Albedo.png'
      * './materials/T_MetalWorktable_A01_Normal.png'
      * './materials/T_MetalWorktable_A01_ORM.png'
    * Inputs:
      * 'diffuse_texture' [asset] = './materials/T_MetalWorktable_A01_Albedo.png'
      * 'metallic_texture_influence' [float] = '1'
      * 'normalmap_texture' [asset] = './materials/T_MetalWorktable_A01_Normal.png'
      * 'ORM_texture' [asset] = './materials/T_MetalWorktable_A01_ORM.png'
      * 'reflection_roughness_texture_influence' [float] = '1'

---

### /World/Conveyor_1/Looks/Acrylic_Clear_Glossy_A

* **Prim路径 (Prim Path):**/World/Conveyor_1/Looks/Acrylic_Clear_Glossy_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_1/Looks/Acrylic_Clear_Glossy_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_1/Looks/Acrylic_Clear_Glossy_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniGlass.mdl' (Sub Id: 'OmniGlass')
    * 纹理引用 (Texture Assets):
      * '../Material Library/Plastic/Textures/T_Acrylic_Clear_Glossy_A_Rough.png'
      * '../Material Library/Plastic/Textures/T_Plastic_Rough_Black_A_Normal.png'
    * Inputs:
      * 'normal_map_strength' [float] = '0.5'
      * 'texture_scale' [float2] = '(1.000, 3.000)'
      * 'normal_map_texture' [asset] = '../Material Library/Plastic/Textures/T_Plastic_Rough_Black_A_Normal.png'
      * 'roughness_texture' [asset] = '../Material Library/Plastic/Textures/T_Acrylic_Clear_Glossy_A_Rough.png'
      * 'roughness_texture_influence' [float] = '0.3'
      * 'glass_ior' [float] = '1.05'
      * 'frosting_roughness' [float] = '0.17'
      * 'glass_color' [color3f] = '(0.734, 0.734, 0.734)'

---

### /World/Conveyor_1/Looks/M_ConveyorBelt_A01_Belt

* **Prim路径 (Prim Path):**/World/Conveyor_1/Looks/M_ConveyorBelt_A01_Belt
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_1/Looks/M_ConveyorBelt_A01_Belt/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_1/Looks/M_ConveyorBelt_A01_Belt/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * 纹理引用 (Texture Assets):
      * './T_ConveyorBelt_A01_Belt_Albedo.png'
      * './T_ConveyorBelt_A01_Belt_Normal.png'
      * './T_ConveyorBelt_A01_Belt_ORM.png'
    * Inputs:
      * 'normalmap_texture' [asset] = './T_ConveyorBelt_A01_Belt_Normal.png'
      * 'diffuse_texture' [asset] = './T_ConveyorBelt_A01_Belt_Albedo.png'
      * 'reflection_roughness_texture_influence' [float] = '1'
      * 'metallic_texture_influence' [float] = '1'
      * 'ORM_texture' [asset] = './T_ConveyorBelt_A01_Belt_ORM.png'

---

### /World/Conveyor_1/Looks/M_ConveyorBelt_A01_Decal

* **Prim路径 (Prim Path):**/World/Conveyor_1/Looks/M_ConveyorBelt_A01_Decal
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_1/Looks/M_ConveyorBelt_A01_Decal/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_1/Looks/M_ConveyorBelt_A01_Decal/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * 纹理引用 (Texture Assets):
      * './T_ConveyorsBelt_A01_Decal_Albedo.png'
      * './T_ConveyorsBelt_A01_Decal_Alpha.png'
      * './T_ConveyorsBelt_A01_Decal_ORM.png'
    * Inputs:
      * 'opacity_texture' [asset] = './T_ConveyorsBelt_A01_Decal_Alpha.png'
      * 'diffuse_texture' [asset] = './T_ConveyorsBelt_A01_Decal_Albedo.png'
      * 'reflection_roughness_texture_influence' [float] = '1'
      * 'metallic_texture_influence' [float] = '1'
      * 'ORM_texture' [asset] = './T_ConveyorsBelt_A01_Decal_ORM.png'

---

### /World/Conveyor_1/Looks/Metal_Rough_A

* **Prim路径 (Prim Path):**/World/Conveyor_1/Looks/Metal_Rough_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_1/Looks/Metal_Rough_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_1/Looks/Metal_Rough_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Metal/Misc/Metal_Rough_A.mdl' (Sub Id: 'Metal_Rough_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Metal/Misc/Metal_Rough_A.mdl'

---

### /World/Conveyor_1/Looks/MetalPainted_Black_Glossy_A

* **Prim路径 (Prim Path):**/World/Conveyor_1/Looks/MetalPainted_Black_Glossy_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_1/Looks/MetalPainted_Black_Glossy_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_1/Looks/MetalPainted_Black_Glossy_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Metal/Painted/MetalPainted_White_Glossy_A.mdl' (Sub Id: 'MetalPainted_White_Glossy_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Metal/Painted/MetalPainted_White_Glossy_A.mdl'
    * Inputs:
      * 'bump_factor' [float] = '0.5'
      * 'texture_scale' [float2] = '(1.500, 1.500)'
      * 'diffuse_tint' [color3f] = '(0.066, 0.066, 0.066)'
      * 'reflection_roughness_constant' [float] = '0.63'
      * 'reflection_roughness_texture_influence' [float] = '0.91'

---

### /World/Conveyor_1/Looks/MetalPainted_Blue_Glossy_A

* **Prim路径 (Prim Path):**/World/Conveyor_1/Looks/MetalPainted_Blue_Glossy_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_1/Looks/MetalPainted_Blue_Glossy_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_1/Looks/MetalPainted_Blue_Glossy_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Metal/Painted/MetalPainted_White_Glossy_A.mdl' (Sub Id: 'MetalPainted_White_Glossy_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Metal/Painted/MetalPainted_White_Glossy_A.mdl'
    * 纹理引用 (Texture Assets):
      * '../Material Library/Metal/Painted/T_MetalPainted_White_Glossy_A_Albedo.png'
      * '../Material Library/Metal/Painted/T_MetalPainted_White_Glossy_A_Normal.png'
      * '../Material Library/Metal/Painted/T_MetalPainted_White_Glossy_A_ORM.png'
    * Inputs:
      * 'bump_factor' [float] = '0.5'
      * 'normalmap_texture' [asset] = '../Material Library/Metal/Painted/T_MetalPainted_White_Glossy_A_Normal.png'
      * 'texture_scale' [float2] = '(1.500, 1.500)'
      * 'diffuse_texture' [asset] = '../Material Library/Metal/Painted/T_MetalPainted_White_Glossy_A_Albedo.png'
      * 'diffuse_tint' [color3f] = '(0.077, 0.203, 0.587)'
      * 'ORM_texture' [asset] = '../Material Library/Metal/Painted/T_MetalPainted_White_Glossy_A_ORM.png'

---

### /World/Conveyor_1/Looks/Plastic_Orange_A

* **Prim路径 (Prim Path):**/World/Conveyor_1/Looks/Plastic_Orange_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_1/Looks/Plastic_Orange_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_1/Looks/Plastic_Orange_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Plastic/Misc/Plastic_Orange_A.mdl' (Sub Id: 'Plastic_Orange_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Plastic/Misc/Plastic_Orange_A.mdl'

---

### /World/Conveyor_1/Looks/Plastic_Red_A

* **Prim路径 (Prim Path):**/World/Conveyor_1/Looks/Plastic_Red_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_1/Looks/Plastic_Red_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_1/Looks/Plastic_Red_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Plastic/Misc/Plastic_Red_A.mdl' (Sub Id: 'Plastic_Red_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Plastic/Misc/Plastic_Red_A.mdl'

---

### /World/Conveyor_1/Looks/Plastic_Rough_Black_A

* **Prim路径 (Prim Path):**/World/Conveyor_1/Looks/Plastic_Rough_Black_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_1/Looks/Plastic_Rough_Black_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_1/Looks/Plastic_Rough_Black_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Plastic/Misc/Plastic_Rough_Black_A.mdl' (Sub Id: 'Plastic_Rough_Black_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Plastic/Misc/Plastic_Rough_Black_A.mdl'

---

### /World/Conveyor_1/Looks/Steel_A

* **Prim路径 (Prim Path):**/World/Conveyor_1/Looks/Steel_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_1/Looks/Steel_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_1/Looks/Steel_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Metal/Steel/Steel_A.mdl' (Sub Id: 'Steel_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Metal/Steel/Steel_A.mdl'
    * Inputs:
      * 'diffuse_tint' [color3f] = '(0.772, 0.772, 0.772)'
      * 'reflection_roughness_constant' [float] = '0.67'
      * 'reflection_roughness_texture_influence' [float] = '0.88'

---

### /World/Conveyor_2/Looks/Acrylic_Clear_Glossy_A

* **Prim路径 (Prim Path):**/World/Conveyor_2/Looks/Acrylic_Clear_Glossy_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_2/Looks/Acrylic_Clear_Glossy_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_2/Looks/Acrylic_Clear_Glossy_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniGlass.mdl' (Sub Id: 'OmniGlass')
    * 纹理引用 (Texture Assets):
      * '../Material Library/Plastic/Textures/T_Acrylic_Clear_Glossy_A_Rough.png'
      * '../Material Library/Plastic/Textures/T_Plastic_Rough_Black_A_Normal.png'
    * Inputs:
      * 'normal_map_strength' [float] = '0.5'
      * 'texture_scale' [float2] = '(1.000, 3.000)'
      * 'normal_map_texture' [asset] = '../Material Library/Plastic/Textures/T_Plastic_Rough_Black_A_Normal.png'
      * 'roughness_texture' [asset] = '../Material Library/Plastic/Textures/T_Acrylic_Clear_Glossy_A_Rough.png'
      * 'roughness_texture_influence' [float] = '0.3'
      * 'glass_ior' [float] = '1.05'
      * 'frosting_roughness' [float] = '0.17'
      * 'glass_color' [color3f] = '(0.734, 0.734, 0.734)'

---

### /World/Conveyor_2/Looks/M_ConveyorBelt_A01_Belt

* **Prim路径 (Prim Path):**/World/Conveyor_2/Looks/M_ConveyorBelt_A01_Belt
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_2/Looks/M_ConveyorBelt_A01_Belt/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_2/Looks/M_ConveyorBelt_A01_Belt/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * 纹理引用 (Texture Assets):
      * './T_ConveyorBelt_A01_Belt_Albedo.png'
      * './T_ConveyorBelt_A01_Belt_Normal.png'
      * './T_ConveyorBelt_A01_Belt_ORM.png'
    * Inputs:
      * 'normalmap_texture' [asset] = './T_ConveyorBelt_A01_Belt_Normal.png'
      * 'diffuse_texture' [asset] = './T_ConveyorBelt_A01_Belt_Albedo.png'
      * 'reflection_roughness_texture_influence' [float] = '1'
      * 'metallic_texture_influence' [float] = '1'
      * 'ORM_texture' [asset] = './T_ConveyorBelt_A01_Belt_ORM.png'

---

### /World/Conveyor_2/Looks/M_ConveyorBelt_A01_Decal

* **Prim路径 (Prim Path):**/World/Conveyor_2/Looks/M_ConveyorBelt_A01_Decal
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_2/Looks/M_ConveyorBelt_A01_Decal/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_2/Looks/M_ConveyorBelt_A01_Decal/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * 纹理引用 (Texture Assets):
      * './T_ConveyorsBelt_A01_Decal_Albedo.png'
      * './T_ConveyorsBelt_A01_Decal_Alpha.png'
      * './T_ConveyorsBelt_A01_Decal_ORM.png'
    * Inputs:
      * 'opacity_texture' [asset] = './T_ConveyorsBelt_A01_Decal_Alpha.png'
      * 'diffuse_texture' [asset] = './T_ConveyorsBelt_A01_Decal_Albedo.png'
      * 'reflection_roughness_texture_influence' [float] = '1'
      * 'metallic_texture_influence' [float] = '1'
      * 'ORM_texture' [asset] = './T_ConveyorsBelt_A01_Decal_ORM.png'

---

### /World/Conveyor_2/Looks/Metal_Rough_A

* **Prim路径 (Prim Path):**/World/Conveyor_2/Looks/Metal_Rough_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_2/Looks/Metal_Rough_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_2/Looks/Metal_Rough_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Metal/Misc/Metal_Rough_A.mdl' (Sub Id: 'Metal_Rough_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Metal/Misc/Metal_Rough_A.mdl'

---

### /World/Conveyor_2/Looks/MetalPainted_Black_Glossy_A

* **Prim路径 (Prim Path):**/World/Conveyor_2/Looks/MetalPainted_Black_Glossy_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_2/Looks/MetalPainted_Black_Glossy_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_2/Looks/MetalPainted_Black_Glossy_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Metal/Painted/MetalPainted_White_Glossy_A.mdl' (Sub Id: 'MetalPainted_White_Glossy_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Metal/Painted/MetalPainted_White_Glossy_A.mdl'
    * Inputs:
      * 'bump_factor' [float] = '0.5'
      * 'texture_scale' [float2] = '(1.500, 1.500)'
      * 'diffuse_tint' [color3f] = '(0.066, 0.066, 0.066)'
      * 'reflection_roughness_constant' [float] = '0.63'
      * 'reflection_roughness_texture_influence' [float] = '0.91'

---

### /World/Conveyor_2/Looks/MetalPainted_Blue_Glossy_A

* **Prim路径 (Prim Path):**/World/Conveyor_2/Looks/MetalPainted_Blue_Glossy_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_2/Looks/MetalPainted_Blue_Glossy_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_2/Looks/MetalPainted_Blue_Glossy_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Metal/Painted/MetalPainted_White_Glossy_A.mdl' (Sub Id: 'MetalPainted_White_Glossy_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Metal/Painted/MetalPainted_White_Glossy_A.mdl'
    * 纹理引用 (Texture Assets):
      * '../Material Library/Metal/Painted/T_MetalPainted_White_Glossy_A_Albedo.png'
      * '../Material Library/Metal/Painted/T_MetalPainted_White_Glossy_A_Normal.png'
      * '../Material Library/Metal/Painted/T_MetalPainted_White_Glossy_A_ORM.png'
    * Inputs:
      * 'bump_factor' [float] = '0.5'
      * 'normalmap_texture' [asset] = '../Material Library/Metal/Painted/T_MetalPainted_White_Glossy_A_Normal.png'
      * 'texture_scale' [float2] = '(1.500, 1.500)'
      * 'diffuse_texture' [asset] = '../Material Library/Metal/Painted/T_MetalPainted_White_Glossy_A_Albedo.png'
      * 'diffuse_tint' [color3f] = '(0.077, 0.203, 0.587)'
      * 'ORM_texture' [asset] = '../Material Library/Metal/Painted/T_MetalPainted_White_Glossy_A_ORM.png'

---

### /World/Conveyor_2/Looks/Plastic_Orange_A

* **Prim路径 (Prim Path):**/World/Conveyor_2/Looks/Plastic_Orange_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_2/Looks/Plastic_Orange_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_2/Looks/Plastic_Orange_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Plastic/Misc/Plastic_Orange_A.mdl' (Sub Id: 'Plastic_Orange_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Plastic/Misc/Plastic_Orange_A.mdl'

---

### /World/Conveyor_2/Looks/Plastic_Red_A

* **Prim路径 (Prim Path):**/World/Conveyor_2/Looks/Plastic_Red_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_2/Looks/Plastic_Red_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_2/Looks/Plastic_Red_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Plastic/Misc/Plastic_Red_A.mdl' (Sub Id: 'Plastic_Red_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Plastic/Misc/Plastic_Red_A.mdl'

---

### /World/Conveyor_2/Looks/Plastic_Rough_Black_A

* **Prim路径 (Prim Path):**/World/Conveyor_2/Looks/Plastic_Rough_Black_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_2/Looks/Plastic_Rough_Black_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_2/Looks/Plastic_Rough_Black_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Plastic/Misc/Plastic_Rough_Black_A.mdl' (Sub Id: 'Plastic_Rough_Black_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Plastic/Misc/Plastic_Rough_Black_A.mdl'

---

### /World/Conveyor_2/Looks/Steel_A

* **Prim路径 (Prim Path):**/World/Conveyor_2/Looks/Steel_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_2/Looks/Steel_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_2/Looks/Steel_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Metal/Steel/Steel_A.mdl' (Sub Id: 'Steel_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Metal/Steel/Steel_A.mdl'
    * Inputs:
      * 'diffuse_tint' [color3f] = '(0.772, 0.772, 0.772)'
      * 'reflection_roughness_constant' [float] = '0.67'
      * 'reflection_roughness_texture_influence' [float] = '0.88'

---

### /World/Conveyor_3/Looks/Acrylic_Clear_Glossy_A

* **Prim路径 (Prim Path):**/World/Conveyor_3/Looks/Acrylic_Clear_Glossy_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_3/Looks/Acrylic_Clear_Glossy_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_3/Looks/Acrylic_Clear_Glossy_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniGlass.mdl' (Sub Id: 'OmniGlass')
    * 纹理引用 (Texture Assets):
      * '../Material Library/Plastic/Textures/T_Acrylic_Clear_Glossy_A_Rough.png'
      * '../Material Library/Plastic/Textures/T_Plastic_Rough_Black_A_Normal.png'
    * Inputs:
      * 'normal_map_strength' [float] = '0.5'
      * 'texture_scale' [float2] = '(1.000, 3.000)'
      * 'normal_map_texture' [asset] = '../Material Library/Plastic/Textures/T_Plastic_Rough_Black_A_Normal.png'
      * 'roughness_texture' [asset] = '../Material Library/Plastic/Textures/T_Acrylic_Clear_Glossy_A_Rough.png'
      * 'roughness_texture_influence' [float] = '0.3'
      * 'glass_ior' [float] = '1.05'
      * 'frosting_roughness' [float] = '0.17'
      * 'glass_color' [color3f] = '(0.734, 0.734, 0.734)'

---

### /World/Conveyor_3/Looks/M_ConveyorBelt_A01_Belt

* **Prim路径 (Prim Path):**/World/Conveyor_3/Looks/M_ConveyorBelt_A01_Belt
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_3/Looks/M_ConveyorBelt_A01_Belt/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_3/Looks/M_ConveyorBelt_A01_Belt/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * 纹理引用 (Texture Assets):
      * './T_ConveyorBelt_A01_Belt_Albedo.png'
      * './T_ConveyorBelt_A01_Belt_Normal.png'
      * './T_ConveyorBelt_A01_Belt_ORM.png'
    * Inputs:
      * 'normalmap_texture' [asset] = './T_ConveyorBelt_A01_Belt_Normal.png'
      * 'diffuse_texture' [asset] = './T_ConveyorBelt_A01_Belt_Albedo.png'
      * 'reflection_roughness_texture_influence' [float] = '1'
      * 'metallic_texture_influence' [float] = '1'
      * 'ORM_texture' [asset] = './T_ConveyorBelt_A01_Belt_ORM.png'

---

### /World/Conveyor_3/Looks/M_ConveyorBelt_A01_Decal

* **Prim路径 (Prim Path):**/World/Conveyor_3/Looks/M_ConveyorBelt_A01_Decal
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_3/Looks/M_ConveyorBelt_A01_Decal/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_3/Looks/M_ConveyorBelt_A01_Decal/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * 纹理引用 (Texture Assets):
      * './T_ConveyorsBelt_A01_Decal_Albedo.png'
      * './T_ConveyorsBelt_A01_Decal_Alpha.png'
      * './T_ConveyorsBelt_A01_Decal_ORM.png'
    * Inputs:
      * 'opacity_texture' [asset] = './T_ConveyorsBelt_A01_Decal_Alpha.png'
      * 'diffuse_texture' [asset] = './T_ConveyorsBelt_A01_Decal_Albedo.png'
      * 'reflection_roughness_texture_influence' [float] = '1'
      * 'metallic_texture_influence' [float] = '1'
      * 'ORM_texture' [asset] = './T_ConveyorsBelt_A01_Decal_ORM.png'

---

### /World/Conveyor_3/Looks/Metal_Rough_A

* **Prim路径 (Prim Path):**/World/Conveyor_3/Looks/Metal_Rough_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_3/Looks/Metal_Rough_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_3/Looks/Metal_Rough_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Metal/Misc/Metal_Rough_A.mdl' (Sub Id: 'Metal_Rough_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Metal/Misc/Metal_Rough_A.mdl'

---

### /World/Conveyor_3/Looks/MetalPainted_Black_Glossy_A

* **Prim路径 (Prim Path):**/World/Conveyor_3/Looks/MetalPainted_Black_Glossy_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_3/Looks/MetalPainted_Black_Glossy_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_3/Looks/MetalPainted_Black_Glossy_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Metal/Painted/MetalPainted_White_Glossy_A.mdl' (Sub Id: 'MetalPainted_White_Glossy_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Metal/Painted/MetalPainted_White_Glossy_A.mdl'
    * Inputs:
      * 'bump_factor' [float] = '0.5'
      * 'texture_scale' [float2] = '(1.500, 1.500)'
      * 'diffuse_tint' [color3f] = '(0.066, 0.066, 0.066)'
      * 'reflection_roughness_constant' [float] = '0.63'
      * 'reflection_roughness_texture_influence' [float] = '0.91'

---

### /World/Conveyor_3/Looks/MetalPainted_Blue_Glossy_A

* **Prim路径 (Prim Path):**/World/Conveyor_3/Looks/MetalPainted_Blue_Glossy_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_3/Looks/MetalPainted_Blue_Glossy_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_3/Looks/MetalPainted_Blue_Glossy_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Metal/Painted/MetalPainted_White_Glossy_A.mdl' (Sub Id: 'MetalPainted_White_Glossy_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Metal/Painted/MetalPainted_White_Glossy_A.mdl'
    * 纹理引用 (Texture Assets):
      * '../Material Library/Metal/Painted/T_MetalPainted_White_Glossy_A_Albedo.png'
      * '../Material Library/Metal/Painted/T_MetalPainted_White_Glossy_A_Normal.png'
      * '../Material Library/Metal/Painted/T_MetalPainted_White_Glossy_A_ORM.png'
    * Inputs:
      * 'bump_factor' [float] = '0.5'
      * 'normalmap_texture' [asset] = '../Material Library/Metal/Painted/T_MetalPainted_White_Glossy_A_Normal.png'
      * 'texture_scale' [float2] = '(1.500, 1.500)'
      * 'diffuse_texture' [asset] = '../Material Library/Metal/Painted/T_MetalPainted_White_Glossy_A_Albedo.png'
      * 'diffuse_tint' [color3f] = '(0.077, 0.203, 0.587)'
      * 'ORM_texture' [asset] = '../Material Library/Metal/Painted/T_MetalPainted_White_Glossy_A_ORM.png'

---

### /World/Conveyor_3/Looks/Plastic_Orange_A

* **Prim路径 (Prim Path):**/World/Conveyor_3/Looks/Plastic_Orange_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_3/Looks/Plastic_Orange_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_3/Looks/Plastic_Orange_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Plastic/Misc/Plastic_Orange_A.mdl' (Sub Id: 'Plastic_Orange_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Plastic/Misc/Plastic_Orange_A.mdl'

---

### /World/Conveyor_3/Looks/Plastic_Red_A

* **Prim路径 (Prim Path):**/World/Conveyor_3/Looks/Plastic_Red_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_3/Looks/Plastic_Red_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_3/Looks/Plastic_Red_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Plastic/Misc/Plastic_Red_A.mdl' (Sub Id: 'Plastic_Red_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Plastic/Misc/Plastic_Red_A.mdl'

---

### /World/Conveyor_3/Looks/Plastic_Rough_Black_A

* **Prim路径 (Prim Path):**/World/Conveyor_3/Looks/Plastic_Rough_Black_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_3/Looks/Plastic_Rough_Black_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_3/Looks/Plastic_Rough_Black_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Plastic/Misc/Plastic_Rough_Black_A.mdl' (Sub Id: 'Plastic_Rough_Black_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Plastic/Misc/Plastic_Rough_Black_A.mdl'

---

### /World/Conveyor_3/Looks/Steel_A

* **Prim路径 (Prim Path):**/World/Conveyor_3/Looks/Steel_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_3/Looks/Steel_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_3/Looks/Steel_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Metal/Steel/Steel_A.mdl' (Sub Id: 'Steel_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Metal/Steel/Steel_A.mdl'
    * Inputs:
      * 'diffuse_tint' [color3f] = '(0.772, 0.772, 0.772)'
      * 'reflection_roughness_constant' [float] = '0.67'
      * 'reflection_roughness_texture_influence' [float] = '0.88'

---

### /World/Conveyor_4/Looks/Acrylic_Clear_Glossy_A

* **Prim路径 (Prim Path):**/World/Conveyor_4/Looks/Acrylic_Clear_Glossy_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_4/Looks/Acrylic_Clear_Glossy_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_4/Looks/Acrylic_Clear_Glossy_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniGlass.mdl' (Sub Id: 'OmniGlass')
    * 纹理引用 (Texture Assets):
      * '../Material Library/Plastic/Textures/T_Acrylic_Clear_Glossy_A_Rough.png'
      * '../Material Library/Plastic/Textures/T_Plastic_Rough_Black_A_Normal.png'
    * Inputs:
      * 'normal_map_strength' [float] = '0.5'
      * 'texture_scale' [float2] = '(1.000, 3.000)'
      * 'normal_map_texture' [asset] = '../Material Library/Plastic/Textures/T_Plastic_Rough_Black_A_Normal.png'
      * 'roughness_texture' [asset] = '../Material Library/Plastic/Textures/T_Acrylic_Clear_Glossy_A_Rough.png'
      * 'roughness_texture_influence' [float] = '0.3'
      * 'glass_ior' [float] = '1.05'
      * 'frosting_roughness' [float] = '0.17'
      * 'glass_color' [color3f] = '(0.734, 0.734, 0.734)'

---

### /World/Conveyor_4/Looks/M_ConveyorBelt_A01_Belt

* **Prim路径 (Prim Path):**/World/Conveyor_4/Looks/M_ConveyorBelt_A01_Belt
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_4/Looks/M_ConveyorBelt_A01_Belt/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_4/Looks/M_ConveyorBelt_A01_Belt/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * 纹理引用 (Texture Assets):
      * './T_ConveyorBelt_A01_Belt_Albedo.png'
      * './T_ConveyorBelt_A01_Belt_Normal.png'
      * './T_ConveyorBelt_A01_Belt_ORM.png'
    * Inputs:
      * 'normalmap_texture' [asset] = './T_ConveyorBelt_A01_Belt_Normal.png'
      * 'diffuse_texture' [asset] = './T_ConveyorBelt_A01_Belt_Albedo.png'
      * 'reflection_roughness_texture_influence' [float] = '1'
      * 'metallic_texture_influence' [float] = '1'
      * 'ORM_texture' [asset] = './T_ConveyorBelt_A01_Belt_ORM.png'

---

### /World/Conveyor_4/Looks/M_ConveyorBelt_A01_Decal

* **Prim路径 (Prim Path):**/World/Conveyor_4/Looks/M_ConveyorBelt_A01_Decal
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_4/Looks/M_ConveyorBelt_A01_Decal/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_4/Looks/M_ConveyorBelt_A01_Decal/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * 纹理引用 (Texture Assets):
      * './T_ConveyorsBelt_A01_Decal_Albedo.png'
      * './T_ConveyorsBelt_A01_Decal_Alpha.png'
      * './T_ConveyorsBelt_A01_Decal_ORM.png'
    * Inputs:
      * 'opacity_texture' [asset] = './T_ConveyorsBelt_A01_Decal_Alpha.png'
      * 'diffuse_texture' [asset] = './T_ConveyorsBelt_A01_Decal_Albedo.png'
      * 'reflection_roughness_texture_influence' [float] = '1'
      * 'metallic_texture_influence' [float] = '1'
      * 'ORM_texture' [asset] = './T_ConveyorsBelt_A01_Decal_ORM.png'

---

### /World/Conveyor_4/Looks/Metal_Rough_A

* **Prim路径 (Prim Path):**/World/Conveyor_4/Looks/Metal_Rough_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_4/Looks/Metal_Rough_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_4/Looks/Metal_Rough_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Metal/Misc/Metal_Rough_A.mdl' (Sub Id: 'Metal_Rough_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Metal/Misc/Metal_Rough_A.mdl'

---

### /World/Conveyor_4/Looks/MetalPainted_Black_Glossy_A

* **Prim路径 (Prim Path):**/World/Conveyor_4/Looks/MetalPainted_Black_Glossy_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_4/Looks/MetalPainted_Black_Glossy_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_4/Looks/MetalPainted_Black_Glossy_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Metal/Painted/MetalPainted_White_Glossy_A.mdl' (Sub Id: 'MetalPainted_White_Glossy_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Metal/Painted/MetalPainted_White_Glossy_A.mdl'
    * Inputs:
      * 'bump_factor' [float] = '0.5'
      * 'texture_scale' [float2] = '(1.500, 1.500)'
      * 'diffuse_tint' [color3f] = '(0.066, 0.066, 0.066)'
      * 'reflection_roughness_constant' [float] = '0.63'
      * 'reflection_roughness_texture_influence' [float] = '0.91'

---

### /World/Conveyor_4/Looks/MetalPainted_Blue_Glossy_A

* **Prim路径 (Prim Path):**/World/Conveyor_4/Looks/MetalPainted_Blue_Glossy_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_4/Looks/MetalPainted_Blue_Glossy_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_4/Looks/MetalPainted_Blue_Glossy_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Metal/Painted/MetalPainted_White_Glossy_A.mdl' (Sub Id: 'MetalPainted_White_Glossy_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Metal/Painted/MetalPainted_White_Glossy_A.mdl'
    * 纹理引用 (Texture Assets):
      * '../Material Library/Metal/Painted/T_MetalPainted_White_Glossy_A_Albedo.png'
      * '../Material Library/Metal/Painted/T_MetalPainted_White_Glossy_A_Normal.png'
      * '../Material Library/Metal/Painted/T_MetalPainted_White_Glossy_A_ORM.png'
    * Inputs:
      * 'bump_factor' [float] = '0.5'
      * 'normalmap_texture' [asset] = '../Material Library/Metal/Painted/T_MetalPainted_White_Glossy_A_Normal.png'
      * 'texture_scale' [float2] = '(1.500, 1.500)'
      * 'diffuse_texture' [asset] = '../Material Library/Metal/Painted/T_MetalPainted_White_Glossy_A_Albedo.png'
      * 'diffuse_tint' [color3f] = '(0.077, 0.203, 0.587)'
      * 'ORM_texture' [asset] = '../Material Library/Metal/Painted/T_MetalPainted_White_Glossy_A_ORM.png'

---

### /World/Conveyor_4/Looks/Plastic_Orange_A

* **Prim路径 (Prim Path):**/World/Conveyor_4/Looks/Plastic_Orange_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_4/Looks/Plastic_Orange_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_4/Looks/Plastic_Orange_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Plastic/Misc/Plastic_Orange_A.mdl' (Sub Id: 'Plastic_Orange_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Plastic/Misc/Plastic_Orange_A.mdl'

---

### /World/Conveyor_4/Looks/Plastic_Red_A

* **Prim路径 (Prim Path):**/World/Conveyor_4/Looks/Plastic_Red_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_4/Looks/Plastic_Red_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_4/Looks/Plastic_Red_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Plastic/Misc/Plastic_Red_A.mdl' (Sub Id: 'Plastic_Red_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Plastic/Misc/Plastic_Red_A.mdl'

---

### /World/Conveyor_4/Looks/Plastic_Rough_Black_A

* **Prim路径 (Prim Path):**/World/Conveyor_4/Looks/Plastic_Rough_Black_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_4/Looks/Plastic_Rough_Black_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_4/Looks/Plastic_Rough_Black_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Plastic/Misc/Plastic_Rough_Black_A.mdl' (Sub Id: 'Plastic_Rough_Black_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Plastic/Misc/Plastic_Rough_Black_A.mdl'

---

### /World/Conveyor_4/Looks/Steel_A

* **Prim路径 (Prim Path):**/World/Conveyor_4/Looks/Steel_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_4/Looks/Steel_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_4/Looks/Steel_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Metal/Steel/Steel_A.mdl' (Sub Id: 'Steel_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Metal/Steel/Steel_A.mdl'
    * Inputs:
      * 'diffuse_tint' [color3f] = '(0.772, 0.772, 0.772)'
      * 'reflection_roughness_constant' [float] = '0.67'
      * 'reflection_roughness_texture_influence' [float] = '0.88'

---

### /World/Conveyor_5/Looks/Acrylic_Clear_Glossy_A

* **Prim路径 (Prim Path):**/World/Conveyor_5/Looks/Acrylic_Clear_Glossy_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_5/Looks/Acrylic_Clear_Glossy_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_5/Looks/Acrylic_Clear_Glossy_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniGlass.mdl' (Sub Id: 'OmniGlass')
    * 纹理引用 (Texture Assets):
      * '../Material Library/Plastic/Textures/T_Acrylic_Clear_Glossy_A_Rough.png'
      * '../Material Library/Plastic/Textures/T_Plastic_Rough_Black_A_Normal.png'
    * Inputs:
      * 'normal_map_strength' [float] = '0.5'
      * 'texture_scale' [float2] = '(1.000, 3.000)'
      * 'normal_map_texture' [asset] = '../Material Library/Plastic/Textures/T_Plastic_Rough_Black_A_Normal.png'
      * 'roughness_texture' [asset] = '../Material Library/Plastic/Textures/T_Acrylic_Clear_Glossy_A_Rough.png'
      * 'roughness_texture_influence' [float] = '0.3'
      * 'glass_ior' [float] = '1.05'
      * 'frosting_roughness' [float] = '0.17'
      * 'glass_color' [color3f] = '(0.734, 0.734, 0.734)'

---

### /World/Conveyor_5/Looks/M_ConveyorBelt_A01_Belt

* **Prim路径 (Prim Path):**/World/Conveyor_5/Looks/M_ConveyorBelt_A01_Belt
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_5/Looks/M_ConveyorBelt_A01_Belt/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_5/Looks/M_ConveyorBelt_A01_Belt/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * 纹理引用 (Texture Assets):
      * './T_ConveyorBelt_A01_Belt_Albedo.png'
      * './T_ConveyorBelt_A01_Belt_Normal.png'
      * './T_ConveyorBelt_A01_Belt_ORM.png'
    * Inputs:
      * 'normalmap_texture' [asset] = './T_ConveyorBelt_A01_Belt_Normal.png'
      * 'diffuse_texture' [asset] = './T_ConveyorBelt_A01_Belt_Albedo.png'
      * 'reflection_roughness_texture_influence' [float] = '1'
      * 'metallic_texture_influence' [float] = '1'
      * 'ORM_texture' [asset] = './T_ConveyorBelt_A01_Belt_ORM.png'

---

### /World/Conveyor_5/Looks/M_ConveyorBelt_A01_Decal

* **Prim路径 (Prim Path):**/World/Conveyor_5/Looks/M_ConveyorBelt_A01_Decal
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_5/Looks/M_ConveyorBelt_A01_Decal/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_5/Looks/M_ConveyorBelt_A01_Decal/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * 纹理引用 (Texture Assets):
      * './T_ConveyorsBelt_A01_Decal_Albedo.png'
      * './T_ConveyorsBelt_A01_Decal_Alpha.png'
      * './T_ConveyorsBelt_A01_Decal_ORM.png'
    * Inputs:
      * 'opacity_texture' [asset] = './T_ConveyorsBelt_A01_Decal_Alpha.png'
      * 'diffuse_texture' [asset] = './T_ConveyorsBelt_A01_Decal_Albedo.png'
      * 'reflection_roughness_texture_influence' [float] = '1'
      * 'metallic_texture_influence' [float] = '1'
      * 'ORM_texture' [asset] = './T_ConveyorsBelt_A01_Decal_ORM.png'

---

### /World/Conveyor_5/Looks/Metal_Rough_A

* **Prim路径 (Prim Path):**/World/Conveyor_5/Looks/Metal_Rough_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_5/Looks/Metal_Rough_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_5/Looks/Metal_Rough_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Metal/Misc/Metal_Rough_A.mdl' (Sub Id: 'Metal_Rough_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Metal/Misc/Metal_Rough_A.mdl'

---

### /World/Conveyor_5/Looks/MetalPainted_Black_Glossy_A

* **Prim路径 (Prim Path):**/World/Conveyor_5/Looks/MetalPainted_Black_Glossy_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_5/Looks/MetalPainted_Black_Glossy_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_5/Looks/MetalPainted_Black_Glossy_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Metal/Painted/MetalPainted_White_Glossy_A.mdl' (Sub Id: 'MetalPainted_White_Glossy_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Metal/Painted/MetalPainted_White_Glossy_A.mdl'
    * Inputs:
      * 'bump_factor' [float] = '0.5'
      * 'texture_scale' [float2] = '(1.500, 1.500)'
      * 'diffuse_tint' [color3f] = '(0.066, 0.066, 0.066)'
      * 'reflection_roughness_constant' [float] = '0.63'
      * 'reflection_roughness_texture_influence' [float] = '0.91'

---

### /World/Conveyor_5/Looks/MetalPainted_Blue_Glossy_A

* **Prim路径 (Prim Path):**/World/Conveyor_5/Looks/MetalPainted_Blue_Glossy_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_5/Looks/MetalPainted_Blue_Glossy_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_5/Looks/MetalPainted_Blue_Glossy_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Metal/Painted/MetalPainted_White_Glossy_A.mdl' (Sub Id: 'MetalPainted_White_Glossy_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Metal/Painted/MetalPainted_White_Glossy_A.mdl'
    * 纹理引用 (Texture Assets):
      * '../Material Library/Metal/Painted/T_MetalPainted_White_Glossy_A_Albedo.png'
      * '../Material Library/Metal/Painted/T_MetalPainted_White_Glossy_A_Normal.png'
      * '../Material Library/Metal/Painted/T_MetalPainted_White_Glossy_A_ORM.png'
    * Inputs:
      * 'bump_factor' [float] = '0.5'
      * 'normalmap_texture' [asset] = '../Material Library/Metal/Painted/T_MetalPainted_White_Glossy_A_Normal.png'
      * 'texture_scale' [float2] = '(1.500, 1.500)'
      * 'diffuse_texture' [asset] = '../Material Library/Metal/Painted/T_MetalPainted_White_Glossy_A_Albedo.png'
      * 'diffuse_tint' [color3f] = '(0.077, 0.203, 0.587)'
      * 'ORM_texture' [asset] = '../Material Library/Metal/Painted/T_MetalPainted_White_Glossy_A_ORM.png'

---

### /World/Conveyor_5/Looks/Plastic_Orange_A

* **Prim路径 (Prim Path):**/World/Conveyor_5/Looks/Plastic_Orange_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_5/Looks/Plastic_Orange_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_5/Looks/Plastic_Orange_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Plastic/Misc/Plastic_Orange_A.mdl' (Sub Id: 'Plastic_Orange_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Plastic/Misc/Plastic_Orange_A.mdl'

---

### /World/Conveyor_5/Looks/Plastic_Red_A

* **Prim路径 (Prim Path):**/World/Conveyor_5/Looks/Plastic_Red_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_5/Looks/Plastic_Red_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_5/Looks/Plastic_Red_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Plastic/Misc/Plastic_Red_A.mdl' (Sub Id: 'Plastic_Red_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Plastic/Misc/Plastic_Red_A.mdl'

---

### /World/Conveyor_5/Looks/Plastic_Rough_Black_A

* **Prim路径 (Prim Path):**/World/Conveyor_5/Looks/Plastic_Rough_Black_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_5/Looks/Plastic_Rough_Black_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_5/Looks/Plastic_Rough_Black_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Plastic/Misc/Plastic_Rough_Black_A.mdl' (Sub Id: 'Plastic_Rough_Black_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Plastic/Misc/Plastic_Rough_Black_A.mdl'

---

### /World/Conveyor_5/Looks/Steel_A

* **Prim路径 (Prim Path):**/World/Conveyor_5/Looks/Steel_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_5/Looks/Steel_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_5/Looks/Steel_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Metal/Steel/Steel_A.mdl' (Sub Id: 'Steel_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Metal/Steel/Steel_A.mdl'
    * Inputs:
      * 'diffuse_tint' [color3f] = '(0.772, 0.772, 0.772)'
      * 'reflection_roughness_constant' [float] = '0.67'
      * 'reflection_roughness_texture_influence' [float] = '0.88'

---

### /World/Conveyor_6/Looks/Acrylic_Clear_Glossy_A

* **Prim路径 (Prim Path):**/World/Conveyor_6/Looks/Acrylic_Clear_Glossy_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_6/Looks/Acrylic_Clear_Glossy_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_6/Looks/Acrylic_Clear_Glossy_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniGlass.mdl' (Sub Id: 'OmniGlass')
    * 纹理引用 (Texture Assets):
      * '../Material Library/Plastic/Textures/T_Acrylic_Clear_Glossy_A_Rough.png'
      * '../Material Library/Plastic/Textures/T_Plastic_Rough_Black_A_Normal.png'
    * Inputs:
      * 'normal_map_strength' [float] = '0.5'
      * 'texture_scale' [float2] = '(1.000, 3.000)'
      * 'normal_map_texture' [asset] = '../Material Library/Plastic/Textures/T_Plastic_Rough_Black_A_Normal.png'
      * 'roughness_texture' [asset] = '../Material Library/Plastic/Textures/T_Acrylic_Clear_Glossy_A_Rough.png'
      * 'roughness_texture_influence' [float] = '0.3'
      * 'glass_ior' [float] = '1.05'
      * 'frosting_roughness' [float] = '0.17'
      * 'glass_color' [color3f] = '(0.734, 0.734, 0.734)'

---

### /World/Conveyor_6/Looks/M_ConveyorBelt_A01_Belt

* **Prim路径 (Prim Path):**/World/Conveyor_6/Looks/M_ConveyorBelt_A01_Belt
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_6/Looks/M_ConveyorBelt_A01_Belt/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_6/Looks/M_ConveyorBelt_A01_Belt/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * 纹理引用 (Texture Assets):
      * './T_ConveyorBelt_A01_Belt_Albedo.png'
      * './T_ConveyorBelt_A01_Belt_Normal.png'
      * './T_ConveyorBelt_A01_Belt_ORM.png'
    * Inputs:
      * 'normalmap_texture' [asset] = './T_ConveyorBelt_A01_Belt_Normal.png'
      * 'diffuse_texture' [asset] = './T_ConveyorBelt_A01_Belt_Albedo.png'
      * 'reflection_roughness_texture_influence' [float] = '1'
      * 'metallic_texture_influence' [float] = '1'
      * 'ORM_texture' [asset] = './T_ConveyorBelt_A01_Belt_ORM.png'

---

### /World/Conveyor_6/Looks/M_ConveyorBelt_A01_Decal

* **Prim路径 (Prim Path):**/World/Conveyor_6/Looks/M_ConveyorBelt_A01_Decal
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_6/Looks/M_ConveyorBelt_A01_Decal/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_6/Looks/M_ConveyorBelt_A01_Decal/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * 纹理引用 (Texture Assets):
      * './T_ConveyorsBelt_A01_Decal_Albedo.png'
      * './T_ConveyorsBelt_A01_Decal_Alpha.png'
      * './T_ConveyorsBelt_A01_Decal_ORM.png'
    * Inputs:
      * 'opacity_texture' [asset] = './T_ConveyorsBelt_A01_Decal_Alpha.png'
      * 'diffuse_texture' [asset] = './T_ConveyorsBelt_A01_Decal_Albedo.png'
      * 'reflection_roughness_texture_influence' [float] = '1'
      * 'metallic_texture_influence' [float] = '1'
      * 'ORM_texture' [asset] = './T_ConveyorsBelt_A01_Decal_ORM.png'

---

### /World/Conveyor_6/Looks/Metal_Rough_A

* **Prim路径 (Prim Path):**/World/Conveyor_6/Looks/Metal_Rough_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_6/Looks/Metal_Rough_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_6/Looks/Metal_Rough_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Metal/Misc/Metal_Rough_A.mdl' (Sub Id: 'Metal_Rough_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Metal/Misc/Metal_Rough_A.mdl'

---

### /World/Conveyor_6/Looks/MetalPainted_Black_Glossy_A

* **Prim路径 (Prim Path):**/World/Conveyor_6/Looks/MetalPainted_Black_Glossy_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_6/Looks/MetalPainted_Black_Glossy_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_6/Looks/MetalPainted_Black_Glossy_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Metal/Painted/MetalPainted_White_Glossy_A.mdl' (Sub Id: 'MetalPainted_White_Glossy_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Metal/Painted/MetalPainted_White_Glossy_A.mdl'
    * Inputs:
      * 'bump_factor' [float] = '0.5'
      * 'texture_scale' [float2] = '(1.500, 1.500)'
      * 'diffuse_tint' [color3f] = '(0.066, 0.066, 0.066)'
      * 'reflection_roughness_constant' [float] = '0.63'
      * 'reflection_roughness_texture_influence' [float] = '0.91'

---

### /World/Conveyor_6/Looks/MetalPainted_Blue_Glossy_A

* **Prim路径 (Prim Path):**/World/Conveyor_6/Looks/MetalPainted_Blue_Glossy_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_6/Looks/MetalPainted_Blue_Glossy_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_6/Looks/MetalPainted_Blue_Glossy_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Metal/Painted/MetalPainted_White_Glossy_A.mdl' (Sub Id: 'MetalPainted_White_Glossy_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Metal/Painted/MetalPainted_White_Glossy_A.mdl'
    * 纹理引用 (Texture Assets):
      * '../Material Library/Metal/Painted/T_MetalPainted_White_Glossy_A_Albedo.png'
      * '../Material Library/Metal/Painted/T_MetalPainted_White_Glossy_A_Normal.png'
      * '../Material Library/Metal/Painted/T_MetalPainted_White_Glossy_A_ORM.png'
    * Inputs:
      * 'bump_factor' [float] = '0.5'
      * 'normalmap_texture' [asset] = '../Material Library/Metal/Painted/T_MetalPainted_White_Glossy_A_Normal.png'
      * 'texture_scale' [float2] = '(1.500, 1.500)'
      * 'diffuse_texture' [asset] = '../Material Library/Metal/Painted/T_MetalPainted_White_Glossy_A_Albedo.png'
      * 'diffuse_tint' [color3f] = '(0.077, 0.203, 0.587)'
      * 'ORM_texture' [asset] = '../Material Library/Metal/Painted/T_MetalPainted_White_Glossy_A_ORM.png'

---

### /World/Conveyor_6/Looks/Plastic_Orange_A

* **Prim路径 (Prim Path):**/World/Conveyor_6/Looks/Plastic_Orange_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_6/Looks/Plastic_Orange_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_6/Looks/Plastic_Orange_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Plastic/Misc/Plastic_Orange_A.mdl' (Sub Id: 'Plastic_Orange_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Plastic/Misc/Plastic_Orange_A.mdl'

---

### /World/Conveyor_6/Looks/Plastic_Red_A

* **Prim路径 (Prim Path):**/World/Conveyor_6/Looks/Plastic_Red_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_6/Looks/Plastic_Red_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_6/Looks/Plastic_Red_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Plastic/Misc/Plastic_Red_A.mdl' (Sub Id: 'Plastic_Red_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Plastic/Misc/Plastic_Red_A.mdl'

---

### /World/Conveyor_6/Looks/Plastic_Rough_Black_A

* **Prim路径 (Prim Path):**/World/Conveyor_6/Looks/Plastic_Rough_Black_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_6/Looks/Plastic_Rough_Black_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_6/Looks/Plastic_Rough_Black_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Plastic/Misc/Plastic_Rough_Black_A.mdl' (Sub Id: 'Plastic_Rough_Black_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Plastic/Misc/Plastic_Rough_Black_A.mdl'

---

### /World/Conveyor_6/Looks/Steel_A

* **Prim路径 (Prim Path):**/World/Conveyor_6/Looks/Steel_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_6/Looks/Steel_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_6/Looks/Steel_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Metal/Steel/Steel_A.mdl' (Sub Id: 'Steel_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Metal/Steel/Steel_A.mdl'
    * Inputs:
      * 'diffuse_tint' [color3f] = '(0.772, 0.772, 0.772)'
      * 'reflection_roughness_constant' [float] = '0.67'
      * 'reflection_roughness_texture_influence' [float] = '0.88'

---

### /World/Conveyor_7/Looks/Acrylic_Clear_Glossy_A

* **Prim路径 (Prim Path):**/World/Conveyor_7/Looks/Acrylic_Clear_Glossy_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_7/Looks/Acrylic_Clear_Glossy_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_7/Looks/Acrylic_Clear_Glossy_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniGlass.mdl' (Sub Id: 'OmniGlass')
    * 纹理引用 (Texture Assets):
      * '../Material Library/Plastic/Textures/T_Acrylic_Clear_Glossy_A_Rough.png'
      * '../Material Library/Plastic/Textures/T_Plastic_Rough_Black_A_Normal.png'
    * Inputs:
      * 'normal_map_strength' [float] = '0.5'
      * 'texture_scale' [float2] = '(1.000, 3.000)'
      * 'normal_map_texture' [asset] = '../Material Library/Plastic/Textures/T_Plastic_Rough_Black_A_Normal.png'
      * 'roughness_texture' [asset] = '../Material Library/Plastic/Textures/T_Acrylic_Clear_Glossy_A_Rough.png'
      * 'roughness_texture_influence' [float] = '0.3'
      * 'glass_ior' [float] = '1.05'
      * 'frosting_roughness' [float] = '0.17'
      * 'glass_color' [color3f] = '(0.734, 0.734, 0.734)'

---

### /World/Conveyor_7/Looks/M_ConveyorBelt_A01_Belt

* **Prim路径 (Prim Path):**/World/Conveyor_7/Looks/M_ConveyorBelt_A01_Belt
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_7/Looks/M_ConveyorBelt_A01_Belt/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_7/Looks/M_ConveyorBelt_A01_Belt/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * 纹理引用 (Texture Assets):
      * './T_ConveyorBelt_A01_Belt_Albedo.png'
      * './T_ConveyorBelt_A01_Belt_Normal.png'
      * './T_ConveyorBelt_A01_Belt_ORM.png'
    * Inputs:
      * 'normalmap_texture' [asset] = './T_ConveyorBelt_A01_Belt_Normal.png'
      * 'diffuse_texture' [asset] = './T_ConveyorBelt_A01_Belt_Albedo.png'
      * 'reflection_roughness_texture_influence' [float] = '1'
      * 'metallic_texture_influence' [float] = '1'
      * 'ORM_texture' [asset] = './T_ConveyorBelt_A01_Belt_ORM.png'

---

### /World/Conveyor_7/Looks/M_ConveyorBelt_A01_Decal

* **Prim路径 (Prim Path):**/World/Conveyor_7/Looks/M_ConveyorBelt_A01_Decal
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_7/Looks/M_ConveyorBelt_A01_Decal/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_7/Looks/M_ConveyorBelt_A01_Decal/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * 纹理引用 (Texture Assets):
      * './T_ConveyorsBelt_A01_Decal_Albedo.png'
      * './T_ConveyorsBelt_A01_Decal_Alpha.png'
      * './T_ConveyorsBelt_A01_Decal_ORM.png'
    * Inputs:
      * 'opacity_texture' [asset] = './T_ConveyorsBelt_A01_Decal_Alpha.png'
      * 'diffuse_texture' [asset] = './T_ConveyorsBelt_A01_Decal_Albedo.png'
      * 'reflection_roughness_texture_influence' [float] = '1'
      * 'metallic_texture_influence' [float] = '1'
      * 'ORM_texture' [asset] = './T_ConveyorsBelt_A01_Decal_ORM.png'

---

### /World/Conveyor_7/Looks/Metal_Rough_A

* **Prim路径 (Prim Path):**/World/Conveyor_7/Looks/Metal_Rough_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_7/Looks/Metal_Rough_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_7/Looks/Metal_Rough_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Metal/Misc/Metal_Rough_A.mdl' (Sub Id: 'Metal_Rough_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Metal/Misc/Metal_Rough_A.mdl'

---

### /World/Conveyor_7/Looks/MetalPainted_Black_Glossy_A

* **Prim路径 (Prim Path):**/World/Conveyor_7/Looks/MetalPainted_Black_Glossy_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_7/Looks/MetalPainted_Black_Glossy_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_7/Looks/MetalPainted_Black_Glossy_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Metal/Painted/MetalPainted_White_Glossy_A.mdl' (Sub Id: 'MetalPainted_White_Glossy_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Metal/Painted/MetalPainted_White_Glossy_A.mdl'
    * Inputs:
      * 'bump_factor' [float] = '0.5'
      * 'texture_scale' [float2] = '(1.500, 1.500)'
      * 'diffuse_tint' [color3f] = '(0.066, 0.066, 0.066)'
      * 'reflection_roughness_constant' [float] = '0.63'
      * 'reflection_roughness_texture_influence' [float] = '0.91'

---

### /World/Conveyor_7/Looks/MetalPainted_Blue_Glossy_A

* **Prim路径 (Prim Path):**/World/Conveyor_7/Looks/MetalPainted_Blue_Glossy_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_7/Looks/MetalPainted_Blue_Glossy_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_7/Looks/MetalPainted_Blue_Glossy_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Metal/Painted/MetalPainted_White_Glossy_A.mdl' (Sub Id: 'MetalPainted_White_Glossy_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Metal/Painted/MetalPainted_White_Glossy_A.mdl'
    * 纹理引用 (Texture Assets):
      * '../Material Library/Metal/Painted/T_MetalPainted_White_Glossy_A_Albedo.png'
      * '../Material Library/Metal/Painted/T_MetalPainted_White_Glossy_A_Normal.png'
      * '../Material Library/Metal/Painted/T_MetalPainted_White_Glossy_A_ORM.png'
    * Inputs:
      * 'bump_factor' [float] = '0.5'
      * 'normalmap_texture' [asset] = '../Material Library/Metal/Painted/T_MetalPainted_White_Glossy_A_Normal.png'
      * 'texture_scale' [float2] = '(1.500, 1.500)'
      * 'diffuse_texture' [asset] = '../Material Library/Metal/Painted/T_MetalPainted_White_Glossy_A_Albedo.png'
      * 'diffuse_tint' [color3f] = '(0.077, 0.203, 0.587)'
      * 'ORM_texture' [asset] = '../Material Library/Metal/Painted/T_MetalPainted_White_Glossy_A_ORM.png'

---

### /World/Conveyor_7/Looks/Plastic_Orange_A

* **Prim路径 (Prim Path):**/World/Conveyor_7/Looks/Plastic_Orange_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_7/Looks/Plastic_Orange_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_7/Looks/Plastic_Orange_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Plastic/Misc/Plastic_Orange_A.mdl' (Sub Id: 'Plastic_Orange_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Plastic/Misc/Plastic_Orange_A.mdl'

---

### /World/Conveyor_7/Looks/Plastic_Red_A

* **Prim路径 (Prim Path):**/World/Conveyor_7/Looks/Plastic_Red_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_7/Looks/Plastic_Red_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_7/Looks/Plastic_Red_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Plastic/Misc/Plastic_Red_A.mdl' (Sub Id: 'Plastic_Red_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Plastic/Misc/Plastic_Red_A.mdl'

---

### /World/Conveyor_7/Looks/Plastic_Rough_Black_A

* **Prim路径 (Prim Path):**/World/Conveyor_7/Looks/Plastic_Rough_Black_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_7/Looks/Plastic_Rough_Black_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_7/Looks/Plastic_Rough_Black_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Plastic/Misc/Plastic_Rough_Black_A.mdl' (Sub Id: 'Plastic_Rough_Black_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Plastic/Misc/Plastic_Rough_Black_A.mdl'

---

### /World/Conveyor_7/Looks/Steel_A

* **Prim路径 (Prim Path):**/World/Conveyor_7/Looks/Steel_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_7/Looks/Steel_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_7/Looks/Steel_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Metal/Steel/Steel_A.mdl' (Sub Id: 'Steel_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Metal/Steel/Steel_A.mdl'
    * Inputs:
      * 'diffuse_tint' [color3f] = '(0.772, 0.772, 0.772)'
      * 'reflection_roughness_constant' [float] = '0.67'
      * 'reflection_roughness_texture_influence' [float] = '0.88'

---

### /World/Conveyor_8/Looks/Acrylic_Clear_Glossy_A

* **Prim路径 (Prim Path):**/World/Conveyor_8/Looks/Acrylic_Clear_Glossy_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_8/Looks/Acrylic_Clear_Glossy_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_8/Looks/Acrylic_Clear_Glossy_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniGlass.mdl' (Sub Id: 'OmniGlass')
    * 纹理引用 (Texture Assets):
      * '../Material Library/Plastic/Textures/T_Acrylic_Clear_Glossy_A_Rough.png'
      * '../Material Library/Plastic/Textures/T_Plastic_Rough_Black_A_Normal.png'
    * Inputs:
      * 'normal_map_strength' [float] = '0.5'
      * 'texture_scale' [float2] = '(1.000, 3.000)'
      * 'normal_map_texture' [asset] = '../Material Library/Plastic/Textures/T_Plastic_Rough_Black_A_Normal.png'
      * 'roughness_texture' [asset] = '../Material Library/Plastic/Textures/T_Acrylic_Clear_Glossy_A_Rough.png'
      * 'roughness_texture_influence' [float] = '0.3'
      * 'glass_ior' [float] = '1.05'
      * 'frosting_roughness' [float] = '0.17'
      * 'glass_color' [color3f] = '(0.734, 0.734, 0.734)'

---

### /World/Conveyor_8/Looks/M_ConveyorBelt_A01_Belt

* **Prim路径 (Prim Path):**/World/Conveyor_8/Looks/M_ConveyorBelt_A01_Belt
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_8/Looks/M_ConveyorBelt_A01_Belt/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_8/Looks/M_ConveyorBelt_A01_Belt/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * 纹理引用 (Texture Assets):
      * './T_ConveyorBelt_A01_Belt_Albedo.png'
      * './T_ConveyorBelt_A01_Belt_Normal.png'
      * './T_ConveyorBelt_A01_Belt_ORM.png'
    * Inputs:
      * 'normalmap_texture' [asset] = './T_ConveyorBelt_A01_Belt_Normal.png'
      * 'diffuse_texture' [asset] = './T_ConveyorBelt_A01_Belt_Albedo.png'
      * 'reflection_roughness_texture_influence' [float] = '1'
      * 'metallic_texture_influence' [float] = '1'
      * 'ORM_texture' [asset] = './T_ConveyorBelt_A01_Belt_ORM.png'

---

### /World/Conveyor_8/Looks/M_ConveyorBelt_A01_Decal

* **Prim路径 (Prim Path):**/World/Conveyor_8/Looks/M_ConveyorBelt_A01_Decal
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_8/Looks/M_ConveyorBelt_A01_Decal/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_8/Looks/M_ConveyorBelt_A01_Decal/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * 纹理引用 (Texture Assets):
      * './T_ConveyorsBelt_A01_Decal_Albedo.png'
      * './T_ConveyorsBelt_A01_Decal_Alpha.png'
      * './T_ConveyorsBelt_A01_Decal_ORM.png'
    * Inputs:
      * 'opacity_texture' [asset] = './T_ConveyorsBelt_A01_Decal_Alpha.png'
      * 'diffuse_texture' [asset] = './T_ConveyorsBelt_A01_Decal_Albedo.png'
      * 'reflection_roughness_texture_influence' [float] = '1'
      * 'metallic_texture_influence' [float] = '1'
      * 'ORM_texture' [asset] = './T_ConveyorsBelt_A01_Decal_ORM.png'

---

### /World/Conveyor_8/Looks/Metal_Rough_A

* **Prim路径 (Prim Path):**/World/Conveyor_8/Looks/Metal_Rough_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_8/Looks/Metal_Rough_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_8/Looks/Metal_Rough_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Metal/Misc/Metal_Rough_A.mdl' (Sub Id: 'Metal_Rough_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Metal/Misc/Metal_Rough_A.mdl'

---

### /World/Conveyor_8/Looks/MetalPainted_Black_Glossy_A

* **Prim路径 (Prim Path):**/World/Conveyor_8/Looks/MetalPainted_Black_Glossy_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_8/Looks/MetalPainted_Black_Glossy_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_8/Looks/MetalPainted_Black_Glossy_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Metal/Painted/MetalPainted_White_Glossy_A.mdl' (Sub Id: 'MetalPainted_White_Glossy_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Metal/Painted/MetalPainted_White_Glossy_A.mdl'
    * Inputs:
      * 'bump_factor' [float] = '0.5'
      * 'texture_scale' [float2] = '(1.500, 1.500)'
      * 'diffuse_tint' [color3f] = '(0.066, 0.066, 0.066)'
      * 'reflection_roughness_constant' [float] = '0.63'
      * 'reflection_roughness_texture_influence' [float] = '0.91'

---

### /World/Conveyor_8/Looks/MetalPainted_Blue_Glossy_A

* **Prim路径 (Prim Path):**/World/Conveyor_8/Looks/MetalPainted_Blue_Glossy_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_8/Looks/MetalPainted_Blue_Glossy_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_8/Looks/MetalPainted_Blue_Glossy_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Metal/Painted/MetalPainted_White_Glossy_A.mdl' (Sub Id: 'MetalPainted_White_Glossy_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Metal/Painted/MetalPainted_White_Glossy_A.mdl'
    * 纹理引用 (Texture Assets):
      * '../Material Library/Metal/Painted/T_MetalPainted_White_Glossy_A_Albedo.png'
      * '../Material Library/Metal/Painted/T_MetalPainted_White_Glossy_A_Normal.png'
      * '../Material Library/Metal/Painted/T_MetalPainted_White_Glossy_A_ORM.png'
    * Inputs:
      * 'bump_factor' [float] = '0.5'
      * 'normalmap_texture' [asset] = '../Material Library/Metal/Painted/T_MetalPainted_White_Glossy_A_Normal.png'
      * 'texture_scale' [float2] = '(1.500, 1.500)'
      * 'diffuse_texture' [asset] = '../Material Library/Metal/Painted/T_MetalPainted_White_Glossy_A_Albedo.png'
      * 'diffuse_tint' [color3f] = '(0.077, 0.203, 0.587)'
      * 'ORM_texture' [asset] = '../Material Library/Metal/Painted/T_MetalPainted_White_Glossy_A_ORM.png'

---

### /World/Conveyor_8/Looks/Plastic_Orange_A

* **Prim路径 (Prim Path):**/World/Conveyor_8/Looks/Plastic_Orange_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_8/Looks/Plastic_Orange_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_8/Looks/Plastic_Orange_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Plastic/Misc/Plastic_Orange_A.mdl' (Sub Id: 'Plastic_Orange_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Plastic/Misc/Plastic_Orange_A.mdl'

---

### /World/Conveyor_8/Looks/Plastic_Red_A

* **Prim路径 (Prim Path):**/World/Conveyor_8/Looks/Plastic_Red_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_8/Looks/Plastic_Red_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_8/Looks/Plastic_Red_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Plastic/Misc/Plastic_Red_A.mdl' (Sub Id: 'Plastic_Red_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Plastic/Misc/Plastic_Red_A.mdl'

---

### /World/Conveyor_8/Looks/Plastic_Rough_Black_A

* **Prim路径 (Prim Path):**/World/Conveyor_8/Looks/Plastic_Rough_Black_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_8/Looks/Plastic_Rough_Black_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_8/Looks/Plastic_Rough_Black_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Plastic/Misc/Plastic_Rough_Black_A.mdl' (Sub Id: 'Plastic_Rough_Black_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Plastic/Misc/Plastic_Rough_Black_A.mdl'

---

### /World/Conveyor_8/Looks/Steel_A

* **Prim路径 (Prim Path):**/World/Conveyor_8/Looks/Steel_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_8/Looks/Steel_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_8/Looks/Steel_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Metal/Steel/Steel_A.mdl' (Sub Id: 'Steel_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Metal/Steel/Steel_A.mdl'
    * Inputs:
      * 'diffuse_tint' [color3f] = '(0.772, 0.772, 0.772)'
      * 'reflection_roughness_constant' [float] = '0.67'
      * 'reflection_roughness_texture_influence' [float] = '0.88'

---

### /World/Conveyor_9/Looks/Acrylic_Clear_Glossy_A

* **Prim路径 (Prim Path):**/World/Conveyor_9/Looks/Acrylic_Clear_Glossy_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_9/Looks/Acrylic_Clear_Glossy_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_9/Looks/Acrylic_Clear_Glossy_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniGlass.mdl' (Sub Id: 'OmniGlass')
    * 纹理引用 (Texture Assets):
      * '../Material Library/Plastic/Textures/T_Acrylic_Clear_Glossy_A_Rough.png'
      * '../Material Library/Plastic/Textures/T_Plastic_Rough_Black_A_Normal.png'
    * Inputs:
      * 'normal_map_strength' [float] = '0.5'
      * 'texture_scale' [float2] = '(1.000, 3.000)'
      * 'normal_map_texture' [asset] = '../Material Library/Plastic/Textures/T_Plastic_Rough_Black_A_Normal.png'
      * 'roughness_texture' [asset] = '../Material Library/Plastic/Textures/T_Acrylic_Clear_Glossy_A_Rough.png'
      * 'roughness_texture_influence' [float] = '0.3'
      * 'glass_ior' [float] = '1.05'
      * 'frosting_roughness' [float] = '0.17'
      * 'glass_color' [color3f] = '(0.734, 0.734, 0.734)'

---

### /World/Conveyor_9/Looks/M_ConveyorBelt_A01_Belt

* **Prim路径 (Prim Path):**/World/Conveyor_9/Looks/M_ConveyorBelt_A01_Belt
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_9/Looks/M_ConveyorBelt_A01_Belt/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_9/Looks/M_ConveyorBelt_A01_Belt/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * 纹理引用 (Texture Assets):
      * './T_ConveyorBelt_A01_Belt_Albedo.png'
      * './T_ConveyorBelt_A01_Belt_Normal.png'
      * './T_ConveyorBelt_A01_Belt_ORM.png'
    * Inputs:
      * 'normalmap_texture' [asset] = './T_ConveyorBelt_A01_Belt_Normal.png'
      * 'diffuse_texture' [asset] = './T_ConveyorBelt_A01_Belt_Albedo.png'
      * 'reflection_roughness_texture_influence' [float] = '1'
      * 'metallic_texture_influence' [float] = '1'
      * 'ORM_texture' [asset] = './T_ConveyorBelt_A01_Belt_ORM.png'

---

### /World/Conveyor_9/Looks/M_ConveyorBelt_A01_Decal

* **Prim路径 (Prim Path):**/World/Conveyor_9/Looks/M_ConveyorBelt_A01_Decal
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_9/Looks/M_ConveyorBelt_A01_Decal/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_9/Looks/M_ConveyorBelt_A01_Decal/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * 纹理引用 (Texture Assets):
      * './T_ConveyorsBelt_A01_Decal_Albedo.png'
      * './T_ConveyorsBelt_A01_Decal_Alpha.png'
      * './T_ConveyorsBelt_A01_Decal_ORM.png'
    * Inputs:
      * 'opacity_texture' [asset] = './T_ConveyorsBelt_A01_Decal_Alpha.png'
      * 'diffuse_texture' [asset] = './T_ConveyorsBelt_A01_Decal_Albedo.png'
      * 'reflection_roughness_texture_influence' [float] = '1'
      * 'metallic_texture_influence' [float] = '1'
      * 'ORM_texture' [asset] = './T_ConveyorsBelt_A01_Decal_ORM.png'

---

### /World/Conveyor_9/Looks/Metal_Rough_A

* **Prim路径 (Prim Path):**/World/Conveyor_9/Looks/Metal_Rough_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_9/Looks/Metal_Rough_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_9/Looks/Metal_Rough_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Metal/Misc/Metal_Rough_A.mdl' (Sub Id: 'Metal_Rough_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Metal/Misc/Metal_Rough_A.mdl'

---

### /World/Conveyor_9/Looks/MetalPainted_Black_Glossy_A

* **Prim路径 (Prim Path):**/World/Conveyor_9/Looks/MetalPainted_Black_Glossy_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_9/Looks/MetalPainted_Black_Glossy_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_9/Looks/MetalPainted_Black_Glossy_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Metal/Painted/MetalPainted_White_Glossy_A.mdl' (Sub Id: 'MetalPainted_White_Glossy_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Metal/Painted/MetalPainted_White_Glossy_A.mdl'
    * Inputs:
      * 'bump_factor' [float] = '0.5'
      * 'texture_scale' [float2] = '(1.500, 1.500)'
      * 'diffuse_tint' [color3f] = '(0.066, 0.066, 0.066)'
      * 'reflection_roughness_constant' [float] = '0.63'
      * 'reflection_roughness_texture_influence' [float] = '0.91'

---

### /World/Conveyor_9/Looks/MetalPainted_Blue_Glossy_A

* **Prim路径 (Prim Path):**/World/Conveyor_9/Looks/MetalPainted_Blue_Glossy_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_9/Looks/MetalPainted_Blue_Glossy_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_9/Looks/MetalPainted_Blue_Glossy_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Metal/Painted/MetalPainted_White_Glossy_A.mdl' (Sub Id: 'MetalPainted_White_Glossy_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Metal/Painted/MetalPainted_White_Glossy_A.mdl'
    * 纹理引用 (Texture Assets):
      * '../Material Library/Metal/Painted/T_MetalPainted_White_Glossy_A_Albedo.png'
      * '../Material Library/Metal/Painted/T_MetalPainted_White_Glossy_A_Normal.png'
      * '../Material Library/Metal/Painted/T_MetalPainted_White_Glossy_A_ORM.png'
    * Inputs:
      * 'bump_factor' [float] = '0.5'
      * 'normalmap_texture' [asset] = '../Material Library/Metal/Painted/T_MetalPainted_White_Glossy_A_Normal.png'
      * 'texture_scale' [float2] = '(1.500, 1.500)'
      * 'diffuse_texture' [asset] = '../Material Library/Metal/Painted/T_MetalPainted_White_Glossy_A_Albedo.png'
      * 'diffuse_tint' [color3f] = '(0.077, 0.203, 0.587)'
      * 'ORM_texture' [asset] = '../Material Library/Metal/Painted/T_MetalPainted_White_Glossy_A_ORM.png'

---

### /World/Conveyor_9/Looks/Plastic_Orange_A

* **Prim路径 (Prim Path):**/World/Conveyor_9/Looks/Plastic_Orange_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_9/Looks/Plastic_Orange_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_9/Looks/Plastic_Orange_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Plastic/Misc/Plastic_Orange_A.mdl' (Sub Id: 'Plastic_Orange_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Plastic/Misc/Plastic_Orange_A.mdl'

---

### /World/Conveyor_9/Looks/Plastic_Red_A

* **Prim路径 (Prim Path):**/World/Conveyor_9/Looks/Plastic_Red_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_9/Looks/Plastic_Red_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_9/Looks/Plastic_Red_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Plastic/Misc/Plastic_Red_A.mdl' (Sub Id: 'Plastic_Red_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Plastic/Misc/Plastic_Red_A.mdl'

---

### /World/Conveyor_9/Looks/Plastic_Rough_Black_A

* **Prim路径 (Prim Path):**/World/Conveyor_9/Looks/Plastic_Rough_Black_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_9/Looks/Plastic_Rough_Black_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_9/Looks/Plastic_Rough_Black_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Plastic/Misc/Plastic_Rough_Black_A.mdl' (Sub Id: 'Plastic_Rough_Black_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Plastic/Misc/Plastic_Rough_Black_A.mdl'

---

### /World/Conveyor_9/Looks/Steel_A

* **Prim路径 (Prim Path):**/World/Conveyor_9/Looks/Steel_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_9/Looks/Steel_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_9/Looks/Steel_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Metal/Steel/Steel_A.mdl' (Sub Id: 'Steel_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Metal/Steel/Steel_A.mdl'
    * Inputs:
      * 'diffuse_tint' [color3f] = '(0.772, 0.772, 0.772)'
      * 'reflection_roughness_constant' [float] = '0.67'
      * 'reflection_roughness_texture_influence' [float] = '0.88'

---

### /World/Conveyor_10/Looks/Acrylic_Clear_Glossy_A

* **Prim路径 (Prim Path):**/World/Conveyor_10/Looks/Acrylic_Clear_Glossy_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_10/Looks/Acrylic_Clear_Glossy_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_10/Looks/Acrylic_Clear_Glossy_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniGlass.mdl' (Sub Id: 'OmniGlass')
    * 纹理引用 (Texture Assets):
      * '../Material Library/Plastic/Textures/T_Acrylic_Clear_Glossy_A_Rough.png'
      * '../Material Library/Plastic/Textures/T_Plastic_Rough_Black_A_Normal.png'
    * Inputs:
      * 'normal_map_strength' [float] = '0.5'
      * 'texture_scale' [float2] = '(1.000, 3.000)'
      * 'normal_map_texture' [asset] = '../Material Library/Plastic/Textures/T_Plastic_Rough_Black_A_Normal.png'
      * 'roughness_texture' [asset] = '../Material Library/Plastic/Textures/T_Acrylic_Clear_Glossy_A_Rough.png'
      * 'roughness_texture_influence' [float] = '0.3'
      * 'glass_ior' [float] = '1.05'
      * 'frosting_roughness' [float] = '0.17'
      * 'glass_color' [color3f] = '(0.734, 0.734, 0.734)'

---

### /World/Conveyor_10/Looks/M_ConveyorBelt_A01_Belt

* **Prim路径 (Prim Path):**/World/Conveyor_10/Looks/M_ConveyorBelt_A01_Belt
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_10/Looks/M_ConveyorBelt_A01_Belt/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_10/Looks/M_ConveyorBelt_A01_Belt/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * 纹理引用 (Texture Assets):
      * './T_ConveyorBelt_A01_Belt_Albedo.png'
      * './T_ConveyorBelt_A01_Belt_Normal.png'
      * './T_ConveyorBelt_A01_Belt_ORM.png'
    * Inputs:
      * 'normalmap_texture' [asset] = './T_ConveyorBelt_A01_Belt_Normal.png'
      * 'diffuse_texture' [asset] = './T_ConveyorBelt_A01_Belt_Albedo.png'
      * 'reflection_roughness_texture_influence' [float] = '1'
      * 'metallic_texture_influence' [float] = '1'
      * 'ORM_texture' [asset] = './T_ConveyorBelt_A01_Belt_ORM.png'

---

### /World/Conveyor_10/Looks/M_ConveyorBelt_A01_Decal

* **Prim路径 (Prim Path):**/World/Conveyor_10/Looks/M_ConveyorBelt_A01_Decal
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_10/Looks/M_ConveyorBelt_A01_Decal/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_10/Looks/M_ConveyorBelt_A01_Decal/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * 纹理引用 (Texture Assets):
      * './T_ConveyorsBelt_A01_Decal_Albedo.png'
      * './T_ConveyorsBelt_A01_Decal_Alpha.png'
      * './T_ConveyorsBelt_A01_Decal_ORM.png'
    * Inputs:
      * 'opacity_texture' [asset] = './T_ConveyorsBelt_A01_Decal_Alpha.png'
      * 'diffuse_texture' [asset] = './T_ConveyorsBelt_A01_Decal_Albedo.png'
      * 'reflection_roughness_texture_influence' [float] = '1'
      * 'metallic_texture_influence' [float] = '1'
      * 'ORM_texture' [asset] = './T_ConveyorsBelt_A01_Decal_ORM.png'

---

### /World/Conveyor_10/Looks/Metal_Rough_A

* **Prim路径 (Prim Path):**/World/Conveyor_10/Looks/Metal_Rough_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_10/Looks/Metal_Rough_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_10/Looks/Metal_Rough_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Metal/Misc/Metal_Rough_A.mdl' (Sub Id: 'Metal_Rough_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Metal/Misc/Metal_Rough_A.mdl'

---

### /World/Conveyor_10/Looks/MetalPainted_Black_Glossy_A

* **Prim路径 (Prim Path):**/World/Conveyor_10/Looks/MetalPainted_Black_Glossy_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_10/Looks/MetalPainted_Black_Glossy_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_10/Looks/MetalPainted_Black_Glossy_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Metal/Painted/MetalPainted_White_Glossy_A.mdl' (Sub Id: 'MetalPainted_White_Glossy_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Metal/Painted/MetalPainted_White_Glossy_A.mdl'
    * Inputs:
      * 'bump_factor' [float] = '0.5'
      * 'texture_scale' [float2] = '(1.500, 1.500)'
      * 'diffuse_tint' [color3f] = '(0.066, 0.066, 0.066)'
      * 'reflection_roughness_constant' [float] = '0.63'
      * 'reflection_roughness_texture_influence' [float] = '0.91'

---

### /World/Conveyor_10/Looks/MetalPainted_Blue_Glossy_A

* **Prim路径 (Prim Path):**/World/Conveyor_10/Looks/MetalPainted_Blue_Glossy_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_10/Looks/MetalPainted_Blue_Glossy_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_10/Looks/MetalPainted_Blue_Glossy_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Metal/Painted/MetalPainted_White_Glossy_A.mdl' (Sub Id: 'MetalPainted_White_Glossy_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Metal/Painted/MetalPainted_White_Glossy_A.mdl'
    * 纹理引用 (Texture Assets):
      * '../Material Library/Metal/Painted/T_MetalPainted_White_Glossy_A_Albedo.png'
      * '../Material Library/Metal/Painted/T_MetalPainted_White_Glossy_A_Normal.png'
      * '../Material Library/Metal/Painted/T_MetalPainted_White_Glossy_A_ORM.png'
    * Inputs:
      * 'bump_factor' [float] = '0.5'
      * 'normalmap_texture' [asset] = '../Material Library/Metal/Painted/T_MetalPainted_White_Glossy_A_Normal.png'
      * 'texture_scale' [float2] = '(1.500, 1.500)'
      * 'diffuse_texture' [asset] = '../Material Library/Metal/Painted/T_MetalPainted_White_Glossy_A_Albedo.png'
      * 'diffuse_tint' [color3f] = '(0.077, 0.203, 0.587)'
      * 'ORM_texture' [asset] = '../Material Library/Metal/Painted/T_MetalPainted_White_Glossy_A_ORM.png'

---

### /World/Conveyor_10/Looks/Plastic_Orange_A

* **Prim路径 (Prim Path):**/World/Conveyor_10/Looks/Plastic_Orange_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_10/Looks/Plastic_Orange_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_10/Looks/Plastic_Orange_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Plastic/Misc/Plastic_Orange_A.mdl' (Sub Id: 'Plastic_Orange_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Plastic/Misc/Plastic_Orange_A.mdl'

---

### /World/Conveyor_10/Looks/Plastic_Red_A

* **Prim路径 (Prim Path):**/World/Conveyor_10/Looks/Plastic_Red_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_10/Looks/Plastic_Red_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_10/Looks/Plastic_Red_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Plastic/Misc/Plastic_Red_A.mdl' (Sub Id: 'Plastic_Red_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Plastic/Misc/Plastic_Red_A.mdl'

---

### /World/Conveyor_10/Looks/Plastic_Rough_Black_A

* **Prim路径 (Prim Path):**/World/Conveyor_10/Looks/Plastic_Rough_Black_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_10/Looks/Plastic_Rough_Black_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_10/Looks/Plastic_Rough_Black_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Plastic/Misc/Plastic_Rough_Black_A.mdl' (Sub Id: 'Plastic_Rough_Black_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Plastic/Misc/Plastic_Rough_Black_A.mdl'

---

### /World/Conveyor_10/Looks/Steel_A

* **Prim路径 (Prim Path):**/World/Conveyor_10/Looks/Steel_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_10/Looks/Steel_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_10/Looks/Steel_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Metal/Steel/Steel_A.mdl' (Sub Id: 'Steel_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Metal/Steel/Steel_A.mdl'
    * Inputs:
      * 'diffuse_tint' [color3f] = '(0.772, 0.772, 0.772)'
      * 'reflection_roughness_constant' [float] = '0.67'
      * 'reflection_roughness_texture_influence' [float] = '0.88'

---

### /World/Conveyor_11/Looks/Acrylic_Clear_Glossy_A

* **Prim路径 (Prim Path):**/World/Conveyor_11/Looks/Acrylic_Clear_Glossy_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_11/Looks/Acrylic_Clear_Glossy_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_11/Looks/Acrylic_Clear_Glossy_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniGlass.mdl' (Sub Id: 'OmniGlass')
    * 纹理引用 (Texture Assets):
      * '../Material Library/Plastic/Textures/T_Acrylic_Clear_Glossy_A_Rough.png'
      * '../Material Library/Plastic/Textures/T_Plastic_Rough_Black_A_Normal.png'
    * Inputs:
      * 'normal_map_strength' [float] = '0.5'
      * 'texture_scale' [float2] = '(1.000, 3.000)'
      * 'normal_map_texture' [asset] = '../Material Library/Plastic/Textures/T_Plastic_Rough_Black_A_Normal.png'
      * 'roughness_texture' [asset] = '../Material Library/Plastic/Textures/T_Acrylic_Clear_Glossy_A_Rough.png'
      * 'roughness_texture_influence' [float] = '0.3'
      * 'glass_ior' [float] = '1.05'
      * 'frosting_roughness' [float] = '0.17'
      * 'glass_color' [color3f] = '(0.734, 0.734, 0.734)'

---

### /World/Conveyor_11/Looks/M_ConveyorBelt_A01_Belt

* **Prim路径 (Prim Path):**/World/Conveyor_11/Looks/M_ConveyorBelt_A01_Belt
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_11/Looks/M_ConveyorBelt_A01_Belt/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_11/Looks/M_ConveyorBelt_A01_Belt/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * 纹理引用 (Texture Assets):
      * './T_ConveyorBelt_A01_Belt_Albedo.png'
      * './T_ConveyorBelt_A01_Belt_Normal.png'
      * './T_ConveyorBelt_A01_Belt_ORM.png'
    * Inputs:
      * 'normalmap_texture' [asset] = './T_ConveyorBelt_A01_Belt_Normal.png'
      * 'diffuse_texture' [asset] = './T_ConveyorBelt_A01_Belt_Albedo.png'
      * 'reflection_roughness_texture_influence' [float] = '1'
      * 'metallic_texture_influence' [float] = '1'
      * 'ORM_texture' [asset] = './T_ConveyorBelt_A01_Belt_ORM.png'

---

### /World/Conveyor_11/Looks/M_ConveyorBelt_A01_Decal

* **Prim路径 (Prim Path):**/World/Conveyor_11/Looks/M_ConveyorBelt_A01_Decal
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_11/Looks/M_ConveyorBelt_A01_Decal/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_11/Looks/M_ConveyorBelt_A01_Decal/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * 纹理引用 (Texture Assets):
      * './T_ConveyorsBelt_A01_Decal_Albedo.png'
      * './T_ConveyorsBelt_A01_Decal_Alpha.png'
      * './T_ConveyorsBelt_A01_Decal_ORM.png'
    * Inputs:
      * 'opacity_texture' [asset] = './T_ConveyorsBelt_A01_Decal_Alpha.png'
      * 'diffuse_texture' [asset] = './T_ConveyorsBelt_A01_Decal_Albedo.png'
      * 'reflection_roughness_texture_influence' [float] = '1'
      * 'metallic_texture_influence' [float] = '1'
      * 'ORM_texture' [asset] = './T_ConveyorsBelt_A01_Decal_ORM.png'

---

### /World/Conveyor_11/Looks/Metal_Rough_A

* **Prim路径 (Prim Path):**/World/Conveyor_11/Looks/Metal_Rough_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_11/Looks/Metal_Rough_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_11/Looks/Metal_Rough_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Metal/Misc/Metal_Rough_A.mdl' (Sub Id: 'Metal_Rough_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Metal/Misc/Metal_Rough_A.mdl'

---

### /World/Conveyor_11/Looks/MetalPainted_Black_Glossy_A

* **Prim路径 (Prim Path):**/World/Conveyor_11/Looks/MetalPainted_Black_Glossy_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_11/Looks/MetalPainted_Black_Glossy_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_11/Looks/MetalPainted_Black_Glossy_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Metal/Painted/MetalPainted_White_Glossy_A.mdl' (Sub Id: 'MetalPainted_White_Glossy_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Metal/Painted/MetalPainted_White_Glossy_A.mdl'
    * Inputs:
      * 'bump_factor' [float] = '0.5'
      * 'texture_scale' [float2] = '(1.500, 1.500)'
      * 'diffuse_tint' [color3f] = '(0.066, 0.066, 0.066)'
      * 'reflection_roughness_constant' [float] = '0.63'
      * 'reflection_roughness_texture_influence' [float] = '0.91'

---

### /World/Conveyor_11/Looks/MetalPainted_Blue_Glossy_A

* **Prim路径 (Prim Path):**/World/Conveyor_11/Looks/MetalPainted_Blue_Glossy_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_11/Looks/MetalPainted_Blue_Glossy_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_11/Looks/MetalPainted_Blue_Glossy_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Metal/Painted/MetalPainted_White_Glossy_A.mdl' (Sub Id: 'MetalPainted_White_Glossy_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Metal/Painted/MetalPainted_White_Glossy_A.mdl'
    * 纹理引用 (Texture Assets):
      * '../Material Library/Metal/Painted/T_MetalPainted_White_Glossy_A_Albedo.png'
      * '../Material Library/Metal/Painted/T_MetalPainted_White_Glossy_A_Normal.png'
      * '../Material Library/Metal/Painted/T_MetalPainted_White_Glossy_A_ORM.png'
    * Inputs:
      * 'bump_factor' [float] = '0.5'
      * 'normalmap_texture' [asset] = '../Material Library/Metal/Painted/T_MetalPainted_White_Glossy_A_Normal.png'
      * 'texture_scale' [float2] = '(1.500, 1.500)'
      * 'diffuse_texture' [asset] = '../Material Library/Metal/Painted/T_MetalPainted_White_Glossy_A_Albedo.png'
      * 'diffuse_tint' [color3f] = '(0.077, 0.203, 0.587)'
      * 'ORM_texture' [asset] = '../Material Library/Metal/Painted/T_MetalPainted_White_Glossy_A_ORM.png'

---

### /World/Conveyor_11/Looks/Plastic_Orange_A

* **Prim路径 (Prim Path):**/World/Conveyor_11/Looks/Plastic_Orange_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_11/Looks/Plastic_Orange_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_11/Looks/Plastic_Orange_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Plastic/Misc/Plastic_Orange_A.mdl' (Sub Id: 'Plastic_Orange_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Plastic/Misc/Plastic_Orange_A.mdl'

---

### /World/Conveyor_11/Looks/Plastic_Red_A

* **Prim路径 (Prim Path):**/World/Conveyor_11/Looks/Plastic_Red_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_11/Looks/Plastic_Red_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_11/Looks/Plastic_Red_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Plastic/Misc/Plastic_Red_A.mdl' (Sub Id: 'Plastic_Red_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Plastic/Misc/Plastic_Red_A.mdl'

---

### /World/Conveyor_11/Looks/Plastic_Rough_Black_A

* **Prim路径 (Prim Path):**/World/Conveyor_11/Looks/Plastic_Rough_Black_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_11/Looks/Plastic_Rough_Black_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_11/Looks/Plastic_Rough_Black_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Plastic/Misc/Plastic_Rough_Black_A.mdl' (Sub Id: 'Plastic_Rough_Black_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Plastic/Misc/Plastic_Rough_Black_A.mdl'

---

### /World/Conveyor_11/Looks/Steel_A

* **Prim路径 (Prim Path):**/World/Conveyor_11/Looks/Steel_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_11/Looks/Steel_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_11/Looks/Steel_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Metal/Steel/Steel_A.mdl' (Sub Id: 'Steel_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Metal/Steel/Steel_A.mdl'
    * Inputs:
      * 'diffuse_tint' [color3f] = '(0.772, 0.772, 0.772)'
      * 'reflection_roughness_constant' [float] = '0.67'
      * 'reflection_roughness_texture_influence' [float] = '0.88'

---

### /World/Conveyor_12/Looks/Acrylic_Clear_Glossy_A

* **Prim路径 (Prim Path):**/World/Conveyor_12/Looks/Acrylic_Clear_Glossy_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_12/Looks/Acrylic_Clear_Glossy_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_12/Looks/Acrylic_Clear_Glossy_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniGlass.mdl' (Sub Id: 'OmniGlass')
    * 纹理引用 (Texture Assets):
      * '../Material Library/Plastic/Textures/T_Acrylic_Clear_Glossy_A_Rough.png'
      * '../Material Library/Plastic/Textures/T_Plastic_Rough_Black_A_Normal.png'
    * Inputs:
      * 'normal_map_strength' [float] = '0.5'
      * 'texture_scale' [float2] = '(1.000, 3.000)'
      * 'normal_map_texture' [asset] = '../Material Library/Plastic/Textures/T_Plastic_Rough_Black_A_Normal.png'
      * 'roughness_texture' [asset] = '../Material Library/Plastic/Textures/T_Acrylic_Clear_Glossy_A_Rough.png'
      * 'roughness_texture_influence' [float] = '0.3'
      * 'glass_ior' [float] = '1.05'
      * 'frosting_roughness' [float] = '0.17'
      * 'glass_color' [color3f] = '(0.734, 0.734, 0.734)'

---

### /World/Conveyor_12/Looks/M_ConveyorBelt_A01_Belt

* **Prim路径 (Prim Path):**/World/Conveyor_12/Looks/M_ConveyorBelt_A01_Belt
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_12/Looks/M_ConveyorBelt_A01_Belt/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_12/Looks/M_ConveyorBelt_A01_Belt/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * 纹理引用 (Texture Assets):
      * './T_ConveyorBelt_A01_Belt_Albedo.png'
      * './T_ConveyorBelt_A01_Belt_Normal.png'
      * './T_ConveyorBelt_A01_Belt_ORM.png'
    * Inputs:
      * 'normalmap_texture' [asset] = './T_ConveyorBelt_A01_Belt_Normal.png'
      * 'diffuse_texture' [asset] = './T_ConveyorBelt_A01_Belt_Albedo.png'
      * 'reflection_roughness_texture_influence' [float] = '1'
      * 'metallic_texture_influence' [float] = '1'
      * 'ORM_texture' [asset] = './T_ConveyorBelt_A01_Belt_ORM.png'

---

### /World/Conveyor_12/Looks/M_ConveyorBelt_A01_Decal

* **Prim路径 (Prim Path):**/World/Conveyor_12/Looks/M_ConveyorBelt_A01_Decal
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_12/Looks/M_ConveyorBelt_A01_Decal/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_12/Looks/M_ConveyorBelt_A01_Decal/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * 纹理引用 (Texture Assets):
      * './T_ConveyorsBelt_A01_Decal_Albedo.png'
      * './T_ConveyorsBelt_A01_Decal_Alpha.png'
      * './T_ConveyorsBelt_A01_Decal_ORM.png'
    * Inputs:
      * 'opacity_texture' [asset] = './T_ConveyorsBelt_A01_Decal_Alpha.png'
      * 'diffuse_texture' [asset] = './T_ConveyorsBelt_A01_Decal_Albedo.png'
      * 'reflection_roughness_texture_influence' [float] = '1'
      * 'metallic_texture_influence' [float] = '1'
      * 'ORM_texture' [asset] = './T_ConveyorsBelt_A01_Decal_ORM.png'

---

### /World/Conveyor_12/Looks/Metal_Rough_A

* **Prim路径 (Prim Path):**/World/Conveyor_12/Looks/Metal_Rough_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_12/Looks/Metal_Rough_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_12/Looks/Metal_Rough_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Metal/Misc/Metal_Rough_A.mdl' (Sub Id: 'Metal_Rough_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Metal/Misc/Metal_Rough_A.mdl'

---

### /World/Conveyor_12/Looks/MetalPainted_Black_Glossy_A

* **Prim路径 (Prim Path):**/World/Conveyor_12/Looks/MetalPainted_Black_Glossy_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_12/Looks/MetalPainted_Black_Glossy_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_12/Looks/MetalPainted_Black_Glossy_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Metal/Painted/MetalPainted_White_Glossy_A.mdl' (Sub Id: 'MetalPainted_White_Glossy_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Metal/Painted/MetalPainted_White_Glossy_A.mdl'
    * Inputs:
      * 'bump_factor' [float] = '0.5'
      * 'texture_scale' [float2] = '(1.500, 1.500)'
      * 'diffuse_tint' [color3f] = '(0.066, 0.066, 0.066)'
      * 'reflection_roughness_constant' [float] = '0.63'
      * 'reflection_roughness_texture_influence' [float] = '0.91'

---

### /World/Conveyor_12/Looks/MetalPainted_Blue_Glossy_A

* **Prim路径 (Prim Path):**/World/Conveyor_12/Looks/MetalPainted_Blue_Glossy_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_12/Looks/MetalPainted_Blue_Glossy_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_12/Looks/MetalPainted_Blue_Glossy_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Metal/Painted/MetalPainted_White_Glossy_A.mdl' (Sub Id: 'MetalPainted_White_Glossy_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Metal/Painted/MetalPainted_White_Glossy_A.mdl'
    * 纹理引用 (Texture Assets):
      * '../Material Library/Metal/Painted/T_MetalPainted_White_Glossy_A_Albedo.png'
      * '../Material Library/Metal/Painted/T_MetalPainted_White_Glossy_A_Normal.png'
      * '../Material Library/Metal/Painted/T_MetalPainted_White_Glossy_A_ORM.png'
    * Inputs:
      * 'bump_factor' [float] = '0.5'
      * 'normalmap_texture' [asset] = '../Material Library/Metal/Painted/T_MetalPainted_White_Glossy_A_Normal.png'
      * 'texture_scale' [float2] = '(1.500, 1.500)'
      * 'diffuse_texture' [asset] = '../Material Library/Metal/Painted/T_MetalPainted_White_Glossy_A_Albedo.png'
      * 'diffuse_tint' [color3f] = '(0.077, 0.203, 0.587)'
      * 'ORM_texture' [asset] = '../Material Library/Metal/Painted/T_MetalPainted_White_Glossy_A_ORM.png'

---

### /World/Conveyor_12/Looks/Plastic_Orange_A

* **Prim路径 (Prim Path):**/World/Conveyor_12/Looks/Plastic_Orange_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_12/Looks/Plastic_Orange_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_12/Looks/Plastic_Orange_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Plastic/Misc/Plastic_Orange_A.mdl' (Sub Id: 'Plastic_Orange_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Plastic/Misc/Plastic_Orange_A.mdl'

---

### /World/Conveyor_12/Looks/Plastic_Red_A

* **Prim路径 (Prim Path):**/World/Conveyor_12/Looks/Plastic_Red_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_12/Looks/Plastic_Red_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_12/Looks/Plastic_Red_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Plastic/Misc/Plastic_Red_A.mdl' (Sub Id: 'Plastic_Red_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Plastic/Misc/Plastic_Red_A.mdl'

---

### /World/Conveyor_12/Looks/Plastic_Rough_Black_A

* **Prim路径 (Prim Path):**/World/Conveyor_12/Looks/Plastic_Rough_Black_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_12/Looks/Plastic_Rough_Black_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_12/Looks/Plastic_Rough_Black_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Plastic/Misc/Plastic_Rough_Black_A.mdl' (Sub Id: 'Plastic_Rough_Black_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Plastic/Misc/Plastic_Rough_Black_A.mdl'

---

### /World/Conveyor_12/Looks/Steel_A

* **Prim路径 (Prim Path):**/World/Conveyor_12/Looks/Steel_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_12/Looks/Steel_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_12/Looks/Steel_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Metal/Steel/Steel_A.mdl' (Sub Id: 'Steel_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Metal/Steel/Steel_A.mdl'
    * Inputs:
      * 'diffuse_tint' [color3f] = '(0.772, 0.772, 0.772)'
      * 'reflection_roughness_constant' [float] = '0.67'
      * 'reflection_roughness_texture_influence' [float] = '0.88'

---

### /World/Conveyor_13/Looks/Acrylic_Clear_Glossy_A

* **Prim路径 (Prim Path):**/World/Conveyor_13/Looks/Acrylic_Clear_Glossy_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_13/Looks/Acrylic_Clear_Glossy_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_13/Looks/Acrylic_Clear_Glossy_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniGlass.mdl' (Sub Id: 'OmniGlass')
    * 纹理引用 (Texture Assets):
      * '../Material Library/Plastic/Textures/T_Acrylic_Clear_Glossy_A_Rough.png'
      * '../Material Library/Plastic/Textures/T_Plastic_Rough_Black_A_Normal.png'
    * Inputs:
      * 'normal_map_strength' [float] = '0.5'
      * 'texture_scale' [float2] = '(1.000, 3.000)'
      * 'normal_map_texture' [asset] = '../Material Library/Plastic/Textures/T_Plastic_Rough_Black_A_Normal.png'
      * 'roughness_texture' [asset] = '../Material Library/Plastic/Textures/T_Acrylic_Clear_Glossy_A_Rough.png'
      * 'roughness_texture_influence' [float] = '0.3'
      * 'glass_ior' [float] = '1.05'
      * 'frosting_roughness' [float] = '0.17'
      * 'glass_color' [color3f] = '(0.734, 0.734, 0.734)'

---

### /World/Conveyor_13/Looks/M_ConveyorBelt_A01_Belt

* **Prim路径 (Prim Path):**/World/Conveyor_13/Looks/M_ConveyorBelt_A01_Belt
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_13/Looks/M_ConveyorBelt_A01_Belt/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_13/Looks/M_ConveyorBelt_A01_Belt/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * 纹理引用 (Texture Assets):
      * './T_ConveyorBelt_A01_Belt_Albedo.png'
      * './T_ConveyorBelt_A01_Belt_Normal.png'
      * './T_ConveyorBelt_A01_Belt_ORM.png'
    * Inputs:
      * 'normalmap_texture' [asset] = './T_ConveyorBelt_A01_Belt_Normal.png'
      * 'diffuse_texture' [asset] = './T_ConveyorBelt_A01_Belt_Albedo.png'
      * 'reflection_roughness_texture_influence' [float] = '1'
      * 'metallic_texture_influence' [float] = '1'
      * 'ORM_texture' [asset] = './T_ConveyorBelt_A01_Belt_ORM.png'

---

### /World/Conveyor_13/Looks/M_ConveyorBelt_A01_Decal

* **Prim路径 (Prim Path):**/World/Conveyor_13/Looks/M_ConveyorBelt_A01_Decal
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_13/Looks/M_ConveyorBelt_A01_Decal/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_13/Looks/M_ConveyorBelt_A01_Decal/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * 纹理引用 (Texture Assets):
      * './T_ConveyorsBelt_A01_Decal_Albedo.png'
      * './T_ConveyorsBelt_A01_Decal_Alpha.png'
      * './T_ConveyorsBelt_A01_Decal_ORM.png'
    * Inputs:
      * 'opacity_texture' [asset] = './T_ConveyorsBelt_A01_Decal_Alpha.png'
      * 'diffuse_texture' [asset] = './T_ConveyorsBelt_A01_Decal_Albedo.png'
      * 'reflection_roughness_texture_influence' [float] = '1'
      * 'metallic_texture_influence' [float] = '1'
      * 'ORM_texture' [asset] = './T_ConveyorsBelt_A01_Decal_ORM.png'

---

### /World/Conveyor_13/Looks/Metal_Rough_A

* **Prim路径 (Prim Path):**/World/Conveyor_13/Looks/Metal_Rough_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_13/Looks/Metal_Rough_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_13/Looks/Metal_Rough_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Metal/Misc/Metal_Rough_A.mdl' (Sub Id: 'Metal_Rough_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Metal/Misc/Metal_Rough_A.mdl'

---

### /World/Conveyor_13/Looks/MetalPainted_Black_Glossy_A

* **Prim路径 (Prim Path):**/World/Conveyor_13/Looks/MetalPainted_Black_Glossy_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_13/Looks/MetalPainted_Black_Glossy_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_13/Looks/MetalPainted_Black_Glossy_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Metal/Painted/MetalPainted_White_Glossy_A.mdl' (Sub Id: 'MetalPainted_White_Glossy_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Metal/Painted/MetalPainted_White_Glossy_A.mdl'
    * Inputs:
      * 'bump_factor' [float] = '0.5'
      * 'texture_scale' [float2] = '(1.500, 1.500)'
      * 'diffuse_tint' [color3f] = '(0.066, 0.066, 0.066)'
      * 'reflection_roughness_constant' [float] = '0.63'
      * 'reflection_roughness_texture_influence' [float] = '0.91'

---

### /World/Conveyor_13/Looks/MetalPainted_Blue_Glossy_A

* **Prim路径 (Prim Path):**/World/Conveyor_13/Looks/MetalPainted_Blue_Glossy_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_13/Looks/MetalPainted_Blue_Glossy_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_13/Looks/MetalPainted_Blue_Glossy_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Metal/Painted/MetalPainted_White_Glossy_A.mdl' (Sub Id: 'MetalPainted_White_Glossy_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Metal/Painted/MetalPainted_White_Glossy_A.mdl'
    * 纹理引用 (Texture Assets):
      * '../Material Library/Metal/Painted/T_MetalPainted_White_Glossy_A_Albedo.png'
      * '../Material Library/Metal/Painted/T_MetalPainted_White_Glossy_A_Normal.png'
      * '../Material Library/Metal/Painted/T_MetalPainted_White_Glossy_A_ORM.png'
    * Inputs:
      * 'bump_factor' [float] = '0.5'
      * 'normalmap_texture' [asset] = '../Material Library/Metal/Painted/T_MetalPainted_White_Glossy_A_Normal.png'
      * 'texture_scale' [float2] = '(1.500, 1.500)'
      * 'diffuse_texture' [asset] = '../Material Library/Metal/Painted/T_MetalPainted_White_Glossy_A_Albedo.png'
      * 'diffuse_tint' [color3f] = '(0.077, 0.203, 0.587)'
      * 'ORM_texture' [asset] = '../Material Library/Metal/Painted/T_MetalPainted_White_Glossy_A_ORM.png'

---

### /World/Conveyor_13/Looks/Plastic_Orange_A

* **Prim路径 (Prim Path):**/World/Conveyor_13/Looks/Plastic_Orange_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_13/Looks/Plastic_Orange_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_13/Looks/Plastic_Orange_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Plastic/Misc/Plastic_Orange_A.mdl' (Sub Id: 'Plastic_Orange_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Plastic/Misc/Plastic_Orange_A.mdl'

---

### /World/Conveyor_13/Looks/Plastic_Red_A

* **Prim路径 (Prim Path):**/World/Conveyor_13/Looks/Plastic_Red_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_13/Looks/Plastic_Red_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_13/Looks/Plastic_Red_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Plastic/Misc/Plastic_Red_A.mdl' (Sub Id: 'Plastic_Red_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Plastic/Misc/Plastic_Red_A.mdl'

---

### /World/Conveyor_13/Looks/Plastic_Rough_Black_A

* **Prim路径 (Prim Path):**/World/Conveyor_13/Looks/Plastic_Rough_Black_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_13/Looks/Plastic_Rough_Black_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_13/Looks/Plastic_Rough_Black_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Plastic/Misc/Plastic_Rough_Black_A.mdl' (Sub Id: 'Plastic_Rough_Black_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Plastic/Misc/Plastic_Rough_Black_A.mdl'

---

### /World/Conveyor_13/Looks/Steel_A

* **Prim路径 (Prim Path):**/World/Conveyor_13/Looks/Steel_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_13/Looks/Steel_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_13/Looks/Steel_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Metal/Steel/Steel_A.mdl' (Sub Id: 'Steel_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Metal/Steel/Steel_A.mdl'
    * Inputs:
      * 'diffuse_tint' [color3f] = '(0.772, 0.772, 0.772)'
      * 'reflection_roughness_constant' [float] = '0.67'
      * 'reflection_roughness_texture_influence' [float] = '0.88'

---

### /World/Conveyor_14/Looks/Acrylic_Clear_Glossy_A

* **Prim路径 (Prim Path):**/World/Conveyor_14/Looks/Acrylic_Clear_Glossy_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_14/Looks/Acrylic_Clear_Glossy_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_14/Looks/Acrylic_Clear_Glossy_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniGlass.mdl' (Sub Id: 'OmniGlass')
    * 纹理引用 (Texture Assets):
      * '../Material Library/Plastic/Textures/T_Acrylic_Clear_Glossy_A_Rough.png'
      * '../Material Library/Plastic/Textures/T_Plastic_Rough_Black_A_Normal.png'
    * Inputs:
      * 'normal_map_strength' [float] = '0.5'
      * 'texture_scale' [float2] = '(1.000, 3.000)'
      * 'normal_map_texture' [asset] = '../Material Library/Plastic/Textures/T_Plastic_Rough_Black_A_Normal.png'
      * 'roughness_texture' [asset] = '../Material Library/Plastic/Textures/T_Acrylic_Clear_Glossy_A_Rough.png'
      * 'roughness_texture_influence' [float] = '0.3'
      * 'glass_ior' [float] = '1.05'
      * 'frosting_roughness' [float] = '0.17'
      * 'glass_color' [color3f] = '(0.734, 0.734, 0.734)'

---

### /World/Conveyor_14/Looks/M_ConveyorBelt_A01_Belt

* **Prim路径 (Prim Path):**/World/Conveyor_14/Looks/M_ConveyorBelt_A01_Belt
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_14/Looks/M_ConveyorBelt_A01_Belt/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_14/Looks/M_ConveyorBelt_A01_Belt/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * 纹理引用 (Texture Assets):
      * './T_ConveyorBelt_A01_Belt_Albedo.png'
      * './T_ConveyorBelt_A01_Belt_Normal.png'
      * './T_ConveyorBelt_A01_Belt_ORM.png'
    * Inputs:
      * 'normalmap_texture' [asset] = './T_ConveyorBelt_A01_Belt_Normal.png'
      * 'diffuse_texture' [asset] = './T_ConveyorBelt_A01_Belt_Albedo.png'
      * 'reflection_roughness_texture_influence' [float] = '1'
      * 'metallic_texture_influence' [float] = '1'
      * 'ORM_texture' [asset] = './T_ConveyorBelt_A01_Belt_ORM.png'

---

### /World/Conveyor_14/Looks/M_ConveyorBelt_A01_Decal

* **Prim路径 (Prim Path):**/World/Conveyor_14/Looks/M_ConveyorBelt_A01_Decal
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_14/Looks/M_ConveyorBelt_A01_Decal/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_14/Looks/M_ConveyorBelt_A01_Decal/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * 纹理引用 (Texture Assets):
      * './T_ConveyorsBelt_A01_Decal_Albedo.png'
      * './T_ConveyorsBelt_A01_Decal_Alpha.png'
      * './T_ConveyorsBelt_A01_Decal_ORM.png'
    * Inputs:
      * 'opacity_texture' [asset] = './T_ConveyorsBelt_A01_Decal_Alpha.png'
      * 'diffuse_texture' [asset] = './T_ConveyorsBelt_A01_Decal_Albedo.png'
      * 'reflection_roughness_texture_influence' [float] = '1'
      * 'metallic_texture_influence' [float] = '1'
      * 'ORM_texture' [asset] = './T_ConveyorsBelt_A01_Decal_ORM.png'

---

### /World/Conveyor_14/Looks/Metal_Rough_A

* **Prim路径 (Prim Path):**/World/Conveyor_14/Looks/Metal_Rough_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_14/Looks/Metal_Rough_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_14/Looks/Metal_Rough_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Metal/Misc/Metal_Rough_A.mdl' (Sub Id: 'Metal_Rough_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Metal/Misc/Metal_Rough_A.mdl'

---

### /World/Conveyor_14/Looks/MetalPainted_Black_Glossy_A

* **Prim路径 (Prim Path):**/World/Conveyor_14/Looks/MetalPainted_Black_Glossy_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_14/Looks/MetalPainted_Black_Glossy_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_14/Looks/MetalPainted_Black_Glossy_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Metal/Painted/MetalPainted_White_Glossy_A.mdl' (Sub Id: 'MetalPainted_White_Glossy_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Metal/Painted/MetalPainted_White_Glossy_A.mdl'
    * Inputs:
      * 'bump_factor' [float] = '0.5'
      * 'texture_scale' [float2] = '(1.500, 1.500)'
      * 'diffuse_tint' [color3f] = '(0.066, 0.066, 0.066)'
      * 'reflection_roughness_constant' [float] = '0.63'
      * 'reflection_roughness_texture_influence' [float] = '0.91'

---

### /World/Conveyor_14/Looks/MetalPainted_Blue_Glossy_A

* **Prim路径 (Prim Path):**/World/Conveyor_14/Looks/MetalPainted_Blue_Glossy_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_14/Looks/MetalPainted_Blue_Glossy_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_14/Looks/MetalPainted_Blue_Glossy_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Metal/Painted/MetalPainted_White_Glossy_A.mdl' (Sub Id: 'MetalPainted_White_Glossy_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Metal/Painted/MetalPainted_White_Glossy_A.mdl'
    * 纹理引用 (Texture Assets):
      * '../Material Library/Metal/Painted/T_MetalPainted_White_Glossy_A_Albedo.png'
      * '../Material Library/Metal/Painted/T_MetalPainted_White_Glossy_A_Normal.png'
      * '../Material Library/Metal/Painted/T_MetalPainted_White_Glossy_A_ORM.png'
    * Inputs:
      * 'bump_factor' [float] = '0.5'
      * 'normalmap_texture' [asset] = '../Material Library/Metal/Painted/T_MetalPainted_White_Glossy_A_Normal.png'
      * 'texture_scale' [float2] = '(1.500, 1.500)'
      * 'diffuse_texture' [asset] = '../Material Library/Metal/Painted/T_MetalPainted_White_Glossy_A_Albedo.png'
      * 'diffuse_tint' [color3f] = '(0.077, 0.203, 0.587)'
      * 'ORM_texture' [asset] = '../Material Library/Metal/Painted/T_MetalPainted_White_Glossy_A_ORM.png'

---

### /World/Conveyor_14/Looks/Plastic_Orange_A

* **Prim路径 (Prim Path):**/World/Conveyor_14/Looks/Plastic_Orange_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_14/Looks/Plastic_Orange_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_14/Looks/Plastic_Orange_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Plastic/Misc/Plastic_Orange_A.mdl' (Sub Id: 'Plastic_Orange_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Plastic/Misc/Plastic_Orange_A.mdl'

---

### /World/Conveyor_14/Looks/Plastic_Red_A

* **Prim路径 (Prim Path):**/World/Conveyor_14/Looks/Plastic_Red_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_14/Looks/Plastic_Red_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_14/Looks/Plastic_Red_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Plastic/Misc/Plastic_Red_A.mdl' (Sub Id: 'Plastic_Red_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Plastic/Misc/Plastic_Red_A.mdl'

---

### /World/Conveyor_14/Looks/Plastic_Rough_Black_A

* **Prim路径 (Prim Path):**/World/Conveyor_14/Looks/Plastic_Rough_Black_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_14/Looks/Plastic_Rough_Black_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_14/Looks/Plastic_Rough_Black_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Plastic/Misc/Plastic_Rough_Black_A.mdl' (Sub Id: 'Plastic_Rough_Black_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Plastic/Misc/Plastic_Rough_Black_A.mdl'

---

### /World/Conveyor_14/Looks/Steel_A

* **Prim路径 (Prim Path):**/World/Conveyor_14/Looks/Steel_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_14/Looks/Steel_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_14/Looks/Steel_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Metal/Steel/Steel_A.mdl' (Sub Id: 'Steel_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Metal/Steel/Steel_A.mdl'
    * Inputs:
      * 'diffuse_tint' [color3f] = '(0.772, 0.772, 0.772)'
      * 'reflection_roughness_constant' [float] = '0.67'
      * 'reflection_roughness_texture_influence' [float] = '0.88'

---

### /World/Conveyor_15/Looks/Acrylic_Clear_Glossy_A

* **Prim路径 (Prim Path):**/World/Conveyor_15/Looks/Acrylic_Clear_Glossy_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_15/Looks/Acrylic_Clear_Glossy_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_15/Looks/Acrylic_Clear_Glossy_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniGlass.mdl' (Sub Id: 'OmniGlass')
    * 纹理引用 (Texture Assets):
      * '../Material Library/Plastic/Textures/T_Acrylic_Clear_Glossy_A_Rough.png'
      * '../Material Library/Plastic/Textures/T_Plastic_Rough_Black_A_Normal.png'
    * Inputs:
      * 'normal_map_strength' [float] = '0.5'
      * 'texture_scale' [float2] = '(1.000, 3.000)'
      * 'normal_map_texture' [asset] = '../Material Library/Plastic/Textures/T_Plastic_Rough_Black_A_Normal.png'
      * 'roughness_texture' [asset] = '../Material Library/Plastic/Textures/T_Acrylic_Clear_Glossy_A_Rough.png'
      * 'roughness_texture_influence' [float] = '0.3'
      * 'glass_ior' [float] = '1.05'
      * 'frosting_roughness' [float] = '0.17'
      * 'glass_color' [color3f] = '(0.734, 0.734, 0.734)'

---

### /World/Conveyor_15/Looks/M_ConveyorBelt_A01_Belt

* **Prim路径 (Prim Path):**/World/Conveyor_15/Looks/M_ConveyorBelt_A01_Belt
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_15/Looks/M_ConveyorBelt_A01_Belt/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_15/Looks/M_ConveyorBelt_A01_Belt/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * 纹理引用 (Texture Assets):
      * './T_ConveyorBelt_A01_Belt_Albedo.png'
      * './T_ConveyorBelt_A01_Belt_Normal.png'
      * './T_ConveyorBelt_A01_Belt_ORM.png'
    * Inputs:
      * 'normalmap_texture' [asset] = './T_ConveyorBelt_A01_Belt_Normal.png'
      * 'diffuse_texture' [asset] = './T_ConveyorBelt_A01_Belt_Albedo.png'
      * 'reflection_roughness_texture_influence' [float] = '1'
      * 'metallic_texture_influence' [float] = '1'
      * 'ORM_texture' [asset] = './T_ConveyorBelt_A01_Belt_ORM.png'

---

### /World/Conveyor_15/Looks/M_ConveyorBelt_A01_Decal

* **Prim路径 (Prim Path):**/World/Conveyor_15/Looks/M_ConveyorBelt_A01_Decal
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_15/Looks/M_ConveyorBelt_A01_Decal/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_15/Looks/M_ConveyorBelt_A01_Decal/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * 纹理引用 (Texture Assets):
      * './T_ConveyorsBelt_A01_Decal_Albedo.png'
      * './T_ConveyorsBelt_A01_Decal_Alpha.png'
      * './T_ConveyorsBelt_A01_Decal_ORM.png'
    * Inputs:
      * 'opacity_texture' [asset] = './T_ConveyorsBelt_A01_Decal_Alpha.png'
      * 'diffuse_texture' [asset] = './T_ConveyorsBelt_A01_Decal_Albedo.png'
      * 'reflection_roughness_texture_influence' [float] = '1'
      * 'metallic_texture_influence' [float] = '1'
      * 'ORM_texture' [asset] = './T_ConveyorsBelt_A01_Decal_ORM.png'

---

### /World/Conveyor_15/Looks/Metal_Rough_A

* **Prim路径 (Prim Path):**/World/Conveyor_15/Looks/Metal_Rough_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_15/Looks/Metal_Rough_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_15/Looks/Metal_Rough_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Metal/Misc/Metal_Rough_A.mdl' (Sub Id: 'Metal_Rough_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Metal/Misc/Metal_Rough_A.mdl'

---

### /World/Conveyor_15/Looks/MetalPainted_Black_Glossy_A

* **Prim路径 (Prim Path):**/World/Conveyor_15/Looks/MetalPainted_Black_Glossy_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_15/Looks/MetalPainted_Black_Glossy_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_15/Looks/MetalPainted_Black_Glossy_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Metal/Painted/MetalPainted_White_Glossy_A.mdl' (Sub Id: 'MetalPainted_White_Glossy_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Metal/Painted/MetalPainted_White_Glossy_A.mdl'
    * Inputs:
      * 'bump_factor' [float] = '0.5'
      * 'texture_scale' [float2] = '(1.500, 1.500)'
      * 'diffuse_tint' [color3f] = '(0.066, 0.066, 0.066)'
      * 'reflection_roughness_constant' [float] = '0.63'
      * 'reflection_roughness_texture_influence' [float] = '0.91'

---

### /World/Conveyor_15/Looks/MetalPainted_Blue_Glossy_A

* **Prim路径 (Prim Path):**/World/Conveyor_15/Looks/MetalPainted_Blue_Glossy_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_15/Looks/MetalPainted_Blue_Glossy_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_15/Looks/MetalPainted_Blue_Glossy_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Metal/Painted/MetalPainted_White_Glossy_A.mdl' (Sub Id: 'MetalPainted_White_Glossy_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Metal/Painted/MetalPainted_White_Glossy_A.mdl'
    * 纹理引用 (Texture Assets):
      * '../Material Library/Metal/Painted/T_MetalPainted_White_Glossy_A_Albedo.png'
      * '../Material Library/Metal/Painted/T_MetalPainted_White_Glossy_A_Normal.png'
      * '../Material Library/Metal/Painted/T_MetalPainted_White_Glossy_A_ORM.png'
    * Inputs:
      * 'bump_factor' [float] = '0.5'
      * 'normalmap_texture' [asset] = '../Material Library/Metal/Painted/T_MetalPainted_White_Glossy_A_Normal.png'
      * 'texture_scale' [float2] = '(1.500, 1.500)'
      * 'diffuse_texture' [asset] = '../Material Library/Metal/Painted/T_MetalPainted_White_Glossy_A_Albedo.png'
      * 'diffuse_tint' [color3f] = '(0.077, 0.203, 0.587)'
      * 'ORM_texture' [asset] = '../Material Library/Metal/Painted/T_MetalPainted_White_Glossy_A_ORM.png'

---

### /World/Conveyor_15/Looks/Plastic_Orange_A

* **Prim路径 (Prim Path):**/World/Conveyor_15/Looks/Plastic_Orange_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_15/Looks/Plastic_Orange_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_15/Looks/Plastic_Orange_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Plastic/Misc/Plastic_Orange_A.mdl' (Sub Id: 'Plastic_Orange_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Plastic/Misc/Plastic_Orange_A.mdl'

---

### /World/Conveyor_15/Looks/Plastic_Red_A

* **Prim路径 (Prim Path):**/World/Conveyor_15/Looks/Plastic_Red_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_15/Looks/Plastic_Red_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_15/Looks/Plastic_Red_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Plastic/Misc/Plastic_Red_A.mdl' (Sub Id: 'Plastic_Red_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Plastic/Misc/Plastic_Red_A.mdl'

---

### /World/Conveyor_15/Looks/Plastic_Rough_Black_A

* **Prim路径 (Prim Path):**/World/Conveyor_15/Looks/Plastic_Rough_Black_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_15/Looks/Plastic_Rough_Black_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_15/Looks/Plastic_Rough_Black_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Plastic/Misc/Plastic_Rough_Black_A.mdl' (Sub Id: 'Plastic_Rough_Black_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Plastic/Misc/Plastic_Rough_Black_A.mdl'

---

### /World/Conveyor_15/Looks/Steel_A

* **Prim路径 (Prim Path):**/World/Conveyor_15/Looks/Steel_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_15/Looks/Steel_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_15/Looks/Steel_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Metal/Steel/Steel_A.mdl' (Sub Id: 'Steel_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Metal/Steel/Steel_A.mdl'
    * Inputs:
      * 'diffuse_tint' [color3f] = '(0.772, 0.772, 0.772)'
      * 'reflection_roughness_constant' [float] = '0.67'
      * 'reflection_roughness_texture_influence' [float] = '0.88'

---

### /World/Conveyor_16/Looks/Acrylic_Clear_Glossy_A

* **Prim路径 (Prim Path):**/World/Conveyor_16/Looks/Acrylic_Clear_Glossy_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_16/Looks/Acrylic_Clear_Glossy_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_16/Looks/Acrylic_Clear_Glossy_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniGlass.mdl' (Sub Id: 'OmniGlass')
    * 纹理引用 (Texture Assets):
      * '../Material Library/Plastic/Textures/T_Acrylic_Clear_Glossy_A_Rough.png'
      * '../Material Library/Plastic/Textures/T_Plastic_Rough_Black_A_Normal.png'
    * Inputs:
      * 'normal_map_strength' [float] = '0.5'
      * 'texture_scale' [float2] = '(1.000, 3.000)'
      * 'normal_map_texture' [asset] = '../Material Library/Plastic/Textures/T_Plastic_Rough_Black_A_Normal.png'
      * 'roughness_texture' [asset] = '../Material Library/Plastic/Textures/T_Acrylic_Clear_Glossy_A_Rough.png'
      * 'roughness_texture_influence' [float] = '0.3'
      * 'glass_ior' [float] = '1.05'
      * 'frosting_roughness' [float] = '0.17'
      * 'glass_color' [color3f] = '(0.734, 0.734, 0.734)'

---

### /World/Conveyor_16/Looks/M_ConveyorBelt_A01_Belt

* **Prim路径 (Prim Path):**/World/Conveyor_16/Looks/M_ConveyorBelt_A01_Belt
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_16/Looks/M_ConveyorBelt_A01_Belt/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_16/Looks/M_ConveyorBelt_A01_Belt/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * 纹理引用 (Texture Assets):
      * './T_ConveyorBelt_A01_Belt_Albedo.png'
      * './T_ConveyorBelt_A01_Belt_Normal.png'
      * './T_ConveyorBelt_A01_Belt_ORM.png'
    * Inputs:
      * 'normalmap_texture' [asset] = './T_ConveyorBelt_A01_Belt_Normal.png'
      * 'diffuse_texture' [asset] = './T_ConveyorBelt_A01_Belt_Albedo.png'
      * 'reflection_roughness_texture_influence' [float] = '1'
      * 'metallic_texture_influence' [float] = '1'
      * 'ORM_texture' [asset] = './T_ConveyorBelt_A01_Belt_ORM.png'

---

### /World/Conveyor_16/Looks/M_ConveyorBelt_A01_Decal

* **Prim路径 (Prim Path):**/World/Conveyor_16/Looks/M_ConveyorBelt_A01_Decal
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_16/Looks/M_ConveyorBelt_A01_Decal/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_16/Looks/M_ConveyorBelt_A01_Decal/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * 纹理引用 (Texture Assets):
      * './T_ConveyorsBelt_A01_Decal_Albedo.png'
      * './T_ConveyorsBelt_A01_Decal_Alpha.png'
      * './T_ConveyorsBelt_A01_Decal_ORM.png'
    * Inputs:
      * 'opacity_texture' [asset] = './T_ConveyorsBelt_A01_Decal_Alpha.png'
      * 'diffuse_texture' [asset] = './T_ConveyorsBelt_A01_Decal_Albedo.png'
      * 'reflection_roughness_texture_influence' [float] = '1'
      * 'metallic_texture_influence' [float] = '1'
      * 'ORM_texture' [asset] = './T_ConveyorsBelt_A01_Decal_ORM.png'

---

### /World/Conveyor_16/Looks/Metal_Rough_A

* **Prim路径 (Prim Path):**/World/Conveyor_16/Looks/Metal_Rough_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_16/Looks/Metal_Rough_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_16/Looks/Metal_Rough_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Metal/Misc/Metal_Rough_A.mdl' (Sub Id: 'Metal_Rough_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Metal/Misc/Metal_Rough_A.mdl'

---

### /World/Conveyor_16/Looks/MetalPainted_Black_Glossy_A

* **Prim路径 (Prim Path):**/World/Conveyor_16/Looks/MetalPainted_Black_Glossy_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_16/Looks/MetalPainted_Black_Glossy_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_16/Looks/MetalPainted_Black_Glossy_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Metal/Painted/MetalPainted_White_Glossy_A.mdl' (Sub Id: 'MetalPainted_White_Glossy_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Metal/Painted/MetalPainted_White_Glossy_A.mdl'
    * Inputs:
      * 'bump_factor' [float] = '0.5'
      * 'texture_scale' [float2] = '(1.500, 1.500)'
      * 'diffuse_tint' [color3f] = '(0.066, 0.066, 0.066)'
      * 'reflection_roughness_constant' [float] = '0.63'
      * 'reflection_roughness_texture_influence' [float] = '0.91'

---

### /World/Conveyor_16/Looks/MetalPainted_Blue_Glossy_A

* **Prim路径 (Prim Path):**/World/Conveyor_16/Looks/MetalPainted_Blue_Glossy_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_16/Looks/MetalPainted_Blue_Glossy_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_16/Looks/MetalPainted_Blue_Glossy_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Metal/Painted/MetalPainted_White_Glossy_A.mdl' (Sub Id: 'MetalPainted_White_Glossy_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Metal/Painted/MetalPainted_White_Glossy_A.mdl'
    * 纹理引用 (Texture Assets):
      * '../Material Library/Metal/Painted/T_MetalPainted_White_Glossy_A_Albedo.png'
      * '../Material Library/Metal/Painted/T_MetalPainted_White_Glossy_A_Normal.png'
      * '../Material Library/Metal/Painted/T_MetalPainted_White_Glossy_A_ORM.png'
    * Inputs:
      * 'bump_factor' [float] = '0.5'
      * 'normalmap_texture' [asset] = '../Material Library/Metal/Painted/T_MetalPainted_White_Glossy_A_Normal.png'
      * 'texture_scale' [float2] = '(1.500, 1.500)'
      * 'diffuse_texture' [asset] = '../Material Library/Metal/Painted/T_MetalPainted_White_Glossy_A_Albedo.png'
      * 'diffuse_tint' [color3f] = '(0.077, 0.203, 0.587)'
      * 'ORM_texture' [asset] = '../Material Library/Metal/Painted/T_MetalPainted_White_Glossy_A_ORM.png'

---

### /World/Conveyor_16/Looks/Plastic_Orange_A

* **Prim路径 (Prim Path):**/World/Conveyor_16/Looks/Plastic_Orange_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_16/Looks/Plastic_Orange_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_16/Looks/Plastic_Orange_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Plastic/Misc/Plastic_Orange_A.mdl' (Sub Id: 'Plastic_Orange_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Plastic/Misc/Plastic_Orange_A.mdl'

---

### /World/Conveyor_16/Looks/Plastic_Red_A

* **Prim路径 (Prim Path):**/World/Conveyor_16/Looks/Plastic_Red_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_16/Looks/Plastic_Red_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_16/Looks/Plastic_Red_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Plastic/Misc/Plastic_Red_A.mdl' (Sub Id: 'Plastic_Red_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Plastic/Misc/Plastic_Red_A.mdl'

---

### /World/Conveyor_16/Looks/Plastic_Rough_Black_A

* **Prim路径 (Prim Path):**/World/Conveyor_16/Looks/Plastic_Rough_Black_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_16/Looks/Plastic_Rough_Black_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_16/Looks/Plastic_Rough_Black_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Plastic/Misc/Plastic_Rough_Black_A.mdl' (Sub Id: 'Plastic_Rough_Black_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Plastic/Misc/Plastic_Rough_Black_A.mdl'

---

### /World/Conveyor_16/Looks/Steel_A

* **Prim路径 (Prim Path):**/World/Conveyor_16/Looks/Steel_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_16/Looks/Steel_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_16/Looks/Steel_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Metal/Steel/Steel_A.mdl' (Sub Id: 'Steel_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Metal/Steel/Steel_A.mdl'
    * Inputs:
      * 'diffuse_tint' [color3f] = '(0.772, 0.772, 0.772)'
      * 'reflection_roughness_constant' [float] = '0.67'
      * 'reflection_roughness_texture_influence' [float] = '0.88'

---

### /World/Conveyor_17/Looks/Acrylic_Clear_Glossy_A

* **Prim路径 (Prim Path):**/World/Conveyor_17/Looks/Acrylic_Clear_Glossy_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_17/Looks/Acrylic_Clear_Glossy_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_17/Looks/Acrylic_Clear_Glossy_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniGlass.mdl' (Sub Id: 'OmniGlass')
    * 纹理引用 (Texture Assets):
      * '../Material Library/Plastic/Textures/T_Acrylic_Clear_Glossy_A_Rough.png'
      * '../Material Library/Plastic/Textures/T_Plastic_Rough_Black_A_Normal.png'
    * Inputs:
      * 'normal_map_strength' [float] = '0.5'
      * 'texture_scale' [float2] = '(1.000, 3.000)'
      * 'normal_map_texture' [asset] = '../Material Library/Plastic/Textures/T_Plastic_Rough_Black_A_Normal.png'
      * 'roughness_texture' [asset] = '../Material Library/Plastic/Textures/T_Acrylic_Clear_Glossy_A_Rough.png'
      * 'roughness_texture_influence' [float] = '0.3'
      * 'glass_ior' [float] = '1.05'
      * 'frosting_roughness' [float] = '0.17'
      * 'glass_color' [color3f] = '(0.734, 0.734, 0.734)'

---

### /World/Conveyor_17/Looks/M_ConveyorBelt_A01_Belt

* **Prim路径 (Prim Path):**/World/Conveyor_17/Looks/M_ConveyorBelt_A01_Belt
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_17/Looks/M_ConveyorBelt_A01_Belt/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_17/Looks/M_ConveyorBelt_A01_Belt/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * 纹理引用 (Texture Assets):
      * './T_ConveyorBelt_A01_Belt_Albedo.png'
      * './T_ConveyorBelt_A01_Belt_Normal.png'
      * './T_ConveyorBelt_A01_Belt_ORM.png'
    * Inputs:
      * 'normalmap_texture' [asset] = './T_ConveyorBelt_A01_Belt_Normal.png'
      * 'diffuse_texture' [asset] = './T_ConveyorBelt_A01_Belt_Albedo.png'
      * 'reflection_roughness_texture_influence' [float] = '1'
      * 'metallic_texture_influence' [float] = '1'
      * 'ORM_texture' [asset] = './T_ConveyorBelt_A01_Belt_ORM.png'

---

### /World/Conveyor_17/Looks/M_ConveyorBelt_A01_Decal

* **Prim路径 (Prim Path):**/World/Conveyor_17/Looks/M_ConveyorBelt_A01_Decal
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_17/Looks/M_ConveyorBelt_A01_Decal/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_17/Looks/M_ConveyorBelt_A01_Decal/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * 纹理引用 (Texture Assets):
      * './T_ConveyorsBelt_A01_Decal_Albedo.png'
      * './T_ConveyorsBelt_A01_Decal_Alpha.png'
      * './T_ConveyorsBelt_A01_Decal_ORM.png'
    * Inputs:
      * 'opacity_texture' [asset] = './T_ConveyorsBelt_A01_Decal_Alpha.png'
      * 'diffuse_texture' [asset] = './T_ConveyorsBelt_A01_Decal_Albedo.png'
      * 'reflection_roughness_texture_influence' [float] = '1'
      * 'metallic_texture_influence' [float] = '1'
      * 'ORM_texture' [asset] = './T_ConveyorsBelt_A01_Decal_ORM.png'

---

### /World/Conveyor_17/Looks/Metal_Rough_A

* **Prim路径 (Prim Path):**/World/Conveyor_17/Looks/Metal_Rough_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_17/Looks/Metal_Rough_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_17/Looks/Metal_Rough_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Metal/Misc/Metal_Rough_A.mdl' (Sub Id: 'Metal_Rough_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Metal/Misc/Metal_Rough_A.mdl'

---

### /World/Conveyor_17/Looks/MetalPainted_Black_Glossy_A

* **Prim路径 (Prim Path):**/World/Conveyor_17/Looks/MetalPainted_Black_Glossy_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_17/Looks/MetalPainted_Black_Glossy_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_17/Looks/MetalPainted_Black_Glossy_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Metal/Painted/MetalPainted_White_Glossy_A.mdl' (Sub Id: 'MetalPainted_White_Glossy_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Metal/Painted/MetalPainted_White_Glossy_A.mdl'
    * Inputs:
      * 'bump_factor' [float] = '0.5'
      * 'texture_scale' [float2] = '(1.500, 1.500)'
      * 'diffuse_tint' [color3f] = '(0.066, 0.066, 0.066)'
      * 'reflection_roughness_constant' [float] = '0.63'
      * 'reflection_roughness_texture_influence' [float] = '0.91'

---

### /World/Conveyor_17/Looks/MetalPainted_Blue_Glossy_A

* **Prim路径 (Prim Path):**/World/Conveyor_17/Looks/MetalPainted_Blue_Glossy_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_17/Looks/MetalPainted_Blue_Glossy_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_17/Looks/MetalPainted_Blue_Glossy_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Metal/Painted/MetalPainted_White_Glossy_A.mdl' (Sub Id: 'MetalPainted_White_Glossy_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Metal/Painted/MetalPainted_White_Glossy_A.mdl'
    * 纹理引用 (Texture Assets):
      * '../Material Library/Metal/Painted/T_MetalPainted_White_Glossy_A_Albedo.png'
      * '../Material Library/Metal/Painted/T_MetalPainted_White_Glossy_A_Normal.png'
      * '../Material Library/Metal/Painted/T_MetalPainted_White_Glossy_A_ORM.png'
    * Inputs:
      * 'bump_factor' [float] = '0.5'
      * 'normalmap_texture' [asset] = '../Material Library/Metal/Painted/T_MetalPainted_White_Glossy_A_Normal.png'
      * 'texture_scale' [float2] = '(1.500, 1.500)'
      * 'diffuse_texture' [asset] = '../Material Library/Metal/Painted/T_MetalPainted_White_Glossy_A_Albedo.png'
      * 'diffuse_tint' [color3f] = '(0.077, 0.203, 0.587)'
      * 'ORM_texture' [asset] = '../Material Library/Metal/Painted/T_MetalPainted_White_Glossy_A_ORM.png'

---

### /World/Conveyor_17/Looks/Plastic_Orange_A

* **Prim路径 (Prim Path):**/World/Conveyor_17/Looks/Plastic_Orange_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_17/Looks/Plastic_Orange_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_17/Looks/Plastic_Orange_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Plastic/Misc/Plastic_Orange_A.mdl' (Sub Id: 'Plastic_Orange_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Plastic/Misc/Plastic_Orange_A.mdl'

---

### /World/Conveyor_17/Looks/Plastic_Red_A

* **Prim路径 (Prim Path):**/World/Conveyor_17/Looks/Plastic_Red_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_17/Looks/Plastic_Red_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_17/Looks/Plastic_Red_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Plastic/Misc/Plastic_Red_A.mdl' (Sub Id: 'Plastic_Red_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Plastic/Misc/Plastic_Red_A.mdl'

---

### /World/Conveyor_17/Looks/Plastic_Rough_Black_A

* **Prim路径 (Prim Path):**/World/Conveyor_17/Looks/Plastic_Rough_Black_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_17/Looks/Plastic_Rough_Black_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_17/Looks/Plastic_Rough_Black_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Plastic/Misc/Plastic_Rough_Black_A.mdl' (Sub Id: 'Plastic_Rough_Black_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Plastic/Misc/Plastic_Rough_Black_A.mdl'

---

### /World/Conveyor_17/Looks/Steel_A

* **Prim路径 (Prim Path):**/World/Conveyor_17/Looks/Steel_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_17/Looks/Steel_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_17/Looks/Steel_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Metal/Steel/Steel_A.mdl' (Sub Id: 'Steel_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Metal/Steel/Steel_A.mdl'
    * Inputs:
      * 'diffuse_tint' [color3f] = '(0.772, 0.772, 0.772)'
      * 'reflection_roughness_constant' [float] = '0.67'
      * 'reflection_roughness_texture_influence' [float] = '0.88'

---

### /World/Conveyor_18/Looks/Acrylic_Clear_Glossy_A

* **Prim路径 (Prim Path):**/World/Conveyor_18/Looks/Acrylic_Clear_Glossy_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_18/Looks/Acrylic_Clear_Glossy_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_18/Looks/Acrylic_Clear_Glossy_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniGlass.mdl' (Sub Id: 'OmniGlass')
    * 纹理引用 (Texture Assets):
      * '../Material Library/Plastic/Textures/T_Acrylic_Clear_Glossy_A_Rough.png'
      * '../Material Library/Plastic/Textures/T_Plastic_Rough_Black_A_Normal.png'
    * Inputs:
      * 'normal_map_strength' [float] = '0.5'
      * 'texture_scale' [float2] = '(1.000, 3.000)'
      * 'normal_map_texture' [asset] = '../Material Library/Plastic/Textures/T_Plastic_Rough_Black_A_Normal.png'
      * 'roughness_texture' [asset] = '../Material Library/Plastic/Textures/T_Acrylic_Clear_Glossy_A_Rough.png'
      * 'roughness_texture_influence' [float] = '0.3'
      * 'glass_ior' [float] = '1.05'
      * 'frosting_roughness' [float] = '0.17'
      * 'glass_color' [color3f] = '(0.734, 0.734, 0.734)'

---

### /World/Conveyor_18/Looks/M_ConveyorBelt_A01_Belt

* **Prim路径 (Prim Path):**/World/Conveyor_18/Looks/M_ConveyorBelt_A01_Belt
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_18/Looks/M_ConveyorBelt_A01_Belt/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_18/Looks/M_ConveyorBelt_A01_Belt/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * 纹理引用 (Texture Assets):
      * './T_ConveyorBelt_A01_Belt_Albedo.png'
      * './T_ConveyorBelt_A01_Belt_Normal.png'
      * './T_ConveyorBelt_A01_Belt_ORM.png'
    * Inputs:
      * 'normalmap_texture' [asset] = './T_ConveyorBelt_A01_Belt_Normal.png'
      * 'diffuse_texture' [asset] = './T_ConveyorBelt_A01_Belt_Albedo.png'
      * 'reflection_roughness_texture_influence' [float] = '1'
      * 'metallic_texture_influence' [float] = '1'
      * 'ORM_texture' [asset] = './T_ConveyorBelt_A01_Belt_ORM.png'

---

### /World/Conveyor_18/Looks/M_ConveyorBelt_A01_Decal

* **Prim路径 (Prim Path):**/World/Conveyor_18/Looks/M_ConveyorBelt_A01_Decal
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_18/Looks/M_ConveyorBelt_A01_Decal/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_18/Looks/M_ConveyorBelt_A01_Decal/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * 纹理引用 (Texture Assets):
      * './T_ConveyorsBelt_A01_Decal_Albedo.png'
      * './T_ConveyorsBelt_A01_Decal_Alpha.png'
      * './T_ConveyorsBelt_A01_Decal_ORM.png'
    * Inputs:
      * 'opacity_texture' [asset] = './T_ConveyorsBelt_A01_Decal_Alpha.png'
      * 'diffuse_texture' [asset] = './T_ConveyorsBelt_A01_Decal_Albedo.png'
      * 'reflection_roughness_texture_influence' [float] = '1'
      * 'metallic_texture_influence' [float] = '1'
      * 'ORM_texture' [asset] = './T_ConveyorsBelt_A01_Decal_ORM.png'

---

### /World/Conveyor_18/Looks/Metal_Rough_A

* **Prim路径 (Prim Path):**/World/Conveyor_18/Looks/Metal_Rough_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_18/Looks/Metal_Rough_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_18/Looks/Metal_Rough_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Metal/Misc/Metal_Rough_A.mdl' (Sub Id: 'Metal_Rough_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Metal/Misc/Metal_Rough_A.mdl'

---

### /World/Conveyor_18/Looks/MetalPainted_Black_Glossy_A

* **Prim路径 (Prim Path):**/World/Conveyor_18/Looks/MetalPainted_Black_Glossy_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_18/Looks/MetalPainted_Black_Glossy_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_18/Looks/MetalPainted_Black_Glossy_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Metal/Painted/MetalPainted_White_Glossy_A.mdl' (Sub Id: 'MetalPainted_White_Glossy_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Metal/Painted/MetalPainted_White_Glossy_A.mdl'
    * Inputs:
      * 'bump_factor' [float] = '0.5'
      * 'texture_scale' [float2] = '(1.500, 1.500)'
      * 'diffuse_tint' [color3f] = '(0.066, 0.066, 0.066)'
      * 'reflection_roughness_constant' [float] = '0.63'
      * 'reflection_roughness_texture_influence' [float] = '0.91'

---

### /World/Conveyor_18/Looks/MetalPainted_Blue_Glossy_A

* **Prim路径 (Prim Path):**/World/Conveyor_18/Looks/MetalPainted_Blue_Glossy_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_18/Looks/MetalPainted_Blue_Glossy_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_18/Looks/MetalPainted_Blue_Glossy_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Metal/Painted/MetalPainted_White_Glossy_A.mdl' (Sub Id: 'MetalPainted_White_Glossy_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Metal/Painted/MetalPainted_White_Glossy_A.mdl'
    * 纹理引用 (Texture Assets):
      * '../Material Library/Metal/Painted/T_MetalPainted_White_Glossy_A_Albedo.png'
      * '../Material Library/Metal/Painted/T_MetalPainted_White_Glossy_A_Normal.png'
      * '../Material Library/Metal/Painted/T_MetalPainted_White_Glossy_A_ORM.png'
    * Inputs:
      * 'bump_factor' [float] = '0.5'
      * 'normalmap_texture' [asset] = '../Material Library/Metal/Painted/T_MetalPainted_White_Glossy_A_Normal.png'
      * 'texture_scale' [float2] = '(1.500, 1.500)'
      * 'diffuse_texture' [asset] = '../Material Library/Metal/Painted/T_MetalPainted_White_Glossy_A_Albedo.png'
      * 'diffuse_tint' [color3f] = '(0.077, 0.203, 0.587)'
      * 'ORM_texture' [asset] = '../Material Library/Metal/Painted/T_MetalPainted_White_Glossy_A_ORM.png'

---

### /World/Conveyor_18/Looks/Plastic_Orange_A

* **Prim路径 (Prim Path):**/World/Conveyor_18/Looks/Plastic_Orange_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_18/Looks/Plastic_Orange_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_18/Looks/Plastic_Orange_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Plastic/Misc/Plastic_Orange_A.mdl' (Sub Id: 'Plastic_Orange_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Plastic/Misc/Plastic_Orange_A.mdl'

---

### /World/Conveyor_18/Looks/Plastic_Red_A

* **Prim路径 (Prim Path):**/World/Conveyor_18/Looks/Plastic_Red_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_18/Looks/Plastic_Red_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_18/Looks/Plastic_Red_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Plastic/Misc/Plastic_Red_A.mdl' (Sub Id: 'Plastic_Red_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Plastic/Misc/Plastic_Red_A.mdl'

---

### /World/Conveyor_18/Looks/Plastic_Rough_Black_A

* **Prim路径 (Prim Path):**/World/Conveyor_18/Looks/Plastic_Rough_Black_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_18/Looks/Plastic_Rough_Black_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_18/Looks/Plastic_Rough_Black_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Plastic/Misc/Plastic_Rough_Black_A.mdl' (Sub Id: 'Plastic_Rough_Black_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Plastic/Misc/Plastic_Rough_Black_A.mdl'

---

### /World/Conveyor_18/Looks/Steel_A

* **Prim路径 (Prim Path):**/World/Conveyor_18/Looks/Steel_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_18/Looks/Steel_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_18/Looks/Steel_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Metal/Steel/Steel_A.mdl' (Sub Id: 'Steel_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Metal/Steel/Steel_A.mdl'
    * Inputs:
      * 'diffuse_tint' [color3f] = '(0.772, 0.772, 0.772)'
      * 'reflection_roughness_constant' [float] = '0.67'
      * 'reflection_roughness_texture_influence' [float] = '0.88'

---

### /World/Conveyor_19/Looks/Acrylic_Clear_Glossy_A

* **Prim路径 (Prim Path):**/World/Conveyor_19/Looks/Acrylic_Clear_Glossy_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_19/Looks/Acrylic_Clear_Glossy_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_19/Looks/Acrylic_Clear_Glossy_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniGlass.mdl' (Sub Id: 'OmniGlass')
    * 纹理引用 (Texture Assets):
      * '../Material Library/Plastic/Textures/T_Acrylic_Clear_Glossy_A_Rough.png'
      * '../Material Library/Plastic/Textures/T_Plastic_Rough_Black_A_Normal.png'
    * Inputs:
      * 'normal_map_strength' [float] = '0.5'
      * 'texture_scale' [float2] = '(1.000, 3.000)'
      * 'normal_map_texture' [asset] = '../Material Library/Plastic/Textures/T_Plastic_Rough_Black_A_Normal.png'
      * 'roughness_texture' [asset] = '../Material Library/Plastic/Textures/T_Acrylic_Clear_Glossy_A_Rough.png'
      * 'roughness_texture_influence' [float] = '0.3'
      * 'glass_ior' [float] = '1.05'
      * 'frosting_roughness' [float] = '0.17'
      * 'glass_color' [color3f] = '(0.734, 0.734, 0.734)'

---

### /World/Conveyor_19/Looks/M_ConveyorBelt_A01_Belt

* **Prim路径 (Prim Path):**/World/Conveyor_19/Looks/M_ConveyorBelt_A01_Belt
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_19/Looks/M_ConveyorBelt_A01_Belt/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_19/Looks/M_ConveyorBelt_A01_Belt/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * 纹理引用 (Texture Assets):
      * './T_ConveyorBelt_A01_Belt_Albedo.png'
      * './T_ConveyorBelt_A01_Belt_Normal.png'
      * './T_ConveyorBelt_A01_Belt_ORM.png'
    * Inputs:
      * 'normalmap_texture' [asset] = './T_ConveyorBelt_A01_Belt_Normal.png'
      * 'diffuse_texture' [asset] = './T_ConveyorBelt_A01_Belt_Albedo.png'
      * 'reflection_roughness_texture_influence' [float] = '1'
      * 'metallic_texture_influence' [float] = '1'
      * 'ORM_texture' [asset] = './T_ConveyorBelt_A01_Belt_ORM.png'

---

### /World/Conveyor_19/Looks/M_ConveyorBelt_A01_Decal

* **Prim路径 (Prim Path):**/World/Conveyor_19/Looks/M_ConveyorBelt_A01_Decal
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_19/Looks/M_ConveyorBelt_A01_Decal/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_19/Looks/M_ConveyorBelt_A01_Decal/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * 纹理引用 (Texture Assets):
      * './T_ConveyorsBelt_A01_Decal_Albedo.png'
      * './T_ConveyorsBelt_A01_Decal_Alpha.png'
      * './T_ConveyorsBelt_A01_Decal_ORM.png'
    * Inputs:
      * 'opacity_texture' [asset] = './T_ConveyorsBelt_A01_Decal_Alpha.png'
      * 'diffuse_texture' [asset] = './T_ConveyorsBelt_A01_Decal_Albedo.png'
      * 'reflection_roughness_texture_influence' [float] = '1'
      * 'metallic_texture_influence' [float] = '1'
      * 'ORM_texture' [asset] = './T_ConveyorsBelt_A01_Decal_ORM.png'

---

### /World/Conveyor_19/Looks/Metal_Rough_A

* **Prim路径 (Prim Path):**/World/Conveyor_19/Looks/Metal_Rough_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_19/Looks/Metal_Rough_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_19/Looks/Metal_Rough_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Metal/Misc/Metal_Rough_A.mdl' (Sub Id: 'Metal_Rough_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Metal/Misc/Metal_Rough_A.mdl'

---

### /World/Conveyor_19/Looks/MetalPainted_Black_Glossy_A

* **Prim路径 (Prim Path):**/World/Conveyor_19/Looks/MetalPainted_Black_Glossy_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_19/Looks/MetalPainted_Black_Glossy_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_19/Looks/MetalPainted_Black_Glossy_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Metal/Painted/MetalPainted_White_Glossy_A.mdl' (Sub Id: 'MetalPainted_White_Glossy_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Metal/Painted/MetalPainted_White_Glossy_A.mdl'
    * Inputs:
      * 'bump_factor' [float] = '0.5'
      * 'texture_scale' [float2] = '(1.500, 1.500)'
      * 'diffuse_tint' [color3f] = '(0.066, 0.066, 0.066)'
      * 'reflection_roughness_constant' [float] = '0.63'
      * 'reflection_roughness_texture_influence' [float] = '0.91'

---

### /World/Conveyor_19/Looks/MetalPainted_Blue_Glossy_A

* **Prim路径 (Prim Path):**/World/Conveyor_19/Looks/MetalPainted_Blue_Glossy_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_19/Looks/MetalPainted_Blue_Glossy_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_19/Looks/MetalPainted_Blue_Glossy_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Metal/Painted/MetalPainted_White_Glossy_A.mdl' (Sub Id: 'MetalPainted_White_Glossy_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Metal/Painted/MetalPainted_White_Glossy_A.mdl'
    * 纹理引用 (Texture Assets):
      * '../Material Library/Metal/Painted/T_MetalPainted_White_Glossy_A_Albedo.png'
      * '../Material Library/Metal/Painted/T_MetalPainted_White_Glossy_A_Normal.png'
      * '../Material Library/Metal/Painted/T_MetalPainted_White_Glossy_A_ORM.png'
    * Inputs:
      * 'bump_factor' [float] = '0.5'
      * 'normalmap_texture' [asset] = '../Material Library/Metal/Painted/T_MetalPainted_White_Glossy_A_Normal.png'
      * 'texture_scale' [float2] = '(1.500, 1.500)'
      * 'diffuse_texture' [asset] = '../Material Library/Metal/Painted/T_MetalPainted_White_Glossy_A_Albedo.png'
      * 'diffuse_tint' [color3f] = '(0.077, 0.203, 0.587)'
      * 'ORM_texture' [asset] = '../Material Library/Metal/Painted/T_MetalPainted_White_Glossy_A_ORM.png'

---

### /World/Conveyor_19/Looks/Plastic_Orange_A

* **Prim路径 (Prim Path):**/World/Conveyor_19/Looks/Plastic_Orange_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_19/Looks/Plastic_Orange_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_19/Looks/Plastic_Orange_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Plastic/Misc/Plastic_Orange_A.mdl' (Sub Id: 'Plastic_Orange_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Plastic/Misc/Plastic_Orange_A.mdl'

---

### /World/Conveyor_19/Looks/Plastic_Red_A

* **Prim路径 (Prim Path):**/World/Conveyor_19/Looks/Plastic_Red_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_19/Looks/Plastic_Red_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_19/Looks/Plastic_Red_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Plastic/Misc/Plastic_Red_A.mdl' (Sub Id: 'Plastic_Red_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Plastic/Misc/Plastic_Red_A.mdl'

---

### /World/Conveyor_19/Looks/Plastic_Rough_Black_A

* **Prim路径 (Prim Path):**/World/Conveyor_19/Looks/Plastic_Rough_Black_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_19/Looks/Plastic_Rough_Black_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_19/Looks/Plastic_Rough_Black_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Plastic/Misc/Plastic_Rough_Black_A.mdl' (Sub Id: 'Plastic_Rough_Black_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Plastic/Misc/Plastic_Rough_Black_A.mdl'

---

### /World/Conveyor_19/Looks/Steel_A

* **Prim路径 (Prim Path):**/World/Conveyor_19/Looks/Steel_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_19/Looks/Steel_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_19/Looks/Steel_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Metal/Steel/Steel_A.mdl' (Sub Id: 'Steel_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Metal/Steel/Steel_A.mdl'
    * Inputs:
      * 'diffuse_tint' [color3f] = '(0.772, 0.772, 0.772)'
      * 'reflection_roughness_constant' [float] = '0.67'
      * 'reflection_roughness_texture_influence' [float] = '0.88'

---

### /World/Conveyor_20/Looks/Acrylic_Clear_Glossy_A

* **Prim路径 (Prim Path):**/World/Conveyor_20/Looks/Acrylic_Clear_Glossy_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_20/Looks/Acrylic_Clear_Glossy_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_20/Looks/Acrylic_Clear_Glossy_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniGlass.mdl' (Sub Id: 'OmniGlass')
    * 纹理引用 (Texture Assets):
      * '../Material Library/Plastic/Textures/T_Acrylic_Clear_Glossy_A_Rough.png'
      * '../Material Library/Plastic/Textures/T_Plastic_Rough_Black_A_Normal.png'
    * Inputs:
      * 'normal_map_strength' [float] = '0.5'
      * 'texture_scale' [float2] = '(1.000, 3.000)'
      * 'normal_map_texture' [asset] = '../Material Library/Plastic/Textures/T_Plastic_Rough_Black_A_Normal.png'
      * 'roughness_texture' [asset] = '../Material Library/Plastic/Textures/T_Acrylic_Clear_Glossy_A_Rough.png'
      * 'roughness_texture_influence' [float] = '0.3'
      * 'glass_ior' [float] = '1.05'
      * 'frosting_roughness' [float] = '0.17'
      * 'glass_color' [color3f] = '(0.734, 0.734, 0.734)'

---

### /World/Conveyor_20/Looks/M_ConveyorBelt_A01_Belt

* **Prim路径 (Prim Path):**/World/Conveyor_20/Looks/M_ConveyorBelt_A01_Belt
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_20/Looks/M_ConveyorBelt_A01_Belt/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_20/Looks/M_ConveyorBelt_A01_Belt/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * 纹理引用 (Texture Assets):
      * './T_ConveyorBelt_A01_Belt_Albedo.png'
      * './T_ConveyorBelt_A01_Belt_Normal.png'
      * './T_ConveyorBelt_A01_Belt_ORM.png'
    * Inputs:
      * 'normalmap_texture' [asset] = './T_ConveyorBelt_A01_Belt_Normal.png'
      * 'diffuse_texture' [asset] = './T_ConveyorBelt_A01_Belt_Albedo.png'
      * 'reflection_roughness_texture_influence' [float] = '1'
      * 'metallic_texture_influence' [float] = '1'
      * 'ORM_texture' [asset] = './T_ConveyorBelt_A01_Belt_ORM.png'

---

### /World/Conveyor_20/Looks/M_ConveyorBelt_A01_Decal

* **Prim路径 (Prim Path):**/World/Conveyor_20/Looks/M_ConveyorBelt_A01_Decal
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_20/Looks/M_ConveyorBelt_A01_Decal/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_20/Looks/M_ConveyorBelt_A01_Decal/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * 纹理引用 (Texture Assets):
      * './T_ConveyorsBelt_A01_Decal_Albedo.png'
      * './T_ConveyorsBelt_A01_Decal_Alpha.png'
      * './T_ConveyorsBelt_A01_Decal_ORM.png'
    * Inputs:
      * 'opacity_texture' [asset] = './T_ConveyorsBelt_A01_Decal_Alpha.png'
      * 'diffuse_texture' [asset] = './T_ConveyorsBelt_A01_Decal_Albedo.png'
      * 'reflection_roughness_texture_influence' [float] = '1'
      * 'metallic_texture_influence' [float] = '1'
      * 'ORM_texture' [asset] = './T_ConveyorsBelt_A01_Decal_ORM.png'

---

### /World/Conveyor_20/Looks/Metal_Rough_A

* **Prim路径 (Prim Path):**/World/Conveyor_20/Looks/Metal_Rough_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_20/Looks/Metal_Rough_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_20/Looks/Metal_Rough_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Metal/Misc/Metal_Rough_A.mdl' (Sub Id: 'Metal_Rough_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Metal/Misc/Metal_Rough_A.mdl'

---

### /World/Conveyor_20/Looks/MetalPainted_Black_Glossy_A

* **Prim路径 (Prim Path):**/World/Conveyor_20/Looks/MetalPainted_Black_Glossy_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_20/Looks/MetalPainted_Black_Glossy_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_20/Looks/MetalPainted_Black_Glossy_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Metal/Painted/MetalPainted_White_Glossy_A.mdl' (Sub Id: 'MetalPainted_White_Glossy_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Metal/Painted/MetalPainted_White_Glossy_A.mdl'
    * Inputs:
      * 'bump_factor' [float] = '0.5'
      * 'texture_scale' [float2] = '(1.500, 1.500)'
      * 'diffuse_tint' [color3f] = '(0.066, 0.066, 0.066)'
      * 'reflection_roughness_constant' [float] = '0.63'
      * 'reflection_roughness_texture_influence' [float] = '0.91'

---

### /World/Conveyor_20/Looks/MetalPainted_Blue_Glossy_A

* **Prim路径 (Prim Path):**/World/Conveyor_20/Looks/MetalPainted_Blue_Glossy_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_20/Looks/MetalPainted_Blue_Glossy_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_20/Looks/MetalPainted_Blue_Glossy_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Metal/Painted/MetalPainted_White_Glossy_A.mdl' (Sub Id: 'MetalPainted_White_Glossy_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Metal/Painted/MetalPainted_White_Glossy_A.mdl'
    * 纹理引用 (Texture Assets):
      * '../Material Library/Metal/Painted/T_MetalPainted_White_Glossy_A_Albedo.png'
      * '../Material Library/Metal/Painted/T_MetalPainted_White_Glossy_A_Normal.png'
      * '../Material Library/Metal/Painted/T_MetalPainted_White_Glossy_A_ORM.png'
    * Inputs:
      * 'bump_factor' [float] = '0.5'
      * 'normalmap_texture' [asset] = '../Material Library/Metal/Painted/T_MetalPainted_White_Glossy_A_Normal.png'
      * 'texture_scale' [float2] = '(1.500, 1.500)'
      * 'diffuse_texture' [asset] = '../Material Library/Metal/Painted/T_MetalPainted_White_Glossy_A_Albedo.png'
      * 'diffuse_tint' [color3f] = '(0.077, 0.203, 0.587)'
      * 'ORM_texture' [asset] = '../Material Library/Metal/Painted/T_MetalPainted_White_Glossy_A_ORM.png'

---

### /World/Conveyor_20/Looks/Plastic_Orange_A

* **Prim路径 (Prim Path):**/World/Conveyor_20/Looks/Plastic_Orange_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_20/Looks/Plastic_Orange_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_20/Looks/Plastic_Orange_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Plastic/Misc/Plastic_Orange_A.mdl' (Sub Id: 'Plastic_Orange_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Plastic/Misc/Plastic_Orange_A.mdl'

---

### /World/Conveyor_20/Looks/Plastic_Red_A

* **Prim路径 (Prim Path):**/World/Conveyor_20/Looks/Plastic_Red_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_20/Looks/Plastic_Red_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_20/Looks/Plastic_Red_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Plastic/Misc/Plastic_Red_A.mdl' (Sub Id: 'Plastic_Red_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Plastic/Misc/Plastic_Red_A.mdl'

---

### /World/Conveyor_20/Looks/Plastic_Rough_Black_A

* **Prim路径 (Prim Path):**/World/Conveyor_20/Looks/Plastic_Rough_Black_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_20/Looks/Plastic_Rough_Black_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_20/Looks/Plastic_Rough_Black_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Plastic/Misc/Plastic_Rough_Black_A.mdl' (Sub Id: 'Plastic_Rough_Black_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Plastic/Misc/Plastic_Rough_Black_A.mdl'

---

### /World/Conveyor_20/Looks/Steel_A

* **Prim路径 (Prim Path):**/World/Conveyor_20/Looks/Steel_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_20/Looks/Steel_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_20/Looks/Steel_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Metal/Steel/Steel_A.mdl' (Sub Id: 'Steel_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Metal/Steel/Steel_A.mdl'
    * Inputs:
      * 'diffuse_tint' [color3f] = '(0.772, 0.772, 0.772)'
      * 'reflection_roughness_constant' [float] = '0.67'
      * 'reflection_roughness_texture_influence' [float] = '0.88'

---

### /World/Conveyor_21/Looks/Acrylic_Clear_Glossy_A

* **Prim路径 (Prim Path):**/World/Conveyor_21/Looks/Acrylic_Clear_Glossy_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_21/Looks/Acrylic_Clear_Glossy_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_21/Looks/Acrylic_Clear_Glossy_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniGlass.mdl' (Sub Id: 'OmniGlass')
    * 纹理引用 (Texture Assets):
      * '../Material Library/Plastic/Textures/T_Acrylic_Clear_Glossy_A_Rough.png'
      * '../Material Library/Plastic/Textures/T_Plastic_Rough_Black_A_Normal.png'
    * Inputs:
      * 'normal_map_strength' [float] = '0.5'
      * 'texture_scale' [float2] = '(1.000, 3.000)'
      * 'normal_map_texture' [asset] = '../Material Library/Plastic/Textures/T_Plastic_Rough_Black_A_Normal.png'
      * 'roughness_texture' [asset] = '../Material Library/Plastic/Textures/T_Acrylic_Clear_Glossy_A_Rough.png'
      * 'roughness_texture_influence' [float] = '0.3'
      * 'glass_ior' [float] = '1.05'
      * 'frosting_roughness' [float] = '0.17'
      * 'glass_color' [color3f] = '(0.734, 0.734, 0.734)'

---

### /World/Conveyor_21/Looks/M_ConveyorBelt_A01_Belt

* **Prim路径 (Prim Path):**/World/Conveyor_21/Looks/M_ConveyorBelt_A01_Belt
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_21/Looks/M_ConveyorBelt_A01_Belt/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_21/Looks/M_ConveyorBelt_A01_Belt/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * 纹理引用 (Texture Assets):
      * './T_ConveyorBelt_A01_Belt_Albedo.png'
      * './T_ConveyorBelt_A01_Belt_Normal.png'
      * './T_ConveyorBelt_A01_Belt_ORM.png'
    * Inputs:
      * 'normalmap_texture' [asset] = './T_ConveyorBelt_A01_Belt_Normal.png'
      * 'diffuse_texture' [asset] = './T_ConveyorBelt_A01_Belt_Albedo.png'
      * 'reflection_roughness_texture_influence' [float] = '1'
      * 'metallic_texture_influence' [float] = '1'
      * 'ORM_texture' [asset] = './T_ConveyorBelt_A01_Belt_ORM.png'

---

### /World/Conveyor_21/Looks/M_ConveyorBelt_A01_Decal

* **Prim路径 (Prim Path):**/World/Conveyor_21/Looks/M_ConveyorBelt_A01_Decal
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_21/Looks/M_ConveyorBelt_A01_Decal/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_21/Looks/M_ConveyorBelt_A01_Decal/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * 纹理引用 (Texture Assets):
      * './T_ConveyorsBelt_A01_Decal_Albedo.png'
      * './T_ConveyorsBelt_A01_Decal_Alpha.png'
      * './T_ConveyorsBelt_A01_Decal_ORM.png'
    * Inputs:
      * 'opacity_texture' [asset] = './T_ConveyorsBelt_A01_Decal_Alpha.png'
      * 'diffuse_texture' [asset] = './T_ConveyorsBelt_A01_Decal_Albedo.png'
      * 'reflection_roughness_texture_influence' [float] = '1'
      * 'metallic_texture_influence' [float] = '1'
      * 'ORM_texture' [asset] = './T_ConveyorsBelt_A01_Decal_ORM.png'

---

### /World/Conveyor_21/Looks/Metal_Rough_A

* **Prim路径 (Prim Path):**/World/Conveyor_21/Looks/Metal_Rough_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_21/Looks/Metal_Rough_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_21/Looks/Metal_Rough_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Metal/Misc/Metal_Rough_A.mdl' (Sub Id: 'Metal_Rough_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Metal/Misc/Metal_Rough_A.mdl'

---

### /World/Conveyor_21/Looks/MetalPainted_Black_Glossy_A

* **Prim路径 (Prim Path):**/World/Conveyor_21/Looks/MetalPainted_Black_Glossy_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_21/Looks/MetalPainted_Black_Glossy_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_21/Looks/MetalPainted_Black_Glossy_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Metal/Painted/MetalPainted_White_Glossy_A.mdl' (Sub Id: 'MetalPainted_White_Glossy_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Metal/Painted/MetalPainted_White_Glossy_A.mdl'
    * Inputs:
      * 'bump_factor' [float] = '0.5'
      * 'texture_scale' [float2] = '(1.500, 1.500)'
      * 'diffuse_tint' [color3f] = '(0.066, 0.066, 0.066)'
      * 'reflection_roughness_constant' [float] = '0.63'
      * 'reflection_roughness_texture_influence' [float] = '0.91'

---

### /World/Conveyor_21/Looks/MetalPainted_Blue_Glossy_A

* **Prim路径 (Prim Path):**/World/Conveyor_21/Looks/MetalPainted_Blue_Glossy_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_21/Looks/MetalPainted_Blue_Glossy_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_21/Looks/MetalPainted_Blue_Glossy_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Metal/Painted/MetalPainted_White_Glossy_A.mdl' (Sub Id: 'MetalPainted_White_Glossy_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Metal/Painted/MetalPainted_White_Glossy_A.mdl'
    * 纹理引用 (Texture Assets):
      * '../Material Library/Metal/Painted/T_MetalPainted_White_Glossy_A_Albedo.png'
      * '../Material Library/Metal/Painted/T_MetalPainted_White_Glossy_A_Normal.png'
      * '../Material Library/Metal/Painted/T_MetalPainted_White_Glossy_A_ORM.png'
    * Inputs:
      * 'bump_factor' [float] = '0.5'
      * 'normalmap_texture' [asset] = '../Material Library/Metal/Painted/T_MetalPainted_White_Glossy_A_Normal.png'
      * 'texture_scale' [float2] = '(1.500, 1.500)'
      * 'diffuse_texture' [asset] = '../Material Library/Metal/Painted/T_MetalPainted_White_Glossy_A_Albedo.png'
      * 'diffuse_tint' [color3f] = '(0.077, 0.203, 0.587)'
      * 'ORM_texture' [asset] = '../Material Library/Metal/Painted/T_MetalPainted_White_Glossy_A_ORM.png'

---

### /World/Conveyor_21/Looks/Plastic_Orange_A

* **Prim路径 (Prim Path):**/World/Conveyor_21/Looks/Plastic_Orange_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_21/Looks/Plastic_Orange_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_21/Looks/Plastic_Orange_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Plastic/Misc/Plastic_Orange_A.mdl' (Sub Id: 'Plastic_Orange_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Plastic/Misc/Plastic_Orange_A.mdl'

---

### /World/Conveyor_21/Looks/Plastic_Red_A

* **Prim路径 (Prim Path):**/World/Conveyor_21/Looks/Plastic_Red_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_21/Looks/Plastic_Red_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_21/Looks/Plastic_Red_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Plastic/Misc/Plastic_Red_A.mdl' (Sub Id: 'Plastic_Red_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Plastic/Misc/Plastic_Red_A.mdl'

---

### /World/Conveyor_21/Looks/Plastic_Rough_Black_A

* **Prim路径 (Prim Path):**/World/Conveyor_21/Looks/Plastic_Rough_Black_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_21/Looks/Plastic_Rough_Black_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_21/Looks/Plastic_Rough_Black_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Plastic/Misc/Plastic_Rough_Black_A.mdl' (Sub Id: 'Plastic_Rough_Black_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Plastic/Misc/Plastic_Rough_Black_A.mdl'

---

### /World/Conveyor_21/Looks/Steel_A

* **Prim路径 (Prim Path):**/World/Conveyor_21/Looks/Steel_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_21/Looks/Steel_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_21/Looks/Steel_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Metal/Steel/Steel_A.mdl' (Sub Id: 'Steel_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Metal/Steel/Steel_A.mdl'
    * Inputs:
      * 'diffuse_tint' [color3f] = '(0.772, 0.772, 0.772)'
      * 'reflection_roughness_constant' [float] = '0.67'
      * 'reflection_roughness_texture_influence' [float] = '0.88'

---

### /World/Conveyor_22/Looks/Acrylic_Clear_Glossy_A

* **Prim路径 (Prim Path):**/World/Conveyor_22/Looks/Acrylic_Clear_Glossy_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_22/Looks/Acrylic_Clear_Glossy_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_22/Looks/Acrylic_Clear_Glossy_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniGlass.mdl' (Sub Id: 'OmniGlass')
    * 纹理引用 (Texture Assets):
      * '../Material Library/Plastic/Textures/T_Acrylic_Clear_Glossy_A_Rough.png'
      * '../Material Library/Plastic/Textures/T_Plastic_Rough_Black_A_Normal.png'
    * Inputs:
      * 'normal_map_strength' [float] = '0.5'
      * 'texture_scale' [float2] = '(1.000, 3.000)'
      * 'normal_map_texture' [asset] = '../Material Library/Plastic/Textures/T_Plastic_Rough_Black_A_Normal.png'
      * 'roughness_texture' [asset] = '../Material Library/Plastic/Textures/T_Acrylic_Clear_Glossy_A_Rough.png'
      * 'roughness_texture_influence' [float] = '0.3'
      * 'glass_ior' [float] = '1.05'
      * 'frosting_roughness' [float] = '0.17'
      * 'glass_color' [color3f] = '(0.734, 0.734, 0.734)'

---

### /World/Conveyor_22/Looks/M_ConveyorBelt_A01_Belt

* **Prim路径 (Prim Path):**/World/Conveyor_22/Looks/M_ConveyorBelt_A01_Belt
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_22/Looks/M_ConveyorBelt_A01_Belt/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_22/Looks/M_ConveyorBelt_A01_Belt/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * 纹理引用 (Texture Assets):
      * './T_ConveyorBelt_A01_Belt_Albedo.png'
      * './T_ConveyorBelt_A01_Belt_Normal.png'
      * './T_ConveyorBelt_A01_Belt_ORM.png'
    * Inputs:
      * 'normalmap_texture' [asset] = './T_ConveyorBelt_A01_Belt_Normal.png'
      * 'diffuse_texture' [asset] = './T_ConveyorBelt_A01_Belt_Albedo.png'
      * 'reflection_roughness_texture_influence' [float] = '1'
      * 'metallic_texture_influence' [float] = '1'
      * 'ORM_texture' [asset] = './T_ConveyorBelt_A01_Belt_ORM.png'

---

### /World/Conveyor_22/Looks/M_ConveyorBelt_A01_Decal

* **Prim路径 (Prim Path):**/World/Conveyor_22/Looks/M_ConveyorBelt_A01_Decal
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_22/Looks/M_ConveyorBelt_A01_Decal/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_22/Looks/M_ConveyorBelt_A01_Decal/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * 纹理引用 (Texture Assets):
      * './T_ConveyorsBelt_A01_Decal_Albedo.png'
      * './T_ConveyorsBelt_A01_Decal_Alpha.png'
      * './T_ConveyorsBelt_A01_Decal_ORM.png'
    * Inputs:
      * 'opacity_texture' [asset] = './T_ConveyorsBelt_A01_Decal_Alpha.png'
      * 'diffuse_texture' [asset] = './T_ConveyorsBelt_A01_Decal_Albedo.png'
      * 'reflection_roughness_texture_influence' [float] = '1'
      * 'metallic_texture_influence' [float] = '1'
      * 'ORM_texture' [asset] = './T_ConveyorsBelt_A01_Decal_ORM.png'

---

### /World/Conveyor_22/Looks/Metal_Rough_A

* **Prim路径 (Prim Path):**/World/Conveyor_22/Looks/Metal_Rough_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_22/Looks/Metal_Rough_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_22/Looks/Metal_Rough_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Metal/Misc/Metal_Rough_A.mdl' (Sub Id: 'Metal_Rough_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Metal/Misc/Metal_Rough_A.mdl'

---

### /World/Conveyor_22/Looks/MetalPainted_Black_Glossy_A

* **Prim路径 (Prim Path):**/World/Conveyor_22/Looks/MetalPainted_Black_Glossy_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_22/Looks/MetalPainted_Black_Glossy_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_22/Looks/MetalPainted_Black_Glossy_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Metal/Painted/MetalPainted_White_Glossy_A.mdl' (Sub Id: 'MetalPainted_White_Glossy_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Metal/Painted/MetalPainted_White_Glossy_A.mdl'
    * Inputs:
      * 'bump_factor' [float] = '0.5'
      * 'texture_scale' [float2] = '(1.500, 1.500)'
      * 'diffuse_tint' [color3f] = '(0.066, 0.066, 0.066)'
      * 'reflection_roughness_constant' [float] = '0.63'
      * 'reflection_roughness_texture_influence' [float] = '0.91'

---

### /World/Conveyor_22/Looks/MetalPainted_Blue_Glossy_A

* **Prim路径 (Prim Path):**/World/Conveyor_22/Looks/MetalPainted_Blue_Glossy_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_22/Looks/MetalPainted_Blue_Glossy_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_22/Looks/MetalPainted_Blue_Glossy_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Metal/Painted/MetalPainted_White_Glossy_A.mdl' (Sub Id: 'MetalPainted_White_Glossy_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Metal/Painted/MetalPainted_White_Glossy_A.mdl'
    * 纹理引用 (Texture Assets):
      * '../Material Library/Metal/Painted/T_MetalPainted_White_Glossy_A_Albedo.png'
      * '../Material Library/Metal/Painted/T_MetalPainted_White_Glossy_A_Normal.png'
      * '../Material Library/Metal/Painted/T_MetalPainted_White_Glossy_A_ORM.png'
    * Inputs:
      * 'bump_factor' [float] = '0.5'
      * 'normalmap_texture' [asset] = '../Material Library/Metal/Painted/T_MetalPainted_White_Glossy_A_Normal.png'
      * 'texture_scale' [float2] = '(1.500, 1.500)'
      * 'diffuse_texture' [asset] = '../Material Library/Metal/Painted/T_MetalPainted_White_Glossy_A_Albedo.png'
      * 'diffuse_tint' [color3f] = '(0.077, 0.203, 0.587)'
      * 'ORM_texture' [asset] = '../Material Library/Metal/Painted/T_MetalPainted_White_Glossy_A_ORM.png'

---

### /World/Conveyor_22/Looks/Plastic_Orange_A

* **Prim路径 (Prim Path):**/World/Conveyor_22/Looks/Plastic_Orange_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_22/Looks/Plastic_Orange_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_22/Looks/Plastic_Orange_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Plastic/Misc/Plastic_Orange_A.mdl' (Sub Id: 'Plastic_Orange_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Plastic/Misc/Plastic_Orange_A.mdl'

---

### /World/Conveyor_22/Looks/Plastic_Red_A

* **Prim路径 (Prim Path):**/World/Conveyor_22/Looks/Plastic_Red_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_22/Looks/Plastic_Red_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_22/Looks/Plastic_Red_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Plastic/Misc/Plastic_Red_A.mdl' (Sub Id: 'Plastic_Red_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Plastic/Misc/Plastic_Red_A.mdl'

---

### /World/Conveyor_22/Looks/Plastic_Rough_Black_A

* **Prim路径 (Prim Path):**/World/Conveyor_22/Looks/Plastic_Rough_Black_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_22/Looks/Plastic_Rough_Black_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_22/Looks/Plastic_Rough_Black_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Plastic/Misc/Plastic_Rough_Black_A.mdl' (Sub Id: 'Plastic_Rough_Black_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Plastic/Misc/Plastic_Rough_Black_A.mdl'

---

### /World/Conveyor_22/Looks/Steel_A

* **Prim路径 (Prim Path):**/World/Conveyor_22/Looks/Steel_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_22/Looks/Steel_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_22/Looks/Steel_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Metal/Steel/Steel_A.mdl' (Sub Id: 'Steel_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Metal/Steel/Steel_A.mdl'
    * Inputs:
      * 'diffuse_tint' [color3f] = '(0.772, 0.772, 0.772)'
      * 'reflection_roughness_constant' [float] = '0.67'
      * 'reflection_roughness_texture_influence' [float] = '0.88'

---

### /World/Conveyor_23/Looks/Acrylic_Clear_Glossy_A

* **Prim路径 (Prim Path):**/World/Conveyor_23/Looks/Acrylic_Clear_Glossy_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_23/Looks/Acrylic_Clear_Glossy_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_23/Looks/Acrylic_Clear_Glossy_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniGlass.mdl' (Sub Id: 'OmniGlass')
    * 纹理引用 (Texture Assets):
      * '../Material Library/Plastic/Textures/T_Acrylic_Clear_Glossy_A_Rough.png'
      * '../Material Library/Plastic/Textures/T_Plastic_Rough_Black_A_Normal.png'
    * Inputs:
      * 'normal_map_strength' [float] = '0.5'
      * 'texture_scale' [float2] = '(1.000, 3.000)'
      * 'normal_map_texture' [asset] = '../Material Library/Plastic/Textures/T_Plastic_Rough_Black_A_Normal.png'
      * 'roughness_texture' [asset] = '../Material Library/Plastic/Textures/T_Acrylic_Clear_Glossy_A_Rough.png'
      * 'roughness_texture_influence' [float] = '0.3'
      * 'glass_ior' [float] = '1.05'
      * 'frosting_roughness' [float] = '0.17'
      * 'glass_color' [color3f] = '(0.734, 0.734, 0.734)'

---

### /World/Conveyor_23/Looks/M_ConveyorBelt_A01_Belt

* **Prim路径 (Prim Path):**/World/Conveyor_23/Looks/M_ConveyorBelt_A01_Belt
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_23/Looks/M_ConveyorBelt_A01_Belt/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_23/Looks/M_ConveyorBelt_A01_Belt/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * 纹理引用 (Texture Assets):
      * './T_ConveyorBelt_A01_Belt_Albedo.png'
      * './T_ConveyorBelt_A01_Belt_Normal.png'
      * './T_ConveyorBelt_A01_Belt_ORM.png'
    * Inputs:
      * 'normalmap_texture' [asset] = './T_ConveyorBelt_A01_Belt_Normal.png'
      * 'diffuse_texture' [asset] = './T_ConveyorBelt_A01_Belt_Albedo.png'
      * 'reflection_roughness_texture_influence' [float] = '1'
      * 'metallic_texture_influence' [float] = '1'
      * 'ORM_texture' [asset] = './T_ConveyorBelt_A01_Belt_ORM.png'

---

### /World/Conveyor_23/Looks/M_ConveyorBelt_A01_Decal

* **Prim路径 (Prim Path):**/World/Conveyor_23/Looks/M_ConveyorBelt_A01_Decal
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_23/Looks/M_ConveyorBelt_A01_Decal/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_23/Looks/M_ConveyorBelt_A01_Decal/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * 纹理引用 (Texture Assets):
      * './T_ConveyorsBelt_A01_Decal_Albedo.png'
      * './T_ConveyorsBelt_A01_Decal_Alpha.png'
      * './T_ConveyorsBelt_A01_Decal_ORM.png'
    * Inputs:
      * 'opacity_texture' [asset] = './T_ConveyorsBelt_A01_Decal_Alpha.png'
      * 'diffuse_texture' [asset] = './T_ConveyorsBelt_A01_Decal_Albedo.png'
      * 'reflection_roughness_texture_influence' [float] = '1'
      * 'metallic_texture_influence' [float] = '1'
      * 'ORM_texture' [asset] = './T_ConveyorsBelt_A01_Decal_ORM.png'

---

### /World/Conveyor_23/Looks/Metal_Rough_A

* **Prim路径 (Prim Path):**/World/Conveyor_23/Looks/Metal_Rough_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_23/Looks/Metal_Rough_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_23/Looks/Metal_Rough_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Metal/Misc/Metal_Rough_A.mdl' (Sub Id: 'Metal_Rough_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Metal/Misc/Metal_Rough_A.mdl'

---

### /World/Conveyor_23/Looks/MetalPainted_Black_Glossy_A

* **Prim路径 (Prim Path):**/World/Conveyor_23/Looks/MetalPainted_Black_Glossy_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_23/Looks/MetalPainted_Black_Glossy_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_23/Looks/MetalPainted_Black_Glossy_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Metal/Painted/MetalPainted_White_Glossy_A.mdl' (Sub Id: 'MetalPainted_White_Glossy_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Metal/Painted/MetalPainted_White_Glossy_A.mdl'
    * Inputs:
      * 'bump_factor' [float] = '0.5'
      * 'texture_scale' [float2] = '(1.500, 1.500)'
      * 'diffuse_tint' [color3f] = '(0.066, 0.066, 0.066)'
      * 'reflection_roughness_constant' [float] = '0.63'
      * 'reflection_roughness_texture_influence' [float] = '0.91'

---

### /World/Conveyor_23/Looks/MetalPainted_Blue_Glossy_A

* **Prim路径 (Prim Path):**/World/Conveyor_23/Looks/MetalPainted_Blue_Glossy_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_23/Looks/MetalPainted_Blue_Glossy_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_23/Looks/MetalPainted_Blue_Glossy_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Metal/Painted/MetalPainted_White_Glossy_A.mdl' (Sub Id: 'MetalPainted_White_Glossy_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Metal/Painted/MetalPainted_White_Glossy_A.mdl'
    * 纹理引用 (Texture Assets):
      * '../Material Library/Metal/Painted/T_MetalPainted_White_Glossy_A_Albedo.png'
      * '../Material Library/Metal/Painted/T_MetalPainted_White_Glossy_A_Normal.png'
      * '../Material Library/Metal/Painted/T_MetalPainted_White_Glossy_A_ORM.png'
    * Inputs:
      * 'bump_factor' [float] = '0.5'
      * 'normalmap_texture' [asset] = '../Material Library/Metal/Painted/T_MetalPainted_White_Glossy_A_Normal.png'
      * 'texture_scale' [float2] = '(1.500, 1.500)'
      * 'diffuse_texture' [asset] = '../Material Library/Metal/Painted/T_MetalPainted_White_Glossy_A_Albedo.png'
      * 'diffuse_tint' [color3f] = '(0.077, 0.203, 0.587)'
      * 'ORM_texture' [asset] = '../Material Library/Metal/Painted/T_MetalPainted_White_Glossy_A_ORM.png'

---

### /World/Conveyor_23/Looks/Plastic_Orange_A

* **Prim路径 (Prim Path):**/World/Conveyor_23/Looks/Plastic_Orange_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_23/Looks/Plastic_Orange_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_23/Looks/Plastic_Orange_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Plastic/Misc/Plastic_Orange_A.mdl' (Sub Id: 'Plastic_Orange_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Plastic/Misc/Plastic_Orange_A.mdl'

---

### /World/Conveyor_23/Looks/Plastic_Red_A

* **Prim路径 (Prim Path):**/World/Conveyor_23/Looks/Plastic_Red_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_23/Looks/Plastic_Red_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_23/Looks/Plastic_Red_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Plastic/Misc/Plastic_Red_A.mdl' (Sub Id: 'Plastic_Red_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Plastic/Misc/Plastic_Red_A.mdl'

---

### /World/Conveyor_23/Looks/Plastic_Rough_Black_A

* **Prim路径 (Prim Path):**/World/Conveyor_23/Looks/Plastic_Rough_Black_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_23/Looks/Plastic_Rough_Black_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_23/Looks/Plastic_Rough_Black_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Plastic/Misc/Plastic_Rough_Black_A.mdl' (Sub Id: 'Plastic_Rough_Black_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Plastic/Misc/Plastic_Rough_Black_A.mdl'

---

### /World/Conveyor_23/Looks/Steel_A

* **Prim路径 (Prim Path):**/World/Conveyor_23/Looks/Steel_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_23/Looks/Steel_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_23/Looks/Steel_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Metal/Steel/Steel_A.mdl' (Sub Id: 'Steel_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Metal/Steel/Steel_A.mdl'
    * Inputs:
      * 'diffuse_tint' [color3f] = '(0.772, 0.772, 0.772)'
      * 'reflection_roughness_constant' [float] = '0.67'
      * 'reflection_roughness_texture_influence' [float] = '0.88'

---

### /World/Conveyor_24/Looks/Acrylic_Clear_Glossy_A

* **Prim路径 (Prim Path):**/World/Conveyor_24/Looks/Acrylic_Clear_Glossy_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_24/Looks/Acrylic_Clear_Glossy_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_24/Looks/Acrylic_Clear_Glossy_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniGlass.mdl' (Sub Id: 'OmniGlass')
    * 纹理引用 (Texture Assets):
      * '../Material Library/Plastic/Textures/T_Acrylic_Clear_Glossy_A_Rough.png'
      * '../Material Library/Plastic/Textures/T_Plastic_Rough_Black_A_Normal.png'
    * Inputs:
      * 'normal_map_strength' [float] = '0.5'
      * 'texture_scale' [float2] = '(1.000, 3.000)'
      * 'normal_map_texture' [asset] = '../Material Library/Plastic/Textures/T_Plastic_Rough_Black_A_Normal.png'
      * 'roughness_texture' [asset] = '../Material Library/Plastic/Textures/T_Acrylic_Clear_Glossy_A_Rough.png'
      * 'roughness_texture_influence' [float] = '0.3'
      * 'glass_ior' [float] = '1.05'
      * 'frosting_roughness' [float] = '0.17'
      * 'glass_color' [color3f] = '(0.734, 0.734, 0.734)'

---

### /World/Conveyor_24/Looks/M_ConveyorBelt_A01_Belt

* **Prim路径 (Prim Path):**/World/Conveyor_24/Looks/M_ConveyorBelt_A01_Belt
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_24/Looks/M_ConveyorBelt_A01_Belt/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_24/Looks/M_ConveyorBelt_A01_Belt/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * 纹理引用 (Texture Assets):
      * './T_ConveyorBelt_A01_Belt_Albedo.png'
      * './T_ConveyorBelt_A01_Belt_Normal.png'
      * './T_ConveyorBelt_A01_Belt_ORM.png'
    * Inputs:
      * 'normalmap_texture' [asset] = './T_ConveyorBelt_A01_Belt_Normal.png'
      * 'diffuse_texture' [asset] = './T_ConveyorBelt_A01_Belt_Albedo.png'
      * 'reflection_roughness_texture_influence' [float] = '1'
      * 'metallic_texture_influence' [float] = '1'
      * 'ORM_texture' [asset] = './T_ConveyorBelt_A01_Belt_ORM.png'

---

### /World/Conveyor_24/Looks/M_ConveyorBelt_A01_Decal

* **Prim路径 (Prim Path):**/World/Conveyor_24/Looks/M_ConveyorBelt_A01_Decal
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_24/Looks/M_ConveyorBelt_A01_Decal/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_24/Looks/M_ConveyorBelt_A01_Decal/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * 纹理引用 (Texture Assets):
      * './T_ConveyorsBelt_A01_Decal_Albedo.png'
      * './T_ConveyorsBelt_A01_Decal_Alpha.png'
      * './T_ConveyorsBelt_A01_Decal_ORM.png'
    * Inputs:
      * 'opacity_texture' [asset] = './T_ConveyorsBelt_A01_Decal_Alpha.png'
      * 'diffuse_texture' [asset] = './T_ConveyorsBelt_A01_Decal_Albedo.png'
      * 'reflection_roughness_texture_influence' [float] = '1'
      * 'metallic_texture_influence' [float] = '1'
      * 'ORM_texture' [asset] = './T_ConveyorsBelt_A01_Decal_ORM.png'

---

### /World/Conveyor_24/Looks/Metal_Rough_A

* **Prim路径 (Prim Path):**/World/Conveyor_24/Looks/Metal_Rough_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_24/Looks/Metal_Rough_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_24/Looks/Metal_Rough_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Metal/Misc/Metal_Rough_A.mdl' (Sub Id: 'Metal_Rough_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Metal/Misc/Metal_Rough_A.mdl'

---

### /World/Conveyor_24/Looks/MetalPainted_Black_Glossy_A

* **Prim路径 (Prim Path):**/World/Conveyor_24/Looks/MetalPainted_Black_Glossy_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_24/Looks/MetalPainted_Black_Glossy_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_24/Looks/MetalPainted_Black_Glossy_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Metal/Painted/MetalPainted_White_Glossy_A.mdl' (Sub Id: 'MetalPainted_White_Glossy_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Metal/Painted/MetalPainted_White_Glossy_A.mdl'
    * Inputs:
      * 'bump_factor' [float] = '0.5'
      * 'texture_scale' [float2] = '(1.500, 1.500)'
      * 'diffuse_tint' [color3f] = '(0.066, 0.066, 0.066)'
      * 'reflection_roughness_constant' [float] = '0.63'
      * 'reflection_roughness_texture_influence' [float] = '0.91'

---

### /World/Conveyor_24/Looks/MetalPainted_Blue_Glossy_A

* **Prim路径 (Prim Path):**/World/Conveyor_24/Looks/MetalPainted_Blue_Glossy_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_24/Looks/MetalPainted_Blue_Glossy_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_24/Looks/MetalPainted_Blue_Glossy_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Metal/Painted/MetalPainted_White_Glossy_A.mdl' (Sub Id: 'MetalPainted_White_Glossy_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Metal/Painted/MetalPainted_White_Glossy_A.mdl'
    * 纹理引用 (Texture Assets):
      * '../Material Library/Metal/Painted/T_MetalPainted_White_Glossy_A_Albedo.png'
      * '../Material Library/Metal/Painted/T_MetalPainted_White_Glossy_A_Normal.png'
      * '../Material Library/Metal/Painted/T_MetalPainted_White_Glossy_A_ORM.png'
    * Inputs:
      * 'bump_factor' [float] = '0.5'
      * 'normalmap_texture' [asset] = '../Material Library/Metal/Painted/T_MetalPainted_White_Glossy_A_Normal.png'
      * 'texture_scale' [float2] = '(1.500, 1.500)'
      * 'diffuse_texture' [asset] = '../Material Library/Metal/Painted/T_MetalPainted_White_Glossy_A_Albedo.png'
      * 'diffuse_tint' [color3f] = '(0.077, 0.203, 0.587)'
      * 'ORM_texture' [asset] = '../Material Library/Metal/Painted/T_MetalPainted_White_Glossy_A_ORM.png'

---

### /World/Conveyor_24/Looks/Plastic_Orange_A

* **Prim路径 (Prim Path):**/World/Conveyor_24/Looks/Plastic_Orange_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_24/Looks/Plastic_Orange_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_24/Looks/Plastic_Orange_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Plastic/Misc/Plastic_Orange_A.mdl' (Sub Id: 'Plastic_Orange_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Plastic/Misc/Plastic_Orange_A.mdl'

---

### /World/Conveyor_24/Looks/Plastic_Red_A

* **Prim路径 (Prim Path):**/World/Conveyor_24/Looks/Plastic_Red_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_24/Looks/Plastic_Red_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_24/Looks/Plastic_Red_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Plastic/Misc/Plastic_Red_A.mdl' (Sub Id: 'Plastic_Red_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Plastic/Misc/Plastic_Red_A.mdl'

---

### /World/Conveyor_24/Looks/Plastic_Rough_Black_A

* **Prim路径 (Prim Path):**/World/Conveyor_24/Looks/Plastic_Rough_Black_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_24/Looks/Plastic_Rough_Black_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_24/Looks/Plastic_Rough_Black_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Plastic/Misc/Plastic_Rough_Black_A.mdl' (Sub Id: 'Plastic_Rough_Black_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Plastic/Misc/Plastic_Rough_Black_A.mdl'

---

### /World/Conveyor_24/Looks/Steel_A

* **Prim路径 (Prim Path):**/World/Conveyor_24/Looks/Steel_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_24/Looks/Steel_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_24/Looks/Steel_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Metal/Steel/Steel_A.mdl' (Sub Id: 'Steel_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Metal/Steel/Steel_A.mdl'
    * Inputs:
      * 'diffuse_tint' [color3f] = '(0.772, 0.772, 0.772)'
      * 'reflection_roughness_constant' [float] = '0.67'
      * 'reflection_roughness_texture_influence' [float] = '0.88'

---

### /World/Conveyor_25/Looks/Acrylic_Clear_Glossy_A

* **Prim路径 (Prim Path):**/World/Conveyor_25/Looks/Acrylic_Clear_Glossy_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_25/Looks/Acrylic_Clear_Glossy_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_25/Looks/Acrylic_Clear_Glossy_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniGlass.mdl' (Sub Id: 'OmniGlass')
    * 纹理引用 (Texture Assets):
      * '../Material Library/Plastic/Textures/T_Acrylic_Clear_Glossy_A_Rough.png'
      * '../Material Library/Plastic/Textures/T_Plastic_Rough_Black_A_Normal.png'
    * Inputs:
      * 'normal_map_strength' [float] = '0.5'
      * 'texture_scale' [float2] = '(1.000, 3.000)'
      * 'normal_map_texture' [asset] = '../Material Library/Plastic/Textures/T_Plastic_Rough_Black_A_Normal.png'
      * 'roughness_texture' [asset] = '../Material Library/Plastic/Textures/T_Acrylic_Clear_Glossy_A_Rough.png'
      * 'roughness_texture_influence' [float] = '0.3'
      * 'glass_ior' [float] = '1.05'
      * 'frosting_roughness' [float] = '0.17'
      * 'glass_color' [color3f] = '(0.734, 0.734, 0.734)'

---

### /World/Conveyor_25/Looks/M_ConveyorBelt_A01_Belt

* **Prim路径 (Prim Path):**/World/Conveyor_25/Looks/M_ConveyorBelt_A01_Belt
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_25/Looks/M_ConveyorBelt_A01_Belt/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_25/Looks/M_ConveyorBelt_A01_Belt/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * 纹理引用 (Texture Assets):
      * './T_ConveyorBelt_A01_Belt_Albedo.png'
      * './T_ConveyorBelt_A01_Belt_Normal.png'
      * './T_ConveyorBelt_A01_Belt_ORM.png'
    * Inputs:
      * 'normalmap_texture' [asset] = './T_ConveyorBelt_A01_Belt_Normal.png'
      * 'diffuse_texture' [asset] = './T_ConveyorBelt_A01_Belt_Albedo.png'
      * 'reflection_roughness_texture_influence' [float] = '1'
      * 'metallic_texture_influence' [float] = '1'
      * 'ORM_texture' [asset] = './T_ConveyorBelt_A01_Belt_ORM.png'

---

### /World/Conveyor_25/Looks/M_ConveyorBelt_A01_Decal

* **Prim路径 (Prim Path):**/World/Conveyor_25/Looks/M_ConveyorBelt_A01_Decal
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_25/Looks/M_ConveyorBelt_A01_Decal/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_25/Looks/M_ConveyorBelt_A01_Decal/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * 纹理引用 (Texture Assets):
      * './T_ConveyorsBelt_A01_Decal_Albedo.png'
      * './T_ConveyorsBelt_A01_Decal_Alpha.png'
      * './T_ConveyorsBelt_A01_Decal_ORM.png'
    * Inputs:
      * 'opacity_texture' [asset] = './T_ConveyorsBelt_A01_Decal_Alpha.png'
      * 'diffuse_texture' [asset] = './T_ConveyorsBelt_A01_Decal_Albedo.png'
      * 'reflection_roughness_texture_influence' [float] = '1'
      * 'metallic_texture_influence' [float] = '1'
      * 'ORM_texture' [asset] = './T_ConveyorsBelt_A01_Decal_ORM.png'

---

### /World/Conveyor_25/Looks/Metal_Rough_A

* **Prim路径 (Prim Path):**/World/Conveyor_25/Looks/Metal_Rough_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_25/Looks/Metal_Rough_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_25/Looks/Metal_Rough_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Metal/Misc/Metal_Rough_A.mdl' (Sub Id: 'Metal_Rough_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Metal/Misc/Metal_Rough_A.mdl'

---

### /World/Conveyor_25/Looks/MetalPainted_Black_Glossy_A

* **Prim路径 (Prim Path):**/World/Conveyor_25/Looks/MetalPainted_Black_Glossy_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_25/Looks/MetalPainted_Black_Glossy_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_25/Looks/MetalPainted_Black_Glossy_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Metal/Painted/MetalPainted_White_Glossy_A.mdl' (Sub Id: 'MetalPainted_White_Glossy_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Metal/Painted/MetalPainted_White_Glossy_A.mdl'
    * Inputs:
      * 'bump_factor' [float] = '0.5'
      * 'texture_scale' [float2] = '(1.500, 1.500)'
      * 'diffuse_tint' [color3f] = '(0.066, 0.066, 0.066)'
      * 'reflection_roughness_constant' [float] = '0.63'
      * 'reflection_roughness_texture_influence' [float] = '0.91'

---

### /World/Conveyor_25/Looks/MetalPainted_Blue_Glossy_A

* **Prim路径 (Prim Path):**/World/Conveyor_25/Looks/MetalPainted_Blue_Glossy_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_25/Looks/MetalPainted_Blue_Glossy_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_25/Looks/MetalPainted_Blue_Glossy_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Metal/Painted/MetalPainted_White_Glossy_A.mdl' (Sub Id: 'MetalPainted_White_Glossy_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Metal/Painted/MetalPainted_White_Glossy_A.mdl'
    * 纹理引用 (Texture Assets):
      * '../Material Library/Metal/Painted/T_MetalPainted_White_Glossy_A_Albedo.png'
      * '../Material Library/Metal/Painted/T_MetalPainted_White_Glossy_A_Normal.png'
      * '../Material Library/Metal/Painted/T_MetalPainted_White_Glossy_A_ORM.png'
    * Inputs:
      * 'bump_factor' [float] = '0.5'
      * 'normalmap_texture' [asset] = '../Material Library/Metal/Painted/T_MetalPainted_White_Glossy_A_Normal.png'
      * 'texture_scale' [float2] = '(1.500, 1.500)'
      * 'diffuse_texture' [asset] = '../Material Library/Metal/Painted/T_MetalPainted_White_Glossy_A_Albedo.png'
      * 'diffuse_tint' [color3f] = '(0.077, 0.203, 0.587)'
      * 'ORM_texture' [asset] = '../Material Library/Metal/Painted/T_MetalPainted_White_Glossy_A_ORM.png'

---

### /World/Conveyor_25/Looks/Plastic_Orange_A

* **Prim路径 (Prim Path):**/World/Conveyor_25/Looks/Plastic_Orange_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_25/Looks/Plastic_Orange_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_25/Looks/Plastic_Orange_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Plastic/Misc/Plastic_Orange_A.mdl' (Sub Id: 'Plastic_Orange_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Plastic/Misc/Plastic_Orange_A.mdl'

---

### /World/Conveyor_25/Looks/Plastic_Red_A

* **Prim路径 (Prim Path):**/World/Conveyor_25/Looks/Plastic_Red_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_25/Looks/Plastic_Red_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_25/Looks/Plastic_Red_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Plastic/Misc/Plastic_Red_A.mdl' (Sub Id: 'Plastic_Red_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Plastic/Misc/Plastic_Red_A.mdl'

---

### /World/Conveyor_25/Looks/Plastic_Rough_Black_A

* **Prim路径 (Prim Path):**/World/Conveyor_25/Looks/Plastic_Rough_Black_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_25/Looks/Plastic_Rough_Black_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_25/Looks/Plastic_Rough_Black_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Plastic/Misc/Plastic_Rough_Black_A.mdl' (Sub Id: 'Plastic_Rough_Black_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Plastic/Misc/Plastic_Rough_Black_A.mdl'

---

### /World/Conveyor_25/Looks/Steel_A

* **Prim路径 (Prim Path):**/World/Conveyor_25/Looks/Steel_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_25/Looks/Steel_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_25/Looks/Steel_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Metal/Steel/Steel_A.mdl' (Sub Id: 'Steel_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Metal/Steel/Steel_A.mdl'
    * Inputs:
      * 'diffuse_tint' [color3f] = '(0.772, 0.772, 0.772)'
      * 'reflection_roughness_constant' [float] = '0.67'
      * 'reflection_roughness_texture_influence' [float] = '0.88'

---

### /World/Conveyor_26/Looks/Acrylic_Clear_Glossy_A

* **Prim路径 (Prim Path):**/World/Conveyor_26/Looks/Acrylic_Clear_Glossy_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_26/Looks/Acrylic_Clear_Glossy_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_26/Looks/Acrylic_Clear_Glossy_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniGlass.mdl' (Sub Id: 'OmniGlass')
    * 纹理引用 (Texture Assets):
      * '../Material Library/Plastic/Textures/T_Acrylic_Clear_Glossy_A_Rough.png'
      * '../Material Library/Plastic/Textures/T_Plastic_Rough_Black_A_Normal.png'
    * Inputs:
      * 'normal_map_strength' [float] = '0.5'
      * 'texture_scale' [float2] = '(1.000, 3.000)'
      * 'normal_map_texture' [asset] = '../Material Library/Plastic/Textures/T_Plastic_Rough_Black_A_Normal.png'
      * 'roughness_texture' [asset] = '../Material Library/Plastic/Textures/T_Acrylic_Clear_Glossy_A_Rough.png'
      * 'roughness_texture_influence' [float] = '0.3'
      * 'glass_ior' [float] = '1.05'
      * 'frosting_roughness' [float] = '0.17'
      * 'glass_color' [color3f] = '(0.734, 0.734, 0.734)'

---

### /World/Conveyor_26/Looks/M_ConveyorBelt_A01_Belt

* **Prim路径 (Prim Path):**/World/Conveyor_26/Looks/M_ConveyorBelt_A01_Belt
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_26/Looks/M_ConveyorBelt_A01_Belt/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_26/Looks/M_ConveyorBelt_A01_Belt/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * 纹理引用 (Texture Assets):
      * './T_ConveyorBelt_A01_Belt_Albedo.png'
      * './T_ConveyorBelt_A01_Belt_Normal.png'
      * './T_ConveyorBelt_A01_Belt_ORM.png'
    * Inputs:
      * 'normalmap_texture' [asset] = './T_ConveyorBelt_A01_Belt_Normal.png'
      * 'diffuse_texture' [asset] = './T_ConveyorBelt_A01_Belt_Albedo.png'
      * 'reflection_roughness_texture_influence' [float] = '1'
      * 'metallic_texture_influence' [float] = '1'
      * 'ORM_texture' [asset] = './T_ConveyorBelt_A01_Belt_ORM.png'

---

### /World/Conveyor_26/Looks/M_ConveyorBelt_A01_Decal

* **Prim路径 (Prim Path):**/World/Conveyor_26/Looks/M_ConveyorBelt_A01_Decal
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_26/Looks/M_ConveyorBelt_A01_Decal/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_26/Looks/M_ConveyorBelt_A01_Decal/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * 纹理引用 (Texture Assets):
      * './T_ConveyorsBelt_A01_Decal_Albedo.png'
      * './T_ConveyorsBelt_A01_Decal_Alpha.png'
      * './T_ConveyorsBelt_A01_Decal_ORM.png'
    * Inputs:
      * 'opacity_texture' [asset] = './T_ConveyorsBelt_A01_Decal_Alpha.png'
      * 'diffuse_texture' [asset] = './T_ConveyorsBelt_A01_Decal_Albedo.png'
      * 'reflection_roughness_texture_influence' [float] = '1'
      * 'metallic_texture_influence' [float] = '1'
      * 'ORM_texture' [asset] = './T_ConveyorsBelt_A01_Decal_ORM.png'

---

### /World/Conveyor_26/Looks/Metal_Rough_A

* **Prim路径 (Prim Path):**/World/Conveyor_26/Looks/Metal_Rough_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_26/Looks/Metal_Rough_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_26/Looks/Metal_Rough_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Metal/Misc/Metal_Rough_A.mdl' (Sub Id: 'Metal_Rough_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Metal/Misc/Metal_Rough_A.mdl'

---

### /World/Conveyor_26/Looks/MetalPainted_Black_Glossy_A

* **Prim路径 (Prim Path):**/World/Conveyor_26/Looks/MetalPainted_Black_Glossy_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_26/Looks/MetalPainted_Black_Glossy_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_26/Looks/MetalPainted_Black_Glossy_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Metal/Painted/MetalPainted_White_Glossy_A.mdl' (Sub Id: 'MetalPainted_White_Glossy_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Metal/Painted/MetalPainted_White_Glossy_A.mdl'
    * Inputs:
      * 'bump_factor' [float] = '0.5'
      * 'texture_scale' [float2] = '(1.500, 1.500)'
      * 'diffuse_tint' [color3f] = '(0.066, 0.066, 0.066)'
      * 'reflection_roughness_constant' [float] = '0.63'
      * 'reflection_roughness_texture_influence' [float] = '0.91'

---

### /World/Conveyor_26/Looks/MetalPainted_Blue_Glossy_A

* **Prim路径 (Prim Path):**/World/Conveyor_26/Looks/MetalPainted_Blue_Glossy_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_26/Looks/MetalPainted_Blue_Glossy_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_26/Looks/MetalPainted_Blue_Glossy_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Metal/Painted/MetalPainted_White_Glossy_A.mdl' (Sub Id: 'MetalPainted_White_Glossy_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Metal/Painted/MetalPainted_White_Glossy_A.mdl'
    * 纹理引用 (Texture Assets):
      * '../Material Library/Metal/Painted/T_MetalPainted_White_Glossy_A_Albedo.png'
      * '../Material Library/Metal/Painted/T_MetalPainted_White_Glossy_A_Normal.png'
      * '../Material Library/Metal/Painted/T_MetalPainted_White_Glossy_A_ORM.png'
    * Inputs:
      * 'bump_factor' [float] = '0.5'
      * 'normalmap_texture' [asset] = '../Material Library/Metal/Painted/T_MetalPainted_White_Glossy_A_Normal.png'
      * 'texture_scale' [float2] = '(1.500, 1.500)'
      * 'diffuse_texture' [asset] = '../Material Library/Metal/Painted/T_MetalPainted_White_Glossy_A_Albedo.png'
      * 'diffuse_tint' [color3f] = '(0.077, 0.203, 0.587)'
      * 'ORM_texture' [asset] = '../Material Library/Metal/Painted/T_MetalPainted_White_Glossy_A_ORM.png'

---

### /World/Conveyor_26/Looks/Plastic_Orange_A

* **Prim路径 (Prim Path):**/World/Conveyor_26/Looks/Plastic_Orange_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_26/Looks/Plastic_Orange_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_26/Looks/Plastic_Orange_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Plastic/Misc/Plastic_Orange_A.mdl' (Sub Id: 'Plastic_Orange_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Plastic/Misc/Plastic_Orange_A.mdl'

---

### /World/Conveyor_26/Looks/Plastic_Red_A

* **Prim路径 (Prim Path):**/World/Conveyor_26/Looks/Plastic_Red_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_26/Looks/Plastic_Red_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_26/Looks/Plastic_Red_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Plastic/Misc/Plastic_Red_A.mdl' (Sub Id: 'Plastic_Red_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Plastic/Misc/Plastic_Red_A.mdl'

---

### /World/Conveyor_26/Looks/Plastic_Rough_Black_A

* **Prim路径 (Prim Path):**/World/Conveyor_26/Looks/Plastic_Rough_Black_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_26/Looks/Plastic_Rough_Black_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_26/Looks/Plastic_Rough_Black_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Plastic/Misc/Plastic_Rough_Black_A.mdl' (Sub Id: 'Plastic_Rough_Black_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Plastic/Misc/Plastic_Rough_Black_A.mdl'

---

### /World/Conveyor_26/Looks/Steel_A

* **Prim路径 (Prim Path):**/World/Conveyor_26/Looks/Steel_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_26/Looks/Steel_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_26/Looks/Steel_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Metal/Steel/Steel_A.mdl' (Sub Id: 'Steel_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Metal/Steel/Steel_A.mdl'
    * Inputs:
      * 'diffuse_tint' [color3f] = '(0.772, 0.772, 0.772)'
      * 'reflection_roughness_constant' [float] = '0.67'
      * 'reflection_roughness_texture_influence' [float] = '0.88'

---

### /World/Conveyor_27/Looks/Acrylic_Clear_Glossy_A

* **Prim路径 (Prim Path):**/World/Conveyor_27/Looks/Acrylic_Clear_Glossy_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_27/Looks/Acrylic_Clear_Glossy_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_27/Looks/Acrylic_Clear_Glossy_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniGlass.mdl' (Sub Id: 'OmniGlass')
    * 纹理引用 (Texture Assets):
      * '../Material Library/Plastic/Textures/T_Acrylic_Clear_Glossy_A_Rough.png'
      * '../Material Library/Plastic/Textures/T_Plastic_Rough_Black_A_Normal.png'
    * Inputs:
      * 'normal_map_strength' [float] = '0.5'
      * 'texture_scale' [float2] = '(1.000, 3.000)'
      * 'normal_map_texture' [asset] = '../Material Library/Plastic/Textures/T_Plastic_Rough_Black_A_Normal.png'
      * 'roughness_texture' [asset] = '../Material Library/Plastic/Textures/T_Acrylic_Clear_Glossy_A_Rough.png'
      * 'roughness_texture_influence' [float] = '0.3'
      * 'glass_ior' [float] = '1.05'
      * 'frosting_roughness' [float] = '0.17'
      * 'glass_color' [color3f] = '(0.734, 0.734, 0.734)'

---

### /World/Conveyor_27/Looks/M_ConveyorBelt_A01_Belt

* **Prim路径 (Prim Path):**/World/Conveyor_27/Looks/M_ConveyorBelt_A01_Belt
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_27/Looks/M_ConveyorBelt_A01_Belt/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_27/Looks/M_ConveyorBelt_A01_Belt/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * 纹理引用 (Texture Assets):
      * './T_ConveyorBelt_A01_Belt_Albedo.png'
      * './T_ConveyorBelt_A01_Belt_Normal.png'
      * './T_ConveyorBelt_A01_Belt_ORM.png'
    * Inputs:
      * 'normalmap_texture' [asset] = './T_ConveyorBelt_A01_Belt_Normal.png'
      * 'diffuse_texture' [asset] = './T_ConveyorBelt_A01_Belt_Albedo.png'
      * 'reflection_roughness_texture_influence' [float] = '1'
      * 'metallic_texture_influence' [float] = '1'
      * 'ORM_texture' [asset] = './T_ConveyorBelt_A01_Belt_ORM.png'

---

### /World/Conveyor_27/Looks/M_ConveyorBelt_A01_Decal

* **Prim路径 (Prim Path):**/World/Conveyor_27/Looks/M_ConveyorBelt_A01_Decal
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_27/Looks/M_ConveyorBelt_A01_Decal/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_27/Looks/M_ConveyorBelt_A01_Decal/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * 纹理引用 (Texture Assets):
      * './T_ConveyorsBelt_A01_Decal_Albedo.png'
      * './T_ConveyorsBelt_A01_Decal_Alpha.png'
      * './T_ConveyorsBelt_A01_Decal_ORM.png'
    * Inputs:
      * 'opacity_texture' [asset] = './T_ConveyorsBelt_A01_Decal_Alpha.png'
      * 'diffuse_texture' [asset] = './T_ConveyorsBelt_A01_Decal_Albedo.png'
      * 'reflection_roughness_texture_influence' [float] = '1'
      * 'metallic_texture_influence' [float] = '1'
      * 'ORM_texture' [asset] = './T_ConveyorsBelt_A01_Decal_ORM.png'

---

### /World/Conveyor_27/Looks/Metal_Rough_A

* **Prim路径 (Prim Path):**/World/Conveyor_27/Looks/Metal_Rough_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_27/Looks/Metal_Rough_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_27/Looks/Metal_Rough_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Metal/Misc/Metal_Rough_A.mdl' (Sub Id: 'Metal_Rough_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Metal/Misc/Metal_Rough_A.mdl'

---

### /World/Conveyor_27/Looks/MetalPainted_Black_Glossy_A

* **Prim路径 (Prim Path):**/World/Conveyor_27/Looks/MetalPainted_Black_Glossy_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_27/Looks/MetalPainted_Black_Glossy_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_27/Looks/MetalPainted_Black_Glossy_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Metal/Painted/MetalPainted_White_Glossy_A.mdl' (Sub Id: 'MetalPainted_White_Glossy_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Metal/Painted/MetalPainted_White_Glossy_A.mdl'
    * Inputs:
      * 'bump_factor' [float] = '0.5'
      * 'texture_scale' [float2] = '(1.500, 1.500)'
      * 'diffuse_tint' [color3f] = '(0.066, 0.066, 0.066)'
      * 'reflection_roughness_constant' [float] = '0.63'
      * 'reflection_roughness_texture_influence' [float] = '0.91'

---

### /World/Conveyor_27/Looks/MetalPainted_Blue_Glossy_A

* **Prim路径 (Prim Path):**/World/Conveyor_27/Looks/MetalPainted_Blue_Glossy_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_27/Looks/MetalPainted_Blue_Glossy_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_27/Looks/MetalPainted_Blue_Glossy_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Metal/Painted/MetalPainted_White_Glossy_A.mdl' (Sub Id: 'MetalPainted_White_Glossy_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Metal/Painted/MetalPainted_White_Glossy_A.mdl'
    * 纹理引用 (Texture Assets):
      * '../Material Library/Metal/Painted/T_MetalPainted_White_Glossy_A_Albedo.png'
      * '../Material Library/Metal/Painted/T_MetalPainted_White_Glossy_A_Normal.png'
      * '../Material Library/Metal/Painted/T_MetalPainted_White_Glossy_A_ORM.png'
    * Inputs:
      * 'bump_factor' [float] = '0.5'
      * 'normalmap_texture' [asset] = '../Material Library/Metal/Painted/T_MetalPainted_White_Glossy_A_Normal.png'
      * 'texture_scale' [float2] = '(1.500, 1.500)'
      * 'diffuse_texture' [asset] = '../Material Library/Metal/Painted/T_MetalPainted_White_Glossy_A_Albedo.png'
      * 'diffuse_tint' [color3f] = '(0.077, 0.203, 0.587)'
      * 'ORM_texture' [asset] = '../Material Library/Metal/Painted/T_MetalPainted_White_Glossy_A_ORM.png'

---

### /World/Conveyor_27/Looks/Plastic_Orange_A

* **Prim路径 (Prim Path):**/World/Conveyor_27/Looks/Plastic_Orange_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_27/Looks/Plastic_Orange_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_27/Looks/Plastic_Orange_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Plastic/Misc/Plastic_Orange_A.mdl' (Sub Id: 'Plastic_Orange_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Plastic/Misc/Plastic_Orange_A.mdl'

---

### /World/Conveyor_27/Looks/Plastic_Red_A

* **Prim路径 (Prim Path):**/World/Conveyor_27/Looks/Plastic_Red_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_27/Looks/Plastic_Red_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_27/Looks/Plastic_Red_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Plastic/Misc/Plastic_Red_A.mdl' (Sub Id: 'Plastic_Red_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Plastic/Misc/Plastic_Red_A.mdl'

---

### /World/Conveyor_27/Looks/Plastic_Rough_Black_A

* **Prim路径 (Prim Path):**/World/Conveyor_27/Looks/Plastic_Rough_Black_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_27/Looks/Plastic_Rough_Black_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_27/Looks/Plastic_Rough_Black_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Plastic/Misc/Plastic_Rough_Black_A.mdl' (Sub Id: 'Plastic_Rough_Black_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Plastic/Misc/Plastic_Rough_Black_A.mdl'

---

### /World/Conveyor_27/Looks/Steel_A

* **Prim路径 (Prim Path):**/World/Conveyor_27/Looks/Steel_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_27/Looks/Steel_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_27/Looks/Steel_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Metal/Steel/Steel_A.mdl' (Sub Id: 'Steel_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Metal/Steel/Steel_A.mdl'
    * Inputs:
      * 'diffuse_tint' [color3f] = '(0.772, 0.772, 0.772)'
      * 'reflection_roughness_constant' [float] = '0.67'
      * 'reflection_roughness_texture_influence' [float] = '0.88'

---

### /World/Conveyor_28/Looks/Acrylic_Clear_Glossy_A

* **Prim路径 (Prim Path):**/World/Conveyor_28/Looks/Acrylic_Clear_Glossy_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_28/Looks/Acrylic_Clear_Glossy_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_28/Looks/Acrylic_Clear_Glossy_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniGlass.mdl' (Sub Id: 'OmniGlass')
    * 纹理引用 (Texture Assets):
      * '../Material Library/Plastic/Textures/T_Acrylic_Clear_Glossy_A_Rough.png'
      * '../Material Library/Plastic/Textures/T_Plastic_Rough_Black_A_Normal.png'
    * Inputs:
      * 'normal_map_strength' [float] = '0.5'
      * 'texture_scale' [float2] = '(1.000, 3.000)'
      * 'normal_map_texture' [asset] = '../Material Library/Plastic/Textures/T_Plastic_Rough_Black_A_Normal.png'
      * 'roughness_texture' [asset] = '../Material Library/Plastic/Textures/T_Acrylic_Clear_Glossy_A_Rough.png'
      * 'roughness_texture_influence' [float] = '0.3'
      * 'glass_ior' [float] = '1.05'
      * 'frosting_roughness' [float] = '0.17'
      * 'glass_color' [color3f] = '(0.734, 0.734, 0.734)'

---

### /World/Conveyor_28/Looks/M_ConveyorBelt_A01_Belt

* **Prim路径 (Prim Path):**/World/Conveyor_28/Looks/M_ConveyorBelt_A01_Belt
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_28/Looks/M_ConveyorBelt_A01_Belt/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_28/Looks/M_ConveyorBelt_A01_Belt/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * 纹理引用 (Texture Assets):
      * './T_ConveyorBelt_A01_Belt_Albedo.png'
      * './T_ConveyorBelt_A01_Belt_Normal.png'
      * './T_ConveyorBelt_A01_Belt_ORM.png'
    * Inputs:
      * 'normalmap_texture' [asset] = './T_ConveyorBelt_A01_Belt_Normal.png'
      * 'diffuse_texture' [asset] = './T_ConveyorBelt_A01_Belt_Albedo.png'
      * 'reflection_roughness_texture_influence' [float] = '1'
      * 'metallic_texture_influence' [float] = '1'
      * 'ORM_texture' [asset] = './T_ConveyorBelt_A01_Belt_ORM.png'

---

### /World/Conveyor_28/Looks/M_ConveyorBelt_A01_Decal

* **Prim路径 (Prim Path):**/World/Conveyor_28/Looks/M_ConveyorBelt_A01_Decal
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_28/Looks/M_ConveyorBelt_A01_Decal/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_28/Looks/M_ConveyorBelt_A01_Decal/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * 纹理引用 (Texture Assets):
      * './T_ConveyorsBelt_A01_Decal_Albedo.png'
      * './T_ConveyorsBelt_A01_Decal_Alpha.png'
      * './T_ConveyorsBelt_A01_Decal_ORM.png'
    * Inputs:
      * 'opacity_texture' [asset] = './T_ConveyorsBelt_A01_Decal_Alpha.png'
      * 'diffuse_texture' [asset] = './T_ConveyorsBelt_A01_Decal_Albedo.png'
      * 'reflection_roughness_texture_influence' [float] = '1'
      * 'metallic_texture_influence' [float] = '1'
      * 'ORM_texture' [asset] = './T_ConveyorsBelt_A01_Decal_ORM.png'

---

### /World/Conveyor_28/Looks/Metal_Rough_A

* **Prim路径 (Prim Path):**/World/Conveyor_28/Looks/Metal_Rough_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_28/Looks/Metal_Rough_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_28/Looks/Metal_Rough_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Metal/Misc/Metal_Rough_A.mdl' (Sub Id: 'Metal_Rough_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Metal/Misc/Metal_Rough_A.mdl'

---

### /World/Conveyor_28/Looks/MetalPainted_Black_Glossy_A

* **Prim路径 (Prim Path):**/World/Conveyor_28/Looks/MetalPainted_Black_Glossy_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_28/Looks/MetalPainted_Black_Glossy_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_28/Looks/MetalPainted_Black_Glossy_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Metal/Painted/MetalPainted_White_Glossy_A.mdl' (Sub Id: 'MetalPainted_White_Glossy_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Metal/Painted/MetalPainted_White_Glossy_A.mdl'
    * Inputs:
      * 'bump_factor' [float] = '0.5'
      * 'texture_scale' [float2] = '(1.500, 1.500)'
      * 'diffuse_tint' [color3f] = '(0.066, 0.066, 0.066)'
      * 'reflection_roughness_constant' [float] = '0.63'
      * 'reflection_roughness_texture_influence' [float] = '0.91'

---

### /World/Conveyor_28/Looks/MetalPainted_Blue_Glossy_A

* **Prim路径 (Prim Path):**/World/Conveyor_28/Looks/MetalPainted_Blue_Glossy_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_28/Looks/MetalPainted_Blue_Glossy_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_28/Looks/MetalPainted_Blue_Glossy_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Metal/Painted/MetalPainted_White_Glossy_A.mdl' (Sub Id: 'MetalPainted_White_Glossy_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Metal/Painted/MetalPainted_White_Glossy_A.mdl'
    * 纹理引用 (Texture Assets):
      * '../Material Library/Metal/Painted/T_MetalPainted_White_Glossy_A_Albedo.png'
      * '../Material Library/Metal/Painted/T_MetalPainted_White_Glossy_A_Normal.png'
      * '../Material Library/Metal/Painted/T_MetalPainted_White_Glossy_A_ORM.png'
    * Inputs:
      * 'bump_factor' [float] = '0.5'
      * 'normalmap_texture' [asset] = '../Material Library/Metal/Painted/T_MetalPainted_White_Glossy_A_Normal.png'
      * 'texture_scale' [float2] = '(1.500, 1.500)'
      * 'diffuse_texture' [asset] = '../Material Library/Metal/Painted/T_MetalPainted_White_Glossy_A_Albedo.png'
      * 'diffuse_tint' [color3f] = '(0.077, 0.203, 0.587)'
      * 'ORM_texture' [asset] = '../Material Library/Metal/Painted/T_MetalPainted_White_Glossy_A_ORM.png'

---

### /World/Conveyor_28/Looks/Plastic_Orange_A

* **Prim路径 (Prim Path):**/World/Conveyor_28/Looks/Plastic_Orange_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_28/Looks/Plastic_Orange_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_28/Looks/Plastic_Orange_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Plastic/Misc/Plastic_Orange_A.mdl' (Sub Id: 'Plastic_Orange_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Plastic/Misc/Plastic_Orange_A.mdl'

---

### /World/Conveyor_28/Looks/Plastic_Red_A

* **Prim路径 (Prim Path):**/World/Conveyor_28/Looks/Plastic_Red_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_28/Looks/Plastic_Red_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_28/Looks/Plastic_Red_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Plastic/Misc/Plastic_Red_A.mdl' (Sub Id: 'Plastic_Red_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Plastic/Misc/Plastic_Red_A.mdl'

---

### /World/Conveyor_28/Looks/Plastic_Rough_Black_A

* **Prim路径 (Prim Path):**/World/Conveyor_28/Looks/Plastic_Rough_Black_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_28/Looks/Plastic_Rough_Black_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_28/Looks/Plastic_Rough_Black_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Plastic/Misc/Plastic_Rough_Black_A.mdl' (Sub Id: 'Plastic_Rough_Black_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Plastic/Misc/Plastic_Rough_Black_A.mdl'

---

### /World/Conveyor_28/Looks/Steel_A

* **Prim路径 (Prim Path):**/World/Conveyor_28/Looks/Steel_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Conveyor_28/Looks/Steel_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_28/Looks/Steel_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '../Material Library/Metal/Steel/Steel_A.mdl' (Sub Id: 'Steel_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/Material Library/Metal/Steel/Steel_A.mdl'
    * Inputs:
      * 'diffuse_tint' [color3f] = '(0.772, 0.772, 0.772)'
      * 'reflection_roughness_constant' [float] = '0.67'
      * 'reflection_roughness_texture_influence' [float] = '0.88'

---

### /World/agv_1/Materials/ASELSAN_CATS_04

* **Prim路径 (Prim Path):**/World/agv_1/Materials/ASELSAN_CATS_04
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_1/Materials/ASELSAN_CATS_04/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_1/Materials/ASELSAN_CATS_04/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.158, 0.158, 0.158)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_1/Materials/ASELSAN_CATS_04_2

* **Prim路径 (Prim Path):**/World/agv_1/Materials/ASELSAN_CATS_04_2
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_1/Materials/ASELSAN_CATS_04_2/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_1/Materials/ASELSAN_CATS_04_2/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.769, 0.773, 0.749)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_1/Materials/ASELSAN_CATS_13

* **Prim路径 (Prim Path):**/World/agv_1/Materials/ASELSAN_CATS_13
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_1/Materials/ASELSAN_CATS_13/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_1/Materials/ASELSAN_CATS_13/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.706, 0.718, 0.729)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_1/Materials/Color_000

* **Prim路径 (Prim Path):**/World/agv_1/Materials/Color_000
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_1/Materials/Color_000/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_1/Materials/Color_000/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(1.000, 1.000, 1.000)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_1/Materials/Color_A05

* **Prim路径 (Prim Path):**/World/agv_1/Materials/Color_A05
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_1/Materials/Color_A05/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_1/Materials/Color_A05/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(1.000, 0.000, 0.000)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0.959234'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0'

---

### /World/agv_1/Materials/Color_A06

* **Prim路径 (Prim Path):**/World/agv_1/Materials/Color_A06
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_1/Materials/Color_A06/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_1/Materials/Color_A06/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.800, 0.000, 0.000)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_1/Materials/Color_B05

* **Prim路径 (Prim Path):**/World/agv_1/Materials/Color_B05
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_1/Materials/Color_B05/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_1/Materials/Color_B05/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(1.000, 0.247, 0.000)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '1'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0'

---

### /World/agv_1/Materials/Color_E02

* **Prim路径 (Prim Path):**/World/agv_1/Materials/Color_E02
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_1/Materials/Color_E02/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_1/Materials/Color_E02/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(1.000, 1.000, 0.196)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_1/Materials/Color_E05

* **Prim路径 (Prim Path):**/World/agv_1/Materials/Color_E05
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_1/Materials/Color_E05/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_1/Materials/Color_E05/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(1.000, 0.910, 0.000)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0.625455'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0.133891'

---

### /World/agv_1/Materials/Color_F06

* **Prim路径 (Prim Path):**/World/agv_1/Materials/Color_F06
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_1/Materials/Color_F06/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_1/Materials/Color_F06/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.400, 0.800, 0.000)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_1/Materials/Color_G03

* **Prim路径 (Prim Path):**/World/agv_1/Materials/Color_G03
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_1/Materials/Color_G03/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_1/Materials/Color_G03/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.396, 1.000, 0.396)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_1/Materials/Color_M02

* **Prim路径 (Prim Path):**/World/agv_1/Materials/Color_M02
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_1/Materials/Color_M02/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_1/Materials/Color_M02/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.776, 0.776, 0.776)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_1/Materials/Color_M03

* **Prim路径 (Prim Path):**/World/agv_1/Materials/Color_M03
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_1/Materials/Color_M03/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_1/Materials/Color_M03/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.667, 0.667, 0.667)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_1/Materials/Mtl39

* **Prim路径 (Prim Path):**/World/agv_1/Materials/Mtl39
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_1/Materials/Mtl39/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_1/Materials/Mtl39/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.494, 0.494, 0.494)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_1/Materials/Mtl6

* **Prim路径 (Prim Path):**/World/agv_1/Materials/Mtl6
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_1/Materials/Mtl6/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_1/Materials/Mtl6/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f]
        * Connected: '/World/agv_1/Materials/Mtl6/tex_base.outputs:rgb' @ '/World/agv_1/Materials/Mtl6/tex_base'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/Mtl6_baseColor.jpg'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'
    * '/World/agv_1/Materials/Mtl6/tex_base' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/Mtl6_baseColor.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'file' [asset] = '0/Mtl6_baseColor.jpg'
      * 'st' [float2]
        * Connected: '/World/agv_1/Materials/Mtl6/uvset0.outputs:result' @ '/World/agv_1/Materials/Mtl6/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/agv_1/Materials/Mtl6/uvset0' (ID: 'UsdPrimvarReader_float2')
    * Implementation: 'id'

---

### /World/agv_1/Materials/Mtl9

* **Prim路径 (Prim Path):**/World/agv_1/Materials/Mtl9
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_1/Materials/Mtl9/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_1/Materials/Mtl9/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.514, 1.000, 0.000)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_1/Materials/Silver

* **Prim路径 (Prim Path):**/World/agv_1/Materials/Silver
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_1/Materials/Silver/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_1/Materials/Silver/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.753, 0.753, 0.753)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_1/Materials/material

* **Prim路径 (Prim Path):**/World/agv_1/Materials/material
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_1/Materials/material/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_1/Materials/material/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f]
        * Connected: '/World/agv_1/Materials/material/tex_base.outputs:rgb' @ '/World/agv_1/Materials/material/tex_base'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/material_baseColor.jpg'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'
    * '/World/agv_1/Materials/material/tex_base' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/material_baseColor.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'file' [asset] = '0/material_baseColor.jpg'
      * 'st' [float2]
        * Connected: '/World/agv_1/Materials/material/uvset0.outputs:result' @ '/World/agv_1/Materials/material/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/agv_1/Materials/material/uvset0' (ID: 'UsdPrimvarReader_float2')
    * Implementation: 'id'

---

### /World/agv_1/Materials/cash_register_keys

* **Prim路径 (Prim Path):**/World/agv_1/Materials/cash_register_keys
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_1/Materials/cash_register_keys/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_1/Materials/cash_register_keys/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.976, 0.992, 0.973)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_1/Materials/Chris_Shoe_Sole

* **Prim路径 (Prim Path):**/World/agv_1/Materials/Chris_Shoe_Sole
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_1/Materials/Chris_Shoe_Sole/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_1/Materials/Chris_Shoe_Sole/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.155, 0.149, 0.149)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'opacity' [float] = '0.25'
      * 'roughness' [float] = '1'

---

### /World/agv_1/Materials/Color_002

* **Prim路径 (Prim Path):**/World/agv_1/Materials/Color_002
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_1/Materials/Color_002/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_1/Materials/Color_002/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.217, 0.217, 0.217)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0.570837'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0'

---

### /World/agv_1/Materials/Color_005

* **Prim路径 (Prim Path):**/World/agv_1/Materials/Color_005
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_1/Materials/Color_005/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_1/Materials/Color_005/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.130, 0.130, 0.130)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0.710417'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0'

---

### /World/agv_1/Materials/Color_006

* **Prim路径 (Prim Path):**/World/agv_1/Materials/Color_006
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_1/Materials/Color_006/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_1/Materials/Color_006/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0.237059'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0'

---

### /World/agv_1/Materials/Color_008

* **Prim路径 (Prim Path):**/World/agv_1/Materials/Color_008
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_1/Materials/Color_008/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_1/Materials/Color_008/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.118, 0.118, 0.118)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0.941027'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0'

---

### /World/agv_1/Materials/Color_A01

* **Prim路径 (Prim Path):**/World/agv_1/Materials/Color_A01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_1/Materials/Color_A01/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_1/Materials/Color_A01/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(1.000, 0.000, 0.000)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0.965302'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0'

---

### /World/agv_1/Materials/Color_A11

* **Prim路径 (Prim Path):**/World/agv_1/Materials/Color_A11
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_1/Materials/Color_A11/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_1/Materials/Color_A11/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.600, 0.000, 0.000)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_1/Materials/Color_M04

* **Prim路径 (Prim Path):**/World/agv_1/Materials/Color_M04
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_1/Materials/Color_M04/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_1/Materials/Color_M04/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.557, 0.557, 0.557)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_1/Materials/Color_M05

* **Prim路径 (Prim Path):**/World/agv_1/Materials/Color_M05
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_1/Materials/Color_M05/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_1/Materials/Color_M05/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.447, 0.447, 0.447)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_1/Materials/Color_M06

* **Prim路径 (Prim Path):**/World/agv_1/Materials/Color_M06
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_1/Materials/Color_M06/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_1/Materials/Color_M06/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_1/Materials/Color_M07

* **Prim路径 (Prim Path):**/World/agv_1/Materials/Color_M07
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_1/Materials/Color_M07/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_1/Materials/Color_M07/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.227, 0.227, 0.227)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_1/Materials/Color_M09

* **Prim路径 (Prim Path):**/World/agv_1/Materials/Color_M09
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_1/Materials/Color_M09/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_1/Materials/Color_M09/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0.340226'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0.085341'

---

### /World/agv_1/Materials/FCP_Charcoal_v2

* **Prim路径 (Prim Path):**/World/agv_1/Materials/FCP_Charcoal_v2
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_1/Materials/FCP_Charcoal_v2/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_1/Materials/FCP_Charcoal_v2/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.216, 0.216, 0.216)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_1/Materials/FrontColor

* **Prim路径 (Prim Path):**/World/agv_1/Materials/FrontColor
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_1/Materials/FrontColor/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_1/Materials/FrontColor/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.504, 0.504, 0.504)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0.637593'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0.218852'

---

### /World/agv_1/Materials/Light_Blue

* **Prim路径 (Prim Path):**/World/agv_1/Materials/Light_Blue
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_1/Materials/Light_Blue/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_1/Materials/Light_Blue/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.601, 0.601, 0.601)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '1'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0.170303'

---

### /World/agv_1/Materials/M_0011_Seashell

* **Prim路径 (Prim Path):**/World/agv_1/Materials/M_0011_Seashell
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_1/Materials/M_0011_Seashell/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_1/Materials/M_0011_Seashell/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(1.000, 0.961, 0.933)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_1/Materials/M_0131_Silver

* **Prim路径 (Prim Path):**/World/agv_1/Materials/M_0131_Silver
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_1/Materials/M_0131_Silver/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_1/Materials/M_0131_Silver/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.242, 0.242, 0.242)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0.613318'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0'

---

### /World/agv_1/Materials/M_0134_DimGray

* **Prim路径 (Prim Path):**/World/agv_1/Materials/M_0134_DimGray
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_1/Materials/M_0134_DimGray/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_1/Materials/M_0134_DimGray/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.412, 0.412, 0.412)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_1/Materials/M_0135_DarkGray

* **Prim路径 (Prim Path):**/World/agv_1/Materials/M_0135_DarkGray
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_1/Materials/M_0135_DarkGray/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_1/Materials/M_0135_DarkGray/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.318, 0.318, 0.318)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_1/Materials/Metal_Silver

* **Prim路径 (Prim Path):**/World/agv_1/Materials/Metal_Silver
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_1/Materials/Metal_Silver/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_1/Materials/Metal_Silver/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.918, 0.914, 0.933)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_1/Materials/Mtl1

* **Prim路径 (Prim Path):**/World/agv_1/Materials/Mtl1
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_1/Materials/Mtl1/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_1/Materials/Mtl1/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.015, 0.015, 0.015)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0.255265'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_1/Materials/Mtl10

* **Prim路径 (Prim Path):**/World/agv_1/Materials/Mtl10
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_1/Materials/Mtl10/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_1/Materials/Mtl10/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.322, 0.322, 0.322)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_1/Materials/Mtl11

* **Prim路径 (Prim Path):**/World/agv_1/Materials/Mtl11
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_1/Materials/Mtl11/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_1/Materials/Mtl11/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.067, 0.757, 0.329)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_1/Materials/Mtl12

* **Prim路径 (Prim Path):**/World/agv_1/Materials/Mtl12
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_1/Materials/Mtl12/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_1/Materials/Mtl12/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.502, 0.502, 0.502)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_1/Materials/Mtl13

* **Prim路径 (Prim Path):**/World/agv_1/Materials/Mtl13
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_1/Materials/Mtl13/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_1/Materials/Mtl13/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.008, 0.514, 0.816)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_1/Materials/Mtl14

* **Prim路径 (Prim Path):**/World/agv_1/Materials/Mtl14
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_1/Materials/Mtl14/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_1/Materials/Mtl14/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.310, 0.310, 0.310)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_1/Materials/Mtl15

* **Prim路径 (Prim Path):**/World/agv_1/Materials/Mtl15
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_1/Materials/Mtl15/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_1/Materials/Mtl15/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.263, 0.275, 0.275)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_1/Materials/Mtl16

* **Prim路径 (Prim Path):**/World/agv_1/Materials/Mtl16
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_1/Materials/Mtl16/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_1/Materials/Mtl16/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.698, 0.698, 0.000)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_1/Materials/Mtl17

* **Prim路径 (Prim Path):**/World/agv_1/Materials/Mtl17
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_1/Materials/Mtl17/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_1/Materials/Mtl17/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.000, 0.863, 1.000)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_1/Materials/Mtl3

* **Prim路径 (Prim Path):**/World/agv_1/Materials/Mtl3
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_1/Materials/Mtl3/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_1/Materials/Mtl3/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.431, 0.455, 0.498)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_1/Materials/Mtl35

* **Prim路径 (Prim Path):**/World/agv_1/Materials/Mtl35
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_1/Materials/Mtl35/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_1/Materials/Mtl35/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.792, 0.820, 0.933)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_1/Materials/Mtl36

* **Prim路径 (Prim Path):**/World/agv_1/Materials/Mtl36
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_1/Materials/Mtl36/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_1/Materials/Mtl36/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.667, 0.698, 0.765)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_1/Materials/Mtl37

* **Prim路径 (Prim Path):**/World/agv_1/Materials/Mtl37
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_1/Materials/Mtl37/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_1/Materials/Mtl37/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.098, 0.098, 0.098)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_1/Materials/Mtl3a

* **Prim路径 (Prim Path):**/World/agv_1/Materials/Mtl3a
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_1/Materials/Mtl3a/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_1/Materials/Mtl3a/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.388, 0.369, 0.322)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_1/Materials/Mtl3b

* **Prim路径 (Prim Path):**/World/agv_1/Materials/Mtl3b
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_1/Materials/Mtl3b/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_1/Materials/Mtl3b/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.365, 0.176, 0.012)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0.959234'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'opacity' [float] = '0.273471'
      * 'roughness' [float] = '0.164234'

---

### /World/agv_1/Materials/Mtl5

* **Prim路径 (Prim Path):**/World/agv_1/Materials/Mtl5
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_1/Materials/Mtl5/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_1/Materials/Mtl5/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.396, 0.408, 0.467)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_1/Materials/Mtl7

* **Prim路径 (Prim Path):**/World/agv_1/Materials/Mtl7
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_1/Materials/Mtl7/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_1/Materials/Mtl7/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.376, 0.376, 0.376)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_1/Materials/Mtl8

* **Prim路径 (Prim Path):**/World/agv_1/Materials/Mtl8
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_1/Materials/Mtl8/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_1/Materials/Mtl8/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.173, 0.173, 0.173)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_1/Materials/Mtla

* **Prim路径 (Prim Path):**/World/agv_1/Materials/Mtla
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_1/Materials/Mtla/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_1/Materials/Mtla/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.612, 0.725, 0.745)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_1/Materials/Mtlb1

* **Prim路径 (Prim Path):**/World/agv_1/Materials/Mtlb1
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_1/Materials/Mtlb1/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_1/Materials/Mtlb1/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.949, 0.925, 0.933)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_1/Materials/Stainless_Steel

* **Prim路径 (Prim Path):**/World/agv_1/Materials/Stainless_Steel
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_1/Materials/Stainless_Steel/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_1/Materials/Stainless_Steel/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.292, 0.294, 0.284)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0.431257'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_1/Materials/Metal_Aluminum_Anodized_1

* **Prim路径 (Prim Path):**/World/agv_1/Materials/Metal_Aluminum_Anodized_1
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_1/Materials/Metal_Aluminum_Anodized_1/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_1/Materials/Metal_Aluminum_Anodized_1/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.260, 0.269, 0.282)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0.309883'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0'

---

### /World/agv_1/Materials/Metal_Aluminum_Anodized_2

* **Prim路径 (Prim Path):**/World/agv_1/Materials/Metal_Aluminum_Anodized_2
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_1/Materials/Metal_Aluminum_Anodized_2/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_1/Materials/Metal_Aluminum_Anodized_2/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.792, 0.820, 0.859)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_1/Materials/basic_gray_plastic

* **Prim路径 (Prim Path):**/World/agv_1/Materials/basic_gray_plastic
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_1/Materials/basic_gray_plastic/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_1/Materials/basic_gray_plastic/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0.297745'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0.115685'

---

### /World/agv_1/Materials/texture

* **Prim路径 (Prim Path):**/World/agv_1/Materials/texture
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_1/Materials/texture/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_1/Materials/texture/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.294, 0.294, 0.294)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_2/Materials/ASELSAN_CATS_04

* **Prim路径 (Prim Path):**/World/agv_2/Materials/ASELSAN_CATS_04
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_2/Materials/ASELSAN_CATS_04/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_2/Materials/ASELSAN_CATS_04/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.158, 0.158, 0.158)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_2/Materials/ASELSAN_CATS_04_2

* **Prim路径 (Prim Path):**/World/agv_2/Materials/ASELSAN_CATS_04_2
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_2/Materials/ASELSAN_CATS_04_2/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_2/Materials/ASELSAN_CATS_04_2/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.769, 0.773, 0.749)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_2/Materials/ASELSAN_CATS_13

* **Prim路径 (Prim Path):**/World/agv_2/Materials/ASELSAN_CATS_13
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_2/Materials/ASELSAN_CATS_13/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_2/Materials/ASELSAN_CATS_13/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.706, 0.718, 0.729)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_2/Materials/Color_000

* **Prim路径 (Prim Path):**/World/agv_2/Materials/Color_000
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_2/Materials/Color_000/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_2/Materials/Color_000/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(1.000, 1.000, 1.000)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_2/Materials/Color_A05

* **Prim路径 (Prim Path):**/World/agv_2/Materials/Color_A05
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_2/Materials/Color_A05/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_2/Materials/Color_A05/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(1.000, 0.000, 0.000)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0.959234'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0'

---

### /World/agv_2/Materials/Color_A06

* **Prim路径 (Prim Path):**/World/agv_2/Materials/Color_A06
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_2/Materials/Color_A06/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_2/Materials/Color_A06/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.800, 0.000, 0.000)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_2/Materials/Color_B05

* **Prim路径 (Prim Path):**/World/agv_2/Materials/Color_B05
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_2/Materials/Color_B05/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_2/Materials/Color_B05/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(1.000, 0.247, 0.000)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '1'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0'

---

### /World/agv_2/Materials/Color_E02

* **Prim路径 (Prim Path):**/World/agv_2/Materials/Color_E02
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_2/Materials/Color_E02/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_2/Materials/Color_E02/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(1.000, 1.000, 0.196)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_2/Materials/Color_E05

* **Prim路径 (Prim Path):**/World/agv_2/Materials/Color_E05
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_2/Materials/Color_E05/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_2/Materials/Color_E05/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(1.000, 0.910, 0.000)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0.625455'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0.133891'

---

### /World/agv_2/Materials/Color_F06

* **Prim路径 (Prim Path):**/World/agv_2/Materials/Color_F06
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_2/Materials/Color_F06/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_2/Materials/Color_F06/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.400, 0.800, 0.000)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_2/Materials/Color_G03

* **Prim路径 (Prim Path):**/World/agv_2/Materials/Color_G03
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_2/Materials/Color_G03/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_2/Materials/Color_G03/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.396, 1.000, 0.396)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_2/Materials/Color_M02

* **Prim路径 (Prim Path):**/World/agv_2/Materials/Color_M02
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_2/Materials/Color_M02/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_2/Materials/Color_M02/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.776, 0.776, 0.776)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_2/Materials/Color_M03

* **Prim路径 (Prim Path):**/World/agv_2/Materials/Color_M03
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_2/Materials/Color_M03/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_2/Materials/Color_M03/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.667, 0.667, 0.667)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_2/Materials/Mtl39

* **Prim路径 (Prim Path):**/World/agv_2/Materials/Mtl39
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_2/Materials/Mtl39/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_2/Materials/Mtl39/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.494, 0.494, 0.494)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_2/Materials/Mtl6

* **Prim路径 (Prim Path):**/World/agv_2/Materials/Mtl6
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_2/Materials/Mtl6/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_2/Materials/Mtl6/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f]
        * Connected: '/World/agv_2/Materials/Mtl6/tex_base.outputs:rgb' @ '/World/agv_2/Materials/Mtl6/tex_base'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/Mtl6_baseColor.jpg'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'
    * '/World/agv_2/Materials/Mtl6/tex_base' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/Mtl6_baseColor.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'file' [asset] = '0/Mtl6_baseColor.jpg'
      * 'st' [float2]
        * Connected: '/World/agv_2/Materials/Mtl6/uvset0.outputs:result' @ '/World/agv_2/Materials/Mtl6/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/agv_2/Materials/Mtl6/uvset0' (ID: 'UsdPrimvarReader_float2')
    * Implementation: 'id'

---

### /World/agv_2/Materials/Mtl9

* **Prim路径 (Prim Path):**/World/agv_2/Materials/Mtl9
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_2/Materials/Mtl9/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_2/Materials/Mtl9/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.514, 1.000, 0.000)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_2/Materials/Silver

* **Prim路径 (Prim Path):**/World/agv_2/Materials/Silver
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_2/Materials/Silver/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_2/Materials/Silver/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.753, 0.753, 0.753)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_2/Materials/material

* **Prim路径 (Prim Path):**/World/agv_2/Materials/material
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_2/Materials/material/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_2/Materials/material/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f]
        * Connected: '/World/agv_2/Materials/material/tex_base.outputs:rgb' @ '/World/agv_2/Materials/material/tex_base'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/material_baseColor.jpg'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'
    * '/World/agv_2/Materials/material/tex_base' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/material_baseColor.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'file' [asset] = '0/material_baseColor.jpg'
      * 'st' [float2]
        * Connected: '/World/agv_2/Materials/material/uvset0.outputs:result' @ '/World/agv_2/Materials/material/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/agv_2/Materials/material/uvset0' (ID: 'UsdPrimvarReader_float2')
    * Implementation: 'id'

---

### /World/agv_2/Materials/cash_register_keys

* **Prim路径 (Prim Path):**/World/agv_2/Materials/cash_register_keys
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_2/Materials/cash_register_keys/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_2/Materials/cash_register_keys/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.976, 0.992, 0.973)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_2/Materials/Chris_Shoe_Sole

* **Prim路径 (Prim Path):**/World/agv_2/Materials/Chris_Shoe_Sole
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_2/Materials/Chris_Shoe_Sole/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_2/Materials/Chris_Shoe_Sole/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.155, 0.149, 0.149)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'opacity' [float] = '0.25'
      * 'roughness' [float] = '1'

---

### /World/agv_2/Materials/Color_002

* **Prim路径 (Prim Path):**/World/agv_2/Materials/Color_002
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_2/Materials/Color_002/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_2/Materials/Color_002/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.217, 0.217, 0.217)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0.570837'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0'

---

### /World/agv_2/Materials/Color_005

* **Prim路径 (Prim Path):**/World/agv_2/Materials/Color_005
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_2/Materials/Color_005/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_2/Materials/Color_005/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.130, 0.130, 0.130)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0.710417'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0'

---

### /World/agv_2/Materials/Color_006

* **Prim路径 (Prim Path):**/World/agv_2/Materials/Color_006
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_2/Materials/Color_006/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_2/Materials/Color_006/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0.237059'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0'

---

### /World/agv_2/Materials/Color_008

* **Prim路径 (Prim Path):**/World/agv_2/Materials/Color_008
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_2/Materials/Color_008/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_2/Materials/Color_008/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.118, 0.118, 0.118)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0.941027'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0'

---

### /World/agv_2/Materials/Color_A01

* **Prim路径 (Prim Path):**/World/agv_2/Materials/Color_A01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_2/Materials/Color_A01/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_2/Materials/Color_A01/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(1.000, 0.000, 0.000)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0.965302'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0'

---

### /World/agv_2/Materials/Color_A11

* **Prim路径 (Prim Path):**/World/agv_2/Materials/Color_A11
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_2/Materials/Color_A11/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_2/Materials/Color_A11/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.600, 0.000, 0.000)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_2/Materials/Color_M04

* **Prim路径 (Prim Path):**/World/agv_2/Materials/Color_M04
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_2/Materials/Color_M04/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_2/Materials/Color_M04/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.557, 0.557, 0.557)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_2/Materials/Color_M05

* **Prim路径 (Prim Path):**/World/agv_2/Materials/Color_M05
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_2/Materials/Color_M05/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_2/Materials/Color_M05/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.447, 0.447, 0.447)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_2/Materials/Color_M06

* **Prim路径 (Prim Path):**/World/agv_2/Materials/Color_M06
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_2/Materials/Color_M06/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_2/Materials/Color_M06/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_2/Materials/Color_M07

* **Prim路径 (Prim Path):**/World/agv_2/Materials/Color_M07
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_2/Materials/Color_M07/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_2/Materials/Color_M07/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.227, 0.227, 0.227)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_2/Materials/Color_M09

* **Prim路径 (Prim Path):**/World/agv_2/Materials/Color_M09
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_2/Materials/Color_M09/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_2/Materials/Color_M09/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0.340226'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0.085341'

---

### /World/agv_2/Materials/FCP_Charcoal_v2

* **Prim路径 (Prim Path):**/World/agv_2/Materials/FCP_Charcoal_v2
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_2/Materials/FCP_Charcoal_v2/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_2/Materials/FCP_Charcoal_v2/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.216, 0.216, 0.216)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_2/Materials/FrontColor

* **Prim路径 (Prim Path):**/World/agv_2/Materials/FrontColor
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_2/Materials/FrontColor/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_2/Materials/FrontColor/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.504, 0.504, 0.504)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0.637593'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0.218852'

---

### /World/agv_2/Materials/Light_Blue

* **Prim路径 (Prim Path):**/World/agv_2/Materials/Light_Blue
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_2/Materials/Light_Blue/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_2/Materials/Light_Blue/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.601, 0.601, 0.601)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '1'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0.170303'

---

### /World/agv_2/Materials/M_0011_Seashell

* **Prim路径 (Prim Path):**/World/agv_2/Materials/M_0011_Seashell
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_2/Materials/M_0011_Seashell/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_2/Materials/M_0011_Seashell/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(1.000, 0.961, 0.933)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_2/Materials/M_0131_Silver

* **Prim路径 (Prim Path):**/World/agv_2/Materials/M_0131_Silver
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_2/Materials/M_0131_Silver/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_2/Materials/M_0131_Silver/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.242, 0.242, 0.242)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0.613318'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0'

---

### /World/agv_2/Materials/M_0134_DimGray

* **Prim路径 (Prim Path):**/World/agv_2/Materials/M_0134_DimGray
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_2/Materials/M_0134_DimGray/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_2/Materials/M_0134_DimGray/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.412, 0.412, 0.412)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_2/Materials/M_0135_DarkGray

* **Prim路径 (Prim Path):**/World/agv_2/Materials/M_0135_DarkGray
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_2/Materials/M_0135_DarkGray/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_2/Materials/M_0135_DarkGray/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.318, 0.318, 0.318)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_2/Materials/Metal_Silver

* **Prim路径 (Prim Path):**/World/agv_2/Materials/Metal_Silver
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_2/Materials/Metal_Silver/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_2/Materials/Metal_Silver/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.918, 0.914, 0.933)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_2/Materials/Mtl1

* **Prim路径 (Prim Path):**/World/agv_2/Materials/Mtl1
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_2/Materials/Mtl1/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_2/Materials/Mtl1/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.015, 0.015, 0.015)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0.255265'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_2/Materials/Mtl10

* **Prim路径 (Prim Path):**/World/agv_2/Materials/Mtl10
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_2/Materials/Mtl10/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_2/Materials/Mtl10/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.322, 0.322, 0.322)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_2/Materials/Mtl11

* **Prim路径 (Prim Path):**/World/agv_2/Materials/Mtl11
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_2/Materials/Mtl11/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_2/Materials/Mtl11/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.067, 0.757, 0.329)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_2/Materials/Mtl12

* **Prim路径 (Prim Path):**/World/agv_2/Materials/Mtl12
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_2/Materials/Mtl12/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_2/Materials/Mtl12/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.502, 0.502, 0.502)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_2/Materials/Mtl13

* **Prim路径 (Prim Path):**/World/agv_2/Materials/Mtl13
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_2/Materials/Mtl13/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_2/Materials/Mtl13/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.008, 0.514, 0.816)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_2/Materials/Mtl14

* **Prim路径 (Prim Path):**/World/agv_2/Materials/Mtl14
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_2/Materials/Mtl14/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_2/Materials/Mtl14/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.310, 0.310, 0.310)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_2/Materials/Mtl15

* **Prim路径 (Prim Path):**/World/agv_2/Materials/Mtl15
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_2/Materials/Mtl15/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_2/Materials/Mtl15/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.263, 0.275, 0.275)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_2/Materials/Mtl16

* **Prim路径 (Prim Path):**/World/agv_2/Materials/Mtl16
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_2/Materials/Mtl16/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_2/Materials/Mtl16/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.698, 0.698, 0.000)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_2/Materials/Mtl17

* **Prim路径 (Prim Path):**/World/agv_2/Materials/Mtl17
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_2/Materials/Mtl17/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_2/Materials/Mtl17/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.000, 0.863, 1.000)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_2/Materials/Mtl3

* **Prim路径 (Prim Path):**/World/agv_2/Materials/Mtl3
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_2/Materials/Mtl3/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_2/Materials/Mtl3/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.431, 0.455, 0.498)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_2/Materials/Mtl35

* **Prim路径 (Prim Path):**/World/agv_2/Materials/Mtl35
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_2/Materials/Mtl35/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_2/Materials/Mtl35/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.792, 0.820, 0.933)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_2/Materials/Mtl36

* **Prim路径 (Prim Path):**/World/agv_2/Materials/Mtl36
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_2/Materials/Mtl36/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_2/Materials/Mtl36/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.667, 0.698, 0.765)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_2/Materials/Mtl37

* **Prim路径 (Prim Path):**/World/agv_2/Materials/Mtl37
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_2/Materials/Mtl37/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_2/Materials/Mtl37/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.098, 0.098, 0.098)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_2/Materials/Mtl3a

* **Prim路径 (Prim Path):**/World/agv_2/Materials/Mtl3a
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_2/Materials/Mtl3a/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_2/Materials/Mtl3a/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.388, 0.369, 0.322)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_2/Materials/Mtl3b

* **Prim路径 (Prim Path):**/World/agv_2/Materials/Mtl3b
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_2/Materials/Mtl3b/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_2/Materials/Mtl3b/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.365, 0.176, 0.012)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0.959234'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'opacity' [float] = '0.273471'
      * 'roughness' [float] = '0.164234'

---

### /World/agv_2/Materials/Mtl5

* **Prim路径 (Prim Path):**/World/agv_2/Materials/Mtl5
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_2/Materials/Mtl5/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_2/Materials/Mtl5/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.396, 0.408, 0.467)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_2/Materials/Mtl7

* **Prim路径 (Prim Path):**/World/agv_2/Materials/Mtl7
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_2/Materials/Mtl7/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_2/Materials/Mtl7/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.376, 0.376, 0.376)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_2/Materials/Mtl8

* **Prim路径 (Prim Path):**/World/agv_2/Materials/Mtl8
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_2/Materials/Mtl8/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_2/Materials/Mtl8/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.173, 0.173, 0.173)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_2/Materials/Mtla

* **Prim路径 (Prim Path):**/World/agv_2/Materials/Mtla
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_2/Materials/Mtla/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_2/Materials/Mtla/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.612, 0.725, 0.745)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_2/Materials/Mtlb1

* **Prim路径 (Prim Path):**/World/agv_2/Materials/Mtlb1
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_2/Materials/Mtlb1/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_2/Materials/Mtlb1/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.949, 0.925, 0.933)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_2/Materials/Stainless_Steel

* **Prim路径 (Prim Path):**/World/agv_2/Materials/Stainless_Steel
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_2/Materials/Stainless_Steel/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_2/Materials/Stainless_Steel/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.292, 0.294, 0.284)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0.431257'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_2/Materials/Metal_Aluminum_Anodized_1

* **Prim路径 (Prim Path):**/World/agv_2/Materials/Metal_Aluminum_Anodized_1
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_2/Materials/Metal_Aluminum_Anodized_1/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_2/Materials/Metal_Aluminum_Anodized_1/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.260, 0.269, 0.282)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0.309883'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0'

---

### /World/agv_2/Materials/Metal_Aluminum_Anodized_2

* **Prim路径 (Prim Path):**/World/agv_2/Materials/Metal_Aluminum_Anodized_2
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_2/Materials/Metal_Aluminum_Anodized_2/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_2/Materials/Metal_Aluminum_Anodized_2/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.792, 0.820, 0.859)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_2/Materials/basic_gray_plastic

* **Prim路径 (Prim Path):**/World/agv_2/Materials/basic_gray_plastic
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_2/Materials/basic_gray_plastic/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_2/Materials/basic_gray_plastic/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0.297745'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0.115685'

---

### /World/agv_2/Materials/texture

* **Prim路径 (Prim Path):**/World/agv_2/Materials/texture
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_2/Materials/texture/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_2/Materials/texture/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.294, 0.294, 0.294)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_3/Materials/ASELSAN_CATS_04

* **Prim路径 (Prim Path):**/World/agv_3/Materials/ASELSAN_CATS_04
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_3/Materials/ASELSAN_CATS_04/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_3/Materials/ASELSAN_CATS_04/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.158, 0.158, 0.158)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_3/Materials/ASELSAN_CATS_04_2

* **Prim路径 (Prim Path):**/World/agv_3/Materials/ASELSAN_CATS_04_2
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_3/Materials/ASELSAN_CATS_04_2/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_3/Materials/ASELSAN_CATS_04_2/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.769, 0.773, 0.749)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_3/Materials/ASELSAN_CATS_13

* **Prim路径 (Prim Path):**/World/agv_3/Materials/ASELSAN_CATS_13
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_3/Materials/ASELSAN_CATS_13/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_3/Materials/ASELSAN_CATS_13/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.706, 0.718, 0.729)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_3/Materials/Color_000

* **Prim路径 (Prim Path):**/World/agv_3/Materials/Color_000
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_3/Materials/Color_000/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_3/Materials/Color_000/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(1.000, 1.000, 1.000)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_3/Materials/Color_A05

* **Prim路径 (Prim Path):**/World/agv_3/Materials/Color_A05
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_3/Materials/Color_A05/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_3/Materials/Color_A05/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(1.000, 0.000, 0.000)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0.959234'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0'

---

### /World/agv_3/Materials/Color_A06

* **Prim路径 (Prim Path):**/World/agv_3/Materials/Color_A06
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_3/Materials/Color_A06/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_3/Materials/Color_A06/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.800, 0.000, 0.000)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_3/Materials/Color_B05

* **Prim路径 (Prim Path):**/World/agv_3/Materials/Color_B05
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_3/Materials/Color_B05/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_3/Materials/Color_B05/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(1.000, 0.247, 0.000)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '1'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0'

---

### /World/agv_3/Materials/Color_E02

* **Prim路径 (Prim Path):**/World/agv_3/Materials/Color_E02
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_3/Materials/Color_E02/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_3/Materials/Color_E02/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(1.000, 1.000, 0.196)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_3/Materials/Color_E05

* **Prim路径 (Prim Path):**/World/agv_3/Materials/Color_E05
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_3/Materials/Color_E05/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_3/Materials/Color_E05/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(1.000, 0.910, 0.000)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0.625455'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0.133891'

---

### /World/agv_3/Materials/Color_F06

* **Prim路径 (Prim Path):**/World/agv_3/Materials/Color_F06
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_3/Materials/Color_F06/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_3/Materials/Color_F06/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.400, 0.800, 0.000)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_3/Materials/Color_G03

* **Prim路径 (Prim Path):**/World/agv_3/Materials/Color_G03
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_3/Materials/Color_G03/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_3/Materials/Color_G03/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.396, 1.000, 0.396)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_3/Materials/Color_M02

* **Prim路径 (Prim Path):**/World/agv_3/Materials/Color_M02
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_3/Materials/Color_M02/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_3/Materials/Color_M02/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.776, 0.776, 0.776)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_3/Materials/Color_M03

* **Prim路径 (Prim Path):**/World/agv_3/Materials/Color_M03
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_3/Materials/Color_M03/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_3/Materials/Color_M03/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.667, 0.667, 0.667)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_3/Materials/Mtl39

* **Prim路径 (Prim Path):**/World/agv_3/Materials/Mtl39
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_3/Materials/Mtl39/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_3/Materials/Mtl39/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.494, 0.494, 0.494)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_3/Materials/Mtl6

* **Prim路径 (Prim Path):**/World/agv_3/Materials/Mtl6
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_3/Materials/Mtl6/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_3/Materials/Mtl6/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f]
        * Connected: '/World/agv_3/Materials/Mtl6/tex_base.outputs:rgb' @ '/World/agv_3/Materials/Mtl6/tex_base'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/Mtl6_baseColor.jpg'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'
    * '/World/agv_3/Materials/Mtl6/tex_base' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/Mtl6_baseColor.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'file' [asset] = '0/Mtl6_baseColor.jpg'
      * 'st' [float2]
        * Connected: '/World/agv_3/Materials/Mtl6/uvset0.outputs:result' @ '/World/agv_3/Materials/Mtl6/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/agv_3/Materials/Mtl6/uvset0' (ID: 'UsdPrimvarReader_float2')
    * Implementation: 'id'

---

### /World/agv_3/Materials/Mtl9

* **Prim路径 (Prim Path):**/World/agv_3/Materials/Mtl9
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_3/Materials/Mtl9/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_3/Materials/Mtl9/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.514, 1.000, 0.000)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_3/Materials/Silver

* **Prim路径 (Prim Path):**/World/agv_3/Materials/Silver
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_3/Materials/Silver/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_3/Materials/Silver/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.753, 0.753, 0.753)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_3/Materials/material

* **Prim路径 (Prim Path):**/World/agv_3/Materials/material
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_3/Materials/material/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_3/Materials/material/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f]
        * Connected: '/World/agv_3/Materials/material/tex_base.outputs:rgb' @ '/World/agv_3/Materials/material/tex_base'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/material_baseColor.jpg'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'
    * '/World/agv_3/Materials/material/tex_base' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/material_baseColor.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'file' [asset] = '0/material_baseColor.jpg'
      * 'st' [float2]
        * Connected: '/World/agv_3/Materials/material/uvset0.outputs:result' @ '/World/agv_3/Materials/material/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/agv_3/Materials/material/uvset0' (ID: 'UsdPrimvarReader_float2')
    * Implementation: 'id'

---

### /World/agv_3/Materials/cash_register_keys

* **Prim路径 (Prim Path):**/World/agv_3/Materials/cash_register_keys
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_3/Materials/cash_register_keys/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_3/Materials/cash_register_keys/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.976, 0.992, 0.973)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_3/Materials/Chris_Shoe_Sole

* **Prim路径 (Prim Path):**/World/agv_3/Materials/Chris_Shoe_Sole
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_3/Materials/Chris_Shoe_Sole/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_3/Materials/Chris_Shoe_Sole/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.155, 0.149, 0.149)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'opacity' [float] = '0.25'
      * 'roughness' [float] = '1'

---

### /World/agv_3/Materials/Color_002

* **Prim路径 (Prim Path):**/World/agv_3/Materials/Color_002
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_3/Materials/Color_002/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_3/Materials/Color_002/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.217, 0.217, 0.217)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0.570837'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0'

---

### /World/agv_3/Materials/Color_005

* **Prim路径 (Prim Path):**/World/agv_3/Materials/Color_005
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_3/Materials/Color_005/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_3/Materials/Color_005/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.130, 0.130, 0.130)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0.710417'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0'

---

### /World/agv_3/Materials/Color_006

* **Prim路径 (Prim Path):**/World/agv_3/Materials/Color_006
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_3/Materials/Color_006/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_3/Materials/Color_006/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0.237059'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0'

---

### /World/agv_3/Materials/Color_008

* **Prim路径 (Prim Path):**/World/agv_3/Materials/Color_008
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_3/Materials/Color_008/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_3/Materials/Color_008/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.118, 0.118, 0.118)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0.941027'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0'

---

### /World/agv_3/Materials/Color_A01

* **Prim路径 (Prim Path):**/World/agv_3/Materials/Color_A01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_3/Materials/Color_A01/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_3/Materials/Color_A01/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(1.000, 0.000, 0.000)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0.965302'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0'

---

### /World/agv_3/Materials/Color_A11

* **Prim路径 (Prim Path):**/World/agv_3/Materials/Color_A11
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_3/Materials/Color_A11/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_3/Materials/Color_A11/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.600, 0.000, 0.000)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_3/Materials/Color_M04

* **Prim路径 (Prim Path):**/World/agv_3/Materials/Color_M04
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_3/Materials/Color_M04/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_3/Materials/Color_M04/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.557, 0.557, 0.557)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_3/Materials/Color_M05

* **Prim路径 (Prim Path):**/World/agv_3/Materials/Color_M05
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_3/Materials/Color_M05/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_3/Materials/Color_M05/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.447, 0.447, 0.447)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_3/Materials/Color_M06

* **Prim路径 (Prim Path):**/World/agv_3/Materials/Color_M06
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_3/Materials/Color_M06/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_3/Materials/Color_M06/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_3/Materials/Color_M07

* **Prim路径 (Prim Path):**/World/agv_3/Materials/Color_M07
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_3/Materials/Color_M07/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_3/Materials/Color_M07/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.227, 0.227, 0.227)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_3/Materials/Color_M09

* **Prim路径 (Prim Path):**/World/agv_3/Materials/Color_M09
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_3/Materials/Color_M09/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_3/Materials/Color_M09/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0.340226'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0.085341'

---

### /World/agv_3/Materials/FCP_Charcoal_v2

* **Prim路径 (Prim Path):**/World/agv_3/Materials/FCP_Charcoal_v2
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_3/Materials/FCP_Charcoal_v2/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_3/Materials/FCP_Charcoal_v2/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.216, 0.216, 0.216)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_3/Materials/FrontColor

* **Prim路径 (Prim Path):**/World/agv_3/Materials/FrontColor
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_3/Materials/FrontColor/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_3/Materials/FrontColor/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.504, 0.504, 0.504)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0.637593'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0.218852'

---

### /World/agv_3/Materials/Light_Blue

* **Prim路径 (Prim Path):**/World/agv_3/Materials/Light_Blue
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_3/Materials/Light_Blue/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_3/Materials/Light_Blue/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.601, 0.601, 0.601)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '1'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0.170303'

---

### /World/agv_3/Materials/M_0011_Seashell

* **Prim路径 (Prim Path):**/World/agv_3/Materials/M_0011_Seashell
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_3/Materials/M_0011_Seashell/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_3/Materials/M_0011_Seashell/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(1.000, 0.961, 0.933)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_3/Materials/M_0131_Silver

* **Prim路径 (Prim Path):**/World/agv_3/Materials/M_0131_Silver
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_3/Materials/M_0131_Silver/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_3/Materials/M_0131_Silver/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.242, 0.242, 0.242)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0.613318'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0'

---

### /World/agv_3/Materials/M_0134_DimGray

* **Prim路径 (Prim Path):**/World/agv_3/Materials/M_0134_DimGray
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_3/Materials/M_0134_DimGray/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_3/Materials/M_0134_DimGray/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.412, 0.412, 0.412)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_3/Materials/M_0135_DarkGray

* **Prim路径 (Prim Path):**/World/agv_3/Materials/M_0135_DarkGray
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_3/Materials/M_0135_DarkGray/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_3/Materials/M_0135_DarkGray/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.318, 0.318, 0.318)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_3/Materials/Metal_Silver

* **Prim路径 (Prim Path):**/World/agv_3/Materials/Metal_Silver
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_3/Materials/Metal_Silver/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_3/Materials/Metal_Silver/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.918, 0.914, 0.933)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_3/Materials/Mtl1

* **Prim路径 (Prim Path):**/World/agv_3/Materials/Mtl1
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_3/Materials/Mtl1/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_3/Materials/Mtl1/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.015, 0.015, 0.015)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0.255265'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_3/Materials/Mtl10

* **Prim路径 (Prim Path):**/World/agv_3/Materials/Mtl10
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_3/Materials/Mtl10/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_3/Materials/Mtl10/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.322, 0.322, 0.322)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_3/Materials/Mtl11

* **Prim路径 (Prim Path):**/World/agv_3/Materials/Mtl11
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_3/Materials/Mtl11/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_3/Materials/Mtl11/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.067, 0.757, 0.329)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_3/Materials/Mtl12

* **Prim路径 (Prim Path):**/World/agv_3/Materials/Mtl12
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_3/Materials/Mtl12/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_3/Materials/Mtl12/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.502, 0.502, 0.502)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_3/Materials/Mtl13

* **Prim路径 (Prim Path):**/World/agv_3/Materials/Mtl13
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_3/Materials/Mtl13/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_3/Materials/Mtl13/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.008, 0.514, 0.816)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_3/Materials/Mtl14

* **Prim路径 (Prim Path):**/World/agv_3/Materials/Mtl14
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_3/Materials/Mtl14/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_3/Materials/Mtl14/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.310, 0.310, 0.310)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_3/Materials/Mtl15

* **Prim路径 (Prim Path):**/World/agv_3/Materials/Mtl15
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_3/Materials/Mtl15/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_3/Materials/Mtl15/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.263, 0.275, 0.275)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_3/Materials/Mtl16

* **Prim路径 (Prim Path):**/World/agv_3/Materials/Mtl16
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_3/Materials/Mtl16/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_3/Materials/Mtl16/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.698, 0.698, 0.000)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_3/Materials/Mtl17

* **Prim路径 (Prim Path):**/World/agv_3/Materials/Mtl17
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_3/Materials/Mtl17/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_3/Materials/Mtl17/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.000, 0.863, 1.000)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_3/Materials/Mtl3

* **Prim路径 (Prim Path):**/World/agv_3/Materials/Mtl3
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_3/Materials/Mtl3/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_3/Materials/Mtl3/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.431, 0.455, 0.498)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_3/Materials/Mtl35

* **Prim路径 (Prim Path):**/World/agv_3/Materials/Mtl35
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_3/Materials/Mtl35/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_3/Materials/Mtl35/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.792, 0.820, 0.933)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_3/Materials/Mtl36

* **Prim路径 (Prim Path):**/World/agv_3/Materials/Mtl36
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_3/Materials/Mtl36/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_3/Materials/Mtl36/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.667, 0.698, 0.765)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_3/Materials/Mtl37

* **Prim路径 (Prim Path):**/World/agv_3/Materials/Mtl37
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_3/Materials/Mtl37/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_3/Materials/Mtl37/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.098, 0.098, 0.098)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_3/Materials/Mtl3a

* **Prim路径 (Prim Path):**/World/agv_3/Materials/Mtl3a
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_3/Materials/Mtl3a/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_3/Materials/Mtl3a/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.388, 0.369, 0.322)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_3/Materials/Mtl3b

* **Prim路径 (Prim Path):**/World/agv_3/Materials/Mtl3b
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_3/Materials/Mtl3b/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_3/Materials/Mtl3b/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.365, 0.176, 0.012)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0.959234'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'opacity' [float] = '0.273471'
      * 'roughness' [float] = '0.164234'

---

### /World/agv_3/Materials/Mtl5

* **Prim路径 (Prim Path):**/World/agv_3/Materials/Mtl5
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_3/Materials/Mtl5/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_3/Materials/Mtl5/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.396, 0.408, 0.467)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_3/Materials/Mtl7

* **Prim路径 (Prim Path):**/World/agv_3/Materials/Mtl7
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_3/Materials/Mtl7/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_3/Materials/Mtl7/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.376, 0.376, 0.376)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_3/Materials/Mtl8

* **Prim路径 (Prim Path):**/World/agv_3/Materials/Mtl8
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_3/Materials/Mtl8/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_3/Materials/Mtl8/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.173, 0.173, 0.173)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_3/Materials/Mtla

* **Prim路径 (Prim Path):**/World/agv_3/Materials/Mtla
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_3/Materials/Mtla/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_3/Materials/Mtla/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.612, 0.725, 0.745)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_3/Materials/Mtlb1

* **Prim路径 (Prim Path):**/World/agv_3/Materials/Mtlb1
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_3/Materials/Mtlb1/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_3/Materials/Mtlb1/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.949, 0.925, 0.933)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_3/Materials/Stainless_Steel

* **Prim路径 (Prim Path):**/World/agv_3/Materials/Stainless_Steel
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_3/Materials/Stainless_Steel/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_3/Materials/Stainless_Steel/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.292, 0.294, 0.284)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0.431257'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_3/Materials/Metal_Aluminum_Anodized_1

* **Prim路径 (Prim Path):**/World/agv_3/Materials/Metal_Aluminum_Anodized_1
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_3/Materials/Metal_Aluminum_Anodized_1/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_3/Materials/Metal_Aluminum_Anodized_1/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.260, 0.269, 0.282)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0.309883'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0'

---

### /World/agv_3/Materials/Metal_Aluminum_Anodized_2

* **Prim路径 (Prim Path):**/World/agv_3/Materials/Metal_Aluminum_Anodized_2
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_3/Materials/Metal_Aluminum_Anodized_2/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_3/Materials/Metal_Aluminum_Anodized_2/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.792, 0.820, 0.859)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_3/Materials/basic_gray_plastic

* **Prim路径 (Prim Path):**/World/agv_3/Materials/basic_gray_plastic
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_3/Materials/basic_gray_plastic/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_3/Materials/basic_gray_plastic/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0.297745'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0.115685'

---

### /World/agv_3/Materials/texture

* **Prim路径 (Prim Path):**/World/agv_3/Materials/texture
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_3/Materials/texture/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_3/Materials/texture/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.294, 0.294, 0.294)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_4/Materials/ASELSAN_CATS_04

* **Prim路径 (Prim Path):**/World/agv_4/Materials/ASELSAN_CATS_04
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_4/Materials/ASELSAN_CATS_04/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_4/Materials/ASELSAN_CATS_04/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.158, 0.158, 0.158)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_4/Materials/ASELSAN_CATS_04_2

* **Prim路径 (Prim Path):**/World/agv_4/Materials/ASELSAN_CATS_04_2
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_4/Materials/ASELSAN_CATS_04_2/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_4/Materials/ASELSAN_CATS_04_2/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.769, 0.773, 0.749)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_4/Materials/ASELSAN_CATS_13

* **Prim路径 (Prim Path):**/World/agv_4/Materials/ASELSAN_CATS_13
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_4/Materials/ASELSAN_CATS_13/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_4/Materials/ASELSAN_CATS_13/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.706, 0.718, 0.729)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_4/Materials/Color_000

* **Prim路径 (Prim Path):**/World/agv_4/Materials/Color_000
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_4/Materials/Color_000/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_4/Materials/Color_000/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(1.000, 1.000, 1.000)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_4/Materials/Color_A05

* **Prim路径 (Prim Path):**/World/agv_4/Materials/Color_A05
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_4/Materials/Color_A05/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_4/Materials/Color_A05/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(1.000, 0.000, 0.000)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0.959234'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0'

---

### /World/agv_4/Materials/Color_A06

* **Prim路径 (Prim Path):**/World/agv_4/Materials/Color_A06
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_4/Materials/Color_A06/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_4/Materials/Color_A06/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.800, 0.000, 0.000)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_4/Materials/Color_B05

* **Prim路径 (Prim Path):**/World/agv_4/Materials/Color_B05
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_4/Materials/Color_B05/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_4/Materials/Color_B05/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(1.000, 0.247, 0.000)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '1'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0'

---

### /World/agv_4/Materials/Color_E02

* **Prim路径 (Prim Path):**/World/agv_4/Materials/Color_E02
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_4/Materials/Color_E02/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_4/Materials/Color_E02/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(1.000, 1.000, 0.196)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_4/Materials/Color_E05

* **Prim路径 (Prim Path):**/World/agv_4/Materials/Color_E05
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_4/Materials/Color_E05/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_4/Materials/Color_E05/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(1.000, 0.910, 0.000)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0.625455'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0.133891'

---

### /World/agv_4/Materials/Color_F06

* **Prim路径 (Prim Path):**/World/agv_4/Materials/Color_F06
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_4/Materials/Color_F06/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_4/Materials/Color_F06/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.400, 0.800, 0.000)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_4/Materials/Color_G03

* **Prim路径 (Prim Path):**/World/agv_4/Materials/Color_G03
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_4/Materials/Color_G03/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_4/Materials/Color_G03/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.396, 1.000, 0.396)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_4/Materials/Color_M02

* **Prim路径 (Prim Path):**/World/agv_4/Materials/Color_M02
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_4/Materials/Color_M02/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_4/Materials/Color_M02/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.776, 0.776, 0.776)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_4/Materials/Color_M03

* **Prim路径 (Prim Path):**/World/agv_4/Materials/Color_M03
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_4/Materials/Color_M03/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_4/Materials/Color_M03/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.667, 0.667, 0.667)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_4/Materials/Mtl39

* **Prim路径 (Prim Path):**/World/agv_4/Materials/Mtl39
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_4/Materials/Mtl39/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_4/Materials/Mtl39/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.494, 0.494, 0.494)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_4/Materials/Mtl6

* **Prim路径 (Prim Path):**/World/agv_4/Materials/Mtl6
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_4/Materials/Mtl6/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_4/Materials/Mtl6/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f]
        * Connected: '/World/agv_4/Materials/Mtl6/tex_base.outputs:rgb' @ '/World/agv_4/Materials/Mtl6/tex_base'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/Mtl6_baseColor.jpg'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'
    * '/World/agv_4/Materials/Mtl6/tex_base' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/Mtl6_baseColor.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'file' [asset] = '0/Mtl6_baseColor.jpg'
      * 'st' [float2]
        * Connected: '/World/agv_4/Materials/Mtl6/uvset0.outputs:result' @ '/World/agv_4/Materials/Mtl6/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/agv_4/Materials/Mtl6/uvset0' (ID: 'UsdPrimvarReader_float2')
    * Implementation: 'id'

---

### /World/agv_4/Materials/Mtl9

* **Prim路径 (Prim Path):**/World/agv_4/Materials/Mtl9
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_4/Materials/Mtl9/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_4/Materials/Mtl9/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.514, 1.000, 0.000)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_4/Materials/Silver

* **Prim路径 (Prim Path):**/World/agv_4/Materials/Silver
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_4/Materials/Silver/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_4/Materials/Silver/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.753, 0.753, 0.753)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_4/Materials/material

* **Prim路径 (Prim Path):**/World/agv_4/Materials/material
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_4/Materials/material/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_4/Materials/material/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f]
        * Connected: '/World/agv_4/Materials/material/tex_base.outputs:rgb' @ '/World/agv_4/Materials/material/tex_base'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/material_baseColor.jpg'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'
    * '/World/agv_4/Materials/material/tex_base' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/material_baseColor.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'file' [asset] = '0/material_baseColor.jpg'
      * 'st' [float2]
        * Connected: '/World/agv_4/Materials/material/uvset0.outputs:result' @ '/World/agv_4/Materials/material/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/agv_4/Materials/material/uvset0' (ID: 'UsdPrimvarReader_float2')
    * Implementation: 'id'

---

### /World/agv_4/Materials/cash_register_keys

* **Prim路径 (Prim Path):**/World/agv_4/Materials/cash_register_keys
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_4/Materials/cash_register_keys/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_4/Materials/cash_register_keys/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.976, 0.992, 0.973)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_4/Materials/Chris_Shoe_Sole

* **Prim路径 (Prim Path):**/World/agv_4/Materials/Chris_Shoe_Sole
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_4/Materials/Chris_Shoe_Sole/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_4/Materials/Chris_Shoe_Sole/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.155, 0.149, 0.149)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'opacity' [float] = '0.25'
      * 'roughness' [float] = '1'

---

### /World/agv_4/Materials/Color_002

* **Prim路径 (Prim Path):**/World/agv_4/Materials/Color_002
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_4/Materials/Color_002/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_4/Materials/Color_002/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.217, 0.217, 0.217)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0.570837'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0'

---

### /World/agv_4/Materials/Color_005

* **Prim路径 (Prim Path):**/World/agv_4/Materials/Color_005
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_4/Materials/Color_005/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_4/Materials/Color_005/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.130, 0.130, 0.130)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0.710417'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0'

---

### /World/agv_4/Materials/Color_006

* **Prim路径 (Prim Path):**/World/agv_4/Materials/Color_006
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_4/Materials/Color_006/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_4/Materials/Color_006/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0.237059'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0'

---

### /World/agv_4/Materials/Color_008

* **Prim路径 (Prim Path):**/World/agv_4/Materials/Color_008
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_4/Materials/Color_008/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_4/Materials/Color_008/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.118, 0.118, 0.118)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0.941027'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0'

---

### /World/agv_4/Materials/Color_A01

* **Prim路径 (Prim Path):**/World/agv_4/Materials/Color_A01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_4/Materials/Color_A01/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_4/Materials/Color_A01/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(1.000, 0.000, 0.000)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0.965302'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0'

---

### /World/agv_4/Materials/Color_A11

* **Prim路径 (Prim Path):**/World/agv_4/Materials/Color_A11
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_4/Materials/Color_A11/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_4/Materials/Color_A11/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.600, 0.000, 0.000)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_4/Materials/Color_M04

* **Prim路径 (Prim Path):**/World/agv_4/Materials/Color_M04
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_4/Materials/Color_M04/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_4/Materials/Color_M04/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.557, 0.557, 0.557)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_4/Materials/Color_M05

* **Prim路径 (Prim Path):**/World/agv_4/Materials/Color_M05
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_4/Materials/Color_M05/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_4/Materials/Color_M05/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.447, 0.447, 0.447)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_4/Materials/Color_M06

* **Prim路径 (Prim Path):**/World/agv_4/Materials/Color_M06
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_4/Materials/Color_M06/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_4/Materials/Color_M06/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_4/Materials/Color_M07

* **Prim路径 (Prim Path):**/World/agv_4/Materials/Color_M07
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_4/Materials/Color_M07/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_4/Materials/Color_M07/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.227, 0.227, 0.227)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_4/Materials/Color_M09

* **Prim路径 (Prim Path):**/World/agv_4/Materials/Color_M09
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_4/Materials/Color_M09/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_4/Materials/Color_M09/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0.340226'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0.085341'

---

### /World/agv_4/Materials/FCP_Charcoal_v2

* **Prim路径 (Prim Path):**/World/agv_4/Materials/FCP_Charcoal_v2
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_4/Materials/FCP_Charcoal_v2/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_4/Materials/FCP_Charcoal_v2/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.216, 0.216, 0.216)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_4/Materials/FrontColor

* **Prim路径 (Prim Path):**/World/agv_4/Materials/FrontColor
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_4/Materials/FrontColor/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_4/Materials/FrontColor/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.504, 0.504, 0.504)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0.637593'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0.218852'

---

### /World/agv_4/Materials/Light_Blue

* **Prim路径 (Prim Path):**/World/agv_4/Materials/Light_Blue
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_4/Materials/Light_Blue/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_4/Materials/Light_Blue/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.601, 0.601, 0.601)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '1'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0.170303'

---

### /World/agv_4/Materials/M_0011_Seashell

* **Prim路径 (Prim Path):**/World/agv_4/Materials/M_0011_Seashell
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_4/Materials/M_0011_Seashell/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_4/Materials/M_0011_Seashell/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(1.000, 0.961, 0.933)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_4/Materials/M_0131_Silver

* **Prim路径 (Prim Path):**/World/agv_4/Materials/M_0131_Silver
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_4/Materials/M_0131_Silver/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_4/Materials/M_0131_Silver/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.242, 0.242, 0.242)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0.613318'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0'

---

### /World/agv_4/Materials/M_0134_DimGray

* **Prim路径 (Prim Path):**/World/agv_4/Materials/M_0134_DimGray
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_4/Materials/M_0134_DimGray/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_4/Materials/M_0134_DimGray/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.412, 0.412, 0.412)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_4/Materials/M_0135_DarkGray

* **Prim路径 (Prim Path):**/World/agv_4/Materials/M_0135_DarkGray
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_4/Materials/M_0135_DarkGray/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_4/Materials/M_0135_DarkGray/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.318, 0.318, 0.318)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_4/Materials/Metal_Silver

* **Prim路径 (Prim Path):**/World/agv_4/Materials/Metal_Silver
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_4/Materials/Metal_Silver/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_4/Materials/Metal_Silver/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.918, 0.914, 0.933)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_4/Materials/Mtl1

* **Prim路径 (Prim Path):**/World/agv_4/Materials/Mtl1
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_4/Materials/Mtl1/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_4/Materials/Mtl1/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.015, 0.015, 0.015)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0.255265'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_4/Materials/Mtl10

* **Prim路径 (Prim Path):**/World/agv_4/Materials/Mtl10
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_4/Materials/Mtl10/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_4/Materials/Mtl10/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.322, 0.322, 0.322)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_4/Materials/Mtl11

* **Prim路径 (Prim Path):**/World/agv_4/Materials/Mtl11
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_4/Materials/Mtl11/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_4/Materials/Mtl11/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.067, 0.757, 0.329)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_4/Materials/Mtl12

* **Prim路径 (Prim Path):**/World/agv_4/Materials/Mtl12
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_4/Materials/Mtl12/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_4/Materials/Mtl12/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.502, 0.502, 0.502)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_4/Materials/Mtl13

* **Prim路径 (Prim Path):**/World/agv_4/Materials/Mtl13
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_4/Materials/Mtl13/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_4/Materials/Mtl13/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.008, 0.514, 0.816)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_4/Materials/Mtl14

* **Prim路径 (Prim Path):**/World/agv_4/Materials/Mtl14
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_4/Materials/Mtl14/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_4/Materials/Mtl14/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.310, 0.310, 0.310)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_4/Materials/Mtl15

* **Prim路径 (Prim Path):**/World/agv_4/Materials/Mtl15
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_4/Materials/Mtl15/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_4/Materials/Mtl15/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.263, 0.275, 0.275)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_4/Materials/Mtl16

* **Prim路径 (Prim Path):**/World/agv_4/Materials/Mtl16
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_4/Materials/Mtl16/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_4/Materials/Mtl16/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.698, 0.698, 0.000)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_4/Materials/Mtl17

* **Prim路径 (Prim Path):**/World/agv_4/Materials/Mtl17
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_4/Materials/Mtl17/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_4/Materials/Mtl17/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.000, 0.863, 1.000)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_4/Materials/Mtl3

* **Prim路径 (Prim Path):**/World/agv_4/Materials/Mtl3
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_4/Materials/Mtl3/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_4/Materials/Mtl3/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.431, 0.455, 0.498)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_4/Materials/Mtl35

* **Prim路径 (Prim Path):**/World/agv_4/Materials/Mtl35
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_4/Materials/Mtl35/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_4/Materials/Mtl35/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.792, 0.820, 0.933)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_4/Materials/Mtl36

* **Prim路径 (Prim Path):**/World/agv_4/Materials/Mtl36
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_4/Materials/Mtl36/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_4/Materials/Mtl36/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.667, 0.698, 0.765)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_4/Materials/Mtl37

* **Prim路径 (Prim Path):**/World/agv_4/Materials/Mtl37
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_4/Materials/Mtl37/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_4/Materials/Mtl37/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.098, 0.098, 0.098)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_4/Materials/Mtl3a

* **Prim路径 (Prim Path):**/World/agv_4/Materials/Mtl3a
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_4/Materials/Mtl3a/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_4/Materials/Mtl3a/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.388, 0.369, 0.322)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_4/Materials/Mtl3b

* **Prim路径 (Prim Path):**/World/agv_4/Materials/Mtl3b
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_4/Materials/Mtl3b/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_4/Materials/Mtl3b/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.365, 0.176, 0.012)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0.959234'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'opacity' [float] = '0.273471'
      * 'roughness' [float] = '0.164234'

---

### /World/agv_4/Materials/Mtl5

* **Prim路径 (Prim Path):**/World/agv_4/Materials/Mtl5
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_4/Materials/Mtl5/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_4/Materials/Mtl5/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.396, 0.408, 0.467)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_4/Materials/Mtl7

* **Prim路径 (Prim Path):**/World/agv_4/Materials/Mtl7
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_4/Materials/Mtl7/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_4/Materials/Mtl7/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.376, 0.376, 0.376)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_4/Materials/Mtl8

* **Prim路径 (Prim Path):**/World/agv_4/Materials/Mtl8
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_4/Materials/Mtl8/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_4/Materials/Mtl8/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.173, 0.173, 0.173)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_4/Materials/Mtla

* **Prim路径 (Prim Path):**/World/agv_4/Materials/Mtla
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_4/Materials/Mtla/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_4/Materials/Mtla/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.612, 0.725, 0.745)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_4/Materials/Mtlb1

* **Prim路径 (Prim Path):**/World/agv_4/Materials/Mtlb1
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_4/Materials/Mtlb1/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_4/Materials/Mtlb1/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.949, 0.925, 0.933)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_4/Materials/Stainless_Steel

* **Prim路径 (Prim Path):**/World/agv_4/Materials/Stainless_Steel
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_4/Materials/Stainless_Steel/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_4/Materials/Stainless_Steel/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.292, 0.294, 0.284)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0.431257'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_4/Materials/Metal_Aluminum_Anodized_1

* **Prim路径 (Prim Path):**/World/agv_4/Materials/Metal_Aluminum_Anodized_1
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_4/Materials/Metal_Aluminum_Anodized_1/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_4/Materials/Metal_Aluminum_Anodized_1/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.260, 0.269, 0.282)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0.309883'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0'

---

### /World/agv_4/Materials/Metal_Aluminum_Anodized_2

* **Prim路径 (Prim Path):**/World/agv_4/Materials/Metal_Aluminum_Anodized_2
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_4/Materials/Metal_Aluminum_Anodized_2/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_4/Materials/Metal_Aluminum_Anodized_2/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.792, 0.820, 0.859)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_4/Materials/basic_gray_plastic

* **Prim路径 (Prim Path):**/World/agv_4/Materials/basic_gray_plastic
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_4/Materials/basic_gray_plastic/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_4/Materials/basic_gray_plastic/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0.297745'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0.115685'

---

### /World/agv_4/Materials/texture

* **Prim路径 (Prim Path):**/World/agv_4/Materials/texture
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_4/Materials/texture/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_4/Materials/texture/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.294, 0.294, 0.294)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_5/Materials/ASELSAN_CATS_04

* **Prim路径 (Prim Path):**/World/agv_5/Materials/ASELSAN_CATS_04
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_5/Materials/ASELSAN_CATS_04/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_5/Materials/ASELSAN_CATS_04/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.158, 0.158, 0.158)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_5/Materials/ASELSAN_CATS_04_2

* **Prim路径 (Prim Path):**/World/agv_5/Materials/ASELSAN_CATS_04_2
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_5/Materials/ASELSAN_CATS_04_2/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_5/Materials/ASELSAN_CATS_04_2/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.769, 0.773, 0.749)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_5/Materials/ASELSAN_CATS_13

* **Prim路径 (Prim Path):**/World/agv_5/Materials/ASELSAN_CATS_13
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_5/Materials/ASELSAN_CATS_13/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_5/Materials/ASELSAN_CATS_13/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.706, 0.718, 0.729)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_5/Materials/Color_000

* **Prim路径 (Prim Path):**/World/agv_5/Materials/Color_000
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_5/Materials/Color_000/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_5/Materials/Color_000/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(1.000, 1.000, 1.000)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_5/Materials/Color_A05

* **Prim路径 (Prim Path):**/World/agv_5/Materials/Color_A05
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_5/Materials/Color_A05/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_5/Materials/Color_A05/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(1.000, 0.000, 0.000)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0.959234'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0'

---

### /World/agv_5/Materials/Color_A06

* **Prim路径 (Prim Path):**/World/agv_5/Materials/Color_A06
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_5/Materials/Color_A06/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_5/Materials/Color_A06/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.800, 0.000, 0.000)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_5/Materials/Color_B05

* **Prim路径 (Prim Path):**/World/agv_5/Materials/Color_B05
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_5/Materials/Color_B05/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_5/Materials/Color_B05/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(1.000, 0.247, 0.000)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '1'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0'

---

### /World/agv_5/Materials/Color_E02

* **Prim路径 (Prim Path):**/World/agv_5/Materials/Color_E02
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_5/Materials/Color_E02/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_5/Materials/Color_E02/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(1.000, 1.000, 0.196)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_5/Materials/Color_E05

* **Prim路径 (Prim Path):**/World/agv_5/Materials/Color_E05
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_5/Materials/Color_E05/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_5/Materials/Color_E05/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(1.000, 0.910, 0.000)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0.625455'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0.133891'

---

### /World/agv_5/Materials/Color_F06

* **Prim路径 (Prim Path):**/World/agv_5/Materials/Color_F06
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_5/Materials/Color_F06/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_5/Materials/Color_F06/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.400, 0.800, 0.000)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_5/Materials/Color_G03

* **Prim路径 (Prim Path):**/World/agv_5/Materials/Color_G03
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_5/Materials/Color_G03/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_5/Materials/Color_G03/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.396, 1.000, 0.396)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_5/Materials/Color_M02

* **Prim路径 (Prim Path):**/World/agv_5/Materials/Color_M02
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_5/Materials/Color_M02/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_5/Materials/Color_M02/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.776, 0.776, 0.776)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_5/Materials/Color_M03

* **Prim路径 (Prim Path):**/World/agv_5/Materials/Color_M03
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_5/Materials/Color_M03/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_5/Materials/Color_M03/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.667, 0.667, 0.667)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_5/Materials/Mtl39

* **Prim路径 (Prim Path):**/World/agv_5/Materials/Mtl39
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_5/Materials/Mtl39/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_5/Materials/Mtl39/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.494, 0.494, 0.494)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_5/Materials/Mtl6

* **Prim路径 (Prim Path):**/World/agv_5/Materials/Mtl6
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_5/Materials/Mtl6/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_5/Materials/Mtl6/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f]
        * Connected: '/World/agv_5/Materials/Mtl6/tex_base.outputs:rgb' @ '/World/agv_5/Materials/Mtl6/tex_base'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/Mtl6_baseColor.jpg'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'
    * '/World/agv_5/Materials/Mtl6/tex_base' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/Mtl6_baseColor.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'file' [asset] = '0/Mtl6_baseColor.jpg'
      * 'st' [float2]
        * Connected: '/World/agv_5/Materials/Mtl6/uvset0.outputs:result' @ '/World/agv_5/Materials/Mtl6/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/agv_5/Materials/Mtl6/uvset0' (ID: 'UsdPrimvarReader_float2')
    * Implementation: 'id'

---

### /World/agv_5/Materials/Mtl9

* **Prim路径 (Prim Path):**/World/agv_5/Materials/Mtl9
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_5/Materials/Mtl9/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_5/Materials/Mtl9/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.514, 1.000, 0.000)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_5/Materials/Silver

* **Prim路径 (Prim Path):**/World/agv_5/Materials/Silver
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_5/Materials/Silver/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_5/Materials/Silver/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.753, 0.753, 0.753)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_5/Materials/material

* **Prim路径 (Prim Path):**/World/agv_5/Materials/material
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_5/Materials/material/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_5/Materials/material/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f]
        * Connected: '/World/agv_5/Materials/material/tex_base.outputs:rgb' @ '/World/agv_5/Materials/material/tex_base'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/material_baseColor.jpg'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'
    * '/World/agv_5/Materials/material/tex_base' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/material_baseColor.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'file' [asset] = '0/material_baseColor.jpg'
      * 'st' [float2]
        * Connected: '/World/agv_5/Materials/material/uvset0.outputs:result' @ '/World/agv_5/Materials/material/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/agv_5/Materials/material/uvset0' (ID: 'UsdPrimvarReader_float2')
    * Implementation: 'id'

---

### /World/agv_5/Materials/cash_register_keys

* **Prim路径 (Prim Path):**/World/agv_5/Materials/cash_register_keys
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_5/Materials/cash_register_keys/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_5/Materials/cash_register_keys/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.976, 0.992, 0.973)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_5/Materials/Chris_Shoe_Sole

* **Prim路径 (Prim Path):**/World/agv_5/Materials/Chris_Shoe_Sole
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_5/Materials/Chris_Shoe_Sole/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_5/Materials/Chris_Shoe_Sole/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.155, 0.149, 0.149)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'opacity' [float] = '0.25'
      * 'roughness' [float] = '1'

---

### /World/agv_5/Materials/Color_002

* **Prim路径 (Prim Path):**/World/agv_5/Materials/Color_002
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_5/Materials/Color_002/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_5/Materials/Color_002/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.217, 0.217, 0.217)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0.570837'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0'

---

### /World/agv_5/Materials/Color_005

* **Prim路径 (Prim Path):**/World/agv_5/Materials/Color_005
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_5/Materials/Color_005/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_5/Materials/Color_005/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.130, 0.130, 0.130)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0.710417'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0'

---

### /World/agv_5/Materials/Color_006

* **Prim路径 (Prim Path):**/World/agv_5/Materials/Color_006
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_5/Materials/Color_006/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_5/Materials/Color_006/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0.237059'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0'

---

### /World/agv_5/Materials/Color_008

* **Prim路径 (Prim Path):**/World/agv_5/Materials/Color_008
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_5/Materials/Color_008/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_5/Materials/Color_008/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.118, 0.118, 0.118)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0.941027'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0'

---

### /World/agv_5/Materials/Color_A01

* **Prim路径 (Prim Path):**/World/agv_5/Materials/Color_A01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_5/Materials/Color_A01/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_5/Materials/Color_A01/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(1.000, 0.000, 0.000)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0.965302'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0'

---

### /World/agv_5/Materials/Color_A11

* **Prim路径 (Prim Path):**/World/agv_5/Materials/Color_A11
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_5/Materials/Color_A11/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_5/Materials/Color_A11/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.600, 0.000, 0.000)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_5/Materials/Color_M04

* **Prim路径 (Prim Path):**/World/agv_5/Materials/Color_M04
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_5/Materials/Color_M04/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_5/Materials/Color_M04/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.557, 0.557, 0.557)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_5/Materials/Color_M05

* **Prim路径 (Prim Path):**/World/agv_5/Materials/Color_M05
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_5/Materials/Color_M05/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_5/Materials/Color_M05/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.447, 0.447, 0.447)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_5/Materials/Color_M06

* **Prim路径 (Prim Path):**/World/agv_5/Materials/Color_M06
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_5/Materials/Color_M06/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_5/Materials/Color_M06/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_5/Materials/Color_M07

* **Prim路径 (Prim Path):**/World/agv_5/Materials/Color_M07
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_5/Materials/Color_M07/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_5/Materials/Color_M07/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.227, 0.227, 0.227)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_5/Materials/Color_M09

* **Prim路径 (Prim Path):**/World/agv_5/Materials/Color_M09
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_5/Materials/Color_M09/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_5/Materials/Color_M09/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0.340226'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0.085341'

---

### /World/agv_5/Materials/FCP_Charcoal_v2

* **Prim路径 (Prim Path):**/World/agv_5/Materials/FCP_Charcoal_v2
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_5/Materials/FCP_Charcoal_v2/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_5/Materials/FCP_Charcoal_v2/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.216, 0.216, 0.216)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_5/Materials/FrontColor

* **Prim路径 (Prim Path):**/World/agv_5/Materials/FrontColor
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_5/Materials/FrontColor/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_5/Materials/FrontColor/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.504, 0.504, 0.504)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0.637593'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0.218852'

---

### /World/agv_5/Materials/Light_Blue

* **Prim路径 (Prim Path):**/World/agv_5/Materials/Light_Blue
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_5/Materials/Light_Blue/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_5/Materials/Light_Blue/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.601, 0.601, 0.601)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '1'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0.170303'

---

### /World/agv_5/Materials/M_0011_Seashell

* **Prim路径 (Prim Path):**/World/agv_5/Materials/M_0011_Seashell
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_5/Materials/M_0011_Seashell/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_5/Materials/M_0011_Seashell/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(1.000, 0.961, 0.933)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_5/Materials/M_0131_Silver

* **Prim路径 (Prim Path):**/World/agv_5/Materials/M_0131_Silver
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_5/Materials/M_0131_Silver/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_5/Materials/M_0131_Silver/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.242, 0.242, 0.242)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0.613318'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0'

---

### /World/agv_5/Materials/M_0134_DimGray

* **Prim路径 (Prim Path):**/World/agv_5/Materials/M_0134_DimGray
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_5/Materials/M_0134_DimGray/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_5/Materials/M_0134_DimGray/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.412, 0.412, 0.412)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_5/Materials/M_0135_DarkGray

* **Prim路径 (Prim Path):**/World/agv_5/Materials/M_0135_DarkGray
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_5/Materials/M_0135_DarkGray/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_5/Materials/M_0135_DarkGray/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.318, 0.318, 0.318)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_5/Materials/Metal_Silver

* **Prim路径 (Prim Path):**/World/agv_5/Materials/Metal_Silver
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_5/Materials/Metal_Silver/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_5/Materials/Metal_Silver/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.918, 0.914, 0.933)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_5/Materials/Mtl1

* **Prim路径 (Prim Path):**/World/agv_5/Materials/Mtl1
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_5/Materials/Mtl1/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_5/Materials/Mtl1/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.015, 0.015, 0.015)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0.255265'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_5/Materials/Mtl10

* **Prim路径 (Prim Path):**/World/agv_5/Materials/Mtl10
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_5/Materials/Mtl10/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_5/Materials/Mtl10/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.322, 0.322, 0.322)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_5/Materials/Mtl11

* **Prim路径 (Prim Path):**/World/agv_5/Materials/Mtl11
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_5/Materials/Mtl11/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_5/Materials/Mtl11/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.067, 0.757, 0.329)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_5/Materials/Mtl12

* **Prim路径 (Prim Path):**/World/agv_5/Materials/Mtl12
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_5/Materials/Mtl12/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_5/Materials/Mtl12/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.502, 0.502, 0.502)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_5/Materials/Mtl13

* **Prim路径 (Prim Path):**/World/agv_5/Materials/Mtl13
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_5/Materials/Mtl13/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_5/Materials/Mtl13/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.008, 0.514, 0.816)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_5/Materials/Mtl14

* **Prim路径 (Prim Path):**/World/agv_5/Materials/Mtl14
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_5/Materials/Mtl14/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_5/Materials/Mtl14/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.310, 0.310, 0.310)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_5/Materials/Mtl15

* **Prim路径 (Prim Path):**/World/agv_5/Materials/Mtl15
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_5/Materials/Mtl15/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_5/Materials/Mtl15/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.263, 0.275, 0.275)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_5/Materials/Mtl16

* **Prim路径 (Prim Path):**/World/agv_5/Materials/Mtl16
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_5/Materials/Mtl16/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_5/Materials/Mtl16/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.698, 0.698, 0.000)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_5/Materials/Mtl17

* **Prim路径 (Prim Path):**/World/agv_5/Materials/Mtl17
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_5/Materials/Mtl17/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_5/Materials/Mtl17/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.000, 0.863, 1.000)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_5/Materials/Mtl3

* **Prim路径 (Prim Path):**/World/agv_5/Materials/Mtl3
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_5/Materials/Mtl3/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_5/Materials/Mtl3/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.431, 0.455, 0.498)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_5/Materials/Mtl35

* **Prim路径 (Prim Path):**/World/agv_5/Materials/Mtl35
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_5/Materials/Mtl35/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_5/Materials/Mtl35/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.792, 0.820, 0.933)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_5/Materials/Mtl36

* **Prim路径 (Prim Path):**/World/agv_5/Materials/Mtl36
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_5/Materials/Mtl36/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_5/Materials/Mtl36/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.667, 0.698, 0.765)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_5/Materials/Mtl37

* **Prim路径 (Prim Path):**/World/agv_5/Materials/Mtl37
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_5/Materials/Mtl37/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_5/Materials/Mtl37/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.098, 0.098, 0.098)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_5/Materials/Mtl3a

* **Prim路径 (Prim Path):**/World/agv_5/Materials/Mtl3a
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_5/Materials/Mtl3a/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_5/Materials/Mtl3a/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.388, 0.369, 0.322)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_5/Materials/Mtl3b

* **Prim路径 (Prim Path):**/World/agv_5/Materials/Mtl3b
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_5/Materials/Mtl3b/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_5/Materials/Mtl3b/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.365, 0.176, 0.012)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0.959234'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'opacity' [float] = '0.273471'
      * 'roughness' [float] = '0.164234'

---

### /World/agv_5/Materials/Mtl5

* **Prim路径 (Prim Path):**/World/agv_5/Materials/Mtl5
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_5/Materials/Mtl5/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_5/Materials/Mtl5/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.396, 0.408, 0.467)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_5/Materials/Mtl7

* **Prim路径 (Prim Path):**/World/agv_5/Materials/Mtl7
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_5/Materials/Mtl7/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_5/Materials/Mtl7/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.376, 0.376, 0.376)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_5/Materials/Mtl8

* **Prim路径 (Prim Path):**/World/agv_5/Materials/Mtl8
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_5/Materials/Mtl8/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_5/Materials/Mtl8/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.173, 0.173, 0.173)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_5/Materials/Mtla

* **Prim路径 (Prim Path):**/World/agv_5/Materials/Mtla
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_5/Materials/Mtla/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_5/Materials/Mtla/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.612, 0.725, 0.745)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_5/Materials/Mtlb1

* **Prim路径 (Prim Path):**/World/agv_5/Materials/Mtlb1
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_5/Materials/Mtlb1/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_5/Materials/Mtlb1/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.949, 0.925, 0.933)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_5/Materials/Stainless_Steel

* **Prim路径 (Prim Path):**/World/agv_5/Materials/Stainless_Steel
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_5/Materials/Stainless_Steel/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_5/Materials/Stainless_Steel/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.292, 0.294, 0.284)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0.431257'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_5/Materials/Metal_Aluminum_Anodized_1

* **Prim路径 (Prim Path):**/World/agv_5/Materials/Metal_Aluminum_Anodized_1
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_5/Materials/Metal_Aluminum_Anodized_1/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_5/Materials/Metal_Aluminum_Anodized_1/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.260, 0.269, 0.282)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0.309883'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0'

---

### /World/agv_5/Materials/Metal_Aluminum_Anodized_2

* **Prim路径 (Prim Path):**/World/agv_5/Materials/Metal_Aluminum_Anodized_2
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_5/Materials/Metal_Aluminum_Anodized_2/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_5/Materials/Metal_Aluminum_Anodized_2/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.792, 0.820, 0.859)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_5/Materials/basic_gray_plastic

* **Prim路径 (Prim Path):**/World/agv_5/Materials/basic_gray_plastic
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_5/Materials/basic_gray_plastic/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_5/Materials/basic_gray_plastic/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0.297745'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0.115685'

---

### /World/agv_5/Materials/texture

* **Prim路径 (Prim Path):**/World/agv_5/Materials/texture
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_5/Materials/texture/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_5/Materials/texture/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.294, 0.294, 0.294)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_6/Materials/ASELSAN_CATS_04

* **Prim路径 (Prim Path):**/World/agv_6/Materials/ASELSAN_CATS_04
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_6/Materials/ASELSAN_CATS_04/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_6/Materials/ASELSAN_CATS_04/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.158, 0.158, 0.158)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_6/Materials/ASELSAN_CATS_04_2

* **Prim路径 (Prim Path):**/World/agv_6/Materials/ASELSAN_CATS_04_2
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_6/Materials/ASELSAN_CATS_04_2/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_6/Materials/ASELSAN_CATS_04_2/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.769, 0.773, 0.749)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_6/Materials/ASELSAN_CATS_13

* **Prim路径 (Prim Path):**/World/agv_6/Materials/ASELSAN_CATS_13
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_6/Materials/ASELSAN_CATS_13/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_6/Materials/ASELSAN_CATS_13/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.706, 0.718, 0.729)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_6/Materials/Color_000

* **Prim路径 (Prim Path):**/World/agv_6/Materials/Color_000
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_6/Materials/Color_000/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_6/Materials/Color_000/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(1.000, 1.000, 1.000)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_6/Materials/Color_A05

* **Prim路径 (Prim Path):**/World/agv_6/Materials/Color_A05
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_6/Materials/Color_A05/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_6/Materials/Color_A05/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(1.000, 0.000, 0.000)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0.959234'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0'

---

### /World/agv_6/Materials/Color_A06

* **Prim路径 (Prim Path):**/World/agv_6/Materials/Color_A06
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_6/Materials/Color_A06/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_6/Materials/Color_A06/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.800, 0.000, 0.000)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_6/Materials/Color_B05

* **Prim路径 (Prim Path):**/World/agv_6/Materials/Color_B05
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_6/Materials/Color_B05/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_6/Materials/Color_B05/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(1.000, 0.247, 0.000)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '1'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0'

---

### /World/agv_6/Materials/Color_E02

* **Prim路径 (Prim Path):**/World/agv_6/Materials/Color_E02
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_6/Materials/Color_E02/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_6/Materials/Color_E02/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(1.000, 1.000, 0.196)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_6/Materials/Color_E05

* **Prim路径 (Prim Path):**/World/agv_6/Materials/Color_E05
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_6/Materials/Color_E05/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_6/Materials/Color_E05/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(1.000, 0.910, 0.000)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0.625455'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0.133891'

---

### /World/agv_6/Materials/Color_F06

* **Prim路径 (Prim Path):**/World/agv_6/Materials/Color_F06
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_6/Materials/Color_F06/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_6/Materials/Color_F06/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.400, 0.800, 0.000)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_6/Materials/Color_G03

* **Prim路径 (Prim Path):**/World/agv_6/Materials/Color_G03
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_6/Materials/Color_G03/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_6/Materials/Color_G03/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.396, 1.000, 0.396)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_6/Materials/Color_M02

* **Prim路径 (Prim Path):**/World/agv_6/Materials/Color_M02
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_6/Materials/Color_M02/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_6/Materials/Color_M02/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.776, 0.776, 0.776)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_6/Materials/Color_M03

* **Prim路径 (Prim Path):**/World/agv_6/Materials/Color_M03
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_6/Materials/Color_M03/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_6/Materials/Color_M03/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.667, 0.667, 0.667)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_6/Materials/Mtl39

* **Prim路径 (Prim Path):**/World/agv_6/Materials/Mtl39
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_6/Materials/Mtl39/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_6/Materials/Mtl39/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.494, 0.494, 0.494)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_6/Materials/Mtl6

* **Prim路径 (Prim Path):**/World/agv_6/Materials/Mtl6
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_6/Materials/Mtl6/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_6/Materials/Mtl6/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f]
        * Connected: '/World/agv_6/Materials/Mtl6/tex_base.outputs:rgb' @ '/World/agv_6/Materials/Mtl6/tex_base'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/Mtl6_baseColor.jpg'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'
    * '/World/agv_6/Materials/Mtl6/tex_base' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/Mtl6_baseColor.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'file' [asset] = '0/Mtl6_baseColor.jpg'
      * 'st' [float2]
        * Connected: '/World/agv_6/Materials/Mtl6/uvset0.outputs:result' @ '/World/agv_6/Materials/Mtl6/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/agv_6/Materials/Mtl6/uvset0' (ID: 'UsdPrimvarReader_float2')
    * Implementation: 'id'

---

### /World/agv_6/Materials/Mtl9

* **Prim路径 (Prim Path):**/World/agv_6/Materials/Mtl9
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_6/Materials/Mtl9/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_6/Materials/Mtl9/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.514, 1.000, 0.000)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_6/Materials/Silver

* **Prim路径 (Prim Path):**/World/agv_6/Materials/Silver
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_6/Materials/Silver/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_6/Materials/Silver/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.753, 0.753, 0.753)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_6/Materials/material

* **Prim路径 (Prim Path):**/World/agv_6/Materials/material
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_6/Materials/material/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_6/Materials/material/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f]
        * Connected: '/World/agv_6/Materials/material/tex_base.outputs:rgb' @ '/World/agv_6/Materials/material/tex_base'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/material_baseColor.jpg'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'
    * '/World/agv_6/Materials/material/tex_base' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/material_baseColor.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'file' [asset] = '0/material_baseColor.jpg'
      * 'st' [float2]
        * Connected: '/World/agv_6/Materials/material/uvset0.outputs:result' @ '/World/agv_6/Materials/material/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/agv_6/Materials/material/uvset0' (ID: 'UsdPrimvarReader_float2')
    * Implementation: 'id'

---

### /World/agv_6/Materials/cash_register_keys

* **Prim路径 (Prim Path):**/World/agv_6/Materials/cash_register_keys
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_6/Materials/cash_register_keys/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_6/Materials/cash_register_keys/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.976, 0.992, 0.973)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_6/Materials/Chris_Shoe_Sole

* **Prim路径 (Prim Path):**/World/agv_6/Materials/Chris_Shoe_Sole
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_6/Materials/Chris_Shoe_Sole/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_6/Materials/Chris_Shoe_Sole/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.155, 0.149, 0.149)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'opacity' [float] = '0.25'
      * 'roughness' [float] = '1'

---

### /World/agv_6/Materials/Color_002

* **Prim路径 (Prim Path):**/World/agv_6/Materials/Color_002
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_6/Materials/Color_002/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_6/Materials/Color_002/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.217, 0.217, 0.217)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0.570837'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0'

---

### /World/agv_6/Materials/Color_005

* **Prim路径 (Prim Path):**/World/agv_6/Materials/Color_005
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_6/Materials/Color_005/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_6/Materials/Color_005/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.130, 0.130, 0.130)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0.710417'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0'

---

### /World/agv_6/Materials/Color_006

* **Prim路径 (Prim Path):**/World/agv_6/Materials/Color_006
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_6/Materials/Color_006/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_6/Materials/Color_006/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0.237059'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0'

---

### /World/agv_6/Materials/Color_008

* **Prim路径 (Prim Path):**/World/agv_6/Materials/Color_008
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_6/Materials/Color_008/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_6/Materials/Color_008/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.118, 0.118, 0.118)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0.941027'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0'

---

### /World/agv_6/Materials/Color_A01

* **Prim路径 (Prim Path):**/World/agv_6/Materials/Color_A01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_6/Materials/Color_A01/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_6/Materials/Color_A01/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(1.000, 0.000, 0.000)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0.965302'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0'

---

### /World/agv_6/Materials/Color_A11

* **Prim路径 (Prim Path):**/World/agv_6/Materials/Color_A11
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_6/Materials/Color_A11/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_6/Materials/Color_A11/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.600, 0.000, 0.000)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_6/Materials/Color_M04

* **Prim路径 (Prim Path):**/World/agv_6/Materials/Color_M04
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_6/Materials/Color_M04/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_6/Materials/Color_M04/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.557, 0.557, 0.557)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_6/Materials/Color_M05

* **Prim路径 (Prim Path):**/World/agv_6/Materials/Color_M05
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_6/Materials/Color_M05/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_6/Materials/Color_M05/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.447, 0.447, 0.447)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_6/Materials/Color_M06

* **Prim路径 (Prim Path):**/World/agv_6/Materials/Color_M06
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_6/Materials/Color_M06/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_6/Materials/Color_M06/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_6/Materials/Color_M07

* **Prim路径 (Prim Path):**/World/agv_6/Materials/Color_M07
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_6/Materials/Color_M07/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_6/Materials/Color_M07/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.227, 0.227, 0.227)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_6/Materials/Color_M09

* **Prim路径 (Prim Path):**/World/agv_6/Materials/Color_M09
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_6/Materials/Color_M09/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_6/Materials/Color_M09/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0.340226'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0.085341'

---

### /World/agv_6/Materials/FCP_Charcoal_v2

* **Prim路径 (Prim Path):**/World/agv_6/Materials/FCP_Charcoal_v2
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_6/Materials/FCP_Charcoal_v2/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_6/Materials/FCP_Charcoal_v2/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.216, 0.216, 0.216)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_6/Materials/FrontColor

* **Prim路径 (Prim Path):**/World/agv_6/Materials/FrontColor
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_6/Materials/FrontColor/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_6/Materials/FrontColor/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.504, 0.504, 0.504)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0.637593'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0.218852'

---

### /World/agv_6/Materials/Light_Blue

* **Prim路径 (Prim Path):**/World/agv_6/Materials/Light_Blue
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_6/Materials/Light_Blue/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_6/Materials/Light_Blue/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.601, 0.601, 0.601)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '1'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0.170303'

---

### /World/agv_6/Materials/M_0011_Seashell

* **Prim路径 (Prim Path):**/World/agv_6/Materials/M_0011_Seashell
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_6/Materials/M_0011_Seashell/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_6/Materials/M_0011_Seashell/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(1.000, 0.961, 0.933)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_6/Materials/M_0131_Silver

* **Prim路径 (Prim Path):**/World/agv_6/Materials/M_0131_Silver
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_6/Materials/M_0131_Silver/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_6/Materials/M_0131_Silver/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.242, 0.242, 0.242)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0.613318'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0'

---

### /World/agv_6/Materials/M_0134_DimGray

* **Prim路径 (Prim Path):**/World/agv_6/Materials/M_0134_DimGray
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_6/Materials/M_0134_DimGray/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_6/Materials/M_0134_DimGray/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.412, 0.412, 0.412)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_6/Materials/M_0135_DarkGray

* **Prim路径 (Prim Path):**/World/agv_6/Materials/M_0135_DarkGray
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_6/Materials/M_0135_DarkGray/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_6/Materials/M_0135_DarkGray/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.318, 0.318, 0.318)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_6/Materials/Metal_Silver

* **Prim路径 (Prim Path):**/World/agv_6/Materials/Metal_Silver
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_6/Materials/Metal_Silver/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_6/Materials/Metal_Silver/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.918, 0.914, 0.933)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_6/Materials/Mtl1

* **Prim路径 (Prim Path):**/World/agv_6/Materials/Mtl1
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_6/Materials/Mtl1/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_6/Materials/Mtl1/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.015, 0.015, 0.015)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0.255265'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_6/Materials/Mtl10

* **Prim路径 (Prim Path):**/World/agv_6/Materials/Mtl10
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_6/Materials/Mtl10/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_6/Materials/Mtl10/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.322, 0.322, 0.322)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_6/Materials/Mtl11

* **Prim路径 (Prim Path):**/World/agv_6/Materials/Mtl11
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_6/Materials/Mtl11/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_6/Materials/Mtl11/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.067, 0.757, 0.329)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_6/Materials/Mtl12

* **Prim路径 (Prim Path):**/World/agv_6/Materials/Mtl12
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_6/Materials/Mtl12/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_6/Materials/Mtl12/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.502, 0.502, 0.502)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_6/Materials/Mtl13

* **Prim路径 (Prim Path):**/World/agv_6/Materials/Mtl13
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_6/Materials/Mtl13/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_6/Materials/Mtl13/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.008, 0.514, 0.816)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_6/Materials/Mtl14

* **Prim路径 (Prim Path):**/World/agv_6/Materials/Mtl14
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_6/Materials/Mtl14/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_6/Materials/Mtl14/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.310, 0.310, 0.310)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_6/Materials/Mtl15

* **Prim路径 (Prim Path):**/World/agv_6/Materials/Mtl15
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_6/Materials/Mtl15/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_6/Materials/Mtl15/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.263, 0.275, 0.275)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_6/Materials/Mtl16

* **Prim路径 (Prim Path):**/World/agv_6/Materials/Mtl16
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_6/Materials/Mtl16/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_6/Materials/Mtl16/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.698, 0.698, 0.000)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_6/Materials/Mtl17

* **Prim路径 (Prim Path):**/World/agv_6/Materials/Mtl17
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_6/Materials/Mtl17/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_6/Materials/Mtl17/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.000, 0.863, 1.000)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_6/Materials/Mtl3

* **Prim路径 (Prim Path):**/World/agv_6/Materials/Mtl3
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_6/Materials/Mtl3/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_6/Materials/Mtl3/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.431, 0.455, 0.498)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_6/Materials/Mtl35

* **Prim路径 (Prim Path):**/World/agv_6/Materials/Mtl35
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_6/Materials/Mtl35/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_6/Materials/Mtl35/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.792, 0.820, 0.933)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_6/Materials/Mtl36

* **Prim路径 (Prim Path):**/World/agv_6/Materials/Mtl36
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_6/Materials/Mtl36/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_6/Materials/Mtl36/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.667, 0.698, 0.765)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_6/Materials/Mtl37

* **Prim路径 (Prim Path):**/World/agv_6/Materials/Mtl37
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_6/Materials/Mtl37/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_6/Materials/Mtl37/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.098, 0.098, 0.098)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_6/Materials/Mtl3a

* **Prim路径 (Prim Path):**/World/agv_6/Materials/Mtl3a
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_6/Materials/Mtl3a/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_6/Materials/Mtl3a/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.388, 0.369, 0.322)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_6/Materials/Mtl3b

* **Prim路径 (Prim Path):**/World/agv_6/Materials/Mtl3b
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_6/Materials/Mtl3b/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_6/Materials/Mtl3b/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.365, 0.176, 0.012)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0.959234'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'opacity' [float] = '0.273471'
      * 'roughness' [float] = '0.164234'

---

### /World/agv_6/Materials/Mtl5

* **Prim路径 (Prim Path):**/World/agv_6/Materials/Mtl5
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_6/Materials/Mtl5/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_6/Materials/Mtl5/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.396, 0.408, 0.467)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_6/Materials/Mtl7

* **Prim路径 (Prim Path):**/World/agv_6/Materials/Mtl7
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_6/Materials/Mtl7/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_6/Materials/Mtl7/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.376, 0.376, 0.376)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_6/Materials/Mtl8

* **Prim路径 (Prim Path):**/World/agv_6/Materials/Mtl8
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_6/Materials/Mtl8/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_6/Materials/Mtl8/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.173, 0.173, 0.173)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_6/Materials/Mtla

* **Prim路径 (Prim Path):**/World/agv_6/Materials/Mtla
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_6/Materials/Mtla/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_6/Materials/Mtla/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.612, 0.725, 0.745)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_6/Materials/Mtlb1

* **Prim路径 (Prim Path):**/World/agv_6/Materials/Mtlb1
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_6/Materials/Mtlb1/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_6/Materials/Mtlb1/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.949, 0.925, 0.933)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_6/Materials/Stainless_Steel

* **Prim路径 (Prim Path):**/World/agv_6/Materials/Stainless_Steel
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_6/Materials/Stainless_Steel/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_6/Materials/Stainless_Steel/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.292, 0.294, 0.284)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0.431257'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_6/Materials/Metal_Aluminum_Anodized_1

* **Prim路径 (Prim Path):**/World/agv_6/Materials/Metal_Aluminum_Anodized_1
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_6/Materials/Metal_Aluminum_Anodized_1/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_6/Materials/Metal_Aluminum_Anodized_1/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.260, 0.269, 0.282)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0.309883'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0'

---

### /World/agv_6/Materials/Metal_Aluminum_Anodized_2

* **Prim路径 (Prim Path):**/World/agv_6/Materials/Metal_Aluminum_Anodized_2
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_6/Materials/Metal_Aluminum_Anodized_2/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_6/Materials/Metal_Aluminum_Anodized_2/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.792, 0.820, 0.859)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_6/Materials/basic_gray_plastic

* **Prim路径 (Prim Path):**/World/agv_6/Materials/basic_gray_plastic
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_6/Materials/basic_gray_plastic/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_6/Materials/basic_gray_plastic/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0.297745'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0.115685'

---

### /World/agv_6/Materials/texture

* **Prim路径 (Prim Path):**/World/agv_6/Materials/texture
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_6/Materials/texture/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_6/Materials/texture/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.294, 0.294, 0.294)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/StackedCarton_1/Materials/Material_1

* **Prim路径 (Prim Path):**/World/StackedCarton_1/Materials/Material_1
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/StackedCarton_1/Materials/Material_1/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/StackedCarton_1/Materials/Material_1/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f]
        * Connected: '/World/StackedCarton_1/Materials/Material_1/tex_base.outputs:rgb' @ '/World/StackedCarton_1/Materials/Material_1/tex_base'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/Material_1_baseColor_cutoff173.png'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(1.000, 1.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'opacity' [float]
        * Connected: '/World/StackedCarton_1/Materials/Material_1/tex_base.outputs:a' @ '/World/StackedCarton_1/Materials/Material_1/tex_base'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/Material_1_baseColor_cutoff173.png'
      * 'roughness' [float] = '0.6'
    * '/World/StackedCarton_1/Materials/Material_1/tex_base' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/Material_1_baseColor_cutoff173.png'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'file' [asset] = '0/Material_1_baseColor_cutoff173.png'
      * 'st' [float2]
        * Connected: '/World/StackedCarton_1/Materials/Material_1/uvset0.outputs:result' @ '/World/StackedCarton_1/Materials/Material_1/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/StackedCarton_1/Materials/Material_1/uvset0' (ID: 'UsdPrimvarReader_float2')
    * Implementation: 'id'

---

### /World/StackedCarton_2/Materials/Material_1

* **Prim路径 (Prim Path):**/World/StackedCarton_2/Materials/Material_1
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/StackedCarton_2/Materials/Material_1/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/StackedCarton_2/Materials/Material_1/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f]
        * Connected: '/World/StackedCarton_2/Materials/Material_1/tex_base.outputs:rgb' @ '/World/StackedCarton_2/Materials/Material_1/tex_base'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/Material_1_baseColor_cutoff173.png'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(1.000, 1.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'opacity' [float]
        * Connected: '/World/StackedCarton_2/Materials/Material_1/tex_base.outputs:a' @ '/World/StackedCarton_2/Materials/Material_1/tex_base'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/Material_1_baseColor_cutoff173.png'
      * 'roughness' [float] = '0.6'
    * '/World/StackedCarton_2/Materials/Material_1/tex_base' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/Material_1_baseColor_cutoff173.png'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'file' [asset] = '0/Material_1_baseColor_cutoff173.png'
      * 'st' [float2]
        * Connected: '/World/StackedCarton_2/Materials/Material_1/uvset0.outputs:result' @ '/World/StackedCarton_2/Materials/Material_1/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/StackedCarton_2/Materials/Material_1/uvset0' (ID: 'UsdPrimvarReader_float2')
    * Implementation: 'id'

---

### /World/StackedCarton_3/Materials/Material_1

* **Prim路径 (Prim Path):**/World/StackedCarton_3/Materials/Material_1
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/StackedCarton_3/Materials/Material_1/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/StackedCarton_3/Materials/Material_1/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f]
        * Connected: '/World/StackedCarton_3/Materials/Material_1/tex_base.outputs:rgb' @ '/World/StackedCarton_3/Materials/Material_1/tex_base'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/Material_1_baseColor_cutoff173.png'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(1.000, 1.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'opacity' [float]
        * Connected: '/World/StackedCarton_3/Materials/Material_1/tex_base.outputs:a' @ '/World/StackedCarton_3/Materials/Material_1/tex_base'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/Material_1_baseColor_cutoff173.png'
      * 'roughness' [float] = '0.6'
    * '/World/StackedCarton_3/Materials/Material_1/tex_base' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/Material_1_baseColor_cutoff173.png'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'file' [asset] = '0/Material_1_baseColor_cutoff173.png'
      * 'st' [float2]
        * Connected: '/World/StackedCarton_3/Materials/Material_1/uvset0.outputs:result' @ '/World/StackedCarton_3/Materials/Material_1/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/StackedCarton_3/Materials/Material_1/uvset0' (ID: 'UsdPrimvarReader_float2')
    * Implementation: 'id'

---

### /World/StackedCarton_4/Materials/Material_1

* **Prim路径 (Prim Path):**/World/StackedCarton_4/Materials/Material_1
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/StackedCarton_4/Materials/Material_1/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/StackedCarton_4/Materials/Material_1/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f]
        * Connected: '/World/StackedCarton_4/Materials/Material_1/tex_base.outputs:rgb' @ '/World/StackedCarton_4/Materials/Material_1/tex_base'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/Material_1_baseColor_cutoff173.png'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(1.000, 1.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'opacity' [float]
        * Connected: '/World/StackedCarton_4/Materials/Material_1/tex_base.outputs:a' @ '/World/StackedCarton_4/Materials/Material_1/tex_base'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/Material_1_baseColor_cutoff173.png'
      * 'roughness' [float] = '0.6'
    * '/World/StackedCarton_4/Materials/Material_1/tex_base' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/Material_1_baseColor_cutoff173.png'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'file' [asset] = '0/Material_1_baseColor_cutoff173.png'
      * 'st' [float2]
        * Connected: '/World/StackedCarton_4/Materials/Material_1/uvset0.outputs:result' @ '/World/StackedCarton_4/Materials/Material_1/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/StackedCarton_4/Materials/Material_1/uvset0' (ID: 'UsdPrimvarReader_float2')
    * Implementation: 'id'

---

### /World/StackedCarton_5/Materials/Material_1

* **Prim路径 (Prim Path):**/World/StackedCarton_5/Materials/Material_1
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/StackedCarton_5/Materials/Material_1/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/StackedCarton_5/Materials/Material_1/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f]
        * Connected: '/World/StackedCarton_5/Materials/Material_1/tex_base.outputs:rgb' @ '/World/StackedCarton_5/Materials/Material_1/tex_base'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/Material_1_baseColor_cutoff173.png'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(1.000, 1.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'opacity' [float]
        * Connected: '/World/StackedCarton_5/Materials/Material_1/tex_base.outputs:a' @ '/World/StackedCarton_5/Materials/Material_1/tex_base'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/Material_1_baseColor_cutoff173.png'
      * 'roughness' [float] = '0.6'
    * '/World/StackedCarton_5/Materials/Material_1/tex_base' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/Material_1_baseColor_cutoff173.png'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'file' [asset] = '0/Material_1_baseColor_cutoff173.png'
      * 'st' [float2]
        * Connected: '/World/StackedCarton_5/Materials/Material_1/uvset0.outputs:result' @ '/World/StackedCarton_5/Materials/Material_1/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/StackedCarton_5/Materials/Material_1/uvset0' (ID: 'UsdPrimvarReader_float2')
    * Implementation: 'id'

---

### /World/StackedCarton_6/Materials/Material_1

* **Prim路径 (Prim Path):**/World/StackedCarton_6/Materials/Material_1
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/StackedCarton_6/Materials/Material_1/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/StackedCarton_6/Materials/Material_1/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f]
        * Connected: '/World/StackedCarton_6/Materials/Material_1/tex_base.outputs:rgb' @ '/World/StackedCarton_6/Materials/Material_1/tex_base'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/Material_1_baseColor_cutoff173.png'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(1.000, 1.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'opacity' [float]
        * Connected: '/World/StackedCarton_6/Materials/Material_1/tex_base.outputs:a' @ '/World/StackedCarton_6/Materials/Material_1/tex_base'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/Material_1_baseColor_cutoff173.png'
      * 'roughness' [float] = '0.6'
    * '/World/StackedCarton_6/Materials/Material_1/tex_base' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/Material_1_baseColor_cutoff173.png'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'file' [asset] = '0/Material_1_baseColor_cutoff173.png'
      * 'st' [float2]
        * Connected: '/World/StackedCarton_6/Materials/Material_1/uvset0.outputs:result' @ '/World/StackedCarton_6/Materials/Material_1/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/StackedCarton_6/Materials/Material_1/uvset0' (ID: 'UsdPrimvarReader_float2')
    * Implementation: 'id'

---

### /World/Black_Honey___Robotic_Arm/Materials/robo_arm

* **Prim路径 (Prim Path):**/World/Black_Honey___Robotic_Arm/Materials/robo_arm
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/Black_Honey___Robotic_Arm/Materials/robo_arm/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Black_Honey___Robotic_Arm/Materials/robo_arm/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f]
        * Connected: '/World/Black_Honey___Robotic_Arm/Materials/robo_arm/tex_base.outputs:rgb' @ '/World/Black_Honey___Robotic_Arm/Materials/robo_arm/tex_base'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/robo_arm_baseColor.jpg'
      * 'emissiveColor' [color3f]
        * Connected: '/World/Black_Honey___Robotic_Arm/Materials/robo_arm/tex_emissive.outputs:rgb' @ '/World/Black_Honey___Robotic_Arm/Materials/robo_arm/tex_emissive'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/robo_arm_emissive.jpg'
      * 'metallic' [float]
        * Connected: '/World/Black_Honey___Robotic_Arm/Materials/robo_arm/tex_metallic.outputs:r' @ '/World/Black_Honey___Robotic_Arm/Materials/robo_arm/tex_metallic'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/robo_arm_metallicRoughness_metal.jpg'
      * 'normal' [normal3f]
        * Connected: '/World/Black_Honey___Robotic_Arm/Materials/robo_arm/tex_normal.outputs:rgb' @ '/World/Black_Honey___Robotic_Arm/Materials/robo_arm/tex_normal'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/robo_arm_normal_norm.jpg'
      * 'occlusion' [float] = '1'
      * 'roughness' [float]
        * Connected: '/World/Black_Honey___Robotic_Arm/Materials/robo_arm/tex_roughness.outputs:r' @ '/World/Black_Honey___Robotic_Arm/Materials/robo_arm/tex_roughness'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/robo_arm_metallicRoughness_rough.jpg'
    * '/World/Black_Honey___Robotic_Arm/Materials/robo_arm/tex_base' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/robo_arm_baseColor.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'file' [asset] = '0/robo_arm_baseColor.jpg'
      * 'st' [float2]
        * Connected: '/World/Black_Honey___Robotic_Arm/Materials/robo_arm/uvset0.outputs:result' @ '/World/Black_Honey___Robotic_Arm/Materials/robo_arm/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/Black_Honey___Robotic_Arm/Materials/robo_arm/uvset0' (ID: 'UsdPrimvarReader_float2')
    * Implementation: 'id'
    * '/World/Black_Honey___Robotic_Arm/Materials/robo_arm/tex_emissive' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/robo_arm_emissive.jpg'
    * Inputs:
      * 'fallback' [float4] = '(0.000, 0.000, 0.000, 1.000)'
      * 'file' [asset] = '0/robo_arm_emissive.jpg'
      * 'st' [float2]
        * Connected: '/World/Black_Honey___Robotic_Arm/Materials/robo_arm/uvset0.outputs:result' @ '/World/Black_Honey___Robotic_Arm/Materials/robo_arm/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/Black_Honey___Robotic_Arm/Materials/robo_arm/tex_metallic' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/robo_arm_metallicRoughness_metal.jpg'
    * Inputs:
      * 'fallback' [float4] = '(0.000, 0.000, 0.000, 1.000)'
      * 'file' [asset] = '0/robo_arm_metallicRoughness_metal.jpg'
      * 'st' [float2]
        * Connected: '/World/Black_Honey___Robotic_Arm/Materials/robo_arm/uvset0.outputs:result' @ '/World/Black_Honey___Robotic_Arm/Materials/robo_arm/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/Black_Honey___Robotic_Arm/Materials/robo_arm/tex_normal' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/robo_arm_normal_norm.jpg'
    * Inputs:
      * 'bias' [float4] = '(-1.000, -1.000, -1.000, -1.000)'
      * 'fallback' [float4] = '(0.000, 0.000, 1.000, 1.000)'
      * 'file' [asset] = '0/robo_arm_normal_norm.jpg'
      * 'scale' [float4] = '(2.000, 2.000, 2.000, 2.000)'
      * 'st' [float2]
        * Connected: '/World/Black_Honey___Robotic_Arm/Materials/robo_arm/uvset0.outputs:result' @ '/World/Black_Honey___Robotic_Arm/Materials/robo_arm/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/Black_Honey___Robotic_Arm/Materials/robo_arm/tex_roughness' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/robo_arm_metallicRoughness_rough.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 0.000, 0.000, 1.000)'
      * 'file' [asset] = '0/robo_arm_metallicRoughness_rough.jpg'
      * 'st' [float2]
        * Connected: '/World/Black_Honey___Robotic_Arm/Materials/robo_arm/uvset0.outputs:result' @ '/World/Black_Honey___Robotic_Arm/Materials/robo_arm/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'

---

### /World/Black_Honey___Robotic_Arm/Materials/robot_base

* **Prim路径 (Prim Path):**/World/Black_Honey___Robotic_Arm/Materials/robot_base
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/Black_Honey___Robotic_Arm/Materials/robot_base/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Black_Honey___Robotic_Arm/Materials/robot_base/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f]
        * Connected: '/World/Black_Honey___Robotic_Arm/Materials/robot_base/tex_base.outputs:rgb' @ '/World/Black_Honey___Robotic_Arm/Materials/robot_base/tex_base'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/robot_base_baseColor.jpg'
      * 'emissiveColor' [color3f]
        * Connected: '/World/Black_Honey___Robotic_Arm/Materials/robot_base/tex_emissive.outputs:rgb' @ '/World/Black_Honey___Robotic_Arm/Materials/robot_base/tex_emissive'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/robot_base_emissive.jpg'
      * 'metallic' [float]
        * Connected: '/World/Black_Honey___Robotic_Arm/Materials/robot_base/tex_metallic.outputs:r' @ '/World/Black_Honey___Robotic_Arm/Materials/robot_base/tex_metallic'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/robot_base_metallicRoughness_metal.jpg'
      * 'normal' [normal3f]
        * Connected: '/World/Black_Honey___Robotic_Arm/Materials/robot_base/tex_normal.outputs:rgb' @ '/World/Black_Honey___Robotic_Arm/Materials/robot_base/tex_normal'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/robot_base_normal_norm.jpg'
      * 'occlusion' [float] = '1'
      * 'roughness' [float]
        * Connected: '/World/Black_Honey___Robotic_Arm/Materials/robot_base/tex_roughness.outputs:r' @ '/World/Black_Honey___Robotic_Arm/Materials/robot_base/tex_roughness'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/robot_base_metallicRoughness_rough.jpg'
    * '/World/Black_Honey___Robotic_Arm/Materials/robot_base/tex_base' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/robot_base_baseColor.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'file' [asset] = '0/robot_base_baseColor.jpg'
      * 'st' [float2]
        * Connected: '/World/Black_Honey___Robotic_Arm/Materials/robot_base/uvset0.outputs:result' @ '/World/Black_Honey___Robotic_Arm/Materials/robot_base/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/Black_Honey___Robotic_Arm/Materials/robot_base/uvset0' (ID: 'UsdPrimvarReader_float2')
    * Implementation: 'id'
    * '/World/Black_Honey___Robotic_Arm/Materials/robot_base/tex_emissive' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/robot_base_emissive.jpg'
    * Inputs:
      * 'fallback' [float4] = '(0.000, 0.000, 0.000, 1.000)'
      * 'file' [asset] = '0/robot_base_emissive.jpg'
      * 'st' [float2]
        * Connected: '/World/Black_Honey___Robotic_Arm/Materials/robot_base/uvset0.outputs:result' @ '/World/Black_Honey___Robotic_Arm/Materials/robot_base/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/Black_Honey___Robotic_Arm/Materials/robot_base/tex_metallic' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/robot_base_metallicRoughness_metal.jpg'
    * Inputs:
      * 'fallback' [float4] = '(0.000, 0.000, 0.000, 1.000)'
      * 'file' [asset] = '0/robot_base_metallicRoughness_metal.jpg'
      * 'st' [float2]
        * Connected: '/World/Black_Honey___Robotic_Arm/Materials/robot_base/uvset0.outputs:result' @ '/World/Black_Honey___Robotic_Arm/Materials/robot_base/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/Black_Honey___Robotic_Arm/Materials/robot_base/tex_normal' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/robot_base_normal_norm.jpg'
    * Inputs:
      * 'bias' [float4] = '(-1.000, -1.000, -1.000, -1.000)'
      * 'fallback' [float4] = '(0.000, 0.000, 1.000, 1.000)'
      * 'file' [asset] = '0/robot_base_normal_norm.jpg'
      * 'scale' [float4] = '(2.000, 2.000, 2.000, 2.000)'
      * 'st' [float2]
        * Connected: '/World/Black_Honey___Robotic_Arm/Materials/robot_base/uvset0.outputs:result' @ '/World/Black_Honey___Robotic_Arm/Materials/robot_base/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/Black_Honey___Robotic_Arm/Materials/robot_base/tex_roughness' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/robot_base_metallicRoughness_rough.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 0.000, 0.000, 1.000)'
      * 'file' [asset] = '0/robot_base_metallicRoughness_rough.jpg'
      * 'st' [float2]
        * Connected: '/World/Black_Honey___Robotic_Arm/Materials/robot_base/uvset0.outputs:result' @ '/World/Black_Honey___Robotic_Arm/Materials/robot_base/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'

---

### /World/rs007l_onrobot_rg2/Looks/material_Black

* **Prim路径 (Prim Path):**/World/rs007l_onrobot_rg2/Looks/material_Black
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/rs007l_onrobot_rg2/Looks/material_Black/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/rs007l_onrobot_rg2/Looks/material_Black/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * Inputs:
      * 'diffuse_color_constant' [color3f] = '(0.000, 0.000, 0.000)'

---

### /World/rs007l_onrobot_rg2/Looks/material_White

* **Prim路径 (Prim Path):**/World/rs007l_onrobot_rg2/Looks/material_White
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/rs007l_onrobot_rg2/Looks/material_White/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/rs007l_onrobot_rg2/Looks/material_White/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * Inputs:
      * 'diffuse_color_constant' [color3f] = '(1.000, 1.000, 1.000)'

---

### /World/rs007l_onrobot_rg2/Looks/material_CCCCCC

* **Prim路径 (Prim Path):**/World/rs007l_onrobot_rg2/Looks/material_CCCCCC
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/rs007l_onrobot_rg2/Looks/material_CCCCCC/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/rs007l_onrobot_rg2/Looks/material_CCCCCC/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * Inputs:
      * 'diffuse_color_constant' [color3f] = '(0.800, 0.800, 0.800)'

---

### /World/rs007l_onrobot_rg2/Looks/material_191919

* **Prim路径 (Prim Path):**/World/rs007l_onrobot_rg2/Looks/material_191919
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/rs007l_onrobot_rg2/Looks/material_191919/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/rs007l_onrobot_rg2/Looks/material_191919/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * Inputs:
      * 'diffuse_color_constant' [color3f] = '(0.100, 0.100, 0.100)'

---
