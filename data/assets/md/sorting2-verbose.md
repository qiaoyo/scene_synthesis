# USDA场景描述文档:sorting2.usda

## 1.场景元数据(Scene Metadata)

* **USDA文件路径(USDA File Path):**`/media/simple/another_Documents/isaacsim_assets/scenedata/sorting2.usda`
* **默认Prim (Default Prim):**'Not Set'
* **单位与坐标系 (Units & Coordinate System):**
  * **米(Meters Per Unit):**1.0
  * **Up Axis:**Z
* **场景描述(Scene Describe):** 该场景呈现出一个极具秩序感且高度智能化的现代工业分拣车间，整体规划严谨地遵循了“生产流与物流分离、固定站与移动单元协同”的先进布局理念，展现了一个高效、整洁且逻辑清晰的工业处理环境。从厂区的空间格局来看，车间地面采用了深灰色的高强度耐磨涂层，表面带有细腻的工业质感，其上精准绘制了平行的黄色安全警示线，划定了明确的自动化设备行驶路径与人工作业边界。厂房墙面由白色的砖纹结构与上方明黄色的装饰板构成，不仅提升了室内采光效果，也通过色彩对比增强了区域辨识度。整个车间被科学地划分为三个核心功能区：首先是横贯画面右侧的自动化输送区，该区域部署了一套由深蓝色钢性支架支撑的高架皮带输送机，黑色传送带表面正载运着半圆弧形和长方体形状的灰色工件，正处于匀速流转状态。其次是位于画面中心偏下位置的精密装配与分拣站台，该站台由三组并排的黄色拼合式木质工作台组成，台面上方垂直安装了两台白色的六轴协作机器人，其修长的机械臂正处于灵活的作业姿态，负责对台面上整齐排列的数十个工件进行精确抓取或装配。工作台下方设有开放式的黄色储物格，用于存放工序备件。第三个区域是占据地面开阔空间的柔性物流转运区。在这个区域内，部署了多台不同功能属性的自动化移动设备。其中，两台底盘呈亮黄色的自动导引运输车（AGV）占据了显要位置，它们顶部各自载有一个淡蓝色的镂空塑料周转筐，正沿着预设路径在输送线与工作站之间执行物料配送任务。与此同时，一台深灰色的自主移动机器人（AMR）位于画面中央，其底座侧边贴有亮黄色安全标识，顶部集成了一台小型的白色协作机械臂，正配合两台载货AGV进行动态的物料交互与接驳。在背景的远端通道处，还可以识别出一台处于待命姿态的亮黄色重型工业叉车，其货叉平放于地面，为车间提供了大宗物料的装卸保障。从设备排布方式与整体规划结构分析，该场景巧妙地将固定式的输送线（线）与点对点的协作站（点）通过网格化的移动物流（面）有机结合在一起。这种“点-线-面”交织的拓扑结构极大地提升了生产线的柔性，能够根据实时产量需求快速调整AGV的调度频率。设备间的排布距离经过了精密计算，确保了协作机器人的工作包络圆能够覆盖工作台的所有作业点，同时又为AGV与AMR预留了充足的避障与转向空间。色彩管理在场景中起到了关键的导向作用：蓝色输送架定义了稳定的生产轴心，黄色移动底座与警示线标识了动态的物流能量，白色机器人柜体则代表了高精度的执行核心。整个车间没有任何散乱的杂物或暴露的线缆，所有工业设备均呈现出极佳的维护状态，深刻诠释了工业4.0时代关于“数字孪生、人机协同、柔性调度”的顶层设计理念，是一个功能完备、作业逻辑自洽的现代化智慧工厂范本。
* **设备数量(Device Number):**
  * **Scene: 1**
  * **IndustrialRobot: 3**
  * **Workbench: 4**
  * **Conveyor: 2**
  * **AGV: 3**
  * **Forklift: 1**
  * **Box: 4**
  * **Rack: 0**
  * **Pallet: 0**
  * **Part: 24**
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
  * SortingArea (Xform)
    * DistantLight (Xform)
      * DistantLight (DistantLight)
    * GroundPlane (Xform)
      * GroundPlane (Xform)
        * CollisionMesh (Mesh)
        * CollisionPlane (Plane)
    * NavMesh (Scope)
      * NavMeshVolume (NavMeshVolume)
      * NavMeshVolume_01 (NavMeshVolume)
      * NavMeshVolume_02 (NavMeshVolume)
      * NavMeshVolume_03 (NavMeshVolume)
      * NavMeshVolume_04 (NavMeshVolume)
      * NavMeshVolume_05 (NavMeshVolume)
    * PhysicsScene (PhysicsScene)
    * RectLight (Xform)
      * RectLight (RectLight)
    * SM_BeamA_9M25 (Xform)
      * SM_BeamA_9M25 (Xform)
        * SM_BeamA_9M (Mesh)
        * Looks (Scope)
          * MI_BeamsA_01 (Material)
            * MI_CeilingA_06b (Shader)
    * SM_BeamA_9M26 (Xform)
      * SM_BeamA_9M26 (Xform)
        * SM_BeamA_9M (Mesh)
        * Looks (Scope)
          * MI_BeamsA_01 (Material)
            * MI_CeilingA_06b (Shader)
    * SM_BeamA_9M27 (Xform)
      * SM_BeamA_9M27 (Xform)
        * SM_BeamA_9M (Mesh)
        * Looks (Scope)
          * MI_BeamsA_01 (Material)
            * MI_CeilingA_06b (Shader)
    * SM_BeamA_9M29 (Xform)
      * SM_BeamA_9M29 (Xform)
        * SM_BeamA_9M (Mesh)
        * Looks (Scope)
          * MI_BeamsA_01 (Material)
            * MI_CeilingA_06b (Shader)
    * SM_BeamA_9M30 (Xform)
      * SM_BeamA_9M30 (Xform)
        * SM_BeamA_9M (Mesh)
        * Looks (Scope)
          * MI_BeamsA_01 (Material)
            * MI_CeilingA_06b (Shader)
    * SM_BeamA_9M31 (Xform)
      * SM_BeamA_9M31 (Xform)
        * SM_BeamA_9M (Mesh)
        * Looks (Scope)
          * MI_BeamsA_01 (Material)
            * MI_CeilingA_06b (Shader)
    * SM_BeamA_9M33 (Xform)
      * SM_BeamA_9M33 (Xform)
        * SM_BeamA_9M (Mesh)
        * Looks (Scope)
          * MI_BeamsA_01 (Material)
            * MI_CeilingA_06b (Shader)
    * SM_BeamA_9M34 (Xform)
      * SM_BeamA_9M34 (Xform)
        * SM_BeamA_9M (Mesh)
        * Looks (Scope)
          * MI_BeamsA_01 (Material)
            * MI_CeilingA_06b (Shader)
    * SM_BeamA_9M35 (Xform)
      * SM_BeamA_9M35 (Xform)
        * SM_BeamA_9M (Mesh)
        * Looks (Scope)
          * MI_BeamsA_01 (Material)
            * MI_CeilingA_06b (Shader)
    * SM_BeamA_9M37 (Xform)
      * SM_BeamA_9M37 (Xform)
        * SM_BeamA_9M (Mesh)
        * Looks (Scope)
          * MI_BeamsA_01 (Material)
            * MI_CeilingA_06b (Shader)
    * SM_BeamA_9M38 (Xform)
      * SM_BeamA_9M38 (Xform)
        * SM_BeamA_9M (Mesh)
        * Looks (Scope)
          * MI_BeamsA_01 (Material)
            * MI_CeilingA_06b (Shader)
    * SM_BeamA_9M39 (Xform)
      * SM_BeamA_9M39 (Xform)
        * SM_BeamA_9M (Mesh)
        * Looks (Scope)
          * MI_BeamsA_01 (Material)
            * MI_CeilingA_06b (Shader)
    * SM_BracketBeam_6m10 (Xform)
      * SM_BracketBeam_6m10 (Xform)
        * SM_BracketBeam_3m (Mesh)
        * Looks (Scope)
          * MI_BeamsA_01 (Material)
            * MI_CeilingA_06b (Shader)
    * SM_BracketBeam_6m11 (Xform)
      * SM_BracketBeam_6m11 (Xform)
        * SM_BracketBeam_3m (Mesh)
        * Looks (Scope)
          * MI_BeamsA_01 (Material)
            * MI_CeilingA_06b (Shader)
    * SM_BracketBeam_6m12 (Xform)
      * SM_BracketBeam_6m12 (Xform)
        * SM_BracketBeam (Mesh)
        * Looks (Scope)
          * MI_BeamsA_01 (Material)
            * MI_CeilingA_06b (Shader)
    * SM_BracketBeam_6m13 (Xform)
      * SM_BracketBeam_6m13 (Xform)
        * SM_BracketBeam_3m (Mesh)
        * Looks (Scope)
          * MI_BeamsA_01 (Material)
            * MI_CeilingA_06b (Shader)
    * SM_BracketBeam_6m14 (Xform)
      * SM_BracketBeam_6m14 (Xform)
        * SM_BracketBeam_3m (Mesh)
        * Looks (Scope)
          * MI_BeamsA_01 (Material)
            * MI_CeilingA_06b (Shader)
    * SM_BracketBeam_6m15 (Xform)
      * SM_BracketBeam_6m15 (Xform)
        * SM_BracketBeam_3m (Mesh)
        * Looks (Scope)
          * MI_BeamsA_01 (Material)
            * MI_CeilingA_06b (Shader)
    * SM_BracketBeam_6m16 (Xform)
      * SM_BracketBeam_6m16 (Xform)
        * SM_BracketBeam_3m (Mesh)
        * Looks (Scope)
          * MI_BeamsA_01 (Material)
            * MI_CeilingA_06b (Shader)
    * SM_BracketBeam_6m7 (Xform)
      * SM_BracketBeam_6m7 (Xform)
        * SM_BracketBeam_3m (Mesh)
        * Looks (Scope)
          * MI_BeamsA_01 (Material)
            * MI_CeilingA_06b (Shader)
    * SM_BracketBeam_6m8 (Xform)
      * SM_BracketBeam_6m8 (Xform)
        * SM_BracketBeam_3m (Mesh)
        * Looks (Scope)
          * MI_BeamsA_01 (Material)
            * MI_CeilingA_06b (Shader)
    * SM_BracketBeam_6m9 (Xform)
      * SM_BracketBeam_6m9 (Xform)
        * SM_BracketBeam_3m (Mesh)
        * Looks (Scope)
          * MI_BeamsA_01 (Material)
            * MI_CeilingA_06b (Shader)
    * SM_BracketSlot10 (Xform)
      * SM_BracketSlot10 (Xform)
        * SM_BracketSlot (Mesh)
        * Looks (Scope)
          * MI_FrameA_01 (Material)
            * MI_FrameA_01 (Shader)
    * SM_BracketSlot12 (Xform)
      * SM_BracketSlot12 (Xform)
        * SM_BracketSlot (Mesh)
        * Looks (Scope)
          * MI_FrameA_01 (Material)
            * MI_FrameA_01 (Shader)
    * SM_BracketSlot13 (Xform)
      * SM_BracketSlot13 (Xform)
        * SM_BracketSlot (Mesh)
        * Looks (Scope)
          * MI_FrameA_01 (Material)
            * MI_FrameA_01 (Shader)
    * SM_BracketSlot14 (Xform)
      * SM_BracketSlot14 (Xform)
        * SM_BracketSlot (Mesh)
        * Looks (Scope)
          * MI_FrameA_01 (Material)
            * MI_FrameA_01 (Shader)
    * SM_BracketSlot15 (Xform)
      * SM_BracketSlot15 (Xform)
        * SM_BracketSlot (Mesh)
        * Looks (Scope)
          * MI_FrameA_01 (Material)
            * MI_FrameA_01 (Shader)
    * SM_BracketSlot16 (Xform)
      * SM_BracketSlot16 (Xform)
        * SM_BracketSlot (Mesh)
        * Looks (Scope)
          * MI_FrameA_01 (Material)
            * MI_FrameA_01 (Shader)
    * SM_BracketSlot17 (Xform)
      * SM_BracketSlot17 (Xform)
        * SM_BracketSlot (Mesh)
        * Looks (Scope)
          * MI_FrameA_01 (Material)
            * MI_FrameA_01 (Shader)
    * SM_BracketSlot18 (Xform)
      * SM_BracketSlot18 (Xform)
        * SM_BracketSlot (Mesh)
        * Looks (Scope)
          * MI_FrameA_01 (Material)
            * MI_FrameA_01 (Shader)
    * SM_BracketSlot19 (Xform)
      * SM_BracketSlot19 (Xform)
        * SM_BracketSlot (Mesh)
        * Looks (Scope)
          * MI_FrameA_01 (Material)
            * MI_FrameA_01 (Shader)
    * SM_BracketSlot20 (Xform)
      * SM_BracketSlot20 (Xform)
        * SM_BracketSlot (Mesh)
        * Looks (Scope)
          * MI_FrameA_01 (Material)
            * MI_FrameA_01 (Shader)
    * SM_BracketSlot21 (Xform)
      * SM_BracketSlot21 (Xform)
        * SM_BracketSlot (Mesh)
        * Looks (Scope)
          * MI_FrameA_01 (Material)
            * MI_FrameA_01 (Shader)
    * SM_BracketSlot22 (Xform)
      * SM_BracketSlot22 (Xform)
        * SM_BracketSlot (Mesh)
        * Looks (Scope)
          * MI_FrameA_01 (Material)
            * MI_FrameA_01 (Shader)
    * SM_BracketSlot23 (Xform)
      * SM_BracketSlot23 (Xform)
        * SM_BracketSlot (Mesh)
        * Looks (Scope)
          * MI_FrameA_01 (Material)
            * MI_FrameA_01 (Shader)
    * SM_BracketSlot24 (Xform)
      * SM_BracketSlot24 (Xform)
        * SM_BracketSlot (Mesh)
        * Looks (Scope)
          * MI_FrameA_01 (Material)
            * MI_FrameA_01 (Shader)
    * SM_BracketSlot26_1493 (Xform)
      * SM_BracketSlot26_1493 (Xform)
        * SM_BracketSlot (Mesh)
        * Looks (Scope)
          * MI_FrameA_01 (Material)
            * MI_FrameA_01 (Shader)
    * SM_BracketSlot27 (Xform)
      * SM_BracketSlot27 (Xform)
        * SM_BracketSlot (Mesh)
        * Looks (Scope)
          * MI_FrameA_01 (Material)
            * MI_FrameA_01 (Shader)
    * SM_BracketSlot3 (Xform)
      * SM_BracketSlot3 (Xform)
        * SM_BracketSlot (Mesh)
        * Looks (Scope)
          * MI_FrameA_01 (Material)
            * MI_FrameA_01 (Shader)
    * SM_BracketSlot41 (Xform)
      * SM_BracketSlot41 (Xform)
        * SM_BracketSlot (Mesh)
        * Looks (Scope)
          * MI_FrameA_01 (Material)
            * MI_FrameA_01 (Shader)
    * SM_BracketSlot8 (Xform)
      * SM_BracketSlot8 (Xform)
        * SM_BracketSlot (Mesh)
        * Looks (Scope)
          * MI_FrameA_01 (Material)
            * MI_FrameA_01 (Shader)
    * SM_BracketSlot9 (Xform)
      * SM_BracketSlot9 (Xform)
        * SM_BracketSlot (Mesh)
        * Looks (Scope)
          * MI_FrameA_01 (Material)
            * MI_FrameA_01 (Shader)
    * SM_CeilingA_6X17 (Xform)
      * SM_CeilingA_6X17 (Xform)
        * SM_CeilingA_6X6 (Mesh)
        * Looks (Scope)
          * MI_WallB_01 (Material)
            * MI_WallB_01 (Shader)
    * SM_CeilingA_6X19 (Xform)
      * SM_CeilingA_6X19 (Xform)
        * SM_CeilingA_6X6 (Mesh)
        * Looks (Scope)
          * MI_WallB_01 (Material)
            * MI_WallB_01 (Shader)
    * SM_CeilingA_6X21 (Xform)
      * SM_CeilingA_6X21 (Xform)
        * SM_CeilingA_6X6 (Mesh)
        * Looks (Scope)
          * MI_WallB_01 (Material)
            * MI_WallB_01 (Shader)
    * SM_CeilingA_6X23 (Xform)
      * SM_CeilingA_6X23 (Xform)
        * SM_CeilingA_6X6 (Mesh)
        * Looks (Scope)
          * MI_WallB_01 (Material)
            * MI_WallB_01 (Shader)
    * SM_CeilingA_6X25 (Xform)
      * SM_CeilingA_6X25 (Xform)
        * SM_CeilingA_6X6 (Mesh)
        * Looks (Scope)
          * MI_WallB_01 (Material)
            * MI_WallB_01 (Shader)
    * SM_CeilingA_6X27 (Xform)
      * SM_CeilingA_6X27 (Xform)
        * SM_CeilingA_6X6 (Mesh)
        * Looks (Scope)
          * MI_WallB_01 (Material)
            * MI_WallB_01 (Shader)
    * SM_CeilingA_6X28 (Xform)
      * SM_CeilingA_6X28 (Xform)
        * SM_CeilingA_6X6 (Mesh)
        * Looks (Scope)
          * MI_WallB_01 (Material)
            * MI_WallB_01 (Shader)
    * SM_CeilingA_6X29 (Xform)
      * SM_CeilingA_6X29 (Xform)
        * SM_CeilingA_6X6 (Mesh)
        * Looks (Scope)
          * MI_WallB_01 (Material)
            * MI_WallB_01 (Shader)
    * SM_CeilingA_6X30 (Xform)
      * SM_CeilingA_6X30 (Xform)
        * SM_CeilingA_6X6 (Mesh)
        * Looks (Scope)
          * MI_WallB_01 (Material)
            * MI_WallB_01 (Shader)
    * SM_CeilingA_6X31 (Xform)
      * SM_CeilingA_6X31 (Xform)
        * SM_CeilingA_6X6 (Mesh)
        * Looks (Scope)
          * MI_WallB_01 (Material)
            * MI_WallB_01 (Shader)
    * SM_CeilingA_6X34 (Xform)
      * SM_CeilingA_6X34 (Xform)
        * SM_CeilingA_6X6 (Mesh)
        * Looks (Scope)
          * MI_WallB_01 (Material)
            * MI_WallB_01 (Shader)
    * SM_CeilingA_6X36 (Xform)
      * SM_CeilingA_6X36 (Xform)
        * SM_CeilingA_6X6 (Mesh)
        * Looks (Scope)
          * MI_WallB_01 (Material)
            * MI_WallB_01 (Shader)
    * SM_CeilingA_6X37 (Xform)
      * SM_CeilingA_6X37 (Xform)
        * SM_CeilingA_6X6 (Mesh)
        * Looks (Scope)
          * MI_WallB_01 (Material)
            * MI_WallB_01 (Shader)
    * SM_CeilingA_6X38 (Xform)
      * SM_CeilingA_6X38 (Xform)
        * SM_CeilingA_6X6 (Mesh)
        * Looks (Scope)
          * MI_WallB_01 (Material)
            * MI_WallB_01 (Shader)
    * SM_CeilingA_6X39 (Xform)
      * SM_CeilingA_6X39 (Xform)
        * SM_CeilingA_6X6 (Mesh)
        * Looks (Scope)
          * MI_WallB_01 (Material)
            * MI_WallB_01 (Shader)
    * SM_CeilingA_6X40 (Xform)
      * SM_CeilingA_6X40 (Xform)
        * SM_CeilingA_6X6 (Mesh)
        * Looks (Scope)
          * MI_WallB_01 (Material)
            * MI_WallB_01 (Shader)
    * SM_CeilingA_6X41 (Xform)
      * SM_CeilingA_6X41 (Xform)
        * SM_CeilingA_6X6 (Mesh)
        * Looks (Scope)
          * MI_WallB_01 (Material)
            * MI_WallB_01 (Shader)
    * SM_CeilingA_6X42 (Xform)
      * SM_CeilingA_6X42 (Xform)
        * SM_CeilingA_6X6 (Mesh)
        * Looks (Scope)
          * MI_WallB_01 (Material)
            * MI_WallB_01 (Shader)
    * SM_CeilingA_6X43 (Xform)
      * SM_CeilingA_6X43 (Xform)
        * SM_CeilingA_6X6 (Mesh)
        * Looks (Scope)
          * MI_WallB_01 (Material)
            * MI_WallB_01 (Shader)
    * SM_CeilingA_6X58 (Xform)
      * SM_CeilingA_6X58 (Xform)
        * SM_CeilingA_6X6 (Mesh)
        * Looks (Scope)
          * MI_WallB_01 (Material)
            * MI_WallB_01 (Shader)
    * SM_CeilingA_6X75 (Xform)
      * SM_CeilingA_6X75 (Xform)
        * SM_CeilingA_6X6 (Mesh)
        * Looks (Scope)
          * MI_WallB_01 (Material)
            * MI_WallB_01 (Shader)
    * SM_CeilingA_6X76 (Xform)
      * SM_CeilingA_6X76 (Xform)
        * SM_CeilingA_6X6 (Mesh)
        * Looks (Scope)
          * MI_WallB_01 (Material)
            * MI_WallB_01 (Shader)
    * SM_CeilingA_6X77 (Xform)
      * SM_CeilingA_6X77 (Xform)
        * SM_CeilingA_6X6 (Mesh)
        * Looks (Scope)
          * MI_WallB_01 (Material)
            * MI_WallB_01 (Shader)
    * SM_CeilingA_6X84 (Xform)
      * SM_CeilingA_6X84 (Xform)
        * SM_CeilingA_6X6 (Mesh)
        * Looks (Scope)
          * MI_WallB_01 (Material)
            * MI_WallB_01 (Shader)
    * SM_FloorDecal_Keepclear6_446 (Xform)
      * SM_FloorDecal_Keepclear6_446 (Xform)
        * SM_FloorDecal_Keepclear (Mesh)
        * Looks (Scope)
          * M_FloorStripes_01 (Material)
            * M_WallBoard_01 (Shader)
    * SM_FloorDecal_RecRed1X15 (Xform)
      * SM_FloorDecal_RecRed1X15 (Xform)
        * SM_FloorDecal_RecRed1X1 (Mesh)
        * Looks (Scope)
          * M_FloorStripes_01 (Material)
            * M_WallBoard_01 (Shader)
    * SM_FloorDecal_RecRed1X16 (Xform)
      * SM_FloorDecal_RecRed1X16 (Xform)
        * SM_FloorDecal_RecRed1X1 (Mesh)
        * Looks (Scope)
          * M_FloorStripes_01 (Material)
            * M_WallBoard_01 (Shader)
    * SM_FloorDecal_StripeFull_4m74 (Xform)
      * SM_FloorDecal_StripeFull_4m74 (Xform)
        * SM_FloorDecal_StripeFull_4m (Mesh)
        * Looks (Scope)
          * M_FloorStripes_01 (Material)
            * M_WallBoard_01 (Shader)
    * SM_FloorDecal_StripeFull_4m75 (Xform)
      * SM_FloorDecal_StripeFull_4m75 (Xform)
        * SM_FloorDecal_StripeFull_4m (Mesh)
        * Looks (Scope)
          * M_FloorStripes_01 (Material)
            * M_WallBoard_01 (Shader)
    * SM_FloorDecal_StripeFull_4m76 (Xform)
      * SM_FloorDecal_StripeFull_4m76 (Xform)
        * SM_FloorDecal_StripeFull_4m (Mesh)
        * Looks (Scope)
          * M_FloorStripes_01 (Material)
            * M_WallBoard_01 (Shader)
    * SM_FloorDecal_StripeFull_4m77 (Xform)
      * SM_FloorDecal_StripeFull_4m77 (Xform)
        * SM_FloorDecal_StripeFull_4m (Mesh)
        * Looks (Scope)
          * M_FloorStripes_01 (Material)
            * M_WallBoard_01 (Shader)
    * SM_FloorDecal_StripeFull_4m78 (Xform)
      * SM_FloorDecal_StripeFull_4m78 (Xform)
        * SM_FloorDecal_StripeFull_4m (Mesh)
        * Looks (Scope)
          * M_FloorStripes_01 (Material)
            * M_WallBoard_01 (Shader)
    * SM_FloorDecal_StripeFull_4m79 (Xform)
      * SM_FloorDecal_StripeFull_4m79 (Xform)
        * SM_FloorDecal_StripeFull_4m (Mesh)
        * Looks (Scope)
          * M_FloorStripes_01 (Material)
            * M_WallBoard_01 (Shader)
    * SM_FloorDecal_StripeFull_4m80 (Xform)
      * SM_FloorDecal_StripeFull_4m80 (Xform)
        * SM_FloorDecal_StripeFull_4m (Mesh)
        * Looks (Scope)
          * M_FloorStripes_01 (Material)
            * M_WallBoard_01 (Shader)
    * SM_FloorDecal_StripeFull_4m81 (Xform)
      * SM_FloorDecal_StripeFull_4m81 (Xform)
        * SM_FloorDecal_StripeFull_4m (Mesh)
        * Looks (Scope)
          * M_FloorStripes_01 (Material)
            * M_WallBoard_01 (Shader)
    * SM_FuseBox_24 (Xform)
      * SM_FuseBox_24 (Xform)
        * SM_FuseBox_01 (Mesh)
        * Looks (Scope)
          * MI_WallDetails_01 (Material)
            * MI_LampCeilingA (Shader)
    * SM_FuseBox_25 (Xform)
      * SM_FuseBox_25 (Xform)
        * SM_FuseBox_04 (Mesh)
        * Looks (Scope)
          * MI_WallDetails_01 (Material)
            * MI_LampCeilingA (Shader)
    * SM_LampCeilingA_23 (Xform)
      * SM_LampCeilingA_23 (Xform)
        * SM_LampCeilingA_04 (Xform)
          * Section0 (Mesh)
          * Section1 (Mesh)
        * Looks (Scope)
          * MI_LampCeilingA (Material)
            * MI_LampCeilingA (Shader)
          * M_Glow (Material)
            * M_Glow (Shader)
        * RectLight (RectLight)
    * SM_LampCeilingA_24 (Xform)
      * SM_LampCeilingA_24 (Xform)
        * SM_LampCeilingA_04 (Xform)
          * Section0 (Mesh)
          * Section1 (Mesh)
        * Looks (Scope)
          * MI_LampCeilingA (Material)
            * MI_LampCeilingA (Shader)
          * M_Glow (Material)
            * M_Glow (Shader)
        * RectLight (RectLight)
    * SM_LampCeilingA_25 (Xform)
      * SM_LampCeilingA_25 (Xform)
        * SM_LampCeilingA_04 (Xform)
          * Section0 (Mesh)
          * Section1 (Mesh)
        * Looks (Scope)
          * MI_LampCeilingA (Material)
            * MI_LampCeilingA (Shader)
          * M_Glow (Material)
            * M_Glow (Shader)
        * RectLight (RectLight)
    * SM_LampCeilingA_33 (Xform)
      * SM_LampCeilingA_33 (Xform)
        * SM_LampCeilingA_04 (Xform)
          * Section0 (Mesh)
          * Section1 (Mesh)
        * Looks (Scope)
          * MI_LampCeilingA (Material)
            * MI_LampCeilingA (Shader)
          * M_Glow (Material)
            * M_Glow (Shader)
        * RectLight (RectLight)
    * SM_LampCeilingA_35 (Xform)
      * SM_LampCeilingA_35 (Xform)
        * SM_LampCeilingA_04 (Xform)
          * Section0 (Mesh)
          * Section1 (Mesh)
        * Looks (Scope)
          * MI_LampCeilingA (Material)
            * MI_LampCeilingA (Shader)
          * M_Glow (Material)
            * M_Glow (Shader)
        * RectLight (RectLight)
    * SM_LampCeilingA_36 (Xform)
      * SM_LampCeilingA_36 (Xform)
        * SM_LampCeilingA_04 (Xform)
          * Section0 (Mesh)
          * Section1 (Mesh)
        * Looks (Scope)
          * MI_LampCeilingA (Material)
            * MI_LampCeilingA (Shader)
          * M_Glow (Material)
            * M_Glow (Shader)
        * RectLight (RectLight)
    * SM_LampCeilingA_37 (Xform)
      * SM_LampCeilingA_37 (Xform)
        * SM_LampCeilingA_04 (Xform)
          * Section0 (Mesh)
          * Section1 (Mesh)
        * Looks (Scope)
          * MI_LampCeilingA (Material)
            * MI_LampCeilingA (Shader)
          * M_Glow (Material)
            * M_Glow (Shader)
        * RectLight (RectLight)
    * SM_LampCeilingA_38 (Xform)
      * SM_LampCeilingA_38 (Xform)
        * SM_LampCeilingA_04 (Xform)
          * Section0 (Mesh)
          * Section1 (Mesh)
        * Looks (Scope)
          * MI_LampCeilingA (Material)
            * MI_LampCeilingA (Shader)
          * M_Glow (Material)
            * M_Glow (Shader)
        * RectLight (RectLight)
    * SM_LampCeilingA_39 (Xform)
      * SM_LampCeilingA_39 (Xform)
        * SM_LampCeilingA_04 (Xform)
          * Section0 (Mesh)
          * Section1 (Mesh)
        * Looks (Scope)
          * MI_LampCeilingA (Material)
            * MI_LampCeilingA (Shader)
          * M_Glow (Material)
            * M_Glow (Shader)
        * RectLight (RectLight)
    * SM_LampCeilingA_40 (Xform)
      * SM_LampCeilingA_40 (Xform)
        * SM_LampCeilingA_04 (Xform)
          * Section0 (Mesh)
          * Section1 (Mesh)
        * Looks (Scope)
          * MI_LampCeilingA (Material)
            * MI_LampCeilingA (Shader)
          * M_Glow (Material)
            * M_Glow (Shader)
        * RectLight (RectLight)
    * SM_LampCeilingA_41 (Xform)
      * SM_LampCeilingA_41 (Xform)
        * SM_LampCeilingA_04 (Xform)
          * Section0 (Mesh)
          * Section1 (Mesh)
        * Looks (Scope)
          * MI_LampCeilingA (Material)
            * MI_LampCeilingA (Shader)
          * M_Glow (Material)
            * M_Glow (Shader)
        * RectLight (RectLight)
    * SM_LampCeilingA_42 (Xform)
      * SM_LampCeilingA_42 (Xform)
        * SM_LampCeilingA_04 (Xform)
          * Section0 (Mesh)
          * Section1 (Mesh)
        * Looks (Scope)
          * MI_LampCeilingA (Material)
            * MI_LampCeilingA (Shader)
          * M_Glow (Material)
            * M_Glow (Shader)
        * RectLight (RectLight)
    * SM_LampCeilingA_43 (Xform)
      * SM_LampCeilingA_43 (Xform)
        * SM_LampCeilingA_04 (Xform)
          * Section0 (Mesh)
          * Section1 (Mesh)
        * Looks (Scope)
          * MI_LampCeilingA (Material)
            * MI_LampCeilingA (Shader)
          * M_Glow (Material)
            * M_Glow (Shader)
        * RectLight (RectLight)
    * SM_LampCeilingA_44 (Xform)
      * SM_LampCeilingA_44 (Xform)
        * SM_LampCeilingA_04 (Xform)
          * Section0 (Mesh)
          * Section1 (Mesh)
        * Looks (Scope)
          * MI_LampCeilingA (Material)
            * MI_LampCeilingA (Shader)
          * M_Glow (Material)
            * M_Glow (Shader)
        * RectLight (RectLight)
    * SM_LampCeilingA_45 (Xform)
      * SM_LampCeilingA_45 (Xform)
        * SM_LampCeilingA_04 (Xform)
          * Section0 (Mesh)
          * Section1 (Mesh)
        * Looks (Scope)
          * MI_LampCeilingA (Material)
            * MI_LampCeilingA (Shader)
          * M_Glow (Material)
            * M_Glow (Shader)
        * RectLight (RectLight)
    * SM_LampCeilingA_46 (Xform)
      * SM_LampCeilingA_46 (Xform)
        * SM_LampCeilingA_04 (Xform)
          * Section0 (Mesh)
          * Section1 (Mesh)
        * Looks (Scope)
          * MI_LampCeilingA (Material)
            * MI_LampCeilingA (Shader)
          * M_Glow (Material)
            * M_Glow (Shader)
        * RectLight (RectLight)
    * SM_PaletteA_360 (Xform)
      * SM_PaletteA_360 (Xform)
        * SM_PaletteA_01 (Mesh)
        * Looks (Scope)
          * MI_PaletteSmallA_01 (Material)
            * MI_CeilingA_06b (Shader)
    * SM_PillarA_9M4 (Xform)
      * SM_PillarA_9M4 (Xform)
        * SM_PillarA_9M (Mesh)
        * Looks (Scope)
          * MI_BeamsA_01 (Material)
            * MI_CeilingA_06b (Shader)
    * SM_PillarA_9M4_01 (Xform)
      * SM_PillarA_9M4_01 (Xform)
        * SM_PillarA_9M (Mesh)
        * Looks (Scope)
          * MI_BeamsA_01 (Material)
            * MI_CeilingA_06b (Shader)
    * SM_PillarA_9M4_02 (Xform)
      * SM_PillarA_9M4_02 (Xform)
        * SM_PillarA_9M (Mesh)
        * Looks (Scope)
          * MI_BeamsA_01 (Material)
            * MI_CeilingA_06b (Shader)
    * SM_PillarA_9M4_03 (Xform)
      * SM_PillarA_9M4_03 (Xform)
        * SM_PillarA_9M (Mesh)
        * Looks (Scope)
          * MI_BeamsA_01 (Material)
            * MI_CeilingA_06b (Shader)
    * SM_PillarA_9M4_04 (Xform)
      * SM_PillarA_9M4_04 (Xform)
        * SM_PillarA_9M (Mesh)
        * Looks (Scope)
          * MI_BeamsA_01 (Material)
            * MI_CeilingA_06b (Shader)
    * SM_PillarPartA_9M10_1473 (Xform)
      * SM_PillarPartA_9M10_1473 (Xform)
        * SM_PillarPartA_9M (Xform)
          * Section0 (Mesh)
          * Section1 (Mesh)
        * Looks (Scope)
          * MI_BeamsA_01 (Material)
            * MI_CeilingA_06b (Shader)
          * MI_FrameA_01 (Material)
            * MI_FrameA_01 (Shader)
    * SM_PillarPartA_9M11_1481 (Xform)
      * SM_PillarPartA_9M11_1481 (Xform)
        * SM_PillarPartA_9M (Xform)
          * Section0 (Mesh)
          * Section1 (Mesh)
        * Looks (Scope)
          * MI_BeamsA_01 (Material)
            * MI_CeilingA_06b (Shader)
          * MI_FrameA_01 (Material)
            * MI_FrameA_01 (Shader)
    * SM_PillarPartA_9M12_1482 (Xform)
      * SM_PillarPartA_9M12_1482 (Xform)
        * SM_PillarPartA_9M (Xform)
          * Section0 (Mesh)
          * Section1 (Mesh)
        * Looks (Scope)
          * MI_BeamsA_01 (Material)
            * MI_CeilingA_06b (Shader)
          * MI_FrameA_01 (Material)
            * MI_FrameA_01 (Shader)
    * SM_PillarPartA_9M3_1445 (Xform)
      * SM_PillarPartA_9M3_1445 (Xform)
        * SM_PillarPartA_9M (Xform)
          * Section0 (Mesh)
          * Section1 (Mesh)
        * Looks (Scope)
          * MI_BeamsA_01 (Material)
            * MI_CeilingA_06b (Shader)
          * MI_FrameA_01 (Material)
            * MI_FrameA_01 (Shader)
    * SM_PillarPartA_9M4_1446 (Xform)
      * SM_PillarPartA_9M4_1446 (Xform)
        * SM_PillarPartA_9M (Xform)
          * Section0 (Mesh)
          * Section1 (Mesh)
        * Looks (Scope)
          * MI_BeamsA_01 (Material)
            * MI_CeilingA_06b (Shader)
          * MI_FrameA_01 (Material)
            * MI_FrameA_01 (Shader)
    * SM_PillarPartA_9M5_1454 (Xform)
      * SM_PillarPartA_9M5_1454 (Xform)
        * SM_PillarPartA_9M (Xform)
          * Section0 (Mesh)
          * Section1 (Mesh)
        * Looks (Scope)
          * MI_BeamsA_01 (Material)
            * MI_CeilingA_06b (Shader)
          * MI_FrameA_01 (Material)
            * MI_FrameA_01 (Shader)
    * SM_PillarPartA_9M6_1455 (Xform)
      * SM_PillarPartA_9M6_1455 (Xform)
        * SM_PillarPartA_9M (Xform)
          * Section0 (Mesh)
          * Section1 (Mesh)
        * Looks (Scope)
          * MI_BeamsA_01 (Material)
            * MI_CeilingA_06b (Shader)
          * MI_FrameA_01 (Material)
            * MI_FrameA_01 (Shader)
    * SM_PillarPartA_9M7_1463 (Xform)
      * SM_PillarPartA_9M7_1463 (Xform)
        * SM_PillarPartA_9M (Xform)
          * Section0 (Mesh)
          * Section1 (Mesh)
        * Looks (Scope)
          * MI_BeamsA_01 (Material)
            * MI_CeilingA_06b (Shader)
          * MI_FrameA_01 (Material)
            * MI_FrameA_01 (Shader)
    * SM_PillarPartA_9M8_1464 (Xform)
      * SM_PillarPartA_9M8_1464 (Xform)
        * SM_PillarPartA_9M (Xform)
          * Section0 (Mesh)
          * Section1 (Mesh)
        * Looks (Scope)
          * MI_BeamsA_01 (Material)
            * MI_CeilingA_06b (Shader)
          * MI_FrameA_01 (Material)
            * MI_FrameA_01 (Shader)
    * SM_PillarPartA_9M9_1472 (Xform)
      * SM_PillarPartA_9M9_1472 (Xform)
        * SM_PillarPartA_9M (Xform)
          * Section0 (Mesh)
          * Section1 (Mesh)
        * Looks (Scope)
          * MI_BeamsA_01 (Material)
            * MI_CeilingA_06b (Shader)
          * MI_FrameA_01 (Material)
            * MI_FrameA_01 (Shader)
    * SM_PushcartA_02_22 (Xform)
      * SM_PushcartA_02_22 (Xform)
        * SM_PushcartA_02 (Mesh)
        * Looks (Scope)
          * MI_PushcartA_01 (Material)
            * MI_PushcartA_01 (Shader)
    * SM_SignA_27 (Xform)
      * SM_SignA_27 (Xform)
        * SM_SignA_02 (Mesh)
        * Looks (Scope)
          * M_SignA (Material)
            * MI_SignB (Shader)
    * SM_SignB_23 (Xform)
      * SM_SignB_23 (Xform)
        * SM_SignB_11 (Mesh)
        * Looks (Scope)
          * MI_SignB (Material)
            * MI_SignB (Shader)
    * SM_SignB_3 (Xform)
      * SM_SignB_3 (Xform)
        * SM_SignB_02 (Mesh)
        * Looks (Scope)
          * MI_SignB (Material)
            * MI_SignB (Shader)
    * SM_WallA_3M13 (Xform)
      * SM_WallA_3M13 (Xform)
        * SM_WallB_6M (Mesh)
        * Looks (Scope)
          * MI_CeilingA_01 (Material)
            * MI_CeilingA_06b (Shader)
    * SM_WallA_3M13_01 (Xform)
      * SM_WallA_3M13_01 (Xform)
        * SM_WallB_6M (Mesh)
        * Looks (Scope)
          * MI_CeilingA_01 (Material)
            * MI_CeilingA_06b (Shader)
    * SM_WallA_3M14 (Xform)
      * SM_WallA_3M14 (Xform)
        * SM_WallB_6M (Mesh)
        * Looks (Scope)
          * MI_CeilingA_01 (Material)
            * MI_CeilingA_06b (Shader)
    * SM_WallA_3M14_01 (Xform)
      * SM_WallA_3M14_01 (Xform)
        * SM_WallB_6M (Mesh)
        * Looks (Scope)
          * MI_CeilingA_01 (Material)
            * MI_CeilingA_06b (Shader)
    * SM_WallA_3M15 (Xform)
      * SM_WallA_3M15 (Xform)
        * SM_WallB_6M (Mesh)
        * Looks (Scope)
          * MI_CeilingA_01 (Material)
            * MI_CeilingA_06b (Shader)
    * SM_WallA_3M16 (Xform)
      * SM_WallA_3M16 (Xform)
        * SM_WallB_6M (Mesh)
        * Looks (Scope)
          * MI_CeilingA_01 (Material)
            * MI_CeilingA_06b (Shader)
    * SM_WallA_3M18_460 (Xform)
      * SM_WallA_3M18_460 (Xform)
        * SM_WallB_6M (Mesh)
        * Looks (Scope)
          * MI_CeilingA_01 (Material)
            * MI_CeilingA_06b (Shader)
    * SM_WallA_3M19 (Xform)
      * SM_WallA_3M19 (Xform)
        * SM_WallB_6M (Mesh)
        * Looks (Scope)
          * MI_CeilingA_01 (Material)
            * MI_CeilingA_06b (Shader)
    * SM_WallA_3M20 (Xform)
      * SM_WallA_3M20 (Xform)
        * SM_WallB_6M (Mesh)
        * Looks (Scope)
          * MI_CeilingA_01 (Material)
            * MI_CeilingA_06b (Shader)
    * SM_WallA_3M21_1371 (Xform)
      * SM_WallA_3M21_1371 (Xform)
        * SM_WallB_6M (Mesh)
        * Looks (Scope)
          * MI_CeilingA_01 (Material)
            * MI_CeilingA_06b (Shader)
    * SM_WallA_3M26 (Xform)
      * SM_WallA_3M26 (Xform)
        * SM_WallB_6M (Mesh)
        * Looks (Scope)
          * MI_CeilingA_01 (Material)
            * MI_CeilingA_06b (Shader)
    * SM_WallA_3M27 (Xform)
      * SM_WallA_3M27 (Xform)
        * SM_WallB_6M (Mesh)
        * Looks (Scope)
          * MI_CeilingA_01 (Material)
            * MI_CeilingA_06b (Shader)
    * SM_WallA_3M28 (Xform)
      * SM_WallA_3M28 (Xform)
        * SM_WallB_6M (Mesh)
        * Looks (Scope)
          * MI_CeilingA_01 (Material)
            * MI_CeilingA_06b (Shader)
    * SM_WallA_3M36 (Xform)
      * SM_WallA_3M36 (Xform)
        * SM_WallB_6M (Mesh)
        * Looks (Scope)
          * MI_CeilingA_01 (Material)
            * MI_CeilingA_06b (Shader)
    * SM_WallA_3M37 (Xform)
      * SM_WallA_3M37 (Xform)
        * SM_WallB_6M (Mesh)
        * Looks (Scope)
          * MI_CeilingA_01 (Material)
            * MI_CeilingA_06b (Shader)
    * SM_WallA_3M38 (Xform)
      * SM_WallA_3M38 (Xform)
        * SM_WallB_6M (Mesh)
        * Looks (Scope)
          * MI_CeilingA_01 (Material)
            * MI_CeilingA_06b (Shader)
    * SM_WallA_3M39 (Xform)
      * SM_WallA_3M39 (Xform)
        * SM_WallB_6M (Mesh)
        * Looks (Scope)
          * MI_CeilingA_01 (Material)
            * MI_CeilingA_06b (Shader)
    * SM_WallA_3M40 (Xform)
      * SM_WallA_3M40 (Xform)
        * SM_WallB_6M (Mesh)
        * Looks (Scope)
          * MI_CeilingA_01 (Material)
            * MI_CeilingA_06b (Shader)
    * SM_WallA_3M41 (Xform)
      * SM_WallA_3M41 (Xform)
        * SM_WallB_6M (Mesh)
        * Looks (Scope)
          * MI_CeilingA_01 (Material)
            * MI_CeilingA_06b (Shader)
    * SM_WallA_3M43 (Xform)
      * SM_WallA_3M43 (Xform)
        * SM_WallA_6M (Xform)
          * Section0 (Mesh)
          * Section1 (Mesh)
        * Looks (Scope)
          * MI_WallA_01 (Material)
            * MI_Floor_01 (Shader)
          * MI_BeamsA_02 (Material)
            * MI_CeilingA_06b (Shader)
    * SM_WallA_3M43_01 (Xform)
      * SM_WallA_3M43_01 (Xform)
        * SM_WallA_6M (Xform)
          * Section0 (Mesh)
          * Section1 (Mesh)
        * Looks (Scope)
          * MI_WallA_01 (Material)
            * MI_Floor_01 (Shader)
          * MI_BeamsA_02 (Material)
            * MI_CeilingA_06b (Shader)
    * SM_WallA_3M44 (Xform)
      * SM_WallA_3M44 (Xform)
        * SM_WallA_6M (Xform)
          * Section0 (Mesh)
          * Section1 (Mesh)
        * Looks (Scope)
          * MI_WallA_01 (Material)
            * MI_Floor_01 (Shader)
          * MI_BeamsA_02 (Material)
            * MI_CeilingA_06b (Shader)
    * SM_WallA_3M8 (Xform)
      * SM_WallA_3M8 (Xform)
        * SM_WallB_6M (Mesh)
        * Looks (Scope)
          * MI_CeilingA_01 (Material)
            * MI_CeilingA_06b (Shader)
    * SM_WallA_6M10 (Xform)
      * SM_WallA_6M10 (Xform)
        * SM_WallA_6M (Xform)
          * Section0 (Mesh)
          * Section1 (Mesh)
        * Looks (Scope)
          * MI_WallA_01 (Material)
            * MI_Floor_01 (Shader)
          * MI_BeamsA_02 (Material)
            * MI_CeilingA_06b (Shader)
    * SM_WallA_6M11 (Xform)
      * SM_WallA_6M11 (Xform)
        * SM_WallA_6M (Xform)
          * Section0 (Mesh)
          * Section1 (Mesh)
        * Looks (Scope)
          * MI_WallA_01 (Material)
            * MI_Floor_01 (Shader)
          * MI_BeamsA_02 (Material)
            * MI_CeilingA_06b (Shader)
    * SM_WallA_6M12 (Xform)
      * SM_WallA_6M12 (Xform)
        * SM_WallA_6M (Xform)
          * Section0 (Mesh)
          * Section1 (Mesh)
        * Looks (Scope)
          * MI_WallA_01 (Material)
            * MI_Floor_01 (Shader)
          * MI_BeamsA_02 (Material)
            * MI_CeilingA_06b (Shader)
    * SM_WallA_6M15 (Xform)
      * SM_WallA_6M15 (Xform)
        * SM_WallA_6M (Xform)
          * Section0 (Mesh)
          * Section1 (Mesh)
        * Looks (Scope)
          * MI_WallA_01 (Material)
            * MI_Floor_01 (Shader)
          * MI_BeamsA_02 (Material)
            * MI_CeilingA_06b (Shader)
    * SM_WallA_6M16 (Xform)
      * SM_WallA_6M16 (Xform)
        * SM_WallA_6M (Xform)
          * Section0 (Mesh)
          * Section1 (Mesh)
        * Looks (Scope)
          * MI_WallA_01 (Material)
            * MI_Floor_01 (Shader)
          * MI_BeamsA_02 (Material)
            * MI_CeilingA_06b (Shader)
    * SM_WallA_6M17 (Xform)
      * SM_WallA_6M17 (Xform)
        * SM_WallA_6M (Xform)
          * Section0 (Mesh)
          * Section1 (Mesh)
        * Looks (Scope)
          * MI_WallA_01 (Material)
            * MI_Floor_01 (Shader)
          * MI_BeamsA_02 (Material)
            * MI_CeilingA_06b (Shader)
    * SM_WallA_6M18 (Xform)
      * SM_WallA_6M18 (Xform)
        * SM_WallA_6M (Xform)
          * Section0 (Mesh)
          * Section1 (Mesh)
        * Looks (Scope)
          * MI_WallA_01 (Material)
            * MI_Floor_01 (Shader)
          * MI_BeamsA_02 (Material)
            * MI_CeilingA_06b (Shader)
    * SM_WallA_6M4 (Xform)
      * SM_WallA_6M4 (Xform)
        * SM_WallA_6M (Xform)
          * Section0 (Mesh)
          * Section1 (Mesh)
        * Looks (Scope)
          * MI_WallA_01 (Material)
            * MI_Floor_01 (Shader)
          * MI_BeamsA_02 (Material)
            * MI_CeilingA_06b (Shader)
    * SM_WallA_6M5 (Xform)
      * SM_WallA_6M5 (Xform)
        * SM_WallA_6M (Xform)
          * Section0 (Mesh)
          * Section1 (Mesh)
        * Looks (Scope)
          * MI_WallA_01 (Material)
            * MI_Floor_01 (Shader)
          * MI_BeamsA_02 (Material)
            * MI_CeilingA_06b (Shader)
    * SM_WallA_6M6 (Xform)
      * SM_WallA_6M6 (Xform)
        * SM_WallA_6M (Xform)
          * Section0 (Mesh)
          * Section1 (Mesh)
        * Looks (Scope)
          * MI_WallA_01 (Material)
            * MI_Floor_01 (Shader)
          * MI_BeamsA_02 (Material)
            * MI_CeilingA_06b (Shader)
    * SM_WallA_6M7 (Xform)
      * SM_WallA_6M7 (Xform)
        * SM_WallA_6M (Xform)
          * Section0 (Mesh)
          * Section1 (Mesh)
        * Looks (Scope)
          * MI_WallA_01 (Material)
            * MI_Floor_01 (Shader)
          * MI_BeamsA_02 (Material)
            * MI_CeilingA_06b (Shader)
    * SM_WallA_InnerCorner10 (Xform)
      * SM_WallA_InnerCorner10 (Xform)
        * SM_WallA_InnerCorner (Xform)
          * Section0 (Mesh)
          * Section1 (Mesh)
        * Looks (Scope)
          * MI_WallA_01 (Material)
            * MI_Floor_01 (Shader)
          * MI_BeamsA_02 (Material)
            * MI_CeilingA_06b (Shader)
    * SM_WallA_InnerCorner11 (Xform)
      * SM_WallA_InnerCorner11 (Xform)
        * SM_WallA_InnerCorner (Xform)
          * Section0 (Mesh)
          * Section1 (Mesh)
        * Looks (Scope)
          * MI_WallA_01 (Material)
            * MI_Floor_01 (Shader)
          * MI_BeamsA_02 (Material)
            * MI_CeilingA_06b (Shader)
    * SM_WallA_InnerCorner12 (Xform)
      * SM_WallA_InnerCorner12 (Xform)
        * SM_WallA_InnerCorner (Xform)
          * Section0 (Mesh)
          * Section1 (Mesh)
        * Looks (Scope)
          * MI_WallA_01 (Material)
            * MI_Floor_01 (Shader)
          * MI_BeamsA_02 (Material)
            * MI_CeilingA_06b (Shader)
    * SM_WallA_InnerCorner13 (Xform)
      * SM_WallA_InnerCorner13 (Xform)
        * SM_WallB_InnerCorner (Mesh)
        * Looks (Scope)
          * MI_CeilingA_01 (Material)
            * MI_CeilingA_06b (Shader)
    * SM_WallA_InnerCorner14 (Xform)
      * SM_WallA_InnerCorner14 (Xform)
        * SM_WallB_InnerCorner (Mesh)
        * Looks (Scope)
          * MI_CeilingA_01 (Material)
            * MI_CeilingA_06b (Shader)
    * SM_WallA_InnerCorner15 (Xform)
      * SM_WallA_InnerCorner15 (Xform)
        * SM_WallB_InnerCorner (Mesh)
        * Looks (Scope)
          * MI_CeilingA_01 (Material)
            * MI_CeilingA_06b (Shader)
    * SM_WallA_InnerCorner16 (Xform)
      * SM_WallA_InnerCorner16 (Xform)
        * SM_WallB_InnerCorner (Mesh)
        * Looks (Scope)
          * MI_CeilingA_01 (Material)
            * MI_CeilingA_06b (Shader)
    * SM_WallA_InnerCorner18 (Xform)
      * SM_WallA_InnerCorner18 (Xform)
        * SM_WallB_6M (Mesh)
        * Looks (Scope)
          * MI_CeilingA_01 (Material)
            * MI_CeilingA_06b (Shader)
    * SM_WallA_InnerCorner24 (Xform)
      * SM_WallA_InnerCorner24 (Xform)
        * SM_WallB_6M (Mesh)
        * Looks (Scope)
          * MI_CeilingA_01 (Material)
            * MI_CeilingA_06b (Shader)
    * SM_WallA_InnerCorner25 (Xform)
      * SM_WallA_InnerCorner25 (Xform)
        * SM_WallB_6M (Mesh)
        * Looks (Scope)
          * MI_CeilingA_01 (Material)
            * MI_CeilingA_06b (Shader)
    * SM_WallA_InnerCorner26 (Xform)
      * SM_WallA_InnerCorner26 (Xform)
        * SM_WallB_6M (Mesh)
        * Looks (Scope)
          * MI_CeilingA_01 (Material)
            * MI_CeilingA_06b (Shader)
    * SM_WallA_InnerCorner27 (Xform)
      * SM_WallA_InnerCorner27 (Xform)
        * SM_WallB_InnerCorner (Mesh)
        * Looks (Scope)
          * MI_CeilingA_01 (Material)
            * MI_CeilingA_06b (Shader)
    * SM_WallA_InnerCorner28 (Xform)
      * SM_WallA_InnerCorner28 (Xform)
        * SM_WallB_InnerCorner (Mesh)
        * Looks (Scope)
          * MI_CeilingA_01 (Material)
            * MI_CeilingA_06b (Shader)
    * SM_WallA_InnerCorner29 (Xform)
      * SM_WallA_InnerCorner29 (Xform)
        * SM_WallB_InnerCorner (Mesh)
        * Looks (Scope)
          * MI_CeilingA_01 (Material)
            * MI_CeilingA_06b (Shader)
    * SM_WallA_InnerCorner30 (Xform)
      * SM_WallA_InnerCorner30 (Xform)
        * SM_WallB_6M (Mesh)
        * Looks (Scope)
          * MI_CeilingA_01 (Material)
            * MI_CeilingA_06b (Shader)
    * SM_WallA_InnerCorner32 (Xform)
      * SM_WallA_InnerCorner32 (Xform)
        * SM_WallB_6M (Mesh)
        * Looks (Scope)
          * MI_CeilingA_01 (Material)
            * MI_CeilingA_06b (Shader)
    * SM_WallA_InnerCorner33 (Xform)
      * SM_WallA_InnerCorner33 (Xform)
        * SM_WallB_6M (Mesh)
        * Looks (Scope)
          * MI_CeilingA_01 (Material)
            * MI_CeilingA_06b (Shader)
    * SM_WallA_InnerCorner34 (Xform)
      * SM_WallA_InnerCorner34 (Xform)
        * SM_WallB_6M (Mesh)
        * Looks (Scope)
          * MI_CeilingA_01 (Material)
            * MI_CeilingA_06b (Shader)
    * SM_WallA_InnerCorner35 (Xform)
      * SM_WallA_InnerCorner35 (Xform)
        * SM_WallB_InnerCorner (Mesh)
        * Looks (Scope)
          * MI_CeilingA_01 (Material)
            * MI_CeilingA_06b (Shader)
    * SM_WallA_InnerCorner9_88 (Xform)
      * SM_WallA_InnerCorner9_88 (Xform)
        * SM_WallA_InnerCorner (Xform)
          * Section0 (Mesh)
          * Section1 (Mesh)
        * Looks (Scope)
          * MI_WallA_01 (Material)
            * MI_Floor_01 (Shader)
          * MI_BeamsA_02 (Material)
            * MI_CeilingA_06b (Shader)
    * SM_WallWire_63 (Xform)
      * SM_WallWire_63 (Xform)
        * SM_WallWire_03 (Mesh)
        * Looks (Scope)
          * MI_WallDetails_01 (Material)
            * MI_LampCeilingA (Shader)
    * SM_WallWire_64 (Xform)
      * SM_WallWire_64 (Xform)
        * SM_WallWire_02 (Mesh)
        * Looks (Scope)
          * MI_WallDetails_01 (Material)
            * MI_LampCeilingA (Shader)
    * SM_WallWire_65 (Xform)
      * SM_WallWire_65 (Xform)
        * SM_WallWire_07 (Mesh)
        * Looks (Scope)
          * MI_WallDetails_01 (Material)
            * MI_LampCeilingA (Shader)
    * SM_WallWire_68 (Xform)
      * SM_WallWire_68 (Xform)
        * SM_WallWire_08 (Mesh)
        * Looks (Scope)
          * MI_WallDetails_01 (Material)
            * MI_LampCeilingA (Shader)
    * SM_WallWire_69 (Xform)
      * SM_WallWire_69 (Xform)
        * SM_WallWire_08 (Mesh)
        * Looks (Scope)
          * MI_WallDetails_01 (Material)
            * MI_LampCeilingA (Shader)
    * SM_WallWire_70 (Xform)
      * SM_WallWire_70 (Xform)
        * SM_WallWire_06 (Mesh)
        * Looks (Scope)
          * MI_WallDetails_01 (Material)
            * MI_LampCeilingA (Shader)
    * SM_WallWire_71 (Xform)
      * SM_WallWire_71 (Xform)
        * SM_WallWire_08 (Mesh)
        * Looks (Scope)
          * MI_WallDetails_01 (Material)
            * MI_LampCeilingA (Shader)
    * SM_WallWire_73 (Xform)
      * SM_WallWire_73 (Xform)
        * SM_WallWire_10 (Mesh)
        * Looks (Scope)
          * MI_WallDetails_01 (Material)
            * MI_LampCeilingA (Shader)
    * SM_WallWire_74 (Xform)
      * SM_WallWire_74 (Xform)
        * SM_WallWire_10 (Mesh)
        * Looks (Scope)
          * MI_WallDetails_01 (Material)
            * MI_LampCeilingA (Shader)
    * SM_floor27 (Xform)
      * SM_floor27 (Xform)
        * SM_floor02 (Mesh)
        * Looks (Scope)
          * MI_Floor_01 (Material)
            * MI_Floor_01 (Shader)
    * SM_floor29 (Xform)
      * SM_floor29 (Xform)
        * SM_floor02 (Mesh)
        * Looks (Scope)
          * MI_Floor_01 (Material)
            * MI_Floor_01 (Shader)
    * SM_floor32 (Xform)
      * SM_floor32 (Xform)
        * SM_floor02 (Mesh)
        * Looks (Scope)
          * MI_Floor_01 (Material)
            * MI_Floor_01 (Shader)
    * SM_floor33 (Xform)
      * SM_floor33 (Xform)
        * SM_floor02 (Mesh)
        * Looks (Scope)
          * MI_Floor_01 (Material)
            * MI_Floor_01 (Shader)
    * SM_floor34 (Xform)
      * SM_floor34 (Xform)
        * SM_floor02 (Mesh)
        * Looks (Scope)
          * MI_Floor_01 (Material)
            * MI_Floor_01 (Shader)
    * SM_floor35 (Xform)
      * SM_floor35 (Xform)
        * SM_floor02 (Mesh)
        * Looks (Scope)
          * MI_Floor_01 (Material)
            * MI_Floor_01 (Shader)
    * SM_floor36 (Xform)
      * SM_floor36 (Xform)
        * SM_floor02 (Mesh)
        * Looks (Scope)
          * MI_Floor_01 (Material)
            * MI_Floor_01 (Shader)
    * SM_floor37 (Xform)
      * SM_floor37 (Xform)
        * SM_floor02 (Mesh)
        * Looks (Scope)
          * MI_Floor_01 (Material)
            * MI_Floor_01 (Shader)
    * SM_floor39 (Xform)
      * SM_floor39 (Xform)
        * SM_floor02 (Mesh)
        * Looks (Scope)
          * MI_Floor_01 (Material)
            * MI_Floor_01 (Shader)
    * SM_floor44 (Xform)
      * SM_floor44 (Xform)
        * SM_floor02 (Mesh)
        * Looks (Scope)
          * MI_Floor_01 (Material)
            * MI_Floor_01 (Shader)
    * SM_floor47 (Xform)
      * SM_floor47 (Xform)
        * SM_floor02 (Mesh)
        * Looks (Scope)
          * MI_Floor_01 (Material)
            * MI_Floor_01 (Shader)
    * SM_floor49 (Xform)
      * SM_floor49 (Xform)
        * SM_floor02 (Mesh)
        * Looks (Scope)
          * MI_Floor_01 (Material)
            * MI_Floor_01 (Shader)
    * SM_floor51 (Xform)
      * SM_floor51 (Xform)
        * SM_floor02 (Mesh)
        * Looks (Scope)
          * MI_Floor_01 (Material)
            * MI_Floor_01 (Shader)
    * SM_floor53 (Xform)
      * SM_floor53 (Xform)
        * SM_floor02 (Mesh)
        * Looks (Scope)
          * MI_Floor_01 (Material)
            * MI_Floor_01 (Shader)
    * SM_floor54 (Xform)
      * SM_floor54 (Xform)
        * SM_floor02 (Mesh)
        * Looks (Scope)
          * MI_Floor_01 (Material)
            * MI_Floor_01 (Shader)
    * SM_floor55 (Xform)
      * SM_floor55 (Xform)
        * SM_floor02 (Mesh)
        * Looks (Scope)
          * MI_Floor_01 (Material)
            * MI_Floor_01 (Shader)
    * SM_floor56 (Xform)
      * SM_floor56 (Xform)
        * SM_floor02 (Mesh)
        * Looks (Scope)
          * MI_Floor_01 (Material)
            * MI_Floor_01 (Shader)
    * SM_floor57 (Xform)
      * SM_floor57 (Xform)
        * SM_floor02 (Mesh)
        * Looks (Scope)
          * MI_Floor_01 (Material)
            * MI_Floor_01 (Shader)
    * SM_floor58 (Xform)
      * SM_floor58 (Xform)
        * SM_floor02 (Mesh)
        * Looks (Scope)
          * MI_Floor_01 (Material)
            * MI_Floor_01 (Shader)
    * SM_floor59 (Xform)
      * SM_floor59 (Xform)
        * SM_floor02 (Mesh)
        * Looks (Scope)
          * MI_Floor_01 (Material)
            * MI_Floor_01 (Shader)
    * SM_floor60 (Xform)
      * SM_floor60 (Xform)
        * SM_floor02 (Mesh)
        * Looks (Scope)
          * MI_Floor_01 (Material)
            * MI_Floor_01 (Shader)
    * SM_floor61 (Xform)
      * SM_floor61 (Xform)
        * SM_floor02 (Mesh)
        * Looks (Scope)
          * MI_Floor_01 (Material)
            * MI_Floor_01 (Shader)
    * SM_floor62 (Xform)
      * SM_floor62 (Xform)
        * SM_floor02 (Mesh)
        * Looks (Scope)
          * MI_Floor_01 (Material)
            * MI_Floor_01 (Shader)
    * SM_floor63 (Xform)
      * SM_floor63 (Xform)
        * SM_floor02 (Mesh)
        * Looks (Scope)
          * MI_Floor_01 (Material)
            * MI_Floor_01 (Shader)
    * S_Barcode886 (Xform)
      * S_Barcode886 (Xform)
        * S_Barcode (Mesh)
        * Looks (Scope)
          * MI_Barcode_0001 (Material)
            * MI_Barcode_0001 (Shader)
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
  * PartA_OnWorkbench_1 (Xform)
    * node__Size_1_0x1_4x4_SUPPRESSION_Default (Xform)
      * geometry_1 (Mesh)
  * PartA_OnWorkbench_2 (Xform)
    * node__Size_1_0x1_4x4_SUPPRESSION_Default (Xform)
      * geometry_1 (Mesh)
  * PartA_OnWorkbench_3 (Xform)
    * node__Size_1_0x1_4x4_SUPPRESSION_Default (Xform)
      * geometry_1 (Mesh)
  * PartA_OnWorkbench1_1 (Xform)
    * node__Size_1_0x1_4x4_SUPPRESSION_Default (Xform)
      * geometry_1 (Mesh)
  * PartA_OnWorkbench1_2 (Xform)
    * node__Size_1_0x1_4x4_SUPPRESSION_Default (Xform)
      * geometry_1 (Mesh)
  * PartA_OnWorkbench1_3 (Xform)
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
  * StackedCarton (Xform)
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
  * Workbench (Xform)
  * agv_02 (Xform)
  * Plastic_Crate_02 (Prim)
  * agv_03 (Xform)
  * Plastic_Crate_01 (Prim)
  * Plastic_Crate (Xform)
    * Materials (Scope)
      * Crate (Material)
        * pbr_shader (Shader)
        * uvset0 (Shader)
        * tex_base (Shader)
        * tex_metallic (Shader)
        * tex_roughness (Shader)
        * tex_normal (Shader)
    * Meshes (Xform)
      * Sketchfab_model (Xform)
        * _04449d6b57f43e4a66c142c8bf4355d_fbx (Xform)
          * RootNode (Xform)
            * PlasticCrate (Xform)
              * PlasticCrate_Crate_0 (Xform)
                * PlasticCrate_Crate_0 (Mesh)
  * model_forklift (Xform)
    * materials (Scope)
      * mat_0 (Material)
        * PBRShader (Shader)
      * mat_130 (Material)
        * PBRShader (Shader)
        * stReader (Shader)
        * transform_st (Shader)
        * diffuseTexture (Shader)
      * mat_138 (Material)
        * PBRShader (Shader)
        * stReader (Shader)
        * transform_st (Shader)
        * diffuseTexture (Shader)
      * mat_88 (Material)
        * PBRShader (Shader)
        * stReader (Shader)
        * transform_st (Shader)
        * diffuseTexture (Shader)
      * mat_127 (Material)
        * PBRShader (Shader)
      * mat_77 (Material)
        * PBRShader (Shader)
      * mat_104 (Material)
        * PBRShader (Shader)
        * stReader (Shader)
        * transform_st (Shader)
        * diffuseTexture (Shader)
      * mat_123 (Material)
        * PBRShader (Shader)
        * stReader (Shader)
        * transform_st (Shader)
        * diffuseTexture (Shader)
      * mat_119 (Material)
        * PBRShader (Shader)
        * stReader (Shader)
        * transform_st (Shader)
        * diffuseTexture (Shader)
      * mat_116 (Material)
        * PBRShader (Shader)
      * mat_143 (Material)
        * PBRShader (Shader)
      * mat_112 (Material)
        * PBRShader (Shader)
        * stReader (Shader)
        * transform_st (Shader)
        * diffuseTexture (Shader)
      * mat_84 (Material)
        * PBRShader (Shader)
        * stReader (Shader)
        * transform_st (Shader)
        * diffuseTexture (Shader)
      * mat_74 (Material)
        * PBRShader (Shader)
      * mat_100 (Material)
        * PBRShader (Shader)
        * stReader (Shader)
        * transform_st (Shader)
        * diffuseTexture (Shader)
      * mat_142 (Material)
        * PBRShader (Shader)
      * mat_92 (Material)
        * PBRShader (Shader)
        * stReader (Shader)
        * transform_st (Shader)
        * diffuseTexture (Shader)
      * mat_96 (Material)
        * PBRShader (Shader)
        * stReader (Shader)
        * transform_st (Shader)
        * diffuseTexture (Shader)
      * mat_145 (Material)
        * PBRShader (Shader)
    * E_car_1 (Xform)
      * E_light_2 (Xform)
        * E_light1_10 (Xform)
          * P_6794159b4d97ba4 (Mesh)
        * E_light2_3 (Xform)
          * P_9cbe0c4970530f28 (Mesh)
        * E_light4_4 (Xform)
          * P_603898df33083f28 (Mesh)
        * E_light6_5 (Xform)
          * P_b89d5b7d78f10f28 (Mesh)
        * E_light7_6 (Xform)
          * P_453bc8167b420f28 (Mesh)
        * E_light8_7 (Xform)
          * P_5eeb335fb395fba4 (Mesh)
        * E_light5_8 (Xform)
          * P_321ca304ac8b33a4 (Mesh)
        * E_light3_9 (Xform)
          * P_3cb07990a848a3a4 (Mesh)
      * E_obj3d66M842_11 (Xform)
        * P_3be02ebaa7a5dfa4 (Mesh)
      * E_obj3d66M72640_12 (Xform)
        * P_a8f89250d63d7ba4 (Mesh)
      * E_obj3d66M142741_13 (Xform)
        * P_d29f611922f7fba4 (Mesh)
      * E_obj3d66M249702_14 (Xform)
        * P_c122d1154b6780a4 (Mesh)
      * E_obj3d66M305130_15 (Xform)
        * P_28cfff291fa0a7a4 (Mesh)
      * E_Obj3d66M441049_16 (Xform)
        * P_fb4a7ac6d1d8fc14 (Mesh)
      * E_obj3d66M475834_17 (Xform)
        * E_Group_18 (Xform)
          * P_f20d486c0e08e78f (Mesh)
        * E_clutch_pedal_19 (Xform)
          * P_57ed0a06fe85e78f (Mesh)
        * E_brake_pedal_20 (Xform)
          * P_993401bbfc95e78f (Mesh)
        * E_accelerator_21 (Xform)
          * P_900f95d46f1e78f (Mesh)
        * E_handlebar_22 (Xform)
          * P_d48bebcda255fe4f (Mesh)
      * E_obj3d66M573428_23 (Xform)
        * P_e6141c991493678f (Mesh)
      * E_obj3d66M649779_24 (Xform)
        * P_c5bc7281712a98f (Mesh)
      * E_obj3d66M696145_25 (Xform)
        * P_f204ce66f0f4678f (Mesh)
      * E_obj3d66M708199_26 (Xform)
        * P_ddd0dc780895e78f (Mesh)
      * E_obj3d66M765770_27 (Xform)
        * P_356107260855e78f (Mesh)
      * E_obj3d66M844633_28 (Xform)
        * P_7dcea60ad912aa91 (Mesh)
      * E_obj3d66M894215_29 (Xform)
        * P_e0edb4ff48977491 (Mesh)
    * E_forks_30 (Xform)
      * E_frame_31 (Xform)
        * P_7d6bd8f04c49d491 (Mesh)
      * E_frame2_32 (Xform)
        * P_cc2892e67c939491 (Mesh)
      * E_bolt5_33 (Xform)
        * P_b46ce8b98c87d491 (Mesh)
      * E_bolt4_34 (Xform)
        * P_2b7d8fe63f1fd491 (Mesh)
      * E_fork_35 (Xform)
        * P_28ea59d149424391 (Mesh)
      * E_bolt1_36 (Xform)
        * P_783528d9f6689491 (Mesh)
      * E_bolt2_37 (Xform)
        * P_b467b40fdc49d491 (Mesh)
      * E_roller1_38 (Xform)
        * P_4c9593b644b5d491 (Mesh)
      * E_bolt3_39 (Xform)
        * P_2054ff83795d491 (Mesh)
      * E_bolt_40 (Xform)
        * P_25f3168e69b5c106 (Mesh)
      * E_roller_41 (Xform)
        * P_7645c9e4a51cda06 (Mesh)
      * E_roller_42 (Xform)
        * P_8e70b3e83f010106 (Mesh)
      * E_roller_43 (Xform)
        * P_f92e149d0b1d1106 (Mesh)
      * E_roller_44 (Xform)
        * P_10a4ff8f254a4906 (Mesh)
      * E_roller1_45 (Xform)
        * P_26c023e5c311c106 (Mesh)
      * E_roller1_46 (Xform)
        * P_8fa7c0a10a3ce106 (Mesh)
      * E_roller1_47 (Xform)
        * P_a802b6d9b7704e86 (Mesh)
      * E_fork_48 (Xform)
        * P_805a366c8f3fa506 (Mesh)
      * PrismaticJoint_forklift_middle (PhysicsPrismaticJoint)
    * E_wheel4_49 (Xform)
      * P_50bff80caab5c106 (Mesh)
      * P_d49e5516066fc106 (Mesh)
      * P_86e23f4d6edc906 (Mesh)
      * P_c4cefac3eab1ad52 (Mesh)
      * RevoluteJoint_forklift_left_01 (PhysicsRevoluteJoint)
    * E_wheel3_50 (Xform)
      * P_be5f81694f55ad52 (Mesh)
      * P_af165295a50d3752 (Mesh)
      * P_552cfe620025ad52 (Mesh)
      * P_202d67628d2d4552 (Mesh)
      * RevoluteJoint_forklift_right_01 (PhysicsRevoluteJoint)
    * E_wheel1_51 (Xform)
      * P_25454954cbc43d52 (Mesh)
      * P_6aa656ebe809ad52 (Mesh)
      * P_54bc3e1791c09552 (Mesh)
      * P_e328f8676dd2552 (Mesh)
      * RevoluteJoint_forklift_left_02 (PhysicsRevoluteJoint)
    * E_wheel2_52 (Xform)
      * P_6a6ed5a9240cad52 (Mesh)
      * P_1c56e4db1795ad52 (Mesh)
      * P_885cc6a54e442d52 (Mesh)
      * P_985337c819783eb2 (Mesh)
      * RevoluteJoint_forklift_right_02 (PhysicsRevoluteJoint)
    * PhysicsMaterial (Material)
    * PhysicsMaterial_01 (Material)
    * PhysicsMaterial_02 (Material)
  * ridgeback_franka (Xform)
    * world (Xform)
      * dummy_base_prismatic_x_joint (PhysicsPrismaticJoint)
    * dummy_base_x (Xform)
      * dummy_base_prismatic_y_joint (PhysicsPrismaticJoint)
    * dummy_base_y (Xform)
      * dummy_base_revolute_z_joint (PhysicsRevoluteJoint)
    * base_link (Xform)
      * base_to_arm_mount_joint (PhysicsFixedJoint)
      * front_laser_joint (PhysicsFixedJoint)
      * rear_laser_joint (PhysicsFixedJoint)
      * visuals (Prim)
        * mesh_0 (Mesh)
        * mesh_1 (Mesh)
        * mesh_2 (Mesh)
        * mesh_3 (Mesh)
        * mesh_4 (Mesh)
        * mesh_5 (Mesh)
        * mesh_6 (Mesh)
        * mesh_7 (Mesh)
      * collisions (Prim)
        * mesh_0 (Mesh)
        * mesh_1 (Mesh)
    * arm_mount_link (Xform)
      * panda_arm_mount_joint (PhysicsFixedJoint)
    * panda_link0 (Xform)
      * panda_joint1 (PhysicsRevoluteJoint)
      * collisions (Mesh)
      * visuals (Xform)
        * panda_link0 (Mesh)
          * subset (GeomSubset)
          * subset_1 (GeomSubset)
          * subset_2 (GeomSubset)
          * subset_3 (GeomSubset)
          * subset_4 (GeomSubset)
          * subset_5 (GeomSubset)
        * Looks (Scope)
          * EmissiveBlue (Material)
            * Shader (Shader)
          * PlasticGray (Material)
            * Shader (Shader)
          * Aluminum (Material)
            * Shader (Shader)
          * PlasticBlack (Material)
            * Shader (Shader)
          * RubberGreen (Material)
            * Shader (Shader)
          * RubberRed (Material)
            * Shader (Shader)
          * RubberWhite (Material)
            * Shader (Shader)
          * RubberGray (Material)
            * Shader (Shader)
          * RubberLightGray (Material)
            * Shader (Shader)
          * AluminumRough (Material)
            * Shader (Shader)
          * rubber_cable (Material)
            * Shader (Shader)
          * PlasticWhite (Material)
            * Shader (Shader)
    * panda_link1 (Xform)
      * panda_joint2 (PhysicsRevoluteJoint)
      * collisions (Mesh)
      * visuals (Xform)
        * panda_link1 (Mesh)
          * subset (GeomSubset)
        * Looks (Scope)
          * EmissiveBlue (Material)
            * Shader (Shader)
          * PlasticGray (Material)
            * Shader (Shader)
          * Aluminum (Material)
            * Shader (Shader)
          * PlasticBlack (Material)
            * Shader (Shader)
          * RubberGreen (Material)
            * Shader (Shader)
          * RubberRed (Material)
            * Shader (Shader)
          * RubberWhite (Material)
            * Shader (Shader)
          * RubberGray (Material)
            * Shader (Shader)
          * RubberLightGray (Material)
            * Shader (Shader)
          * AluminumRough (Material)
            * Shader (Shader)
          * rubber_cable (Material)
            * Shader (Shader)
          * PlasticWhite (Material)
            * Shader (Shader)
    * panda_link2 (Xform)
      * panda_joint3 (PhysicsRevoluteJoint)
      * collisions (Mesh)
      * visuals (Xform)
        * panda_link2 (Mesh)
          * subset (GeomSubset)
        * Looks (Scope)
          * EmissiveBlue (Material)
            * Shader (Shader)
          * PlasticGray (Material)
            * Shader (Shader)
          * Aluminum (Material)
            * Shader (Shader)
          * PlasticBlack (Material)
            * Shader (Shader)
          * RubberGreen (Material)
            * Shader (Shader)
          * RubberRed (Material)
            * Shader (Shader)
          * RubberWhite (Material)
            * Shader (Shader)
          * RubberGray (Material)
            * Shader (Shader)
          * RubberLightGray (Material)
            * Shader (Shader)
          * AluminumRough (Material)
            * Shader (Shader)
          * rubber_cable (Material)
            * Shader (Shader)
          * PlasticWhite (Material)
            * Shader (Shader)
    * panda_link3 (Xform)
      * panda_joint4 (PhysicsRevoluteJoint)
      * collisions (Mesh)
      * visuals (Xform)
        * panda_link3 (Mesh)
          * subset (GeomSubset)
          * subset_1 (GeomSubset)
          * subset_2 (GeomSubset)
        * Looks (Scope)
          * EmissiveBlue (Material)
            * Shader (Shader)
          * PlasticGray (Material)
            * Shader (Shader)
          * Aluminum (Material)
            * Shader (Shader)
          * PlasticBlack (Material)
            * Shader (Shader)
          * RubberGreen (Material)
            * Shader (Shader)
          * RubberRed (Material)
            * Shader (Shader)
          * RubberWhite (Material)
            * Shader (Shader)
          * RubberGray (Material)
            * Shader (Shader)
          * RubberLightGray (Material)
            * Shader (Shader)
          * AluminumRough (Material)
            * Shader (Shader)
          * rubber_cable (Material)
            * Shader (Shader)
          * PlasticWhite (Material)
            * Shader (Shader)
    * panda_link4 (Xform)
      * panda_joint5 (PhysicsRevoluteJoint)
      * collisions (Mesh)
      * visuals (Xform)
        * panda_link4 (Mesh)
          * subset (GeomSubset)
          * subset_1 (GeomSubset)
          * subset_2 (GeomSubset)
        * Looks (Scope)
          * EmissiveBlue (Material)
            * Shader (Shader)
          * PlasticGray (Material)
            * Shader (Shader)
          * Aluminum (Material)
            * Shader (Shader)
          * PlasticBlack (Material)
            * Shader (Shader)
          * RubberGreen (Material)
            * Shader (Shader)
          * RubberRed (Material)
            * Shader (Shader)
          * RubberWhite (Material)
            * Shader (Shader)
          * RubberGray (Material)
            * Shader (Shader)
          * RubberLightGray (Material)
            * Shader (Shader)
          * AluminumRough (Material)
            * Shader (Shader)
          * rubber_cable (Material)
            * Shader (Shader)
          * PlasticWhite (Material)
            * Shader (Shader)
    * panda_link5 (Xform)
      * panda_joint6 (PhysicsRevoluteJoint)
      * collisions (Mesh)
      * visuals (Xform)
        * panda_link5 (Mesh)
          * subset (GeomSubset)
          * subset_1 (GeomSubset)
          * subset_2 (GeomSubset)
        * Looks (Scope)
          * EmissiveBlue (Material)
            * Shader (Shader)
          * PlasticGray (Material)
            * Shader (Shader)
          * Aluminum (Material)
            * Shader (Shader)
          * PlasticBlack (Material)
            * Shader (Shader)
          * RubberGreen (Material)
            * Shader (Shader)
          * RubberRed (Material)
            * Shader (Shader)
          * RubberWhite (Material)
            * Shader (Shader)
          * RubberGray (Material)
            * Shader (Shader)
          * RubberLightGray (Material)
            * Shader (Shader)
          * AluminumRough (Material)
            * Shader (Shader)
          * rubber_cable (Material)
            * Shader (Shader)
          * PlasticWhite (Material)
            * Shader (Shader)
    * panda_link6 (Xform)
      * panda_joint7 (PhysicsRevoluteJoint)
      * collisions (Mesh)
      * visuals (Xform)
        * panda_link6 (Mesh)
          * subset (GeomSubset)
          * subset_1 (GeomSubset)
          * subset_10 (GeomSubset)
          * subset_11 (GeomSubset)
          * subset_12 (GeomSubset)
          * subset_13 (GeomSubset)
          * subset_2 (GeomSubset)
          * subset_3 (GeomSubset)
          * subset_4 (GeomSubset)
          * subset_5 (GeomSubset)
          * subset_6 (GeomSubset)
          * subset_7 (GeomSubset)
          * subset_8 (GeomSubset)
          * subset_9 (GeomSubset)
        * Looks (Scope)
          * EmissiveBlue (Material)
            * Shader (Shader)
          * PlasticGray (Material)
            * Shader (Shader)
          * Aluminum (Material)
            * Shader (Shader)
          * PlasticBlack (Material)
            * Shader (Shader)
          * RubberGreen (Material)
            * Shader (Shader)
          * RubberRed (Material)
            * Shader (Shader)
          * RubberWhite (Material)
            * Shader (Shader)
          * RubberGray (Material)
            * Shader (Shader)
          * RubberLightGray (Material)
            * Shader (Shader)
          * AluminumRough (Material)
            * Shader (Shader)
          * rubber_cable (Material)
            * Shader (Shader)
          * PlasticWhite (Material)
            * Shader (Shader)
    * panda_link7 (Xform)
      * panda_hand_joint (PhysicsFixedJoint)
      * collisions (Mesh)
      * visuals (Xform)
        * panda_link7 (Mesh)
          * subset (GeomSubset)
          * subset_1 (GeomSubset)
          * subset_2 (GeomSubset)
          * subset_3 (GeomSubset)
        * Looks (Scope)
          * EmissiveBlue (Material)
            * Shader (Shader)
          * PlasticGray (Material)
            * Shader (Shader)
          * Aluminum (Material)
            * Shader (Shader)
          * PlasticBlack (Material)
            * Shader (Shader)
          * RubberGreen (Material)
            * Shader (Shader)
          * RubberRed (Material)
            * Shader (Shader)
          * RubberWhite (Material)
            * Shader (Shader)
          * RubberGray (Material)
            * Shader (Shader)
          * RubberLightGray (Material)
            * Shader (Shader)
          * AluminumRough (Material)
            * Shader (Shader)
          * rubber_cable (Material)
            * Shader (Shader)
          * PlasticWhite (Material)
            * Shader (Shader)
    * panda_hand (Xform)
      * panda_finger_joint1 (PhysicsPrismaticJoint)
      * panda_finger_joint2 (PhysicsPrismaticJoint)
      * panda_hand_endeffector_joint (PhysicsFixedJoint)
      * collisions (Mesh)
      * visuals (Xform)
        * panda_hand (Mesh)
          * subset (GeomSubset)
          * subset_1 (GeomSubset)
          * subset_2 (GeomSubset)
          * subset_3 (GeomSubset)
          * subset_4 (GeomSubset)
        * Looks (Scope)
          * EmissiveBlue (Material)
            * Shader (Shader)
          * PlasticGray (Material)
            * Shader (Shader)
          * Aluminum (Material)
            * Shader (Shader)
          * PlasticBlack (Material)
            * Shader (Shader)
          * RubberGreen (Material)
            * Shader (Shader)
          * RubberRed (Material)
            * Shader (Shader)
          * RubberWhite (Material)
            * Shader (Shader)
          * RubberGray (Material)
            * Shader (Shader)
          * RubberLightGray (Material)
            * Shader (Shader)
          * AluminumRough (Material)
            * Shader (Shader)
          * rubber_cable (Material)
            * Shader (Shader)
          * PlasticWhite (Material)
            * Shader (Shader)
    * panda_leftfinger (Xform)
      * collisions (Mesh)
      * visuals (Xform)
        * panda_leftfinger (Mesh)
          * subset (GeomSubset)
          * subset_1 (GeomSubset)
        * Looks (Scope)
          * EmissiveBlue (Material)
            * Shader (Shader)
          * PlasticGray (Material)
            * Shader (Shader)
          * Aluminum (Material)
            * Shader (Shader)
          * PlasticBlack (Material)
            * Shader (Shader)
          * RubberGreen (Material)
            * Shader (Shader)
          * RubberRed (Material)
            * Shader (Shader)
          * RubberWhite (Material)
            * Shader (Shader)
          * RubberGray (Material)
            * Shader (Shader)
          * RubberLightGray (Material)
            * Shader (Shader)
          * AluminumRough (Material)
            * Shader (Shader)
          * rubber_cable (Material)
            * Shader (Shader)
          * PlasticWhite (Material)
            * Shader (Shader)
    * panda_rightfinger (Xform)
      * collisions (Mesh)
      * visuals (Xform)
        * panda_rightfinger (Mesh)
          * subset (GeomSubset)
          * subset_1 (GeomSubset)
        * Looks (Scope)
          * EmissiveBlue (Material)
            * Shader (Shader)
          * PlasticGray (Material)
            * Shader (Shader)
          * Aluminum (Material)
            * Shader (Shader)
          * PlasticBlack (Material)
            * Shader (Shader)
          * RubberGreen (Material)
            * Shader (Shader)
          * RubberRed (Material)
            * Shader (Shader)
          * RubberWhite (Material)
            * Shader (Shader)
          * RubberGray (Material)
            * Shader (Shader)
          * RubberLightGray (Material)
            * Shader (Shader)
          * AluminumRough (Material)
            * Shader (Shader)
          * rubber_cable (Material)
            * Shader (Shader)
          * PlasticWhite (Material)
            * Shader (Shader)
    * endeffector (Xform)
    * front_laser (Xform)
      * visuals (Mesh)
      * collisions (Cube)
    * rear_laser (Xform)
      * visuals (Mesh)
      * collisions (Cube)
    * Looks (Scope)
      * material_black (Material)
        * Shader (Shader)
      * material_dark_grey (Material)
        * Shader (Shader)
      * material_grasp_loc_color (Material)
        * Shader (Shader)
      * material_light_grey (Material)
        * Shader (Shader)
      * material_panda_white (Material)
        * Shader (Shader)
      * material_red (Material)
        * Shader (Shader)
      * material_white (Material)
        * Shader (Shader)
      * material_yellow (Material)
        * Shader (Shader)
      * material_Face636_001 (Material)
        * Shader (Shader)
      * material_Part__Feature017_001 (Material)
        * Shader (Shader)
      * material_Part__Feature019_001 (Material)
        * Shader (Shader)
      * material_Part__Feature023_001 (Material)
        * Shader (Shader)
      * material_Part__Feature_001 (Material)
        * Shader (Shader)
      * material_Part__Feature024 (Material)
        * Shader (Shader)
      * material_Part__Feature001_010_001_002 (Material)
        * Shader (Shader)
      * material_Part__Feature_001_001_001_002 (Material)
        * Shader (Shader)
      * material_Part__Feature001_001_003_001 (Material)
        * Shader (Shader)
      * material_Part__Feature002_001_003_001 (Material)
        * Shader (Shader)
      * material_Part__Feature_002_004_003 (Material)
        * Shader (Shader)
      * material_Shell001_001_001_003 (Material)
        * Shader (Shader)
      * material_Face064_002_001_002_001 (Material)
        * Shader (Shader)
      * material_Face065_002_001_002_001 (Material)
        * Shader (Shader)
      * material_Face374_002_001_002_001 (Material)
        * Shader (Shader)
      * material_Face539_002_001_002_001 (Material)
        * Shader (Shader)
      * material_Shell006_003_002_001 (Material)
        * Shader (Shader)
      * material_Shell007_002_002_001 (Material)
        * Shader (Shader)
      * material_Union001_001_001_002_001 (Material)
        * Shader (Shader)
      * material_Part__Mirroring001_004_002 (Material)
        * Shader (Shader)
      * material_Part__Mirroring002_004_001 (Material)
        * Shader (Shader)
      * material_Part__Mirroring004_004_002 (Material)
        * Shader (Shader)
      * material_Part__Mirroring_004_001 (Material)
        * Shader (Shader)
      * material_Part__Feature001_008_005 (Material)
        * Shader (Shader)
      * material_Part__Feature002_005_005 (Material)
        * Shader (Shader)
      * material_Part__Feature005_001_005 (Material)
        * Shader (Shader)
      * material_Part__Feature_009_005 (Material)
        * Shader (Shader)
      * material_Part__Feature001_006 (Material)
        * Shader (Shader)
      * material_Part__Feature_007 (Material)
        * Shader (Shader)
  * PartB_OnWorkbench_07 (Xform)
  * PartB_OnWorkbench_04 (Xform)
  * PartA_OnWorkbench1_03 (Xform)
  * PartA_OnWorkbench1_02 (Xform)
  * panda_instanceable1_01 (Prim)
  * panda_instanceable1 (Xform)
    * Group (Xform)
      * panda_hand (Xform)
        * visuals (Xform)
        * collisions (Xform)
        * panda_finger_joint1 (PhysicsPrismaticJoint)
        * panda_finger_joint2 (PhysicsPrismaticJoint)
      * panda_leftfinger (Xform)
        * visuals (Xform)
        * collisions (Xform)
      * panda_link0 (Xform)
        * visuals (Xform)
        * collisions (Xform)
        * panda_joint1 (PhysicsRevoluteJoint)
      * panda_link1 (Xform)
        * visuals (Xform)
        * collisions (Xform)
        * panda_joint2 (PhysicsRevoluteJoint)
      * panda_link2 (Xform)
        * visuals (Xform)
        * collisions (Xform)
        * panda_joint3 (PhysicsRevoluteJoint)
      * panda_link3 (Xform)
        * visuals (Xform)
        * collisions (Xform)
        * panda_joint4 (PhysicsRevoluteJoint)
      * panda_link4 (Xform)
        * visuals (Xform)
        * collisions (Xform)
        * panda_joint5 (PhysicsRevoluteJoint)
      * panda_link5 (Xform)
        * visuals (Xform)
        * collisions (Xform)
        * panda_joint6 (PhysicsRevoluteJoint)
      * panda_link6 (Xform)
        * visuals (Xform)
        * collisions (Xform)
        * panda_joint7 (PhysicsRevoluteJoint)
      * panda_link7 (Xform)
        * visuals (Xform)
        * collisions (Xform)
        * panda_hand_joint (PhysicsFixedJoint)
      * panda_rightfinger (Xform)
        * visuals (Xform)
        * collisions (Xform)
      * rootJoint (PhysicsFixedJoint)
  * Workbench_03 (Xform)
  * Workbench_02 (Xform)
  * Workbench_01 (Xform)

## 3. 对象详细描述 (Detailed Prim Descriptions)

### /World/SortingArea

* **Prim路径 (Prim Path):**/World/SortingArea
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/scene/smallscene.usd'
* **世界包围盒 (World BBox):**
  * Size: '(24.000, 38.818, 9.300)'
  * Center: '(-0.000, 0.000, 4.700)'

---

### /World/Conveyor_1

* **Prim路径 (Prim Path):**/World/Conveyor_1
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/ConveyorBelt_A09.usd'
* **世界包围盒 (World BBox):**
  * Size: '(1.177, 4.003, 2.311)'
  * Center: '(0.013, -2.001, 1.155)'

---

### /World/Conveyor_2

* **Prim路径 (Prim Path):**/World/Conveyor_2
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Props/Conveyors/ConveyorBelt_A09.usd'
* **世界包围盒 (World BBox):**
  * Size: '(1.177, 4.003, 2.311)'
  * Center: '(0.013, 2.019, 1.155)'

---

### /World/PartA_OnBelt_1

* **Prim路径 (Prim Path):**/World/PartA_OnBelt_1
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ban_Yuan_Jian/Woodruff keys GB_converted/0;Size=1.0x1.4x4;SUPPRESSION=Default.usd'
* **世界包围盒 (World BBox):**
  * Size: '(3.816, 1.400, 1.000)'
  * Center: '(0.000, -3.370, 1.830)'

---

### /World/PartA_OnBelt_2

* **Prim路径 (Prim Path):**/World/PartA_OnBelt_2
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ban_Yuan_Jian/Woodruff keys GB_converted/0;Size=1.0x1.4x4;SUPPRESSION=Default.usd'
* **世界包围盒 (World BBox):**
  * Size: '(3.816, 1.400, 1.000)'
  * Center: '(0.000, -1.370, 1.830)'

---

### /World/PartA_OnBelt_3

* **Prim路径 (Prim Path):**/World/PartA_OnBelt_3
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ban_Yuan_Jian/Woodruff keys GB_converted/0;Size=1.0x1.4x4;SUPPRESSION=Default.usd'
* **世界包围盒 (World BBox):**
  * Size: '(3.816, 1.400, 1.000)'
  * Center: '(0.000, 0.630, 1.830)'

---

### /World/PartA_OnBelt_4

* **Prim路径 (Prim Path):**/World/PartA_OnBelt_4
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ban_Yuan_Jian/Woodruff keys GB_converted/0;Size=1.0x1.4x4;SUPPRESSION=Default.usd'
* **世界包围盒 (World BBox):**
  * Size: '(3.816, 1.400, 1.000)'
  * Center: '(0.000, 2.630, 1.830)'

---

### /World/PartB_OnBelt_1

* **Prim路径 (Prim Path):**/World/PartB_OnBelt_1
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ping_Jian/Feather keys GB_converted/6;Size=8;Length=28;SUPPRESSION=A,Simplified.usd'
* **世界包围盒 (World BBox):**
  * Size: '(28.000, 8.000, 7.000)'
  * Center: '(-0.100, -2.500, 1.830)'

---

### /World/PartB_OnBelt_2

* **Prim路径 (Prim Path):**/World/PartB_OnBelt_2
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ping_Jian/Feather keys GB_converted/6;Size=8;Length=28;SUPPRESSION=A,Simplified.usd'
* **世界包围盒 (World BBox):**
  * Size: '(28.000, 8.000, 7.000)'
  * Center: '(-0.100, -0.500, 1.830)'

---

### /World/PartB_OnBelt_3

* **Prim路径 (Prim Path):**/World/PartB_OnBelt_3
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ping_Jian/Feather keys GB_converted/6;Size=8;Length=28;SUPPRESSION=A,Simplified.usd'
* **世界包围盒 (World BBox):**
  * Size: '(28.000, 8.000, 7.000)'
  * Center: '(-0.100, 1.500, 1.830)'

---

### /World/PartB_OnBelt_4

* **Prim路径 (Prim Path):**/World/PartB_OnBelt_4
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ping_Jian/Feather keys GB_converted/6;Size=8;Length=28;SUPPRESSION=A,Simplified.usd'
* **世界包围盒 (World BBox):**
  * Size: '(28.000, 8.000, 7.000)'
  * Center: '(-0.100, 3.500, 1.830)'

---

### /World/PartA_OnWorkbench_1

* **Prim路径 (Prim Path):**/World/PartA_OnWorkbench_1
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ban_Yuan_Jian/Woodruff keys GB_converted/0;Size=1.0x1.4x4;SUPPRESSION=Default.usd'
* **世界包围盒 (World BBox):**
  * Size: '(3.816, 1.400, 1.000)'
  * Center: '(-1.434, -5.700, 0.890)'

---

### /World/PartA_OnWorkbench_2

* **Prim路径 (Prim Path):**/World/PartA_OnWorkbench_2
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ban_Yuan_Jian/Woodruff keys GB_converted/0;Size=1.0x1.4x4;SUPPRESSION=Default.usd'
* **世界包围盒 (World BBox):**
  * Size: '(3.816, 1.400, 1.000)'
  * Center: '(-1.434, -5.200, 0.890)'

---

### /World/PartA_OnWorkbench_3

* **Prim路径 (Prim Path):**/World/PartA_OnWorkbench_3
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ban_Yuan_Jian/Woodruff keys GB_converted/0;Size=1.0x1.4x4;SUPPRESSION=Default.usd'
* **世界包围盒 (World BBox):**
  * Size: '(3.816, 1.400, 1.000)'
  * Center: '(-1.434, -4.700, 0.890)'

---

### /World/PartA_OnWorkbench1_1

* **Prim路径 (Prim Path):**/World/PartA_OnWorkbench1_1
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ban_Yuan_Jian/Woodruff keys GB_converted/0;Size=1.0x1.4x4;SUPPRESSION=Default.usd'
* **世界包围盒 (World BBox):**
  * Size: '(3.816, 1.400, 1.000)'
  * Center: '(-0.447, -5.700, 0.890)'

---

### /World/PartA_OnWorkbench1_2

* **Prim路径 (Prim Path):**/World/PartA_OnWorkbench1_2
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ban_Yuan_Jian/Woodruff keys GB_converted/0;Size=1.0x1.4x4;SUPPRESSION=Default.usd'
* **世界包围盒 (World BBox):**
  * Size: '(3.816, 1.400, 1.000)'
  * Center: '(-0.447, -5.200, 0.890)'

---

### /World/PartA_OnWorkbench1_3

* **Prim路径 (Prim Path):**/World/PartA_OnWorkbench1_3
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ban_Yuan_Jian/Woodruff keys GB_converted/0;Size=1.0x1.4x4;SUPPRESSION=Default.usd'
* **世界包围盒 (World BBox):**
  * Size: '(3.816, 1.400, 1.000)'
  * Center: '(-0.447, -4.700, 0.890)'

---

### /World/PartB_OnWorkbench_1

* **Prim路径 (Prim Path):**/World/PartB_OnWorkbench_1
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ping_Jian/Feather keys GB_converted/6;Size=8;Length=28;SUPPRESSION=A,Simplified.usd'
* **世界包围盒 (World BBox):**
  * Size: '(28.000, 8.000, 7.000)'
  * Center: '(0.807, -5.700, 0.890)'

---

### /World/PartB_OnWorkbench_2

* **Prim路径 (Prim Path):**/World/PartB_OnWorkbench_2
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ping_Jian/Feather keys GB_converted/6;Size=8;Length=28;SUPPRESSION=A,Simplified.usd'
* **世界包围盒 (World BBox):**
  * Size: '(28.000, 8.000, 7.000)'
  * Center: '(0.807, -5.450, 0.890)'

---

### /World/PartB_OnWorkbench_3

* **Prim路径 (Prim Path):**/World/PartB_OnWorkbench_3
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ping_Jian/Feather keys GB_converted/6;Size=8;Length=28;SUPPRESSION=A,Simplified.usd'
* **世界包围盒 (World BBox):**
  * Size: '(28.000, 8.000, 7.000)'
  * Center: '(0.807, -5.200, 0.890)'

---

### /World/PartB_OnWorkbench_4

* **Prim路径 (Prim Path):**/World/PartB_OnWorkbench_4
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ping_Jian/Feather keys GB_converted/6;Size=8;Length=28;SUPPRESSION=A,Simplified.usd'
* **世界包围盒 (World BBox):**
  * Size: '(28.000, 8.000, 7.000)'
  * Center: '(0.232, -5.735, 0.890)'

---

### /World/PartB_OnWorkbench_5

* **Prim路径 (Prim Path):**/World/PartB_OnWorkbench_5
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ping_Jian/Feather keys GB_converted/6;Size=8;Length=28;SUPPRESSION=A,Simplified.usd'
* **世界包围盒 (World BBox):**
  * Size: '(28.000, 8.000, 7.000)'
  * Center: '(0.232, -5.485, 0.890)'

---

### /World/PartB_OnWorkbench_6

* **Prim路径 (Prim Path):**/World/PartB_OnWorkbench_6
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ping_Jian/Feather keys GB_converted/6;Size=8;Length=28;SUPPRESSION=A,Simplified.usd'
* **世界包围盒 (World BBox):**
  * Size: '(28.000, 8.000, 7.000)'
  * Center: '(0.232, -5.235, 0.890)'

---

### /World/agv_1

* **Prim路径 (Prim Path):**/World/agv_1
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/assets/AGV_ready_1/AGV_ready_1.usdc'
* **世界包围盒 (World BBox):**
  * Size: '(1.457, 0.340, 0.669)'
  * Center: '(-5.318, -5.286, 0.159)'

---

### /World/StackedCarton

* **Prim路径 (Prim Path):**/World/StackedCarton
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '/media/simple/another_Documents/isaacsim_assets/assets/Plastic_Crate(1)/Plastic_Crate.usdc'
* **世界包围盒 (World BBox):**
  * Size: '(0.424, 0.365, 0.421)'
  * Center: '(-4.083, -5.673, 0.284)'

---

### /World/Workbench

* **Prim路径 (Prim Path):**/World/Workbench
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] 'file:/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/5.0/NVIDIA/Assets/DigitalTwin/Assets/Warehouse/Furnishing/Workbenches/MetalWorktable_A/MetalWorktable_A12_01.usd'
* **世界包围盒 (World BBox):**
  * Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
  * Center: '(0.000, 0.000, 0.000)'

---

### /World/agv_02

* **Prim路径 (Prim Path):**/World/agv_02
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] 'file:/media/simple/another_Documents/isaacsim_assets/assets/AGV_ready_1/AGV_ready_1.usdc'
* **世界包围盒 (World BBox):**
  * Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
  * Center: '(0.000, 0.000, 0.000)'

---

### /World/agv_03

* **Prim路径 (Prim Path):**/World/agv_03
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] 'file:/media/simple/another_Documents/isaacsim_assets/assets/AGV_ready_1/AGV_ready_1.usdc'
* **世界包围盒 (World BBox):**
  * Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
  * Center: '(0.000, 0.000, 0.000)'

---

### /World/Plastic_Crate

* **Prim路径 (Prim Path):**/World/Plastic_Crate
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '../device_data/usdz/Box/Plastic_Crate.usdz'
* **世界包围盒 (World BBox):**
  * Size: '(68.986, 38.096, 45.367)'
  * Center: '(-5.294, -5.516, 0.492)'

---

### /World/model_forklift

* **Prim路径 (Prim Path):**/World/model_forklift
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '../device_data/usdz/Forklift/model_forklift.usdz'
* **世界包围盒 (World BBox):**
  * Size: '(1.196, 3.710, 2.118)'
  * Center: '(-5.143, 6.547, 1.114)'

---

### /World/ridgeback_franka

* **Prim路径 (Prim Path):**/World/ridgeback_franka
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '../device_data/usdz/IndustrialRobot/ridgeback_franka.usdz'
* **世界包围盒 (World BBox):**
  * Size: '(1.543, 0.793, 1.134)'
  * Center: '(-3.125, -1.730, 0.621)'

---

### /World/PartB_OnWorkbench_07

* **Prim路径 (Prim Path):**/World/PartB_OnWorkbench_07
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] 'file:/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ping_Jian/Feather keys GB_converted/6;Size=8;Length=28;SUPPRESSION=A,Simplified.usd'
* **世界包围盒 (World BBox):**
  * Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
  * Center: '(0.000, 0.000, 0.000)'

---

### /World/PartB_OnWorkbench_04

* **Prim路径 (Prim Path):**/World/PartB_OnWorkbench_04
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] 'file:/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ping_Jian/Feather keys GB_converted/6;Size=8;Length=28;SUPPRESSION=A,Simplified.usd'
* **世界包围盒 (World BBox):**
  * Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
  * Center: '(0.000, 0.000, 0.000)'

---

### /World/PartA_OnWorkbench1_03

* **Prim路径 (Prim Path):**/World/PartA_OnWorkbench1_03
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] 'file:/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ban_Yuan_Jian/Woodruff keys GB_converted/0;Size=1.0x1.4x4;SUPPRESSION=Default.usd'
* **世界包围盒 (World BBox):**
  * Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
  * Center: '(0.000, 0.000, 0.000)'

---

### /World/PartA_OnWorkbench1_02

* **Prim路径 (Prim Path):**/World/PartA_OnWorkbench1_02
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] 'file:/media/simple/another_Documents/isaacsim_assets/part/obj-20260107/_Ban_Yuan_Jian/Woodruff keys GB_converted/0;Size=1.0x1.4x4;SUPPRESSION=Default.usd'
* **世界包围盒 (World BBox):**
  * Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
  * Center: '(0.000, 0.000, 0.000)'

---

### /World/panda_instanceable1

* **Prim路径 (Prim Path):**/World/panda_instanceable1
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '../device_data/usdz/IndustrialRobot/panda_instanceable1.usdz'
* **世界包围盒 (World BBox):**
  * Size: '(0.503, 0.389, 1.672)'
  * Center: '(-0.781, -4.360, 1.675)'

---

### /World/panda_instanceable1/Group/panda_hand/visuals

* **Prim路径 (Prim Path):**/World/panda_instanceable1/Group/panda_hand/visuals
* **Prim类型 (Prim Type):**Xform
* **变换信息 (Transform):**
  * **平移 (Translate):**'(0.000, 0.000, 0.000)'
  * **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
  * **缩放 (Scale):**'(1.000, 1.000, 1.000)'
* **外部引用 (Referenced USD Files):**
  * [reference] 'Reference 1'
  * Prim Path: '/Flattened_Prototype_6'
* **世界包围盒 (World BBox):**
  * Size: '(0.063, 0.205, 0.092)'
  * Center: '(-0.671, -4.359, 2.198)'

---

### /World/panda_instanceable1/Group/panda_hand/collisions

* **Prim路径 (Prim Path):**/World/panda_instanceable1/Group/panda_hand/collisions
* **Prim类型 (Prim Type):**Xform
* **变换信息 (Transform):**
  * **平移 (Translate):**'(0.000, 0.000, 0.000)'
  * **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
  * **缩放 (Scale):**'(1.000, 1.000, 1.000)'
* **外部引用 (Referenced USD Files):**
  * [reference] 'Reference 1'
  * Prim Path: '/Flattened_Prototype_13'
* **世界包围盒 (World BBox):**
  * Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
  * Center: '(-0.669, -4.361, 2.228)'

---

### /World/panda_instanceable1/Group/panda_leftfinger/visuals

* **Prim路径 (Prim Path):**/World/panda_instanceable1/Group/panda_leftfinger/visuals
* **Prim类型 (Prim Type):**Xform
* **变换信息 (Transform):**
  * **平移 (Translate):**'(0.000, 0.000, 0.000)'
  * **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
  * **缩放 (Scale):**'(1.000, 1.000, 1.000)'
* **外部引用 (Referenced USD Files):**
  * [reference] 'Reference 1'
  * Prim Path: '/Flattened_Prototype_2'
* **世界包围盒 (World BBox):**
  * Size: '(0.021, 0.026, 0.054)'
  * Center: '(-0.655, -4.375, 2.100)'

---

### /World/panda_instanceable1/Group/panda_leftfinger/collisions

* **Prim路径 (Prim Path):**/World/panda_instanceable1/Group/panda_leftfinger/collisions
* **Prim类型 (Prim Type):**Xform
* **变换信息 (Transform):**
  * **平移 (Translate):**'(0.000, 0.000, 0.000)'
  * **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
  * **缩放 (Scale):**'(1.000, 1.000, 1.000)'
* **外部引用 (Referenced USD Files):**
  * [reference] 'Reference 1'
  * Prim Path: '/Flattened_Prototype_22'
* **世界包围盒 (World BBox):**
  * Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
  * Center: '(-0.669, -4.361, 2.140)'

---

### /World/panda_instanceable1/Group/panda_link0/visuals

* **Prim路径 (Prim Path):**/World/panda_instanceable1/Group/panda_link0/visuals
* **Prim类型 (Prim Type):**Xform
* **变换信息 (Transform):**
  * **平移 (Translate):**'(0.000, 0.000, 0.000)'
  * **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
  * **缩放 (Scale):**'(1.000, 1.000, 1.000)'
* **外部引用 (Referenced USD Files):**
  * [reference] 'Reference 1'
  * Prim Path: '/Flattened_Prototype_5'
* **世界包围盒 (World BBox):**
  * Size: '(0.226, 0.189, 0.140)'
  * Center: '(-0.863, -4.361, 0.944)'

---

### /World/panda_instanceable1/Group/panda_link0/collisions

* **Prim路径 (Prim Path):**/World/panda_instanceable1/Group/panda_link0/collisions
* **Prim类型 (Prim Type):**Xform
* **变换信息 (Transform):**
  * **平移 (Translate):**'(0.000, 0.000, 0.000)'
  * **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
  * **缩放 (Scale):**'(1.000, 1.000, 1.000)'
* **外部引用 (Referenced USD Files):**
  * [reference] 'Reference 1'
  * Prim Path: '/Flattened_Prototype_19'
* **世界包围盒 (World BBox):**
  * Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
  * Center: '(-0.801, -4.361, 0.839)'

---

### /World/panda_instanceable1/Group/panda_link1/visuals

* **Prim路径 (Prim Path):**/World/panda_instanceable1/Group/panda_link1/visuals
* **Prim类型 (Prim Type):**Xform
* **变换信息 (Transform):**
  * **平移 (Translate):**'(0.000, 0.000, 0.000)'
  * **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
  * **缩放 (Scale):**'(1.000, 1.000, 1.000)'
* **外部引用 (Referenced USD Files):**
  * [reference] 'Reference 1'
  * Prim Path: '/Flattened_Prototype_16'
* **世界包围盒 (World BBox):**
  * Size: '(0.110, 0.184, 0.247)'
  * Center: '(-0.801, -4.416, 1.235)'

---

### /World/panda_instanceable1/Group/panda_link1/collisions

* **Prim路径 (Prim Path):**/World/panda_instanceable1/Group/panda_link1/collisions
* **Prim类型 (Prim Type):**Xform
* **变换信息 (Transform):**
  * **平移 (Translate):**'(0.000, 0.000, 0.000)'
  * **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
  * **缩放 (Scale):**'(1.000, 1.000, 1.000)'
* **外部引用 (Referenced USD Files):**
  * [reference] 'Reference 1'
  * Prim Path: '/Flattened_Prototype_18'
* **世界包围盒 (World BBox):**
  * Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
  * Center: '(-0.801, -4.361, 1.338)'

---

### /World/panda_instanceable1/Group/panda_link2/visuals

* **Prim路径 (Prim Path):**/World/panda_instanceable1/Group/panda_link2/visuals
* **Prim类型 (Prim Type):**Xform
* **变换信息 (Transform):**
  * **平移 (Translate):**'(0.000, 0.000, 0.000)'
  * **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
  * **缩放 (Scale):**'(1.000, 1.000, 1.000)'
* **外部引用 (Referenced USD Files):**
  * [reference] 'Reference 1'
  * Prim Path: '/Flattened_Prototype_1'
* **世界包围盒 (World BBox):**
  * Size: '(0.110, 0.249, 0.184)'
  * Center: '(-0.801, -4.305, 1.443)'

---

### /World/panda_instanceable1/Group/panda_link2/collisions

* **Prim路径 (Prim Path):**/World/panda_instanceable1/Group/panda_link2/collisions
* **Prim类型 (Prim Type):**Xform
* **变换信息 (Transform):**
  * **平移 (Translate):**'(0.000, 0.000, 0.000)'
  * **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
  * **缩放 (Scale):**'(1.000, 1.000, 1.000)'
* **外部引用 (Referenced USD Files):**
  * [reference] 'Reference 1'
  * Prim Path: '/Flattened_Prototype_12'
* **世界包围盒 (World BBox):**
  * Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
  * Center: '(-0.801, -4.361, 1.338)'

---

### /World/panda_instanceable1/Group/panda_link3/visuals

* **Prim路径 (Prim Path):**/World/panda_instanceable1/Group/panda_link3/visuals
* **Prim类型 (Prim Type):**Xform
* **变换信息 (Transform):**
  * **平移 (Translate):**'(0.000, 0.000, 0.000)'
  * **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
  * **缩放 (Scale):**'(1.000, 1.000, 1.000)'
* **外部引用 (Referenced USD Files):**
  * [reference] 'Reference 1'
  * Prim Path: '/Flattened_Prototype_14'
* **世界包围盒 (World BBox):**
  * Size: '(0.193, 0.166, 0.176)'
  * Center: '(-0.739, -4.319, 1.763)'

---

### /World/panda_instanceable1/Group/panda_link3/collisions

* **Prim路径 (Prim Path):**/World/panda_instanceable1/Group/panda_link3/collisions
* **Prim类型 (Prim Type):**Xform
* **变换信息 (Transform):**
  * **平移 (Translate):**'(0.000, 0.000, 0.000)'
  * **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
  * **缩放 (Scale):**'(1.000, 1.000, 1.000)'
* **外部引用 (Referenced USD Files):**
  * [reference] 'Reference 1'
  * Prim Path: '/Flattened_Prototype_15'
* **世界包围盒 (World BBox):**
  * Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
  * Center: '(-0.801, -4.361, 1.812)'

---

### /World/panda_instanceable1/Group/panda_link4/visuals

* **Prim路径 (Prim Path):**/World/panda_instanceable1/Group/panda_link4/visuals
* **Prim类型 (Prim Type):**Xform
* **变换信息 (Transform):**
  * **平移 (Translate):**'(0.000, 0.000, 0.000)'
  * **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
  * **缩放 (Scale):**'(1.000, 1.000, 1.000)'
* **外部引用 (Referenced USD Files):**
  * [reference] 'Reference 1'
  * Prim Path: '/Flattened_Prototype_8'
* **世界包围盒 (World BBox):**
  * Size: '(0.193, 0.179, 0.166)'
  * Center: '(-0.739, -4.403, 1.864)'

---

### /World/panda_instanceable1/Group/panda_link4/collisions

* **Prim路径 (Prim Path):**/World/panda_instanceable1/Group/panda_link4/collisions
* **Prim类型 (Prim Type):**Xform
* **变换信息 (Transform):**
  * **平移 (Translate):**'(0.000, 0.000, 0.000)'
  * **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
  * **缩放 (Scale):**'(1.000, 1.000, 1.000)'
* **外部引用 (Referenced USD Files):**
  * [reference] 'Reference 1'
  * Prim Path: '/Flattened_Prototype_3'
* **世界包围盒 (World BBox):**
  * Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
  * Center: '(-0.678, -4.361, 1.812)'

---

### /World/panda_instanceable1/Group/panda_link5/visuals

* **Prim路径 (Prim Path):**/World/panda_instanceable1/Group/panda_link5/visuals
* **Prim类型 (Prim Type):**Xform
* **变换信息 (Transform):**
  * **平移 (Translate):**'(0.000, 0.000, 0.000)'
  * **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
  * **缩放 (Scale):**'(1.000, 1.000, 1.000)'
* **外部引用 (Referenced USD Files):**
  * [reference] 'Reference 1'
  * Prim Path: '/Flattened_Prototype_10'
* **世界包围盒 (World BBox):**
  * Size: '(0.110, 0.185, 0.311)'
  * Center: '(-0.801, -4.304, 2.233)'

---

### /World/panda_instanceable1/Group/panda_link5/collisions

* **Prim路径 (Prim Path):**/World/panda_instanceable1/Group/panda_link5/collisions
* **Prim类型 (Prim Type):**Xform
* **变换信息 (Transform):**
  * **平移 (Translate):**'(0.000, 0.000, 0.000)'
  * **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
  * **缩放 (Scale):**'(1.000, 1.000, 1.000)'
* **外部引用 (Referenced USD Files):**
  * [reference] 'Reference 1'
  * Prim Path: '/Flattened_Prototype_4'
* **世界包围盒 (World BBox):**
  * Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
  * Center: '(-0.801, -4.361, 2.388)'

---

### /World/panda_instanceable1/Group/panda_link6/visuals

* **Prim路径 (Prim Path):**/World/panda_instanceable1/Group/panda_link6/visuals
* **Prim类型 (Prim Type):**Xform
* **变换信息 (Transform):**
  * **平移 (Translate):**'(0.000, 0.000, 0.000)'
  * **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
  * **缩放 (Scale):**'(1.000, 1.000, 1.000)'
* **外部引用 (Referenced USD Files):**
  * [reference] 'Reference 1'
  * Prim Path: '/Flattened_Prototype_9'
* **世界包围盒 (World BBox):**
  * Size: '(0.180, 0.133, 0.100)'
  * Center: '(-0.738, -4.370, 2.411)'

---

### /World/panda_instanceable1/Group/panda_link6/collisions

* **Prim路径 (Prim Path):**/World/panda_instanceable1/Group/panda_link6/collisions
* **Prim类型 (Prim Type):**Xform
* **变换信息 (Transform):**
  * **平移 (Translate):**'(0.000, 0.000, 0.000)'
  * **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
  * **缩放 (Scale):**'(1.000, 1.000, 1.000)'
* **外部引用 (Referenced USD Files):**
  * [reference] 'Reference 1'
  * Prim Path: '/Flattened_Prototype_11'
* **世界包围盒 (World BBox):**
  * Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
  * Center: '(-0.801, -4.361, 2.388)'

---

### /World/panda_instanceable1/Group/panda_link7/visuals

* **Prim路径 (Prim Path):**/World/panda_instanceable1/Group/panda_link7/visuals
* **Prim类型 (Prim Type):**Xform
* **变换信息 (Transform):**
  * **平移 (Translate):**'(0.000, 0.000, 0.000)'
  * **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
  * **缩放 (Scale):**'(1.000, 1.000, 1.000)'
* **外部引用 (Referenced USD Files):**
  * [reference] 'Reference 1'
  * Prim Path: '/Flattened_Prototype_17'
* **世界包围盒 (World BBox):**
  * Size: '(0.125, 0.125, 0.055)'
  * Center: '(-0.641, -4.389, 2.269)'

---

### /World/panda_instanceable1/Group/panda_link7/collisions

* **Prim路径 (Prim Path):**/World/panda_instanceable1/Group/panda_link7/collisions
* **Prim类型 (Prim Type):**Xform
* **变换信息 (Transform):**
  * **平移 (Translate):**'(0.000, 0.000, 0.000)'
  * **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
  * **缩放 (Scale):**'(1.000, 1.000, 1.000)'
* **外部引用 (Referenced USD Files):**
  * [reference] 'Reference 1'
  * Prim Path: '/Flattened_Prototype_21'
* **世界包围盒 (World BBox):**
  * Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
  * Center: '(-0.669, -4.361, 2.388)'

---

### /World/panda_instanceable1/Group/panda_rightfinger/visuals

* **Prim路径 (Prim Path):**/World/panda_instanceable1/Group/panda_rightfinger/visuals
* **Prim类型 (Prim Type):**Xform
* **变换信息 (Transform):**
  * **平移 (Translate):**'(0.000, 0.000, 0.000)'
  * **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
  * **缩放 (Scale):**'(1.000, 1.000, 1.000)'
* **外部引用 (Referenced USD Files):**
  * [reference] 'Reference 1'
  * Prim Path: '/Flattened_Prototype_7'
* **世界包围盒 (World BBox):**
  * Size: '(0.021, 0.026, 0.054)'
  * Center: '(-0.683, -4.347, 2.100)'

---

### /World/panda_instanceable1/Group/panda_rightfinger/collisions

* **Prim路径 (Prim Path):**/World/panda_instanceable1/Group/panda_rightfinger/collisions
* **Prim类型 (Prim Type):**Xform
* **变换信息 (Transform):**
  * **平移 (Translate):**'(0.000, 0.000, 0.000)'
  * **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
  * **缩放 (Scale):**'(1.000, 1.000, 1.000)'
* **外部引用 (Referenced USD Files):**
  * [reference] 'Reference 1'
  * Prim Path: '/Flattened_Prototype_20'
* **世界包围盒 (World BBox):**
  * Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
  * Center: '(-0.669, -4.361, 2.140)'

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

### /World/Workbench_02

* **Prim路径 (Prim Path):**/World/Workbench_02
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] 'file:/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/5.0/NVIDIA/Assets/DigitalTwin/Assets/Warehouse/Furnishing/Workbenches/MetalWorktable_A/MetalWorktable_A12_01.usd'
* **世界包围盒 (World BBox):**
  * Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
  * Center: '(0.000, 0.000, 0.000)'

---

### /World/Workbench_01

* **Prim路径 (Prim Path):**/World/Workbench_01
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] 'file:/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/5.0/NVIDIA/Assets/DigitalTwin/Assets/Warehouse/Furnishing/Workbenches/MetalWorktable_A/MetalWorktable_A12_01.usd'
* **世界包围盒 (World BBox):**
  * Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
  * Center: '(0.000, 0.000, 0.000)'

---

## 4. 材质库 (Material Library)

### /World/SortingArea/SM_BeamA_9M25/SM_BeamA_9M25/Looks/MI_BeamsA_01

* **Prim路径 (Prim Path):**/World/SortingArea/SM_BeamA_9M25/SM_BeamA_9M25/Looks/MI_BeamsA_01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_BeamA_9M25/SM_BeamA_9M25/Looks/MI_BeamsA_01/MI_CeilingA_06b'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_BeamA_9M25/SM_BeamA_9M25/Looks/MI_BeamsA_01/MI_CeilingA_06b'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_CeilingA_06b.mdl' (Sub Id: 'MI_CeilingA_06b')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_CeilingA_06b.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_D.png'
      * 'ColorAlbedo' [float4] = '(0.145, 0.145, 0.145, 0.000)'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_N.png'
      * 'MainTiling' [float4] = '(1.000, 1.000, 0.000, 1.000)'
      * 'MaskSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_M.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_ORM.png'
      * 'RoughnessMax' [float] = '0.9'
      * 'RoughnessMin' [float] = '0.1'

---

### /World/SortingArea/SM_BeamA_9M26/SM_BeamA_9M26/Looks/MI_BeamsA_01

* **Prim路径 (Prim Path):**/World/SortingArea/SM_BeamA_9M26/SM_BeamA_9M26/Looks/MI_BeamsA_01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_BeamA_9M26/SM_BeamA_9M26/Looks/MI_BeamsA_01/MI_CeilingA_06b'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_BeamA_9M26/SM_BeamA_9M26/Looks/MI_BeamsA_01/MI_CeilingA_06b'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_CeilingA_06b.mdl' (Sub Id: 'MI_CeilingA_06b')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_CeilingA_06b.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_D.png'
      * 'ColorAlbedo' [float4] = '(0.145, 0.145, 0.145, 0.000)'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_N.png'
      * 'MainTiling' [float4] = '(1.000, 1.000, 0.000, 1.000)'
      * 'MaskSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_M.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_ORM.png'
      * 'RoughnessMax' [float] = '0.9'
      * 'RoughnessMin' [float] = '0.1'

---

### /World/SortingArea/SM_BeamA_9M27/SM_BeamA_9M27/Looks/MI_BeamsA_01

* **Prim路径 (Prim Path):**/World/SortingArea/SM_BeamA_9M27/SM_BeamA_9M27/Looks/MI_BeamsA_01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_BeamA_9M27/SM_BeamA_9M27/Looks/MI_BeamsA_01/MI_CeilingA_06b'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_BeamA_9M27/SM_BeamA_9M27/Looks/MI_BeamsA_01/MI_CeilingA_06b'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_CeilingA_06b.mdl' (Sub Id: 'MI_CeilingA_06b')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_CeilingA_06b.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_D.png'
      * 'ColorAlbedo' [float4] = '(0.145, 0.145, 0.145, 0.000)'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_N.png'
      * 'MainTiling' [float4] = '(1.000, 1.000, 0.000, 1.000)'
      * 'MaskSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_M.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_ORM.png'
      * 'RoughnessMax' [float] = '0.9'
      * 'RoughnessMin' [float] = '0.1'

---

### /World/SortingArea/SM_BeamA_9M29/SM_BeamA_9M29/Looks/MI_BeamsA_01

* **Prim路径 (Prim Path):**/World/SortingArea/SM_BeamA_9M29/SM_BeamA_9M29/Looks/MI_BeamsA_01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_BeamA_9M29/SM_BeamA_9M29/Looks/MI_BeamsA_01/MI_CeilingA_06b'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_BeamA_9M29/SM_BeamA_9M29/Looks/MI_BeamsA_01/MI_CeilingA_06b'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_CeilingA_06b.mdl' (Sub Id: 'MI_CeilingA_06b')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_CeilingA_06b.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_D.png'
      * 'ColorAlbedo' [float4] = '(0.145, 0.145, 0.145, 0.000)'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_N.png'
      * 'MainTiling' [float4] = '(1.000, 1.000, 0.000, 1.000)'
      * 'MaskSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_M.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_ORM.png'
      * 'RoughnessMax' [float] = '0.9'
      * 'RoughnessMin' [float] = '0.1'

---

### /World/SortingArea/SM_BeamA_9M30/SM_BeamA_9M30/Looks/MI_BeamsA_01

* **Prim路径 (Prim Path):**/World/SortingArea/SM_BeamA_9M30/SM_BeamA_9M30/Looks/MI_BeamsA_01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_BeamA_9M30/SM_BeamA_9M30/Looks/MI_BeamsA_01/MI_CeilingA_06b'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_BeamA_9M30/SM_BeamA_9M30/Looks/MI_BeamsA_01/MI_CeilingA_06b'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_CeilingA_06b.mdl' (Sub Id: 'MI_CeilingA_06b')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_CeilingA_06b.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_D.png'
      * 'ColorAlbedo' [float4] = '(0.145, 0.145, 0.145, 0.000)'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_N.png'
      * 'MainTiling' [float4] = '(1.000, 1.000, 0.000, 1.000)'
      * 'MaskSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_M.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_ORM.png'
      * 'RoughnessMax' [float] = '0.9'
      * 'RoughnessMin' [float] = '0.1'

---

### /World/SortingArea/SM_BeamA_9M31/SM_BeamA_9M31/Looks/MI_BeamsA_01

* **Prim路径 (Prim Path):**/World/SortingArea/SM_BeamA_9M31/SM_BeamA_9M31/Looks/MI_BeamsA_01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_BeamA_9M31/SM_BeamA_9M31/Looks/MI_BeamsA_01/MI_CeilingA_06b'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_BeamA_9M31/SM_BeamA_9M31/Looks/MI_BeamsA_01/MI_CeilingA_06b'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_CeilingA_06b.mdl' (Sub Id: 'MI_CeilingA_06b')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_CeilingA_06b.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_D.png'
      * 'ColorAlbedo' [float4] = '(0.145, 0.145, 0.145, 0.000)'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_N.png'
      * 'MainTiling' [float4] = '(1.000, 1.000, 0.000, 1.000)'
      * 'MaskSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_M.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_ORM.png'
      * 'RoughnessMax' [float] = '0.9'
      * 'RoughnessMin' [float] = '0.1'

---

### /World/SortingArea/SM_BeamA_9M33/SM_BeamA_9M33/Looks/MI_BeamsA_01

* **Prim路径 (Prim Path):**/World/SortingArea/SM_BeamA_9M33/SM_BeamA_9M33/Looks/MI_BeamsA_01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_BeamA_9M33/SM_BeamA_9M33/Looks/MI_BeamsA_01/MI_CeilingA_06b'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_BeamA_9M33/SM_BeamA_9M33/Looks/MI_BeamsA_01/MI_CeilingA_06b'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_CeilingA_06b.mdl' (Sub Id: 'MI_CeilingA_06b')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_CeilingA_06b.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_D.png'
      * 'ColorAlbedo' [float4] = '(0.145, 0.145, 0.145, 0.000)'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_N.png'
      * 'MainTiling' [float4] = '(1.000, 1.000, 0.000, 1.000)'
      * 'MaskSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_M.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_ORM.png'
      * 'RoughnessMax' [float] = '0.9'
      * 'RoughnessMin' [float] = '0.1'

---

### /World/SortingArea/SM_BeamA_9M34/SM_BeamA_9M34/Looks/MI_BeamsA_01

* **Prim路径 (Prim Path):**/World/SortingArea/SM_BeamA_9M34/SM_BeamA_9M34/Looks/MI_BeamsA_01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_BeamA_9M34/SM_BeamA_9M34/Looks/MI_BeamsA_01/MI_CeilingA_06b'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_BeamA_9M34/SM_BeamA_9M34/Looks/MI_BeamsA_01/MI_CeilingA_06b'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_CeilingA_06b.mdl' (Sub Id: 'MI_CeilingA_06b')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_CeilingA_06b.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_D.png'
      * 'ColorAlbedo' [float4] = '(0.145, 0.145, 0.145, 0.000)'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_N.png'
      * 'MainTiling' [float4] = '(1.000, 1.000, 0.000, 1.000)'
      * 'MaskSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_M.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_ORM.png'
      * 'RoughnessMax' [float] = '0.9'
      * 'RoughnessMin' [float] = '0.1'

---

### /World/SortingArea/SM_BeamA_9M35/SM_BeamA_9M35/Looks/MI_BeamsA_01

* **Prim路径 (Prim Path):**/World/SortingArea/SM_BeamA_9M35/SM_BeamA_9M35/Looks/MI_BeamsA_01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_BeamA_9M35/SM_BeamA_9M35/Looks/MI_BeamsA_01/MI_CeilingA_06b'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_BeamA_9M35/SM_BeamA_9M35/Looks/MI_BeamsA_01/MI_CeilingA_06b'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_CeilingA_06b.mdl' (Sub Id: 'MI_CeilingA_06b')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_CeilingA_06b.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_D.png'
      * 'ColorAlbedo' [float4] = '(0.145, 0.145, 0.145, 0.000)'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_N.png'
      * 'MainTiling' [float4] = '(1.000, 1.000, 0.000, 1.000)'
      * 'MaskSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_M.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_ORM.png'
      * 'RoughnessMax' [float] = '0.9'
      * 'RoughnessMin' [float] = '0.1'

---

### /World/SortingArea/SM_BeamA_9M37/SM_BeamA_9M37/Looks/MI_BeamsA_01

* **Prim路径 (Prim Path):**/World/SortingArea/SM_BeamA_9M37/SM_BeamA_9M37/Looks/MI_BeamsA_01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_BeamA_9M37/SM_BeamA_9M37/Looks/MI_BeamsA_01/MI_CeilingA_06b'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_BeamA_9M37/SM_BeamA_9M37/Looks/MI_BeamsA_01/MI_CeilingA_06b'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_CeilingA_06b.mdl' (Sub Id: 'MI_CeilingA_06b')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_CeilingA_06b.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_D.png'
      * 'ColorAlbedo' [float4] = '(0.145, 0.145, 0.145, 0.000)'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_N.png'
      * 'MainTiling' [float4] = '(1.000, 1.000, 0.000, 1.000)'
      * 'MaskSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_M.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_ORM.png'
      * 'RoughnessMax' [float] = '0.9'
      * 'RoughnessMin' [float] = '0.1'

---

### /World/SortingArea/SM_BeamA_9M38/SM_BeamA_9M38/Looks/MI_BeamsA_01

* **Prim路径 (Prim Path):**/World/SortingArea/SM_BeamA_9M38/SM_BeamA_9M38/Looks/MI_BeamsA_01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_BeamA_9M38/SM_BeamA_9M38/Looks/MI_BeamsA_01/MI_CeilingA_06b'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_BeamA_9M38/SM_BeamA_9M38/Looks/MI_BeamsA_01/MI_CeilingA_06b'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_CeilingA_06b.mdl' (Sub Id: 'MI_CeilingA_06b')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_CeilingA_06b.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_D.png'
      * 'ColorAlbedo' [float4] = '(0.145, 0.145, 0.145, 0.000)'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_N.png'
      * 'MainTiling' [float4] = '(1.000, 1.000, 0.000, 1.000)'
      * 'MaskSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_M.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_ORM.png'
      * 'RoughnessMax' [float] = '0.9'
      * 'RoughnessMin' [float] = '0.1'

---

### /World/SortingArea/SM_BeamA_9M39/SM_BeamA_9M39/Looks/MI_BeamsA_01

* **Prim路径 (Prim Path):**/World/SortingArea/SM_BeamA_9M39/SM_BeamA_9M39/Looks/MI_BeamsA_01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_BeamA_9M39/SM_BeamA_9M39/Looks/MI_BeamsA_01/MI_CeilingA_06b'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_BeamA_9M39/SM_BeamA_9M39/Looks/MI_BeamsA_01/MI_CeilingA_06b'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_CeilingA_06b.mdl' (Sub Id: 'MI_CeilingA_06b')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_CeilingA_06b.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_D.png'
      * 'ColorAlbedo' [float4] = '(0.145, 0.145, 0.145, 0.000)'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_N.png'
      * 'MainTiling' [float4] = '(1.000, 1.000, 0.000, 1.000)'
      * 'MaskSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_M.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_ORM.png'
      * 'RoughnessMax' [float] = '0.9'
      * 'RoughnessMin' [float] = '0.1'

---

### /World/SortingArea/SM_BracketBeam_6m10/SM_BracketBeam_6m10/Looks/MI_BeamsA_01

* **Prim路径 (Prim Path):**/World/SortingArea/SM_BracketBeam_6m10/SM_BracketBeam_6m10/Looks/MI_BeamsA_01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_BracketBeam_6m10/SM_BracketBeam_6m10/Looks/MI_BeamsA_01/MI_CeilingA_06b'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_BracketBeam_6m10/SM_BracketBeam_6m10/Looks/MI_BeamsA_01/MI_CeilingA_06b'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_CeilingA_06b.mdl' (Sub Id: 'MI_CeilingA_06b')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_CeilingA_06b.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_D.png'
      * 'ColorAlbedo' [float4] = '(0.145, 0.145, 0.145, 0.000)'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_N.png'
      * 'MainTiling' [float4] = '(1.000, 1.000, 0.000, 1.000)'
      * 'MaskSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_M.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_ORM.png'
      * 'RoughnessMax' [float] = '0.9'
      * 'RoughnessMin' [float] = '0.1'

---

### /World/SortingArea/SM_BracketBeam_6m11/SM_BracketBeam_6m11/Looks/MI_BeamsA_01

* **Prim路径 (Prim Path):**/World/SortingArea/SM_BracketBeam_6m11/SM_BracketBeam_6m11/Looks/MI_BeamsA_01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_BracketBeam_6m11/SM_BracketBeam_6m11/Looks/MI_BeamsA_01/MI_CeilingA_06b'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_BracketBeam_6m11/SM_BracketBeam_6m11/Looks/MI_BeamsA_01/MI_CeilingA_06b'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_CeilingA_06b.mdl' (Sub Id: 'MI_CeilingA_06b')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_CeilingA_06b.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_D.png'
      * 'ColorAlbedo' [float4] = '(0.145, 0.145, 0.145, 0.000)'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_N.png'
      * 'MainTiling' [float4] = '(1.000, 1.000, 0.000, 1.000)'
      * 'MaskSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_M.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_ORM.png'
      * 'RoughnessMax' [float] = '0.9'
      * 'RoughnessMin' [float] = '0.1'

---

### /World/SortingArea/SM_BracketBeam_6m12/SM_BracketBeam_6m12/Looks/MI_BeamsA_01

* **Prim路径 (Prim Path):**/World/SortingArea/SM_BracketBeam_6m12/SM_BracketBeam_6m12/Looks/MI_BeamsA_01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_BracketBeam_6m12/SM_BracketBeam_6m12/Looks/MI_BeamsA_01/MI_CeilingA_06b'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_BracketBeam_6m12/SM_BracketBeam_6m12/Looks/MI_BeamsA_01/MI_CeilingA_06b'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_CeilingA_06b.mdl' (Sub Id: 'MI_CeilingA_06b')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_CeilingA_06b.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_D.png'
      * 'ColorAlbedo' [float4] = '(0.145, 0.145, 0.145, 0.000)'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_N.png'
      * 'MainTiling' [float4] = '(1.000, 1.000, 0.000, 1.000)'
      * 'MaskSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_M.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_ORM.png'
      * 'RoughnessMax' [float] = '0.9'
      * 'RoughnessMin' [float] = '0.1'

---

### /World/SortingArea/SM_BracketBeam_6m13/SM_BracketBeam_6m13/Looks/MI_BeamsA_01

* **Prim路径 (Prim Path):**/World/SortingArea/SM_BracketBeam_6m13/SM_BracketBeam_6m13/Looks/MI_BeamsA_01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_BracketBeam_6m13/SM_BracketBeam_6m13/Looks/MI_BeamsA_01/MI_CeilingA_06b'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_BracketBeam_6m13/SM_BracketBeam_6m13/Looks/MI_BeamsA_01/MI_CeilingA_06b'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_CeilingA_06b.mdl' (Sub Id: 'MI_CeilingA_06b')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_CeilingA_06b.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_D.png'
      * 'ColorAlbedo' [float4] = '(0.145, 0.145, 0.145, 0.000)'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_N.png'
      * 'MainTiling' [float4] = '(1.000, 1.000, 0.000, 1.000)'
      * 'MaskSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_M.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_ORM.png'
      * 'RoughnessMax' [float] = '0.9'
      * 'RoughnessMin' [float] = '0.1'

---

### /World/SortingArea/SM_BracketBeam_6m14/SM_BracketBeam_6m14/Looks/MI_BeamsA_01

* **Prim路径 (Prim Path):**/World/SortingArea/SM_BracketBeam_6m14/SM_BracketBeam_6m14/Looks/MI_BeamsA_01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_BracketBeam_6m14/SM_BracketBeam_6m14/Looks/MI_BeamsA_01/MI_CeilingA_06b'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_BracketBeam_6m14/SM_BracketBeam_6m14/Looks/MI_BeamsA_01/MI_CeilingA_06b'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_CeilingA_06b.mdl' (Sub Id: 'MI_CeilingA_06b')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_CeilingA_06b.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_D.png'
      * 'ColorAlbedo' [float4] = '(0.145, 0.145, 0.145, 0.000)'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_N.png'
      * 'MainTiling' [float4] = '(1.000, 1.000, 0.000, 1.000)'
      * 'MaskSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_M.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_ORM.png'
      * 'RoughnessMax' [float] = '0.9'
      * 'RoughnessMin' [float] = '0.1'

---

### /World/SortingArea/SM_BracketBeam_6m15/SM_BracketBeam_6m15/Looks/MI_BeamsA_01

* **Prim路径 (Prim Path):**/World/SortingArea/SM_BracketBeam_6m15/SM_BracketBeam_6m15/Looks/MI_BeamsA_01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_BracketBeam_6m15/SM_BracketBeam_6m15/Looks/MI_BeamsA_01/MI_CeilingA_06b'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_BracketBeam_6m15/SM_BracketBeam_6m15/Looks/MI_BeamsA_01/MI_CeilingA_06b'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_CeilingA_06b.mdl' (Sub Id: 'MI_CeilingA_06b')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_CeilingA_06b.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_D.png'
      * 'ColorAlbedo' [float4] = '(0.145, 0.145, 0.145, 0.000)'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_N.png'
      * 'MainTiling' [float4] = '(1.000, 1.000, 0.000, 1.000)'
      * 'MaskSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_M.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_ORM.png'
      * 'RoughnessMax' [float] = '0.9'
      * 'RoughnessMin' [float] = '0.1'

---

### /World/SortingArea/SM_BracketBeam_6m16/SM_BracketBeam_6m16/Looks/MI_BeamsA_01

* **Prim路径 (Prim Path):**/World/SortingArea/SM_BracketBeam_6m16/SM_BracketBeam_6m16/Looks/MI_BeamsA_01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_BracketBeam_6m16/SM_BracketBeam_6m16/Looks/MI_BeamsA_01/MI_CeilingA_06b'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_BracketBeam_6m16/SM_BracketBeam_6m16/Looks/MI_BeamsA_01/MI_CeilingA_06b'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_CeilingA_06b.mdl' (Sub Id: 'MI_CeilingA_06b')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_CeilingA_06b.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_D.png'
      * 'ColorAlbedo' [float4] = '(0.145, 0.145, 0.145, 0.000)'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_N.png'
      * 'MainTiling' [float4] = '(1.000, 1.000, 0.000, 1.000)'
      * 'MaskSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_M.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_ORM.png'
      * 'RoughnessMax' [float] = '0.9'
      * 'RoughnessMin' [float] = '0.1'

---

### /World/SortingArea/SM_BracketBeam_6m7/SM_BracketBeam_6m7/Looks/MI_BeamsA_01

* **Prim路径 (Prim Path):**/World/SortingArea/SM_BracketBeam_6m7/SM_BracketBeam_6m7/Looks/MI_BeamsA_01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_BracketBeam_6m7/SM_BracketBeam_6m7/Looks/MI_BeamsA_01/MI_CeilingA_06b'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_BracketBeam_6m7/SM_BracketBeam_6m7/Looks/MI_BeamsA_01/MI_CeilingA_06b'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_CeilingA_06b.mdl' (Sub Id: 'MI_CeilingA_06b')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_CeilingA_06b.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_D.png'
      * 'ColorAlbedo' [float4] = '(0.145, 0.145, 0.145, 0.000)'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_N.png'
      * 'MainTiling' [float4] = '(1.000, 1.000, 0.000, 1.000)'
      * 'MaskSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_M.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_ORM.png'
      * 'RoughnessMax' [float] = '0.9'
      * 'RoughnessMin' [float] = '0.1'

---

### /World/SortingArea/SM_BracketBeam_6m8/SM_BracketBeam_6m8/Looks/MI_BeamsA_01

* **Prim路径 (Prim Path):**/World/SortingArea/SM_BracketBeam_6m8/SM_BracketBeam_6m8/Looks/MI_BeamsA_01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_BracketBeam_6m8/SM_BracketBeam_6m8/Looks/MI_BeamsA_01/MI_CeilingA_06b'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_BracketBeam_6m8/SM_BracketBeam_6m8/Looks/MI_BeamsA_01/MI_CeilingA_06b'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_CeilingA_06b.mdl' (Sub Id: 'MI_CeilingA_06b')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_CeilingA_06b.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_D.png'
      * 'ColorAlbedo' [float4] = '(0.145, 0.145, 0.145, 0.000)'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_N.png'
      * 'MainTiling' [float4] = '(1.000, 1.000, 0.000, 1.000)'
      * 'MaskSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_M.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_ORM.png'
      * 'RoughnessMax' [float] = '0.9'
      * 'RoughnessMin' [float] = '0.1'

---

### /World/SortingArea/SM_BracketBeam_6m9/SM_BracketBeam_6m9/Looks/MI_BeamsA_01

* **Prim路径 (Prim Path):**/World/SortingArea/SM_BracketBeam_6m9/SM_BracketBeam_6m9/Looks/MI_BeamsA_01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_BracketBeam_6m9/SM_BracketBeam_6m9/Looks/MI_BeamsA_01/MI_CeilingA_06b'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_BracketBeam_6m9/SM_BracketBeam_6m9/Looks/MI_BeamsA_01/MI_CeilingA_06b'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_CeilingA_06b.mdl' (Sub Id: 'MI_CeilingA_06b')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_CeilingA_06b.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_D.png'
      * 'ColorAlbedo' [float4] = '(0.145, 0.145, 0.145, 0.000)'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_N.png'
      * 'MainTiling' [float4] = '(1.000, 1.000, 0.000, 1.000)'
      * 'MaskSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_M.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_ORM.png'
      * 'RoughnessMax' [float] = '0.9'
      * 'RoughnessMin' [float] = '0.1'

---

### /World/SortingArea/SM_BracketSlot10/SM_BracketSlot10/Looks/MI_FrameA_01

* **Prim路径 (Prim Path):**/World/SortingArea/SM_BracketSlot10/SM_BracketSlot10/Looks/MI_FrameA_01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_BracketSlot10/SM_BracketSlot10/Looks/MI_FrameA_01/MI_FrameA_01'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_BracketSlot10/SM_BracketSlot10/Looks/MI_FrameA_01/MI_FrameA_01'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_FrameA_01.mdl' (Sub Id: 'MI_FrameA_01')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_FrameA_01.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_D.png'
      * 'ColorAlbedo' [float4] = '(0.145, 0.145, 0.145, 0.000)'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_N.png'
      * 'MainTiling' [float4] = '(1.000, 1.000, 0.000, 1.000)'
      * 'MaskSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_M.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_ORM.png'
      * 'RoughnessMax' [float] = '0.9'
      * 'RoughnessMin' [float] = '0.1'

---

### /World/SortingArea/SM_BracketSlot12/SM_BracketSlot12/Looks/MI_FrameA_01

* **Prim路径 (Prim Path):**/World/SortingArea/SM_BracketSlot12/SM_BracketSlot12/Looks/MI_FrameA_01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_BracketSlot12/SM_BracketSlot12/Looks/MI_FrameA_01/MI_FrameA_01'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_BracketSlot12/SM_BracketSlot12/Looks/MI_FrameA_01/MI_FrameA_01'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_FrameA_01.mdl' (Sub Id: 'MI_FrameA_01')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_FrameA_01.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_D.png'
      * 'ColorAlbedo' [float4] = '(0.145, 0.145, 0.145, 0.000)'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_N.png'
      * 'MainTiling' [float4] = '(1.000, 1.000, 0.000, 1.000)'
      * 'MaskSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_M.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_ORM.png'
      * 'RoughnessMax' [float] = '0.9'
      * 'RoughnessMin' [float] = '0.1'

---

### /World/SortingArea/SM_BracketSlot13/SM_BracketSlot13/Looks/MI_FrameA_01

* **Prim路径 (Prim Path):**/World/SortingArea/SM_BracketSlot13/SM_BracketSlot13/Looks/MI_FrameA_01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_BracketSlot13/SM_BracketSlot13/Looks/MI_FrameA_01/MI_FrameA_01'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_BracketSlot13/SM_BracketSlot13/Looks/MI_FrameA_01/MI_FrameA_01'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_FrameA_01.mdl' (Sub Id: 'MI_FrameA_01')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_FrameA_01.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_D.png'
      * 'ColorAlbedo' [float4] = '(0.145, 0.145, 0.145, 0.000)'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_N.png'
      * 'MainTiling' [float4] = '(1.000, 1.000, 0.000, 1.000)'
      * 'MaskSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_M.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_ORM.png'
      * 'RoughnessMax' [float] = '0.9'
      * 'RoughnessMin' [float] = '0.1'

---

### /World/SortingArea/SM_BracketSlot14/SM_BracketSlot14/Looks/MI_FrameA_01

* **Prim路径 (Prim Path):**/World/SortingArea/SM_BracketSlot14/SM_BracketSlot14/Looks/MI_FrameA_01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_BracketSlot14/SM_BracketSlot14/Looks/MI_FrameA_01/MI_FrameA_01'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_BracketSlot14/SM_BracketSlot14/Looks/MI_FrameA_01/MI_FrameA_01'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_FrameA_01.mdl' (Sub Id: 'MI_FrameA_01')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_FrameA_01.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_D.png'
      * 'ColorAlbedo' [float4] = '(0.145, 0.145, 0.145, 0.000)'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_N.png'
      * 'MainTiling' [float4] = '(1.000, 1.000, 0.000, 1.000)'
      * 'MaskSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_M.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_ORM.png'
      * 'RoughnessMax' [float] = '0.9'
      * 'RoughnessMin' [float] = '0.1'

---

### /World/SortingArea/SM_BracketSlot15/SM_BracketSlot15/Looks/MI_FrameA_01

* **Prim路径 (Prim Path):**/World/SortingArea/SM_BracketSlot15/SM_BracketSlot15/Looks/MI_FrameA_01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_BracketSlot15/SM_BracketSlot15/Looks/MI_FrameA_01/MI_FrameA_01'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_BracketSlot15/SM_BracketSlot15/Looks/MI_FrameA_01/MI_FrameA_01'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_FrameA_01.mdl' (Sub Id: 'MI_FrameA_01')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_FrameA_01.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_D.png'
      * 'ColorAlbedo' [float4] = '(0.145, 0.145, 0.145, 0.000)'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_N.png'
      * 'MainTiling' [float4] = '(1.000, 1.000, 0.000, 1.000)'
      * 'MaskSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_M.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_ORM.png'
      * 'RoughnessMax' [float] = '0.9'
      * 'RoughnessMin' [float] = '0.1'

---

### /World/SortingArea/SM_BracketSlot16/SM_BracketSlot16/Looks/MI_FrameA_01

* **Prim路径 (Prim Path):**/World/SortingArea/SM_BracketSlot16/SM_BracketSlot16/Looks/MI_FrameA_01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_BracketSlot16/SM_BracketSlot16/Looks/MI_FrameA_01/MI_FrameA_01'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_BracketSlot16/SM_BracketSlot16/Looks/MI_FrameA_01/MI_FrameA_01'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_FrameA_01.mdl' (Sub Id: 'MI_FrameA_01')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_FrameA_01.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_D.png'
      * 'ColorAlbedo' [float4] = '(0.145, 0.145, 0.145, 0.000)'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_N.png'
      * 'MainTiling' [float4] = '(1.000, 1.000, 0.000, 1.000)'
      * 'MaskSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_M.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_ORM.png'
      * 'RoughnessMax' [float] = '0.9'
      * 'RoughnessMin' [float] = '0.1'

---

### /World/SortingArea/SM_BracketSlot17/SM_BracketSlot17/Looks/MI_FrameA_01

* **Prim路径 (Prim Path):**/World/SortingArea/SM_BracketSlot17/SM_BracketSlot17/Looks/MI_FrameA_01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_BracketSlot17/SM_BracketSlot17/Looks/MI_FrameA_01/MI_FrameA_01'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_BracketSlot17/SM_BracketSlot17/Looks/MI_FrameA_01/MI_FrameA_01'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_FrameA_01.mdl' (Sub Id: 'MI_FrameA_01')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_FrameA_01.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_D.png'
      * 'ColorAlbedo' [float4] = '(0.145, 0.145, 0.145, 0.000)'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_N.png'
      * 'MainTiling' [float4] = '(1.000, 1.000, 0.000, 1.000)'
      * 'MaskSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_M.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_ORM.png'
      * 'RoughnessMax' [float] = '0.9'
      * 'RoughnessMin' [float] = '0.1'

---

### /World/SortingArea/SM_BracketSlot18/SM_BracketSlot18/Looks/MI_FrameA_01

* **Prim路径 (Prim Path):**/World/SortingArea/SM_BracketSlot18/SM_BracketSlot18/Looks/MI_FrameA_01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_BracketSlot18/SM_BracketSlot18/Looks/MI_FrameA_01/MI_FrameA_01'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_BracketSlot18/SM_BracketSlot18/Looks/MI_FrameA_01/MI_FrameA_01'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_FrameA_01.mdl' (Sub Id: 'MI_FrameA_01')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_FrameA_01.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_D.png'
      * 'ColorAlbedo' [float4] = '(0.145, 0.145, 0.145, 0.000)'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_N.png'
      * 'MainTiling' [float4] = '(1.000, 1.000, 0.000, 1.000)'
      * 'MaskSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_M.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_ORM.png'
      * 'RoughnessMax' [float] = '0.9'
      * 'RoughnessMin' [float] = '0.1'

---

### /World/SortingArea/SM_BracketSlot19/SM_BracketSlot19/Looks/MI_FrameA_01

* **Prim路径 (Prim Path):**/World/SortingArea/SM_BracketSlot19/SM_BracketSlot19/Looks/MI_FrameA_01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_BracketSlot19/SM_BracketSlot19/Looks/MI_FrameA_01/MI_FrameA_01'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_BracketSlot19/SM_BracketSlot19/Looks/MI_FrameA_01/MI_FrameA_01'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_FrameA_01.mdl' (Sub Id: 'MI_FrameA_01')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_FrameA_01.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_D.png'
      * 'ColorAlbedo' [float4] = '(0.145, 0.145, 0.145, 0.000)'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_N.png'
      * 'MainTiling' [float4] = '(1.000, 1.000, 0.000, 1.000)'
      * 'MaskSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_M.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_ORM.png'
      * 'RoughnessMax' [float] = '0.9'
      * 'RoughnessMin' [float] = '0.1'

---

### /World/SortingArea/SM_BracketSlot20/SM_BracketSlot20/Looks/MI_FrameA_01

* **Prim路径 (Prim Path):**/World/SortingArea/SM_BracketSlot20/SM_BracketSlot20/Looks/MI_FrameA_01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_BracketSlot20/SM_BracketSlot20/Looks/MI_FrameA_01/MI_FrameA_01'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_BracketSlot20/SM_BracketSlot20/Looks/MI_FrameA_01/MI_FrameA_01'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_FrameA_01.mdl' (Sub Id: 'MI_FrameA_01')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_FrameA_01.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_D.png'
      * 'ColorAlbedo' [float4] = '(0.145, 0.145, 0.145, 0.000)'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_N.png'
      * 'MainTiling' [float4] = '(1.000, 1.000, 0.000, 1.000)'
      * 'MaskSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_M.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_ORM.png'
      * 'RoughnessMax' [float] = '0.9'
      * 'RoughnessMin' [float] = '0.1'

---

### /World/SortingArea/SM_BracketSlot21/SM_BracketSlot21/Looks/MI_FrameA_01

* **Prim路径 (Prim Path):**/World/SortingArea/SM_BracketSlot21/SM_BracketSlot21/Looks/MI_FrameA_01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_BracketSlot21/SM_BracketSlot21/Looks/MI_FrameA_01/MI_FrameA_01'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_BracketSlot21/SM_BracketSlot21/Looks/MI_FrameA_01/MI_FrameA_01'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_FrameA_01.mdl' (Sub Id: 'MI_FrameA_01')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_FrameA_01.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_D.png'
      * 'ColorAlbedo' [float4] = '(0.145, 0.145, 0.145, 0.000)'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_N.png'
      * 'MainTiling' [float4] = '(1.000, 1.000, 0.000, 1.000)'
      * 'MaskSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_M.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_ORM.png'
      * 'RoughnessMax' [float] = '0.9'
      * 'RoughnessMin' [float] = '0.1'

---

### /World/SortingArea/SM_BracketSlot22/SM_BracketSlot22/Looks/MI_FrameA_01

* **Prim路径 (Prim Path):**/World/SortingArea/SM_BracketSlot22/SM_BracketSlot22/Looks/MI_FrameA_01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_BracketSlot22/SM_BracketSlot22/Looks/MI_FrameA_01/MI_FrameA_01'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_BracketSlot22/SM_BracketSlot22/Looks/MI_FrameA_01/MI_FrameA_01'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_FrameA_01.mdl' (Sub Id: 'MI_FrameA_01')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_FrameA_01.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_D.png'
      * 'ColorAlbedo' [float4] = '(0.145, 0.145, 0.145, 0.000)'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_N.png'
      * 'MainTiling' [float4] = '(1.000, 1.000, 0.000, 1.000)'
      * 'MaskSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_M.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_ORM.png'
      * 'RoughnessMax' [float] = '0.9'
      * 'RoughnessMin' [float] = '0.1'

---

### /World/SortingArea/SM_BracketSlot23/SM_BracketSlot23/Looks/MI_FrameA_01

* **Prim路径 (Prim Path):**/World/SortingArea/SM_BracketSlot23/SM_BracketSlot23/Looks/MI_FrameA_01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_BracketSlot23/SM_BracketSlot23/Looks/MI_FrameA_01/MI_FrameA_01'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_BracketSlot23/SM_BracketSlot23/Looks/MI_FrameA_01/MI_FrameA_01'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_FrameA_01.mdl' (Sub Id: 'MI_FrameA_01')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_FrameA_01.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_D.png'
      * 'ColorAlbedo' [float4] = '(0.145, 0.145, 0.145, 0.000)'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_N.png'
      * 'MainTiling' [float4] = '(1.000, 1.000, 0.000, 1.000)'
      * 'MaskSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_M.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_ORM.png'
      * 'RoughnessMax' [float] = '0.9'
      * 'RoughnessMin' [float] = '0.1'

---

### /World/SortingArea/SM_BracketSlot24/SM_BracketSlot24/Looks/MI_FrameA_01

* **Prim路径 (Prim Path):**/World/SortingArea/SM_BracketSlot24/SM_BracketSlot24/Looks/MI_FrameA_01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_BracketSlot24/SM_BracketSlot24/Looks/MI_FrameA_01/MI_FrameA_01'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_BracketSlot24/SM_BracketSlot24/Looks/MI_FrameA_01/MI_FrameA_01'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_FrameA_01.mdl' (Sub Id: 'MI_FrameA_01')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_FrameA_01.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_D.png'
      * 'ColorAlbedo' [float4] = '(0.145, 0.145, 0.145, 0.000)'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_N.png'
      * 'MainTiling' [float4] = '(1.000, 1.000, 0.000, 1.000)'
      * 'MaskSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_M.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_ORM.png'
      * 'RoughnessMax' [float] = '0.9'
      * 'RoughnessMin' [float] = '0.1'

---

### /World/SortingArea/SM_BracketSlot26_1493/SM_BracketSlot26_1493/Looks/MI_FrameA_01

* **Prim路径 (Prim Path):**/World/SortingArea/SM_BracketSlot26_1493/SM_BracketSlot26_1493/Looks/MI_FrameA_01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_BracketSlot26_1493/SM_BracketSlot26_1493/Looks/MI_FrameA_01/MI_FrameA_01'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_BracketSlot26_1493/SM_BracketSlot26_1493/Looks/MI_FrameA_01/MI_FrameA_01'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_FrameA_01.mdl' (Sub Id: 'MI_FrameA_01')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_FrameA_01.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_D.png'
      * 'ColorAlbedo' [float4] = '(0.145, 0.145, 0.145, 0.000)'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_N.png'
      * 'MainTiling' [float4] = '(1.000, 1.000, 0.000, 1.000)'
      * 'MaskSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_M.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_ORM.png'
      * 'RoughnessMax' [float] = '0.9'
      * 'RoughnessMin' [float] = '0.1'

---

### /World/SortingArea/SM_BracketSlot27/SM_BracketSlot27/Looks/MI_FrameA_01

* **Prim路径 (Prim Path):**/World/SortingArea/SM_BracketSlot27/SM_BracketSlot27/Looks/MI_FrameA_01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_BracketSlot27/SM_BracketSlot27/Looks/MI_FrameA_01/MI_FrameA_01'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_BracketSlot27/SM_BracketSlot27/Looks/MI_FrameA_01/MI_FrameA_01'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_FrameA_01.mdl' (Sub Id: 'MI_FrameA_01')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_FrameA_01.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_D.png'
      * 'ColorAlbedo' [float4] = '(0.145, 0.145, 0.145, 0.000)'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_N.png'
      * 'MainTiling' [float4] = '(1.000, 1.000, 0.000, 1.000)'
      * 'MaskSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_M.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_ORM.png'
      * 'RoughnessMax' [float] = '0.9'
      * 'RoughnessMin' [float] = '0.1'

---

### /World/SortingArea/SM_BracketSlot3/SM_BracketSlot3/Looks/MI_FrameA_01

* **Prim路径 (Prim Path):**/World/SortingArea/SM_BracketSlot3/SM_BracketSlot3/Looks/MI_FrameA_01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_BracketSlot3/SM_BracketSlot3/Looks/MI_FrameA_01/MI_FrameA_01'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_BracketSlot3/SM_BracketSlot3/Looks/MI_FrameA_01/MI_FrameA_01'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_FrameA_01.mdl' (Sub Id: 'MI_FrameA_01')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_FrameA_01.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_D.png'
      * 'ColorAlbedo' [float4] = '(0.145, 0.145, 0.145, 0.000)'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_N.png'
      * 'MainTiling' [float4] = '(1.000, 1.000, 0.000, 1.000)'
      * 'MaskSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_M.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_ORM.png'
      * 'RoughnessMax' [float] = '0.9'
      * 'RoughnessMin' [float] = '0.1'

---

### /World/SortingArea/SM_BracketSlot41/SM_BracketSlot41/Looks/MI_FrameA_01

* **Prim路径 (Prim Path):**/World/SortingArea/SM_BracketSlot41/SM_BracketSlot41/Looks/MI_FrameA_01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_BracketSlot41/SM_BracketSlot41/Looks/MI_FrameA_01/MI_FrameA_01'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_BracketSlot41/SM_BracketSlot41/Looks/MI_FrameA_01/MI_FrameA_01'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_FrameA_01.mdl' (Sub Id: 'MI_FrameA_01')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_FrameA_01.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_D.png'
      * 'ColorAlbedo' [float4] = '(0.145, 0.145, 0.145, 0.000)'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_N.png'
      * 'MainTiling' [float4] = '(1.000, 1.000, 0.000, 1.000)'
      * 'MaskSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_M.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_ORM.png'
      * 'RoughnessMax' [float] = '0.9'
      * 'RoughnessMin' [float] = '0.1'

---

### /World/SortingArea/SM_BracketSlot8/SM_BracketSlot8/Looks/MI_FrameA_01

* **Prim路径 (Prim Path):**/World/SortingArea/SM_BracketSlot8/SM_BracketSlot8/Looks/MI_FrameA_01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_BracketSlot8/SM_BracketSlot8/Looks/MI_FrameA_01/MI_FrameA_01'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_BracketSlot8/SM_BracketSlot8/Looks/MI_FrameA_01/MI_FrameA_01'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_FrameA_01.mdl' (Sub Id: 'MI_FrameA_01')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_FrameA_01.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_D.png'
      * 'ColorAlbedo' [float4] = '(0.145, 0.145, 0.145, 0.000)'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_N.png'
      * 'MainTiling' [float4] = '(1.000, 1.000, 0.000, 1.000)'
      * 'MaskSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_M.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_ORM.png'
      * 'RoughnessMax' [float] = '0.9'
      * 'RoughnessMin' [float] = '0.1'

---

### /World/SortingArea/SM_BracketSlot9/SM_BracketSlot9/Looks/MI_FrameA_01

* **Prim路径 (Prim Path):**/World/SortingArea/SM_BracketSlot9/SM_BracketSlot9/Looks/MI_FrameA_01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_BracketSlot9/SM_BracketSlot9/Looks/MI_FrameA_01/MI_FrameA_01'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_BracketSlot9/SM_BracketSlot9/Looks/MI_FrameA_01/MI_FrameA_01'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_FrameA_01.mdl' (Sub Id: 'MI_FrameA_01')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_FrameA_01.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_D.png'
      * 'ColorAlbedo' [float4] = '(0.145, 0.145, 0.145, 0.000)'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_N.png'
      * 'MainTiling' [float4] = '(1.000, 1.000, 0.000, 1.000)'
      * 'MaskSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_M.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_ORM.png'
      * 'RoughnessMax' [float] = '0.9'
      * 'RoughnessMin' [float] = '0.1'

---

### /World/SortingArea/SM_CeilingA_6X17/SM_CeilingA_6X17/Looks/MI_WallB_01

* **Prim路径 (Prim Path):**/World/SortingArea/SM_CeilingA_6X17/SM_CeilingA_6X17/Looks/MI_WallB_01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_CeilingA_6X17/SM_CeilingA_6X17/Looks/MI_WallB_01/MI_WallB_01'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_CeilingA_6X17/SM_CeilingA_6X17/Looks/MI_WallB_01/MI_WallB_01'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_WallB_01.mdl' (Sub Id: 'MI_WallB_01')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_WallB_01.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BlankMask_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_02_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_02_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_02_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_02_D.png'
      * 'ColorAlbedo' [float4] = '(0.145, 0.145, 0.145, 0.000)'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_02_N.png'
      * 'MainNormalStrenght' [float4] = '(1.000, 1.000, 0.900, 1.000)'
      * 'MainTiling' [float4] = '(1.000, 1.000, 0.000, 1.000)'
      * 'MaskSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BlankMask_M.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_02_ORM.png'
      * 'RoughnessMax' [float] = '3.306332'
      * 'RoughnessMin' [float] = '-0.046789'

---

### /World/SortingArea/SM_CeilingA_6X19/SM_CeilingA_6X19/Looks/MI_WallB_01

* **Prim路径 (Prim Path):**/World/SortingArea/SM_CeilingA_6X19/SM_CeilingA_6X19/Looks/MI_WallB_01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_CeilingA_6X19/SM_CeilingA_6X19/Looks/MI_WallB_01/MI_WallB_01'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_CeilingA_6X19/SM_CeilingA_6X19/Looks/MI_WallB_01/MI_WallB_01'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_WallB_01.mdl' (Sub Id: 'MI_WallB_01')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_WallB_01.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BlankMask_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_02_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_02_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_02_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_02_D.png'
      * 'ColorAlbedo' [float4] = '(0.145, 0.145, 0.145, 0.000)'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_02_N.png'
      * 'MainNormalStrenght' [float4] = '(1.000, 1.000, 0.900, 1.000)'
      * 'MainTiling' [float4] = '(1.000, 1.000, 0.000, 1.000)'
      * 'MaskSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BlankMask_M.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_02_ORM.png'
      * 'RoughnessMax' [float] = '3.306332'
      * 'RoughnessMin' [float] = '-0.046789'

---

### /World/SortingArea/SM_CeilingA_6X21/SM_CeilingA_6X21/Looks/MI_WallB_01

* **Prim路径 (Prim Path):**/World/SortingArea/SM_CeilingA_6X21/SM_CeilingA_6X21/Looks/MI_WallB_01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_CeilingA_6X21/SM_CeilingA_6X21/Looks/MI_WallB_01/MI_WallB_01'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_CeilingA_6X21/SM_CeilingA_6X21/Looks/MI_WallB_01/MI_WallB_01'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_WallB_01.mdl' (Sub Id: 'MI_WallB_01')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_WallB_01.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BlankMask_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_02_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_02_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_02_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_02_D.png'
      * 'ColorAlbedo' [float4] = '(0.145, 0.145, 0.145, 0.000)'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_02_N.png'
      * 'MainNormalStrenght' [float4] = '(1.000, 1.000, 0.900, 1.000)'
      * 'MainTiling' [float4] = '(1.000, 1.000, 0.000, 1.000)'
      * 'MaskSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BlankMask_M.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_02_ORM.png'
      * 'RoughnessMax' [float] = '3.306332'
      * 'RoughnessMin' [float] = '-0.046789'

---

### /World/SortingArea/SM_CeilingA_6X23/SM_CeilingA_6X23/Looks/MI_WallB_01

* **Prim路径 (Prim Path):**/World/SortingArea/SM_CeilingA_6X23/SM_CeilingA_6X23/Looks/MI_WallB_01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_CeilingA_6X23/SM_CeilingA_6X23/Looks/MI_WallB_01/MI_WallB_01'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_CeilingA_6X23/SM_CeilingA_6X23/Looks/MI_WallB_01/MI_WallB_01'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_WallB_01.mdl' (Sub Id: 'MI_WallB_01')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_WallB_01.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BlankMask_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_02_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_02_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_02_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_02_D.png'
      * 'ColorAlbedo' [float4] = '(0.145, 0.145, 0.145, 0.000)'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_02_N.png'
      * 'MainNormalStrenght' [float4] = '(1.000, 1.000, 0.900, 1.000)'
      * 'MainTiling' [float4] = '(1.000, 1.000, 0.000, 1.000)'
      * 'MaskSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BlankMask_M.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_02_ORM.png'
      * 'RoughnessMax' [float] = '3.306332'
      * 'RoughnessMin' [float] = '-0.046789'

---

### /World/SortingArea/SM_CeilingA_6X25/SM_CeilingA_6X25/Looks/MI_WallB_01

* **Prim路径 (Prim Path):**/World/SortingArea/SM_CeilingA_6X25/SM_CeilingA_6X25/Looks/MI_WallB_01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_CeilingA_6X25/SM_CeilingA_6X25/Looks/MI_WallB_01/MI_WallB_01'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_CeilingA_6X25/SM_CeilingA_6X25/Looks/MI_WallB_01/MI_WallB_01'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_WallB_01.mdl' (Sub Id: 'MI_WallB_01')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_WallB_01.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BlankMask_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_02_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_02_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_02_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_02_D.png'
      * 'ColorAlbedo' [float4] = '(0.145, 0.145, 0.145, 0.000)'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_02_N.png'
      * 'MainNormalStrenght' [float4] = '(1.000, 1.000, 0.900, 1.000)'
      * 'MainTiling' [float4] = '(1.000, 1.000, 0.000, 1.000)'
      * 'MaskSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BlankMask_M.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_02_ORM.png'
      * 'RoughnessMax' [float] = '3.306332'
      * 'RoughnessMin' [float] = '-0.046789'

---

### /World/SortingArea/SM_CeilingA_6X27/SM_CeilingA_6X27/Looks/MI_WallB_01

* **Prim路径 (Prim Path):**/World/SortingArea/SM_CeilingA_6X27/SM_CeilingA_6X27/Looks/MI_WallB_01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_CeilingA_6X27/SM_CeilingA_6X27/Looks/MI_WallB_01/MI_WallB_01'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_CeilingA_6X27/SM_CeilingA_6X27/Looks/MI_WallB_01/MI_WallB_01'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_WallB_01.mdl' (Sub Id: 'MI_WallB_01')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_WallB_01.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BlankMask_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_02_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_02_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_02_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_02_D.png'
      * 'ColorAlbedo' [float4] = '(0.145, 0.145, 0.145, 0.000)'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_02_N.png'
      * 'MainNormalStrenght' [float4] = '(1.000, 1.000, 0.900, 1.000)'
      * 'MainTiling' [float4] = '(1.000, 1.000, 0.000, 1.000)'
      * 'MaskSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BlankMask_M.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_02_ORM.png'
      * 'RoughnessMax' [float] = '3.306332'
      * 'RoughnessMin' [float] = '-0.046789'

---

### /World/SortingArea/SM_CeilingA_6X28/SM_CeilingA_6X28/Looks/MI_WallB_01

* **Prim路径 (Prim Path):**/World/SortingArea/SM_CeilingA_6X28/SM_CeilingA_6X28/Looks/MI_WallB_01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_CeilingA_6X28/SM_CeilingA_6X28/Looks/MI_WallB_01/MI_WallB_01'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_CeilingA_6X28/SM_CeilingA_6X28/Looks/MI_WallB_01/MI_WallB_01'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_WallB_01.mdl' (Sub Id: 'MI_WallB_01')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_WallB_01.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BlankMask_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_02_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_02_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_02_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_02_D.png'
      * 'ColorAlbedo' [float4] = '(0.145, 0.145, 0.145, 0.000)'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_02_N.png'
      * 'MainNormalStrenght' [float4] = '(1.000, 1.000, 0.900, 1.000)'
      * 'MainTiling' [float4] = '(1.000, 1.000, 0.000, 1.000)'
      * 'MaskSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BlankMask_M.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_02_ORM.png'
      * 'RoughnessMax' [float] = '3.306332'
      * 'RoughnessMin' [float] = '-0.046789'

---

### /World/SortingArea/SM_CeilingA_6X29/SM_CeilingA_6X29/Looks/MI_WallB_01

* **Prim路径 (Prim Path):**/World/SortingArea/SM_CeilingA_6X29/SM_CeilingA_6X29/Looks/MI_WallB_01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_CeilingA_6X29/SM_CeilingA_6X29/Looks/MI_WallB_01/MI_WallB_01'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_CeilingA_6X29/SM_CeilingA_6X29/Looks/MI_WallB_01/MI_WallB_01'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_WallB_01.mdl' (Sub Id: 'MI_WallB_01')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_WallB_01.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BlankMask_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_02_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_02_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_02_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_02_D.png'
      * 'ColorAlbedo' [float4] = '(0.145, 0.145, 0.145, 0.000)'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_02_N.png'
      * 'MainNormalStrenght' [float4] = '(1.000, 1.000, 0.900, 1.000)'
      * 'MainTiling' [float4] = '(1.000, 1.000, 0.000, 1.000)'
      * 'MaskSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BlankMask_M.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_02_ORM.png'
      * 'RoughnessMax' [float] = '3.306332'
      * 'RoughnessMin' [float] = '-0.046789'

---

### /World/SortingArea/SM_CeilingA_6X30/SM_CeilingA_6X30/Looks/MI_WallB_01

* **Prim路径 (Prim Path):**/World/SortingArea/SM_CeilingA_6X30/SM_CeilingA_6X30/Looks/MI_WallB_01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_CeilingA_6X30/SM_CeilingA_6X30/Looks/MI_WallB_01/MI_WallB_01'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_CeilingA_6X30/SM_CeilingA_6X30/Looks/MI_WallB_01/MI_WallB_01'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_WallB_01.mdl' (Sub Id: 'MI_WallB_01')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_WallB_01.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BlankMask_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_02_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_02_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_02_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_02_D.png'
      * 'ColorAlbedo' [float4] = '(0.145, 0.145, 0.145, 0.000)'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_02_N.png'
      * 'MainNormalStrenght' [float4] = '(1.000, 1.000, 0.900, 1.000)'
      * 'MainTiling' [float4] = '(1.000, 1.000, 0.000, 1.000)'
      * 'MaskSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BlankMask_M.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_02_ORM.png'
      * 'RoughnessMax' [float] = '3.306332'
      * 'RoughnessMin' [float] = '-0.046789'

---

### /World/SortingArea/SM_CeilingA_6X31/SM_CeilingA_6X31/Looks/MI_WallB_01

* **Prim路径 (Prim Path):**/World/SortingArea/SM_CeilingA_6X31/SM_CeilingA_6X31/Looks/MI_WallB_01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_CeilingA_6X31/SM_CeilingA_6X31/Looks/MI_WallB_01/MI_WallB_01'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_CeilingA_6X31/SM_CeilingA_6X31/Looks/MI_WallB_01/MI_WallB_01'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_WallB_01.mdl' (Sub Id: 'MI_WallB_01')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_WallB_01.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BlankMask_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_02_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_02_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_02_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_02_D.png'
      * 'ColorAlbedo' [float4] = '(0.145, 0.145, 0.145, 0.000)'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_02_N.png'
      * 'MainNormalStrenght' [float4] = '(1.000, 1.000, 0.900, 1.000)'
      * 'MainTiling' [float4] = '(1.000, 1.000, 0.000, 1.000)'
      * 'MaskSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BlankMask_M.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_02_ORM.png'
      * 'RoughnessMax' [float] = '3.306332'
      * 'RoughnessMin' [float] = '-0.046789'

---

### /World/SortingArea/SM_CeilingA_6X34/SM_CeilingA_6X34/Looks/MI_WallB_01

* **Prim路径 (Prim Path):**/World/SortingArea/SM_CeilingA_6X34/SM_CeilingA_6X34/Looks/MI_WallB_01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_CeilingA_6X34/SM_CeilingA_6X34/Looks/MI_WallB_01/MI_WallB_01'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_CeilingA_6X34/SM_CeilingA_6X34/Looks/MI_WallB_01/MI_WallB_01'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_WallB_01.mdl' (Sub Id: 'MI_WallB_01')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_WallB_01.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BlankMask_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_02_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_02_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_02_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_02_D.png'
      * 'ColorAlbedo' [float4] = '(0.145, 0.145, 0.145, 0.000)'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_02_N.png'
      * 'MainNormalStrenght' [float4] = '(1.000, 1.000, 0.900, 1.000)'
      * 'MainTiling' [float4] = '(1.000, 1.000, 0.000, 1.000)'
      * 'MaskSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BlankMask_M.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_02_ORM.png'
      * 'RoughnessMax' [float] = '3.306332'
      * 'RoughnessMin' [float] = '-0.046789'

---

### /World/SortingArea/SM_CeilingA_6X36/SM_CeilingA_6X36/Looks/MI_WallB_01

* **Prim路径 (Prim Path):**/World/SortingArea/SM_CeilingA_6X36/SM_CeilingA_6X36/Looks/MI_WallB_01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_CeilingA_6X36/SM_CeilingA_6X36/Looks/MI_WallB_01/MI_WallB_01'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_CeilingA_6X36/SM_CeilingA_6X36/Looks/MI_WallB_01/MI_WallB_01'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_WallB_01.mdl' (Sub Id: 'MI_WallB_01')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_WallB_01.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BlankMask_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_02_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_02_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_02_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_02_D.png'
      * 'ColorAlbedo' [float4] = '(0.145, 0.145, 0.145, 0.000)'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_02_N.png'
      * 'MainNormalStrenght' [float4] = '(1.000, 1.000, 0.900, 1.000)'
      * 'MainTiling' [float4] = '(1.000, 1.000, 0.000, 1.000)'
      * 'MaskSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BlankMask_M.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_02_ORM.png'
      * 'RoughnessMax' [float] = '3.306332'
      * 'RoughnessMin' [float] = '-0.046789'

---

### /World/SortingArea/SM_CeilingA_6X37/SM_CeilingA_6X37/Looks/MI_WallB_01

* **Prim路径 (Prim Path):**/World/SortingArea/SM_CeilingA_6X37/SM_CeilingA_6X37/Looks/MI_WallB_01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_CeilingA_6X37/SM_CeilingA_6X37/Looks/MI_WallB_01/MI_WallB_01'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_CeilingA_6X37/SM_CeilingA_6X37/Looks/MI_WallB_01/MI_WallB_01'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_WallB_01.mdl' (Sub Id: 'MI_WallB_01')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_WallB_01.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BlankMask_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_02_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_02_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_02_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_02_D.png'
      * 'ColorAlbedo' [float4] = '(0.145, 0.145, 0.145, 0.000)'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_02_N.png'
      * 'MainNormalStrenght' [float4] = '(1.000, 1.000, 0.900, 1.000)'
      * 'MainTiling' [float4] = '(1.000, 1.000, 0.000, 1.000)'
      * 'MaskSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BlankMask_M.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_02_ORM.png'
      * 'RoughnessMax' [float] = '3.306332'
      * 'RoughnessMin' [float] = '-0.046789'

---

### /World/SortingArea/SM_CeilingA_6X38/SM_CeilingA_6X38/Looks/MI_WallB_01

* **Prim路径 (Prim Path):**/World/SortingArea/SM_CeilingA_6X38/SM_CeilingA_6X38/Looks/MI_WallB_01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_CeilingA_6X38/SM_CeilingA_6X38/Looks/MI_WallB_01/MI_WallB_01'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_CeilingA_6X38/SM_CeilingA_6X38/Looks/MI_WallB_01/MI_WallB_01'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_WallB_01.mdl' (Sub Id: 'MI_WallB_01')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_WallB_01.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BlankMask_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_02_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_02_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_02_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_02_D.png'
      * 'ColorAlbedo' [float4] = '(0.145, 0.145, 0.145, 0.000)'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_02_N.png'
      * 'MainNormalStrenght' [float4] = '(1.000, 1.000, 0.900, 1.000)'
      * 'MainTiling' [float4] = '(1.000, 1.000, 0.000, 1.000)'
      * 'MaskSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BlankMask_M.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_02_ORM.png'
      * 'RoughnessMax' [float] = '3.306332'
      * 'RoughnessMin' [float] = '-0.046789'

---

### /World/SortingArea/SM_CeilingA_6X39/SM_CeilingA_6X39/Looks/MI_WallB_01

* **Prim路径 (Prim Path):**/World/SortingArea/SM_CeilingA_6X39/SM_CeilingA_6X39/Looks/MI_WallB_01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_CeilingA_6X39/SM_CeilingA_6X39/Looks/MI_WallB_01/MI_WallB_01'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_CeilingA_6X39/SM_CeilingA_6X39/Looks/MI_WallB_01/MI_WallB_01'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_WallB_01.mdl' (Sub Id: 'MI_WallB_01')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_WallB_01.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BlankMask_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_02_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_02_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_02_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_02_D.png'
      * 'ColorAlbedo' [float4] = '(0.145, 0.145, 0.145, 0.000)'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_02_N.png'
      * 'MainNormalStrenght' [float4] = '(1.000, 1.000, 0.900, 1.000)'
      * 'MainTiling' [float4] = '(1.000, 1.000, 0.000, 1.000)'
      * 'MaskSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BlankMask_M.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_02_ORM.png'
      * 'RoughnessMax' [float] = '3.306332'
      * 'RoughnessMin' [float] = '-0.046789'

---

### /World/SortingArea/SM_CeilingA_6X40/SM_CeilingA_6X40/Looks/MI_WallB_01

* **Prim路径 (Prim Path):**/World/SortingArea/SM_CeilingA_6X40/SM_CeilingA_6X40/Looks/MI_WallB_01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_CeilingA_6X40/SM_CeilingA_6X40/Looks/MI_WallB_01/MI_WallB_01'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_CeilingA_6X40/SM_CeilingA_6X40/Looks/MI_WallB_01/MI_WallB_01'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_WallB_01.mdl' (Sub Id: 'MI_WallB_01')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_WallB_01.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BlankMask_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_02_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_02_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_02_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_02_D.png'
      * 'ColorAlbedo' [float4] = '(0.145, 0.145, 0.145, 0.000)'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_02_N.png'
      * 'MainNormalStrenght' [float4] = '(1.000, 1.000, 0.900, 1.000)'
      * 'MainTiling' [float4] = '(1.000, 1.000, 0.000, 1.000)'
      * 'MaskSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BlankMask_M.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_02_ORM.png'
      * 'RoughnessMax' [float] = '3.306332'
      * 'RoughnessMin' [float] = '-0.046789'

---

### /World/SortingArea/SM_CeilingA_6X41/SM_CeilingA_6X41/Looks/MI_WallB_01

* **Prim路径 (Prim Path):**/World/SortingArea/SM_CeilingA_6X41/SM_CeilingA_6X41/Looks/MI_WallB_01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_CeilingA_6X41/SM_CeilingA_6X41/Looks/MI_WallB_01/MI_WallB_01'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_CeilingA_6X41/SM_CeilingA_6X41/Looks/MI_WallB_01/MI_WallB_01'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_WallB_01.mdl' (Sub Id: 'MI_WallB_01')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_WallB_01.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BlankMask_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_02_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_02_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_02_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_02_D.png'
      * 'ColorAlbedo' [float4] = '(0.145, 0.145, 0.145, 0.000)'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_02_N.png'
      * 'MainNormalStrenght' [float4] = '(1.000, 1.000, 0.900, 1.000)'
      * 'MainTiling' [float4] = '(1.000, 1.000, 0.000, 1.000)'
      * 'MaskSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BlankMask_M.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_02_ORM.png'
      * 'RoughnessMax' [float] = '3.306332'
      * 'RoughnessMin' [float] = '-0.046789'

---

### /World/SortingArea/SM_CeilingA_6X42/SM_CeilingA_6X42/Looks/MI_WallB_01

* **Prim路径 (Prim Path):**/World/SortingArea/SM_CeilingA_6X42/SM_CeilingA_6X42/Looks/MI_WallB_01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_CeilingA_6X42/SM_CeilingA_6X42/Looks/MI_WallB_01/MI_WallB_01'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_CeilingA_6X42/SM_CeilingA_6X42/Looks/MI_WallB_01/MI_WallB_01'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_WallB_01.mdl' (Sub Id: 'MI_WallB_01')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_WallB_01.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BlankMask_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_02_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_02_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_02_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_02_D.png'
      * 'ColorAlbedo' [float4] = '(0.145, 0.145, 0.145, 0.000)'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_02_N.png'
      * 'MainNormalStrenght' [float4] = '(1.000, 1.000, 0.900, 1.000)'
      * 'MainTiling' [float4] = '(1.000, 1.000, 0.000, 1.000)'
      * 'MaskSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BlankMask_M.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_02_ORM.png'
      * 'RoughnessMax' [float] = '3.306332'
      * 'RoughnessMin' [float] = '-0.046789'

---

### /World/SortingArea/SM_CeilingA_6X43/SM_CeilingA_6X43/Looks/MI_WallB_01

* **Prim路径 (Prim Path):**/World/SortingArea/SM_CeilingA_6X43/SM_CeilingA_6X43/Looks/MI_WallB_01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_CeilingA_6X43/SM_CeilingA_6X43/Looks/MI_WallB_01/MI_WallB_01'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_CeilingA_6X43/SM_CeilingA_6X43/Looks/MI_WallB_01/MI_WallB_01'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_WallB_01.mdl' (Sub Id: 'MI_WallB_01')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_WallB_01.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BlankMask_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_02_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_02_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_02_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_02_D.png'
      * 'ColorAlbedo' [float4] = '(0.145, 0.145, 0.145, 0.000)'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_02_N.png'
      * 'MainNormalStrenght' [float4] = '(1.000, 1.000, 0.900, 1.000)'
      * 'MainTiling' [float4] = '(1.000, 1.000, 0.000, 1.000)'
      * 'MaskSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BlankMask_M.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_02_ORM.png'
      * 'RoughnessMax' [float] = '3.306332'
      * 'RoughnessMin' [float] = '-0.046789'

---

### /World/SortingArea/SM_CeilingA_6X58/SM_CeilingA_6X58/Looks/MI_WallB_01

* **Prim路径 (Prim Path):**/World/SortingArea/SM_CeilingA_6X58/SM_CeilingA_6X58/Looks/MI_WallB_01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_CeilingA_6X58/SM_CeilingA_6X58/Looks/MI_WallB_01/MI_WallB_01'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_CeilingA_6X58/SM_CeilingA_6X58/Looks/MI_WallB_01/MI_WallB_01'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_WallB_01.mdl' (Sub Id: 'MI_WallB_01')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_WallB_01.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BlankMask_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_02_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_02_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_02_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_02_D.png'
      * 'ColorAlbedo' [float4] = '(0.145, 0.145, 0.145, 0.000)'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_02_N.png'
      * 'MainNormalStrenght' [float4] = '(1.000, 1.000, 0.900, 1.000)'
      * 'MainTiling' [float4] = '(1.000, 1.000, 0.000, 1.000)'
      * 'MaskSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BlankMask_M.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_02_ORM.png'
      * 'RoughnessMax' [float] = '3.306332'
      * 'RoughnessMin' [float] = '-0.046789'

---

### /World/SortingArea/SM_CeilingA_6X75/SM_CeilingA_6X75/Looks/MI_WallB_01

* **Prim路径 (Prim Path):**/World/SortingArea/SM_CeilingA_6X75/SM_CeilingA_6X75/Looks/MI_WallB_01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_CeilingA_6X75/SM_CeilingA_6X75/Looks/MI_WallB_01/MI_WallB_01'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_CeilingA_6X75/SM_CeilingA_6X75/Looks/MI_WallB_01/MI_WallB_01'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_WallB_01.mdl' (Sub Id: 'MI_WallB_01')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_WallB_01.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BlankMask_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_02_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_02_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_02_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_02_D.png'
      * 'ColorAlbedo' [float4] = '(0.145, 0.145, 0.145, 0.000)'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_02_N.png'
      * 'MainNormalStrenght' [float4] = '(1.000, 1.000, 0.900, 1.000)'
      * 'MainTiling' [float4] = '(1.000, 1.000, 0.000, 1.000)'
      * 'MaskSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BlankMask_M.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_02_ORM.png'
      * 'RoughnessMax' [float] = '3.306332'
      * 'RoughnessMin' [float] = '-0.046789'

---

### /World/SortingArea/SM_CeilingA_6X76/SM_CeilingA_6X76/Looks/MI_WallB_01

* **Prim路径 (Prim Path):**/World/SortingArea/SM_CeilingA_6X76/SM_CeilingA_6X76/Looks/MI_WallB_01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_CeilingA_6X76/SM_CeilingA_6X76/Looks/MI_WallB_01/MI_WallB_01'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_CeilingA_6X76/SM_CeilingA_6X76/Looks/MI_WallB_01/MI_WallB_01'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_WallB_01.mdl' (Sub Id: 'MI_WallB_01')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_WallB_01.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BlankMask_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_02_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_02_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_02_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_02_D.png'
      * 'ColorAlbedo' [float4] = '(0.145, 0.145, 0.145, 0.000)'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_02_N.png'
      * 'MainNormalStrenght' [float4] = '(1.000, 1.000, 0.900, 1.000)'
      * 'MainTiling' [float4] = '(1.000, 1.000, 0.000, 1.000)'
      * 'MaskSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BlankMask_M.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_02_ORM.png'
      * 'RoughnessMax' [float] = '3.306332'
      * 'RoughnessMin' [float] = '-0.046789'

---

### /World/SortingArea/SM_CeilingA_6X77/SM_CeilingA_6X77/Looks/MI_WallB_01

* **Prim路径 (Prim Path):**/World/SortingArea/SM_CeilingA_6X77/SM_CeilingA_6X77/Looks/MI_WallB_01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_CeilingA_6X77/SM_CeilingA_6X77/Looks/MI_WallB_01/MI_WallB_01'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_CeilingA_6X77/SM_CeilingA_6X77/Looks/MI_WallB_01/MI_WallB_01'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_WallB_01.mdl' (Sub Id: 'MI_WallB_01')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_WallB_01.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BlankMask_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_02_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_02_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_02_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_02_D.png'
      * 'ColorAlbedo' [float4] = '(0.145, 0.145, 0.145, 0.000)'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_02_N.png'
      * 'MainNormalStrenght' [float4] = '(1.000, 1.000, 0.900, 1.000)'
      * 'MainTiling' [float4] = '(1.000, 1.000, 0.000, 1.000)'
      * 'MaskSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BlankMask_M.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_02_ORM.png'
      * 'RoughnessMax' [float] = '3.306332'
      * 'RoughnessMin' [float] = '-0.046789'

---

### /World/SortingArea/SM_CeilingA_6X84/SM_CeilingA_6X84/Looks/MI_WallB_01

* **Prim路径 (Prim Path):**/World/SortingArea/SM_CeilingA_6X84/SM_CeilingA_6X84/Looks/MI_WallB_01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_CeilingA_6X84/SM_CeilingA_6X84/Looks/MI_WallB_01/MI_WallB_01'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_CeilingA_6X84/SM_CeilingA_6X84/Looks/MI_WallB_01/MI_WallB_01'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_WallB_01.mdl' (Sub Id: 'MI_WallB_01')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_WallB_01.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BlankMask_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_02_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_02_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_02_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_02_D.png'
      * 'ColorAlbedo' [float4] = '(0.145, 0.145, 0.145, 0.000)'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_02_N.png'
      * 'MainNormalStrenght' [float4] = '(1.000, 1.000, 0.900, 1.000)'
      * 'MainTiling' [float4] = '(1.000, 1.000, 0.000, 1.000)'
      * 'MaskSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BlankMask_M.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_02_ORM.png'
      * 'RoughnessMax' [float] = '3.306332'
      * 'RoughnessMin' [float] = '-0.046789'

---

### /World/SortingArea/SM_FloorDecal_Keepclear6_446/SM_FloorDecal_Keepclear6_446/Looks/M_FloorStripes_01

* **Prim路径 (Prim Path):**/World/SortingArea/SM_FloorDecal_Keepclear6_446/SM_FloorDecal_Keepclear6_446/Looks/M_FloorStripes_01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_FloorDecal_Keepclear6_446/SM_FloorDecal_Keepclear6_446/Looks/M_FloorStripes_01/M_WallBoard_01'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_FloorDecal_Keepclear6_446/SM_FloorDecal_Keepclear6_446/Looks/M_FloorStripes_01/M_WallBoard_01'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/M_WallBoard_01.mdl' (Sub Id: 'M_WallBoard_01')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/M_WallBoard_01.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FloorStripes_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FloorStripes_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FloorStripes_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FloorStripes_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FloorStripes_D.png'
      * 'AlphaSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FloorStripes_M.png'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FloorStripes_N.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FloorStripes_ORM.png'
      * 'RoughnessMax' [float] = '2.204305'
      * 'RoughnessMin' [float] = '0.044954'

---

### /World/SortingArea/SM_FloorDecal_RecRed1X15/SM_FloorDecal_RecRed1X15/Looks/M_FloorStripes_01

* **Prim路径 (Prim Path):**/World/SortingArea/SM_FloorDecal_RecRed1X15/SM_FloorDecal_RecRed1X15/Looks/M_FloorStripes_01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_FloorDecal_RecRed1X15/SM_FloorDecal_RecRed1X15/Looks/M_FloorStripes_01/M_WallBoard_01'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_FloorDecal_RecRed1X15/SM_FloorDecal_RecRed1X15/Looks/M_FloorStripes_01/M_WallBoard_01'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/M_WallBoard_01.mdl' (Sub Id: 'M_WallBoard_01')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/M_WallBoard_01.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FloorStripes_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FloorStripes_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FloorStripes_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FloorStripes_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FloorStripes_D.png'
      * 'AlphaSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FloorStripes_M.png'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FloorStripes_N.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FloorStripes_ORM.png'
      * 'RoughnessMax' [float] = '2.204305'
      * 'RoughnessMin' [float] = '0.044954'

---

### /World/SortingArea/SM_FloorDecal_RecRed1X16/SM_FloorDecal_RecRed1X16/Looks/M_FloorStripes_01

* **Prim路径 (Prim Path):**/World/SortingArea/SM_FloorDecal_RecRed1X16/SM_FloorDecal_RecRed1X16/Looks/M_FloorStripes_01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_FloorDecal_RecRed1X16/SM_FloorDecal_RecRed1X16/Looks/M_FloorStripes_01/M_WallBoard_01'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_FloorDecal_RecRed1X16/SM_FloorDecal_RecRed1X16/Looks/M_FloorStripes_01/M_WallBoard_01'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/M_WallBoard_01.mdl' (Sub Id: 'M_WallBoard_01')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/M_WallBoard_01.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FloorStripes_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FloorStripes_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FloorStripes_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FloorStripes_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FloorStripes_D.png'
      * 'AlphaSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FloorStripes_M.png'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FloorStripes_N.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FloorStripes_ORM.png'
      * 'RoughnessMax' [float] = '2.204305'
      * 'RoughnessMin' [float] = '0.044954'

---

### /World/SortingArea/SM_FloorDecal_StripeFull_4m74/SM_FloorDecal_StripeFull_4m74/Looks/M_FloorStripes_01

* **Prim路径 (Prim Path):**/World/SortingArea/SM_FloorDecal_StripeFull_4m74/SM_FloorDecal_StripeFull_4m74/Looks/M_FloorStripes_01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_FloorDecal_StripeFull_4m74/SM_FloorDecal_StripeFull_4m74/Looks/M_FloorStripes_01/M_WallBoard_01'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_FloorDecal_StripeFull_4m74/SM_FloorDecal_StripeFull_4m74/Looks/M_FloorStripes_01/M_WallBoard_01'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/M_WallBoard_01.mdl' (Sub Id: 'M_WallBoard_01')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/M_WallBoard_01.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FloorStripes_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FloorStripes_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FloorStripes_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FloorStripes_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FloorStripes_D.png'
      * 'AlphaSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FloorStripes_M.png'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FloorStripes_N.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FloorStripes_ORM.png'
      * 'RoughnessMax' [float] = '2.204305'
      * 'RoughnessMin' [float] = '0.044954'

---

### /World/SortingArea/SM_FloorDecal_StripeFull_4m75/SM_FloorDecal_StripeFull_4m75/Looks/M_FloorStripes_01

* **Prim路径 (Prim Path):**/World/SortingArea/SM_FloorDecal_StripeFull_4m75/SM_FloorDecal_StripeFull_4m75/Looks/M_FloorStripes_01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_FloorDecal_StripeFull_4m75/SM_FloorDecal_StripeFull_4m75/Looks/M_FloorStripes_01/M_WallBoard_01'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_FloorDecal_StripeFull_4m75/SM_FloorDecal_StripeFull_4m75/Looks/M_FloorStripes_01/M_WallBoard_01'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/M_WallBoard_01.mdl' (Sub Id: 'M_WallBoard_01')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/M_WallBoard_01.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FloorStripes_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FloorStripes_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FloorStripes_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FloorStripes_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FloorStripes_D.png'
      * 'AlphaSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FloorStripes_M.png'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FloorStripes_N.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FloorStripes_ORM.png'
      * 'RoughnessMax' [float] = '2.204305'
      * 'RoughnessMin' [float] = '0.044954'

---

### /World/SortingArea/SM_FloorDecal_StripeFull_4m76/SM_FloorDecal_StripeFull_4m76/Looks/M_FloorStripes_01

* **Prim路径 (Prim Path):**/World/SortingArea/SM_FloorDecal_StripeFull_4m76/SM_FloorDecal_StripeFull_4m76/Looks/M_FloorStripes_01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_FloorDecal_StripeFull_4m76/SM_FloorDecal_StripeFull_4m76/Looks/M_FloorStripes_01/M_WallBoard_01'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_FloorDecal_StripeFull_4m76/SM_FloorDecal_StripeFull_4m76/Looks/M_FloorStripes_01/M_WallBoard_01'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/M_WallBoard_01.mdl' (Sub Id: 'M_WallBoard_01')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/M_WallBoard_01.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FloorStripes_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FloorStripes_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FloorStripes_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FloorStripes_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FloorStripes_D.png'
      * 'AlphaSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FloorStripes_M.png'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FloorStripes_N.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FloorStripes_ORM.png'
      * 'RoughnessMax' [float] = '2.204305'
      * 'RoughnessMin' [float] = '0.044954'

---

### /World/SortingArea/SM_FloorDecal_StripeFull_4m77/SM_FloorDecal_StripeFull_4m77/Looks/M_FloorStripes_01

* **Prim路径 (Prim Path):**/World/SortingArea/SM_FloorDecal_StripeFull_4m77/SM_FloorDecal_StripeFull_4m77/Looks/M_FloorStripes_01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_FloorDecal_StripeFull_4m77/SM_FloorDecal_StripeFull_4m77/Looks/M_FloorStripes_01/M_WallBoard_01'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_FloorDecal_StripeFull_4m77/SM_FloorDecal_StripeFull_4m77/Looks/M_FloorStripes_01/M_WallBoard_01'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/M_WallBoard_01.mdl' (Sub Id: 'M_WallBoard_01')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/M_WallBoard_01.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FloorStripes_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FloorStripes_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FloorStripes_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FloorStripes_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FloorStripes_D.png'
      * 'AlphaSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FloorStripes_M.png'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FloorStripes_N.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FloorStripes_ORM.png'
      * 'RoughnessMax' [float] = '2.204305'
      * 'RoughnessMin' [float] = '0.044954'

---

### /World/SortingArea/SM_FloorDecal_StripeFull_4m78/SM_FloorDecal_StripeFull_4m78/Looks/M_FloorStripes_01

* **Prim路径 (Prim Path):**/World/SortingArea/SM_FloorDecal_StripeFull_4m78/SM_FloorDecal_StripeFull_4m78/Looks/M_FloorStripes_01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_FloorDecal_StripeFull_4m78/SM_FloorDecal_StripeFull_4m78/Looks/M_FloorStripes_01/M_WallBoard_01'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_FloorDecal_StripeFull_4m78/SM_FloorDecal_StripeFull_4m78/Looks/M_FloorStripes_01/M_WallBoard_01'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/M_WallBoard_01.mdl' (Sub Id: 'M_WallBoard_01')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/M_WallBoard_01.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FloorStripes_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FloorStripes_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FloorStripes_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FloorStripes_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FloorStripes_D.png'
      * 'AlphaSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FloorStripes_M.png'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FloorStripes_N.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FloorStripes_ORM.png'
      * 'RoughnessMax' [float] = '2.204305'
      * 'RoughnessMin' [float] = '0.044954'

---

### /World/SortingArea/SM_FloorDecal_StripeFull_4m79/SM_FloorDecal_StripeFull_4m79/Looks/M_FloorStripes_01

* **Prim路径 (Prim Path):**/World/SortingArea/SM_FloorDecal_StripeFull_4m79/SM_FloorDecal_StripeFull_4m79/Looks/M_FloorStripes_01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_FloorDecal_StripeFull_4m79/SM_FloorDecal_StripeFull_4m79/Looks/M_FloorStripes_01/M_WallBoard_01'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_FloorDecal_StripeFull_4m79/SM_FloorDecal_StripeFull_4m79/Looks/M_FloorStripes_01/M_WallBoard_01'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/M_WallBoard_01.mdl' (Sub Id: 'M_WallBoard_01')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/M_WallBoard_01.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FloorStripes_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FloorStripes_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FloorStripes_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FloorStripes_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FloorStripes_D.png'
      * 'AlphaSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FloorStripes_M.png'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FloorStripes_N.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FloorStripes_ORM.png'
      * 'RoughnessMax' [float] = '2.204305'
      * 'RoughnessMin' [float] = '0.044954'

---

### /World/SortingArea/SM_FloorDecal_StripeFull_4m80/SM_FloorDecal_StripeFull_4m80/Looks/M_FloorStripes_01

* **Prim路径 (Prim Path):**/World/SortingArea/SM_FloorDecal_StripeFull_4m80/SM_FloorDecal_StripeFull_4m80/Looks/M_FloorStripes_01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_FloorDecal_StripeFull_4m80/SM_FloorDecal_StripeFull_4m80/Looks/M_FloorStripes_01/M_WallBoard_01'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_FloorDecal_StripeFull_4m80/SM_FloorDecal_StripeFull_4m80/Looks/M_FloorStripes_01/M_WallBoard_01'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/M_WallBoard_01.mdl' (Sub Id: 'M_WallBoard_01')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/M_WallBoard_01.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FloorStripes_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FloorStripes_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FloorStripes_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FloorStripes_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FloorStripes_D.png'
      * 'AlphaSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FloorStripes_M.png'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FloorStripes_N.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FloorStripes_ORM.png'
      * 'RoughnessMax' [float] = '2.204305'
      * 'RoughnessMin' [float] = '0.044954'

---

### /World/SortingArea/SM_FloorDecal_StripeFull_4m81/SM_FloorDecal_StripeFull_4m81/Looks/M_FloorStripes_01

* **Prim路径 (Prim Path):**/World/SortingArea/SM_FloorDecal_StripeFull_4m81/SM_FloorDecal_StripeFull_4m81/Looks/M_FloorStripes_01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_FloorDecal_StripeFull_4m81/SM_FloorDecal_StripeFull_4m81/Looks/M_FloorStripes_01/M_WallBoard_01'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_FloorDecal_StripeFull_4m81/SM_FloorDecal_StripeFull_4m81/Looks/M_FloorStripes_01/M_WallBoard_01'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/M_WallBoard_01.mdl' (Sub Id: 'M_WallBoard_01')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/M_WallBoard_01.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FloorStripes_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FloorStripes_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FloorStripes_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FloorStripes_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FloorStripes_D.png'
      * 'AlphaSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FloorStripes_M.png'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FloorStripes_N.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FloorStripes_ORM.png'
      * 'RoughnessMax' [float] = '2.204305'
      * 'RoughnessMin' [float] = '0.044954'

---

### /World/SortingArea/SM_FuseBox_24/SM_FuseBox_24/Looks/MI_WallDetails_01

* **Prim路径 (Prim Path):**/World/SortingArea/SM_FuseBox_24/SM_FuseBox_24/Looks/MI_WallDetails_01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_FuseBox_24/SM_FuseBox_24/Looks/MI_WallDetails_01/MI_LampCeilingA'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_FuseBox_24/SM_FuseBox_24/Looks/MI_WallDetails_01/MI_LampCeilingA'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_LampCeilingA.mdl' (Sub Id: 'MI_LampCeilingA')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_LampCeilingA.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallDetails_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallDetails_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallDetails_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallDetails_D.png'
      * 'BaseColor_Tint' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'Desaturation' [float] = '0'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallDetails_N.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallDetails_ORM.png'
      * 'RoughnessMax' [float] = '0.56055'
      * 'RoughnessMin' [float] = '0.1'
      * 'U_Tiling' [float] = '1'
      * 'V_Tiling' [float] = '1'

---

### /World/SortingArea/SM_FuseBox_25/SM_FuseBox_25/Looks/MI_WallDetails_01

* **Prim路径 (Prim Path):**/World/SortingArea/SM_FuseBox_25/SM_FuseBox_25/Looks/MI_WallDetails_01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_FuseBox_25/SM_FuseBox_25/Looks/MI_WallDetails_01/MI_LampCeilingA'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_FuseBox_25/SM_FuseBox_25/Looks/MI_WallDetails_01/MI_LampCeilingA'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_LampCeilingA.mdl' (Sub Id: 'MI_LampCeilingA')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_LampCeilingA.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallDetails_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallDetails_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallDetails_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallDetails_D.png'
      * 'BaseColor_Tint' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'Desaturation' [float] = '0'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallDetails_N.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallDetails_ORM.png'
      * 'RoughnessMax' [float] = '0.56055'
      * 'RoughnessMin' [float] = '0.1'
      * 'U_Tiling' [float] = '1'
      * 'V_Tiling' [float] = '1'

---

### /World/SortingArea/SM_LampCeilingA_23/SM_LampCeilingA_23/Looks/MI_LampCeilingA

* **Prim路径 (Prim Path):**/World/SortingArea/SM_LampCeilingA_23/SM_LampCeilingA_23/Looks/MI_LampCeilingA
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_LampCeilingA_23/SM_LampCeilingA_23/Looks/MI_LampCeilingA/MI_LampCeilingA'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_LampCeilingA_23/SM_LampCeilingA_23/Looks/MI_LampCeilingA/MI_LampCeilingA'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_LampCeilingA.mdl' (Sub Id: 'MI_LampCeilingA')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_LampCeilingA.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_LampCeilingA_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_LampCeilingA_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_LampCeilingA_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_LampCeilingA_D.png'
      * 'BaseColor_Tint' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'Desaturation' [float] = '0'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_LampCeilingA_N.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_LampCeilingA_ORM.png'
      * 'RoughnessMax' [float] = '0.9'
      * 'RoughnessMin' [float] = '0.1'
      * 'U_Tiling' [float] = '1'
      * 'V_Tiling' [float] = '1'

---

### /World/SortingArea/SM_LampCeilingA_23/SM_LampCeilingA_23/Looks/M_Glow

* **Prim路径 (Prim Path):**/World/SortingArea/SM_LampCeilingA_23/SM_LampCeilingA_23/Looks/M_Glow
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_LampCeilingA_23/SM_LampCeilingA_23/Looks/M_Glow/M_Glow'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_LampCeilingA_23/SM_LampCeilingA_23/Looks/M_Glow/M_Glow'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/M_Glow.mdl' (Sub Id: 'M_Glow')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/M_Glow.mdl'

---

### /World/SortingArea/SM_LampCeilingA_24/SM_LampCeilingA_24/Looks/MI_LampCeilingA

* **Prim路径 (Prim Path):**/World/SortingArea/SM_LampCeilingA_24/SM_LampCeilingA_24/Looks/MI_LampCeilingA
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_LampCeilingA_24/SM_LampCeilingA_24/Looks/MI_LampCeilingA/MI_LampCeilingA'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_LampCeilingA_24/SM_LampCeilingA_24/Looks/MI_LampCeilingA/MI_LampCeilingA'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_LampCeilingA.mdl' (Sub Id: 'MI_LampCeilingA')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_LampCeilingA.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_LampCeilingA_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_LampCeilingA_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_LampCeilingA_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_LampCeilingA_D.png'
      * 'BaseColor_Tint' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'Desaturation' [float] = '0'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_LampCeilingA_N.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_LampCeilingA_ORM.png'
      * 'RoughnessMax' [float] = '0.9'
      * 'RoughnessMin' [float] = '0.1'
      * 'U_Tiling' [float] = '1'
      * 'V_Tiling' [float] = '1'

---

### /World/SortingArea/SM_LampCeilingA_24/SM_LampCeilingA_24/Looks/M_Glow

* **Prim路径 (Prim Path):**/World/SortingArea/SM_LampCeilingA_24/SM_LampCeilingA_24/Looks/M_Glow
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_LampCeilingA_24/SM_LampCeilingA_24/Looks/M_Glow/M_Glow'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_LampCeilingA_24/SM_LampCeilingA_24/Looks/M_Glow/M_Glow'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/M_Glow.mdl' (Sub Id: 'M_Glow')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/M_Glow.mdl'

---

### /World/SortingArea/SM_LampCeilingA_25/SM_LampCeilingA_25/Looks/MI_LampCeilingA

* **Prim路径 (Prim Path):**/World/SortingArea/SM_LampCeilingA_25/SM_LampCeilingA_25/Looks/MI_LampCeilingA
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_LampCeilingA_25/SM_LampCeilingA_25/Looks/MI_LampCeilingA/MI_LampCeilingA'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_LampCeilingA_25/SM_LampCeilingA_25/Looks/MI_LampCeilingA/MI_LampCeilingA'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_LampCeilingA.mdl' (Sub Id: 'MI_LampCeilingA')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_LampCeilingA.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_LampCeilingA_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_LampCeilingA_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_LampCeilingA_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_LampCeilingA_D.png'
      * 'BaseColor_Tint' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'Desaturation' [float] = '0'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_LampCeilingA_N.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_LampCeilingA_ORM.png'
      * 'RoughnessMax' [float] = '0.9'
      * 'RoughnessMin' [float] = '0.1'
      * 'U_Tiling' [float] = '1'
      * 'V_Tiling' [float] = '1'

---

### /World/SortingArea/SM_LampCeilingA_25/SM_LampCeilingA_25/Looks/M_Glow

* **Prim路径 (Prim Path):**/World/SortingArea/SM_LampCeilingA_25/SM_LampCeilingA_25/Looks/M_Glow
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_LampCeilingA_25/SM_LampCeilingA_25/Looks/M_Glow/M_Glow'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_LampCeilingA_25/SM_LampCeilingA_25/Looks/M_Glow/M_Glow'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/M_Glow.mdl' (Sub Id: 'M_Glow')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/M_Glow.mdl'

---

### /World/SortingArea/SM_LampCeilingA_33/SM_LampCeilingA_33/Looks/MI_LampCeilingA

* **Prim路径 (Prim Path):**/World/SortingArea/SM_LampCeilingA_33/SM_LampCeilingA_33/Looks/MI_LampCeilingA
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_LampCeilingA_33/SM_LampCeilingA_33/Looks/MI_LampCeilingA/MI_LampCeilingA'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_LampCeilingA_33/SM_LampCeilingA_33/Looks/MI_LampCeilingA/MI_LampCeilingA'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_LampCeilingA.mdl' (Sub Id: 'MI_LampCeilingA')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_LampCeilingA.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_LampCeilingA_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_LampCeilingA_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_LampCeilingA_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_LampCeilingA_D.png'
      * 'BaseColor_Tint' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'Desaturation' [float] = '0'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_LampCeilingA_N.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_LampCeilingA_ORM.png'
      * 'RoughnessMax' [float] = '0.9'
      * 'RoughnessMin' [float] = '0.1'
      * 'U_Tiling' [float] = '1'
      * 'V_Tiling' [float] = '1'

---

### /World/SortingArea/SM_LampCeilingA_33/SM_LampCeilingA_33/Looks/M_Glow

* **Prim路径 (Prim Path):**/World/SortingArea/SM_LampCeilingA_33/SM_LampCeilingA_33/Looks/M_Glow
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_LampCeilingA_33/SM_LampCeilingA_33/Looks/M_Glow/M_Glow'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_LampCeilingA_33/SM_LampCeilingA_33/Looks/M_Glow/M_Glow'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/M_Glow.mdl' (Sub Id: 'M_Glow')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/M_Glow.mdl'

---

### /World/SortingArea/SM_LampCeilingA_35/SM_LampCeilingA_35/Looks/MI_LampCeilingA

* **Prim路径 (Prim Path):**/World/SortingArea/SM_LampCeilingA_35/SM_LampCeilingA_35/Looks/MI_LampCeilingA
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_LampCeilingA_35/SM_LampCeilingA_35/Looks/MI_LampCeilingA/MI_LampCeilingA'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_LampCeilingA_35/SM_LampCeilingA_35/Looks/MI_LampCeilingA/MI_LampCeilingA'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_LampCeilingA.mdl' (Sub Id: 'MI_LampCeilingA')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_LampCeilingA.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_LampCeilingA_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_LampCeilingA_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_LampCeilingA_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_LampCeilingA_D.png'
      * 'BaseColor_Tint' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'Desaturation' [float] = '0'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_LampCeilingA_N.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_LampCeilingA_ORM.png'
      * 'RoughnessMax' [float] = '0.9'
      * 'RoughnessMin' [float] = '0.1'
      * 'U_Tiling' [float] = '1'
      * 'V_Tiling' [float] = '1'

---

### /World/SortingArea/SM_LampCeilingA_35/SM_LampCeilingA_35/Looks/M_Glow

* **Prim路径 (Prim Path):**/World/SortingArea/SM_LampCeilingA_35/SM_LampCeilingA_35/Looks/M_Glow
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_LampCeilingA_35/SM_LampCeilingA_35/Looks/M_Glow/M_Glow'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_LampCeilingA_35/SM_LampCeilingA_35/Looks/M_Glow/M_Glow'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/M_Glow.mdl' (Sub Id: 'M_Glow')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/M_Glow.mdl'

---

### /World/SortingArea/SM_LampCeilingA_36/SM_LampCeilingA_36/Looks/MI_LampCeilingA

* **Prim路径 (Prim Path):**/World/SortingArea/SM_LampCeilingA_36/SM_LampCeilingA_36/Looks/MI_LampCeilingA
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_LampCeilingA_36/SM_LampCeilingA_36/Looks/MI_LampCeilingA/MI_LampCeilingA'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_LampCeilingA_36/SM_LampCeilingA_36/Looks/MI_LampCeilingA/MI_LampCeilingA'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_LampCeilingA.mdl' (Sub Id: 'MI_LampCeilingA')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_LampCeilingA.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_LampCeilingA_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_LampCeilingA_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_LampCeilingA_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_LampCeilingA_D.png'
      * 'BaseColor_Tint' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'Desaturation' [float] = '0'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_LampCeilingA_N.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_LampCeilingA_ORM.png'
      * 'RoughnessMax' [float] = '0.9'
      * 'RoughnessMin' [float] = '0.1'
      * 'U_Tiling' [float] = '1'
      * 'V_Tiling' [float] = '1'

---

### /World/SortingArea/SM_LampCeilingA_36/SM_LampCeilingA_36/Looks/M_Glow

* **Prim路径 (Prim Path):**/World/SortingArea/SM_LampCeilingA_36/SM_LampCeilingA_36/Looks/M_Glow
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_LampCeilingA_36/SM_LampCeilingA_36/Looks/M_Glow/M_Glow'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_LampCeilingA_36/SM_LampCeilingA_36/Looks/M_Glow/M_Glow'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/M_Glow.mdl' (Sub Id: 'M_Glow')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/M_Glow.mdl'

---

### /World/SortingArea/SM_LampCeilingA_37/SM_LampCeilingA_37/Looks/MI_LampCeilingA

* **Prim路径 (Prim Path):**/World/SortingArea/SM_LampCeilingA_37/SM_LampCeilingA_37/Looks/MI_LampCeilingA
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_LampCeilingA_37/SM_LampCeilingA_37/Looks/MI_LampCeilingA/MI_LampCeilingA'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_LampCeilingA_37/SM_LampCeilingA_37/Looks/MI_LampCeilingA/MI_LampCeilingA'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_LampCeilingA.mdl' (Sub Id: 'MI_LampCeilingA')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_LampCeilingA.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_LampCeilingA_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_LampCeilingA_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_LampCeilingA_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_LampCeilingA_D.png'
      * 'BaseColor_Tint' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'Desaturation' [float] = '0'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_LampCeilingA_N.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_LampCeilingA_ORM.png'
      * 'RoughnessMax' [float] = '0.9'
      * 'RoughnessMin' [float] = '0.1'
      * 'U_Tiling' [float] = '1'
      * 'V_Tiling' [float] = '1'

---

### /World/SortingArea/SM_LampCeilingA_37/SM_LampCeilingA_37/Looks/M_Glow

* **Prim路径 (Prim Path):**/World/SortingArea/SM_LampCeilingA_37/SM_LampCeilingA_37/Looks/M_Glow
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_LampCeilingA_37/SM_LampCeilingA_37/Looks/M_Glow/M_Glow'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_LampCeilingA_37/SM_LampCeilingA_37/Looks/M_Glow/M_Glow'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/M_Glow.mdl' (Sub Id: 'M_Glow')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/M_Glow.mdl'

---

### /World/SortingArea/SM_LampCeilingA_38/SM_LampCeilingA_38/Looks/MI_LampCeilingA

* **Prim路径 (Prim Path):**/World/SortingArea/SM_LampCeilingA_38/SM_LampCeilingA_38/Looks/MI_LampCeilingA
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_LampCeilingA_38/SM_LampCeilingA_38/Looks/MI_LampCeilingA/MI_LampCeilingA'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_LampCeilingA_38/SM_LampCeilingA_38/Looks/MI_LampCeilingA/MI_LampCeilingA'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_LampCeilingA.mdl' (Sub Id: 'MI_LampCeilingA')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_LampCeilingA.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_LampCeilingA_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_LampCeilingA_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_LampCeilingA_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_LampCeilingA_D.png'
      * 'BaseColor_Tint' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'Desaturation' [float] = '0'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_LampCeilingA_N.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_LampCeilingA_ORM.png'
      * 'RoughnessMax' [float] = '0.9'
      * 'RoughnessMin' [float] = '0.1'
      * 'U_Tiling' [float] = '1'
      * 'V_Tiling' [float] = '1'

---

### /World/SortingArea/SM_LampCeilingA_38/SM_LampCeilingA_38/Looks/M_Glow

* **Prim路径 (Prim Path):**/World/SortingArea/SM_LampCeilingA_38/SM_LampCeilingA_38/Looks/M_Glow
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_LampCeilingA_38/SM_LampCeilingA_38/Looks/M_Glow/M_Glow'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_LampCeilingA_38/SM_LampCeilingA_38/Looks/M_Glow/M_Glow'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/M_Glow.mdl' (Sub Id: 'M_Glow')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/M_Glow.mdl'

---

### /World/SortingArea/SM_LampCeilingA_39/SM_LampCeilingA_39/Looks/MI_LampCeilingA

* **Prim路径 (Prim Path):**/World/SortingArea/SM_LampCeilingA_39/SM_LampCeilingA_39/Looks/MI_LampCeilingA
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_LampCeilingA_39/SM_LampCeilingA_39/Looks/MI_LampCeilingA/MI_LampCeilingA'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_LampCeilingA_39/SM_LampCeilingA_39/Looks/MI_LampCeilingA/MI_LampCeilingA'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_LampCeilingA.mdl' (Sub Id: 'MI_LampCeilingA')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_LampCeilingA.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_LampCeilingA_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_LampCeilingA_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_LampCeilingA_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_LampCeilingA_D.png'
      * 'BaseColor_Tint' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'Desaturation' [float] = '0'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_LampCeilingA_N.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_LampCeilingA_ORM.png'
      * 'RoughnessMax' [float] = '0.9'
      * 'RoughnessMin' [float] = '0.1'
      * 'U_Tiling' [float] = '1'
      * 'V_Tiling' [float] = '1'

---

### /World/SortingArea/SM_LampCeilingA_39/SM_LampCeilingA_39/Looks/M_Glow

* **Prim路径 (Prim Path):**/World/SortingArea/SM_LampCeilingA_39/SM_LampCeilingA_39/Looks/M_Glow
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_LampCeilingA_39/SM_LampCeilingA_39/Looks/M_Glow/M_Glow'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_LampCeilingA_39/SM_LampCeilingA_39/Looks/M_Glow/M_Glow'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/M_Glow.mdl' (Sub Id: 'M_Glow')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/M_Glow.mdl'

---

### /World/SortingArea/SM_LampCeilingA_40/SM_LampCeilingA_40/Looks/MI_LampCeilingA

* **Prim路径 (Prim Path):**/World/SortingArea/SM_LampCeilingA_40/SM_LampCeilingA_40/Looks/MI_LampCeilingA
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_LampCeilingA_40/SM_LampCeilingA_40/Looks/MI_LampCeilingA/MI_LampCeilingA'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_LampCeilingA_40/SM_LampCeilingA_40/Looks/MI_LampCeilingA/MI_LampCeilingA'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_LampCeilingA.mdl' (Sub Id: 'MI_LampCeilingA')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_LampCeilingA.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_LampCeilingA_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_LampCeilingA_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_LampCeilingA_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_LampCeilingA_D.png'
      * 'BaseColor_Tint' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'Desaturation' [float] = '0'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_LampCeilingA_N.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_LampCeilingA_ORM.png'
      * 'RoughnessMax' [float] = '0.9'
      * 'RoughnessMin' [float] = '0.1'
      * 'U_Tiling' [float] = '1'
      * 'V_Tiling' [float] = '1'

---

### /World/SortingArea/SM_LampCeilingA_40/SM_LampCeilingA_40/Looks/M_Glow

* **Prim路径 (Prim Path):**/World/SortingArea/SM_LampCeilingA_40/SM_LampCeilingA_40/Looks/M_Glow
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_LampCeilingA_40/SM_LampCeilingA_40/Looks/M_Glow/M_Glow'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_LampCeilingA_40/SM_LampCeilingA_40/Looks/M_Glow/M_Glow'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/M_Glow.mdl' (Sub Id: 'M_Glow')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/M_Glow.mdl'

---

### /World/SortingArea/SM_LampCeilingA_41/SM_LampCeilingA_41/Looks/MI_LampCeilingA

* **Prim路径 (Prim Path):**/World/SortingArea/SM_LampCeilingA_41/SM_LampCeilingA_41/Looks/MI_LampCeilingA
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_LampCeilingA_41/SM_LampCeilingA_41/Looks/MI_LampCeilingA/MI_LampCeilingA'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_LampCeilingA_41/SM_LampCeilingA_41/Looks/MI_LampCeilingA/MI_LampCeilingA'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_LampCeilingA.mdl' (Sub Id: 'MI_LampCeilingA')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_LampCeilingA.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_LampCeilingA_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_LampCeilingA_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_LampCeilingA_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_LampCeilingA_D.png'
      * 'BaseColor_Tint' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'Desaturation' [float] = '0'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_LampCeilingA_N.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_LampCeilingA_ORM.png'
      * 'RoughnessMax' [float] = '0.9'
      * 'RoughnessMin' [float] = '0.1'
      * 'U_Tiling' [float] = '1'
      * 'V_Tiling' [float] = '1'

---

### /World/SortingArea/SM_LampCeilingA_41/SM_LampCeilingA_41/Looks/M_Glow

* **Prim路径 (Prim Path):**/World/SortingArea/SM_LampCeilingA_41/SM_LampCeilingA_41/Looks/M_Glow
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_LampCeilingA_41/SM_LampCeilingA_41/Looks/M_Glow/M_Glow'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_LampCeilingA_41/SM_LampCeilingA_41/Looks/M_Glow/M_Glow'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/M_Glow.mdl' (Sub Id: 'M_Glow')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/M_Glow.mdl'

---

### /World/SortingArea/SM_LampCeilingA_42/SM_LampCeilingA_42/Looks/MI_LampCeilingA

* **Prim路径 (Prim Path):**/World/SortingArea/SM_LampCeilingA_42/SM_LampCeilingA_42/Looks/MI_LampCeilingA
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_LampCeilingA_42/SM_LampCeilingA_42/Looks/MI_LampCeilingA/MI_LampCeilingA'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_LampCeilingA_42/SM_LampCeilingA_42/Looks/MI_LampCeilingA/MI_LampCeilingA'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_LampCeilingA.mdl' (Sub Id: 'MI_LampCeilingA')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_LampCeilingA.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_LampCeilingA_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_LampCeilingA_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_LampCeilingA_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_LampCeilingA_D.png'
      * 'BaseColor_Tint' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'Desaturation' [float] = '0'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_LampCeilingA_N.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_LampCeilingA_ORM.png'
      * 'RoughnessMax' [float] = '0.9'
      * 'RoughnessMin' [float] = '0.1'
      * 'U_Tiling' [float] = '1'
      * 'V_Tiling' [float] = '1'

---

### /World/SortingArea/SM_LampCeilingA_42/SM_LampCeilingA_42/Looks/M_Glow

* **Prim路径 (Prim Path):**/World/SortingArea/SM_LampCeilingA_42/SM_LampCeilingA_42/Looks/M_Glow
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_LampCeilingA_42/SM_LampCeilingA_42/Looks/M_Glow/M_Glow'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_LampCeilingA_42/SM_LampCeilingA_42/Looks/M_Glow/M_Glow'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/M_Glow.mdl' (Sub Id: 'M_Glow')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/M_Glow.mdl'

---

### /World/SortingArea/SM_LampCeilingA_43/SM_LampCeilingA_43/Looks/MI_LampCeilingA

* **Prim路径 (Prim Path):**/World/SortingArea/SM_LampCeilingA_43/SM_LampCeilingA_43/Looks/MI_LampCeilingA
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_LampCeilingA_43/SM_LampCeilingA_43/Looks/MI_LampCeilingA/MI_LampCeilingA'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_LampCeilingA_43/SM_LampCeilingA_43/Looks/MI_LampCeilingA/MI_LampCeilingA'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_LampCeilingA.mdl' (Sub Id: 'MI_LampCeilingA')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_LampCeilingA.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_LampCeilingA_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_LampCeilingA_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_LampCeilingA_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_LampCeilingA_D.png'
      * 'BaseColor_Tint' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'Desaturation' [float] = '0'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_LampCeilingA_N.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_LampCeilingA_ORM.png'
      * 'RoughnessMax' [float] = '0.9'
      * 'RoughnessMin' [float] = '0.1'
      * 'U_Tiling' [float] = '1'
      * 'V_Tiling' [float] = '1'

---

### /World/SortingArea/SM_LampCeilingA_43/SM_LampCeilingA_43/Looks/M_Glow

* **Prim路径 (Prim Path):**/World/SortingArea/SM_LampCeilingA_43/SM_LampCeilingA_43/Looks/M_Glow
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_LampCeilingA_43/SM_LampCeilingA_43/Looks/M_Glow/M_Glow'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_LampCeilingA_43/SM_LampCeilingA_43/Looks/M_Glow/M_Glow'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/M_Glow.mdl' (Sub Id: 'M_Glow')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/M_Glow.mdl'

---

### /World/SortingArea/SM_LampCeilingA_44/SM_LampCeilingA_44/Looks/MI_LampCeilingA

* **Prim路径 (Prim Path):**/World/SortingArea/SM_LampCeilingA_44/SM_LampCeilingA_44/Looks/MI_LampCeilingA
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_LampCeilingA_44/SM_LampCeilingA_44/Looks/MI_LampCeilingA/MI_LampCeilingA'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_LampCeilingA_44/SM_LampCeilingA_44/Looks/MI_LampCeilingA/MI_LampCeilingA'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_LampCeilingA.mdl' (Sub Id: 'MI_LampCeilingA')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_LampCeilingA.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_LampCeilingA_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_LampCeilingA_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_LampCeilingA_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_LampCeilingA_D.png'
      * 'BaseColor_Tint' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'Desaturation' [float] = '0'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_LampCeilingA_N.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_LampCeilingA_ORM.png'
      * 'RoughnessMax' [float] = '0.9'
      * 'RoughnessMin' [float] = '0.1'
      * 'U_Tiling' [float] = '1'
      * 'V_Tiling' [float] = '1'

---

### /World/SortingArea/SM_LampCeilingA_44/SM_LampCeilingA_44/Looks/M_Glow

* **Prim路径 (Prim Path):**/World/SortingArea/SM_LampCeilingA_44/SM_LampCeilingA_44/Looks/M_Glow
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_LampCeilingA_44/SM_LampCeilingA_44/Looks/M_Glow/M_Glow'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_LampCeilingA_44/SM_LampCeilingA_44/Looks/M_Glow/M_Glow'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/M_Glow.mdl' (Sub Id: 'M_Glow')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/M_Glow.mdl'

---

### /World/SortingArea/SM_LampCeilingA_45/SM_LampCeilingA_45/Looks/MI_LampCeilingA

* **Prim路径 (Prim Path):**/World/SortingArea/SM_LampCeilingA_45/SM_LampCeilingA_45/Looks/MI_LampCeilingA
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_LampCeilingA_45/SM_LampCeilingA_45/Looks/MI_LampCeilingA/MI_LampCeilingA'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_LampCeilingA_45/SM_LampCeilingA_45/Looks/MI_LampCeilingA/MI_LampCeilingA'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_LampCeilingA.mdl' (Sub Id: 'MI_LampCeilingA')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_LampCeilingA.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_LampCeilingA_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_LampCeilingA_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_LampCeilingA_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_LampCeilingA_D.png'
      * 'BaseColor_Tint' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'Desaturation' [float] = '0'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_LampCeilingA_N.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_LampCeilingA_ORM.png'
      * 'RoughnessMax' [float] = '0.9'
      * 'RoughnessMin' [float] = '0.1'
      * 'U_Tiling' [float] = '1'
      * 'V_Tiling' [float] = '1'

---

### /World/SortingArea/SM_LampCeilingA_45/SM_LampCeilingA_45/Looks/M_Glow

* **Prim路径 (Prim Path):**/World/SortingArea/SM_LampCeilingA_45/SM_LampCeilingA_45/Looks/M_Glow
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_LampCeilingA_45/SM_LampCeilingA_45/Looks/M_Glow/M_Glow'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_LampCeilingA_45/SM_LampCeilingA_45/Looks/M_Glow/M_Glow'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/M_Glow.mdl' (Sub Id: 'M_Glow')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/M_Glow.mdl'

---

### /World/SortingArea/SM_LampCeilingA_46/SM_LampCeilingA_46/Looks/MI_LampCeilingA

* **Prim路径 (Prim Path):**/World/SortingArea/SM_LampCeilingA_46/SM_LampCeilingA_46/Looks/MI_LampCeilingA
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_LampCeilingA_46/SM_LampCeilingA_46/Looks/MI_LampCeilingA/MI_LampCeilingA'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_LampCeilingA_46/SM_LampCeilingA_46/Looks/MI_LampCeilingA/MI_LampCeilingA'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_LampCeilingA.mdl' (Sub Id: 'MI_LampCeilingA')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_LampCeilingA.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_LampCeilingA_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_LampCeilingA_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_LampCeilingA_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_LampCeilingA_D.png'
      * 'BaseColor_Tint' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'Desaturation' [float] = '0'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_LampCeilingA_N.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_LampCeilingA_ORM.png'
      * 'RoughnessMax' [float] = '0.9'
      * 'RoughnessMin' [float] = '0.1'
      * 'U_Tiling' [float] = '1'
      * 'V_Tiling' [float] = '1'

---

### /World/SortingArea/SM_LampCeilingA_46/SM_LampCeilingA_46/Looks/M_Glow

* **Prim路径 (Prim Path):**/World/SortingArea/SM_LampCeilingA_46/SM_LampCeilingA_46/Looks/M_Glow
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_LampCeilingA_46/SM_LampCeilingA_46/Looks/M_Glow/M_Glow'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_LampCeilingA_46/SM_LampCeilingA_46/Looks/M_Glow/M_Glow'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/M_Glow.mdl' (Sub Id: 'M_Glow')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/M_Glow.mdl'

---

### /World/SortingArea/SM_PaletteA_360/SM_PaletteA_360/Looks/MI_PaletteSmallA_01

* **Prim路径 (Prim Path):**/World/SortingArea/SM_PaletteA_360/SM_PaletteA_360/Looks/MI_PaletteSmallA_01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_PaletteA_360/SM_PaletteA_360/Looks/MI_PaletteSmallA_01/MI_CeilingA_06b'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_PaletteA_360/SM_PaletteA_360/Looks/MI_PaletteSmallA_01/MI_CeilingA_06b'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_CeilingA_06b.mdl' (Sub Id: 'MI_CeilingA_06b')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_CeilingA_06b.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_PaletteA_01_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_PaletteA_01_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_PaletteA_01_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_PaletteA_01_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_PaletteA_01_D.png'
      * 'ColorAlbedo' [float4] = '(0.073, 0.093, 0.120, 0.000)'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_PaletteA_01_N.png'
      * 'MainTiling' [float4] = '(1.000, 1.000, 0.000, 1.000)'
      * 'MaskSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_PaletteA_01_M.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_PaletteA_01_ORM.png'
      * 'RoughnessMax' [float] = '0.9'
      * 'RoughnessMin' [float] = '0.1'

---

### /World/SortingArea/SM_PillarA_9M4/SM_PillarA_9M4/Looks/MI_BeamsA_01

* **Prim路径 (Prim Path):**/World/SortingArea/SM_PillarA_9M4/SM_PillarA_9M4/Looks/MI_BeamsA_01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_PillarA_9M4/SM_PillarA_9M4/Looks/MI_BeamsA_01/MI_CeilingA_06b'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_PillarA_9M4/SM_PillarA_9M4/Looks/MI_BeamsA_01/MI_CeilingA_06b'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_CeilingA_06b.mdl' (Sub Id: 'MI_CeilingA_06b')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_CeilingA_06b.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_D.png'
      * 'ColorAlbedo' [float4] = '(0.145, 0.145, 0.145, 0.000)'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_N.png'
      * 'MainTiling' [float4] = '(1.000, 1.000, 0.000, 1.000)'
      * 'MaskSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_M.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_ORM.png'
      * 'RoughnessMax' [float] = '0.9'
      * 'RoughnessMin' [float] = '0.1'

---

### /World/SortingArea/SM_PillarA_9M4_01/SM_PillarA_9M4_01/Looks/MI_BeamsA_01

* **Prim路径 (Prim Path):**/World/SortingArea/SM_PillarA_9M4_01/SM_PillarA_9M4_01/Looks/MI_BeamsA_01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_PillarA_9M4_01/SM_PillarA_9M4_01/Looks/MI_BeamsA_01/MI_CeilingA_06b'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_PillarA_9M4_01/SM_PillarA_9M4_01/Looks/MI_BeamsA_01/MI_CeilingA_06b'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_CeilingA_06b.mdl' (Sub Id: 'MI_CeilingA_06b')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_CeilingA_06b.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_D.png'
      * 'ColorAlbedo' [float4] = '(0.145, 0.145, 0.145, 0.000)'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_N.png'
      * 'MainTiling' [float4] = '(1.000, 1.000, 0.000, 1.000)'
      * 'MaskSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_M.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_ORM.png'
      * 'RoughnessMax' [float] = '0.9'
      * 'RoughnessMin' [float] = '0.1'

---

### /World/SortingArea/SM_PillarA_9M4_02/SM_PillarA_9M4_02/Looks/MI_BeamsA_01

* **Prim路径 (Prim Path):**/World/SortingArea/SM_PillarA_9M4_02/SM_PillarA_9M4_02/Looks/MI_BeamsA_01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_PillarA_9M4_02/SM_PillarA_9M4_02/Looks/MI_BeamsA_01/MI_CeilingA_06b'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_PillarA_9M4_02/SM_PillarA_9M4_02/Looks/MI_BeamsA_01/MI_CeilingA_06b'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_CeilingA_06b.mdl' (Sub Id: 'MI_CeilingA_06b')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_CeilingA_06b.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_D.png'
      * 'ColorAlbedo' [float4] = '(0.145, 0.145, 0.145, 0.000)'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_N.png'
      * 'MainTiling' [float4] = '(1.000, 1.000, 0.000, 1.000)'
      * 'MaskSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_M.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_ORM.png'
      * 'RoughnessMax' [float] = '0.9'
      * 'RoughnessMin' [float] = '0.1'

---

### /World/SortingArea/SM_PillarA_9M4_03/SM_PillarA_9M4_03/Looks/MI_BeamsA_01

* **Prim路径 (Prim Path):**/World/SortingArea/SM_PillarA_9M4_03/SM_PillarA_9M4_03/Looks/MI_BeamsA_01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_PillarA_9M4_03/SM_PillarA_9M4_03/Looks/MI_BeamsA_01/MI_CeilingA_06b'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_PillarA_9M4_03/SM_PillarA_9M4_03/Looks/MI_BeamsA_01/MI_CeilingA_06b'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_CeilingA_06b.mdl' (Sub Id: 'MI_CeilingA_06b')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_CeilingA_06b.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_D.png'
      * 'ColorAlbedo' [float4] = '(0.145, 0.145, 0.145, 0.000)'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_N.png'
      * 'MainTiling' [float4] = '(1.000, 1.000, 0.000, 1.000)'
      * 'MaskSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_M.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_ORM.png'
      * 'RoughnessMax' [float] = '0.9'
      * 'RoughnessMin' [float] = '0.1'

---

### /World/SortingArea/SM_PillarA_9M4_04/SM_PillarA_9M4_04/Looks/MI_BeamsA_01

* **Prim路径 (Prim Path):**/World/SortingArea/SM_PillarA_9M4_04/SM_PillarA_9M4_04/Looks/MI_BeamsA_01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_PillarA_9M4_04/SM_PillarA_9M4_04/Looks/MI_BeamsA_01/MI_CeilingA_06b'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_PillarA_9M4_04/SM_PillarA_9M4_04/Looks/MI_BeamsA_01/MI_CeilingA_06b'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_CeilingA_06b.mdl' (Sub Id: 'MI_CeilingA_06b')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_CeilingA_06b.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_D.png'
      * 'ColorAlbedo' [float4] = '(0.145, 0.145, 0.145, 0.000)'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_N.png'
      * 'MainTiling' [float4] = '(1.000, 1.000, 0.000, 1.000)'
      * 'MaskSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_M.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_ORM.png'
      * 'RoughnessMax' [float] = '0.9'
      * 'RoughnessMin' [float] = '0.1'

---

### /World/SortingArea/SM_PillarPartA_9M10_1473/SM_PillarPartA_9M10_1473/Looks/MI_BeamsA_01

* **Prim路径 (Prim Path):**/World/SortingArea/SM_PillarPartA_9M10_1473/SM_PillarPartA_9M10_1473/Looks/MI_BeamsA_01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_PillarPartA_9M10_1473/SM_PillarPartA_9M10_1473/Looks/MI_BeamsA_01/MI_CeilingA_06b'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_PillarPartA_9M10_1473/SM_PillarPartA_9M10_1473/Looks/MI_BeamsA_01/MI_CeilingA_06b'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_CeilingA_06b.mdl' (Sub Id: 'MI_CeilingA_06b')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_CeilingA_06b.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_D.png'
      * 'ColorAlbedo' [float4] = '(0.145, 0.145, 0.145, 0.000)'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_N.png'
      * 'MainTiling' [float4] = '(1.000, 1.000, 0.000, 1.000)'
      * 'MaskSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_M.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_ORM.png'
      * 'RoughnessMax' [float] = '0.9'
      * 'RoughnessMin' [float] = '0.1'

---

### /World/SortingArea/SM_PillarPartA_9M10_1473/SM_PillarPartA_9M10_1473/Looks/MI_FrameA_01

* **Prim路径 (Prim Path):**/World/SortingArea/SM_PillarPartA_9M10_1473/SM_PillarPartA_9M10_1473/Looks/MI_FrameA_01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_PillarPartA_9M10_1473/SM_PillarPartA_9M10_1473/Looks/MI_FrameA_01/MI_FrameA_01'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_PillarPartA_9M10_1473/SM_PillarPartA_9M10_1473/Looks/MI_FrameA_01/MI_FrameA_01'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_FrameA_01.mdl' (Sub Id: 'MI_FrameA_01')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_FrameA_01.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_D.png'
      * 'ColorAlbedo' [float4] = '(0.145, 0.145, 0.145, 0.000)'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_N.png'
      * 'MainTiling' [float4] = '(1.000, 1.000, 0.000, 1.000)'
      * 'MaskSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_M.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_ORM.png'
      * 'RoughnessMax' [float] = '0.9'
      * 'RoughnessMin' [float] = '0.1'

---

### /World/SortingArea/SM_PillarPartA_9M11_1481/SM_PillarPartA_9M11_1481/Looks/MI_BeamsA_01

* **Prim路径 (Prim Path):**/World/SortingArea/SM_PillarPartA_9M11_1481/SM_PillarPartA_9M11_1481/Looks/MI_BeamsA_01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_PillarPartA_9M11_1481/SM_PillarPartA_9M11_1481/Looks/MI_BeamsA_01/MI_CeilingA_06b'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_PillarPartA_9M11_1481/SM_PillarPartA_9M11_1481/Looks/MI_BeamsA_01/MI_CeilingA_06b'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_CeilingA_06b.mdl' (Sub Id: 'MI_CeilingA_06b')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_CeilingA_06b.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_D.png'
      * 'ColorAlbedo' [float4] = '(0.145, 0.145, 0.145, 0.000)'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_N.png'
      * 'MainTiling' [float4] = '(1.000, 1.000, 0.000, 1.000)'
      * 'MaskSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_M.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_ORM.png'
      * 'RoughnessMax' [float] = '0.9'
      * 'RoughnessMin' [float] = '0.1'

---

### /World/SortingArea/SM_PillarPartA_9M11_1481/SM_PillarPartA_9M11_1481/Looks/MI_FrameA_01

* **Prim路径 (Prim Path):**/World/SortingArea/SM_PillarPartA_9M11_1481/SM_PillarPartA_9M11_1481/Looks/MI_FrameA_01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_PillarPartA_9M11_1481/SM_PillarPartA_9M11_1481/Looks/MI_FrameA_01/MI_FrameA_01'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_PillarPartA_9M11_1481/SM_PillarPartA_9M11_1481/Looks/MI_FrameA_01/MI_FrameA_01'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_FrameA_01.mdl' (Sub Id: 'MI_FrameA_01')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_FrameA_01.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_D.png'
      * 'ColorAlbedo' [float4] = '(0.145, 0.145, 0.145, 0.000)'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_N.png'
      * 'MainTiling' [float4] = '(1.000, 1.000, 0.000, 1.000)'
      * 'MaskSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_M.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_ORM.png'
      * 'RoughnessMax' [float] = '0.9'
      * 'RoughnessMin' [float] = '0.1'

---

### /World/SortingArea/SM_PillarPartA_9M12_1482/SM_PillarPartA_9M12_1482/Looks/MI_BeamsA_01

* **Prim路径 (Prim Path):**/World/SortingArea/SM_PillarPartA_9M12_1482/SM_PillarPartA_9M12_1482/Looks/MI_BeamsA_01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_PillarPartA_9M12_1482/SM_PillarPartA_9M12_1482/Looks/MI_BeamsA_01/MI_CeilingA_06b'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_PillarPartA_9M12_1482/SM_PillarPartA_9M12_1482/Looks/MI_BeamsA_01/MI_CeilingA_06b'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_CeilingA_06b.mdl' (Sub Id: 'MI_CeilingA_06b')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_CeilingA_06b.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_D.png'
      * 'ColorAlbedo' [float4] = '(0.145, 0.145, 0.145, 0.000)'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_N.png'
      * 'MainTiling' [float4] = '(1.000, 1.000, 0.000, 1.000)'
      * 'MaskSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_M.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_ORM.png'
      * 'RoughnessMax' [float] = '0.9'
      * 'RoughnessMin' [float] = '0.1'

---

### /World/SortingArea/SM_PillarPartA_9M12_1482/SM_PillarPartA_9M12_1482/Looks/MI_FrameA_01

* **Prim路径 (Prim Path):**/World/SortingArea/SM_PillarPartA_9M12_1482/SM_PillarPartA_9M12_1482/Looks/MI_FrameA_01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_PillarPartA_9M12_1482/SM_PillarPartA_9M12_1482/Looks/MI_FrameA_01/MI_FrameA_01'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_PillarPartA_9M12_1482/SM_PillarPartA_9M12_1482/Looks/MI_FrameA_01/MI_FrameA_01'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_FrameA_01.mdl' (Sub Id: 'MI_FrameA_01')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_FrameA_01.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_D.png'
      * 'ColorAlbedo' [float4] = '(0.145, 0.145, 0.145, 0.000)'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_N.png'
      * 'MainTiling' [float4] = '(1.000, 1.000, 0.000, 1.000)'
      * 'MaskSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_M.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_ORM.png'
      * 'RoughnessMax' [float] = '0.9'
      * 'RoughnessMin' [float] = '0.1'

---

### /World/SortingArea/SM_PillarPartA_9M3_1445/SM_PillarPartA_9M3_1445/Looks/MI_BeamsA_01

* **Prim路径 (Prim Path):**/World/SortingArea/SM_PillarPartA_9M3_1445/SM_PillarPartA_9M3_1445/Looks/MI_BeamsA_01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_PillarPartA_9M3_1445/SM_PillarPartA_9M3_1445/Looks/MI_BeamsA_01/MI_CeilingA_06b'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_PillarPartA_9M3_1445/SM_PillarPartA_9M3_1445/Looks/MI_BeamsA_01/MI_CeilingA_06b'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_CeilingA_06b.mdl' (Sub Id: 'MI_CeilingA_06b')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_CeilingA_06b.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_D.png'
      * 'ColorAlbedo' [float4] = '(0.145, 0.145, 0.145, 0.000)'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_N.png'
      * 'MainTiling' [float4] = '(1.000, 1.000, 0.000, 1.000)'
      * 'MaskSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_M.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_ORM.png'
      * 'RoughnessMax' [float] = '0.9'
      * 'RoughnessMin' [float] = '0.1'

---

### /World/SortingArea/SM_PillarPartA_9M3_1445/SM_PillarPartA_9M3_1445/Looks/MI_FrameA_01

* **Prim路径 (Prim Path):**/World/SortingArea/SM_PillarPartA_9M3_1445/SM_PillarPartA_9M3_1445/Looks/MI_FrameA_01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_PillarPartA_9M3_1445/SM_PillarPartA_9M3_1445/Looks/MI_FrameA_01/MI_FrameA_01'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_PillarPartA_9M3_1445/SM_PillarPartA_9M3_1445/Looks/MI_FrameA_01/MI_FrameA_01'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_FrameA_01.mdl' (Sub Id: 'MI_FrameA_01')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_FrameA_01.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_D.png'
      * 'ColorAlbedo' [float4] = '(0.145, 0.145, 0.145, 0.000)'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_N.png'
      * 'MainTiling' [float4] = '(1.000, 1.000, 0.000, 1.000)'
      * 'MaskSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_M.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_ORM.png'
      * 'RoughnessMax' [float] = '0.9'
      * 'RoughnessMin' [float] = '0.1'

---

### /World/SortingArea/SM_PillarPartA_9M4_1446/SM_PillarPartA_9M4_1446/Looks/MI_BeamsA_01

* **Prim路径 (Prim Path):**/World/SortingArea/SM_PillarPartA_9M4_1446/SM_PillarPartA_9M4_1446/Looks/MI_BeamsA_01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_PillarPartA_9M4_1446/SM_PillarPartA_9M4_1446/Looks/MI_BeamsA_01/MI_CeilingA_06b'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_PillarPartA_9M4_1446/SM_PillarPartA_9M4_1446/Looks/MI_BeamsA_01/MI_CeilingA_06b'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_CeilingA_06b.mdl' (Sub Id: 'MI_CeilingA_06b')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_CeilingA_06b.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_D.png'
      * 'ColorAlbedo' [float4] = '(0.145, 0.145, 0.145, 0.000)'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_N.png'
      * 'MainTiling' [float4] = '(1.000, 1.000, 0.000, 1.000)'
      * 'MaskSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_M.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_ORM.png'
      * 'RoughnessMax' [float] = '0.9'
      * 'RoughnessMin' [float] = '0.1'

---

### /World/SortingArea/SM_PillarPartA_9M4_1446/SM_PillarPartA_9M4_1446/Looks/MI_FrameA_01

* **Prim路径 (Prim Path):**/World/SortingArea/SM_PillarPartA_9M4_1446/SM_PillarPartA_9M4_1446/Looks/MI_FrameA_01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_PillarPartA_9M4_1446/SM_PillarPartA_9M4_1446/Looks/MI_FrameA_01/MI_FrameA_01'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_PillarPartA_9M4_1446/SM_PillarPartA_9M4_1446/Looks/MI_FrameA_01/MI_FrameA_01'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_FrameA_01.mdl' (Sub Id: 'MI_FrameA_01')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_FrameA_01.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_D.png'
      * 'ColorAlbedo' [float4] = '(0.145, 0.145, 0.145, 0.000)'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_N.png'
      * 'MainTiling' [float4] = '(1.000, 1.000, 0.000, 1.000)'
      * 'MaskSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_M.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_ORM.png'
      * 'RoughnessMax' [float] = '0.9'
      * 'RoughnessMin' [float] = '0.1'

---

### /World/SortingArea/SM_PillarPartA_9M5_1454/SM_PillarPartA_9M5_1454/Looks/MI_BeamsA_01

* **Prim路径 (Prim Path):**/World/SortingArea/SM_PillarPartA_9M5_1454/SM_PillarPartA_9M5_1454/Looks/MI_BeamsA_01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_PillarPartA_9M5_1454/SM_PillarPartA_9M5_1454/Looks/MI_BeamsA_01/MI_CeilingA_06b'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_PillarPartA_9M5_1454/SM_PillarPartA_9M5_1454/Looks/MI_BeamsA_01/MI_CeilingA_06b'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_CeilingA_06b.mdl' (Sub Id: 'MI_CeilingA_06b')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_CeilingA_06b.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_D.png'
      * 'ColorAlbedo' [float4] = '(0.145, 0.145, 0.145, 0.000)'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_N.png'
      * 'MainTiling' [float4] = '(1.000, 1.000, 0.000, 1.000)'
      * 'MaskSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_M.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_ORM.png'
      * 'RoughnessMax' [float] = '0.9'
      * 'RoughnessMin' [float] = '0.1'

---

### /World/SortingArea/SM_PillarPartA_9M5_1454/SM_PillarPartA_9M5_1454/Looks/MI_FrameA_01

* **Prim路径 (Prim Path):**/World/SortingArea/SM_PillarPartA_9M5_1454/SM_PillarPartA_9M5_1454/Looks/MI_FrameA_01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_PillarPartA_9M5_1454/SM_PillarPartA_9M5_1454/Looks/MI_FrameA_01/MI_FrameA_01'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_PillarPartA_9M5_1454/SM_PillarPartA_9M5_1454/Looks/MI_FrameA_01/MI_FrameA_01'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_FrameA_01.mdl' (Sub Id: 'MI_FrameA_01')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_FrameA_01.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_D.png'
      * 'ColorAlbedo' [float4] = '(0.145, 0.145, 0.145, 0.000)'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_N.png'
      * 'MainTiling' [float4] = '(1.000, 1.000, 0.000, 1.000)'
      * 'MaskSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_M.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_ORM.png'
      * 'RoughnessMax' [float] = '0.9'
      * 'RoughnessMin' [float] = '0.1'

---

### /World/SortingArea/SM_PillarPartA_9M6_1455/SM_PillarPartA_9M6_1455/Looks/MI_BeamsA_01

* **Prim路径 (Prim Path):**/World/SortingArea/SM_PillarPartA_9M6_1455/SM_PillarPartA_9M6_1455/Looks/MI_BeamsA_01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_PillarPartA_9M6_1455/SM_PillarPartA_9M6_1455/Looks/MI_BeamsA_01/MI_CeilingA_06b'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_PillarPartA_9M6_1455/SM_PillarPartA_9M6_1455/Looks/MI_BeamsA_01/MI_CeilingA_06b'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_CeilingA_06b.mdl' (Sub Id: 'MI_CeilingA_06b')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_CeilingA_06b.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_D.png'
      * 'ColorAlbedo' [float4] = '(0.145, 0.145, 0.145, 0.000)'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_N.png'
      * 'MainTiling' [float4] = '(1.000, 1.000, 0.000, 1.000)'
      * 'MaskSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_M.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_ORM.png'
      * 'RoughnessMax' [float] = '0.9'
      * 'RoughnessMin' [float] = '0.1'

---

### /World/SortingArea/SM_PillarPartA_9M6_1455/SM_PillarPartA_9M6_1455/Looks/MI_FrameA_01

* **Prim路径 (Prim Path):**/World/SortingArea/SM_PillarPartA_9M6_1455/SM_PillarPartA_9M6_1455/Looks/MI_FrameA_01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_PillarPartA_9M6_1455/SM_PillarPartA_9M6_1455/Looks/MI_FrameA_01/MI_FrameA_01'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_PillarPartA_9M6_1455/SM_PillarPartA_9M6_1455/Looks/MI_FrameA_01/MI_FrameA_01'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_FrameA_01.mdl' (Sub Id: 'MI_FrameA_01')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_FrameA_01.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_D.png'
      * 'ColorAlbedo' [float4] = '(0.145, 0.145, 0.145, 0.000)'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_N.png'
      * 'MainTiling' [float4] = '(1.000, 1.000, 0.000, 1.000)'
      * 'MaskSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_M.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_ORM.png'
      * 'RoughnessMax' [float] = '0.9'
      * 'RoughnessMin' [float] = '0.1'

---

### /World/SortingArea/SM_PillarPartA_9M7_1463/SM_PillarPartA_9M7_1463/Looks/MI_BeamsA_01

* **Prim路径 (Prim Path):**/World/SortingArea/SM_PillarPartA_9M7_1463/SM_PillarPartA_9M7_1463/Looks/MI_BeamsA_01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_PillarPartA_9M7_1463/SM_PillarPartA_9M7_1463/Looks/MI_BeamsA_01/MI_CeilingA_06b'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_PillarPartA_9M7_1463/SM_PillarPartA_9M7_1463/Looks/MI_BeamsA_01/MI_CeilingA_06b'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_CeilingA_06b.mdl' (Sub Id: 'MI_CeilingA_06b')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_CeilingA_06b.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_D.png'
      * 'ColorAlbedo' [float4] = '(0.145, 0.145, 0.145, 0.000)'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_N.png'
      * 'MainTiling' [float4] = '(1.000, 1.000, 0.000, 1.000)'
      * 'MaskSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_M.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_ORM.png'
      * 'RoughnessMax' [float] = '0.9'
      * 'RoughnessMin' [float] = '0.1'

---

### /World/SortingArea/SM_PillarPartA_9M7_1463/SM_PillarPartA_9M7_1463/Looks/MI_FrameA_01

* **Prim路径 (Prim Path):**/World/SortingArea/SM_PillarPartA_9M7_1463/SM_PillarPartA_9M7_1463/Looks/MI_FrameA_01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_PillarPartA_9M7_1463/SM_PillarPartA_9M7_1463/Looks/MI_FrameA_01/MI_FrameA_01'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_PillarPartA_9M7_1463/SM_PillarPartA_9M7_1463/Looks/MI_FrameA_01/MI_FrameA_01'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_FrameA_01.mdl' (Sub Id: 'MI_FrameA_01')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_FrameA_01.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_D.png'
      * 'ColorAlbedo' [float4] = '(0.145, 0.145, 0.145, 0.000)'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_N.png'
      * 'MainTiling' [float4] = '(1.000, 1.000, 0.000, 1.000)'
      * 'MaskSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_M.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_ORM.png'
      * 'RoughnessMax' [float] = '0.9'
      * 'RoughnessMin' [float] = '0.1'

---

### /World/SortingArea/SM_PillarPartA_9M8_1464/SM_PillarPartA_9M8_1464/Looks/MI_BeamsA_01

* **Prim路径 (Prim Path):**/World/SortingArea/SM_PillarPartA_9M8_1464/SM_PillarPartA_9M8_1464/Looks/MI_BeamsA_01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_PillarPartA_9M8_1464/SM_PillarPartA_9M8_1464/Looks/MI_BeamsA_01/MI_CeilingA_06b'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_PillarPartA_9M8_1464/SM_PillarPartA_9M8_1464/Looks/MI_BeamsA_01/MI_CeilingA_06b'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_CeilingA_06b.mdl' (Sub Id: 'MI_CeilingA_06b')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_CeilingA_06b.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_D.png'
      * 'ColorAlbedo' [float4] = '(0.145, 0.145, 0.145, 0.000)'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_N.png'
      * 'MainTiling' [float4] = '(1.000, 1.000, 0.000, 1.000)'
      * 'MaskSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_M.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_ORM.png'
      * 'RoughnessMax' [float] = '0.9'
      * 'RoughnessMin' [float] = '0.1'

---

### /World/SortingArea/SM_PillarPartA_9M8_1464/SM_PillarPartA_9M8_1464/Looks/MI_FrameA_01

* **Prim路径 (Prim Path):**/World/SortingArea/SM_PillarPartA_9M8_1464/SM_PillarPartA_9M8_1464/Looks/MI_FrameA_01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_PillarPartA_9M8_1464/SM_PillarPartA_9M8_1464/Looks/MI_FrameA_01/MI_FrameA_01'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_PillarPartA_9M8_1464/SM_PillarPartA_9M8_1464/Looks/MI_FrameA_01/MI_FrameA_01'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_FrameA_01.mdl' (Sub Id: 'MI_FrameA_01')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_FrameA_01.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_D.png'
      * 'ColorAlbedo' [float4] = '(0.145, 0.145, 0.145, 0.000)'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_N.png'
      * 'MainTiling' [float4] = '(1.000, 1.000, 0.000, 1.000)'
      * 'MaskSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_M.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_ORM.png'
      * 'RoughnessMax' [float] = '0.9'
      * 'RoughnessMin' [float] = '0.1'

---

### /World/SortingArea/SM_PillarPartA_9M9_1472/SM_PillarPartA_9M9_1472/Looks/MI_BeamsA_01

* **Prim路径 (Prim Path):**/World/SortingArea/SM_PillarPartA_9M9_1472/SM_PillarPartA_9M9_1472/Looks/MI_BeamsA_01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_PillarPartA_9M9_1472/SM_PillarPartA_9M9_1472/Looks/MI_BeamsA_01/MI_CeilingA_06b'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_PillarPartA_9M9_1472/SM_PillarPartA_9M9_1472/Looks/MI_BeamsA_01/MI_CeilingA_06b'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_CeilingA_06b.mdl' (Sub Id: 'MI_CeilingA_06b')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_CeilingA_06b.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_D.png'
      * 'ColorAlbedo' [float4] = '(0.145, 0.145, 0.145, 0.000)'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_N.png'
      * 'MainTiling' [float4] = '(1.000, 1.000, 0.000, 1.000)'
      * 'MaskSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_M.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_ORM.png'
      * 'RoughnessMax' [float] = '0.9'
      * 'RoughnessMin' [float] = '0.1'

---

### /World/SortingArea/SM_PillarPartA_9M9_1472/SM_PillarPartA_9M9_1472/Looks/MI_FrameA_01

* **Prim路径 (Prim Path):**/World/SortingArea/SM_PillarPartA_9M9_1472/SM_PillarPartA_9M9_1472/Looks/MI_FrameA_01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_PillarPartA_9M9_1472/SM_PillarPartA_9M9_1472/Looks/MI_FrameA_01/MI_FrameA_01'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_PillarPartA_9M9_1472/SM_PillarPartA_9M9_1472/Looks/MI_FrameA_01/MI_FrameA_01'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_FrameA_01.mdl' (Sub Id: 'MI_FrameA_01')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_FrameA_01.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_D.png'
      * 'ColorAlbedo' [float4] = '(0.145, 0.145, 0.145, 0.000)'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_N.png'
      * 'MainTiling' [float4] = '(1.000, 1.000, 0.000, 1.000)'
      * 'MaskSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_M.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_FrameA_ORM.png'
      * 'RoughnessMax' [float] = '0.9'
      * 'RoughnessMin' [float] = '0.1'

---

### /World/SortingArea/SM_PushcartA_02_22/SM_PushcartA_02_22/Looks/MI_PushcartA_01

* **Prim路径 (Prim Path):**/World/SortingArea/SM_PushcartA_02_22/SM_PushcartA_02_22/Looks/MI_PushcartA_01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_PushcartA_02_22/SM_PushcartA_02_22/Looks/MI_PushcartA_01/MI_PushcartA_01'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_PushcartA_02_22/SM_PushcartA_02_22/Looks/MI_PushcartA_01/MI_PushcartA_01'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_PushcartA_01.mdl' (Sub Id: 'MI_PushcartA_01')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_PushcartA_01.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_PushcartA_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_PushcartA_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_PushcartA_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_PushcartA_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_PushcartA_D.png'
      * 'Body' [float4] = '(0.148, 0.176, 0.185, 1.000)'
      * 'Cap' [float4] = '(0.043, 0.155, 0.215, 1.000)'
      * 'Handle' [float4] = '(0.128, 0.128, 0.128, 1.000)'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_PushcartA_N.png'
      * 'MaskSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_PushcartA_M.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_PushcartA_ORM.png'
      * 'RoughnessMax' [float] = '0.9'
      * 'RoughnessMin' [float] = '0.1'

---

### /World/SortingArea/SM_SignA_27/SM_SignA_27/Looks/M_SignA

* **Prim路径 (Prim Path):**/World/SortingArea/SM_SignA_27/SM_SignA_27/Looks/M_SignA
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_SignA_27/SM_SignA_27/Looks/M_SignA/MI_SignB'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_SignA_27/SM_SignA_27/Looks/M_SignA/MI_SignB'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_SignB.mdl' (Sub Id: 'MI_SignB')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_SignB.mdl'

---

### /World/SortingArea/SM_SignB_23/SM_SignB_23/Looks/MI_SignB

* **Prim路径 (Prim Path):**/World/SortingArea/SM_SignB_23/SM_SignB_23/Looks/MI_SignB
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_SignB_23/SM_SignB_23/Looks/MI_SignB/MI_SignB'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_SignB_23/SM_SignB_23/Looks/MI_SignB/MI_SignB'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_SignB.mdl' (Sub Id: 'MI_SignB')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_SignB.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_SignsB_D.png'
    * Inputs:
      * 'TextureSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_SignsB_D.png'

---

### /World/SortingArea/SM_SignB_3/SM_SignB_3/Looks/MI_SignB

* **Prim路径 (Prim Path):**/World/SortingArea/SM_SignB_3/SM_SignB_3/Looks/MI_SignB
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_SignB_3/SM_SignB_3/Looks/MI_SignB/MI_SignB'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_SignB_3/SM_SignB_3/Looks/MI_SignB/MI_SignB'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_SignB.mdl' (Sub Id: 'MI_SignB')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_SignB.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_SignsB_D.png'
    * Inputs:
      * 'TextureSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_SignsB_D.png'

---

### /World/SortingArea/SM_WallA_3M13/SM_WallA_3M13/Looks/MI_CeilingA_01

* **Prim路径 (Prim Path):**/World/SortingArea/SM_WallA_3M13/SM_WallA_3M13/Looks/MI_CeilingA_01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_WallA_3M13/SM_WallA_3M13/Looks/MI_CeilingA_01/MI_CeilingA_06b'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_WallA_3M13/SM_WallA_3M13/Looks/MI_CeilingA_01/MI_CeilingA_06b'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_CeilingA_06b.mdl' (Sub Id: 'MI_CeilingA_06b')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_CeilingA_06b.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_D.png'
      * 'ColorAlbedo' [float4] = '(0.485, 0.194, 0.000, 1.000)'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_N.png'
      * 'MainTiling' [float4] = '(1.000, 1.000, 0.000, 1.000)'
      * 'MaskSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_M.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_ORM.png'
      * 'RoughnessMax' [float] = '0.9'
      * 'RoughnessMin' [float] = '0.1'

---

### /World/SortingArea/SM_WallA_3M13_01/SM_WallA_3M13_01/Looks/MI_CeilingA_01

* **Prim路径 (Prim Path):**/World/SortingArea/SM_WallA_3M13_01/SM_WallA_3M13_01/Looks/MI_CeilingA_01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_WallA_3M13_01/SM_WallA_3M13_01/Looks/MI_CeilingA_01/MI_CeilingA_06b'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_WallA_3M13_01/SM_WallA_3M13_01/Looks/MI_CeilingA_01/MI_CeilingA_06b'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_CeilingA_06b.mdl' (Sub Id: 'MI_CeilingA_06b')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_CeilingA_06b.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_D.png'
      * 'ColorAlbedo' [float4] = '(0.485, 0.194, 0.000, 1.000)'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_N.png'
      * 'MainTiling' [float4] = '(1.000, 1.000, 0.000, 1.000)'
      * 'MaskSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_M.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_ORM.png'
      * 'RoughnessMax' [float] = '0.9'
      * 'RoughnessMin' [float] = '0.1'

---

### /World/SortingArea/SM_WallA_3M14/SM_WallA_3M14/Looks/MI_CeilingA_01

* **Prim路径 (Prim Path):**/World/SortingArea/SM_WallA_3M14/SM_WallA_3M14/Looks/MI_CeilingA_01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_WallA_3M14/SM_WallA_3M14/Looks/MI_CeilingA_01/MI_CeilingA_06b'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_WallA_3M14/SM_WallA_3M14/Looks/MI_CeilingA_01/MI_CeilingA_06b'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_CeilingA_06b.mdl' (Sub Id: 'MI_CeilingA_06b')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_CeilingA_06b.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_D.png'
      * 'ColorAlbedo' [float4] = '(0.485, 0.194, 0.000, 1.000)'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_N.png'
      * 'MainTiling' [float4] = '(1.000, 1.000, 0.000, 1.000)'
      * 'MaskSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_M.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_ORM.png'
      * 'RoughnessMax' [float] = '0.9'
      * 'RoughnessMin' [float] = '0.1'

---

### /World/SortingArea/SM_WallA_3M14_01/SM_WallA_3M14_01/Looks/MI_CeilingA_01

* **Prim路径 (Prim Path):**/World/SortingArea/SM_WallA_3M14_01/SM_WallA_3M14_01/Looks/MI_CeilingA_01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_WallA_3M14_01/SM_WallA_3M14_01/Looks/MI_CeilingA_01/MI_CeilingA_06b'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_WallA_3M14_01/SM_WallA_3M14_01/Looks/MI_CeilingA_01/MI_CeilingA_06b'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_CeilingA_06b.mdl' (Sub Id: 'MI_CeilingA_06b')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_CeilingA_06b.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_D.png'
      * 'ColorAlbedo' [float4] = '(0.485, 0.194, 0.000, 1.000)'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_N.png'
      * 'MainTiling' [float4] = '(1.000, 1.000, 0.000, 1.000)'
      * 'MaskSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_M.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_ORM.png'
      * 'RoughnessMax' [float] = '0.9'
      * 'RoughnessMin' [float] = '0.1'

---

### /World/SortingArea/SM_WallA_3M15/SM_WallA_3M15/Looks/MI_CeilingA_01

* **Prim路径 (Prim Path):**/World/SortingArea/SM_WallA_3M15/SM_WallA_3M15/Looks/MI_CeilingA_01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_WallA_3M15/SM_WallA_3M15/Looks/MI_CeilingA_01/MI_CeilingA_06b'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_WallA_3M15/SM_WallA_3M15/Looks/MI_CeilingA_01/MI_CeilingA_06b'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_CeilingA_06b.mdl' (Sub Id: 'MI_CeilingA_06b')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_CeilingA_06b.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_D.png'
      * 'ColorAlbedo' [float4] = '(0.485, 0.194, 0.000, 1.000)'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_N.png'
      * 'MainTiling' [float4] = '(1.000, 1.000, 0.000, 1.000)'
      * 'MaskSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_M.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_ORM.png'
      * 'RoughnessMax' [float] = '0.9'
      * 'RoughnessMin' [float] = '0.1'

---

### /World/SortingArea/SM_WallA_3M16/SM_WallA_3M16/Looks/MI_CeilingA_01

* **Prim路径 (Prim Path):**/World/SortingArea/SM_WallA_3M16/SM_WallA_3M16/Looks/MI_CeilingA_01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_WallA_3M16/SM_WallA_3M16/Looks/MI_CeilingA_01/MI_CeilingA_06b'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_WallA_3M16/SM_WallA_3M16/Looks/MI_CeilingA_01/MI_CeilingA_06b'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_CeilingA_06b.mdl' (Sub Id: 'MI_CeilingA_06b')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_CeilingA_06b.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_D.png'
      * 'ColorAlbedo' [float4] = '(0.485, 0.194, 0.000, 1.000)'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_N.png'
      * 'MainTiling' [float4] = '(1.000, 1.000, 0.000, 1.000)'
      * 'MaskSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_M.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_ORM.png'
      * 'RoughnessMax' [float] = '0.9'
      * 'RoughnessMin' [float] = '0.1'

---

### /World/SortingArea/SM_WallA_3M18_460/SM_WallA_3M18_460/Looks/MI_CeilingA_01

* **Prim路径 (Prim Path):**/World/SortingArea/SM_WallA_3M18_460/SM_WallA_3M18_460/Looks/MI_CeilingA_01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_WallA_3M18_460/SM_WallA_3M18_460/Looks/MI_CeilingA_01/MI_CeilingA_06b'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_WallA_3M18_460/SM_WallA_3M18_460/Looks/MI_CeilingA_01/MI_CeilingA_06b'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_CeilingA_06b.mdl' (Sub Id: 'MI_CeilingA_06b')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_CeilingA_06b.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_D.png'
      * 'ColorAlbedo' [float4] = '(0.485, 0.194, 0.000, 1.000)'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_N.png'
      * 'MainTiling' [float4] = '(1.000, 1.000, 0.000, 1.000)'
      * 'MaskSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_M.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_ORM.png'
      * 'RoughnessMax' [float] = '0.9'
      * 'RoughnessMin' [float] = '0.1'

---

### /World/SortingArea/SM_WallA_3M19/SM_WallA_3M19/Looks/MI_CeilingA_01

* **Prim路径 (Prim Path):**/World/SortingArea/SM_WallA_3M19/SM_WallA_3M19/Looks/MI_CeilingA_01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_WallA_3M19/SM_WallA_3M19/Looks/MI_CeilingA_01/MI_CeilingA_06b'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_WallA_3M19/SM_WallA_3M19/Looks/MI_CeilingA_01/MI_CeilingA_06b'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_CeilingA_06b.mdl' (Sub Id: 'MI_CeilingA_06b')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_CeilingA_06b.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_D.png'
      * 'ColorAlbedo' [float4] = '(0.485, 0.194, 0.000, 1.000)'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_N.png'
      * 'MainTiling' [float4] = '(1.000, 1.000, 0.000, 1.000)'
      * 'MaskSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_M.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_ORM.png'
      * 'RoughnessMax' [float] = '0.9'
      * 'RoughnessMin' [float] = '0.1'

---

### /World/SortingArea/SM_WallA_3M20/SM_WallA_3M20/Looks/MI_CeilingA_01

* **Prim路径 (Prim Path):**/World/SortingArea/SM_WallA_3M20/SM_WallA_3M20/Looks/MI_CeilingA_01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_WallA_3M20/SM_WallA_3M20/Looks/MI_CeilingA_01/MI_CeilingA_06b'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_WallA_3M20/SM_WallA_3M20/Looks/MI_CeilingA_01/MI_CeilingA_06b'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_CeilingA_06b.mdl' (Sub Id: 'MI_CeilingA_06b')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_CeilingA_06b.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_D.png'
      * 'ColorAlbedo' [float4] = '(0.485, 0.194, 0.000, 1.000)'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_N.png'
      * 'MainTiling' [float4] = '(1.000, 1.000, 0.000, 1.000)'
      * 'MaskSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_M.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_ORM.png'
      * 'RoughnessMax' [float] = '0.9'
      * 'RoughnessMin' [float] = '0.1'

---

### /World/SortingArea/SM_WallA_3M21_1371/SM_WallA_3M21_1371/Looks/MI_CeilingA_01

* **Prim路径 (Prim Path):**/World/SortingArea/SM_WallA_3M21_1371/SM_WallA_3M21_1371/Looks/MI_CeilingA_01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_WallA_3M21_1371/SM_WallA_3M21_1371/Looks/MI_CeilingA_01/MI_CeilingA_06b'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_WallA_3M21_1371/SM_WallA_3M21_1371/Looks/MI_CeilingA_01/MI_CeilingA_06b'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_CeilingA_06b.mdl' (Sub Id: 'MI_CeilingA_06b')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_CeilingA_06b.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_D.png'
      * 'ColorAlbedo' [float4] = '(0.485, 0.194, 0.000, 1.000)'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_N.png'
      * 'MainTiling' [float4] = '(1.000, 1.000, 0.000, 1.000)'
      * 'MaskSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_M.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_ORM.png'
      * 'RoughnessMax' [float] = '0.9'
      * 'RoughnessMin' [float] = '0.1'

---

### /World/SortingArea/SM_WallA_3M26/SM_WallA_3M26/Looks/MI_CeilingA_01

* **Prim路径 (Prim Path):**/World/SortingArea/SM_WallA_3M26/SM_WallA_3M26/Looks/MI_CeilingA_01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_WallA_3M26/SM_WallA_3M26/Looks/MI_CeilingA_01/MI_CeilingA_06b'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_WallA_3M26/SM_WallA_3M26/Looks/MI_CeilingA_01/MI_CeilingA_06b'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_CeilingA_06b.mdl' (Sub Id: 'MI_CeilingA_06b')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_CeilingA_06b.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_D.png'
      * 'ColorAlbedo' [float4] = '(0.485, 0.194, 0.000, 1.000)'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_N.png'
      * 'MainTiling' [float4] = '(1.000, 1.000, 0.000, 1.000)'
      * 'MaskSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_M.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_ORM.png'
      * 'RoughnessMax' [float] = '0.9'
      * 'RoughnessMin' [float] = '0.1'

---

### /World/SortingArea/SM_WallA_3M27/SM_WallA_3M27/Looks/MI_CeilingA_01

* **Prim路径 (Prim Path):**/World/SortingArea/SM_WallA_3M27/SM_WallA_3M27/Looks/MI_CeilingA_01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_WallA_3M27/SM_WallA_3M27/Looks/MI_CeilingA_01/MI_CeilingA_06b'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_WallA_3M27/SM_WallA_3M27/Looks/MI_CeilingA_01/MI_CeilingA_06b'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_CeilingA_06b.mdl' (Sub Id: 'MI_CeilingA_06b')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_CeilingA_06b.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_D.png'
      * 'ColorAlbedo' [float4] = '(0.485, 0.194, 0.000, 1.000)'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_N.png'
      * 'MainTiling' [float4] = '(1.000, 1.000, 0.000, 1.000)'
      * 'MaskSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_M.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_ORM.png'
      * 'RoughnessMax' [float] = '0.9'
      * 'RoughnessMin' [float] = '0.1'

---

### /World/SortingArea/SM_WallA_3M28/SM_WallA_3M28/Looks/MI_CeilingA_01

* **Prim路径 (Prim Path):**/World/SortingArea/SM_WallA_3M28/SM_WallA_3M28/Looks/MI_CeilingA_01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_WallA_3M28/SM_WallA_3M28/Looks/MI_CeilingA_01/MI_CeilingA_06b'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_WallA_3M28/SM_WallA_3M28/Looks/MI_CeilingA_01/MI_CeilingA_06b'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_CeilingA_06b.mdl' (Sub Id: 'MI_CeilingA_06b')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_CeilingA_06b.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_D.png'
      * 'ColorAlbedo' [float4] = '(0.485, 0.194, 0.000, 1.000)'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_N.png'
      * 'MainTiling' [float4] = '(1.000, 1.000, 0.000, 1.000)'
      * 'MaskSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_M.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_ORM.png'
      * 'RoughnessMax' [float] = '0.9'
      * 'RoughnessMin' [float] = '0.1'

---

### /World/SortingArea/SM_WallA_3M36/SM_WallA_3M36/Looks/MI_CeilingA_01

* **Prim路径 (Prim Path):**/World/SortingArea/SM_WallA_3M36/SM_WallA_3M36/Looks/MI_CeilingA_01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_WallA_3M36/SM_WallA_3M36/Looks/MI_CeilingA_01/MI_CeilingA_06b'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_WallA_3M36/SM_WallA_3M36/Looks/MI_CeilingA_01/MI_CeilingA_06b'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_CeilingA_06b.mdl' (Sub Id: 'MI_CeilingA_06b')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_CeilingA_06b.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_D.png'
      * 'ColorAlbedo' [float4] = '(0.485, 0.194, 0.000, 1.000)'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_N.png'
      * 'MainTiling' [float4] = '(1.000, 1.000, 0.000, 1.000)'
      * 'MaskSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_M.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_ORM.png'
      * 'RoughnessMax' [float] = '0.9'
      * 'RoughnessMin' [float] = '0.1'

---

### /World/SortingArea/SM_WallA_3M37/SM_WallA_3M37/Looks/MI_CeilingA_01

* **Prim路径 (Prim Path):**/World/SortingArea/SM_WallA_3M37/SM_WallA_3M37/Looks/MI_CeilingA_01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_WallA_3M37/SM_WallA_3M37/Looks/MI_CeilingA_01/MI_CeilingA_06b'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_WallA_3M37/SM_WallA_3M37/Looks/MI_CeilingA_01/MI_CeilingA_06b'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_CeilingA_06b.mdl' (Sub Id: 'MI_CeilingA_06b')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_CeilingA_06b.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_D.png'
      * 'ColorAlbedo' [float4] = '(0.485, 0.194, 0.000, 1.000)'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_N.png'
      * 'MainTiling' [float4] = '(1.000, 1.000, 0.000, 1.000)'
      * 'MaskSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_M.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_ORM.png'
      * 'RoughnessMax' [float] = '0.9'
      * 'RoughnessMin' [float] = '0.1'

---

### /World/SortingArea/SM_WallA_3M38/SM_WallA_3M38/Looks/MI_CeilingA_01

* **Prim路径 (Prim Path):**/World/SortingArea/SM_WallA_3M38/SM_WallA_3M38/Looks/MI_CeilingA_01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_WallA_3M38/SM_WallA_3M38/Looks/MI_CeilingA_01/MI_CeilingA_06b'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_WallA_3M38/SM_WallA_3M38/Looks/MI_CeilingA_01/MI_CeilingA_06b'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_CeilingA_06b.mdl' (Sub Id: 'MI_CeilingA_06b')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_CeilingA_06b.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_D.png'
      * 'ColorAlbedo' [float4] = '(0.485, 0.194, 0.000, 1.000)'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_N.png'
      * 'MainTiling' [float4] = '(1.000, 1.000, 0.000, 1.000)'
      * 'MaskSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_M.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_ORM.png'
      * 'RoughnessMax' [float] = '0.9'
      * 'RoughnessMin' [float] = '0.1'

---

### /World/SortingArea/SM_WallA_3M39/SM_WallA_3M39/Looks/MI_CeilingA_01

* **Prim路径 (Prim Path):**/World/SortingArea/SM_WallA_3M39/SM_WallA_3M39/Looks/MI_CeilingA_01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_WallA_3M39/SM_WallA_3M39/Looks/MI_CeilingA_01/MI_CeilingA_06b'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_WallA_3M39/SM_WallA_3M39/Looks/MI_CeilingA_01/MI_CeilingA_06b'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_CeilingA_06b.mdl' (Sub Id: 'MI_CeilingA_06b')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_CeilingA_06b.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_D.png'
      * 'ColorAlbedo' [float4] = '(0.485, 0.194, 0.000, 1.000)'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_N.png'
      * 'MainTiling' [float4] = '(1.000, 1.000, 0.000, 1.000)'
      * 'MaskSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_M.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_ORM.png'
      * 'RoughnessMax' [float] = '0.9'
      * 'RoughnessMin' [float] = '0.1'

---

### /World/SortingArea/SM_WallA_3M40/SM_WallA_3M40/Looks/MI_CeilingA_01

* **Prim路径 (Prim Path):**/World/SortingArea/SM_WallA_3M40/SM_WallA_3M40/Looks/MI_CeilingA_01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_WallA_3M40/SM_WallA_3M40/Looks/MI_CeilingA_01/MI_CeilingA_06b'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_WallA_3M40/SM_WallA_3M40/Looks/MI_CeilingA_01/MI_CeilingA_06b'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_CeilingA_06b.mdl' (Sub Id: 'MI_CeilingA_06b')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_CeilingA_06b.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_D.png'
      * 'ColorAlbedo' [float4] = '(0.485, 0.194, 0.000, 1.000)'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_N.png'
      * 'MainTiling' [float4] = '(1.000, 1.000, 0.000, 1.000)'
      * 'MaskSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_M.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_ORM.png'
      * 'RoughnessMax' [float] = '0.9'
      * 'RoughnessMin' [float] = '0.1'

---

### /World/SortingArea/SM_WallA_3M41/SM_WallA_3M41/Looks/MI_CeilingA_01

* **Prim路径 (Prim Path):**/World/SortingArea/SM_WallA_3M41/SM_WallA_3M41/Looks/MI_CeilingA_01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_WallA_3M41/SM_WallA_3M41/Looks/MI_CeilingA_01/MI_CeilingA_06b'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_WallA_3M41/SM_WallA_3M41/Looks/MI_CeilingA_01/MI_CeilingA_06b'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_CeilingA_06b.mdl' (Sub Id: 'MI_CeilingA_06b')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_CeilingA_06b.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_D.png'
      * 'ColorAlbedo' [float4] = '(0.485, 0.194, 0.000, 1.000)'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_N.png'
      * 'MainTiling' [float4] = '(1.000, 1.000, 0.000, 1.000)'
      * 'MaskSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_M.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_ORM.png'
      * 'RoughnessMax' [float] = '0.9'
      * 'RoughnessMin' [float] = '0.1'

---

### /World/SortingArea/SM_WallA_3M43/SM_WallA_3M43/Looks/MI_WallA_01

* **Prim路径 (Prim Path):**/World/SortingArea/SM_WallA_3M43/SM_WallA_3M43/Looks/MI_WallA_01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_WallA_3M43/SM_WallA_3M43/Looks/MI_WallA_01/MI_Floor_01'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_WallA_3M43/SM_WallA_3M43/Looks/MI_WallA_01/MI_Floor_01'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_Floor_01.mdl' (Sub Id: 'MI_Floor_01')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_Floor_01.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BlankMask_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_01_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_01_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_01_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_01_D.png'
      * 'ColorAlbedo' [float4] = '(0.560, 0.560, 0.560, 0.000)'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_01_N.png'
      * 'MainNormalStrenght' [float4] = '(1.000, 1.000, 0.900, 1.000)'
      * 'MainTiling' [float4] = '(1.300, 1.300, 0.000, 0.000)'
      * 'MaskSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BlankMask_M.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_01_ORM.png'
      * 'RoughnessMax' [float] = '0.9'
      * 'RoughnessMin' [float] = '0.1'

---

### /World/SortingArea/SM_WallA_3M43/SM_WallA_3M43/Looks/MI_BeamsA_02

* **Prim路径 (Prim Path):**/World/SortingArea/SM_WallA_3M43/SM_WallA_3M43/Looks/MI_BeamsA_02
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_WallA_3M43/SM_WallA_3M43/Looks/MI_BeamsA_02/MI_CeilingA_06b'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_WallA_3M43/SM_WallA_3M43/Looks/MI_BeamsA_02/MI_CeilingA_06b'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_CeilingA_06b.mdl' (Sub Id: 'MI_CeilingA_06b')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_CeilingA_06b.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_D.png'
      * 'ColorAlbedo' [float4] = '(0.035, 0.035, 0.035, 1.000)'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_N.png'
      * 'MainTiling' [float4] = '(1.000, 1.000, 0.000, 1.000)'
      * 'MaskSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_M.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_ORM.png'
      * 'RoughnessMax' [float] = '0.9'
      * 'RoughnessMin' [float] = '0.1'

---

### /World/SortingArea/SM_WallA_3M43_01/SM_WallA_3M43_01/Looks/MI_WallA_01

* **Prim路径 (Prim Path):**/World/SortingArea/SM_WallA_3M43_01/SM_WallA_3M43_01/Looks/MI_WallA_01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_WallA_3M43_01/SM_WallA_3M43_01/Looks/MI_WallA_01/MI_Floor_01'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_WallA_3M43_01/SM_WallA_3M43_01/Looks/MI_WallA_01/MI_Floor_01'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_Floor_01.mdl' (Sub Id: 'MI_Floor_01')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_Floor_01.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BlankMask_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_01_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_01_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_01_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_01_D.png'
      * 'ColorAlbedo' [float4] = '(0.560, 0.560, 0.560, 0.000)'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_01_N.png'
      * 'MainNormalStrenght' [float4] = '(1.000, 1.000, 0.900, 1.000)'
      * 'MainTiling' [float4] = '(1.300, 1.300, 0.000, 0.000)'
      * 'MaskSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BlankMask_M.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_01_ORM.png'
      * 'RoughnessMax' [float] = '0.9'
      * 'RoughnessMin' [float] = '0.1'

---

### /World/SortingArea/SM_WallA_3M43_01/SM_WallA_3M43_01/Looks/MI_BeamsA_02

* **Prim路径 (Prim Path):**/World/SortingArea/SM_WallA_3M43_01/SM_WallA_3M43_01/Looks/MI_BeamsA_02
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_WallA_3M43_01/SM_WallA_3M43_01/Looks/MI_BeamsA_02/MI_CeilingA_06b'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_WallA_3M43_01/SM_WallA_3M43_01/Looks/MI_BeamsA_02/MI_CeilingA_06b'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_CeilingA_06b.mdl' (Sub Id: 'MI_CeilingA_06b')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_CeilingA_06b.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_D.png'
      * 'ColorAlbedo' [float4] = '(0.035, 0.035, 0.035, 1.000)'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_N.png'
      * 'MainTiling' [float4] = '(1.000, 1.000, 0.000, 1.000)'
      * 'MaskSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_M.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_ORM.png'
      * 'RoughnessMax' [float] = '0.9'
      * 'RoughnessMin' [float] = '0.1'

---

### /World/SortingArea/SM_WallA_3M44/SM_WallA_3M44/Looks/MI_WallA_01

* **Prim路径 (Prim Path):**/World/SortingArea/SM_WallA_3M44/SM_WallA_3M44/Looks/MI_WallA_01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_WallA_3M44/SM_WallA_3M44/Looks/MI_WallA_01/MI_Floor_01'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_WallA_3M44/SM_WallA_3M44/Looks/MI_WallA_01/MI_Floor_01'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_Floor_01.mdl' (Sub Id: 'MI_Floor_01')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_Floor_01.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BlankMask_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_01_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_01_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_01_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_01_D.png'
      * 'ColorAlbedo' [float4] = '(0.560, 0.560, 0.560, 0.000)'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_01_N.png'
      * 'MainNormalStrenght' [float4] = '(1.000, 1.000, 0.900, 1.000)'
      * 'MainTiling' [float4] = '(1.300, 1.300, 0.000, 0.000)'
      * 'MaskSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BlankMask_M.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_01_ORM.png'
      * 'RoughnessMax' [float] = '0.9'
      * 'RoughnessMin' [float] = '0.1'

---

### /World/SortingArea/SM_WallA_3M44/SM_WallA_3M44/Looks/MI_BeamsA_02

* **Prim路径 (Prim Path):**/World/SortingArea/SM_WallA_3M44/SM_WallA_3M44/Looks/MI_BeamsA_02
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_WallA_3M44/SM_WallA_3M44/Looks/MI_BeamsA_02/MI_CeilingA_06b'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_WallA_3M44/SM_WallA_3M44/Looks/MI_BeamsA_02/MI_CeilingA_06b'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_CeilingA_06b.mdl' (Sub Id: 'MI_CeilingA_06b')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_CeilingA_06b.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_D.png'
      * 'ColorAlbedo' [float4] = '(0.035, 0.035, 0.035, 1.000)'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_N.png'
      * 'MainTiling' [float4] = '(1.000, 1.000, 0.000, 1.000)'
      * 'MaskSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_M.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_ORM.png'
      * 'RoughnessMax' [float] = '0.9'
      * 'RoughnessMin' [float] = '0.1'

---

### /World/SortingArea/SM_WallA_3M8/SM_WallA_3M8/Looks/MI_CeilingA_01

* **Prim路径 (Prim Path):**/World/SortingArea/SM_WallA_3M8/SM_WallA_3M8/Looks/MI_CeilingA_01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_WallA_3M8/SM_WallA_3M8/Looks/MI_CeilingA_01/MI_CeilingA_06b'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_WallA_3M8/SM_WallA_3M8/Looks/MI_CeilingA_01/MI_CeilingA_06b'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_CeilingA_06b.mdl' (Sub Id: 'MI_CeilingA_06b')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_CeilingA_06b.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_D.png'
      * 'ColorAlbedo' [float4] = '(0.485, 0.194, 0.000, 1.000)'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_N.png'
      * 'MainTiling' [float4] = '(1.000, 1.000, 0.000, 1.000)'
      * 'MaskSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_M.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_ORM.png'
      * 'RoughnessMax' [float] = '0.9'
      * 'RoughnessMin' [float] = '0.1'

---

### /World/SortingArea/SM_WallA_6M10/SM_WallA_6M10/Looks/MI_WallA_01

* **Prim路径 (Prim Path):**/World/SortingArea/SM_WallA_6M10/SM_WallA_6M10/Looks/MI_WallA_01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_WallA_6M10/SM_WallA_6M10/Looks/MI_WallA_01/MI_Floor_01'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_WallA_6M10/SM_WallA_6M10/Looks/MI_WallA_01/MI_Floor_01'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_Floor_01.mdl' (Sub Id: 'MI_Floor_01')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_Floor_01.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BlankMask_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_01_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_01_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_01_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_01_D.png'
      * 'ColorAlbedo' [float4] = '(0.560, 0.560, 0.560, 0.000)'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_01_N.png'
      * 'MainNormalStrenght' [float4] = '(1.000, 1.000, 0.900, 1.000)'
      * 'MainTiling' [float4] = '(1.300, 1.300, 0.000, 0.000)'
      * 'MaskSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BlankMask_M.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_01_ORM.png'
      * 'RoughnessMax' [float] = '0.9'
      * 'RoughnessMin' [float] = '0.1'

---

### /World/SortingArea/SM_WallA_6M10/SM_WallA_6M10/Looks/MI_BeamsA_02

* **Prim路径 (Prim Path):**/World/SortingArea/SM_WallA_6M10/SM_WallA_6M10/Looks/MI_BeamsA_02
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_WallA_6M10/SM_WallA_6M10/Looks/MI_BeamsA_02/MI_CeilingA_06b'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_WallA_6M10/SM_WallA_6M10/Looks/MI_BeamsA_02/MI_CeilingA_06b'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_CeilingA_06b.mdl' (Sub Id: 'MI_CeilingA_06b')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_CeilingA_06b.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_D.png'
      * 'ColorAlbedo' [float4] = '(0.035, 0.035, 0.035, 1.000)'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_N.png'
      * 'MainTiling' [float4] = '(1.000, 1.000, 0.000, 1.000)'
      * 'MaskSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_M.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_ORM.png'
      * 'RoughnessMax' [float] = '0.9'
      * 'RoughnessMin' [float] = '0.1'

---

### /World/SortingArea/SM_WallA_6M11/SM_WallA_6M11/Looks/MI_WallA_01

* **Prim路径 (Prim Path):**/World/SortingArea/SM_WallA_6M11/SM_WallA_6M11/Looks/MI_WallA_01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_WallA_6M11/SM_WallA_6M11/Looks/MI_WallA_01/MI_Floor_01'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_WallA_6M11/SM_WallA_6M11/Looks/MI_WallA_01/MI_Floor_01'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_Floor_01.mdl' (Sub Id: 'MI_Floor_01')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_Floor_01.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BlankMask_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_01_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_01_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_01_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_01_D.png'
      * 'ColorAlbedo' [float4] = '(0.560, 0.560, 0.560, 0.000)'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_01_N.png'
      * 'MainNormalStrenght' [float4] = '(1.000, 1.000, 0.900, 1.000)'
      * 'MainTiling' [float4] = '(1.300, 1.300, 0.000, 0.000)'
      * 'MaskSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BlankMask_M.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_01_ORM.png'
      * 'RoughnessMax' [float] = '0.9'
      * 'RoughnessMin' [float] = '0.1'

---

### /World/SortingArea/SM_WallA_6M11/SM_WallA_6M11/Looks/MI_BeamsA_02

* **Prim路径 (Prim Path):**/World/SortingArea/SM_WallA_6M11/SM_WallA_6M11/Looks/MI_BeamsA_02
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_WallA_6M11/SM_WallA_6M11/Looks/MI_BeamsA_02/MI_CeilingA_06b'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_WallA_6M11/SM_WallA_6M11/Looks/MI_BeamsA_02/MI_CeilingA_06b'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_CeilingA_06b.mdl' (Sub Id: 'MI_CeilingA_06b')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_CeilingA_06b.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_D.png'
      * 'ColorAlbedo' [float4] = '(0.035, 0.035, 0.035, 1.000)'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_N.png'
      * 'MainTiling' [float4] = '(1.000, 1.000, 0.000, 1.000)'
      * 'MaskSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_M.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_ORM.png'
      * 'RoughnessMax' [float] = '0.9'
      * 'RoughnessMin' [float] = '0.1'

---

### /World/SortingArea/SM_WallA_6M12/SM_WallA_6M12/Looks/MI_WallA_01

* **Prim路径 (Prim Path):**/World/SortingArea/SM_WallA_6M12/SM_WallA_6M12/Looks/MI_WallA_01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_WallA_6M12/SM_WallA_6M12/Looks/MI_WallA_01/MI_Floor_01'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_WallA_6M12/SM_WallA_6M12/Looks/MI_WallA_01/MI_Floor_01'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_Floor_01.mdl' (Sub Id: 'MI_Floor_01')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_Floor_01.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BlankMask_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_01_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_01_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_01_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_01_D.png'
      * 'ColorAlbedo' [float4] = '(0.560, 0.560, 0.560, 0.000)'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_01_N.png'
      * 'MainNormalStrenght' [float4] = '(1.000, 1.000, 0.900, 1.000)'
      * 'MainTiling' [float4] = '(1.300, 1.300, 0.000, 0.000)'
      * 'MaskSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BlankMask_M.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_01_ORM.png'
      * 'RoughnessMax' [float] = '0.9'
      * 'RoughnessMin' [float] = '0.1'

---

### /World/SortingArea/SM_WallA_6M12/SM_WallA_6M12/Looks/MI_BeamsA_02

* **Prim路径 (Prim Path):**/World/SortingArea/SM_WallA_6M12/SM_WallA_6M12/Looks/MI_BeamsA_02
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_WallA_6M12/SM_WallA_6M12/Looks/MI_BeamsA_02/MI_CeilingA_06b'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_WallA_6M12/SM_WallA_6M12/Looks/MI_BeamsA_02/MI_CeilingA_06b'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_CeilingA_06b.mdl' (Sub Id: 'MI_CeilingA_06b')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_CeilingA_06b.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_D.png'
      * 'ColorAlbedo' [float4] = '(0.035, 0.035, 0.035, 1.000)'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_N.png'
      * 'MainTiling' [float4] = '(1.000, 1.000, 0.000, 1.000)'
      * 'MaskSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_M.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_ORM.png'
      * 'RoughnessMax' [float] = '0.9'
      * 'RoughnessMin' [float] = '0.1'

---

### /World/SortingArea/SM_WallA_6M15/SM_WallA_6M15/Looks/MI_WallA_01

* **Prim路径 (Prim Path):**/World/SortingArea/SM_WallA_6M15/SM_WallA_6M15/Looks/MI_WallA_01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_WallA_6M15/SM_WallA_6M15/Looks/MI_WallA_01/MI_Floor_01'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_WallA_6M15/SM_WallA_6M15/Looks/MI_WallA_01/MI_Floor_01'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_Floor_01.mdl' (Sub Id: 'MI_Floor_01')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_Floor_01.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BlankMask_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_01_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_01_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_01_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_01_D.png'
      * 'ColorAlbedo' [float4] = '(0.560, 0.560, 0.560, 0.000)'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_01_N.png'
      * 'MainNormalStrenght' [float4] = '(1.000, 1.000, 0.900, 1.000)'
      * 'MainTiling' [float4] = '(1.300, 1.300, 0.000, 0.000)'
      * 'MaskSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BlankMask_M.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_01_ORM.png'
      * 'RoughnessMax' [float] = '0.9'
      * 'RoughnessMin' [float] = '0.1'

---

### /World/SortingArea/SM_WallA_6M15/SM_WallA_6M15/Looks/MI_BeamsA_02

* **Prim路径 (Prim Path):**/World/SortingArea/SM_WallA_6M15/SM_WallA_6M15/Looks/MI_BeamsA_02
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_WallA_6M15/SM_WallA_6M15/Looks/MI_BeamsA_02/MI_CeilingA_06b'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_WallA_6M15/SM_WallA_6M15/Looks/MI_BeamsA_02/MI_CeilingA_06b'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_CeilingA_06b.mdl' (Sub Id: 'MI_CeilingA_06b')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_CeilingA_06b.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_D.png'
      * 'ColorAlbedo' [float4] = '(0.035, 0.035, 0.035, 1.000)'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_N.png'
      * 'MainTiling' [float4] = '(1.000, 1.000, 0.000, 1.000)'
      * 'MaskSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_M.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_ORM.png'
      * 'RoughnessMax' [float] = '0.9'
      * 'RoughnessMin' [float] = '0.1'

---

### /World/SortingArea/SM_WallA_6M16/SM_WallA_6M16/Looks/MI_WallA_01

* **Prim路径 (Prim Path):**/World/SortingArea/SM_WallA_6M16/SM_WallA_6M16/Looks/MI_WallA_01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_WallA_6M16/SM_WallA_6M16/Looks/MI_WallA_01/MI_Floor_01'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_WallA_6M16/SM_WallA_6M16/Looks/MI_WallA_01/MI_Floor_01'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_Floor_01.mdl' (Sub Id: 'MI_Floor_01')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_Floor_01.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BlankMask_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_01_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_01_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_01_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_01_D.png'
      * 'ColorAlbedo' [float4] = '(0.560, 0.560, 0.560, 0.000)'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_01_N.png'
      * 'MainNormalStrenght' [float4] = '(1.000, 1.000, 0.900, 1.000)'
      * 'MainTiling' [float4] = '(1.300, 1.300, 0.000, 0.000)'
      * 'MaskSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BlankMask_M.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_01_ORM.png'
      * 'RoughnessMax' [float] = '0.9'
      * 'RoughnessMin' [float] = '0.1'

---

### /World/SortingArea/SM_WallA_6M16/SM_WallA_6M16/Looks/MI_BeamsA_02

* **Prim路径 (Prim Path):**/World/SortingArea/SM_WallA_6M16/SM_WallA_6M16/Looks/MI_BeamsA_02
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_WallA_6M16/SM_WallA_6M16/Looks/MI_BeamsA_02/MI_CeilingA_06b'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_WallA_6M16/SM_WallA_6M16/Looks/MI_BeamsA_02/MI_CeilingA_06b'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_CeilingA_06b.mdl' (Sub Id: 'MI_CeilingA_06b')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_CeilingA_06b.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_D.png'
      * 'ColorAlbedo' [float4] = '(0.035, 0.035, 0.035, 1.000)'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_N.png'
      * 'MainTiling' [float4] = '(1.000, 1.000, 0.000, 1.000)'
      * 'MaskSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_M.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_ORM.png'
      * 'RoughnessMax' [float] = '0.9'
      * 'RoughnessMin' [float] = '0.1'

---

### /World/SortingArea/SM_WallA_6M17/SM_WallA_6M17/Looks/MI_WallA_01

* **Prim路径 (Prim Path):**/World/SortingArea/SM_WallA_6M17/SM_WallA_6M17/Looks/MI_WallA_01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_WallA_6M17/SM_WallA_6M17/Looks/MI_WallA_01/MI_Floor_01'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_WallA_6M17/SM_WallA_6M17/Looks/MI_WallA_01/MI_Floor_01'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_Floor_01.mdl' (Sub Id: 'MI_Floor_01')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_Floor_01.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BlankMask_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_01_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_01_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_01_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_01_D.png'
      * 'ColorAlbedo' [float4] = '(0.560, 0.560, 0.560, 0.000)'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_01_N.png'
      * 'MainNormalStrenght' [float4] = '(1.000, 1.000, 0.900, 1.000)'
      * 'MainTiling' [float4] = '(1.300, 1.300, 0.000, 0.000)'
      * 'MaskSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BlankMask_M.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_01_ORM.png'
      * 'RoughnessMax' [float] = '0.9'
      * 'RoughnessMin' [float] = '0.1'

---

### /World/SortingArea/SM_WallA_6M17/SM_WallA_6M17/Looks/MI_BeamsA_02

* **Prim路径 (Prim Path):**/World/SortingArea/SM_WallA_6M17/SM_WallA_6M17/Looks/MI_BeamsA_02
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_WallA_6M17/SM_WallA_6M17/Looks/MI_BeamsA_02/MI_CeilingA_06b'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_WallA_6M17/SM_WallA_6M17/Looks/MI_BeamsA_02/MI_CeilingA_06b'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_CeilingA_06b.mdl' (Sub Id: 'MI_CeilingA_06b')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_CeilingA_06b.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_D.png'
      * 'ColorAlbedo' [float4] = '(0.035, 0.035, 0.035, 1.000)'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_N.png'
      * 'MainTiling' [float4] = '(1.000, 1.000, 0.000, 1.000)'
      * 'MaskSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_M.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_ORM.png'
      * 'RoughnessMax' [float] = '0.9'
      * 'RoughnessMin' [float] = '0.1'

---

### /World/SortingArea/SM_WallA_6M18/SM_WallA_6M18/Looks/MI_WallA_01

* **Prim路径 (Prim Path):**/World/SortingArea/SM_WallA_6M18/SM_WallA_6M18/Looks/MI_WallA_01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_WallA_6M18/SM_WallA_6M18/Looks/MI_WallA_01/MI_Floor_01'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_WallA_6M18/SM_WallA_6M18/Looks/MI_WallA_01/MI_Floor_01'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_Floor_01.mdl' (Sub Id: 'MI_Floor_01')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_Floor_01.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BlankMask_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_01_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_01_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_01_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_01_D.png'
      * 'ColorAlbedo' [float4] = '(0.560, 0.560, 0.560, 0.000)'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_01_N.png'
      * 'MainNormalStrenght' [float4] = '(1.000, 1.000, 0.900, 1.000)'
      * 'MainTiling' [float4] = '(1.300, 1.300, 0.000, 0.000)'
      * 'MaskSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BlankMask_M.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_01_ORM.png'
      * 'RoughnessMax' [float] = '0.9'
      * 'RoughnessMin' [float] = '0.1'

---

### /World/SortingArea/SM_WallA_6M18/SM_WallA_6M18/Looks/MI_BeamsA_02

* **Prim路径 (Prim Path):**/World/SortingArea/SM_WallA_6M18/SM_WallA_6M18/Looks/MI_BeamsA_02
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_WallA_6M18/SM_WallA_6M18/Looks/MI_BeamsA_02/MI_CeilingA_06b'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_WallA_6M18/SM_WallA_6M18/Looks/MI_BeamsA_02/MI_CeilingA_06b'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_CeilingA_06b.mdl' (Sub Id: 'MI_CeilingA_06b')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_CeilingA_06b.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_D.png'
      * 'ColorAlbedo' [float4] = '(0.035, 0.035, 0.035, 1.000)'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_N.png'
      * 'MainTiling' [float4] = '(1.000, 1.000, 0.000, 1.000)'
      * 'MaskSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_M.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_ORM.png'
      * 'RoughnessMax' [float] = '0.9'
      * 'RoughnessMin' [float] = '0.1'

---

### /World/SortingArea/SM_WallA_6M4/SM_WallA_6M4/Looks/MI_WallA_01

* **Prim路径 (Prim Path):**/World/SortingArea/SM_WallA_6M4/SM_WallA_6M4/Looks/MI_WallA_01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_WallA_6M4/SM_WallA_6M4/Looks/MI_WallA_01/MI_Floor_01'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_WallA_6M4/SM_WallA_6M4/Looks/MI_WallA_01/MI_Floor_01'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_Floor_01.mdl' (Sub Id: 'MI_Floor_01')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_Floor_01.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BlankMask_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_01_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_01_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_01_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_01_D.png'
      * 'ColorAlbedo' [float4] = '(0.560, 0.560, 0.560, 0.000)'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_01_N.png'
      * 'MainNormalStrenght' [float4] = '(1.000, 1.000, 0.900, 1.000)'
      * 'MainTiling' [float4] = '(1.300, 1.300, 0.000, 0.000)'
      * 'MaskSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BlankMask_M.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_01_ORM.png'
      * 'RoughnessMax' [float] = '0.9'
      * 'RoughnessMin' [float] = '0.1'

---

### /World/SortingArea/SM_WallA_6M4/SM_WallA_6M4/Looks/MI_BeamsA_02

* **Prim路径 (Prim Path):**/World/SortingArea/SM_WallA_6M4/SM_WallA_6M4/Looks/MI_BeamsA_02
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_WallA_6M4/SM_WallA_6M4/Looks/MI_BeamsA_02/MI_CeilingA_06b'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_WallA_6M4/SM_WallA_6M4/Looks/MI_BeamsA_02/MI_CeilingA_06b'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_CeilingA_06b.mdl' (Sub Id: 'MI_CeilingA_06b')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_CeilingA_06b.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_D.png'
      * 'ColorAlbedo' [float4] = '(0.035, 0.035, 0.035, 1.000)'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_N.png'
      * 'MainTiling' [float4] = '(1.000, 1.000, 0.000, 1.000)'
      * 'MaskSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_M.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_ORM.png'
      * 'RoughnessMax' [float] = '0.9'
      * 'RoughnessMin' [float] = '0.1'

---

### /World/SortingArea/SM_WallA_6M5/SM_WallA_6M5/Looks/MI_WallA_01

* **Prim路径 (Prim Path):**/World/SortingArea/SM_WallA_6M5/SM_WallA_6M5/Looks/MI_WallA_01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_WallA_6M5/SM_WallA_6M5/Looks/MI_WallA_01/MI_Floor_01'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_WallA_6M5/SM_WallA_6M5/Looks/MI_WallA_01/MI_Floor_01'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_Floor_01.mdl' (Sub Id: 'MI_Floor_01')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_Floor_01.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BlankMask_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_01_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_01_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_01_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_01_D.png'
      * 'ColorAlbedo' [float4] = '(0.560, 0.560, 0.560, 0.000)'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_01_N.png'
      * 'MainNormalStrenght' [float4] = '(1.000, 1.000, 0.900, 1.000)'
      * 'MainTiling' [float4] = '(1.300, 1.300, 0.000, 0.000)'
      * 'MaskSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BlankMask_M.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_01_ORM.png'
      * 'RoughnessMax' [float] = '0.9'
      * 'RoughnessMin' [float] = '0.1'

---

### /World/SortingArea/SM_WallA_6M5/SM_WallA_6M5/Looks/MI_BeamsA_02

* **Prim路径 (Prim Path):**/World/SortingArea/SM_WallA_6M5/SM_WallA_6M5/Looks/MI_BeamsA_02
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_WallA_6M5/SM_WallA_6M5/Looks/MI_BeamsA_02/MI_CeilingA_06b'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_WallA_6M5/SM_WallA_6M5/Looks/MI_BeamsA_02/MI_CeilingA_06b'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_CeilingA_06b.mdl' (Sub Id: 'MI_CeilingA_06b')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_CeilingA_06b.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_D.png'
      * 'ColorAlbedo' [float4] = '(0.035, 0.035, 0.035, 1.000)'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_N.png'
      * 'MainTiling' [float4] = '(1.000, 1.000, 0.000, 1.000)'
      * 'MaskSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_M.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_ORM.png'
      * 'RoughnessMax' [float] = '0.9'
      * 'RoughnessMin' [float] = '0.1'

---

### /World/SortingArea/SM_WallA_6M6/SM_WallA_6M6/Looks/MI_WallA_01

* **Prim路径 (Prim Path):**/World/SortingArea/SM_WallA_6M6/SM_WallA_6M6/Looks/MI_WallA_01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_WallA_6M6/SM_WallA_6M6/Looks/MI_WallA_01/MI_Floor_01'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_WallA_6M6/SM_WallA_6M6/Looks/MI_WallA_01/MI_Floor_01'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_Floor_01.mdl' (Sub Id: 'MI_Floor_01')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_Floor_01.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BlankMask_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_01_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_01_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_01_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_01_D.png'
      * 'ColorAlbedo' [float4] = '(0.560, 0.560, 0.560, 0.000)'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_01_N.png'
      * 'MainNormalStrenght' [float4] = '(1.000, 1.000, 0.900, 1.000)'
      * 'MainTiling' [float4] = '(1.300, 1.300, 0.000, 0.000)'
      * 'MaskSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BlankMask_M.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_01_ORM.png'
      * 'RoughnessMax' [float] = '0.9'
      * 'RoughnessMin' [float] = '0.1'

---

### /World/SortingArea/SM_WallA_6M6/SM_WallA_6M6/Looks/MI_BeamsA_02

* **Prim路径 (Prim Path):**/World/SortingArea/SM_WallA_6M6/SM_WallA_6M6/Looks/MI_BeamsA_02
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_WallA_6M6/SM_WallA_6M6/Looks/MI_BeamsA_02/MI_CeilingA_06b'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_WallA_6M6/SM_WallA_6M6/Looks/MI_BeamsA_02/MI_CeilingA_06b'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_CeilingA_06b.mdl' (Sub Id: 'MI_CeilingA_06b')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_CeilingA_06b.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_D.png'
      * 'ColorAlbedo' [float4] = '(0.035, 0.035, 0.035, 1.000)'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_N.png'
      * 'MainTiling' [float4] = '(1.000, 1.000, 0.000, 1.000)'
      * 'MaskSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_M.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_ORM.png'
      * 'RoughnessMax' [float] = '0.9'
      * 'RoughnessMin' [float] = '0.1'

---

### /World/SortingArea/SM_WallA_6M7/SM_WallA_6M7/Looks/MI_WallA_01

* **Prim路径 (Prim Path):**/World/SortingArea/SM_WallA_6M7/SM_WallA_6M7/Looks/MI_WallA_01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_WallA_6M7/SM_WallA_6M7/Looks/MI_WallA_01/MI_Floor_01'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_WallA_6M7/SM_WallA_6M7/Looks/MI_WallA_01/MI_Floor_01'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_Floor_01.mdl' (Sub Id: 'MI_Floor_01')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_Floor_01.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BlankMask_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_01_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_01_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_01_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_01_D.png'
      * 'ColorAlbedo' [float4] = '(0.560, 0.560, 0.560, 0.000)'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_01_N.png'
      * 'MainNormalStrenght' [float4] = '(1.000, 1.000, 0.900, 1.000)'
      * 'MainTiling' [float4] = '(1.300, 1.300, 0.000, 0.000)'
      * 'MaskSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BlankMask_M.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_01_ORM.png'
      * 'RoughnessMax' [float] = '0.9'
      * 'RoughnessMin' [float] = '0.1'

---

### /World/SortingArea/SM_WallA_6M7/SM_WallA_6M7/Looks/MI_BeamsA_02

* **Prim路径 (Prim Path):**/World/SortingArea/SM_WallA_6M7/SM_WallA_6M7/Looks/MI_BeamsA_02
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_WallA_6M7/SM_WallA_6M7/Looks/MI_BeamsA_02/MI_CeilingA_06b'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_WallA_6M7/SM_WallA_6M7/Looks/MI_BeamsA_02/MI_CeilingA_06b'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_CeilingA_06b.mdl' (Sub Id: 'MI_CeilingA_06b')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_CeilingA_06b.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_D.png'
      * 'ColorAlbedo' [float4] = '(0.035, 0.035, 0.035, 1.000)'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_N.png'
      * 'MainTiling' [float4] = '(1.000, 1.000, 0.000, 1.000)'
      * 'MaskSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_M.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_ORM.png'
      * 'RoughnessMax' [float] = '0.9'
      * 'RoughnessMin' [float] = '0.1'

---

### /World/SortingArea/SM_WallA_InnerCorner10/SM_WallA_InnerCorner10/Looks/MI_WallA_01

* **Prim路径 (Prim Path):**/World/SortingArea/SM_WallA_InnerCorner10/SM_WallA_InnerCorner10/Looks/MI_WallA_01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_WallA_InnerCorner10/SM_WallA_InnerCorner10/Looks/MI_WallA_01/MI_Floor_01'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_WallA_InnerCorner10/SM_WallA_InnerCorner10/Looks/MI_WallA_01/MI_Floor_01'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_Floor_01.mdl' (Sub Id: 'MI_Floor_01')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_Floor_01.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BlankMask_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_01_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_01_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_01_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_01_D.png'
      * 'ColorAlbedo' [float4] = '(0.560, 0.560, 0.560, 0.000)'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_01_N.png'
      * 'MainNormalStrenght' [float4] = '(1.000, 1.000, 0.900, 1.000)'
      * 'MainTiling' [float4] = '(1.300, 1.300, 0.000, 0.000)'
      * 'MaskSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BlankMask_M.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_01_ORM.png'
      * 'RoughnessMax' [float] = '0.9'
      * 'RoughnessMin' [float] = '0.1'

---

### /World/SortingArea/SM_WallA_InnerCorner10/SM_WallA_InnerCorner10/Looks/MI_BeamsA_02

* **Prim路径 (Prim Path):**/World/SortingArea/SM_WallA_InnerCorner10/SM_WallA_InnerCorner10/Looks/MI_BeamsA_02
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_WallA_InnerCorner10/SM_WallA_InnerCorner10/Looks/MI_BeamsA_02/MI_CeilingA_06b'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_WallA_InnerCorner10/SM_WallA_InnerCorner10/Looks/MI_BeamsA_02/MI_CeilingA_06b'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_CeilingA_06b.mdl' (Sub Id: 'MI_CeilingA_06b')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_CeilingA_06b.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_D.png'
      * 'ColorAlbedo' [float4] = '(0.035, 0.035, 0.035, 1.000)'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_N.png'
      * 'MainTiling' [float4] = '(1.000, 1.000, 0.000, 1.000)'
      * 'MaskSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_M.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_ORM.png'
      * 'RoughnessMax' [float] = '0.9'
      * 'RoughnessMin' [float] = '0.1'

---

### /World/SortingArea/SM_WallA_InnerCorner11/SM_WallA_InnerCorner11/Looks/MI_WallA_01

* **Prim路径 (Prim Path):**/World/SortingArea/SM_WallA_InnerCorner11/SM_WallA_InnerCorner11/Looks/MI_WallA_01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_WallA_InnerCorner11/SM_WallA_InnerCorner11/Looks/MI_WallA_01/MI_Floor_01'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_WallA_InnerCorner11/SM_WallA_InnerCorner11/Looks/MI_WallA_01/MI_Floor_01'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_Floor_01.mdl' (Sub Id: 'MI_Floor_01')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_Floor_01.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BlankMask_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_01_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_01_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_01_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_01_D.png'
      * 'ColorAlbedo' [float4] = '(0.560, 0.560, 0.560, 0.000)'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_01_N.png'
      * 'MainNormalStrenght' [float4] = '(1.000, 1.000, 0.900, 1.000)'
      * 'MainTiling' [float4] = '(1.300, 1.300, 0.000, 0.000)'
      * 'MaskSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BlankMask_M.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_01_ORM.png'
      * 'RoughnessMax' [float] = '0.9'
      * 'RoughnessMin' [float] = '0.1'

---

### /World/SortingArea/SM_WallA_InnerCorner11/SM_WallA_InnerCorner11/Looks/MI_BeamsA_02

* **Prim路径 (Prim Path):**/World/SortingArea/SM_WallA_InnerCorner11/SM_WallA_InnerCorner11/Looks/MI_BeamsA_02
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_WallA_InnerCorner11/SM_WallA_InnerCorner11/Looks/MI_BeamsA_02/MI_CeilingA_06b'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_WallA_InnerCorner11/SM_WallA_InnerCorner11/Looks/MI_BeamsA_02/MI_CeilingA_06b'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_CeilingA_06b.mdl' (Sub Id: 'MI_CeilingA_06b')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_CeilingA_06b.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_D.png'
      * 'ColorAlbedo' [float4] = '(0.035, 0.035, 0.035, 1.000)'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_N.png'
      * 'MainTiling' [float4] = '(1.000, 1.000, 0.000, 1.000)'
      * 'MaskSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_M.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_ORM.png'
      * 'RoughnessMax' [float] = '0.9'
      * 'RoughnessMin' [float] = '0.1'

---

### /World/SortingArea/SM_WallA_InnerCorner12/SM_WallA_InnerCorner12/Looks/MI_WallA_01

* **Prim路径 (Prim Path):**/World/SortingArea/SM_WallA_InnerCorner12/SM_WallA_InnerCorner12/Looks/MI_WallA_01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_WallA_InnerCorner12/SM_WallA_InnerCorner12/Looks/MI_WallA_01/MI_Floor_01'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_WallA_InnerCorner12/SM_WallA_InnerCorner12/Looks/MI_WallA_01/MI_Floor_01'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_Floor_01.mdl' (Sub Id: 'MI_Floor_01')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_Floor_01.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BlankMask_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_01_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_01_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_01_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_01_D.png'
      * 'ColorAlbedo' [float4] = '(0.560, 0.560, 0.560, 0.000)'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_01_N.png'
      * 'MainNormalStrenght' [float4] = '(1.000, 1.000, 0.900, 1.000)'
      * 'MainTiling' [float4] = '(1.300, 1.300, 0.000, 0.000)'
      * 'MaskSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BlankMask_M.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_01_ORM.png'
      * 'RoughnessMax' [float] = '0.9'
      * 'RoughnessMin' [float] = '0.1'

---

### /World/SortingArea/SM_WallA_InnerCorner12/SM_WallA_InnerCorner12/Looks/MI_BeamsA_02

* **Prim路径 (Prim Path):**/World/SortingArea/SM_WallA_InnerCorner12/SM_WallA_InnerCorner12/Looks/MI_BeamsA_02
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_WallA_InnerCorner12/SM_WallA_InnerCorner12/Looks/MI_BeamsA_02/MI_CeilingA_06b'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_WallA_InnerCorner12/SM_WallA_InnerCorner12/Looks/MI_BeamsA_02/MI_CeilingA_06b'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_CeilingA_06b.mdl' (Sub Id: 'MI_CeilingA_06b')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_CeilingA_06b.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_D.png'
      * 'ColorAlbedo' [float4] = '(0.035, 0.035, 0.035, 1.000)'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_N.png'
      * 'MainTiling' [float4] = '(1.000, 1.000, 0.000, 1.000)'
      * 'MaskSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_M.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_ORM.png'
      * 'RoughnessMax' [float] = '0.9'
      * 'RoughnessMin' [float] = '0.1'

---

### /World/SortingArea/SM_WallA_InnerCorner13/SM_WallA_InnerCorner13/Looks/MI_CeilingA_01

* **Prim路径 (Prim Path):**/World/SortingArea/SM_WallA_InnerCorner13/SM_WallA_InnerCorner13/Looks/MI_CeilingA_01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_WallA_InnerCorner13/SM_WallA_InnerCorner13/Looks/MI_CeilingA_01/MI_CeilingA_06b'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_WallA_InnerCorner13/SM_WallA_InnerCorner13/Looks/MI_CeilingA_01/MI_CeilingA_06b'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_CeilingA_06b.mdl' (Sub Id: 'MI_CeilingA_06b')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_CeilingA_06b.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_D.png'
      * 'ColorAlbedo' [float4] = '(0.485, 0.194, 0.000, 1.000)'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_N.png'
      * 'MainTiling' [float4] = '(1.000, 1.000, 0.000, 1.000)'
      * 'MaskSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_M.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_ORM.png'
      * 'RoughnessMax' [float] = '0.9'
      * 'RoughnessMin' [float] = '0.1'

---

### /World/SortingArea/SM_WallA_InnerCorner14/SM_WallA_InnerCorner14/Looks/MI_CeilingA_01

* **Prim路径 (Prim Path):**/World/SortingArea/SM_WallA_InnerCorner14/SM_WallA_InnerCorner14/Looks/MI_CeilingA_01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_WallA_InnerCorner14/SM_WallA_InnerCorner14/Looks/MI_CeilingA_01/MI_CeilingA_06b'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_WallA_InnerCorner14/SM_WallA_InnerCorner14/Looks/MI_CeilingA_01/MI_CeilingA_06b'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_CeilingA_06b.mdl' (Sub Id: 'MI_CeilingA_06b')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_CeilingA_06b.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_D.png'
      * 'ColorAlbedo' [float4] = '(0.485, 0.194, 0.000, 1.000)'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_N.png'
      * 'MainTiling' [float4] = '(1.000, 1.000, 0.000, 1.000)'
      * 'MaskSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_M.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_ORM.png'
      * 'RoughnessMax' [float] = '0.9'
      * 'RoughnessMin' [float] = '0.1'

---

### /World/SortingArea/SM_WallA_InnerCorner15/SM_WallA_InnerCorner15/Looks/MI_CeilingA_01

* **Prim路径 (Prim Path):**/World/SortingArea/SM_WallA_InnerCorner15/SM_WallA_InnerCorner15/Looks/MI_CeilingA_01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_WallA_InnerCorner15/SM_WallA_InnerCorner15/Looks/MI_CeilingA_01/MI_CeilingA_06b'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_WallA_InnerCorner15/SM_WallA_InnerCorner15/Looks/MI_CeilingA_01/MI_CeilingA_06b'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_CeilingA_06b.mdl' (Sub Id: 'MI_CeilingA_06b')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_CeilingA_06b.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_D.png'
      * 'ColorAlbedo' [float4] = '(0.485, 0.194, 0.000, 1.000)'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_N.png'
      * 'MainTiling' [float4] = '(1.000, 1.000, 0.000, 1.000)'
      * 'MaskSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_M.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_ORM.png'
      * 'RoughnessMax' [float] = '0.9'
      * 'RoughnessMin' [float] = '0.1'

---

### /World/SortingArea/SM_WallA_InnerCorner16/SM_WallA_InnerCorner16/Looks/MI_CeilingA_01

* **Prim路径 (Prim Path):**/World/SortingArea/SM_WallA_InnerCorner16/SM_WallA_InnerCorner16/Looks/MI_CeilingA_01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_WallA_InnerCorner16/SM_WallA_InnerCorner16/Looks/MI_CeilingA_01/MI_CeilingA_06b'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_WallA_InnerCorner16/SM_WallA_InnerCorner16/Looks/MI_CeilingA_01/MI_CeilingA_06b'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_CeilingA_06b.mdl' (Sub Id: 'MI_CeilingA_06b')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_CeilingA_06b.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_D.png'
      * 'ColorAlbedo' [float4] = '(0.485, 0.194, 0.000, 1.000)'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_N.png'
      * 'MainTiling' [float4] = '(1.000, 1.000, 0.000, 1.000)'
      * 'MaskSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_M.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_ORM.png'
      * 'RoughnessMax' [float] = '0.9'
      * 'RoughnessMin' [float] = '0.1'

---

### /World/SortingArea/SM_WallA_InnerCorner18/SM_WallA_InnerCorner18/Looks/MI_CeilingA_01

* **Prim路径 (Prim Path):**/World/SortingArea/SM_WallA_InnerCorner18/SM_WallA_InnerCorner18/Looks/MI_CeilingA_01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_WallA_InnerCorner18/SM_WallA_InnerCorner18/Looks/MI_CeilingA_01/MI_CeilingA_06b'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_WallA_InnerCorner18/SM_WallA_InnerCorner18/Looks/MI_CeilingA_01/MI_CeilingA_06b'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_CeilingA_06b.mdl' (Sub Id: 'MI_CeilingA_06b')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_CeilingA_06b.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_D.png'
      * 'ColorAlbedo' [float4] = '(0.485, 0.194, 0.000, 1.000)'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_N.png'
      * 'MainTiling' [float4] = '(1.000, 1.000, 0.000, 1.000)'
      * 'MaskSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_M.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_ORM.png'
      * 'RoughnessMax' [float] = '0.9'
      * 'RoughnessMin' [float] = '0.1'

---

### /World/SortingArea/SM_WallA_InnerCorner24/SM_WallA_InnerCorner24/Looks/MI_CeilingA_01

* **Prim路径 (Prim Path):**/World/SortingArea/SM_WallA_InnerCorner24/SM_WallA_InnerCorner24/Looks/MI_CeilingA_01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_WallA_InnerCorner24/SM_WallA_InnerCorner24/Looks/MI_CeilingA_01/MI_CeilingA_06b'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_WallA_InnerCorner24/SM_WallA_InnerCorner24/Looks/MI_CeilingA_01/MI_CeilingA_06b'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_CeilingA_06b.mdl' (Sub Id: 'MI_CeilingA_06b')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_CeilingA_06b.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_D.png'
      * 'ColorAlbedo' [float4] = '(0.485, 0.194, 0.000, 1.000)'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_N.png'
      * 'MainTiling' [float4] = '(1.000, 1.000, 0.000, 1.000)'
      * 'MaskSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_M.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_ORM.png'
      * 'RoughnessMax' [float] = '0.9'
      * 'RoughnessMin' [float] = '0.1'

---

### /World/SortingArea/SM_WallA_InnerCorner25/SM_WallA_InnerCorner25/Looks/MI_CeilingA_01

* **Prim路径 (Prim Path):**/World/SortingArea/SM_WallA_InnerCorner25/SM_WallA_InnerCorner25/Looks/MI_CeilingA_01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_WallA_InnerCorner25/SM_WallA_InnerCorner25/Looks/MI_CeilingA_01/MI_CeilingA_06b'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_WallA_InnerCorner25/SM_WallA_InnerCorner25/Looks/MI_CeilingA_01/MI_CeilingA_06b'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_CeilingA_06b.mdl' (Sub Id: 'MI_CeilingA_06b')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_CeilingA_06b.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_D.png'
      * 'ColorAlbedo' [float4] = '(0.485, 0.194, 0.000, 1.000)'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_N.png'
      * 'MainTiling' [float4] = '(1.000, 1.000, 0.000, 1.000)'
      * 'MaskSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_M.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_ORM.png'
      * 'RoughnessMax' [float] = '0.9'
      * 'RoughnessMin' [float] = '0.1'

---

### /World/SortingArea/SM_WallA_InnerCorner26/SM_WallA_InnerCorner26/Looks/MI_CeilingA_01

* **Prim路径 (Prim Path):**/World/SortingArea/SM_WallA_InnerCorner26/SM_WallA_InnerCorner26/Looks/MI_CeilingA_01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_WallA_InnerCorner26/SM_WallA_InnerCorner26/Looks/MI_CeilingA_01/MI_CeilingA_06b'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_WallA_InnerCorner26/SM_WallA_InnerCorner26/Looks/MI_CeilingA_01/MI_CeilingA_06b'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_CeilingA_06b.mdl' (Sub Id: 'MI_CeilingA_06b')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_CeilingA_06b.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_D.png'
      * 'ColorAlbedo' [float4] = '(0.485, 0.194, 0.000, 1.000)'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_N.png'
      * 'MainTiling' [float4] = '(1.000, 1.000, 0.000, 1.000)'
      * 'MaskSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_M.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_ORM.png'
      * 'RoughnessMax' [float] = '0.9'
      * 'RoughnessMin' [float] = '0.1'

---

### /World/SortingArea/SM_WallA_InnerCorner27/SM_WallA_InnerCorner27/Looks/MI_CeilingA_01

* **Prim路径 (Prim Path):**/World/SortingArea/SM_WallA_InnerCorner27/SM_WallA_InnerCorner27/Looks/MI_CeilingA_01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_WallA_InnerCorner27/SM_WallA_InnerCorner27/Looks/MI_CeilingA_01/MI_CeilingA_06b'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_WallA_InnerCorner27/SM_WallA_InnerCorner27/Looks/MI_CeilingA_01/MI_CeilingA_06b'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_CeilingA_06b.mdl' (Sub Id: 'MI_CeilingA_06b')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_CeilingA_06b.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_D.png'
      * 'ColorAlbedo' [float4] = '(0.485, 0.194, 0.000, 1.000)'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_N.png'
      * 'MainTiling' [float4] = '(1.000, 1.000, 0.000, 1.000)'
      * 'MaskSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_M.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_ORM.png'
      * 'RoughnessMax' [float] = '0.9'
      * 'RoughnessMin' [float] = '0.1'

---

### /World/SortingArea/SM_WallA_InnerCorner28/SM_WallA_InnerCorner28/Looks/MI_CeilingA_01

* **Prim路径 (Prim Path):**/World/SortingArea/SM_WallA_InnerCorner28/SM_WallA_InnerCorner28/Looks/MI_CeilingA_01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_WallA_InnerCorner28/SM_WallA_InnerCorner28/Looks/MI_CeilingA_01/MI_CeilingA_06b'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_WallA_InnerCorner28/SM_WallA_InnerCorner28/Looks/MI_CeilingA_01/MI_CeilingA_06b'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_CeilingA_06b.mdl' (Sub Id: 'MI_CeilingA_06b')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_CeilingA_06b.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_D.png'
      * 'ColorAlbedo' [float4] = '(0.485, 0.194, 0.000, 1.000)'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_N.png'
      * 'MainTiling' [float4] = '(1.000, 1.000, 0.000, 1.000)'
      * 'MaskSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_M.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_ORM.png'
      * 'RoughnessMax' [float] = '0.9'
      * 'RoughnessMin' [float] = '0.1'

---

### /World/SortingArea/SM_WallA_InnerCorner29/SM_WallA_InnerCorner29/Looks/MI_CeilingA_01

* **Prim路径 (Prim Path):**/World/SortingArea/SM_WallA_InnerCorner29/SM_WallA_InnerCorner29/Looks/MI_CeilingA_01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_WallA_InnerCorner29/SM_WallA_InnerCorner29/Looks/MI_CeilingA_01/MI_CeilingA_06b'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_WallA_InnerCorner29/SM_WallA_InnerCorner29/Looks/MI_CeilingA_01/MI_CeilingA_06b'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_CeilingA_06b.mdl' (Sub Id: 'MI_CeilingA_06b')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_CeilingA_06b.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_D.png'
      * 'ColorAlbedo' [float4] = '(0.485, 0.194, 0.000, 1.000)'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_N.png'
      * 'MainTiling' [float4] = '(1.000, 1.000, 0.000, 1.000)'
      * 'MaskSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_M.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_ORM.png'
      * 'RoughnessMax' [float] = '0.9'
      * 'RoughnessMin' [float] = '0.1'

---

### /World/SortingArea/SM_WallA_InnerCorner30/SM_WallA_InnerCorner30/Looks/MI_CeilingA_01

* **Prim路径 (Prim Path):**/World/SortingArea/SM_WallA_InnerCorner30/SM_WallA_InnerCorner30/Looks/MI_CeilingA_01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_WallA_InnerCorner30/SM_WallA_InnerCorner30/Looks/MI_CeilingA_01/MI_CeilingA_06b'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_WallA_InnerCorner30/SM_WallA_InnerCorner30/Looks/MI_CeilingA_01/MI_CeilingA_06b'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_CeilingA_06b.mdl' (Sub Id: 'MI_CeilingA_06b')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_CeilingA_06b.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_D.png'
      * 'ColorAlbedo' [float4] = '(0.485, 0.194, 0.000, 1.000)'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_N.png'
      * 'MainTiling' [float4] = '(1.000, 1.000, 0.000, 1.000)'
      * 'MaskSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_M.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_ORM.png'
      * 'RoughnessMax' [float] = '0.9'
      * 'RoughnessMin' [float] = '0.1'

---

### /World/SortingArea/SM_WallA_InnerCorner32/SM_WallA_InnerCorner32/Looks/MI_CeilingA_01

* **Prim路径 (Prim Path):**/World/SortingArea/SM_WallA_InnerCorner32/SM_WallA_InnerCorner32/Looks/MI_CeilingA_01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_WallA_InnerCorner32/SM_WallA_InnerCorner32/Looks/MI_CeilingA_01/MI_CeilingA_06b'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_WallA_InnerCorner32/SM_WallA_InnerCorner32/Looks/MI_CeilingA_01/MI_CeilingA_06b'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_CeilingA_06b.mdl' (Sub Id: 'MI_CeilingA_06b')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_CeilingA_06b.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_D.png'
      * 'ColorAlbedo' [float4] = '(0.485, 0.194, 0.000, 1.000)'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_N.png'
      * 'MainTiling' [float4] = '(1.000, 1.000, 0.000, 1.000)'
      * 'MaskSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_M.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_ORM.png'
      * 'RoughnessMax' [float] = '0.9'
      * 'RoughnessMin' [float] = '0.1'

---

### /World/SortingArea/SM_WallA_InnerCorner33/SM_WallA_InnerCorner33/Looks/MI_CeilingA_01

* **Prim路径 (Prim Path):**/World/SortingArea/SM_WallA_InnerCorner33/SM_WallA_InnerCorner33/Looks/MI_CeilingA_01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_WallA_InnerCorner33/SM_WallA_InnerCorner33/Looks/MI_CeilingA_01/MI_CeilingA_06b'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_WallA_InnerCorner33/SM_WallA_InnerCorner33/Looks/MI_CeilingA_01/MI_CeilingA_06b'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_CeilingA_06b.mdl' (Sub Id: 'MI_CeilingA_06b')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_CeilingA_06b.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_D.png'
      * 'ColorAlbedo' [float4] = '(0.485, 0.194, 0.000, 1.000)'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_N.png'
      * 'MainTiling' [float4] = '(1.000, 1.000, 0.000, 1.000)'
      * 'MaskSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_M.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_ORM.png'
      * 'RoughnessMax' [float] = '0.9'
      * 'RoughnessMin' [float] = '0.1'

---

### /World/SortingArea/SM_WallA_InnerCorner34/SM_WallA_InnerCorner34/Looks/MI_CeilingA_01

* **Prim路径 (Prim Path):**/World/SortingArea/SM_WallA_InnerCorner34/SM_WallA_InnerCorner34/Looks/MI_CeilingA_01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_WallA_InnerCorner34/SM_WallA_InnerCorner34/Looks/MI_CeilingA_01/MI_CeilingA_06b'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_WallA_InnerCorner34/SM_WallA_InnerCorner34/Looks/MI_CeilingA_01/MI_CeilingA_06b'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_CeilingA_06b.mdl' (Sub Id: 'MI_CeilingA_06b')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_CeilingA_06b.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_D.png'
      * 'ColorAlbedo' [float4] = '(0.485, 0.194, 0.000, 1.000)'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_N.png'
      * 'MainTiling' [float4] = '(1.000, 1.000, 0.000, 1.000)'
      * 'MaskSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_M.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_ORM.png'
      * 'RoughnessMax' [float] = '0.9'
      * 'RoughnessMin' [float] = '0.1'

---

### /World/SortingArea/SM_WallA_InnerCorner35/SM_WallA_InnerCorner35/Looks/MI_CeilingA_01

* **Prim路径 (Prim Path):**/World/SortingArea/SM_WallA_InnerCorner35/SM_WallA_InnerCorner35/Looks/MI_CeilingA_01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_WallA_InnerCorner35/SM_WallA_InnerCorner35/Looks/MI_CeilingA_01/MI_CeilingA_06b'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_WallA_InnerCorner35/SM_WallA_InnerCorner35/Looks/MI_CeilingA_01/MI_CeilingA_06b'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_CeilingA_06b.mdl' (Sub Id: 'MI_CeilingA_06b')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_CeilingA_06b.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_D.png'
      * 'ColorAlbedo' [float4] = '(0.485, 0.194, 0.000, 1.000)'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_N.png'
      * 'MainTiling' [float4] = '(1.000, 1.000, 0.000, 1.000)'
      * 'MaskSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_M.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_CeilingA_ORM.png'
      * 'RoughnessMax' [float] = '0.9'
      * 'RoughnessMin' [float] = '0.1'

---

### /World/SortingArea/SM_WallA_InnerCorner9_88/SM_WallA_InnerCorner9_88/Looks/MI_WallA_01

* **Prim路径 (Prim Path):**/World/SortingArea/SM_WallA_InnerCorner9_88/SM_WallA_InnerCorner9_88/Looks/MI_WallA_01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_WallA_InnerCorner9_88/SM_WallA_InnerCorner9_88/Looks/MI_WallA_01/MI_Floor_01'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_WallA_InnerCorner9_88/SM_WallA_InnerCorner9_88/Looks/MI_WallA_01/MI_Floor_01'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_Floor_01.mdl' (Sub Id: 'MI_Floor_01')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_Floor_01.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BlankMask_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_01_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_01_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_01_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_01_D.png'
      * 'ColorAlbedo' [float4] = '(0.560, 0.560, 0.560, 0.000)'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_01_N.png'
      * 'MainNormalStrenght' [float4] = '(1.000, 1.000, 0.900, 1.000)'
      * 'MainTiling' [float4] = '(1.300, 1.300, 0.000, 0.000)'
      * 'MaskSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BlankMask_M.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallA_01_ORM.png'
      * 'RoughnessMax' [float] = '0.9'
      * 'RoughnessMin' [float] = '0.1'

---

### /World/SortingArea/SM_WallA_InnerCorner9_88/SM_WallA_InnerCorner9_88/Looks/MI_BeamsA_02

* **Prim路径 (Prim Path):**/World/SortingArea/SM_WallA_InnerCorner9_88/SM_WallA_InnerCorner9_88/Looks/MI_BeamsA_02
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_WallA_InnerCorner9_88/SM_WallA_InnerCorner9_88/Looks/MI_BeamsA_02/MI_CeilingA_06b'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_WallA_InnerCorner9_88/SM_WallA_InnerCorner9_88/Looks/MI_BeamsA_02/MI_CeilingA_06b'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_CeilingA_06b.mdl' (Sub Id: 'MI_CeilingA_06b')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_CeilingA_06b.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_D.png'
      * 'ColorAlbedo' [float4] = '(0.035, 0.035, 0.035, 1.000)'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_N.png'
      * 'MainTiling' [float4] = '(1.000, 1.000, 0.000, 1.000)'
      * 'MaskSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_M.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_BeamsA_ORM.png'
      * 'RoughnessMax' [float] = '0.9'
      * 'RoughnessMin' [float] = '0.1'

---

### /World/SortingArea/SM_WallWire_63/SM_WallWire_63/Looks/MI_WallDetails_01

* **Prim路径 (Prim Path):**/World/SortingArea/SM_WallWire_63/SM_WallWire_63/Looks/MI_WallDetails_01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_WallWire_63/SM_WallWire_63/Looks/MI_WallDetails_01/MI_LampCeilingA'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_WallWire_63/SM_WallWire_63/Looks/MI_WallDetails_01/MI_LampCeilingA'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_LampCeilingA.mdl' (Sub Id: 'MI_LampCeilingA')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_LampCeilingA.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallDetails_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallDetails_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallDetails_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallDetails_D.png'
      * 'BaseColor_Tint' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'Desaturation' [float] = '0'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallDetails_N.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallDetails_ORM.png'
      * 'RoughnessMax' [float] = '0.56055'
      * 'RoughnessMin' [float] = '0.1'
      * 'U_Tiling' [float] = '1'
      * 'V_Tiling' [float] = '1'

---

### /World/SortingArea/SM_WallWire_64/SM_WallWire_64/Looks/MI_WallDetails_01

* **Prim路径 (Prim Path):**/World/SortingArea/SM_WallWire_64/SM_WallWire_64/Looks/MI_WallDetails_01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_WallWire_64/SM_WallWire_64/Looks/MI_WallDetails_01/MI_LampCeilingA'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_WallWire_64/SM_WallWire_64/Looks/MI_WallDetails_01/MI_LampCeilingA'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_LampCeilingA.mdl' (Sub Id: 'MI_LampCeilingA')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_LampCeilingA.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallDetails_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallDetails_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallDetails_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallDetails_D.png'
      * 'BaseColor_Tint' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'Desaturation' [float] = '0'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallDetails_N.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallDetails_ORM.png'
      * 'RoughnessMax' [float] = '0.56055'
      * 'RoughnessMin' [float] = '0.1'
      * 'U_Tiling' [float] = '1'
      * 'V_Tiling' [float] = '1'

---

### /World/SortingArea/SM_WallWire_65/SM_WallWire_65/Looks/MI_WallDetails_01

* **Prim路径 (Prim Path):**/World/SortingArea/SM_WallWire_65/SM_WallWire_65/Looks/MI_WallDetails_01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_WallWire_65/SM_WallWire_65/Looks/MI_WallDetails_01/MI_LampCeilingA'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_WallWire_65/SM_WallWire_65/Looks/MI_WallDetails_01/MI_LampCeilingA'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_LampCeilingA.mdl' (Sub Id: 'MI_LampCeilingA')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_LampCeilingA.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallDetails_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallDetails_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallDetails_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallDetails_D.png'
      * 'BaseColor_Tint' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'Desaturation' [float] = '0'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallDetails_N.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallDetails_ORM.png'
      * 'RoughnessMax' [float] = '0.56055'
      * 'RoughnessMin' [float] = '0.1'
      * 'U_Tiling' [float] = '1'
      * 'V_Tiling' [float] = '1'

---

### /World/SortingArea/SM_WallWire_68/SM_WallWire_68/Looks/MI_WallDetails_01

* **Prim路径 (Prim Path):**/World/SortingArea/SM_WallWire_68/SM_WallWire_68/Looks/MI_WallDetails_01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_WallWire_68/SM_WallWire_68/Looks/MI_WallDetails_01/MI_LampCeilingA'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_WallWire_68/SM_WallWire_68/Looks/MI_WallDetails_01/MI_LampCeilingA'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_LampCeilingA.mdl' (Sub Id: 'MI_LampCeilingA')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_LampCeilingA.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallDetails_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallDetails_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallDetails_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallDetails_D.png'
      * 'BaseColor_Tint' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'Desaturation' [float] = '0'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallDetails_N.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallDetails_ORM.png'
      * 'RoughnessMax' [float] = '0.56055'
      * 'RoughnessMin' [float] = '0.1'
      * 'U_Tiling' [float] = '1'
      * 'V_Tiling' [float] = '1'

---

### /World/SortingArea/SM_WallWire_69/SM_WallWire_69/Looks/MI_WallDetails_01

* **Prim路径 (Prim Path):**/World/SortingArea/SM_WallWire_69/SM_WallWire_69/Looks/MI_WallDetails_01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_WallWire_69/SM_WallWire_69/Looks/MI_WallDetails_01/MI_LampCeilingA'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_WallWire_69/SM_WallWire_69/Looks/MI_WallDetails_01/MI_LampCeilingA'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_LampCeilingA.mdl' (Sub Id: 'MI_LampCeilingA')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_LampCeilingA.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallDetails_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallDetails_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallDetails_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallDetails_D.png'
      * 'BaseColor_Tint' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'Desaturation' [float] = '0'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallDetails_N.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallDetails_ORM.png'
      * 'RoughnessMax' [float] = '0.56055'
      * 'RoughnessMin' [float] = '0.1'
      * 'U_Tiling' [float] = '1'
      * 'V_Tiling' [float] = '1'

---

### /World/SortingArea/SM_WallWire_70/SM_WallWire_70/Looks/MI_WallDetails_01

* **Prim路径 (Prim Path):**/World/SortingArea/SM_WallWire_70/SM_WallWire_70/Looks/MI_WallDetails_01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_WallWire_70/SM_WallWire_70/Looks/MI_WallDetails_01/MI_LampCeilingA'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_WallWire_70/SM_WallWire_70/Looks/MI_WallDetails_01/MI_LampCeilingA'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_LampCeilingA.mdl' (Sub Id: 'MI_LampCeilingA')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_LampCeilingA.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallDetails_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallDetails_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallDetails_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallDetails_D.png'
      * 'BaseColor_Tint' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'Desaturation' [float] = '0'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallDetails_N.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallDetails_ORM.png'
      * 'RoughnessMax' [float] = '0.56055'
      * 'RoughnessMin' [float] = '0.1'
      * 'U_Tiling' [float] = '1'
      * 'V_Tiling' [float] = '1'

---

### /World/SortingArea/SM_WallWire_71/SM_WallWire_71/Looks/MI_WallDetails_01

* **Prim路径 (Prim Path):**/World/SortingArea/SM_WallWire_71/SM_WallWire_71/Looks/MI_WallDetails_01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_WallWire_71/SM_WallWire_71/Looks/MI_WallDetails_01/MI_LampCeilingA'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_WallWire_71/SM_WallWire_71/Looks/MI_WallDetails_01/MI_LampCeilingA'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_LampCeilingA.mdl' (Sub Id: 'MI_LampCeilingA')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_LampCeilingA.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallDetails_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallDetails_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallDetails_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallDetails_D.png'
      * 'BaseColor_Tint' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'Desaturation' [float] = '0'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallDetails_N.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallDetails_ORM.png'
      * 'RoughnessMax' [float] = '0.56055'
      * 'RoughnessMin' [float] = '0.1'
      * 'U_Tiling' [float] = '1'
      * 'V_Tiling' [float] = '1'

---

### /World/SortingArea/SM_WallWire_73/SM_WallWire_73/Looks/MI_WallDetails_01

* **Prim路径 (Prim Path):**/World/SortingArea/SM_WallWire_73/SM_WallWire_73/Looks/MI_WallDetails_01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_WallWire_73/SM_WallWire_73/Looks/MI_WallDetails_01/MI_LampCeilingA'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_WallWire_73/SM_WallWire_73/Looks/MI_WallDetails_01/MI_LampCeilingA'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_LampCeilingA.mdl' (Sub Id: 'MI_LampCeilingA')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_LampCeilingA.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallDetails_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallDetails_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallDetails_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallDetails_D.png'
      * 'BaseColor_Tint' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'Desaturation' [float] = '0'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallDetails_N.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallDetails_ORM.png'
      * 'RoughnessMax' [float] = '0.56055'
      * 'RoughnessMin' [float] = '0.1'
      * 'U_Tiling' [float] = '1'
      * 'V_Tiling' [float] = '1'

---

### /World/SortingArea/SM_WallWire_74/SM_WallWire_74/Looks/MI_WallDetails_01

* **Prim路径 (Prim Path):**/World/SortingArea/SM_WallWire_74/SM_WallWire_74/Looks/MI_WallDetails_01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_WallWire_74/SM_WallWire_74/Looks/MI_WallDetails_01/MI_LampCeilingA'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_WallWire_74/SM_WallWire_74/Looks/MI_WallDetails_01/MI_LampCeilingA'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_LampCeilingA.mdl' (Sub Id: 'MI_LampCeilingA')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_LampCeilingA.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallDetails_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallDetails_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallDetails_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallDetails_D.png'
      * 'BaseColor_Tint' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'Desaturation' [float] = '0'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallDetails_N.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_WallDetails_ORM.png'
      * 'RoughnessMax' [float] = '0.56055'
      * 'RoughnessMin' [float] = '0.1'
      * 'U_Tiling' [float] = '1'
      * 'V_Tiling' [float] = '1'

---

### /World/SortingArea/SM_floor27/SM_floor27/Looks/MI_Floor_01

* **Prim路径 (Prim Path):**/World/SortingArea/SM_floor27/SM_floor27/Looks/MI_Floor_01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_floor27/SM_floor27/Looks/MI_Floor_01/MI_Floor_01'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_floor27/SM_floor27/Looks/MI_Floor_01/MI_Floor_01'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_Floor_01.mdl' (Sub Id: 'MI_Floor_01')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_Floor_01.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_Floor_01_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_Floor_01_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_Floor_01_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_Floor_01_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_Floor_01_D.png'
      * 'ColorAlbedo' [float4] = '(0.010, 0.020, 0.030, 0.000)'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_Floor_01_N.png'
      * 'MainNormalStrenght' [float4] = '(1.000, 1.000, 0.900, 1.000)'
      * 'MainTiling' [float4] = '(1.000, 1.000, 0.000, 1.000)'
      * 'MaskSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_Floor_01_M.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_Floor_01_ORM.png'
      * 'RoughnessMax' [float] = '1'
      * 'RoughnessMin' [float] = '0.25'

---

### /World/SortingArea/SM_floor29/SM_floor29/Looks/MI_Floor_01

* **Prim路径 (Prim Path):**/World/SortingArea/SM_floor29/SM_floor29/Looks/MI_Floor_01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_floor29/SM_floor29/Looks/MI_Floor_01/MI_Floor_01'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_floor29/SM_floor29/Looks/MI_Floor_01/MI_Floor_01'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_Floor_01.mdl' (Sub Id: 'MI_Floor_01')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_Floor_01.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_Floor_01_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_Floor_01_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_Floor_01_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_Floor_01_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_Floor_01_D.png'
      * 'ColorAlbedo' [float4] = '(0.010, 0.020, 0.030, 0.000)'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_Floor_01_N.png'
      * 'MainNormalStrenght' [float4] = '(1.000, 1.000, 0.900, 1.000)'
      * 'MainTiling' [float4] = '(1.000, 1.000, 0.000, 1.000)'
      * 'MaskSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_Floor_01_M.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_Floor_01_ORM.png'
      * 'RoughnessMax' [float] = '1'
      * 'RoughnessMin' [float] = '0.25'

---

### /World/SortingArea/SM_floor32/SM_floor32/Looks/MI_Floor_01

* **Prim路径 (Prim Path):**/World/SortingArea/SM_floor32/SM_floor32/Looks/MI_Floor_01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_floor32/SM_floor32/Looks/MI_Floor_01/MI_Floor_01'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_floor32/SM_floor32/Looks/MI_Floor_01/MI_Floor_01'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_Floor_01.mdl' (Sub Id: 'MI_Floor_01')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_Floor_01.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_Floor_01_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_Floor_01_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_Floor_01_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_Floor_01_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_Floor_01_D.png'
      * 'ColorAlbedo' [float4] = '(0.010, 0.020, 0.030, 0.000)'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_Floor_01_N.png'
      * 'MainNormalStrenght' [float4] = '(1.000, 1.000, 0.900, 1.000)'
      * 'MainTiling' [float4] = '(1.000, 1.000, 0.000, 1.000)'
      * 'MaskSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_Floor_01_M.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_Floor_01_ORM.png'
      * 'RoughnessMax' [float] = '1'
      * 'RoughnessMin' [float] = '0.25'

---

### /World/SortingArea/SM_floor33/SM_floor33/Looks/MI_Floor_01

* **Prim路径 (Prim Path):**/World/SortingArea/SM_floor33/SM_floor33/Looks/MI_Floor_01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_floor33/SM_floor33/Looks/MI_Floor_01/MI_Floor_01'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_floor33/SM_floor33/Looks/MI_Floor_01/MI_Floor_01'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_Floor_01.mdl' (Sub Id: 'MI_Floor_01')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_Floor_01.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_Floor_01_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_Floor_01_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_Floor_01_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_Floor_01_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_Floor_01_D.png'
      * 'ColorAlbedo' [float4] = '(0.010, 0.020, 0.030, 0.000)'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_Floor_01_N.png'
      * 'MainNormalStrenght' [float4] = '(1.000, 1.000, 0.900, 1.000)'
      * 'MainTiling' [float4] = '(1.000, 1.000, 0.000, 1.000)'
      * 'MaskSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_Floor_01_M.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_Floor_01_ORM.png'
      * 'RoughnessMax' [float] = '1'
      * 'RoughnessMin' [float] = '0.25'

---

### /World/SortingArea/SM_floor34/SM_floor34/Looks/MI_Floor_01

* **Prim路径 (Prim Path):**/World/SortingArea/SM_floor34/SM_floor34/Looks/MI_Floor_01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_floor34/SM_floor34/Looks/MI_Floor_01/MI_Floor_01'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_floor34/SM_floor34/Looks/MI_Floor_01/MI_Floor_01'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_Floor_01.mdl' (Sub Id: 'MI_Floor_01')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_Floor_01.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_Floor_01_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_Floor_01_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_Floor_01_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_Floor_01_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_Floor_01_D.png'
      * 'ColorAlbedo' [float4] = '(0.010, 0.020, 0.030, 0.000)'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_Floor_01_N.png'
      * 'MainNormalStrenght' [float4] = '(1.000, 1.000, 0.900, 1.000)'
      * 'MainTiling' [float4] = '(1.000, 1.000, 0.000, 1.000)'
      * 'MaskSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_Floor_01_M.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_Floor_01_ORM.png'
      * 'RoughnessMax' [float] = '1'
      * 'RoughnessMin' [float] = '0.25'

---

### /World/SortingArea/SM_floor35/SM_floor35/Looks/MI_Floor_01

* **Prim路径 (Prim Path):**/World/SortingArea/SM_floor35/SM_floor35/Looks/MI_Floor_01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_floor35/SM_floor35/Looks/MI_Floor_01/MI_Floor_01'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_floor35/SM_floor35/Looks/MI_Floor_01/MI_Floor_01'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_Floor_01.mdl' (Sub Id: 'MI_Floor_01')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_Floor_01.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_Floor_01_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_Floor_01_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_Floor_01_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_Floor_01_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_Floor_01_D.png'
      * 'ColorAlbedo' [float4] = '(0.010, 0.020, 0.030, 0.000)'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_Floor_01_N.png'
      * 'MainNormalStrenght' [float4] = '(1.000, 1.000, 0.900, 1.000)'
      * 'MainTiling' [float4] = '(1.000, 1.000, 0.000, 1.000)'
      * 'MaskSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_Floor_01_M.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_Floor_01_ORM.png'
      * 'RoughnessMax' [float] = '1'
      * 'RoughnessMin' [float] = '0.25'

---

### /World/SortingArea/SM_floor36/SM_floor36/Looks/MI_Floor_01

* **Prim路径 (Prim Path):**/World/SortingArea/SM_floor36/SM_floor36/Looks/MI_Floor_01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_floor36/SM_floor36/Looks/MI_Floor_01/MI_Floor_01'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_floor36/SM_floor36/Looks/MI_Floor_01/MI_Floor_01'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_Floor_01.mdl' (Sub Id: 'MI_Floor_01')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_Floor_01.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_Floor_01_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_Floor_01_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_Floor_01_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_Floor_01_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_Floor_01_D.png'
      * 'ColorAlbedo' [float4] = '(0.010, 0.020, 0.030, 0.000)'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_Floor_01_N.png'
      * 'MainNormalStrenght' [float4] = '(1.000, 1.000, 0.900, 1.000)'
      * 'MainTiling' [float4] = '(1.000, 1.000, 0.000, 1.000)'
      * 'MaskSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_Floor_01_M.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_Floor_01_ORM.png'
      * 'RoughnessMax' [float] = '1'
      * 'RoughnessMin' [float] = '0.25'

---

### /World/SortingArea/SM_floor37/SM_floor37/Looks/MI_Floor_01

* **Prim路径 (Prim Path):**/World/SortingArea/SM_floor37/SM_floor37/Looks/MI_Floor_01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_floor37/SM_floor37/Looks/MI_Floor_01/MI_Floor_01'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_floor37/SM_floor37/Looks/MI_Floor_01/MI_Floor_01'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_Floor_01.mdl' (Sub Id: 'MI_Floor_01')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_Floor_01.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_Floor_01_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_Floor_01_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_Floor_01_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_Floor_01_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_Floor_01_D.png'
      * 'ColorAlbedo' [float4] = '(0.010, 0.020, 0.030, 0.000)'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_Floor_01_N.png'
      * 'MainNormalStrenght' [float4] = '(1.000, 1.000, 0.900, 1.000)'
      * 'MainTiling' [float4] = '(1.000, 1.000, 0.000, 1.000)'
      * 'MaskSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_Floor_01_M.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_Floor_01_ORM.png'
      * 'RoughnessMax' [float] = '1'
      * 'RoughnessMin' [float] = '0.25'

---

### /World/SortingArea/SM_floor39/SM_floor39/Looks/MI_Floor_01

* **Prim路径 (Prim Path):**/World/SortingArea/SM_floor39/SM_floor39/Looks/MI_Floor_01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_floor39/SM_floor39/Looks/MI_Floor_01/MI_Floor_01'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_floor39/SM_floor39/Looks/MI_Floor_01/MI_Floor_01'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_Floor_01.mdl' (Sub Id: 'MI_Floor_01')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_Floor_01.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_Floor_01_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_Floor_01_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_Floor_01_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_Floor_01_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_Floor_01_D.png'
      * 'ColorAlbedo' [float4] = '(0.010, 0.020, 0.030, 0.000)'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_Floor_01_N.png'
      * 'MainNormalStrenght' [float4] = '(1.000, 1.000, 0.900, 1.000)'
      * 'MainTiling' [float4] = '(1.000, 1.000, 0.000, 1.000)'
      * 'MaskSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_Floor_01_M.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_Floor_01_ORM.png'
      * 'RoughnessMax' [float] = '1'
      * 'RoughnessMin' [float] = '0.25'

---

### /World/SortingArea/SM_floor44/SM_floor44/Looks/MI_Floor_01

* **Prim路径 (Prim Path):**/World/SortingArea/SM_floor44/SM_floor44/Looks/MI_Floor_01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_floor44/SM_floor44/Looks/MI_Floor_01/MI_Floor_01'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_floor44/SM_floor44/Looks/MI_Floor_01/MI_Floor_01'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_Floor_01.mdl' (Sub Id: 'MI_Floor_01')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_Floor_01.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_Floor_01_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_Floor_01_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_Floor_01_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_Floor_01_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_Floor_01_D.png'
      * 'ColorAlbedo' [float4] = '(0.010, 0.020, 0.030, 0.000)'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_Floor_01_N.png'
      * 'MainNormalStrenght' [float4] = '(1.000, 1.000, 0.900, 1.000)'
      * 'MainTiling' [float4] = '(1.000, 1.000, 0.000, 1.000)'
      * 'MaskSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_Floor_01_M.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_Floor_01_ORM.png'
      * 'RoughnessMax' [float] = '1'
      * 'RoughnessMin' [float] = '0.25'

---

### /World/SortingArea/SM_floor47/SM_floor47/Looks/MI_Floor_01

* **Prim路径 (Prim Path):**/World/SortingArea/SM_floor47/SM_floor47/Looks/MI_Floor_01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_floor47/SM_floor47/Looks/MI_Floor_01/MI_Floor_01'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_floor47/SM_floor47/Looks/MI_Floor_01/MI_Floor_01'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_Floor_01.mdl' (Sub Id: 'MI_Floor_01')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_Floor_01.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_Floor_01_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_Floor_01_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_Floor_01_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_Floor_01_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_Floor_01_D.png'
      * 'ColorAlbedo' [float4] = '(0.010, 0.020, 0.030, 0.000)'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_Floor_01_N.png'
      * 'MainNormalStrenght' [float4] = '(1.000, 1.000, 0.900, 1.000)'
      * 'MainTiling' [float4] = '(1.000, 1.000, 0.000, 1.000)'
      * 'MaskSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_Floor_01_M.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_Floor_01_ORM.png'
      * 'RoughnessMax' [float] = '1'
      * 'RoughnessMin' [float] = '0.25'

---

### /World/SortingArea/SM_floor49/SM_floor49/Looks/MI_Floor_01

* **Prim路径 (Prim Path):**/World/SortingArea/SM_floor49/SM_floor49/Looks/MI_Floor_01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_floor49/SM_floor49/Looks/MI_Floor_01/MI_Floor_01'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_floor49/SM_floor49/Looks/MI_Floor_01/MI_Floor_01'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_Floor_01.mdl' (Sub Id: 'MI_Floor_01')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_Floor_01.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_Floor_01_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_Floor_01_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_Floor_01_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_Floor_01_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_Floor_01_D.png'
      * 'ColorAlbedo' [float4] = '(0.010, 0.020, 0.030, 0.000)'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_Floor_01_N.png'
      * 'MainNormalStrenght' [float4] = '(1.000, 1.000, 0.900, 1.000)'
      * 'MainTiling' [float4] = '(1.000, 1.000, 0.000, 1.000)'
      * 'MaskSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_Floor_01_M.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_Floor_01_ORM.png'
      * 'RoughnessMax' [float] = '1'
      * 'RoughnessMin' [float] = '0.25'

---

### /World/SortingArea/SM_floor51/SM_floor51/Looks/MI_Floor_01

* **Prim路径 (Prim Path):**/World/SortingArea/SM_floor51/SM_floor51/Looks/MI_Floor_01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_floor51/SM_floor51/Looks/MI_Floor_01/MI_Floor_01'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_floor51/SM_floor51/Looks/MI_Floor_01/MI_Floor_01'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_Floor_01.mdl' (Sub Id: 'MI_Floor_01')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_Floor_01.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_Floor_01_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_Floor_01_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_Floor_01_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_Floor_01_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_Floor_01_D.png'
      * 'ColorAlbedo' [float4] = '(0.010, 0.020, 0.030, 0.000)'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_Floor_01_N.png'
      * 'MainNormalStrenght' [float4] = '(1.000, 1.000, 0.900, 1.000)'
      * 'MainTiling' [float4] = '(1.000, 1.000, 0.000, 1.000)'
      * 'MaskSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_Floor_01_M.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_Floor_01_ORM.png'
      * 'RoughnessMax' [float] = '1'
      * 'RoughnessMin' [float] = '0.25'

---

### /World/SortingArea/SM_floor53/SM_floor53/Looks/MI_Floor_01

* **Prim路径 (Prim Path):**/World/SortingArea/SM_floor53/SM_floor53/Looks/MI_Floor_01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_floor53/SM_floor53/Looks/MI_Floor_01/MI_Floor_01'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_floor53/SM_floor53/Looks/MI_Floor_01/MI_Floor_01'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_Floor_01.mdl' (Sub Id: 'MI_Floor_01')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_Floor_01.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_Floor_01_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_Floor_01_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_Floor_01_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_Floor_01_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_Floor_01_D.png'
      * 'ColorAlbedo' [float4] = '(0.010, 0.020, 0.030, 0.000)'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_Floor_01_N.png'
      * 'MainNormalStrenght' [float4] = '(1.000, 1.000, 0.900, 1.000)'
      * 'MainTiling' [float4] = '(1.000, 1.000, 0.000, 1.000)'
      * 'MaskSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_Floor_01_M.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_Floor_01_ORM.png'
      * 'RoughnessMax' [float] = '1'
      * 'RoughnessMin' [float] = '0.25'

---

### /World/SortingArea/SM_floor54/SM_floor54/Looks/MI_Floor_01

* **Prim路径 (Prim Path):**/World/SortingArea/SM_floor54/SM_floor54/Looks/MI_Floor_01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_floor54/SM_floor54/Looks/MI_Floor_01/MI_Floor_01'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_floor54/SM_floor54/Looks/MI_Floor_01/MI_Floor_01'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_Floor_01.mdl' (Sub Id: 'MI_Floor_01')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_Floor_01.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_Floor_01_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_Floor_01_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_Floor_01_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_Floor_01_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_Floor_01_D.png'
      * 'ColorAlbedo' [float4] = '(0.010, 0.020, 0.030, 0.000)'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_Floor_01_N.png'
      * 'MainNormalStrenght' [float4] = '(1.000, 1.000, 0.900, 1.000)'
      * 'MainTiling' [float4] = '(1.000, 1.000, 0.000, 1.000)'
      * 'MaskSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_Floor_01_M.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_Floor_01_ORM.png'
      * 'RoughnessMax' [float] = '1'
      * 'RoughnessMin' [float] = '0.25'

---

### /World/SortingArea/SM_floor55/SM_floor55/Looks/MI_Floor_01

* **Prim路径 (Prim Path):**/World/SortingArea/SM_floor55/SM_floor55/Looks/MI_Floor_01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_floor55/SM_floor55/Looks/MI_Floor_01/MI_Floor_01'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_floor55/SM_floor55/Looks/MI_Floor_01/MI_Floor_01'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_Floor_01.mdl' (Sub Id: 'MI_Floor_01')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_Floor_01.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_Floor_01_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_Floor_01_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_Floor_01_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_Floor_01_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_Floor_01_D.png'
      * 'ColorAlbedo' [float4] = '(0.010, 0.020, 0.030, 0.000)'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_Floor_01_N.png'
      * 'MainNormalStrenght' [float4] = '(1.000, 1.000, 0.900, 1.000)'
      * 'MainTiling' [float4] = '(1.000, 1.000, 0.000, 1.000)'
      * 'MaskSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_Floor_01_M.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_Floor_01_ORM.png'
      * 'RoughnessMax' [float] = '1'
      * 'RoughnessMin' [float] = '0.25'

---

### /World/SortingArea/SM_floor56/SM_floor56/Looks/MI_Floor_01

* **Prim路径 (Prim Path):**/World/SortingArea/SM_floor56/SM_floor56/Looks/MI_Floor_01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_floor56/SM_floor56/Looks/MI_Floor_01/MI_Floor_01'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_floor56/SM_floor56/Looks/MI_Floor_01/MI_Floor_01'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_Floor_01.mdl' (Sub Id: 'MI_Floor_01')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_Floor_01.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_Floor_01_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_Floor_01_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_Floor_01_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_Floor_01_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_Floor_01_D.png'
      * 'ColorAlbedo' [float4] = '(0.010, 0.020, 0.030, 0.000)'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_Floor_01_N.png'
      * 'MainNormalStrenght' [float4] = '(1.000, 1.000, 0.900, 1.000)'
      * 'MainTiling' [float4] = '(1.000, 1.000, 0.000, 1.000)'
      * 'MaskSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_Floor_01_M.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_Floor_01_ORM.png'
      * 'RoughnessMax' [float] = '1'
      * 'RoughnessMin' [float] = '0.25'

---

### /World/SortingArea/SM_floor57/SM_floor57/Looks/MI_Floor_01

* **Prim路径 (Prim Path):**/World/SortingArea/SM_floor57/SM_floor57/Looks/MI_Floor_01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_floor57/SM_floor57/Looks/MI_Floor_01/MI_Floor_01'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_floor57/SM_floor57/Looks/MI_Floor_01/MI_Floor_01'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_Floor_01.mdl' (Sub Id: 'MI_Floor_01')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_Floor_01.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_Floor_01_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_Floor_01_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_Floor_01_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_Floor_01_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_Floor_01_D.png'
      * 'ColorAlbedo' [float4] = '(0.010, 0.020, 0.030, 0.000)'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_Floor_01_N.png'
      * 'MainNormalStrenght' [float4] = '(1.000, 1.000, 0.900, 1.000)'
      * 'MainTiling' [float4] = '(1.000, 1.000, 0.000, 1.000)'
      * 'MaskSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_Floor_01_M.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_Floor_01_ORM.png'
      * 'RoughnessMax' [float] = '1'
      * 'RoughnessMin' [float] = '0.25'

---

### /World/SortingArea/SM_floor58/SM_floor58/Looks/MI_Floor_01

* **Prim路径 (Prim Path):**/World/SortingArea/SM_floor58/SM_floor58/Looks/MI_Floor_01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_floor58/SM_floor58/Looks/MI_Floor_01/MI_Floor_01'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_floor58/SM_floor58/Looks/MI_Floor_01/MI_Floor_01'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_Floor_01.mdl' (Sub Id: 'MI_Floor_01')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_Floor_01.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_Floor_01_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_Floor_01_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_Floor_01_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_Floor_01_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_Floor_01_D.png'
      * 'ColorAlbedo' [float4] = '(0.010, 0.020, 0.030, 0.000)'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_Floor_01_N.png'
      * 'MainNormalStrenght' [float4] = '(1.000, 1.000, 0.900, 1.000)'
      * 'MainTiling' [float4] = '(1.000, 1.000, 0.000, 1.000)'
      * 'MaskSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_Floor_01_M.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_Floor_01_ORM.png'
      * 'RoughnessMax' [float] = '1'
      * 'RoughnessMin' [float] = '0.25'

---

### /World/SortingArea/SM_floor59/SM_floor59/Looks/MI_Floor_01

* **Prim路径 (Prim Path):**/World/SortingArea/SM_floor59/SM_floor59/Looks/MI_Floor_01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_floor59/SM_floor59/Looks/MI_Floor_01/MI_Floor_01'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_floor59/SM_floor59/Looks/MI_Floor_01/MI_Floor_01'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_Floor_01.mdl' (Sub Id: 'MI_Floor_01')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_Floor_01.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_Floor_01_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_Floor_01_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_Floor_01_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_Floor_01_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_Floor_01_D.png'
      * 'ColorAlbedo' [float4] = '(0.010, 0.020, 0.030, 0.000)'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_Floor_01_N.png'
      * 'MainNormalStrenght' [float4] = '(1.000, 1.000, 0.900, 1.000)'
      * 'MainTiling' [float4] = '(1.000, 1.000, 0.000, 1.000)'
      * 'MaskSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_Floor_01_M.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_Floor_01_ORM.png'
      * 'RoughnessMax' [float] = '1'
      * 'RoughnessMin' [float] = '0.25'

---

### /World/SortingArea/SM_floor60/SM_floor60/Looks/MI_Floor_01

* **Prim路径 (Prim Path):**/World/SortingArea/SM_floor60/SM_floor60/Looks/MI_Floor_01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_floor60/SM_floor60/Looks/MI_Floor_01/MI_Floor_01'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_floor60/SM_floor60/Looks/MI_Floor_01/MI_Floor_01'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_Floor_01.mdl' (Sub Id: 'MI_Floor_01')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_Floor_01.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_Floor_01_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_Floor_01_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_Floor_01_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_Floor_01_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_Floor_01_D.png'
      * 'ColorAlbedo' [float4] = '(0.010, 0.020, 0.030, 0.000)'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_Floor_01_N.png'
      * 'MainNormalStrenght' [float4] = '(1.000, 1.000, 0.900, 1.000)'
      * 'MainTiling' [float4] = '(1.000, 1.000, 0.000, 1.000)'
      * 'MaskSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_Floor_01_M.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_Floor_01_ORM.png'
      * 'RoughnessMax' [float] = '1'
      * 'RoughnessMin' [float] = '0.25'

---

### /World/SortingArea/SM_floor61/SM_floor61/Looks/MI_Floor_01

* **Prim路径 (Prim Path):**/World/SortingArea/SM_floor61/SM_floor61/Looks/MI_Floor_01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_floor61/SM_floor61/Looks/MI_Floor_01/MI_Floor_01'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_floor61/SM_floor61/Looks/MI_Floor_01/MI_Floor_01'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_Floor_01.mdl' (Sub Id: 'MI_Floor_01')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_Floor_01.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_Floor_01_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_Floor_01_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_Floor_01_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_Floor_01_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_Floor_01_D.png'
      * 'ColorAlbedo' [float4] = '(0.010, 0.020, 0.030, 0.000)'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_Floor_01_N.png'
      * 'MainNormalStrenght' [float4] = '(1.000, 1.000, 0.900, 1.000)'
      * 'MainTiling' [float4] = '(1.000, 1.000, 0.000, 1.000)'
      * 'MaskSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_Floor_01_M.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_Floor_01_ORM.png'
      * 'RoughnessMax' [float] = '1'
      * 'RoughnessMin' [float] = '0.25'

---

### /World/SortingArea/SM_floor62/SM_floor62/Looks/MI_Floor_01

* **Prim路径 (Prim Path):**/World/SortingArea/SM_floor62/SM_floor62/Looks/MI_Floor_01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_floor62/SM_floor62/Looks/MI_Floor_01/MI_Floor_01'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_floor62/SM_floor62/Looks/MI_Floor_01/MI_Floor_01'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_Floor_01.mdl' (Sub Id: 'MI_Floor_01')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_Floor_01.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_Floor_01_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_Floor_01_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_Floor_01_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_Floor_01_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_Floor_01_D.png'
      * 'ColorAlbedo' [float4] = '(0.010, 0.020, 0.030, 0.000)'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_Floor_01_N.png'
      * 'MainNormalStrenght' [float4] = '(1.000, 1.000, 0.900, 1.000)'
      * 'MainTiling' [float4] = '(1.000, 1.000, 0.000, 1.000)'
      * 'MaskSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_Floor_01_M.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_Floor_01_ORM.png'
      * 'RoughnessMax' [float] = '1'
      * 'RoughnessMin' [float] = '0.25'

---

### /World/SortingArea/SM_floor63/SM_floor63/Looks/MI_Floor_01

* **Prim路径 (Prim Path):**/World/SortingArea/SM_floor63/SM_floor63/Looks/MI_Floor_01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/SM_floor63/SM_floor63/Looks/MI_Floor_01/MI_Floor_01'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/SM_floor63/SM_floor63/Looks/MI_Floor_01/MI_Floor_01'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_Floor_01.mdl' (Sub Id: 'MI_Floor_01')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_Floor_01.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_Floor_01_D.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_Floor_01_M.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_Floor_01_N.png'
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_Floor_01_ORM.png'
    * Inputs:
      * 'AlbedoTexture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_Floor_01_D.png'
      * 'ColorAlbedo' [float4] = '(0.010, 0.020, 0.030, 0.000)'
      * 'MainNormalInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_Floor_01_N.png'
      * 'MainNormalStrenght' [float4] = '(1.000, 1.000, 0.900, 1.000)'
      * 'MainTiling' [float4] = '(1.000, 1.000, 0.000, 1.000)'
      * 'MaskSelection' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_Floor_01_M.png'
      * 'MergeMapInput' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/T_Floor_01_ORM.png'
      * 'RoughnessMax' [float] = '1'
      * 'RoughnessMin' [float] = '0.25'

---

### /World/SortingArea/S_Barcode886/S_Barcode886/Looks/MI_Barcode_0001

* **Prim路径 (Prim Path):**/World/SortingArea/S_Barcode886/S_Barcode886/Looks/MI_Barcode_0001
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/SortingArea/S_Barcode886/S_Barcode886/Looks/MI_Barcode_0001/MI_Barcode_0001'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/SortingArea/S_Barcode886/S_Barcode886/Looks/MI_Barcode_0001/MI_Barcode_0001'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_Barcode_0001.mdl' (Sub Id: 'MI_Barcode_0001')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/MI_Barcode_0001.mdl'
    * 纹理引用 (Texture Assets):
      * '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/0001.png'
    * Inputs:
      * 'BaseColor_Texture' [asset] = '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/4.5/Isaac/Environments/Simple_Warehouse/Materials/Textures/0001.png'
      * 'BaseColor_Tint' [float4] = '(0.550, 0.550, 0.550, 1.000)'
      * 'Metallic' [float] = '0.05'
      * 'Roughness' [float] = '0.3'

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

### /World/StackedCarton/Materials/Material_1

* **Prim路径 (Prim Path):**/World/StackedCarton/Materials/Material_1
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/StackedCarton/Materials/Material_1/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/StackedCarton/Materials/Material_1/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f]
        * Connected: '/World/StackedCarton/Materials/Material_1/tex_base.outputs:rgb' @ '/World/StackedCarton/Materials/Material_1/tex_base'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/Material_1_baseColor_cutoff173.png'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(1.000, 1.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'opacity' [float]
        * Connected: '/World/StackedCarton/Materials/Material_1/tex_base.outputs:a' @ '/World/StackedCarton/Materials/Material_1/tex_base'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/Material_1_baseColor_cutoff173.png'
      * 'roughness' [float] = '0.6'
    * '/World/StackedCarton/Materials/Material_1/tex_base' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/Material_1_baseColor_cutoff173.png'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'file' [asset] = '0/Material_1_baseColor_cutoff173.png'
      * 'st' [float2]
        * Connected: '/World/StackedCarton/Materials/Material_1/uvset0.outputs:result' @ '/World/StackedCarton/Materials/Material_1/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/StackedCarton/Materials/Material_1/uvset0' (ID: 'UsdPrimvarReader_float2')
    * Implementation: 'id'

---

### /World/Plastic_Crate/Materials/Crate

* **Prim路径 (Prim Path):**/World/Plastic_Crate/Materials/Crate
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/Plastic_Crate/Materials/Crate/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Plastic_Crate/Materials/Crate/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f]
        * Connected: '/World/Plastic_Crate/Materials/Crate/tex_base.outputs:rgb' @ '/World/Plastic_Crate/Materials/Crate/tex_base'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/Crate_baseColor.jpg'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float]
        * Connected: '/World/Plastic_Crate/Materials/Crate/tex_metallic.outputs:r' @ '/World/Plastic_Crate/Materials/Crate/tex_metallic'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/Crate_metallicRoughness_metal_scale0.jpg'
      * 'normal' [normal3f]
        * Connected: '/World/Plastic_Crate/Materials/Crate/tex_normal.outputs:rgb' @ '/World/Plastic_Crate/Materials/Crate/tex_normal'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/Crate_normal.jpg'
      * 'occlusion' [float] = '1'
      * 'roughness' [float]
        * Connected: '/World/Plastic_Crate/Materials/Crate/tex_roughness.outputs:r' @ '/World/Plastic_Crate/Materials/Crate/tex_roughness'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/Crate_metallicRoughness_rough.jpg'
    * '/World/Plastic_Crate/Materials/Crate/tex_base' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/Crate_baseColor.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'file' [asset] = '0/Crate_baseColor.jpg'
      * 'st' [float2]
        * Connected: '/World/Plastic_Crate/Materials/Crate/uvset0.outputs:result' @ '/World/Plastic_Crate/Materials/Crate/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/Plastic_Crate/Materials/Crate/uvset0' (ID: 'UsdPrimvarReader_float2')
    * Implementation: 'id'
    * '/World/Plastic_Crate/Materials/Crate/tex_metallic' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/Crate_metallicRoughness_metal_scale0.jpg'
    * Inputs:
      * 'fallback' [float4] = '(0.000, 0.000, 0.000, 1.000)'
      * 'file' [asset] = '0/Crate_metallicRoughness_metal_scale0.jpg'
      * 'st' [float2]
        * Connected: '/World/Plastic_Crate/Materials/Crate/uvset0.outputs:result' @ '/World/Plastic_Crate/Materials/Crate/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/Plastic_Crate/Materials/Crate/tex_normal' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/Crate_normal.jpg'
    * Inputs:
      * 'bias' [float4] = '(-1.000, -1.000, -1.000, -1.000)'
      * 'fallback' [float4] = '(0.000, 0.000, 1.000, 1.000)'
      * 'file' [asset] = '0/Crate_normal.jpg'
      * 'scale' [float4] = '(2.000, 2.000, 2.000, 2.000)'
      * 'st' [float2]
        * Connected: '/World/Plastic_Crate/Materials/Crate/uvset0.outputs:result' @ '/World/Plastic_Crate/Materials/Crate/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/Plastic_Crate/Materials/Crate/tex_roughness' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/Crate_metallicRoughness_rough.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 0.000, 0.000, 1.000)'
      * 'file' [asset] = '0/Crate_metallicRoughness_rough.jpg'
      * 'st' [float2]
        * Connected: '/World/Plastic_Crate/Materials/Crate/uvset0.outputs:result' @ '/World/Plastic_Crate/Materials/Crate/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'

---

### /World/model_forklift/materials/mat_0

* **Prim路径 (Prim Path):**/World/model_forklift/materials/mat_0
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/model_forklift/materials/mat_0/PBRShader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/model_forklift/materials/mat_0/PBRShader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'clearcoat' [float] = '0.05'
      * 'clearcoatRoughness' [float] = '0.05'
      * 'diffuseColor' [color3f] = '(0.939, 0.965, 1.000)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'ior' [float] = '1'
      * 'opacity' [float] = '1'
      * 'roughness' [float] = '0.5'
      * 'specularColor' [color3f] = '(0.000, 0.000, 0.000)'

---

### /World/model_forklift/materials/mat_130

* **Prim路径 (Prim Path):**/World/model_forklift/materials/mat_130
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/model_forklift/materials/mat_130/PBRShader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/model_forklift/materials/mat_130/PBRShader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'clearcoat' [float] = '0.15'
      * 'clearcoatRoughness' [float] = '0.05'
      * 'diffuseColor' [color3f]
        * Connected: '/World/model_forklift/materials/mat_130/diffuseTexture.outputs:rgb' @ '/World/model_forklift/materials/mat_130/diffuseTexture'
          * Shader ID: 'UsdUVTexture'
          * Texture: './img/73c8128d0eedec3594256b6f73d56e4f.png'
      * 'emissiveColor' [color3f] = '(1.000, 0.371, 0.000)'
      * 'ior' [float] = '1'
      * 'metallic' [float] = '0.1'
      * 'opacity' [float] = '1'
      * 'roughness' [float] = '0.15'
      * 'specularColor' [color3f] = '(0.000, 0.000, 0.000)'
    * '/World/model_forklift/materials/mat_130/diffuseTexture' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * './img/73c8128d0eedec3594256b6f73d56e4f.png'
    * Inputs:
      * 'file' [asset] = './img/73c8128d0eedec3594256b6f73d56e4f.png'
      * 'st' [float2]
        * Connected: '/World/model_forklift/materials/mat_130/transform_st.outputs:result' @ '/World/model_forklift/materials/mat_130/transform_st'
          * Shader ID: 'UsdTransform2d'
    * '/World/model_forklift/materials/mat_130/transform_st' (ID: 'UsdTransform2d')
    * Implementation: 'id'
    * Inputs:
      * 'in' [float2]
        * Connected: '/World/model_forklift/materials/mat_130/stReader.outputs:result' @ '/World/model_forklift/materials/mat_130/stReader'
          * Shader ID: 'UsdPrimvarReader_float2'
      * 'rotation' [float] = '0'
      * 'scale' [float2] = '(39.370, 39.370)'
      * 'translation' [float2] = '(0.000, 0.000)'
    * '/World/model_forklift/materials/mat_130/stReader' (ID: 'UsdPrimvarReader_float2')
    * Implementation: 'id'
    * Inputs:
      * 'varname' [string]
        * Connected: '/World/model_forklift/materials/mat_130.inputs:frame:stPrimvarName' @ '/World/model_forklift/materials/mat_130'

---

### /World/model_forklift/materials/mat_138

* **Prim路径 (Prim Path):**/World/model_forklift/materials/mat_138
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/model_forklift/materials/mat_138/PBRShader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/model_forklift/materials/mat_138/PBRShader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'clearcoat' [float] = '0.1'
      * 'clearcoatRoughness' [float] = '0.05'
      * 'diffuseColor' [color3f]
        * Connected: '/World/model_forklift/materials/mat_138/diffuseTexture.outputs:rgb' @ '/World/model_forklift/materials/mat_138/diffuseTexture'
          * Shader ID: 'UsdUVTexture'
          * Texture: './img/7012e5a5c0e57b119e31b46ce09d2564.png'
      * 'emissiveColor' [color3f] = '(1.000, 0.000, 0.000)'
      * 'ior' [float] = '1'
      * 'metallic' [float] = '0.1'
      * 'opacity' [float] = '1'
      * 'roughness' [float] = '0.15'
      * 'specularColor' [color3f] = '(0.000, 0.000, 0.000)'
    * '/World/model_forklift/materials/mat_138/diffuseTexture' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * './img/7012e5a5c0e57b119e31b46ce09d2564.png'
    * Inputs:
      * 'file' [asset] = './img/7012e5a5c0e57b119e31b46ce09d2564.png'
      * 'st' [float2]
        * Connected: '/World/model_forklift/materials/mat_138/transform_st.outputs:result' @ '/World/model_forklift/materials/mat_138/transform_st'
          * Shader ID: 'UsdTransform2d'
    * '/World/model_forklift/materials/mat_138/transform_st' (ID: 'UsdTransform2d')
    * Implementation: 'id'
    * Inputs:
      * 'in' [float2]
        * Connected: '/World/model_forklift/materials/mat_138/stReader.outputs:result' @ '/World/model_forklift/materials/mat_138/stReader'
          * Shader ID: 'UsdPrimvarReader_float2'
      * 'rotation' [float] = '0'
      * 'scale' [float2] = '(39.370, 39.370)'
      * 'translation' [float2] = '(0.000, 0.000)'
    * '/World/model_forklift/materials/mat_138/stReader' (ID: 'UsdPrimvarReader_float2')
    * Implementation: 'id'
    * Inputs:
      * 'varname' [string]
        * Connected: '/World/model_forklift/materials/mat_138.inputs:frame:stPrimvarName' @ '/World/model_forklift/materials/mat_138'

---

### /World/model_forklift/materials/mat_88

* **Prim路径 (Prim Path):**/World/model_forklift/materials/mat_88
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/model_forklift/materials/mat_88/PBRShader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/model_forklift/materials/mat_88/PBRShader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'clearcoat' [float] = '0.1'
      * 'clearcoatRoughness' [float] = '0.05'
      * 'diffuseColor' [color3f]
        * Connected: '/World/model_forklift/materials/mat_88/diffuseTexture.outputs:rgb' @ '/World/model_forklift/materials/mat_88/diffuseTexture'
          * Shader ID: 'UsdUVTexture'
          * Texture: './img/b4f355beed9aea1c0908de492d5731e8.png'
      * 'emissiveColor' [color3f] = '(1.000, 1.000, 1.000)'
      * 'ior' [float] = '1'
      * 'metallic' [float] = '0.1'
      * 'opacity' [float] = '1'
      * 'roughness' [float] = '0.15'
      * 'specularColor' [color3f] = '(0.000, 0.000, 0.000)'
    * '/World/model_forklift/materials/mat_88/diffuseTexture' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * './img/b4f355beed9aea1c0908de492d5731e8.png'
    * Inputs:
      * 'file' [asset] = './img/b4f355beed9aea1c0908de492d5731e8.png'
      * 'st' [float2]
        * Connected: '/World/model_forklift/materials/mat_88/transform_st.outputs:result' @ '/World/model_forklift/materials/mat_88/transform_st'
          * Shader ID: 'UsdTransform2d'
    * '/World/model_forklift/materials/mat_88/transform_st' (ID: 'UsdTransform2d')
    * Implementation: 'id'
    * Inputs:
      * 'in' [float2]
        * Connected: '/World/model_forklift/materials/mat_88/stReader.outputs:result' @ '/World/model_forklift/materials/mat_88/stReader'
          * Shader ID: 'UsdPrimvarReader_float2'
      * 'rotation' [float] = '0'
      * 'scale' [float2] = '(39.370, 39.370)'
      * 'translation' [float2] = '(0.000, 0.000)'
    * '/World/model_forklift/materials/mat_88/stReader' (ID: 'UsdPrimvarReader_float2')
    * Implementation: 'id'
    * Inputs:
      * 'varname' [string]
        * Connected: '/World/model_forklift/materials/mat_88.inputs:frame:stPrimvarName' @ '/World/model_forklift/materials/mat_88'

---

### /World/model_forklift/materials/mat_127

* **Prim路径 (Prim Path):**/World/model_forklift/materials/mat_127
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/model_forklift/materials/mat_127/PBRShader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/model_forklift/materials/mat_127/PBRShader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'clearcoat' [float] = '0.2'
      * 'clearcoatRoughness' [float] = '0.05'
      * 'diffuseColor' [color3f] = '(0.125, 0.127, 0.141)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'ior' [float] = '1'
      * 'metallic' [float] = '0.15'
      * 'opacity' [float] = '1'
      * 'roughness' [float] = '0.3'
      * 'specularColor' [color3f] = '(0.000, 0.000, 0.000)'

---

### /World/model_forklift/materials/mat_77

* **Prim路径 (Prim Path):**/World/model_forklift/materials/mat_77
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/model_forklift/materials/mat_77/PBRShader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/model_forklift/materials/mat_77/PBRShader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'clearcoat' [float] = '0.2'
      * 'clearcoatRoughness' [float] = '0.05'
      * 'diffuseColor' [color3f] = '(0.032, 0.032, 0.032)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'ior' [float] = '1'
      * 'metallic' [float] = '0.15'
      * 'opacity' [float] = '1'
      * 'roughness' [float] = '0.3'
      * 'specularColor' [color3f] = '(0.000, 0.000, 0.000)'

---

### /World/model_forklift/materials/mat_104

* **Prim路径 (Prim Path):**/World/model_forklift/materials/mat_104
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/model_forklift/materials/mat_104/PBRShader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/model_forklift/materials/mat_104/PBRShader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'clearcoat' [float] = '0.2'
      * 'clearcoatRoughness' [float] = '0.05'
      * 'diffuseColor' [color3f]
        * Connected: '/World/model_forklift/materials/mat_104/diffuseTexture.outputs:rgb' @ '/World/model_forklift/materials/mat_104/diffuseTexture'
          * Shader ID: 'UsdUVTexture'
          * Texture: './img/6ee577008303a3c264f0e35514bec78f.png'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'ior' [float] = '1'
      * 'metallic' [float] = '0.2'
      * 'opacity' [float] = '1'
      * 'roughness' [float] = '0.3'
      * 'specularColor' [color3f] = '(0.000, 0.000, 0.000)'
    * '/World/model_forklift/materials/mat_104/diffuseTexture' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * './img/6ee577008303a3c264f0e35514bec78f.png'
    * Inputs:
      * 'file' [asset] = './img/6ee577008303a3c264f0e35514bec78f.png'
      * 'st' [float2]
        * Connected: '/World/model_forklift/materials/mat_104/transform_st.outputs:result' @ '/World/model_forklift/materials/mat_104/transform_st'
          * Shader ID: 'UsdTransform2d'
    * '/World/model_forklift/materials/mat_104/transform_st' (ID: 'UsdTransform2d')
    * Implementation: 'id'
    * Inputs:
      * 'in' [float2]
        * Connected: '/World/model_forklift/materials/mat_104/stReader.outputs:result' @ '/World/model_forklift/materials/mat_104/stReader'
          * Shader ID: 'UsdPrimvarReader_float2'
      * 'rotation' [float] = '0'
      * 'scale' [float2] = '(39.370, 39.370)'
      * 'translation' [float2] = '(0.000, 0.000)'
    * '/World/model_forklift/materials/mat_104/stReader' (ID: 'UsdPrimvarReader_float2')
    * Implementation: 'id'
    * Inputs:
      * 'varname' [string]
        * Connected: '/World/model_forklift/materials/mat_104.inputs:frame:stPrimvarName' @ '/World/model_forklift/materials/mat_104'

---

### /World/model_forklift/materials/mat_123

* **Prim路径 (Prim Path):**/World/model_forklift/materials/mat_123
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/model_forklift/materials/mat_123/PBRShader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/model_forklift/materials/mat_123/PBRShader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'clearcoat' [float] = '0.15'
      * 'clearcoatRoughness' [float] = '0.05'
      * 'diffuseColor' [color3f]
        * Connected: '/World/model_forklift/materials/mat_123/diffuseTexture.outputs:rgb' @ '/World/model_forklift/materials/mat_123/diffuseTexture'
          * Shader ID: 'UsdUVTexture'
          * Texture: './img/8b8645cea4a1caf14ce4855afa533f45.png'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'ior' [float] = '1'
      * 'metallic' [float] = '0.15'
      * 'opacity' [float] = '1'
      * 'roughness' [float] = '0.3'
      * 'specularColor' [color3f] = '(0.000, 0.000, 0.000)'
    * '/World/model_forklift/materials/mat_123/diffuseTexture' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * './img/8b8645cea4a1caf14ce4855afa533f45.png'
    * Inputs:
      * 'file' [asset] = './img/8b8645cea4a1caf14ce4855afa533f45.png'
      * 'st' [float2]
        * Connected: '/World/model_forklift/materials/mat_123/transform_st.outputs:result' @ '/World/model_forklift/materials/mat_123/transform_st'
          * Shader ID: 'UsdTransform2d'
    * '/World/model_forklift/materials/mat_123/transform_st' (ID: 'UsdTransform2d')
    * Implementation: 'id'
    * Inputs:
      * 'in' [float2]
        * Connected: '/World/model_forklift/materials/mat_123/stReader.outputs:result' @ '/World/model_forklift/materials/mat_123/stReader'
          * Shader ID: 'UsdPrimvarReader_float2'
      * 'rotation' [float] = '0'
      * 'scale' [float2] = '(39.370, 39.370)'
      * 'translation' [float2] = '(0.000, 0.000)'
    * '/World/model_forklift/materials/mat_123/stReader' (ID: 'UsdPrimvarReader_float2')
    * Implementation: 'id'
    * Inputs:
      * 'varname' [string]
        * Connected: '/World/model_forklift/materials/mat_123.inputs:frame:stPrimvarName' @ '/World/model_forklift/materials/mat_123'

---

### /World/model_forklift/materials/mat_119

* **Prim路径 (Prim Path):**/World/model_forklift/materials/mat_119
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/model_forklift/materials/mat_119/PBRShader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/model_forklift/materials/mat_119/PBRShader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'clearcoat' [float] = '0.15'
      * 'clearcoatRoughness' [float] = '0.05'
      * 'diffuseColor' [color3f]
        * Connected: '/World/model_forklift/materials/mat_119/diffuseTexture.outputs:rgb' @ '/World/model_forklift/materials/mat_119/diffuseTexture'
          * Shader ID: 'UsdUVTexture'
          * Texture: './img/acb12c1631ba68d4722ef4381db65808.png'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'ior' [float] = '1'
      * 'metallic' [float] = '0.15'
      * 'opacity' [float] = '1'
      * 'roughness' [float] = '0.3'
      * 'specularColor' [color3f] = '(0.000, 0.000, 0.000)'
    * '/World/model_forklift/materials/mat_119/diffuseTexture' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * './img/acb12c1631ba68d4722ef4381db65808.png'
    * Inputs:
      * 'file' [asset] = './img/acb12c1631ba68d4722ef4381db65808.png'
      * 'st' [float2]
        * Connected: '/World/model_forklift/materials/mat_119/transform_st.outputs:result' @ '/World/model_forklift/materials/mat_119/transform_st'
          * Shader ID: 'UsdTransform2d'
    * '/World/model_forklift/materials/mat_119/transform_st' (ID: 'UsdTransform2d')
    * Implementation: 'id'
    * Inputs:
      * 'in' [float2]
        * Connected: '/World/model_forklift/materials/mat_119/stReader.outputs:result' @ '/World/model_forklift/materials/mat_119/stReader'
          * Shader ID: 'UsdPrimvarReader_float2'
      * 'rotation' [float] = '0'
      * 'scale' [float2] = '(39.370, 39.370)'
      * 'translation' [float2] = '(0.000, 0.000)'
    * '/World/model_forklift/materials/mat_119/stReader' (ID: 'UsdPrimvarReader_float2')
    * Implementation: 'id'
    * Inputs:
      * 'varname' [string]
        * Connected: '/World/model_forklift/materials/mat_119.inputs:frame:stPrimvarName' @ '/World/model_forklift/materials/mat_119'

---

### /World/model_forklift/materials/mat_116

* **Prim路径 (Prim Path):**/World/model_forklift/materials/mat_116
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/model_forklift/materials/mat_116/PBRShader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/model_forklift/materials/mat_116/PBRShader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'clearcoat' [float] = '0.15'
      * 'clearcoatRoughness' [float] = '0.05'
      * 'diffuseColor' [color3f] = '(0.051, 0.051, 0.051)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'ior' [float] = '1'
      * 'metallic' [float] = '0.15'
      * 'opacity' [float] = '1'
      * 'roughness' [float] = '0.3'
      * 'specularColor' [color3f] = '(0.000, 0.000, 0.000)'

---

### /World/model_forklift/materials/mat_143

* **Prim路径 (Prim Path):**/World/model_forklift/materials/mat_143
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/model_forklift/materials/mat_143/PBRShader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/model_forklift/materials/mat_143/PBRShader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'clearcoat' [float] = '0.2'
      * 'clearcoatRoughness' [float] = '0.05'
      * 'diffuseColor' [color3f] = '(0.093, 0.093, 0.093)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'ior' [float] = '1'
      * 'metallic' [float] = '0.15'
      * 'opacity' [float] = '1'
      * 'roughness' [float] = '0.25'
      * 'specularColor' [color3f] = '(0.000, 0.000, 0.000)'

---

### /World/model_forklift/materials/mat_112

* **Prim路径 (Prim Path):**/World/model_forklift/materials/mat_112
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/model_forklift/materials/mat_112/PBRShader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/model_forklift/materials/mat_112/PBRShader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'clearcoat' [float] = '0.15'
      * 'clearcoatRoughness' [float] = '0.05'
      * 'diffuseColor' [color3f]
        * Connected: '/World/model_forklift/materials/mat_112/diffuseTexture.outputs:rgb' @ '/World/model_forklift/materials/mat_112/diffuseTexture'
          * Shader ID: 'UsdUVTexture'
          * Texture: './img/dc9c76a4e45481606a82131fba383206.png'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'ior' [float] = '1'
      * 'metallic' [float] = '0.1'
      * 'opacity' [float] = '1'
      * 'roughness' [float] = '0.25'
      * 'specularColor' [color3f] = '(0.000, 0.000, 0.000)'
    * '/World/model_forklift/materials/mat_112/diffuseTexture' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * './img/dc9c76a4e45481606a82131fba383206.png'
    * Inputs:
      * 'file' [asset] = './img/dc9c76a4e45481606a82131fba383206.png'
      * 'st' [float2]
        * Connected: '/World/model_forklift/materials/mat_112/transform_st.outputs:result' @ '/World/model_forklift/materials/mat_112/transform_st'
          * Shader ID: 'UsdTransform2d'
    * '/World/model_forklift/materials/mat_112/transform_st' (ID: 'UsdTransform2d')
    * Implementation: 'id'
    * Inputs:
      * 'in' [float2]
        * Connected: '/World/model_forklift/materials/mat_112/stReader.outputs:result' @ '/World/model_forklift/materials/mat_112/stReader'
          * Shader ID: 'UsdPrimvarReader_float2'
      * 'rotation' [float] = '0'
      * 'scale' [float2] = '(39.370, 39.370)'
      * 'translation' [float2] = '(0.000, 0.000)'
    * '/World/model_forklift/materials/mat_112/stReader' (ID: 'UsdPrimvarReader_float2')
    * Implementation: 'id'
    * Inputs:
      * 'varname' [string]
        * Connected: '/World/model_forklift/materials/mat_112.inputs:frame:stPrimvarName' @ '/World/model_forklift/materials/mat_112'

---

### /World/model_forklift/materials/mat_84

* **Prim路径 (Prim Path):**/World/model_forklift/materials/mat_84
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/model_forklift/materials/mat_84/PBRShader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/model_forklift/materials/mat_84/PBRShader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'clearcoat' [float] = '0.15'
      * 'clearcoatRoughness' [float] = '0.05'
      * 'diffuseColor' [color3f]
        * Connected: '/World/model_forklift/materials/mat_84/diffuseTexture.outputs:rgb' @ '/World/model_forklift/materials/mat_84/diffuseTexture'
          * Shader ID: 'UsdUVTexture'
          * Texture: './img/58f1910b7464e1374dd30eb65a5bf8e2.png'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'ior' [float] = '1'
      * 'metallic' [float] = '0.1'
      * 'opacity' [float] = '1'
      * 'roughness' [float] = '0.3'
      * 'specularColor' [color3f] = '(0.000, 0.000, 0.000)'
    * '/World/model_forklift/materials/mat_84/diffuseTexture' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * './img/58f1910b7464e1374dd30eb65a5bf8e2.png'
    * Inputs:
      * 'file' [asset] = './img/58f1910b7464e1374dd30eb65a5bf8e2.png'
      * 'st' [float2]
        * Connected: '/World/model_forklift/materials/mat_84/transform_st.outputs:result' @ '/World/model_forklift/materials/mat_84/transform_st'
          * Shader ID: 'UsdTransform2d'
    * '/World/model_forklift/materials/mat_84/transform_st' (ID: 'UsdTransform2d')
    * Implementation: 'id'
    * Inputs:
      * 'in' [float2]
        * Connected: '/World/model_forklift/materials/mat_84/stReader.outputs:result' @ '/World/model_forklift/materials/mat_84/stReader'
          * Shader ID: 'UsdPrimvarReader_float2'
      * 'rotation' [float] = '0'
      * 'scale' [float2] = '(39.370, 39.370)'
      * 'translation' [float2] = '(0.000, 0.000)'
    * '/World/model_forklift/materials/mat_84/stReader' (ID: 'UsdPrimvarReader_float2')
    * Implementation: 'id'
    * Inputs:
      * 'varname' [string]
        * Connected: '/World/model_forklift/materials/mat_84.inputs:frame:stPrimvarName' @ '/World/model_forklift/materials/mat_84'

---

### /World/model_forklift/materials/mat_74

* **Prim路径 (Prim Path):**/World/model_forklift/materials/mat_74
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/model_forklift/materials/mat_74/PBRShader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/model_forklift/materials/mat_74/PBRShader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'clearcoat' [float] = '0.2'
      * 'clearcoatRoughness' [float] = '0.05'
      * 'diffuseColor' [color3f] = '(0.081, 0.081, 0.081)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'ior' [float] = '1'
      * 'metallic' [float] = '0.1'
      * 'opacity' [float] = '1'
      * 'roughness' [float] = '0.3'
      * 'specularColor' [color3f] = '(0.000, 0.000, 0.000)'

---

### /World/model_forklift/materials/mat_100

* **Prim路径 (Prim Path):**/World/model_forklift/materials/mat_100
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/model_forklift/materials/mat_100/PBRShader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/model_forklift/materials/mat_100/PBRShader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'clearcoat' [float] = '0.2'
      * 'clearcoatRoughness' [float] = '0.05'
      * 'diffuseColor' [color3f]
        * Connected: '/World/model_forklift/materials/mat_100/diffuseTexture.outputs:rgb' @ '/World/model_forklift/materials/mat_100/diffuseTexture'
          * Shader ID: 'UsdUVTexture'
          * Texture: './img/b8d26289158ec752eb29a4126deec547.png'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'ior' [float] = '1'
      * 'metallic' [float] = '0.1'
      * 'opacity' [float] = '1'
      * 'roughness' [float] = '0.3'
      * 'specularColor' [color3f] = '(0.000, 0.000, 0.000)'
    * '/World/model_forklift/materials/mat_100/diffuseTexture' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * './img/b8d26289158ec752eb29a4126deec547.png'
    * Inputs:
      * 'file' [asset] = './img/b8d26289158ec752eb29a4126deec547.png'
      * 'st' [float2]
        * Connected: '/World/model_forklift/materials/mat_100/transform_st.outputs:result' @ '/World/model_forklift/materials/mat_100/transform_st'
          * Shader ID: 'UsdTransform2d'
    * '/World/model_forklift/materials/mat_100/transform_st' (ID: 'UsdTransform2d')
    * Implementation: 'id'
    * Inputs:
      * 'in' [float2]
        * Connected: '/World/model_forklift/materials/mat_100/stReader.outputs:result' @ '/World/model_forklift/materials/mat_100/stReader'
          * Shader ID: 'UsdPrimvarReader_float2'
      * 'rotation' [float] = '0'
      * 'scale' [float2] = '(39.370, 39.370)'
      * 'translation' [float2] = '(0.000, 0.000)'
    * '/World/model_forklift/materials/mat_100/stReader' (ID: 'UsdPrimvarReader_float2')
    * Implementation: 'id'
    * Inputs:
      * 'varname' [string]
        * Connected: '/World/model_forklift/materials/mat_100.inputs:frame:stPrimvarName' @ '/World/model_forklift/materials/mat_100'

---

### /World/model_forklift/materials/mat_142

* **Prim路径 (Prim Path):**/World/model_forklift/materials/mat_142
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/model_forklift/materials/mat_142/PBRShader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/model_forklift/materials/mat_142/PBRShader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'clearcoat' [float] = '0.2'
      * 'clearcoatRoughness' [float] = '0.05'
      * 'diffuseColor' [color3f] = '(0.042, 0.042, 0.042)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'ior' [float] = '1'
      * 'metallic' [float] = '0.2'
      * 'opacity' [float] = '1'
      * 'roughness' [float] = '0.3'
      * 'specularColor' [color3f] = '(0.000, 0.000, 0.000)'

---

### /World/model_forklift/materials/mat_92

* **Prim路径 (Prim Path):**/World/model_forklift/materials/mat_92
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/model_forklift/materials/mat_92/PBRShader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/model_forklift/materials/mat_92/PBRShader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'clearcoat' [float] = '0.15'
      * 'clearcoatRoughness' [float] = '0.05'
      * 'diffuseColor' [color3f]
        * Connected: '/World/model_forklift/materials/mat_92/diffuseTexture.outputs:rgb' @ '/World/model_forklift/materials/mat_92/diffuseTexture'
          * Shader ID: 'UsdUVTexture'
          * Texture: './img/62a898f4d8d6e046b1cf3f3ff7f954e7.png'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'ior' [float] = '1'
      * 'metallic' [float] = '0.05'
      * 'opacity' [float] = '1'
      * 'roughness' [float] = '0.3'
      * 'specularColor' [color3f] = '(0.000, 0.000, 0.000)'
    * '/World/model_forklift/materials/mat_92/diffuseTexture' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * './img/62a898f4d8d6e046b1cf3f3ff7f954e7.png'
    * Inputs:
      * 'file' [asset] = './img/62a898f4d8d6e046b1cf3f3ff7f954e7.png'
      * 'st' [float2]
        * Connected: '/World/model_forklift/materials/mat_92/transform_st.outputs:result' @ '/World/model_forklift/materials/mat_92/transform_st'
          * Shader ID: 'UsdTransform2d'
    * '/World/model_forklift/materials/mat_92/transform_st' (ID: 'UsdTransform2d')
    * Implementation: 'id'
    * Inputs:
      * 'in' [float2]
        * Connected: '/World/model_forklift/materials/mat_92/stReader.outputs:result' @ '/World/model_forklift/materials/mat_92/stReader'
          * Shader ID: 'UsdPrimvarReader_float2'
      * 'rotation' [float] = '0'
      * 'scale' [float2] = '(39.370, 39.370)'
      * 'translation' [float2] = '(0.000, 0.000)'
    * '/World/model_forklift/materials/mat_92/stReader' (ID: 'UsdPrimvarReader_float2')
    * Implementation: 'id'
    * Inputs:
      * 'varname' [string]
        * Connected: '/World/model_forklift/materials/mat_92.inputs:frame:stPrimvarName' @ '/World/model_forklift/materials/mat_92'

---

### /World/model_forklift/materials/mat_96

* **Prim路径 (Prim Path):**/World/model_forklift/materials/mat_96
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/model_forklift/materials/mat_96/PBRShader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/model_forklift/materials/mat_96/PBRShader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'clearcoat' [float] = '0.2'
      * 'clearcoatRoughness' [float] = '0.05'
      * 'diffuseColor' [color3f]
        * Connected: '/World/model_forklift/materials/mat_96/diffuseTexture.outputs:rgb' @ '/World/model_forklift/materials/mat_96/diffuseTexture'
          * Shader ID: 'UsdUVTexture'
          * Texture: './img/fd350e4bb19acb8fcc0aa3e29f5c9da1.png'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'ior' [float] = '1'
      * 'metallic' [float] = '0.05'
      * 'opacity' [float] = '1'
      * 'roughness' [float] = '0.3'
      * 'specularColor' [color3f] = '(0.000, 0.000, 0.000)'
    * '/World/model_forklift/materials/mat_96/diffuseTexture' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * './img/fd350e4bb19acb8fcc0aa3e29f5c9da1.png'
    * Inputs:
      * 'file' [asset] = './img/fd350e4bb19acb8fcc0aa3e29f5c9da1.png'
      * 'st' [float2]
        * Connected: '/World/model_forklift/materials/mat_96/transform_st.outputs:result' @ '/World/model_forklift/materials/mat_96/transform_st'
          * Shader ID: 'UsdTransform2d'
    * '/World/model_forklift/materials/mat_96/transform_st' (ID: 'UsdTransform2d')
    * Implementation: 'id'
    * Inputs:
      * 'in' [float2]
        * Connected: '/World/model_forklift/materials/mat_96/stReader.outputs:result' @ '/World/model_forklift/materials/mat_96/stReader'
          * Shader ID: 'UsdPrimvarReader_float2'
      * 'rotation' [float] = '0'
      * 'scale' [float2] = '(39.370, 39.370)'
      * 'translation' [float2] = '(0.000, 0.000)'
    * '/World/model_forklift/materials/mat_96/stReader' (ID: 'UsdPrimvarReader_float2')
    * Implementation: 'id'
    * Inputs:
      * 'varname' [string]
        * Connected: '/World/model_forklift/materials/mat_96.inputs:frame:stPrimvarName' @ '/World/model_forklift/materials/mat_96'

---

### /World/model_forklift/materials/mat_145

* **Prim路径 (Prim Path):**/World/model_forklift/materials/mat_145
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/model_forklift/materials/mat_145/PBRShader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/model_forklift/materials/mat_145/PBRShader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'clearcoat' [float] = '0.2'
      * 'clearcoatRoughness' [float] = '0.05'
      * 'diffuseColor' [color3f] = '(0.402, 0.402, 0.402)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'ior' [float] = '1'
      * 'metallic' [float] = '0.2'
      * 'opacity' [float] = '1'
      * 'roughness' [float] = '0.25'
      * 'specularColor' [color3f] = '(0.000, 0.000, 0.000)'

---

### /World/model_forklift/PhysicsMaterial

* **Prim路径 (Prim Path):**/World/model_forklift/PhysicsMaterial
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'

---

### /World/model_forklift/PhysicsMaterial_01

* **Prim路径 (Prim Path):**/World/model_forklift/PhysicsMaterial_01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'

---

### /World/model_forklift/PhysicsMaterial_02

* **Prim路径 (Prim Path):**/World/model_forklift/PhysicsMaterial_02
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'

---

### /World/ridgeback_franka/panda_link0/visuals/Looks/EmissiveBlue

* **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_link0/visuals/Looks/EmissiveBlue
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_link0/visuals/Looks/EmissiveBlue/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/ridgeback_franka/panda_link0/visuals/Looks/EmissiveBlue/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * Inputs:
      * 'diffuse_color_constant' [color3f] = '(1.000, 1.000, 1.000)'
      * 'emissive_color' [color3f] = '(0.000, 0.100, 1.000)'
      * 'emissive_intensity' [float] = '29000'
      * 'reflection_roughness_constant' [float] = '0.298'

---

### /World/ridgeback_franka/panda_link0/visuals/Looks/PlasticGray

* **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_link0/visuals/Looks/PlasticGray
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_link0/visuals/Looks/PlasticGray/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/ridgeback_franka/panda_link0/visuals/Looks/PlasticGray/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * Inputs:
      * 'diffuse_color_constant' [color3f] = '(0.100, 0.100, 0.100)'
      * 'reflection_roughness_constant' [float] = '0.292'

---

### /World/ridgeback_franka/panda_link0/visuals/Looks/Aluminum

* **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_link0/visuals/Looks/Aluminum
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_link0/visuals/Looks/Aluminum/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/ridgeback_franka/panda_link0/visuals/Looks/Aluminum/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * Inputs:
      * 'diffuse_color_constant' [color3f] = '(0.900, 0.900, 0.900)'
      * 'metallic_constant' [float] = '0.899'
      * 'reflection_roughness_constant' [float] = '0.101'

---

### /World/ridgeback_franka/panda_link0/visuals/Looks/PlasticBlack

* **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_link0/visuals/Looks/PlasticBlack
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_link0/visuals/Looks/PlasticBlack/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/ridgeback_franka/panda_link0/visuals/Looks/PlasticBlack/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * Inputs:
      * 'diffuse_color_constant' [color3f] = '(0.000, 0.000, 0.000)'
      * 'reflection_roughness_constant' [float] = '0'

---

### /World/ridgeback_franka/panda_link0/visuals/Looks/RubberGreen

* **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_link0/visuals/Looks/RubberGreen
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_link0/visuals/Looks/RubberGreen/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/ridgeback_franka/panda_link0/visuals/Looks/RubberGreen/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * Inputs:
      * 'diffuse_color_constant' [color3f] = '(0.000, 0.500, 0.000)'

---

### /World/ridgeback_franka/panda_link0/visuals/Looks/RubberRed

* **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_link0/visuals/Looks/RubberRed
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_link0/visuals/Looks/RubberRed/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/ridgeback_franka/panda_link0/visuals/Looks/RubberRed/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * Inputs:
      * 'diffuse_color_constant' [color3f] = '(0.500, 0.000, 0.000)'

---

### /World/ridgeback_franka/panda_link0/visuals/Looks/RubberWhite

* **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_link0/visuals/Looks/RubberWhite
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_link0/visuals/Looks/RubberWhite/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/ridgeback_franka/panda_link0/visuals/Looks/RubberWhite/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * Inputs:
      * 'diffuse_color_constant' [color3f] = '(0.900, 0.900, 0.900)'

---

### /World/ridgeback_franka/panda_link0/visuals/Looks/RubberGray

* **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_link0/visuals/Looks/RubberGray
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_link0/visuals/Looks/RubberGray/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/ridgeback_franka/panda_link0/visuals/Looks/RubberGray/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * Inputs:
      * 'diffuse_color_constant' [color3f] = '(0.050, 0.050, 0.050)'

---

### /World/ridgeback_franka/panda_link0/visuals/Looks/RubberLightGray

* **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_link0/visuals/Looks/RubberLightGray
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_link0/visuals/Looks/RubberLightGray/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/ridgeback_franka/panda_link0/visuals/Looks/RubberLightGray/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')

---

### /World/ridgeback_franka/panda_link0/visuals/Looks/AluminumRough

* **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_link0/visuals/Looks/AluminumRough
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_link0/visuals/Looks/AluminumRough/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/ridgeback_franka/panda_link0/visuals/Looks/AluminumRough/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * Inputs:
      * 'diffuse_color_constant' [color3f] = '(0.400, 0.400, 0.400)'
      * 'metallic_constant' [float] = '0.399'
      * 'reflection_roughness_constant' [float] = '0.202'

---

### /World/ridgeback_franka/panda_link0/visuals/Looks/rubber_cable

* **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_link0/visuals/Looks/rubber_cable
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_link0/visuals/Looks/rubber_cable/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/ridgeback_franka/panda_link0/visuals/Looks/rubber_cable/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * Inputs:
      * 'diffuse_color_constant' [color3f] = '(0.050, 0.050, 0.050)'
      * 'metallic_constant' [float] = '0'
      * 'reflection_roughness_constant' [float] = '0.5'
      * 'specular_level' [float] = '0'

---

### /World/ridgeback_franka/panda_link0/visuals/Looks/PlasticWhite

* **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_link0/visuals/Looks/PlasticWhite
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_link0/visuals/Looks/PlasticWhite/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/ridgeback_franka/panda_link0/visuals/Looks/PlasticWhite/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * Inputs:
      * 'diffuse_color_constant' [color3f] = '(0.700, 0.700, 0.700)'
      * 'reflection_roughness_constant' [float] = '0.18'

---

### /World/ridgeback_franka/panda_link1/visuals/Looks/EmissiveBlue

* **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_link1/visuals/Looks/EmissiveBlue
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_link1/visuals/Looks/EmissiveBlue/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/ridgeback_franka/panda_link1/visuals/Looks/EmissiveBlue/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * Inputs:
      * 'diffuse_color_constant' [color3f] = '(1.000, 1.000, 1.000)'
      * 'emissive_color' [color3f] = '(0.000, 0.100, 1.000)'
      * 'emissive_intensity' [float] = '29000'
      * 'reflection_roughness_constant' [float] = '0.298'

---

### /World/ridgeback_franka/panda_link1/visuals/Looks/PlasticGray

* **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_link1/visuals/Looks/PlasticGray
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_link1/visuals/Looks/PlasticGray/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/ridgeback_franka/panda_link1/visuals/Looks/PlasticGray/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * Inputs:
      * 'diffuse_color_constant' [color3f] = '(0.100, 0.100, 0.100)'
      * 'reflection_roughness_constant' [float] = '0.292'

---

### /World/ridgeback_franka/panda_link1/visuals/Looks/Aluminum

* **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_link1/visuals/Looks/Aluminum
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_link1/visuals/Looks/Aluminum/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/ridgeback_franka/panda_link1/visuals/Looks/Aluminum/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * Inputs:
      * 'diffuse_color_constant' [color3f] = '(0.900, 0.900, 0.900)'
      * 'metallic_constant' [float] = '0.899'
      * 'reflection_roughness_constant' [float] = '0.101'

---

### /World/ridgeback_franka/panda_link1/visuals/Looks/PlasticBlack

* **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_link1/visuals/Looks/PlasticBlack
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_link1/visuals/Looks/PlasticBlack/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/ridgeback_franka/panda_link1/visuals/Looks/PlasticBlack/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * Inputs:
      * 'diffuse_color_constant' [color3f] = '(0.000, 0.000, 0.000)'
      * 'reflection_roughness_constant' [float] = '0'

---

### /World/ridgeback_franka/panda_link1/visuals/Looks/RubberGreen

* **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_link1/visuals/Looks/RubberGreen
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_link1/visuals/Looks/RubberGreen/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/ridgeback_franka/panda_link1/visuals/Looks/RubberGreen/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * Inputs:
      * 'diffuse_color_constant' [color3f] = '(0.000, 0.500, 0.000)'

---

### /World/ridgeback_franka/panda_link1/visuals/Looks/RubberRed

* **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_link1/visuals/Looks/RubberRed
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_link1/visuals/Looks/RubberRed/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/ridgeback_franka/panda_link1/visuals/Looks/RubberRed/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * Inputs:
      * 'diffuse_color_constant' [color3f] = '(0.500, 0.000, 0.000)'

---

### /World/ridgeback_franka/panda_link1/visuals/Looks/RubberWhite

* **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_link1/visuals/Looks/RubberWhite
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_link1/visuals/Looks/RubberWhite/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/ridgeback_franka/panda_link1/visuals/Looks/RubberWhite/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * Inputs:
      * 'diffuse_color_constant' [color3f] = '(0.900, 0.900, 0.900)'

---

### /World/ridgeback_franka/panda_link1/visuals/Looks/RubberGray

* **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_link1/visuals/Looks/RubberGray
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_link1/visuals/Looks/RubberGray/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/ridgeback_franka/panda_link1/visuals/Looks/RubberGray/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * Inputs:
      * 'diffuse_color_constant' [color3f] = '(0.050, 0.050, 0.050)'

---

### /World/ridgeback_franka/panda_link1/visuals/Looks/RubberLightGray

* **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_link1/visuals/Looks/RubberLightGray
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_link1/visuals/Looks/RubberLightGray/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/ridgeback_franka/panda_link1/visuals/Looks/RubberLightGray/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')

---

### /World/ridgeback_franka/panda_link1/visuals/Looks/AluminumRough

* **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_link1/visuals/Looks/AluminumRough
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_link1/visuals/Looks/AluminumRough/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/ridgeback_franka/panda_link1/visuals/Looks/AluminumRough/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * Inputs:
      * 'diffuse_color_constant' [color3f] = '(0.400, 0.400, 0.400)'
      * 'metallic_constant' [float] = '0.399'
      * 'reflection_roughness_constant' [float] = '0.202'

---

### /World/ridgeback_franka/panda_link1/visuals/Looks/rubber_cable

* **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_link1/visuals/Looks/rubber_cable
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_link1/visuals/Looks/rubber_cable/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/ridgeback_franka/panda_link1/visuals/Looks/rubber_cable/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * Inputs:
      * 'diffuse_color_constant' [color3f] = '(0.050, 0.050, 0.050)'
      * 'metallic_constant' [float] = '0'
      * 'reflection_roughness_constant' [float] = '0.5'
      * 'specular_level' [float] = '0'

---

### /World/ridgeback_franka/panda_link1/visuals/Looks/PlasticWhite

* **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_link1/visuals/Looks/PlasticWhite
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_link1/visuals/Looks/PlasticWhite/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/ridgeback_franka/panda_link1/visuals/Looks/PlasticWhite/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * Inputs:
      * 'diffuse_color_constant' [color3f] = '(0.700, 0.700, 0.700)'
      * 'reflection_roughness_constant' [float] = '0.18'

---

### /World/ridgeback_franka/panda_link2/visuals/Looks/EmissiveBlue

* **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_link2/visuals/Looks/EmissiveBlue
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_link2/visuals/Looks/EmissiveBlue/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/ridgeback_franka/panda_link2/visuals/Looks/EmissiveBlue/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * Inputs:
      * 'diffuse_color_constant' [color3f] = '(1.000, 1.000, 1.000)'
      * 'emissive_color' [color3f] = '(0.000, 0.100, 1.000)'
      * 'emissive_intensity' [float] = '29000'
      * 'reflection_roughness_constant' [float] = '0.298'

---

### /World/ridgeback_franka/panda_link2/visuals/Looks/PlasticGray

* **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_link2/visuals/Looks/PlasticGray
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_link2/visuals/Looks/PlasticGray/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/ridgeback_franka/panda_link2/visuals/Looks/PlasticGray/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * Inputs:
      * 'diffuse_color_constant' [color3f] = '(0.100, 0.100, 0.100)'
      * 'reflection_roughness_constant' [float] = '0.292'

---

### /World/ridgeback_franka/panda_link2/visuals/Looks/Aluminum

* **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_link2/visuals/Looks/Aluminum
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_link2/visuals/Looks/Aluminum/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/ridgeback_franka/panda_link2/visuals/Looks/Aluminum/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * Inputs:
      * 'diffuse_color_constant' [color3f] = '(0.900, 0.900, 0.900)'
      * 'metallic_constant' [float] = '0.899'
      * 'reflection_roughness_constant' [float] = '0.101'

---

### /World/ridgeback_franka/panda_link2/visuals/Looks/PlasticBlack

* **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_link2/visuals/Looks/PlasticBlack
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_link2/visuals/Looks/PlasticBlack/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/ridgeback_franka/panda_link2/visuals/Looks/PlasticBlack/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * Inputs:
      * 'diffuse_color_constant' [color3f] = '(0.000, 0.000, 0.000)'
      * 'reflection_roughness_constant' [float] = '0'

---

### /World/ridgeback_franka/panda_link2/visuals/Looks/RubberGreen

* **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_link2/visuals/Looks/RubberGreen
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_link2/visuals/Looks/RubberGreen/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/ridgeback_franka/panda_link2/visuals/Looks/RubberGreen/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * Inputs:
      * 'diffuse_color_constant' [color3f] = '(0.000, 0.500, 0.000)'

---

### /World/ridgeback_franka/panda_link2/visuals/Looks/RubberRed

* **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_link2/visuals/Looks/RubberRed
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_link2/visuals/Looks/RubberRed/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/ridgeback_franka/panda_link2/visuals/Looks/RubberRed/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * Inputs:
      * 'diffuse_color_constant' [color3f] = '(0.500, 0.000, 0.000)'

---

### /World/ridgeback_franka/panda_link2/visuals/Looks/RubberWhite

* **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_link2/visuals/Looks/RubberWhite
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_link2/visuals/Looks/RubberWhite/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/ridgeback_franka/panda_link2/visuals/Looks/RubberWhite/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * Inputs:
      * 'diffuse_color_constant' [color3f] = '(0.900, 0.900, 0.900)'

---

### /World/ridgeback_franka/panda_link2/visuals/Looks/RubberGray

* **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_link2/visuals/Looks/RubberGray
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_link2/visuals/Looks/RubberGray/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/ridgeback_franka/panda_link2/visuals/Looks/RubberGray/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * Inputs:
      * 'diffuse_color_constant' [color3f] = '(0.050, 0.050, 0.050)'

---

### /World/ridgeback_franka/panda_link2/visuals/Looks/RubberLightGray

* **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_link2/visuals/Looks/RubberLightGray
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_link2/visuals/Looks/RubberLightGray/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/ridgeback_franka/panda_link2/visuals/Looks/RubberLightGray/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')

---

### /World/ridgeback_franka/panda_link2/visuals/Looks/AluminumRough

* **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_link2/visuals/Looks/AluminumRough
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_link2/visuals/Looks/AluminumRough/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/ridgeback_franka/panda_link2/visuals/Looks/AluminumRough/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * Inputs:
      * 'diffuse_color_constant' [color3f] = '(0.400, 0.400, 0.400)'
      * 'metallic_constant' [float] = '0.399'
      * 'reflection_roughness_constant' [float] = '0.202'

---

### /World/ridgeback_franka/panda_link2/visuals/Looks/rubber_cable

* **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_link2/visuals/Looks/rubber_cable
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_link2/visuals/Looks/rubber_cable/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/ridgeback_franka/panda_link2/visuals/Looks/rubber_cable/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * Inputs:
      * 'diffuse_color_constant' [color3f] = '(0.050, 0.050, 0.050)'
      * 'metallic_constant' [float] = '0'
      * 'reflection_roughness_constant' [float] = '0.5'
      * 'specular_level' [float] = '0'

---

### /World/ridgeback_franka/panda_link2/visuals/Looks/PlasticWhite

* **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_link2/visuals/Looks/PlasticWhite
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_link2/visuals/Looks/PlasticWhite/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/ridgeback_franka/panda_link2/visuals/Looks/PlasticWhite/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * Inputs:
      * 'diffuse_color_constant' [color3f] = '(0.700, 0.700, 0.700)'
      * 'reflection_roughness_constant' [float] = '0.18'

---

### /World/ridgeback_franka/panda_link3/visuals/Looks/EmissiveBlue

* **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_link3/visuals/Looks/EmissiveBlue
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_link3/visuals/Looks/EmissiveBlue/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/ridgeback_franka/panda_link3/visuals/Looks/EmissiveBlue/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * Inputs:
      * 'diffuse_color_constant' [color3f] = '(1.000, 1.000, 1.000)'
      * 'emissive_color' [color3f] = '(0.000, 0.100, 1.000)'
      * 'emissive_intensity' [float] = '29000'
      * 'reflection_roughness_constant' [float] = '0.298'

---

### /World/ridgeback_franka/panda_link3/visuals/Looks/PlasticGray

* **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_link3/visuals/Looks/PlasticGray
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_link3/visuals/Looks/PlasticGray/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/ridgeback_franka/panda_link3/visuals/Looks/PlasticGray/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * Inputs:
      * 'diffuse_color_constant' [color3f] = '(0.100, 0.100, 0.100)'
      * 'reflection_roughness_constant' [float] = '0.292'

---

### /World/ridgeback_franka/panda_link3/visuals/Looks/Aluminum

* **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_link3/visuals/Looks/Aluminum
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_link3/visuals/Looks/Aluminum/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/ridgeback_franka/panda_link3/visuals/Looks/Aluminum/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * Inputs:
      * 'diffuse_color_constant' [color3f] = '(0.900, 0.900, 0.900)'
      * 'metallic_constant' [float] = '0.899'
      * 'reflection_roughness_constant' [float] = '0.101'

---

### /World/ridgeback_franka/panda_link3/visuals/Looks/PlasticBlack

* **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_link3/visuals/Looks/PlasticBlack
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_link3/visuals/Looks/PlasticBlack/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/ridgeback_franka/panda_link3/visuals/Looks/PlasticBlack/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * Inputs:
      * 'diffuse_color_constant' [color3f] = '(0.000, 0.000, 0.000)'
      * 'reflection_roughness_constant' [float] = '0'

---

### /World/ridgeback_franka/panda_link3/visuals/Looks/RubberGreen

* **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_link3/visuals/Looks/RubberGreen
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_link3/visuals/Looks/RubberGreen/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/ridgeback_franka/panda_link3/visuals/Looks/RubberGreen/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * Inputs:
      * 'diffuse_color_constant' [color3f] = '(0.000, 0.500, 0.000)'

---

### /World/ridgeback_franka/panda_link3/visuals/Looks/RubberRed

* **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_link3/visuals/Looks/RubberRed
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_link3/visuals/Looks/RubberRed/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/ridgeback_franka/panda_link3/visuals/Looks/RubberRed/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * Inputs:
      * 'diffuse_color_constant' [color3f] = '(0.500, 0.000, 0.000)'

---

### /World/ridgeback_franka/panda_link3/visuals/Looks/RubberWhite

* **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_link3/visuals/Looks/RubberWhite
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_link3/visuals/Looks/RubberWhite/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/ridgeback_franka/panda_link3/visuals/Looks/RubberWhite/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * Inputs:
      * 'diffuse_color_constant' [color3f] = '(0.900, 0.900, 0.900)'

---

### /World/ridgeback_franka/panda_link3/visuals/Looks/RubberGray

* **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_link3/visuals/Looks/RubberGray
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_link3/visuals/Looks/RubberGray/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/ridgeback_franka/panda_link3/visuals/Looks/RubberGray/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * Inputs:
      * 'diffuse_color_constant' [color3f] = '(0.050, 0.050, 0.050)'

---

### /World/ridgeback_franka/panda_link3/visuals/Looks/RubberLightGray

* **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_link3/visuals/Looks/RubberLightGray
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_link3/visuals/Looks/RubberLightGray/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/ridgeback_franka/panda_link3/visuals/Looks/RubberLightGray/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')

---

### /World/ridgeback_franka/panda_link3/visuals/Looks/AluminumRough

* **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_link3/visuals/Looks/AluminumRough
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_link3/visuals/Looks/AluminumRough/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/ridgeback_franka/panda_link3/visuals/Looks/AluminumRough/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * Inputs:
      * 'diffuse_color_constant' [color3f] = '(0.400, 0.400, 0.400)'
      * 'metallic_constant' [float] = '0.399'
      * 'reflection_roughness_constant' [float] = '0.202'

---

### /World/ridgeback_franka/panda_link3/visuals/Looks/rubber_cable

* **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_link3/visuals/Looks/rubber_cable
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_link3/visuals/Looks/rubber_cable/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/ridgeback_franka/panda_link3/visuals/Looks/rubber_cable/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * Inputs:
      * 'diffuse_color_constant' [color3f] = '(0.050, 0.050, 0.050)'
      * 'metallic_constant' [float] = '0'
      * 'reflection_roughness_constant' [float] = '0.5'
      * 'specular_level' [float] = '0'

---

### /World/ridgeback_franka/panda_link3/visuals/Looks/PlasticWhite

* **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_link3/visuals/Looks/PlasticWhite
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_link3/visuals/Looks/PlasticWhite/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/ridgeback_franka/panda_link3/visuals/Looks/PlasticWhite/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * Inputs:
      * 'diffuse_color_constant' [color3f] = '(0.700, 0.700, 0.700)'
      * 'reflection_roughness_constant' [float] = '0.18'

---

### /World/ridgeback_franka/panda_link4/visuals/Looks/EmissiveBlue

* **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_link4/visuals/Looks/EmissiveBlue
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_link4/visuals/Looks/EmissiveBlue/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/ridgeback_franka/panda_link4/visuals/Looks/EmissiveBlue/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * Inputs:
      * 'diffuse_color_constant' [color3f] = '(1.000, 1.000, 1.000)'
      * 'emissive_color' [color3f] = '(0.000, 0.100, 1.000)'
      * 'emissive_intensity' [float] = '29000'
      * 'reflection_roughness_constant' [float] = '0.298'

---

### /World/ridgeback_franka/panda_link4/visuals/Looks/PlasticGray

* **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_link4/visuals/Looks/PlasticGray
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_link4/visuals/Looks/PlasticGray/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/ridgeback_franka/panda_link4/visuals/Looks/PlasticGray/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * Inputs:
      * 'diffuse_color_constant' [color3f] = '(0.100, 0.100, 0.100)'
      * 'reflection_roughness_constant' [float] = '0.292'

---

### /World/ridgeback_franka/panda_link4/visuals/Looks/Aluminum

* **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_link4/visuals/Looks/Aluminum
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_link4/visuals/Looks/Aluminum/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/ridgeback_franka/panda_link4/visuals/Looks/Aluminum/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * Inputs:
      * 'diffuse_color_constant' [color3f] = '(0.900, 0.900, 0.900)'
      * 'metallic_constant' [float] = '0.899'
      * 'reflection_roughness_constant' [float] = '0.101'

---

### /World/ridgeback_franka/panda_link4/visuals/Looks/PlasticBlack

* **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_link4/visuals/Looks/PlasticBlack
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_link4/visuals/Looks/PlasticBlack/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/ridgeback_franka/panda_link4/visuals/Looks/PlasticBlack/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * Inputs:
      * 'diffuse_color_constant' [color3f] = '(0.000, 0.000, 0.000)'
      * 'reflection_roughness_constant' [float] = '0'

---

### /World/ridgeback_franka/panda_link4/visuals/Looks/RubberGreen

* **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_link4/visuals/Looks/RubberGreen
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_link4/visuals/Looks/RubberGreen/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/ridgeback_franka/panda_link4/visuals/Looks/RubberGreen/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * Inputs:
      * 'diffuse_color_constant' [color3f] = '(0.000, 0.500, 0.000)'

---

### /World/ridgeback_franka/panda_link4/visuals/Looks/RubberRed

* **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_link4/visuals/Looks/RubberRed
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_link4/visuals/Looks/RubberRed/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/ridgeback_franka/panda_link4/visuals/Looks/RubberRed/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * Inputs:
      * 'diffuse_color_constant' [color3f] = '(0.500, 0.000, 0.000)'

---

### /World/ridgeback_franka/panda_link4/visuals/Looks/RubberWhite

* **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_link4/visuals/Looks/RubberWhite
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_link4/visuals/Looks/RubberWhite/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/ridgeback_franka/panda_link4/visuals/Looks/RubberWhite/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * Inputs:
      * 'diffuse_color_constant' [color3f] = '(0.900, 0.900, 0.900)'

---

### /World/ridgeback_franka/panda_link4/visuals/Looks/RubberGray

* **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_link4/visuals/Looks/RubberGray
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_link4/visuals/Looks/RubberGray/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/ridgeback_franka/panda_link4/visuals/Looks/RubberGray/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * Inputs:
      * 'diffuse_color_constant' [color3f] = '(0.050, 0.050, 0.050)'

---

### /World/ridgeback_franka/panda_link4/visuals/Looks/RubberLightGray

* **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_link4/visuals/Looks/RubberLightGray
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_link4/visuals/Looks/RubberLightGray/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/ridgeback_franka/panda_link4/visuals/Looks/RubberLightGray/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')

---

### /World/ridgeback_franka/panda_link4/visuals/Looks/AluminumRough

* **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_link4/visuals/Looks/AluminumRough
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_link4/visuals/Looks/AluminumRough/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/ridgeback_franka/panda_link4/visuals/Looks/AluminumRough/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * Inputs:
      * 'diffuse_color_constant' [color3f] = '(0.400, 0.400, 0.400)'
      * 'metallic_constant' [float] = '0.399'
      * 'reflection_roughness_constant' [float] = '0.202'

---

### /World/ridgeback_franka/panda_link4/visuals/Looks/rubber_cable

* **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_link4/visuals/Looks/rubber_cable
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_link4/visuals/Looks/rubber_cable/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/ridgeback_franka/panda_link4/visuals/Looks/rubber_cable/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * Inputs:
      * 'diffuse_color_constant' [color3f] = '(0.050, 0.050, 0.050)'
      * 'metallic_constant' [float] = '0'
      * 'reflection_roughness_constant' [float] = '0.5'
      * 'specular_level' [float] = '0'

---

### /World/ridgeback_franka/panda_link4/visuals/Looks/PlasticWhite

* **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_link4/visuals/Looks/PlasticWhite
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_link4/visuals/Looks/PlasticWhite/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/ridgeback_franka/panda_link4/visuals/Looks/PlasticWhite/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * Inputs:
      * 'diffuse_color_constant' [color3f] = '(0.700, 0.700, 0.700)'
      * 'reflection_roughness_constant' [float] = '0.18'

---

### /World/ridgeback_franka/panda_link5/visuals/Looks/EmissiveBlue

* **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_link5/visuals/Looks/EmissiveBlue
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_link5/visuals/Looks/EmissiveBlue/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/ridgeback_franka/panda_link5/visuals/Looks/EmissiveBlue/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * Inputs:
      * 'diffuse_color_constant' [color3f] = '(1.000, 1.000, 1.000)'
      * 'emissive_color' [color3f] = '(0.000, 0.100, 1.000)'
      * 'emissive_intensity' [float] = '29000'
      * 'reflection_roughness_constant' [float] = '0.298'

---

### /World/ridgeback_franka/panda_link5/visuals/Looks/PlasticGray

* **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_link5/visuals/Looks/PlasticGray
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_link5/visuals/Looks/PlasticGray/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/ridgeback_franka/panda_link5/visuals/Looks/PlasticGray/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * Inputs:
      * 'diffuse_color_constant' [color3f] = '(0.100, 0.100, 0.100)'
      * 'reflection_roughness_constant' [float] = '0.292'

---

### /World/ridgeback_franka/panda_link5/visuals/Looks/Aluminum

* **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_link5/visuals/Looks/Aluminum
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_link5/visuals/Looks/Aluminum/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/ridgeback_franka/panda_link5/visuals/Looks/Aluminum/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * Inputs:
      * 'diffuse_color_constant' [color3f] = '(0.900, 0.900, 0.900)'
      * 'metallic_constant' [float] = '0.899'
      * 'reflection_roughness_constant' [float] = '0.101'

---

### /World/ridgeback_franka/panda_link5/visuals/Looks/PlasticBlack

* **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_link5/visuals/Looks/PlasticBlack
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_link5/visuals/Looks/PlasticBlack/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/ridgeback_franka/panda_link5/visuals/Looks/PlasticBlack/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * Inputs:
      * 'diffuse_color_constant' [color3f] = '(0.000, 0.000, 0.000)'
      * 'reflection_roughness_constant' [float] = '0'

---

### /World/ridgeback_franka/panda_link5/visuals/Looks/RubberGreen

* **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_link5/visuals/Looks/RubberGreen
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_link5/visuals/Looks/RubberGreen/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/ridgeback_franka/panda_link5/visuals/Looks/RubberGreen/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * Inputs:
      * 'diffuse_color_constant' [color3f] = '(0.000, 0.500, 0.000)'

---

### /World/ridgeback_franka/panda_link5/visuals/Looks/RubberRed

* **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_link5/visuals/Looks/RubberRed
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_link5/visuals/Looks/RubberRed/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/ridgeback_franka/panda_link5/visuals/Looks/RubberRed/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * Inputs:
      * 'diffuse_color_constant' [color3f] = '(0.500, 0.000, 0.000)'

---

### /World/ridgeback_franka/panda_link5/visuals/Looks/RubberWhite

* **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_link5/visuals/Looks/RubberWhite
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_link5/visuals/Looks/RubberWhite/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/ridgeback_franka/panda_link5/visuals/Looks/RubberWhite/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * Inputs:
      * 'diffuse_color_constant' [color3f] = '(0.900, 0.900, 0.900)'

---

### /World/ridgeback_franka/panda_link5/visuals/Looks/RubberGray

* **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_link5/visuals/Looks/RubberGray
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_link5/visuals/Looks/RubberGray/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/ridgeback_franka/panda_link5/visuals/Looks/RubberGray/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * Inputs:
      * 'diffuse_color_constant' [color3f] = '(0.050, 0.050, 0.050)'

---

### /World/ridgeback_franka/panda_link5/visuals/Looks/RubberLightGray

* **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_link5/visuals/Looks/RubberLightGray
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_link5/visuals/Looks/RubberLightGray/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/ridgeback_franka/panda_link5/visuals/Looks/RubberLightGray/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')

---

### /World/ridgeback_franka/panda_link5/visuals/Looks/AluminumRough

* **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_link5/visuals/Looks/AluminumRough
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_link5/visuals/Looks/AluminumRough/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/ridgeback_franka/panda_link5/visuals/Looks/AluminumRough/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * Inputs:
      * 'diffuse_color_constant' [color3f] = '(0.400, 0.400, 0.400)'
      * 'metallic_constant' [float] = '0.399'
      * 'reflection_roughness_constant' [float] = '0.202'

---

### /World/ridgeback_franka/panda_link5/visuals/Looks/rubber_cable

* **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_link5/visuals/Looks/rubber_cable
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_link5/visuals/Looks/rubber_cable/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/ridgeback_franka/panda_link5/visuals/Looks/rubber_cable/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * Inputs:
      * 'diffuse_color_constant' [color3f] = '(0.050, 0.050, 0.050)'
      * 'metallic_constant' [float] = '0'
      * 'reflection_roughness_constant' [float] = '0.5'
      * 'specular_level' [float] = '0'

---

### /World/ridgeback_franka/panda_link5/visuals/Looks/PlasticWhite

* **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_link5/visuals/Looks/PlasticWhite
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_link5/visuals/Looks/PlasticWhite/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/ridgeback_franka/panda_link5/visuals/Looks/PlasticWhite/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * Inputs:
      * 'diffuse_color_constant' [color3f] = '(0.700, 0.700, 0.700)'
      * 'reflection_roughness_constant' [float] = '0.18'

---

### /World/ridgeback_franka/panda_link6/visuals/Looks/EmissiveBlue

* **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_link6/visuals/Looks/EmissiveBlue
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_link6/visuals/Looks/EmissiveBlue/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/ridgeback_franka/panda_link6/visuals/Looks/EmissiveBlue/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * Inputs:
      * 'diffuse_color_constant' [color3f] = '(1.000, 1.000, 1.000)'
      * 'emissive_color' [color3f] = '(0.000, 0.100, 1.000)'
      * 'emissive_intensity' [float] = '29000'
      * 'reflection_roughness_constant' [float] = '0.298'

---

### /World/ridgeback_franka/panda_link6/visuals/Looks/PlasticGray

* **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_link6/visuals/Looks/PlasticGray
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_link6/visuals/Looks/PlasticGray/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/ridgeback_franka/panda_link6/visuals/Looks/PlasticGray/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * Inputs:
      * 'diffuse_color_constant' [color3f] = '(0.100, 0.100, 0.100)'
      * 'reflection_roughness_constant' [float] = '0.292'

---

### /World/ridgeback_franka/panda_link6/visuals/Looks/Aluminum

* **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_link6/visuals/Looks/Aluminum
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_link6/visuals/Looks/Aluminum/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/ridgeback_franka/panda_link6/visuals/Looks/Aluminum/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * Inputs:
      * 'diffuse_color_constant' [color3f] = '(0.900, 0.900, 0.900)'
      * 'metallic_constant' [float] = '0.899'
      * 'reflection_roughness_constant' [float] = '0.101'

---

### /World/ridgeback_franka/panda_link6/visuals/Looks/PlasticBlack

* **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_link6/visuals/Looks/PlasticBlack
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_link6/visuals/Looks/PlasticBlack/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/ridgeback_franka/panda_link6/visuals/Looks/PlasticBlack/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * Inputs:
      * 'diffuse_color_constant' [color3f] = '(0.000, 0.000, 0.000)'
      * 'reflection_roughness_constant' [float] = '0'

---

### /World/ridgeback_franka/panda_link6/visuals/Looks/RubberGreen

* **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_link6/visuals/Looks/RubberGreen
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_link6/visuals/Looks/RubberGreen/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/ridgeback_franka/panda_link6/visuals/Looks/RubberGreen/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * Inputs:
      * 'diffuse_color_constant' [color3f] = '(0.000, 0.500, 0.000)'

---

### /World/ridgeback_franka/panda_link6/visuals/Looks/RubberRed

* **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_link6/visuals/Looks/RubberRed
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_link6/visuals/Looks/RubberRed/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/ridgeback_franka/panda_link6/visuals/Looks/RubberRed/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * Inputs:
      * 'diffuse_color_constant' [color3f] = '(0.500, 0.000, 0.000)'

---

### /World/ridgeback_franka/panda_link6/visuals/Looks/RubberWhite

* **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_link6/visuals/Looks/RubberWhite
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_link6/visuals/Looks/RubberWhite/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/ridgeback_franka/panda_link6/visuals/Looks/RubberWhite/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * Inputs:
      * 'diffuse_color_constant' [color3f] = '(0.900, 0.900, 0.900)'

---

### /World/ridgeback_franka/panda_link6/visuals/Looks/RubberGray

* **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_link6/visuals/Looks/RubberGray
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_link6/visuals/Looks/RubberGray/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/ridgeback_franka/panda_link6/visuals/Looks/RubberGray/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * Inputs:
      * 'diffuse_color_constant' [color3f] = '(0.050, 0.050, 0.050)'

---

### /World/ridgeback_franka/panda_link6/visuals/Looks/RubberLightGray

* **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_link6/visuals/Looks/RubberLightGray
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_link6/visuals/Looks/RubberLightGray/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/ridgeback_franka/panda_link6/visuals/Looks/RubberLightGray/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')

---

### /World/ridgeback_franka/panda_link6/visuals/Looks/AluminumRough

* **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_link6/visuals/Looks/AluminumRough
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_link6/visuals/Looks/AluminumRough/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/ridgeback_franka/panda_link6/visuals/Looks/AluminumRough/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * Inputs:
      * 'diffuse_color_constant' [color3f] = '(0.400, 0.400, 0.400)'
      * 'metallic_constant' [float] = '0.399'
      * 'reflection_roughness_constant' [float] = '0.202'

---

### /World/ridgeback_franka/panda_link6/visuals/Looks/rubber_cable

* **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_link6/visuals/Looks/rubber_cable
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_link6/visuals/Looks/rubber_cable/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/ridgeback_franka/panda_link6/visuals/Looks/rubber_cable/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * Inputs:
      * 'diffuse_color_constant' [color3f] = '(0.050, 0.050, 0.050)'
      * 'metallic_constant' [float] = '0'
      * 'reflection_roughness_constant' [float] = '0.5'
      * 'specular_level' [float] = '0'

---

### /World/ridgeback_franka/panda_link6/visuals/Looks/PlasticWhite

* **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_link6/visuals/Looks/PlasticWhite
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_link6/visuals/Looks/PlasticWhite/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/ridgeback_franka/panda_link6/visuals/Looks/PlasticWhite/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * Inputs:
      * 'diffuse_color_constant' [color3f] = '(0.700, 0.700, 0.700)'
      * 'reflection_roughness_constant' [float] = '0.18'

---

### /World/ridgeback_franka/panda_link7/visuals/Looks/EmissiveBlue

* **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_link7/visuals/Looks/EmissiveBlue
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_link7/visuals/Looks/EmissiveBlue/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/ridgeback_franka/panda_link7/visuals/Looks/EmissiveBlue/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * Inputs:
      * 'diffuse_color_constant' [color3f] = '(1.000, 1.000, 1.000)'
      * 'emissive_color' [color3f] = '(0.000, 0.100, 1.000)'
      * 'emissive_intensity' [float] = '29000'
      * 'reflection_roughness_constant' [float] = '0.298'

---

### /World/ridgeback_franka/panda_link7/visuals/Looks/PlasticGray

* **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_link7/visuals/Looks/PlasticGray
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_link7/visuals/Looks/PlasticGray/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/ridgeback_franka/panda_link7/visuals/Looks/PlasticGray/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * Inputs:
      * 'diffuse_color_constant' [color3f] = '(0.100, 0.100, 0.100)'
      * 'reflection_roughness_constant' [float] = '0.292'

---

### /World/ridgeback_franka/panda_link7/visuals/Looks/Aluminum

* **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_link7/visuals/Looks/Aluminum
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_link7/visuals/Looks/Aluminum/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/ridgeback_franka/panda_link7/visuals/Looks/Aluminum/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * Inputs:
      * 'diffuse_color_constant' [color3f] = '(0.900, 0.900, 0.900)'
      * 'metallic_constant' [float] = '0.899'
      * 'reflection_roughness_constant' [float] = '0.101'

---

### /World/ridgeback_franka/panda_link7/visuals/Looks/PlasticBlack

* **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_link7/visuals/Looks/PlasticBlack
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_link7/visuals/Looks/PlasticBlack/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/ridgeback_franka/panda_link7/visuals/Looks/PlasticBlack/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * Inputs:
      * 'diffuse_color_constant' [color3f] = '(0.000, 0.000, 0.000)'
      * 'reflection_roughness_constant' [float] = '0'

---

### /World/ridgeback_franka/panda_link7/visuals/Looks/RubberGreen

* **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_link7/visuals/Looks/RubberGreen
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_link7/visuals/Looks/RubberGreen/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/ridgeback_franka/panda_link7/visuals/Looks/RubberGreen/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * Inputs:
      * 'diffuse_color_constant' [color3f] = '(0.000, 0.500, 0.000)'

---

### /World/ridgeback_franka/panda_link7/visuals/Looks/RubberRed

* **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_link7/visuals/Looks/RubberRed
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_link7/visuals/Looks/RubberRed/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/ridgeback_franka/panda_link7/visuals/Looks/RubberRed/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * Inputs:
      * 'diffuse_color_constant' [color3f] = '(0.500, 0.000, 0.000)'

---

### /World/ridgeback_franka/panda_link7/visuals/Looks/RubberWhite

* **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_link7/visuals/Looks/RubberWhite
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_link7/visuals/Looks/RubberWhite/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/ridgeback_franka/panda_link7/visuals/Looks/RubberWhite/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * Inputs:
      * 'diffuse_color_constant' [color3f] = '(0.900, 0.900, 0.900)'

---

### /World/ridgeback_franka/panda_link7/visuals/Looks/RubberGray

* **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_link7/visuals/Looks/RubberGray
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_link7/visuals/Looks/RubberGray/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/ridgeback_franka/panda_link7/visuals/Looks/RubberGray/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * Inputs:
      * 'diffuse_color_constant' [color3f] = '(0.050, 0.050, 0.050)'

---

### /World/ridgeback_franka/panda_link7/visuals/Looks/RubberLightGray

* **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_link7/visuals/Looks/RubberLightGray
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_link7/visuals/Looks/RubberLightGray/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/ridgeback_franka/panda_link7/visuals/Looks/RubberLightGray/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')

---

### /World/ridgeback_franka/panda_link7/visuals/Looks/AluminumRough

* **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_link7/visuals/Looks/AluminumRough
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_link7/visuals/Looks/AluminumRough/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/ridgeback_franka/panda_link7/visuals/Looks/AluminumRough/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * Inputs:
      * 'diffuse_color_constant' [color3f] = '(0.400, 0.400, 0.400)'
      * 'metallic_constant' [float] = '0.399'
      * 'reflection_roughness_constant' [float] = '0.202'

---

### /World/ridgeback_franka/panda_link7/visuals/Looks/rubber_cable

* **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_link7/visuals/Looks/rubber_cable
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_link7/visuals/Looks/rubber_cable/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/ridgeback_franka/panda_link7/visuals/Looks/rubber_cable/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * Inputs:
      * 'diffuse_color_constant' [color3f] = '(0.050, 0.050, 0.050)'
      * 'metallic_constant' [float] = '0'
      * 'reflection_roughness_constant' [float] = '0.5'
      * 'specular_level' [float] = '0'

---

### /World/ridgeback_franka/panda_link7/visuals/Looks/PlasticWhite

* **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_link7/visuals/Looks/PlasticWhite
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_link7/visuals/Looks/PlasticWhite/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/ridgeback_franka/panda_link7/visuals/Looks/PlasticWhite/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * Inputs:
      * 'diffuse_color_constant' [color3f] = '(0.700, 0.700, 0.700)'
      * 'reflection_roughness_constant' [float] = '0.18'

---

### /World/ridgeback_franka/panda_hand/visuals/Looks/EmissiveBlue

* **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_hand/visuals/Looks/EmissiveBlue
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_hand/visuals/Looks/EmissiveBlue/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/ridgeback_franka/panda_hand/visuals/Looks/EmissiveBlue/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * Inputs:
      * 'diffuse_color_constant' [color3f] = '(1.000, 1.000, 1.000)'
      * 'emissive_color' [color3f] = '(0.000, 0.100, 1.000)'
      * 'emissive_intensity' [float] = '29000'
      * 'reflection_roughness_constant' [float] = '0.298'

---

### /World/ridgeback_franka/panda_hand/visuals/Looks/PlasticGray

* **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_hand/visuals/Looks/PlasticGray
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_hand/visuals/Looks/PlasticGray/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/ridgeback_franka/panda_hand/visuals/Looks/PlasticGray/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * Inputs:
      * 'diffuse_color_constant' [color3f] = '(0.100, 0.100, 0.100)'
      * 'reflection_roughness_constant' [float] = '0.292'

---

### /World/ridgeback_franka/panda_hand/visuals/Looks/Aluminum

* **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_hand/visuals/Looks/Aluminum
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_hand/visuals/Looks/Aluminum/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/ridgeback_franka/panda_hand/visuals/Looks/Aluminum/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * Inputs:
      * 'diffuse_color_constant' [color3f] = '(0.900, 0.900, 0.900)'
      * 'metallic_constant' [float] = '0.899'
      * 'reflection_roughness_constant' [float] = '0.101'

---

### /World/ridgeback_franka/panda_hand/visuals/Looks/PlasticBlack

* **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_hand/visuals/Looks/PlasticBlack
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_hand/visuals/Looks/PlasticBlack/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/ridgeback_franka/panda_hand/visuals/Looks/PlasticBlack/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * Inputs:
      * 'diffuse_color_constant' [color3f] = '(0.000, 0.000, 0.000)'
      * 'reflection_roughness_constant' [float] = '0'

---

### /World/ridgeback_franka/panda_hand/visuals/Looks/RubberGreen

* **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_hand/visuals/Looks/RubberGreen
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_hand/visuals/Looks/RubberGreen/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/ridgeback_franka/panda_hand/visuals/Looks/RubberGreen/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * Inputs:
      * 'diffuse_color_constant' [color3f] = '(0.000, 0.500, 0.000)'

---

### /World/ridgeback_franka/panda_hand/visuals/Looks/RubberRed

* **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_hand/visuals/Looks/RubberRed
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_hand/visuals/Looks/RubberRed/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/ridgeback_franka/panda_hand/visuals/Looks/RubberRed/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * Inputs:
      * 'diffuse_color_constant' [color3f] = '(0.500, 0.000, 0.000)'

---

### /World/ridgeback_franka/panda_hand/visuals/Looks/RubberWhite

* **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_hand/visuals/Looks/RubberWhite
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_hand/visuals/Looks/RubberWhite/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/ridgeback_franka/panda_hand/visuals/Looks/RubberWhite/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * Inputs:
      * 'diffuse_color_constant' [color3f] = '(0.900, 0.900, 0.900)'

---

### /World/ridgeback_franka/panda_hand/visuals/Looks/RubberGray

* **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_hand/visuals/Looks/RubberGray
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_hand/visuals/Looks/RubberGray/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/ridgeback_franka/panda_hand/visuals/Looks/RubberGray/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * Inputs:
      * 'diffuse_color_constant' [color3f] = '(0.050, 0.050, 0.050)'

---

### /World/ridgeback_franka/panda_hand/visuals/Looks/RubberLightGray

* **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_hand/visuals/Looks/RubberLightGray
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_hand/visuals/Looks/RubberLightGray/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/ridgeback_franka/panda_hand/visuals/Looks/RubberLightGray/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')

---

### /World/ridgeback_franka/panda_hand/visuals/Looks/AluminumRough

* **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_hand/visuals/Looks/AluminumRough
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_hand/visuals/Looks/AluminumRough/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/ridgeback_franka/panda_hand/visuals/Looks/AluminumRough/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * Inputs:
      * 'diffuse_color_constant' [color3f] = '(0.400, 0.400, 0.400)'
      * 'metallic_constant' [float] = '0.399'
      * 'reflection_roughness_constant' [float] = '0.202'

---

### /World/ridgeback_franka/panda_hand/visuals/Looks/rubber_cable

* **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_hand/visuals/Looks/rubber_cable
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_hand/visuals/Looks/rubber_cable/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/ridgeback_franka/panda_hand/visuals/Looks/rubber_cable/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * Inputs:
      * 'diffuse_color_constant' [color3f] = '(0.050, 0.050, 0.050)'
      * 'metallic_constant' [float] = '0'
      * 'reflection_roughness_constant' [float] = '0.5'
      * 'specular_level' [float] = '0'

---

### /World/ridgeback_franka/panda_hand/visuals/Looks/PlasticWhite

* **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_hand/visuals/Looks/PlasticWhite
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_hand/visuals/Looks/PlasticWhite/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/ridgeback_franka/panda_hand/visuals/Looks/PlasticWhite/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * Inputs:
      * 'diffuse_color_constant' [color3f] = '(0.700, 0.700, 0.700)'
      * 'reflection_roughness_constant' [float] = '0.18'

---

### /World/ridgeback_franka/panda_leftfinger/visuals/Looks/EmissiveBlue

* **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_leftfinger/visuals/Looks/EmissiveBlue
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_leftfinger/visuals/Looks/EmissiveBlue/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/ridgeback_franka/panda_leftfinger/visuals/Looks/EmissiveBlue/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * Inputs:
      * 'diffuse_color_constant' [color3f] = '(1.000, 1.000, 1.000)'
      * 'emissive_color' [color3f] = '(0.000, 0.100, 1.000)'
      * 'emissive_intensity' [float] = '29000'
      * 'reflection_roughness_constant' [float] = '0.298'

---

### /World/ridgeback_franka/panda_leftfinger/visuals/Looks/PlasticGray

* **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_leftfinger/visuals/Looks/PlasticGray
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_leftfinger/visuals/Looks/PlasticGray/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/ridgeback_franka/panda_leftfinger/visuals/Looks/PlasticGray/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * Inputs:
      * 'diffuse_color_constant' [color3f] = '(0.100, 0.100, 0.100)'
      * 'reflection_roughness_constant' [float] = '0.292'

---

### /World/ridgeback_franka/panda_leftfinger/visuals/Looks/Aluminum

* **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_leftfinger/visuals/Looks/Aluminum
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_leftfinger/visuals/Looks/Aluminum/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/ridgeback_franka/panda_leftfinger/visuals/Looks/Aluminum/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * Inputs:
      * 'diffuse_color_constant' [color3f] = '(0.900, 0.900, 0.900)'
      * 'metallic_constant' [float] = '0.899'
      * 'reflection_roughness_constant' [float] = '0.101'

---

### /World/ridgeback_franka/panda_leftfinger/visuals/Looks/PlasticBlack

* **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_leftfinger/visuals/Looks/PlasticBlack
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_leftfinger/visuals/Looks/PlasticBlack/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/ridgeback_franka/panda_leftfinger/visuals/Looks/PlasticBlack/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * Inputs:
      * 'diffuse_color_constant' [color3f] = '(0.000, 0.000, 0.000)'
      * 'reflection_roughness_constant' [float] = '0'

---

### /World/ridgeback_franka/panda_leftfinger/visuals/Looks/RubberGreen

* **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_leftfinger/visuals/Looks/RubberGreen
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_leftfinger/visuals/Looks/RubberGreen/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/ridgeback_franka/panda_leftfinger/visuals/Looks/RubberGreen/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * Inputs:
      * 'diffuse_color_constant' [color3f] = '(0.000, 0.500, 0.000)'

---

### /World/ridgeback_franka/panda_leftfinger/visuals/Looks/RubberRed

* **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_leftfinger/visuals/Looks/RubberRed
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_leftfinger/visuals/Looks/RubberRed/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/ridgeback_franka/panda_leftfinger/visuals/Looks/RubberRed/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * Inputs:
      * 'diffuse_color_constant' [color3f] = '(0.500, 0.000, 0.000)'

---

### /World/ridgeback_franka/panda_leftfinger/visuals/Looks/RubberWhite

* **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_leftfinger/visuals/Looks/RubberWhite
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_leftfinger/visuals/Looks/RubberWhite/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/ridgeback_franka/panda_leftfinger/visuals/Looks/RubberWhite/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * Inputs:
      * 'diffuse_color_constant' [color3f] = '(0.900, 0.900, 0.900)'

---

### /World/ridgeback_franka/panda_leftfinger/visuals/Looks/RubberGray

* **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_leftfinger/visuals/Looks/RubberGray
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_leftfinger/visuals/Looks/RubberGray/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/ridgeback_franka/panda_leftfinger/visuals/Looks/RubberGray/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * Inputs:
      * 'diffuse_color_constant' [color3f] = '(0.050, 0.050, 0.050)'

---

### /World/ridgeback_franka/panda_leftfinger/visuals/Looks/RubberLightGray

* **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_leftfinger/visuals/Looks/RubberLightGray
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_leftfinger/visuals/Looks/RubberLightGray/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/ridgeback_franka/panda_leftfinger/visuals/Looks/RubberLightGray/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')

---

### /World/ridgeback_franka/panda_leftfinger/visuals/Looks/AluminumRough

* **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_leftfinger/visuals/Looks/AluminumRough
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_leftfinger/visuals/Looks/AluminumRough/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/ridgeback_franka/panda_leftfinger/visuals/Looks/AluminumRough/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * Inputs:
      * 'diffuse_color_constant' [color3f] = '(0.400, 0.400, 0.400)'
      * 'metallic_constant' [float] = '0.399'
      * 'reflection_roughness_constant' [float] = '0.202'

---

### /World/ridgeback_franka/panda_leftfinger/visuals/Looks/rubber_cable

* **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_leftfinger/visuals/Looks/rubber_cable
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_leftfinger/visuals/Looks/rubber_cable/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/ridgeback_franka/panda_leftfinger/visuals/Looks/rubber_cable/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * Inputs:
      * 'diffuse_color_constant' [color3f] = '(0.050, 0.050, 0.050)'
      * 'metallic_constant' [float] = '0'
      * 'reflection_roughness_constant' [float] = '0.5'
      * 'specular_level' [float] = '0'

---

### /World/ridgeback_franka/panda_leftfinger/visuals/Looks/PlasticWhite

* **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_leftfinger/visuals/Looks/PlasticWhite
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_leftfinger/visuals/Looks/PlasticWhite/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/ridgeback_franka/panda_leftfinger/visuals/Looks/PlasticWhite/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * Inputs:
      * 'diffuse_color_constant' [color3f] = '(0.700, 0.700, 0.700)'
      * 'reflection_roughness_constant' [float] = '0.18'

---

### /World/ridgeback_franka/panda_rightfinger/visuals/Looks/EmissiveBlue

* **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_rightfinger/visuals/Looks/EmissiveBlue
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_rightfinger/visuals/Looks/EmissiveBlue/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/ridgeback_franka/panda_rightfinger/visuals/Looks/EmissiveBlue/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * Inputs:
      * 'diffuse_color_constant' [color3f] = '(1.000, 1.000, 1.000)'
      * 'emissive_color' [color3f] = '(0.000, 0.100, 1.000)'
      * 'emissive_intensity' [float] = '29000'
      * 'reflection_roughness_constant' [float] = '0.298'

---

### /World/ridgeback_franka/panda_rightfinger/visuals/Looks/PlasticGray

* **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_rightfinger/visuals/Looks/PlasticGray
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_rightfinger/visuals/Looks/PlasticGray/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/ridgeback_franka/panda_rightfinger/visuals/Looks/PlasticGray/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * Inputs:
      * 'diffuse_color_constant' [color3f] = '(0.100, 0.100, 0.100)'
      * 'reflection_roughness_constant' [float] = '0.292'

---

### /World/ridgeback_franka/panda_rightfinger/visuals/Looks/Aluminum

* **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_rightfinger/visuals/Looks/Aluminum
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_rightfinger/visuals/Looks/Aluminum/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/ridgeback_franka/panda_rightfinger/visuals/Looks/Aluminum/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * Inputs:
      * 'diffuse_color_constant' [color3f] = '(0.900, 0.900, 0.900)'
      * 'metallic_constant' [float] = '0.899'
      * 'reflection_roughness_constant' [float] = '0.101'

---

### /World/ridgeback_franka/panda_rightfinger/visuals/Looks/PlasticBlack

* **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_rightfinger/visuals/Looks/PlasticBlack
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_rightfinger/visuals/Looks/PlasticBlack/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/ridgeback_franka/panda_rightfinger/visuals/Looks/PlasticBlack/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * Inputs:
      * 'diffuse_color_constant' [color3f] = '(0.000, 0.000, 0.000)'
      * 'reflection_roughness_constant' [float] = '0'

---

### /World/ridgeback_franka/panda_rightfinger/visuals/Looks/RubberGreen

* **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_rightfinger/visuals/Looks/RubberGreen
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_rightfinger/visuals/Looks/RubberGreen/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/ridgeback_franka/panda_rightfinger/visuals/Looks/RubberGreen/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * Inputs:
      * 'diffuse_color_constant' [color3f] = '(0.000, 0.500, 0.000)'

---

### /World/ridgeback_franka/panda_rightfinger/visuals/Looks/RubberRed

* **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_rightfinger/visuals/Looks/RubberRed
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_rightfinger/visuals/Looks/RubberRed/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/ridgeback_franka/panda_rightfinger/visuals/Looks/RubberRed/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * Inputs:
      * 'diffuse_color_constant' [color3f] = '(0.500, 0.000, 0.000)'

---

### /World/ridgeback_franka/panda_rightfinger/visuals/Looks/RubberWhite

* **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_rightfinger/visuals/Looks/RubberWhite
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_rightfinger/visuals/Looks/RubberWhite/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/ridgeback_franka/panda_rightfinger/visuals/Looks/RubberWhite/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * Inputs:
      * 'diffuse_color_constant' [color3f] = '(0.900, 0.900, 0.900)'

---

### /World/ridgeback_franka/panda_rightfinger/visuals/Looks/RubberGray

* **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_rightfinger/visuals/Looks/RubberGray
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_rightfinger/visuals/Looks/RubberGray/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/ridgeback_franka/panda_rightfinger/visuals/Looks/RubberGray/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * Inputs:
      * 'diffuse_color_constant' [color3f] = '(0.050, 0.050, 0.050)'

---

### /World/ridgeback_franka/panda_rightfinger/visuals/Looks/RubberLightGray

* **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_rightfinger/visuals/Looks/RubberLightGray
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_rightfinger/visuals/Looks/RubberLightGray/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/ridgeback_franka/panda_rightfinger/visuals/Looks/RubberLightGray/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')

---

### /World/ridgeback_franka/panda_rightfinger/visuals/Looks/AluminumRough

* **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_rightfinger/visuals/Looks/AluminumRough
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_rightfinger/visuals/Looks/AluminumRough/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/ridgeback_franka/panda_rightfinger/visuals/Looks/AluminumRough/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * Inputs:
      * 'diffuse_color_constant' [color3f] = '(0.400, 0.400, 0.400)'
      * 'metallic_constant' [float] = '0.399'
      * 'reflection_roughness_constant' [float] = '0.202'

---

### /World/ridgeback_franka/panda_rightfinger/visuals/Looks/rubber_cable

* **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_rightfinger/visuals/Looks/rubber_cable
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_rightfinger/visuals/Looks/rubber_cable/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/ridgeback_franka/panda_rightfinger/visuals/Looks/rubber_cable/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * Inputs:
      * 'diffuse_color_constant' [color3f] = '(0.050, 0.050, 0.050)'
      * 'metallic_constant' [float] = '0'
      * 'reflection_roughness_constant' [float] = '0.5'
      * 'specular_level' [float] = '0'

---

### /World/ridgeback_franka/panda_rightfinger/visuals/Looks/PlasticWhite

* **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_rightfinger/visuals/Looks/PlasticWhite
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_rightfinger/visuals/Looks/PlasticWhite/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/ridgeback_franka/panda_rightfinger/visuals/Looks/PlasticWhite/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * Inputs:
      * 'diffuse_color_constant' [color3f] = '(0.700, 0.700, 0.700)'
      * 'reflection_roughness_constant' [float] = '0.18'

---

### /World/ridgeback_franka/Looks/material_black

* **Prim路径 (Prim Path):**/World/ridgeback_franka/Looks/material_black
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/ridgeback_franka/Looks/material_black/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/ridgeback_franka/Looks/material_black/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * Inputs:
      * 'diffuse_tint' [color3f] = '(0.194, 0.194, 0.194)'
      * 'diffuse_color_constant' [color3f] = '(0.150, 0.150, 0.150)'

---

### /World/ridgeback_franka/Looks/material_dark_grey

* **Prim路径 (Prim Path):**/World/ridgeback_franka/Looks/material_dark_grey
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/ridgeback_franka/Looks/material_dark_grey/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/ridgeback_franka/Looks/material_dark_grey/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * Inputs:
      * 'diffuse_color_constant' [color3f] = '(0.200, 0.200, 0.200)'

---

### /World/ridgeback_franka/Looks/material_grasp_loc_color

* **Prim路径 (Prim Path):**/World/ridgeback_franka/Looks/material_grasp_loc_color
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/ridgeback_franka/Looks/material_grasp_loc_color/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/ridgeback_franka/Looks/material_grasp_loc_color/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * Inputs:
      * 'diffuse_color_constant' [color3f] = '(0.900, 0.000, 0.000)'

---

### /World/ridgeback_franka/Looks/material_light_grey

* **Prim路径 (Prim Path):**/World/ridgeback_franka/Looks/material_light_grey
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/ridgeback_franka/Looks/material_light_grey/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/ridgeback_franka/Looks/material_light_grey/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * Inputs:
      * 'diffuse_color_constant' [color3f] = '(0.400, 0.400, 0.400)'

---

### /World/ridgeback_franka/Looks/material_panda_white

* **Prim路径 (Prim Path):**/World/ridgeback_franka/Looks/material_panda_white
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/ridgeback_franka/Looks/material_panda_white/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/ridgeback_franka/Looks/material_panda_white/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * Inputs:
      * 'diffuse_color_constant' [color3f] = '(0.900, 0.900, 0.900)'

---

### /World/ridgeback_franka/Looks/material_red

* **Prim路径 (Prim Path):**/World/ridgeback_franka/Looks/material_red
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/ridgeback_franka/Looks/material_red/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/ridgeback_franka/Looks/material_red/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * Inputs:
      * 'diffuse_color_constant' [color3f] = '(0.800, 0.000, 0.000)'

---

### /World/ridgeback_franka/Looks/material_white

* **Prim路径 (Prim Path):**/World/ridgeback_franka/Looks/material_white
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/ridgeback_franka/Looks/material_white/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/ridgeback_franka/Looks/material_white/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * Inputs:
      * 'diffuse_color_constant' [color3f] = '(0.900, 0.900, 0.900)'

---

### /World/ridgeback_franka/Looks/material_yellow

* **Prim路径 (Prim Path):**/World/ridgeback_franka/Looks/material_yellow
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/ridgeback_franka/Looks/material_yellow/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/ridgeback_franka/Looks/material_yellow/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * Inputs:
      * 'diffuse_tint' [color3f] = '(0.679, 0.679, 0.679)'
      * 'diffuse_color_constant' [color3f] = '(0.800, 0.800, 0.000)'

---

### /World/ridgeback_franka/Looks/material_Face636_001

* **Prim路径 (Prim Path):**/World/ridgeback_franka/Looks/material_Face636_001
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/ridgeback_franka/Looks/material_Face636_001/Shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/ridgeback_franka/Looks/material_Face636_001/Shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * Inputs:
      * 'diffuse_color_constant' [color3f] = '(0.902, 0.922, 0.929)'
      * 'emissive_color' [color3f] = '(0.000, 0.000, 0.000)'

---

### /World/ridgeback_franka/Looks/material_Part__Feature017_001

* **Prim路径 (Prim Path):**/World/ridgeback_franka/Looks/material_Part__Feature017_001
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/ridgeback_franka/Looks/material_Part__Feature017_001/Shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/ridgeback_franka/Looks/material_Part__Feature017_001/Shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * Inputs:
      * 'diffuse_color_constant' [color3f] = '(1.000, 1.000, 1.000)'
      * 'emissive_color' [color3f] = '(0.000, 0.000, 0.000)'

---

### /World/ridgeback_franka/Looks/material_Part__Feature019_001

* **Prim路径 (Prim Path):**/World/ridgeback_franka/Looks/material_Part__Feature019_001
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/ridgeback_franka/Looks/material_Part__Feature019_001/Shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/ridgeback_franka/Looks/material_Part__Feature019_001/Shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * Inputs:
      * 'diffuse_color_constant' [color3f] = '(1.000, 1.000, 1.000)'
      * 'emissive_color' [color3f] = '(0.000, 0.000, 0.000)'

---

### /World/ridgeback_franka/Looks/material_Part__Feature023_001

* **Prim路径 (Prim Path):**/World/ridgeback_franka/Looks/material_Part__Feature023_001
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/ridgeback_franka/Looks/material_Part__Feature023_001/Shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/ridgeback_franka/Looks/material_Part__Feature023_001/Shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * Inputs:
      * 'diffuse_color_constant' [color3f] = '(0.251, 0.251, 0.251)'
      * 'emissive_color' [color3f] = '(0.000, 0.000, 0.000)'

---

### /World/ridgeback_franka/Looks/material_Part__Feature_001

* **Prim路径 (Prim Path):**/World/ridgeback_franka/Looks/material_Part__Feature_001
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/ridgeback_franka/Looks/material_Part__Feature_001/Shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/ridgeback_franka/Looks/material_Part__Feature_001/Shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * Inputs:
      * 'diffuse_color_constant' [color3f] = '(1.000, 1.000, 1.000)'
      * 'emissive_color' [color3f] = '(0.000, 0.000, 0.000)'

---

### /World/ridgeback_franka/Looks/material_Part__Feature024

* **Prim路径 (Prim Path):**/World/ridgeback_franka/Looks/material_Part__Feature024
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/ridgeback_franka/Looks/material_Part__Feature024/Shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/ridgeback_franka/Looks/material_Part__Feature024/Shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * Inputs:
      * 'diffuse_color_constant' [color3f] = '(1.000, 1.000, 1.000)'
      * 'emissive_color' [color3f] = '(0.000, 0.000, 0.000)'

---

### /World/ridgeback_franka/Looks/material_Part__Feature001_010_001_002

* **Prim路径 (Prim Path):**/World/ridgeback_franka/Looks/material_Part__Feature001_010_001_002
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/ridgeback_franka/Looks/material_Part__Feature001_010_001_002/Shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/ridgeback_franka/Looks/material_Part__Feature001_010_001_002/Shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * Inputs:
      * 'diffuse_color_constant' [color3f] = '(1.000, 1.000, 1.000)'
      * 'emissive_color' [color3f] = '(0.000, 0.000, 0.000)'

---

### /World/ridgeback_franka/Looks/material_Part__Feature_001_001_001_002

* **Prim路径 (Prim Path):**/World/ridgeback_franka/Looks/material_Part__Feature_001_001_001_002
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/ridgeback_franka/Looks/material_Part__Feature_001_001_001_002/Shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/ridgeback_franka/Looks/material_Part__Feature_001_001_001_002/Shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * Inputs:
      * 'diffuse_color_constant' [color3f] = '(0.251, 0.251, 0.251)'
      * 'emissive_color' [color3f] = '(0.000, 0.000, 0.000)'

---

### /World/ridgeback_franka/Looks/material_Part__Feature001_001_003_001

* **Prim路径 (Prim Path):**/World/ridgeback_franka/Looks/material_Part__Feature001_001_003_001
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/ridgeback_franka/Looks/material_Part__Feature001_001_003_001/Shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/ridgeback_franka/Looks/material_Part__Feature001_001_003_001/Shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * Inputs:
      * 'diffuse_color_constant' [color3f] = '(1.000, 1.000, 1.000)'
      * 'emissive_color' [color3f] = '(0.000, 0.000, 0.000)'

---

### /World/ridgeback_franka/Looks/material_Part__Feature002_001_003_001

* **Prim路径 (Prim Path):**/World/ridgeback_franka/Looks/material_Part__Feature002_001_003_001
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/ridgeback_franka/Looks/material_Part__Feature002_001_003_001/Shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/ridgeback_franka/Looks/material_Part__Feature002_001_003_001/Shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * Inputs:
      * 'diffuse_color_constant' [color3f] = '(0.251, 0.251, 0.251)'
      * 'emissive_color' [color3f] = '(0.000, 0.000, 0.000)'

---

### /World/ridgeback_franka/Looks/material_Part__Feature_002_004_003

* **Prim路径 (Prim Path):**/World/ridgeback_franka/Looks/material_Part__Feature_002_004_003
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/ridgeback_franka/Looks/material_Part__Feature_002_004_003/Shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/ridgeback_franka/Looks/material_Part__Feature_002_004_003/Shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * Inputs:
      * 'diffuse_color_constant' [color3f] = '(1.000, 1.000, 1.000)'
      * 'emissive_color' [color3f] = '(0.000, 0.000, 0.000)'

---

### /World/ridgeback_franka/Looks/material_Shell001_001_001_003

* **Prim路径 (Prim Path):**/World/ridgeback_franka/Looks/material_Shell001_001_001_003
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/ridgeback_franka/Looks/material_Shell001_001_001_003/Shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/ridgeback_franka/Looks/material_Shell001_001_001_003/Shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * Inputs:
      * 'diffuse_color_constant' [color3f] = '(0.250, 0.250, 0.250)'
      * 'emissive_color' [color3f] = '(0.000, 0.000, 0.000)'

---

### /World/ridgeback_franka/Looks/material_Face064_002_001_002_001

* **Prim路径 (Prim Path):**/World/ridgeback_franka/Looks/material_Face064_002_001_002_001
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/ridgeback_franka/Looks/material_Face064_002_001_002_001/Shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/ridgeback_franka/Looks/material_Face064_002_001_002_001/Shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * Inputs:
      * 'diffuse_color_constant' [color3f] = '(1.000, 0.000, 0.000)'
      * 'emissive_color' [color3f] = '(0.000, 0.000, 0.000)'

---

### /World/ridgeback_franka/Looks/material_Face065_002_001_002_001

* **Prim路径 (Prim Path):**/World/ridgeback_franka/Looks/material_Face065_002_001_002_001
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/ridgeback_franka/Looks/material_Face065_002_001_002_001/Shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/ridgeback_franka/Looks/material_Face065_002_001_002_001/Shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * Inputs:
      * 'diffuse_color_constant' [color3f] = '(0.000, 1.000, 0.000)'
      * 'emissive_color' [color3f] = '(0.000, 0.000, 0.000)'

---

### /World/ridgeback_franka/Looks/material_Face374_002_001_002_001

* **Prim路径 (Prim Path):**/World/ridgeback_franka/Looks/material_Face374_002_001_002_001
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/ridgeback_franka/Looks/material_Face374_002_001_002_001/Shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/ridgeback_franka/Looks/material_Face374_002_001_002_001/Shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * Inputs:
      * 'diffuse_color_constant' [color3f] = '(1.000, 1.000, 1.000)'
      * 'emissive_color' [color3f] = '(0.000, 0.000, 0.000)'

---

### /World/ridgeback_franka/Looks/material_Face539_002_001_002_001

* **Prim路径 (Prim Path):**/World/ridgeback_franka/Looks/material_Face539_002_001_002_001
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/ridgeback_franka/Looks/material_Face539_002_001_002_001/Shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/ridgeback_franka/Looks/material_Face539_002_001_002_001/Shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * Inputs:
      * 'diffuse_color_constant' [color3f] = '(0.251, 0.251, 0.251)'
      * 'emissive_color' [color3f] = '(0.000, 0.000, 0.000)'

---

### /World/ridgeback_franka/Looks/material_Shell006_003_002_001

* **Prim路径 (Prim Path):**/World/ridgeback_franka/Looks/material_Shell006_003_002_001
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/ridgeback_franka/Looks/material_Shell006_003_002_001/Shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/ridgeback_franka/Looks/material_Shell006_003_002_001/Shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * Inputs:
      * 'diffuse_color_constant' [color3f] = '(0.902, 0.922, 0.929)'
      * 'emissive_color' [color3f] = '(0.000, 0.000, 0.000)'

---

### /World/ridgeback_franka/Looks/material_Shell007_002_002_001

* **Prim路径 (Prim Path):**/World/ridgeback_franka/Looks/material_Shell007_002_002_001
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/ridgeback_franka/Looks/material_Shell007_002_002_001/Shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/ridgeback_franka/Looks/material_Shell007_002_002_001/Shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * Inputs:
      * 'diffuse_color_constant' [color3f] = '(0.250, 0.250, 0.250)'
      * 'emissive_color' [color3f] = '(0.000, 0.000, 0.000)'

---

### /World/ridgeback_franka/Looks/material_Union001_001_001_002_001

* **Prim路径 (Prim Path):**/World/ridgeback_franka/Looks/material_Union001_001_001_002_001
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/ridgeback_franka/Looks/material_Union001_001_001_002_001/Shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/ridgeback_franka/Looks/material_Union001_001_001_002_001/Shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * Inputs:
      * 'diffuse_color_constant' [color3f] = '(0.039, 0.541, 0.780)'
      * 'emissive_color' [color3f] = '(0.000, 0.000, 0.000)'

---

### /World/ridgeback_franka/Looks/material_Part__Mirroring001_004_002

* **Prim路径 (Prim Path):**/World/ridgeback_franka/Looks/material_Part__Mirroring001_004_002
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/ridgeback_franka/Looks/material_Part__Mirroring001_004_002/Shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/ridgeback_franka/Looks/material_Part__Mirroring001_004_002/Shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * Inputs:
      * 'diffuse_color_constant' [color3f] = '(0.251, 0.251, 0.251)'
      * 'emissive_color' [color3f] = '(0.000, 0.000, 0.000)'

---

### /World/ridgeback_franka/Looks/material_Part__Mirroring002_004_001

* **Prim路径 (Prim Path):**/World/ridgeback_franka/Looks/material_Part__Mirroring002_004_001
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/ridgeback_franka/Looks/material_Part__Mirroring002_004_001/Shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/ridgeback_franka/Looks/material_Part__Mirroring002_004_001/Shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * Inputs:
      * 'diffuse_color_constant' [color3f] = '(0.251, 0.251, 0.251)'
      * 'emissive_color' [color3f] = '(0.000, 0.000, 0.000)'

---

### /World/ridgeback_franka/Looks/material_Part__Mirroring004_004_002

* **Prim路径 (Prim Path):**/World/ridgeback_franka/Looks/material_Part__Mirroring004_004_002
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/ridgeback_franka/Looks/material_Part__Mirroring004_004_002/Shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/ridgeback_franka/Looks/material_Part__Mirroring004_004_002/Shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * Inputs:
      * 'diffuse_color_constant' [color3f] = '(1.000, 1.000, 1.000)'
      * 'emissive_color' [color3f] = '(0.000, 0.000, 0.000)'

---

### /World/ridgeback_franka/Looks/material_Part__Mirroring_004_001

* **Prim路径 (Prim Path):**/World/ridgeback_franka/Looks/material_Part__Mirroring_004_001
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/ridgeback_franka/Looks/material_Part__Mirroring_004_001/Shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/ridgeback_franka/Looks/material_Part__Mirroring_004_001/Shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * Inputs:
      * 'diffuse_color_constant' [color3f] = '(0.898, 0.918, 0.929)'
      * 'emissive_color' [color3f] = '(0.000, 0.000, 0.000)'

---

### /World/ridgeback_franka/Looks/material_Part__Feature001_008_005

* **Prim路径 (Prim Path):**/World/ridgeback_franka/Looks/material_Part__Feature001_008_005
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/ridgeback_franka/Looks/material_Part__Feature001_008_005/Shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/ridgeback_franka/Looks/material_Part__Feature001_008_005/Shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * Inputs:
      * 'diffuse_color_constant' [color3f] = '(0.251, 0.251, 0.251)'
      * 'emissive_color' [color3f] = '(0.000, 0.000, 0.000)'

---

### /World/ridgeback_franka/Looks/material_Part__Feature002_005_005

* **Prim路径 (Prim Path):**/World/ridgeback_franka/Looks/material_Part__Feature002_005_005
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/ridgeback_franka/Looks/material_Part__Feature002_005_005/Shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/ridgeback_franka/Looks/material_Part__Feature002_005_005/Shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * Inputs:
      * 'diffuse_color_constant' [color3f] = '(0.902, 0.922, 0.929)'
      * 'emissive_color' [color3f] = '(0.000, 0.000, 0.000)'

---

### /World/ridgeback_franka/Looks/material_Part__Feature005_001_005

* **Prim路径 (Prim Path):**/World/ridgeback_franka/Looks/material_Part__Feature005_001_005
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/ridgeback_franka/Looks/material_Part__Feature005_001_005/Shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/ridgeback_franka/Looks/material_Part__Feature005_001_005/Shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * Inputs:
      * 'diffuse_color_constant' [color3f] = '(1.000, 1.000, 1.000)'
      * 'emissive_color' [color3f] = '(0.000, 0.000, 0.000)'

---

### /World/ridgeback_franka/Looks/material_Part__Feature_009_005

* **Prim路径 (Prim Path):**/World/ridgeback_franka/Looks/material_Part__Feature_009_005
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/ridgeback_franka/Looks/material_Part__Feature_009_005/Shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/ridgeback_franka/Looks/material_Part__Feature_009_005/Shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * Inputs:
      * 'diffuse_color_constant' [color3f] = '(0.251, 0.251, 0.251)'
      * 'emissive_color' [color3f] = '(0.000, 0.000, 0.000)'

---

### /World/ridgeback_franka/Looks/material_Part__Feature001_006

* **Prim路径 (Prim Path):**/World/ridgeback_franka/Looks/material_Part__Feature001_006
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/ridgeback_franka/Looks/material_Part__Feature001_006/Shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/ridgeback_franka/Looks/material_Part__Feature001_006/Shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * Inputs:
      * 'diffuse_color_constant' [color3f] = '(0.902, 0.922, 0.929)'
      * 'emissive_color' [color3f] = '(0.000, 0.000, 0.000)'

---

### /World/ridgeback_franka/Looks/material_Part__Feature_007

* **Prim路径 (Prim Path):**/World/ridgeback_franka/Looks/material_Part__Feature_007
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/ridgeback_franka/Looks/material_Part__Feature_007/Shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/ridgeback_franka/Looks/material_Part__Feature_007/Shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * Inputs:
      * 'diffuse_color_constant' [color3f] = '(0.251, 0.251, 0.251)'
      * 'emissive_color' [color3f] = '(0.000, 0.000, 0.000)'

---
