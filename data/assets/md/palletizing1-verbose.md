# USDA场景描述文档:palletizing1.usda

## 1.场景元数据(Scene Metadata)

* **USDA文件路径(USDA File Path):**`/media/simple/another_Documents/isaacsim_assets/scenedata/palletizing1.usda`
* **默认Prim (Default Prim):**'Not Set'
* **单位与坐标系 (Units & Coordinate System):**
  * **米(Meters Per Unit):**1.0
  * **Up Axis:**Z
* **场景描述(Scene Describe):** 该场景呈现出一个高度标准化、模块化的智能化码垛车间，整体规划严谨地遵循了“单元化设计”与“矩阵式排列”的现代工业美学。从厂区的空间格局来看，地面铺设了具有大理石纹理的大型灰色瓷砖，砖缝清晰且整洁，为自动化设备的运行提供了极佳的水平度与视觉美感。整个车间被划分为多个重复且独立的作业集群，每个集群在空间分布上呈现出精准的几何对齐关系。核心工业设备由四组完全一致的自动化作业单元构成，它们在车间内呈等间距纵向排列，形成了一个强大的并行处理矩阵。每一组单元内部都包含三个关键模块：首先是高架式的蓝色带式输送机，这些输送装置采用醒目的亮蓝色钢制支架支撑，黑色皮带表面平整，上方正载有多个呈等距分布的淡黄色方形纸质包装箱，工件正由输送机向作业端平稳移动。其次是紧邻输送机末端部署的独立作业平台，平台顶部铺设有淡色实木纹理的面板，台面上安装有一台修长的白色六轴协作机器人，其机械臂正处于灵活的作业姿态，负责从流水线精准抓取工件并放置在移动端。最后是处于协作机器人下方的物流接驳模块，由一台亮黄色的自动导引运输车（AGV）组成。这些AGV底盘低矮，轮廓圆润，其顶部载有一个带有木质顶面的物料支架，且支架上已叠放了多个已完成封装的纸质包装箱，标志着物流的自动化收集阶段。在设备排布方式上，该场景采用了“流水线-机器人-移动平台”的一对一耦合结构，这种布阵方式消除了不同工位间的交叉干扰，极大提升了生产线的故障容忍度与扩展性。固定式的输送装置（共四条）作为生产的骨干脉络，提供了稳定的物料流；而四台白色协作机器人作为执行核心，实现了从静态流水线到动态物流车的无缝衔接。在场景的侧翼，还可以观察到深褐色的金属质感防护墙，为作业区提供了物理隔离与安全屏障。从整体规划结构分析，该场景巧妙地将固定的自动化生产线与灵活的移动机器人相结合，每一组作业单元都是一个自成体系的“微型工厂”。设备间的分布距离经过了精密测算，确保了AGV在集群间行驶时有充足的路径宽度，同时也保证了机器人的工作包络圆能够覆盖输送带末端与移动车顶部的所有作业点。这种由蓝色输送架、黄色物流车、白色机械手臂与灰色纹理地面构成的工业景观，不仅在视觉上层次分明，更在功能上诠释了“柔性制造”与“工业4.0”的核心内涵：通过高度重复的标准化模块实现大规模定制，通过无人化的协作流程确保生产精度与安全。整个车间逻辑清晰，没有任何冗余的杂物或暴露的电缆，展现了一个处于极佳运行状态、具备高度协同能力的现代化智能分拣装配范本。
* **设备数量(Device Number):**
  * **Scene: 1**
  * **IndustrialRobot: 8**
  * **Workbench: 8**
  * **Conveyor: 8**
  * **AGV: 8**
  * **Forklift: 0**
  * **Box: 56**
  * **Rack: 0**
  * **Pallet: 0**
  * **Part: 0**
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
  * Ground (Xform)
    * geom (Mesh)
    * collisionPlane (Plane)
  * Physics_Materials (Prim)
    * physics_material (Material)
  * Looks (Prim)
    * visual_material (Material)
      * shader (Shader)
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
  * agv_7 (Xform)
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
  * agv_8 (Xform)
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
  * Conveyor_1 (Xform)
    * Materials (Scope)
      * Conveyor (Material)
        * pbr_shader (Shader)
        * uvset0 (Shader)
        * tex_base (Shader)
        * tex_specular (Shader)
        * tex_glossiness (Shader)
        * tex_normal (Shader)
        * tex_occlusion (Shader)
      * Belt (Material)
        * pbr_shader (Shader)
        * uvset0 (Shader)
        * tex_base (Shader)
    * Meshes (Xform)
      * Sketchfab_model (Xform)
        * Conveyor_FBX (Xform)
          * RootNode (Xform)
            * Conveyor01Frame (Xform)
              * Conveyor01Frame_Conveyor_0 (Xform)
                * Conveyor01Frame_Conveyor_0 (Mesh)
            * Conveyor01Frame01 (Xform)
              * Conveyor01Frame01_Conveyor_0 (Xform)
                * Conveyor01Frame01_Conveyor_0 (Mesh)
            * Conveyor01Frame02 (Xform)
              * Conveyor01Frame02_Conveyor_0 (Xform)
                * Conveyor01Frame02_Conveyor_0 (Mesh)
            * Conveyor01Legs (Xform)
              * Conveyor01Legs_Conveyor_0 (Xform)
                * Conveyor01Legs_Conveyor_0 (Mesh)
            * Conveyor01Belt (Xform)
              * Conveyor01Belt_Belt_0 (Xform)
                * Conveyor01Belt_Belt_0 (Mesh)
  * Conveyor_2 (Xform)
    * Materials (Scope)
      * Conveyor (Material)
        * pbr_shader (Shader)
        * uvset0 (Shader)
        * tex_base (Shader)
        * tex_specular (Shader)
        * tex_glossiness (Shader)
        * tex_normal (Shader)
        * tex_occlusion (Shader)
      * Belt (Material)
        * pbr_shader (Shader)
        * uvset0 (Shader)
        * tex_base (Shader)
    * Meshes (Xform)
      * Sketchfab_model (Xform)
        * Conveyor_FBX (Xform)
          * RootNode (Xform)
            * Conveyor01Frame (Xform)
              * Conveyor01Frame_Conveyor_0 (Xform)
                * Conveyor01Frame_Conveyor_0 (Mesh)
            * Conveyor01Frame01 (Xform)
              * Conveyor01Frame01_Conveyor_0 (Xform)
                * Conveyor01Frame01_Conveyor_0 (Mesh)
            * Conveyor01Frame02 (Xform)
              * Conveyor01Frame02_Conveyor_0 (Xform)
                * Conveyor01Frame02_Conveyor_0 (Mesh)
            * Conveyor01Legs (Xform)
              * Conveyor01Legs_Conveyor_0 (Xform)
                * Conveyor01Legs_Conveyor_0 (Mesh)
            * Conveyor01Belt (Xform)
              * Conveyor01Belt_Belt_0 (Xform)
                * Conveyor01Belt_Belt_0 (Mesh)
  * Conveyor_3 (Xform)
    * Materials (Scope)
      * Conveyor (Material)
        * pbr_shader (Shader)
        * uvset0 (Shader)
        * tex_base (Shader)
        * tex_specular (Shader)
        * tex_glossiness (Shader)
        * tex_normal (Shader)
        * tex_occlusion (Shader)
      * Belt (Material)
        * pbr_shader (Shader)
        * uvset0 (Shader)
        * tex_base (Shader)
    * Meshes (Xform)
      * Sketchfab_model (Xform)
        * Conveyor_FBX (Xform)
          * RootNode (Xform)
            * Conveyor01Frame (Xform)
              * Conveyor01Frame_Conveyor_0 (Xform)
                * Conveyor01Frame_Conveyor_0 (Mesh)
            * Conveyor01Frame01 (Xform)
              * Conveyor01Frame01_Conveyor_0 (Xform)
                * Conveyor01Frame01_Conveyor_0 (Mesh)
            * Conveyor01Frame02 (Xform)
              * Conveyor01Frame02_Conveyor_0 (Xform)
                * Conveyor01Frame02_Conveyor_0 (Mesh)
            * Conveyor01Legs (Xform)
              * Conveyor01Legs_Conveyor_0 (Xform)
                * Conveyor01Legs_Conveyor_0 (Mesh)
            * Conveyor01Belt (Xform)
              * Conveyor01Belt_Belt_0 (Xform)
                * Conveyor01Belt_Belt_0 (Mesh)
  * Conveyor_4 (Xform)
    * Materials (Scope)
      * Conveyor (Material)
        * pbr_shader (Shader)
        * uvset0 (Shader)
        * tex_base (Shader)
        * tex_specular (Shader)
        * tex_glossiness (Shader)
        * tex_normal (Shader)
        * tex_occlusion (Shader)
      * Belt (Material)
        * pbr_shader (Shader)
        * uvset0 (Shader)
        * tex_base (Shader)
    * Meshes (Xform)
      * Sketchfab_model (Xform)
        * Conveyor_FBX (Xform)
          * RootNode (Xform)
            * Conveyor01Frame (Xform)
              * Conveyor01Frame_Conveyor_0 (Xform)
                * Conveyor01Frame_Conveyor_0 (Mesh)
            * Conveyor01Frame01 (Xform)
              * Conveyor01Frame01_Conveyor_0 (Xform)
                * Conveyor01Frame01_Conveyor_0 (Mesh)
            * Conveyor01Frame02 (Xform)
              * Conveyor01Frame02_Conveyor_0 (Xform)
                * Conveyor01Frame02_Conveyor_0 (Mesh)
            * Conveyor01Legs (Xform)
              * Conveyor01Legs_Conveyor_0 (Xform)
                * Conveyor01Legs_Conveyor_0 (Mesh)
            * Conveyor01Belt (Xform)
              * Conveyor01Belt_Belt_0 (Xform)
                * Conveyor01Belt_Belt_0 (Mesh)
  * Conveyor_5 (Xform)
    * Materials (Scope)
      * Conveyor (Material)
        * pbr_shader (Shader)
        * uvset0 (Shader)
        * tex_base (Shader)
        * tex_specular (Shader)
        * tex_glossiness (Shader)
        * tex_normal (Shader)
        * tex_occlusion (Shader)
      * Belt (Material)
        * pbr_shader (Shader)
        * uvset0 (Shader)
        * tex_base (Shader)
    * Meshes (Xform)
      * Sketchfab_model (Xform)
        * Conveyor_FBX (Xform)
          * RootNode (Xform)
            * Conveyor01Frame (Xform)
              * Conveyor01Frame_Conveyor_0 (Xform)
                * Conveyor01Frame_Conveyor_0 (Mesh)
            * Conveyor01Frame01 (Xform)
              * Conveyor01Frame01_Conveyor_0 (Xform)
                * Conveyor01Frame01_Conveyor_0 (Mesh)
            * Conveyor01Frame02 (Xform)
              * Conveyor01Frame02_Conveyor_0 (Xform)
                * Conveyor01Frame02_Conveyor_0 (Mesh)
            * Conveyor01Legs (Xform)
              * Conveyor01Legs_Conveyor_0 (Xform)
                * Conveyor01Legs_Conveyor_0 (Mesh)
            * Conveyor01Belt (Xform)
              * Conveyor01Belt_Belt_0 (Xform)
                * Conveyor01Belt_Belt_0 (Mesh)
  * Conveyor_6 (Xform)
    * Materials (Scope)
      * Conveyor (Material)
        * pbr_shader (Shader)
        * uvset0 (Shader)
        * tex_base (Shader)
        * tex_specular (Shader)
        * tex_glossiness (Shader)
        * tex_normal (Shader)
        * tex_occlusion (Shader)
      * Belt (Material)
        * pbr_shader (Shader)
        * uvset0 (Shader)
        * tex_base (Shader)
    * Meshes (Xform)
      * Sketchfab_model (Xform)
        * Conveyor_FBX (Xform)
          * RootNode (Xform)
            * Conveyor01Frame (Xform)
              * Conveyor01Frame_Conveyor_0 (Xform)
                * Conveyor01Frame_Conveyor_0 (Mesh)
            * Conveyor01Frame01 (Xform)
              * Conveyor01Frame01_Conveyor_0 (Xform)
                * Conveyor01Frame01_Conveyor_0 (Mesh)
            * Conveyor01Frame02 (Xform)
              * Conveyor01Frame02_Conveyor_0 (Xform)
                * Conveyor01Frame02_Conveyor_0 (Mesh)
            * Conveyor01Legs (Xform)
              * Conveyor01Legs_Conveyor_0 (Xform)
                * Conveyor01Legs_Conveyor_0 (Mesh)
            * Conveyor01Belt (Xform)
              * Conveyor01Belt_Belt_0 (Xform)
                * Conveyor01Belt_Belt_0 (Mesh)
  * Conveyor_7 (Xform)
    * Materials (Scope)
      * Conveyor (Material)
        * pbr_shader (Shader)
        * uvset0 (Shader)
        * tex_base (Shader)
        * tex_specular (Shader)
        * tex_glossiness (Shader)
        * tex_normal (Shader)
        * tex_occlusion (Shader)
      * Belt (Material)
        * pbr_shader (Shader)
        * uvset0 (Shader)
        * tex_base (Shader)
    * Meshes (Xform)
      * Sketchfab_model (Xform)
        * Conveyor_FBX (Xform)
          * RootNode (Xform)
            * Conveyor01Frame (Xform)
              * Conveyor01Frame_Conveyor_0 (Xform)
                * Conveyor01Frame_Conveyor_0 (Mesh)
            * Conveyor01Frame01 (Xform)
              * Conveyor01Frame01_Conveyor_0 (Xform)
                * Conveyor01Frame01_Conveyor_0 (Mesh)
            * Conveyor01Frame02 (Xform)
              * Conveyor01Frame02_Conveyor_0 (Xform)
                * Conveyor01Frame02_Conveyor_0 (Mesh)
            * Conveyor01Legs (Xform)
              * Conveyor01Legs_Conveyor_0 (Xform)
                * Conveyor01Legs_Conveyor_0 (Mesh)
            * Conveyor01Belt (Xform)
              * Conveyor01Belt_Belt_0 (Xform)
                * Conveyor01Belt_Belt_0 (Mesh)
  * Conveyor_8 (Xform)
    * Materials (Scope)
      * Conveyor (Material)
        * pbr_shader (Shader)
        * uvset0 (Shader)
        * tex_base (Shader)
        * tex_specular (Shader)
        * tex_glossiness (Shader)
        * tex_normal (Shader)
        * tex_occlusion (Shader)
      * Belt (Material)
        * pbr_shader (Shader)
        * uvset0 (Shader)
        * tex_base (Shader)
    * Meshes (Xform)
      * Sketchfab_model (Xform)
        * Conveyor_FBX (Xform)
          * RootNode (Xform)
            * Conveyor01Frame (Xform)
              * Conveyor01Frame_Conveyor_0 (Xform)
                * Conveyor01Frame_Conveyor_0 (Mesh)
            * Conveyor01Frame01 (Xform)
              * Conveyor01Frame01_Conveyor_0 (Xform)
                * Conveyor01Frame01_Conveyor_0 (Mesh)
            * Conveyor01Frame02 (Xform)
              * Conveyor01Frame02_Conveyor_0 (Xform)
                * Conveyor01Frame02_Conveyor_0 (Mesh)
            * Conveyor01Legs (Xform)
              * Conveyor01Legs_Conveyor_0 (Xform)
                * Conveyor01Legs_Conveyor_0 (Mesh)
            * Conveyor01Belt (Xform)
              * Conveyor01Belt_Belt_0 (Xform)
                * Conveyor01Belt_Belt_0 (Mesh)
  * BoxOnConveyor_1 (Xform)
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
  * BoxOnConveyor_2 (Xform)
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
  * BoxOnConveyor_3 (Xform)
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
  * BoxOnConveyor_4 (Xform)
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
  * BoxOnConveyor_5 (Xform)
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
  * BoxOnConveyor_6 (Xform)
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
  * BoxOnConveyor_7 (Xform)
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
  * BoxOnConveyor_8 (Xform)
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
  * BoxOnConveyor_1_1 (Xform)
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
  * BoxOnConveyor_1_2 (Xform)
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
  * BoxOnConveyor_1_3 (Xform)
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
  * BoxOnConveyor_1_4 (Xform)
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
  * BoxOnConveyor_1_5 (Xform)
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
  * BoxOnConveyor_1_6 (Xform)
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
  * BoxOnConveyor_1_7 (Xform)
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
  * BoxOnConveyor_1_8 (Xform)
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
  * BoxOnConveyor_2_1 (Xform)
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
  * BoxOnConveyor_2_2 (Xform)
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
  * BoxOnConveyor_2_3 (Xform)
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
  * BoxOnConveyor_2_4 (Xform)
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
  * BoxOnConveyor_2_5 (Xform)
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
  * BoxOnConveyor_2_6 (Xform)
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
  * BoxOnConveyor_2_7 (Xform)
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
  * BoxOnConveyor_2_8 (Xform)
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
  * BoxOnConveyor_3_1 (Xform)
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
  * BoxOnConveyor_3_2 (Xform)
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
  * BoxOnConveyor_3_3 (Xform)
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
  * BoxOnConveyor_3_4 (Xform)
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
  * BoxOnConveyor_3_5 (Xform)
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
  * BoxOnConveyor_3_6 (Xform)
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
  * BoxOnConveyor_3_7 (Xform)
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
  * BoxOnConveyor_3_8 (Xform)
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
  * StackedCarton_1 (Xform)
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
  * StackedCarton_2 (Xform)
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
  * StackedCarton_3 (Xform)
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
  * StackedCarton_4 (Xform)
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
  * StackedCarton_5 (Xform)
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
  * StackedCarton_6 (Xform)
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
  * StackedCarton_7 (Xform)
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
  * StackedCarton_8 (Xform)
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
  * StackedCarton_1_1 (Xform)
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
  * StackedCarton_1_2 (Xform)
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
  * StackedCarton_1_3 (Xform)
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
  * StackedCarton_1_4 (Xform)
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
  * StackedCarton_1_5 (Xform)
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
  * StackedCarton_1_6 (Xform)
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
  * StackedCarton_1_7 (Xform)
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
  * StackedCarton_1_8 (Xform)
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
  * StackedCarton_2_1 (Xform)
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
  * StackedCarton_2_2 (Xform)
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
  * StackedCarton_2_3 (Xform)
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
  * StackedCarton_2_4 (Xform)
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
  * StackedCarton_2_5 (Xform)
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
  * StackedCarton_2_6 (Xform)
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
  * StackedCarton_2_7 (Xform)
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
  * StackedCarton_2_8 (Xform)
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
  * HeavyDutyPackingTable_A01_01 (Xform)
    * SM_HeavyDutyPackingTable_A01_01 (Mesh)
      * M_HeavyDutyPackingTable_A01_Body (GeomSubset)
      * M_HeavyDutyPackingTable_A01_Bolts (GeomSubset)
      * M_HeavyDutyPackingTable_A01_TableTop (GeomSubset)
    * Looks (Scope)
      * Wood_Maple_HeavyDutyPackingTable_A (Material)
        * Shader (Shader)
      * Metal_Glossy_A_HeavyDutyPackingTable_A (Material)
        * Shader (Shader)
      * Metal_Painted_Gray_Glossy_A_HeavyDutyPackingTable_A (Material)
        * Shader (Shader)
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
  * HeavyDutyPackingTable_A01_02 (Prim)
  * panda_instanceable1_01 (Prim)
  * HeavyDutyPackingTable_A01_03 (Prim)
  * panda_instanceable1_02 (Prim)
  * HeavyDutyPackingTable_A01_04 (Prim)
  * panda_instanceable1_03 (Prim)
  * HeavyDutyPackingTable_A01_05 (Prim)
  * panda_instanceable1_04 (Prim)
  * HeavyDutyPackingTable_A01_06 (Prim)
  * panda_instanceable1_05 (Prim)
  * HeavyDutyPackingTable_A01_07 (Prim)
  * panda_instanceable1_06 (Prim)
  * panda_instanceable1_07 (Prim)
  * HeavyDutyPackingTable_A01_08 (Prim)

## 3. 对象详细描述 (Detailed Prim Descriptions)

### /World/factory

* **Prim路径 (Prim Path):**/World/factory
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  *   [reference] '/media/simple/another_Documents/isaacsim_assets/scene/factory/factory.usdc'
* **世界包围盒 (World BBox):**
  * Size: '(49.139, 19.897, 67.754)'
  * Center: '(0.761, 0.769, 9.470)'

---

### /World/agv_1

* **Prim路径 (Prim Path):**/World/agv_1
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  *   [reference] '/media/simple/another_Documents/isaacsim_assets/assets/AGV_ready_1/AGV_ready_1.usdc'
* **世界包围盒 (World BBox):**
  * Size: '(1.457, 0.340, 0.669)'
  * Center: '(-18.818, 29.714, 0.279)'

---

### /World/agv_2

* **Prim路径 (Prim Path):**/World/agv_2
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  *   [reference] '/media/simple/another_Documents/isaacsim_assets/assets/AGV_ready_1/AGV_ready_1.usdc'
* **世界包围盒 (World BBox):**
  * Size: '(1.457, 0.340, 0.669)'
  * Center: '(-13.818, 29.714, 0.279)'

---

### /World/agv_3

* **Prim路径 (Prim Path):**/World/agv_3
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  *   [reference] '/media/simple/another_Documents/isaacsim_assets/assets/AGV_ready_1/AGV_ready_1.usdc'
* **世界包围盒 (World BBox):**
  * Size: '(1.457, 0.340, 0.669)'
  * Center: '(-8.818, 29.714, 0.279)'

---

### /World/agv_4

* **Prim路径 (Prim Path):**/World/agv_4
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  *   [reference] '/media/simple/another_Documents/isaacsim_assets/assets/AGV_ready_1/AGV_ready_1.usdc'
* **世界包围盒 (World BBox):**
  * Size: '(1.457, 0.340, 0.669)'
  * Center: '(-3.818, 29.714, 0.279)'

---

### /World/agv_5

* **Prim路径 (Prim Path):**/World/agv_5
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  *   [reference] '/media/simple/another_Documents/isaacsim_assets/assets/AGV_ready_1/AGV_ready_1.usdc'
* **世界包围盒 (World BBox):**
  * Size: '(1.457, 0.340, 0.669)'
  * Center: '(1.182, 29.714, 0.279)'

---

### /World/agv_6

* **Prim路径 (Prim Path):**/World/agv_6
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  *   [reference] '/media/simple/another_Documents/isaacsim_assets/assets/AGV_ready_1/AGV_ready_1.usdc'
* **世界包围盒 (World BBox):**
  * Size: '(1.457, 0.340, 0.669)'
  * Center: '(6.182, 29.714, 0.279)'

---

### /World/agv_7

* **Prim路径 (Prim Path):**/World/agv_7
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  *   [reference] '/media/simple/another_Documents/isaacsim_assets/assets/AGV_ready_1/AGV_ready_1.usdc'
* **世界包围盒 (World BBox):**
  * Size: '(1.457, 0.340, 0.669)'
  * Center: '(11.182, 29.714, 0.279)'

---

### /World/agv_8

* **Prim路径 (Prim Path):**/World/agv_8
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  *   [reference] '/media/simple/another_Documents/isaacsim_assets/assets/AGV_ready_1/AGV_ready_1.usdc'
* **世界包围盒 (World BBox):**
  * Size: '(1.457, 0.340, 0.669)'
  * Center: '(16.182, 29.714, 0.279)'

---

### /World/Conveyor_1

* **Prim路径 (Prim Path):**/World/Conveyor_1
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  *   [reference] '/media/simple/another_Documents/isaacsim_assets/assets/Simple_rubber_conveyor/Simple_rubber_conveyor.usdc'
* **世界包围盒 (World BBox):**
  * Size: '(188.440, 149.880, 400.080)'
  * Center: '(-19.029, 26.804, 0.889)'

---

### /World/Conveyor_2

* **Prim路径 (Prim Path):**/World/Conveyor_2
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  *   [reference] '/media/simple/another_Documents/isaacsim_assets/assets/Simple_rubber_conveyor/Simple_rubber_conveyor.usdc'
* **世界包围盒 (World BBox):**
  * Size: '(188.440, 149.880, 400.080)'
  * Center: '(-14.029, 26.804, 0.889)'

---

### /World/Conveyor_3

* **Prim路径 (Prim Path):**/World/Conveyor_3
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  *   [reference] '/media/simple/another_Documents/isaacsim_assets/assets/Simple_rubber_conveyor/Simple_rubber_conveyor.usdc'
* **世界包围盒 (World BBox):**
  * Size: '(188.440, 149.880, 400.080)'
  * Center: '(-9.029, 26.804, 0.889)'

---

### /World/Conveyor_4

* **Prim路径 (Prim Path):**/World/Conveyor_4
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  *   [reference] '/media/simple/another_Documents/isaacsim_assets/assets/Simple_rubber_conveyor/Simple_rubber_conveyor.usdc'
* **世界包围盒 (World BBox):**
  * Size: '(188.440, 149.880, 400.080)'
  * Center: '(-4.029, 26.804, 0.889)'

---

### /World/Conveyor_5

* **Prim路径 (Prim Path):**/World/Conveyor_5
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  *   [reference] '/media/simple/another_Documents/isaacsim_assets/assets/Simple_rubber_conveyor/Simple_rubber_conveyor.usdc'
* **世界包围盒 (World BBox):**
  * Size: '(188.440, 149.880, 400.080)'
  * Center: '(0.971, 26.804, 0.889)'

---

### /World/Conveyor_6

* **Prim路径 (Prim Path):**/World/Conveyor_6
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  *   [reference] '/media/simple/another_Documents/isaacsim_assets/assets/Simple_rubber_conveyor/Simple_rubber_conveyor.usdc'
* **世界包围盒 (World BBox):**
  * Size: '(188.440, 149.880, 400.080)'
  * Center: '(5.971, 26.804, 0.889)'

---

### /World/Conveyor_7

* **Prim路径 (Prim Path):**/World/Conveyor_7
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  *   [reference] '/media/simple/another_Documents/isaacsim_assets/assets/Simple_rubber_conveyor/Simple_rubber_conveyor.usdc'
* **世界包围盒 (World BBox):**
  * Size: '(188.440, 149.880, 400.080)'
  * Center: '(10.971, 26.804, 0.889)'

---

### /World/Conveyor_8

* **Prim路径 (Prim Path):**/World/Conveyor_8
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  *   [reference] '/media/simple/another_Documents/isaacsim_assets/assets/Simple_rubber_conveyor/Simple_rubber_conveyor.usdc'
* **世界包围盒 (World BBox):**
  * Size: '(188.440, 149.880, 400.080)'
  * Center: '(15.971, 26.804, 0.889)'

---

### /World/BoxOnConveyor_1

* **Prim路径 (Prim Path):**/World/BoxOnConveyor_1
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  *   [reference] '/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc'
* **世界包围盒 (World BBox):**
  * Size: '(35.888, 35.888, 35.888)'
  * Center: '(-19.000, 25.600, 1.751)'

---

### /World/BoxOnConveyor_2

* **Prim路径 (Prim Path):**/World/BoxOnConveyor_2
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  *   [reference] '/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc'
* **世界包围盒 (World BBox):**
  * Size: '(35.888, 35.888, 35.888)'
  * Center: '(-14.000, 25.600, 1.751)'

---

### /World/BoxOnConveyor_3

* **Prim路径 (Prim Path):**/World/BoxOnConveyor_3
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  *   [reference] '/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc'
* **世界包围盒 (World BBox):**
  * Size: '(35.888, 35.888, 35.888)'
  * Center: '(-9.000, 25.600, 1.751)'

---

### /World/BoxOnConveyor_4

* **Prim路径 (Prim Path):**/World/BoxOnConveyor_4
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  *   [reference] '/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc'
* **世界包围盒 (World BBox):**
  * Size: '(35.888, 35.888, 35.888)'
  * Center: '(-4.000, 25.600, 1.751)'

---

### /World/BoxOnConveyor_5

* **Prim路径 (Prim Path):**/World/BoxOnConveyor_5
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  *   [reference] '/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc'
* **世界包围盒 (World BBox):**
  * Size: '(35.888, 35.888, 35.888)'
  * Center: '(1.000, 25.600, 1.751)'

---

### /World/BoxOnConveyor_6

* **Prim路径 (Prim Path):**/World/BoxOnConveyor_6
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  *   [reference] '/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc'
* **世界包围盒 (World BBox):**
  * Size: '(35.888, 35.888, 35.888)'
  * Center: '(6.000, 25.600, 1.751)'

---

### /World/BoxOnConveyor_7

* **Prim路径 (Prim Path):**/World/BoxOnConveyor_7
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  *   [reference] '/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc'
* **世界包围盒 (World BBox):**
  * Size: '(35.888, 35.888, 35.888)'
  * Center: '(11.000, 25.600, 1.751)'

---

### /World/BoxOnConveyor_8

* **Prim路径 (Prim Path):**/World/BoxOnConveyor_8
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  *   [reference] '/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc'
* **世界包围盒 (World BBox):**
  * Size: '(35.888, 35.888, 35.888)'
  * Center: '(16.000, 25.600, 1.751)'

---

### /World/BoxOnConveyor_1_1

* **Prim路径 (Prim Path):**/World/BoxOnConveyor_1_1
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  *   [reference] '/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc'
* **世界包围盒 (World BBox):**
  * Size: '(35.888, 35.888, 35.888)'
  * Center: '(-19.000, 26.500, 1.751)'

---

### /World/BoxOnConveyor_1_2

* **Prim路径 (Prim Path):**/World/BoxOnConveyor_1_2
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  *   [reference] '/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc'
* **世界包围盒 (World BBox):**
  * Size: '(35.888, 35.888, 35.888)'
  * Center: '(-14.000, 26.500, 1.751)'

---

### /World/BoxOnConveyor_1_3

* **Prim路径 (Prim Path):**/World/BoxOnConveyor_1_3
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  *   [reference] '/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc'
* **世界包围盒 (World BBox):**
  * Size: '(35.888, 35.888, 35.888)'
  * Center: '(-9.000, 26.500, 1.751)'

---

### /World/BoxOnConveyor_1_4

* **Prim路径 (Prim Path):**/World/BoxOnConveyor_1_4
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  *   [reference] '/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc'
* **世界包围盒 (World BBox):**
  * Size: '(35.888, 35.888, 35.888)'
  * Center: '(-4.000, 26.500, 1.751)'

---

### /World/BoxOnConveyor_1_5

* **Prim路径 (Prim Path):**/World/BoxOnConveyor_1_5
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  *   [reference] '/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc'
* **世界包围盒 (World BBox):**
  * Size: '(35.888, 35.888, 35.888)'
  * Center: '(1.000, 26.500, 1.751)'

---

### /World/BoxOnConveyor_1_6

* **Prim路径 (Prim Path):**/World/BoxOnConveyor_1_6
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  *   [reference] '/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc'
* **世界包围盒 (World BBox):**
  * Size: '(35.888, 35.888, 35.888)'
  * Center: '(6.000, 26.500, 1.751)'

---

### /World/BoxOnConveyor_1_7

* **Prim路径 (Prim Path):**/World/BoxOnConveyor_1_7
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  *   [reference] '/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc'
* **世界包围盒 (World BBox):**
  * Size: '(35.888, 35.888, 35.888)'
  * Center: '(11.000, 26.500, 1.751)'

---

### /World/BoxOnConveyor_1_8

* **Prim路径 (Prim Path):**/World/BoxOnConveyor_1_8
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  *   [reference] '/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc'
* **世界包围盒 (World BBox):**
  * Size: '(35.888, 35.888, 35.888)'
  * Center: '(16.000, 26.500, 1.751)'

---

### /World/BoxOnConveyor_2_1

* **Prim路径 (Prim Path):**/World/BoxOnConveyor_2_1
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  *   [reference] '/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc'
* **世界包围盒 (World BBox):**
  * Size: '(35.888, 35.888, 35.888)'
  * Center: '(-19.000, 27.400, 1.751)'

---

### /World/BoxOnConveyor_2_2

* **Prim路径 (Prim Path):**/World/BoxOnConveyor_2_2
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  *   [reference] '/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc'
* **世界包围盒 (World BBox):**
  * Size: '(35.888, 35.888, 35.888)'
  * Center: '(-14.000, 27.400, 1.751)'

---

### /World/BoxOnConveyor_2_3

* **Prim路径 (Prim Path):**/World/BoxOnConveyor_2_3
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  *   [reference] '/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc'
* **世界包围盒 (World BBox):**
  * Size: '(35.888, 35.888, 35.888)'
  * Center: '(-9.000, 27.400, 1.751)'

---

### /World/BoxOnConveyor_2_4

* **Prim路径 (Prim Path):**/World/BoxOnConveyor_2_4
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  *   [reference] '/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc'
* **世界包围盒 (World BBox):**
  * Size: '(35.888, 35.888, 35.888)'
  * Center: '(-4.000, 27.400, 1.751)'

---

### /World/BoxOnConveyor_2_5

* **Prim路径 (Prim Path):**/World/BoxOnConveyor_2_5
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  *   [reference] '/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc'
* **世界包围盒 (World BBox):**
  * Size: '(35.888, 35.888, 35.888)'
  * Center: '(1.000, 27.400, 1.751)'

---

### /World/BoxOnConveyor_2_6

* **Prim路径 (Prim Path):**/World/BoxOnConveyor_2_6
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  *   [reference] '/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc'
* **世界包围盒 (World BBox):**
  * Size: '(35.888, 35.888, 35.888)'
  * Center: '(6.000, 27.400, 1.751)'

---

### /World/BoxOnConveyor_2_7

* **Prim路径 (Prim Path):**/World/BoxOnConveyor_2_7
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  *   [reference] '/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc'
* **世界包围盒 (World BBox):**
  * Size: '(35.888, 35.888, 35.888)'
  * Center: '(11.000, 27.400, 1.751)'

---

### /World/BoxOnConveyor_2_8

* **Prim路径 (Prim Path):**/World/BoxOnConveyor_2_8
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  *   [reference] '/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc'
* **世界包围盒 (World BBox):**
  * Size: '(35.888, 35.888, 35.888)'
  * Center: '(16.000, 27.400, 1.751)'

---

### /World/BoxOnConveyor_3_1

* **Prim路径 (Prim Path):**/World/BoxOnConveyor_3_1
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  *   [reference] '/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc'
* **世界包围盒 (World BBox):**
  * Size: '(35.888, 35.888, 35.888)'
  * Center: '(-19.000, 28.300, 1.751)'

---

### /World/BoxOnConveyor_3_2

* **Prim路径 (Prim Path):**/World/BoxOnConveyor_3_2
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  *   [reference] '/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc'
* **世界包围盒 (World BBox):**
  * Size: '(35.888, 35.888, 35.888)'
  * Center: '(-14.000, 28.300, 1.751)'

---

### /World/BoxOnConveyor_3_3

* **Prim路径 (Prim Path):**/World/BoxOnConveyor_3_3
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  *   [reference] '/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc'
* **世界包围盒 (World BBox):**
  * Size: '(35.888, 35.888, 35.888)'
  * Center: '(-9.000, 28.300, 1.751)'

---

### /World/BoxOnConveyor_3_4

* **Prim路径 (Prim Path):**/World/BoxOnConveyor_3_4
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  *   [reference] '/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc'
* **世界包围盒 (World BBox):**
  * Size: '(35.888, 35.888, 35.888)'
  * Center: '(-4.000, 28.300, 1.751)'

---

### /World/BoxOnConveyor_3_5

* **Prim路径 (Prim Path):**/World/BoxOnConveyor_3_5
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  *   [reference] '/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc'
* **世界包围盒 (World BBox):**
  * Size: '(35.888, 35.888, 35.888)'
  * Center: '(1.000, 28.300, 1.751)'

---

### /World/BoxOnConveyor_3_6

* **Prim路径 (Prim Path):**/World/BoxOnConveyor_3_6
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  *   [reference] '/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc'
* **世界包围盒 (World BBox):**
  * Size: '(35.888, 35.888, 35.888)'
  * Center: '(6.000, 28.300, 1.751)'

---

### /World/BoxOnConveyor_3_7

* **Prim路径 (Prim Path):**/World/BoxOnConveyor_3_7
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  *   [reference] '/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc'
* **世界包围盒 (World BBox):**
  * Size: '(35.888, 35.888, 35.888)'
  * Center: '(11.000, 28.300, 1.751)'

---

### /World/BoxOnConveyor_3_8

* **Prim路径 (Prim Path):**/World/BoxOnConveyor_3_8
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  *   [reference] '/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc'
* **世界包围盒 (World BBox):**
  * Size: '(35.888, 35.888, 35.888)'
  * Center: '(16.000, 28.300, 1.751)'

---

### /World/StackedCarton_1

* **Prim路径 (Prim Path):**/World/StackedCarton_1
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  *   [reference] '/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc'
* **世界包围盒 (World BBox):**
  * Size: '(35.888, 35.888, 35.888)'
  * Center: '(-18.800, 29.300, 0.631)'

---

### /World/StackedCarton_2

* **Prim路径 (Prim Path):**/World/StackedCarton_2
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  *   [reference] '/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc'
* **世界包围盒 (World BBox):**
  * Size: '(35.888, 35.888, 35.888)'
  * Center: '(-13.800, 29.300, 0.631)'

---

### /World/StackedCarton_3

* **Prim路径 (Prim Path):**/World/StackedCarton_3
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  *   [reference] '/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc'
* **世界包围盒 (World BBox):**
  * Size: '(35.888, 35.888, 35.888)'
  * Center: '(-8.800, 29.300, 0.631)'

---

### /World/StackedCarton_4

* **Prim路径 (Prim Path):**/World/StackedCarton_4
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  *   [reference] '/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc'
* **世界包围盒 (World BBox):**
  * Size: '(35.888, 35.888, 35.888)'
  * Center: '(-3.800, 29.300, 0.631)'

---

### /World/StackedCarton_5

* **Prim路径 (Prim Path):**/World/StackedCarton_5
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  *   [reference] '/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc'
* **世界包围盒 (World BBox):**
  * Size: '(35.888, 35.888, 35.888)'
  * Center: '(1.200, 29.300, 0.631)'

---

### /World/StackedCarton_6

* **Prim路径 (Prim Path):**/World/StackedCarton_6
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  *   [reference] '/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc'
* **世界包围盒 (World BBox):**
  * Size: '(35.888, 35.888, 35.888)'
  * Center: '(6.200, 29.300, 0.631)'

---

### /World/StackedCarton_7

* **Prim路径 (Prim Path):**/World/StackedCarton_7
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  *   [reference] '/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc'
* **世界包围盒 (World BBox):**
  * Size: '(35.888, 35.888, 35.888)'
  * Center: '(11.200, 29.300, 0.631)'

---

### /World/StackedCarton_8

* **Prim路径 (Prim Path):**/World/StackedCarton_8
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  *   [reference] '/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc'
* **世界包围盒 (World BBox):**
  * Size: '(35.888, 35.888, 35.888)'
  * Center: '(16.200, 29.300, 0.631)'

---

### /World/StackedCarton_1_1

* **Prim路径 (Prim Path):**/World/StackedCarton_1_1
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  *   [reference] '/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc'
* **世界包围盒 (World BBox):**
  * Size: '(35.888, 35.888, 35.888)'
  * Center: '(-18.800, 29.700, 0.631)'

---

### /World/StackedCarton_1_2

* **Prim路径 (Prim Path):**/World/StackedCarton_1_2
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  *   [reference] '/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc'
* **世界包围盒 (World BBox):**
  * Size: '(35.888, 35.888, 35.888)'
  * Center: '(-13.800, 29.700, 0.631)'

---

### /World/StackedCarton_1_3

* **Prim路径 (Prim Path):**/World/StackedCarton_1_3
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  *   [reference] '/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc'
* **世界包围盒 (World BBox):**
  * Size: '(35.888, 35.888, 35.888)'
  * Center: '(-8.800, 29.700, 0.631)'

---

### /World/StackedCarton_1_4

* **Prim路径 (Prim Path):**/World/StackedCarton_1_4
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  *   [reference] '/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc'
* **世界包围盒 (World BBox):**
  * Size: '(35.888, 35.888, 35.888)'
  * Center: '(-3.800, 29.700, 0.631)'

---

### /World/StackedCarton_1_5

* **Prim路径 (Prim Path):**/World/StackedCarton_1_5
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  *   [reference] '/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc'
* **世界包围盒 (World BBox):**
  * Size: '(35.888, 35.888, 35.888)'
  * Center: '(1.200, 29.700, 0.631)'

---

### /World/StackedCarton_1_6

* **Prim路径 (Prim Path):**/World/StackedCarton_1_6
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  *   [reference] '/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc'
* **世界包围盒 (World BBox):**
  * Size: '(35.888, 35.888, 35.888)'
  * Center: '(6.200, 29.700, 0.631)'

---

### /World/StackedCarton_1_7

* **Prim路径 (Prim Path):**/World/StackedCarton_1_7
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  *   [reference] '/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc'
* **世界包围盒 (World BBox):**
  * Size: '(35.888, 35.888, 35.888)'
  * Center: '(11.200, 29.700, 0.631)'

---

### /World/StackedCarton_1_8

* **Prim路径 (Prim Path):**/World/StackedCarton_1_8
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  *   [reference] '/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc'
* **世界包围盒 (World BBox):**
  * Size: '(35.888, 35.888, 35.888)'
  * Center: '(16.200, 29.700, 0.631)'

---

### /World/StackedCarton_2_1

* **Prim路径 (Prim Path):**/World/StackedCarton_2_1
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  *   [reference] '/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc'
* **世界包围盒 (World BBox):**
  * Size: '(35.888, 35.888, 35.888)'
  * Center: '(-18.800, 29.500, 0.996)'

---

### /World/StackedCarton_2_2

* **Prim路径 (Prim Path):**/World/StackedCarton_2_2
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  *   [reference] '/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc'
* **世界包围盒 (World BBox):**
  * Size: '(35.888, 35.888, 35.888)'
  * Center: '(-13.800, 29.500, 0.996)'

---

### /World/StackedCarton_2_3

* **Prim路径 (Prim Path):**/World/StackedCarton_2_3
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  *   [reference] '/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc'
* **世界包围盒 (World BBox):**
  * Size: '(35.888, 35.888, 35.888)'
  * Center: '(-8.800, 29.500, 0.996)'

---

### /World/StackedCarton_2_4

* **Prim路径 (Prim Path):**/World/StackedCarton_2_4
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  *   [reference] '/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc'
* **世界包围盒 (World BBox):**
  * Size: '(35.888, 35.888, 35.888)'
  * Center: '(-3.800, 29.500, 0.996)'

---

### /World/StackedCarton_2_5

* **Prim路径 (Prim Path):**/World/StackedCarton_2_5
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  *   [reference] '/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc'
* **世界包围盒 (World BBox):**
  * Size: '(35.888, 35.888, 35.888)'
  * Center: '(1.200, 29.500, 0.996)'

---

### /World/StackedCarton_2_6

* **Prim路径 (Prim Path):**/World/StackedCarton_2_6
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  *   [reference] '/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc'
* **世界包围盒 (World BBox):**
  * Size: '(35.888, 35.888, 35.888)'
  * Center: '(6.200, 29.500, 0.996)'

---

### /World/StackedCarton_2_7

* **Prim路径 (Prim Path):**/World/StackedCarton_2_7
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  *   [reference] '/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc'
* **世界包围盒 (World BBox):**
  * Size: '(35.888, 35.888, 35.888)'
  * Center: '(11.200, 29.500, 0.996)'

---

### /World/StackedCarton_2_8

* **Prim路径 (Prim Path):**/World/StackedCarton_2_8
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  *   [reference] '/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc'
* **世界包围盒 (World BBox):**
  * Size: '(35.888, 35.888, 35.888)'
  * Center: '(16.200, 29.500, 0.996)'

---

### /World/HeavyDutyPackingTable_A01_01

* **Prim路径 (Prim Path):**/World/HeavyDutyPackingTable_A01_01
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  *   [reference] '../device_data/usdz/Workbench/HeavyDutyPackingTable_A01_01.usdz'
* **世界包围盒 (World BBox):**
  * Size: '(186.690, 121.948, 99.405)'
  * Center: '(14.843, 29.361, 0.651)'

---

### /World/panda_instanceable1

* **Prim路径 (Prim Path):**/World/panda_instanceable1
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  *   [reference] '../device_data/usdz/IndustrialRobot/panda_instanceable1.usdz'
* **世界包围盒 (World BBox):**
  * Size: '(0.503, 0.389, 1.672)'
  * Center: '(15.146, 29.424, 1.981)'

---

### /World/panda_instanceable1/Group/panda_hand/visuals

* **Prim路径 (Prim Path):**/World/panda_instanceable1/Group/panda_hand/visuals
* **Prim类型 (Prim Type):**Xform
* **变换信息 (Transform):**
  * **平移 (Translate):**'(0.000, 0.000, 0.000)'
  * **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
  * **缩放 (Scale):**'(1.000, 1.000, 1.000)'
* **外部引用 (Referenced USD Files):**
  *   [reference] 'Reference 1'
  *   Prim Path: '/Flattened_Prototype_6'
* **世界包围盒 (World BBox):**
  * Size: '(0.063, 0.205, 0.092)'
  * Center: '(15.255, 29.425, 2.504)'

---

### /World/panda_instanceable1/Group/panda_hand/collisions

* **Prim路径 (Prim Path):**/World/panda_instanceable1/Group/panda_hand/collisions
* **Prim类型 (Prim Type):**Xform
* **变换信息 (Transform):**
  * **平移 (Translate):**'(0.000, 0.000, 0.000)'
  * **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
  * **缩放 (Scale):**'(1.000, 1.000, 1.000)'
* **外部引用 (Referenced USD Files):**
  *   [reference] 'Reference 1'
  *   Prim Path: '/Flattened_Prototype_13'
* **世界包围盒 (World BBox):**
  * Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
  * Center: '(15.257, 29.424, 2.534)'

---

### /World/panda_instanceable1/Group/panda_leftfinger/visuals

* **Prim路径 (Prim Path):**/World/panda_instanceable1/Group/panda_leftfinger/visuals
* **Prim类型 (Prim Type):**Xform
* **变换信息 (Transform):**
  * **平移 (Translate):**'(0.000, 0.000, 0.000)'
  * **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
  * **缩放 (Scale):**'(1.000, 1.000, 1.000)'
* **外部引用 (Referenced USD Files):**
  *   [reference] 'Reference 1'
  *   Prim Path: '/Flattened_Prototype_2'
* **世界包围盒 (World BBox):**
  * Size: '(0.021, 0.026, 0.054)'
  * Center: '(15.271, 29.410, 2.406)'

---

### /World/panda_instanceable1/Group/panda_leftfinger/collisions

* **Prim路径 (Prim Path):**/World/panda_instanceable1/Group/panda_leftfinger/collisions
* **Prim类型 (Prim Type):**Xform
* **变换信息 (Transform):**
  * **平移 (Translate):**'(0.000, 0.000, 0.000)'
  * **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
  * **缩放 (Scale):**'(1.000, 1.000, 1.000)'
* **外部引用 (Referenced USD Files):**
  *   [reference] 'Reference 1'
  *   Prim Path: '/Flattened_Prototype_22'
* **世界包围盒 (World BBox):**
  * Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
  * Center: '(15.257, 29.424, 2.446)'

---

### /World/panda_instanceable1/Group/panda_link0/visuals

* **Prim路径 (Prim Path):**/World/panda_instanceable1/Group/panda_link0/visuals
* **Prim类型 (Prim Type):**Xform
* **变换信息 (Transform):**
  * **平移 (Translate):**'(0.000, 0.000, 0.000)'
  * **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
  * **缩放 (Scale):**'(1.000, 1.000, 1.000)'
* **外部引用 (Referenced USD Files):**
  *   [reference] 'Reference 1'
  *   Prim Path: '/Flattened_Prototype_5'
* **世界包围盒 (World BBox):**
  * Size: '(0.226, 0.189, 0.140)'
  * Center: '(15.063, 29.423, 1.250)'

---

### /World/panda_instanceable1/Group/panda_link0/collisions

* **Prim路径 (Prim Path):**/World/panda_instanceable1/Group/panda_link0/collisions
* **Prim类型 (Prim Type):**Xform
* **变换信息 (Transform):**
  * **平移 (Translate):**'(0.000, 0.000, 0.000)'
  * **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
  * **缩放 (Scale):**'(1.000, 1.000, 1.000)'
* **外部引用 (Referenced USD Files):**
  *   [reference] 'Reference 1'
  *   Prim Path: '/Flattened_Prototype_19'
* **世界包围盒 (World BBox):**
  * Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
  * Center: '(15.125, 29.424, 1.145)'

---

### /World/panda_instanceable1/Group/panda_link1/visuals

* **Prim路径 (Prim Path):**/World/panda_instanceable1/Group/panda_link1/visuals
* **Prim类型 (Prim Type):**Xform
* **变换信息 (Transform):**
  * **平移 (Translate):**'(0.000, 0.000, 0.000)'
  * **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
  * **缩放 (Scale):**'(1.000, 1.000, 1.000)'
* **外部引用 (Referenced USD Files):**
  *   [reference] 'Reference 1'
  *   Prim Path: '/Flattened_Prototype_16'
* **世界包围盒 (World BBox):**
  * Size: '(0.110, 0.184, 0.247)'
  * Center: '(15.125, 29.368, 1.541)'

---

### /World/panda_instanceable1/Group/panda_link1/collisions

* **Prim路径 (Prim Path):**/World/panda_instanceable1/Group/panda_link1/collisions
* **Prim类型 (Prim Type):**Xform
* **变换信息 (Transform):**
  * **平移 (Translate):**'(0.000, 0.000, 0.000)'
  * **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
  * **缩放 (Scale):**'(1.000, 1.000, 1.000)'
* **外部引用 (Referenced USD Files):**
  *   [reference] 'Reference 1'
  *   Prim Path: '/Flattened_Prototype_18'
* **世界包围盒 (World BBox):**
  * Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
  * Center: '(15.125, 29.424, 1.644)'

---

### /World/panda_instanceable1/Group/panda_link2/visuals

* **Prim路径 (Prim Path):**/World/panda_instanceable1/Group/panda_link2/visuals
* **Prim类型 (Prim Type):**Xform
* **变换信息 (Transform):**
  * **平移 (Translate):**'(0.000, 0.000, 0.000)'
  * **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
  * **缩放 (Scale):**'(1.000, 1.000, 1.000)'
* **外部引用 (Referenced USD Files):**
  *   [reference] 'Reference 1'
  *   Prim Path: '/Flattened_Prototype_1'
* **世界包围盒 (World BBox):**
  * Size: '(0.110, 0.249, 0.184)'
  * Center: '(15.125, 29.479, 1.749)'

---

### /World/panda_instanceable1/Group/panda_link2/collisions

* **Prim路径 (Prim Path):**/World/panda_instanceable1/Group/panda_link2/collisions
* **Prim类型 (Prim Type):**Xform
* **变换信息 (Transform):**
  * **平移 (Translate):**'(0.000, 0.000, 0.000)'
  * **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
  * **缩放 (Scale):**'(1.000, 1.000, 1.000)'
* **外部引用 (Referenced USD Files):**
  *   [reference] 'Reference 1'
  *   Prim Path: '/Flattened_Prototype_12'
* **世界包围盒 (World BBox):**
  * Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
  * Center: '(15.125, 29.424, 1.644)'

---

### /World/panda_instanceable1/Group/panda_link3/visuals

* **Prim路径 (Prim Path):**/World/panda_instanceable1/Group/panda_link3/visuals
* **Prim类型 (Prim Type):**Xform
* **变换信息 (Transform):**
  * **平移 (Translate):**'(0.000, 0.000, 0.000)'
  * **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
  * **缩放 (Scale):**'(1.000, 1.000, 1.000)'
* **外部引用 (Referenced USD Files):**
  *   [reference] 'Reference 1'
  *   Prim Path: '/Flattened_Prototype_14'
* **世界包围盒 (World BBox):**
  * Size: '(0.193, 0.166, 0.176)'
  * Center: '(15.187, 29.466, 2.069)'

---

### /World/panda_instanceable1/Group/panda_link3/collisions

* **Prim路径 (Prim Path):**/World/panda_instanceable1/Group/panda_link3/collisions
* **Prim类型 (Prim Type):**Xform
* **变换信息 (Transform):**
  * **平移 (Translate):**'(0.000, 0.000, 0.000)'
  * **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
  * **缩放 (Scale):**'(1.000, 1.000, 1.000)'
* **外部引用 (Referenced USD Files):**
  *   [reference] 'Reference 1'
  *   Prim Path: '/Flattened_Prototype_15'
* **世界包围盒 (World BBox):**
  * Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
  * Center: '(15.125, 29.424, 2.118)'

---

### /World/panda_instanceable1/Group/panda_link4/visuals

* **Prim路径 (Prim Path):**/World/panda_instanceable1/Group/panda_link4/visuals
* **Prim类型 (Prim Type):**Xform
* **变换信息 (Transform):**
  * **平移 (Translate):**'(0.000, 0.000, 0.000)'
  * **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
  * **缩放 (Scale):**'(1.000, 1.000, 1.000)'
* **外部引用 (Referenced USD Files):**
  *   [reference] 'Reference 1'
  *   Prim Path: '/Flattened_Prototype_8'
* **世界包围盒 (World BBox):**
  * Size: '(0.193, 0.179, 0.166)'
  * Center: '(15.187, 29.382, 2.170)'

---

### /World/panda_instanceable1/Group/panda_link4/collisions

* **Prim路径 (Prim Path):**/World/panda_instanceable1/Group/panda_link4/collisions
* **Prim类型 (Prim Type):**Xform
* **变换信息 (Transform):**
  * **平移 (Translate):**'(0.000, 0.000, 0.000)'
  * **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
  * **缩放 (Scale):**'(1.000, 1.000, 1.000)'
* **外部引用 (Referenced USD Files):**
  *   [reference] 'Reference 1'
  *   Prim Path: '/Flattened_Prototype_3'
* **世界包围盒 (World BBox):**
  * Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
  * Center: '(15.249, 29.424, 2.118)'

---

### /World/panda_instanceable1/Group/panda_link5/visuals

* **Prim路径 (Prim Path):**/World/panda_instanceable1/Group/panda_link5/visuals
* **Prim类型 (Prim Type):**Xform
* **变换信息 (Transform):**
  * **平移 (Translate):**'(0.000, 0.000, 0.000)'
  * **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
  * **缩放 (Scale):**'(1.000, 1.000, 1.000)'
* **外部引用 (Referenced USD Files):**
  *   [reference] 'Reference 1'
  *   Prim Path: '/Flattened_Prototype_10'
* **世界包围盒 (World BBox):**
  * Size: '(0.110, 0.185, 0.311)'
  * Center: '(15.125, 29.480, 2.539)'

---

### /World/panda_instanceable1/Group/panda_link5/collisions

* **Prim路径 (Prim Path):**/World/panda_instanceable1/Group/panda_link5/collisions
* **Prim类型 (Prim Type):**Xform
* **变换信息 (Transform):**
  * **平移 (Translate):**'(0.000, 0.000, 0.000)'
  * **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
  * **缩放 (Scale):**'(1.000, 1.000, 1.000)'
* **外部引用 (Referenced USD Files):**
  *   [reference] 'Reference 1'
  *   Prim Path: '/Flattened_Prototype_4'
* **世界包围盒 (World BBox):**
  * Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
  * Center: '(15.125, 29.424, 2.694)'

---

### /World/panda_instanceable1/Group/panda_link6/visuals

* **Prim路径 (Prim Path):**/World/panda_instanceable1/Group/panda_link6/visuals
* **Prim类型 (Prim Type):**Xform
* **变换信息 (Transform):**
  * **平移 (Translate):**'(0.000, 0.000, 0.000)'
  * **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
  * **缩放 (Scale):**'(1.000, 1.000, 1.000)'
* **外部引用 (Referenced USD Files):**
  *   [reference] 'Reference 1'
  *   Prim Path: '/Flattened_Prototype_9'
* **世界包围盒 (World BBox):**
  * Size: '(0.180, 0.133, 0.100)'
  * Center: '(15.188, 29.414, 2.717)'

---

### /World/panda_instanceable1/Group/panda_link6/collisions

* **Prim路径 (Prim Path):**/World/panda_instanceable1/Group/panda_link6/collisions
* **Prim类型 (Prim Type):**Xform
* **变换信息 (Transform):**
  * **平移 (Translate):**'(0.000, 0.000, 0.000)'
  * **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
  * **缩放 (Scale):**'(1.000, 1.000, 1.000)'
* **外部引用 (Referenced USD Files):**
  *   [reference] 'Reference 1'
  *   Prim Path: '/Flattened_Prototype_11'
* **世界包围盒 (World BBox):**
  * Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
  * Center: '(15.125, 29.424, 2.694)'

---

### /World/panda_instanceable1/Group/panda_link7/visuals

* **Prim路径 (Prim Path):**/World/panda_instanceable1/Group/panda_link7/visuals
* **Prim类型 (Prim Type):**Xform
* **变换信息 (Transform):**
  * **平移 (Translate):**'(0.000, 0.000, 0.000)'
  * **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
  * **缩放 (Scale):**'(1.000, 1.000, 1.000)'
* **外部引用 (Referenced USD Files):**
  *   [reference] 'Reference 1'
  *   Prim Path: '/Flattened_Prototype_17'
* **世界包围盒 (World BBox):**
  * Size: '(0.125, 0.125, 0.055)'
  * Center: '(15.285, 29.396, 2.575)'

---

### /World/panda_instanceable1/Group/panda_link7/collisions

* **Prim路径 (Prim Path):**/World/panda_instanceable1/Group/panda_link7/collisions
* **Prim类型 (Prim Type):**Xform
* **变换信息 (Transform):**
  * **平移 (Translate):**'(0.000, 0.000, 0.000)'
  * **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
  * **缩放 (Scale):**'(1.000, 1.000, 1.000)'
* **外部引用 (Referenced USD Files):**
  *   [reference] 'Reference 1'
  *   Prim Path: '/Flattened_Prototype_21'
* **世界包围盒 (World BBox):**
  * Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
  * Center: '(15.257, 29.424, 2.694)'

---

### /World/panda_instanceable1/Group/panda_rightfinger/visuals

* **Prim路径 (Prim Path):**/World/panda_instanceable1/Group/panda_rightfinger/visuals
* **Prim类型 (Prim Type):**Xform
* **变换信息 (Transform):**
  * **平移 (Translate):**'(0.000, 0.000, 0.000)'
  * **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
  * **缩放 (Scale):**'(1.000, 1.000, 1.000)'
* **外部引用 (Referenced USD Files):**
  *   [reference] 'Reference 1'
  *   Prim Path: '/Flattened_Prototype_7'
* **世界包围盒 (World BBox):**
  * Size: '(0.021, 0.026, 0.054)'
  * Center: '(15.243, 29.437, 2.406)'

---

### /World/panda_instanceable1/Group/panda_rightfinger/collisions

* **Prim路径 (Prim Path):**/World/panda_instanceable1/Group/panda_rightfinger/collisions
* **Prim类型 (Prim Type):**Xform
* **变换信息 (Transform):**
  * **平移 (Translate):**'(0.000, 0.000, 0.000)'
  * **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
  * **缩放 (Scale):**'(1.000, 1.000, 1.000)'
* **外部引用 (Referenced USD Files):**
  *   [reference] 'Reference 1'
  *   Prim Path: '/Flattened_Prototype_20'
* **世界包围盒 (World BBox):**
  * Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
  * Center: '(15.257, 29.424, 2.446)'

---

## 4. 材质库 (Material Library)

### /World/Physics_Materials/physics_material

* **Prim路径 (Prim Path):**/World/Physics_Materials/physics_material
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'

---

### /World/Looks/visual_material

* **Prim路径 (Prim Path):**/World/Looks/visual_material
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/Looks/visual_material/shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Looks/visual_material/shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [float3] = '(0.000, 0.000, 0.000)'

---

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

### /World/agv_7/Materials/ASELSAN_CATS_04

* **Prim路径 (Prim Path):**/World/agv_7/Materials/ASELSAN_CATS_04
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_7/Materials/ASELSAN_CATS_04/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_7/Materials/ASELSAN_CATS_04/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.158, 0.158, 0.158)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_7/Materials/ASELSAN_CATS_04_2

* **Prim路径 (Prim Path):**/World/agv_7/Materials/ASELSAN_CATS_04_2
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_7/Materials/ASELSAN_CATS_04_2/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_7/Materials/ASELSAN_CATS_04_2/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.769, 0.773, 0.749)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_7/Materials/ASELSAN_CATS_13

* **Prim路径 (Prim Path):**/World/agv_7/Materials/ASELSAN_CATS_13
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_7/Materials/ASELSAN_CATS_13/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_7/Materials/ASELSAN_CATS_13/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.706, 0.718, 0.729)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_7/Materials/Color_000

* **Prim路径 (Prim Path):**/World/agv_7/Materials/Color_000
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_7/Materials/Color_000/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_7/Materials/Color_000/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(1.000, 1.000, 1.000)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_7/Materials/Color_A05

* **Prim路径 (Prim Path):**/World/agv_7/Materials/Color_A05
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_7/Materials/Color_A05/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_7/Materials/Color_A05/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(1.000, 0.000, 0.000)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0.959234'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0'

---

### /World/agv_7/Materials/Color_A06

* **Prim路径 (Prim Path):**/World/agv_7/Materials/Color_A06
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_7/Materials/Color_A06/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_7/Materials/Color_A06/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.800, 0.000, 0.000)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_7/Materials/Color_B05

* **Prim路径 (Prim Path):**/World/agv_7/Materials/Color_B05
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_7/Materials/Color_B05/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_7/Materials/Color_B05/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(1.000, 0.247, 0.000)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '1'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0'

---

### /World/agv_7/Materials/Color_E02

* **Prim路径 (Prim Path):**/World/agv_7/Materials/Color_E02
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_7/Materials/Color_E02/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_7/Materials/Color_E02/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(1.000, 1.000, 0.196)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_7/Materials/Color_E05

* **Prim路径 (Prim Path):**/World/agv_7/Materials/Color_E05
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_7/Materials/Color_E05/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_7/Materials/Color_E05/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(1.000, 0.910, 0.000)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0.625455'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0.133891'

---

### /World/agv_7/Materials/Color_F06

* **Prim路径 (Prim Path):**/World/agv_7/Materials/Color_F06
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_7/Materials/Color_F06/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_7/Materials/Color_F06/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.400, 0.800, 0.000)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_7/Materials/Color_G03

* **Prim路径 (Prim Path):**/World/agv_7/Materials/Color_G03
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_7/Materials/Color_G03/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_7/Materials/Color_G03/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.396, 1.000, 0.396)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_7/Materials/Color_M02

* **Prim路径 (Prim Path):**/World/agv_7/Materials/Color_M02
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_7/Materials/Color_M02/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_7/Materials/Color_M02/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.776, 0.776, 0.776)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_7/Materials/Color_M03

* **Prim路径 (Prim Path):**/World/agv_7/Materials/Color_M03
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_7/Materials/Color_M03/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_7/Materials/Color_M03/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.667, 0.667, 0.667)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_7/Materials/Mtl39

* **Prim路径 (Prim Path):**/World/agv_7/Materials/Mtl39
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_7/Materials/Mtl39/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_7/Materials/Mtl39/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.494, 0.494, 0.494)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_7/Materials/Mtl6

* **Prim路径 (Prim Path):**/World/agv_7/Materials/Mtl6
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_7/Materials/Mtl6/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_7/Materials/Mtl6/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f]
        * Connected: '/World/agv_7/Materials/Mtl6/tex_base.outputs:rgb' @ '/World/agv_7/Materials/Mtl6/tex_base'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/Mtl6_baseColor.jpg'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'
    * '/World/agv_7/Materials/Mtl6/tex_base' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/Mtl6_baseColor.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'file' [asset] = '0/Mtl6_baseColor.jpg'
      * 'st' [float2]
        * Connected: '/World/agv_7/Materials/Mtl6/uvset0.outputs:result' @ '/World/agv_7/Materials/Mtl6/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/agv_7/Materials/Mtl6/uvset0' (ID: 'UsdPrimvarReader_float2')
    * Implementation: 'id'

---

### /World/agv_7/Materials/Mtl9

* **Prim路径 (Prim Path):**/World/agv_7/Materials/Mtl9
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_7/Materials/Mtl9/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_7/Materials/Mtl9/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.514, 1.000, 0.000)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_7/Materials/Silver

* **Prim路径 (Prim Path):**/World/agv_7/Materials/Silver
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_7/Materials/Silver/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_7/Materials/Silver/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.753, 0.753, 0.753)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_7/Materials/material

* **Prim路径 (Prim Path):**/World/agv_7/Materials/material
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_7/Materials/material/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_7/Materials/material/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f]
        * Connected: '/World/agv_7/Materials/material/tex_base.outputs:rgb' @ '/World/agv_7/Materials/material/tex_base'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/material_baseColor.jpg'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'
    * '/World/agv_7/Materials/material/tex_base' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/material_baseColor.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'file' [asset] = '0/material_baseColor.jpg'
      * 'st' [float2]
        * Connected: '/World/agv_7/Materials/material/uvset0.outputs:result' @ '/World/agv_7/Materials/material/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/agv_7/Materials/material/uvset0' (ID: 'UsdPrimvarReader_float2')
    * Implementation: 'id'

---

### /World/agv_7/Materials/cash_register_keys

* **Prim路径 (Prim Path):**/World/agv_7/Materials/cash_register_keys
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_7/Materials/cash_register_keys/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_7/Materials/cash_register_keys/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.976, 0.992, 0.973)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_7/Materials/Chris_Shoe_Sole

* **Prim路径 (Prim Path):**/World/agv_7/Materials/Chris_Shoe_Sole
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_7/Materials/Chris_Shoe_Sole/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_7/Materials/Chris_Shoe_Sole/pbr_shader' (ID: 'UsdPreviewSurface')
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

### /World/agv_7/Materials/Color_002

* **Prim路径 (Prim Path):**/World/agv_7/Materials/Color_002
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_7/Materials/Color_002/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_7/Materials/Color_002/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.217, 0.217, 0.217)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0.570837'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0'

---

### /World/agv_7/Materials/Color_005

* **Prim路径 (Prim Path):**/World/agv_7/Materials/Color_005
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_7/Materials/Color_005/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_7/Materials/Color_005/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.130, 0.130, 0.130)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0.710417'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0'

---

### /World/agv_7/Materials/Color_006

* **Prim路径 (Prim Path):**/World/agv_7/Materials/Color_006
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_7/Materials/Color_006/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_7/Materials/Color_006/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0.237059'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0'

---

### /World/agv_7/Materials/Color_008

* **Prim路径 (Prim Path):**/World/agv_7/Materials/Color_008
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_7/Materials/Color_008/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_7/Materials/Color_008/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.118, 0.118, 0.118)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0.941027'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0'

---

### /World/agv_7/Materials/Color_A01

* **Prim路径 (Prim Path):**/World/agv_7/Materials/Color_A01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_7/Materials/Color_A01/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_7/Materials/Color_A01/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(1.000, 0.000, 0.000)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0.965302'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0'

---

### /World/agv_7/Materials/Color_A11

* **Prim路径 (Prim Path):**/World/agv_7/Materials/Color_A11
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_7/Materials/Color_A11/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_7/Materials/Color_A11/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.600, 0.000, 0.000)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_7/Materials/Color_M04

* **Prim路径 (Prim Path):**/World/agv_7/Materials/Color_M04
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_7/Materials/Color_M04/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_7/Materials/Color_M04/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.557, 0.557, 0.557)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_7/Materials/Color_M05

* **Prim路径 (Prim Path):**/World/agv_7/Materials/Color_M05
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_7/Materials/Color_M05/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_7/Materials/Color_M05/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.447, 0.447, 0.447)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_7/Materials/Color_M06

* **Prim路径 (Prim Path):**/World/agv_7/Materials/Color_M06
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_7/Materials/Color_M06/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_7/Materials/Color_M06/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_7/Materials/Color_M07

* **Prim路径 (Prim Path):**/World/agv_7/Materials/Color_M07
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_7/Materials/Color_M07/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_7/Materials/Color_M07/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.227, 0.227, 0.227)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_7/Materials/Color_M09

* **Prim路径 (Prim Path):**/World/agv_7/Materials/Color_M09
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_7/Materials/Color_M09/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_7/Materials/Color_M09/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0.340226'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0.085341'

---

### /World/agv_7/Materials/FCP_Charcoal_v2

* **Prim路径 (Prim Path):**/World/agv_7/Materials/FCP_Charcoal_v2
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_7/Materials/FCP_Charcoal_v2/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_7/Materials/FCP_Charcoal_v2/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.216, 0.216, 0.216)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_7/Materials/FrontColor

* **Prim路径 (Prim Path):**/World/agv_7/Materials/FrontColor
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_7/Materials/FrontColor/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_7/Materials/FrontColor/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.504, 0.504, 0.504)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0.637593'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0.218852'

---

### /World/agv_7/Materials/Light_Blue

* **Prim路径 (Prim Path):**/World/agv_7/Materials/Light_Blue
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_7/Materials/Light_Blue/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_7/Materials/Light_Blue/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.601, 0.601, 0.601)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '1'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0.170303'

---

### /World/agv_7/Materials/M_0011_Seashell

* **Prim路径 (Prim Path):**/World/agv_7/Materials/M_0011_Seashell
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_7/Materials/M_0011_Seashell/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_7/Materials/M_0011_Seashell/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(1.000, 0.961, 0.933)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_7/Materials/M_0131_Silver

* **Prim路径 (Prim Path):**/World/agv_7/Materials/M_0131_Silver
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_7/Materials/M_0131_Silver/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_7/Materials/M_0131_Silver/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.242, 0.242, 0.242)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0.613318'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0'

---

### /World/agv_7/Materials/M_0134_DimGray

* **Prim路径 (Prim Path):**/World/agv_7/Materials/M_0134_DimGray
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_7/Materials/M_0134_DimGray/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_7/Materials/M_0134_DimGray/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.412, 0.412, 0.412)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_7/Materials/M_0135_DarkGray

* **Prim路径 (Prim Path):**/World/agv_7/Materials/M_0135_DarkGray
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_7/Materials/M_0135_DarkGray/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_7/Materials/M_0135_DarkGray/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.318, 0.318, 0.318)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_7/Materials/Metal_Silver

* **Prim路径 (Prim Path):**/World/agv_7/Materials/Metal_Silver
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_7/Materials/Metal_Silver/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_7/Materials/Metal_Silver/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.918, 0.914, 0.933)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_7/Materials/Mtl1

* **Prim路径 (Prim Path):**/World/agv_7/Materials/Mtl1
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_7/Materials/Mtl1/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_7/Materials/Mtl1/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.015, 0.015, 0.015)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0.255265'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_7/Materials/Mtl10

* **Prim路径 (Prim Path):**/World/agv_7/Materials/Mtl10
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_7/Materials/Mtl10/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_7/Materials/Mtl10/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.322, 0.322, 0.322)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_7/Materials/Mtl11

* **Prim路径 (Prim Path):**/World/agv_7/Materials/Mtl11
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_7/Materials/Mtl11/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_7/Materials/Mtl11/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.067, 0.757, 0.329)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_7/Materials/Mtl12

* **Prim路径 (Prim Path):**/World/agv_7/Materials/Mtl12
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_7/Materials/Mtl12/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_7/Materials/Mtl12/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.502, 0.502, 0.502)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_7/Materials/Mtl13

* **Prim路径 (Prim Path):**/World/agv_7/Materials/Mtl13
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_7/Materials/Mtl13/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_7/Materials/Mtl13/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.008, 0.514, 0.816)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_7/Materials/Mtl14

* **Prim路径 (Prim Path):**/World/agv_7/Materials/Mtl14
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_7/Materials/Mtl14/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_7/Materials/Mtl14/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.310, 0.310, 0.310)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_7/Materials/Mtl15

* **Prim路径 (Prim Path):**/World/agv_7/Materials/Mtl15
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_7/Materials/Mtl15/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_7/Materials/Mtl15/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.263, 0.275, 0.275)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_7/Materials/Mtl16

* **Prim路径 (Prim Path):**/World/agv_7/Materials/Mtl16
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_7/Materials/Mtl16/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_7/Materials/Mtl16/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.698, 0.698, 0.000)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_7/Materials/Mtl17

* **Prim路径 (Prim Path):**/World/agv_7/Materials/Mtl17
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_7/Materials/Mtl17/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_7/Materials/Mtl17/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.000, 0.863, 1.000)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_7/Materials/Mtl3

* **Prim路径 (Prim Path):**/World/agv_7/Materials/Mtl3
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_7/Materials/Mtl3/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_7/Materials/Mtl3/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.431, 0.455, 0.498)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_7/Materials/Mtl35

* **Prim路径 (Prim Path):**/World/agv_7/Materials/Mtl35
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_7/Materials/Mtl35/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_7/Materials/Mtl35/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.792, 0.820, 0.933)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_7/Materials/Mtl36

* **Prim路径 (Prim Path):**/World/agv_7/Materials/Mtl36
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_7/Materials/Mtl36/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_7/Materials/Mtl36/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.667, 0.698, 0.765)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_7/Materials/Mtl37

* **Prim路径 (Prim Path):**/World/agv_7/Materials/Mtl37
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_7/Materials/Mtl37/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_7/Materials/Mtl37/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.098, 0.098, 0.098)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_7/Materials/Mtl3a

* **Prim路径 (Prim Path):**/World/agv_7/Materials/Mtl3a
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_7/Materials/Mtl3a/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_7/Materials/Mtl3a/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.388, 0.369, 0.322)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_7/Materials/Mtl3b

* **Prim路径 (Prim Path):**/World/agv_7/Materials/Mtl3b
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_7/Materials/Mtl3b/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_7/Materials/Mtl3b/pbr_shader' (ID: 'UsdPreviewSurface')
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

### /World/agv_7/Materials/Mtl5

* **Prim路径 (Prim Path):**/World/agv_7/Materials/Mtl5
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_7/Materials/Mtl5/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_7/Materials/Mtl5/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.396, 0.408, 0.467)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_7/Materials/Mtl7

* **Prim路径 (Prim Path):**/World/agv_7/Materials/Mtl7
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_7/Materials/Mtl7/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_7/Materials/Mtl7/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.376, 0.376, 0.376)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_7/Materials/Mtl8

* **Prim路径 (Prim Path):**/World/agv_7/Materials/Mtl8
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_7/Materials/Mtl8/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_7/Materials/Mtl8/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.173, 0.173, 0.173)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_7/Materials/Mtla

* **Prim路径 (Prim Path):**/World/agv_7/Materials/Mtla
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_7/Materials/Mtla/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_7/Materials/Mtla/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.612, 0.725, 0.745)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_7/Materials/Mtlb1

* **Prim路径 (Prim Path):**/World/agv_7/Materials/Mtlb1
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_7/Materials/Mtlb1/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_7/Materials/Mtlb1/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.949, 0.925, 0.933)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_7/Materials/Stainless_Steel

* **Prim路径 (Prim Path):**/World/agv_7/Materials/Stainless_Steel
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_7/Materials/Stainless_Steel/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_7/Materials/Stainless_Steel/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.292, 0.294, 0.284)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0.431257'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_7/Materials/Metal_Aluminum_Anodized_1

* **Prim路径 (Prim Path):**/World/agv_7/Materials/Metal_Aluminum_Anodized_1
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_7/Materials/Metal_Aluminum_Anodized_1/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_7/Materials/Metal_Aluminum_Anodized_1/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.260, 0.269, 0.282)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0.309883'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0'

---

### /World/agv_7/Materials/Metal_Aluminum_Anodized_2

* **Prim路径 (Prim Path):**/World/agv_7/Materials/Metal_Aluminum_Anodized_2
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_7/Materials/Metal_Aluminum_Anodized_2/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_7/Materials/Metal_Aluminum_Anodized_2/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.792, 0.820, 0.859)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_7/Materials/basic_gray_plastic

* **Prim路径 (Prim Path):**/World/agv_7/Materials/basic_gray_plastic
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_7/Materials/basic_gray_plastic/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_7/Materials/basic_gray_plastic/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0.297745'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0.115685'

---

### /World/agv_7/Materials/texture

* **Prim路径 (Prim Path):**/World/agv_7/Materials/texture
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_7/Materials/texture/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_7/Materials/texture/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.294, 0.294, 0.294)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_8/Materials/ASELSAN_CATS_04

* **Prim路径 (Prim Path):**/World/agv_8/Materials/ASELSAN_CATS_04
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_8/Materials/ASELSAN_CATS_04/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_8/Materials/ASELSAN_CATS_04/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.158, 0.158, 0.158)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_8/Materials/ASELSAN_CATS_04_2

* **Prim路径 (Prim Path):**/World/agv_8/Materials/ASELSAN_CATS_04_2
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_8/Materials/ASELSAN_CATS_04_2/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_8/Materials/ASELSAN_CATS_04_2/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.769, 0.773, 0.749)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_8/Materials/ASELSAN_CATS_13

* **Prim路径 (Prim Path):**/World/agv_8/Materials/ASELSAN_CATS_13
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_8/Materials/ASELSAN_CATS_13/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_8/Materials/ASELSAN_CATS_13/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.706, 0.718, 0.729)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_8/Materials/Color_000

* **Prim路径 (Prim Path):**/World/agv_8/Materials/Color_000
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_8/Materials/Color_000/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_8/Materials/Color_000/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(1.000, 1.000, 1.000)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_8/Materials/Color_A05

* **Prim路径 (Prim Path):**/World/agv_8/Materials/Color_A05
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_8/Materials/Color_A05/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_8/Materials/Color_A05/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(1.000, 0.000, 0.000)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0.959234'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0'

---

### /World/agv_8/Materials/Color_A06

* **Prim路径 (Prim Path):**/World/agv_8/Materials/Color_A06
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_8/Materials/Color_A06/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_8/Materials/Color_A06/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.800, 0.000, 0.000)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_8/Materials/Color_B05

* **Prim路径 (Prim Path):**/World/agv_8/Materials/Color_B05
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_8/Materials/Color_B05/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_8/Materials/Color_B05/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(1.000, 0.247, 0.000)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '1'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0'

---

### /World/agv_8/Materials/Color_E02

* **Prim路径 (Prim Path):**/World/agv_8/Materials/Color_E02
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_8/Materials/Color_E02/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_8/Materials/Color_E02/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(1.000, 1.000, 0.196)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_8/Materials/Color_E05

* **Prim路径 (Prim Path):**/World/agv_8/Materials/Color_E05
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_8/Materials/Color_E05/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_8/Materials/Color_E05/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(1.000, 0.910, 0.000)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0.625455'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0.133891'

---

### /World/agv_8/Materials/Color_F06

* **Prim路径 (Prim Path):**/World/agv_8/Materials/Color_F06
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_8/Materials/Color_F06/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_8/Materials/Color_F06/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.400, 0.800, 0.000)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_8/Materials/Color_G03

* **Prim路径 (Prim Path):**/World/agv_8/Materials/Color_G03
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_8/Materials/Color_G03/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_8/Materials/Color_G03/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.396, 1.000, 0.396)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_8/Materials/Color_M02

* **Prim路径 (Prim Path):**/World/agv_8/Materials/Color_M02
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_8/Materials/Color_M02/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_8/Materials/Color_M02/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.776, 0.776, 0.776)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_8/Materials/Color_M03

* **Prim路径 (Prim Path):**/World/agv_8/Materials/Color_M03
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_8/Materials/Color_M03/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_8/Materials/Color_M03/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.667, 0.667, 0.667)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_8/Materials/Mtl39

* **Prim路径 (Prim Path):**/World/agv_8/Materials/Mtl39
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_8/Materials/Mtl39/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_8/Materials/Mtl39/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.494, 0.494, 0.494)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_8/Materials/Mtl6

* **Prim路径 (Prim Path):**/World/agv_8/Materials/Mtl6
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_8/Materials/Mtl6/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_8/Materials/Mtl6/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f]
        * Connected: '/World/agv_8/Materials/Mtl6/tex_base.outputs:rgb' @ '/World/agv_8/Materials/Mtl6/tex_base'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/Mtl6_baseColor.jpg'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'
    * '/World/agv_8/Materials/Mtl6/tex_base' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/Mtl6_baseColor.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'file' [asset] = '0/Mtl6_baseColor.jpg'
      * 'st' [float2]
        * Connected: '/World/agv_8/Materials/Mtl6/uvset0.outputs:result' @ '/World/agv_8/Materials/Mtl6/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/agv_8/Materials/Mtl6/uvset0' (ID: 'UsdPrimvarReader_float2')
    * Implementation: 'id'

---

### /World/agv_8/Materials/Mtl9

* **Prim路径 (Prim Path):**/World/agv_8/Materials/Mtl9
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_8/Materials/Mtl9/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_8/Materials/Mtl9/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.514, 1.000, 0.000)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_8/Materials/Silver

* **Prim路径 (Prim Path):**/World/agv_8/Materials/Silver
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_8/Materials/Silver/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_8/Materials/Silver/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.753, 0.753, 0.753)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_8/Materials/material

* **Prim路径 (Prim Path):**/World/agv_8/Materials/material
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_8/Materials/material/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_8/Materials/material/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f]
        * Connected: '/World/agv_8/Materials/material/tex_base.outputs:rgb' @ '/World/agv_8/Materials/material/tex_base'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/material_baseColor.jpg'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'
    * '/World/agv_8/Materials/material/tex_base' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/material_baseColor.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'file' [asset] = '0/material_baseColor.jpg'
      * 'st' [float2]
        * Connected: '/World/agv_8/Materials/material/uvset0.outputs:result' @ '/World/agv_8/Materials/material/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/agv_8/Materials/material/uvset0' (ID: 'UsdPrimvarReader_float2')
    * Implementation: 'id'

---

### /World/agv_8/Materials/cash_register_keys

* **Prim路径 (Prim Path):**/World/agv_8/Materials/cash_register_keys
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_8/Materials/cash_register_keys/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_8/Materials/cash_register_keys/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.976, 0.992, 0.973)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_8/Materials/Chris_Shoe_Sole

* **Prim路径 (Prim Path):**/World/agv_8/Materials/Chris_Shoe_Sole
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_8/Materials/Chris_Shoe_Sole/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_8/Materials/Chris_Shoe_Sole/pbr_shader' (ID: 'UsdPreviewSurface')
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

### /World/agv_8/Materials/Color_002

* **Prim路径 (Prim Path):**/World/agv_8/Materials/Color_002
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_8/Materials/Color_002/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_8/Materials/Color_002/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.217, 0.217, 0.217)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0.570837'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0'

---

### /World/agv_8/Materials/Color_005

* **Prim路径 (Prim Path):**/World/agv_8/Materials/Color_005
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_8/Materials/Color_005/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_8/Materials/Color_005/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.130, 0.130, 0.130)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0.710417'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0'

---

### /World/agv_8/Materials/Color_006

* **Prim路径 (Prim Path):**/World/agv_8/Materials/Color_006
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_8/Materials/Color_006/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_8/Materials/Color_006/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0.237059'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0'

---

### /World/agv_8/Materials/Color_008

* **Prim路径 (Prim Path):**/World/agv_8/Materials/Color_008
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_8/Materials/Color_008/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_8/Materials/Color_008/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.118, 0.118, 0.118)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0.941027'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0'

---

### /World/agv_8/Materials/Color_A01

* **Prim路径 (Prim Path):**/World/agv_8/Materials/Color_A01
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_8/Materials/Color_A01/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_8/Materials/Color_A01/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(1.000, 0.000, 0.000)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0.965302'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0'

---

### /World/agv_8/Materials/Color_A11

* **Prim路径 (Prim Path):**/World/agv_8/Materials/Color_A11
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_8/Materials/Color_A11/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_8/Materials/Color_A11/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.600, 0.000, 0.000)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_8/Materials/Color_M04

* **Prim路径 (Prim Path):**/World/agv_8/Materials/Color_M04
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_8/Materials/Color_M04/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_8/Materials/Color_M04/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.557, 0.557, 0.557)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_8/Materials/Color_M05

* **Prim路径 (Prim Path):**/World/agv_8/Materials/Color_M05
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_8/Materials/Color_M05/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_8/Materials/Color_M05/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.447, 0.447, 0.447)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_8/Materials/Color_M06

* **Prim路径 (Prim Path):**/World/agv_8/Materials/Color_M06
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_8/Materials/Color_M06/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_8/Materials/Color_M06/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_8/Materials/Color_M07

* **Prim路径 (Prim Path):**/World/agv_8/Materials/Color_M07
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_8/Materials/Color_M07/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_8/Materials/Color_M07/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.227, 0.227, 0.227)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_8/Materials/Color_M09

* **Prim路径 (Prim Path):**/World/agv_8/Materials/Color_M09
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_8/Materials/Color_M09/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_8/Materials/Color_M09/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0.340226'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0.085341'

---

### /World/agv_8/Materials/FCP_Charcoal_v2

* **Prim路径 (Prim Path):**/World/agv_8/Materials/FCP_Charcoal_v2
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_8/Materials/FCP_Charcoal_v2/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_8/Materials/FCP_Charcoal_v2/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.216, 0.216, 0.216)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_8/Materials/FrontColor

* **Prim路径 (Prim Path):**/World/agv_8/Materials/FrontColor
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_8/Materials/FrontColor/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_8/Materials/FrontColor/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.504, 0.504, 0.504)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0.637593'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0.218852'

---

### /World/agv_8/Materials/Light_Blue

* **Prim路径 (Prim Path):**/World/agv_8/Materials/Light_Blue
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_8/Materials/Light_Blue/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_8/Materials/Light_Blue/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.601, 0.601, 0.601)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '1'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0.170303'

---

### /World/agv_8/Materials/M_0011_Seashell

* **Prim路径 (Prim Path):**/World/agv_8/Materials/M_0011_Seashell
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_8/Materials/M_0011_Seashell/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_8/Materials/M_0011_Seashell/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(1.000, 0.961, 0.933)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_8/Materials/M_0131_Silver

* **Prim路径 (Prim Path):**/World/agv_8/Materials/M_0131_Silver
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_8/Materials/M_0131_Silver/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_8/Materials/M_0131_Silver/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.242, 0.242, 0.242)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0.613318'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0'

---

### /World/agv_8/Materials/M_0134_DimGray

* **Prim路径 (Prim Path):**/World/agv_8/Materials/M_0134_DimGray
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_8/Materials/M_0134_DimGray/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_8/Materials/M_0134_DimGray/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.412, 0.412, 0.412)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_8/Materials/M_0135_DarkGray

* **Prim路径 (Prim Path):**/World/agv_8/Materials/M_0135_DarkGray
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_8/Materials/M_0135_DarkGray/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_8/Materials/M_0135_DarkGray/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.318, 0.318, 0.318)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_8/Materials/Metal_Silver

* **Prim路径 (Prim Path):**/World/agv_8/Materials/Metal_Silver
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_8/Materials/Metal_Silver/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_8/Materials/Metal_Silver/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.918, 0.914, 0.933)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_8/Materials/Mtl1

* **Prim路径 (Prim Path):**/World/agv_8/Materials/Mtl1
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_8/Materials/Mtl1/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_8/Materials/Mtl1/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.015, 0.015, 0.015)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0.255265'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_8/Materials/Mtl10

* **Prim路径 (Prim Path):**/World/agv_8/Materials/Mtl10
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_8/Materials/Mtl10/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_8/Materials/Mtl10/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.322, 0.322, 0.322)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_8/Materials/Mtl11

* **Prim路径 (Prim Path):**/World/agv_8/Materials/Mtl11
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_8/Materials/Mtl11/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_8/Materials/Mtl11/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.067, 0.757, 0.329)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_8/Materials/Mtl12

* **Prim路径 (Prim Path):**/World/agv_8/Materials/Mtl12
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_8/Materials/Mtl12/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_8/Materials/Mtl12/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.502, 0.502, 0.502)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_8/Materials/Mtl13

* **Prim路径 (Prim Path):**/World/agv_8/Materials/Mtl13
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_8/Materials/Mtl13/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_8/Materials/Mtl13/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.008, 0.514, 0.816)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_8/Materials/Mtl14

* **Prim路径 (Prim Path):**/World/agv_8/Materials/Mtl14
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_8/Materials/Mtl14/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_8/Materials/Mtl14/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.310, 0.310, 0.310)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_8/Materials/Mtl15

* **Prim路径 (Prim Path):**/World/agv_8/Materials/Mtl15
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_8/Materials/Mtl15/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_8/Materials/Mtl15/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.263, 0.275, 0.275)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_8/Materials/Mtl16

* **Prim路径 (Prim Path):**/World/agv_8/Materials/Mtl16
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_8/Materials/Mtl16/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_8/Materials/Mtl16/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.698, 0.698, 0.000)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_8/Materials/Mtl17

* **Prim路径 (Prim Path):**/World/agv_8/Materials/Mtl17
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_8/Materials/Mtl17/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_8/Materials/Mtl17/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.000, 0.863, 1.000)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_8/Materials/Mtl3

* **Prim路径 (Prim Path):**/World/agv_8/Materials/Mtl3
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_8/Materials/Mtl3/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_8/Materials/Mtl3/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.431, 0.455, 0.498)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_8/Materials/Mtl35

* **Prim路径 (Prim Path):**/World/agv_8/Materials/Mtl35
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_8/Materials/Mtl35/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_8/Materials/Mtl35/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.792, 0.820, 0.933)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_8/Materials/Mtl36

* **Prim路径 (Prim Path):**/World/agv_8/Materials/Mtl36
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_8/Materials/Mtl36/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_8/Materials/Mtl36/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.667, 0.698, 0.765)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_8/Materials/Mtl37

* **Prim路径 (Prim Path):**/World/agv_8/Materials/Mtl37
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_8/Materials/Mtl37/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_8/Materials/Mtl37/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.098, 0.098, 0.098)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_8/Materials/Mtl3a

* **Prim路径 (Prim Path):**/World/agv_8/Materials/Mtl3a
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_8/Materials/Mtl3a/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_8/Materials/Mtl3a/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.388, 0.369, 0.322)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_8/Materials/Mtl3b

* **Prim路径 (Prim Path):**/World/agv_8/Materials/Mtl3b
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_8/Materials/Mtl3b/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_8/Materials/Mtl3b/pbr_shader' (ID: 'UsdPreviewSurface')
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

### /World/agv_8/Materials/Mtl5

* **Prim路径 (Prim Path):**/World/agv_8/Materials/Mtl5
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_8/Materials/Mtl5/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_8/Materials/Mtl5/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.396, 0.408, 0.467)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_8/Materials/Mtl7

* **Prim路径 (Prim Path):**/World/agv_8/Materials/Mtl7
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_8/Materials/Mtl7/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_8/Materials/Mtl7/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.376, 0.376, 0.376)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_8/Materials/Mtl8

* **Prim路径 (Prim Path):**/World/agv_8/Materials/Mtl8
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_8/Materials/Mtl8/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_8/Materials/Mtl8/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.173, 0.173, 0.173)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_8/Materials/Mtla

* **Prim路径 (Prim Path):**/World/agv_8/Materials/Mtla
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_8/Materials/Mtla/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_8/Materials/Mtla/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.612, 0.725, 0.745)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_8/Materials/Mtlb1

* **Prim路径 (Prim Path):**/World/agv_8/Materials/Mtlb1
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_8/Materials/Mtlb1/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_8/Materials/Mtlb1/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.949, 0.925, 0.933)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_8/Materials/Stainless_Steel

* **Prim路径 (Prim Path):**/World/agv_8/Materials/Stainless_Steel
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_8/Materials/Stainless_Steel/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_8/Materials/Stainless_Steel/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.292, 0.294, 0.284)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0.431257'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_8/Materials/Metal_Aluminum_Anodized_1

* **Prim路径 (Prim Path):**/World/agv_8/Materials/Metal_Aluminum_Anodized_1
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_8/Materials/Metal_Aluminum_Anodized_1/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_8/Materials/Metal_Aluminum_Anodized_1/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.260, 0.269, 0.282)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0.309883'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0'

---

### /World/agv_8/Materials/Metal_Aluminum_Anodized_2

* **Prim路径 (Prim Path):**/World/agv_8/Materials/Metal_Aluminum_Anodized_2
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_8/Materials/Metal_Aluminum_Anodized_2/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_8/Materials/Metal_Aluminum_Anodized_2/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.792, 0.820, 0.859)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/agv_8/Materials/basic_gray_plastic

* **Prim路径 (Prim Path):**/World/agv_8/Materials/basic_gray_plastic
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_8/Materials/basic_gray_plastic/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_8/Materials/basic_gray_plastic/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0.297745'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0.115685'

---

### /World/agv_8/Materials/texture

* **Prim路径 (Prim Path):**/World/agv_8/Materials/texture
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/agv_8/Materials/texture/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/agv_8/Materials/texture/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.294, 0.294, 0.294)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/Conveyor_1/Materials/Conveyor

* **Prim路径 (Prim Path):**/World/Conveyor_1/Materials/Conveyor
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/Conveyor_1/Materials/Conveyor/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_1/Materials/Conveyor/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f]
        * Connected: '/World/Conveyor_1/Materials/Conveyor/tex_base.outputs:rgb' @ '/World/Conveyor_1/Materials/Conveyor/tex_base'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/Conveyor_diffuse.jpg'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'glossiness' [float]
        * Connected: '/World/Conveyor_1/Materials/Conveyor/tex_glossiness.outputs:r' @ '/World/Conveyor_1/Materials/Conveyor/tex_glossiness'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/Conveyor_specularGlossiness_gloss_scale0.jpg'
      * 'normal' [normal3f]
        * Connected: '/World/Conveyor_1/Materials/Conveyor/tex_normal.outputs:rgb' @ '/World/Conveyor_1/Materials/Conveyor/tex_normal'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/Conveyor_normal.jpg'
      * 'occlusion' [float]
        * Connected: '/World/Conveyor_1/Materials/Conveyor/tex_occlusion.outputs:r' @ '/World/Conveyor_1/Materials/Conveyor/tex_occlusion'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/Conveyor_occlusion_occl.jpg'
      * 'specularColor' [float3]
        * Connected: '/World/Conveyor_1/Materials/Conveyor/tex_specular.outputs:rgb' @ '/World/Conveyor_1/Materials/Conveyor/tex_specular'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/Conveyor_specularGlossiness_spec.jpg'
    * '/World/Conveyor_1/Materials/Conveyor/tex_base' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/Conveyor_diffuse.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'file' [asset] = '0/Conveyor_diffuse.jpg'
      * 'st' [float2]
        * Connected: '/World/Conveyor_1/Materials/Conveyor/uvset0.outputs:result' @ '/World/Conveyor_1/Materials/Conveyor/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/Conveyor_1/Materials/Conveyor/uvset0' (ID: 'UsdPrimvarReader_float2')
    * Implementation: 'id'
    * '/World/Conveyor_1/Materials/Conveyor/tex_glossiness' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/Conveyor_specularGlossiness_gloss_scale0.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 0.000, 0.000, 1.000)'
      * 'file' [asset] = '0/Conveyor_specularGlossiness_gloss_scale0.jpg'
      * 'st' [float2]
        * Connected: '/World/Conveyor_1/Materials/Conveyor/uvset0.outputs:result' @ '/World/Conveyor_1/Materials/Conveyor/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/Conveyor_1/Materials/Conveyor/tex_normal' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/Conveyor_normal.jpg'
    * Inputs:
      * 'bias' [float4] = '(-1.000, -1.000, -1.000, -1.000)'
      * 'fallback' [float4] = '(0.000, 0.000, 1.000, 1.000)'
      * 'file' [asset] = '0/Conveyor_normal.jpg'
      * 'scale' [float4] = '(2.000, 2.000, 2.000, 2.000)'
      * 'st' [float2]
        * Connected: '/World/Conveyor_1/Materials/Conveyor/uvset0.outputs:result' @ '/World/Conveyor_1/Materials/Conveyor/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/Conveyor_1/Materials/Conveyor/tex_occlusion' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/Conveyor_occlusion_occl.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 0.000, 0.000, 1.000)'
      * 'file' [asset] = '0/Conveyor_occlusion_occl.jpg'
      * 'st' [float2]
        * Connected: '/World/Conveyor_1/Materials/Conveyor/uvset0.outputs:result' @ '/World/Conveyor_1/Materials/Conveyor/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/Conveyor_1/Materials/Conveyor/tex_specular' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/Conveyor_specularGlossiness_spec.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'file' [asset] = '0/Conveyor_specularGlossiness_spec.jpg'
      * 'st' [float2]
        * Connected: '/World/Conveyor_1/Materials/Conveyor/uvset0.outputs:result' @ '/World/Conveyor_1/Materials/Conveyor/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'

---

### /World/Conveyor_1/Materials/Belt

* **Prim路径 (Prim Path):**/World/Conveyor_1/Materials/Belt
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/Conveyor_1/Materials/Belt/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_1/Materials/Belt/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f]
        * Connected: '/World/Conveyor_1/Materials/Belt/tex_base.outputs:rgb' @ '/World/Conveyor_1/Materials/Belt/tex_base'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/Belt_diffuse.jpg'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'glossiness' [float] = '0.060939'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'specularColor' [float3] = '(0.050, 0.050, 0.050)'
    * '/World/Conveyor_1/Materials/Belt/tex_base' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/Belt_diffuse.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'file' [asset] = '0/Belt_diffuse.jpg'
      * 'st' [float2]
        * Connected: '/World/Conveyor_1/Materials/Belt/uvset0.outputs:result' @ '/World/Conveyor_1/Materials/Belt/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/Conveyor_1/Materials/Belt/uvset0' (ID: 'UsdPrimvarReader_float2')
    * Implementation: 'id'

---

### /World/Conveyor_2/Materials/Conveyor

* **Prim路径 (Prim Path):**/World/Conveyor_2/Materials/Conveyor
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/Conveyor_2/Materials/Conveyor/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_2/Materials/Conveyor/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f]
        * Connected: '/World/Conveyor_2/Materials/Conveyor/tex_base.outputs:rgb' @ '/World/Conveyor_2/Materials/Conveyor/tex_base'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/Conveyor_diffuse.jpg'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'glossiness' [float]
        * Connected: '/World/Conveyor_2/Materials/Conveyor/tex_glossiness.outputs:r' @ '/World/Conveyor_2/Materials/Conveyor/tex_glossiness'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/Conveyor_specularGlossiness_gloss_scale0.jpg'
      * 'normal' [normal3f]
        * Connected: '/World/Conveyor_2/Materials/Conveyor/tex_normal.outputs:rgb' @ '/World/Conveyor_2/Materials/Conveyor/tex_normal'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/Conveyor_normal.jpg'
      * 'occlusion' [float]
        * Connected: '/World/Conveyor_2/Materials/Conveyor/tex_occlusion.outputs:r' @ '/World/Conveyor_2/Materials/Conveyor/tex_occlusion'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/Conveyor_occlusion_occl.jpg'
      * 'specularColor' [float3]
        * Connected: '/World/Conveyor_2/Materials/Conveyor/tex_specular.outputs:rgb' @ '/World/Conveyor_2/Materials/Conveyor/tex_specular'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/Conveyor_specularGlossiness_spec.jpg'
    * '/World/Conveyor_2/Materials/Conveyor/tex_base' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/Conveyor_diffuse.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'file' [asset] = '0/Conveyor_diffuse.jpg'
      * 'st' [float2]
        * Connected: '/World/Conveyor_2/Materials/Conveyor/uvset0.outputs:result' @ '/World/Conveyor_2/Materials/Conveyor/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/Conveyor_2/Materials/Conveyor/uvset0' (ID: 'UsdPrimvarReader_float2')
    * Implementation: 'id'
    * '/World/Conveyor_2/Materials/Conveyor/tex_glossiness' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/Conveyor_specularGlossiness_gloss_scale0.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 0.000, 0.000, 1.000)'
      * 'file' [asset] = '0/Conveyor_specularGlossiness_gloss_scale0.jpg'
      * 'st' [float2]
        * Connected: '/World/Conveyor_2/Materials/Conveyor/uvset0.outputs:result' @ '/World/Conveyor_2/Materials/Conveyor/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/Conveyor_2/Materials/Conveyor/tex_normal' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/Conveyor_normal.jpg'
    * Inputs:
      * 'bias' [float4] = '(-1.000, -1.000, -1.000, -1.000)'
      * 'fallback' [float4] = '(0.000, 0.000, 1.000, 1.000)'
      * 'file' [asset] = '0/Conveyor_normal.jpg'
      * 'scale' [float4] = '(2.000, 2.000, 2.000, 2.000)'
      * 'st' [float2]
        * Connected: '/World/Conveyor_2/Materials/Conveyor/uvset0.outputs:result' @ '/World/Conveyor_2/Materials/Conveyor/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/Conveyor_2/Materials/Conveyor/tex_occlusion' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/Conveyor_occlusion_occl.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 0.000, 0.000, 1.000)'
      * 'file' [asset] = '0/Conveyor_occlusion_occl.jpg'
      * 'st' [float2]
        * Connected: '/World/Conveyor_2/Materials/Conveyor/uvset0.outputs:result' @ '/World/Conveyor_2/Materials/Conveyor/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/Conveyor_2/Materials/Conveyor/tex_specular' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/Conveyor_specularGlossiness_spec.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'file' [asset] = '0/Conveyor_specularGlossiness_spec.jpg'
      * 'st' [float2]
        * Connected: '/World/Conveyor_2/Materials/Conveyor/uvset0.outputs:result' @ '/World/Conveyor_2/Materials/Conveyor/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'

---

### /World/Conveyor_2/Materials/Belt

* **Prim路径 (Prim Path):**/World/Conveyor_2/Materials/Belt
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/Conveyor_2/Materials/Belt/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_2/Materials/Belt/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f]
        * Connected: '/World/Conveyor_2/Materials/Belt/tex_base.outputs:rgb' @ '/World/Conveyor_2/Materials/Belt/tex_base'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/Belt_diffuse.jpg'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'glossiness' [float] = '0.060939'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'specularColor' [float3] = '(0.050, 0.050, 0.050)'
    * '/World/Conveyor_2/Materials/Belt/tex_base' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/Belt_diffuse.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'file' [asset] = '0/Belt_diffuse.jpg'
      * 'st' [float2]
        * Connected: '/World/Conveyor_2/Materials/Belt/uvset0.outputs:result' @ '/World/Conveyor_2/Materials/Belt/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/Conveyor_2/Materials/Belt/uvset0' (ID: 'UsdPrimvarReader_float2')
    * Implementation: 'id'

---

### /World/Conveyor_3/Materials/Conveyor

* **Prim路径 (Prim Path):**/World/Conveyor_3/Materials/Conveyor
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/Conveyor_3/Materials/Conveyor/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_3/Materials/Conveyor/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f]
        * Connected: '/World/Conveyor_3/Materials/Conveyor/tex_base.outputs:rgb' @ '/World/Conveyor_3/Materials/Conveyor/tex_base'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/Conveyor_diffuse.jpg'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'glossiness' [float]
        * Connected: '/World/Conveyor_3/Materials/Conveyor/tex_glossiness.outputs:r' @ '/World/Conveyor_3/Materials/Conveyor/tex_glossiness'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/Conveyor_specularGlossiness_gloss_scale0.jpg'
      * 'normal' [normal3f]
        * Connected: '/World/Conveyor_3/Materials/Conveyor/tex_normal.outputs:rgb' @ '/World/Conveyor_3/Materials/Conveyor/tex_normal'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/Conveyor_normal.jpg'
      * 'occlusion' [float]
        * Connected: '/World/Conveyor_3/Materials/Conveyor/tex_occlusion.outputs:r' @ '/World/Conveyor_3/Materials/Conveyor/tex_occlusion'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/Conveyor_occlusion_occl.jpg'
      * 'specularColor' [float3]
        * Connected: '/World/Conveyor_3/Materials/Conveyor/tex_specular.outputs:rgb' @ '/World/Conveyor_3/Materials/Conveyor/tex_specular'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/Conveyor_specularGlossiness_spec.jpg'
    * '/World/Conveyor_3/Materials/Conveyor/tex_base' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/Conveyor_diffuse.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'file' [asset] = '0/Conveyor_diffuse.jpg'
      * 'st' [float2]
        * Connected: '/World/Conveyor_3/Materials/Conveyor/uvset0.outputs:result' @ '/World/Conveyor_3/Materials/Conveyor/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/Conveyor_3/Materials/Conveyor/uvset0' (ID: 'UsdPrimvarReader_float2')
    * Implementation: 'id'
    * '/World/Conveyor_3/Materials/Conveyor/tex_glossiness' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/Conveyor_specularGlossiness_gloss_scale0.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 0.000, 0.000, 1.000)'
      * 'file' [asset] = '0/Conveyor_specularGlossiness_gloss_scale0.jpg'
      * 'st' [float2]
        * Connected: '/World/Conveyor_3/Materials/Conveyor/uvset0.outputs:result' @ '/World/Conveyor_3/Materials/Conveyor/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/Conveyor_3/Materials/Conveyor/tex_normal' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/Conveyor_normal.jpg'
    * Inputs:
      * 'bias' [float4] = '(-1.000, -1.000, -1.000, -1.000)'
      * 'fallback' [float4] = '(0.000, 0.000, 1.000, 1.000)'
      * 'file' [asset] = '0/Conveyor_normal.jpg'
      * 'scale' [float4] = '(2.000, 2.000, 2.000, 2.000)'
      * 'st' [float2]
        * Connected: '/World/Conveyor_3/Materials/Conveyor/uvset0.outputs:result' @ '/World/Conveyor_3/Materials/Conveyor/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/Conveyor_3/Materials/Conveyor/tex_occlusion' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/Conveyor_occlusion_occl.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 0.000, 0.000, 1.000)'
      * 'file' [asset] = '0/Conveyor_occlusion_occl.jpg'
      * 'st' [float2]
        * Connected: '/World/Conveyor_3/Materials/Conveyor/uvset0.outputs:result' @ '/World/Conveyor_3/Materials/Conveyor/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/Conveyor_3/Materials/Conveyor/tex_specular' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/Conveyor_specularGlossiness_spec.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'file' [asset] = '0/Conveyor_specularGlossiness_spec.jpg'
      * 'st' [float2]
        * Connected: '/World/Conveyor_3/Materials/Conveyor/uvset0.outputs:result' @ '/World/Conveyor_3/Materials/Conveyor/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'

---

### /World/Conveyor_3/Materials/Belt

* **Prim路径 (Prim Path):**/World/Conveyor_3/Materials/Belt
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/Conveyor_3/Materials/Belt/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_3/Materials/Belt/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f]
        * Connected: '/World/Conveyor_3/Materials/Belt/tex_base.outputs:rgb' @ '/World/Conveyor_3/Materials/Belt/tex_base'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/Belt_diffuse.jpg'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'glossiness' [float] = '0.060939'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'specularColor' [float3] = '(0.050, 0.050, 0.050)'
    * '/World/Conveyor_3/Materials/Belt/tex_base' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/Belt_diffuse.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'file' [asset] = '0/Belt_diffuse.jpg'
      * 'st' [float2]
        * Connected: '/World/Conveyor_3/Materials/Belt/uvset0.outputs:result' @ '/World/Conveyor_3/Materials/Belt/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/Conveyor_3/Materials/Belt/uvset0' (ID: 'UsdPrimvarReader_float2')
    * Implementation: 'id'

---

### /World/Conveyor_4/Materials/Conveyor

* **Prim路径 (Prim Path):**/World/Conveyor_4/Materials/Conveyor
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/Conveyor_4/Materials/Conveyor/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_4/Materials/Conveyor/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f]
        * Connected: '/World/Conveyor_4/Materials/Conveyor/tex_base.outputs:rgb' @ '/World/Conveyor_4/Materials/Conveyor/tex_base'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/Conveyor_diffuse.jpg'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'glossiness' [float]
        * Connected: '/World/Conveyor_4/Materials/Conveyor/tex_glossiness.outputs:r' @ '/World/Conveyor_4/Materials/Conveyor/tex_glossiness'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/Conveyor_specularGlossiness_gloss_scale0.jpg'
      * 'normal' [normal3f]
        * Connected: '/World/Conveyor_4/Materials/Conveyor/tex_normal.outputs:rgb' @ '/World/Conveyor_4/Materials/Conveyor/tex_normal'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/Conveyor_normal.jpg'
      * 'occlusion' [float]
        * Connected: '/World/Conveyor_4/Materials/Conveyor/tex_occlusion.outputs:r' @ '/World/Conveyor_4/Materials/Conveyor/tex_occlusion'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/Conveyor_occlusion_occl.jpg'
      * 'specularColor' [float3]
        * Connected: '/World/Conveyor_4/Materials/Conveyor/tex_specular.outputs:rgb' @ '/World/Conveyor_4/Materials/Conveyor/tex_specular'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/Conveyor_specularGlossiness_spec.jpg'
    * '/World/Conveyor_4/Materials/Conveyor/tex_base' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/Conveyor_diffuse.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'file' [asset] = '0/Conveyor_diffuse.jpg'
      * 'st' [float2]
        * Connected: '/World/Conveyor_4/Materials/Conveyor/uvset0.outputs:result' @ '/World/Conveyor_4/Materials/Conveyor/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/Conveyor_4/Materials/Conveyor/uvset0' (ID: 'UsdPrimvarReader_float2')
    * Implementation: 'id'
    * '/World/Conveyor_4/Materials/Conveyor/tex_glossiness' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/Conveyor_specularGlossiness_gloss_scale0.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 0.000, 0.000, 1.000)'
      * 'file' [asset] = '0/Conveyor_specularGlossiness_gloss_scale0.jpg'
      * 'st' [float2]
        * Connected: '/World/Conveyor_4/Materials/Conveyor/uvset0.outputs:result' @ '/World/Conveyor_4/Materials/Conveyor/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/Conveyor_4/Materials/Conveyor/tex_normal' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/Conveyor_normal.jpg'
    * Inputs:
      * 'bias' [float4] = '(-1.000, -1.000, -1.000, -1.000)'
      * 'fallback' [float4] = '(0.000, 0.000, 1.000, 1.000)'
      * 'file' [asset] = '0/Conveyor_normal.jpg'
      * 'scale' [float4] = '(2.000, 2.000, 2.000, 2.000)'
      * 'st' [float2]
        * Connected: '/World/Conveyor_4/Materials/Conveyor/uvset0.outputs:result' @ '/World/Conveyor_4/Materials/Conveyor/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/Conveyor_4/Materials/Conveyor/tex_occlusion' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/Conveyor_occlusion_occl.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 0.000, 0.000, 1.000)'
      * 'file' [asset] = '0/Conveyor_occlusion_occl.jpg'
      * 'st' [float2]
        * Connected: '/World/Conveyor_4/Materials/Conveyor/uvset0.outputs:result' @ '/World/Conveyor_4/Materials/Conveyor/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/Conveyor_4/Materials/Conveyor/tex_specular' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/Conveyor_specularGlossiness_spec.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'file' [asset] = '0/Conveyor_specularGlossiness_spec.jpg'
      * 'st' [float2]
        * Connected: '/World/Conveyor_4/Materials/Conveyor/uvset0.outputs:result' @ '/World/Conveyor_4/Materials/Conveyor/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'

---

### /World/Conveyor_4/Materials/Belt

* **Prim路径 (Prim Path):**/World/Conveyor_4/Materials/Belt
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/Conveyor_4/Materials/Belt/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_4/Materials/Belt/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f]
        * Connected: '/World/Conveyor_4/Materials/Belt/tex_base.outputs:rgb' @ '/World/Conveyor_4/Materials/Belt/tex_base'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/Belt_diffuse.jpg'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'glossiness' [float] = '0.060939'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'specularColor' [float3] = '(0.050, 0.050, 0.050)'
    * '/World/Conveyor_4/Materials/Belt/tex_base' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/Belt_diffuse.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'file' [asset] = '0/Belt_diffuse.jpg'
      * 'st' [float2]
        * Connected: '/World/Conveyor_4/Materials/Belt/uvset0.outputs:result' @ '/World/Conveyor_4/Materials/Belt/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/Conveyor_4/Materials/Belt/uvset0' (ID: 'UsdPrimvarReader_float2')
    * Implementation: 'id'

---

### /World/Conveyor_5/Materials/Conveyor

* **Prim路径 (Prim Path):**/World/Conveyor_5/Materials/Conveyor
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/Conveyor_5/Materials/Conveyor/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_5/Materials/Conveyor/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f]
        * Connected: '/World/Conveyor_5/Materials/Conveyor/tex_base.outputs:rgb' @ '/World/Conveyor_5/Materials/Conveyor/tex_base'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/Conveyor_diffuse.jpg'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'glossiness' [float]
        * Connected: '/World/Conveyor_5/Materials/Conveyor/tex_glossiness.outputs:r' @ '/World/Conveyor_5/Materials/Conveyor/tex_glossiness'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/Conveyor_specularGlossiness_gloss_scale0.jpg'
      * 'normal' [normal3f]
        * Connected: '/World/Conveyor_5/Materials/Conveyor/tex_normal.outputs:rgb' @ '/World/Conveyor_5/Materials/Conveyor/tex_normal'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/Conveyor_normal.jpg'
      * 'occlusion' [float]
        * Connected: '/World/Conveyor_5/Materials/Conveyor/tex_occlusion.outputs:r' @ '/World/Conveyor_5/Materials/Conveyor/tex_occlusion'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/Conveyor_occlusion_occl.jpg'
      * 'specularColor' [float3]
        * Connected: '/World/Conveyor_5/Materials/Conveyor/tex_specular.outputs:rgb' @ '/World/Conveyor_5/Materials/Conveyor/tex_specular'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/Conveyor_specularGlossiness_spec.jpg'
    * '/World/Conveyor_5/Materials/Conveyor/tex_base' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/Conveyor_diffuse.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'file' [asset] = '0/Conveyor_diffuse.jpg'
      * 'st' [float2]
        * Connected: '/World/Conveyor_5/Materials/Conveyor/uvset0.outputs:result' @ '/World/Conveyor_5/Materials/Conveyor/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/Conveyor_5/Materials/Conveyor/uvset0' (ID: 'UsdPrimvarReader_float2')
    * Implementation: 'id'
    * '/World/Conveyor_5/Materials/Conveyor/tex_glossiness' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/Conveyor_specularGlossiness_gloss_scale0.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 0.000, 0.000, 1.000)'
      * 'file' [asset] = '0/Conveyor_specularGlossiness_gloss_scale0.jpg'
      * 'st' [float2]
        * Connected: '/World/Conveyor_5/Materials/Conveyor/uvset0.outputs:result' @ '/World/Conveyor_5/Materials/Conveyor/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/Conveyor_5/Materials/Conveyor/tex_normal' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/Conveyor_normal.jpg'
    * Inputs:
      * 'bias' [float4] = '(-1.000, -1.000, -1.000, -1.000)'
      * 'fallback' [float4] = '(0.000, 0.000, 1.000, 1.000)'
      * 'file' [asset] = '0/Conveyor_normal.jpg'
      * 'scale' [float4] = '(2.000, 2.000, 2.000, 2.000)'
      * 'st' [float2]
        * Connected: '/World/Conveyor_5/Materials/Conveyor/uvset0.outputs:result' @ '/World/Conveyor_5/Materials/Conveyor/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/Conveyor_5/Materials/Conveyor/tex_occlusion' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/Conveyor_occlusion_occl.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 0.000, 0.000, 1.000)'
      * 'file' [asset] = '0/Conveyor_occlusion_occl.jpg'
      * 'st' [float2]
        * Connected: '/World/Conveyor_5/Materials/Conveyor/uvset0.outputs:result' @ '/World/Conveyor_5/Materials/Conveyor/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/Conveyor_5/Materials/Conveyor/tex_specular' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/Conveyor_specularGlossiness_spec.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'file' [asset] = '0/Conveyor_specularGlossiness_spec.jpg'
      * 'st' [float2]
        * Connected: '/World/Conveyor_5/Materials/Conveyor/uvset0.outputs:result' @ '/World/Conveyor_5/Materials/Conveyor/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'

---

### /World/Conveyor_5/Materials/Belt

* **Prim路径 (Prim Path):**/World/Conveyor_5/Materials/Belt
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/Conveyor_5/Materials/Belt/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_5/Materials/Belt/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f]
        * Connected: '/World/Conveyor_5/Materials/Belt/tex_base.outputs:rgb' @ '/World/Conveyor_5/Materials/Belt/tex_base'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/Belt_diffuse.jpg'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'glossiness' [float] = '0.060939'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'specularColor' [float3] = '(0.050, 0.050, 0.050)'
    * '/World/Conveyor_5/Materials/Belt/tex_base' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/Belt_diffuse.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'file' [asset] = '0/Belt_diffuse.jpg'
      * 'st' [float2]
        * Connected: '/World/Conveyor_5/Materials/Belt/uvset0.outputs:result' @ '/World/Conveyor_5/Materials/Belt/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/Conveyor_5/Materials/Belt/uvset0' (ID: 'UsdPrimvarReader_float2')
    * Implementation: 'id'

---

### /World/Conveyor_6/Materials/Conveyor

* **Prim路径 (Prim Path):**/World/Conveyor_6/Materials/Conveyor
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/Conveyor_6/Materials/Conveyor/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_6/Materials/Conveyor/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f]
        * Connected: '/World/Conveyor_6/Materials/Conveyor/tex_base.outputs:rgb' @ '/World/Conveyor_6/Materials/Conveyor/tex_base'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/Conveyor_diffuse.jpg'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'glossiness' [float]
        * Connected: '/World/Conveyor_6/Materials/Conveyor/tex_glossiness.outputs:r' @ '/World/Conveyor_6/Materials/Conveyor/tex_glossiness'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/Conveyor_specularGlossiness_gloss_scale0.jpg'
      * 'normal' [normal3f]
        * Connected: '/World/Conveyor_6/Materials/Conveyor/tex_normal.outputs:rgb' @ '/World/Conveyor_6/Materials/Conveyor/tex_normal'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/Conveyor_normal.jpg'
      * 'occlusion' [float]
        * Connected: '/World/Conveyor_6/Materials/Conveyor/tex_occlusion.outputs:r' @ '/World/Conveyor_6/Materials/Conveyor/tex_occlusion'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/Conveyor_occlusion_occl.jpg'
      * 'specularColor' [float3]
        * Connected: '/World/Conveyor_6/Materials/Conveyor/tex_specular.outputs:rgb' @ '/World/Conveyor_6/Materials/Conveyor/tex_specular'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/Conveyor_specularGlossiness_spec.jpg'
    * '/World/Conveyor_6/Materials/Conveyor/tex_base' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/Conveyor_diffuse.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'file' [asset] = '0/Conveyor_diffuse.jpg'
      * 'st' [float2]
        * Connected: '/World/Conveyor_6/Materials/Conveyor/uvset0.outputs:result' @ '/World/Conveyor_6/Materials/Conveyor/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/Conveyor_6/Materials/Conveyor/uvset0' (ID: 'UsdPrimvarReader_float2')
    * Implementation: 'id'
    * '/World/Conveyor_6/Materials/Conveyor/tex_glossiness' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/Conveyor_specularGlossiness_gloss_scale0.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 0.000, 0.000, 1.000)'
      * 'file' [asset] = '0/Conveyor_specularGlossiness_gloss_scale0.jpg'
      * 'st' [float2]
        * Connected: '/World/Conveyor_6/Materials/Conveyor/uvset0.outputs:result' @ '/World/Conveyor_6/Materials/Conveyor/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/Conveyor_6/Materials/Conveyor/tex_normal' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/Conveyor_normal.jpg'
    * Inputs:
      * 'bias' [float4] = '(-1.000, -1.000, -1.000, -1.000)'
      * 'fallback' [float4] = '(0.000, 0.000, 1.000, 1.000)'
      * 'file' [asset] = '0/Conveyor_normal.jpg'
      * 'scale' [float4] = '(2.000, 2.000, 2.000, 2.000)'
      * 'st' [float2]
        * Connected: '/World/Conveyor_6/Materials/Conveyor/uvset0.outputs:result' @ '/World/Conveyor_6/Materials/Conveyor/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/Conveyor_6/Materials/Conveyor/tex_occlusion' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/Conveyor_occlusion_occl.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 0.000, 0.000, 1.000)'
      * 'file' [asset] = '0/Conveyor_occlusion_occl.jpg'
      * 'st' [float2]
        * Connected: '/World/Conveyor_6/Materials/Conveyor/uvset0.outputs:result' @ '/World/Conveyor_6/Materials/Conveyor/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/Conveyor_6/Materials/Conveyor/tex_specular' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/Conveyor_specularGlossiness_spec.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'file' [asset] = '0/Conveyor_specularGlossiness_spec.jpg'
      * 'st' [float2]
        * Connected: '/World/Conveyor_6/Materials/Conveyor/uvset0.outputs:result' @ '/World/Conveyor_6/Materials/Conveyor/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'

---

### /World/Conveyor_6/Materials/Belt

* **Prim路径 (Prim Path):**/World/Conveyor_6/Materials/Belt
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/Conveyor_6/Materials/Belt/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_6/Materials/Belt/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f]
        * Connected: '/World/Conveyor_6/Materials/Belt/tex_base.outputs:rgb' @ '/World/Conveyor_6/Materials/Belt/tex_base'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/Belt_diffuse.jpg'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'glossiness' [float] = '0.060939'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'specularColor' [float3] = '(0.050, 0.050, 0.050)'
    * '/World/Conveyor_6/Materials/Belt/tex_base' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/Belt_diffuse.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'file' [asset] = '0/Belt_diffuse.jpg'
      * 'st' [float2]
        * Connected: '/World/Conveyor_6/Materials/Belt/uvset0.outputs:result' @ '/World/Conveyor_6/Materials/Belt/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/Conveyor_6/Materials/Belt/uvset0' (ID: 'UsdPrimvarReader_float2')
    * Implementation: 'id'

---

### /World/Conveyor_7/Materials/Conveyor

* **Prim路径 (Prim Path):**/World/Conveyor_7/Materials/Conveyor
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/Conveyor_7/Materials/Conveyor/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_7/Materials/Conveyor/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f]
        * Connected: '/World/Conveyor_7/Materials/Conveyor/tex_base.outputs:rgb' @ '/World/Conveyor_7/Materials/Conveyor/tex_base'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/Conveyor_diffuse.jpg'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'glossiness' [float]
        * Connected: '/World/Conveyor_7/Materials/Conveyor/tex_glossiness.outputs:r' @ '/World/Conveyor_7/Materials/Conveyor/tex_glossiness'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/Conveyor_specularGlossiness_gloss_scale0.jpg'
      * 'normal' [normal3f]
        * Connected: '/World/Conveyor_7/Materials/Conveyor/tex_normal.outputs:rgb' @ '/World/Conveyor_7/Materials/Conveyor/tex_normal'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/Conveyor_normal.jpg'
      * 'occlusion' [float]
        * Connected: '/World/Conveyor_7/Materials/Conveyor/tex_occlusion.outputs:r' @ '/World/Conveyor_7/Materials/Conveyor/tex_occlusion'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/Conveyor_occlusion_occl.jpg'
      * 'specularColor' [float3]
        * Connected: '/World/Conveyor_7/Materials/Conveyor/tex_specular.outputs:rgb' @ '/World/Conveyor_7/Materials/Conveyor/tex_specular'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/Conveyor_specularGlossiness_spec.jpg'
    * '/World/Conveyor_7/Materials/Conveyor/tex_base' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/Conveyor_diffuse.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'file' [asset] = '0/Conveyor_diffuse.jpg'
      * 'st' [float2]
        * Connected: '/World/Conveyor_7/Materials/Conveyor/uvset0.outputs:result' @ '/World/Conveyor_7/Materials/Conveyor/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/Conveyor_7/Materials/Conveyor/uvset0' (ID: 'UsdPrimvarReader_float2')
    * Implementation: 'id'
    * '/World/Conveyor_7/Materials/Conveyor/tex_glossiness' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/Conveyor_specularGlossiness_gloss_scale0.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 0.000, 0.000, 1.000)'
      * 'file' [asset] = '0/Conveyor_specularGlossiness_gloss_scale0.jpg'
      * 'st' [float2]
        * Connected: '/World/Conveyor_7/Materials/Conveyor/uvset0.outputs:result' @ '/World/Conveyor_7/Materials/Conveyor/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/Conveyor_7/Materials/Conveyor/tex_normal' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/Conveyor_normal.jpg'
    * Inputs:
      * 'bias' [float4] = '(-1.000, -1.000, -1.000, -1.000)'
      * 'fallback' [float4] = '(0.000, 0.000, 1.000, 1.000)'
      * 'file' [asset] = '0/Conveyor_normal.jpg'
      * 'scale' [float4] = '(2.000, 2.000, 2.000, 2.000)'
      * 'st' [float2]
        * Connected: '/World/Conveyor_7/Materials/Conveyor/uvset0.outputs:result' @ '/World/Conveyor_7/Materials/Conveyor/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/Conveyor_7/Materials/Conveyor/tex_occlusion' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/Conveyor_occlusion_occl.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 0.000, 0.000, 1.000)'
      * 'file' [asset] = '0/Conveyor_occlusion_occl.jpg'
      * 'st' [float2]
        * Connected: '/World/Conveyor_7/Materials/Conveyor/uvset0.outputs:result' @ '/World/Conveyor_7/Materials/Conveyor/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/Conveyor_7/Materials/Conveyor/tex_specular' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/Conveyor_specularGlossiness_spec.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'file' [asset] = '0/Conveyor_specularGlossiness_spec.jpg'
      * 'st' [float2]
        * Connected: '/World/Conveyor_7/Materials/Conveyor/uvset0.outputs:result' @ '/World/Conveyor_7/Materials/Conveyor/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'

---

### /World/Conveyor_7/Materials/Belt

* **Prim路径 (Prim Path):**/World/Conveyor_7/Materials/Belt
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/Conveyor_7/Materials/Belt/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_7/Materials/Belt/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f]
        * Connected: '/World/Conveyor_7/Materials/Belt/tex_base.outputs:rgb' @ '/World/Conveyor_7/Materials/Belt/tex_base'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/Belt_diffuse.jpg'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'glossiness' [float] = '0.060939'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'specularColor' [float3] = '(0.050, 0.050, 0.050)'
    * '/World/Conveyor_7/Materials/Belt/tex_base' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/Belt_diffuse.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'file' [asset] = '0/Belt_diffuse.jpg'
      * 'st' [float2]
        * Connected: '/World/Conveyor_7/Materials/Belt/uvset0.outputs:result' @ '/World/Conveyor_7/Materials/Belt/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/Conveyor_7/Materials/Belt/uvset0' (ID: 'UsdPrimvarReader_float2')
    * Implementation: 'id'

---

### /World/Conveyor_8/Materials/Conveyor

* **Prim路径 (Prim Path):**/World/Conveyor_8/Materials/Conveyor
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/Conveyor_8/Materials/Conveyor/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_8/Materials/Conveyor/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f]
        * Connected: '/World/Conveyor_8/Materials/Conveyor/tex_base.outputs:rgb' @ '/World/Conveyor_8/Materials/Conveyor/tex_base'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/Conveyor_diffuse.jpg'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'glossiness' [float]
        * Connected: '/World/Conveyor_8/Materials/Conveyor/tex_glossiness.outputs:r' @ '/World/Conveyor_8/Materials/Conveyor/tex_glossiness'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/Conveyor_specularGlossiness_gloss_scale0.jpg'
      * 'normal' [normal3f]
        * Connected: '/World/Conveyor_8/Materials/Conveyor/tex_normal.outputs:rgb' @ '/World/Conveyor_8/Materials/Conveyor/tex_normal'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/Conveyor_normal.jpg'
      * 'occlusion' [float]
        * Connected: '/World/Conveyor_8/Materials/Conveyor/tex_occlusion.outputs:r' @ '/World/Conveyor_8/Materials/Conveyor/tex_occlusion'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/Conveyor_occlusion_occl.jpg'
      * 'specularColor' [float3]
        * Connected: '/World/Conveyor_8/Materials/Conveyor/tex_specular.outputs:rgb' @ '/World/Conveyor_8/Materials/Conveyor/tex_specular'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/Conveyor_specularGlossiness_spec.jpg'
    * '/World/Conveyor_8/Materials/Conveyor/tex_base' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/Conveyor_diffuse.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'file' [asset] = '0/Conveyor_diffuse.jpg'
      * 'st' [float2]
        * Connected: '/World/Conveyor_8/Materials/Conveyor/uvset0.outputs:result' @ '/World/Conveyor_8/Materials/Conveyor/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/Conveyor_8/Materials/Conveyor/uvset0' (ID: 'UsdPrimvarReader_float2')
    * Implementation: 'id'
    * '/World/Conveyor_8/Materials/Conveyor/tex_glossiness' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/Conveyor_specularGlossiness_gloss_scale0.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 0.000, 0.000, 1.000)'
      * 'file' [asset] = '0/Conveyor_specularGlossiness_gloss_scale0.jpg'
      * 'st' [float2]
        * Connected: '/World/Conveyor_8/Materials/Conveyor/uvset0.outputs:result' @ '/World/Conveyor_8/Materials/Conveyor/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/Conveyor_8/Materials/Conveyor/tex_normal' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/Conveyor_normal.jpg'
    * Inputs:
      * 'bias' [float4] = '(-1.000, -1.000, -1.000, -1.000)'
      * 'fallback' [float4] = '(0.000, 0.000, 1.000, 1.000)'
      * 'file' [asset] = '0/Conveyor_normal.jpg'
      * 'scale' [float4] = '(2.000, 2.000, 2.000, 2.000)'
      * 'st' [float2]
        * Connected: '/World/Conveyor_8/Materials/Conveyor/uvset0.outputs:result' @ '/World/Conveyor_8/Materials/Conveyor/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/Conveyor_8/Materials/Conveyor/tex_occlusion' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/Conveyor_occlusion_occl.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 0.000, 0.000, 1.000)'
      * 'file' [asset] = '0/Conveyor_occlusion_occl.jpg'
      * 'st' [float2]
        * Connected: '/World/Conveyor_8/Materials/Conveyor/uvset0.outputs:result' @ '/World/Conveyor_8/Materials/Conveyor/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/Conveyor_8/Materials/Conveyor/tex_specular' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/Conveyor_specularGlossiness_spec.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'file' [asset] = '0/Conveyor_specularGlossiness_spec.jpg'
      * 'st' [float2]
        * Connected: '/World/Conveyor_8/Materials/Conveyor/uvset0.outputs:result' @ '/World/Conveyor_8/Materials/Conveyor/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'

---

### /World/Conveyor_8/Materials/Belt

* **Prim路径 (Prim Path):**/World/Conveyor_8/Materials/Belt
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/Conveyor_8/Materials/Belt/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_8/Materials/Belt/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f]
        * Connected: '/World/Conveyor_8/Materials/Belt/tex_base.outputs:rgb' @ '/World/Conveyor_8/Materials/Belt/tex_base'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/Belt_diffuse.jpg'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'glossiness' [float] = '0.060939'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'specularColor' [float3] = '(0.050, 0.050, 0.050)'
    * '/World/Conveyor_8/Materials/Belt/tex_base' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/Belt_diffuse.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'file' [asset] = '0/Belt_diffuse.jpg'
      * 'st' [float2]
        * Connected: '/World/Conveyor_8/Materials/Belt/uvset0.outputs:result' @ '/World/Conveyor_8/Materials/Belt/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/Conveyor_8/Materials/Belt/uvset0' (ID: 'UsdPrimvarReader_float2')
    * Implementation: 'id'

---

### /World/BoxOnConveyor_1/Materials/_6___Default

* **Prim路径 (Prim Path):**/World/BoxOnConveyor_1/Materials/_6___Default
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/BoxOnConveyor_1/Materials/_6___Default/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/BoxOnConveyor_1/Materials/_6___Default/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f]
        * Connected: '/World/BoxOnConveyor_1/Materials/_6___Default/tex_base.outputs:rgb' @ '/World/BoxOnConveyor_1/Materials/_6___Default/tex_base'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/06_-_Default_baseColor.jpg'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(1.000, 1.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0.892971'
    * '/World/BoxOnConveyor_1/Materials/_6___Default/tex_base' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/06_-_Default_baseColor.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'file' [asset] = '0/06_-_Default_baseColor.jpg'
      * 'st' [float2]
        * Connected: '/World/BoxOnConveyor_1/Materials/_6___Default/uvset0.outputs:result' @ '/World/BoxOnConveyor_1/Materials/_6___Default/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/BoxOnConveyor_1/Materials/_6___Default/uvset0' (ID: 'UsdPrimvarReader_float2')
    * Implementation: 'id'

---

### /World/BoxOnConveyor_2/Materials/_6___Default

* **Prim路径 (Prim Path):**/World/BoxOnConveyor_2/Materials/_6___Default
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/BoxOnConveyor_2/Materials/_6___Default/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/BoxOnConveyor_2/Materials/_6___Default/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f]
        * Connected: '/World/BoxOnConveyor_2/Materials/_6___Default/tex_base.outputs:rgb' @ '/World/BoxOnConveyor_2/Materials/_6___Default/tex_base'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/06_-_Default_baseColor.jpg'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(1.000, 1.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0.892971'
    * '/World/BoxOnConveyor_2/Materials/_6___Default/tex_base' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/06_-_Default_baseColor.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'file' [asset] = '0/06_-_Default_baseColor.jpg'
      * 'st' [float2]
        * Connected: '/World/BoxOnConveyor_2/Materials/_6___Default/uvset0.outputs:result' @ '/World/BoxOnConveyor_2/Materials/_6___Default/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/BoxOnConveyor_2/Materials/_6___Default/uvset0' (ID: 'UsdPrimvarReader_float2')
    * Implementation: 'id'

---

### /World/BoxOnConveyor_3/Materials/_6___Default

* **Prim路径 (Prim Path):**/World/BoxOnConveyor_3/Materials/_6___Default
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/BoxOnConveyor_3/Materials/_6___Default/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/BoxOnConveyor_3/Materials/_6___Default/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f]
        * Connected: '/World/BoxOnConveyor_3/Materials/_6___Default/tex_base.outputs:rgb' @ '/World/BoxOnConveyor_3/Materials/_6___Default/tex_base'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/06_-_Default_baseColor.jpg'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(1.000, 1.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0.892971'
    * '/World/BoxOnConveyor_3/Materials/_6___Default/tex_base' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/06_-_Default_baseColor.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'file' [asset] = '0/06_-_Default_baseColor.jpg'
      * 'st' [float2]
        * Connected: '/World/BoxOnConveyor_3/Materials/_6___Default/uvset0.outputs:result' @ '/World/BoxOnConveyor_3/Materials/_6___Default/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/BoxOnConveyor_3/Materials/_6___Default/uvset0' (ID: 'UsdPrimvarReader_float2')
    * Implementation: 'id'

---

### /World/BoxOnConveyor_4/Materials/_6___Default

* **Prim路径 (Prim Path):**/World/BoxOnConveyor_4/Materials/_6___Default
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/BoxOnConveyor_4/Materials/_6___Default/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/BoxOnConveyor_4/Materials/_6___Default/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f]
        * Connected: '/World/BoxOnConveyor_4/Materials/_6___Default/tex_base.outputs:rgb' @ '/World/BoxOnConveyor_4/Materials/_6___Default/tex_base'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/06_-_Default_baseColor.jpg'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(1.000, 1.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0.892971'
    * '/World/BoxOnConveyor_4/Materials/_6___Default/tex_base' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/06_-_Default_baseColor.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'file' [asset] = '0/06_-_Default_baseColor.jpg'
      * 'st' [float2]
        * Connected: '/World/BoxOnConveyor_4/Materials/_6___Default/uvset0.outputs:result' @ '/World/BoxOnConveyor_4/Materials/_6___Default/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/BoxOnConveyor_4/Materials/_6___Default/uvset0' (ID: 'UsdPrimvarReader_float2')
    * Implementation: 'id'

---

### /World/BoxOnConveyor_5/Materials/_6___Default

* **Prim路径 (Prim Path):**/World/BoxOnConveyor_5/Materials/_6___Default
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/BoxOnConveyor_5/Materials/_6___Default/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/BoxOnConveyor_5/Materials/_6___Default/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f]
        * Connected: '/World/BoxOnConveyor_5/Materials/_6___Default/tex_base.outputs:rgb' @ '/World/BoxOnConveyor_5/Materials/_6___Default/tex_base'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/06_-_Default_baseColor.jpg'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(1.000, 1.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0.892971'
    * '/World/BoxOnConveyor_5/Materials/_6___Default/tex_base' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/06_-_Default_baseColor.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'file' [asset] = '0/06_-_Default_baseColor.jpg'
      * 'st' [float2]
        * Connected: '/World/BoxOnConveyor_5/Materials/_6___Default/uvset0.outputs:result' @ '/World/BoxOnConveyor_5/Materials/_6___Default/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/BoxOnConveyor_5/Materials/_6___Default/uvset0' (ID: 'UsdPrimvarReader_float2')
    * Implementation: 'id'

---

### /World/BoxOnConveyor_6/Materials/_6___Default

* **Prim路径 (Prim Path):**/World/BoxOnConveyor_6/Materials/_6___Default
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/BoxOnConveyor_6/Materials/_6___Default/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/BoxOnConveyor_6/Materials/_6___Default/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f]
        * Connected: '/World/BoxOnConveyor_6/Materials/_6___Default/tex_base.outputs:rgb' @ '/World/BoxOnConveyor_6/Materials/_6___Default/tex_base'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/06_-_Default_baseColor.jpg'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(1.000, 1.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0.892971'
    * '/World/BoxOnConveyor_6/Materials/_6___Default/tex_base' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/06_-_Default_baseColor.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'file' [asset] = '0/06_-_Default_baseColor.jpg'
      * 'st' [float2]
        * Connected: '/World/BoxOnConveyor_6/Materials/_6___Default/uvset0.outputs:result' @ '/World/BoxOnConveyor_6/Materials/_6___Default/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/BoxOnConveyor_6/Materials/_6___Default/uvset0' (ID: 'UsdPrimvarReader_float2')
    * Implementation: 'id'

---

### /World/BoxOnConveyor_7/Materials/_6___Default

* **Prim路径 (Prim Path):**/World/BoxOnConveyor_7/Materials/_6___Default
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/BoxOnConveyor_7/Materials/_6___Default/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/BoxOnConveyor_7/Materials/_6___Default/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f]
        * Connected: '/World/BoxOnConveyor_7/Materials/_6___Default/tex_base.outputs:rgb' @ '/World/BoxOnConveyor_7/Materials/_6___Default/tex_base'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/06_-_Default_baseColor.jpg'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(1.000, 1.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0.892971'
    * '/World/BoxOnConveyor_7/Materials/_6___Default/tex_base' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/06_-_Default_baseColor.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'file' [asset] = '0/06_-_Default_baseColor.jpg'
      * 'st' [float2]
        * Connected: '/World/BoxOnConveyor_7/Materials/_6___Default/uvset0.outputs:result' @ '/World/BoxOnConveyor_7/Materials/_6___Default/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/BoxOnConveyor_7/Materials/_6___Default/uvset0' (ID: 'UsdPrimvarReader_float2')
    * Implementation: 'id'

---

### /World/BoxOnConveyor_8/Materials/_6___Default

* **Prim路径 (Prim Path):**/World/BoxOnConveyor_8/Materials/_6___Default
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/BoxOnConveyor_8/Materials/_6___Default/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/BoxOnConveyor_8/Materials/_6___Default/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f]
        * Connected: '/World/BoxOnConveyor_8/Materials/_6___Default/tex_base.outputs:rgb' @ '/World/BoxOnConveyor_8/Materials/_6___Default/tex_base'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/06_-_Default_baseColor.jpg'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(1.000, 1.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0.892971'
    * '/World/BoxOnConveyor_8/Materials/_6___Default/tex_base' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/06_-_Default_baseColor.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'file' [asset] = '0/06_-_Default_baseColor.jpg'
      * 'st' [float2]
        * Connected: '/World/BoxOnConveyor_8/Materials/_6___Default/uvset0.outputs:result' @ '/World/BoxOnConveyor_8/Materials/_6___Default/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/BoxOnConveyor_8/Materials/_6___Default/uvset0' (ID: 'UsdPrimvarReader_float2')
    * Implementation: 'id'

---

### /World/BoxOnConveyor_1_1/Materials/_6___Default

* **Prim路径 (Prim Path):**/World/BoxOnConveyor_1_1/Materials/_6___Default
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/BoxOnConveyor_1_1/Materials/_6___Default/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/BoxOnConveyor_1_1/Materials/_6___Default/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f]
        * Connected: '/World/BoxOnConveyor_1_1/Materials/_6___Default/tex_base.outputs:rgb' @ '/World/BoxOnConveyor_1_1/Materials/_6___Default/tex_base'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/06_-_Default_baseColor.jpg'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(1.000, 1.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0.892971'
    * '/World/BoxOnConveyor_1_1/Materials/_6___Default/tex_base' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/06_-_Default_baseColor.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'file' [asset] = '0/06_-_Default_baseColor.jpg'
      * 'st' [float2]
        * Connected: '/World/BoxOnConveyor_1_1/Materials/_6___Default/uvset0.outputs:result' @ '/World/BoxOnConveyor_1_1/Materials/_6___Default/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/BoxOnConveyor_1_1/Materials/_6___Default/uvset0' (ID: 'UsdPrimvarReader_float2')
    * Implementation: 'id'

---

### /World/BoxOnConveyor_1_2/Materials/_6___Default

* **Prim路径 (Prim Path):**/World/BoxOnConveyor_1_2/Materials/_6___Default
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/BoxOnConveyor_1_2/Materials/_6___Default/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/BoxOnConveyor_1_2/Materials/_6___Default/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f]
        * Connected: '/World/BoxOnConveyor_1_2/Materials/_6___Default/tex_base.outputs:rgb' @ '/World/BoxOnConveyor_1_2/Materials/_6___Default/tex_base'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/06_-_Default_baseColor.jpg'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(1.000, 1.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0.892971'
    * '/World/BoxOnConveyor_1_2/Materials/_6___Default/tex_base' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/06_-_Default_baseColor.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'file' [asset] = '0/06_-_Default_baseColor.jpg'
      * 'st' [float2]
        * Connected: '/World/BoxOnConveyor_1_2/Materials/_6___Default/uvset0.outputs:result' @ '/World/BoxOnConveyor_1_2/Materials/_6___Default/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/BoxOnConveyor_1_2/Materials/_6___Default/uvset0' (ID: 'UsdPrimvarReader_float2')
    * Implementation: 'id'

---

### /World/BoxOnConveyor_1_3/Materials/_6___Default

* **Prim路径 (Prim Path):**/World/BoxOnConveyor_1_3/Materials/_6___Default
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/BoxOnConveyor_1_3/Materials/_6___Default/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/BoxOnConveyor_1_3/Materials/_6___Default/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f]
        * Connected: '/World/BoxOnConveyor_1_3/Materials/_6___Default/tex_base.outputs:rgb' @ '/World/BoxOnConveyor_1_3/Materials/_6___Default/tex_base'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/06_-_Default_baseColor.jpg'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(1.000, 1.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0.892971'
    * '/World/BoxOnConveyor_1_3/Materials/_6___Default/tex_base' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/06_-_Default_baseColor.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'file' [asset] = '0/06_-_Default_baseColor.jpg'
      * 'st' [float2]
        * Connected: '/World/BoxOnConveyor_1_3/Materials/_6___Default/uvset0.outputs:result' @ '/World/BoxOnConveyor_1_3/Materials/_6___Default/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/BoxOnConveyor_1_3/Materials/_6___Default/uvset0' (ID: 'UsdPrimvarReader_float2')
    * Implementation: 'id'

---

### /World/BoxOnConveyor_1_4/Materials/_6___Default

* **Prim路径 (Prim Path):**/World/BoxOnConveyor_1_4/Materials/_6___Default
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/BoxOnConveyor_1_4/Materials/_6___Default/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/BoxOnConveyor_1_4/Materials/_6___Default/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f]
        * Connected: '/World/BoxOnConveyor_1_4/Materials/_6___Default/tex_base.outputs:rgb' @ '/World/BoxOnConveyor_1_4/Materials/_6___Default/tex_base'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/06_-_Default_baseColor.jpg'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(1.000, 1.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0.892971'
    * '/World/BoxOnConveyor_1_4/Materials/_6___Default/tex_base' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/06_-_Default_baseColor.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'file' [asset] = '0/06_-_Default_baseColor.jpg'
      * 'st' [float2]
        * Connected: '/World/BoxOnConveyor_1_4/Materials/_6___Default/uvset0.outputs:result' @ '/World/BoxOnConveyor_1_4/Materials/_6___Default/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/BoxOnConveyor_1_4/Materials/_6___Default/uvset0' (ID: 'UsdPrimvarReader_float2')
    * Implementation: 'id'

---

### /World/BoxOnConveyor_1_5/Materials/_6___Default

* **Prim路径 (Prim Path):**/World/BoxOnConveyor_1_5/Materials/_6___Default
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/BoxOnConveyor_1_5/Materials/_6___Default/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/BoxOnConveyor_1_5/Materials/_6___Default/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f]
        * Connected: '/World/BoxOnConveyor_1_5/Materials/_6___Default/tex_base.outputs:rgb' @ '/World/BoxOnConveyor_1_5/Materials/_6___Default/tex_base'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/06_-_Default_baseColor.jpg'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(1.000, 1.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0.892971'
    * '/World/BoxOnConveyor_1_5/Materials/_6___Default/tex_base' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/06_-_Default_baseColor.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'file' [asset] = '0/06_-_Default_baseColor.jpg'
      * 'st' [float2]
        * Connected: '/World/BoxOnConveyor_1_5/Materials/_6___Default/uvset0.outputs:result' @ '/World/BoxOnConveyor_1_5/Materials/_6___Default/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/BoxOnConveyor_1_5/Materials/_6___Default/uvset0' (ID: 'UsdPrimvarReader_float2')
    * Implementation: 'id'

---

### /World/BoxOnConveyor_1_6/Materials/_6___Default

* **Prim路径 (Prim Path):**/World/BoxOnConveyor_1_6/Materials/_6___Default
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/BoxOnConveyor_1_6/Materials/_6___Default/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/BoxOnConveyor_1_6/Materials/_6___Default/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f]
        * Connected: '/World/BoxOnConveyor_1_6/Materials/_6___Default/tex_base.outputs:rgb' @ '/World/BoxOnConveyor_1_6/Materials/_6___Default/tex_base'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/06_-_Default_baseColor.jpg'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(1.000, 1.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0.892971'
    * '/World/BoxOnConveyor_1_6/Materials/_6___Default/tex_base' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/06_-_Default_baseColor.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'file' [asset] = '0/06_-_Default_baseColor.jpg'
      * 'st' [float2]
        * Connected: '/World/BoxOnConveyor_1_6/Materials/_6___Default/uvset0.outputs:result' @ '/World/BoxOnConveyor_1_6/Materials/_6___Default/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/BoxOnConveyor_1_6/Materials/_6___Default/uvset0' (ID: 'UsdPrimvarReader_float2')
    * Implementation: 'id'

---

### /World/BoxOnConveyor_1_7/Materials/_6___Default

* **Prim路径 (Prim Path):**/World/BoxOnConveyor_1_7/Materials/_6___Default
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/BoxOnConveyor_1_7/Materials/_6___Default/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/BoxOnConveyor_1_7/Materials/_6___Default/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f]
        * Connected: '/World/BoxOnConveyor_1_7/Materials/_6___Default/tex_base.outputs:rgb' @ '/World/BoxOnConveyor_1_7/Materials/_6___Default/tex_base'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/06_-_Default_baseColor.jpg'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(1.000, 1.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0.892971'
    * '/World/BoxOnConveyor_1_7/Materials/_6___Default/tex_base' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/06_-_Default_baseColor.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'file' [asset] = '0/06_-_Default_baseColor.jpg'
      * 'st' [float2]
        * Connected: '/World/BoxOnConveyor_1_7/Materials/_6___Default/uvset0.outputs:result' @ '/World/BoxOnConveyor_1_7/Materials/_6___Default/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/BoxOnConveyor_1_7/Materials/_6___Default/uvset0' (ID: 'UsdPrimvarReader_float2')
    * Implementation: 'id'

---

### /World/BoxOnConveyor_1_8/Materials/_6___Default

* **Prim路径 (Prim Path):**/World/BoxOnConveyor_1_8/Materials/_6___Default
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/BoxOnConveyor_1_8/Materials/_6___Default/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/BoxOnConveyor_1_8/Materials/_6___Default/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f]
        * Connected: '/World/BoxOnConveyor_1_8/Materials/_6___Default/tex_base.outputs:rgb' @ '/World/BoxOnConveyor_1_8/Materials/_6___Default/tex_base'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/06_-_Default_baseColor.jpg'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(1.000, 1.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0.892971'
    * '/World/BoxOnConveyor_1_8/Materials/_6___Default/tex_base' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/06_-_Default_baseColor.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'file' [asset] = '0/06_-_Default_baseColor.jpg'
      * 'st' [float2]
        * Connected: '/World/BoxOnConveyor_1_8/Materials/_6___Default/uvset0.outputs:result' @ '/World/BoxOnConveyor_1_8/Materials/_6___Default/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/BoxOnConveyor_1_8/Materials/_6___Default/uvset0' (ID: 'UsdPrimvarReader_float2')
    * Implementation: 'id'

---

### /World/BoxOnConveyor_2_1/Materials/_6___Default

* **Prim路径 (Prim Path):**/World/BoxOnConveyor_2_1/Materials/_6___Default
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/BoxOnConveyor_2_1/Materials/_6___Default/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/BoxOnConveyor_2_1/Materials/_6___Default/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f]
        * Connected: '/World/BoxOnConveyor_2_1/Materials/_6___Default/tex_base.outputs:rgb' @ '/World/BoxOnConveyor_2_1/Materials/_6___Default/tex_base'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/06_-_Default_baseColor.jpg'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(1.000, 1.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0.892971'
    * '/World/BoxOnConveyor_2_1/Materials/_6___Default/tex_base' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/06_-_Default_baseColor.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'file' [asset] = '0/06_-_Default_baseColor.jpg'
      * 'st' [float2]
        * Connected: '/World/BoxOnConveyor_2_1/Materials/_6___Default/uvset0.outputs:result' @ '/World/BoxOnConveyor_2_1/Materials/_6___Default/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/BoxOnConveyor_2_1/Materials/_6___Default/uvset0' (ID: 'UsdPrimvarReader_float2')
    * Implementation: 'id'

---

### /World/BoxOnConveyor_2_2/Materials/_6___Default

* **Prim路径 (Prim Path):**/World/BoxOnConveyor_2_2/Materials/_6___Default
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/BoxOnConveyor_2_2/Materials/_6___Default/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/BoxOnConveyor_2_2/Materials/_6___Default/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f]
        * Connected: '/World/BoxOnConveyor_2_2/Materials/_6___Default/tex_base.outputs:rgb' @ '/World/BoxOnConveyor_2_2/Materials/_6___Default/tex_base'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/06_-_Default_baseColor.jpg'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(1.000, 1.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0.892971'
    * '/World/BoxOnConveyor_2_2/Materials/_6___Default/tex_base' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/06_-_Default_baseColor.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'file' [asset] = '0/06_-_Default_baseColor.jpg'
      * 'st' [float2]
        * Connected: '/World/BoxOnConveyor_2_2/Materials/_6___Default/uvset0.outputs:result' @ '/World/BoxOnConveyor_2_2/Materials/_6___Default/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/BoxOnConveyor_2_2/Materials/_6___Default/uvset0' (ID: 'UsdPrimvarReader_float2')
    * Implementation: 'id'

---

### /World/BoxOnConveyor_2_3/Materials/_6___Default

* **Prim路径 (Prim Path):**/World/BoxOnConveyor_2_3/Materials/_6___Default
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/BoxOnConveyor_2_3/Materials/_6___Default/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/BoxOnConveyor_2_3/Materials/_6___Default/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f]
        * Connected: '/World/BoxOnConveyor_2_3/Materials/_6___Default/tex_base.outputs:rgb' @ '/World/BoxOnConveyor_2_3/Materials/_6___Default/tex_base'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/06_-_Default_baseColor.jpg'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(1.000, 1.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0.892971'
    * '/World/BoxOnConveyor_2_3/Materials/_6___Default/tex_base' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/06_-_Default_baseColor.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'file' [asset] = '0/06_-_Default_baseColor.jpg'
      * 'st' [float2]
        * Connected: '/World/BoxOnConveyor_2_3/Materials/_6___Default/uvset0.outputs:result' @ '/World/BoxOnConveyor_2_3/Materials/_6___Default/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/BoxOnConveyor_2_3/Materials/_6___Default/uvset0' (ID: 'UsdPrimvarReader_float2')
    * Implementation: 'id'

---

### /World/BoxOnConveyor_2_4/Materials/_6___Default

* **Prim路径 (Prim Path):**/World/BoxOnConveyor_2_4/Materials/_6___Default
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/BoxOnConveyor_2_4/Materials/_6___Default/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/BoxOnConveyor_2_4/Materials/_6___Default/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f]
        * Connected: '/World/BoxOnConveyor_2_4/Materials/_6___Default/tex_base.outputs:rgb' @ '/World/BoxOnConveyor_2_4/Materials/_6___Default/tex_base'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/06_-_Default_baseColor.jpg'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(1.000, 1.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0.892971'
    * '/World/BoxOnConveyor_2_4/Materials/_6___Default/tex_base' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/06_-_Default_baseColor.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'file' [asset] = '0/06_-_Default_baseColor.jpg'
      * 'st' [float2]
        * Connected: '/World/BoxOnConveyor_2_4/Materials/_6___Default/uvset0.outputs:result' @ '/World/BoxOnConveyor_2_4/Materials/_6___Default/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/BoxOnConveyor_2_4/Materials/_6___Default/uvset0' (ID: 'UsdPrimvarReader_float2')
    * Implementation: 'id'

---

### /World/BoxOnConveyor_2_5/Materials/_6___Default

* **Prim路径 (Prim Path):**/World/BoxOnConveyor_2_5/Materials/_6___Default
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/BoxOnConveyor_2_5/Materials/_6___Default/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/BoxOnConveyor_2_5/Materials/_6___Default/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f]
        * Connected: '/World/BoxOnConveyor_2_5/Materials/_6___Default/tex_base.outputs:rgb' @ '/World/BoxOnConveyor_2_5/Materials/_6___Default/tex_base'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/06_-_Default_baseColor.jpg'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(1.000, 1.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0.892971'
    * '/World/BoxOnConveyor_2_5/Materials/_6___Default/tex_base' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/06_-_Default_baseColor.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'file' [asset] = '0/06_-_Default_baseColor.jpg'
      * 'st' [float2]
        * Connected: '/World/BoxOnConveyor_2_5/Materials/_6___Default/uvset0.outputs:result' @ '/World/BoxOnConveyor_2_5/Materials/_6___Default/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/BoxOnConveyor_2_5/Materials/_6___Default/uvset0' (ID: 'UsdPrimvarReader_float2')
    * Implementation: 'id'

---

### /World/BoxOnConveyor_2_6/Materials/_6___Default

* **Prim路径 (Prim Path):**/World/BoxOnConveyor_2_6/Materials/_6___Default
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/BoxOnConveyor_2_6/Materials/_6___Default/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/BoxOnConveyor_2_6/Materials/_6___Default/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f]
        * Connected: '/World/BoxOnConveyor_2_6/Materials/_6___Default/tex_base.outputs:rgb' @ '/World/BoxOnConveyor_2_6/Materials/_6___Default/tex_base'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/06_-_Default_baseColor.jpg'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(1.000, 1.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0.892971'
    * '/World/BoxOnConveyor_2_6/Materials/_6___Default/tex_base' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/06_-_Default_baseColor.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'file' [asset] = '0/06_-_Default_baseColor.jpg'
      * 'st' [float2]
        * Connected: '/World/BoxOnConveyor_2_6/Materials/_6___Default/uvset0.outputs:result' @ '/World/BoxOnConveyor_2_6/Materials/_6___Default/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/BoxOnConveyor_2_6/Materials/_6___Default/uvset0' (ID: 'UsdPrimvarReader_float2')
    * Implementation: 'id'

---

### /World/BoxOnConveyor_2_7/Materials/_6___Default

* **Prim路径 (Prim Path):**/World/BoxOnConveyor_2_7/Materials/_6___Default
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/BoxOnConveyor_2_7/Materials/_6___Default/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/BoxOnConveyor_2_7/Materials/_6___Default/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f]
        * Connected: '/World/BoxOnConveyor_2_7/Materials/_6___Default/tex_base.outputs:rgb' @ '/World/BoxOnConveyor_2_7/Materials/_6___Default/tex_base'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/06_-_Default_baseColor.jpg'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(1.000, 1.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0.892971'
    * '/World/BoxOnConveyor_2_7/Materials/_6___Default/tex_base' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/06_-_Default_baseColor.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'file' [asset] = '0/06_-_Default_baseColor.jpg'
      * 'st' [float2]
        * Connected: '/World/BoxOnConveyor_2_7/Materials/_6___Default/uvset0.outputs:result' @ '/World/BoxOnConveyor_2_7/Materials/_6___Default/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/BoxOnConveyor_2_7/Materials/_6___Default/uvset0' (ID: 'UsdPrimvarReader_float2')
    * Implementation: 'id'

---

### /World/BoxOnConveyor_2_8/Materials/_6___Default

* **Prim路径 (Prim Path):**/World/BoxOnConveyor_2_8/Materials/_6___Default
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/BoxOnConveyor_2_8/Materials/_6___Default/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/BoxOnConveyor_2_8/Materials/_6___Default/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f]
        * Connected: '/World/BoxOnConveyor_2_8/Materials/_6___Default/tex_base.outputs:rgb' @ '/World/BoxOnConveyor_2_8/Materials/_6___Default/tex_base'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/06_-_Default_baseColor.jpg'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(1.000, 1.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0.892971'
    * '/World/BoxOnConveyor_2_8/Materials/_6___Default/tex_base' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/06_-_Default_baseColor.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'file' [asset] = '0/06_-_Default_baseColor.jpg'
      * 'st' [float2]
        * Connected: '/World/BoxOnConveyor_2_8/Materials/_6___Default/uvset0.outputs:result' @ '/World/BoxOnConveyor_2_8/Materials/_6___Default/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/BoxOnConveyor_2_8/Materials/_6___Default/uvset0' (ID: 'UsdPrimvarReader_float2')
    * Implementation: 'id'

---

### /World/BoxOnConveyor_3_1/Materials/_6___Default

* **Prim路径 (Prim Path):**/World/BoxOnConveyor_3_1/Materials/_6___Default
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/BoxOnConveyor_3_1/Materials/_6___Default/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/BoxOnConveyor_3_1/Materials/_6___Default/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f]
        * Connected: '/World/BoxOnConveyor_3_1/Materials/_6___Default/tex_base.outputs:rgb' @ '/World/BoxOnConveyor_3_1/Materials/_6___Default/tex_base'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/06_-_Default_baseColor.jpg'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(1.000, 1.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0.892971'
    * '/World/BoxOnConveyor_3_1/Materials/_6___Default/tex_base' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/06_-_Default_baseColor.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'file' [asset] = '0/06_-_Default_baseColor.jpg'
      * 'st' [float2]
        * Connected: '/World/BoxOnConveyor_3_1/Materials/_6___Default/uvset0.outputs:result' @ '/World/BoxOnConveyor_3_1/Materials/_6___Default/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/BoxOnConveyor_3_1/Materials/_6___Default/uvset0' (ID: 'UsdPrimvarReader_float2')
    * Implementation: 'id'

---

### /World/BoxOnConveyor_3_2/Materials/_6___Default

* **Prim路径 (Prim Path):**/World/BoxOnConveyor_3_2/Materials/_6___Default
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/BoxOnConveyor_3_2/Materials/_6___Default/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/BoxOnConveyor_3_2/Materials/_6___Default/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f]
        * Connected: '/World/BoxOnConveyor_3_2/Materials/_6___Default/tex_base.outputs:rgb' @ '/World/BoxOnConveyor_3_2/Materials/_6___Default/tex_base'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/06_-_Default_baseColor.jpg'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(1.000, 1.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0.892971'
    * '/World/BoxOnConveyor_3_2/Materials/_6___Default/tex_base' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/06_-_Default_baseColor.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'file' [asset] = '0/06_-_Default_baseColor.jpg'
      * 'st' [float2]
        * Connected: '/World/BoxOnConveyor_3_2/Materials/_6___Default/uvset0.outputs:result' @ '/World/BoxOnConveyor_3_2/Materials/_6___Default/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/BoxOnConveyor_3_2/Materials/_6___Default/uvset0' (ID: 'UsdPrimvarReader_float2')
    * Implementation: 'id'

---

### /World/BoxOnConveyor_3_3/Materials/_6___Default

* **Prim路径 (Prim Path):**/World/BoxOnConveyor_3_3/Materials/_6___Default
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/BoxOnConveyor_3_3/Materials/_6___Default/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/BoxOnConveyor_3_3/Materials/_6___Default/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f]
        * Connected: '/World/BoxOnConveyor_3_3/Materials/_6___Default/tex_base.outputs:rgb' @ '/World/BoxOnConveyor_3_3/Materials/_6___Default/tex_base'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/06_-_Default_baseColor.jpg'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(1.000, 1.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0.892971'
    * '/World/BoxOnConveyor_3_3/Materials/_6___Default/tex_base' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/06_-_Default_baseColor.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'file' [asset] = '0/06_-_Default_baseColor.jpg'
      * 'st' [float2]
        * Connected: '/World/BoxOnConveyor_3_3/Materials/_6___Default/uvset0.outputs:result' @ '/World/BoxOnConveyor_3_3/Materials/_6___Default/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/BoxOnConveyor_3_3/Materials/_6___Default/uvset0' (ID: 'UsdPrimvarReader_float2')
    * Implementation: 'id'

---

### /World/BoxOnConveyor_3_4/Materials/_6___Default

* **Prim路径 (Prim Path):**/World/BoxOnConveyor_3_4/Materials/_6___Default
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/BoxOnConveyor_3_4/Materials/_6___Default/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/BoxOnConveyor_3_4/Materials/_6___Default/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f]
        * Connected: '/World/BoxOnConveyor_3_4/Materials/_6___Default/tex_base.outputs:rgb' @ '/World/BoxOnConveyor_3_4/Materials/_6___Default/tex_base'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/06_-_Default_baseColor.jpg'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(1.000, 1.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0.892971'
    * '/World/BoxOnConveyor_3_4/Materials/_6___Default/tex_base' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/06_-_Default_baseColor.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'file' [asset] = '0/06_-_Default_baseColor.jpg'
      * 'st' [float2]
        * Connected: '/World/BoxOnConveyor_3_4/Materials/_6___Default/uvset0.outputs:result' @ '/World/BoxOnConveyor_3_4/Materials/_6___Default/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/BoxOnConveyor_3_4/Materials/_6___Default/uvset0' (ID: 'UsdPrimvarReader_float2')
    * Implementation: 'id'

---

### /World/BoxOnConveyor_3_5/Materials/_6___Default

* **Prim路径 (Prim Path):**/World/BoxOnConveyor_3_5/Materials/_6___Default
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/BoxOnConveyor_3_5/Materials/_6___Default/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/BoxOnConveyor_3_5/Materials/_6___Default/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f]
        * Connected: '/World/BoxOnConveyor_3_5/Materials/_6___Default/tex_base.outputs:rgb' @ '/World/BoxOnConveyor_3_5/Materials/_6___Default/tex_base'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/06_-_Default_baseColor.jpg'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(1.000, 1.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0.892971'
    * '/World/BoxOnConveyor_3_5/Materials/_6___Default/tex_base' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/06_-_Default_baseColor.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'file' [asset] = '0/06_-_Default_baseColor.jpg'
      * 'st' [float2]
        * Connected: '/World/BoxOnConveyor_3_5/Materials/_6___Default/uvset0.outputs:result' @ '/World/BoxOnConveyor_3_5/Materials/_6___Default/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/BoxOnConveyor_3_5/Materials/_6___Default/uvset0' (ID: 'UsdPrimvarReader_float2')
    * Implementation: 'id'

---

### /World/BoxOnConveyor_3_6/Materials/_6___Default

* **Prim路径 (Prim Path):**/World/BoxOnConveyor_3_6/Materials/_6___Default
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/BoxOnConveyor_3_6/Materials/_6___Default/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/BoxOnConveyor_3_6/Materials/_6___Default/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f]
        * Connected: '/World/BoxOnConveyor_3_6/Materials/_6___Default/tex_base.outputs:rgb' @ '/World/BoxOnConveyor_3_6/Materials/_6___Default/tex_base'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/06_-_Default_baseColor.jpg'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(1.000, 1.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0.892971'
    * '/World/BoxOnConveyor_3_6/Materials/_6___Default/tex_base' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/06_-_Default_baseColor.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'file' [asset] = '0/06_-_Default_baseColor.jpg'
      * 'st' [float2]
        * Connected: '/World/BoxOnConveyor_3_6/Materials/_6___Default/uvset0.outputs:result' @ '/World/BoxOnConveyor_3_6/Materials/_6___Default/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/BoxOnConveyor_3_6/Materials/_6___Default/uvset0' (ID: 'UsdPrimvarReader_float2')
    * Implementation: 'id'

---

### /World/BoxOnConveyor_3_7/Materials/_6___Default

* **Prim路径 (Prim Path):**/World/BoxOnConveyor_3_7/Materials/_6___Default
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/BoxOnConveyor_3_7/Materials/_6___Default/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/BoxOnConveyor_3_7/Materials/_6___Default/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f]
        * Connected: '/World/BoxOnConveyor_3_7/Materials/_6___Default/tex_base.outputs:rgb' @ '/World/BoxOnConveyor_3_7/Materials/_6___Default/tex_base'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/06_-_Default_baseColor.jpg'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(1.000, 1.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0.892971'
    * '/World/BoxOnConveyor_3_7/Materials/_6___Default/tex_base' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/06_-_Default_baseColor.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'file' [asset] = '0/06_-_Default_baseColor.jpg'
      * 'st' [float2]
        * Connected: '/World/BoxOnConveyor_3_7/Materials/_6___Default/uvset0.outputs:result' @ '/World/BoxOnConveyor_3_7/Materials/_6___Default/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/BoxOnConveyor_3_7/Materials/_6___Default/uvset0' (ID: 'UsdPrimvarReader_float2')
    * Implementation: 'id'

---

### /World/BoxOnConveyor_3_8/Materials/_6___Default

* **Prim路径 (Prim Path):**/World/BoxOnConveyor_3_8/Materials/_6___Default
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/BoxOnConveyor_3_8/Materials/_6___Default/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/BoxOnConveyor_3_8/Materials/_6___Default/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f]
        * Connected: '/World/BoxOnConveyor_3_8/Materials/_6___Default/tex_base.outputs:rgb' @ '/World/BoxOnConveyor_3_8/Materials/_6___Default/tex_base'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/06_-_Default_baseColor.jpg'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(1.000, 1.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0.892971'
    * '/World/BoxOnConveyor_3_8/Materials/_6___Default/tex_base' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/06_-_Default_baseColor.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'file' [asset] = '0/06_-_Default_baseColor.jpg'
      * 'st' [float2]
        * Connected: '/World/BoxOnConveyor_3_8/Materials/_6___Default/uvset0.outputs:result' @ '/World/BoxOnConveyor_3_8/Materials/_6___Default/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/BoxOnConveyor_3_8/Materials/_6___Default/uvset0' (ID: 'UsdPrimvarReader_float2')
    * Implementation: 'id'

---

### /World/StackedCarton_1/Materials/_6___Default

* **Prim路径 (Prim Path):**/World/StackedCarton_1/Materials/_6___Default
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/StackedCarton_1/Materials/_6___Default/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/StackedCarton_1/Materials/_6___Default/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f]
        * Connected: '/World/StackedCarton_1/Materials/_6___Default/tex_base.outputs:rgb' @ '/World/StackedCarton_1/Materials/_6___Default/tex_base'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/06_-_Default_baseColor.jpg'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(1.000, 1.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0.892971'
    * '/World/StackedCarton_1/Materials/_6___Default/tex_base' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/06_-_Default_baseColor.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'file' [asset] = '0/06_-_Default_baseColor.jpg'
      * 'st' [float2]
        * Connected: '/World/StackedCarton_1/Materials/_6___Default/uvset0.outputs:result' @ '/World/StackedCarton_1/Materials/_6___Default/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/StackedCarton_1/Materials/_6___Default/uvset0' (ID: 'UsdPrimvarReader_float2')
    * Implementation: 'id'

---

### /World/StackedCarton_2/Materials/_6___Default

* **Prim路径 (Prim Path):**/World/StackedCarton_2/Materials/_6___Default
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/StackedCarton_2/Materials/_6___Default/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/StackedCarton_2/Materials/_6___Default/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f]
        * Connected: '/World/StackedCarton_2/Materials/_6___Default/tex_base.outputs:rgb' @ '/World/StackedCarton_2/Materials/_6___Default/tex_base'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/06_-_Default_baseColor.jpg'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(1.000, 1.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0.892971'
    * '/World/StackedCarton_2/Materials/_6___Default/tex_base' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/06_-_Default_baseColor.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'file' [asset] = '0/06_-_Default_baseColor.jpg'
      * 'st' [float2]
        * Connected: '/World/StackedCarton_2/Materials/_6___Default/uvset0.outputs:result' @ '/World/StackedCarton_2/Materials/_6___Default/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/StackedCarton_2/Materials/_6___Default/uvset0' (ID: 'UsdPrimvarReader_float2')
    * Implementation: 'id'

---

### /World/StackedCarton_3/Materials/_6___Default

* **Prim路径 (Prim Path):**/World/StackedCarton_3/Materials/_6___Default
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/StackedCarton_3/Materials/_6___Default/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/StackedCarton_3/Materials/_6___Default/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f]
        * Connected: '/World/StackedCarton_3/Materials/_6___Default/tex_base.outputs:rgb' @ '/World/StackedCarton_3/Materials/_6___Default/tex_base'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/06_-_Default_baseColor.jpg'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(1.000, 1.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0.892971'
    * '/World/StackedCarton_3/Materials/_6___Default/tex_base' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/06_-_Default_baseColor.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'file' [asset] = '0/06_-_Default_baseColor.jpg'
      * 'st' [float2]
        * Connected: '/World/StackedCarton_3/Materials/_6___Default/uvset0.outputs:result' @ '/World/StackedCarton_3/Materials/_6___Default/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/StackedCarton_3/Materials/_6___Default/uvset0' (ID: 'UsdPrimvarReader_float2')
    * Implementation: 'id'

---

### /World/StackedCarton_4/Materials/_6___Default

* **Prim路径 (Prim Path):**/World/StackedCarton_4/Materials/_6___Default
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/StackedCarton_4/Materials/_6___Default/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/StackedCarton_4/Materials/_6___Default/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f]
        * Connected: '/World/StackedCarton_4/Materials/_6___Default/tex_base.outputs:rgb' @ '/World/StackedCarton_4/Materials/_6___Default/tex_base'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/06_-_Default_baseColor.jpg'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(1.000, 1.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0.892971'
    * '/World/StackedCarton_4/Materials/_6___Default/tex_base' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/06_-_Default_baseColor.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'file' [asset] = '0/06_-_Default_baseColor.jpg'
      * 'st' [float2]
        * Connected: '/World/StackedCarton_4/Materials/_6___Default/uvset0.outputs:result' @ '/World/StackedCarton_4/Materials/_6___Default/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/StackedCarton_4/Materials/_6___Default/uvset0' (ID: 'UsdPrimvarReader_float2')
    * Implementation: 'id'

---

### /World/StackedCarton_5/Materials/_6___Default

* **Prim路径 (Prim Path):**/World/StackedCarton_5/Materials/_6___Default
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/StackedCarton_5/Materials/_6___Default/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/StackedCarton_5/Materials/_6___Default/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f]
        * Connected: '/World/StackedCarton_5/Materials/_6___Default/tex_base.outputs:rgb' @ '/World/StackedCarton_5/Materials/_6___Default/tex_base'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/06_-_Default_baseColor.jpg'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(1.000, 1.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0.892971'
    * '/World/StackedCarton_5/Materials/_6___Default/tex_base' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/06_-_Default_baseColor.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'file' [asset] = '0/06_-_Default_baseColor.jpg'
      * 'st' [float2]
        * Connected: '/World/StackedCarton_5/Materials/_6___Default/uvset0.outputs:result' @ '/World/StackedCarton_5/Materials/_6___Default/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/StackedCarton_5/Materials/_6___Default/uvset0' (ID: 'UsdPrimvarReader_float2')
    * Implementation: 'id'

---

### /World/StackedCarton_6/Materials/_6___Default

* **Prim路径 (Prim Path):**/World/StackedCarton_6/Materials/_6___Default
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/StackedCarton_6/Materials/_6___Default/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/StackedCarton_6/Materials/_6___Default/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f]
        * Connected: '/World/StackedCarton_6/Materials/_6___Default/tex_base.outputs:rgb' @ '/World/StackedCarton_6/Materials/_6___Default/tex_base'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/06_-_Default_baseColor.jpg'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(1.000, 1.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0.892971'
    * '/World/StackedCarton_6/Materials/_6___Default/tex_base' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/06_-_Default_baseColor.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'file' [asset] = '0/06_-_Default_baseColor.jpg'
      * 'st' [float2]
        * Connected: '/World/StackedCarton_6/Materials/_6___Default/uvset0.outputs:result' @ '/World/StackedCarton_6/Materials/_6___Default/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/StackedCarton_6/Materials/_6___Default/uvset0' (ID: 'UsdPrimvarReader_float2')
    * Implementation: 'id'

---

### /World/StackedCarton_7/Materials/_6___Default

* **Prim路径 (Prim Path):**/World/StackedCarton_7/Materials/_6___Default
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/StackedCarton_7/Materials/_6___Default/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/StackedCarton_7/Materials/_6___Default/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f]
        * Connected: '/World/StackedCarton_7/Materials/_6___Default/tex_base.outputs:rgb' @ '/World/StackedCarton_7/Materials/_6___Default/tex_base'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/06_-_Default_baseColor.jpg'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(1.000, 1.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0.892971'
    * '/World/StackedCarton_7/Materials/_6___Default/tex_base' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/06_-_Default_baseColor.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'file' [asset] = '0/06_-_Default_baseColor.jpg'
      * 'st' [float2]
        * Connected: '/World/StackedCarton_7/Materials/_6___Default/uvset0.outputs:result' @ '/World/StackedCarton_7/Materials/_6___Default/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/StackedCarton_7/Materials/_6___Default/uvset0' (ID: 'UsdPrimvarReader_float2')
    * Implementation: 'id'

---

### /World/StackedCarton_8/Materials/_6___Default

* **Prim路径 (Prim Path):**/World/StackedCarton_8/Materials/_6___Default
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/StackedCarton_8/Materials/_6___Default/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/StackedCarton_8/Materials/_6___Default/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f]
        * Connected: '/World/StackedCarton_8/Materials/_6___Default/tex_base.outputs:rgb' @ '/World/StackedCarton_8/Materials/_6___Default/tex_base'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/06_-_Default_baseColor.jpg'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(1.000, 1.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0.892971'
    * '/World/StackedCarton_8/Materials/_6___Default/tex_base' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/06_-_Default_baseColor.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'file' [asset] = '0/06_-_Default_baseColor.jpg'
      * 'st' [float2]
        * Connected: '/World/StackedCarton_8/Materials/_6___Default/uvset0.outputs:result' @ '/World/StackedCarton_8/Materials/_6___Default/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/StackedCarton_8/Materials/_6___Default/uvset0' (ID: 'UsdPrimvarReader_float2')
    * Implementation: 'id'

---

### /World/StackedCarton_1_1/Materials/_6___Default

* **Prim路径 (Prim Path):**/World/StackedCarton_1_1/Materials/_6___Default
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/StackedCarton_1_1/Materials/_6___Default/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/StackedCarton_1_1/Materials/_6___Default/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f]
        * Connected: '/World/StackedCarton_1_1/Materials/_6___Default/tex_base.outputs:rgb' @ '/World/StackedCarton_1_1/Materials/_6___Default/tex_base'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/06_-_Default_baseColor.jpg'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(1.000, 1.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0.892971'
    * '/World/StackedCarton_1_1/Materials/_6___Default/tex_base' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/06_-_Default_baseColor.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'file' [asset] = '0/06_-_Default_baseColor.jpg'
      * 'st' [float2]
        * Connected: '/World/StackedCarton_1_1/Materials/_6___Default/uvset0.outputs:result' @ '/World/StackedCarton_1_1/Materials/_6___Default/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/StackedCarton_1_1/Materials/_6___Default/uvset0' (ID: 'UsdPrimvarReader_float2')
    * Implementation: 'id'

---

### /World/StackedCarton_1_2/Materials/_6___Default

* **Prim路径 (Prim Path):**/World/StackedCarton_1_2/Materials/_6___Default
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/StackedCarton_1_2/Materials/_6___Default/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/StackedCarton_1_2/Materials/_6___Default/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f]
        * Connected: '/World/StackedCarton_1_2/Materials/_6___Default/tex_base.outputs:rgb' @ '/World/StackedCarton_1_2/Materials/_6___Default/tex_base'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/06_-_Default_baseColor.jpg'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(1.000, 1.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0.892971'
    * '/World/StackedCarton_1_2/Materials/_6___Default/tex_base' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/06_-_Default_baseColor.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'file' [asset] = '0/06_-_Default_baseColor.jpg'
      * 'st' [float2]
        * Connected: '/World/StackedCarton_1_2/Materials/_6___Default/uvset0.outputs:result' @ '/World/StackedCarton_1_2/Materials/_6___Default/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/StackedCarton_1_2/Materials/_6___Default/uvset0' (ID: 'UsdPrimvarReader_float2')
    * Implementation: 'id'

---

### /World/StackedCarton_1_3/Materials/_6___Default

* **Prim路径 (Prim Path):**/World/StackedCarton_1_3/Materials/_6___Default
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/StackedCarton_1_3/Materials/_6___Default/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/StackedCarton_1_3/Materials/_6___Default/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f]
        * Connected: '/World/StackedCarton_1_3/Materials/_6___Default/tex_base.outputs:rgb' @ '/World/StackedCarton_1_3/Materials/_6___Default/tex_base'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/06_-_Default_baseColor.jpg'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(1.000, 1.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0.892971'
    * '/World/StackedCarton_1_3/Materials/_6___Default/tex_base' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/06_-_Default_baseColor.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'file' [asset] = '0/06_-_Default_baseColor.jpg'
      * 'st' [float2]
        * Connected: '/World/StackedCarton_1_3/Materials/_6___Default/uvset0.outputs:result' @ '/World/StackedCarton_1_3/Materials/_6___Default/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/StackedCarton_1_3/Materials/_6___Default/uvset0' (ID: 'UsdPrimvarReader_float2')
    * Implementation: 'id'

---

### /World/StackedCarton_1_4/Materials/_6___Default

* **Prim路径 (Prim Path):**/World/StackedCarton_1_4/Materials/_6___Default
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/StackedCarton_1_4/Materials/_6___Default/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/StackedCarton_1_4/Materials/_6___Default/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f]
        * Connected: '/World/StackedCarton_1_4/Materials/_6___Default/tex_base.outputs:rgb' @ '/World/StackedCarton_1_4/Materials/_6___Default/tex_base'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/06_-_Default_baseColor.jpg'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(1.000, 1.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0.892971'
    * '/World/StackedCarton_1_4/Materials/_6___Default/tex_base' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/06_-_Default_baseColor.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'file' [asset] = '0/06_-_Default_baseColor.jpg'
      * 'st' [float2]
        * Connected: '/World/StackedCarton_1_4/Materials/_6___Default/uvset0.outputs:result' @ '/World/StackedCarton_1_4/Materials/_6___Default/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/StackedCarton_1_4/Materials/_6___Default/uvset0' (ID: 'UsdPrimvarReader_float2')
    * Implementation: 'id'

---

### /World/StackedCarton_1_5/Materials/_6___Default

* **Prim路径 (Prim Path):**/World/StackedCarton_1_5/Materials/_6___Default
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/StackedCarton_1_5/Materials/_6___Default/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/StackedCarton_1_5/Materials/_6___Default/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f]
        * Connected: '/World/StackedCarton_1_5/Materials/_6___Default/tex_base.outputs:rgb' @ '/World/StackedCarton_1_5/Materials/_6___Default/tex_base'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/06_-_Default_baseColor.jpg'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(1.000, 1.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0.892971'
    * '/World/StackedCarton_1_5/Materials/_6___Default/tex_base' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/06_-_Default_baseColor.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'file' [asset] = '0/06_-_Default_baseColor.jpg'
      * 'st' [float2]
        * Connected: '/World/StackedCarton_1_5/Materials/_6___Default/uvset0.outputs:result' @ '/World/StackedCarton_1_5/Materials/_6___Default/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/StackedCarton_1_5/Materials/_6___Default/uvset0' (ID: 'UsdPrimvarReader_float2')
    * Implementation: 'id'

---

### /World/StackedCarton_1_6/Materials/_6___Default

* **Prim路径 (Prim Path):**/World/StackedCarton_1_6/Materials/_6___Default
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/StackedCarton_1_6/Materials/_6___Default/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/StackedCarton_1_6/Materials/_6___Default/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f]
        * Connected: '/World/StackedCarton_1_6/Materials/_6___Default/tex_base.outputs:rgb' @ '/World/StackedCarton_1_6/Materials/_6___Default/tex_base'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/06_-_Default_baseColor.jpg'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(1.000, 1.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0.892971'
    * '/World/StackedCarton_1_6/Materials/_6___Default/tex_base' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/06_-_Default_baseColor.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'file' [asset] = '0/06_-_Default_baseColor.jpg'
      * 'st' [float2]
        * Connected: '/World/StackedCarton_1_6/Materials/_6___Default/uvset0.outputs:result' @ '/World/StackedCarton_1_6/Materials/_6___Default/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/StackedCarton_1_6/Materials/_6___Default/uvset0' (ID: 'UsdPrimvarReader_float2')
    * Implementation: 'id'

---

### /World/StackedCarton_1_7/Materials/_6___Default

* **Prim路径 (Prim Path):**/World/StackedCarton_1_7/Materials/_6___Default
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/StackedCarton_1_7/Materials/_6___Default/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/StackedCarton_1_7/Materials/_6___Default/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f]
        * Connected: '/World/StackedCarton_1_7/Materials/_6___Default/tex_base.outputs:rgb' @ '/World/StackedCarton_1_7/Materials/_6___Default/tex_base'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/06_-_Default_baseColor.jpg'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(1.000, 1.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0.892971'
    * '/World/StackedCarton_1_7/Materials/_6___Default/tex_base' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/06_-_Default_baseColor.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'file' [asset] = '0/06_-_Default_baseColor.jpg'
      * 'st' [float2]
        * Connected: '/World/StackedCarton_1_7/Materials/_6___Default/uvset0.outputs:result' @ '/World/StackedCarton_1_7/Materials/_6___Default/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/StackedCarton_1_7/Materials/_6___Default/uvset0' (ID: 'UsdPrimvarReader_float2')
    * Implementation: 'id'

---

### /World/StackedCarton_1_8/Materials/_6___Default

* **Prim路径 (Prim Path):**/World/StackedCarton_1_8/Materials/_6___Default
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/StackedCarton_1_8/Materials/_6___Default/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/StackedCarton_1_8/Materials/_6___Default/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f]
        * Connected: '/World/StackedCarton_1_8/Materials/_6___Default/tex_base.outputs:rgb' @ '/World/StackedCarton_1_8/Materials/_6___Default/tex_base'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/06_-_Default_baseColor.jpg'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(1.000, 1.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0.892971'
    * '/World/StackedCarton_1_8/Materials/_6___Default/tex_base' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/06_-_Default_baseColor.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'file' [asset] = '0/06_-_Default_baseColor.jpg'
      * 'st' [float2]
        * Connected: '/World/StackedCarton_1_8/Materials/_6___Default/uvset0.outputs:result' @ '/World/StackedCarton_1_8/Materials/_6___Default/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/StackedCarton_1_8/Materials/_6___Default/uvset0' (ID: 'UsdPrimvarReader_float2')
    * Implementation: 'id'

---

### /World/StackedCarton_2_1/Materials/_6___Default

* **Prim路径 (Prim Path):**/World/StackedCarton_2_1/Materials/_6___Default
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/StackedCarton_2_1/Materials/_6___Default/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/StackedCarton_2_1/Materials/_6___Default/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f]
        * Connected: '/World/StackedCarton_2_1/Materials/_6___Default/tex_base.outputs:rgb' @ '/World/StackedCarton_2_1/Materials/_6___Default/tex_base'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/06_-_Default_baseColor.jpg'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(1.000, 1.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0.892971'
    * '/World/StackedCarton_2_1/Materials/_6___Default/tex_base' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/06_-_Default_baseColor.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'file' [asset] = '0/06_-_Default_baseColor.jpg'
      * 'st' [float2]
        * Connected: '/World/StackedCarton_2_1/Materials/_6___Default/uvset0.outputs:result' @ '/World/StackedCarton_2_1/Materials/_6___Default/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/StackedCarton_2_1/Materials/_6___Default/uvset0' (ID: 'UsdPrimvarReader_float2')
    * Implementation: 'id'

---

### /World/StackedCarton_2_2/Materials/_6___Default

* **Prim路径 (Prim Path):**/World/StackedCarton_2_2/Materials/_6___Default
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/StackedCarton_2_2/Materials/_6___Default/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/StackedCarton_2_2/Materials/_6___Default/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f]
        * Connected: '/World/StackedCarton_2_2/Materials/_6___Default/tex_base.outputs:rgb' @ '/World/StackedCarton_2_2/Materials/_6___Default/tex_base'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/06_-_Default_baseColor.jpg'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(1.000, 1.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0.892971'
    * '/World/StackedCarton_2_2/Materials/_6___Default/tex_base' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/06_-_Default_baseColor.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'file' [asset] = '0/06_-_Default_baseColor.jpg'
      * 'st' [float2]
        * Connected: '/World/StackedCarton_2_2/Materials/_6___Default/uvset0.outputs:result' @ '/World/StackedCarton_2_2/Materials/_6___Default/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/StackedCarton_2_2/Materials/_6___Default/uvset0' (ID: 'UsdPrimvarReader_float2')
    * Implementation: 'id'

---

### /World/StackedCarton_2_3/Materials/_6___Default

* **Prim路径 (Prim Path):**/World/StackedCarton_2_3/Materials/_6___Default
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/StackedCarton_2_3/Materials/_6___Default/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/StackedCarton_2_3/Materials/_6___Default/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f]
        * Connected: '/World/StackedCarton_2_3/Materials/_6___Default/tex_base.outputs:rgb' @ '/World/StackedCarton_2_3/Materials/_6___Default/tex_base'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/06_-_Default_baseColor.jpg'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(1.000, 1.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0.892971'
    * '/World/StackedCarton_2_3/Materials/_6___Default/tex_base' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/06_-_Default_baseColor.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'file' [asset] = '0/06_-_Default_baseColor.jpg'
      * 'st' [float2]
        * Connected: '/World/StackedCarton_2_3/Materials/_6___Default/uvset0.outputs:result' @ '/World/StackedCarton_2_3/Materials/_6___Default/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/StackedCarton_2_3/Materials/_6___Default/uvset0' (ID: 'UsdPrimvarReader_float2')
    * Implementation: 'id'

---

### /World/StackedCarton_2_4/Materials/_6___Default

* **Prim路径 (Prim Path):**/World/StackedCarton_2_4/Materials/_6___Default
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/StackedCarton_2_4/Materials/_6___Default/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/StackedCarton_2_4/Materials/_6___Default/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f]
        * Connected: '/World/StackedCarton_2_4/Materials/_6___Default/tex_base.outputs:rgb' @ '/World/StackedCarton_2_4/Materials/_6___Default/tex_base'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/06_-_Default_baseColor.jpg'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(1.000, 1.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0.892971'
    * '/World/StackedCarton_2_4/Materials/_6___Default/tex_base' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/06_-_Default_baseColor.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'file' [asset] = '0/06_-_Default_baseColor.jpg'
      * 'st' [float2]
        * Connected: '/World/StackedCarton_2_4/Materials/_6___Default/uvset0.outputs:result' @ '/World/StackedCarton_2_4/Materials/_6___Default/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/StackedCarton_2_4/Materials/_6___Default/uvset0' (ID: 'UsdPrimvarReader_float2')
    * Implementation: 'id'

---

### /World/StackedCarton_2_5/Materials/_6___Default

* **Prim路径 (Prim Path):**/World/StackedCarton_2_5/Materials/_6___Default
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/StackedCarton_2_5/Materials/_6___Default/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/StackedCarton_2_5/Materials/_6___Default/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f]
        * Connected: '/World/StackedCarton_2_5/Materials/_6___Default/tex_base.outputs:rgb' @ '/World/StackedCarton_2_5/Materials/_6___Default/tex_base'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/06_-_Default_baseColor.jpg'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(1.000, 1.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0.892971'
    * '/World/StackedCarton_2_5/Materials/_6___Default/tex_base' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/06_-_Default_baseColor.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'file' [asset] = '0/06_-_Default_baseColor.jpg'
      * 'st' [float2]
        * Connected: '/World/StackedCarton_2_5/Materials/_6___Default/uvset0.outputs:result' @ '/World/StackedCarton_2_5/Materials/_6___Default/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/StackedCarton_2_5/Materials/_6___Default/uvset0' (ID: 'UsdPrimvarReader_float2')
    * Implementation: 'id'

---

### /World/StackedCarton_2_6/Materials/_6___Default

* **Prim路径 (Prim Path):**/World/StackedCarton_2_6/Materials/_6___Default
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/StackedCarton_2_6/Materials/_6___Default/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/StackedCarton_2_6/Materials/_6___Default/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f]
        * Connected: '/World/StackedCarton_2_6/Materials/_6___Default/tex_base.outputs:rgb' @ '/World/StackedCarton_2_6/Materials/_6___Default/tex_base'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/06_-_Default_baseColor.jpg'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(1.000, 1.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0.892971'
    * '/World/StackedCarton_2_6/Materials/_6___Default/tex_base' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/06_-_Default_baseColor.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'file' [asset] = '0/06_-_Default_baseColor.jpg'
      * 'st' [float2]
        * Connected: '/World/StackedCarton_2_6/Materials/_6___Default/uvset0.outputs:result' @ '/World/StackedCarton_2_6/Materials/_6___Default/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/StackedCarton_2_6/Materials/_6___Default/uvset0' (ID: 'UsdPrimvarReader_float2')
    * Implementation: 'id'

---

### /World/StackedCarton_2_7/Materials/_6___Default

* **Prim路径 (Prim Path):**/World/StackedCarton_2_7/Materials/_6___Default
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/StackedCarton_2_7/Materials/_6___Default/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/StackedCarton_2_7/Materials/_6___Default/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f]
        * Connected: '/World/StackedCarton_2_7/Materials/_6___Default/tex_base.outputs:rgb' @ '/World/StackedCarton_2_7/Materials/_6___Default/tex_base'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/06_-_Default_baseColor.jpg'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(1.000, 1.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0.892971'
    * '/World/StackedCarton_2_7/Materials/_6___Default/tex_base' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/06_-_Default_baseColor.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'file' [asset] = '0/06_-_Default_baseColor.jpg'
      * 'st' [float2]
        * Connected: '/World/StackedCarton_2_7/Materials/_6___Default/uvset0.outputs:result' @ '/World/StackedCarton_2_7/Materials/_6___Default/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/StackedCarton_2_7/Materials/_6___Default/uvset0' (ID: 'UsdPrimvarReader_float2')
    * Implementation: 'id'

---

### /World/StackedCarton_2_8/Materials/_6___Default

* **Prim路径 (Prim Path):**/World/StackedCarton_2_8/Materials/_6___Default
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/StackedCarton_2_8/Materials/_6___Default/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/StackedCarton_2_8/Materials/_6___Default/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f]
        * Connected: '/World/StackedCarton_2_8/Materials/_6___Default/tex_base.outputs:rgb' @ '/World/StackedCarton_2_8/Materials/_6___Default/tex_base'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/06_-_Default_baseColor.jpg'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(1.000, 1.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0.892971'
    * '/World/StackedCarton_2_8/Materials/_6___Default/tex_base' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/06_-_Default_baseColor.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'file' [asset] = '0/06_-_Default_baseColor.jpg'
      * 'st' [float2]
        * Connected: '/World/StackedCarton_2_8/Materials/_6___Default/uvset0.outputs:result' @ '/World/StackedCarton_2_8/Materials/_6___Default/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/StackedCarton_2_8/Materials/_6___Default/uvset0' (ID: 'UsdPrimvarReader_float2')
    * Implementation: 'id'

---

### /World/HeavyDutyPackingTable_A01_01/Looks/Wood_Maple_HeavyDutyPackingTable_A

* **Prim路径 (Prim Path):**/World/HeavyDutyPackingTable_A01_01/Looks/Wood_Maple_HeavyDutyPackingTable_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/HeavyDutyPackingTable_A01_01/Looks/Wood_Maple_HeavyDutyPackingTable_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/HeavyDutyPackingTable_A01_01/Looks/Wood_Maple_HeavyDutyPackingTable_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
    * 纹理引用 (Texture Assets):
      * '1/T_HeavyDutyPackingTable_A01_Albedo.png'
      * '1/T_HeavyDutyPackingTable_A01_Normal.png'
      * '1/T_HeavyDutyPackingTable_A01_ORM.png'
    * Inputs:
      * 'albedo_add' [float] = '0'
      * 'diffuse_texture' [asset] = '1/T_HeavyDutyPackingTable_A01_Albedo.png'
      * 'diffuse_tint' [color3f] = '(0.784, 0.784, 0.784)'
      * 'metallic_texture_influence' [float] = '1'
      * 'normalmap_texture' [asset] = '1/T_HeavyDutyPackingTable_A01_Normal.png'
      * 'ORM_texture' [asset] = '1/T_HeavyDutyPackingTable_A01_ORM.png'
      * 'reflection_roughness_texture_influence' [float] = '1'

---

### /World/HeavyDutyPackingTable_A01_01/Looks/Metal_Glossy_A_HeavyDutyPackingTable_A

* **Prim路径 (Prim Path):**/World/HeavyDutyPackingTable_A01_01/Looks/Metal_Glossy_A_HeavyDutyPackingTable_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/HeavyDutyPackingTable_A01_01/Looks/Metal_Glossy_A_HeavyDutyPackingTable_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/HeavyDutyPackingTable_A01_01/Looks/Metal_Glossy_A_HeavyDutyPackingTable_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '0/Metal_Glossy_A.mdl' (Sub Id: 'Metal_Glossy_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/device_data/usdz/Workbench/HeavyDutyPackingTable_A01_01.usdz[0/Metal_Glossy_A.mdl]'

---

### /World/HeavyDutyPackingTable_A01_01/Looks/Metal_Painted_Gray_Glossy_A_HeavyDutyPackingTable_A

* **Prim路径 (Prim Path):**/World/HeavyDutyPackingTable_A01_01/Looks/Metal_Painted_Gray_Glossy_A_HeavyDutyPackingTable_A
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface'
    * 'outputs:mdl:surface' -> '/World/HeavyDutyPackingTable_A01_01/Looks/Metal_Painted_Gray_Glossy_A_HeavyDutyPackingTable_A/Shader'
    * Connection: 'out' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/HeavyDutyPackingTable_A01_01/Looks/Metal_Painted_Gray_Glossy_A_HeavyDutyPackingTable_A/Shader'
    * Implementation: 'sourceAsset'
    * Source Assets:
      * [mdl] '0/Metal_Painted_White_Glossy_A.mdl' (Sub Id: 'Metal_Painted_White_Glossy_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/device_data/usdz/Workbench/HeavyDutyPackingTable_A01_01.usdz[0/Metal_Painted_White_Glossy_A.mdl]'
    * Inputs:
      * 'diffuse_tint' [color3f] = '(0.170, 0.170, 0.170)'
      * 'texture_scale' [float2] = '(2.000, 2.000)'

---
