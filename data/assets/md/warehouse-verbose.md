# USDA场景描述文档:warehouse.usda

## 1.场景元数据(Scene Metadata)

* **USDA文件路径(USDA File Path):**`/media/simple/another_Documents/isaacsim_assets/scenedata/warehouse.usda`
* **默认Prim (Default Prim):**'World'
* **单位与坐标系 (Units & Coordinate System):**
  * **米(Meters Per Unit):**1.0
  * **Up Axis:**Z
* **场景描述(Scene Describe):** 该场景展现了一个高度集成化且具备强柔性特征的现代智能仓储作业区，其空间格局与设备排布深刻体现了工业4.0时代下的数字化物流规划逻辑。在整体布局与空间规划方面，该场景采用了功能导向的非对称式排布。车间地面由灰色大理石质感的长方形瓷砖铺设，间杂着红褐色的天然纹理，展现出极高的工业洁净度与空间质感。厂区在空间上被划分为高密度存储区、自动化分拣区以及灵活的AGV中转路径。背景墙面由深褐色的工业金属板材构成，上方配有条带状的自然采光窗，整体环境呈现出一种紧凑而有序的专业化氛围。这种规划通过明确的区域功能界定，将静态的仓储空间转变为动态的物流处理节点。核心工业设备之首是位于画面右侧与左侧的大型仓储货架系统。这些货架采用深蓝色金属骨架与黑色承重横梁组合，结构稳固。右侧货架呈现阶梯状的高度分布，分为三层存储结构，顶层放置着大型木质包装箱，中层与底层则堆放着规格统一的棕色纸质包装盒及中型木箱。货架的排布方式最大限度地利用了垂直空间，形成了密集的货位矩阵。左侧货架则更偏向于分拣辅助功能，其横梁较低且排布紧密，上方放置着待处理的纸箱，通过多层平面的延伸，构成了从存储到分拣的过渡空间。该场景中最引人注目的工业设备是位于中央区域的复合型自动化移动机器人（AMR/AGV）。这台机器人具有宽大的白色长方形底座，顶部安装了一个带有三块绿色作业区域的高性能分拣平台，平台上正运载着一个蓝色半透明周转箱。更为先进的是，底座上方集成了一台银灰色的六轴协作机械臂，机械臂末端配备了精密的抓取机构。这种“底座+平台+机械臂”的三合一设备排布方式，打破了传统固定式产线的束缚，使其能够自主导航至货架前完成精准的货位存取，并实现区域间的灵活配送。紧邻移动机器人的是一套多样化的工业搬运机械体系。画面中央分布着一台蓝色与灰色相间的自动化前移式叉车（Reach Truck），其车身紧凑，具有多级可伸缩的门架系统，专门负责高层货架的精准插取作业。旁边则是一台低矮的小型灰色自动叉车（Walkie Stacker），其货叉部分贴地运行，适用于地面托盘的短距离移位。此外，地面上还停放着一台小巧的黄色穿梭车（Shuttle），它通常与货架内部的轨道系统配合使用。这些设备在位置上呈现出一种交错互补的排布态势，展示了仓储中心针对不同高度、不同载荷物料的多层级处理能力。在工装设备与物料载体方面，场景中大量使用了标准化的工业包装。货架上密布着各类规格的木质周转箱，箱体带有明显的加固木条和工业印记，显示其具有极强的耐冲击性。同时，地面上散落着几个蓝色半透明的塑料周转箱，其箱体带有格栅状加强筋，主要用于轻量化零部件的零散存放。在画面左下角的货架层板上，可以看到整齐排列的棕色纸箱，这些纸箱作为终端包装，是物流循环中的最小单元。这些工装设备与机械设备在数量与排布上保持着严密的对应关系，体现了物流单元化、标准化的设计初衷。总结该场景的整体规划结构，可以看到一种基于数字化映射的精细化作业模式。高大稳固的蓝色货架作为仓储的支撑“骨架”，界定了作业的物理边界；多维度的自动化叉车与穿梭车作为“神经末梢”，完成了垂直与水平的空间触达；而处于中心位置的协作式移动机器人则是整个场景的“智慧核心”，通过其强大的自主作业能力，将货架、叉车与物料载体紧密连接在一起。这种排布方式不仅极大提升了单位面积的存储密度，更通过多机协作实现了物料的无缝流转。整个场景客观真实地还原了一个无人的、智能的、具备快速响应能力的现代工业仓储环境，每一台设备的分布位置都经过了精确的路径优化与效率模拟，展现出工业设计中极致的逻辑美感。
* **设备数量(Device Number):**
  * **Scene: 1**
  * **IndustrialRobot: 1**
  * **Workbench: 0**
  * **Conveyor: 0**
  * **AGV: 1**
  * **Forklift: 2**
  * **Box: 54**
  * **Rack: 8**
  * **Pallet: 0**
  * **Part: 0**
  * **Decoration: 0**

## 2.场景对象层级(Scene Hierarchy)

* World (Xform)
  * factory (Xform)
    * Materials (Scope)
      * WindowsIndustrial_frontSolid_OpenWindows_Mat (Material)
        * pbr_shader (Shader)
        * uvset0 (Shader)
        * tex_base (Shader)
      * WindowsIndustrial_frontSolid_Mat (Material)
        * pbr_shader (Shader)
        * uvset0 (Shader)
        * tex_base (Shader)
      * WindowsIndustrial_frontDoorclosed_Mat (Material)
        * pbr_shader (Shader)
        * uvset0 (Shader)
        * tex_base (Shader)
      * WindowsIndustrial_frontDoorOpen_Mat (Material)
        * pbr_shader (Shader)
        * uvset0 (Shader)
        * tex_base (Shader)
      * WindowsIndustrial_front_Mat (Material)
        * pbr_shader (Shader)
        * uvset0 (Shader)
        * tex_base (Shader)
      * _1___Default (Material)
        * pbr_shader (Shader)
        * uvset0 (Shader)
        * tex_base (Shader)
      * _0___Default (Material)
        * pbr_shader (Shader)
        * uvset0 (Shader)
        * tex_base (Shader)
    * Meshes (Xform)
      * Sketchfab_model (Xform)
        * cc020ec10d3e484ab6eb350963eb38d0_fbx (Xform)
          * RootNode (Xform)
            * Factory002 (Xform)
              * Factory002_WindowsIndustrial_frontSolid_OpenWindows_Mat_0 (Xform)
                * Factory002_WindowsIndustrial_frontSolid_OpenWindows_Mat_0 (Mesh)
              * Factory002_WindowsIndustrial_frontSolid_Mat_0 (Xform)
                * Factory002_WindowsIndustrial_frontSolid_Mat_0 (Mesh)
              * Factory002_WindowsIndustrial_frontDoorclosed_Mat_0 (Xform)
                * Factory002_WindowsIndustrial_frontDoorclosed_Mat_0 (Mesh)
              * Factory002_WindowsIndustrial_frontDoorOpen_Mat_0 (Xform)
                * Factory002_WindowsIndustrial_frontDoorOpen_Mat_0 (Mesh)
              * Factory002_WindowsIndustrial_front_Mat_0 (Xform)
                * Factory002_WindowsIndustrial_front_Mat_0 (Mesh)
              * Factory002_11___Default_0 (Xform)
                * Factory002_11___Default_0 (Mesh)
            * Object001 (Xform)
              * Object001_20___Default_0 (Xform)
                * Object001_20___Default_0 (Mesh)
  * RackLargeEmpty_A1 (Xform)
    * RackLargeEmpty_A1 (Xform)
      * RackLegs_A1_2x4_01 (Mesh)
      * RackShelf_A2_2x4_01 (Mesh)
      * RackShelf_A2_2x4_02 (Mesh)
    * Looks (Scope)
      * Shelf (Material)
        * Shader (Shader)
  * carton (Xform)
    * Materials (Scope)
      * _6___Default (Material)
        * pbr_shader (Shader)
        * uvset0 (Shader)
        * tex_base (Shader)
    * Meshes (Xform)
      * Sketchfab_model (Xform)
        * f49ad5edc352496894d3a02181012422_fbx (Xform)
          * RootNode (Xform)
            * Box072 (Xform)
              * Box072_06___Default_0 (Xform)
                * Box072_06___Default_0 (Mesh)
  * carton_01 (Xform)
    * Materials (Scope)
      * _6___Default (Material)
        * pbr_shader (Shader)
        * uvset0 (Shader)
        * tex_base (Shader)
    * Meshes (Xform)
      * Sketchfab_model (Xform)
        * f49ad5edc352496894d3a02181012422_fbx (Xform)
          * RootNode (Xform)
            * Box072 (Xform)
              * Box072_06___Default_0 (Xform)
                * Box072_06___Default_0 (Mesh)
  * carton_02 (Xform)
    * Materials (Scope)
      * _6___Default (Material)
        * pbr_shader (Shader)
        * uvset0 (Shader)
        * tex_base (Shader)
    * Meshes (Xform)
      * Sketchfab_model (Xform)
        * f49ad5edc352496894d3a02181012422_fbx (Xform)
          * RootNode (Xform)
            * Box072 (Xform)
              * Box072_06___Default_0 (Xform)
                * Box072_06___Default_0 (Mesh)
  * carton_03 (Xform)
    * Materials (Scope)
      * _6___Default (Material)
        * pbr_shader (Shader)
        * uvset0 (Shader)
        * tex_base (Shader)
    * Meshes (Xform)
      * Sketchfab_model (Xform)
        * f49ad5edc352496894d3a02181012422_fbx (Xform)
          * RootNode (Xform)
            * Box072 (Xform)
              * Box072_06___Default_0 (Xform)
                * Box072_06___Default_0 (Mesh)
  * WoodenCrate_A1 (Xform)
    * WoodenCrate_A1 (Mesh)
    * Looks (Scope)
      * Crate (Material)
        * Shader (Shader)
  * WoodenCrate_A2 (Xform)
    * WoodenCrate_A2 (Mesh)
    * Looks (Scope)
      * Crate (Material)
        * Shader (Shader)
  * WoodenCrate_B1 (Xform)
    * WoodenCrate_B1 (Mesh)
    * Looks (Scope)
      * Crate (Material)
        * Shader (Shader)
  * WoodenCrate_B2 (Xform)
    * WoodenCrate_B2 (Mesh)
    * Looks (Scope)
      * Crate (Material)
        * Shader (Shader)
  * RackLargeEmpty_A1_01 (Xform)
    * RackLargeEmpty_A1 (Xform)
      * RackLegs_A1_2x4_01 (Mesh)
      * RackShelf_A2_2x4_01 (Mesh)
      * RackShelf_A2_2x4_02 (Mesh)
    * Looks (Scope)
      * Shelf (Material)
        * Shader (Shader)
  * RackSmallEmpty_A2 (Xform)
    * RackSmallEmpty_A2 (Xform)
      * RackLegs_A1_1x2_01 (Mesh)
      * RackShelf_A2_1x2_01 (Mesh)
      * RackShelf_A1_1x2_02 (Mesh)
    * Looks (Scope)
      * Shelf (Material)
        * Shader (Shader)
  * Cardbox_A1 (Xform)
    * Cardbox_A1 (Mesh)
    * Looks (Scope)
      * Cardboard_A (Material)
        * Shader (Shader)
  * Cardbox_A1_01 (Xform)
    * Cardbox_A1 (Mesh)
    * Looks (Scope)
      * Cardboard_A (Material)
        * Shader (Shader)
  * Cardbox_A1_02 (Xform)
    * Cardbox_A1 (Mesh)
    * Looks (Scope)
      * Cardboard_A (Material)
        * Shader (Shader)
  * Cardbox_B3 (Xform)
    * Cardbox_B3 (Mesh)
    * Looks (Scope)
      * Cardboard_B3 (Material)
        * Shader (Shader)
  * Cardbox_C1 (Xform)
    * Cardbox_C1 (Mesh)
    * Looks (Scope)
      * Cardboard_C1 (Material)
        * Shader (Shader)
  * Cardbox_B3_01 (Xform)
    * Cardbox_B3 (Mesh)
    * Looks (Scope)
      * Cardboard_B3 (Material)
        * Shader (Shader)
  * Cardbox_C2 (Xform)
    * Cardbox_C2 (Mesh)
    * Looks (Scope)
      * Cardboard_C2 (Material)
        * Shader (Shader)
  * RackSmallEmpty_A2_01 (Xform)
    * RackSmallEmpty_A2 (Xform)
      * RackLegs_A1_1x2_01 (Mesh)
      * RackShelf_A2_1x2_01 (Mesh)
      * RackShelf_A1_1x2_02 (Mesh)
    * Looks (Scope)
      * Shelf (Material)
        * Shader (Shader)
  * RackLongEmpty_A2 (Xform)
    * RackLongEmpty_A2_001 (Xform)
      * RackLegs_A1_1x4_01 (Mesh)
      * RackShelf_A2_1x4_01 (Mesh)
      * RackShelf_A2_1x4_02 (Mesh)
      * RackShelf_A1_1x4_03 (Mesh)
    * Looks (Scope)
      * Shelf (Material)
        * Shader (Shader)
  * RackLongEmpty_A2_01 (Xform)
    * RackLongEmpty_A2_001 (Xform)
      * RackLegs_A1_1x4_01 (Mesh)
      * RackShelf_A2_1x4_01 (Mesh)
      * RackShelf_A2_1x4_02 (Mesh)
      * RackShelf_A1_1x4_03 (Mesh)
    * Looks (Scope)
      * Shelf (Material)
        * Shader (Shader)
  * RackLargeEmpty_A1_02 (Xform)
    * RackLargeEmpty_A1 (Xform)
      * RackLegs_A1_2x4_01 (Mesh)
      * RackShelf_A2_2x4_01 (Mesh)
      * RackShelf_A2_2x4_02 (Mesh)
    * Looks (Scope)
      * Shelf (Material)
        * Shader (Shader)
  * WoodenCrate_B2_01 (Xform)
    * WoodenCrate_B2 (Mesh)
    * Looks (Scope)
      * Crate (Material)
        * Shader (Shader)
  * WoodenCrate_B1_01 (Xform)
    * WoodenCrate_B1 (Mesh)
    * Looks (Scope)
      * Crate (Material)
        * Shader (Shader)
  * WoodenCrate_A2_01 (Xform)
    * WoodenCrate_A2 (Mesh)
    * Looks (Scope)
      * Crate (Material)
        * Shader (Shader)
  * WoodenCrate_A1_01 (Xform)
    * WoodenCrate_A1 (Mesh)
    * Looks (Scope)
      * Crate (Material)
        * Shader (Shader)
  * RackLargeEmpty_A1_03 (Xform)
    * RackLargeEmpty_A1 (Xform)
      * RackLegs_A1_2x4_01 (Mesh)
      * RackShelf_A2_2x4_01 (Mesh)
      * RackShelf_A2_2x4_02 (Mesh)
    * Looks (Scope)
      * Shelf (Material)
        * Shader (Shader)
  * carton_04 (Xform)
    * Materials (Scope)
      * _6___Default (Material)
        * pbr_shader (Shader)
        * uvset0 (Shader)
        * tex_base (Shader)
    * Meshes (Xform)
      * Sketchfab_model (Xform)
        * f49ad5edc352496894d3a02181012422_fbx (Xform)
          * RootNode (Xform)
            * Box072 (Xform)
              * Box072_06___Default_0 (Xform)
                * Box072_06___Default_0 (Mesh)
  * carton_05 (Xform)
    * Materials (Scope)
      * _6___Default (Material)
        * pbr_shader (Shader)
        * uvset0 (Shader)
        * tex_base (Shader)
    * Meshes (Xform)
      * Sketchfab_model (Xform)
        * f49ad5edc352496894d3a02181012422_fbx (Xform)
          * RootNode (Xform)
            * Box072 (Xform)
              * Box072_06___Default_0 (Xform)
                * Box072_06___Default_0 (Mesh)
  * carton_06 (Xform)
    * Materials (Scope)
      * _6___Default (Material)
        * pbr_shader (Shader)
        * uvset0 (Shader)
        * tex_base (Shader)
    * Meshes (Xform)
      * Sketchfab_model (Xform)
        * f49ad5edc352496894d3a02181012422_fbx (Xform)
          * RootNode (Xform)
            * Box072 (Xform)
              * Box072_06___Default_0 (Xform)
                * Box072_06___Default_0 (Mesh)
  * carton_07 (Xform)
    * Materials (Scope)
      * _6___Default (Material)
        * pbr_shader (Shader)
        * uvset0 (Shader)
        * tex_base (Shader)
    * Meshes (Xform)
      * Sketchfab_model (Xform)
        * f49ad5edc352496894d3a02181012422_fbx (Xform)
          * RootNode (Xform)
            * Box072 (Xform)
              * Box072_06___Default_0 (Xform)
                * Box072_06___Default_0 (Mesh)
  * Cardbox_C3 (Xform)
    * Cardbox_C3 (Mesh)
    * Looks (Scope)
      * Cardboard_C3 (Material)
        * Shader (Shader)
  * Cardbox_C2_01 (Xform)
    * Cardbox_C2 (Mesh)
    * Looks (Scope)
      * Cardboard_C2 (Material)
        * Shader (Shader)
  * Cardbox_B3_02 (Xform)
    * Cardbox_B3 (Mesh)
    * Looks (Scope)
      * Cardboard_B3 (Material)
        * Shader (Shader)
  * Cardbox_B2 (Xform)
    * Cardbox_B2 (Mesh)
    * Looks (Scope)
      * Cardboard_B2 (Material)
        * Shader (Shader)
  * Cardbox_B1 (Xform)
    * Cardbox_B1 (Mesh)
    * Looks (Scope)
      * Cardboard_B1 (Material)
        * Shader (Shader)
  * Cardbox_A3 (Xform)
    * Cardbox_A3 (Mesh)
    * Looks (Scope)
      * Cardboard_A3 (Material)
        * Shader (Shader)
  * Cardbox_A2 (Xform)
    * Cardbox_A2 (Mesh)
    * Looks (Scope)
      * Cardboard_A2 (Material)
        * Shader (Shader)
  * Cardbox_A1_03 (Xform)
    * Cardbox_A1 (Mesh)
    * Looks (Scope)
      * Cardboard_A (Material)
        * Shader (Shader)
  * AGV_ready_1 (Xform)
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
  * AGV (Xform)
    * Materials (Scope)
      * Tyre_Bake1_baked (Material)
        * pbr_shader (Shader)
        * uvset0 (Shader)
        * tex_base (Shader)
        * tex_metallic (Shader)
        * tex_roughness (Shader)
        * tex_normal (Shader)
      * Bolt_003_Bake1_baked (Material)
        * pbr_shader (Shader)
        * uvset0 (Shader)
        * tex_base (Shader)
        * tex_metallic (Shader)
        * tex_roughness (Shader)
        * tex_normal (Shader)
      * Bolt_004_Bake1_baked (Material)
        * pbr_shader (Shader)
        * uvset0 (Shader)
        * tex_base (Shader)
        * tex_metallic (Shader)
        * tex_roughness (Shader)
        * tex_normal (Shader)
      * Cylinder_002_Bake1_baked (Material)
        * pbr_shader (Shader)
        * uvset0 (Shader)
        * tex_base (Shader)
        * tex_metallic (Shader)
        * tex_roughness (Shader)
        * tex_normal (Shader)
      * Cylinder_003_Bake1_baked (Material)
        * pbr_shader (Shader)
        * uvset0 (Shader)
        * tex_base (Shader)
        * tex_metallic (Shader)
        * tex_roughness (Shader)
        * tex_normal (Shader)
      * Hub_002_Bake1_baked (Material)
        * pbr_shader (Shader)
        * uvset0 (Shader)
        * tex_base (Shader)
        * tex_metallic (Shader)
        * tex_roughness (Shader)
        * tex_normal (Shader)
      * Hub_003_Bake1_baked (Material)
        * pbr_shader (Shader)
        * uvset0 (Shader)
        * tex_base (Shader)
        * tex_metallic (Shader)
        * tex_roughness (Shader)
        * tex_normal (Shader)
      * Cube_Bake1_baked (Material)
        * pbr_shader (Shader)
        * uvset0 (Shader)
        * tex_base (Shader)
        * tex_metallic (Shader)
        * tex_roughness (Shader)
        * tex_normal (Shader)
      * Cube_001_Bake1_baked (Material)
        * pbr_shader (Shader)
        * uvset0 (Shader)
        * tex_base (Shader)
        * tex_metallic (Shader)
        * tex_roughness (Shader)
        * tex_normal (Shader)
      * Slice_Bake1_baked (Material)
        * pbr_shader (Shader)
        * uvset0 (Shader)
        * tex_base (Shader)
        * tex_metallic (Shader)
        * tex_roughness (Shader)
        * tex_normal (Shader)
      * Slice_001_Bake1_baked (Material)
        * pbr_shader (Shader)
        * uvset0 (Shader)
        * tex_base (Shader)
        * tex_metallic (Shader)
        * tex_roughness (Shader)
        * tex_normal (Shader)
      * Cube_002_Bake1_baked (Material)
        * pbr_shader (Shader)
        * uvset0 (Shader)
        * tex_base (Shader)
        * tex_metallic (Shader)
        * tex_roughness (Shader)
        * tex_normal (Shader)
      * Cube_003_Bake1_baked (Material)
        * pbr_shader (Shader)
        * uvset0 (Shader)
        * tex_base (Shader)
        * tex_metallic (Shader)
        * tex_roughness (Shader)
        * tex_normal (Shader)
      * Cylinder_004_Bake1_baked (Material)
        * pbr_shader (Shader)
        * uvset0 (Shader)
        * tex_base (Shader)
        * tex_metallic (Shader)
        * tex_roughness (Shader)
        * tex_normal (Shader)
      * Cylinder_006_Bake1_baked (Material)
        * pbr_shader (Shader)
        * uvset0 (Shader)
        * tex_base (Shader)
        * tex_metallic (Shader)
        * tex_roughness (Shader)
        * tex_normal (Shader)
      * Front_lambert1_0_Bake1_baked (Material)
        * pbr_shader (Shader)
        * uvset0 (Shader)
        * tex_base (Shader)
        * tex_metallic (Shader)
        * tex_roughness (Shader)
        * tex_normal (Shader)
      * pCylinder27_lambert1_0_Bake1_baked (Material)
        * pbr_shader (Shader)
        * uvset0 (Shader)
        * tex_base (Shader)
        * tex_metallic (Shader)
        * tex_roughness (Shader)
        * tex_normal (Shader)
      * polySurface35_lambert1_0_Bake1_baked (Material)
        * pbr_shader (Shader)
        * uvset0 (Shader)
        * tex_base (Shader)
        * tex_metallic (Shader)
        * tex_roughness (Shader)
        * tex_normal (Shader)
      * polySurface41_lambert1_0_Bake1_baked (Material)
        * pbr_shader (Shader)
        * uvset0 (Shader)
        * tex_base (Shader)
        * tex_metallic (Shader)
        * tex_roughness (Shader)
        * tex_normal (Shader)
      * polySurface35_lambert1_0_001_Bake1_baked (Material)
        * pbr_shader (Shader)
        * uvset0 (Shader)
        * tex_base (Shader)
        * tex_metallic (Shader)
        * tex_roughness (Shader)
        * tex_normal (Shader)
      * Slice_002_Bake1_baked (Material)
        * pbr_shader (Shader)
        * uvset0 (Shader)
        * tex_base (Shader)
        * tex_metallic (Shader)
        * tex_roughness (Shader)
        * tex_normal (Shader)
      * Slice_003_Bake1_baked (Material)
        * pbr_shader (Shader)
        * uvset0 (Shader)
        * tex_base (Shader)
        * tex_metallic (Shader)
        * tex_roughness (Shader)
        * tex_normal (Shader)
      * Body_001_Bake1_baked (Material)
        * pbr_shader (Shader)
        * uvset0 (Shader)
        * tex_base (Shader)
        * tex_metallic (Shader)
        * tex_roughness (Shader)
        * tex_normal (Shader)
      * Body_003_Bake1_baked (Material)
        * pbr_shader (Shader)
        * uvset0 (Shader)
        * tex_base (Shader)
        * tex_metallic (Shader)
        * tex_roughness (Shader)
        * tex_normal (Shader)
      * Body_004_Bake1_baked (Material)
        * pbr_shader (Shader)
        * uvset0 (Shader)
        * tex_base (Shader)
        * tex_metallic (Shader)
        * tex_roughness (Shader)
        * tex_normal (Shader)
      * Plane_Bake1_baked (Material)
        * pbr_shader (Shader)
        * uvset0 (Shader)
        * tex_base (Shader)
        * tex_metallic (Shader)
        * tex_roughness (Shader)
        * tex_normal (Shader)
      * F_Switch_ob_flipswitcha_003_Bake1_baked (Material)
        * pbr_shader (Shader)
        * uvset0 (Shader)
        * tex_base (Shader)
        * tex_metallic (Shader)
        * tex_roughness (Shader)
        * tex_normal (Shader)
      * F_Switch_ob_flipswitcha_003_001_Bake1_baked (Material)
        * pbr_shader (Shader)
        * uvset0 (Shader)
        * tex_base (Shader)
        * tex_metallic (Shader)
        * tex_roughness (Shader)
        * tex_normal (Shader)
      * F_Switch_ob_flipswitcha_003_002_Bake1_baked (Material)
        * pbr_shader (Shader)
        * uvset0 (Shader)
        * tex_base (Shader)
        * tex_metallic (Shader)
        * tex_roughness (Shader)
        * tex_normal (Shader)
    * Meshes (Xform)
      * Sketchfab_model (Xform)
        * AGV_sketchfab_fbx (Xform)
          * RootNode (Xform)
            * Tyre_Baked (Xform)
              * Tyre_Baked_Tyre_Bake1_baked_0 (Xform)
                * Tyre_Baked_Tyre_Bake1_baked_0 (Mesh)
            * Bolt_003_Baked (Xform)
              * Bolt_003_Baked_Bolt_003_Bake1_baked_0 (Xform)
                * Bolt_003_Baked_Bolt_003_Bake1_baked_0 (Mesh)
              * Bolt_003_Baked_Bolt_003_Bake1_baked_0_1 (Xform)
                * Bolt_003_Baked_Bolt_003_Bake1_baked_0 (Mesh)
            * Bolt_004_Baked (Xform)
              * Bolt_004_Baked_Bolt_004_Bake1_baked_0 (Xform)
                * Bolt_004_Baked_Bolt_004_Bake1_baked_0 (Mesh)
            * Cylinder_002_Baked (Xform)
              * Cylinder_002_Baked_Cylinder_002_Bake1_baked_0 (Xform)
                * Cylinder_002_Baked_Cylinder_002_Bake1_baked_0 (Mesh)
            * Cylinder_003_Baked (Xform)
              * Cylinder_003_Baked_Cylinder_003_Bake1_baked_0 (Xform)
                * Cylinder_003_Baked_Cylinder_003_Bake1_baked_0 (Mesh)
            * Hub_002_Baked (Xform)
              * Hub_002_Baked_Hub_002_Bake1_baked_0 (Xform)
                * Hub_002_Baked_Hub_002_Bake1_baked_0 (Mesh)
            * Hub_003_Baked (Xform)
              * Hub_003_Baked_Hub_003_Bake1_baked_0 (Xform)
                * Hub_003_Baked_Hub_003_Bake1_baked_0 (Mesh)
            * Cube_Baked (Xform)
              * Cube_Baked_Cube_Bake1_baked_0 (Xform)
                * Cube_Baked_Cube_Bake1_baked_0 (Mesh)
            * Cube_001_Baked (Xform)
              * Cube_001_Baked_Cube_001_Bake1_baked_0 (Xform)
                * Cube_001_Baked_Cube_001_Bake1_baked_0 (Mesh)
            * Slice_Baked (Xform)
              * Slice_Baked_Slice_Bake1_baked_0 (Xform)
                * Slice_Baked_Slice_Bake1_baked_0 (Mesh)
            * Slice_001_Baked (Xform)
              * Slice_001_Baked_Slice_001_Bake1_baked_0 (Xform)
                * Slice_001_Baked_Slice_001_Bake1_baked_0 (Mesh)
            * Cube_002_Baked (Xform)
              * Cube_002_Baked_Cube_002_Bake1_baked_0 (Xform)
                * Cube_002_Baked_Cube_002_Bake1_baked_0 (Mesh)
            * Cube_003_Baked (Xform)
              * Cube_003_Baked_Cube_003_Bake1_baked_0 (Xform)
                * Cube_003_Baked_Cube_003_Bake1_baked_0 (Mesh)
            * Cylinder_004_Baked (Xform)
              * Cylinder_004_Baked_Cylinder_004_Bake1_baked_0 (Xform)
                * Cylinder_004_Baked_Cylinder_004_Bake1_baked_0 (Mesh)
            * Cylinder_006_Baked (Xform)
              * Cylinder_006_Baked_Cylinder_006_Bake1_baked_0 (Xform)
                * Cylinder_006_Baked_Cylinder_006_Bake1_baked_0 (Mesh)
            * Front_lambert1_0_Baked (Xform)
              * Front_lambert1_0_Baked_Front_lambert1_0_Bake1_baked_0 (Xform)
                * Front_lambert1_0_Baked_Front_lambert1_0_Bake1_baked_0 (Mesh)
            * pCylinder27_lambert1_0_Baked (Xform)
              * pCylinder27_lambert1_0_Baked_pCylinder27_lambert1_0_Bake1_baked_0 (Xform)
                * pCylinder27_lambert1_0_Baked_pCylinder27_lambert1_0_Bake1_baked_0 (Mesh)
            * polySurface35_lambert1_0_Baked (Xform)
              * polySurface35_lambert1_0_Baked_polySurface35_lambert1_0_Bake1_baked_0 (Xform)
                * polySurface35_lambert1_0_Baked_polySurface35_lambert1_0_Bake1_baked_0 (Mesh)
            * polySurface41_lambert1_0_Baked (Xform)
              * polySurface41_lambert1_0_Baked_polySurface41_lambert1_0_Bake1_baked_0 (Xform)
                * polySurface41_lambert1_0_Baked_polySurface41_lambert1_0_Bake1_baked_0 (Mesh)
            * polySurface35_lambert1_0_001_Baked (Xform)
              * polySurface35_lambert1_0_001_Baked_polySurface35_lambert1_0_001_Bake1_baked_0 (Xform)
                * polySurface35_lambert1_0_001_Baked_polySurface35_lambert1_0_001_Bake1_baked_0 (Mesh)
            * Slice_002_Baked (Xform)
              * Slice_002_Baked_Slice_002_Bake1_baked_0 (Xform)
                * Slice_002_Baked_Slice_002_Bake1_baked_0 (Mesh)
            * Slice_003_Baked (Xform)
              * Slice_003_Baked_Slice_003_Bake1_baked_0 (Xform)
                * Slice_003_Baked_Slice_003_Bake1_baked_0 (Mesh)
            * Body_001_Baked (Xform)
              * Body_001_Baked_Body_001_Bake1_baked_0 (Xform)
                * Body_001_Baked_Body_001_Bake1_baked_0 (Mesh)
            * Body_003_Baked (Xform)
              * Body_003_Baked_Body_003_Bake1_baked_0 (Xform)
                * Body_003_Baked_Body_003_Bake1_baked_0 (Mesh)
            * Body_004_Baked (Xform)
              * Body_004_Baked_Body_004_Bake1_baked_0 (Xform)
                * Body_004_Baked_Body_004_Bake1_baked_0 (Mesh)
            * Plane_Baked (Xform)
              * Plane_Baked_Plane_Bake1_baked_0 (Xform)
                * Plane_Baked_Plane_Bake1_baked_0 (Mesh)
            * F_Switch_ob_flipswitcha_003_Baked (Xform)
              * F_Switch_ob_flipswitcha_003_Baked_F_Switch_ob_flipswitcha_003_Bake1_baked_0 (Xform)
                * F_Switch_ob_flipswitcha_003_Baked_F_Switch_ob_flipswitcha_003_Bake1_baked_0 (Mesh)
            * F_Switch_ob_flipswitcha_003_001_Baked (Xform)
              * F_Switch_ob_flipswitcha_003_001_Baked_F_Switch_ob_flipswitcha_003_001_Bake1_baked_0 (Xform)
                * F_Switch_ob_flipswitcha_003_001_Baked_F_Switch_ob_flipswitcha_003_001_Bake1_baked_0 (Mesh)
            * F_Switch_ob_flipswitcha_003_002_Baked (Xform)
              * F_Switch_ob_flipswitcha_003_002_Baked_F_Switch_ob_flipswitcha_003_002_Bake1_baked_0 (Xform)
                * F_Switch_ob_flipswitcha_003_002_Baked_F_Switch_ob_flipswitcha_003_002_Bake1_baked_0 (Mesh)
  * UR__Cobot_Mir_AMR (Xform)
    * Materials (Scope)
      * Allu_Mat_001 (Material)
        * pbr_shader (Shader)
      * Stahl_003 (Material)
        * pbr_shader (Shader)
        * uvset0 (Shader)
        * tex_base (Shader)
        * tex_metallic (Shader)
        * tex_roughness (Shader)
        * tex_normal (Shader)
      * Schwarz_metal_mat_001 (Material)
        * pbr_shader (Shader)
      * Allu_Mat_Dunkel_001 (Material)
        * pbr_shader (Shader)
        * uvset0 (Shader)
        * tex_base (Shader)
        * tex_metallic (Shader)
        * tex_roughness (Shader)
        * tex_normal (Shader)
      * Hel_Blau_Plastik_001 (Material)
        * pbr_shader (Shader)
      * Gumi_Schwarz_001 (Material)
        * pbr_shader (Shader)
      * Material_003 (Material)
        * pbr_shader (Shader)
      * _00000FF (Material)
        * pbr_shader (Shader)
      * _A0A0AFF (Material)
        * pbr_shader (Shader)
      * _E0000FF (Material)
        * pbr_shader (Shader)
      * _1585CFF_001 (Material)
        * pbr_shader (Shader)
      * _92929FF (Material)
        * pbr_shader (Shader)
      * _000FFFF (Material)
        * pbr_shader (Shader)
      * A5ADB1FF (Material)
        * pbr_shader (Shader)
      * B28C01FF (Material)
        * pbr_shader (Shader)
      * FFFF00FF (Material)
        * pbr_shader (Shader)
      * _04040FF (Material)
        * pbr_shader (Shader)
      * BFBFBFFF (Material)
        * pbr_shader (Shader)
      * CBD2EEFF (Material)
        * pbr_shader (Shader)
      * FFFFFFFF (Material)
        * pbr_shader (Shader)
      * _85858FF (Material)
        * pbr_shader (Shader)
      * BEBEBEFF (Material)
        * pbr_shader (Shader)
      * B09C86FF (Material)
        * pbr_shader (Shader)
      * AAAAAAFF (Material)
        * pbr_shader (Shader)
      * _0FF0CFF (Material)
        * pbr_shader (Shader)
      * FEFEFFFF (Material)
        * pbr_shader (Shader)
      * _99999FF (Material)
        * pbr_shader (Shader)
      * _0FF00FF (Material)
        * pbr_shader (Shader)
      * E6C76CFF (Material)
        * pbr_shader (Shader)
      * _0007FFF (Material)
        * pbr_shader (Shader)
      * FF0000FF (Material)
        * pbr_shader (Shader)
      * F47F0AFF (Material)
        * pbr_shader (Shader)
      * _724F7FF (Material)
        * pbr_shader (Shader)
      * DDDD0CFF (Material)
        * pbr_shader (Shader)
      * F4F4F4FF (Material)
        * pbr_shader (Shader)
      * B1D8B9FF (Material)
        * pbr_shader (Shader)
      * _6F2FFFF (Material)
        * pbr_shader (Shader)
      * _9192EFF (Material)
        * pbr_shader (Shader)
      * FFDC40FF (Material)
        * pbr_shader (Shader)
      * _1585CFF (Material)
        * pbr_shader (Shader)
      * BDBBB9FF (Material)
        * pbr_shader (Shader)
      * _E7DA1FF (Material)
        * pbr_shader (Shader)
      * EAEAEAFF (Material)
        * pbr_shader (Shader)
      * Material_004 (Material)
        * pbr_shader (Shader)
    * Meshes (Xform)
      * Sketchfab_model (Xform)
        * root (Xform)
          * GLTF_SceneRootNode (Xform)
            * Universal_robots_ur5e_with_on_robot_two_finger_gripper_RG2__16 (Xform)
              * Base_0 (Xform)
                * Object_5 (Xform)
                  * Object_0 (Mesh)
                * Object_6 (Xform)
                  * Object_1 (Mesh)
                * Object_7 (Xform)
                  * Object_2 (Mesh)
              * Joint_001_15 (Xform)
                * Object_9 (Xform)
                  * Object_3 (Mesh)
                * Object_10 (Xform)
                  * Object_4 (Mesh)
                * Bow_001_13 (Xform)
                  * Object_12 (Xform)
                    * Object_5 (Mesh)
                  * Object_13 (Xform)
                    * Object_6 (Mesh)
                  * Object_14 (Xform)
                    * Object_7 (Mesh)
                  * Joint_002_12 (Xform)
                    * Object_16 (Xform)
                      * Object_8 (Mesh)
                    * Object_17 (Xform)
                      * Object_9 (Mesh)
                    * Bow_002_10 (Xform)
                      * Object_19 (Xform)
                        * Object_10 (Mesh)
                      * Object_20 (Xform)
                        * Object_11 (Mesh)
                      * Object_21 (Xform)
                        * Object_12 (Mesh)
                      * Joint_003_9 (Xform)
                        * Object_23 (Xform)
                          * Object_13 (Mesh)
                        * Object_24 (Xform)
                          * Object_14 (Mesh)
                        * Bow_003_7 (Xform)
                          * Object_26 (Xform)
                            * Object_15 (Mesh)
                          * Object_27 (Xform)
                            * Object_16 (Mesh)
                          * Joint_004_6 (Xform)
                            * Object_29 (Xform)
                              * Object_17 (Mesh)
                            * Object_30 (Xform)
                              * Object_18 (Mesh)
                            * Cap_004_1 (Xform)
                              * Object_32 (Xform)
                                * Object_19 (Mesh)
                              * Object_33 (Xform)
                                * Object_20 (Mesh)
                            * wrist_5 (Xform)
                              * Object_35 (Xform)
                                * Object_21 (Mesh)
                              * Object_36 (Xform)
                                * Object_22 (Mesh)
                              * Object_37 (Xform)
                                * Object_23 (Mesh)
                              * Object_38 (Xform)
                                * Object_24 (Mesh)
                              * Claw_brecket_3 (Xform)
                                * Object_40 (Xform)
                                  * Object_25 (Mesh)
                                * Claw_Brecket_Bolt_2 (Xform)
                                  * Object_42 (Xform)
                                    * Object_26 (Mesh)
                                  * Object_43 (Xform)
                                    * Object_27 (Mesh)
                              * wrist_Bolt_4 (Xform)
                                * Object_45 (Xform)
                                  * Object_28 (Mesh)
                        * Cap_003_8 (Xform)
                          * Object_47 (Xform)
                            * Object_29 (Mesh)
                          * Object_48 (Xform)
                            * Object_30 (Mesh)
                    * Cap_002_11 (Xform)
                      * Object_50 (Xform)
                        * Object_31 (Mesh)
                      * Object_51 (Xform)
                        * Object_32 (Mesh)
                * Cap_001_14 (Xform)
                  * Object_53 (Xform)
                    * Object_33 (Mesh)
                  * Object_54 (Xform)
                    * Object_34 (Mesh)
            * Node0_58 (Xform)
              * Node1_57 (Xform)
                * Object_57 (Xform)
                  * Object_35 (Mesh)
                * Node10_19 (Xform)
                  * Object_59 (Xform)
                    * Object_36 (Mesh)
                * Node11_20 (Xform)
                  * Object_61 (Xform)
                    * Object_37 (Mesh)
                  * Object_62 (Xform)
                    * Object_38 (Mesh)
                  * Object_63 (Xform)
                    * Object_39 (Mesh)
                * Node12_21 (Xform)
                  * Object_65 (Xform)
                    * Object_40 (Mesh)
                  * Object_66 (Xform)
                    * Object_41 (Mesh)
                * Node13_22 (Xform)
                  * Object_68 (Xform)
                    * Object_42 (Mesh)
                * Node14_23 (Xform)
                  * Object_70 (Xform)
                    * Object_43 (Mesh)
                * Node15_24 (Xform)
                  * Object_72 (Xform)
                    * Object_44 (Mesh)
                * Node16_25 (Xform)
                  * Object_74 (Xform)
                    * Object_45 (Mesh)
                * Node17_26 (Xform)
                  * Object_76 (Xform)
                    * Object_46 (Mesh)
                * Node18_27 (Xform)
                  * Object_78 (Xform)
                    * Object_47 (Mesh)
                  * Object_79 (Xform)
                    * Object_48 (Mesh)
                * Node19_28 (Xform)
                  * Object_81 (Xform)
                    * Object_49 (Mesh)
                * Node2_29 (Xform)
                  * Object_83 (Xform)
                    * Object_50 (Mesh)
                  * Object_84 (Xform)
                    * Object_51 (Mesh)
                * Node20_30 (Xform)
                  * Object_86 (Xform)
                    * Object_52 (Mesh)
                * Node21_31 (Xform)
                  * Object_88 (Xform)
                    * Object_53 (Mesh)
                * Node22_32 (Xform)
                  * Object_90 (Xform)
                    * Object_54 (Mesh)
                * Node23_33 (Xform)
                  * Object_92 (Xform)
                    * Object_55 (Mesh)
                * Node24_34 (Xform)
                  * Object_94 (Xform)
                    * Object_56 (Mesh)
                * Node25_35 (Xform)
                  * Object_96 (Xform)
                    * Object_57 (Mesh)
                * Node26_36 (Xform)
                  * Object_98 (Xform)
                    * Object_58 (Mesh)
                * Node27_37 (Xform)
                  * Object_100 (Xform)
                    * Object_59 (Mesh)
                * Node28_38 (Xform)
                  * Object_102 (Xform)
                    * Object_60 (Mesh)
                * Node29_39 (Xform)
                  * Object_104 (Xform)
                    * Object_61 (Mesh)
                * Node3_40 (Xform)
                  * Object_106 (Xform)
                    * Object_62 (Mesh)
                  * Object_107 (Xform)
                    * Object_63 (Mesh)
                * Node30_41 (Xform)
                  * Object_109 (Xform)
                    * Object_64 (Mesh)
                * Node31_42 (Xform)
                  * Object_111 (Xform)
                    * Object_65 (Mesh)
                * Node32_43 (Xform)
                  * Object_113 (Xform)
                    * Object_66 (Mesh)
                * Node33_44 (Xform)
                  * Object_115 (Xform)
                    * Object_67 (Mesh)
                * Node34_45 (Xform)
                  * Object_117 (Xform)
                    * Object_68 (Mesh)
                * Node35_46 (Xform)
                  * Object_119 (Xform)
                    * Object_69 (Mesh)
                * Node36_47 (Xform)
                  * Object_121 (Xform)
                    * Object_70 (Mesh)
                * Node37_48 (Xform)
                  * Object_123 (Xform)
                    * Object_71 (Mesh)
                * Node38_49 (Xform)
                  * Object_125 (Xform)
                    * Object_72 (Mesh)
                * Node39_50 (Xform)
                  * Object_127 (Xform)
                    * Object_73 (Mesh)
                  * Object_128 (Xform)
                    * Object_74 (Mesh)
                * Node4_51 (Xform)
                  * Object_130 (Xform)
                    * Object_75 (Mesh)
                * Node5_52 (Xform)
                  * Object_132 (Xform)
                    * Object_76 (Mesh)
                  * Object_133 (Xform)
                    * Object_77 (Mesh)
                  * Object_134 (Xform)
                    * Object_78 (Mesh)
                * Node6_53 (Xform)
                  * Object_136 (Xform)
                    * Object_79 (Mesh)
                * Node7_54 (Xform)
                  * Object_138 (Xform)
                    * Object_80 (Mesh)
                  * Object_139 (Xform)
                    * Object_81 (Mesh)
                * Node8_55 (Xform)
                  * Object_141 (Xform)
                    * Object_82 (Mesh)
                * Node9_56 (Xform)
                  * Object_143 (Xform)
                    * Object_83 (Mesh)
            * mask_placment_59 (Xform)
              * Object_145 (Xform)
                * Object_84 (Mesh)
              * Object_146 (Xform)
                * Object_85 (Mesh)
            * cobotbase_61 (Xform)
              * Object_148 (Xform)
                * Object_86 (Mesh)
  * Plastic_Crate_1_ (Xform)
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
  * Plastic_Crate_1__01 (Xform)
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
  * Cardbox_A1_04 (Xform)
    * Cardbox_A1 (Mesh)
    * Looks (Scope)
      * Cardboard_A (Material)
        * Shader (Shader)
  * Cardbox_C1_01 (Xform)
    * Cardbox_C1 (Mesh)
    * Looks (Scope)
      * Cardboard_C1 (Material)
        * Shader (Shader)
  * Cardbox_A1_05 (Xform)
    * Cardbox_A1 (Mesh)
    * Looks (Scope)
      * Cardboard_A (Material)
        * Shader (Shader)
  * Cardbox_A3_01 (Xform)
    * Cardbox_A3 (Mesh)
    * Looks (Scope)
      * Cardboard_A3 (Material)
        * Shader (Shader)
  * Cardbox_B1_01 (Xform)
    * Cardbox_B1 (Mesh)
    * Looks (Scope)
      * Cardboard_B1 (Material)
        * Shader (Shader)
  * Cardbox_C1_02 (Xform)
    * Cardbox_C1 (Mesh)
    * Looks (Scope)
      * Cardboard_C1 (Material)
        * Shader (Shader)
  * Cardbox_C3_01 (Xform)
    * Cardbox_C3 (Mesh)
    * Looks (Scope)
      * Cardboard_C3 (Material)
        * Shader (Shader)
  * Cardbox_A1_06 (Xform)
    * Cardbox_A1 (Mesh)
    * Looks (Scope)
      * Cardboard_A (Material)
        * Shader (Shader)
  * Cardbox_A1_07 (Xform)
    * Cardbox_A1 (Mesh)
    * Looks (Scope)
      * Cardboard_A (Material)
        * Shader (Shader)
  * Cardbox_B1_02 (Xform)
    * Cardbox_B1 (Mesh)
    * Looks (Scope)
      * Cardboard_B1 (Material)
        * Shader (Shader)
  * Cardbox_B2_01 (Xform)
    * Cardbox_B2 (Mesh)
    * Looks (Scope)
      * Cardboard_B2 (Material)
        * Shader (Shader)
  * Cardbox_B3_03 (Xform)
    * Cardbox_B3 (Mesh)
    * Looks (Scope)
      * Cardboard_B3 (Material)
        * Shader (Shader)
  * Cardbox_C1_03 (Xform)
    * Cardbox_C1 (Mesh)
    * Looks (Scope)
      * Cardboard_C1 (Material)
        * Shader (Shader)
  * Cardbox_D3 (Xform)
    * Cardbox_D3 (Mesh)
    * Looks (Scope)
      * Cardboard_D3 (Material)
        * Shader (Shader)
  * Plastic_Crate_1__02 (Prim)
  * Cardbox_D3_05 (Prim)
  * Cardbox_D3_04 (Prim)
  * Cardbox_D3_03 (Prim)
  * Cardbox_D3_02 (Prim)
  * Cardbox_D3_01 (Prim)
  * Cardbox_D3_06 (Prim)
  * Forklift_A01_PR_V_NVD_01 (Xform)
    * Looks (Scope)
      * M_Forklift_Paint (Material)
        * Shader (Shader)
      * M_Forklift_A1 (Material)
        * Shader (Shader)
      * M_Forklift_A1_Plastic (Material)
        * Shader (Shader)
      * M_Forklift_A1_Glass (Material)
        * Shader (Shader)
      * M_Forklift_A1_Decals (Material)
        * Shader (Shader)
    * Geometry (Scope)
      * Forklift_Body_A01_01 (Mesh)
        * M_Forklift_A1 (GeomSubset)
        * M_Forklift_A1_Plastic (GeomSubset)
      * SM_Forklift_Glass_A01_01 (Mesh)
      * SM_Forklift_DecalBody_A01_01 (Mesh)
      * SM_Forklift_Fork_A01_01 (Mesh)
      * SM_Forklift_Rudder_A01_01 (Mesh)
        * M_Forklift_A1 (GeomSubset)
        * M_Forklift_A1_Plastic (GeomSubset)
      * SM_Forklift_FrontWheelRight_A01_01 (Mesh)
      * SM_Forklift_BackRightWheel_A01_01 (Mesh)
      * SM_Forklift_BackLeftWheel_A01_01 (Mesh)
      * SM_Forklift_RudderCables_A01_01 (Mesh)
      * SM_Forklift_RudderMechanism_A01_01 (Mesh)
      * SM_Forklift_LiftMechanism_A01_01 (Mesh)
      * SM_Forklift_LiftMechanismWheels_A01_01 (Mesh)
      * SM_Forklift_Chain_A01_01 (Mesh)
      * SM_Forklift_FrontWheelLeft_A01_01 (Mesh)
      * SM_Forklift_DecalHandle_A01_01 (Mesh)
      * SM_Forklift_LiftMechanismWheelsTop_A01_01 (Mesh)
      * SM_Forklift_LiftMechanismWheelsBottom_A01_01 (Mesh)
      * SM_Forklift_RudderLift_A01_01 (Mesh)
  * forklift_b (Xform)
    * lift (Xform)
      * SM_Forklift_Lift_B01_01 (Mesh)
      * SM_Forklift_OperatorCabGlass_B01_01 (Mesh)
      * SM_Forklift_OperatorCab_B01_01 (Mesh)
      * SM_Forklift_OperatorCabDecal_B01_01 (Mesh)
      * SM_Forklift_OperatorCabPedal_B01_01 (Mesh)
    * body (Xform)
      * body (Xform)
        * SM_Forklift_RightChainWheel_B01_01 (Mesh)
        * SM_Forklift_CenterChain_B01_01 (Mesh)
        * SM_Forklift_LeftChainWheel_B01_01 (Mesh)
        * SM_Forklift_RightHose_B01_01 (Mesh)
        * SM_Forklift_LeftHose_B01_01 (Mesh)
        * SM_Forklift_HoseWheel_B01_01 (Mesh)
        * SM_Forklift_CenterChainWheel_B01_01 (Mesh)
        * SM_Forklift_OperatorCabTopWheels_B01_01 (Mesh)
        * SM_Forklift_OperatorCabBotWheels_B01_01 (Mesh)
        * SM_Forklift_LiftBotWheels_B01_01 (Mesh)
        * SM_Forklift_LiftTopWheels_B01_01 (Mesh)
        * SM_Forklift_MastTopWheels_B01_01 (Mesh)
        * SM_Forklift_MastBottomWheels_B01_01 (Mesh)
        * SM_Forklift_CenterHydralicLift_B01_01 (Mesh)
        * SM_Forklift_HydraulicSystem_B01_01 (Mesh)
        * SM_Forklift_LeftChain_B01_01 (Mesh)
        * SM_Forklift_RightChain_B01_01 (Mesh)
        * SM_Forklift_Body_B01_01 (Mesh)
          * M_Forklift_B1_Body (GeomSubset)
          * M_Forklift_B1_Plastic (GeomSubset)
        * SM_Forklift_BodyDecal_B01_01 (Mesh)
        * SM_Forklift_BodyGlass_B01_01 (Mesh)
    * back_wheel (Xform)
      * SM_Forklift_BackWheel_B01_01 (Mesh)
      * Sphere (Sphere)
    * roller_front_right (Xform)
      * SM_Forklift_LeadWheelsFrontRight_B01_01 (Mesh)
      * Cylinder (Cylinder)
    * roller_back_left (Xform)
      * SM_Forklift_LeadWheelsBackLeft_B01_01 (Mesh)
      * Cylinder_01 (Cylinder)
    * roller_back_right (Xform)
      * SM_Forklift_LeadWheelsBackRight_B01_01 (Mesh)
      * Cylinder_02 (Cylinder)
    * roller_front_left (Xform)
      * SM_Forklift_LeadWheelsFrontLeft_B01_01 (Mesh)
      * Cylinder_03 (Cylinder)
    * back_wheel_swivel (Xform)
      * SM_Forklift_BackWheelbase_B01_01 (Mesh)
    * lift_joint (PhysicsPrismaticJoint)
    * back_wheel_joints (Scope)
      * back_wheel_drive (PhysicsRevoluteJoint)
      * back_wheel_swivel (PhysicsRevoluteJoint)
    * roller_joints (Scope)
      * front_right_roller (PhysicsRevoluteJoint)
      * back_left_roller (PhysicsRevoluteJoint)
      * back_right_roller (PhysicsRevoluteJoint)
      * front_left_roller (PhysicsRevoluteJoint)
    * Looks (Scope)
      * M_Forklift_B1_Body (Material)
        * Shader (Shader)
      * M_Forklift_B1_Decals (Material)
        * Shader (Shader)
      * M_Forklift_B1_Glass (Material)
        * Shader (Shader)
      * M_Forklift_B1_Blue (Material)
        * Shader (Shader)
* Environment (Xform)
  * defaultLight (DistantLight)
* Render (Prim)
  * OmniverseKit (Prim)
    * HydraTextures (Prim)
      * omni_kit_widget_viewport_ViewportTexture_0 (RenderProduct)
  * OmniverseGlobalRenderSettings (RenderSettings)
  * Vars (Prim)
    * LdrColor (RenderVar)

## 3. 对象详细描述 (Detailed Prim Descriptions)

### /World/factory

* **Prim路径 (Prim Path):**/World/factory
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  *   [reference] '../scene/factory/factory.usdc'
* **世界包围盒 (World BBox):**
  * Size: '(49.139, 19.897, 67.754)'
  * Center: '(4.932, -39.847, -17.842)'

---

### /World/RackLargeEmpty_A1

* **Prim路径 (Prim Path):**/World/RackLargeEmpty_A1
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  *   [reference] '../Assets/new/Industrial_NVD@10012/Assets/ArchVis/Industrial/Shelves/RackLargeEmpty_A1.usd'
* **世界包围盒 (World BBox):**
  * Size: '(206.658, 399.998, 301.000)'
  * Center: '(-8.927, -49.481, -25.475)'

---

### /World/carton

* **Prim路径 (Prim Path):**/World/carton
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  *   [reference] '../assets/carton/carton.usdc'
* **世界包围盒 (World BBox):**
  * Size: '(35.888, 35.888, 35.888)'
  * Center: '(-8.086, -49.397, -26.294)'

---

### /World/carton_01

* **Prim路径 (Prim Path):**/World/carton_01
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  *   [reference] '../assets/carton/carton.usdc'
* **世界包围盒 (World BBox):**
  * Size: '(35.888, 35.888, 35.888)'
  * Center: '(-9.885, -49.306, -26.294)'

---

### /World/carton_02

* **Prim路径 (Prim Path):**/World/carton_02
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  *   [reference] '../assets/carton/carton.usdc'
* **世界包围盒 (World BBox):**
  * Size: '(35.888, 35.888, 35.888)'
  * Center: '(-9.885, -49.306, -24.405)'

---

### /World/carton_03

* **Prim路径 (Prim Path):**/World/carton_03
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  *   [reference] '../assets/carton/carton.usdc'
* **世界包围盒 (World BBox):**
  * Size: '(35.888, 35.888, 35.888)'
  * Center: '(-8.086, -49.397, -24.405)'

---

### /World/WoodenCrate_A1

* **Prim路径 (Prim Path):**/World/WoodenCrate_A1
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  *   [reference] '../Assets/new/Industrial_NVD@10012/Assets/ArchVis/Industrial/Containers/Wooden/WoodenCrate_A1.usd'
* **世界包围盒 (World BBox):**
  * Size: '(100.221, 100.867, 101.654)'
  * Center: '(-9.920, -39.166, -25.967)'

---

### /World/WoodenCrate_A2

* **Prim路径 (Prim Path):**/World/WoodenCrate_A2
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  *   [reference] '../Assets/new/Industrial_NVD@10012/Assets/ArchVis/Industrial/Containers/Wooden/WoodenCrate_A2.usd'
* **世界包围盒 (World BBox):**
  * Size: '(100.221, 100.867, 101.654)'
  * Center: '(-8.161, -39.119, -25.967)'

---

### /World/WoodenCrate_B1

* **Prim路径 (Prim Path):**/World/WoodenCrate_B1
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  *   [reference] '../Assets/new/Industrial_NVD@10012/Assets/ArchVis/Industrial/Containers/Wooden/WoodenCrate_B1.usd'
* **世界包围盒 (World BBox):**
  * Size: '(100.522, 200.800, 101.761)'
  * Center: '(-9.829, -39.116, -24.091)'

---

### /World/WoodenCrate_B2

* **Prim路径 (Prim Path):**/World/WoodenCrate_B2
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  *   [reference] '../Assets/new/Industrial_NVD@10012/Assets/ArchVis/Industrial/Containers/Wooden/WoodenCrate_B2.usd'
* **世界包围盒 (World BBox):**
  * Size: '(100.522, 200.800, 101.761)'
  * Center: '(-8.090, -39.116, -24.091)'

---

### /World/RackLargeEmpty_A1_01

* **Prim路径 (Prim Path):**/World/RackLargeEmpty_A1_01
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  *   [reference] '../Assets/new/Industrial_NVD@10012/Assets/ArchVis/Industrial/Shelves/RackLargeEmpty_A1.usd'
* **世界包围盒 (World BBox):**
  * Size: '(206.658, 399.998, 301.000)'
  * Center: '(-8.927, -39.133, -25.475)'

---

### /World/RackSmallEmpty_A2

* **Prim路径 (Prim Path):**/World/RackSmallEmpty_A2
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  *   [reference] '../Assets/new/Industrial_NVD@10012/Assets/ArchVis/Industrial/Shelves/RackSmallEmpty_A2.usd'
* **世界包围盒 (World BBox):**
  * Size: '(108.019, 199.810, 301.000)'
  * Center: '(-4.814, -49.299, -25.475)'

---

### /World/Cardbox_A1

* **Prim路径 (Prim Path):**/World/Cardbox_A1
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  *   [reference] '../Assets/new/Industrial_NVD@10012/Assets/ArchVis/Industrial/Containers/Cardboard/Cardbox_A1.usd'
* **世界包围盒 (World BBox):**
  * Size: '(69.944, 52.115, 50.993)'
  * Center: '(-4.630, -49.337, -26.219)'

---

### /World/Cardbox_A1_01

* **Prim路径 (Prim Path):**/World/Cardbox_A1_01
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  *   [reference] '../Assets/new/Industrial_NVD@10012/Assets/ArchVis/Industrial/Containers/Cardboard/Cardbox_A1.usd'
* **世界包围盒 (World BBox):**
  * Size: '(69.944, 52.115, 50.993)'
  * Center: '(-5.343, -49.323, -24.842)'

---

### /World/Cardbox_A1_02

* **Prim路径 (Prim Path):**/World/Cardbox_A1_02
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  *   [reference] '../Assets/new/Industrial_NVD@10012/Assets/ArchVis/Industrial/Containers/Cardboard/Cardbox_A1.usd'
* **世界包围盒 (World BBox):**
  * Size: '(69.944, 52.115, 50.993)'
  * Center: '(-4.407, -49.291, -24.842)'

---

### /World/Cardbox_B3

* **Prim路径 (Prim Path):**/World/Cardbox_B3
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  *   [reference] '../Assets/new/Industrial_NVD@10012/Assets/ArchVis/Industrial/Containers/Cardboard/Cardbox_B3.usd'
* **世界包围盒 (World BBox):**
  * Size: '(51.028, 50.994, 52.067)'
  * Center: '(-5.114, -39.059, -24.836)'

---

### /World/Cardbox_C1

* **Prim路径 (Prim Path):**/World/Cardbox_C1
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  *   [reference] '../Assets/new/Industrial_NVD@10012/Assets/ArchVis/Industrial/Containers/Cardboard/Cardbox_C1.usd'
* **世界包围盒 (World BBox):**
  * Size: '(51.324, 51.056, 25.969)'
  * Center: '(-4.531, -39.021, -26.344)'

---

### /World/Cardbox_B3_01

* **Prim路径 (Prim Path):**/World/Cardbox_B3_01
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  *   [reference] '../Assets/new/Industrial_NVD@10012/Assets/ArchVis/Industrial/Containers/Cardboard/Cardbox_B3.usd'
* **世界包围盒 (World BBox):**
  * Size: '(51.028, 50.994, 52.067)'
  * Center: '(-4.338, -39.043, -24.838)'

---

### /World/Cardbox_C2

* **Prim路径 (Prim Path):**/World/Cardbox_C2
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  *   [reference] '../Assets/new/Industrial_NVD@10012/Assets/ArchVis/Industrial/Containers/Cardboard/Cardbox_C2.usd'
* **世界包围盒 (World BBox):**
  * Size: '(51.324, 51.056, 25.969)'
  * Center: '(-5.398, -39.036, -26.344)'

---

### /World/RackSmallEmpty_A2_01

* **Prim路径 (Prim Path):**/World/RackSmallEmpty_A2_01
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  *   [reference] '../Assets/new/Industrial_NVD@10012/Assets/ArchVis/Industrial/Shelves/RackSmallEmpty_A2.usd'
* **世界包围盒 (World BBox):**
  * Size: '(108.019, 199.810, 301.000)'
  * Center: '(-4.814, -39.072, -25.475)'

---

### /World/RackLongEmpty_A2

* **Prim路径 (Prim Path):**/World/RackLongEmpty_A2
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  *   [reference] '../Assets/new/Industrial_NVD@10012/Assets/ArchVis/Industrial/Shelves/RackLongEmpty_A2.usd'
* **世界包围盒 (World BBox):**
  * Size: '(108.049, 399.997, 301.000)'
  * Center: '(-1.091, -49.202, -25.475)'

---

### /World/RackLongEmpty_A2_01

* **Prim路径 (Prim Path):**/World/RackLongEmpty_A2_01
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  *   [reference] '../Assets/new/Industrial_NVD@10012/Assets/ArchVis/Industrial/Shelves/RackLongEmpty_A2.usd'
* **世界包围盒 (World BBox):**
  * Size: '(108.049, 399.997, 301.000)'
  * Center: '(-1.091, -39.053, -25.475)'

---

### /World/RackLargeEmpty_A1_02

* **Prim路径 (Prim Path):**/World/RackLargeEmpty_A1_02
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  *   [reference] '../Assets/new/Industrial_NVD@10012/Assets/ArchVis/Industrial/Shelves/RackLargeEmpty_A1.usd'
* **世界包围盒 (World BBox):**
  * Size: '(206.658, 399.998, 301.000)'
  * Center: '(3.980, -49.481, -25.475)'

---

### /World/WoodenCrate_B2_01

* **Prim路径 (Prim Path):**/World/WoodenCrate_B2_01
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  *   [reference] '../Assets/new/Industrial_NVD@10012/Assets/ArchVis/Industrial/Containers/Wooden/WoodenCrate_B2.usd'
* **世界包围盒 (World BBox):**
  * Size: '(100.522, 200.800, 101.761)'
  * Center: '(4.893, -39.116, -24.091)'

---

### /World/WoodenCrate_B1_01

* **Prim路径 (Prim Path):**/World/WoodenCrate_B1_01
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  *   [reference] '../Assets/new/Industrial_NVD@10012/Assets/ArchVis/Industrial/Containers/Wooden/WoodenCrate_B1.usd'
* **世界包围盒 (World BBox):**
  * Size: '(100.522, 200.800, 101.761)'
  * Center: '(3.154, -39.116, -24.091)'

---

### /World/WoodenCrate_A2_01

* **Prim路径 (Prim Path):**/World/WoodenCrate_A2_01
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  *   [reference] '../Assets/new/Industrial_NVD@10012/Assets/ArchVis/Industrial/Containers/Wooden/WoodenCrate_A2.usd'
* **世界包围盒 (World BBox):**
  * Size: '(100.221, 100.867, 101.654)'
  * Center: '(4.822, -39.119, -25.967)'

---

### /World/WoodenCrate_A1_01

* **Prim路径 (Prim Path):**/World/WoodenCrate_A1_01
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  *   [reference] '../Assets/new/Industrial_NVD@10012/Assets/ArchVis/Industrial/Containers/Wooden/WoodenCrate_A1.usd'
* **世界包围盒 (World BBox):**
  * Size: '(100.221, 100.867, 101.654)'
  * Center: '(3.063, -39.166, -25.967)'

---

### /World/RackLargeEmpty_A1_03

* **Prim路径 (Prim Path):**/World/RackLargeEmpty_A1_03
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  *   [reference] '../Assets/new/Industrial_NVD@10012/Assets/ArchVis/Industrial/Shelves/RackLargeEmpty_A1.usd'
* **世界包围盒 (World BBox):**
  * Size: '(206.658, 399.998, 301.000)'
  * Center: '(4.056, -39.133, -25.475)'

---

### /World/carton_04

* **Prim路径 (Prim Path):**/World/carton_04
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  *   [reference] '../assets/carton/carton.usdc'
* **世界包围盒 (World BBox):**
  * Size: '(35.888, 35.888, 35.888)'
  * Center: '(4.820, -49.397, -24.405)'

---

### /World/carton_05

* **Prim路径 (Prim Path):**/World/carton_05
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  *   [reference] '../assets/carton/carton.usdc'
* **世界包围盒 (World BBox):**
  * Size: '(35.888, 35.888, 35.888)'
  * Center: '(3.022, -49.306, -24.405)'

---

### /World/carton_06

* **Prim路径 (Prim Path):**/World/carton_06
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  *   [reference] '../assets/carton/carton.usdc'
* **世界包围盒 (World BBox):**
  * Size: '(35.888, 35.888, 35.888)'
  * Center: '(3.022, -49.306, -26.294)'

---

### /World/carton_07

* **Prim路径 (Prim Path):**/World/carton_07
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  *   [reference] '../assets/carton/carton.usdc'
* **世界包围盒 (World BBox):**
  * Size: '(35.888, 35.888, 35.888)'
  * Center: '(4.820, -49.397, -26.294)'

---

### /World/Cardbox_C3

* **Prim路径 (Prim Path):**/World/Cardbox_C3
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  *   [reference] '../Assets/new/Industrial_NVD@10012/Assets/ArchVis/Industrial/Containers/Cardboard/Cardbox_C3.usd'
* **世界包围盒 (World BBox):**
  * Size: '(51.374, 51.106, 25.969)'
  * Center: '(-0.631, -49.118, -24.592)'

---

### /World/Cardbox_C2_01

* **Prim路径 (Prim Path):**/World/Cardbox_C2_01
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  *   [reference] '../Assets/new/Industrial_NVD@10012/Assets/ArchVis/Industrial/Containers/Cardboard/Cardbox_C2.usd'
* **世界包围盒 (World BBox):**
  * Size: '(53.097, 52.839, 25.969)'
  * Center: '(-0.100, -49.141, -24.592)'

---

### /World/Cardbox_B3_02

* **Prim路径 (Prim Path):**/World/Cardbox_B3_02
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  *   [reference] '../Assets/new/Industrial_NVD@10012/Assets/ArchVis/Industrial/Containers/Cardboard/Cardbox_B3.usd'
* **世界包围盒 (World BBox):**
  * Size: '(51.028, 50.994, 52.067)'
  * Center: '(-2.232, -39.018, -26.214)'

---

### /World/Cardbox_B2

* **Prim路径 (Prim Path):**/World/Cardbox_B2
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  *   [reference] '../Assets/new/Industrial_NVD@10012/Assets/ArchVis/Industrial/Containers/Cardboard/Cardbox_B2.usd'
* **世界包围盒 (World BBox):**
  * Size: '(51.028, 50.994, 52.067)'
  * Center: '(-1.360, -38.960, -26.214)'

---

### /World/Cardbox_B1

* **Prim路径 (Prim Path):**/World/Cardbox_B1
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  *   [reference] '../Assets/new/Industrial_NVD@10012/Assets/ArchVis/Industrial/Containers/Cardboard/Cardbox_B1.usd'
* **世界包围盒 (World BBox):**
  * Size: '(51.028, 50.994, 52.067)'
  * Center: '(-0.542, -38.936, -26.214)'

---

### /World/Cardbox_A3

* **Prim路径 (Prim Path):**/World/Cardbox_A3
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  *   [reference] '../Assets/new/Industrial_NVD@10012/Assets/ArchVis/Industrial/Containers/Cardboard/Cardbox_A3.usd'
* **世界包围盒 (World BBox):**
  * Size: '(69.944, 50.993, 52.115)'
  * Center: '(-2.176, -38.924, -24.461)'

---

### /World/Cardbox_A2

* **Prim路径 (Prim Path):**/World/Cardbox_A2
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  *   [reference] '../Assets/new/Industrial_NVD@10012/Assets/ArchVis/Industrial/Containers/Cardboard/Cardbox_A2.usd'
* **世界包围盒 (World BBox):**
  * Size: '(69.944, 50.993, 52.115)'
  * Center: '(-1.224, -38.935, -24.461)'

---

### /World/Cardbox_A1_03

* **Prim路径 (Prim Path):**/World/Cardbox_A1_03
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  *   [reference] '../Assets/new/Industrial_NVD@10012/Assets/ArchVis/Industrial/Containers/Cardboard/Cardbox_A1.usd'
* **世界包围盒 (World BBox):**
  * Size: '(69.944, 52.115, 50.993)'
  * Center: '(-0.170, -38.945, -24.467)'

---

### /World/AGV_ready_1

* **Prim路径 (Prim Path):**/World/AGV_ready_1
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  *   [reference] '../assets/AGV_ready_1/AGV_ready_1.usdc'
* **世界包围盒 (World BBox):**
  * Size: '(1.457, 0.340, 0.669)'
  * Center: '(3.782, -46.384, -26.979)'

---

### /World/AGV

* **Prim路径 (Prim Path):**/World/AGV
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  *   [reference] '../assets/AGV/AGV.usdc'
* **世界包围盒 (World BBox):**
  * Size: '(166.769, 25.021, 37.304)'
  * Center: '(-1.207, -42.850, -26.854)'

---

### /World/UR__Cobot_Mir_AMR

* **Prim路径 (Prim Path):**/World/UR__Cobot_Mir_AMR
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  *   [reference] '../assets/UR__Cobot_Mir_AMR/UR__Cobot_Mir_AMR.usdc'
* **世界包围盒 (World BBox):**
  * Size: '(168.136, 300.000, 240.391)'
  * Center: '(-2.127, -46.093, -25.481)'

---

### /World/Plastic_Crate_1_

* **Prim路径 (Prim Path):**/World/Plastic_Crate_1_
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  *   [reference] '../assets/Plastic_Crate(1)/Plastic_Crate.usdc'
* **世界包围盒 (World BBox):**
  * Size: '(0.424, 0.365, 0.421)'
  * Center: '(5.058, -46.349, -26.796)'

---

### /World/Plastic_Crate_1__01

* **Prim路径 (Prim Path):**/World/Plastic_Crate_1__01
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  *   [reference] '../assets/Plastic_Crate(1)/Plastic_Crate.usdc'
* **世界包围盒 (World BBox):**
  * Size: '(0.424, 0.365, 0.421)'
  * Center: '(-1.785, -46.006, -25.461)'

---

### /World/Cardbox_A1_04

* **Prim路径 (Prim Path):**/World/Cardbox_A1_04
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  *   [reference] '../Assets/new/Industrial_NVD@10012/Assets/ArchVis/Industrial/Containers/Cardboard/Cardbox_A1.usd'
* **世界包围盒 (World BBox):**
  * Size: '(69.944, 52.115, 50.993)'
  * Center: '(0.431, -49.155, -24.467)'

---

### /World/Cardbox_C1_01

* **Prim路径 (Prim Path):**/World/Cardbox_C1_01
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  *   [reference] '../Assets/new/Industrial_NVD@10012/Assets/ArchVis/Industrial/Containers/Cardboard/Cardbox_C1.usd'
* **世界包围盒 (World BBox):**
  * Size: '(55.172, 54.925, 25.969)'
  * Center: '(0.414, -49.080, -24.082)'

---

### /World/Cardbox_A1_05

* **Prim路径 (Prim Path):**/World/Cardbox_A1_05
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  *   [reference] '../Assets/new/Industrial_NVD@10012/Assets/ArchVis/Industrial/Containers/Cardboard/Cardbox_A1.usd'
* **世界包围盒 (World BBox):**
  * Size: '(69.944, 52.115, 50.993)'
  * Center: '(-0.365, -49.113, -24.208)'

---

### /World/Cardbox_A3_01

* **Prim路径 (Prim Path):**/World/Cardbox_A3_01
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  *   [reference] '../Assets/new/Industrial_NVD@10012/Assets/ArchVis/Industrial/Containers/Cardboard/Cardbox_A3.usd'
* **世界包围盒 (World BBox):**
  * Size: '(69.944, 50.993, 52.115)'
  * Center: '(-1.678, -49.023, -24.461)'

---

### /World/Cardbox_B1_01

* **Prim路径 (Prim Path):**/World/Cardbox_B1_01
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  *   [reference] '../Assets/new/Industrial_NVD@10012/Assets/ArchVis/Industrial/Containers/Cardboard/Cardbox_B1.usd'
* **世界包围盒 (World BBox):**
  * Size: '(51.028, 50.994, 52.067)'
  * Center: '(-2.302, -49.004, -24.462)'

---

### /World/Cardbox_C1_02

* **Prim路径 (Prim Path):**/World/Cardbox_C1_02
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  *   [reference] '../Assets/new/Industrial_NVD@10012/Assets/ArchVis/Industrial/Containers/Cardboard/Cardbox_C1.usd'
* **世界包围盒 (World BBox):**
  * Size: '(51.324, 51.056, 25.969)'
  * Center: '(-1.685, -49.057, -24.072)'

---

### /World/Cardbox_C3_01

* **Prim路径 (Prim Path):**/World/Cardbox_C3_01
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  *   [reference] '../Assets/new/Industrial_NVD@10012/Assets/ArchVis/Industrial/Containers/Cardboard/Cardbox_C3.usd'
* **世界包围盒 (World BBox):**
  * Size: '(51.324, 51.056, 25.969)'
  * Center: '(-2.300, -49.022, -24.072)'

---

### /World/Cardbox_A1_06

* **Prim路径 (Prim Path):**/World/Cardbox_A1_06
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  *   [reference] '../Assets/new/Industrial_NVD@10012/Assets/ArchVis/Industrial/Containers/Cardboard/Cardbox_A1.usd'
* **世界包围盒 (World BBox):**
  * Size: '(69.944, 52.115, 50.993)'
  * Center: '(0.355, -49.133, -26.219)'

---

### /World/Cardbox_A1_07

* **Prim路径 (Prim Path):**/World/Cardbox_A1_07
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  *   [reference] '../Assets/new/Industrial_NVD@10012/Assets/ArchVis/Industrial/Containers/Cardboard/Cardbox_A1.usd'
* **世界包围盒 (World BBox):**
  * Size: '(69.944, 52.115, 50.993)'
  * Center: '(-0.379, -49.169, -26.219)'

---

### /World/Cardbox_B1_02

* **Prim路径 (Prim Path):**/World/Cardbox_B1_02
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  *   [reference] '../Assets/new/Industrial_NVD@10012/Assets/ArchVis/Industrial/Containers/Cardboard/Cardbox_B1.usd'
* **世界包围盒 (World BBox):**
  * Size: '(51.028, 50.994, 52.067)'
  * Center: '(-1.553, -49.176, -26.214)'

---

### /World/Cardbox_B2_01

* **Prim路径 (Prim Path):**/World/Cardbox_B2_01
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  *   [reference] '../Assets/new/Industrial_NVD@10012/Assets/ArchVis/Industrial/Containers/Cardboard/Cardbox_B2.usd'
* **世界包围盒 (World BBox):**
  * Size: '(51.028, 50.994, 52.067)'
  * Center: '(-2.689, -49.134, -26.214)'

---

### /World/Cardbox_B3_03

* **Prim路径 (Prim Path):**/World/Cardbox_B3_03
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  *   [reference] '../Assets/new/Industrial_NVD@10012/Assets/ArchVis/Industrial/Containers/Cardboard/Cardbox_B3.usd'
* **世界包围盒 (World BBox):**
  * Size: '(51.028, 50.994, 52.067)'
  * Center: '(-2.116, -49.125, -26.214)'

---

### /World/Cardbox_C1_03

* **Prim路径 (Prim Path):**/World/Cardbox_C1_03
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  *   [reference] '../Assets/new/Industrial_NVD@10012/Assets/ArchVis/Industrial/Containers/Cardboard/Cardbox_C1.usd'
* **世界包围盒 (World BBox):**
  * Size: '(51.324, 51.056, 25.969)'
  * Center: '(-1.083, -49.110, -24.455)'

---

### /World/Cardbox_D3

* **Prim路径 (Prim Path):**/World/Cardbox_D3
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  *   [reference] '../Assets/new/Industrial_NVD@10012/Assets/ArchVis/Industrial/Containers/Cardboard/Cardbox_D3.usd'
* **世界包围盒 (World BBox):**
  * Size: '(34.484, 26.438, 16.611)'
  * Center: '(0.500, -49.166, -25.390)'

---

### /World/Forklift_A01_PR_V_NVD_01

* **Prim路径 (Prim Path):**/World/Forklift_A01_PR_V_NVD_01
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  *   [reference] '../device_data/usdz/Forklift/Forklift_A01_PR_V_NVD_01.usdz'
* **世界包围盒 (World BBox):**
  * Size: '(82.260, 188.529, 196.132)'
  * Center: '(1.549, -45.021, -26.163)'

---

### /World/forklift_b

* **Prim路径 (Prim Path):**/World/forklift_b
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  *   [reference] '../device_data/usdz/Forklift/forklift_b.usdz'
* **世界包围盒 (World BBox):**
  * Size: '(3.031, 1.130, 2.935)'
  * Center: '(2.475, -42.851, -25.677)'

---

## 4. 材质库 (Material Library)

### /World/factory/Materials/WindowsIndustrial_frontSolid_OpenWindows_Mat

* **Prim路径 (Prim Path):**/World/factory/Materials/WindowsIndustrial_frontSolid_OpenWindows_Mat
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/factory/Materials/WindowsIndustrial_frontSolid_OpenWindows_Mat/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/factory/Materials/WindowsIndustrial_frontSolid_OpenWindows_Mat/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f]
        * Connected: '/World/factory/Materials/WindowsIndustrial_frontSolid_OpenWindows_Mat/tex_base.outputs:rgb' @ '/World/factory/Materials/WindowsIndustrial_frontSolid_OpenWindows_Mat/tex_base'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/WindowsIndustrial-frontSolid-OpenWindows_Mat_baseColor.jpg'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(1.000, 1.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0.957705'
    * '/World/factory/Materials/WindowsIndustrial_frontSolid_OpenWindows_Mat/tex_base' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/WindowsIndustrial-frontSolid-OpenWindows_Mat_baseColor.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'file' [asset] = '0/WindowsIndustrial-frontSolid-OpenWindows_Mat_baseColor.jpg'
      * 'st' [float2]
        * Connected: '/World/factory/Materials/WindowsIndustrial_frontSolid_OpenWindows_Mat/uvset0.outputs:result' @ '/World/factory/Materials/WindowsIndustrial_frontSolid_OpenWindows_Mat/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/factory/Materials/WindowsIndustrial_frontSolid_OpenWindows_Mat/uvset0' (ID: 'UsdPrimvarReader_float2')
    * Implementation: 'id'

---

### /World/factory/Materials/WindowsIndustrial_frontSolid_Mat

* **Prim路径 (Prim Path):**/World/factory/Materials/WindowsIndustrial_frontSolid_Mat
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/factory/Materials/WindowsIndustrial_frontSolid_Mat/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/factory/Materials/WindowsIndustrial_frontSolid_Mat/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f]
        * Connected: '/World/factory/Materials/WindowsIndustrial_frontSolid_Mat/tex_base.outputs:rgb' @ '/World/factory/Materials/WindowsIndustrial_frontSolid_Mat/tex_base'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/WindowsIndustrial-frontSolid_Mat_baseColor.jpg'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(1.000, 1.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0.957705'
    * '/World/factory/Materials/WindowsIndustrial_frontSolid_Mat/tex_base' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/WindowsIndustrial-frontSolid_Mat_baseColor.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'file' [asset] = '0/WindowsIndustrial-frontSolid_Mat_baseColor.jpg'
      * 'st' [float2]
        * Connected: '/World/factory/Materials/WindowsIndustrial_frontSolid_Mat/uvset0.outputs:result' @ '/World/factory/Materials/WindowsIndustrial_frontSolid_Mat/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/factory/Materials/WindowsIndustrial_frontSolid_Mat/uvset0' (ID: 'UsdPrimvarReader_float2')
    * Implementation: 'id'

---

### /World/factory/Materials/WindowsIndustrial_frontDoorclosed_Mat

* **Prim路径 (Prim Path):**/World/factory/Materials/WindowsIndustrial_frontDoorclosed_Mat
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/factory/Materials/WindowsIndustrial_frontDoorclosed_Mat/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/factory/Materials/WindowsIndustrial_frontDoorclosed_Mat/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f]
        * Connected: '/World/factory/Materials/WindowsIndustrial_frontDoorclosed_Mat/tex_base.outputs:rgb' @ '/World/factory/Materials/WindowsIndustrial_frontDoorclosed_Mat/tex_base'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/WindowsIndustrial-frontDoorclosed_Mat_baseColor.jpg'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(1.000, 1.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0.957705'
    * '/World/factory/Materials/WindowsIndustrial_frontDoorclosed_Mat/tex_base' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/WindowsIndustrial-frontDoorclosed_Mat_baseColor.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'file' [asset] = '0/WindowsIndustrial-frontDoorclosed_Mat_baseColor.jpg'
      * 'st' [float2]
        * Connected: '/World/factory/Materials/WindowsIndustrial_frontDoorclosed_Mat/uvset0.outputs:result' @ '/World/factory/Materials/WindowsIndustrial_frontDoorclosed_Mat/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/factory/Materials/WindowsIndustrial_frontDoorclosed_Mat/uvset0' (ID: 'UsdPrimvarReader_float2')
    * Implementation: 'id'

---

### /World/factory/Materials/WindowsIndustrial_frontDoorOpen_Mat

* **Prim路径 (Prim Path):**/World/factory/Materials/WindowsIndustrial_frontDoorOpen_Mat
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/factory/Materials/WindowsIndustrial_frontDoorOpen_Mat/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/factory/Materials/WindowsIndustrial_frontDoorOpen_Mat/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f]
        * Connected: '/World/factory/Materials/WindowsIndustrial_frontDoorOpen_Mat/tex_base.outputs:rgb' @ '/World/factory/Materials/WindowsIndustrial_frontDoorOpen_Mat/tex_base'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/WindowsIndustrial-frontDoorOpen_Mat_baseColor.jpg'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(1.000, 1.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0.957705'
    * '/World/factory/Materials/WindowsIndustrial_frontDoorOpen_Mat/tex_base' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/WindowsIndustrial-frontDoorOpen_Mat_baseColor.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'file' [asset] = '0/WindowsIndustrial-frontDoorOpen_Mat_baseColor.jpg'
      * 'st' [float2]
        * Connected: '/World/factory/Materials/WindowsIndustrial_frontDoorOpen_Mat/uvset0.outputs:result' @ '/World/factory/Materials/WindowsIndustrial_frontDoorOpen_Mat/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/factory/Materials/WindowsIndustrial_frontDoorOpen_Mat/uvset0' (ID: 'UsdPrimvarReader_float2')
    * Implementation: 'id'

---

### /World/factory/Materials/WindowsIndustrial_front_Mat

* **Prim路径 (Prim Path):**/World/factory/Materials/WindowsIndustrial_front_Mat
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/factory/Materials/WindowsIndustrial_front_Mat/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/factory/Materials/WindowsIndustrial_front_Mat/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f]
        * Connected: '/World/factory/Materials/WindowsIndustrial_front_Mat/tex_base.outputs:rgb' @ '/World/factory/Materials/WindowsIndustrial_front_Mat/tex_base'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/WindowsIndustrial-front_Mat_baseColor.jpg'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(1.000, 1.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0.957705'
    * '/World/factory/Materials/WindowsIndustrial_front_Mat/tex_base' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/WindowsIndustrial-front_Mat_baseColor.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'file' [asset] = '0/WindowsIndustrial-front_Mat_baseColor.jpg'
      * 'st' [float2]
        * Connected: '/World/factory/Materials/WindowsIndustrial_front_Mat/uvset0.outputs:result' @ '/World/factory/Materials/WindowsIndustrial_front_Mat/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/factory/Materials/WindowsIndustrial_front_Mat/uvset0' (ID: 'UsdPrimvarReader_float2')
    * Implementation: 'id'

---

### /World/factory/Materials/_1___Default

* **Prim路径 (Prim Path):**/World/factory/Materials/_1___Default
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/factory/Materials/_1___Default/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/factory/Materials/_1___Default/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f]
        * Connected: '/World/factory/Materials/_1___Default/tex_base.outputs:rgb' @ '/World/factory/Materials/_1___Default/tex_base'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/11_-_Default_baseColor.jpg'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(1.000, 1.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0.892971'
    * '/World/factory/Materials/_1___Default/tex_base' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/11_-_Default_baseColor.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'file' [asset] = '0/11_-_Default_baseColor.jpg'
      * 'st' [float2]
        * Connected: '/World/factory/Materials/_1___Default/uvset0.outputs:result' @ '/World/factory/Materials/_1___Default/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/factory/Materials/_1___Default/uvset0' (ID: 'UsdPrimvarReader_float2')
    * Implementation: 'id'

---

### /World/factory/Materials/_0___Default

* **Prim路径 (Prim Path):**/World/factory/Materials/_0___Default
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/factory/Materials/_0___Default/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/factory/Materials/_0___Default/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f]
        * Connected: '/World/factory/Materials/_0___Default/tex_base.outputs:rgb' @ '/World/factory/Materials/_0___Default/tex_base'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/20_-_Default_baseColor.jpg'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(1.000, 1.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0.892971'
    * '/World/factory/Materials/_0___Default/tex_base' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/20_-_Default_baseColor.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'file' [asset] = '0/20_-_Default_baseColor.jpg'
      * 'st' [float2]
        * Connected: '/World/factory/Materials/_0___Default/uvset0.outputs:result' @ '/World/factory/Materials/_0___Default/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/factory/Materials/_0___Default/uvset0' (ID: 'UsdPrimvarReader_float2')
    * Implementation: 'id'

---

### /World/RackLargeEmpty_A1/Looks/Shelf

* **Prim路径 (Prim Path):**/World/RackLargeEmpty_A1/Looks/Shelf
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/RackLargeEmpty_A1/Looks/Shelf/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/RackLargeEmpty_A1/Looks/Shelf/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * 纹理引用 (Texture Assets):
      * './Textures/T_Rack_A1_Albedo.`<UDIM>`.png'
      * './Textures/T_Rack_A1_Normal.`<UDIM>`.png'
      * './Textures/T_Rack_A1_ORM.`<UDIM>`.png'
    * Inputs:
      * 'diffuse_texture' [asset] = './Textures/T_Rack_A1_Albedo.`<UDIM>`.png'
      * 'metallic_texture_influence' [float] = '1'
      * 'normalmap_texture' [asset] = './Textures/T_Rack_A1_Normal.`<UDIM>`.png'
      * 'ORM_texture' [asset] = './Textures/T_Rack_A1_ORM.`<UDIM>`.png'
      * 'reflection_roughness_texture_influence' [float] = '1'

---

### /World/carton/Materials/_6___Default

* **Prim路径 (Prim Path):**/World/carton/Materials/_6___Default
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/carton/Materials/_6___Default/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/carton/Materials/_6___Default/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f]
        * Connected: '/World/carton/Materials/_6___Default/tex_base.outputs:rgb' @ '/World/carton/Materials/_6___Default/tex_base'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/06_-_Default_baseColor.jpg'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(1.000, 1.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0.892971'
    * '/World/carton/Materials/_6___Default/tex_base' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/06_-_Default_baseColor.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'file' [asset] = '0/06_-_Default_baseColor.jpg'
      * 'st' [float2]
        * Connected: '/World/carton/Materials/_6___Default/uvset0.outputs:result' @ '/World/carton/Materials/_6___Default/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/carton/Materials/_6___Default/uvset0' (ID: 'UsdPrimvarReader_float2')
    * Implementation: 'id'

---

### /World/carton_01/Materials/_6___Default

* **Prim路径 (Prim Path):**/World/carton_01/Materials/_6___Default
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/carton_01/Materials/_6___Default/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/carton_01/Materials/_6___Default/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f]
        * Connected: '/World/carton_01/Materials/_6___Default/tex_base.outputs:rgb' @ '/World/carton_01/Materials/_6___Default/tex_base'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/06_-_Default_baseColor.jpg'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(1.000, 1.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0.892971'
    * '/World/carton_01/Materials/_6___Default/tex_base' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/06_-_Default_baseColor.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'file' [asset] = '0/06_-_Default_baseColor.jpg'
      * 'st' [float2]
        * Connected: '/World/carton_01/Materials/_6___Default/uvset0.outputs:result' @ '/World/carton_01/Materials/_6___Default/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/carton_01/Materials/_6___Default/uvset0' (ID: 'UsdPrimvarReader_float2')
    * Implementation: 'id'

---

### /World/carton_02/Materials/_6___Default

* **Prim路径 (Prim Path):**/World/carton_02/Materials/_6___Default
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/carton_02/Materials/_6___Default/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/carton_02/Materials/_6___Default/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f]
        * Connected: '/World/carton_02/Materials/_6___Default/tex_base.outputs:rgb' @ '/World/carton_02/Materials/_6___Default/tex_base'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/06_-_Default_baseColor.jpg'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(1.000, 1.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0.892971'
    * '/World/carton_02/Materials/_6___Default/tex_base' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/06_-_Default_baseColor.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'file' [asset] = '0/06_-_Default_baseColor.jpg'
      * 'st' [float2]
        * Connected: '/World/carton_02/Materials/_6___Default/uvset0.outputs:result' @ '/World/carton_02/Materials/_6___Default/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/carton_02/Materials/_6___Default/uvset0' (ID: 'UsdPrimvarReader_float2')
    * Implementation: 'id'

---

### /World/carton_03/Materials/_6___Default

* **Prim路径 (Prim Path):**/World/carton_03/Materials/_6___Default
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/carton_03/Materials/_6___Default/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/carton_03/Materials/_6___Default/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f]
        * Connected: '/World/carton_03/Materials/_6___Default/tex_base.outputs:rgb' @ '/World/carton_03/Materials/_6___Default/tex_base'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/06_-_Default_baseColor.jpg'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(1.000, 1.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0.892971'
    * '/World/carton_03/Materials/_6___Default/tex_base' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/06_-_Default_baseColor.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'file' [asset] = '0/06_-_Default_baseColor.jpg'
      * 'st' [float2]
        * Connected: '/World/carton_03/Materials/_6___Default/uvset0.outputs:result' @ '/World/carton_03/Materials/_6___Default/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/carton_03/Materials/_6___Default/uvset0' (ID: 'UsdPrimvarReader_float2')
    * Implementation: 'id'

---

### /World/WoodenCrate_A1/Looks/Crate

* **Prim路径 (Prim Path):**/World/WoodenCrate_A1/Looks/Crate
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/WoodenCrate_A1/Looks/Crate/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/WoodenCrate_A1/Looks/Crate/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * 纹理引用 (Texture Assets):
      * './Textures/T_WoodenCrates_A1_Albedo.`<UDIM>`.png'
      * './Textures/T_WoodenCrates_A1_Normal.`<UDIM>`.png'
      * './Textures/T_WoodenCrates_A1_ORM.`<UDIM>`.png'
    * Inputs:
      * 'diffuse_texture' [asset] = './Textures/T_WoodenCrates_A1_Albedo.`<UDIM>`.png'
      * 'metallic_texture_influence' [float] = '1'
      * 'normalmap_texture' [asset] = './Textures/T_WoodenCrates_A1_Normal.`<UDIM>`.png'
      * 'ORM_texture' [asset] = './Textures/T_WoodenCrates_A1_ORM.`<UDIM>`.png'
      * 'reflection_roughness_texture_influence' [float] = '1'

---

### /World/WoodenCrate_A2/Looks/Crate

* **Prim路径 (Prim Path):**/World/WoodenCrate_A2/Looks/Crate
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/WoodenCrate_A2/Looks/Crate/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/WoodenCrate_A2/Looks/Crate/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * 纹理引用 (Texture Assets):
      * './Textures/T_WoodenCrates_A1_Albedo.`<UDIM>`.png'
      * './Textures/T_WoodenCrates_A1_Normal.`<UDIM>`.png'
      * './Textures/T_WoodenCrates_A1_ORM.`<UDIM>`.png'
    * Inputs:
      * 'diffuse_texture' [asset] = './Textures/T_WoodenCrates_A1_Albedo.`<UDIM>`.png'
      * 'metallic_texture_influence' [float] = '1'
      * 'normalmap_texture' [asset] = './Textures/T_WoodenCrates_A1_Normal.`<UDIM>`.png'
      * 'ORM_texture' [asset] = './Textures/T_WoodenCrates_A1_ORM.`<UDIM>`.png'
      * 'reflection_roughness_texture_influence' [float] = '1'

---

### /World/WoodenCrate_B1/Looks/Crate

* **Prim路径 (Prim Path):**/World/WoodenCrate_B1/Looks/Crate
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/WoodenCrate_B1/Looks/Crate/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/WoodenCrate_B1/Looks/Crate/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * 纹理引用 (Texture Assets):
      * './Textures/T_WoodenCrates_A1_Albedo.`<UDIM>`.png'
      * './Textures/T_WoodenCrates_A1_Normal.`<UDIM>`.png'
      * './Textures/T_WoodenCrates_A1_ORM.`<UDIM>`.png'
    * Inputs:
      * 'diffuse_texture' [asset] = './Textures/T_WoodenCrates_A1_Albedo.`<UDIM>`.png'
      * 'metallic_texture_influence' [float] = '1'
      * 'normalmap_texture' [asset] = './Textures/T_WoodenCrates_A1_Normal.`<UDIM>`.png'
      * 'ORM_texture' [asset] = './Textures/T_WoodenCrates_A1_ORM.`<UDIM>`.png'
      * 'reflection_roughness_texture_influence' [float] = '1'

---

### /World/WoodenCrate_B2/Looks/Crate

* **Prim路径 (Prim Path):**/World/WoodenCrate_B2/Looks/Crate
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/WoodenCrate_B2/Looks/Crate/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/WoodenCrate_B2/Looks/Crate/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * 纹理引用 (Texture Assets):
      * './Textures/T_WoodenCrates_A1_Albedo.`<UDIM>`.png'
      * './Textures/T_WoodenCrates_A1_Normal.`<UDIM>`.png'
      * './Textures/T_WoodenCrates_A1_ORM.`<UDIM>`.png'
    * Inputs:
      * 'diffuse_texture' [asset] = './Textures/T_WoodenCrates_A1_Albedo.`<UDIM>`.png'
      * 'metallic_texture_influence' [float] = '1'
      * 'normalmap_texture' [asset] = './Textures/T_WoodenCrates_A1_Normal.`<UDIM>`.png'
      * 'ORM_texture' [asset] = './Textures/T_WoodenCrates_A1_ORM.`<UDIM>`.png'
      * 'reflection_roughness_texture_influence' [float] = '1'

---

### /World/RackLargeEmpty_A1_01/Looks/Shelf

* **Prim路径 (Prim Path):**/World/RackLargeEmpty_A1_01/Looks/Shelf
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/RackLargeEmpty_A1_01/Looks/Shelf/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/RackLargeEmpty_A1_01/Looks/Shelf/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * 纹理引用 (Texture Assets):
      * './Textures/T_Rack_A1_Albedo.`<UDIM>`.png'
      * './Textures/T_Rack_A1_Normal.`<UDIM>`.png'
      * './Textures/T_Rack_A1_ORM.`<UDIM>`.png'
    * Inputs:
      * 'diffuse_texture' [asset] = './Textures/T_Rack_A1_Albedo.`<UDIM>`.png'
      * 'metallic_texture_influence' [float] = '1'
      * 'normalmap_texture' [asset] = './Textures/T_Rack_A1_Normal.`<UDIM>`.png'
      * 'ORM_texture' [asset] = './Textures/T_Rack_A1_ORM.`<UDIM>`.png'
      * 'reflection_roughness_texture_influence' [float] = '1'

---

### /World/RackSmallEmpty_A2/Looks/Shelf

* **Prim路径 (Prim Path):**/World/RackSmallEmpty_A2/Looks/Shelf
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/RackSmallEmpty_A2/Looks/Shelf/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/RackSmallEmpty_A2/Looks/Shelf/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * 纹理引用 (Texture Assets):
      * './Textures/T_Rack_A1_Albedo.`<UDIM>`.png'
      * './Textures/T_Rack_A1_Normal.`<UDIM>`.png'
      * './Textures/T_Rack_A1_ORM.`<UDIM>`.png'
    * Inputs:
      * 'diffuse_texture' [asset] = './Textures/T_Rack_A1_Albedo.`<UDIM>`.png'
      * 'metallic_texture_influence' [float] = '1'
      * 'normalmap_texture' [asset] = './Textures/T_Rack_A1_Normal.`<UDIM>`.png'
      * 'ORM_texture' [asset] = './Textures/T_Rack_A1_ORM.`<UDIM>`.png'
      * 'reflection_roughness_texture_influence' [float] = '1'

---

### /World/Cardbox_A1/Looks/Cardboard_A

* **Prim路径 (Prim Path):**/World/Cardbox_A1/Looks/Cardboard_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Cardbox_A1/Looks/Cardboard_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Cardbox_A1/Looks/Cardboard_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * 纹理引用 (Texture Assets):
      * './Textures/T_Cardbox_A1_Albedo.png'
      * './Textures/T_Cardbox_A1_Normal.png'
      * './Textures/T_Cardbox_A1_ORM.png'
    * Inputs:
      * 'diffuse_texture' [asset] = './Textures/T_Cardbox_A1_Albedo.png'
      * 'normalmap_texture' [asset] = './Textures/T_Cardbox_A1_Normal.png'
      * 'ORM_texture' [asset] = './Textures/T_Cardbox_A1_ORM.png'
      * 'reflection_roughness_texture_influence' [float] = '1'

---

### /World/Cardbox_A1_01/Looks/Cardboard_A

* **Prim路径 (Prim Path):**/World/Cardbox_A1_01/Looks/Cardboard_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Cardbox_A1_01/Looks/Cardboard_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Cardbox_A1_01/Looks/Cardboard_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * 纹理引用 (Texture Assets):
      * './Textures/T_Cardbox_A1_Albedo.png'
      * './Textures/T_Cardbox_A1_Normal.png'
      * './Textures/T_Cardbox_A1_ORM.png'
    * Inputs:
      * 'diffuse_texture' [asset] = './Textures/T_Cardbox_A1_Albedo.png'
      * 'normalmap_texture' [asset] = './Textures/T_Cardbox_A1_Normal.png'
      * 'ORM_texture' [asset] = './Textures/T_Cardbox_A1_ORM.png'
      * 'reflection_roughness_texture_influence' [float] = '1'

---

### /World/Cardbox_A1_02/Looks/Cardboard_A

* **Prim路径 (Prim Path):**/World/Cardbox_A1_02/Looks/Cardboard_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Cardbox_A1_02/Looks/Cardboard_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Cardbox_A1_02/Looks/Cardboard_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * 纹理引用 (Texture Assets):
      * './Textures/T_Cardbox_A1_Albedo.png'
      * './Textures/T_Cardbox_A1_Normal.png'
      * './Textures/T_Cardbox_A1_ORM.png'
    * Inputs:
      * 'diffuse_texture' [asset] = './Textures/T_Cardbox_A1_Albedo.png'
      * 'normalmap_texture' [asset] = './Textures/T_Cardbox_A1_Normal.png'
      * 'ORM_texture' [asset] = './Textures/T_Cardbox_A1_ORM.png'
      * 'reflection_roughness_texture_influence' [float] = '1'

---

### /World/Cardbox_B3/Looks/Cardboard_B3

* **Prim路径 (Prim Path):**/World/Cardbox_B3/Looks/Cardboard_B3
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Cardbox_B3/Looks/Cardboard_B3/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Cardbox_B3/Looks/Cardboard_B3/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * 纹理引用 (Texture Assets):
      * './Textures/T_Cardbox_B3_Albedo.png'
      * './Textures/T_Cardbox_B3_Normal.png'
      * './Textures/T_Cardbox_B3_ORM.png'
    * Inputs:
      * 'diffuse_texture' [asset] = './Textures/T_Cardbox_B3_Albedo.png'
      * 'normalmap_texture' [asset] = './Textures/T_Cardbox_B3_Normal.png'
      * 'ORM_texture' [asset] = './Textures/T_Cardbox_B3_ORM.png'
      * 'reflection_roughness_texture_influence' [float] = '1'

---

### /World/Cardbox_C1/Looks/Cardboard_C1

* **Prim路径 (Prim Path):**/World/Cardbox_C1/Looks/Cardboard_C1
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Cardbox_C1/Looks/Cardboard_C1/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Cardbox_C1/Looks/Cardboard_C1/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * 纹理引用 (Texture Assets):
      * './Textures/T_Cardbox_C1_Albedo.png'
      * './Textures/T_Cardbox_C1_Normal.png'
      * './Textures/T_Cardbox_C1_ORM.png'
    * Inputs:
      * 'diffuse_texture' [asset] = './Textures/T_Cardbox_C1_Albedo.png'
      * 'normalmap_texture' [asset] = './Textures/T_Cardbox_C1_Normal.png'
      * 'ORM_texture' [asset] = './Textures/T_Cardbox_C1_ORM.png'
      * 'reflection_roughness_texture_influence' [float] = '1'

---

### /World/Cardbox_B3_01/Looks/Cardboard_B3

* **Prim路径 (Prim Path):**/World/Cardbox_B3_01/Looks/Cardboard_B3
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Cardbox_B3_01/Looks/Cardboard_B3/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Cardbox_B3_01/Looks/Cardboard_B3/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * 纹理引用 (Texture Assets):
      * './Textures/T_Cardbox_B3_Albedo.png'
      * './Textures/T_Cardbox_B3_Normal.png'
      * './Textures/T_Cardbox_B3_ORM.png'
    * Inputs:
      * 'diffuse_texture' [asset] = './Textures/T_Cardbox_B3_Albedo.png'
      * 'normalmap_texture' [asset] = './Textures/T_Cardbox_B3_Normal.png'
      * 'ORM_texture' [asset] = './Textures/T_Cardbox_B3_ORM.png'
      * 'reflection_roughness_texture_influence' [float] = '1'

---

### /World/Cardbox_C2/Looks/Cardboard_C2

* **Prim路径 (Prim Path):**/World/Cardbox_C2/Looks/Cardboard_C2
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Cardbox_C2/Looks/Cardboard_C2/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Cardbox_C2/Looks/Cardboard_C2/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * 纹理引用 (Texture Assets):
      * './Textures/T_Cardbox_C2_Albedo.png'
      * './Textures/T_Cardbox_C2_Normal.png'
      * './Textures/T_Cardbox_C2_ORM.png'
    * Inputs:
      * 'diffuse_texture' [asset] = './Textures/T_Cardbox_C2_Albedo.png'
      * 'normalmap_texture' [asset] = './Textures/T_Cardbox_C2_Normal.png'
      * 'ORM_texture' [asset] = './Textures/T_Cardbox_C2_ORM.png'
      * 'reflection_roughness_texture_influence' [float] = '1'

---

### /World/RackSmallEmpty_A2_01/Looks/Shelf

* **Prim路径 (Prim Path):**/World/RackSmallEmpty_A2_01/Looks/Shelf
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/RackSmallEmpty_A2_01/Looks/Shelf/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/RackSmallEmpty_A2_01/Looks/Shelf/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * 纹理引用 (Texture Assets):
      * './Textures/T_Rack_A1_Albedo.`<UDIM>`.png'
      * './Textures/T_Rack_A1_Normal.`<UDIM>`.png'
      * './Textures/T_Rack_A1_ORM.`<UDIM>`.png'
    * Inputs:
      * 'diffuse_texture' [asset] = './Textures/T_Rack_A1_Albedo.`<UDIM>`.png'
      * 'metallic_texture_influence' [float] = '1'
      * 'normalmap_texture' [asset] = './Textures/T_Rack_A1_Normal.`<UDIM>`.png'
      * 'ORM_texture' [asset] = './Textures/T_Rack_A1_ORM.`<UDIM>`.png'
      * 'reflection_roughness_texture_influence' [float] = '1'

---

### /World/RackLongEmpty_A2/Looks/Shelf

* **Prim路径 (Prim Path):**/World/RackLongEmpty_A2/Looks/Shelf
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/RackLongEmpty_A2/Looks/Shelf/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/RackLongEmpty_A2/Looks/Shelf/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * 纹理引用 (Texture Assets):
      * './Textures/T_Rack_A1_Albedo.`<UDIM>`.png'
      * './Textures/T_Rack_A1_Normal.`<UDIM>`.png'
      * './Textures/T_Rack_A1_ORM.`<UDIM>`.png'
    * Inputs:
      * 'diffuse_texture' [asset] = './Textures/T_Rack_A1_Albedo.`<UDIM>`.png'
      * 'metallic_texture_influence' [float] = '1'
      * 'normalmap_texture' [asset] = './Textures/T_Rack_A1_Normal.`<UDIM>`.png'
      * 'ORM_texture' [asset] = './Textures/T_Rack_A1_ORM.`<UDIM>`.png'
      * 'reflection_roughness_texture_influence' [float] = '1'

---

### /World/RackLongEmpty_A2_01/Looks/Shelf

* **Prim路径 (Prim Path):**/World/RackLongEmpty_A2_01/Looks/Shelf
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/RackLongEmpty_A2_01/Looks/Shelf/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/RackLongEmpty_A2_01/Looks/Shelf/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * 纹理引用 (Texture Assets):
      * './Textures/T_Rack_A1_Albedo.`<UDIM>`.png'
      * './Textures/T_Rack_A1_Normal.`<UDIM>`.png'
      * './Textures/T_Rack_A1_ORM.`<UDIM>`.png'
    * Inputs:
      * 'diffuse_texture' [asset] = './Textures/T_Rack_A1_Albedo.`<UDIM>`.png'
      * 'metallic_texture_influence' [float] = '1'
      * 'normalmap_texture' [asset] = './Textures/T_Rack_A1_Normal.`<UDIM>`.png'
      * 'ORM_texture' [asset] = './Textures/T_Rack_A1_ORM.`<UDIM>`.png'
      * 'reflection_roughness_texture_influence' [float] = '1'

---

### /World/RackLargeEmpty_A1_02/Looks/Shelf

* **Prim路径 (Prim Path):**/World/RackLargeEmpty_A1_02/Looks/Shelf
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/RackLargeEmpty_A1_02/Looks/Shelf/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/RackLargeEmpty_A1_02/Looks/Shelf/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * 纹理引用 (Texture Assets):
      * './Textures/T_Rack_A1_Albedo.`<UDIM>`.png'
      * './Textures/T_Rack_A1_Normal.`<UDIM>`.png'
      * './Textures/T_Rack_A1_ORM.`<UDIM>`.png'
    * Inputs:
      * 'diffuse_texture' [asset] = './Textures/T_Rack_A1_Albedo.`<UDIM>`.png'
      * 'metallic_texture_influence' [float] = '1'
      * 'normalmap_texture' [asset] = './Textures/T_Rack_A1_Normal.`<UDIM>`.png'
      * 'ORM_texture' [asset] = './Textures/T_Rack_A1_ORM.`<UDIM>`.png'
      * 'reflection_roughness_texture_influence' [float] = '1'

---

### /World/WoodenCrate_B2_01/Looks/Crate

* **Prim路径 (Prim Path):**/World/WoodenCrate_B2_01/Looks/Crate
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/WoodenCrate_B2_01/Looks/Crate/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/WoodenCrate_B2_01/Looks/Crate/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * 纹理引用 (Texture Assets):
      * './Textures/T_WoodenCrates_A1_Albedo.`<UDIM>`.png'
      * './Textures/T_WoodenCrates_A1_Normal.`<UDIM>`.png'
      * './Textures/T_WoodenCrates_A1_ORM.`<UDIM>`.png'
    * Inputs:
      * 'diffuse_texture' [asset] = './Textures/T_WoodenCrates_A1_Albedo.`<UDIM>`.png'
      * 'metallic_texture_influence' [float] = '1'
      * 'normalmap_texture' [asset] = './Textures/T_WoodenCrates_A1_Normal.`<UDIM>`.png'
      * 'ORM_texture' [asset] = './Textures/T_WoodenCrates_A1_ORM.`<UDIM>`.png'
      * 'reflection_roughness_texture_influence' [float] = '1'

---

### /World/WoodenCrate_B1_01/Looks/Crate

* **Prim路径 (Prim Path):**/World/WoodenCrate_B1_01/Looks/Crate
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/WoodenCrate_B1_01/Looks/Crate/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/WoodenCrate_B1_01/Looks/Crate/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * 纹理引用 (Texture Assets):
      * './Textures/T_WoodenCrates_A1_Albedo.`<UDIM>`.png'
      * './Textures/T_WoodenCrates_A1_Normal.`<UDIM>`.png'
      * './Textures/T_WoodenCrates_A1_ORM.`<UDIM>`.png'
    * Inputs:
      * 'diffuse_texture' [asset] = './Textures/T_WoodenCrates_A1_Albedo.`<UDIM>`.png'
      * 'metallic_texture_influence' [float] = '1'
      * 'normalmap_texture' [asset] = './Textures/T_WoodenCrates_A1_Normal.`<UDIM>`.png'
      * 'ORM_texture' [asset] = './Textures/T_WoodenCrates_A1_ORM.`<UDIM>`.png'
      * 'reflection_roughness_texture_influence' [float] = '1'

---

### /World/WoodenCrate_A2_01/Looks/Crate

* **Prim路径 (Prim Path):**/World/WoodenCrate_A2_01/Looks/Crate
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/WoodenCrate_A2_01/Looks/Crate/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/WoodenCrate_A2_01/Looks/Crate/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * 纹理引用 (Texture Assets):
      * './Textures/T_WoodenCrates_A1_Albedo.`<UDIM>`.png'
      * './Textures/T_WoodenCrates_A1_Normal.`<UDIM>`.png'
      * './Textures/T_WoodenCrates_A1_ORM.`<UDIM>`.png'
    * Inputs:
      * 'diffuse_texture' [asset] = './Textures/T_WoodenCrates_A1_Albedo.`<UDIM>`.png'
      * 'metallic_texture_influence' [float] = '1'
      * 'normalmap_texture' [asset] = './Textures/T_WoodenCrates_A1_Normal.`<UDIM>`.png'
      * 'ORM_texture' [asset] = './Textures/T_WoodenCrates_A1_ORM.`<UDIM>`.png'
      * 'reflection_roughness_texture_influence' [float] = '1'

---

### /World/WoodenCrate_A1_01/Looks/Crate

* **Prim路径 (Prim Path):**/World/WoodenCrate_A1_01/Looks/Crate
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/WoodenCrate_A1_01/Looks/Crate/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/WoodenCrate_A1_01/Looks/Crate/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * 纹理引用 (Texture Assets):
      * './Textures/T_WoodenCrates_A1_Albedo.`<UDIM>`.png'
      * './Textures/T_WoodenCrates_A1_Normal.`<UDIM>`.png'
      * './Textures/T_WoodenCrates_A1_ORM.`<UDIM>`.png'
    * Inputs:
      * 'diffuse_texture' [asset] = './Textures/T_WoodenCrates_A1_Albedo.`<UDIM>`.png'
      * 'metallic_texture_influence' [float] = '1'
      * 'normalmap_texture' [asset] = './Textures/T_WoodenCrates_A1_Normal.`<UDIM>`.png'
      * 'ORM_texture' [asset] = './Textures/T_WoodenCrates_A1_ORM.`<UDIM>`.png'
      * 'reflection_roughness_texture_influence' [float] = '1'

---

### /World/RackLargeEmpty_A1_03/Looks/Shelf

* **Prim路径 (Prim Path):**/World/RackLargeEmpty_A1_03/Looks/Shelf
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/RackLargeEmpty_A1_03/Looks/Shelf/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/RackLargeEmpty_A1_03/Looks/Shelf/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * 纹理引用 (Texture Assets):
      * './Textures/T_Rack_A1_Albedo.`<UDIM>`.png'
      * './Textures/T_Rack_A1_Normal.`<UDIM>`.png'
      * './Textures/T_Rack_A1_ORM.`<UDIM>`.png'
    * Inputs:
      * 'diffuse_texture' [asset] = './Textures/T_Rack_A1_Albedo.`<UDIM>`.png'
      * 'metallic_texture_influence' [float] = '1'
      * 'normalmap_texture' [asset] = './Textures/T_Rack_A1_Normal.`<UDIM>`.png'
      * 'ORM_texture' [asset] = './Textures/T_Rack_A1_ORM.`<UDIM>`.png'
      * 'reflection_roughness_texture_influence' [float] = '1'

---

### /World/carton_04/Materials/_6___Default

* **Prim路径 (Prim Path):**/World/carton_04/Materials/_6___Default
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/carton_04/Materials/_6___Default/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/carton_04/Materials/_6___Default/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f]
        * Connected: '/World/carton_04/Materials/_6___Default/tex_base.outputs:rgb' @ '/World/carton_04/Materials/_6___Default/tex_base'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/06_-_Default_baseColor.jpg'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(1.000, 1.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0.892971'
    * '/World/carton_04/Materials/_6___Default/tex_base' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/06_-_Default_baseColor.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'file' [asset] = '0/06_-_Default_baseColor.jpg'
      * 'st' [float2]
        * Connected: '/World/carton_04/Materials/_6___Default/uvset0.outputs:result' @ '/World/carton_04/Materials/_6___Default/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/carton_04/Materials/_6___Default/uvset0' (ID: 'UsdPrimvarReader_float2')
    * Implementation: 'id'

---

### /World/carton_05/Materials/_6___Default

* **Prim路径 (Prim Path):**/World/carton_05/Materials/_6___Default
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/carton_05/Materials/_6___Default/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/carton_05/Materials/_6___Default/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f]
        * Connected: '/World/carton_05/Materials/_6___Default/tex_base.outputs:rgb' @ '/World/carton_05/Materials/_6___Default/tex_base'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/06_-_Default_baseColor.jpg'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(1.000, 1.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0.892971'
    * '/World/carton_05/Materials/_6___Default/tex_base' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/06_-_Default_baseColor.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'file' [asset] = '0/06_-_Default_baseColor.jpg'
      * 'st' [float2]
        * Connected: '/World/carton_05/Materials/_6___Default/uvset0.outputs:result' @ '/World/carton_05/Materials/_6___Default/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/carton_05/Materials/_6___Default/uvset0' (ID: 'UsdPrimvarReader_float2')
    * Implementation: 'id'

---

### /World/carton_06/Materials/_6___Default

* **Prim路径 (Prim Path):**/World/carton_06/Materials/_6___Default
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/carton_06/Materials/_6___Default/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/carton_06/Materials/_6___Default/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f]
        * Connected: '/World/carton_06/Materials/_6___Default/tex_base.outputs:rgb' @ '/World/carton_06/Materials/_6___Default/tex_base'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/06_-_Default_baseColor.jpg'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(1.000, 1.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0.892971'
    * '/World/carton_06/Materials/_6___Default/tex_base' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/06_-_Default_baseColor.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'file' [asset] = '0/06_-_Default_baseColor.jpg'
      * 'st' [float2]
        * Connected: '/World/carton_06/Materials/_6___Default/uvset0.outputs:result' @ '/World/carton_06/Materials/_6___Default/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/carton_06/Materials/_6___Default/uvset0' (ID: 'UsdPrimvarReader_float2')
    * Implementation: 'id'

---

### /World/carton_07/Materials/_6___Default

* **Prim路径 (Prim Path):**/World/carton_07/Materials/_6___Default
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/carton_07/Materials/_6___Default/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/carton_07/Materials/_6___Default/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f]
        * Connected: '/World/carton_07/Materials/_6___Default/tex_base.outputs:rgb' @ '/World/carton_07/Materials/_6___Default/tex_base'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/06_-_Default_baseColor.jpg'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(1.000, 1.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0.892971'
    * '/World/carton_07/Materials/_6___Default/tex_base' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/06_-_Default_baseColor.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'file' [asset] = '0/06_-_Default_baseColor.jpg'
      * 'st' [float2]
        * Connected: '/World/carton_07/Materials/_6___Default/uvset0.outputs:result' @ '/World/carton_07/Materials/_6___Default/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/carton_07/Materials/_6___Default/uvset0' (ID: 'UsdPrimvarReader_float2')
    * Implementation: 'id'

---

### /World/Cardbox_C3/Looks/Cardboard_C3

* **Prim路径 (Prim Path):**/World/Cardbox_C3/Looks/Cardboard_C3
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Cardbox_C3/Looks/Cardboard_C3/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Cardbox_C3/Looks/Cardboard_C3/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * 纹理引用 (Texture Assets):
      * './Textures/T_Cardbox_C3_Albedo.png'
      * './Textures/T_Cardbox_C3_Normal.png'
      * './Textures/T_Cardbox_C3_ORM.png'
    * Inputs:
      * 'diffuse_texture' [asset] = './Textures/T_Cardbox_C3_Albedo.png'
      * 'normalmap_texture' [asset] = './Textures/T_Cardbox_C3_Normal.png'
      * 'ORM_texture' [asset] = './Textures/T_Cardbox_C3_ORM.png'
      * 'reflection_roughness_texture_influence' [float] = '1'

---

### /World/Cardbox_C2_01/Looks/Cardboard_C2

* **Prim路径 (Prim Path):**/World/Cardbox_C2_01/Looks/Cardboard_C2
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Cardbox_C2_01/Looks/Cardboard_C2/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Cardbox_C2_01/Looks/Cardboard_C2/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * 纹理引用 (Texture Assets):
      * './Textures/T_Cardbox_C2_Albedo.png'
      * './Textures/T_Cardbox_C2_Normal.png'
      * './Textures/T_Cardbox_C2_ORM.png'
    * Inputs:
      * 'diffuse_texture' [asset] = './Textures/T_Cardbox_C2_Albedo.png'
      * 'normalmap_texture' [asset] = './Textures/T_Cardbox_C2_Normal.png'
      * 'ORM_texture' [asset] = './Textures/T_Cardbox_C2_ORM.png'
      * 'reflection_roughness_texture_influence' [float] = '1'

---

### /World/Cardbox_B3_02/Looks/Cardboard_B3

* **Prim路径 (Prim Path):**/World/Cardbox_B3_02/Looks/Cardboard_B3
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Cardbox_B3_02/Looks/Cardboard_B3/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Cardbox_B3_02/Looks/Cardboard_B3/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * 纹理引用 (Texture Assets):
      * './Textures/T_Cardbox_B3_Albedo.png'
      * './Textures/T_Cardbox_B3_Normal.png'
      * './Textures/T_Cardbox_B3_ORM.png'
    * Inputs:
      * 'diffuse_texture' [asset] = './Textures/T_Cardbox_B3_Albedo.png'
      * 'normalmap_texture' [asset] = './Textures/T_Cardbox_B3_Normal.png'
      * 'ORM_texture' [asset] = './Textures/T_Cardbox_B3_ORM.png'
      * 'reflection_roughness_texture_influence' [float] = '1'

---

### /World/Cardbox_B2/Looks/Cardboard_B2

* **Prim路径 (Prim Path):**/World/Cardbox_B2/Looks/Cardboard_B2
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Cardbox_B2/Looks/Cardboard_B2/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Cardbox_B2/Looks/Cardboard_B2/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * 纹理引用 (Texture Assets):
      * './Textures/T_Cardbox_B2_Albedo.png'
      * './Textures/T_Cardbox_B2_Normal.png'
      * './Textures/T_Cardbox_B2_ORM.png'
    * Inputs:
      * 'diffuse_texture' [asset] = './Textures/T_Cardbox_B2_Albedo.png'
      * 'normalmap_texture' [asset] = './Textures/T_Cardbox_B2_Normal.png'
      * 'ORM_texture' [asset] = './Textures/T_Cardbox_B2_ORM.png'
      * 'reflection_roughness_texture_influence' [float] = '1'

---

### /World/Cardbox_B1/Looks/Cardboard_B1

* **Prim路径 (Prim Path):**/World/Cardbox_B1/Looks/Cardboard_B1
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Cardbox_B1/Looks/Cardboard_B1/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Cardbox_B1/Looks/Cardboard_B1/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * 纹理引用 (Texture Assets):
      * './Textures/T_Cardbox_B1_Albedo.png'
      * './Textures/T_Cardbox_B1_Normal.png'
      * './Textures/T_Cardbox_B1_ORM.png'
    * Inputs:
      * 'diffuse_texture' [asset] = './Textures/T_Cardbox_B1_Albedo.png'
      * 'normalmap_texture' [asset] = './Textures/T_Cardbox_B1_Normal.png'
      * 'ORM_texture' [asset] = './Textures/T_Cardbox_B1_ORM.png'
      * 'reflection_roughness_texture_influence' [float] = '1'

---

### /World/Cardbox_A3/Looks/Cardboard_A3

* **Prim路径 (Prim Path):**/World/Cardbox_A3/Looks/Cardboard_A3
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Cardbox_A3/Looks/Cardboard_A3/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Cardbox_A3/Looks/Cardboard_A3/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * 纹理引用 (Texture Assets):
      * './Textures/T_Cardbox_A3_Albedo.png'
      * './Textures/T_Cardbox_A3_Normal.png'
      * './Textures/T_Cardbox_A3_ORM.png'
    * Inputs:
      * 'diffuse_texture' [asset] = './Textures/T_Cardbox_A3_Albedo.png'
      * 'normalmap_texture' [asset] = './Textures/T_Cardbox_A3_Normal.png'
      * 'ORM_texture' [asset] = './Textures/T_Cardbox_A3_ORM.png'
      * 'reflection_roughness_texture_influence' [float] = '1'

---

### /World/Cardbox_A2/Looks/Cardboard_A2

* **Prim路径 (Prim Path):**/World/Cardbox_A2/Looks/Cardboard_A2
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Cardbox_A2/Looks/Cardboard_A2/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Cardbox_A2/Looks/Cardboard_A2/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * 纹理引用 (Texture Assets):
      * './Textures/T_Cardbox_A2_Albedo.png'
      * './Textures/T_Cardbox_A2_Normal.png'
      * './Textures/T_Cardbox_A2_ORM.png'
    * Inputs:
      * 'diffuse_texture' [asset] = './Textures/T_Cardbox_A2_Albedo.png'
      * 'normalmap_texture' [asset] = './Textures/T_Cardbox_A2_Normal.png'
      * 'ORM_texture' [asset] = './Textures/T_Cardbox_A2_ORM.png'
      * 'reflection_roughness_texture_influence' [float] = '1'

---

### /World/Cardbox_A1_03/Looks/Cardboard_A

* **Prim路径 (Prim Path):**/World/Cardbox_A1_03/Looks/Cardboard_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Cardbox_A1_03/Looks/Cardboard_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Cardbox_A1_03/Looks/Cardboard_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * 纹理引用 (Texture Assets):
      * './Textures/T_Cardbox_A1_Albedo.png'
      * './Textures/T_Cardbox_A1_Normal.png'
      * './Textures/T_Cardbox_A1_ORM.png'
    * Inputs:
      * 'diffuse_texture' [asset] = './Textures/T_Cardbox_A1_Albedo.png'
      * 'normalmap_texture' [asset] = './Textures/T_Cardbox_A1_Normal.png'
      * 'ORM_texture' [asset] = './Textures/T_Cardbox_A1_ORM.png'
      * 'reflection_roughness_texture_influence' [float] = '1'

---

### /World/AGV_ready_1/Materials/ASELSAN_CATS_04

* **Prim路径 (Prim Path):**/World/AGV_ready_1/Materials/ASELSAN_CATS_04
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/AGV_ready_1/Materials/ASELSAN_CATS_04/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/AGV_ready_1/Materials/ASELSAN_CATS_04/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.158, 0.158, 0.158)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/AGV_ready_1/Materials/ASELSAN_CATS_04_2

* **Prim路径 (Prim Path):**/World/AGV_ready_1/Materials/ASELSAN_CATS_04_2
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/AGV_ready_1/Materials/ASELSAN_CATS_04_2/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/AGV_ready_1/Materials/ASELSAN_CATS_04_2/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.769, 0.773, 0.749)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/AGV_ready_1/Materials/ASELSAN_CATS_13

* **Prim路径 (Prim Path):**/World/AGV_ready_1/Materials/ASELSAN_CATS_13
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/AGV_ready_1/Materials/ASELSAN_CATS_13/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/AGV_ready_1/Materials/ASELSAN_CATS_13/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.706, 0.718, 0.729)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/AGV_ready_1/Materials/Color_000

* **Prim路径 (Prim Path):**/World/AGV_ready_1/Materials/Color_000
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/AGV_ready_1/Materials/Color_000/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/AGV_ready_1/Materials/Color_000/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(1.000, 1.000, 1.000)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/AGV_ready_1/Materials/Color_A05

* **Prim路径 (Prim Path):**/World/AGV_ready_1/Materials/Color_A05
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/AGV_ready_1/Materials/Color_A05/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/AGV_ready_1/Materials/Color_A05/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(1.000, 0.000, 0.000)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0.959234'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0'

---

### /World/AGV_ready_1/Materials/Color_A06

* **Prim路径 (Prim Path):**/World/AGV_ready_1/Materials/Color_A06
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/AGV_ready_1/Materials/Color_A06/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/AGV_ready_1/Materials/Color_A06/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.800, 0.000, 0.000)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/AGV_ready_1/Materials/Color_B05

* **Prim路径 (Prim Path):**/World/AGV_ready_1/Materials/Color_B05
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/AGV_ready_1/Materials/Color_B05/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/AGV_ready_1/Materials/Color_B05/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(1.000, 0.247, 0.000)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '1'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0'

---

### /World/AGV_ready_1/Materials/Color_E02

* **Prim路径 (Prim Path):**/World/AGV_ready_1/Materials/Color_E02
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/AGV_ready_1/Materials/Color_E02/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/AGV_ready_1/Materials/Color_E02/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(1.000, 1.000, 0.196)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/AGV_ready_1/Materials/Color_E05

* **Prim路径 (Prim Path):**/World/AGV_ready_1/Materials/Color_E05
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/AGV_ready_1/Materials/Color_E05/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/AGV_ready_1/Materials/Color_E05/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(1.000, 0.910, 0.000)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0.625455'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0.133891'

---

### /World/AGV_ready_1/Materials/Color_F06

* **Prim路径 (Prim Path):**/World/AGV_ready_1/Materials/Color_F06
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/AGV_ready_1/Materials/Color_F06/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/AGV_ready_1/Materials/Color_F06/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.400, 0.800, 0.000)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/AGV_ready_1/Materials/Color_G03

* **Prim路径 (Prim Path):**/World/AGV_ready_1/Materials/Color_G03
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/AGV_ready_1/Materials/Color_G03/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/AGV_ready_1/Materials/Color_G03/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.396, 1.000, 0.396)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/AGV_ready_1/Materials/Color_M02

* **Prim路径 (Prim Path):**/World/AGV_ready_1/Materials/Color_M02
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/AGV_ready_1/Materials/Color_M02/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/AGV_ready_1/Materials/Color_M02/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.776, 0.776, 0.776)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/AGV_ready_1/Materials/Color_M03

* **Prim路径 (Prim Path):**/World/AGV_ready_1/Materials/Color_M03
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/AGV_ready_1/Materials/Color_M03/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/AGV_ready_1/Materials/Color_M03/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.667, 0.667, 0.667)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/AGV_ready_1/Materials/Mtl39

* **Prim路径 (Prim Path):**/World/AGV_ready_1/Materials/Mtl39
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/AGV_ready_1/Materials/Mtl39/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/AGV_ready_1/Materials/Mtl39/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.494, 0.494, 0.494)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/AGV_ready_1/Materials/Mtl6

* **Prim路径 (Prim Path):**/World/AGV_ready_1/Materials/Mtl6
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/AGV_ready_1/Materials/Mtl6/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/AGV_ready_1/Materials/Mtl6/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f]
        * Connected: '/World/AGV_ready_1/Materials/Mtl6/tex_base.outputs:rgb' @ '/World/AGV_ready_1/Materials/Mtl6/tex_base'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/Mtl6_baseColor.jpg'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'
    * '/World/AGV_ready_1/Materials/Mtl6/tex_base' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/Mtl6_baseColor.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'file' [asset] = '0/Mtl6_baseColor.jpg'
      * 'st' [float2]
        * Connected: '/World/AGV_ready_1/Materials/Mtl6/uvset0.outputs:result' @ '/World/AGV_ready_1/Materials/Mtl6/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/AGV_ready_1/Materials/Mtl6/uvset0' (ID: 'UsdPrimvarReader_float2')
    * Implementation: 'id'

---

### /World/AGV_ready_1/Materials/Mtl9

* **Prim路径 (Prim Path):**/World/AGV_ready_1/Materials/Mtl9
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/AGV_ready_1/Materials/Mtl9/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/AGV_ready_1/Materials/Mtl9/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.514, 1.000, 0.000)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/AGV_ready_1/Materials/Silver

* **Prim路径 (Prim Path):**/World/AGV_ready_1/Materials/Silver
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/AGV_ready_1/Materials/Silver/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/AGV_ready_1/Materials/Silver/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.753, 0.753, 0.753)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/AGV_ready_1/Materials/material

* **Prim路径 (Prim Path):**/World/AGV_ready_1/Materials/material
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/AGV_ready_1/Materials/material/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/AGV_ready_1/Materials/material/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f]
        * Connected: '/World/AGV_ready_1/Materials/material/tex_base.outputs:rgb' @ '/World/AGV_ready_1/Materials/material/tex_base'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/material_baseColor.jpg'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'
    * '/World/AGV_ready_1/Materials/material/tex_base' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/material_baseColor.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'file' [asset] = '0/material_baseColor.jpg'
      * 'st' [float2]
        * Connected: '/World/AGV_ready_1/Materials/material/uvset0.outputs:result' @ '/World/AGV_ready_1/Materials/material/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/AGV_ready_1/Materials/material/uvset0' (ID: 'UsdPrimvarReader_float2')
    * Implementation: 'id'

---

### /World/AGV_ready_1/Materials/cash_register_keys

* **Prim路径 (Prim Path):**/World/AGV_ready_1/Materials/cash_register_keys
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/AGV_ready_1/Materials/cash_register_keys/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/AGV_ready_1/Materials/cash_register_keys/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.976, 0.992, 0.973)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/AGV_ready_1/Materials/Chris_Shoe_Sole

* **Prim路径 (Prim Path):**/World/AGV_ready_1/Materials/Chris_Shoe_Sole
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/AGV_ready_1/Materials/Chris_Shoe_Sole/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/AGV_ready_1/Materials/Chris_Shoe_Sole/pbr_shader' (ID: 'UsdPreviewSurface')
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

### /World/AGV_ready_1/Materials/Color_002

* **Prim路径 (Prim Path):**/World/AGV_ready_1/Materials/Color_002
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/AGV_ready_1/Materials/Color_002/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/AGV_ready_1/Materials/Color_002/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.217, 0.217, 0.217)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0.570837'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0'

---

### /World/AGV_ready_1/Materials/Color_005

* **Prim路径 (Prim Path):**/World/AGV_ready_1/Materials/Color_005
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/AGV_ready_1/Materials/Color_005/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/AGV_ready_1/Materials/Color_005/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.130, 0.130, 0.130)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0.710417'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0'

---

### /World/AGV_ready_1/Materials/Color_006

* **Prim路径 (Prim Path):**/World/AGV_ready_1/Materials/Color_006
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/AGV_ready_1/Materials/Color_006/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/AGV_ready_1/Materials/Color_006/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0.237059'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0'

---

### /World/AGV_ready_1/Materials/Color_008

* **Prim路径 (Prim Path):**/World/AGV_ready_1/Materials/Color_008
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/AGV_ready_1/Materials/Color_008/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/AGV_ready_1/Materials/Color_008/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.118, 0.118, 0.118)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0.941027'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0'

---

### /World/AGV_ready_1/Materials/Color_A01

* **Prim路径 (Prim Path):**/World/AGV_ready_1/Materials/Color_A01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/AGV_ready_1/Materials/Color_A01/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/AGV_ready_1/Materials/Color_A01/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(1.000, 0.000, 0.000)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0.965302'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0'

---

### /World/AGV_ready_1/Materials/Color_A11

* **Prim路径 (Prim Path):**/World/AGV_ready_1/Materials/Color_A11
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/AGV_ready_1/Materials/Color_A11/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/AGV_ready_1/Materials/Color_A11/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.600, 0.000, 0.000)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/AGV_ready_1/Materials/Color_M04

* **Prim路径 (Prim Path):**/World/AGV_ready_1/Materials/Color_M04
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/AGV_ready_1/Materials/Color_M04/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/AGV_ready_1/Materials/Color_M04/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.557, 0.557, 0.557)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/AGV_ready_1/Materials/Color_M05

* **Prim路径 (Prim Path):**/World/AGV_ready_1/Materials/Color_M05
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/AGV_ready_1/Materials/Color_M05/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/AGV_ready_1/Materials/Color_M05/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.447, 0.447, 0.447)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/AGV_ready_1/Materials/Color_M06

* **Prim路径 (Prim Path):**/World/AGV_ready_1/Materials/Color_M06
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/AGV_ready_1/Materials/Color_M06/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/AGV_ready_1/Materials/Color_M06/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/AGV_ready_1/Materials/Color_M07

* **Prim路径 (Prim Path):**/World/AGV_ready_1/Materials/Color_M07
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/AGV_ready_1/Materials/Color_M07/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/AGV_ready_1/Materials/Color_M07/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.227, 0.227, 0.227)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/AGV_ready_1/Materials/Color_M09

* **Prim路径 (Prim Path):**/World/AGV_ready_1/Materials/Color_M09
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/AGV_ready_1/Materials/Color_M09/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/AGV_ready_1/Materials/Color_M09/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0.340226'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0.085341'

---

### /World/AGV_ready_1/Materials/FCP_Charcoal_v2

* **Prim路径 (Prim Path):**/World/AGV_ready_1/Materials/FCP_Charcoal_v2
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/AGV_ready_1/Materials/FCP_Charcoal_v2/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/AGV_ready_1/Materials/FCP_Charcoal_v2/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.216, 0.216, 0.216)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/AGV_ready_1/Materials/FrontColor

* **Prim路径 (Prim Path):**/World/AGV_ready_1/Materials/FrontColor
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/AGV_ready_1/Materials/FrontColor/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/AGV_ready_1/Materials/FrontColor/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.504, 0.504, 0.504)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0.637593'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0.218852'

---

### /World/AGV_ready_1/Materials/Light_Blue

* **Prim路径 (Prim Path):**/World/AGV_ready_1/Materials/Light_Blue
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/AGV_ready_1/Materials/Light_Blue/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/AGV_ready_1/Materials/Light_Blue/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.601, 0.601, 0.601)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '1'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0.170303'

---

### /World/AGV_ready_1/Materials/M_0011_Seashell

* **Prim路径 (Prim Path):**/World/AGV_ready_1/Materials/M_0011_Seashell
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/AGV_ready_1/Materials/M_0011_Seashell/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/AGV_ready_1/Materials/M_0011_Seashell/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(1.000, 0.961, 0.933)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/AGV_ready_1/Materials/M_0131_Silver

* **Prim路径 (Prim Path):**/World/AGV_ready_1/Materials/M_0131_Silver
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/AGV_ready_1/Materials/M_0131_Silver/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/AGV_ready_1/Materials/M_0131_Silver/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.242, 0.242, 0.242)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0.613318'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0'

---

### /World/AGV_ready_1/Materials/M_0134_DimGray

* **Prim路径 (Prim Path):**/World/AGV_ready_1/Materials/M_0134_DimGray
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/AGV_ready_1/Materials/M_0134_DimGray/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/AGV_ready_1/Materials/M_0134_DimGray/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.412, 0.412, 0.412)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/AGV_ready_1/Materials/M_0135_DarkGray

* **Prim路径 (Prim Path):**/World/AGV_ready_1/Materials/M_0135_DarkGray
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/AGV_ready_1/Materials/M_0135_DarkGray/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/AGV_ready_1/Materials/M_0135_DarkGray/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.318, 0.318, 0.318)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/AGV_ready_1/Materials/Metal_Silver

* **Prim路径 (Prim Path):**/World/AGV_ready_1/Materials/Metal_Silver
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/AGV_ready_1/Materials/Metal_Silver/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/AGV_ready_1/Materials/Metal_Silver/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.918, 0.914, 0.933)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/AGV_ready_1/Materials/Mtl1

* **Prim路径 (Prim Path):**/World/AGV_ready_1/Materials/Mtl1
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/AGV_ready_1/Materials/Mtl1/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/AGV_ready_1/Materials/Mtl1/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.015, 0.015, 0.015)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0.255265'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/AGV_ready_1/Materials/Mtl10

* **Prim路径 (Prim Path):**/World/AGV_ready_1/Materials/Mtl10
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/AGV_ready_1/Materials/Mtl10/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/AGV_ready_1/Materials/Mtl10/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.322, 0.322, 0.322)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/AGV_ready_1/Materials/Mtl11

* **Prim路径 (Prim Path):**/World/AGV_ready_1/Materials/Mtl11
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/AGV_ready_1/Materials/Mtl11/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/AGV_ready_1/Materials/Mtl11/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.067, 0.757, 0.329)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/AGV_ready_1/Materials/Mtl12

* **Prim路径 (Prim Path):**/World/AGV_ready_1/Materials/Mtl12
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/AGV_ready_1/Materials/Mtl12/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/AGV_ready_1/Materials/Mtl12/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.502, 0.502, 0.502)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/AGV_ready_1/Materials/Mtl13

* **Prim路径 (Prim Path):**/World/AGV_ready_1/Materials/Mtl13
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/AGV_ready_1/Materials/Mtl13/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/AGV_ready_1/Materials/Mtl13/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.008, 0.514, 0.816)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/AGV_ready_1/Materials/Mtl14

* **Prim路径 (Prim Path):**/World/AGV_ready_1/Materials/Mtl14
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/AGV_ready_1/Materials/Mtl14/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/AGV_ready_1/Materials/Mtl14/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.310, 0.310, 0.310)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/AGV_ready_1/Materials/Mtl15

* **Prim路径 (Prim Path):**/World/AGV_ready_1/Materials/Mtl15
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/AGV_ready_1/Materials/Mtl15/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/AGV_ready_1/Materials/Mtl15/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.263, 0.275, 0.275)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/AGV_ready_1/Materials/Mtl16

* **Prim路径 (Prim Path):**/World/AGV_ready_1/Materials/Mtl16
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/AGV_ready_1/Materials/Mtl16/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/AGV_ready_1/Materials/Mtl16/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.698, 0.698, 0.000)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/AGV_ready_1/Materials/Mtl17

* **Prim路径 (Prim Path):**/World/AGV_ready_1/Materials/Mtl17
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/AGV_ready_1/Materials/Mtl17/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/AGV_ready_1/Materials/Mtl17/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.000, 0.863, 1.000)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/AGV_ready_1/Materials/Mtl3

* **Prim路径 (Prim Path):**/World/AGV_ready_1/Materials/Mtl3
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/AGV_ready_1/Materials/Mtl3/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/AGV_ready_1/Materials/Mtl3/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.431, 0.455, 0.498)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/AGV_ready_1/Materials/Mtl35

* **Prim路径 (Prim Path):**/World/AGV_ready_1/Materials/Mtl35
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/AGV_ready_1/Materials/Mtl35/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/AGV_ready_1/Materials/Mtl35/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.792, 0.820, 0.933)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/AGV_ready_1/Materials/Mtl36

* **Prim路径 (Prim Path):**/World/AGV_ready_1/Materials/Mtl36
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/AGV_ready_1/Materials/Mtl36/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/AGV_ready_1/Materials/Mtl36/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.667, 0.698, 0.765)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/AGV_ready_1/Materials/Mtl37

* **Prim路径 (Prim Path):**/World/AGV_ready_1/Materials/Mtl37
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/AGV_ready_1/Materials/Mtl37/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/AGV_ready_1/Materials/Mtl37/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.098, 0.098, 0.098)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/AGV_ready_1/Materials/Mtl3a

* **Prim路径 (Prim Path):**/World/AGV_ready_1/Materials/Mtl3a
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/AGV_ready_1/Materials/Mtl3a/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/AGV_ready_1/Materials/Mtl3a/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.388, 0.369, 0.322)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/AGV_ready_1/Materials/Mtl3b

* **Prim路径 (Prim Path):**/World/AGV_ready_1/Materials/Mtl3b
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/AGV_ready_1/Materials/Mtl3b/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/AGV_ready_1/Materials/Mtl3b/pbr_shader' (ID: 'UsdPreviewSurface')
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

### /World/AGV_ready_1/Materials/Mtl5

* **Prim路径 (Prim Path):**/World/AGV_ready_1/Materials/Mtl5
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/AGV_ready_1/Materials/Mtl5/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/AGV_ready_1/Materials/Mtl5/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.396, 0.408, 0.467)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/AGV_ready_1/Materials/Mtl7

* **Prim路径 (Prim Path):**/World/AGV_ready_1/Materials/Mtl7
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/AGV_ready_1/Materials/Mtl7/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/AGV_ready_1/Materials/Mtl7/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.376, 0.376, 0.376)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/AGV_ready_1/Materials/Mtl8

* **Prim路径 (Prim Path):**/World/AGV_ready_1/Materials/Mtl8
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/AGV_ready_1/Materials/Mtl8/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/AGV_ready_1/Materials/Mtl8/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.173, 0.173, 0.173)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/AGV_ready_1/Materials/Mtla

* **Prim路径 (Prim Path):**/World/AGV_ready_1/Materials/Mtla
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/AGV_ready_1/Materials/Mtla/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/AGV_ready_1/Materials/Mtla/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.612, 0.725, 0.745)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/AGV_ready_1/Materials/Mtlb1

* **Prim路径 (Prim Path):**/World/AGV_ready_1/Materials/Mtlb1
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/AGV_ready_1/Materials/Mtlb1/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/AGV_ready_1/Materials/Mtlb1/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.949, 0.925, 0.933)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/AGV_ready_1/Materials/Stainless_Steel

* **Prim路径 (Prim Path):**/World/AGV_ready_1/Materials/Stainless_Steel
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/AGV_ready_1/Materials/Stainless_Steel/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/AGV_ready_1/Materials/Stainless_Steel/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.292, 0.294, 0.284)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0.431257'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/AGV_ready_1/Materials/Metal_Aluminum_Anodized_1

* **Prim路径 (Prim Path):**/World/AGV_ready_1/Materials/Metal_Aluminum_Anodized_1
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/AGV_ready_1/Materials/Metal_Aluminum_Anodized_1/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/AGV_ready_1/Materials/Metal_Aluminum_Anodized_1/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.260, 0.269, 0.282)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0.309883'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0'

---

### /World/AGV_ready_1/Materials/Metal_Aluminum_Anodized_2

* **Prim路径 (Prim Path):**/World/AGV_ready_1/Materials/Metal_Aluminum_Anodized_2
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/AGV_ready_1/Materials/Metal_Aluminum_Anodized_2/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/AGV_ready_1/Materials/Metal_Aluminum_Anodized_2/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.792, 0.820, 0.859)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/AGV_ready_1/Materials/basic_gray_plastic

* **Prim路径 (Prim Path):**/World/AGV_ready_1/Materials/basic_gray_plastic
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/AGV_ready_1/Materials/basic_gray_plastic/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/AGV_ready_1/Materials/basic_gray_plastic/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0.297745'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0.115685'

---

### /World/AGV_ready_1/Materials/texture

* **Prim路径 (Prim Path):**/World/AGV_ready_1/Materials/texture
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/AGV_ready_1/Materials/texture/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/AGV_ready_1/Materials/texture/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.294, 0.294, 0.294)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/AGV/Materials/Tyre_Bake1_baked

* **Prim路径 (Prim Path):**/World/AGV/Materials/Tyre_Bake1_baked
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/AGV/Materials/Tyre_Bake1_baked/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/AGV/Materials/Tyre_Bake1_baked/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f]
        * Connected: '/World/AGV/Materials/Tyre_Bake1_baked/tex_base.outputs:rgb' @ '/World/AGV/Materials/Tyre_Bake1_baked/tex_base'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/Tyre_Bake1_baked_baseColor.jpg'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float]
        * Connected: '/World/AGV/Materials/Tyre_Bake1_baked/tex_metallic.outputs:r' @ '/World/AGV/Materials/Tyre_Bake1_baked/tex_metallic'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/Tyre_Bake1_baked_metallicRoughness_metal.jpg'
      * 'normal' [normal3f]
        * Connected: '/World/AGV/Materials/Tyre_Bake1_baked/tex_normal.outputs:rgb' @ '/World/AGV/Materials/Tyre_Bake1_baked/tex_normal'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/Tyre_Bake1_baked_normal.jpg'
      * 'occlusion' [float] = '1'
      * 'roughness' [float]
        * Connected: '/World/AGV/Materials/Tyre_Bake1_baked/tex_roughness.outputs:r' @ '/World/AGV/Materials/Tyre_Bake1_baked/tex_roughness'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/Tyre_Bake1_baked_metallicRoughness_rough.jpg'
    * '/World/AGV/Materials/Tyre_Bake1_baked/tex_base' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/Tyre_Bake1_baked_baseColor.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'file' [asset] = '0/Tyre_Bake1_baked_baseColor.jpg'
      * 'st' [float2]
        * Connected: '/World/AGV/Materials/Tyre_Bake1_baked/uvset0.outputs:result' @ '/World/AGV/Materials/Tyre_Bake1_baked/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/AGV/Materials/Tyre_Bake1_baked/uvset0' (ID: 'UsdPrimvarReader_float2')
    * Implementation: 'id'
    * '/World/AGV/Materials/Tyre_Bake1_baked/tex_metallic' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/Tyre_Bake1_baked_metallicRoughness_metal.jpg'
    * Inputs:
      * 'fallback' [float4] = '(0.000, 0.000, 0.000, 1.000)'
      * 'file' [asset] = '0/Tyre_Bake1_baked_metallicRoughness_metal.jpg'
      * 'st' [float2]
        * Connected: '/World/AGV/Materials/Tyre_Bake1_baked/uvset0.outputs:result' @ '/World/AGV/Materials/Tyre_Bake1_baked/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/AGV/Materials/Tyre_Bake1_baked/tex_normal' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/Tyre_Bake1_baked_normal.jpg'
    * Inputs:
      * 'bias' [float4] = '(-1.000, -1.000, -1.000, -1.000)'
      * 'fallback' [float4] = '(0.000, 0.000, 1.000, 1.000)'
      * 'file' [asset] = '0/Tyre_Bake1_baked_normal.jpg'
      * 'scale' [float4] = '(2.000, 2.000, 2.000, 2.000)'
      * 'st' [float2]
        * Connected: '/World/AGV/Materials/Tyre_Bake1_baked/uvset0.outputs:result' @ '/World/AGV/Materials/Tyre_Bake1_baked/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/AGV/Materials/Tyre_Bake1_baked/tex_roughness' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/Tyre_Bake1_baked_metallicRoughness_rough.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 0.000, 0.000, 1.000)'
      * 'file' [asset] = '0/Tyre_Bake1_baked_metallicRoughness_rough.jpg'
      * 'st' [float2]
        * Connected: '/World/AGV/Materials/Tyre_Bake1_baked/uvset0.outputs:result' @ '/World/AGV/Materials/Tyre_Bake1_baked/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'

---

### /World/AGV/Materials/Bolt_003_Bake1_baked

* **Prim路径 (Prim Path):**/World/AGV/Materials/Bolt_003_Bake1_baked
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/AGV/Materials/Bolt_003_Bake1_baked/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/AGV/Materials/Bolt_003_Bake1_baked/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f]
        * Connected: '/World/AGV/Materials/Bolt_003_Bake1_baked/tex_base.outputs:rgb' @ '/World/AGV/Materials/Bolt_003_Bake1_baked/tex_base'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/Bolt.003_Bake1_baked_baseColor.jpg'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float]
        * Connected: '/World/AGV/Materials/Bolt_003_Bake1_baked/tex_metallic.outputs:r' @ '/World/AGV/Materials/Bolt_003_Bake1_baked/tex_metallic'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/Bolt.003_Bake1_baked_metallicRoughness_metal.jpg'
      * 'normal' [normal3f]
        * Connected: '/World/AGV/Materials/Bolt_003_Bake1_baked/tex_normal.outputs:rgb' @ '/World/AGV/Materials/Bolt_003_Bake1_baked/tex_normal'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/Bolt.003_Bake1_baked_normal.jpg'
      * 'occlusion' [float] = '1'
      * 'roughness' [float]
        * Connected: '/World/AGV/Materials/Bolt_003_Bake1_baked/tex_roughness.outputs:r' @ '/World/AGV/Materials/Bolt_003_Bake1_baked/tex_roughness'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/Bolt.003_Bake1_baked_metallicRoughness_rough.jpg'
    * '/World/AGV/Materials/Bolt_003_Bake1_baked/tex_base' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/Bolt.003_Bake1_baked_baseColor.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'file' [asset] = '0/Bolt.003_Bake1_baked_baseColor.jpg'
      * 'st' [float2]
        * Connected: '/World/AGV/Materials/Bolt_003_Bake1_baked/uvset0.outputs:result' @ '/World/AGV/Materials/Bolt_003_Bake1_baked/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/AGV/Materials/Bolt_003_Bake1_baked/uvset0' (ID: 'UsdPrimvarReader_float2')
    * Implementation: 'id'
    * '/World/AGV/Materials/Bolt_003_Bake1_baked/tex_metallic' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/Bolt.003_Bake1_baked_metallicRoughness_metal.jpg'
    * Inputs:
      * 'fallback' [float4] = '(0.000, 0.000, 0.000, 1.000)'
      * 'file' [asset] = '0/Bolt.003_Bake1_baked_metallicRoughness_metal.jpg'
      * 'st' [float2]
        * Connected: '/World/AGV/Materials/Bolt_003_Bake1_baked/uvset0.outputs:result' @ '/World/AGV/Materials/Bolt_003_Bake1_baked/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/AGV/Materials/Bolt_003_Bake1_baked/tex_normal' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/Bolt.003_Bake1_baked_normal.jpg'
    * Inputs:
      * 'bias' [float4] = '(-1.000, -1.000, -1.000, -1.000)'
      * 'fallback' [float4] = '(0.000, 0.000, 1.000, 1.000)'
      * 'file' [asset] = '0/Bolt.003_Bake1_baked_normal.jpg'
      * 'scale' [float4] = '(2.000, 2.000, 2.000, 2.000)'
      * 'st' [float2]
        * Connected: '/World/AGV/Materials/Bolt_003_Bake1_baked/uvset0.outputs:result' @ '/World/AGV/Materials/Bolt_003_Bake1_baked/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/AGV/Materials/Bolt_003_Bake1_baked/tex_roughness' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/Bolt.003_Bake1_baked_metallicRoughness_rough.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 0.000, 0.000, 1.000)'
      * 'file' [asset] = '0/Bolt.003_Bake1_baked_metallicRoughness_rough.jpg'
      * 'st' [float2]
        * Connected: '/World/AGV/Materials/Bolt_003_Bake1_baked/uvset0.outputs:result' @ '/World/AGV/Materials/Bolt_003_Bake1_baked/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'

---

### /World/AGV/Materials/Bolt_004_Bake1_baked

* **Prim路径 (Prim Path):**/World/AGV/Materials/Bolt_004_Bake1_baked
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/AGV/Materials/Bolt_004_Bake1_baked/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/AGV/Materials/Bolt_004_Bake1_baked/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f]
        * Connected: '/World/AGV/Materials/Bolt_004_Bake1_baked/tex_base.outputs:rgb' @ '/World/AGV/Materials/Bolt_004_Bake1_baked/tex_base'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/Bolt.004_Bake1_baked_baseColor.jpg'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float]
        * Connected: '/World/AGV/Materials/Bolt_004_Bake1_baked/tex_metallic.outputs:r' @ '/World/AGV/Materials/Bolt_004_Bake1_baked/tex_metallic'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/Bolt.004_Bake1_baked_metallicRoughness_metal.jpg'
      * 'normal' [normal3f]
        * Connected: '/World/AGV/Materials/Bolt_004_Bake1_baked/tex_normal.outputs:rgb' @ '/World/AGV/Materials/Bolt_004_Bake1_baked/tex_normal'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/Bolt.004_Bake1_baked_normal.jpg'
      * 'occlusion' [float] = '1'
      * 'roughness' [float]
        * Connected: '/World/AGV/Materials/Bolt_004_Bake1_baked/tex_roughness.outputs:r' @ '/World/AGV/Materials/Bolt_004_Bake1_baked/tex_roughness'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/Bolt.004_Bake1_baked_metallicRoughness_rough.jpg'
    * '/World/AGV/Materials/Bolt_004_Bake1_baked/tex_base' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/Bolt.004_Bake1_baked_baseColor.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'file' [asset] = '0/Bolt.004_Bake1_baked_baseColor.jpg'
      * 'st' [float2]
        * Connected: '/World/AGV/Materials/Bolt_004_Bake1_baked/uvset0.outputs:result' @ '/World/AGV/Materials/Bolt_004_Bake1_baked/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/AGV/Materials/Bolt_004_Bake1_baked/uvset0' (ID: 'UsdPrimvarReader_float2')
    * Implementation: 'id'
    * '/World/AGV/Materials/Bolt_004_Bake1_baked/tex_metallic' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/Bolt.004_Bake1_baked_metallicRoughness_metal.jpg'
    * Inputs:
      * 'fallback' [float4] = '(0.000, 0.000, 0.000, 1.000)'
      * 'file' [asset] = '0/Bolt.004_Bake1_baked_metallicRoughness_metal.jpg'
      * 'st' [float2]
        * Connected: '/World/AGV/Materials/Bolt_004_Bake1_baked/uvset0.outputs:result' @ '/World/AGV/Materials/Bolt_004_Bake1_baked/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/AGV/Materials/Bolt_004_Bake1_baked/tex_normal' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/Bolt.004_Bake1_baked_normal.jpg'
    * Inputs:
      * 'bias' [float4] = '(-1.000, -1.000, -1.000, -1.000)'
      * 'fallback' [float4] = '(0.000, 0.000, 1.000, 1.000)'
      * 'file' [asset] = '0/Bolt.004_Bake1_baked_normal.jpg'
      * 'scale' [float4] = '(2.000, 2.000, 2.000, 2.000)'
      * 'st' [float2]
        * Connected: '/World/AGV/Materials/Bolt_004_Bake1_baked/uvset0.outputs:result' @ '/World/AGV/Materials/Bolt_004_Bake1_baked/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/AGV/Materials/Bolt_004_Bake1_baked/tex_roughness' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/Bolt.004_Bake1_baked_metallicRoughness_rough.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 0.000, 0.000, 1.000)'
      * 'file' [asset] = '0/Bolt.004_Bake1_baked_metallicRoughness_rough.jpg'
      * 'st' [float2]
        * Connected: '/World/AGV/Materials/Bolt_004_Bake1_baked/uvset0.outputs:result' @ '/World/AGV/Materials/Bolt_004_Bake1_baked/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'

---

### /World/AGV/Materials/Cylinder_002_Bake1_baked

* **Prim路径 (Prim Path):**/World/AGV/Materials/Cylinder_002_Bake1_baked
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/AGV/Materials/Cylinder_002_Bake1_baked/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/AGV/Materials/Cylinder_002_Bake1_baked/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f]
        * Connected: '/World/AGV/Materials/Cylinder_002_Bake1_baked/tex_base.outputs:rgb' @ '/World/AGV/Materials/Cylinder_002_Bake1_baked/tex_base'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/Cylinder.002_Bake1_baked_baseColor.jpg'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float]
        * Connected: '/World/AGV/Materials/Cylinder_002_Bake1_baked/tex_metallic.outputs:r' @ '/World/AGV/Materials/Cylinder_002_Bake1_baked/tex_metallic'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/Cylinder.002_Bake1_baked_metallicRoughness_metal.jpg'
      * 'normal' [normal3f]
        * Connected: '/World/AGV/Materials/Cylinder_002_Bake1_baked/tex_normal.outputs:rgb' @ '/World/AGV/Materials/Cylinder_002_Bake1_baked/tex_normal'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/Cylinder.002_Bake1_baked_normal.jpg'
      * 'occlusion' [float] = '1'
      * 'roughness' [float]
        * Connected: '/World/AGV/Materials/Cylinder_002_Bake1_baked/tex_roughness.outputs:r' @ '/World/AGV/Materials/Cylinder_002_Bake1_baked/tex_roughness'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/Cylinder.002_Bake1_baked_metallicRoughness_rough.jpg'
    * '/World/AGV/Materials/Cylinder_002_Bake1_baked/tex_base' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/Cylinder.002_Bake1_baked_baseColor.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'file' [asset] = '0/Cylinder.002_Bake1_baked_baseColor.jpg'
      * 'st' [float2]
        * Connected: '/World/AGV/Materials/Cylinder_002_Bake1_baked/uvset0.outputs:result' @ '/World/AGV/Materials/Cylinder_002_Bake1_baked/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/AGV/Materials/Cylinder_002_Bake1_baked/uvset0' (ID: 'UsdPrimvarReader_float2')
    * Implementation: 'id'
    * '/World/AGV/Materials/Cylinder_002_Bake1_baked/tex_metallic' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/Cylinder.002_Bake1_baked_metallicRoughness_metal.jpg'
    * Inputs:
      * 'fallback' [float4] = '(0.000, 0.000, 0.000, 1.000)'
      * 'file' [asset] = '0/Cylinder.002_Bake1_baked_metallicRoughness_metal.jpg'
      * 'st' [float2]
        * Connected: '/World/AGV/Materials/Cylinder_002_Bake1_baked/uvset0.outputs:result' @ '/World/AGV/Materials/Cylinder_002_Bake1_baked/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/AGV/Materials/Cylinder_002_Bake1_baked/tex_normal' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/Cylinder.002_Bake1_baked_normal.jpg'
    * Inputs:
      * 'bias' [float4] = '(-1.000, -1.000, -1.000, -1.000)'
      * 'fallback' [float4] = '(0.000, 0.000, 1.000, 1.000)'
      * 'file' [asset] = '0/Cylinder.002_Bake1_baked_normal.jpg'
      * 'scale' [float4] = '(2.000, 2.000, 2.000, 2.000)'
      * 'st' [float2]
        * Connected: '/World/AGV/Materials/Cylinder_002_Bake1_baked/uvset0.outputs:result' @ '/World/AGV/Materials/Cylinder_002_Bake1_baked/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/AGV/Materials/Cylinder_002_Bake1_baked/tex_roughness' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/Cylinder.002_Bake1_baked_metallicRoughness_rough.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 0.000, 0.000, 1.000)'
      * 'file' [asset] = '0/Cylinder.002_Bake1_baked_metallicRoughness_rough.jpg'
      * 'st' [float2]
        * Connected: '/World/AGV/Materials/Cylinder_002_Bake1_baked/uvset0.outputs:result' @ '/World/AGV/Materials/Cylinder_002_Bake1_baked/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'

---

### /World/AGV/Materials/Cylinder_003_Bake1_baked

* **Prim路径 (Prim Path):**/World/AGV/Materials/Cylinder_003_Bake1_baked
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/AGV/Materials/Cylinder_003_Bake1_baked/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/AGV/Materials/Cylinder_003_Bake1_baked/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f]
        * Connected: '/World/AGV/Materials/Cylinder_003_Bake1_baked/tex_base.outputs:rgb' @ '/World/AGV/Materials/Cylinder_003_Bake1_baked/tex_base'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/Cylinder.003_Bake1_baked_baseColor.jpg'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float]
        * Connected: '/World/AGV/Materials/Cylinder_003_Bake1_baked/tex_metallic.outputs:r' @ '/World/AGV/Materials/Cylinder_003_Bake1_baked/tex_metallic'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/Cylinder.003_Bake1_baked_metallicRoughness_metal.jpg'
      * 'normal' [normal3f]
        * Connected: '/World/AGV/Materials/Cylinder_003_Bake1_baked/tex_normal.outputs:rgb' @ '/World/AGV/Materials/Cylinder_003_Bake1_baked/tex_normal'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/Cylinder.003_Bake1_baked_normal.jpg'
      * 'occlusion' [float] = '1'
      * 'roughness' [float]
        * Connected: '/World/AGV/Materials/Cylinder_003_Bake1_baked/tex_roughness.outputs:r' @ '/World/AGV/Materials/Cylinder_003_Bake1_baked/tex_roughness'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/Cylinder.003_Bake1_baked_metallicRoughness_rough.jpg'
    * '/World/AGV/Materials/Cylinder_003_Bake1_baked/tex_base' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/Cylinder.003_Bake1_baked_baseColor.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'file' [asset] = '0/Cylinder.003_Bake1_baked_baseColor.jpg'
      * 'st' [float2]
        * Connected: '/World/AGV/Materials/Cylinder_003_Bake1_baked/uvset0.outputs:result' @ '/World/AGV/Materials/Cylinder_003_Bake1_baked/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/AGV/Materials/Cylinder_003_Bake1_baked/uvset0' (ID: 'UsdPrimvarReader_float2')
    * Implementation: 'id'
    * '/World/AGV/Materials/Cylinder_003_Bake1_baked/tex_metallic' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/Cylinder.003_Bake1_baked_metallicRoughness_metal.jpg'
    * Inputs:
      * 'fallback' [float4] = '(0.000, 0.000, 0.000, 1.000)'
      * 'file' [asset] = '0/Cylinder.003_Bake1_baked_metallicRoughness_metal.jpg'
      * 'st' [float2]
        * Connected: '/World/AGV/Materials/Cylinder_003_Bake1_baked/uvset0.outputs:result' @ '/World/AGV/Materials/Cylinder_003_Bake1_baked/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/AGV/Materials/Cylinder_003_Bake1_baked/tex_normal' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/Cylinder.003_Bake1_baked_normal.jpg'
    * Inputs:
      * 'bias' [float4] = '(-1.000, -1.000, -1.000, -1.000)'
      * 'fallback' [float4] = '(0.000, 0.000, 1.000, 1.000)'
      * 'file' [asset] = '0/Cylinder.003_Bake1_baked_normal.jpg'
      * 'scale' [float4] = '(2.000, 2.000, 2.000, 2.000)'
      * 'st' [float2]
        * Connected: '/World/AGV/Materials/Cylinder_003_Bake1_baked/uvset0.outputs:result' @ '/World/AGV/Materials/Cylinder_003_Bake1_baked/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/AGV/Materials/Cylinder_003_Bake1_baked/tex_roughness' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/Cylinder.003_Bake1_baked_metallicRoughness_rough.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 0.000, 0.000, 1.000)'
      * 'file' [asset] = '0/Cylinder.003_Bake1_baked_metallicRoughness_rough.jpg'
      * 'st' [float2]
        * Connected: '/World/AGV/Materials/Cylinder_003_Bake1_baked/uvset0.outputs:result' @ '/World/AGV/Materials/Cylinder_003_Bake1_baked/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'

---

### /World/AGV/Materials/Hub_002_Bake1_baked

* **Prim路径 (Prim Path):**/World/AGV/Materials/Hub_002_Bake1_baked
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/AGV/Materials/Hub_002_Bake1_baked/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/AGV/Materials/Hub_002_Bake1_baked/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f]
        * Connected: '/World/AGV/Materials/Hub_002_Bake1_baked/tex_base.outputs:rgb' @ '/World/AGV/Materials/Hub_002_Bake1_baked/tex_base'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/Hub.002_Bake1_baked_baseColor.jpg'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float]
        * Connected: '/World/AGV/Materials/Hub_002_Bake1_baked/tex_metallic.outputs:r' @ '/World/AGV/Materials/Hub_002_Bake1_baked/tex_metallic'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/Hub.002_Bake1_baked_metallicRoughness_metal.jpg'
      * 'normal' [normal3f]
        * Connected: '/World/AGV/Materials/Hub_002_Bake1_baked/tex_normal.outputs:rgb' @ '/World/AGV/Materials/Hub_002_Bake1_baked/tex_normal'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/Hub.002_Bake1_baked_normal.jpg'
      * 'occlusion' [float] = '1'
      * 'roughness' [float]
        * Connected: '/World/AGV/Materials/Hub_002_Bake1_baked/tex_roughness.outputs:r' @ '/World/AGV/Materials/Hub_002_Bake1_baked/tex_roughness'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/Hub.002_Bake1_baked_metallicRoughness_rough.jpg'
    * '/World/AGV/Materials/Hub_002_Bake1_baked/tex_base' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/Hub.002_Bake1_baked_baseColor.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'file' [asset] = '0/Hub.002_Bake1_baked_baseColor.jpg'
      * 'st' [float2]
        * Connected: '/World/AGV/Materials/Hub_002_Bake1_baked/uvset0.outputs:result' @ '/World/AGV/Materials/Hub_002_Bake1_baked/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/AGV/Materials/Hub_002_Bake1_baked/uvset0' (ID: 'UsdPrimvarReader_float2')
    * Implementation: 'id'
    * '/World/AGV/Materials/Hub_002_Bake1_baked/tex_metallic' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/Hub.002_Bake1_baked_metallicRoughness_metal.jpg'
    * Inputs:
      * 'fallback' [float4] = '(0.000, 0.000, 0.000, 1.000)'
      * 'file' [asset] = '0/Hub.002_Bake1_baked_metallicRoughness_metal.jpg'
      * 'st' [float2]
        * Connected: '/World/AGV/Materials/Hub_002_Bake1_baked/uvset0.outputs:result' @ '/World/AGV/Materials/Hub_002_Bake1_baked/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/AGV/Materials/Hub_002_Bake1_baked/tex_normal' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/Hub.002_Bake1_baked_normal.jpg'
    * Inputs:
      * 'bias' [float4] = '(-1.000, -1.000, -1.000, -1.000)'
      * 'fallback' [float4] = '(0.000, 0.000, 1.000, 1.000)'
      * 'file' [asset] = '0/Hub.002_Bake1_baked_normal.jpg'
      * 'scale' [float4] = '(2.000, 2.000, 2.000, 2.000)'
      * 'st' [float2]
        * Connected: '/World/AGV/Materials/Hub_002_Bake1_baked/uvset0.outputs:result' @ '/World/AGV/Materials/Hub_002_Bake1_baked/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/AGV/Materials/Hub_002_Bake1_baked/tex_roughness' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/Hub.002_Bake1_baked_metallicRoughness_rough.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 0.000, 0.000, 1.000)'
      * 'file' [asset] = '0/Hub.002_Bake1_baked_metallicRoughness_rough.jpg'
      * 'st' [float2]
        * Connected: '/World/AGV/Materials/Hub_002_Bake1_baked/uvset0.outputs:result' @ '/World/AGV/Materials/Hub_002_Bake1_baked/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'

---

### /World/AGV/Materials/Hub_003_Bake1_baked

* **Prim路径 (Prim Path):**/World/AGV/Materials/Hub_003_Bake1_baked
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/AGV/Materials/Hub_003_Bake1_baked/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/AGV/Materials/Hub_003_Bake1_baked/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f]
        * Connected: '/World/AGV/Materials/Hub_003_Bake1_baked/tex_base.outputs:rgb' @ '/World/AGV/Materials/Hub_003_Bake1_baked/tex_base'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/Hub.003_Bake1_baked_baseColor.jpg'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float]
        * Connected: '/World/AGV/Materials/Hub_003_Bake1_baked/tex_metallic.outputs:r' @ '/World/AGV/Materials/Hub_003_Bake1_baked/tex_metallic'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/Hub.003_Bake1_baked_metallicRoughness_metal.jpg'
      * 'normal' [normal3f]
        * Connected: '/World/AGV/Materials/Hub_003_Bake1_baked/tex_normal.outputs:rgb' @ '/World/AGV/Materials/Hub_003_Bake1_baked/tex_normal'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/Hub.003_Bake1_baked_normal.jpg'
      * 'occlusion' [float] = '1'
      * 'roughness' [float]
        * Connected: '/World/AGV/Materials/Hub_003_Bake1_baked/tex_roughness.outputs:r' @ '/World/AGV/Materials/Hub_003_Bake1_baked/tex_roughness'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/Hub.003_Bake1_baked_metallicRoughness_rough.jpg'
    * '/World/AGV/Materials/Hub_003_Bake1_baked/tex_base' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/Hub.003_Bake1_baked_baseColor.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'file' [asset] = '0/Hub.003_Bake1_baked_baseColor.jpg'
      * 'st' [float2]
        * Connected: '/World/AGV/Materials/Hub_003_Bake1_baked/uvset0.outputs:result' @ '/World/AGV/Materials/Hub_003_Bake1_baked/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/AGV/Materials/Hub_003_Bake1_baked/uvset0' (ID: 'UsdPrimvarReader_float2')
    * Implementation: 'id'
    * '/World/AGV/Materials/Hub_003_Bake1_baked/tex_metallic' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/Hub.003_Bake1_baked_metallicRoughness_metal.jpg'
    * Inputs:
      * 'fallback' [float4] = '(0.000, 0.000, 0.000, 1.000)'
      * 'file' [asset] = '0/Hub.003_Bake1_baked_metallicRoughness_metal.jpg'
      * 'st' [float2]
        * Connected: '/World/AGV/Materials/Hub_003_Bake1_baked/uvset0.outputs:result' @ '/World/AGV/Materials/Hub_003_Bake1_baked/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/AGV/Materials/Hub_003_Bake1_baked/tex_normal' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/Hub.003_Bake1_baked_normal.jpg'
    * Inputs:
      * 'bias' [float4] = '(-1.000, -1.000, -1.000, -1.000)'
      * 'fallback' [float4] = '(0.000, 0.000, 1.000, 1.000)'
      * 'file' [asset] = '0/Hub.003_Bake1_baked_normal.jpg'
      * 'scale' [float4] = '(2.000, 2.000, 2.000, 2.000)'
      * 'st' [float2]
        * Connected: '/World/AGV/Materials/Hub_003_Bake1_baked/uvset0.outputs:result' @ '/World/AGV/Materials/Hub_003_Bake1_baked/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/AGV/Materials/Hub_003_Bake1_baked/tex_roughness' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/Hub.003_Bake1_baked_metallicRoughness_rough.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 0.000, 0.000, 1.000)'
      * 'file' [asset] = '0/Hub.003_Bake1_baked_metallicRoughness_rough.jpg'
      * 'st' [float2]
        * Connected: '/World/AGV/Materials/Hub_003_Bake1_baked/uvset0.outputs:result' @ '/World/AGV/Materials/Hub_003_Bake1_baked/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'

---

### /World/AGV/Materials/Cube_Bake1_baked

* **Prim路径 (Prim Path):**/World/AGV/Materials/Cube_Bake1_baked
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/AGV/Materials/Cube_Bake1_baked/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/AGV/Materials/Cube_Bake1_baked/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f]
        * Connected: '/World/AGV/Materials/Cube_Bake1_baked/tex_base.outputs:rgb' @ '/World/AGV/Materials/Cube_Bake1_baked/tex_base'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/Cube_Bake1_baked_baseColor.jpg'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float]
        * Connected: '/World/AGV/Materials/Cube_Bake1_baked/tex_metallic.outputs:r' @ '/World/AGV/Materials/Cube_Bake1_baked/tex_metallic'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/Cube_Bake1_baked_metallicRoughness_metal.jpg'
      * 'normal' [normal3f]
        * Connected: '/World/AGV/Materials/Cube_Bake1_baked/tex_normal.outputs:rgb' @ '/World/AGV/Materials/Cube_Bake1_baked/tex_normal'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/Cube_Bake1_baked_normal.jpg'
      * 'occlusion' [float] = '1'
      * 'roughness' [float]
        * Connected: '/World/AGV/Materials/Cube_Bake1_baked/tex_roughness.outputs:r' @ '/World/AGV/Materials/Cube_Bake1_baked/tex_roughness'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/Cube_Bake1_baked_metallicRoughness_rough.jpg'
    * '/World/AGV/Materials/Cube_Bake1_baked/tex_base' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/Cube_Bake1_baked_baseColor.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'file' [asset] = '0/Cube_Bake1_baked_baseColor.jpg'
      * 'st' [float2]
        * Connected: '/World/AGV/Materials/Cube_Bake1_baked/uvset0.outputs:result' @ '/World/AGV/Materials/Cube_Bake1_baked/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/AGV/Materials/Cube_Bake1_baked/uvset0' (ID: 'UsdPrimvarReader_float2')
    * Implementation: 'id'
    * '/World/AGV/Materials/Cube_Bake1_baked/tex_metallic' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/Cube_Bake1_baked_metallicRoughness_metal.jpg'
    * Inputs:
      * 'fallback' [float4] = '(0.000, 0.000, 0.000, 1.000)'
      * 'file' [asset] = '0/Cube_Bake1_baked_metallicRoughness_metal.jpg'
      * 'st' [float2]
        * Connected: '/World/AGV/Materials/Cube_Bake1_baked/uvset0.outputs:result' @ '/World/AGV/Materials/Cube_Bake1_baked/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/AGV/Materials/Cube_Bake1_baked/tex_normal' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/Cube_Bake1_baked_normal.jpg'
    * Inputs:
      * 'bias' [float4] = '(-1.000, -1.000, -1.000, -1.000)'
      * 'fallback' [float4] = '(0.000, 0.000, 1.000, 1.000)'
      * 'file' [asset] = '0/Cube_Bake1_baked_normal.jpg'
      * 'scale' [float4] = '(2.000, 2.000, 2.000, 2.000)'
      * 'st' [float2]
        * Connected: '/World/AGV/Materials/Cube_Bake1_baked/uvset0.outputs:result' @ '/World/AGV/Materials/Cube_Bake1_baked/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/AGV/Materials/Cube_Bake1_baked/tex_roughness' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/Cube_Bake1_baked_metallicRoughness_rough.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 0.000, 0.000, 1.000)'
      * 'file' [asset] = '0/Cube_Bake1_baked_metallicRoughness_rough.jpg'
      * 'st' [float2]
        * Connected: '/World/AGV/Materials/Cube_Bake1_baked/uvset0.outputs:result' @ '/World/AGV/Materials/Cube_Bake1_baked/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'

---

### /World/AGV/Materials/Cube_001_Bake1_baked

* **Prim路径 (Prim Path):**/World/AGV/Materials/Cube_001_Bake1_baked
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/AGV/Materials/Cube_001_Bake1_baked/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/AGV/Materials/Cube_001_Bake1_baked/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f]
        * Connected: '/World/AGV/Materials/Cube_001_Bake1_baked/tex_base.outputs:rgb' @ '/World/AGV/Materials/Cube_001_Bake1_baked/tex_base'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/Cube.001_Bake1_baked_baseColor.jpg'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float]
        * Connected: '/World/AGV/Materials/Cube_001_Bake1_baked/tex_metallic.outputs:r' @ '/World/AGV/Materials/Cube_001_Bake1_baked/tex_metallic'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/Cube.001_Bake1_baked_metallicRoughness_metal.jpg'
      * 'normal' [normal3f]
        * Connected: '/World/AGV/Materials/Cube_001_Bake1_baked/tex_normal.outputs:rgb' @ '/World/AGV/Materials/Cube_001_Bake1_baked/tex_normal'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/Cube.001_Bake1_baked_normal.jpg'
      * 'occlusion' [float] = '1'
      * 'roughness' [float]
        * Connected: '/World/AGV/Materials/Cube_001_Bake1_baked/tex_roughness.outputs:r' @ '/World/AGV/Materials/Cube_001_Bake1_baked/tex_roughness'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/Cube.001_Bake1_baked_metallicRoughness_rough.jpg'
    * '/World/AGV/Materials/Cube_001_Bake1_baked/tex_base' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/Cube.001_Bake1_baked_baseColor.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'file' [asset] = '0/Cube.001_Bake1_baked_baseColor.jpg'
      * 'st' [float2]
        * Connected: '/World/AGV/Materials/Cube_001_Bake1_baked/uvset0.outputs:result' @ '/World/AGV/Materials/Cube_001_Bake1_baked/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/AGV/Materials/Cube_001_Bake1_baked/uvset0' (ID: 'UsdPrimvarReader_float2')
    * Implementation: 'id'
    * '/World/AGV/Materials/Cube_001_Bake1_baked/tex_metallic' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/Cube.001_Bake1_baked_metallicRoughness_metal.jpg'
    * Inputs:
      * 'fallback' [float4] = '(0.000, 0.000, 0.000, 1.000)'
      * 'file' [asset] = '0/Cube.001_Bake1_baked_metallicRoughness_metal.jpg'
      * 'st' [float2]
        * Connected: '/World/AGV/Materials/Cube_001_Bake1_baked/uvset0.outputs:result' @ '/World/AGV/Materials/Cube_001_Bake1_baked/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/AGV/Materials/Cube_001_Bake1_baked/tex_normal' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/Cube.001_Bake1_baked_normal.jpg'
    * Inputs:
      * 'bias' [float4] = '(-1.000, -1.000, -1.000, -1.000)'
      * 'fallback' [float4] = '(0.000, 0.000, 1.000, 1.000)'
      * 'file' [asset] = '0/Cube.001_Bake1_baked_normal.jpg'
      * 'scale' [float4] = '(2.000, 2.000, 2.000, 2.000)'
      * 'st' [float2]
        * Connected: '/World/AGV/Materials/Cube_001_Bake1_baked/uvset0.outputs:result' @ '/World/AGV/Materials/Cube_001_Bake1_baked/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/AGV/Materials/Cube_001_Bake1_baked/tex_roughness' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/Cube.001_Bake1_baked_metallicRoughness_rough.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 0.000, 0.000, 1.000)'
      * 'file' [asset] = '0/Cube.001_Bake1_baked_metallicRoughness_rough.jpg'
      * 'st' [float2]
        * Connected: '/World/AGV/Materials/Cube_001_Bake1_baked/uvset0.outputs:result' @ '/World/AGV/Materials/Cube_001_Bake1_baked/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'

---

### /World/AGV/Materials/Slice_Bake1_baked

* **Prim路径 (Prim Path):**/World/AGV/Materials/Slice_Bake1_baked
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/AGV/Materials/Slice_Bake1_baked/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/AGV/Materials/Slice_Bake1_baked/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f]
        * Connected: '/World/AGV/Materials/Slice_Bake1_baked/tex_base.outputs:rgb' @ '/World/AGV/Materials/Slice_Bake1_baked/tex_base'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/Slice_Bake1_baked_baseColor.jpg'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float]
        * Connected: '/World/AGV/Materials/Slice_Bake1_baked/tex_metallic.outputs:r' @ '/World/AGV/Materials/Slice_Bake1_baked/tex_metallic'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/Slice_Bake1_baked_metallicRoughness_metal.jpg'
      * 'normal' [normal3f]
        * Connected: '/World/AGV/Materials/Slice_Bake1_baked/tex_normal.outputs:rgb' @ '/World/AGV/Materials/Slice_Bake1_baked/tex_normal'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/Slice_Bake1_baked_normal.jpg'
      * 'occlusion' [float] = '1'
      * 'roughness' [float]
        * Connected: '/World/AGV/Materials/Slice_Bake1_baked/tex_roughness.outputs:r' @ '/World/AGV/Materials/Slice_Bake1_baked/tex_roughness'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/Slice_Bake1_baked_metallicRoughness_rough.jpg'
    * '/World/AGV/Materials/Slice_Bake1_baked/tex_base' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/Slice_Bake1_baked_baseColor.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'file' [asset] = '0/Slice_Bake1_baked_baseColor.jpg'
      * 'st' [float2]
        * Connected: '/World/AGV/Materials/Slice_Bake1_baked/uvset0.outputs:result' @ '/World/AGV/Materials/Slice_Bake1_baked/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/AGV/Materials/Slice_Bake1_baked/uvset0' (ID: 'UsdPrimvarReader_float2')
    * Implementation: 'id'
    * '/World/AGV/Materials/Slice_Bake1_baked/tex_metallic' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/Slice_Bake1_baked_metallicRoughness_metal.jpg'
    * Inputs:
      * 'fallback' [float4] = '(0.000, 0.000, 0.000, 1.000)'
      * 'file' [asset] = '0/Slice_Bake1_baked_metallicRoughness_metal.jpg'
      * 'st' [float2]
        * Connected: '/World/AGV/Materials/Slice_Bake1_baked/uvset0.outputs:result' @ '/World/AGV/Materials/Slice_Bake1_baked/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/AGV/Materials/Slice_Bake1_baked/tex_normal' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/Slice_Bake1_baked_normal.jpg'
    * Inputs:
      * 'bias' [float4] = '(-1.000, -1.000, -1.000, -1.000)'
      * 'fallback' [float4] = '(0.000, 0.000, 1.000, 1.000)'
      * 'file' [asset] = '0/Slice_Bake1_baked_normal.jpg'
      * 'scale' [float4] = '(2.000, 2.000, 2.000, 2.000)'
      * 'st' [float2]
        * Connected: '/World/AGV/Materials/Slice_Bake1_baked/uvset0.outputs:result' @ '/World/AGV/Materials/Slice_Bake1_baked/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/AGV/Materials/Slice_Bake1_baked/tex_roughness' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/Slice_Bake1_baked_metallicRoughness_rough.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 0.000, 0.000, 1.000)'
      * 'file' [asset] = '0/Slice_Bake1_baked_metallicRoughness_rough.jpg'
      * 'st' [float2]
        * Connected: '/World/AGV/Materials/Slice_Bake1_baked/uvset0.outputs:result' @ '/World/AGV/Materials/Slice_Bake1_baked/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'

---

### /World/AGV/Materials/Slice_001_Bake1_baked

* **Prim路径 (Prim Path):**/World/AGV/Materials/Slice_001_Bake1_baked
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/AGV/Materials/Slice_001_Bake1_baked/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/AGV/Materials/Slice_001_Bake1_baked/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f]
        * Connected: '/World/AGV/Materials/Slice_001_Bake1_baked/tex_base.outputs:rgb' @ '/World/AGV/Materials/Slice_001_Bake1_baked/tex_base'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/Slice.001_Bake1_baked_baseColor.jpg'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float]
        * Connected: '/World/AGV/Materials/Slice_001_Bake1_baked/tex_metallic.outputs:r' @ '/World/AGV/Materials/Slice_001_Bake1_baked/tex_metallic'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/Slice.001_Bake1_baked_metallicRoughness_metal.jpg'
      * 'normal' [normal3f]
        * Connected: '/World/AGV/Materials/Slice_001_Bake1_baked/tex_normal.outputs:rgb' @ '/World/AGV/Materials/Slice_001_Bake1_baked/tex_normal'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/Slice.001_Bake1_baked_normal.jpg'
      * 'occlusion' [float] = '1'
      * 'roughness' [float]
        * Connected: '/World/AGV/Materials/Slice_001_Bake1_baked/tex_roughness.outputs:r' @ '/World/AGV/Materials/Slice_001_Bake1_baked/tex_roughness'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/Slice.001_Bake1_baked_metallicRoughness_rough.jpg'
    * '/World/AGV/Materials/Slice_001_Bake1_baked/tex_base' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/Slice.001_Bake1_baked_baseColor.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'file' [asset] = '0/Slice.001_Bake1_baked_baseColor.jpg'
      * 'st' [float2]
        * Connected: '/World/AGV/Materials/Slice_001_Bake1_baked/uvset0.outputs:result' @ '/World/AGV/Materials/Slice_001_Bake1_baked/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/AGV/Materials/Slice_001_Bake1_baked/uvset0' (ID: 'UsdPrimvarReader_float2')
    * Implementation: 'id'
    * '/World/AGV/Materials/Slice_001_Bake1_baked/tex_metallic' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/Slice.001_Bake1_baked_metallicRoughness_metal.jpg'
    * Inputs:
      * 'fallback' [float4] = '(0.000, 0.000, 0.000, 1.000)'
      * 'file' [asset] = '0/Slice.001_Bake1_baked_metallicRoughness_metal.jpg'
      * 'st' [float2]
        * Connected: '/World/AGV/Materials/Slice_001_Bake1_baked/uvset0.outputs:result' @ '/World/AGV/Materials/Slice_001_Bake1_baked/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/AGV/Materials/Slice_001_Bake1_baked/tex_normal' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/Slice.001_Bake1_baked_normal.jpg'
    * Inputs:
      * 'bias' [float4] = '(-1.000, -1.000, -1.000, -1.000)'
      * 'fallback' [float4] = '(0.000, 0.000, 1.000, 1.000)'
      * 'file' [asset] = '0/Slice.001_Bake1_baked_normal.jpg'
      * 'scale' [float4] = '(2.000, 2.000, 2.000, 2.000)'
      * 'st' [float2]
        * Connected: '/World/AGV/Materials/Slice_001_Bake1_baked/uvset0.outputs:result' @ '/World/AGV/Materials/Slice_001_Bake1_baked/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/AGV/Materials/Slice_001_Bake1_baked/tex_roughness' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/Slice.001_Bake1_baked_metallicRoughness_rough.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 0.000, 0.000, 1.000)'
      * 'file' [asset] = '0/Slice.001_Bake1_baked_metallicRoughness_rough.jpg'
      * 'st' [float2]
        * Connected: '/World/AGV/Materials/Slice_001_Bake1_baked/uvset0.outputs:result' @ '/World/AGV/Materials/Slice_001_Bake1_baked/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'

---

### /World/AGV/Materials/Cube_002_Bake1_baked

* **Prim路径 (Prim Path):**/World/AGV/Materials/Cube_002_Bake1_baked
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/AGV/Materials/Cube_002_Bake1_baked/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/AGV/Materials/Cube_002_Bake1_baked/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f]
        * Connected: '/World/AGV/Materials/Cube_002_Bake1_baked/tex_base.outputs:rgb' @ '/World/AGV/Materials/Cube_002_Bake1_baked/tex_base'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/Cube.002_Bake1_baked_baseColor.jpg'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float]
        * Connected: '/World/AGV/Materials/Cube_002_Bake1_baked/tex_metallic.outputs:r' @ '/World/AGV/Materials/Cube_002_Bake1_baked/tex_metallic'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/Cube.002_Bake1_baked_metallicRoughness_metal.jpg'
      * 'normal' [normal3f]
        * Connected: '/World/AGV/Materials/Cube_002_Bake1_baked/tex_normal.outputs:rgb' @ '/World/AGV/Materials/Cube_002_Bake1_baked/tex_normal'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/Cube.002_Bake1_baked_normal.jpg'
      * 'occlusion' [float] = '1'
      * 'roughness' [float]
        * Connected: '/World/AGV/Materials/Cube_002_Bake1_baked/tex_roughness.outputs:r' @ '/World/AGV/Materials/Cube_002_Bake1_baked/tex_roughness'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/Cube.002_Bake1_baked_metallicRoughness_rough.jpg'
    * '/World/AGV/Materials/Cube_002_Bake1_baked/tex_base' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/Cube.002_Bake1_baked_baseColor.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'file' [asset] = '0/Cube.002_Bake1_baked_baseColor.jpg'
      * 'st' [float2]
        * Connected: '/World/AGV/Materials/Cube_002_Bake1_baked/uvset0.outputs:result' @ '/World/AGV/Materials/Cube_002_Bake1_baked/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/AGV/Materials/Cube_002_Bake1_baked/uvset0' (ID: 'UsdPrimvarReader_float2')
    * Implementation: 'id'
    * '/World/AGV/Materials/Cube_002_Bake1_baked/tex_metallic' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/Cube.002_Bake1_baked_metallicRoughness_metal.jpg'
    * Inputs:
      * 'fallback' [float4] = '(0.000, 0.000, 0.000, 1.000)'
      * 'file' [asset] = '0/Cube.002_Bake1_baked_metallicRoughness_metal.jpg'
      * 'st' [float2]
        * Connected: '/World/AGV/Materials/Cube_002_Bake1_baked/uvset0.outputs:result' @ '/World/AGV/Materials/Cube_002_Bake1_baked/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/AGV/Materials/Cube_002_Bake1_baked/tex_normal' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/Cube.002_Bake1_baked_normal.jpg'
    * Inputs:
      * 'bias' [float4] = '(-1.000, -1.000, -1.000, -1.000)'
      * 'fallback' [float4] = '(0.000, 0.000, 1.000, 1.000)'
      * 'file' [asset] = '0/Cube.002_Bake1_baked_normal.jpg'
      * 'scale' [float4] = '(2.000, 2.000, 2.000, 2.000)'
      * 'st' [float2]
        * Connected: '/World/AGV/Materials/Cube_002_Bake1_baked/uvset0.outputs:result' @ '/World/AGV/Materials/Cube_002_Bake1_baked/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/AGV/Materials/Cube_002_Bake1_baked/tex_roughness' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/Cube.002_Bake1_baked_metallicRoughness_rough.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 0.000, 0.000, 1.000)'
      * 'file' [asset] = '0/Cube.002_Bake1_baked_metallicRoughness_rough.jpg'
      * 'st' [float2]
        * Connected: '/World/AGV/Materials/Cube_002_Bake1_baked/uvset0.outputs:result' @ '/World/AGV/Materials/Cube_002_Bake1_baked/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'

---

### /World/AGV/Materials/Cube_003_Bake1_baked

* **Prim路径 (Prim Path):**/World/AGV/Materials/Cube_003_Bake1_baked
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/AGV/Materials/Cube_003_Bake1_baked/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/AGV/Materials/Cube_003_Bake1_baked/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f]
        * Connected: '/World/AGV/Materials/Cube_003_Bake1_baked/tex_base.outputs:rgb' @ '/World/AGV/Materials/Cube_003_Bake1_baked/tex_base'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/Cube.003_Bake1_baked_baseColor.jpg'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float]
        * Connected: '/World/AGV/Materials/Cube_003_Bake1_baked/tex_metallic.outputs:r' @ '/World/AGV/Materials/Cube_003_Bake1_baked/tex_metallic'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/Cube.003_Bake1_baked_metallicRoughness_metal.jpg'
      * 'normal' [normal3f]
        * Connected: '/World/AGV/Materials/Cube_003_Bake1_baked/tex_normal.outputs:rgb' @ '/World/AGV/Materials/Cube_003_Bake1_baked/tex_normal'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/Cube.003_Bake1_baked_normal.jpg'
      * 'occlusion' [float] = '1'
      * 'roughness' [float]
        * Connected: '/World/AGV/Materials/Cube_003_Bake1_baked/tex_roughness.outputs:r' @ '/World/AGV/Materials/Cube_003_Bake1_baked/tex_roughness'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/Cube.003_Bake1_baked_metallicRoughness_rough.jpg'
    * '/World/AGV/Materials/Cube_003_Bake1_baked/tex_base' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/Cube.003_Bake1_baked_baseColor.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'file' [asset] = '0/Cube.003_Bake1_baked_baseColor.jpg'
      * 'st' [float2]
        * Connected: '/World/AGV/Materials/Cube_003_Bake1_baked/uvset0.outputs:result' @ '/World/AGV/Materials/Cube_003_Bake1_baked/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/AGV/Materials/Cube_003_Bake1_baked/uvset0' (ID: 'UsdPrimvarReader_float2')
    * Implementation: 'id'
    * '/World/AGV/Materials/Cube_003_Bake1_baked/tex_metallic' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/Cube.003_Bake1_baked_metallicRoughness_metal.jpg'
    * Inputs:
      * 'fallback' [float4] = '(0.000, 0.000, 0.000, 1.000)'
      * 'file' [asset] = '0/Cube.003_Bake1_baked_metallicRoughness_metal.jpg'
      * 'st' [float2]
        * Connected: '/World/AGV/Materials/Cube_003_Bake1_baked/uvset0.outputs:result' @ '/World/AGV/Materials/Cube_003_Bake1_baked/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/AGV/Materials/Cube_003_Bake1_baked/tex_normal' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/Cube.003_Bake1_baked_normal.jpg'
    * Inputs:
      * 'bias' [float4] = '(-1.000, -1.000, -1.000, -1.000)'
      * 'fallback' [float4] = '(0.000, 0.000, 1.000, 1.000)'
      * 'file' [asset] = '0/Cube.003_Bake1_baked_normal.jpg'
      * 'scale' [float4] = '(2.000, 2.000, 2.000, 2.000)'
      * 'st' [float2]
        * Connected: '/World/AGV/Materials/Cube_003_Bake1_baked/uvset0.outputs:result' @ '/World/AGV/Materials/Cube_003_Bake1_baked/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/AGV/Materials/Cube_003_Bake1_baked/tex_roughness' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/Cube.003_Bake1_baked_metallicRoughness_rough.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 0.000, 0.000, 1.000)'
      * 'file' [asset] = '0/Cube.003_Bake1_baked_metallicRoughness_rough.jpg'
      * 'st' [float2]
        * Connected: '/World/AGV/Materials/Cube_003_Bake1_baked/uvset0.outputs:result' @ '/World/AGV/Materials/Cube_003_Bake1_baked/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'

---

### /World/AGV/Materials/Cylinder_004_Bake1_baked

* **Prim路径 (Prim Path):**/World/AGV/Materials/Cylinder_004_Bake1_baked
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/AGV/Materials/Cylinder_004_Bake1_baked/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/AGV/Materials/Cylinder_004_Bake1_baked/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f]
        * Connected: '/World/AGV/Materials/Cylinder_004_Bake1_baked/tex_base.outputs:rgb' @ '/World/AGV/Materials/Cylinder_004_Bake1_baked/tex_base'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/Cylinder.004_Bake1_baked_baseColor.jpg'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float]
        * Connected: '/World/AGV/Materials/Cylinder_004_Bake1_baked/tex_metallic.outputs:r' @ '/World/AGV/Materials/Cylinder_004_Bake1_baked/tex_metallic'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/Cylinder.004_Bake1_baked_metallicRoughness_metal.jpg'
      * 'normal' [normal3f]
        * Connected: '/World/AGV/Materials/Cylinder_004_Bake1_baked/tex_normal.outputs:rgb' @ '/World/AGV/Materials/Cylinder_004_Bake1_baked/tex_normal'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/Cylinder.004_Bake1_baked_normal.jpg'
      * 'occlusion' [float] = '1'
      * 'roughness' [float]
        * Connected: '/World/AGV/Materials/Cylinder_004_Bake1_baked/tex_roughness.outputs:r' @ '/World/AGV/Materials/Cylinder_004_Bake1_baked/tex_roughness'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/Cylinder.004_Bake1_baked_metallicRoughness_rough.jpg'
    * '/World/AGV/Materials/Cylinder_004_Bake1_baked/tex_base' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/Cylinder.004_Bake1_baked_baseColor.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'file' [asset] = '0/Cylinder.004_Bake1_baked_baseColor.jpg'
      * 'st' [float2]
        * Connected: '/World/AGV/Materials/Cylinder_004_Bake1_baked/uvset0.outputs:result' @ '/World/AGV/Materials/Cylinder_004_Bake1_baked/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/AGV/Materials/Cylinder_004_Bake1_baked/uvset0' (ID: 'UsdPrimvarReader_float2')
    * Implementation: 'id'
    * '/World/AGV/Materials/Cylinder_004_Bake1_baked/tex_metallic' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/Cylinder.004_Bake1_baked_metallicRoughness_metal.jpg'
    * Inputs:
      * 'fallback' [float4] = '(0.000, 0.000, 0.000, 1.000)'
      * 'file' [asset] = '0/Cylinder.004_Bake1_baked_metallicRoughness_metal.jpg'
      * 'st' [float2]
        * Connected: '/World/AGV/Materials/Cylinder_004_Bake1_baked/uvset0.outputs:result' @ '/World/AGV/Materials/Cylinder_004_Bake1_baked/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/AGV/Materials/Cylinder_004_Bake1_baked/tex_normal' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/Cylinder.004_Bake1_baked_normal.jpg'
    * Inputs:
      * 'bias' [float4] = '(-1.000, -1.000, -1.000, -1.000)'
      * 'fallback' [float4] = '(0.000, 0.000, 1.000, 1.000)'
      * 'file' [asset] = '0/Cylinder.004_Bake1_baked_normal.jpg'
      * 'scale' [float4] = '(2.000, 2.000, 2.000, 2.000)'
      * 'st' [float2]
        * Connected: '/World/AGV/Materials/Cylinder_004_Bake1_baked/uvset0.outputs:result' @ '/World/AGV/Materials/Cylinder_004_Bake1_baked/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/AGV/Materials/Cylinder_004_Bake1_baked/tex_roughness' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/Cylinder.004_Bake1_baked_metallicRoughness_rough.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 0.000, 0.000, 1.000)'
      * 'file' [asset] = '0/Cylinder.004_Bake1_baked_metallicRoughness_rough.jpg'
      * 'st' [float2]
        * Connected: '/World/AGV/Materials/Cylinder_004_Bake1_baked/uvset0.outputs:result' @ '/World/AGV/Materials/Cylinder_004_Bake1_baked/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'

---

### /World/AGV/Materials/Cylinder_006_Bake1_baked

* **Prim路径 (Prim Path):**/World/AGV/Materials/Cylinder_006_Bake1_baked
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/AGV/Materials/Cylinder_006_Bake1_baked/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/AGV/Materials/Cylinder_006_Bake1_baked/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f]
        * Connected: '/World/AGV/Materials/Cylinder_006_Bake1_baked/tex_base.outputs:rgb' @ '/World/AGV/Materials/Cylinder_006_Bake1_baked/tex_base'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/Cylinder.006_Bake1_baked_baseColor.jpg'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float]
        * Connected: '/World/AGV/Materials/Cylinder_006_Bake1_baked/tex_metallic.outputs:r' @ '/World/AGV/Materials/Cylinder_006_Bake1_baked/tex_metallic'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/Cylinder.006_Bake1_baked_metallicRoughness_metal.jpg'
      * 'normal' [normal3f]
        * Connected: '/World/AGV/Materials/Cylinder_006_Bake1_baked/tex_normal.outputs:rgb' @ '/World/AGV/Materials/Cylinder_006_Bake1_baked/tex_normal'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/Cylinder.006_Bake1_baked_normal.jpg'
      * 'occlusion' [float] = '1'
      * 'roughness' [float]
        * Connected: '/World/AGV/Materials/Cylinder_006_Bake1_baked/tex_roughness.outputs:r' @ '/World/AGV/Materials/Cylinder_006_Bake1_baked/tex_roughness'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/Cylinder.006_Bake1_baked_metallicRoughness_rough.jpg'
    * '/World/AGV/Materials/Cylinder_006_Bake1_baked/tex_base' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/Cylinder.006_Bake1_baked_baseColor.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'file' [asset] = '0/Cylinder.006_Bake1_baked_baseColor.jpg'
      * 'st' [float2]
        * Connected: '/World/AGV/Materials/Cylinder_006_Bake1_baked/uvset0.outputs:result' @ '/World/AGV/Materials/Cylinder_006_Bake1_baked/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/AGV/Materials/Cylinder_006_Bake1_baked/uvset0' (ID: 'UsdPrimvarReader_float2')
    * Implementation: 'id'
    * '/World/AGV/Materials/Cylinder_006_Bake1_baked/tex_metallic' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/Cylinder.006_Bake1_baked_metallicRoughness_metal.jpg'
    * Inputs:
      * 'fallback' [float4] = '(0.000, 0.000, 0.000, 1.000)'
      * 'file' [asset] = '0/Cylinder.006_Bake1_baked_metallicRoughness_metal.jpg'
      * 'st' [float2]
        * Connected: '/World/AGV/Materials/Cylinder_006_Bake1_baked/uvset0.outputs:result' @ '/World/AGV/Materials/Cylinder_006_Bake1_baked/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/AGV/Materials/Cylinder_006_Bake1_baked/tex_normal' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/Cylinder.006_Bake1_baked_normal.jpg'
    * Inputs:
      * 'bias' [float4] = '(-1.000, -1.000, -1.000, -1.000)'
      * 'fallback' [float4] = '(0.000, 0.000, 1.000, 1.000)'
      * 'file' [asset] = '0/Cylinder.006_Bake1_baked_normal.jpg'
      * 'scale' [float4] = '(2.000, 2.000, 2.000, 2.000)'
      * 'st' [float2]
        * Connected: '/World/AGV/Materials/Cylinder_006_Bake1_baked/uvset0.outputs:result' @ '/World/AGV/Materials/Cylinder_006_Bake1_baked/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/AGV/Materials/Cylinder_006_Bake1_baked/tex_roughness' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/Cylinder.006_Bake1_baked_metallicRoughness_rough.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 0.000, 0.000, 1.000)'
      * 'file' [asset] = '0/Cylinder.006_Bake1_baked_metallicRoughness_rough.jpg'
      * 'st' [float2]
        * Connected: '/World/AGV/Materials/Cylinder_006_Bake1_baked/uvset0.outputs:result' @ '/World/AGV/Materials/Cylinder_006_Bake1_baked/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'

---

### /World/AGV/Materials/Front_lambert1_0_Bake1_baked

* **Prim路径 (Prim Path):**/World/AGV/Materials/Front_lambert1_0_Bake1_baked
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/AGV/Materials/Front_lambert1_0_Bake1_baked/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/AGV/Materials/Front_lambert1_0_Bake1_baked/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f]
        * Connected: '/World/AGV/Materials/Front_lambert1_0_Bake1_baked/tex_base.outputs:rgb' @ '/World/AGV/Materials/Front_lambert1_0_Bake1_baked/tex_base'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/Front_lambert1_0_Bake1_baked_baseColor.jpg'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float]
        * Connected: '/World/AGV/Materials/Front_lambert1_0_Bake1_baked/tex_metallic.outputs:r' @ '/World/AGV/Materials/Front_lambert1_0_Bake1_baked/tex_metallic'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/Front_lambert1_0_Bake1_baked_metallicRoughness_metal.jpg'
      * 'normal' [normal3f]
        * Connected: '/World/AGV/Materials/Front_lambert1_0_Bake1_baked/tex_normal.outputs:rgb' @ '/World/AGV/Materials/Front_lambert1_0_Bake1_baked/tex_normal'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/Front_lambert1_0_Bake1_baked_normal.jpg'
      * 'occlusion' [float] = '1'
      * 'roughness' [float]
        * Connected: '/World/AGV/Materials/Front_lambert1_0_Bake1_baked/tex_roughness.outputs:r' @ '/World/AGV/Materials/Front_lambert1_0_Bake1_baked/tex_roughness'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/Front_lambert1_0_Bake1_baked_metallicRoughness_rough.jpg'
    * '/World/AGV/Materials/Front_lambert1_0_Bake1_baked/tex_base' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/Front_lambert1_0_Bake1_baked_baseColor.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'file' [asset] = '0/Front_lambert1_0_Bake1_baked_baseColor.jpg'
      * 'st' [float2]
        * Connected: '/World/AGV/Materials/Front_lambert1_0_Bake1_baked/uvset0.outputs:result' @ '/World/AGV/Materials/Front_lambert1_0_Bake1_baked/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/AGV/Materials/Front_lambert1_0_Bake1_baked/uvset0' (ID: 'UsdPrimvarReader_float2')
    * Implementation: 'id'
    * '/World/AGV/Materials/Front_lambert1_0_Bake1_baked/tex_metallic' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/Front_lambert1_0_Bake1_baked_metallicRoughness_metal.jpg'
    * Inputs:
      * 'fallback' [float4] = '(0.000, 0.000, 0.000, 1.000)'
      * 'file' [asset] = '0/Front_lambert1_0_Bake1_baked_metallicRoughness_metal.jpg'
      * 'st' [float2]
        * Connected: '/World/AGV/Materials/Front_lambert1_0_Bake1_baked/uvset0.outputs:result' @ '/World/AGV/Materials/Front_lambert1_0_Bake1_baked/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/AGV/Materials/Front_lambert1_0_Bake1_baked/tex_normal' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/Front_lambert1_0_Bake1_baked_normal.jpg'
    * Inputs:
      * 'bias' [float4] = '(-1.000, -1.000, -1.000, -1.000)'
      * 'fallback' [float4] = '(0.000, 0.000, 1.000, 1.000)'
      * 'file' [asset] = '0/Front_lambert1_0_Bake1_baked_normal.jpg'
      * 'scale' [float4] = '(2.000, 2.000, 2.000, 2.000)'
      * 'st' [float2]
        * Connected: '/World/AGV/Materials/Front_lambert1_0_Bake1_baked/uvset0.outputs:result' @ '/World/AGV/Materials/Front_lambert1_0_Bake1_baked/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/AGV/Materials/Front_lambert1_0_Bake1_baked/tex_roughness' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/Front_lambert1_0_Bake1_baked_metallicRoughness_rough.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 0.000, 0.000, 1.000)'
      * 'file' [asset] = '0/Front_lambert1_0_Bake1_baked_metallicRoughness_rough.jpg'
      * 'st' [float2]
        * Connected: '/World/AGV/Materials/Front_lambert1_0_Bake1_baked/uvset0.outputs:result' @ '/World/AGV/Materials/Front_lambert1_0_Bake1_baked/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'

---

### /World/AGV/Materials/pCylinder27_lambert1_0_Bake1_baked

* **Prim路径 (Prim Path):**/World/AGV/Materials/pCylinder27_lambert1_0_Bake1_baked
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/AGV/Materials/pCylinder27_lambert1_0_Bake1_baked/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/AGV/Materials/pCylinder27_lambert1_0_Bake1_baked/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f]
        * Connected: '/World/AGV/Materials/pCylinder27_lambert1_0_Bake1_baked/tex_base.outputs:rgb' @ '/World/AGV/Materials/pCylinder27_lambert1_0_Bake1_baked/tex_base'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/pCylinder27_lambert1_0_Bake1_baked_baseColor.jpg'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float]
        * Connected: '/World/AGV/Materials/pCylinder27_lambert1_0_Bake1_baked/tex_metallic.outputs:r' @ '/World/AGV/Materials/pCylinder27_lambert1_0_Bake1_baked/tex_metallic'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/pCylinder27_lambert1_0_Bake1_baked_metallicRoughness_metal.jpg'
      * 'normal' [normal3f]
        * Connected: '/World/AGV/Materials/pCylinder27_lambert1_0_Bake1_baked/tex_normal.outputs:rgb' @ '/World/AGV/Materials/pCylinder27_lambert1_0_Bake1_baked/tex_normal'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/pCylinder27_lambert1_0_Bake1_baked_normal.jpg'
      * 'occlusion' [float] = '1'
      * 'roughness' [float]
        * Connected: '/World/AGV/Materials/pCylinder27_lambert1_0_Bake1_baked/tex_roughness.outputs:r' @ '/World/AGV/Materials/pCylinder27_lambert1_0_Bake1_baked/tex_roughness'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/pCylinder27_lambert1_0_Bake1_baked_metallicRoughness_rough.jpg'
    * '/World/AGV/Materials/pCylinder27_lambert1_0_Bake1_baked/tex_base' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/pCylinder27_lambert1_0_Bake1_baked_baseColor.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'file' [asset] = '0/pCylinder27_lambert1_0_Bake1_baked_baseColor.jpg'
      * 'st' [float2]
        * Connected: '/World/AGV/Materials/pCylinder27_lambert1_0_Bake1_baked/uvset0.outputs:result' @ '/World/AGV/Materials/pCylinder27_lambert1_0_Bake1_baked/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/AGV/Materials/pCylinder27_lambert1_0_Bake1_baked/uvset0' (ID: 'UsdPrimvarReader_float2')
    * Implementation: 'id'
    * '/World/AGV/Materials/pCylinder27_lambert1_0_Bake1_baked/tex_metallic' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/pCylinder27_lambert1_0_Bake1_baked_metallicRoughness_metal.jpg'
    * Inputs:
      * 'fallback' [float4] = '(0.000, 0.000, 0.000, 1.000)'
      * 'file' [asset] = '0/pCylinder27_lambert1_0_Bake1_baked_metallicRoughness_metal.jpg'
      * 'st' [float2]
        * Connected: '/World/AGV/Materials/pCylinder27_lambert1_0_Bake1_baked/uvset0.outputs:result' @ '/World/AGV/Materials/pCylinder27_lambert1_0_Bake1_baked/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/AGV/Materials/pCylinder27_lambert1_0_Bake1_baked/tex_normal' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/pCylinder27_lambert1_0_Bake1_baked_normal.jpg'
    * Inputs:
      * 'bias' [float4] = '(-1.000, -1.000, -1.000, -1.000)'
      * 'fallback' [float4] = '(0.000, 0.000, 1.000, 1.000)'
      * 'file' [asset] = '0/pCylinder27_lambert1_0_Bake1_baked_normal.jpg'
      * 'scale' [float4] = '(2.000, 2.000, 2.000, 2.000)'
      * 'st' [float2]
        * Connected: '/World/AGV/Materials/pCylinder27_lambert1_0_Bake1_baked/uvset0.outputs:result' @ '/World/AGV/Materials/pCylinder27_lambert1_0_Bake1_baked/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/AGV/Materials/pCylinder27_lambert1_0_Bake1_baked/tex_roughness' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/pCylinder27_lambert1_0_Bake1_baked_metallicRoughness_rough.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 0.000, 0.000, 1.000)'
      * 'file' [asset] = '0/pCylinder27_lambert1_0_Bake1_baked_metallicRoughness_rough.jpg'
      * 'st' [float2]
        * Connected: '/World/AGV/Materials/pCylinder27_lambert1_0_Bake1_baked/uvset0.outputs:result' @ '/World/AGV/Materials/pCylinder27_lambert1_0_Bake1_baked/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'

---

### /World/AGV/Materials/polySurface35_lambert1_0_Bake1_baked

* **Prim路径 (Prim Path):**/World/AGV/Materials/polySurface35_lambert1_0_Bake1_baked
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/AGV/Materials/polySurface35_lambert1_0_Bake1_baked/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/AGV/Materials/polySurface35_lambert1_0_Bake1_baked/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f]
        * Connected: '/World/AGV/Materials/polySurface35_lambert1_0_Bake1_baked/tex_base.outputs:rgb' @ '/World/AGV/Materials/polySurface35_lambert1_0_Bake1_baked/tex_base'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/polySurface35_lambert1_0_Bake1_baked_baseColor.jpg'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float]
        * Connected: '/World/AGV/Materials/polySurface35_lambert1_0_Bake1_baked/tex_metallic.outputs:r' @ '/World/AGV/Materials/polySurface35_lambert1_0_Bake1_baked/tex_metallic'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/polySurface35_lambert1_0_Bake1_baked_metallicRoughness_metal.jpg'
      * 'normal' [normal3f]
        * Connected: '/World/AGV/Materials/polySurface35_lambert1_0_Bake1_baked/tex_normal.outputs:rgb' @ '/World/AGV/Materials/polySurface35_lambert1_0_Bake1_baked/tex_normal'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/polySurface35_lambert1_0_Bake1_baked_normal.jpg'
      * 'occlusion' [float] = '1'
      * 'roughness' [float]
        * Connected: '/World/AGV/Materials/polySurface35_lambert1_0_Bake1_baked/tex_roughness.outputs:r' @ '/World/AGV/Materials/polySurface35_lambert1_0_Bake1_baked/tex_roughness'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/polySurface35_lambert1_0_Bake1_baked_metallicRoughness_rough.jpg'
    * '/World/AGV/Materials/polySurface35_lambert1_0_Bake1_baked/tex_base' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/polySurface35_lambert1_0_Bake1_baked_baseColor.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'file' [asset] = '0/polySurface35_lambert1_0_Bake1_baked_baseColor.jpg'
      * 'st' [float2]
        * Connected: '/World/AGV/Materials/polySurface35_lambert1_0_Bake1_baked/uvset0.outputs:result' @ '/World/AGV/Materials/polySurface35_lambert1_0_Bake1_baked/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/AGV/Materials/polySurface35_lambert1_0_Bake1_baked/uvset0' (ID: 'UsdPrimvarReader_float2')
    * Implementation: 'id'
    * '/World/AGV/Materials/polySurface35_lambert1_0_Bake1_baked/tex_metallic' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/polySurface35_lambert1_0_Bake1_baked_metallicRoughness_metal.jpg'
    * Inputs:
      * 'fallback' [float4] = '(0.000, 0.000, 0.000, 1.000)'
      * 'file' [asset] = '0/polySurface35_lambert1_0_Bake1_baked_metallicRoughness_metal.jpg'
      * 'st' [float2]
        * Connected: '/World/AGV/Materials/polySurface35_lambert1_0_Bake1_baked/uvset0.outputs:result' @ '/World/AGV/Materials/polySurface35_lambert1_0_Bake1_baked/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/AGV/Materials/polySurface35_lambert1_0_Bake1_baked/tex_normal' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/polySurface35_lambert1_0_Bake1_baked_normal.jpg'
    * Inputs:
      * 'bias' [float4] = '(-1.000, -1.000, -1.000, -1.000)'
      * 'fallback' [float4] = '(0.000, 0.000, 1.000, 1.000)'
      * 'file' [asset] = '0/polySurface35_lambert1_0_Bake1_baked_normal.jpg'
      * 'scale' [float4] = '(2.000, 2.000, 2.000, 2.000)'
      * 'st' [float2]
        * Connected: '/World/AGV/Materials/polySurface35_lambert1_0_Bake1_baked/uvset0.outputs:result' @ '/World/AGV/Materials/polySurface35_lambert1_0_Bake1_baked/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/AGV/Materials/polySurface35_lambert1_0_Bake1_baked/tex_roughness' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/polySurface35_lambert1_0_Bake1_baked_metallicRoughness_rough.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 0.000, 0.000, 1.000)'
      * 'file' [asset] = '0/polySurface35_lambert1_0_Bake1_baked_metallicRoughness_rough.jpg'
      * 'st' [float2]
        * Connected: '/World/AGV/Materials/polySurface35_lambert1_0_Bake1_baked/uvset0.outputs:result' @ '/World/AGV/Materials/polySurface35_lambert1_0_Bake1_baked/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'

---

### /World/AGV/Materials/polySurface41_lambert1_0_Bake1_baked

* **Prim路径 (Prim Path):**/World/AGV/Materials/polySurface41_lambert1_0_Bake1_baked
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/AGV/Materials/polySurface41_lambert1_0_Bake1_baked/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/AGV/Materials/polySurface41_lambert1_0_Bake1_baked/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f]
        * Connected: '/World/AGV/Materials/polySurface41_lambert1_0_Bake1_baked/tex_base.outputs:rgb' @ '/World/AGV/Materials/polySurface41_lambert1_0_Bake1_baked/tex_base'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/polySurface41_lambert1_0_Bake1_baked_baseColor.jpg'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float]
        * Connected: '/World/AGV/Materials/polySurface41_lambert1_0_Bake1_baked/tex_metallic.outputs:r' @ '/World/AGV/Materials/polySurface41_lambert1_0_Bake1_baked/tex_metallic'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/polySurface41_lambert1_0_Bake1_baked_metallicRoughness_metal.jpg'
      * 'normal' [normal3f]
        * Connected: '/World/AGV/Materials/polySurface41_lambert1_0_Bake1_baked/tex_normal.outputs:rgb' @ '/World/AGV/Materials/polySurface41_lambert1_0_Bake1_baked/tex_normal'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/polySurface41_lambert1_0_Bake1_baked_normal.jpg'
      * 'occlusion' [float] = '1'
      * 'roughness' [float]
        * Connected: '/World/AGV/Materials/polySurface41_lambert1_0_Bake1_baked/tex_roughness.outputs:r' @ '/World/AGV/Materials/polySurface41_lambert1_0_Bake1_baked/tex_roughness'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/polySurface41_lambert1_0_Bake1_baked_metallicRoughness_rough.jpg'
    * '/World/AGV/Materials/polySurface41_lambert1_0_Bake1_baked/tex_base' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/polySurface41_lambert1_0_Bake1_baked_baseColor.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'file' [asset] = '0/polySurface41_lambert1_0_Bake1_baked_baseColor.jpg'
      * 'st' [float2]
        * Connected: '/World/AGV/Materials/polySurface41_lambert1_0_Bake1_baked/uvset0.outputs:result' @ '/World/AGV/Materials/polySurface41_lambert1_0_Bake1_baked/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/AGV/Materials/polySurface41_lambert1_0_Bake1_baked/uvset0' (ID: 'UsdPrimvarReader_float2')
    * Implementation: 'id'
    * '/World/AGV/Materials/polySurface41_lambert1_0_Bake1_baked/tex_metallic' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/polySurface41_lambert1_0_Bake1_baked_metallicRoughness_metal.jpg'
    * Inputs:
      * 'fallback' [float4] = '(0.000, 0.000, 0.000, 1.000)'
      * 'file' [asset] = '0/polySurface41_lambert1_0_Bake1_baked_metallicRoughness_metal.jpg'
      * 'st' [float2]
        * Connected: '/World/AGV/Materials/polySurface41_lambert1_0_Bake1_baked/uvset0.outputs:result' @ '/World/AGV/Materials/polySurface41_lambert1_0_Bake1_baked/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/AGV/Materials/polySurface41_lambert1_0_Bake1_baked/tex_normal' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/polySurface41_lambert1_0_Bake1_baked_normal.jpg'
    * Inputs:
      * 'bias' [float4] = '(-1.000, -1.000, -1.000, -1.000)'
      * 'fallback' [float4] = '(0.000, 0.000, 1.000, 1.000)'
      * 'file' [asset] = '0/polySurface41_lambert1_0_Bake1_baked_normal.jpg'
      * 'scale' [float4] = '(2.000, 2.000, 2.000, 2.000)'
      * 'st' [float2]
        * Connected: '/World/AGV/Materials/polySurface41_lambert1_0_Bake1_baked/uvset0.outputs:result' @ '/World/AGV/Materials/polySurface41_lambert1_0_Bake1_baked/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/AGV/Materials/polySurface41_lambert1_0_Bake1_baked/tex_roughness' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/polySurface41_lambert1_0_Bake1_baked_metallicRoughness_rough.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 0.000, 0.000, 1.000)'
      * 'file' [asset] = '0/polySurface41_lambert1_0_Bake1_baked_metallicRoughness_rough.jpg'
      * 'st' [float2]
        * Connected: '/World/AGV/Materials/polySurface41_lambert1_0_Bake1_baked/uvset0.outputs:result' @ '/World/AGV/Materials/polySurface41_lambert1_0_Bake1_baked/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'

---

### /World/AGV/Materials/polySurface35_lambert1_0_001_Bake1_baked

* **Prim路径 (Prim Path):**/World/AGV/Materials/polySurface35_lambert1_0_001_Bake1_baked
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/AGV/Materials/polySurface35_lambert1_0_001_Bake1_baked/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/AGV/Materials/polySurface35_lambert1_0_001_Bake1_baked/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f]
        * Connected: '/World/AGV/Materials/polySurface35_lambert1_0_001_Bake1_baked/tex_base.outputs:rgb' @ '/World/AGV/Materials/polySurface35_lambert1_0_001_Bake1_baked/tex_base'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/polySurface35_lambert1_0.001_Bake1_baked_baseColor.jpg'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float]
        * Connected: '/World/AGV/Materials/polySurface35_lambert1_0_001_Bake1_baked/tex_metallic.outputs:r' @ '/World/AGV/Materials/polySurface35_lambert1_0_001_Bake1_baked/tex_metallic'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/polySurface35_lambert1_0.001_Bake1_baked_metallicRoughness_metal.jpg'
      * 'normal' [normal3f]
        * Connected: '/World/AGV/Materials/polySurface35_lambert1_0_001_Bake1_baked/tex_normal.outputs:rgb' @ '/World/AGV/Materials/polySurface35_lambert1_0_001_Bake1_baked/tex_normal'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/polySurface35_lambert1_0.001_Bake1_baked_normal.jpg'
      * 'occlusion' [float] = '1'
      * 'roughness' [float]
        * Connected: '/World/AGV/Materials/polySurface35_lambert1_0_001_Bake1_baked/tex_roughness.outputs:r' @ '/World/AGV/Materials/polySurface35_lambert1_0_001_Bake1_baked/tex_roughness'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/polySurface35_lambert1_0.001_Bake1_baked_metallicRoughness_rough.jpg'
    * '/World/AGV/Materials/polySurface35_lambert1_0_001_Bake1_baked/tex_base' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/polySurface35_lambert1_0.001_Bake1_baked_baseColor.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'file' [asset] = '0/polySurface35_lambert1_0.001_Bake1_baked_baseColor.jpg'
      * 'st' [float2]
        * Connected: '/World/AGV/Materials/polySurface35_lambert1_0_001_Bake1_baked/uvset0.outputs:result' @ '/World/AGV/Materials/polySurface35_lambert1_0_001_Bake1_baked/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/AGV/Materials/polySurface35_lambert1_0_001_Bake1_baked/uvset0' (ID: 'UsdPrimvarReader_float2')
    * Implementation: 'id'
    * '/World/AGV/Materials/polySurface35_lambert1_0_001_Bake1_baked/tex_metallic' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/polySurface35_lambert1_0.001_Bake1_baked_metallicRoughness_metal.jpg'
    * Inputs:
      * 'fallback' [float4] = '(0.000, 0.000, 0.000, 1.000)'
      * 'file' [asset] = '0/polySurface35_lambert1_0.001_Bake1_baked_metallicRoughness_metal.jpg'
      * 'st' [float2]
        * Connected: '/World/AGV/Materials/polySurface35_lambert1_0_001_Bake1_baked/uvset0.outputs:result' @ '/World/AGV/Materials/polySurface35_lambert1_0_001_Bake1_baked/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/AGV/Materials/polySurface35_lambert1_0_001_Bake1_baked/tex_normal' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/polySurface35_lambert1_0.001_Bake1_baked_normal.jpg'
    * Inputs:
      * 'bias' [float4] = '(-1.000, -1.000, -1.000, -1.000)'
      * 'fallback' [float4] = '(0.000, 0.000, 1.000, 1.000)'
      * 'file' [asset] = '0/polySurface35_lambert1_0.001_Bake1_baked_normal.jpg'
      * 'scale' [float4] = '(2.000, 2.000, 2.000, 2.000)'
      * 'st' [float2]
        * Connected: '/World/AGV/Materials/polySurface35_lambert1_0_001_Bake1_baked/uvset0.outputs:result' @ '/World/AGV/Materials/polySurface35_lambert1_0_001_Bake1_baked/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/AGV/Materials/polySurface35_lambert1_0_001_Bake1_baked/tex_roughness' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/polySurface35_lambert1_0.001_Bake1_baked_metallicRoughness_rough.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 0.000, 0.000, 1.000)'
      * 'file' [asset] = '0/polySurface35_lambert1_0.001_Bake1_baked_metallicRoughness_rough.jpg'
      * 'st' [float2]
        * Connected: '/World/AGV/Materials/polySurface35_lambert1_0_001_Bake1_baked/uvset0.outputs:result' @ '/World/AGV/Materials/polySurface35_lambert1_0_001_Bake1_baked/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'

---

### /World/AGV/Materials/Slice_002_Bake1_baked

* **Prim路径 (Prim Path):**/World/AGV/Materials/Slice_002_Bake1_baked
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/AGV/Materials/Slice_002_Bake1_baked/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/AGV/Materials/Slice_002_Bake1_baked/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f]
        * Connected: '/World/AGV/Materials/Slice_002_Bake1_baked/tex_base.outputs:rgb' @ '/World/AGV/Materials/Slice_002_Bake1_baked/tex_base'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/Slice.002_Bake1_baked_baseColor.jpg'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float]
        * Connected: '/World/AGV/Materials/Slice_002_Bake1_baked/tex_metallic.outputs:r' @ '/World/AGV/Materials/Slice_002_Bake1_baked/tex_metallic'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/Slice.002_Bake1_baked_metallicRoughness_metal.jpg'
      * 'normal' [normal3f]
        * Connected: '/World/AGV/Materials/Slice_002_Bake1_baked/tex_normal.outputs:rgb' @ '/World/AGV/Materials/Slice_002_Bake1_baked/tex_normal'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/Slice.002_Bake1_baked_normal.jpg'
      * 'occlusion' [float] = '1'
      * 'roughness' [float]
        * Connected: '/World/AGV/Materials/Slice_002_Bake1_baked/tex_roughness.outputs:r' @ '/World/AGV/Materials/Slice_002_Bake1_baked/tex_roughness'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/Slice.002_Bake1_baked_metallicRoughness_rough.jpg'
    * '/World/AGV/Materials/Slice_002_Bake1_baked/tex_base' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/Slice.002_Bake1_baked_baseColor.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'file' [asset] = '0/Slice.002_Bake1_baked_baseColor.jpg'
      * 'st' [float2]
        * Connected: '/World/AGV/Materials/Slice_002_Bake1_baked/uvset0.outputs:result' @ '/World/AGV/Materials/Slice_002_Bake1_baked/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/AGV/Materials/Slice_002_Bake1_baked/uvset0' (ID: 'UsdPrimvarReader_float2')
    * Implementation: 'id'
    * '/World/AGV/Materials/Slice_002_Bake1_baked/tex_metallic' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/Slice.002_Bake1_baked_metallicRoughness_metal.jpg'
    * Inputs:
      * 'fallback' [float4] = '(0.000, 0.000, 0.000, 1.000)'
      * 'file' [asset] = '0/Slice.002_Bake1_baked_metallicRoughness_metal.jpg'
      * 'st' [float2]
        * Connected: '/World/AGV/Materials/Slice_002_Bake1_baked/uvset0.outputs:result' @ '/World/AGV/Materials/Slice_002_Bake1_baked/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/AGV/Materials/Slice_002_Bake1_baked/tex_normal' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/Slice.002_Bake1_baked_normal.jpg'
    * Inputs:
      * 'bias' [float4] = '(-1.000, -1.000, -1.000, -1.000)'
      * 'fallback' [float4] = '(0.000, 0.000, 1.000, 1.000)'
      * 'file' [asset] = '0/Slice.002_Bake1_baked_normal.jpg'
      * 'scale' [float4] = '(2.000, 2.000, 2.000, 2.000)'
      * 'st' [float2]
        * Connected: '/World/AGV/Materials/Slice_002_Bake1_baked/uvset0.outputs:result' @ '/World/AGV/Materials/Slice_002_Bake1_baked/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/AGV/Materials/Slice_002_Bake1_baked/tex_roughness' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/Slice.002_Bake1_baked_metallicRoughness_rough.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 0.000, 0.000, 1.000)'
      * 'file' [asset] = '0/Slice.002_Bake1_baked_metallicRoughness_rough.jpg'
      * 'st' [float2]
        * Connected: '/World/AGV/Materials/Slice_002_Bake1_baked/uvset0.outputs:result' @ '/World/AGV/Materials/Slice_002_Bake1_baked/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'

---

### /World/AGV/Materials/Slice_003_Bake1_baked

* **Prim路径 (Prim Path):**/World/AGV/Materials/Slice_003_Bake1_baked
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/AGV/Materials/Slice_003_Bake1_baked/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/AGV/Materials/Slice_003_Bake1_baked/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f]
        * Connected: '/World/AGV/Materials/Slice_003_Bake1_baked/tex_base.outputs:rgb' @ '/World/AGV/Materials/Slice_003_Bake1_baked/tex_base'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/Slice.003_Bake1_baked_baseColor.jpg'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float]
        * Connected: '/World/AGV/Materials/Slice_003_Bake1_baked/tex_metallic.outputs:r' @ '/World/AGV/Materials/Slice_003_Bake1_baked/tex_metallic'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/Slice.003_Bake1_baked_metallicRoughness_metal.jpg'
      * 'normal' [normal3f]
        * Connected: '/World/AGV/Materials/Slice_003_Bake1_baked/tex_normal.outputs:rgb' @ '/World/AGV/Materials/Slice_003_Bake1_baked/tex_normal'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/Slice.003_Bake1_baked_normal.jpg'
      * 'occlusion' [float] = '1'
      * 'roughness' [float]
        * Connected: '/World/AGV/Materials/Slice_003_Bake1_baked/tex_roughness.outputs:r' @ '/World/AGV/Materials/Slice_003_Bake1_baked/tex_roughness'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/Slice.003_Bake1_baked_metallicRoughness_rough.jpg'
    * '/World/AGV/Materials/Slice_003_Bake1_baked/tex_base' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/Slice.003_Bake1_baked_baseColor.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'file' [asset] = '0/Slice.003_Bake1_baked_baseColor.jpg'
      * 'st' [float2]
        * Connected: '/World/AGV/Materials/Slice_003_Bake1_baked/uvset0.outputs:result' @ '/World/AGV/Materials/Slice_003_Bake1_baked/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/AGV/Materials/Slice_003_Bake1_baked/uvset0' (ID: 'UsdPrimvarReader_float2')
    * Implementation: 'id'
    * '/World/AGV/Materials/Slice_003_Bake1_baked/tex_metallic' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/Slice.003_Bake1_baked_metallicRoughness_metal.jpg'
    * Inputs:
      * 'fallback' [float4] = '(0.000, 0.000, 0.000, 1.000)'
      * 'file' [asset] = '0/Slice.003_Bake1_baked_metallicRoughness_metal.jpg'
      * 'st' [float2]
        * Connected: '/World/AGV/Materials/Slice_003_Bake1_baked/uvset0.outputs:result' @ '/World/AGV/Materials/Slice_003_Bake1_baked/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/AGV/Materials/Slice_003_Bake1_baked/tex_normal' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/Slice.003_Bake1_baked_normal.jpg'
    * Inputs:
      * 'bias' [float4] = '(-1.000, -1.000, -1.000, -1.000)'
      * 'fallback' [float4] = '(0.000, 0.000, 1.000, 1.000)'
      * 'file' [asset] = '0/Slice.003_Bake1_baked_normal.jpg'
      * 'scale' [float4] = '(2.000, 2.000, 2.000, 2.000)'
      * 'st' [float2]
        * Connected: '/World/AGV/Materials/Slice_003_Bake1_baked/uvset0.outputs:result' @ '/World/AGV/Materials/Slice_003_Bake1_baked/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/AGV/Materials/Slice_003_Bake1_baked/tex_roughness' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/Slice.003_Bake1_baked_metallicRoughness_rough.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 0.000, 0.000, 1.000)'
      * 'file' [asset] = '0/Slice.003_Bake1_baked_metallicRoughness_rough.jpg'
      * 'st' [float2]
        * Connected: '/World/AGV/Materials/Slice_003_Bake1_baked/uvset0.outputs:result' @ '/World/AGV/Materials/Slice_003_Bake1_baked/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'

---

### /World/AGV/Materials/Body_001_Bake1_baked

* **Prim路径 (Prim Path):**/World/AGV/Materials/Body_001_Bake1_baked
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/AGV/Materials/Body_001_Bake1_baked/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/AGV/Materials/Body_001_Bake1_baked/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f]
        * Connected: '/World/AGV/Materials/Body_001_Bake1_baked/tex_base.outputs:rgb' @ '/World/AGV/Materials/Body_001_Bake1_baked/tex_base'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/Body.001_Bake1_baked_baseColor.jpg'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float]
        * Connected: '/World/AGV/Materials/Body_001_Bake1_baked/tex_metallic.outputs:r' @ '/World/AGV/Materials/Body_001_Bake1_baked/tex_metallic'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/Body.001_Bake1_baked_metallicRoughness_metal.jpg'
      * 'normal' [normal3f]
        * Connected: '/World/AGV/Materials/Body_001_Bake1_baked/tex_normal.outputs:rgb' @ '/World/AGV/Materials/Body_001_Bake1_baked/tex_normal'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/Body.001_Bake1_baked_normal.jpg'
      * 'occlusion' [float] = '1'
      * 'roughness' [float]
        * Connected: '/World/AGV/Materials/Body_001_Bake1_baked/tex_roughness.outputs:r' @ '/World/AGV/Materials/Body_001_Bake1_baked/tex_roughness'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/Body.001_Bake1_baked_metallicRoughness_rough.jpg'
    * '/World/AGV/Materials/Body_001_Bake1_baked/tex_base' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/Body.001_Bake1_baked_baseColor.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'file' [asset] = '0/Body.001_Bake1_baked_baseColor.jpg'
      * 'st' [float2]
        * Connected: '/World/AGV/Materials/Body_001_Bake1_baked/uvset0.outputs:result' @ '/World/AGV/Materials/Body_001_Bake1_baked/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/AGV/Materials/Body_001_Bake1_baked/uvset0' (ID: 'UsdPrimvarReader_float2')
    * Implementation: 'id'
    * '/World/AGV/Materials/Body_001_Bake1_baked/tex_metallic' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/Body.001_Bake1_baked_metallicRoughness_metal.jpg'
    * Inputs:
      * 'fallback' [float4] = '(0.000, 0.000, 0.000, 1.000)'
      * 'file' [asset] = '0/Body.001_Bake1_baked_metallicRoughness_metal.jpg'
      * 'st' [float2]
        * Connected: '/World/AGV/Materials/Body_001_Bake1_baked/uvset0.outputs:result' @ '/World/AGV/Materials/Body_001_Bake1_baked/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/AGV/Materials/Body_001_Bake1_baked/tex_normal' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/Body.001_Bake1_baked_normal.jpg'
    * Inputs:
      * 'bias' [float4] = '(-1.000, -1.000, -1.000, -1.000)'
      * 'fallback' [float4] = '(0.000, 0.000, 1.000, 1.000)'
      * 'file' [asset] = '0/Body.001_Bake1_baked_normal.jpg'
      * 'scale' [float4] = '(2.000, 2.000, 2.000, 2.000)'
      * 'st' [float2]
        * Connected: '/World/AGV/Materials/Body_001_Bake1_baked/uvset0.outputs:result' @ '/World/AGV/Materials/Body_001_Bake1_baked/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/AGV/Materials/Body_001_Bake1_baked/tex_roughness' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/Body.001_Bake1_baked_metallicRoughness_rough.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 0.000, 0.000, 1.000)'
      * 'file' [asset] = '0/Body.001_Bake1_baked_metallicRoughness_rough.jpg'
      * 'st' [float2]
        * Connected: '/World/AGV/Materials/Body_001_Bake1_baked/uvset0.outputs:result' @ '/World/AGV/Materials/Body_001_Bake1_baked/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'

---

### /World/AGV/Materials/Body_003_Bake1_baked

* **Prim路径 (Prim Path):**/World/AGV/Materials/Body_003_Bake1_baked
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/AGV/Materials/Body_003_Bake1_baked/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/AGV/Materials/Body_003_Bake1_baked/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f]
        * Connected: '/World/AGV/Materials/Body_003_Bake1_baked/tex_base.outputs:rgb' @ '/World/AGV/Materials/Body_003_Bake1_baked/tex_base'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/Body.003_Bake1_baked_baseColor.jpg'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float]
        * Connected: '/World/AGV/Materials/Body_003_Bake1_baked/tex_metallic.outputs:r' @ '/World/AGV/Materials/Body_003_Bake1_baked/tex_metallic'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/Body.003_Bake1_baked_metallicRoughness_metal.jpg'
      * 'normal' [normal3f]
        * Connected: '/World/AGV/Materials/Body_003_Bake1_baked/tex_normal.outputs:rgb' @ '/World/AGV/Materials/Body_003_Bake1_baked/tex_normal'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/Body.003_Bake1_baked_normal.jpg'
      * 'occlusion' [float] = '1'
      * 'roughness' [float]
        * Connected: '/World/AGV/Materials/Body_003_Bake1_baked/tex_roughness.outputs:r' @ '/World/AGV/Materials/Body_003_Bake1_baked/tex_roughness'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/Body.003_Bake1_baked_metallicRoughness_rough.jpg'
    * '/World/AGV/Materials/Body_003_Bake1_baked/tex_base' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/Body.003_Bake1_baked_baseColor.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'file' [asset] = '0/Body.003_Bake1_baked_baseColor.jpg'
      * 'st' [float2]
        * Connected: '/World/AGV/Materials/Body_003_Bake1_baked/uvset0.outputs:result' @ '/World/AGV/Materials/Body_003_Bake1_baked/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/AGV/Materials/Body_003_Bake1_baked/uvset0' (ID: 'UsdPrimvarReader_float2')
    * Implementation: 'id'
    * '/World/AGV/Materials/Body_003_Bake1_baked/tex_metallic' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/Body.003_Bake1_baked_metallicRoughness_metal.jpg'
    * Inputs:
      * 'fallback' [float4] = '(0.000, 0.000, 0.000, 1.000)'
      * 'file' [asset] = '0/Body.003_Bake1_baked_metallicRoughness_metal.jpg'
      * 'st' [float2]
        * Connected: '/World/AGV/Materials/Body_003_Bake1_baked/uvset0.outputs:result' @ '/World/AGV/Materials/Body_003_Bake1_baked/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/AGV/Materials/Body_003_Bake1_baked/tex_normal' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/Body.003_Bake1_baked_normal.jpg'
    * Inputs:
      * 'bias' [float4] = '(-1.000, -1.000, -1.000, -1.000)'
      * 'fallback' [float4] = '(0.000, 0.000, 1.000, 1.000)'
      * 'file' [asset] = '0/Body.003_Bake1_baked_normal.jpg'
      * 'scale' [float4] = '(2.000, 2.000, 2.000, 2.000)'
      * 'st' [float2]
        * Connected: '/World/AGV/Materials/Body_003_Bake1_baked/uvset0.outputs:result' @ '/World/AGV/Materials/Body_003_Bake1_baked/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/AGV/Materials/Body_003_Bake1_baked/tex_roughness' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/Body.003_Bake1_baked_metallicRoughness_rough.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 0.000, 0.000, 1.000)'
      * 'file' [asset] = '0/Body.003_Bake1_baked_metallicRoughness_rough.jpg'
      * 'st' [float2]
        * Connected: '/World/AGV/Materials/Body_003_Bake1_baked/uvset0.outputs:result' @ '/World/AGV/Materials/Body_003_Bake1_baked/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'

---

### /World/AGV/Materials/Body_004_Bake1_baked

* **Prim路径 (Prim Path):**/World/AGV/Materials/Body_004_Bake1_baked
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/AGV/Materials/Body_004_Bake1_baked/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/AGV/Materials/Body_004_Bake1_baked/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f]
        * Connected: '/World/AGV/Materials/Body_004_Bake1_baked/tex_base.outputs:rgb' @ '/World/AGV/Materials/Body_004_Bake1_baked/tex_base'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/Body.004_Bake1_baked_baseColor.jpg'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float]
        * Connected: '/World/AGV/Materials/Body_004_Bake1_baked/tex_metallic.outputs:r' @ '/World/AGV/Materials/Body_004_Bake1_baked/tex_metallic'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/Body.004_Bake1_baked_metallicRoughness_metal.jpg'
      * 'normal' [normal3f]
        * Connected: '/World/AGV/Materials/Body_004_Bake1_baked/tex_normal.outputs:rgb' @ '/World/AGV/Materials/Body_004_Bake1_baked/tex_normal'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/Body.004_Bake1_baked_normal.jpg'
      * 'occlusion' [float] = '1'
      * 'roughness' [float]
        * Connected: '/World/AGV/Materials/Body_004_Bake1_baked/tex_roughness.outputs:r' @ '/World/AGV/Materials/Body_004_Bake1_baked/tex_roughness'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/Body.004_Bake1_baked_metallicRoughness_rough.jpg'
    * '/World/AGV/Materials/Body_004_Bake1_baked/tex_base' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/Body.004_Bake1_baked_baseColor.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'file' [asset] = '0/Body.004_Bake1_baked_baseColor.jpg'
      * 'st' [float2]
        * Connected: '/World/AGV/Materials/Body_004_Bake1_baked/uvset0.outputs:result' @ '/World/AGV/Materials/Body_004_Bake1_baked/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/AGV/Materials/Body_004_Bake1_baked/uvset0' (ID: 'UsdPrimvarReader_float2')
    * Implementation: 'id'
    * '/World/AGV/Materials/Body_004_Bake1_baked/tex_metallic' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/Body.004_Bake1_baked_metallicRoughness_metal.jpg'
    * Inputs:
      * 'fallback' [float4] = '(0.000, 0.000, 0.000, 1.000)'
      * 'file' [asset] = '0/Body.004_Bake1_baked_metallicRoughness_metal.jpg'
      * 'st' [float2]
        * Connected: '/World/AGV/Materials/Body_004_Bake1_baked/uvset0.outputs:result' @ '/World/AGV/Materials/Body_004_Bake1_baked/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/AGV/Materials/Body_004_Bake1_baked/tex_normal' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/Body.004_Bake1_baked_normal.jpg'
    * Inputs:
      * 'bias' [float4] = '(-1.000, -1.000, -1.000, -1.000)'
      * 'fallback' [float4] = '(0.000, 0.000, 1.000, 1.000)'
      * 'file' [asset] = '0/Body.004_Bake1_baked_normal.jpg'
      * 'scale' [float4] = '(2.000, 2.000, 2.000, 2.000)'
      * 'st' [float2]
        * Connected: '/World/AGV/Materials/Body_004_Bake1_baked/uvset0.outputs:result' @ '/World/AGV/Materials/Body_004_Bake1_baked/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/AGV/Materials/Body_004_Bake1_baked/tex_roughness' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/Body.004_Bake1_baked_metallicRoughness_rough.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 0.000, 0.000, 1.000)'
      * 'file' [asset] = '0/Body.004_Bake1_baked_metallicRoughness_rough.jpg'
      * 'st' [float2]
        * Connected: '/World/AGV/Materials/Body_004_Bake1_baked/uvset0.outputs:result' @ '/World/AGV/Materials/Body_004_Bake1_baked/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'

---

### /World/AGV/Materials/Plane_Bake1_baked

* **Prim路径 (Prim Path):**/World/AGV/Materials/Plane_Bake1_baked
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/AGV/Materials/Plane_Bake1_baked/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/AGV/Materials/Plane_Bake1_baked/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f]
        * Connected: '/World/AGV/Materials/Plane_Bake1_baked/tex_base.outputs:rgb' @ '/World/AGV/Materials/Plane_Bake1_baked/tex_base'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/Plane_Bake1_baked_baseColor.jpg'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float]
        * Connected: '/World/AGV/Materials/Plane_Bake1_baked/tex_metallic.outputs:r' @ '/World/AGV/Materials/Plane_Bake1_baked/tex_metallic'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/Plane_Bake1_baked_metallicRoughness_metal.jpg'
      * 'normal' [normal3f]
        * Connected: '/World/AGV/Materials/Plane_Bake1_baked/tex_normal.outputs:rgb' @ '/World/AGV/Materials/Plane_Bake1_baked/tex_normal'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/Plane_Bake1_baked_normal.jpg'
      * 'occlusion' [float] = '1'
      * 'roughness' [float]
        * Connected: '/World/AGV/Materials/Plane_Bake1_baked/tex_roughness.outputs:r' @ '/World/AGV/Materials/Plane_Bake1_baked/tex_roughness'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/Plane_Bake1_baked_metallicRoughness_rough.jpg'
    * '/World/AGV/Materials/Plane_Bake1_baked/tex_base' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/Plane_Bake1_baked_baseColor.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'file' [asset] = '0/Plane_Bake1_baked_baseColor.jpg'
      * 'st' [float2]
        * Connected: '/World/AGV/Materials/Plane_Bake1_baked/uvset0.outputs:result' @ '/World/AGV/Materials/Plane_Bake1_baked/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/AGV/Materials/Plane_Bake1_baked/uvset0' (ID: 'UsdPrimvarReader_float2')
    * Implementation: 'id'
    * '/World/AGV/Materials/Plane_Bake1_baked/tex_metallic' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/Plane_Bake1_baked_metallicRoughness_metal.jpg'
    * Inputs:
      * 'fallback' [float4] = '(0.000, 0.000, 0.000, 1.000)'
      * 'file' [asset] = '0/Plane_Bake1_baked_metallicRoughness_metal.jpg'
      * 'st' [float2]
        * Connected: '/World/AGV/Materials/Plane_Bake1_baked/uvset0.outputs:result' @ '/World/AGV/Materials/Plane_Bake1_baked/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/AGV/Materials/Plane_Bake1_baked/tex_normal' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/Plane_Bake1_baked_normal.jpg'
    * Inputs:
      * 'bias' [float4] = '(-1.000, -1.000, -1.000, -1.000)'
      * 'fallback' [float4] = '(0.000, 0.000, 1.000, 1.000)'
      * 'file' [asset] = '0/Plane_Bake1_baked_normal.jpg'
      * 'scale' [float4] = '(2.000, 2.000, 2.000, 2.000)'
      * 'st' [float2]
        * Connected: '/World/AGV/Materials/Plane_Bake1_baked/uvset0.outputs:result' @ '/World/AGV/Materials/Plane_Bake1_baked/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/AGV/Materials/Plane_Bake1_baked/tex_roughness' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/Plane_Bake1_baked_metallicRoughness_rough.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 0.000, 0.000, 1.000)'
      * 'file' [asset] = '0/Plane_Bake1_baked_metallicRoughness_rough.jpg'
      * 'st' [float2]
        * Connected: '/World/AGV/Materials/Plane_Bake1_baked/uvset0.outputs:result' @ '/World/AGV/Materials/Plane_Bake1_baked/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'

---

### /World/AGV/Materials/F_Switch_ob_flipswitcha_003_Bake1_baked

* **Prim路径 (Prim Path):**/World/AGV/Materials/F_Switch_ob_flipswitcha_003_Bake1_baked
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/AGV/Materials/F_Switch_ob_flipswitcha_003_Bake1_baked/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/AGV/Materials/F_Switch_ob_flipswitcha_003_Bake1_baked/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f]
        * Connected: '/World/AGV/Materials/F_Switch_ob_flipswitcha_003_Bake1_baked/tex_base.outputs:rgb' @ '/World/AGV/Materials/F_Switch_ob_flipswitcha_003_Bake1_baked/tex_base'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/F_Switch_ob_flipswitcha_003_Bake1_baked_baseColor.jpg'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float]
        * Connected: '/World/AGV/Materials/F_Switch_ob_flipswitcha_003_Bake1_baked/tex_metallic.outputs:r' @ '/World/AGV/Materials/F_Switch_ob_flipswitcha_003_Bake1_baked/tex_metallic'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/F_Switch_ob_flipswitcha_003_Bake1_baked_metallicRoughness_metal.jpg'
      * 'normal' [normal3f]
        * Connected: '/World/AGV/Materials/F_Switch_ob_flipswitcha_003_Bake1_baked/tex_normal.outputs:rgb' @ '/World/AGV/Materials/F_Switch_ob_flipswitcha_003_Bake1_baked/tex_normal'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/F_Switch_ob_flipswitcha_003_Bake1_baked_normal.jpg'
      * 'occlusion' [float] = '1'
      * 'roughness' [float]
        * Connected: '/World/AGV/Materials/F_Switch_ob_flipswitcha_003_Bake1_baked/tex_roughness.outputs:r' @ '/World/AGV/Materials/F_Switch_ob_flipswitcha_003_Bake1_baked/tex_roughness'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/F_Switch_ob_flipswitcha_003_Bake1_baked_metallicRoughness_rough.jpg'
    * '/World/AGV/Materials/F_Switch_ob_flipswitcha_003_Bake1_baked/tex_base' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/F_Switch_ob_flipswitcha_003_Bake1_baked_baseColor.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'file' [asset] = '0/F_Switch_ob_flipswitcha_003_Bake1_baked_baseColor.jpg'
      * 'st' [float2]
        * Connected: '/World/AGV/Materials/F_Switch_ob_flipswitcha_003_Bake1_baked/uvset0.outputs:result' @ '/World/AGV/Materials/F_Switch_ob_flipswitcha_003_Bake1_baked/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/AGV/Materials/F_Switch_ob_flipswitcha_003_Bake1_baked/uvset0' (ID: 'UsdPrimvarReader_float2')
    * Implementation: 'id'
    * '/World/AGV/Materials/F_Switch_ob_flipswitcha_003_Bake1_baked/tex_metallic' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/F_Switch_ob_flipswitcha_003_Bake1_baked_metallicRoughness_metal.jpg'
    * Inputs:
      * 'fallback' [float4] = '(0.000, 0.000, 0.000, 1.000)'
      * 'file' [asset] = '0/F_Switch_ob_flipswitcha_003_Bake1_baked_metallicRoughness_metal.jpg'
      * 'st' [float2]
        * Connected: '/World/AGV/Materials/F_Switch_ob_flipswitcha_003_Bake1_baked/uvset0.outputs:result' @ '/World/AGV/Materials/F_Switch_ob_flipswitcha_003_Bake1_baked/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/AGV/Materials/F_Switch_ob_flipswitcha_003_Bake1_baked/tex_normal' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/F_Switch_ob_flipswitcha_003_Bake1_baked_normal.jpg'
    * Inputs:
      * 'bias' [float4] = '(-1.000, -1.000, -1.000, -1.000)'
      * 'fallback' [float4] = '(0.000, 0.000, 1.000, 1.000)'
      * 'file' [asset] = '0/F_Switch_ob_flipswitcha_003_Bake1_baked_normal.jpg'
      * 'scale' [float4] = '(2.000, 2.000, 2.000, 2.000)'
      * 'st' [float2]
        * Connected: '/World/AGV/Materials/F_Switch_ob_flipswitcha_003_Bake1_baked/uvset0.outputs:result' @ '/World/AGV/Materials/F_Switch_ob_flipswitcha_003_Bake1_baked/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/AGV/Materials/F_Switch_ob_flipswitcha_003_Bake1_baked/tex_roughness' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/F_Switch_ob_flipswitcha_003_Bake1_baked_metallicRoughness_rough.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 0.000, 0.000, 1.000)'
      * 'file' [asset] = '0/F_Switch_ob_flipswitcha_003_Bake1_baked_metallicRoughness_rough.jpg'
      * 'st' [float2]
        * Connected: '/World/AGV/Materials/F_Switch_ob_flipswitcha_003_Bake1_baked/uvset0.outputs:result' @ '/World/AGV/Materials/F_Switch_ob_flipswitcha_003_Bake1_baked/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'

---

### /World/AGV/Materials/F_Switch_ob_flipswitcha_003_001_Bake1_baked

* **Prim路径 (Prim Path):**/World/AGV/Materials/F_Switch_ob_flipswitcha_003_001_Bake1_baked
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/AGV/Materials/F_Switch_ob_flipswitcha_003_001_Bake1_baked/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/AGV/Materials/F_Switch_ob_flipswitcha_003_001_Bake1_baked/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f]
        * Connected: '/World/AGV/Materials/F_Switch_ob_flipswitcha_003_001_Bake1_baked/tex_base.outputs:rgb' @ '/World/AGV/Materials/F_Switch_ob_flipswitcha_003_001_Bake1_baked/tex_base'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/F_Switch_ob_flipswitcha_003.001_Bake1_baked_baseColor.jpg'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float]
        * Connected: '/World/AGV/Materials/F_Switch_ob_flipswitcha_003_001_Bake1_baked/tex_metallic.outputs:r' @ '/World/AGV/Materials/F_Switch_ob_flipswitcha_003_001_Bake1_baked/tex_metallic'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/F_Switch_ob_flipswitcha_003.001_Bake1_baked_metallicRoughness_metal.jpg'
      * 'normal' [normal3f]
        * Connected: '/World/AGV/Materials/F_Switch_ob_flipswitcha_003_001_Bake1_baked/tex_normal.outputs:rgb' @ '/World/AGV/Materials/F_Switch_ob_flipswitcha_003_001_Bake1_baked/tex_normal'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/F_Switch_ob_flipswitcha_003.001_Bake1_baked_normal.jpg'
      * 'occlusion' [float] = '1'
      * 'roughness' [float]
        * Connected: '/World/AGV/Materials/F_Switch_ob_flipswitcha_003_001_Bake1_baked/tex_roughness.outputs:r' @ '/World/AGV/Materials/F_Switch_ob_flipswitcha_003_001_Bake1_baked/tex_roughness'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/F_Switch_ob_flipswitcha_003.001_Bake1_baked_metallicRoughness_rough.jpg'
    * '/World/AGV/Materials/F_Switch_ob_flipswitcha_003_001_Bake1_baked/tex_base' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/F_Switch_ob_flipswitcha_003.001_Bake1_baked_baseColor.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'file' [asset] = '0/F_Switch_ob_flipswitcha_003.001_Bake1_baked_baseColor.jpg'
      * 'st' [float2]
        * Connected: '/World/AGV/Materials/F_Switch_ob_flipswitcha_003_001_Bake1_baked/uvset0.outputs:result' @ '/World/AGV/Materials/F_Switch_ob_flipswitcha_003_001_Bake1_baked/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/AGV/Materials/F_Switch_ob_flipswitcha_003_001_Bake1_baked/uvset0' (ID: 'UsdPrimvarReader_float2')
    * Implementation: 'id'
    * '/World/AGV/Materials/F_Switch_ob_flipswitcha_003_001_Bake1_baked/tex_metallic' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/F_Switch_ob_flipswitcha_003.001_Bake1_baked_metallicRoughness_metal.jpg'
    * Inputs:
      * 'fallback' [float4] = '(0.000, 0.000, 0.000, 1.000)'
      * 'file' [asset] = '0/F_Switch_ob_flipswitcha_003.001_Bake1_baked_metallicRoughness_metal.jpg'
      * 'st' [float2]
        * Connected: '/World/AGV/Materials/F_Switch_ob_flipswitcha_003_001_Bake1_baked/uvset0.outputs:result' @ '/World/AGV/Materials/F_Switch_ob_flipswitcha_003_001_Bake1_baked/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/AGV/Materials/F_Switch_ob_flipswitcha_003_001_Bake1_baked/tex_normal' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/F_Switch_ob_flipswitcha_003.001_Bake1_baked_normal.jpg'
    * Inputs:
      * 'bias' [float4] = '(-1.000, -1.000, -1.000, -1.000)'
      * 'fallback' [float4] = '(0.000, 0.000, 1.000, 1.000)'
      * 'file' [asset] = '0/F_Switch_ob_flipswitcha_003.001_Bake1_baked_normal.jpg'
      * 'scale' [float4] = '(2.000, 2.000, 2.000, 2.000)'
      * 'st' [float2]
        * Connected: '/World/AGV/Materials/F_Switch_ob_flipswitcha_003_001_Bake1_baked/uvset0.outputs:result' @ '/World/AGV/Materials/F_Switch_ob_flipswitcha_003_001_Bake1_baked/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/AGV/Materials/F_Switch_ob_flipswitcha_003_001_Bake1_baked/tex_roughness' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/F_Switch_ob_flipswitcha_003.001_Bake1_baked_metallicRoughness_rough.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 0.000, 0.000, 1.000)'
      * 'file' [asset] = '0/F_Switch_ob_flipswitcha_003.001_Bake1_baked_metallicRoughness_rough.jpg'
      * 'st' [float2]
        * Connected: '/World/AGV/Materials/F_Switch_ob_flipswitcha_003_001_Bake1_baked/uvset0.outputs:result' @ '/World/AGV/Materials/F_Switch_ob_flipswitcha_003_001_Bake1_baked/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'

---

### /World/AGV/Materials/F_Switch_ob_flipswitcha_003_002_Bake1_baked

* **Prim路径 (Prim Path):**/World/AGV/Materials/F_Switch_ob_flipswitcha_003_002_Bake1_baked
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/AGV/Materials/F_Switch_ob_flipswitcha_003_002_Bake1_baked/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/AGV/Materials/F_Switch_ob_flipswitcha_003_002_Bake1_baked/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f]
        * Connected: '/World/AGV/Materials/F_Switch_ob_flipswitcha_003_002_Bake1_baked/tex_base.outputs:rgb' @ '/World/AGV/Materials/F_Switch_ob_flipswitcha_003_002_Bake1_baked/tex_base'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/F_Switch_ob_flipswitcha_003.002_Bake1_baked_baseColor.jpg'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float]
        * Connected: '/World/AGV/Materials/F_Switch_ob_flipswitcha_003_002_Bake1_baked/tex_metallic.outputs:r' @ '/World/AGV/Materials/F_Switch_ob_flipswitcha_003_002_Bake1_baked/tex_metallic'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/F_Switch_ob_flipswitcha_003.002_Bake1_baked_metallicRoughness_metal.jpg'
      * 'normal' [normal3f]
        * Connected: '/World/AGV/Materials/F_Switch_ob_flipswitcha_003_002_Bake1_baked/tex_normal.outputs:rgb' @ '/World/AGV/Materials/F_Switch_ob_flipswitcha_003_002_Bake1_baked/tex_normal'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/F_Switch_ob_flipswitcha_003.002_Bake1_baked_normal.jpg'
      * 'occlusion' [float] = '1'
      * 'roughness' [float]
        * Connected: '/World/AGV/Materials/F_Switch_ob_flipswitcha_003_002_Bake1_baked/tex_roughness.outputs:r' @ '/World/AGV/Materials/F_Switch_ob_flipswitcha_003_002_Bake1_baked/tex_roughness'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/F_Switch_ob_flipswitcha_003.002_Bake1_baked_metallicRoughness_rough.jpg'
    * '/World/AGV/Materials/F_Switch_ob_flipswitcha_003_002_Bake1_baked/tex_base' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/F_Switch_ob_flipswitcha_003.002_Bake1_baked_baseColor.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'file' [asset] = '0/F_Switch_ob_flipswitcha_003.002_Bake1_baked_baseColor.jpg'
      * 'st' [float2]
        * Connected: '/World/AGV/Materials/F_Switch_ob_flipswitcha_003_002_Bake1_baked/uvset0.outputs:result' @ '/World/AGV/Materials/F_Switch_ob_flipswitcha_003_002_Bake1_baked/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/AGV/Materials/F_Switch_ob_flipswitcha_003_002_Bake1_baked/uvset0' (ID: 'UsdPrimvarReader_float2')
    * Implementation: 'id'
    * '/World/AGV/Materials/F_Switch_ob_flipswitcha_003_002_Bake1_baked/tex_metallic' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/F_Switch_ob_flipswitcha_003.002_Bake1_baked_metallicRoughness_metal.jpg'
    * Inputs:
      * 'fallback' [float4] = '(0.000, 0.000, 0.000, 1.000)'
      * 'file' [asset] = '0/F_Switch_ob_flipswitcha_003.002_Bake1_baked_metallicRoughness_metal.jpg'
      * 'st' [float2]
        * Connected: '/World/AGV/Materials/F_Switch_ob_flipswitcha_003_002_Bake1_baked/uvset0.outputs:result' @ '/World/AGV/Materials/F_Switch_ob_flipswitcha_003_002_Bake1_baked/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/AGV/Materials/F_Switch_ob_flipswitcha_003_002_Bake1_baked/tex_normal' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/F_Switch_ob_flipswitcha_003.002_Bake1_baked_normal.jpg'
    * Inputs:
      * 'bias' [float4] = '(-1.000, -1.000, -1.000, -1.000)'
      * 'fallback' [float4] = '(0.000, 0.000, 1.000, 1.000)'
      * 'file' [asset] = '0/F_Switch_ob_flipswitcha_003.002_Bake1_baked_normal.jpg'
      * 'scale' [float4] = '(2.000, 2.000, 2.000, 2.000)'
      * 'st' [float2]
        * Connected: '/World/AGV/Materials/F_Switch_ob_flipswitcha_003_002_Bake1_baked/uvset0.outputs:result' @ '/World/AGV/Materials/F_Switch_ob_flipswitcha_003_002_Bake1_baked/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/AGV/Materials/F_Switch_ob_flipswitcha_003_002_Bake1_baked/tex_roughness' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/F_Switch_ob_flipswitcha_003.002_Bake1_baked_metallicRoughness_rough.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 0.000, 0.000, 1.000)'
      * 'file' [asset] = '0/F_Switch_ob_flipswitcha_003.002_Bake1_baked_metallicRoughness_rough.jpg'
      * 'st' [float2]
        * Connected: '/World/AGV/Materials/F_Switch_ob_flipswitcha_003_002_Bake1_baked/uvset0.outputs:result' @ '/World/AGV/Materials/F_Switch_ob_flipswitcha_003_002_Bake1_baked/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'

---

### /World/UR__Cobot_Mir_AMR/Materials/Allu_Mat_001

* **Prim路径 (Prim Path):**/World/UR__Cobot_Mir_AMR/Materials/Allu_Mat_001
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/UR__Cobot_Mir_AMR/Materials/Allu_Mat_001/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/UR__Cobot_Mir_AMR/Materials/Allu_Mat_001/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.815, 0.831, 0.839)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '1'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0.3'

---

### /World/UR__Cobot_Mir_AMR/Materials/Stahl_003

* **Prim路径 (Prim Path):**/World/UR__Cobot_Mir_AMR/Materials/Stahl_003
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/UR__Cobot_Mir_AMR/Materials/Stahl_003/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/UR__Cobot_Mir_AMR/Materials/Stahl_003/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f]
        * Connected: '/World/UR__Cobot_Mir_AMR/Materials/Stahl_003/tex_base.outputs:rgb' @ '/World/UR__Cobot_Mir_AMR/Materials/Stahl_003/tex_base'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/Stahl.003_baseColor.jpg'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float]
        * Connected: '/World/UR__Cobot_Mir_AMR/Materials/Stahl_003/tex_metallic.outputs:r' @ '/World/UR__Cobot_Mir_AMR/Materials/Stahl_003/tex_metallic'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/Stahl.003_metallicRoughness_metal.jpg'
      * 'normal' [normal3f]
        * Connected: '/World/UR__Cobot_Mir_AMR/Materials/Stahl_003/tex_normal.outputs:rgb' @ '/World/UR__Cobot_Mir_AMR/Materials/Stahl_003/tex_normal'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/Stahl.003_normal_scale0_norm.jpg'
      * 'occlusion' [float] = '1'
      * 'roughness' [float]
        * Connected: '/World/UR__Cobot_Mir_AMR/Materials/Stahl_003/tex_roughness.outputs:r' @ '/World/UR__Cobot_Mir_AMR/Materials/Stahl_003/tex_roughness'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/Stahl.003_metallicRoughness_rough.jpg'
    * '/World/UR__Cobot_Mir_AMR/Materials/Stahl_003/tex_base' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/Stahl.003_baseColor.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'file' [asset] = '0/Stahl.003_baseColor.jpg'
      * 'st' [float2]
        * Connected: '/World/UR__Cobot_Mir_AMR/Materials/Stahl_003/uvset0.outputs:result' @ '/World/UR__Cobot_Mir_AMR/Materials/Stahl_003/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/UR__Cobot_Mir_AMR/Materials/Stahl_003/uvset0' (ID: 'UsdPrimvarReader_float2')
    * Implementation: 'id'
    * '/World/UR__Cobot_Mir_AMR/Materials/Stahl_003/tex_metallic' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/Stahl.003_metallicRoughness_metal.jpg'
    * Inputs:
      * 'fallback' [float4] = '(0.000, 0.000, 0.000, 1.000)'
      * 'file' [asset] = '0/Stahl.003_metallicRoughness_metal.jpg'
      * 'st' [float2]
        * Connected: '/World/UR__Cobot_Mir_AMR/Materials/Stahl_003/uvset0.outputs:result' @ '/World/UR__Cobot_Mir_AMR/Materials/Stahl_003/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/UR__Cobot_Mir_AMR/Materials/Stahl_003/tex_normal' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/Stahl.003_normal_scale0_norm.jpg'
    * Inputs:
      * 'bias' [float4] = '(-1.000, -1.000, -1.000, -1.000)'
      * 'fallback' [float4] = '(0.000, 0.000, 1.000, 1.000)'
      * 'file' [asset] = '0/Stahl.003_normal_scale0_norm.jpg'
      * 'scale' [float4] = '(2.000, 2.000, 2.000, 2.000)'
      * 'st' [float2]
        * Connected: '/World/UR__Cobot_Mir_AMR/Materials/Stahl_003/uvset0.outputs:result' @ '/World/UR__Cobot_Mir_AMR/Materials/Stahl_003/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/UR__Cobot_Mir_AMR/Materials/Stahl_003/tex_roughness' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/Stahl.003_metallicRoughness_rough.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 0.000, 0.000, 1.000)'
      * 'file' [asset] = '0/Stahl.003_metallicRoughness_rough.jpg'
      * 'st' [float2]
        * Connected: '/World/UR__Cobot_Mir_AMR/Materials/Stahl_003/uvset0.outputs:result' @ '/World/UR__Cobot_Mir_AMR/Materials/Stahl_003/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'

---

### /World/UR__Cobot_Mir_AMR/Materials/Schwarz_metal_mat_001

* **Prim路径 (Prim Path):**/World/UR__Cobot_Mir_AMR/Materials/Schwarz_metal_mat_001
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/UR__Cobot_Mir_AMR/Materials/Schwarz_metal_mat_001/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/UR__Cobot_Mir_AMR/Materials/Schwarz_metal_mat_001/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.105, 0.107, 0.108)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '1'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0.3'

---

### /World/UR__Cobot_Mir_AMR/Materials/Allu_Mat_Dunkel_001

* **Prim路径 (Prim Path):**/World/UR__Cobot_Mir_AMR/Materials/Allu_Mat_Dunkel_001
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/UR__Cobot_Mir_AMR/Materials/Allu_Mat_Dunkel_001/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/UR__Cobot_Mir_AMR/Materials/Allu_Mat_Dunkel_001/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f]
        * Connected: '/World/UR__Cobot_Mir_AMR/Materials/Allu_Mat_Dunkel_001/tex_base.outputs:rgb' @ '/World/UR__Cobot_Mir_AMR/Materials/Allu_Mat_Dunkel_001/tex_base'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/Allu-Mat.Dunkel.001_baseColor.jpg'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float]
        * Connected: '/World/UR__Cobot_Mir_AMR/Materials/Allu_Mat_Dunkel_001/tex_metallic.outputs:r' @ '/World/UR__Cobot_Mir_AMR/Materials/Allu_Mat_Dunkel_001/tex_metallic'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/Allu-Mat.Dunkel.001_metallicRoughness_metal.jpg'
      * 'normal' [normal3f]
        * Connected: '/World/UR__Cobot_Mir_AMR/Materials/Allu_Mat_Dunkel_001/tex_normal.outputs:rgb' @ '/World/UR__Cobot_Mir_AMR/Materials/Allu_Mat_Dunkel_001/tex_normal'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/Allu-Mat.Dunkel.001_normal_scale1_norm.jpg'
      * 'occlusion' [float] = '1'
      * 'roughness' [float]
        * Connected: '/World/UR__Cobot_Mir_AMR/Materials/Allu_Mat_Dunkel_001/tex_roughness.outputs:r' @ '/World/UR__Cobot_Mir_AMR/Materials/Allu_Mat_Dunkel_001/tex_roughness'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/Allu-Mat.Dunkel.001_metallicRoughness_rough.jpg'
    * '/World/UR__Cobot_Mir_AMR/Materials/Allu_Mat_Dunkel_001/tex_base' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/Allu-Mat.Dunkel.001_baseColor.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'file' [asset] = '0/Allu-Mat.Dunkel.001_baseColor.jpg'
      * 'st' [float2]
        * Connected: '/World/UR__Cobot_Mir_AMR/Materials/Allu_Mat_Dunkel_001/uvset0.outputs:result' @ '/World/UR__Cobot_Mir_AMR/Materials/Allu_Mat_Dunkel_001/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/UR__Cobot_Mir_AMR/Materials/Allu_Mat_Dunkel_001/uvset0' (ID: 'UsdPrimvarReader_float2')
    * Implementation: 'id'
    * '/World/UR__Cobot_Mir_AMR/Materials/Allu_Mat_Dunkel_001/tex_metallic' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/Allu-Mat.Dunkel.001_metallicRoughness_metal.jpg'
    * Inputs:
      * 'fallback' [float4] = '(0.000, 0.000, 0.000, 1.000)'
      * 'file' [asset] = '0/Allu-Mat.Dunkel.001_metallicRoughness_metal.jpg'
      * 'st' [float2]
        * Connected: '/World/UR__Cobot_Mir_AMR/Materials/Allu_Mat_Dunkel_001/uvset0.outputs:result' @ '/World/UR__Cobot_Mir_AMR/Materials/Allu_Mat_Dunkel_001/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/UR__Cobot_Mir_AMR/Materials/Allu_Mat_Dunkel_001/tex_normal' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/Allu-Mat.Dunkel.001_normal_scale1_norm.jpg'
    * Inputs:
      * 'bias' [float4] = '(-1.000, -1.000, -1.000, -1.000)'
      * 'fallback' [float4] = '(0.000, 0.000, 1.000, 1.000)'
      * 'file' [asset] = '0/Allu-Mat.Dunkel.001_normal_scale1_norm.jpg'
      * 'scale' [float4] = '(2.000, 2.000, 2.000, 2.000)'
      * 'st' [float2]
        * Connected: '/World/UR__Cobot_Mir_AMR/Materials/Allu_Mat_Dunkel_001/uvset0.outputs:result' @ '/World/UR__Cobot_Mir_AMR/Materials/Allu_Mat_Dunkel_001/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/UR__Cobot_Mir_AMR/Materials/Allu_Mat_Dunkel_001/tex_roughness' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/Allu-Mat.Dunkel.001_metallicRoughness_rough.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 0.000, 0.000, 1.000)'
      * 'file' [asset] = '0/Allu-Mat.Dunkel.001_metallicRoughness_rough.jpg'
      * 'st' [float2]
        * Connected: '/World/UR__Cobot_Mir_AMR/Materials/Allu_Mat_Dunkel_001/uvset0.outputs:result' @ '/World/UR__Cobot_Mir_AMR/Materials/Allu_Mat_Dunkel_001/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'

---

### /World/UR__Cobot_Mir_AMR/Materials/Hel_Blau_Plastik_001

* **Prim路径 (Prim Path):**/World/UR__Cobot_Mir_AMR/Materials/Hel_Blau_Plastik_001
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/UR__Cobot_Mir_AMR/Materials/Hel_Blau_Plastik_001/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/UR__Cobot_Mir_AMR/Materials/Hel_Blau_Plastik_001/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.323, 0.515, 0.761)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0.078788'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0.175758'

---

### /World/UR__Cobot_Mir_AMR/Materials/Gumi_Schwarz_001

* **Prim路径 (Prim Path):**/World/UR__Cobot_Mir_AMR/Materials/Gumi_Schwarz_001
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/UR__Cobot_Mir_AMR/Materials/Gumi_Schwarz_001/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/UR__Cobot_Mir_AMR/Materials/Gumi_Schwarz_001/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.009, 0.009, 0.009)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0.411212'

---

### /World/UR__Cobot_Mir_AMR/Materials/Material_003

* **Prim路径 (Prim Path):**/World/UR__Cobot_Mir_AMR/Materials/Material_003
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/UR__Cobot_Mir_AMR/Materials/Material_003/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/UR__Cobot_Mir_AMR/Materials/Material_003/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.973, 0.539, 0.109)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '1'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0.1'

---

### /World/UR__Cobot_Mir_AMR/Materials/_00000FF

* **Prim路径 (Prim Path):**/World/UR__Cobot_Mir_AMR/Materials/_00000FF
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/UR__Cobot_Mir_AMR/Materials/_00000FF/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/UR__Cobot_Mir_AMR/Materials/_00000FF/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0.05'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0.5'

---

### /World/UR__Cobot_Mir_AMR/Materials/_A0A0AFF

* **Prim路径 (Prim Path):**/World/UR__Cobot_Mir_AMR/Materials/_A0A0AFF
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/UR__Cobot_Mir_AMR/Materials/_A0A0AFF/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/UR__Cobot_Mir_AMR/Materials/_A0A0AFF/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.039, 0.039, 0.039)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0.05'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0.5'

---

### /World/UR__Cobot_Mir_AMR/Materials/_E0000FF

* **Prim路径 (Prim Path):**/World/UR__Cobot_Mir_AMR/Materials/_E0000FF
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/UR__Cobot_Mir_AMR/Materials/_E0000FF/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/UR__Cobot_Mir_AMR/Materials/_E0000FF/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.055, 0.000, 0.000)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0.05'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0.5'

---

### /World/UR__Cobot_Mir_AMR/Materials/_1585CFF_001

* **Prim路径 (Prim Path):**/World/UR__Cobot_Mir_AMR/Materials/_1585CFF_001
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/UR__Cobot_Mir_AMR/Materials/_1585CFF_001/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/UR__Cobot_Mir_AMR/Materials/_1585CFF_001/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.020, 0.020, 0.020)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0.05'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0.5'

---

### /World/UR__Cobot_Mir_AMR/Materials/_92929FF

* **Prim路径 (Prim Path):**/World/UR__Cobot_Mir_AMR/Materials/_92929FF
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/UR__Cobot_Mir_AMR/Materials/_92929FF/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/UR__Cobot_Mir_AMR/Materials/_92929FF/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.161, 0.161, 0.161)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0.05'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0.5'

---

### /World/UR__Cobot_Mir_AMR/Materials/_000FFFF

* **Prim路径 (Prim Path):**/World/UR__Cobot_Mir_AMR/Materials/_000FFFF
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/UR__Cobot_Mir_AMR/Materials/_000FFFF/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/UR__Cobot_Mir_AMR/Materials/_000FFFF/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.000, 0.000, 1.000)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0.05'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0.5'

---

### /World/UR__Cobot_Mir_AMR/Materials/A5ADB1FF

* **Prim路径 (Prim Path):**/World/UR__Cobot_Mir_AMR/Materials/A5ADB1FF
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/UR__Cobot_Mir_AMR/Materials/A5ADB1FF/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/UR__Cobot_Mir_AMR/Materials/A5ADB1FF/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.647, 0.678, 0.694)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0.05'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0.5'

---

### /World/UR__Cobot_Mir_AMR/Materials/B28C01FF

* **Prim路径 (Prim Path):**/World/UR__Cobot_Mir_AMR/Materials/B28C01FF
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/UR__Cobot_Mir_AMR/Materials/B28C01FF/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/UR__Cobot_Mir_AMR/Materials/B28C01FF/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.698, 0.549, 0.004)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0.05'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0.5'

---

### /World/UR__Cobot_Mir_AMR/Materials/FFFF00FF

* **Prim路径 (Prim Path):**/World/UR__Cobot_Mir_AMR/Materials/FFFF00FF
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/UR__Cobot_Mir_AMR/Materials/FFFF00FF/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/UR__Cobot_Mir_AMR/Materials/FFFF00FF/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(1.000, 1.000, 0.000)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0.05'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0.5'

---

### /World/UR__Cobot_Mir_AMR/Materials/_04040FF

* **Prim路径 (Prim Path):**/World/UR__Cobot_Mir_AMR/Materials/_04040FF
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/UR__Cobot_Mir_AMR/Materials/_04040FF/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/UR__Cobot_Mir_AMR/Materials/_04040FF/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.251, 0.251, 0.251)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0.05'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0.5'

---

### /World/UR__Cobot_Mir_AMR/Materials/BFBFBFFF

* **Prim路径 (Prim Path):**/World/UR__Cobot_Mir_AMR/Materials/BFBFBFFF
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/UR__Cobot_Mir_AMR/Materials/BFBFBFFF/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/UR__Cobot_Mir_AMR/Materials/BFBFBFFF/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.749, 0.749, 0.749)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0.05'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0.5'

---

### /World/UR__Cobot_Mir_AMR/Materials/CBD2EEFF

* **Prim路径 (Prim Path):**/World/UR__Cobot_Mir_AMR/Materials/CBD2EEFF
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/UR__Cobot_Mir_AMR/Materials/CBD2EEFF/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/UR__Cobot_Mir_AMR/Materials/CBD2EEFF/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.796, 0.824, 0.933)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0.05'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0.5'

---

### /World/UR__Cobot_Mir_AMR/Materials/FFFFFFFF

* **Prim路径 (Prim Path):**/World/UR__Cobot_Mir_AMR/Materials/FFFFFFFF
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/UR__Cobot_Mir_AMR/Materials/FFFFFFFF/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/UR__Cobot_Mir_AMR/Materials/FFFFFFFF/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(1.000, 1.000, 1.000)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0.05'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0.5'

---

### /World/UR__Cobot_Mir_AMR/Materials/_85858FF

* **Prim路径 (Prim Path):**/World/UR__Cobot_Mir_AMR/Materials/_85858FF
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/UR__Cobot_Mir_AMR/Materials/_85858FF/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/UR__Cobot_Mir_AMR/Materials/_85858FF/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.345, 0.345, 0.345)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0.05'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0.5'

---

### /World/UR__Cobot_Mir_AMR/Materials/BEBEBEFF

* **Prim路径 (Prim Path):**/World/UR__Cobot_Mir_AMR/Materials/BEBEBEFF
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/UR__Cobot_Mir_AMR/Materials/BEBEBEFF/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/UR__Cobot_Mir_AMR/Materials/BEBEBEFF/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.745, 0.745, 0.745)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0.05'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0.5'

---

### /World/UR__Cobot_Mir_AMR/Materials/B09C86FF

* **Prim路径 (Prim Path):**/World/UR__Cobot_Mir_AMR/Materials/B09C86FF
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/UR__Cobot_Mir_AMR/Materials/B09C86FF/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/UR__Cobot_Mir_AMR/Materials/B09C86FF/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.690, 0.612, 0.525)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0.05'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0.5'

---

### /World/UR__Cobot_Mir_AMR/Materials/AAAAAAFF

* **Prim路径 (Prim Path):**/World/UR__Cobot_Mir_AMR/Materials/AAAAAAFF
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/UR__Cobot_Mir_AMR/Materials/AAAAAAFF/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/UR__Cobot_Mir_AMR/Materials/AAAAAAFF/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.667, 0.667, 0.667)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0.05'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0.5'

---

### /World/UR__Cobot_Mir_AMR/Materials/_0FF0CFF

* **Prim路径 (Prim Path):**/World/UR__Cobot_Mir_AMR/Materials/_0FF0CFF
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/UR__Cobot_Mir_AMR/Materials/_0FF0CFF/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/UR__Cobot_Mir_AMR/Materials/_0FF0CFF/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.000, 1.000, 0.047)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0.05'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0.5'

---

### /World/UR__Cobot_Mir_AMR/Materials/FEFEFFFF

* **Prim路径 (Prim Path):**/World/UR__Cobot_Mir_AMR/Materials/FEFEFFFF
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/UR__Cobot_Mir_AMR/Materials/FEFEFFFF/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/UR__Cobot_Mir_AMR/Materials/FEFEFFFF/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.996, 0.996, 1.000)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0.05'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0.5'

---

### /World/UR__Cobot_Mir_AMR/Materials/_99999FF

* **Prim路径 (Prim Path):**/World/UR__Cobot_Mir_AMR/Materials/_99999FF
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/UR__Cobot_Mir_AMR/Materials/_99999FF/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/UR__Cobot_Mir_AMR/Materials/_99999FF/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.600, 0.600, 0.600)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0.05'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0.5'

---

### /World/UR__Cobot_Mir_AMR/Materials/_0FF00FF

* **Prim路径 (Prim Path):**/World/UR__Cobot_Mir_AMR/Materials/_0FF00FF
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/UR__Cobot_Mir_AMR/Materials/_0FF00FF/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/UR__Cobot_Mir_AMR/Materials/_0FF00FF/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.000, 1.000, 0.000)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0.05'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0.5'

---

### /World/UR__Cobot_Mir_AMR/Materials/E6C76CFF

* **Prim路径 (Prim Path):**/World/UR__Cobot_Mir_AMR/Materials/E6C76CFF
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/UR__Cobot_Mir_AMR/Materials/E6C76CFF/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/UR__Cobot_Mir_AMR/Materials/E6C76CFF/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.902, 0.780, 0.424)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0.05'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0.5'

---

### /World/UR__Cobot_Mir_AMR/Materials/_0007FFF

* **Prim路径 (Prim Path):**/World/UR__Cobot_Mir_AMR/Materials/_0007FFF
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/UR__Cobot_Mir_AMR/Materials/_0007FFF/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/UR__Cobot_Mir_AMR/Materials/_0007FFF/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.000, 0.000, 0.498)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0.05'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0.5'

---

### /World/UR__Cobot_Mir_AMR/Materials/FF0000FF

* **Prim路径 (Prim Path):**/World/UR__Cobot_Mir_AMR/Materials/FF0000FF
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/UR__Cobot_Mir_AMR/Materials/FF0000FF/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/UR__Cobot_Mir_AMR/Materials/FF0000FF/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(1.000, 0.000, 0.000)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0.05'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0.5'

---

### /World/UR__Cobot_Mir_AMR/Materials/F47F0AFF

* **Prim路径 (Prim Path):**/World/UR__Cobot_Mir_AMR/Materials/F47F0AFF
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/UR__Cobot_Mir_AMR/Materials/F47F0AFF/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/UR__Cobot_Mir_AMR/Materials/F47F0AFF/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.957, 0.498, 0.039)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0.05'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0.5'

---

### /World/UR__Cobot_Mir_AMR/Materials/_724F7FF

* **Prim路径 (Prim Path):**/World/UR__Cobot_Mir_AMR/Materials/_724F7FF
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/UR__Cobot_Mir_AMR/Materials/_724F7FF/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/UR__Cobot_Mir_AMR/Materials/_724F7FF/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.090, 0.141, 0.969)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0.05'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0.5'

---

### /World/UR__Cobot_Mir_AMR/Materials/DDDD0CFF

* **Prim路径 (Prim Path):**/World/UR__Cobot_Mir_AMR/Materials/DDDD0CFF
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/UR__Cobot_Mir_AMR/Materials/DDDD0CFF/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/UR__Cobot_Mir_AMR/Materials/DDDD0CFF/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.867, 0.867, 0.047)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0.05'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0.5'

---

### /World/UR__Cobot_Mir_AMR/Materials/F4F4F4FF

* **Prim路径 (Prim Path):**/World/UR__Cobot_Mir_AMR/Materials/F4F4F4FF
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/UR__Cobot_Mir_AMR/Materials/F4F4F4FF/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/UR__Cobot_Mir_AMR/Materials/F4F4F4FF/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.957, 0.957, 0.957)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0.05'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0.5'

---

### /World/UR__Cobot_Mir_AMR/Materials/B1D8B9FF

* **Prim路径 (Prim Path):**/World/UR__Cobot_Mir_AMR/Materials/B1D8B9FF
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/UR__Cobot_Mir_AMR/Materials/B1D8B9FF/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/UR__Cobot_Mir_AMR/Materials/B1D8B9FF/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.694, 0.847, 0.725)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0.05'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0.5'

---

### /World/UR__Cobot_Mir_AMR/Materials/_6F2FFFF

* **Prim路径 (Prim Path):**/World/UR__Cobot_Mir_AMR/Materials/_6F2FFFF
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/UR__Cobot_Mir_AMR/Materials/_6F2FFFF/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/UR__Cobot_Mir_AMR/Materials/_6F2FFFF/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.086, 0.949, 1.000)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0.05'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0.5'

---

### /World/UR__Cobot_Mir_AMR/Materials/_9192EFF

* **Prim路径 (Prim Path):**/World/UR__Cobot_Mir_AMR/Materials/_9192EFF
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/UR__Cobot_Mir_AMR/Materials/_9192EFF/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/UR__Cobot_Mir_AMR/Materials/_9192EFF/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.098, 0.098, 0.180)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0.05'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0.5'

---

### /World/UR__Cobot_Mir_AMR/Materials/FFDC40FF

* **Prim路径 (Prim Path):**/World/UR__Cobot_Mir_AMR/Materials/FFDC40FF
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/UR__Cobot_Mir_AMR/Materials/FFDC40FF/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/UR__Cobot_Mir_AMR/Materials/FFDC40FF/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(1.000, 0.863, 0.251)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0.05'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0.5'

---

### /World/UR__Cobot_Mir_AMR/Materials/_1585CFF

* **Prim路径 (Prim Path):**/World/UR__Cobot_Mir_AMR/Materials/_1585CFF
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/UR__Cobot_Mir_AMR/Materials/_1585CFF/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/UR__Cobot_Mir_AMR/Materials/_1585CFF/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.318, 0.345, 0.361)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0.05'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0.5'

---

### /World/UR__Cobot_Mir_AMR/Materials/BDBBB9FF

* **Prim路径 (Prim Path):**/World/UR__Cobot_Mir_AMR/Materials/BDBBB9FF
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/UR__Cobot_Mir_AMR/Materials/BDBBB9FF/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/UR__Cobot_Mir_AMR/Materials/BDBBB9FF/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.741, 0.733, 0.725)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0.05'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0.5'

---

### /World/UR__Cobot_Mir_AMR/Materials/_E7DA1FF

* **Prim路径 (Prim Path):**/World/UR__Cobot_Mir_AMR/Materials/_E7DA1FF
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/UR__Cobot_Mir_AMR/Materials/_E7DA1FF/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/UR__Cobot_Mir_AMR/Materials/_E7DA1FF/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.431, 0.490, 0.631)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0.05'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0.5'

---

### /World/UR__Cobot_Mir_AMR/Materials/EAEAEAFF

* **Prim路径 (Prim Path):**/World/UR__Cobot_Mir_AMR/Materials/EAEAEAFF
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/UR__Cobot_Mir_AMR/Materials/EAEAEAFF/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/UR__Cobot_Mir_AMR/Materials/EAEAEAFF/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.918, 0.918, 0.918)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0.05'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0.5'

---

### /World/UR__Cobot_Mir_AMR/Materials/Material_004

* **Prim路径 (Prim Path):**/World/UR__Cobot_Mir_AMR/Materials/Material_004
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/UR__Cobot_Mir_AMR/Materials/Material_004/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/UR__Cobot_Mir_AMR/Materials/Material_004/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.004, 0.204, 0.005)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0.5'

---

### /World/Plastic_Crate_1_/Materials/Material_1

* **Prim路径 (Prim Path):**/World/Plastic_Crate_1_/Materials/Material_1
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/Plastic_Crate_1_/Materials/Material_1/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Plastic_Crate_1_/Materials/Material_1/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f]
        * Connected: '/World/Plastic_Crate_1_/Materials/Material_1/tex_base.outputs:rgb' @ '/World/Plastic_Crate_1_/Materials/Material_1/tex_base'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/Material_1_baseColor_cutoff173.png'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(1.000, 1.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'opacity' [float]
        * Connected: '/World/Plastic_Crate_1_/Materials/Material_1/tex_base.outputs:a' @ '/World/Plastic_Crate_1_/Materials/Material_1/tex_base'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/Material_1_baseColor_cutoff173.png'
      * 'roughness' [float] = '0.6'
    * '/World/Plastic_Crate_1_/Materials/Material_1/tex_base' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/Material_1_baseColor_cutoff173.png'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'file' [asset] = '0/Material_1_baseColor_cutoff173.png'
      * 'st' [float2]
        * Connected: '/World/Plastic_Crate_1_/Materials/Material_1/uvset0.outputs:result' @ '/World/Plastic_Crate_1_/Materials/Material_1/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/Plastic_Crate_1_/Materials/Material_1/uvset0' (ID: 'UsdPrimvarReader_float2')
    * Implementation: 'id'

---

### /World/Plastic_Crate_1__01/Materials/Material_1

* **Prim路径 (Prim Path):**/World/Plastic_Crate_1__01/Materials/Material_1
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/Plastic_Crate_1__01/Materials/Material_1/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Plastic_Crate_1__01/Materials/Material_1/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f]
        * Connected: '/World/Plastic_Crate_1__01/Materials/Material_1/tex_base.outputs:rgb' @ '/World/Plastic_Crate_1__01/Materials/Material_1/tex_base'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/Material_1_baseColor_cutoff173.png'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(1.000, 1.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'opacity' [float]
        * Connected: '/World/Plastic_Crate_1__01/Materials/Material_1/tex_base.outputs:a' @ '/World/Plastic_Crate_1__01/Materials/Material_1/tex_base'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/Material_1_baseColor_cutoff173.png'
      * 'roughness' [float] = '0.6'
    * '/World/Plastic_Crate_1__01/Materials/Material_1/tex_base' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/Material_1_baseColor_cutoff173.png'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'file' [asset] = '0/Material_1_baseColor_cutoff173.png'
      * 'st' [float2]
        * Connected: '/World/Plastic_Crate_1__01/Materials/Material_1/uvset0.outputs:result' @ '/World/Plastic_Crate_1__01/Materials/Material_1/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/Plastic_Crate_1__01/Materials/Material_1/uvset0' (ID: 'UsdPrimvarReader_float2')
    * Implementation: 'id'

---

### /World/Cardbox_A1_04/Looks/Cardboard_A

* **Prim路径 (Prim Path):**/World/Cardbox_A1_04/Looks/Cardboard_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Cardbox_A1_04/Looks/Cardboard_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Cardbox_A1_04/Looks/Cardboard_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * 纹理引用 (Texture Assets):
      * './Textures/T_Cardbox_A1_Albedo.png'
      * './Textures/T_Cardbox_A1_Normal.png'
      * './Textures/T_Cardbox_A1_ORM.png'
    * Inputs:
      * 'diffuse_texture' [asset] = './Textures/T_Cardbox_A1_Albedo.png'
      * 'normalmap_texture' [asset] = './Textures/T_Cardbox_A1_Normal.png'
      * 'ORM_texture' [asset] = './Textures/T_Cardbox_A1_ORM.png'
      * 'reflection_roughness_texture_influence' [float] = '1'

---

### /World/Cardbox_C1_01/Looks/Cardboard_C1

* **Prim路径 (Prim Path):**/World/Cardbox_C1_01/Looks/Cardboard_C1
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Cardbox_C1_01/Looks/Cardboard_C1/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Cardbox_C1_01/Looks/Cardboard_C1/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * 纹理引用 (Texture Assets):
      * './Textures/T_Cardbox_C1_Albedo.png'
      * './Textures/T_Cardbox_C1_Normal.png'
      * './Textures/T_Cardbox_C1_ORM.png'
    * Inputs:
      * 'diffuse_texture' [asset] = './Textures/T_Cardbox_C1_Albedo.png'
      * 'normalmap_texture' [asset] = './Textures/T_Cardbox_C1_Normal.png'
      * 'ORM_texture' [asset] = './Textures/T_Cardbox_C1_ORM.png'
      * 'reflection_roughness_texture_influence' [float] = '1'

---

### /World/Cardbox_A1_05/Looks/Cardboard_A

* **Prim路径 (Prim Path):**/World/Cardbox_A1_05/Looks/Cardboard_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Cardbox_A1_05/Looks/Cardboard_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Cardbox_A1_05/Looks/Cardboard_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * 纹理引用 (Texture Assets):
      * './Textures/T_Cardbox_A1_Albedo.png'
      * './Textures/T_Cardbox_A1_Normal.png'
      * './Textures/T_Cardbox_A1_ORM.png'
    * Inputs:
      * 'diffuse_texture' [asset] = './Textures/T_Cardbox_A1_Albedo.png'
      * 'normalmap_texture' [asset] = './Textures/T_Cardbox_A1_Normal.png'
      * 'ORM_texture' [asset] = './Textures/T_Cardbox_A1_ORM.png'
      * 'reflection_roughness_texture_influence' [float] = '1'

---

### /World/Cardbox_A3_01/Looks/Cardboard_A3

* **Prim路径 (Prim Path):**/World/Cardbox_A3_01/Looks/Cardboard_A3
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Cardbox_A3_01/Looks/Cardboard_A3/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Cardbox_A3_01/Looks/Cardboard_A3/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * 纹理引用 (Texture Assets):
      * './Textures/T_Cardbox_A3_Albedo.png'
      * './Textures/T_Cardbox_A3_Normal.png'
      * './Textures/T_Cardbox_A3_ORM.png'
    * Inputs:
      * 'diffuse_texture' [asset] = './Textures/T_Cardbox_A3_Albedo.png'
      * 'normalmap_texture' [asset] = './Textures/T_Cardbox_A3_Normal.png'
      * 'ORM_texture' [asset] = './Textures/T_Cardbox_A3_ORM.png'
      * 'reflection_roughness_texture_influence' [float] = '1'

---

### /World/Cardbox_B1_01/Looks/Cardboard_B1

* **Prim路径 (Prim Path):**/World/Cardbox_B1_01/Looks/Cardboard_B1
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Cardbox_B1_01/Looks/Cardboard_B1/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Cardbox_B1_01/Looks/Cardboard_B1/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * 纹理引用 (Texture Assets):
      * './Textures/T_Cardbox_B1_Albedo.png'
      * './Textures/T_Cardbox_B1_Normal.png'
      * './Textures/T_Cardbox_B1_ORM.png'
    * Inputs:
      * 'diffuse_texture' [asset] = './Textures/T_Cardbox_B1_Albedo.png'
      * 'normalmap_texture' [asset] = './Textures/T_Cardbox_B1_Normal.png'
      * 'ORM_texture' [asset] = './Textures/T_Cardbox_B1_ORM.png'
      * 'reflection_roughness_texture_influence' [float] = '1'

---

### /World/Cardbox_C1_02/Looks/Cardboard_C1

* **Prim路径 (Prim Path):**/World/Cardbox_C1_02/Looks/Cardboard_C1
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Cardbox_C1_02/Looks/Cardboard_C1/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Cardbox_C1_02/Looks/Cardboard_C1/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * 纹理引用 (Texture Assets):
      * './Textures/T_Cardbox_C1_Albedo.png'
      * './Textures/T_Cardbox_C1_Normal.png'
      * './Textures/T_Cardbox_C1_ORM.png'
    * Inputs:
      * 'diffuse_texture' [asset] = './Textures/T_Cardbox_C1_Albedo.png'
      * 'normalmap_texture' [asset] = './Textures/T_Cardbox_C1_Normal.png'
      * 'ORM_texture' [asset] = './Textures/T_Cardbox_C1_ORM.png'
      * 'reflection_roughness_texture_influence' [float] = '1'

---

### /World/Cardbox_C3_01/Looks/Cardboard_C3

* **Prim路径 (Prim Path):**/World/Cardbox_C3_01/Looks/Cardboard_C3
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Cardbox_C3_01/Looks/Cardboard_C3/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Cardbox_C3_01/Looks/Cardboard_C3/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * 纹理引用 (Texture Assets):
      * './Textures/T_Cardbox_C3_Albedo.png'
      * './Textures/T_Cardbox_C3_Normal.png'
      * './Textures/T_Cardbox_C3_ORM.png'
    * Inputs:
      * 'diffuse_texture' [asset] = './Textures/T_Cardbox_C3_Albedo.png'
      * 'normalmap_texture' [asset] = './Textures/T_Cardbox_C3_Normal.png'
      * 'ORM_texture' [asset] = './Textures/T_Cardbox_C3_ORM.png'
      * 'reflection_roughness_texture_influence' [float] = '1'

---

### /World/Cardbox_A1_06/Looks/Cardboard_A

* **Prim路径 (Prim Path):**/World/Cardbox_A1_06/Looks/Cardboard_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Cardbox_A1_06/Looks/Cardboard_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Cardbox_A1_06/Looks/Cardboard_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * 纹理引用 (Texture Assets):
      * './Textures/T_Cardbox_A1_Albedo.png'
      * './Textures/T_Cardbox_A1_Normal.png'
      * './Textures/T_Cardbox_A1_ORM.png'
    * Inputs:
      * 'diffuse_texture' [asset] = './Textures/T_Cardbox_A1_Albedo.png'
      * 'normalmap_texture' [asset] = './Textures/T_Cardbox_A1_Normal.png'
      * 'ORM_texture' [asset] = './Textures/T_Cardbox_A1_ORM.png'
      * 'reflection_roughness_texture_influence' [float] = '1'

---

### /World/Cardbox_A1_07/Looks/Cardboard_A

* **Prim路径 (Prim Path):**/World/Cardbox_A1_07/Looks/Cardboard_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Cardbox_A1_07/Looks/Cardboard_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Cardbox_A1_07/Looks/Cardboard_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * 纹理引用 (Texture Assets):
      * './Textures/T_Cardbox_A1_Albedo.png'
      * './Textures/T_Cardbox_A1_Normal.png'
      * './Textures/T_Cardbox_A1_ORM.png'
    * Inputs:
      * 'diffuse_texture' [asset] = './Textures/T_Cardbox_A1_Albedo.png'
      * 'normalmap_texture' [asset] = './Textures/T_Cardbox_A1_Normal.png'
      * 'ORM_texture' [asset] = './Textures/T_Cardbox_A1_ORM.png'
      * 'reflection_roughness_texture_influence' [float] = '1'

---

### /World/Cardbox_B1_02/Looks/Cardboard_B1

* **Prim路径 (Prim Path):**/World/Cardbox_B1_02/Looks/Cardboard_B1
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Cardbox_B1_02/Looks/Cardboard_B1/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Cardbox_B1_02/Looks/Cardboard_B1/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * 纹理引用 (Texture Assets):
      * './Textures/T_Cardbox_B1_Albedo.png'
      * './Textures/T_Cardbox_B1_Normal.png'
      * './Textures/T_Cardbox_B1_ORM.png'
    * Inputs:
      * 'diffuse_texture' [asset] = './Textures/T_Cardbox_B1_Albedo.png'
      * 'normalmap_texture' [asset] = './Textures/T_Cardbox_B1_Normal.png'
      * 'ORM_texture' [asset] = './Textures/T_Cardbox_B1_ORM.png'
      * 'reflection_roughness_texture_influence' [float] = '1'

---

### /World/Cardbox_B2_01/Looks/Cardboard_B2

* **Prim路径 (Prim Path):**/World/Cardbox_B2_01/Looks/Cardboard_B2
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Cardbox_B2_01/Looks/Cardboard_B2/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Cardbox_B2_01/Looks/Cardboard_B2/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * 纹理引用 (Texture Assets):
      * './Textures/T_Cardbox_B2_Albedo.png'
      * './Textures/T_Cardbox_B2_Normal.png'
      * './Textures/T_Cardbox_B2_ORM.png'
    * Inputs:
      * 'diffuse_texture' [asset] = './Textures/T_Cardbox_B2_Albedo.png'
      * 'normalmap_texture' [asset] = './Textures/T_Cardbox_B2_Normal.png'
      * 'ORM_texture' [asset] = './Textures/T_Cardbox_B2_ORM.png'
      * 'reflection_roughness_texture_influence' [float] = '1'

---

### /World/Cardbox_B3_03/Looks/Cardboard_B3

* **Prim路径 (Prim Path):**/World/Cardbox_B3_03/Looks/Cardboard_B3
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Cardbox_B3_03/Looks/Cardboard_B3/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Cardbox_B3_03/Looks/Cardboard_B3/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * 纹理引用 (Texture Assets):
      * './Textures/T_Cardbox_B3_Albedo.png'
      * './Textures/T_Cardbox_B3_Normal.png'
      * './Textures/T_Cardbox_B3_ORM.png'
    * Inputs:
      * 'diffuse_texture' [asset] = './Textures/T_Cardbox_B3_Albedo.png'
      * 'normalmap_texture' [asset] = './Textures/T_Cardbox_B3_Normal.png'
      * 'ORM_texture' [asset] = './Textures/T_Cardbox_B3_ORM.png'
      * 'reflection_roughness_texture_influence' [float] = '1'

---

### /World/Cardbox_C1_03/Looks/Cardboard_C1

* **Prim路径 (Prim Path):**/World/Cardbox_C1_03/Looks/Cardboard_C1
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Cardbox_C1_03/Looks/Cardboard_C1/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Cardbox_C1_03/Looks/Cardboard_C1/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * 纹理引用 (Texture Assets):
      * './Textures/T_Cardbox_C1_Albedo.png'
      * './Textures/T_Cardbox_C1_Normal.png'
      * './Textures/T_Cardbox_C1_ORM.png'
    * Inputs:
      * 'diffuse_texture' [asset] = './Textures/T_Cardbox_C1_Albedo.png'
      * 'normalmap_texture' [asset] = './Textures/T_Cardbox_C1_Normal.png'
      * 'ORM_texture' [asset] = './Textures/T_Cardbox_C1_ORM.png'
      * 'reflection_roughness_texture_influence' [float] = '1'

---

### /World/Cardbox_D3/Looks/Cardboard_D3

* **Prim路径 (Prim Path):**/World/Cardbox_D3/Looks/Cardboard_D3
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Cardbox_D3/Looks/Cardboard_D3/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Cardbox_D3/Looks/Cardboard_D3/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * 纹理引用 (Texture Assets):
      * './Textures/T_Cardbox_D3_Albedo.png'
      * './Textures/T_Cardbox_D3_Normal.png'
      * './Textures/T_Cardbox_D3_ORM.png'
    * Inputs:
      * 'diffuse_texture' [asset] = './Textures/T_Cardbox_D3_Albedo.png'
      * 'normalmap_texture' [asset] = './Textures/T_Cardbox_D3_Normal.png'
      * 'ORM_texture' [asset] = './Textures/T_Cardbox_D3_ORM.png'
      * 'reflection_roughness_texture_influence' [float] = '1'

---

### /World/Forklift_A01_PR_V_NVD_01/Looks/M_Forklift_Paint

* **Prim路径 (Prim Path):**/World/Forklift_A01_PR_V_NVD_01/Looks/M_Forklift_Paint
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Forklift_A01_PR_V_NVD_01/Looks/M_Forklift_Paint/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Forklift_A01_PR_V_NVD_01/Looks/M_Forklift_Paint/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * 纹理引用 (Texture Assets):
      * '0/T_Forklift_A1_Albedo.`<UDIM>`.png'
      * '0/T_Forklift_A1_Normal.`<UDIM>`.png'
      * '0/T_Forklift_A1_ORM.`<UDIM>`.png'
      * '0/T_Forklift_A1_Rough.`<UDIM>`.png'
    * Inputs:
      * 'diffuse_texture' [asset] = '0/T_Forklift_A1_Albedo.`<UDIM>`.png'
      * 'diffuse_tint' [color3f]
        * Connected: '/World/Forklift_A01_PR_V_NVD_01/Looks/M_Forklift_Paint.inputs:diffuse_tint' @ '/World/Forklift_A01_PR_V_NVD_01/Looks/M_Forklift_Paint'
      * 'metallic_texture_influence' [float] = '1'
      * 'normalmap_texture' [asset] = '0/T_Forklift_A1_Normal.`<UDIM>`.png'
      * 'ORM_texture' [asset] = '0/T_Forklift_A1_ORM.`<UDIM>`.png'
      * 'reflection_roughness_texture_influence' [float] = '1'
      * 'reflectionroughness_texture' [asset] = '0/T_Forklift_A1_Rough.`<UDIM>`.png'

---

### /World/Forklift_A01_PR_V_NVD_01/Looks/M_Forklift_A1

* **Prim路径 (Prim Path):**/World/Forklift_A01_PR_V_NVD_01/Looks/M_Forklift_A1
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Forklift_A01_PR_V_NVD_01/Looks/M_Forklift_A1/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Forklift_A01_PR_V_NVD_01/Looks/M_Forklift_A1/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * 纹理引用 (Texture Assets):
      * '0/T_Forklift_A1_Albedo.`<UDIM>`.png'
      * '0/T_Forklift_A1_Normal.`<UDIM>`.png'
      * '0/T_Forklift_A1_ORM.`<UDIM>`.png'
      * '0/T_Forklift_A1_Rough.`<UDIM>`.png'
    * Inputs:
      * 'diffuse_texture' [asset] = '0/T_Forklift_A1_Albedo.`<UDIM>`.png'
      * 'metallic_texture_influence' [float] = '1'
      * 'normalmap_texture' [asset] = '0/T_Forklift_A1_Normal.`<UDIM>`.png'
      * 'ORM_texture' [asset] = '0/T_Forklift_A1_ORM.`<UDIM>`.png'
      * 'reflection_roughness_texture_influence' [float] = '1'
      * 'reflectionroughness_texture' [asset] = '0/T_Forklift_A1_Rough.`<UDIM>`.png'

---

### /World/Forklift_A01_PR_V_NVD_01/Looks/M_Forklift_A1_Plastic

* **Prim路径 (Prim Path):**/World/Forklift_A01_PR_V_NVD_01/Looks/M_Forklift_A1_Plastic
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Forklift_A01_PR_V_NVD_01/Looks/M_Forklift_A1_Plastic/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Forklift_A01_PR_V_NVD_01/Looks/M_Forklift_A1_Plastic/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * Inputs:
      * 'metallic_texture_influence' [float] = '1'
      * 'reflection_roughness_texture_influence' [float] = '1'

---

### /World/Forklift_A01_PR_V_NVD_01/Looks/M_Forklift_A1_Glass

* **Prim路径 (Prim Path):**/World/Forklift_A01_PR_V_NVD_01/Looks/M_Forklift_A1_Glass
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Forklift_A01_PR_V_NVD_01/Looks/M_Forklift_A1_Glass/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Forklift_A01_PR_V_NVD_01/Looks/M_Forklift_A1_Glass/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniGlass.mdl' (Sub Id: 'OmniGlass')

---

### /World/Forklift_A01_PR_V_NVD_01/Looks/M_Forklift_A1_Decals

* **Prim路径 (Prim Path):**/World/Forklift_A01_PR_V_NVD_01/Looks/M_Forklift_A1_Decals
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/Forklift_A01_PR_V_NVD_01/Looks/M_Forklift_A1_Decals/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Forklift_A01_PR_V_NVD_01/Looks/M_Forklift_A1_Decals/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * 纹理引用 (Texture Assets):
      * '0/T_ForkliftDecal_A1_Albedo.png'
      * '0/T_ForkliftDecal_A1_Normal.png'
      * '0/T_ForkliftDecal_A1_ORM.png'
      * '0/T_ForkliftDecal_A1_Opacity.png'
      * '0/T_ForkliftDecal_A1_Rough.png'
    * Inputs:
      * 'diffuse_texture' [asset] = '0/T_ForkliftDecal_A1_Albedo.png'
      * 'metallic_texture_influence' [float] = '1'
      * 'normalmap_texture' [asset] = '0/T_ForkliftDecal_A1_Normal.png'
      * 'opacity_texture' [asset] = '0/T_ForkliftDecal_A1_Opacity.png'
      * 'opacity_threshold' [float] = '0.2'
      * 'ORM_texture' [asset] = '0/T_ForkliftDecal_A1_ORM.png'
      * 'reflection_roughness_texture_influence' [float] = '1'
      * 'reflectionroughness_texture' [asset] = '0/T_ForkliftDecal_A1_Rough.png'

---

### /World/forklift_b/Looks/M_Forklift_B1_Body

* **Prim路径 (Prim Path):**/World/forklift_b/Looks/M_Forklift_B1_Body
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/forklift_b/Looks/M_Forklift_B1_Body/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/forklift_b/Looks/M_Forklift_B1_Body/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * 纹理引用 (Texture Assets):
      * '0/T_Forklift_B1_Albedo.`<UDIM>`.png'
      * '0/T_Forklift_B1_Normal.`<UDIM>`.png'
      * '0/T_Forklift_B1_ORM.`<UDIM>`.png'
    * Inputs:
      * 'diffuse_texture' [asset] = '0/T_Forklift_B1_Albedo.`<UDIM>`.png'
      * 'metallic_texture_influence' [float] = '1'
      * 'normalmap_texture' [asset] = '0/T_Forklift_B1_Normal.`<UDIM>`.png'
      * 'ORM_texture' [asset] = '0/T_Forklift_B1_ORM.`<UDIM>`.png'
      * 'reflection_roughness_texture_influence' [float] = '1'

---

### /World/forklift_b/Looks/M_Forklift_B1_Decals

* **Prim路径 (Prim Path):**/World/forklift_b/Looks/M_Forklift_B1_Decals
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/forklift_b/Looks/M_Forklift_B1_Decals/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/forklift_b/Looks/M_Forklift_B1_Decals/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * 纹理引用 (Texture Assets):
      * '0/T_Forklift_B1_Decal_Albedo.png'
      * '0/T_Forklift_B1_Decal_Normal.png'
      * '0/T_Forklift_B1_Decal_Opacity.png'
    * Inputs:
      * 'diffuse_texture' [asset] = '0/T_Forklift_B1_Decal_Albedo.png'
      * 'metallic_texture_influence' [float] = '1'
      * 'normalmap_texture' [asset] = '0/T_Forklift_B1_Decal_Normal.png'
      * 'opacity_texture' [asset] = '0/T_Forklift_B1_Decal_Opacity.png'
      * 'opacity_threshold' [float] = '0.2'
      * 'reflection_roughness_texture_influence' [float] = '1'

---

### /World/forklift_b/Looks/M_Forklift_B1_Glass

* **Prim路径 (Prim Path):**/World/forklift_b/Looks/M_Forklift_B1_Glass
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/forklift_b/Looks/M_Forklift_B1_Glass/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/forklift_b/Looks/M_Forklift_B1_Glass/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniGlass.mdl' (Sub Id: 'OmniGlass')

---

### /World/forklift_b/Looks/M_Forklift_B1_Blue

* **Prim路径 (Prim Path):**/World/forklift_b/Looks/M_Forklift_B1_Blue
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/forklift_b/Looks/M_Forklift_B1_Blue/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/forklift_b/Looks/M_Forklift_B1_Blue/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * 纹理引用 (Texture Assets):
      * '0/T_Forklift_B1_Albedo.`<UDIM>`.png'
      * '0/T_Forklift_B1_Normal.`<UDIM>`.png'
      * '0/T_Forklift_B1_ORM.`<UDIM>`.png'
    * Inputs:
      * 'diffuse_texture' [asset] = '0/T_Forklift_B1_Albedo.`<UDIM>`.png'
      * 'diffuse_tint' [color3f] = '(0.064, 0.323, 1.000)'
      * 'metallic_texture_influence' [float] = '1'
      * 'normalmap_texture' [asset] = '0/T_Forklift_B1_Normal.`<UDIM>`.png'
      * 'ORM_texture' [asset] = '0/T_Forklift_B1_ORM.`<UDIM>`.png'
      * 'reflection_roughness_texture_influence' [float] = '1'

---
