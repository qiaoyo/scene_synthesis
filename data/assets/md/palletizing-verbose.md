# USDA场景描述文档:palletizing.usda

## 1.场景元数据(Scene Metadata)
*  **USDA文件路径(USDA File Path):**`/media/simple/another_Documents/isaacsim_assets/scenedata/palletizing.usda`
*  **默认Prim (Default Prim):**'World'
*  **单位与坐标系 (Units & Coordinate System):**
   *   **米(Meters Per Unit):**1.0
   *   **Up Axis:**Z
* **场景描述(Scene Describe):** 该该场景呈现出一个典型的智能化末端物流与码垛作业区，整体规划强调了人机协作、柔性输送与高效装卸的深度融合，展现了一个半开放式且逻辑清晰的工业处理环境。从厂区的空间格局来看，该区域依托于一侧带有浅蓝色砖纹装饰墙面的车间内景，地面平整且呈淡灰色，为各类移动设备提供了充足的作业半径。整个场景在区域划分上表现为明显的“三位一体”结构：即由高架输送线构成的进料区、由协作机器人与移动平台构成的处理区，以及由重型叉车负责的成品接驳区。核心工业设备中，最引人注目的是两组并行的蓝色皮带输送机，它们通过稳固的工字型支撑结构架设在半空中，黑色橡胶皮带上整齐排列着多个土黄色的标准纸质包装箱，正处于匀速输送状态。紧邻输送线末端，部署了一套高度灵活的处理单元，包括一个带有浅色木质纹理顶面的金属架构工作台，台面上安装有一台小巧的白色六轴协作机器人，其末端执行器配备了亮黄色的防护外壳，专门用于从流水线上抓取包装箱并进行二次分拣或精确定位。与此同时，地面上部署了一台黑黄相间的自主移动作业机器人（AMR），该移动平台顶部集成了一根白色的多关节机械臂，正配合工作台进行动态的物料转运。在处理区的中心位置，可以观察到一堆呈阶梯状整齐堆叠的纸质包装箱，这标志着一个临时的码垛点或缓存区，体现了车间对生产节拍的调节能力。而在场景的侧翼，一台亮黄色的重型工业叉车占据了显著位置，其黑色门架与货叉处于下降位，正准备对堆叠完成的箱体进行整体移位或装车作业。叉车的驾驶室结构清晰，车身上方配有防护顶棚，体现了严苛的工业安全标准。从设备排布方式与整体规划结构分析，该场景巧妙地将固定式的流水线输送与移动式的机器人作业相结合，形成了一个“线、点、面”交织的作业网络。固定流水线（线）负责远端物料的持续引入，协作机器人工作站（点）负责局部的精密处理，而AMR与重型叉车（面）则通过大范围的空间移动实现了不同功能模块间的无缝衔接。这种布局不仅保证了码垛工序的连续性，也赋予了生产线极强的柔性，能够根据任务量的变化快速调整设备配比。所有设备在分布位置上保持了科学的距离，既确保了机器人的工作包络圆互不干涉，又为叉车的行驶留出了必要的转向调头空间。整个画面中，蓝色输送架、黄色叉车、白色机械臂与木色工作台形成了鲜明的色彩分区，潜移默化地对作业安全等级进行了提示。这种由高精度工业臂、智能化移动底盘与传统搬运设备构成的混合动力景观，深刻诠释了现代仓储物流向自动化、智能化转型的技术路径，是一个高效、有序且具备高度协同能力的现代化码垛生产示范场景。
* **设备数量(Device Number):**
  * **Scene: 1**
  * **IndustrialRobot: 3**
  * **Workbench: 2**
  * **Conveyor: 2**
  * **AGV: 0**
  * **Forklift: 2**
  * **Box: 26**
  * **Rack: 0**
  * **Pallet: 0**
  * **Part: 0**
  * **Decoration: 0**

## 2.场景对象层级(Scene Hierarchy)
*   World (Xform)
    *   Building (Xform)
        *   Materials (Scope)
            *   industrialWindow_Small (Material)
                *   pbr_shader (Shader)
                *   uvset0 (Shader)
                *   tex_base (Shader)
                *   tex_metallic (Shader)
                *   tex_roughness (Shader)
                *   tex_normal (Shader)
            *   industrialDoor (Material)
                *   pbr_shader (Shader)
                *   uvset0 (Shader)
                *   tex_base (Shader)
                *   tex_metallic (Shader)
                *   tex_roughness (Shader)
                *   tex_normal (Shader)
            *   Atlas_2048x2048_01 (Material)
                *   pbr_shader (Shader)
                *   uvset0 (Shader)
                *   tex_base (Shader)
                *   tex_metallic (Shader)
                *   tex_roughness (Shader)
                *   tex_normal (Shader)
            *   decalMoss01 (Material)
                *   pbr_shader (Shader)
                *   uvset0 (Shader)
                *   tex_base (Shader)
            *   woodenFence (Material)
                *   pbr_shader (Shader)
                *   uvset0 (Shader)
                *   tex_base (Shader)
                *   tex_metallic (Shader)
                *   tex_roughness (Shader)
                *   tex_normal (Shader)
            *   eletricBox_001 (Material)
                *   pbr_shader (Shader)
                *   uvset0 (Shader)
                *   tex_base (Shader)
                *   tex_metallic (Shader)
                *   tex_roughness (Shader)
                *   tex_normal (Shader)
            *   air_conditioning_001 (Material)
                *   pbr_shader (Shader)
                *   uvset0 (Shader)
                *   tex_base (Shader)
                *   tex_metallic (Shader)
                *   tex_roughness (Shader)
                *   tex_normal (Shader)
            *   vents (Material)
                *   pbr_shader (Shader)
                *   uvset0 (Shader)
                *   tex_base (Shader)
                *   tex_metallic (Shader)
                *   tex_roughness (Shader)
            *   roofingSheets (Material)
                *   pbr_shader (Shader)
                *   uvset0 (Shader)
                *   tex_base (Shader)
                *   tex_metallic (Shader)
                *   tex_roughness (Shader)
                *   tex_normal (Shader)
            *   emptyBillboard (Material)
                *   pbr_shader (Shader)
                *   uvset0 (Shader)
                *   tex_base (Shader)
        *   Meshes (Xform)
            *   Sketchfab_model (Xform)
                *   b63827acdd174d9a8e1e6ab96b34b9f7_fbx (Xform)
                    *   RootNode (Xform)
                        *   industrialWindow_Small (Xform)
                            *   industrialWindow_Small_industrialWindow_Small_0 (Xform)
                                *   industrialWindow_Small_industrialWindow_Small_0 (Mesh)
                        *   industrialWindow_Small_001 (Xform)
                            *   industrialWindow_Small_001_industrialWindow_Small_0 (Xform)
                                *   industrialWindow_Small_001_industrialWindow_Small_0 (Mesh)
                        *   industrialWindow_Small_002 (Xform)
                            *   industrialWindow_Small_002_industrialWindow_Small_0 (Xform)
                                *   industrialWindow_Small_002_industrialWindow_Small_0 (Mesh)
                        *   industrialWindow_Small_003 (Xform)
                            *   industrialWindow_Small_003_industrialWindow_Small_0 (Xform)
                                *   industrialWindow_Small_003_industrialWindow_Small_0 (Mesh)
                        *   industrialWindow_Small_004 (Xform)
                            *   industrialWindow_Small_004_industrialWindow_Small_0 (Xform)
                                *   industrialWindow_Small_004_industrialWindow_Small_0 (Mesh)
                        *   industrialWindow_Small_005 (Xform)
                            *   industrialWindow_Small_005_industrialWindow_Small_0 (Xform)
                                *   industrialWindow_Small_005_industrialWindow_Small_0 (Mesh)
                        *   industrialWindow_Small_006 (Xform)
                            *   industrialWindow_Small_006_industrialWindow_Small_0 (Xform)
                                *   industrialWindow_Small_006_industrialWindow_Small_0 (Mesh)
                        *   industrialWindow_Small_007 (Xform)
                            *   industrialWindow_Small_007_industrialWindow_Small_0 (Xform)
                                *   industrialWindow_Small_007_industrialWindow_Small_0 (Mesh)
                        *   industrialWindow_Small_008 (Xform)
                            *   industrialWindow_Small_008_industrialWindow_Small_0 (Xform)
                                *   industrialWindow_Small_008_industrialWindow_Small_0 (Mesh)
                        *   industrialWindow_Small_009 (Xform)
                            *   industrialWindow_Small_009_industrialWindow_Small_0 (Xform)
                                *   industrialWindow_Small_009_industrialWindow_Small_0 (Mesh)
                        *   industrialWindow_Small_010 (Xform)
                            *   industrialWindow_Small_010_industrialWindow_Small_0 (Xform)
                                *   industrialWindow_Small_010_industrialWindow_Small_0 (Mesh)
                        *   industrialWindow_Small_011 (Xform)
                            *   industrialWindow_Small_011_industrialWindow_Small_0 (Xform)
                                *   industrialWindow_Small_011_industrialWindow_Small_0 (Mesh)
                        *   industrialWindow_Small_012 (Xform)
                            *   industrialWindow_Small_012_industrialWindow_Small_0 (Xform)
                                *   industrialWindow_Small_012_industrialWindow_Small_0 (Mesh)
                        *   industrialWindow_Small_013 (Xform)
                            *   industrialWindow_Small_013_industrialWindow_Small_0 (Xform)
                                *   industrialWindow_Small_013_industrialWindow_Small_0 (Mesh)
                        *   industrialWindow_Small_014 (Xform)
                            *   industrialWindow_Small_014_industrialWindow_Small_0 (Xform)
                                *   industrialWindow_Small_014_industrialWindow_Small_0 (Mesh)
                        *   industrialDoor (Xform)
                            *   industrialDoor_industrialDoor_0 (Xform)
                                *   industrialDoor_industrialDoor_0 (Mesh)
                        *   concreteStairs (Xform)
                            *   concreteStairs_Atlas_2048x2048_01_0 (Xform)
                                *   concreteStairs_Atlas_2048x2048_01_0 (Mesh)
                        *   buildingMainwalls (Xform)
                            *   buildingMainwalls_Atlas_2048x2048_01_0 (Xform)
                                *   buildingMainwalls_Atlas_2048x2048_01_0 (Mesh)
                        *   wallbaseboard (Xform)
                            *   wallbaseboard_Atlas_2048x2048_01_0 (Xform)
                                *   wallbaseboard_Atlas_2048x2048_01_0 (Mesh)
                        *   metalFrame (Xform)
                            *   metalFrame_Atlas_2048x2048_01_0 (Xform)
                                *   metalFrame_Atlas_2048x2048_01_0 (Mesh)
                        *   mossDecal (Xform)
                            *   mossDecal_decalMoss01_0 (Xform)
                                *   mossDecal_decalMoss01_0 (Mesh)
                        *   building_Roof (Xform)
                            *   building_Roof_Atlas_2048x2048_01_0 (Xform)
                                *   building_Roof_Atlas_2048x2048_01_0 (Mesh)
                        *   woodenFenceType_02 (Xform)
                            *   woodenFenceType_02_woodenFence_0 (Xform)
                                *   woodenFenceType_02_woodenFence_0 (Mesh)
                        *   woodenFenceType_01 (Xform)
                            *   woodenFenceType_01_woodenFence_0 (Xform)
                                *   woodenFenceType_01_woodenFence_0 (Mesh)
                        *   woodenFenceType_02_001 (Xform)
                            *   woodenFenceType_02_001_woodenFence_0 (Xform)
                                *   woodenFenceType_02_001_woodenFence_0 (Mesh)
                        *   eletricBox_Low_001 (Xform)
                            *   eletricBox_Low_001_eletricBox_001_0 (Xform)
                                *   eletricBox_Low_001_eletricBox_001_0 (Mesh)
                        *   eletricBox_Low_002 (Xform)
                            *   eletricBox_Low_002_eletricBox_001_0 (Xform)
                                *   eletricBox_Low_002_eletricBox_001_0 (Mesh)
                        *   airconditioning_Low_002 (Xform)
                            *   airconditioning_Low_002_air_conditioning_001_0 (Xform)
                                *   airconditioning_Low_002_air_conditioning_001_0 (Mesh)
                        *   airconditioningBraket_002 (Xform)
                            *   airconditioningBraket_002_air_conditioning_001_0 (Xform)
                                *   airconditioningBraket_002_air_conditioning_001_0 (Mesh)
                        *   airconditioning_Low_003 (Xform)
                            *   airconditioning_Low_003_air_conditioning_001_0 (Xform)
                                *   airconditioning_Low_003_air_conditioning_001_0 (Mesh)
                        *   airconditioningBraket_003 (Xform)
                            *   airconditioningBraket_003_air_conditioning_001_0 (Xform)
                                *   airconditioningBraket_003_air_conditioning_001_0 (Mesh)
                        *   vents (Xform)
                            *   vents_vents_0 (Xform)
                                *   vents_vents_0 (Mesh)
                        *   vents_001 (Xform)
                            *   vents_001_vents_0 (Xform)
                                *   vents_001_vents_0 (Mesh)
                        *   vents_002 (Xform)
                            *   vents_002_vents_0 (Xform)
                                *   vents_002_vents_0 (Mesh)
                        *   metalBeams (Xform)
                            *   metalBeams_roofingSheets_0 (Xform)
                                *   metalBeams_roofingSheets_0 (Mesh)
                        *   metalSheet (Xform)
                            *   metalSheet_roofingSheets_0 (Xform)
                                *   metalSheet_roofingSheets_0 (Mesh)
                        *   metalSheet_001 (Xform)
                            *   metalSheet_001_roofingSheets_0 (Xform)
                                *   metalSheet_001_roofingSheets_0 (Mesh)
                        *   metalSheet_002 (Xform)
                            *   metalSheet_002_roofingSheets_0 (Xform)
                                *   metalSheet_002_roofingSheets_0 (Mesh)
                        *   metalSheet_003 (Xform)
                            *   metalSheet_003_roofingSheets_0 (Xform)
                                *   metalSheet_003_roofingSheets_0 (Mesh)
                        *   emptyBillboard (Xform)
                            *   emptyBillboard_emptyBillboard_0 (Xform)
                                *   emptyBillboard_emptyBillboard_0 (Mesh)
                        *   emptyBillboard_001 (Xform)
                            *   emptyBillboard_001_emptyBillboard_0 (Xform)
                                *   emptyBillboard_001_emptyBillboard_0 (Mesh)
        *   GroundPlane (Xform)
            *   CollisionMesh (Mesh)
            *   CollisionPlane (Plane)
    *   Robotic_Manipulator_low_poly (Xform)
        *   Materials (Scope)
            *   Robot_hand (Material)
                *   pbr_shader (Shader)
                *   uvset0 (Shader)
                *   tex_base (Shader)
                *   tex_metallic (Shader)
                *   tex_roughness (Shader)
                *   tex_normal (Shader)
                *   tex_occlusion (Shader)
            *   Stand (Material)
                *   pbr_shader (Shader)
                *   uvset0 (Shader)
                *   tex_base (Shader)
                *   tex_metallic (Shader)
                *   tex_roughness (Shader)
                *   tex_normal (Shader)
                *   tex_emissive (Shader)
                *   tex_occlusion (Shader)
        *   Meshes (Xform)
            *   Sketchfab_model (Xform)
                *   Collada_visual_scene_group (Xform)
                    *   Robotic_hand_018_low (Xform)
                        *   defaultMaterial (Xform)
                            *   defaultMaterial (Mesh)
                    *   Robotic_hand_016_low (Xform)
                        *   defaultMaterial (Xform)
                            *   defaultMaterial (Mesh)
                    *   Robotic_hand_015_low (Xform)
                        *   defaultMaterial (Xform)
                            *   defaultMaterial (Mesh)
                    *   Robotic_hand_017_low (Xform)
                        *   defaultMaterial (Xform)
                            *   defaultMaterial (Mesh)
                    *   Robotic_hand_014_low (Xform)
                        *   defaultMaterial (Xform)
                            *   defaultMaterial (Mesh)
                    *   Robotic_hand_013_low (Xform)
                        *   defaultMaterial (Xform)
                            *   defaultMaterial (Mesh)
                    *   Robotic_hand_012_low (Xform)
                        *   defaultMaterial (Xform)
                            *   defaultMaterial (Mesh)
                    *   Robotic_hand_011_low (Xform)
                        *   defaultMaterial (Xform)
                            *   defaultMaterial (Mesh)
                    *   Robotic_hand_010_low (Xform)
                        *   defaultMaterial (Xform)
                            *   defaultMaterial (Mesh)
                    *   Robotic_hand_009_low (Xform)
                        *   defaultMaterial (Xform)
                            *   defaultMaterial (Mesh)
                    *   Robotic_hand_008_low (Xform)
                        *   defaultMaterial (Xform)
                            *   defaultMaterial (Mesh)
                    *   Robotic_hand_007_low (Xform)
                        *   defaultMaterial (Xform)
                            *   defaultMaterial (Mesh)
                    *   Robotic_hand_006_low (Xform)
                        *   defaultMaterial (Xform)
                            *   defaultMaterial (Mesh)
                    *   Robotic_hand_005_low (Xform)
                        *   defaultMaterial (Xform)
                            *   defaultMaterial (Mesh)
                    *   Robotic_hand_004_low (Xform)
                        *   defaultMaterial (Xform)
                            *   defaultMaterial (Mesh)
                    *   Robotic_hand_003_low (Xform)
                        *   defaultMaterial (Xform)
                            *   defaultMaterial (Mesh)
    *   Simple_rubber_conveyor (Xform)
        *   Materials (Scope)
            *   Conveyor (Material)
                *   pbr_shader (Shader)
                *   uvset0 (Shader)
                *   tex_base (Shader)
                *   tex_specular (Shader)
                *   tex_glossiness (Shader)
                *   tex_normal (Shader)
                *   tex_occlusion (Shader)
            *   Belt (Material)
                *   pbr_shader (Shader)
                *   uvset0 (Shader)
                *   tex_base (Shader)
        *   Meshes (Xform)
            *   Sketchfab_model (Xform)
                *   Conveyor_FBX (Xform)
                    *   RootNode (Xform)
                        *   Conveyor01Frame (Xform)
                            *   Conveyor01Frame_Conveyor_0 (Xform)
                                *   Conveyor01Frame_Conveyor_0 (Mesh)
                        *   Conveyor01Frame01 (Xform)
                            *   Conveyor01Frame01_Conveyor_0 (Xform)
                                *   Conveyor01Frame01_Conveyor_0 (Mesh)
                        *   Conveyor01Frame02 (Xform)
                            *   Conveyor01Frame02_Conveyor_0 (Xform)
                                *   Conveyor01Frame02_Conveyor_0 (Mesh)
                        *   Conveyor01Legs (Xform)
                            *   Conveyor01Legs_Conveyor_0 (Xform)
                                *   Conveyor01Legs_Conveyor_0 (Mesh)
                        *   Conveyor01Belt (Xform)
                            *   Conveyor01Belt_Belt_0 (Xform)
                                *   Conveyor01Belt_Belt_0 (Mesh)
    *   AGV_ready_1 (Xform)
        *   Materials (Scope)
            *   ASELSAN_CATS_04 (Material)
                *   pbr_shader (Shader)
            *   ASELSAN_CATS_04_2 (Material)
                *   pbr_shader (Shader)
            *   ASELSAN_CATS_13 (Material)
                *   pbr_shader (Shader)
            *   Color_000 (Material)
                *   pbr_shader (Shader)
            *   Color_A05 (Material)
                *   pbr_shader (Shader)
            *   Color_A06 (Material)
                *   pbr_shader (Shader)
            *   Color_B05 (Material)
                *   pbr_shader (Shader)
            *   Color_E02 (Material)
                *   pbr_shader (Shader)
            *   Color_E05 (Material)
                *   pbr_shader (Shader)
            *   Color_F06 (Material)
                *   pbr_shader (Shader)
            *   Color_G03 (Material)
                *   pbr_shader (Shader)
            *   Color_M02 (Material)
                *   pbr_shader (Shader)
            *   Color_M03 (Material)
                *   pbr_shader (Shader)
            *   Mtl39 (Material)
                *   pbr_shader (Shader)
            *   Mtl6 (Material)
                *   pbr_shader (Shader)
                *   uvset0 (Shader)
                *   tex_base (Shader)
            *   Mtl9 (Material)
                *   pbr_shader (Shader)
            *   Silver (Material)
                *   pbr_shader (Shader)
            *   material (Material)
                *   pbr_shader (Shader)
                *   uvset0 (Shader)
                *   tex_base (Shader)
            *   cash_register_keys (Material)
                *   pbr_shader (Shader)
            *   Chris_Shoe_Sole (Material)
                *   pbr_shader (Shader)
            *   Color_002 (Material)
                *   pbr_shader (Shader)
            *   Color_005 (Material)
                *   pbr_shader (Shader)
            *   Color_006 (Material)
                *   pbr_shader (Shader)
            *   Color_008 (Material)
                *   pbr_shader (Shader)
            *   Color_A01 (Material)
                *   pbr_shader (Shader)
            *   Color_A11 (Material)
                *   pbr_shader (Shader)
            *   Color_M04 (Material)
                *   pbr_shader (Shader)
            *   Color_M05 (Material)
                *   pbr_shader (Shader)
            *   Color_M06 (Material)
                *   pbr_shader (Shader)
            *   Color_M07 (Material)
                *   pbr_shader (Shader)
            *   Color_M09 (Material)
                *   pbr_shader (Shader)
            *   FCP_Charcoal_v2 (Material)
                *   pbr_shader (Shader)
            *   FrontColor (Material)
                *   pbr_shader (Shader)
            *   Light_Blue (Material)
                *   pbr_shader (Shader)
            *   M_0011_Seashell (Material)
                *   pbr_shader (Shader)
            *   M_0131_Silver (Material)
                *   pbr_shader (Shader)
            *   M_0134_DimGray (Material)
                *   pbr_shader (Shader)
            *   M_0135_DarkGray (Material)
                *   pbr_shader (Shader)
            *   Metal_Silver (Material)
                *   pbr_shader (Shader)
            *   Mtl1 (Material)
                *   pbr_shader (Shader)
            *   Mtl10 (Material)
                *   pbr_shader (Shader)
            *   Mtl11 (Material)
                *   pbr_shader (Shader)
            *   Mtl12 (Material)
                *   pbr_shader (Shader)
            *   Mtl13 (Material)
                *   pbr_shader (Shader)
            *   Mtl14 (Material)
                *   pbr_shader (Shader)
            *   Mtl15 (Material)
                *   pbr_shader (Shader)
            *   Mtl16 (Material)
                *   pbr_shader (Shader)
            *   Mtl17 (Material)
                *   pbr_shader (Shader)
            *   Mtl3 (Material)
                *   pbr_shader (Shader)
            *   Mtl35 (Material)
                *   pbr_shader (Shader)
            *   Mtl36 (Material)
                *   pbr_shader (Shader)
            *   Mtl37 (Material)
                *   pbr_shader (Shader)
            *   Mtl3a (Material)
                *   pbr_shader (Shader)
            *   Mtl3b (Material)
                *   pbr_shader (Shader)
            *   Mtl5 (Material)
                *   pbr_shader (Shader)
            *   Mtl7 (Material)
                *   pbr_shader (Shader)
            *   Mtl8 (Material)
                *   pbr_shader (Shader)
            *   Mtla (Material)
                *   pbr_shader (Shader)
            *   Mtlb1 (Material)
                *   pbr_shader (Shader)
            *   Stainless_Steel (Material)
                *   pbr_shader (Shader)
            *   Metal_Aluminum_Anodized_1 (Material)
                *   pbr_shader (Shader)
            *   Metal_Aluminum_Anodized_2 (Material)
                *   pbr_shader (Shader)
            *   basic_gray_plastic (Material)
                *   pbr_shader (Shader)
            *   texture (Material)
                *   pbr_shader (Shader)
        *   Meshes (Xform)
            *   Sketchfab_model (Xform)
                *   AGV_ready_1_obj_cleaner_materialmerger_gles (Xform)
                    *   Object_2 (Xform)
                        *   Object_0 (Mesh)
                    *   Object_3 (Xform)
                        *   Object_1 (Mesh)
                    *   Object_4 (Xform)
                        *   Object_2 (Mesh)
                    *   Object_5 (Xform)
                        *   Object_3 (Mesh)
                    *   Object_6 (Xform)
                        *   Object_4 (Mesh)
                    *   Object_7 (Xform)
                        *   Object_5 (Mesh)
                    *   Object_8 (Xform)
                        *   Object_6 (Mesh)
                    *   Object_9 (Xform)
                        *   Object_7 (Mesh)
                    *   Object_10 (Xform)
                        *   Object_8 (Mesh)
                    *   Object_11 (Xform)
                        *   Object_9 (Mesh)
                    *   Object_12 (Xform)
                        *   Object_10 (Mesh)
                    *   Object_13 (Xform)
                        *   Object_11 (Mesh)
                    *   Object_14 (Xform)
                        *   Object_12 (Mesh)
                    *   Object_15 (Xform)
                        *   Object_13 (Mesh)
                    *   Object_16 (Xform)
                        *   Object_14 (Mesh)
                    *   Object_17 (Xform)
                        *   Object_15 (Mesh)
                    *   Object_18 (Xform)
                        *   Object_16 (Mesh)
                    *   Object_19 (Xform)
                        *   Object_17 (Mesh)
                    *   Object_20 (Xform)
                        *   Object_18 (Mesh)
                    *   Object_21 (Xform)
                        *   Object_19 (Mesh)
                    *   Object_22 (Xform)
                        *   Object_20 (Mesh)
                    *   Object_23 (Xform)
                        *   Object_21 (Mesh)
                    *   Object_24 (Xform)
                        *   Object_22 (Mesh)
                    *   Object_25 (Xform)
                        *   Object_23 (Mesh)
                    *   Object_26 (Xform)
                        *   Object_24 (Mesh)
                    *   Object_27 (Xform)
                        *   Object_25 (Mesh)
                    *   Object_28 (Xform)
                        *   Object_26 (Mesh)
                    *   Object_29 (Xform)
                        *   Object_27 (Mesh)
                    *   Object_30 (Xform)
                        *   Object_28 (Mesh)
                    *   Object_31 (Xform)
                        *   Object_29 (Mesh)
                    *   Object_32 (Xform)
                        *   Object_30 (Mesh)
                    *   Object_33 (Xform)
                        *   Object_31 (Mesh)
                    *   Object_34 (Xform)
                        *   Object_32 (Mesh)
                    *   Object_35 (Xform)
                        *   Object_33 (Mesh)
                    *   Object_36 (Xform)
                        *   Object_34 (Mesh)
                    *   Object_37 (Xform)
                        *   Object_35 (Mesh)
                    *   Object_38 (Xform)
                        *   Object_36 (Mesh)
                    *   Object_39 (Xform)
                        *   Object_37 (Mesh)
                    *   Object_40 (Xform)
                        *   Object_38 (Mesh)
                    *   Object_41 (Xform)
                        *   Object_39 (Mesh)
                    *   Object_42 (Xform)
                        *   Object_40 (Mesh)
                    *   Object_43 (Xform)
                        *   Object_41 (Mesh)
                    *   Object_44 (Xform)
                        *   Object_42 (Mesh)
                    *   Object_45 (Xform)
                        *   Object_43 (Mesh)
                    *   Object_46 (Xform)
                        *   Object_44 (Mesh)
                    *   Object_47 (Xform)
                        *   Object_45 (Mesh)
                    *   Object_48 (Xform)
                        *   Object_46 (Mesh)
                    *   Object_49 (Xform)
                        *   Object_47 (Mesh)
                    *   Object_50 (Xform)
                        *   Object_48 (Mesh)
                    *   Object_51 (Xform)
                        *   Object_49 (Mesh)
                    *   Object_52 (Xform)
                        *   Object_50 (Mesh)
                    *   Object_53 (Xform)
                        *   Object_51 (Mesh)
                    *   Object_54 (Xform)
                        *   Object_52 (Mesh)
                    *   Object_55 (Xform)
                        *   Object_53 (Mesh)
                    *   Object_56 (Xform)
                        *   Object_54 (Mesh)
                    *   Object_57 (Xform)
                        *   Object_55 (Mesh)
                    *   Object_58 (Xform)
                        *   Object_56 (Mesh)
                    *   Object_59 (Xform)
                        *   Object_57 (Mesh)
                    *   Object_60 (Xform)
                        *   Object_58 (Mesh)
                    *   Object_61 (Xform)
                        *   Object_59 (Mesh)
                    *   Object_62 (Xform)
                        *   Object_60 (Mesh)
                    *   Object_63 (Xform)
                        *   Object_61 (Mesh)
                    *   Object_64 (Xform)
                        *   Object_62 (Mesh)
                    *   Object_65 (Xform)
                        *   Object_63 (Mesh)
                    *   Object_66 (Xform)
                        *   Object_64 (Mesh)
                    *   Object_67 (Xform)
                        *   Object_65 (Mesh)
                    *   Object_68 (Xform)
                        *   Object_66 (Mesh)
                    *   Object_69 (Xform)
                        *   Object_67 (Mesh)
                    *   Object_70 (Xform)
                        *   Object_68 (Mesh)
                    *   Object_71 (Xform)
                        *   Object_69 (Mesh)
                    *   Object_72 (Xform)
                        *   Object_70 (Mesh)
                    *   Object_73 (Xform)
                        *   Object_71 (Mesh)
                    *   Object_74 (Xform)
                        *   Object_72 (Mesh)
                    *   Object_75 (Xform)
                        *   Object_73 (Mesh)
                    *   Object_76 (Xform)
                        *   Object_74 (Mesh)
                    *   Object_77 (Xform)
                        *   Object_75 (Mesh)
                    *   Object_78 (Xform)
                        *   Object_76 (Mesh)
                    *   Object_79 (Xform)
                        *   Object_77 (Mesh)
                    *   Object_80 (Xform)
                        *   Object_78 (Mesh)
                    *   Object_81 (Xform)
                        *   Object_79 (Mesh)
                    *   Object_82 (Xform)
                        *   Object_80 (Mesh)
                    *   Object_83 (Xform)
                        *   Object_81 (Mesh)
                    *   Object_84 (Xform)
                        *   Object_82 (Mesh)
                    *   Object_85 (Xform)
                        *   Object_83 (Mesh)
                    *   Object_86 (Xform)
                        *   Object_84 (Mesh)
                    *   Object_87 (Xform)
                        *   Object_85 (Mesh)
                    *   Object_88 (Xform)
                        *   Object_86 (Mesh)
                    *   Object_89 (Xform)
                        *   Object_87 (Mesh)
                    *   Object_90 (Xform)
                        *   Object_88 (Mesh)
                    *   Object_91 (Xform)
                        *   Object_89 (Mesh)
                    *   Object_92 (Xform)
                        *   Object_90 (Mesh)
                    *   Object_93 (Xform)
                        *   Object_91 (Mesh)
                    *   Object_94 (Xform)
                        *   Object_92 (Mesh)
                    *   Object_95 (Xform)
                        *   Object_93 (Mesh)
                    *   Object_96 (Xform)
                        *   Object_94 (Mesh)
                    *   Object_97 (Xform)
                        *   Object_95 (Mesh)
                    *   Object_98 (Xform)
                        *   Object_96 (Mesh)
                    *   Object_99 (Xform)
                        *   Object_97 (Mesh)
                    *   Object_100 (Xform)
                        *   Object_98 (Mesh)
                    *   Object_101 (Xform)
                        *   Object_99 (Mesh)
                    *   Object_102 (Xform)
                        *   Object_100 (Mesh)
                    *   Object_103 (Xform)
                        *   Object_101 (Mesh)
                    *   Object_104 (Xform)
                        *   Object_102 (Mesh)
                    *   Object_105 (Xform)
                        *   Object_103 (Mesh)
                    *   Object_106 (Xform)
                        *   Object_104 (Mesh)
                    *   Object_107 (Xform)
                        *   Object_105 (Mesh)
                    *   Object_108 (Xform)
                        *   Object_106 (Mesh)
                    *   Object_109 (Xform)
                        *   Object_107 (Mesh)
                    *   Object_110 (Xform)
                        *   Object_108 (Mesh)
                    *   Object_111 (Xform)
                        *   Object_109 (Mesh)
                    *   Object_112 (Xform)
                        *   Object_110 (Mesh)
                    *   Object_113 (Xform)
                        *   Object_111 (Mesh)
                    *   Object_114 (Xform)
                        *   Object_112 (Mesh)
                    *   Object_115 (Xform)
                        *   Object_113 (Mesh)
                    *   Object_116 (Xform)
                        *   Object_114 (Mesh)
                    *   Object_117 (Xform)
                        *   Object_115 (Mesh)
                    *   Object_118 (Xform)
                        *   Object_116 (Mesh)
                    *   Object_119 (Xform)
                        *   Object_117 (Mesh)
                    *   Object_120 (Xform)
                        *   Object_118 (Mesh)
                    *   Object_121 (Xform)
                        *   Object_119 (Mesh)
                    *   Object_122 (Xform)
                        *   Object_120 (Mesh)
                    *   Object_123 (Xform)
                        *   Object_121 (Mesh)
                    *   Object_124 (Xform)
                        *   Object_122 (Mesh)
                    *   Object_125 (Xform)
                        *   Object_123 (Mesh)
                    *   Object_126 (Xform)
                        *   Object_124 (Mesh)
                    *   Object_127 (Xform)
                        *   Object_125 (Mesh)
                    *   Object_128 (Xform)
                        *   Object_126 (Mesh)
                    *   Object_129 (Xform)
                        *   Object_127 (Mesh)
                    *   Object_130 (Xform)
                        *   Object_128 (Mesh)
                    *   Object_131 (Xform)
                        *   Object_129 (Mesh)
                    *   Object_132 (Xform)
                        *   Object_130 (Mesh)
                    *   Object_133 (Xform)
                        *   Object_131 (Mesh)
                    *   Object_134 (Xform)
                        *   Object_132 (Mesh)
                    *   Object_135 (Xform)
                        *   Object_133 (Mesh)
                    *   Object_136 (Xform)
                        *   Object_134 (Mesh)
                    *   Object_137 (Xform)
                        *   Object_135 (Mesh)
                    *   Object_138 (Xform)
                        *   Object_136 (Mesh)
                    *   Object_139 (Xform)
                        *   Object_137 (Mesh)
                    *   Object_140 (Xform)
                        *   Object_138 (Mesh)
                    *   Object_141 (Xform)
                        *   Object_139 (Mesh)
                    *   Object_142 (Xform)
                        *   Object_140 (Mesh)
                    *   Object_143 (Xform)
                        *   Object_141 (Mesh)
                    *   Object_144 (Xform)
                        *   Object_142 (Mesh)
                    *   Object_145 (Xform)
                        *   Object_143 (Mesh)
                    *   Object_146 (Xform)
                        *   Object_144 (Mesh)
                    *   Object_147 (Xform)
                        *   Object_145 (Mesh)
                    *   Object_148 (Xform)
                        *   Object_146 (Mesh)
                    *   Object_149 (Xform)
                        *   Object_147 (Mesh)
                    *   Object_150 (Xform)
                        *   Object_148 (Mesh)
                    *   Object_151 (Xform)
                        *   Object_149 (Mesh)
                    *   Object_152 (Xform)
                        *   Object_150 (Mesh)
                    *   Object_153 (Xform)
                        *   Object_151 (Mesh)
                    *   Object_154 (Xform)
                        *   Object_152 (Mesh)
                    *   Object_155 (Xform)
                        *   Object_153 (Mesh)
                    *   Object_156 (Xform)
                        *   Object_154 (Mesh)
                    *   Object_157 (Xform)
                        *   Object_155 (Mesh)
                    *   Object_158 (Xform)
                        *   Object_156 (Mesh)
                    *   Object_159 (Xform)
                        *   Object_157 (Mesh)
                    *   Object_160 (Xform)
                        *   Object_158 (Mesh)
                    *   Object_161 (Xform)
                        *   Object_159 (Mesh)
                    *   Object_162 (Xform)
                        *   Object_160 (Mesh)
                    *   Object_163 (Xform)
                        *   Object_161 (Mesh)
                    *   Object_164 (Xform)
                        *   Object_162 (Mesh)
                    *   Object_165 (Xform)
                        *   Object_163 (Mesh)
                    *   Object_166 (Xform)
                        *   Object_164 (Mesh)
                    *   Object_167 (Xform)
                        *   Object_165 (Mesh)
                    *   Object_168 (Xform)
                        *   Object_166 (Mesh)
                    *   Object_169 (Xform)
                        *   Object_167 (Mesh)
                    *   Object_170 (Xform)
                        *   Object_168 (Mesh)
                    *   Object_171 (Xform)
                        *   Object_169 (Mesh)
                    *   Object_172 (Xform)
                        *   Object_170 (Mesh)
    *   Cardbox_A1 (Xform)
        *   Cardbox_A1 (Mesh)
        *   Looks (Scope)
            *   Cardboard_A (Material)
                *   Shader (Shader)
    *   Cardbox_A1_01 (Xform)
        *   Cardbox_A1 (Mesh)
        *   Looks (Scope)
            *   Cardboard_A (Material)
                *   Shader (Shader)
    *   Cardbox_A1_02 (Xform)
        *   Cardbox_A1 (Mesh)
        *   Looks (Scope)
            *   Cardboard_A (Material)
                *   Shader (Shader)
    *   Cardbox_A1_03 (Xform)
        *   Cardbox_A1 (Mesh)
        *   Looks (Scope)
            *   Cardboard_A (Material)
                *   Shader (Shader)
    *   Cardbox_A1_04 (Xform)
        *   Cardbox_A1 (Mesh)
        *   Looks (Scope)
            *   Cardboard_A (Material)
                *   Shader (Shader)
    *   Cardbox_A1_05 (Xform)
        *   Cardbox_A1 (Mesh)
        *   Looks (Scope)
            *   Cardboard_A (Material)
                *   Shader (Shader)
    *   Cardbox_A1_06 (Xform)
        *   Cardbox_A1 (Mesh)
        *   Looks (Scope)
            *   Cardboard_A (Material)
                *   Shader (Shader)
    *   Cardbox_A1_07 (Xform)
        *   Cardbox_A1 (Mesh)
        *   Looks (Scope)
            *   Cardboard_A (Material)
                *   Shader (Shader)
    *   Cardbox_A1_08 (Xform)
        *   Cardbox_A1 (Mesh)
        *   Looks (Scope)
            *   Cardboard_A (Material)
                *   Shader (Shader)
    *   Cardbox_A1_09 (Xform)
        *   Cardbox_A1 (Mesh)
        *   Looks (Scope)
            *   Cardboard_A (Material)
                *   Shader (Shader)
    *   Cardbox_A1_10 (Xform)
        *   Cardbox_A1 (Mesh)
        *   Looks (Scope)
            *   Cardboard_A (Material)
                *   Shader (Shader)
    *   Cardbox_A1_11 (Xform)
        *   Cardbox_A1 (Mesh)
        *   Looks (Scope)
            *   Cardboard_A (Material)
                *   Shader (Shader)
    *   Cardbox_A1_12 (Xform)
        *   Cardbox_A1 (Mesh)
        *   Looks (Scope)
            *   Cardboard_A (Material)
                *   Shader (Shader)
    *   Cardbox_A1_13 (Xform)
        *   Cardbox_A1 (Mesh)
        *   Looks (Scope)
            *   Cardboard_A (Material)
                *   Shader (Shader)
    *   Cardbox_A1_14 (Xform)
        *   Cardbox_A1 (Mesh)
        *   Looks (Scope)
            *   Cardboard_A (Material)
                *   Shader (Shader)
    *   Cardbox_A1_15 (Xform)
        *   Cardbox_A1 (Mesh)
        *   Looks (Scope)
            *   Cardboard_A (Material)
                *   Shader (Shader)
    *   Cardbox_A1_16 (Xform)
        *   Cardbox_A1 (Mesh)
        *   Looks (Scope)
            *   Cardboard_A (Material)
                *   Shader (Shader)
    *   Cardbox_A1_17 (Xform)
        *   Cardbox_A1 (Mesh)
        *   Looks (Scope)
            *   Cardboard_A (Material)
                *   Shader (Shader)
    *   Cardbox_A1_18 (Xform)
        *   Cardbox_A1 (Mesh)
        *   Looks (Scope)
            *   Cardboard_A (Material)
                *   Shader (Shader)
    *   Cardbox_A1_19 (Xform)
        *   Cardbox_A1 (Mesh)
        *   Looks (Scope)
            *   Cardboard_A (Material)
                *   Shader (Shader)
    *   Cardbox_A1_20 (Xform)
        *   Cardbox_A1 (Mesh)
        *   Looks (Scope)
            *   Cardboard_A (Material)
                *   Shader (Shader)
    *   Cardbox_A1_21 (Xform)
        *   Cardbox_A1 (Mesh)
        *   Looks (Scope)
            *   Cardboard_A (Material)
                *   Shader (Shader)
    *   Simple_rubber_conveyor_01 (Xform)
        *   Materials (Scope)
            *   Conveyor (Material)
                *   pbr_shader (Shader)
                *   uvset0 (Shader)
                *   tex_base (Shader)
                *   tex_specular (Shader)
                *   tex_glossiness (Shader)
                *   tex_normal (Shader)
                *   tex_occlusion (Shader)
            *   Belt (Material)
                *   pbr_shader (Shader)
                *   uvset0 (Shader)
                *   tex_base (Shader)
        *   Meshes (Xform)
            *   Sketchfab_model (Xform)
                *   Conveyor_FBX (Xform)
                    *   RootNode (Xform)
                        *   Conveyor01Frame (Xform)
                            *   Conveyor01Frame_Conveyor_0 (Xform)
                                *   Conveyor01Frame_Conveyor_0 (Mesh)
                        *   Conveyor01Frame01 (Xform)
                            *   Conveyor01Frame01_Conveyor_0 (Xform)
                                *   Conveyor01Frame01_Conveyor_0 (Mesh)
                        *   Conveyor01Frame02 (Xform)
                            *   Conveyor01Frame02_Conveyor_0 (Xform)
                                *   Conveyor01Frame02_Conveyor_0 (Mesh)
                        *   Conveyor01Legs (Xform)
                            *   Conveyor01Legs_Conveyor_0 (Xform)
                                *   Conveyor01Legs_Conveyor_0 (Mesh)
                        *   Conveyor01Belt (Xform)
                            *   Conveyor01Belt_Belt_0 (Xform)
                                *   Conveyor01Belt_Belt_0 (Mesh)
    *   Cardbox_A1_22 (Xform)
        *   Cardbox_A1 (Mesh)
        *   Looks (Scope)
            *   Cardboard_A (Material)
                *   Shader (Shader)
    *   Cardbox_A1_23 (Xform)
        *   Cardbox_A1 (Mesh)
        *   Looks (Scope)
            *   Cardboard_A (Material)
                *   Shader (Shader)
    *   Cardbox_A1_24 (Xform)
        *   Cardbox_A1 (Mesh)
        *   Looks (Scope)
            *   Cardboard_A (Material)
                *   Shader (Shader)
    *   AGV_ready_02 (Xform)
        *   Materials (Scope)
            *   ASELSAN_CATS_04 (Material)
                *   pbr_shader (Shader)
            *   ASELSAN_CATS_04_2 (Material)
                *   pbr_shader (Shader)
            *   ASELSAN_CATS_13 (Material)
                *   pbr_shader (Shader)
            *   Color_000 (Material)
                *   pbr_shader (Shader)
            *   Color_A05 (Material)
                *   pbr_shader (Shader)
            *   Color_A06 (Material)
                *   pbr_shader (Shader)
            *   Color_B05 (Material)
                *   pbr_shader (Shader)
            *   Color_E02 (Material)
                *   pbr_shader (Shader)
            *   Color_E05 (Material)
                *   pbr_shader (Shader)
            *   Color_F06 (Material)
                *   pbr_shader (Shader)
            *   Color_G03 (Material)
                *   pbr_shader (Shader)
            *   Color_M02 (Material)
                *   pbr_shader (Shader)
            *   Color_M03 (Material)
                *   pbr_shader (Shader)
            *   Mtl39 (Material)
                *   pbr_shader (Shader)
            *   Mtl6 (Material)
                *   pbr_shader (Shader)
                *   uvset0 (Shader)
                *   tex_base (Shader)
            *   Mtl9 (Material)
                *   pbr_shader (Shader)
            *   Silver (Material)
                *   pbr_shader (Shader)
            *   material (Material)
                *   pbr_shader (Shader)
                *   uvset0 (Shader)
                *   tex_base (Shader)
            *   cash_register_keys (Material)
                *   pbr_shader (Shader)
            *   Chris_Shoe_Sole (Material)
                *   pbr_shader (Shader)
            *   Color_002 (Material)
                *   pbr_shader (Shader)
            *   Color_005 (Material)
                *   pbr_shader (Shader)
            *   Color_006 (Material)
                *   pbr_shader (Shader)
            *   Color_008 (Material)
                *   pbr_shader (Shader)
            *   Color_A01 (Material)
                *   pbr_shader (Shader)
            *   Color_A11 (Material)
                *   pbr_shader (Shader)
            *   Color_M04 (Material)
                *   pbr_shader (Shader)
            *   Color_M05 (Material)
                *   pbr_shader (Shader)
            *   Color_M06 (Material)
                *   pbr_shader (Shader)
            *   Color_M07 (Material)
                *   pbr_shader (Shader)
            *   Color_M09 (Material)
                *   pbr_shader (Shader)
            *   FCP_Charcoal_v2 (Material)
                *   pbr_shader (Shader)
            *   FrontColor (Material)
                *   pbr_shader (Shader)
            *   Light_Blue (Material)
                *   pbr_shader (Shader)
            *   M_0011_Seashell (Material)
                *   pbr_shader (Shader)
            *   M_0131_Silver (Material)
                *   pbr_shader (Shader)
            *   M_0134_DimGray (Material)
                *   pbr_shader (Shader)
            *   M_0135_DarkGray (Material)
                *   pbr_shader (Shader)
            *   Metal_Silver (Material)
                *   pbr_shader (Shader)
            *   Mtl1 (Material)
                *   pbr_shader (Shader)
            *   Mtl10 (Material)
                *   pbr_shader (Shader)
            *   Mtl11 (Material)
                *   pbr_shader (Shader)
            *   Mtl12 (Material)
                *   pbr_shader (Shader)
            *   Mtl13 (Material)
                *   pbr_shader (Shader)
            *   Mtl14 (Material)
                *   pbr_shader (Shader)
            *   Mtl15 (Material)
                *   pbr_shader (Shader)
            *   Mtl16 (Material)
                *   pbr_shader (Shader)
            *   Mtl17 (Material)
                *   pbr_shader (Shader)
            *   Mtl3 (Material)
                *   pbr_shader (Shader)
            *   Mtl35 (Material)
                *   pbr_shader (Shader)
            *   Mtl36 (Material)
                *   pbr_shader (Shader)
            *   Mtl37 (Material)
                *   pbr_shader (Shader)
            *   Mtl3a (Material)
                *   pbr_shader (Shader)
            *   Mtl3b (Material)
                *   pbr_shader (Shader)
            *   Mtl5 (Material)
                *   pbr_shader (Shader)
            *   Mtl7 (Material)
                *   pbr_shader (Shader)
            *   Mtl8 (Material)
                *   pbr_shader (Shader)
            *   Mtla (Material)
                *   pbr_shader (Shader)
            *   Mtlb1 (Material)
                *   pbr_shader (Shader)
            *   Stainless_Steel (Material)
                *   pbr_shader (Shader)
            *   Metal_Aluminum_Anodized_1 (Material)
                *   pbr_shader (Shader)
            *   Metal_Aluminum_Anodized_2 (Material)
                *   pbr_shader (Shader)
            *   basic_gray_plastic (Material)
                *   pbr_shader (Shader)
            *   texture (Material)
                *   pbr_shader (Shader)
        *   Meshes (Xform)
            *   Sketchfab_model (Xform)
                *   AGV_ready_1_obj_cleaner_materialmerger_gles (Xform)
                    *   Object_2 (Xform)
                        *   Object_0 (Mesh)
                    *   Object_3 (Xform)
                        *   Object_1 (Mesh)
                    *   Object_4 (Xform)
                        *   Object_2 (Mesh)
                    *   Object_5 (Xform)
                        *   Object_3 (Mesh)
                    *   Object_6 (Xform)
                        *   Object_4 (Mesh)
                    *   Object_7 (Xform)
                        *   Object_5 (Mesh)
                    *   Object_8 (Xform)
                        *   Object_6 (Mesh)
                    *   Object_9 (Xform)
                        *   Object_7 (Mesh)
                    *   Object_10 (Xform)
                        *   Object_8 (Mesh)
                    *   Object_11 (Xform)
                        *   Object_9 (Mesh)
                    *   Object_12 (Xform)
                        *   Object_10 (Mesh)
                    *   Object_13 (Xform)
                        *   Object_11 (Mesh)
                    *   Object_14 (Xform)
                        *   Object_12 (Mesh)
                    *   Object_15 (Xform)
                        *   Object_13 (Mesh)
                    *   Object_16 (Xform)
                        *   Object_14 (Mesh)
                    *   Object_17 (Xform)
                        *   Object_15 (Mesh)
                    *   Object_18 (Xform)
                        *   Object_16 (Mesh)
                    *   Object_19 (Xform)
                        *   Object_17 (Mesh)
                    *   Object_20 (Xform)
                        *   Object_18 (Mesh)
                    *   Object_21 (Xform)
                        *   Object_19 (Mesh)
                    *   Object_22 (Xform)
                        *   Object_20 (Mesh)
                    *   Object_23 (Xform)
                        *   Object_21 (Mesh)
                    *   Object_24 (Xform)
                        *   Object_22 (Mesh)
                    *   Object_25 (Xform)
                        *   Object_23 (Mesh)
                    *   Object_26 (Xform)
                        *   Object_24 (Mesh)
                    *   Object_27 (Xform)
                        *   Object_25 (Mesh)
                    *   Object_28 (Xform)
                        *   Object_26 (Mesh)
                    *   Object_29 (Xform)
                        *   Object_27 (Mesh)
                    *   Object_30 (Xform)
                        *   Object_28 (Mesh)
                    *   Object_31 (Xform)
                        *   Object_29 (Mesh)
                    *   Object_32 (Xform)
                        *   Object_30 (Mesh)
                    *   Object_33 (Xform)
                        *   Object_31 (Mesh)
                    *   Object_34 (Xform)
                        *   Object_32 (Mesh)
                    *   Object_35 (Xform)
                        *   Object_33 (Mesh)
                    *   Object_36 (Xform)
                        *   Object_34 (Mesh)
                    *   Object_37 (Xform)
                        *   Object_35 (Mesh)
                    *   Object_38 (Xform)
                        *   Object_36 (Mesh)
                    *   Object_39 (Xform)
                        *   Object_37 (Mesh)
                    *   Object_40 (Xform)
                        *   Object_38 (Mesh)
                    *   Object_41 (Xform)
                        *   Object_39 (Mesh)
                    *   Object_42 (Xform)
                        *   Object_40 (Mesh)
                    *   Object_43 (Xform)
                        *   Object_41 (Mesh)
                    *   Object_44 (Xform)
                        *   Object_42 (Mesh)
                    *   Object_45 (Xform)
                        *   Object_43 (Mesh)
                    *   Object_46 (Xform)
                        *   Object_44 (Mesh)
                    *   Object_47 (Xform)
                        *   Object_45 (Mesh)
                    *   Object_48 (Xform)
                        *   Object_46 (Mesh)
                    *   Object_49 (Xform)
                        *   Object_47 (Mesh)
                    *   Object_50 (Xform)
                        *   Object_48 (Mesh)
                    *   Object_51 (Xform)
                        *   Object_49 (Mesh)
                    *   Object_52 (Xform)
                        *   Object_50 (Mesh)
                    *   Object_53 (Xform)
                        *   Object_51 (Mesh)
                    *   Object_54 (Xform)
                        *   Object_52 (Mesh)
                    *   Object_55 (Xform)
                        *   Object_53 (Mesh)
                    *   Object_56 (Xform)
                        *   Object_54 (Mesh)
                    *   Object_57 (Xform)
                        *   Object_55 (Mesh)
                    *   Object_58 (Xform)
                        *   Object_56 (Mesh)
                    *   Object_59 (Xform)
                        *   Object_57 (Mesh)
                    *   Object_60 (Xform)
                        *   Object_58 (Mesh)
                    *   Object_61 (Xform)
                        *   Object_59 (Mesh)
                    *   Object_62 (Xform)
                        *   Object_60 (Mesh)
                    *   Object_63 (Xform)
                        *   Object_61 (Mesh)
                    *   Object_64 (Xform)
                        *   Object_62 (Mesh)
                    *   Object_65 (Xform)
                        *   Object_63 (Mesh)
                    *   Object_66 (Xform)
                        *   Object_64 (Mesh)
                    *   Object_67 (Xform)
                        *   Object_65 (Mesh)
                    *   Object_68 (Xform)
                        *   Object_66 (Mesh)
                    *   Object_69 (Xform)
                        *   Object_67 (Mesh)
                    *   Object_70 (Xform)
                        *   Object_68 (Mesh)
                    *   Object_71 (Xform)
                        *   Object_69 (Mesh)
                    *   Object_72 (Xform)
                        *   Object_70 (Mesh)
                    *   Object_73 (Xform)
                        *   Object_71 (Mesh)
                    *   Object_74 (Xform)
                        *   Object_72 (Mesh)
                    *   Object_75 (Xform)
                        *   Object_73 (Mesh)
                    *   Object_76 (Xform)
                        *   Object_74 (Mesh)
                    *   Object_77 (Xform)
                        *   Object_75 (Mesh)
                    *   Object_78 (Xform)
                        *   Object_76 (Mesh)
                    *   Object_79 (Xform)
                        *   Object_77 (Mesh)
                    *   Object_80 (Xform)
                        *   Object_78 (Mesh)
                    *   Object_81 (Xform)
                        *   Object_79 (Mesh)
                    *   Object_82 (Xform)
                        *   Object_80 (Mesh)
                    *   Object_83 (Xform)
                        *   Object_81 (Mesh)
                    *   Object_84 (Xform)
                        *   Object_82 (Mesh)
                    *   Object_85 (Xform)
                        *   Object_83 (Mesh)
                    *   Object_86 (Xform)
                        *   Object_84 (Mesh)
                    *   Object_87 (Xform)
                        *   Object_85 (Mesh)
                    *   Object_88 (Xform)
                        *   Object_86 (Mesh)
                    *   Object_89 (Xform)
                        *   Object_87 (Mesh)
                    *   Object_90 (Xform)
                        *   Object_88 (Mesh)
                    *   Object_91 (Xform)
                        *   Object_89 (Mesh)
                    *   Object_92 (Xform)
                        *   Object_90 (Mesh)
                    *   Object_93 (Xform)
                        *   Object_91 (Mesh)
                    *   Object_94 (Xform)
                        *   Object_92 (Mesh)
                    *   Object_95 (Xform)
                        *   Object_93 (Mesh)
                    *   Object_96 (Xform)
                        *   Object_94 (Mesh)
                    *   Object_97 (Xform)
                        *   Object_95 (Mesh)
                    *   Object_98 (Xform)
                        *   Object_96 (Mesh)
                    *   Object_99 (Xform)
                        *   Object_97 (Mesh)
                    *   Object_100 (Xform)
                        *   Object_98 (Mesh)
                    *   Object_101 (Xform)
                        *   Object_99 (Mesh)
                    *   Object_102 (Xform)
                        *   Object_100 (Mesh)
                    *   Object_103 (Xform)
                        *   Object_101 (Mesh)
                    *   Object_104 (Xform)
                        *   Object_102 (Mesh)
                    *   Object_105 (Xform)
                        *   Object_103 (Mesh)
                    *   Object_106 (Xform)
                        *   Object_104 (Mesh)
                    *   Object_107 (Xform)
                        *   Object_105 (Mesh)
                    *   Object_108 (Xform)
                        *   Object_106 (Mesh)
                    *   Object_109 (Xform)
                        *   Object_107 (Mesh)
                    *   Object_110 (Xform)
                        *   Object_108 (Mesh)
                    *   Object_111 (Xform)
                        *   Object_109 (Mesh)
                    *   Object_112 (Xform)
                        *   Object_110 (Mesh)
                    *   Object_113 (Xform)
                        *   Object_111 (Mesh)
                    *   Object_114 (Xform)
                        *   Object_112 (Mesh)
                    *   Object_115 (Xform)
                        *   Object_113 (Mesh)
                    *   Object_116 (Xform)
                        *   Object_114 (Mesh)
                    *   Object_117 (Xform)
                        *   Object_115 (Mesh)
                    *   Object_118 (Xform)
                        *   Object_116 (Mesh)
                    *   Object_119 (Xform)
                        *   Object_117 (Mesh)
                    *   Object_120 (Xform)
                        *   Object_118 (Mesh)
                    *   Object_121 (Xform)
                        *   Object_119 (Mesh)
                    *   Object_122 (Xform)
                        *   Object_120 (Mesh)
                    *   Object_123 (Xform)
                        *   Object_121 (Mesh)
                    *   Object_124 (Xform)
                        *   Object_122 (Mesh)
                    *   Object_125 (Xform)
                        *   Object_123 (Mesh)
                    *   Object_126 (Xform)
                        *   Object_124 (Mesh)
                    *   Object_127 (Xform)
                        *   Object_125 (Mesh)
                    *   Object_128 (Xform)
                        *   Object_126 (Mesh)
                    *   Object_129 (Xform)
                        *   Object_127 (Mesh)
                    *   Object_130 (Xform)
                        *   Object_128 (Mesh)
                    *   Object_131 (Xform)
                        *   Object_129 (Mesh)
                    *   Object_132 (Xform)
                        *   Object_130 (Mesh)
                    *   Object_133 (Xform)
                        *   Object_131 (Mesh)
                    *   Object_134 (Xform)
                        *   Object_132 (Mesh)
                    *   Object_135 (Xform)
                        *   Object_133 (Mesh)
                    *   Object_136 (Xform)
                        *   Object_134 (Mesh)
                    *   Object_137 (Xform)
                        *   Object_135 (Mesh)
                    *   Object_138 (Xform)
                        *   Object_136 (Mesh)
                    *   Object_139 (Xform)
                        *   Object_137 (Mesh)
                    *   Object_140 (Xform)
                        *   Object_138 (Mesh)
                    *   Object_141 (Xform)
                        *   Object_139 (Mesh)
                    *   Object_142 (Xform)
                        *   Object_140 (Mesh)
                    *   Object_143 (Xform)
                        *   Object_141 (Mesh)
                    *   Object_144 (Xform)
                        *   Object_142 (Mesh)
                    *   Object_145 (Xform)
                        *   Object_143 (Mesh)
                    *   Object_146 (Xform)
                        *   Object_144 (Mesh)
                    *   Object_147 (Xform)
                        *   Object_145 (Mesh)
                    *   Object_148 (Xform)
                        *   Object_146 (Mesh)
                    *   Object_149 (Xform)
                        *   Object_147 (Mesh)
                    *   Object_150 (Xform)
                        *   Object_148 (Mesh)
                    *   Object_151 (Xform)
                        *   Object_149 (Mesh)
                    *   Object_152 (Xform)
                        *   Object_150 (Mesh)
                    *   Object_153 (Xform)
                        *   Object_151 (Mesh)
                    *   Object_154 (Xform)
                        *   Object_152 (Mesh)
                    *   Object_155 (Xform)
                        *   Object_153 (Mesh)
                    *   Object_156 (Xform)
                        *   Object_154 (Mesh)
                    *   Object_157 (Xform)
                        *   Object_155 (Mesh)
                    *   Object_158 (Xform)
                        *   Object_156 (Mesh)
                    *   Object_159 (Xform)
                        *   Object_157 (Mesh)
                    *   Object_160 (Xform)
                        *   Object_158 (Mesh)
                    *   Object_161 (Xform)
                        *   Object_159 (Mesh)
                    *   Object_162 (Xform)
                        *   Object_160 (Mesh)
                    *   Object_163 (Xform)
                        *   Object_161 (Mesh)
                    *   Object_164 (Xform)
                        *   Object_162 (Mesh)
                    *   Object_165 (Xform)
                        *   Object_163 (Mesh)
                    *   Object_166 (Xform)
                        *   Object_164 (Mesh)
                    *   Object_167 (Xform)
                        *   Object_165 (Mesh)
                    *   Object_168 (Xform)
                        *   Object_166 (Mesh)
                    *   Object_169 (Xform)
                        *   Object_167 (Mesh)
                    *   Object_170 (Xform)
                        *   Object_168 (Mesh)
                    *   Object_171 (Xform)
                        *   Object_169 (Mesh)
                    *   Object_172 (Xform)
                        *   Object_170 (Mesh)
    *   Cardbox_A1_25 (Xform)
        *   Cardbox_A1 (Mesh)
        *   Looks (Scope)
            *   Cardboard_A (Material)
                *   Shader (Shader)
    *   HeavyDutyPackingTable_A01_02 (Prim)
    *   forklift (Xform)
        *   S_ForkliftBody (Mesh)
            *   subset (GeomSubset)
        *   S_ForkliftFork (Xform)
            *   S_ForkliftFork (Mesh)
                *   subset (GeomSubset)
            *   collision_box (Mesh)
            *   Materials (Scope)
                *   OmniPBR (Material)
                    *   Shader (Shader)
        *   Materials (Scope)
            *   OmniPBR (Material)
                *   Shader (Shader)
    *   ridgeback_franka (Xform)
        *   world (Xform)
            *   dummy_base_prismatic_x_joint (PhysicsPrismaticJoint)
        *   dummy_base_x (Xform)
            *   dummy_base_prismatic_y_joint (PhysicsPrismaticJoint)
        *   dummy_base_y (Xform)
            *   dummy_base_revolute_z_joint (PhysicsRevoluteJoint)
        *   base_link (Xform)
            *   base_to_arm_mount_joint (PhysicsFixedJoint)
            *   front_laser_joint (PhysicsFixedJoint)
            *   rear_laser_joint (PhysicsFixedJoint)
            *   visuals (Prim)
                *   mesh_0 (Mesh)
                *   mesh_1 (Mesh)
                *   mesh_2 (Mesh)
                *   mesh_3 (Mesh)
                *   mesh_4 (Mesh)
                *   mesh_5 (Mesh)
                *   mesh_6 (Mesh)
                *   mesh_7 (Mesh)
            *   collisions (Prim)
                *   mesh_0 (Mesh)
                *   mesh_1 (Mesh)
        *   arm_mount_link (Xform)
            *   panda_arm_mount_joint (PhysicsFixedJoint)
        *   panda_link0 (Xform)
            *   panda_joint1 (PhysicsRevoluteJoint)
            *   collisions (Mesh)
            *   visuals (Xform)
                *   panda_link0 (Mesh)
                    *   subset (GeomSubset)
                    *   subset_1 (GeomSubset)
                    *   subset_2 (GeomSubset)
                    *   subset_3 (GeomSubset)
                    *   subset_4 (GeomSubset)
                    *   subset_5 (GeomSubset)
                *   Looks (Scope)
                    *   EmissiveBlue (Material)
                        *   Shader (Shader)
                    *   PlasticGray (Material)
                        *   Shader (Shader)
                    *   Aluminum (Material)
                        *   Shader (Shader)
                    *   PlasticBlack (Material)
                        *   Shader (Shader)
                    *   RubberGreen (Material)
                        *   Shader (Shader)
                    *   RubberRed (Material)
                        *   Shader (Shader)
                    *   RubberWhite (Material)
                        *   Shader (Shader)
                    *   RubberGray (Material)
                        *   Shader (Shader)
                    *   RubberLightGray (Material)
                        *   Shader (Shader)
                    *   AluminumRough (Material)
                        *   Shader (Shader)
                    *   rubber_cable (Material)
                        *   Shader (Shader)
                    *   PlasticWhite (Material)
                        *   Shader (Shader)
        *   panda_link1 (Xform)
            *   panda_joint2 (PhysicsRevoluteJoint)
            *   collisions (Mesh)
            *   visuals (Xform)
                *   panda_link1 (Mesh)
                    *   subset (GeomSubset)
                *   Looks (Scope)
                    *   EmissiveBlue (Material)
                        *   Shader (Shader)
                    *   PlasticGray (Material)
                        *   Shader (Shader)
                    *   Aluminum (Material)
                        *   Shader (Shader)
                    *   PlasticBlack (Material)
                        *   Shader (Shader)
                    *   RubberGreen (Material)
                        *   Shader (Shader)
                    *   RubberRed (Material)
                        *   Shader (Shader)
                    *   RubberWhite (Material)
                        *   Shader (Shader)
                    *   RubberGray (Material)
                        *   Shader (Shader)
                    *   RubberLightGray (Material)
                        *   Shader (Shader)
                    *   AluminumRough (Material)
                        *   Shader (Shader)
                    *   rubber_cable (Material)
                        *   Shader (Shader)
                    *   PlasticWhite (Material)
                        *   Shader (Shader)
        *   panda_link2 (Xform)
            *   panda_joint3 (PhysicsRevoluteJoint)
            *   collisions (Mesh)
            *   visuals (Xform)
                *   panda_link2 (Mesh)
                    *   subset (GeomSubset)
                *   Looks (Scope)
                    *   EmissiveBlue (Material)
                        *   Shader (Shader)
                    *   PlasticGray (Material)
                        *   Shader (Shader)
                    *   Aluminum (Material)
                        *   Shader (Shader)
                    *   PlasticBlack (Material)
                        *   Shader (Shader)
                    *   RubberGreen (Material)
                        *   Shader (Shader)
                    *   RubberRed (Material)
                        *   Shader (Shader)
                    *   RubberWhite (Material)
                        *   Shader (Shader)
                    *   RubberGray (Material)
                        *   Shader (Shader)
                    *   RubberLightGray (Material)
                        *   Shader (Shader)
                    *   AluminumRough (Material)
                        *   Shader (Shader)
                    *   rubber_cable (Material)
                        *   Shader (Shader)
                    *   PlasticWhite (Material)
                        *   Shader (Shader)
        *   panda_link3 (Xform)
            *   panda_joint4 (PhysicsRevoluteJoint)
            *   collisions (Mesh)
            *   visuals (Xform)
                *   panda_link3 (Mesh)
                    *   subset (GeomSubset)
                    *   subset_1 (GeomSubset)
                    *   subset_2 (GeomSubset)
                *   Looks (Scope)
                    *   EmissiveBlue (Material)
                        *   Shader (Shader)
                    *   PlasticGray (Material)
                        *   Shader (Shader)
                    *   Aluminum (Material)
                        *   Shader (Shader)
                    *   PlasticBlack (Material)
                        *   Shader (Shader)
                    *   RubberGreen (Material)
                        *   Shader (Shader)
                    *   RubberRed (Material)
                        *   Shader (Shader)
                    *   RubberWhite (Material)
                        *   Shader (Shader)
                    *   RubberGray (Material)
                        *   Shader (Shader)
                    *   RubberLightGray (Material)
                        *   Shader (Shader)
                    *   AluminumRough (Material)
                        *   Shader (Shader)
                    *   rubber_cable (Material)
                        *   Shader (Shader)
                    *   PlasticWhite (Material)
                        *   Shader (Shader)
        *   panda_link4 (Xform)
            *   panda_joint5 (PhysicsRevoluteJoint)
            *   collisions (Mesh)
            *   visuals (Xform)
                *   panda_link4 (Mesh)
                    *   subset (GeomSubset)
                    *   subset_1 (GeomSubset)
                    *   subset_2 (GeomSubset)
                *   Looks (Scope)
                    *   EmissiveBlue (Material)
                        *   Shader (Shader)
                    *   PlasticGray (Material)
                        *   Shader (Shader)
                    *   Aluminum (Material)
                        *   Shader (Shader)
                    *   PlasticBlack (Material)
                        *   Shader (Shader)
                    *   RubberGreen (Material)
                        *   Shader (Shader)
                    *   RubberRed (Material)
                        *   Shader (Shader)
                    *   RubberWhite (Material)
                        *   Shader (Shader)
                    *   RubberGray (Material)
                        *   Shader (Shader)
                    *   RubberLightGray (Material)
                        *   Shader (Shader)
                    *   AluminumRough (Material)
                        *   Shader (Shader)
                    *   rubber_cable (Material)
                        *   Shader (Shader)
                    *   PlasticWhite (Material)
                        *   Shader (Shader)
        *   panda_link5 (Xform)
            *   panda_joint6 (PhysicsRevoluteJoint)
            *   collisions (Mesh)
            *   visuals (Xform)
                *   panda_link5 (Mesh)
                    *   subset (GeomSubset)
                    *   subset_1 (GeomSubset)
                    *   subset_2 (GeomSubset)
                *   Looks (Scope)
                    *   EmissiveBlue (Material)
                        *   Shader (Shader)
                    *   PlasticGray (Material)
                        *   Shader (Shader)
                    *   Aluminum (Material)
                        *   Shader (Shader)
                    *   PlasticBlack (Material)
                        *   Shader (Shader)
                    *   RubberGreen (Material)
                        *   Shader (Shader)
                    *   RubberRed (Material)
                        *   Shader (Shader)
                    *   RubberWhite (Material)
                        *   Shader (Shader)
                    *   RubberGray (Material)
                        *   Shader (Shader)
                    *   RubberLightGray (Material)
                        *   Shader (Shader)
                    *   AluminumRough (Material)
                        *   Shader (Shader)
                    *   rubber_cable (Material)
                        *   Shader (Shader)
                    *   PlasticWhite (Material)
                        *   Shader (Shader)
        *   panda_link6 (Xform)
            *   panda_joint7 (PhysicsRevoluteJoint)
            *   collisions (Mesh)
            *   visuals (Xform)
                *   panda_link6 (Mesh)
                    *   subset (GeomSubset)
                    *   subset_1 (GeomSubset)
                    *   subset_10 (GeomSubset)
                    *   subset_11 (GeomSubset)
                    *   subset_12 (GeomSubset)
                    *   subset_13 (GeomSubset)
                    *   subset_2 (GeomSubset)
                    *   subset_3 (GeomSubset)
                    *   subset_4 (GeomSubset)
                    *   subset_5 (GeomSubset)
                    *   subset_6 (GeomSubset)
                    *   subset_7 (GeomSubset)
                    *   subset_8 (GeomSubset)
                    *   subset_9 (GeomSubset)
                *   Looks (Scope)
                    *   EmissiveBlue (Material)
                        *   Shader (Shader)
                    *   PlasticGray (Material)
                        *   Shader (Shader)
                    *   Aluminum (Material)
                        *   Shader (Shader)
                    *   PlasticBlack (Material)
                        *   Shader (Shader)
                    *   RubberGreen (Material)
                        *   Shader (Shader)
                    *   RubberRed (Material)
                        *   Shader (Shader)
                    *   RubberWhite (Material)
                        *   Shader (Shader)
                    *   RubberGray (Material)
                        *   Shader (Shader)
                    *   RubberLightGray (Material)
                        *   Shader (Shader)
                    *   AluminumRough (Material)
                        *   Shader (Shader)
                    *   rubber_cable (Material)
                        *   Shader (Shader)
                    *   PlasticWhite (Material)
                        *   Shader (Shader)
        *   panda_link7 (Xform)
            *   panda_hand_joint (PhysicsFixedJoint)
            *   collisions (Mesh)
            *   visuals (Xform)
                *   panda_link7 (Mesh)
                    *   subset (GeomSubset)
                    *   subset_1 (GeomSubset)
                    *   subset_2 (GeomSubset)
                    *   subset_3 (GeomSubset)
                *   Looks (Scope)
                    *   EmissiveBlue (Material)
                        *   Shader (Shader)
                    *   PlasticGray (Material)
                        *   Shader (Shader)
                    *   Aluminum (Material)
                        *   Shader (Shader)
                    *   PlasticBlack (Material)
                        *   Shader (Shader)
                    *   RubberGreen (Material)
                        *   Shader (Shader)
                    *   RubberRed (Material)
                        *   Shader (Shader)
                    *   RubberWhite (Material)
                        *   Shader (Shader)
                    *   RubberGray (Material)
                        *   Shader (Shader)
                    *   RubberLightGray (Material)
                        *   Shader (Shader)
                    *   AluminumRough (Material)
                        *   Shader (Shader)
                    *   rubber_cable (Material)
                        *   Shader (Shader)
                    *   PlasticWhite (Material)
                        *   Shader (Shader)
        *   panda_hand (Xform)
            *   panda_finger_joint1 (PhysicsPrismaticJoint)
            *   panda_finger_joint2 (PhysicsPrismaticJoint)
            *   panda_hand_endeffector_joint (PhysicsFixedJoint)
            *   collisions (Mesh)
            *   visuals (Xform)
                *   panda_hand (Mesh)
                    *   subset (GeomSubset)
                    *   subset_1 (GeomSubset)
                    *   subset_2 (GeomSubset)
                    *   subset_3 (GeomSubset)
                    *   subset_4 (GeomSubset)
                *   Looks (Scope)
                    *   EmissiveBlue (Material)
                        *   Shader (Shader)
                    *   PlasticGray (Material)
                        *   Shader (Shader)
                    *   Aluminum (Material)
                        *   Shader (Shader)
                    *   PlasticBlack (Material)
                        *   Shader (Shader)
                    *   RubberGreen (Material)
                        *   Shader (Shader)
                    *   RubberRed (Material)
                        *   Shader (Shader)
                    *   RubberWhite (Material)
                        *   Shader (Shader)
                    *   RubberGray (Material)
                        *   Shader (Shader)
                    *   RubberLightGray (Material)
                        *   Shader (Shader)
                    *   AluminumRough (Material)
                        *   Shader (Shader)
                    *   rubber_cable (Material)
                        *   Shader (Shader)
                    *   PlasticWhite (Material)
                        *   Shader (Shader)
        *   panda_leftfinger (Xform)
            *   collisions (Mesh)
            *   visuals (Xform)
                *   panda_leftfinger (Mesh)
                    *   subset (GeomSubset)
                    *   subset_1 (GeomSubset)
                *   Looks (Scope)
                    *   EmissiveBlue (Material)
                        *   Shader (Shader)
                    *   PlasticGray (Material)
                        *   Shader (Shader)
                    *   Aluminum (Material)
                        *   Shader (Shader)
                    *   PlasticBlack (Material)
                        *   Shader (Shader)
                    *   RubberGreen (Material)
                        *   Shader (Shader)
                    *   RubberRed (Material)
                        *   Shader (Shader)
                    *   RubberWhite (Material)
                        *   Shader (Shader)
                    *   RubberGray (Material)
                        *   Shader (Shader)
                    *   RubberLightGray (Material)
                        *   Shader (Shader)
                    *   AluminumRough (Material)
                        *   Shader (Shader)
                    *   rubber_cable (Material)
                        *   Shader (Shader)
                    *   PlasticWhite (Material)
                        *   Shader (Shader)
        *   panda_rightfinger (Xform)
            *   collisions (Mesh)
            *   visuals (Xform)
                *   panda_rightfinger (Mesh)
                    *   subset (GeomSubset)
                    *   subset_1 (GeomSubset)
                *   Looks (Scope)
                    *   EmissiveBlue (Material)
                        *   Shader (Shader)
                    *   PlasticGray (Material)
                        *   Shader (Shader)
                    *   Aluminum (Material)
                        *   Shader (Shader)
                    *   PlasticBlack (Material)
                        *   Shader (Shader)
                    *   RubberGreen (Material)
                        *   Shader (Shader)
                    *   RubberRed (Material)
                        *   Shader (Shader)
                    *   RubberWhite (Material)
                        *   Shader (Shader)
                    *   RubberGray (Material)
                        *   Shader (Shader)
                    *   RubberLightGray (Material)
                        *   Shader (Shader)
                    *   AluminumRough (Material)
                        *   Shader (Shader)
                    *   rubber_cable (Material)
                        *   Shader (Shader)
                    *   PlasticWhite (Material)
                        *   Shader (Shader)
        *   endeffector (Xform)
        *   front_laser (Xform)
            *   visuals (Mesh)
            *   collisions (Cube)
        *   rear_laser (Xform)
            *   visuals (Mesh)
            *   collisions (Cube)
        *   Looks (Scope)
            *   material_black (Material)
                *   Shader (Shader)
            *   material_dark_grey (Material)
                *   Shader (Shader)
            *   material_grasp_loc_color (Material)
                *   Shader (Shader)
            *   material_light_grey (Material)
                *   Shader (Shader)
            *   material_panda_white (Material)
                *   Shader (Shader)
            *   material_red (Material)
                *   Shader (Shader)
            *   material_white (Material)
                *   Shader (Shader)
            *   material_yellow (Material)
                *   Shader (Shader)
            *   material_Face636_001 (Material)
                *   Shader (Shader)
            *   material_Part__Feature017_001 (Material)
                *   Shader (Shader)
            *   material_Part__Feature019_001 (Material)
                *   Shader (Shader)
            *   material_Part__Feature023_001 (Material)
                *   Shader (Shader)
            *   material_Part__Feature_001 (Material)
                *   Shader (Shader)
            *   material_Part__Feature024 (Material)
                *   Shader (Shader)
            *   material_Part__Feature001_010_001_002 (Material)
                *   Shader (Shader)
            *   material_Part__Feature_001_001_001_002 (Material)
                *   Shader (Shader)
            *   material_Part__Feature001_001_003_001 (Material)
                *   Shader (Shader)
            *   material_Part__Feature002_001_003_001 (Material)
                *   Shader (Shader)
            *   material_Part__Feature_002_004_003 (Material)
                *   Shader (Shader)
            *   material_Shell001_001_001_003 (Material)
                *   Shader (Shader)
            *   material_Face064_002_001_002_001 (Material)
                *   Shader (Shader)
            *   material_Face065_002_001_002_001 (Material)
                *   Shader (Shader)
            *   material_Face374_002_001_002_001 (Material)
                *   Shader (Shader)
            *   material_Face539_002_001_002_001 (Material)
                *   Shader (Shader)
            *   material_Shell006_003_002_001 (Material)
                *   Shader (Shader)
            *   material_Shell007_002_002_001 (Material)
                *   Shader (Shader)
            *   material_Union001_001_001_002_001 (Material)
                *   Shader (Shader)
            *   material_Part__Mirroring001_004_002 (Material)
                *   Shader (Shader)
            *   material_Part__Mirroring002_004_001 (Material)
                *   Shader (Shader)
            *   material_Part__Mirroring004_004_002 (Material)
                *   Shader (Shader)
            *   material_Part__Mirroring_004_001 (Material)
                *   Shader (Shader)
            *   material_Part__Feature001_008_005 (Material)
                *   Shader (Shader)
            *   material_Part__Feature002_005_005 (Material)
                *   Shader (Shader)
            *   material_Part__Feature005_001_005 (Material)
                *   Shader (Shader)
            *   material_Part__Feature_009_005 (Material)
                *   Shader (Shader)
            *   material_Part__Feature001_006 (Material)
                *   Shader (Shader)
            *   material_Part__Feature_007 (Material)
                *   Shader (Shader)
    *   HeavyDutyPackingTable_A01_03 (Prim)
    *   Robotic_Manipulator_low_poly_01 (Prim)
    *   forklift_01 (Prim)
*   Environment (Xform)
    *   defaultLight (DistantLight)
*   Render (Prim)
    *   OmniverseKit (Prim)
        *   HydraTextures (Prim)
            *   omni_kit_widget_viewport_ViewportTexture_0 (RenderProduct)
    *   OmniverseGlobalRenderSettings (RenderSettings)
    *   Vars (Prim)
        *   LdrColor (RenderVar)

## 3. 对象详细描述 (Detailed Prim Descriptions)

### /World/Building
*  **Prim路径 (Prim Path):**/World/Building
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '../scene/Building/Building.usdc'
*  **世界包围盒 (World BBox):**
   *   Size: '(5419.311, 1428.029, 5000.000)'
   *   Center: '(-1.009, 0.654, 6.890)'


---


### /World/Robotic_Manipulator_low_poly
*  **Prim路径 (Prim Path):**/World/Robotic_Manipulator_low_poly
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '../assets/Robotic_Manipulator_low_poly/Robotic_Manipulator_low_poly.usdc'
*  **世界包围盒 (World BBox):**
   *   Size: '(1.174, 0.951, 0.727)'
   *   Center: '(0.111, -3.052, 1.490)'


---


### /World/Simple_rubber_conveyor
*  **Prim路径 (Prim Path):**/World/Simple_rubber_conveyor
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '../assets/Simple_rubber_conveyor/Simple_rubber_conveyor.usdc'
*  **世界包围盒 (World BBox):**
   *   Size: '(188.440, 149.880, 400.080)'
   *   Center: '(1.387, -1.752, 0.785)'


---


### /World/AGV_ready_1
*  **Prim路径 (Prim Path):**/World/AGV_ready_1
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '../assets/AGV_ready_1/AGV_ready_1.usdc'
*  **世界包围盒 (World BBox):**
   *   Size: '(1.457, 0.340, 0.669)'
   *   Center: '(-1.208, 0.401, 0.001)'


---


### /World/Cardbox_A1
*  **Prim路径 (Prim Path):**/World/Cardbox_A1
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '../Assets/new/Industrial_NVD@10012/Assets/ArchVis/Industrial/Containers/Cardboard/Cardbox_A1.usd'
*  **世界包围盒 (World BBox):**
   *   Size: '(69.944, 52.115, 50.993)'
   *   Center: '(3.000, -1.826, 1.718)'


---


### /World/Cardbox_A1_01
*  **Prim路径 (Prim Path):**/World/Cardbox_A1_01
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '../Assets/new/Industrial_NVD@10012/Assets/ArchVis/Industrial/Containers/Cardboard/Cardbox_A1.usd'
*  **世界包围盒 (World BBox):**
   *   Size: '(69.944, 52.115, 50.993)'
   *   Center: '(2.000, -1.826, 1.718)'


---


### /World/Cardbox_A1_02
*  **Prim路径 (Prim Path):**/World/Cardbox_A1_02
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '../Assets/new/Industrial_NVD@10012/Assets/ArchVis/Industrial/Containers/Cardboard/Cardbox_A1.usd'
*  **世界包围盒 (World BBox):**
   *   Size: '(69.944, 52.115, 50.993)'
   *   Center: '(1.000, -1.826, 1.718)'


---


### /World/Cardbox_A1_03
*  **Prim路径 (Prim Path):**/World/Cardbox_A1_03
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '../Assets/new/Industrial_NVD@10012/Assets/ArchVis/Industrial/Containers/Cardboard/Cardbox_A1.usd'
*  **世界包围盒 (World BBox):**
   *   Size: '(69.944, 52.115, 50.993)'
   *   Center: '(0.000, -1.826, 1.718)'


---


### /World/Cardbox_A1_04
*  **Prim路径 (Prim Path):**/World/Cardbox_A1_04
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '../Assets/new/Industrial_NVD@10012/Assets/ArchVis/Industrial/Containers/Cardboard/Cardbox_A1.usd'
*  **世界包围盒 (World BBox):**
   *   Size: '(69.944, 52.115, 50.993)'
   *   Center: '(-0.968, -0.430, 0.255)'


---


### /World/Cardbox_A1_05
*  **Prim路径 (Prim Path):**/World/Cardbox_A1_05
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '../Assets/new/Industrial_NVD@10012/Assets/ArchVis/Industrial/Containers/Cardboard/Cardbox_A1.usd'
*  **世界包围盒 (World BBox):**
   *   Size: '(69.944, 52.115, 50.993)'
   *   Center: '(-1.768, -0.430, 0.255)'


---


### /World/Cardbox_A1_06
*  **Prim路径 (Prim Path):**/World/Cardbox_A1_06
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '../Assets/new/Industrial_NVD@10012/Assets/ArchVis/Industrial/Containers/Cardboard/Cardbox_A1.usd'
*  **世界包围盒 (World BBox):**
   *   Size: '(69.944, 52.115, 50.993)'
   *   Center: '(-0.968, -1.158, 0.255)'


---


### /World/Cardbox_A1_07
*  **Prim路径 (Prim Path):**/World/Cardbox_A1_07
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '../Assets/new/Industrial_NVD@10012/Assets/ArchVis/Industrial/Containers/Cardboard/Cardbox_A1.usd'
*  **世界包围盒 (World BBox):**
   *   Size: '(69.944, 52.115, 50.993)'
   *   Center: '(-0.968, -1.958, 0.255)'


---


### /World/Cardbox_A1_08
*  **Prim路径 (Prim Path):**/World/Cardbox_A1_08
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '../Assets/new/Industrial_NVD@10012/Assets/ArchVis/Industrial/Containers/Cardboard/Cardbox_A1.usd'
*  **世界包围盒 (World BBox):**
   *   Size: '(69.944, 52.115, 50.993)'
   *   Center: '(-1.768, -1.958, 0.255)'


---


### /World/Cardbox_A1_09
*  **Prim路径 (Prim Path):**/World/Cardbox_A1_09
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '../Assets/new/Industrial_NVD@10012/Assets/ArchVis/Industrial/Containers/Cardboard/Cardbox_A1.usd'
*  **世界包围盒 (World BBox):**
   *   Size: '(69.944, 52.115, 50.993)'
   *   Center: '(-1.768, -1.158, 0.255)'


---


### /World/Cardbox_A1_10
*  **Prim路径 (Prim Path):**/World/Cardbox_A1_10
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '../Assets/new/Industrial_NVD@10012/Assets/ArchVis/Industrial/Containers/Cardboard/Cardbox_A1.usd'
*  **世界包围盒 (World BBox):**
   *   Size: '(69.944, 52.115, 50.993)'
   *   Center: '(-1.450, -1.513, 0.762)'


---


### /World/Cardbox_A1_11
*  **Prim路径 (Prim Path):**/World/Cardbox_A1_11
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '../Assets/new/Industrial_NVD@10012/Assets/ArchVis/Industrial/Containers/Cardboard/Cardbox_A1.usd'
*  **世界包围盒 (World BBox):**
   *   Size: '(69.944, 52.115, 50.993)'
   *   Center: '(-1.450, -0.783, 0.762)'


---


### /World/Cardbox_A1_12
*  **Prim路径 (Prim Path):**/World/Cardbox_A1_12
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '../Assets/new/Industrial_NVD@10012/Assets/ArchVis/Industrial/Containers/Cardboard/Cardbox_A1.usd'
*  **世界包围盒 (World BBox):**
   *   Size: '(69.944, 52.115, 50.993)'
   *   Center: '(-1.450, -1.159, 1.273)'


---


### /World/Cardbox_A1_13
*  **Prim路径 (Prim Path):**/World/Cardbox_A1_13
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '../Assets/new/Industrial_NVD@10012/Assets/ArchVis/Industrial/Containers/Cardboard/Cardbox_A1.usd'
*  **世界包围盒 (World BBox):**
   *   Size: '(69.944, 52.115, 50.993)'
   *   Center: '(2.000, 4.203, 1.718)'


---


### /World/Cardbox_A1_14
*  **Prim路径 (Prim Path):**/World/Cardbox_A1_14
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '../Assets/new/Industrial_NVD@10012/Assets/ArchVis/Industrial/Containers/Cardboard/Cardbox_A1.usd'
*  **世界包围盒 (World BBox):**
   *   Size: '(69.944, 52.115, 50.993)'
   *   Center: '(-1.634, 4.249, 0.255)'


---


### /World/Cardbox_A1_15
*  **Prim路径 (Prim Path):**/World/Cardbox_A1_15
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '../Assets/new/Industrial_NVD@10012/Assets/ArchVis/Industrial/Containers/Cardboard/Cardbox_A1.usd'
*  **世界包围盒 (World BBox):**
   *   Size: '(69.944, 52.115, 50.993)'
   *   Center: '(-1.315, 5.048, 1.273)'


---


### /World/Cardbox_A1_16
*  **Prim路径 (Prim Path):**/World/Cardbox_A1_16
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '../Assets/new/Industrial_NVD@10012/Assets/ArchVis/Industrial/Containers/Cardboard/Cardbox_A1.usd'
*  **世界包围盒 (World BBox):**
   *   Size: '(69.944, 52.115, 50.993)'
   *   Center: '(-0.834, 4.249, 0.255)'


---


### /World/Cardbox_A1_17
*  **Prim路径 (Prim Path):**/World/Cardbox_A1_17
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '../Assets/new/Industrial_NVD@10012/Assets/ArchVis/Industrial/Containers/Cardboard/Cardbox_A1.usd'
*  **世界包围盒 (World BBox):**
   *   Size: '(69.944, 52.115, 50.993)'
   *   Center: '(-0.000, 4.203, 1.718)'


---


### /World/Cardbox_A1_18
*  **Prim路径 (Prim Path):**/World/Cardbox_A1_18
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '../Assets/new/Industrial_NVD@10012/Assets/ArchVis/Industrial/Containers/Cardboard/Cardbox_A1.usd'
*  **世界包围盒 (World BBox):**
   *   Size: '(69.944, 52.115, 50.993)'
   *   Center: '(-1.315, 5.424, 0.762)'


---


### /World/Cardbox_A1_19
*  **Prim路径 (Prim Path):**/World/Cardbox_A1_19
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '../Assets/new/Industrial_NVD@10012/Assets/ArchVis/Industrial/Containers/Cardboard/Cardbox_A1.usd'
*  **世界包围盒 (World BBox):**
   *   Size: '(69.944, 52.115, 50.993)'
   *   Center: '(1.000, 4.203, 1.718)'


---


### /World/Cardbox_A1_20
*  **Prim路径 (Prim Path):**/World/Cardbox_A1_20
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '../Assets/new/Industrial_NVD@10012/Assets/ArchVis/Industrial/Containers/Cardboard/Cardbox_A1.usd'
*  **世界包围盒 (World BBox):**
   *   Size: '(69.944, 52.115, 50.993)'
   *   Center: '(-1.315, 4.694, 0.762)'


---


### /World/Cardbox_A1_21
*  **Prim路径 (Prim Path):**/World/Cardbox_A1_21
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '../Assets/new/Industrial_NVD@10012/Assets/ArchVis/Industrial/Containers/Cardboard/Cardbox_A1.usd'
*  **世界包围盒 (World BBox):**
   *   Size: '(69.944, 52.115, 50.993)'
   *   Center: '(-0.834, 5.049, 0.255)'


---


### /World/Simple_rubber_conveyor_01
*  **Prim路径 (Prim Path):**/World/Simple_rubber_conveyor_01
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '../assets/Simple_rubber_conveyor/Simple_rubber_conveyor.usdc'
*  **世界包围盒 (World BBox):**
   *   Size: '(188.440, 149.880, 400.080)'
   *   Center: '(1.387, 4.277, 0.785)'


---


### /World/Cardbox_A1_22
*  **Prim路径 (Prim Path):**/World/Cardbox_A1_22
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '../Assets/new/Industrial_NVD@10012/Assets/ArchVis/Industrial/Containers/Cardboard/Cardbox_A1.usd'
*  **世界包围盒 (World BBox):**
   *   Size: '(69.944, 52.115, 50.993)'
   *   Center: '(-1.634, 5.049, 0.255)'


---


### /World/Cardbox_A1_23
*  **Prim路径 (Prim Path):**/World/Cardbox_A1_23
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '../Assets/new/Industrial_NVD@10012/Assets/ArchVis/Industrial/Containers/Cardboard/Cardbox_A1.usd'
*  **世界包围盒 (World BBox):**
   *   Size: '(69.944, 52.115, 50.993)'
   *   Center: '(-1.634, 5.777, 0.255)'


---


### /World/Cardbox_A1_24
*  **Prim路径 (Prim Path):**/World/Cardbox_A1_24
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '../Assets/new/Industrial_NVD@10012/Assets/ArchVis/Industrial/Containers/Cardboard/Cardbox_A1.usd'
*  **世界包围盒 (World BBox):**
   *   Size: '(69.944, 52.115, 50.993)'
   *   Center: '(3.000, 4.203, 1.718)'


---


### /World/AGV_ready_02
*  **Prim路径 (Prim Path):**/World/AGV_ready_02
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '../assets/AGV_ready_1/AGV_ready_1.usdc'
*  **世界包围盒 (World BBox):**
   *   Size: '(1.457, 0.340, 0.669)'
   *   Center: '(-1.208, 6.431, 0.001)'


---


### /World/Cardbox_A1_25
*  **Prim路径 (Prim Path):**/World/Cardbox_A1_25
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '../Assets/new/Industrial_NVD@10012/Assets/ArchVis/Industrial/Containers/Cardboard/Cardbox_A1.usd'
*  **世界包围盒 (World BBox):**
   *   Size: '(69.944, 52.115, 50.993)'
   *   Center: '(-0.834, 5.777, 0.255)'


---


### /World/forklift
*  **Prim路径 (Prim Path):**/World/forklift
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '../device_data/usdz/Forklift/forklift.usdz'
*  **世界包围盒 (World BBox):**
   *   Size: '(1.214, 3.495, 2.155)'
   *   Center: '(-3.728, 5.951, 1.076)'


---


### /World/ridgeback_franka
*  **Prim路径 (Prim Path):**/World/ridgeback_franka
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '../device_data/usdz/IndustrialRobot/ridgeback_franka.usdz'
*  **世界包围盒 (World BBox):**
   *   Size: '(1.543, 0.793, 1.134)'
   *   Center: '(-3.243, 2.582, 0.571)'


---


## 4. 材质库 (Material Library)

### /World/Building/Materials/industrialWindow_Small
*  **Prim路径 (Prim Path):**/World/Building/Materials/industrialWindow_Small
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/Building/Materials/industrialWindow_Small/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/Building/Materials/industrialWindow_Small/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f]
               *   Connected: '/World/Building/Materials/industrialWindow_Small/tex_base.outputs:rgb' @ '/World/Building/Materials/industrialWindow_Small/tex_base'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/industrialWindow-Small_baseColor.jpg'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float]
               *   Connected: '/World/Building/Materials/industrialWindow_Small/tex_metallic.outputs:r' @ '/World/Building/Materials/industrialWindow_Small/tex_metallic'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/industrialWindow-Small_metallicRoughness_metal_scale0.jpg'
           *   'normal' [normal3f]
               *   Connected: '/World/Building/Materials/industrialWindow_Small/tex_normal.outputs:rgb' @ '/World/Building/Materials/industrialWindow_Small/tex_normal'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/industrialWindow-Small_normal.jpg'
           *   'occlusion' [float] = '1'
           *   'roughness' [float]
               *   Connected: '/World/Building/Materials/industrialWindow_Small/tex_roughness.outputs:r' @ '/World/Building/Materials/industrialWindow_Small/tex_roughness'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/industrialWindow-Small_metallicRoughness_rough.jpg'
       *   '/World/Building/Materials/industrialWindow_Small/tex_base' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/industrialWindow-Small_baseColor.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
           *   'file' [asset] = '0/industrialWindow-Small_baseColor.jpg'
           *   'st' [float2]
               *   Connected: '/World/Building/Materials/industrialWindow_Small/uvset0.outputs:result' @ '/World/Building/Materials/industrialWindow_Small/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/Building/Materials/industrialWindow_Small/uvset0' (ID: 'UsdPrimvarReader_float2')
       *   Implementation: 'id'
       *   '/World/Building/Materials/industrialWindow_Small/tex_metallic' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/industrialWindow-Small_metallicRoughness_metal_scale0.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(0.000, 0.000, 0.000, 1.000)'
           *   'file' [asset] = '0/industrialWindow-Small_metallicRoughness_metal_scale0.jpg'
           *   'st' [float2]
               *   Connected: '/World/Building/Materials/industrialWindow_Small/uvset0.outputs:result' @ '/World/Building/Materials/industrialWindow_Small/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/Building/Materials/industrialWindow_Small/tex_normal' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/industrialWindow-Small_normal.jpg'
       *   Inputs:
           *   'bias' [float4] = '(-1.000, -1.000, -1.000, -1.000)'
           *   'fallback' [float4] = '(0.000, 0.000, 1.000, 1.000)'
           *   'file' [asset] = '0/industrialWindow-Small_normal.jpg'
           *   'scale' [float4] = '(2.000, 2.000, 2.000, 2.000)'
           *   'st' [float2]
               *   Connected: '/World/Building/Materials/industrialWindow_Small/uvset0.outputs:result' @ '/World/Building/Materials/industrialWindow_Small/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/Building/Materials/industrialWindow_Small/tex_roughness' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/industrialWindow-Small_metallicRoughness_rough.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(1.000, 0.000, 0.000, 1.000)'
           *   'file' [asset] = '0/industrialWindow-Small_metallicRoughness_rough.jpg'
           *   'st' [float2]
               *   Connected: '/World/Building/Materials/industrialWindow_Small/uvset0.outputs:result' @ '/World/Building/Materials/industrialWindow_Small/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'


---


### /World/Building/Materials/industrialDoor
*  **Prim路径 (Prim Path):**/World/Building/Materials/industrialDoor
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/Building/Materials/industrialDoor/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/Building/Materials/industrialDoor/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f]
               *   Connected: '/World/Building/Materials/industrialDoor/tex_base.outputs:rgb' @ '/World/Building/Materials/industrialDoor/tex_base'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/industrialDoor_baseColor.jpg'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float]
               *   Connected: '/World/Building/Materials/industrialDoor/tex_metallic.outputs:r' @ '/World/Building/Materials/industrialDoor/tex_metallic'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/industrialDoor_metallicRoughness_metal_scale0.jpg'
           *   'normal' [normal3f]
               *   Connected: '/World/Building/Materials/industrialDoor/tex_normal.outputs:rgb' @ '/World/Building/Materials/industrialDoor/tex_normal'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/industrialDoor_normal.jpg'
           *   'occlusion' [float] = '1'
           *   'roughness' [float]
               *   Connected: '/World/Building/Materials/industrialDoor/tex_roughness.outputs:r' @ '/World/Building/Materials/industrialDoor/tex_roughness'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/industrialDoor_metallicRoughness_rough.jpg'
       *   '/World/Building/Materials/industrialDoor/tex_base' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/industrialDoor_baseColor.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
           *   'file' [asset] = '0/industrialDoor_baseColor.jpg'
           *   'st' [float2]
               *   Connected: '/World/Building/Materials/industrialDoor/uvset0.outputs:result' @ '/World/Building/Materials/industrialDoor/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/Building/Materials/industrialDoor/uvset0' (ID: 'UsdPrimvarReader_float2')
       *   Implementation: 'id'
       *   '/World/Building/Materials/industrialDoor/tex_metallic' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/industrialDoor_metallicRoughness_metal_scale0.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(0.000, 0.000, 0.000, 1.000)'
           *   'file' [asset] = '0/industrialDoor_metallicRoughness_metal_scale0.jpg'
           *   'st' [float2]
               *   Connected: '/World/Building/Materials/industrialDoor/uvset0.outputs:result' @ '/World/Building/Materials/industrialDoor/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/Building/Materials/industrialDoor/tex_normal' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/industrialDoor_normal.jpg'
       *   Inputs:
           *   'bias' [float4] = '(-1.000, -1.000, -1.000, -1.000)'
           *   'fallback' [float4] = '(0.000, 0.000, 1.000, 1.000)'
           *   'file' [asset] = '0/industrialDoor_normal.jpg'
           *   'scale' [float4] = '(2.000, 2.000, 2.000, 2.000)'
           *   'st' [float2]
               *   Connected: '/World/Building/Materials/industrialDoor/uvset0.outputs:result' @ '/World/Building/Materials/industrialDoor/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/Building/Materials/industrialDoor/tex_roughness' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/industrialDoor_metallicRoughness_rough.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(1.000, 0.000, 0.000, 1.000)'
           *   'file' [asset] = '0/industrialDoor_metallicRoughness_rough.jpg'
           *   'st' [float2]
               *   Connected: '/World/Building/Materials/industrialDoor/uvset0.outputs:result' @ '/World/Building/Materials/industrialDoor/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'


---


### /World/Building/Materials/Atlas_2048x2048_01
*  **Prim路径 (Prim Path):**/World/Building/Materials/Atlas_2048x2048_01
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/Building/Materials/Atlas_2048x2048_01/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/Building/Materials/Atlas_2048x2048_01/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f]
               *   Connected: '/World/Building/Materials/Atlas_2048x2048_01/tex_base.outputs:rgb' @ '/World/Building/Materials/Atlas_2048x2048_01/tex_base'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/Atlas_2048x2048_01_baseColor.jpg'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float]
               *   Connected: '/World/Building/Materials/Atlas_2048x2048_01/tex_metallic.outputs:r' @ '/World/Building/Materials/Atlas_2048x2048_01/tex_metallic'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/Atlas_2048x2048_01_metallicRoughness_metal_scale0.jpg'
           *   'normal' [normal3f]
               *   Connected: '/World/Building/Materials/Atlas_2048x2048_01/tex_normal.outputs:rgb' @ '/World/Building/Materials/Atlas_2048x2048_01/tex_normal'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/Atlas_2048x2048_01_normal.jpg'
           *   'occlusion' [float] = '1'
           *   'roughness' [float]
               *   Connected: '/World/Building/Materials/Atlas_2048x2048_01/tex_roughness.outputs:r' @ '/World/Building/Materials/Atlas_2048x2048_01/tex_roughness'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/Atlas_2048x2048_01_metallicRoughness_rough.jpg'
       *   '/World/Building/Materials/Atlas_2048x2048_01/tex_base' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/Atlas_2048x2048_01_baseColor.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
           *   'file' [asset] = '0/Atlas_2048x2048_01_baseColor.jpg'
           *   'st' [float2]
               *   Connected: '/World/Building/Materials/Atlas_2048x2048_01/uvset0.outputs:result' @ '/World/Building/Materials/Atlas_2048x2048_01/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/Building/Materials/Atlas_2048x2048_01/uvset0' (ID: 'UsdPrimvarReader_float2')
       *   Implementation: 'id'
       *   '/World/Building/Materials/Atlas_2048x2048_01/tex_metallic' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/Atlas_2048x2048_01_metallicRoughness_metal_scale0.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(0.000, 0.000, 0.000, 1.000)'
           *   'file' [asset] = '0/Atlas_2048x2048_01_metallicRoughness_metal_scale0.jpg'
           *   'st' [float2]
               *   Connected: '/World/Building/Materials/Atlas_2048x2048_01/uvset0.outputs:result' @ '/World/Building/Materials/Atlas_2048x2048_01/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/Building/Materials/Atlas_2048x2048_01/tex_normal' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/Atlas_2048x2048_01_normal.jpg'
       *   Inputs:
           *   'bias' [float4] = '(-1.000, -1.000, -1.000, -1.000)'
           *   'fallback' [float4] = '(0.000, 0.000, 1.000, 1.000)'
           *   'file' [asset] = '0/Atlas_2048x2048_01_normal.jpg'
           *   'scale' [float4] = '(2.000, 2.000, 2.000, 2.000)'
           *   'st' [float2]
               *   Connected: '/World/Building/Materials/Atlas_2048x2048_01/uvset0.outputs:result' @ '/World/Building/Materials/Atlas_2048x2048_01/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/Building/Materials/Atlas_2048x2048_01/tex_roughness' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/Atlas_2048x2048_01_metallicRoughness_rough.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(1.000, 0.000, 0.000, 1.000)'
           *   'file' [asset] = '0/Atlas_2048x2048_01_metallicRoughness_rough.jpg'
           *   'st' [float2]
               *   Connected: '/World/Building/Materials/Atlas_2048x2048_01/uvset0.outputs:result' @ '/World/Building/Materials/Atlas_2048x2048_01/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'


---


### /World/Building/Materials/decalMoss01
*  **Prim路径 (Prim Path):**/World/Building/Materials/decalMoss01
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/Building/Materials/decalMoss01/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/Building/Materials/decalMoss01/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f]
               *   Connected: '/World/Building/Materials/decalMoss01/tex_base.outputs:rgb' @ '/World/Building/Materials/decalMoss01/tex_base'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/decalMoss01_baseColor.png'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'opacity' [float]
               *   Connected: '/World/Building/Materials/decalMoss01/tex_base.outputs:a' @ '/World/Building/Materials/decalMoss01/tex_base'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/decalMoss01_baseColor.png'
           *   'roughness' [float] = '0.821115'
       *   '/World/Building/Materials/decalMoss01/tex_base' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/decalMoss01_baseColor.png'
       *   Inputs:
           *   'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
           *   'file' [asset] = '0/decalMoss01_baseColor.png'
           *   'st' [float2]
               *   Connected: '/World/Building/Materials/decalMoss01/uvset0.outputs:result' @ '/World/Building/Materials/decalMoss01/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/Building/Materials/decalMoss01/uvset0' (ID: 'UsdPrimvarReader_float2')
       *   Implementation: 'id'


---


### /World/Building/Materials/woodenFence
*  **Prim路径 (Prim Path):**/World/Building/Materials/woodenFence
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/Building/Materials/woodenFence/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/Building/Materials/woodenFence/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f]
               *   Connected: '/World/Building/Materials/woodenFence/tex_base.outputs:rgb' @ '/World/Building/Materials/woodenFence/tex_base'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/woodenFence_baseColor.jpg'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float]
               *   Connected: '/World/Building/Materials/woodenFence/tex_metallic.outputs:r' @ '/World/Building/Materials/woodenFence/tex_metallic'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/woodenFence_metallicRoughness_metal_scale0.jpg'
           *   'normal' [normal3f]
               *   Connected: '/World/Building/Materials/woodenFence/tex_normal.outputs:rgb' @ '/World/Building/Materials/woodenFence/tex_normal'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/woodenFence_normal.jpg'
           *   'occlusion' [float] = '1'
           *   'roughness' [float]
               *   Connected: '/World/Building/Materials/woodenFence/tex_roughness.outputs:r' @ '/World/Building/Materials/woodenFence/tex_roughness'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/woodenFence_metallicRoughness_rough.jpg'
       *   '/World/Building/Materials/woodenFence/tex_base' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/woodenFence_baseColor.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
           *   'file' [asset] = '0/woodenFence_baseColor.jpg'
           *   'st' [float2]
               *   Connected: '/World/Building/Materials/woodenFence/uvset0.outputs:result' @ '/World/Building/Materials/woodenFence/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/Building/Materials/woodenFence/uvset0' (ID: 'UsdPrimvarReader_float2')
       *   Implementation: 'id'
       *   '/World/Building/Materials/woodenFence/tex_metallic' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/woodenFence_metallicRoughness_metal_scale0.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(0.000, 0.000, 0.000, 1.000)'
           *   'file' [asset] = '0/woodenFence_metallicRoughness_metal_scale0.jpg'
           *   'st' [float2]
               *   Connected: '/World/Building/Materials/woodenFence/uvset0.outputs:result' @ '/World/Building/Materials/woodenFence/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/Building/Materials/woodenFence/tex_normal' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/woodenFence_normal.jpg'
       *   Inputs:
           *   'bias' [float4] = '(-1.000, -1.000, -1.000, -1.000)'
           *   'fallback' [float4] = '(0.000, 0.000, 1.000, 1.000)'
           *   'file' [asset] = '0/woodenFence_normal.jpg'
           *   'scale' [float4] = '(2.000, 2.000, 2.000, 2.000)'
           *   'st' [float2]
               *   Connected: '/World/Building/Materials/woodenFence/uvset0.outputs:result' @ '/World/Building/Materials/woodenFence/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/Building/Materials/woodenFence/tex_roughness' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/woodenFence_metallicRoughness_rough.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(1.000, 0.000, 0.000, 1.000)'
           *   'file' [asset] = '0/woodenFence_metallicRoughness_rough.jpg'
           *   'st' [float2]
               *   Connected: '/World/Building/Materials/woodenFence/uvset0.outputs:result' @ '/World/Building/Materials/woodenFence/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'


---


### /World/Building/Materials/eletricBox_001
*  **Prim路径 (Prim Path):**/World/Building/Materials/eletricBox_001
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/Building/Materials/eletricBox_001/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/Building/Materials/eletricBox_001/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f]
               *   Connected: '/World/Building/Materials/eletricBox_001/tex_base.outputs:rgb' @ '/World/Building/Materials/eletricBox_001/tex_base'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/eletricBox.001_baseColor.jpg'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float]
               *   Connected: '/World/Building/Materials/eletricBox_001/tex_metallic.outputs:r' @ '/World/Building/Materials/eletricBox_001/tex_metallic'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/eletricBox.001_metallicRoughness_metal.jpg'
           *   'normal' [normal3f]
               *   Connected: '/World/Building/Materials/eletricBox_001/tex_normal.outputs:rgb' @ '/World/Building/Materials/eletricBox_001/tex_normal'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/eletricBox.001_normal.jpg'
           *   'occlusion' [float] = '1'
           *   'roughness' [float]
               *   Connected: '/World/Building/Materials/eletricBox_001/tex_roughness.outputs:r' @ '/World/Building/Materials/eletricBox_001/tex_roughness'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/eletricBox.001_metallicRoughness_rough.jpg'
       *   '/World/Building/Materials/eletricBox_001/tex_base' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/eletricBox.001_baseColor.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
           *   'file' [asset] = '0/eletricBox.001_baseColor.jpg'
           *   'st' [float2]
               *   Connected: '/World/Building/Materials/eletricBox_001/uvset0.outputs:result' @ '/World/Building/Materials/eletricBox_001/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/Building/Materials/eletricBox_001/uvset0' (ID: 'UsdPrimvarReader_float2')
       *   Implementation: 'id'
       *   '/World/Building/Materials/eletricBox_001/tex_metallic' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/eletricBox.001_metallicRoughness_metal.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(0.000, 0.000, 0.000, 1.000)'
           *   'file' [asset] = '0/eletricBox.001_metallicRoughness_metal.jpg'
           *   'st' [float2]
               *   Connected: '/World/Building/Materials/eletricBox_001/uvset0.outputs:result' @ '/World/Building/Materials/eletricBox_001/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/Building/Materials/eletricBox_001/tex_normal' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/eletricBox.001_normal.jpg'
       *   Inputs:
           *   'bias' [float4] = '(-1.000, -1.000, -1.000, -1.000)'
           *   'fallback' [float4] = '(0.000, 0.000, 1.000, 1.000)'
           *   'file' [asset] = '0/eletricBox.001_normal.jpg'
           *   'scale' [float4] = '(2.000, 2.000, 2.000, 2.000)'
           *   'st' [float2]
               *   Connected: '/World/Building/Materials/eletricBox_001/uvset0.outputs:result' @ '/World/Building/Materials/eletricBox_001/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/Building/Materials/eletricBox_001/tex_roughness' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/eletricBox.001_metallicRoughness_rough.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(1.000, 0.000, 0.000, 1.000)'
           *   'file' [asset] = '0/eletricBox.001_metallicRoughness_rough.jpg'
           *   'st' [float2]
               *   Connected: '/World/Building/Materials/eletricBox_001/uvset0.outputs:result' @ '/World/Building/Materials/eletricBox_001/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'


---


### /World/Building/Materials/air_conditioning_001
*  **Prim路径 (Prim Path):**/World/Building/Materials/air_conditioning_001
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/Building/Materials/air_conditioning_001/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/Building/Materials/air_conditioning_001/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f]
               *   Connected: '/World/Building/Materials/air_conditioning_001/tex_base.outputs:rgb' @ '/World/Building/Materials/air_conditioning_001/tex_base'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/air_conditioning.001_baseColor.jpg'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float]
               *   Connected: '/World/Building/Materials/air_conditioning_001/tex_metallic.outputs:r' @ '/World/Building/Materials/air_conditioning_001/tex_metallic'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/air_conditioning.001_metallicRoughness_metal_scale0.jpg'
           *   'normal' [normal3f]
               *   Connected: '/World/Building/Materials/air_conditioning_001/tex_normal.outputs:rgb' @ '/World/Building/Materials/air_conditioning_001/tex_normal'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/air_conditioning.001_normal.jpg'
           *   'occlusion' [float] = '1'
           *   'roughness' [float]
               *   Connected: '/World/Building/Materials/air_conditioning_001/tex_roughness.outputs:r' @ '/World/Building/Materials/air_conditioning_001/tex_roughness'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/air_conditioning.001_metallicRoughness_rough.jpg'
       *   '/World/Building/Materials/air_conditioning_001/tex_base' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/air_conditioning.001_baseColor.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
           *   'file' [asset] = '0/air_conditioning.001_baseColor.jpg'
           *   'st' [float2]
               *   Connected: '/World/Building/Materials/air_conditioning_001/uvset0.outputs:result' @ '/World/Building/Materials/air_conditioning_001/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/Building/Materials/air_conditioning_001/uvset0' (ID: 'UsdPrimvarReader_float2')
       *   Implementation: 'id'
       *   '/World/Building/Materials/air_conditioning_001/tex_metallic' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/air_conditioning.001_metallicRoughness_metal_scale0.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(0.000, 0.000, 0.000, 1.000)'
           *   'file' [asset] = '0/air_conditioning.001_metallicRoughness_metal_scale0.jpg'
           *   'st' [float2]
               *   Connected: '/World/Building/Materials/air_conditioning_001/uvset0.outputs:result' @ '/World/Building/Materials/air_conditioning_001/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/Building/Materials/air_conditioning_001/tex_normal' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/air_conditioning.001_normal.jpg'
       *   Inputs:
           *   'bias' [float4] = '(-1.000, -1.000, -1.000, -1.000)'
           *   'fallback' [float4] = '(0.000, 0.000, 1.000, 1.000)'
           *   'file' [asset] = '0/air_conditioning.001_normal.jpg'
           *   'scale' [float4] = '(2.000, 2.000, 2.000, 2.000)'
           *   'st' [float2]
               *   Connected: '/World/Building/Materials/air_conditioning_001/uvset0.outputs:result' @ '/World/Building/Materials/air_conditioning_001/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/Building/Materials/air_conditioning_001/tex_roughness' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/air_conditioning.001_metallicRoughness_rough.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(1.000, 0.000, 0.000, 1.000)'
           *   'file' [asset] = '0/air_conditioning.001_metallicRoughness_rough.jpg'
           *   'st' [float2]
               *   Connected: '/World/Building/Materials/air_conditioning_001/uvset0.outputs:result' @ '/World/Building/Materials/air_conditioning_001/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'


---


### /World/Building/Materials/vents
*  **Prim路径 (Prim Path):**/World/Building/Materials/vents
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/Building/Materials/vents/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/Building/Materials/vents/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f]
               *   Connected: '/World/Building/Materials/vents/tex_base.outputs:rgb' @ '/World/Building/Materials/vents/tex_base'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/vents_baseColor.jpg'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float]
               *   Connected: '/World/Building/Materials/vents/tex_metallic.outputs:r' @ '/World/Building/Materials/vents/tex_metallic'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/vents_metallicRoughness_metal_scale0.jpg'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float]
               *   Connected: '/World/Building/Materials/vents/tex_roughness.outputs:r' @ '/World/Building/Materials/vents/tex_roughness'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/vents_metallicRoughness_rough.jpg'
       *   '/World/Building/Materials/vents/tex_base' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/vents_baseColor.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
           *   'file' [asset] = '0/vents_baseColor.jpg'
           *   'st' [float2]
               *   Connected: '/World/Building/Materials/vents/uvset0.outputs:result' @ '/World/Building/Materials/vents/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/Building/Materials/vents/uvset0' (ID: 'UsdPrimvarReader_float2')
       *   Implementation: 'id'
       *   '/World/Building/Materials/vents/tex_metallic' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/vents_metallicRoughness_metal_scale0.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(0.000, 0.000, 0.000, 1.000)'
           *   'file' [asset] = '0/vents_metallicRoughness_metal_scale0.jpg'
           *   'st' [float2]
               *   Connected: '/World/Building/Materials/vents/uvset0.outputs:result' @ '/World/Building/Materials/vents/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/Building/Materials/vents/tex_roughness' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/vents_metallicRoughness_rough.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(1.000, 0.000, 0.000, 1.000)'
           *   'file' [asset] = '0/vents_metallicRoughness_rough.jpg'
           *   'st' [float2]
               *   Connected: '/World/Building/Materials/vents/uvset0.outputs:result' @ '/World/Building/Materials/vents/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'


---


### /World/Building/Materials/roofingSheets
*  **Prim路径 (Prim Path):**/World/Building/Materials/roofingSheets
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/Building/Materials/roofingSheets/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/Building/Materials/roofingSheets/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f]
               *   Connected: '/World/Building/Materials/roofingSheets/tex_base.outputs:rgb' @ '/World/Building/Materials/roofingSheets/tex_base'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/roofingSheets_baseColor.jpg'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float]
               *   Connected: '/World/Building/Materials/roofingSheets/tex_metallic.outputs:r' @ '/World/Building/Materials/roofingSheets/tex_metallic'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/roofingSheets_metallicRoughness_metal_scale0.jpg'
           *   'normal' [normal3f]
               *   Connected: '/World/Building/Materials/roofingSheets/tex_normal.outputs:rgb' @ '/World/Building/Materials/roofingSheets/tex_normal'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/roofingSheets_normal.jpg'
           *   'occlusion' [float] = '1'
           *   'roughness' [float]
               *   Connected: '/World/Building/Materials/roofingSheets/tex_roughness.outputs:r' @ '/World/Building/Materials/roofingSheets/tex_roughness'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/roofingSheets_metallicRoughness_rough_scale1.jpg'
       *   '/World/Building/Materials/roofingSheets/tex_base' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/roofingSheets_baseColor.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
           *   'file' [asset] = '0/roofingSheets_baseColor.jpg'
           *   'st' [float2]
               *   Connected: '/World/Building/Materials/roofingSheets/uvset0.outputs:result' @ '/World/Building/Materials/roofingSheets/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/Building/Materials/roofingSheets/uvset0' (ID: 'UsdPrimvarReader_float2')
       *   Implementation: 'id'
       *   '/World/Building/Materials/roofingSheets/tex_metallic' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/roofingSheets_metallicRoughness_metal_scale0.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(0.000, 0.000, 0.000, 1.000)'
           *   'file' [asset] = '0/roofingSheets_metallicRoughness_metal_scale0.jpg'
           *   'st' [float2]
               *   Connected: '/World/Building/Materials/roofingSheets/uvset0.outputs:result' @ '/World/Building/Materials/roofingSheets/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/Building/Materials/roofingSheets/tex_normal' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/roofingSheets_normal.jpg'
       *   Inputs:
           *   'bias' [float4] = '(-1.000, -1.000, -1.000, -1.000)'
           *   'fallback' [float4] = '(0.000, 0.000, 1.000, 1.000)'
           *   'file' [asset] = '0/roofingSheets_normal.jpg'
           *   'scale' [float4] = '(2.000, 2.000, 2.000, 2.000)'
           *   'st' [float2]
               *   Connected: '/World/Building/Materials/roofingSheets/uvset0.outputs:result' @ '/World/Building/Materials/roofingSheets/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/Building/Materials/roofingSheets/tex_roughness' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/roofingSheets_metallicRoughness_rough_scale1.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(1.000, 0.000, 0.000, 1.000)'
           *   'file' [asset] = '0/roofingSheets_metallicRoughness_rough_scale1.jpg'
           *   'st' [float2]
               *   Connected: '/World/Building/Materials/roofingSheets/uvset0.outputs:result' @ '/World/Building/Materials/roofingSheets/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'


---


### /World/Building/Materials/emptyBillboard
*  **Prim路径 (Prim Path):**/World/Building/Materials/emptyBillboard
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/Building/Materials/emptyBillboard/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/Building/Materials/emptyBillboard/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f]
               *   Connected: '/World/Building/Materials/emptyBillboard/tex_base.outputs:rgb' @ '/World/Building/Materials/emptyBillboard/tex_base'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/emptyBillboard_baseColor.jpg'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0.821115'
       *   '/World/Building/Materials/emptyBillboard/tex_base' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/emptyBillboard_baseColor.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
           *   'file' [asset] = '0/emptyBillboard_baseColor.jpg'
           *   'st' [float2]
               *   Connected: '/World/Building/Materials/emptyBillboard/uvset0.outputs:result' @ '/World/Building/Materials/emptyBillboard/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/Building/Materials/emptyBillboard/uvset0' (ID: 'UsdPrimvarReader_float2')
       *   Implementation: 'id'


---


### /World/Robotic_Manipulator_low_poly/Materials/Robot_hand
*  **Prim路径 (Prim Path):**/World/Robotic_Manipulator_low_poly/Materials/Robot_hand
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/Robotic_Manipulator_low_poly/Materials/Robot_hand/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/Robotic_Manipulator_low_poly/Materials/Robot_hand/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f]
               *   Connected: '/World/Robotic_Manipulator_low_poly/Materials/Robot_hand/tex_base.outputs:rgb' @ '/World/Robotic_Manipulator_low_poly/Materials/Robot_hand/tex_base'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/Robot_hand_baseColor.jpg'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float]
               *   Connected: '/World/Robotic_Manipulator_low_poly/Materials/Robot_hand/tex_metallic.outputs:r' @ '/World/Robotic_Manipulator_low_poly/Materials/Robot_hand/tex_metallic'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/Robot_hand_metallicRoughness_metal.jpg'
           *   'normal' [normal3f]
               *   Connected: '/World/Robotic_Manipulator_low_poly/Materials/Robot_hand/tex_normal.outputs:rgb' @ '/World/Robotic_Manipulator_low_poly/Materials/Robot_hand/tex_normal'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/Robot_hand_normal.jpg'
           *   'occlusion' [float]
               *   Connected: '/World/Robotic_Manipulator_low_poly/Materials/Robot_hand/tex_occlusion.outputs:r' @ '/World/Robotic_Manipulator_low_poly/Materials/Robot_hand/tex_occlusion'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/Robot_hand_metallicRoughness_occl.jpg'
           *   'roughness' [float]
               *   Connected: '/World/Robotic_Manipulator_low_poly/Materials/Robot_hand/tex_roughness.outputs:r' @ '/World/Robotic_Manipulator_low_poly/Materials/Robot_hand/tex_roughness'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/Robot_hand_metallicRoughness_rough.jpg'
       *   '/World/Robotic_Manipulator_low_poly/Materials/Robot_hand/tex_base' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/Robot_hand_baseColor.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
           *   'file' [asset] = '0/Robot_hand_baseColor.jpg'
           *   'st' [float2]
               *   Connected: '/World/Robotic_Manipulator_low_poly/Materials/Robot_hand/uvset0.outputs:result' @ '/World/Robotic_Manipulator_low_poly/Materials/Robot_hand/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/Robotic_Manipulator_low_poly/Materials/Robot_hand/uvset0' (ID: 'UsdPrimvarReader_float2')
       *   Implementation: 'id'
       *   '/World/Robotic_Manipulator_low_poly/Materials/Robot_hand/tex_metallic' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/Robot_hand_metallicRoughness_metal.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(0.000, 0.000, 0.000, 1.000)'
           *   'file' [asset] = '0/Robot_hand_metallicRoughness_metal.jpg'
           *   'st' [float2]
               *   Connected: '/World/Robotic_Manipulator_low_poly/Materials/Robot_hand/uvset0.outputs:result' @ '/World/Robotic_Manipulator_low_poly/Materials/Robot_hand/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/Robotic_Manipulator_low_poly/Materials/Robot_hand/tex_normal' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/Robot_hand_normal.jpg'
       *   Inputs:
           *   'bias' [float4] = '(-1.000, -1.000, -1.000, -1.000)'
           *   'fallback' [float4] = '(0.000, 0.000, 1.000, 1.000)'
           *   'file' [asset] = '0/Robot_hand_normal.jpg'
           *   'scale' [float4] = '(2.000, 2.000, 2.000, 2.000)'
           *   'st' [float2]
               *   Connected: '/World/Robotic_Manipulator_low_poly/Materials/Robot_hand/uvset0.outputs:result' @ '/World/Robotic_Manipulator_low_poly/Materials/Robot_hand/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/Robotic_Manipulator_low_poly/Materials/Robot_hand/tex_occlusion' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/Robot_hand_metallicRoughness_occl.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(1.000, 0.000, 0.000, 1.000)'
           *   'file' [asset] = '0/Robot_hand_metallicRoughness_occl.jpg'
           *   'st' [float2]
               *   Connected: '/World/Robotic_Manipulator_low_poly/Materials/Robot_hand/uvset0.outputs:result' @ '/World/Robotic_Manipulator_low_poly/Materials/Robot_hand/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/Robotic_Manipulator_low_poly/Materials/Robot_hand/tex_roughness' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/Robot_hand_metallicRoughness_rough.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(1.000, 0.000, 0.000, 1.000)'
           *   'file' [asset] = '0/Robot_hand_metallicRoughness_rough.jpg'
           *   'st' [float2]
               *   Connected: '/World/Robotic_Manipulator_low_poly/Materials/Robot_hand/uvset0.outputs:result' @ '/World/Robotic_Manipulator_low_poly/Materials/Robot_hand/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'


---


### /World/Robotic_Manipulator_low_poly/Materials/Stand
*  **Prim路径 (Prim Path):**/World/Robotic_Manipulator_low_poly/Materials/Stand
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/Robotic_Manipulator_low_poly/Materials/Stand/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/Robotic_Manipulator_low_poly/Materials/Stand/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f]
               *   Connected: '/World/Robotic_Manipulator_low_poly/Materials/Stand/tex_base.outputs:rgb' @ '/World/Robotic_Manipulator_low_poly/Materials/Stand/tex_base'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/Stand_baseColor.jpg'
           *   'emissiveColor' [color3f]
               *   Connected: '/World/Robotic_Manipulator_low_poly/Materials/Stand/tex_emissive.outputs:rgb' @ '/World/Robotic_Manipulator_low_poly/Materials/Stand/tex_emissive'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/Stand_emissive.jpg'
           *   'metallic' [float]
               *   Connected: '/World/Robotic_Manipulator_low_poly/Materials/Stand/tex_metallic.outputs:r' @ '/World/Robotic_Manipulator_low_poly/Materials/Stand/tex_metallic'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/Stand_metallicRoughness_metal.jpg'
           *   'normal' [normal3f]
               *   Connected: '/World/Robotic_Manipulator_low_poly/Materials/Stand/tex_normal.outputs:rgb' @ '/World/Robotic_Manipulator_low_poly/Materials/Stand/tex_normal'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/Stand_normal.jpg'
           *   'occlusion' [float]
               *   Connected: '/World/Robotic_Manipulator_low_poly/Materials/Stand/tex_occlusion.outputs:r' @ '/World/Robotic_Manipulator_low_poly/Materials/Stand/tex_occlusion'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/Stand_metallicRoughness_occl.jpg'
           *   'roughness' [float]
               *   Connected: '/World/Robotic_Manipulator_low_poly/Materials/Stand/tex_roughness.outputs:r' @ '/World/Robotic_Manipulator_low_poly/Materials/Stand/tex_roughness'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/Stand_metallicRoughness_rough.jpg'
       *   '/World/Robotic_Manipulator_low_poly/Materials/Stand/tex_base' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/Stand_baseColor.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
           *   'file' [asset] = '0/Stand_baseColor.jpg'
           *   'st' [float2]
               *   Connected: '/World/Robotic_Manipulator_low_poly/Materials/Stand/uvset0.outputs:result' @ '/World/Robotic_Manipulator_low_poly/Materials/Stand/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/Robotic_Manipulator_low_poly/Materials/Stand/uvset0' (ID: 'UsdPrimvarReader_float2')
       *   Implementation: 'id'
       *   '/World/Robotic_Manipulator_low_poly/Materials/Stand/tex_emissive' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/Stand_emissive.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(0.000, 0.000, 0.000, 1.000)'
           *   'file' [asset] = '0/Stand_emissive.jpg'
           *   'st' [float2]
               *   Connected: '/World/Robotic_Manipulator_low_poly/Materials/Stand/uvset0.outputs:result' @ '/World/Robotic_Manipulator_low_poly/Materials/Stand/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/Robotic_Manipulator_low_poly/Materials/Stand/tex_metallic' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/Stand_metallicRoughness_metal.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(0.000, 0.000, 0.000, 1.000)'
           *   'file' [asset] = '0/Stand_metallicRoughness_metal.jpg'
           *   'st' [float2]
               *   Connected: '/World/Robotic_Manipulator_low_poly/Materials/Stand/uvset0.outputs:result' @ '/World/Robotic_Manipulator_low_poly/Materials/Stand/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/Robotic_Manipulator_low_poly/Materials/Stand/tex_normal' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/Stand_normal.jpg'
       *   Inputs:
           *   'bias' [float4] = '(-1.000, -1.000, -1.000, -1.000)'
           *   'fallback' [float4] = '(0.000, 0.000, 1.000, 1.000)'
           *   'file' [asset] = '0/Stand_normal.jpg'
           *   'scale' [float4] = '(2.000, 2.000, 2.000, 2.000)'
           *   'st' [float2]
               *   Connected: '/World/Robotic_Manipulator_low_poly/Materials/Stand/uvset0.outputs:result' @ '/World/Robotic_Manipulator_low_poly/Materials/Stand/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/Robotic_Manipulator_low_poly/Materials/Stand/tex_occlusion' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/Stand_metallicRoughness_occl.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(1.000, 0.000, 0.000, 1.000)'
           *   'file' [asset] = '0/Stand_metallicRoughness_occl.jpg'
           *   'st' [float2]
               *   Connected: '/World/Robotic_Manipulator_low_poly/Materials/Stand/uvset0.outputs:result' @ '/World/Robotic_Manipulator_low_poly/Materials/Stand/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/Robotic_Manipulator_low_poly/Materials/Stand/tex_roughness' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/Stand_metallicRoughness_rough.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(1.000, 0.000, 0.000, 1.000)'
           *   'file' [asset] = '0/Stand_metallicRoughness_rough.jpg'
           *   'st' [float2]
               *   Connected: '/World/Robotic_Manipulator_low_poly/Materials/Stand/uvset0.outputs:result' @ '/World/Robotic_Manipulator_low_poly/Materials/Stand/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'


---


### /World/Simple_rubber_conveyor/Materials/Conveyor
*  **Prim路径 (Prim Path):**/World/Simple_rubber_conveyor/Materials/Conveyor
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/Simple_rubber_conveyor/Materials/Conveyor/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/Simple_rubber_conveyor/Materials/Conveyor/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f]
               *   Connected: '/World/Simple_rubber_conveyor/Materials/Conveyor/tex_base.outputs:rgb' @ '/World/Simple_rubber_conveyor/Materials/Conveyor/tex_base'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/Conveyor_diffuse.jpg'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'glossiness' [float]
               *   Connected: '/World/Simple_rubber_conveyor/Materials/Conveyor/tex_glossiness.outputs:r' @ '/World/Simple_rubber_conveyor/Materials/Conveyor/tex_glossiness'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/Conveyor_specularGlossiness_gloss_scale0.jpg'
           *   'normal' [normal3f]
               *   Connected: '/World/Simple_rubber_conveyor/Materials/Conveyor/tex_normal.outputs:rgb' @ '/World/Simple_rubber_conveyor/Materials/Conveyor/tex_normal'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/Conveyor_normal.jpg'
           *   'occlusion' [float]
               *   Connected: '/World/Simple_rubber_conveyor/Materials/Conveyor/tex_occlusion.outputs:r' @ '/World/Simple_rubber_conveyor/Materials/Conveyor/tex_occlusion'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/Conveyor_occlusion_occl.jpg'
           *   'specularColor' [float3]
               *   Connected: '/World/Simple_rubber_conveyor/Materials/Conveyor/tex_specular.outputs:rgb' @ '/World/Simple_rubber_conveyor/Materials/Conveyor/tex_specular'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/Conveyor_specularGlossiness_spec.jpg'
       *   '/World/Simple_rubber_conveyor/Materials/Conveyor/tex_base' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/Conveyor_diffuse.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
           *   'file' [asset] = '0/Conveyor_diffuse.jpg'
           *   'st' [float2]
               *   Connected: '/World/Simple_rubber_conveyor/Materials/Conveyor/uvset0.outputs:result' @ '/World/Simple_rubber_conveyor/Materials/Conveyor/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/Simple_rubber_conveyor/Materials/Conveyor/uvset0' (ID: 'UsdPrimvarReader_float2')
       *   Implementation: 'id'
       *   '/World/Simple_rubber_conveyor/Materials/Conveyor/tex_glossiness' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/Conveyor_specularGlossiness_gloss_scale0.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(1.000, 0.000, 0.000, 1.000)'
           *   'file' [asset] = '0/Conveyor_specularGlossiness_gloss_scale0.jpg'
           *   'st' [float2]
               *   Connected: '/World/Simple_rubber_conveyor/Materials/Conveyor/uvset0.outputs:result' @ '/World/Simple_rubber_conveyor/Materials/Conveyor/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/Simple_rubber_conveyor/Materials/Conveyor/tex_normal' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/Conveyor_normal.jpg'
       *   Inputs:
           *   'bias' [float4] = '(-1.000, -1.000, -1.000, -1.000)'
           *   'fallback' [float4] = '(0.000, 0.000, 1.000, 1.000)'
           *   'file' [asset] = '0/Conveyor_normal.jpg'
           *   'scale' [float4] = '(2.000, 2.000, 2.000, 2.000)'
           *   'st' [float2]
               *   Connected: '/World/Simple_rubber_conveyor/Materials/Conveyor/uvset0.outputs:result' @ '/World/Simple_rubber_conveyor/Materials/Conveyor/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/Simple_rubber_conveyor/Materials/Conveyor/tex_occlusion' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/Conveyor_occlusion_occl.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(1.000, 0.000, 0.000, 1.000)'
           *   'file' [asset] = '0/Conveyor_occlusion_occl.jpg'
           *   'st' [float2]
               *   Connected: '/World/Simple_rubber_conveyor/Materials/Conveyor/uvset0.outputs:result' @ '/World/Simple_rubber_conveyor/Materials/Conveyor/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/Simple_rubber_conveyor/Materials/Conveyor/tex_specular' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/Conveyor_specularGlossiness_spec.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
           *   'file' [asset] = '0/Conveyor_specularGlossiness_spec.jpg'
           *   'st' [float2]
               *   Connected: '/World/Simple_rubber_conveyor/Materials/Conveyor/uvset0.outputs:result' @ '/World/Simple_rubber_conveyor/Materials/Conveyor/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'


---


### /World/Simple_rubber_conveyor/Materials/Belt
*  **Prim路径 (Prim Path):**/World/Simple_rubber_conveyor/Materials/Belt
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/Simple_rubber_conveyor/Materials/Belt/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/Simple_rubber_conveyor/Materials/Belt/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f]
               *   Connected: '/World/Simple_rubber_conveyor/Materials/Belt/tex_base.outputs:rgb' @ '/World/Simple_rubber_conveyor/Materials/Belt/tex_base'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/Belt_diffuse.jpg'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'glossiness' [float] = '0.060939'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'specularColor' [float3] = '(0.050, 0.050, 0.050)'
       *   '/World/Simple_rubber_conveyor/Materials/Belt/tex_base' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/Belt_diffuse.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
           *   'file' [asset] = '0/Belt_diffuse.jpg'
           *   'st' [float2]
               *   Connected: '/World/Simple_rubber_conveyor/Materials/Belt/uvset0.outputs:result' @ '/World/Simple_rubber_conveyor/Materials/Belt/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/Simple_rubber_conveyor/Materials/Belt/uvset0' (ID: 'UsdPrimvarReader_float2')
       *   Implementation: 'id'


---


### /World/AGV_ready_1/Materials/ASELSAN_CATS_04
*  **Prim路径 (Prim Path):**/World/AGV_ready_1/Materials/ASELSAN_CATS_04
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_1/Materials/ASELSAN_CATS_04/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_1/Materials/ASELSAN_CATS_04/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.158, 0.158, 0.158)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_1/Materials/ASELSAN_CATS_04_2
*  **Prim路径 (Prim Path):**/World/AGV_ready_1/Materials/ASELSAN_CATS_04_2
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_1/Materials/ASELSAN_CATS_04_2/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_1/Materials/ASELSAN_CATS_04_2/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.769, 0.773, 0.749)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_1/Materials/ASELSAN_CATS_13
*  **Prim路径 (Prim Path):**/World/AGV_ready_1/Materials/ASELSAN_CATS_13
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_1/Materials/ASELSAN_CATS_13/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_1/Materials/ASELSAN_CATS_13/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.706, 0.718, 0.729)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_1/Materials/Color_000
*  **Prim路径 (Prim Path):**/World/AGV_ready_1/Materials/Color_000
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_1/Materials/Color_000/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_1/Materials/Color_000/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(1.000, 1.000, 1.000)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_1/Materials/Color_A05
*  **Prim路径 (Prim Path):**/World/AGV_ready_1/Materials/Color_A05
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_1/Materials/Color_A05/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_1/Materials/Color_A05/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(1.000, 0.000, 0.000)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0.959234'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0'


---


### /World/AGV_ready_1/Materials/Color_A06
*  **Prim路径 (Prim Path):**/World/AGV_ready_1/Materials/Color_A06
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_1/Materials/Color_A06/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_1/Materials/Color_A06/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.800, 0.000, 0.000)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_1/Materials/Color_B05
*  **Prim路径 (Prim Path):**/World/AGV_ready_1/Materials/Color_B05
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_1/Materials/Color_B05/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_1/Materials/Color_B05/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(1.000, 0.247, 0.000)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '1'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0'


---


### /World/AGV_ready_1/Materials/Color_E02
*  **Prim路径 (Prim Path):**/World/AGV_ready_1/Materials/Color_E02
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_1/Materials/Color_E02/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_1/Materials/Color_E02/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(1.000, 1.000, 0.196)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_1/Materials/Color_E05
*  **Prim路径 (Prim Path):**/World/AGV_ready_1/Materials/Color_E05
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_1/Materials/Color_E05/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_1/Materials/Color_E05/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(1.000, 0.910, 0.000)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0.625455'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0.133891'


---


### /World/AGV_ready_1/Materials/Color_F06
*  **Prim路径 (Prim Path):**/World/AGV_ready_1/Materials/Color_F06
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_1/Materials/Color_F06/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_1/Materials/Color_F06/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.400, 0.800, 0.000)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_1/Materials/Color_G03
*  **Prim路径 (Prim Path):**/World/AGV_ready_1/Materials/Color_G03
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_1/Materials/Color_G03/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_1/Materials/Color_G03/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.396, 1.000, 0.396)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_1/Materials/Color_M02
*  **Prim路径 (Prim Path):**/World/AGV_ready_1/Materials/Color_M02
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_1/Materials/Color_M02/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_1/Materials/Color_M02/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.776, 0.776, 0.776)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_1/Materials/Color_M03
*  **Prim路径 (Prim Path):**/World/AGV_ready_1/Materials/Color_M03
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_1/Materials/Color_M03/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_1/Materials/Color_M03/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.667, 0.667, 0.667)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_1/Materials/Mtl39
*  **Prim路径 (Prim Path):**/World/AGV_ready_1/Materials/Mtl39
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_1/Materials/Mtl39/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_1/Materials/Mtl39/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.494, 0.494, 0.494)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_1/Materials/Mtl6
*  **Prim路径 (Prim Path):**/World/AGV_ready_1/Materials/Mtl6
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_1/Materials/Mtl6/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_1/Materials/Mtl6/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f]
               *   Connected: '/World/AGV_ready_1/Materials/Mtl6/tex_base.outputs:rgb' @ '/World/AGV_ready_1/Materials/Mtl6/tex_base'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/Mtl6_baseColor.jpg'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'
       *   '/World/AGV_ready_1/Materials/Mtl6/tex_base' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/Mtl6_baseColor.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
           *   'file' [asset] = '0/Mtl6_baseColor.jpg'
           *   'st' [float2]
               *   Connected: '/World/AGV_ready_1/Materials/Mtl6/uvset0.outputs:result' @ '/World/AGV_ready_1/Materials/Mtl6/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/AGV_ready_1/Materials/Mtl6/uvset0' (ID: 'UsdPrimvarReader_float2')
       *   Implementation: 'id'


---


### /World/AGV_ready_1/Materials/Mtl9
*  **Prim路径 (Prim Path):**/World/AGV_ready_1/Materials/Mtl9
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_1/Materials/Mtl9/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_1/Materials/Mtl9/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.514, 1.000, 0.000)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_1/Materials/Silver
*  **Prim路径 (Prim Path):**/World/AGV_ready_1/Materials/Silver
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_1/Materials/Silver/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_1/Materials/Silver/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.753, 0.753, 0.753)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_1/Materials/material
*  **Prim路径 (Prim Path):**/World/AGV_ready_1/Materials/material
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_1/Materials/material/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_1/Materials/material/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f]
               *   Connected: '/World/AGV_ready_1/Materials/material/tex_base.outputs:rgb' @ '/World/AGV_ready_1/Materials/material/tex_base'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/material_baseColor.jpg'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'
       *   '/World/AGV_ready_1/Materials/material/tex_base' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/material_baseColor.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
           *   'file' [asset] = '0/material_baseColor.jpg'
           *   'st' [float2]
               *   Connected: '/World/AGV_ready_1/Materials/material/uvset0.outputs:result' @ '/World/AGV_ready_1/Materials/material/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/AGV_ready_1/Materials/material/uvset0' (ID: 'UsdPrimvarReader_float2')
       *   Implementation: 'id'


---


### /World/AGV_ready_1/Materials/cash_register_keys
*  **Prim路径 (Prim Path):**/World/AGV_ready_1/Materials/cash_register_keys
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_1/Materials/cash_register_keys/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_1/Materials/cash_register_keys/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.976, 0.992, 0.973)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_1/Materials/Chris_Shoe_Sole
*  **Prim路径 (Prim Path):**/World/AGV_ready_1/Materials/Chris_Shoe_Sole
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_1/Materials/Chris_Shoe_Sole/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_1/Materials/Chris_Shoe_Sole/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.155, 0.149, 0.149)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'opacity' [float] = '0.25'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_1/Materials/Color_002
*  **Prim路径 (Prim Path):**/World/AGV_ready_1/Materials/Color_002
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_1/Materials/Color_002/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_1/Materials/Color_002/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.217, 0.217, 0.217)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0.570837'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0'


---


### /World/AGV_ready_1/Materials/Color_005
*  **Prim路径 (Prim Path):**/World/AGV_ready_1/Materials/Color_005
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_1/Materials/Color_005/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_1/Materials/Color_005/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.130, 0.130, 0.130)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0.710417'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0'


---


### /World/AGV_ready_1/Materials/Color_006
*  **Prim路径 (Prim Path):**/World/AGV_ready_1/Materials/Color_006
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_1/Materials/Color_006/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_1/Materials/Color_006/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0.237059'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0'


---


### /World/AGV_ready_1/Materials/Color_008
*  **Prim路径 (Prim Path):**/World/AGV_ready_1/Materials/Color_008
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_1/Materials/Color_008/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_1/Materials/Color_008/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.118, 0.118, 0.118)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0.941027'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0'


---


### /World/AGV_ready_1/Materials/Color_A01
*  **Prim路径 (Prim Path):**/World/AGV_ready_1/Materials/Color_A01
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_1/Materials/Color_A01/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_1/Materials/Color_A01/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(1.000, 0.000, 0.000)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0.965302'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0'


---


### /World/AGV_ready_1/Materials/Color_A11
*  **Prim路径 (Prim Path):**/World/AGV_ready_1/Materials/Color_A11
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_1/Materials/Color_A11/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_1/Materials/Color_A11/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.600, 0.000, 0.000)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_1/Materials/Color_M04
*  **Prim路径 (Prim Path):**/World/AGV_ready_1/Materials/Color_M04
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_1/Materials/Color_M04/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_1/Materials/Color_M04/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.557, 0.557, 0.557)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_1/Materials/Color_M05
*  **Prim路径 (Prim Path):**/World/AGV_ready_1/Materials/Color_M05
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_1/Materials/Color_M05/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_1/Materials/Color_M05/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.447, 0.447, 0.447)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_1/Materials/Color_M06
*  **Prim路径 (Prim Path):**/World/AGV_ready_1/Materials/Color_M06
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_1/Materials/Color_M06/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_1/Materials/Color_M06/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_1/Materials/Color_M07
*  **Prim路径 (Prim Path):**/World/AGV_ready_1/Materials/Color_M07
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_1/Materials/Color_M07/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_1/Materials/Color_M07/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.227, 0.227, 0.227)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_1/Materials/Color_M09
*  **Prim路径 (Prim Path):**/World/AGV_ready_1/Materials/Color_M09
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_1/Materials/Color_M09/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_1/Materials/Color_M09/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0.340226'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0.085341'


---


### /World/AGV_ready_1/Materials/FCP_Charcoal_v2
*  **Prim路径 (Prim Path):**/World/AGV_ready_1/Materials/FCP_Charcoal_v2
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_1/Materials/FCP_Charcoal_v2/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_1/Materials/FCP_Charcoal_v2/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.216, 0.216, 0.216)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_1/Materials/FrontColor
*  **Prim路径 (Prim Path):**/World/AGV_ready_1/Materials/FrontColor
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_1/Materials/FrontColor/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_1/Materials/FrontColor/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.504, 0.504, 0.504)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0.637593'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0.218852'


---


### /World/AGV_ready_1/Materials/Light_Blue
*  **Prim路径 (Prim Path):**/World/AGV_ready_1/Materials/Light_Blue
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_1/Materials/Light_Blue/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_1/Materials/Light_Blue/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.601, 0.601, 0.601)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '1'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0.170303'


---


### /World/AGV_ready_1/Materials/M_0011_Seashell
*  **Prim路径 (Prim Path):**/World/AGV_ready_1/Materials/M_0011_Seashell
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_1/Materials/M_0011_Seashell/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_1/Materials/M_0011_Seashell/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(1.000, 0.961, 0.933)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_1/Materials/M_0131_Silver
*  **Prim路径 (Prim Path):**/World/AGV_ready_1/Materials/M_0131_Silver
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_1/Materials/M_0131_Silver/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_1/Materials/M_0131_Silver/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.242, 0.242, 0.242)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0.613318'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0'


---


### /World/AGV_ready_1/Materials/M_0134_DimGray
*  **Prim路径 (Prim Path):**/World/AGV_ready_1/Materials/M_0134_DimGray
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_1/Materials/M_0134_DimGray/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_1/Materials/M_0134_DimGray/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.412, 0.412, 0.412)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_1/Materials/M_0135_DarkGray
*  **Prim路径 (Prim Path):**/World/AGV_ready_1/Materials/M_0135_DarkGray
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_1/Materials/M_0135_DarkGray/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_1/Materials/M_0135_DarkGray/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.318, 0.318, 0.318)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_1/Materials/Metal_Silver
*  **Prim路径 (Prim Path):**/World/AGV_ready_1/Materials/Metal_Silver
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_1/Materials/Metal_Silver/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_1/Materials/Metal_Silver/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.918, 0.914, 0.933)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_1/Materials/Mtl1
*  **Prim路径 (Prim Path):**/World/AGV_ready_1/Materials/Mtl1
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_1/Materials/Mtl1/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_1/Materials/Mtl1/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.015, 0.015, 0.015)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0.255265'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_1/Materials/Mtl10
*  **Prim路径 (Prim Path):**/World/AGV_ready_1/Materials/Mtl10
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_1/Materials/Mtl10/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_1/Materials/Mtl10/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.322, 0.322, 0.322)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_1/Materials/Mtl11
*  **Prim路径 (Prim Path):**/World/AGV_ready_1/Materials/Mtl11
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_1/Materials/Mtl11/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_1/Materials/Mtl11/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.067, 0.757, 0.329)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_1/Materials/Mtl12
*  **Prim路径 (Prim Path):**/World/AGV_ready_1/Materials/Mtl12
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_1/Materials/Mtl12/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_1/Materials/Mtl12/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.502, 0.502, 0.502)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_1/Materials/Mtl13
*  **Prim路径 (Prim Path):**/World/AGV_ready_1/Materials/Mtl13
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_1/Materials/Mtl13/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_1/Materials/Mtl13/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.008, 0.514, 0.816)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_1/Materials/Mtl14
*  **Prim路径 (Prim Path):**/World/AGV_ready_1/Materials/Mtl14
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_1/Materials/Mtl14/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_1/Materials/Mtl14/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.310, 0.310, 0.310)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_1/Materials/Mtl15
*  **Prim路径 (Prim Path):**/World/AGV_ready_1/Materials/Mtl15
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_1/Materials/Mtl15/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_1/Materials/Mtl15/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.263, 0.275, 0.275)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_1/Materials/Mtl16
*  **Prim路径 (Prim Path):**/World/AGV_ready_1/Materials/Mtl16
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_1/Materials/Mtl16/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_1/Materials/Mtl16/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.698, 0.698, 0.000)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_1/Materials/Mtl17
*  **Prim路径 (Prim Path):**/World/AGV_ready_1/Materials/Mtl17
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_1/Materials/Mtl17/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_1/Materials/Mtl17/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.000, 0.863, 1.000)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_1/Materials/Mtl3
*  **Prim路径 (Prim Path):**/World/AGV_ready_1/Materials/Mtl3
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_1/Materials/Mtl3/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_1/Materials/Mtl3/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.431, 0.455, 0.498)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_1/Materials/Mtl35
*  **Prim路径 (Prim Path):**/World/AGV_ready_1/Materials/Mtl35
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_1/Materials/Mtl35/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_1/Materials/Mtl35/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.792, 0.820, 0.933)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_1/Materials/Mtl36
*  **Prim路径 (Prim Path):**/World/AGV_ready_1/Materials/Mtl36
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_1/Materials/Mtl36/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_1/Materials/Mtl36/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.667, 0.698, 0.765)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_1/Materials/Mtl37
*  **Prim路径 (Prim Path):**/World/AGV_ready_1/Materials/Mtl37
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_1/Materials/Mtl37/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_1/Materials/Mtl37/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.098, 0.098, 0.098)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_1/Materials/Mtl3a
*  **Prim路径 (Prim Path):**/World/AGV_ready_1/Materials/Mtl3a
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_1/Materials/Mtl3a/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_1/Materials/Mtl3a/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.388, 0.369, 0.322)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_1/Materials/Mtl3b
*  **Prim路径 (Prim Path):**/World/AGV_ready_1/Materials/Mtl3b
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_1/Materials/Mtl3b/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_1/Materials/Mtl3b/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.365, 0.176, 0.012)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0.959234'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'opacity' [float] = '0.273471'
           *   'roughness' [float] = '0.164234'


---


### /World/AGV_ready_1/Materials/Mtl5
*  **Prim路径 (Prim Path):**/World/AGV_ready_1/Materials/Mtl5
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_1/Materials/Mtl5/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_1/Materials/Mtl5/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.396, 0.408, 0.467)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_1/Materials/Mtl7
*  **Prim路径 (Prim Path):**/World/AGV_ready_1/Materials/Mtl7
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_1/Materials/Mtl7/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_1/Materials/Mtl7/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.376, 0.376, 0.376)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_1/Materials/Mtl8
*  **Prim路径 (Prim Path):**/World/AGV_ready_1/Materials/Mtl8
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_1/Materials/Mtl8/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_1/Materials/Mtl8/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.173, 0.173, 0.173)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_1/Materials/Mtla
*  **Prim路径 (Prim Path):**/World/AGV_ready_1/Materials/Mtla
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_1/Materials/Mtla/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_1/Materials/Mtla/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.612, 0.725, 0.745)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_1/Materials/Mtlb1
*  **Prim路径 (Prim Path):**/World/AGV_ready_1/Materials/Mtlb1
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_1/Materials/Mtlb1/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_1/Materials/Mtlb1/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.949, 0.925, 0.933)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_1/Materials/Stainless_Steel
*  **Prim路径 (Prim Path):**/World/AGV_ready_1/Materials/Stainless_Steel
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_1/Materials/Stainless_Steel/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_1/Materials/Stainless_Steel/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.292, 0.294, 0.284)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0.431257'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_1/Materials/Metal_Aluminum_Anodized_1
*  **Prim路径 (Prim Path):**/World/AGV_ready_1/Materials/Metal_Aluminum_Anodized_1
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_1/Materials/Metal_Aluminum_Anodized_1/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_1/Materials/Metal_Aluminum_Anodized_1/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.260, 0.269, 0.282)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0.309883'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0'


---


### /World/AGV_ready_1/Materials/Metal_Aluminum_Anodized_2
*  **Prim路径 (Prim Path):**/World/AGV_ready_1/Materials/Metal_Aluminum_Anodized_2
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_1/Materials/Metal_Aluminum_Anodized_2/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_1/Materials/Metal_Aluminum_Anodized_2/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.792, 0.820, 0.859)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_1/Materials/basic_gray_plastic
*  **Prim路径 (Prim Path):**/World/AGV_ready_1/Materials/basic_gray_plastic
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_1/Materials/basic_gray_plastic/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_1/Materials/basic_gray_plastic/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0.297745'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0.115685'


---


### /World/AGV_ready_1/Materials/texture
*  **Prim路径 (Prim Path):**/World/AGV_ready_1/Materials/texture
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_1/Materials/texture/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_1/Materials/texture/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.294, 0.294, 0.294)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/Cardbox_A1/Looks/Cardboard_A
*  **Prim路径 (Prim Path):**/World/Cardbox_A1/Looks/Cardboard_A
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/Cardbox_A1/Looks/Cardboard_A/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/Cardbox_A1/Looks/Cardboard_A/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   纹理引用 (Texture Assets):
           *   './Textures/T_Cardbox_A1_Albedo.png'
           *   './Textures/T_Cardbox_A1_Normal.png'
           *   './Textures/T_Cardbox_A1_ORM.png'
       *   Inputs:
           *   'diffuse_texture' [asset] = './Textures/T_Cardbox_A1_Albedo.png'
           *   'normalmap_texture' [asset] = './Textures/T_Cardbox_A1_Normal.png'
           *   'ORM_texture' [asset] = './Textures/T_Cardbox_A1_ORM.png'
           *   'reflection_roughness_texture_influence' [float] = '1'


---


### /World/Cardbox_A1_01/Looks/Cardboard_A
*  **Prim路径 (Prim Path):**/World/Cardbox_A1_01/Looks/Cardboard_A
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/Cardbox_A1_01/Looks/Cardboard_A/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/Cardbox_A1_01/Looks/Cardboard_A/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   纹理引用 (Texture Assets):
           *   './Textures/T_Cardbox_A1_Albedo.png'
           *   './Textures/T_Cardbox_A1_Normal.png'
           *   './Textures/T_Cardbox_A1_ORM.png'
       *   Inputs:
           *   'diffuse_texture' [asset] = './Textures/T_Cardbox_A1_Albedo.png'
           *   'normalmap_texture' [asset] = './Textures/T_Cardbox_A1_Normal.png'
           *   'ORM_texture' [asset] = './Textures/T_Cardbox_A1_ORM.png'
           *   'reflection_roughness_texture_influence' [float] = '1'


---


### /World/Cardbox_A1_02/Looks/Cardboard_A
*  **Prim路径 (Prim Path):**/World/Cardbox_A1_02/Looks/Cardboard_A
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/Cardbox_A1_02/Looks/Cardboard_A/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/Cardbox_A1_02/Looks/Cardboard_A/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   纹理引用 (Texture Assets):
           *   './Textures/T_Cardbox_A1_Albedo.png'
           *   './Textures/T_Cardbox_A1_Normal.png'
           *   './Textures/T_Cardbox_A1_ORM.png'
       *   Inputs:
           *   'diffuse_texture' [asset] = './Textures/T_Cardbox_A1_Albedo.png'
           *   'normalmap_texture' [asset] = './Textures/T_Cardbox_A1_Normal.png'
           *   'ORM_texture' [asset] = './Textures/T_Cardbox_A1_ORM.png'
           *   'reflection_roughness_texture_influence' [float] = '1'


---


### /World/Cardbox_A1_03/Looks/Cardboard_A
*  **Prim路径 (Prim Path):**/World/Cardbox_A1_03/Looks/Cardboard_A
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/Cardbox_A1_03/Looks/Cardboard_A/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/Cardbox_A1_03/Looks/Cardboard_A/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   纹理引用 (Texture Assets):
           *   './Textures/T_Cardbox_A1_Albedo.png'
           *   './Textures/T_Cardbox_A1_Normal.png'
           *   './Textures/T_Cardbox_A1_ORM.png'
       *   Inputs:
           *   'diffuse_texture' [asset] = './Textures/T_Cardbox_A1_Albedo.png'
           *   'normalmap_texture' [asset] = './Textures/T_Cardbox_A1_Normal.png'
           *   'ORM_texture' [asset] = './Textures/T_Cardbox_A1_ORM.png'
           *   'reflection_roughness_texture_influence' [float] = '1'


---


### /World/Cardbox_A1_04/Looks/Cardboard_A
*  **Prim路径 (Prim Path):**/World/Cardbox_A1_04/Looks/Cardboard_A
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/Cardbox_A1_04/Looks/Cardboard_A/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/Cardbox_A1_04/Looks/Cardboard_A/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   纹理引用 (Texture Assets):
           *   './Textures/T_Cardbox_A1_Albedo.png'
           *   './Textures/T_Cardbox_A1_Normal.png'
           *   './Textures/T_Cardbox_A1_ORM.png'
       *   Inputs:
           *   'diffuse_texture' [asset] = './Textures/T_Cardbox_A1_Albedo.png'
           *   'normalmap_texture' [asset] = './Textures/T_Cardbox_A1_Normal.png'
           *   'ORM_texture' [asset] = './Textures/T_Cardbox_A1_ORM.png'
           *   'reflection_roughness_texture_influence' [float] = '1'


---


### /World/Cardbox_A1_05/Looks/Cardboard_A
*  **Prim路径 (Prim Path):**/World/Cardbox_A1_05/Looks/Cardboard_A
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/Cardbox_A1_05/Looks/Cardboard_A/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/Cardbox_A1_05/Looks/Cardboard_A/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   纹理引用 (Texture Assets):
           *   './Textures/T_Cardbox_A1_Albedo.png'
           *   './Textures/T_Cardbox_A1_Normal.png'
           *   './Textures/T_Cardbox_A1_ORM.png'
       *   Inputs:
           *   'diffuse_texture' [asset] = './Textures/T_Cardbox_A1_Albedo.png'
           *   'normalmap_texture' [asset] = './Textures/T_Cardbox_A1_Normal.png'
           *   'ORM_texture' [asset] = './Textures/T_Cardbox_A1_ORM.png'
           *   'reflection_roughness_texture_influence' [float] = '1'


---


### /World/Cardbox_A1_06/Looks/Cardboard_A
*  **Prim路径 (Prim Path):**/World/Cardbox_A1_06/Looks/Cardboard_A
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/Cardbox_A1_06/Looks/Cardboard_A/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/Cardbox_A1_06/Looks/Cardboard_A/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   纹理引用 (Texture Assets):
           *   './Textures/T_Cardbox_A1_Albedo.png'
           *   './Textures/T_Cardbox_A1_Normal.png'
           *   './Textures/T_Cardbox_A1_ORM.png'
       *   Inputs:
           *   'diffuse_texture' [asset] = './Textures/T_Cardbox_A1_Albedo.png'
           *   'normalmap_texture' [asset] = './Textures/T_Cardbox_A1_Normal.png'
           *   'ORM_texture' [asset] = './Textures/T_Cardbox_A1_ORM.png'
           *   'reflection_roughness_texture_influence' [float] = '1'


---


### /World/Cardbox_A1_07/Looks/Cardboard_A
*  **Prim路径 (Prim Path):**/World/Cardbox_A1_07/Looks/Cardboard_A
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/Cardbox_A1_07/Looks/Cardboard_A/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/Cardbox_A1_07/Looks/Cardboard_A/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   纹理引用 (Texture Assets):
           *   './Textures/T_Cardbox_A1_Albedo.png'
           *   './Textures/T_Cardbox_A1_Normal.png'
           *   './Textures/T_Cardbox_A1_ORM.png'
       *   Inputs:
           *   'diffuse_texture' [asset] = './Textures/T_Cardbox_A1_Albedo.png'
           *   'normalmap_texture' [asset] = './Textures/T_Cardbox_A1_Normal.png'
           *   'ORM_texture' [asset] = './Textures/T_Cardbox_A1_ORM.png'
           *   'reflection_roughness_texture_influence' [float] = '1'


---


### /World/Cardbox_A1_08/Looks/Cardboard_A
*  **Prim路径 (Prim Path):**/World/Cardbox_A1_08/Looks/Cardboard_A
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/Cardbox_A1_08/Looks/Cardboard_A/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/Cardbox_A1_08/Looks/Cardboard_A/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   纹理引用 (Texture Assets):
           *   './Textures/T_Cardbox_A1_Albedo.png'
           *   './Textures/T_Cardbox_A1_Normal.png'
           *   './Textures/T_Cardbox_A1_ORM.png'
       *   Inputs:
           *   'diffuse_texture' [asset] = './Textures/T_Cardbox_A1_Albedo.png'
           *   'normalmap_texture' [asset] = './Textures/T_Cardbox_A1_Normal.png'
           *   'ORM_texture' [asset] = './Textures/T_Cardbox_A1_ORM.png'
           *   'reflection_roughness_texture_influence' [float] = '1'


---


### /World/Cardbox_A1_09/Looks/Cardboard_A
*  **Prim路径 (Prim Path):**/World/Cardbox_A1_09/Looks/Cardboard_A
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/Cardbox_A1_09/Looks/Cardboard_A/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/Cardbox_A1_09/Looks/Cardboard_A/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   纹理引用 (Texture Assets):
           *   './Textures/T_Cardbox_A1_Albedo.png'
           *   './Textures/T_Cardbox_A1_Normal.png'
           *   './Textures/T_Cardbox_A1_ORM.png'
       *   Inputs:
           *   'diffuse_texture' [asset] = './Textures/T_Cardbox_A1_Albedo.png'
           *   'normalmap_texture' [asset] = './Textures/T_Cardbox_A1_Normal.png'
           *   'ORM_texture' [asset] = './Textures/T_Cardbox_A1_ORM.png'
           *   'reflection_roughness_texture_influence' [float] = '1'


---


### /World/Cardbox_A1_10/Looks/Cardboard_A
*  **Prim路径 (Prim Path):**/World/Cardbox_A1_10/Looks/Cardboard_A
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/Cardbox_A1_10/Looks/Cardboard_A/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/Cardbox_A1_10/Looks/Cardboard_A/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   纹理引用 (Texture Assets):
           *   './Textures/T_Cardbox_A1_Albedo.png'
           *   './Textures/T_Cardbox_A1_Normal.png'
           *   './Textures/T_Cardbox_A1_ORM.png'
       *   Inputs:
           *   'diffuse_texture' [asset] = './Textures/T_Cardbox_A1_Albedo.png'
           *   'normalmap_texture' [asset] = './Textures/T_Cardbox_A1_Normal.png'
           *   'ORM_texture' [asset] = './Textures/T_Cardbox_A1_ORM.png'
           *   'reflection_roughness_texture_influence' [float] = '1'


---


### /World/Cardbox_A1_11/Looks/Cardboard_A
*  **Prim路径 (Prim Path):**/World/Cardbox_A1_11/Looks/Cardboard_A
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/Cardbox_A1_11/Looks/Cardboard_A/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/Cardbox_A1_11/Looks/Cardboard_A/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   纹理引用 (Texture Assets):
           *   './Textures/T_Cardbox_A1_Albedo.png'
           *   './Textures/T_Cardbox_A1_Normal.png'
           *   './Textures/T_Cardbox_A1_ORM.png'
       *   Inputs:
           *   'diffuse_texture' [asset] = './Textures/T_Cardbox_A1_Albedo.png'
           *   'normalmap_texture' [asset] = './Textures/T_Cardbox_A1_Normal.png'
           *   'ORM_texture' [asset] = './Textures/T_Cardbox_A1_ORM.png'
           *   'reflection_roughness_texture_influence' [float] = '1'


---


### /World/Cardbox_A1_12/Looks/Cardboard_A
*  **Prim路径 (Prim Path):**/World/Cardbox_A1_12/Looks/Cardboard_A
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/Cardbox_A1_12/Looks/Cardboard_A/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/Cardbox_A1_12/Looks/Cardboard_A/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   纹理引用 (Texture Assets):
           *   './Textures/T_Cardbox_A1_Albedo.png'
           *   './Textures/T_Cardbox_A1_Normal.png'
           *   './Textures/T_Cardbox_A1_ORM.png'
       *   Inputs:
           *   'diffuse_texture' [asset] = './Textures/T_Cardbox_A1_Albedo.png'
           *   'normalmap_texture' [asset] = './Textures/T_Cardbox_A1_Normal.png'
           *   'ORM_texture' [asset] = './Textures/T_Cardbox_A1_ORM.png'
           *   'reflection_roughness_texture_influence' [float] = '1'


---


### /World/Cardbox_A1_13/Looks/Cardboard_A
*  **Prim路径 (Prim Path):**/World/Cardbox_A1_13/Looks/Cardboard_A
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/Cardbox_A1_13/Looks/Cardboard_A/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/Cardbox_A1_13/Looks/Cardboard_A/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   纹理引用 (Texture Assets):
           *   './Textures/T_Cardbox_A1_Albedo.png'
           *   './Textures/T_Cardbox_A1_Normal.png'
           *   './Textures/T_Cardbox_A1_ORM.png'
       *   Inputs:
           *   'diffuse_texture' [asset] = './Textures/T_Cardbox_A1_Albedo.png'
           *   'normalmap_texture' [asset] = './Textures/T_Cardbox_A1_Normal.png'
           *   'ORM_texture' [asset] = './Textures/T_Cardbox_A1_ORM.png'
           *   'reflection_roughness_texture_influence' [float] = '1'


---


### /World/Cardbox_A1_14/Looks/Cardboard_A
*  **Prim路径 (Prim Path):**/World/Cardbox_A1_14/Looks/Cardboard_A
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/Cardbox_A1_14/Looks/Cardboard_A/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/Cardbox_A1_14/Looks/Cardboard_A/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   纹理引用 (Texture Assets):
           *   './Textures/T_Cardbox_A1_Albedo.png'
           *   './Textures/T_Cardbox_A1_Normal.png'
           *   './Textures/T_Cardbox_A1_ORM.png'
       *   Inputs:
           *   'diffuse_texture' [asset] = './Textures/T_Cardbox_A1_Albedo.png'
           *   'normalmap_texture' [asset] = './Textures/T_Cardbox_A1_Normal.png'
           *   'ORM_texture' [asset] = './Textures/T_Cardbox_A1_ORM.png'
           *   'reflection_roughness_texture_influence' [float] = '1'


---


### /World/Cardbox_A1_15/Looks/Cardboard_A
*  **Prim路径 (Prim Path):**/World/Cardbox_A1_15/Looks/Cardboard_A
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/Cardbox_A1_15/Looks/Cardboard_A/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/Cardbox_A1_15/Looks/Cardboard_A/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   纹理引用 (Texture Assets):
           *   './Textures/T_Cardbox_A1_Albedo.png'
           *   './Textures/T_Cardbox_A1_Normal.png'
           *   './Textures/T_Cardbox_A1_ORM.png'
       *   Inputs:
           *   'diffuse_texture' [asset] = './Textures/T_Cardbox_A1_Albedo.png'
           *   'normalmap_texture' [asset] = './Textures/T_Cardbox_A1_Normal.png'
           *   'ORM_texture' [asset] = './Textures/T_Cardbox_A1_ORM.png'
           *   'reflection_roughness_texture_influence' [float] = '1'


---


### /World/Cardbox_A1_16/Looks/Cardboard_A
*  **Prim路径 (Prim Path):**/World/Cardbox_A1_16/Looks/Cardboard_A
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/Cardbox_A1_16/Looks/Cardboard_A/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/Cardbox_A1_16/Looks/Cardboard_A/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   纹理引用 (Texture Assets):
           *   './Textures/T_Cardbox_A1_Albedo.png'
           *   './Textures/T_Cardbox_A1_Normal.png'
           *   './Textures/T_Cardbox_A1_ORM.png'
       *   Inputs:
           *   'diffuse_texture' [asset] = './Textures/T_Cardbox_A1_Albedo.png'
           *   'normalmap_texture' [asset] = './Textures/T_Cardbox_A1_Normal.png'
           *   'ORM_texture' [asset] = './Textures/T_Cardbox_A1_ORM.png'
           *   'reflection_roughness_texture_influence' [float] = '1'


---


### /World/Cardbox_A1_17/Looks/Cardboard_A
*  **Prim路径 (Prim Path):**/World/Cardbox_A1_17/Looks/Cardboard_A
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/Cardbox_A1_17/Looks/Cardboard_A/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/Cardbox_A1_17/Looks/Cardboard_A/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   纹理引用 (Texture Assets):
           *   './Textures/T_Cardbox_A1_Albedo.png'
           *   './Textures/T_Cardbox_A1_Normal.png'
           *   './Textures/T_Cardbox_A1_ORM.png'
       *   Inputs:
           *   'diffuse_texture' [asset] = './Textures/T_Cardbox_A1_Albedo.png'
           *   'normalmap_texture' [asset] = './Textures/T_Cardbox_A1_Normal.png'
           *   'ORM_texture' [asset] = './Textures/T_Cardbox_A1_ORM.png'
           *   'reflection_roughness_texture_influence' [float] = '1'


---


### /World/Cardbox_A1_18/Looks/Cardboard_A
*  **Prim路径 (Prim Path):**/World/Cardbox_A1_18/Looks/Cardboard_A
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/Cardbox_A1_18/Looks/Cardboard_A/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/Cardbox_A1_18/Looks/Cardboard_A/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   纹理引用 (Texture Assets):
           *   './Textures/T_Cardbox_A1_Albedo.png'
           *   './Textures/T_Cardbox_A1_Normal.png'
           *   './Textures/T_Cardbox_A1_ORM.png'
       *   Inputs:
           *   'diffuse_texture' [asset] = './Textures/T_Cardbox_A1_Albedo.png'
           *   'normalmap_texture' [asset] = './Textures/T_Cardbox_A1_Normal.png'
           *   'ORM_texture' [asset] = './Textures/T_Cardbox_A1_ORM.png'
           *   'reflection_roughness_texture_influence' [float] = '1'


---


### /World/Cardbox_A1_19/Looks/Cardboard_A
*  **Prim路径 (Prim Path):**/World/Cardbox_A1_19/Looks/Cardboard_A
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/Cardbox_A1_19/Looks/Cardboard_A/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/Cardbox_A1_19/Looks/Cardboard_A/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   纹理引用 (Texture Assets):
           *   './Textures/T_Cardbox_A1_Albedo.png'
           *   './Textures/T_Cardbox_A1_Normal.png'
           *   './Textures/T_Cardbox_A1_ORM.png'
       *   Inputs:
           *   'diffuse_texture' [asset] = './Textures/T_Cardbox_A1_Albedo.png'
           *   'normalmap_texture' [asset] = './Textures/T_Cardbox_A1_Normal.png'
           *   'ORM_texture' [asset] = './Textures/T_Cardbox_A1_ORM.png'
           *   'reflection_roughness_texture_influence' [float] = '1'


---


### /World/Cardbox_A1_20/Looks/Cardboard_A
*  **Prim路径 (Prim Path):**/World/Cardbox_A1_20/Looks/Cardboard_A
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/Cardbox_A1_20/Looks/Cardboard_A/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/Cardbox_A1_20/Looks/Cardboard_A/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   纹理引用 (Texture Assets):
           *   './Textures/T_Cardbox_A1_Albedo.png'
           *   './Textures/T_Cardbox_A1_Normal.png'
           *   './Textures/T_Cardbox_A1_ORM.png'
       *   Inputs:
           *   'diffuse_texture' [asset] = './Textures/T_Cardbox_A1_Albedo.png'
           *   'normalmap_texture' [asset] = './Textures/T_Cardbox_A1_Normal.png'
           *   'ORM_texture' [asset] = './Textures/T_Cardbox_A1_ORM.png'
           *   'reflection_roughness_texture_influence' [float] = '1'


---


### /World/Cardbox_A1_21/Looks/Cardboard_A
*  **Prim路径 (Prim Path):**/World/Cardbox_A1_21/Looks/Cardboard_A
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/Cardbox_A1_21/Looks/Cardboard_A/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/Cardbox_A1_21/Looks/Cardboard_A/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   纹理引用 (Texture Assets):
           *   './Textures/T_Cardbox_A1_Albedo.png'
           *   './Textures/T_Cardbox_A1_Normal.png'
           *   './Textures/T_Cardbox_A1_ORM.png'
       *   Inputs:
           *   'diffuse_texture' [asset] = './Textures/T_Cardbox_A1_Albedo.png'
           *   'normalmap_texture' [asset] = './Textures/T_Cardbox_A1_Normal.png'
           *   'ORM_texture' [asset] = './Textures/T_Cardbox_A1_ORM.png'
           *   'reflection_roughness_texture_influence' [float] = '1'


---


### /World/Simple_rubber_conveyor_01/Materials/Conveyor
*  **Prim路径 (Prim Path):**/World/Simple_rubber_conveyor_01/Materials/Conveyor
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/Simple_rubber_conveyor_01/Materials/Conveyor/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/Simple_rubber_conveyor_01/Materials/Conveyor/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f]
               *   Connected: '/World/Simple_rubber_conveyor_01/Materials/Conveyor/tex_base.outputs:rgb' @ '/World/Simple_rubber_conveyor_01/Materials/Conveyor/tex_base'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/Conveyor_diffuse.jpg'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'glossiness' [float]
               *   Connected: '/World/Simple_rubber_conveyor_01/Materials/Conveyor/tex_glossiness.outputs:r' @ '/World/Simple_rubber_conveyor_01/Materials/Conveyor/tex_glossiness'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/Conveyor_specularGlossiness_gloss_scale0.jpg'
           *   'normal' [normal3f]
               *   Connected: '/World/Simple_rubber_conveyor_01/Materials/Conveyor/tex_normal.outputs:rgb' @ '/World/Simple_rubber_conveyor_01/Materials/Conveyor/tex_normal'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/Conveyor_normal.jpg'
           *   'occlusion' [float]
               *   Connected: '/World/Simple_rubber_conveyor_01/Materials/Conveyor/tex_occlusion.outputs:r' @ '/World/Simple_rubber_conveyor_01/Materials/Conveyor/tex_occlusion'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/Conveyor_occlusion_occl.jpg'
           *   'specularColor' [float3]
               *   Connected: '/World/Simple_rubber_conveyor_01/Materials/Conveyor/tex_specular.outputs:rgb' @ '/World/Simple_rubber_conveyor_01/Materials/Conveyor/tex_specular'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/Conveyor_specularGlossiness_spec.jpg'
       *   '/World/Simple_rubber_conveyor_01/Materials/Conveyor/tex_base' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/Conveyor_diffuse.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
           *   'file' [asset] = '0/Conveyor_diffuse.jpg'
           *   'st' [float2]
               *   Connected: '/World/Simple_rubber_conveyor_01/Materials/Conveyor/uvset0.outputs:result' @ '/World/Simple_rubber_conveyor_01/Materials/Conveyor/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/Simple_rubber_conveyor_01/Materials/Conveyor/uvset0' (ID: 'UsdPrimvarReader_float2')
       *   Implementation: 'id'
       *   '/World/Simple_rubber_conveyor_01/Materials/Conveyor/tex_glossiness' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/Conveyor_specularGlossiness_gloss_scale0.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(1.000, 0.000, 0.000, 1.000)'
           *   'file' [asset] = '0/Conveyor_specularGlossiness_gloss_scale0.jpg'
           *   'st' [float2]
               *   Connected: '/World/Simple_rubber_conveyor_01/Materials/Conveyor/uvset0.outputs:result' @ '/World/Simple_rubber_conveyor_01/Materials/Conveyor/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/Simple_rubber_conveyor_01/Materials/Conveyor/tex_normal' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/Conveyor_normal.jpg'
       *   Inputs:
           *   'bias' [float4] = '(-1.000, -1.000, -1.000, -1.000)'
           *   'fallback' [float4] = '(0.000, 0.000, 1.000, 1.000)'
           *   'file' [asset] = '0/Conveyor_normal.jpg'
           *   'scale' [float4] = '(2.000, 2.000, 2.000, 2.000)'
           *   'st' [float2]
               *   Connected: '/World/Simple_rubber_conveyor_01/Materials/Conveyor/uvset0.outputs:result' @ '/World/Simple_rubber_conveyor_01/Materials/Conveyor/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/Simple_rubber_conveyor_01/Materials/Conveyor/tex_occlusion' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/Conveyor_occlusion_occl.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(1.000, 0.000, 0.000, 1.000)'
           *   'file' [asset] = '0/Conveyor_occlusion_occl.jpg'
           *   'st' [float2]
               *   Connected: '/World/Simple_rubber_conveyor_01/Materials/Conveyor/uvset0.outputs:result' @ '/World/Simple_rubber_conveyor_01/Materials/Conveyor/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/Simple_rubber_conveyor_01/Materials/Conveyor/tex_specular' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/Conveyor_specularGlossiness_spec.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
           *   'file' [asset] = '0/Conveyor_specularGlossiness_spec.jpg'
           *   'st' [float2]
               *   Connected: '/World/Simple_rubber_conveyor_01/Materials/Conveyor/uvset0.outputs:result' @ '/World/Simple_rubber_conveyor_01/Materials/Conveyor/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'


---


### /World/Simple_rubber_conveyor_01/Materials/Belt
*  **Prim路径 (Prim Path):**/World/Simple_rubber_conveyor_01/Materials/Belt
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/Simple_rubber_conveyor_01/Materials/Belt/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/Simple_rubber_conveyor_01/Materials/Belt/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f]
               *   Connected: '/World/Simple_rubber_conveyor_01/Materials/Belt/tex_base.outputs:rgb' @ '/World/Simple_rubber_conveyor_01/Materials/Belt/tex_base'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/Belt_diffuse.jpg'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'glossiness' [float] = '0.060939'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'specularColor' [float3] = '(0.050, 0.050, 0.050)'
       *   '/World/Simple_rubber_conveyor_01/Materials/Belt/tex_base' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/Belt_diffuse.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
           *   'file' [asset] = '0/Belt_diffuse.jpg'
           *   'st' [float2]
               *   Connected: '/World/Simple_rubber_conveyor_01/Materials/Belt/uvset0.outputs:result' @ '/World/Simple_rubber_conveyor_01/Materials/Belt/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/Simple_rubber_conveyor_01/Materials/Belt/uvset0' (ID: 'UsdPrimvarReader_float2')
       *   Implementation: 'id'


---


### /World/Cardbox_A1_22/Looks/Cardboard_A
*  **Prim路径 (Prim Path):**/World/Cardbox_A1_22/Looks/Cardboard_A
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/Cardbox_A1_22/Looks/Cardboard_A/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/Cardbox_A1_22/Looks/Cardboard_A/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   纹理引用 (Texture Assets):
           *   './Textures/T_Cardbox_A1_Albedo.png'
           *   './Textures/T_Cardbox_A1_Normal.png'
           *   './Textures/T_Cardbox_A1_ORM.png'
       *   Inputs:
           *   'diffuse_texture' [asset] = './Textures/T_Cardbox_A1_Albedo.png'
           *   'normalmap_texture' [asset] = './Textures/T_Cardbox_A1_Normal.png'
           *   'ORM_texture' [asset] = './Textures/T_Cardbox_A1_ORM.png'
           *   'reflection_roughness_texture_influence' [float] = '1'


---


### /World/Cardbox_A1_23/Looks/Cardboard_A
*  **Prim路径 (Prim Path):**/World/Cardbox_A1_23/Looks/Cardboard_A
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/Cardbox_A1_23/Looks/Cardboard_A/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/Cardbox_A1_23/Looks/Cardboard_A/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   纹理引用 (Texture Assets):
           *   './Textures/T_Cardbox_A1_Albedo.png'
           *   './Textures/T_Cardbox_A1_Normal.png'
           *   './Textures/T_Cardbox_A1_ORM.png'
       *   Inputs:
           *   'diffuse_texture' [asset] = './Textures/T_Cardbox_A1_Albedo.png'
           *   'normalmap_texture' [asset] = './Textures/T_Cardbox_A1_Normal.png'
           *   'ORM_texture' [asset] = './Textures/T_Cardbox_A1_ORM.png'
           *   'reflection_roughness_texture_influence' [float] = '1'


---


### /World/Cardbox_A1_24/Looks/Cardboard_A
*  **Prim路径 (Prim Path):**/World/Cardbox_A1_24/Looks/Cardboard_A
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/Cardbox_A1_24/Looks/Cardboard_A/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/Cardbox_A1_24/Looks/Cardboard_A/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   纹理引用 (Texture Assets):
           *   './Textures/T_Cardbox_A1_Albedo.png'
           *   './Textures/T_Cardbox_A1_Normal.png'
           *   './Textures/T_Cardbox_A1_ORM.png'
       *   Inputs:
           *   'diffuse_texture' [asset] = './Textures/T_Cardbox_A1_Albedo.png'
           *   'normalmap_texture' [asset] = './Textures/T_Cardbox_A1_Normal.png'
           *   'ORM_texture' [asset] = './Textures/T_Cardbox_A1_ORM.png'
           *   'reflection_roughness_texture_influence' [float] = '1'


---


### /World/AGV_ready_02/Materials/ASELSAN_CATS_04
*  **Prim路径 (Prim Path):**/World/AGV_ready_02/Materials/ASELSAN_CATS_04
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_02/Materials/ASELSAN_CATS_04/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_02/Materials/ASELSAN_CATS_04/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.158, 0.158, 0.158)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_02/Materials/ASELSAN_CATS_04_2
*  **Prim路径 (Prim Path):**/World/AGV_ready_02/Materials/ASELSAN_CATS_04_2
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_02/Materials/ASELSAN_CATS_04_2/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_02/Materials/ASELSAN_CATS_04_2/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.769, 0.773, 0.749)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_02/Materials/ASELSAN_CATS_13
*  **Prim路径 (Prim Path):**/World/AGV_ready_02/Materials/ASELSAN_CATS_13
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_02/Materials/ASELSAN_CATS_13/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_02/Materials/ASELSAN_CATS_13/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.706, 0.718, 0.729)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_02/Materials/Color_000
*  **Prim路径 (Prim Path):**/World/AGV_ready_02/Materials/Color_000
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_02/Materials/Color_000/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_02/Materials/Color_000/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(1.000, 1.000, 1.000)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_02/Materials/Color_A05
*  **Prim路径 (Prim Path):**/World/AGV_ready_02/Materials/Color_A05
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_02/Materials/Color_A05/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_02/Materials/Color_A05/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(1.000, 0.000, 0.000)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0.959234'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0'


---


### /World/AGV_ready_02/Materials/Color_A06
*  **Prim路径 (Prim Path):**/World/AGV_ready_02/Materials/Color_A06
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_02/Materials/Color_A06/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_02/Materials/Color_A06/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.800, 0.000, 0.000)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_02/Materials/Color_B05
*  **Prim路径 (Prim Path):**/World/AGV_ready_02/Materials/Color_B05
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_02/Materials/Color_B05/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_02/Materials/Color_B05/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(1.000, 0.247, 0.000)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '1'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0'


---


### /World/AGV_ready_02/Materials/Color_E02
*  **Prim路径 (Prim Path):**/World/AGV_ready_02/Materials/Color_E02
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_02/Materials/Color_E02/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_02/Materials/Color_E02/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(1.000, 1.000, 0.196)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_02/Materials/Color_E05
*  **Prim路径 (Prim Path):**/World/AGV_ready_02/Materials/Color_E05
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_02/Materials/Color_E05/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_02/Materials/Color_E05/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(1.000, 0.910, 0.000)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0.625455'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0.133891'


---


### /World/AGV_ready_02/Materials/Color_F06
*  **Prim路径 (Prim Path):**/World/AGV_ready_02/Materials/Color_F06
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_02/Materials/Color_F06/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_02/Materials/Color_F06/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.400, 0.800, 0.000)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_02/Materials/Color_G03
*  **Prim路径 (Prim Path):**/World/AGV_ready_02/Materials/Color_G03
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_02/Materials/Color_G03/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_02/Materials/Color_G03/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.396, 1.000, 0.396)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_02/Materials/Color_M02
*  **Prim路径 (Prim Path):**/World/AGV_ready_02/Materials/Color_M02
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_02/Materials/Color_M02/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_02/Materials/Color_M02/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.776, 0.776, 0.776)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_02/Materials/Color_M03
*  **Prim路径 (Prim Path):**/World/AGV_ready_02/Materials/Color_M03
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_02/Materials/Color_M03/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_02/Materials/Color_M03/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.667, 0.667, 0.667)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_02/Materials/Mtl39
*  **Prim路径 (Prim Path):**/World/AGV_ready_02/Materials/Mtl39
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_02/Materials/Mtl39/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_02/Materials/Mtl39/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.494, 0.494, 0.494)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_02/Materials/Mtl6
*  **Prim路径 (Prim Path):**/World/AGV_ready_02/Materials/Mtl6
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_02/Materials/Mtl6/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_02/Materials/Mtl6/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f]
               *   Connected: '/World/AGV_ready_02/Materials/Mtl6/tex_base.outputs:rgb' @ '/World/AGV_ready_02/Materials/Mtl6/tex_base'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/Mtl6_baseColor.jpg'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'
       *   '/World/AGV_ready_02/Materials/Mtl6/tex_base' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/Mtl6_baseColor.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
           *   'file' [asset] = '0/Mtl6_baseColor.jpg'
           *   'st' [float2]
               *   Connected: '/World/AGV_ready_02/Materials/Mtl6/uvset0.outputs:result' @ '/World/AGV_ready_02/Materials/Mtl6/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/AGV_ready_02/Materials/Mtl6/uvset0' (ID: 'UsdPrimvarReader_float2')
       *   Implementation: 'id'


---


### /World/AGV_ready_02/Materials/Mtl9
*  **Prim路径 (Prim Path):**/World/AGV_ready_02/Materials/Mtl9
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_02/Materials/Mtl9/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_02/Materials/Mtl9/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.514, 1.000, 0.000)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_02/Materials/Silver
*  **Prim路径 (Prim Path):**/World/AGV_ready_02/Materials/Silver
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_02/Materials/Silver/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_02/Materials/Silver/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.753, 0.753, 0.753)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_02/Materials/material
*  **Prim路径 (Prim Path):**/World/AGV_ready_02/Materials/material
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_02/Materials/material/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_02/Materials/material/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f]
               *   Connected: '/World/AGV_ready_02/Materials/material/tex_base.outputs:rgb' @ '/World/AGV_ready_02/Materials/material/tex_base'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/material_baseColor.jpg'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'
       *   '/World/AGV_ready_02/Materials/material/tex_base' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/material_baseColor.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
           *   'file' [asset] = '0/material_baseColor.jpg'
           *   'st' [float2]
               *   Connected: '/World/AGV_ready_02/Materials/material/uvset0.outputs:result' @ '/World/AGV_ready_02/Materials/material/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/AGV_ready_02/Materials/material/uvset0' (ID: 'UsdPrimvarReader_float2')
       *   Implementation: 'id'


---


### /World/AGV_ready_02/Materials/cash_register_keys
*  **Prim路径 (Prim Path):**/World/AGV_ready_02/Materials/cash_register_keys
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_02/Materials/cash_register_keys/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_02/Materials/cash_register_keys/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.976, 0.992, 0.973)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_02/Materials/Chris_Shoe_Sole
*  **Prim路径 (Prim Path):**/World/AGV_ready_02/Materials/Chris_Shoe_Sole
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_02/Materials/Chris_Shoe_Sole/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_02/Materials/Chris_Shoe_Sole/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.155, 0.149, 0.149)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'opacity' [float] = '0.25'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_02/Materials/Color_002
*  **Prim路径 (Prim Path):**/World/AGV_ready_02/Materials/Color_002
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_02/Materials/Color_002/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_02/Materials/Color_002/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.217, 0.217, 0.217)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0.570837'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0'


---


### /World/AGV_ready_02/Materials/Color_005
*  **Prim路径 (Prim Path):**/World/AGV_ready_02/Materials/Color_005
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_02/Materials/Color_005/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_02/Materials/Color_005/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.130, 0.130, 0.130)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0.710417'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0'


---


### /World/AGV_ready_02/Materials/Color_006
*  **Prim路径 (Prim Path):**/World/AGV_ready_02/Materials/Color_006
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_02/Materials/Color_006/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_02/Materials/Color_006/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0.237059'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0'


---


### /World/AGV_ready_02/Materials/Color_008
*  **Prim路径 (Prim Path):**/World/AGV_ready_02/Materials/Color_008
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_02/Materials/Color_008/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_02/Materials/Color_008/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.118, 0.118, 0.118)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0.941027'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0'


---


### /World/AGV_ready_02/Materials/Color_A01
*  **Prim路径 (Prim Path):**/World/AGV_ready_02/Materials/Color_A01
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_02/Materials/Color_A01/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_02/Materials/Color_A01/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(1.000, 0.000, 0.000)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0.965302'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0'


---


### /World/AGV_ready_02/Materials/Color_A11
*  **Prim路径 (Prim Path):**/World/AGV_ready_02/Materials/Color_A11
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_02/Materials/Color_A11/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_02/Materials/Color_A11/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.600, 0.000, 0.000)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_02/Materials/Color_M04
*  **Prim路径 (Prim Path):**/World/AGV_ready_02/Materials/Color_M04
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_02/Materials/Color_M04/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_02/Materials/Color_M04/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.557, 0.557, 0.557)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_02/Materials/Color_M05
*  **Prim路径 (Prim Path):**/World/AGV_ready_02/Materials/Color_M05
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_02/Materials/Color_M05/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_02/Materials/Color_M05/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.447, 0.447, 0.447)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_02/Materials/Color_M06
*  **Prim路径 (Prim Path):**/World/AGV_ready_02/Materials/Color_M06
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_02/Materials/Color_M06/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_02/Materials/Color_M06/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_02/Materials/Color_M07
*  **Prim路径 (Prim Path):**/World/AGV_ready_02/Materials/Color_M07
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_02/Materials/Color_M07/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_02/Materials/Color_M07/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.227, 0.227, 0.227)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_02/Materials/Color_M09
*  **Prim路径 (Prim Path):**/World/AGV_ready_02/Materials/Color_M09
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_02/Materials/Color_M09/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_02/Materials/Color_M09/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0.340226'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0.085341'


---


### /World/AGV_ready_02/Materials/FCP_Charcoal_v2
*  **Prim路径 (Prim Path):**/World/AGV_ready_02/Materials/FCP_Charcoal_v2
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_02/Materials/FCP_Charcoal_v2/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_02/Materials/FCP_Charcoal_v2/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.216, 0.216, 0.216)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_02/Materials/FrontColor
*  **Prim路径 (Prim Path):**/World/AGV_ready_02/Materials/FrontColor
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_02/Materials/FrontColor/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_02/Materials/FrontColor/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.504, 0.504, 0.504)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0.637593'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0.218852'


---


### /World/AGV_ready_02/Materials/Light_Blue
*  **Prim路径 (Prim Path):**/World/AGV_ready_02/Materials/Light_Blue
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_02/Materials/Light_Blue/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_02/Materials/Light_Blue/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.601, 0.601, 0.601)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '1'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0.170303'


---


### /World/AGV_ready_02/Materials/M_0011_Seashell
*  **Prim路径 (Prim Path):**/World/AGV_ready_02/Materials/M_0011_Seashell
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_02/Materials/M_0011_Seashell/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_02/Materials/M_0011_Seashell/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(1.000, 0.961, 0.933)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_02/Materials/M_0131_Silver
*  **Prim路径 (Prim Path):**/World/AGV_ready_02/Materials/M_0131_Silver
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_02/Materials/M_0131_Silver/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_02/Materials/M_0131_Silver/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.242, 0.242, 0.242)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0.613318'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0'


---


### /World/AGV_ready_02/Materials/M_0134_DimGray
*  **Prim路径 (Prim Path):**/World/AGV_ready_02/Materials/M_0134_DimGray
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_02/Materials/M_0134_DimGray/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_02/Materials/M_0134_DimGray/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.412, 0.412, 0.412)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_02/Materials/M_0135_DarkGray
*  **Prim路径 (Prim Path):**/World/AGV_ready_02/Materials/M_0135_DarkGray
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_02/Materials/M_0135_DarkGray/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_02/Materials/M_0135_DarkGray/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.318, 0.318, 0.318)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_02/Materials/Metal_Silver
*  **Prim路径 (Prim Path):**/World/AGV_ready_02/Materials/Metal_Silver
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_02/Materials/Metal_Silver/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_02/Materials/Metal_Silver/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.918, 0.914, 0.933)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_02/Materials/Mtl1
*  **Prim路径 (Prim Path):**/World/AGV_ready_02/Materials/Mtl1
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_02/Materials/Mtl1/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_02/Materials/Mtl1/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.015, 0.015, 0.015)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0.255265'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_02/Materials/Mtl10
*  **Prim路径 (Prim Path):**/World/AGV_ready_02/Materials/Mtl10
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_02/Materials/Mtl10/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_02/Materials/Mtl10/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.322, 0.322, 0.322)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_02/Materials/Mtl11
*  **Prim路径 (Prim Path):**/World/AGV_ready_02/Materials/Mtl11
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_02/Materials/Mtl11/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_02/Materials/Mtl11/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.067, 0.757, 0.329)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_02/Materials/Mtl12
*  **Prim路径 (Prim Path):**/World/AGV_ready_02/Materials/Mtl12
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_02/Materials/Mtl12/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_02/Materials/Mtl12/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.502, 0.502, 0.502)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_02/Materials/Mtl13
*  **Prim路径 (Prim Path):**/World/AGV_ready_02/Materials/Mtl13
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_02/Materials/Mtl13/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_02/Materials/Mtl13/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.008, 0.514, 0.816)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_02/Materials/Mtl14
*  **Prim路径 (Prim Path):**/World/AGV_ready_02/Materials/Mtl14
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_02/Materials/Mtl14/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_02/Materials/Mtl14/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.310, 0.310, 0.310)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_02/Materials/Mtl15
*  **Prim路径 (Prim Path):**/World/AGV_ready_02/Materials/Mtl15
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_02/Materials/Mtl15/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_02/Materials/Mtl15/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.263, 0.275, 0.275)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_02/Materials/Mtl16
*  **Prim路径 (Prim Path):**/World/AGV_ready_02/Materials/Mtl16
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_02/Materials/Mtl16/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_02/Materials/Mtl16/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.698, 0.698, 0.000)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_02/Materials/Mtl17
*  **Prim路径 (Prim Path):**/World/AGV_ready_02/Materials/Mtl17
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_02/Materials/Mtl17/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_02/Materials/Mtl17/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.000, 0.863, 1.000)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_02/Materials/Mtl3
*  **Prim路径 (Prim Path):**/World/AGV_ready_02/Materials/Mtl3
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_02/Materials/Mtl3/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_02/Materials/Mtl3/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.431, 0.455, 0.498)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_02/Materials/Mtl35
*  **Prim路径 (Prim Path):**/World/AGV_ready_02/Materials/Mtl35
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_02/Materials/Mtl35/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_02/Materials/Mtl35/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.792, 0.820, 0.933)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_02/Materials/Mtl36
*  **Prim路径 (Prim Path):**/World/AGV_ready_02/Materials/Mtl36
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_02/Materials/Mtl36/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_02/Materials/Mtl36/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.667, 0.698, 0.765)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_02/Materials/Mtl37
*  **Prim路径 (Prim Path):**/World/AGV_ready_02/Materials/Mtl37
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_02/Materials/Mtl37/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_02/Materials/Mtl37/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.098, 0.098, 0.098)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_02/Materials/Mtl3a
*  **Prim路径 (Prim Path):**/World/AGV_ready_02/Materials/Mtl3a
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_02/Materials/Mtl3a/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_02/Materials/Mtl3a/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.388, 0.369, 0.322)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_02/Materials/Mtl3b
*  **Prim路径 (Prim Path):**/World/AGV_ready_02/Materials/Mtl3b
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_02/Materials/Mtl3b/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_02/Materials/Mtl3b/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.365, 0.176, 0.012)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0.959234'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'opacity' [float] = '0.273471'
           *   'roughness' [float] = '0.164234'


---


### /World/AGV_ready_02/Materials/Mtl5
*  **Prim路径 (Prim Path):**/World/AGV_ready_02/Materials/Mtl5
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_02/Materials/Mtl5/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_02/Materials/Mtl5/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.396, 0.408, 0.467)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_02/Materials/Mtl7
*  **Prim路径 (Prim Path):**/World/AGV_ready_02/Materials/Mtl7
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_02/Materials/Mtl7/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_02/Materials/Mtl7/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.376, 0.376, 0.376)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_02/Materials/Mtl8
*  **Prim路径 (Prim Path):**/World/AGV_ready_02/Materials/Mtl8
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_02/Materials/Mtl8/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_02/Materials/Mtl8/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.173, 0.173, 0.173)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_02/Materials/Mtla
*  **Prim路径 (Prim Path):**/World/AGV_ready_02/Materials/Mtla
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_02/Materials/Mtla/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_02/Materials/Mtla/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.612, 0.725, 0.745)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_02/Materials/Mtlb1
*  **Prim路径 (Prim Path):**/World/AGV_ready_02/Materials/Mtlb1
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_02/Materials/Mtlb1/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_02/Materials/Mtlb1/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.949, 0.925, 0.933)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_02/Materials/Stainless_Steel
*  **Prim路径 (Prim Path):**/World/AGV_ready_02/Materials/Stainless_Steel
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_02/Materials/Stainless_Steel/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_02/Materials/Stainless_Steel/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.292, 0.294, 0.284)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0.431257'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_02/Materials/Metal_Aluminum_Anodized_1
*  **Prim路径 (Prim Path):**/World/AGV_ready_02/Materials/Metal_Aluminum_Anodized_1
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_02/Materials/Metal_Aluminum_Anodized_1/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_02/Materials/Metal_Aluminum_Anodized_1/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.260, 0.269, 0.282)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0.309883'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0'


---


### /World/AGV_ready_02/Materials/Metal_Aluminum_Anodized_2
*  **Prim路径 (Prim Path):**/World/AGV_ready_02/Materials/Metal_Aluminum_Anodized_2
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_02/Materials/Metal_Aluminum_Anodized_2/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_02/Materials/Metal_Aluminum_Anodized_2/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.792, 0.820, 0.859)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_02/Materials/basic_gray_plastic
*  **Prim路径 (Prim Path):**/World/AGV_ready_02/Materials/basic_gray_plastic
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_02/Materials/basic_gray_plastic/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_02/Materials/basic_gray_plastic/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0.297745'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0.115685'


---


### /World/AGV_ready_02/Materials/texture
*  **Prim路径 (Prim Path):**/World/AGV_ready_02/Materials/texture
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_02/Materials/texture/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_02/Materials/texture/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.294, 0.294, 0.294)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/Cardbox_A1_25/Looks/Cardboard_A
*  **Prim路径 (Prim Path):**/World/Cardbox_A1_25/Looks/Cardboard_A
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/Cardbox_A1_25/Looks/Cardboard_A/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/Cardbox_A1_25/Looks/Cardboard_A/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   纹理引用 (Texture Assets):
           *   './Textures/T_Cardbox_A1_Albedo.png'
           *   './Textures/T_Cardbox_A1_Normal.png'
           *   './Textures/T_Cardbox_A1_ORM.png'
       *   Inputs:
           *   'diffuse_texture' [asset] = './Textures/T_Cardbox_A1_Albedo.png'
           *   'normalmap_texture' [asset] = './Textures/T_Cardbox_A1_Normal.png'
           *   'ORM_texture' [asset] = './Textures/T_Cardbox_A1_ORM.png'
           *   'reflection_roughness_texture_influence' [float] = '1'


---


### /World/forklift/S_ForkliftFork/Materials/OmniPBR
*  **Prim路径 (Prim Path):**/World/forklift/S_ForkliftFork/Materials/OmniPBR
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/forklift/S_ForkliftFork/Materials/OmniPBR/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/forklift/S_ForkliftFork/Materials/OmniPBR/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   纹理引用 (Texture Assets):
           *   '0/T_Forklift_D.png'
           *   '0/T_Forklift_N.png'
           *   '0/T_Forklift_ORM.png'
       *   Inputs:
           *   'diffuse_texture' [asset] = '0/T_Forklift_D.png'
           *   'normalmap_texture' [asset] = '0/T_Forklift_N.png'
           *   'ORM_texture' [asset] = '0/T_Forklift_ORM.png'
           *   'reflection_roughness_texture_influence' [float] = '1'


---


### /World/forklift/Materials/OmniPBR
*  **Prim路径 (Prim Path):**/World/forklift/Materials/OmniPBR
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/forklift/Materials/OmniPBR/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/forklift/Materials/OmniPBR/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   纹理引用 (Texture Assets):
           *   '0/T_Forklift_D.png'
           *   '0/T_Forklift_N.png'
           *   '0/T_Forklift_ORM.png'
       *   Inputs:
           *   'diffuse_texture' [asset] = '0/T_Forklift_D.png'
           *   'normalmap_texture' [asset] = '0/T_Forklift_N.png'
           *   'ORM_texture' [asset] = '0/T_Forklift_ORM.png'
           *   'reflection_roughness_texture_influence' [float] = '1'


---


### /World/ridgeback_franka/panda_link0/visuals/Looks/EmissiveBlue
*  **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_link0/visuals/Looks/EmissiveBlue
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_link0/visuals/Looks/EmissiveBlue/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/ridgeback_franka/panda_link0/visuals/Looks/EmissiveBlue/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(1.000, 1.000, 1.000)'
           *   'emissive_color' [color3f] = '(0.000, 0.100, 1.000)'
           *   'emissive_intensity' [float] = '29000'
           *   'reflection_roughness_constant' [float] = '0.298'


---


### /World/ridgeback_franka/panda_link0/visuals/Looks/PlasticGray
*  **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_link0/visuals/Looks/PlasticGray
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_link0/visuals/Looks/PlasticGray/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/ridgeback_franka/panda_link0/visuals/Looks/PlasticGray/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.100, 0.100, 0.100)'
           *   'reflection_roughness_constant' [float] = '0.292'


---


### /World/ridgeback_franka/panda_link0/visuals/Looks/Aluminum
*  **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_link0/visuals/Looks/Aluminum
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_link0/visuals/Looks/Aluminum/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/ridgeback_franka/panda_link0/visuals/Looks/Aluminum/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.900, 0.900, 0.900)'
           *   'metallic_constant' [float] = '0.899'
           *   'reflection_roughness_constant' [float] = '0.101'


---


### /World/ridgeback_franka/panda_link0/visuals/Looks/PlasticBlack
*  **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_link0/visuals/Looks/PlasticBlack
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_link0/visuals/Looks/PlasticBlack/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/ridgeback_franka/panda_link0/visuals/Looks/PlasticBlack/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.000, 0.000, 0.000)'
           *   'reflection_roughness_constant' [float] = '0'


---


### /World/ridgeback_franka/panda_link0/visuals/Looks/RubberGreen
*  **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_link0/visuals/Looks/RubberGreen
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_link0/visuals/Looks/RubberGreen/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/ridgeback_franka/panda_link0/visuals/Looks/RubberGreen/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.000, 0.500, 0.000)'


---


### /World/ridgeback_franka/panda_link0/visuals/Looks/RubberRed
*  **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_link0/visuals/Looks/RubberRed
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_link0/visuals/Looks/RubberRed/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/ridgeback_franka/panda_link0/visuals/Looks/RubberRed/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.500, 0.000, 0.000)'


---


### /World/ridgeback_franka/panda_link0/visuals/Looks/RubberWhite
*  **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_link0/visuals/Looks/RubberWhite
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_link0/visuals/Looks/RubberWhite/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/ridgeback_franka/panda_link0/visuals/Looks/RubberWhite/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.900, 0.900, 0.900)'


---


### /World/ridgeback_franka/panda_link0/visuals/Looks/RubberGray
*  **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_link0/visuals/Looks/RubberGray
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_link0/visuals/Looks/RubberGray/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/ridgeback_franka/panda_link0/visuals/Looks/RubberGray/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.050, 0.050, 0.050)'


---


### /World/ridgeback_franka/panda_link0/visuals/Looks/RubberLightGray
*  **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_link0/visuals/Looks/RubberLightGray
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_link0/visuals/Looks/RubberLightGray/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/ridgeback_franka/panda_link0/visuals/Looks/RubberLightGray/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')


---


### /World/ridgeback_franka/panda_link0/visuals/Looks/AluminumRough
*  **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_link0/visuals/Looks/AluminumRough
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_link0/visuals/Looks/AluminumRough/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/ridgeback_franka/panda_link0/visuals/Looks/AluminumRough/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.400, 0.400, 0.400)'
           *   'metallic_constant' [float] = '0.399'
           *   'reflection_roughness_constant' [float] = '0.202'


---


### /World/ridgeback_franka/panda_link0/visuals/Looks/rubber_cable
*  **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_link0/visuals/Looks/rubber_cable
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_link0/visuals/Looks/rubber_cable/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/ridgeback_franka/panda_link0/visuals/Looks/rubber_cable/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.050, 0.050, 0.050)'
           *   'metallic_constant' [float] = '0'
           *   'reflection_roughness_constant' [float] = '0.5'
           *   'specular_level' [float] = '0'


---


### /World/ridgeback_franka/panda_link0/visuals/Looks/PlasticWhite
*  **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_link0/visuals/Looks/PlasticWhite
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_link0/visuals/Looks/PlasticWhite/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/ridgeback_franka/panda_link0/visuals/Looks/PlasticWhite/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.700, 0.700, 0.700)'
           *   'reflection_roughness_constant' [float] = '0.18'


---


### /World/ridgeback_franka/panda_link1/visuals/Looks/EmissiveBlue
*  **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_link1/visuals/Looks/EmissiveBlue
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_link1/visuals/Looks/EmissiveBlue/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/ridgeback_franka/panda_link1/visuals/Looks/EmissiveBlue/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(1.000, 1.000, 1.000)'
           *   'emissive_color' [color3f] = '(0.000, 0.100, 1.000)'
           *   'emissive_intensity' [float] = '29000'
           *   'reflection_roughness_constant' [float] = '0.298'


---


### /World/ridgeback_franka/panda_link1/visuals/Looks/PlasticGray
*  **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_link1/visuals/Looks/PlasticGray
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_link1/visuals/Looks/PlasticGray/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/ridgeback_franka/panda_link1/visuals/Looks/PlasticGray/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.100, 0.100, 0.100)'
           *   'reflection_roughness_constant' [float] = '0.292'


---


### /World/ridgeback_franka/panda_link1/visuals/Looks/Aluminum
*  **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_link1/visuals/Looks/Aluminum
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_link1/visuals/Looks/Aluminum/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/ridgeback_franka/panda_link1/visuals/Looks/Aluminum/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.900, 0.900, 0.900)'
           *   'metallic_constant' [float] = '0.899'
           *   'reflection_roughness_constant' [float] = '0.101'


---


### /World/ridgeback_franka/panda_link1/visuals/Looks/PlasticBlack
*  **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_link1/visuals/Looks/PlasticBlack
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_link1/visuals/Looks/PlasticBlack/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/ridgeback_franka/panda_link1/visuals/Looks/PlasticBlack/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.000, 0.000, 0.000)'
           *   'reflection_roughness_constant' [float] = '0'


---


### /World/ridgeback_franka/panda_link1/visuals/Looks/RubberGreen
*  **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_link1/visuals/Looks/RubberGreen
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_link1/visuals/Looks/RubberGreen/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/ridgeback_franka/panda_link1/visuals/Looks/RubberGreen/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.000, 0.500, 0.000)'


---


### /World/ridgeback_franka/panda_link1/visuals/Looks/RubberRed
*  **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_link1/visuals/Looks/RubberRed
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_link1/visuals/Looks/RubberRed/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/ridgeback_franka/panda_link1/visuals/Looks/RubberRed/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.500, 0.000, 0.000)'


---


### /World/ridgeback_franka/panda_link1/visuals/Looks/RubberWhite
*  **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_link1/visuals/Looks/RubberWhite
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_link1/visuals/Looks/RubberWhite/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/ridgeback_franka/panda_link1/visuals/Looks/RubberWhite/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.900, 0.900, 0.900)'


---


### /World/ridgeback_franka/panda_link1/visuals/Looks/RubberGray
*  **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_link1/visuals/Looks/RubberGray
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_link1/visuals/Looks/RubberGray/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/ridgeback_franka/panda_link1/visuals/Looks/RubberGray/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.050, 0.050, 0.050)'


---


### /World/ridgeback_franka/panda_link1/visuals/Looks/RubberLightGray
*  **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_link1/visuals/Looks/RubberLightGray
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_link1/visuals/Looks/RubberLightGray/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/ridgeback_franka/panda_link1/visuals/Looks/RubberLightGray/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')


---


### /World/ridgeback_franka/panda_link1/visuals/Looks/AluminumRough
*  **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_link1/visuals/Looks/AluminumRough
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_link1/visuals/Looks/AluminumRough/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/ridgeback_franka/panda_link1/visuals/Looks/AluminumRough/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.400, 0.400, 0.400)'
           *   'metallic_constant' [float] = '0.399'
           *   'reflection_roughness_constant' [float] = '0.202'


---


### /World/ridgeback_franka/panda_link1/visuals/Looks/rubber_cable
*  **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_link1/visuals/Looks/rubber_cable
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_link1/visuals/Looks/rubber_cable/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/ridgeback_franka/panda_link1/visuals/Looks/rubber_cable/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.050, 0.050, 0.050)'
           *   'metallic_constant' [float] = '0'
           *   'reflection_roughness_constant' [float] = '0.5'
           *   'specular_level' [float] = '0'


---


### /World/ridgeback_franka/panda_link1/visuals/Looks/PlasticWhite
*  **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_link1/visuals/Looks/PlasticWhite
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_link1/visuals/Looks/PlasticWhite/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/ridgeback_franka/panda_link1/visuals/Looks/PlasticWhite/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.700, 0.700, 0.700)'
           *   'reflection_roughness_constant' [float] = '0.18'


---


### /World/ridgeback_franka/panda_link2/visuals/Looks/EmissiveBlue
*  **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_link2/visuals/Looks/EmissiveBlue
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_link2/visuals/Looks/EmissiveBlue/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/ridgeback_franka/panda_link2/visuals/Looks/EmissiveBlue/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(1.000, 1.000, 1.000)'
           *   'emissive_color' [color3f] = '(0.000, 0.100, 1.000)'
           *   'emissive_intensity' [float] = '29000'
           *   'reflection_roughness_constant' [float] = '0.298'


---


### /World/ridgeback_franka/panda_link2/visuals/Looks/PlasticGray
*  **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_link2/visuals/Looks/PlasticGray
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_link2/visuals/Looks/PlasticGray/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/ridgeback_franka/panda_link2/visuals/Looks/PlasticGray/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.100, 0.100, 0.100)'
           *   'reflection_roughness_constant' [float] = '0.292'


---


### /World/ridgeback_franka/panda_link2/visuals/Looks/Aluminum
*  **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_link2/visuals/Looks/Aluminum
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_link2/visuals/Looks/Aluminum/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/ridgeback_franka/panda_link2/visuals/Looks/Aluminum/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.900, 0.900, 0.900)'
           *   'metallic_constant' [float] = '0.899'
           *   'reflection_roughness_constant' [float] = '0.101'


---


### /World/ridgeback_franka/panda_link2/visuals/Looks/PlasticBlack
*  **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_link2/visuals/Looks/PlasticBlack
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_link2/visuals/Looks/PlasticBlack/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/ridgeback_franka/panda_link2/visuals/Looks/PlasticBlack/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.000, 0.000, 0.000)'
           *   'reflection_roughness_constant' [float] = '0'


---


### /World/ridgeback_franka/panda_link2/visuals/Looks/RubberGreen
*  **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_link2/visuals/Looks/RubberGreen
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_link2/visuals/Looks/RubberGreen/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/ridgeback_franka/panda_link2/visuals/Looks/RubberGreen/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.000, 0.500, 0.000)'


---


### /World/ridgeback_franka/panda_link2/visuals/Looks/RubberRed
*  **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_link2/visuals/Looks/RubberRed
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_link2/visuals/Looks/RubberRed/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/ridgeback_franka/panda_link2/visuals/Looks/RubberRed/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.500, 0.000, 0.000)'


---


### /World/ridgeback_franka/panda_link2/visuals/Looks/RubberWhite
*  **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_link2/visuals/Looks/RubberWhite
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_link2/visuals/Looks/RubberWhite/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/ridgeback_franka/panda_link2/visuals/Looks/RubberWhite/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.900, 0.900, 0.900)'


---


### /World/ridgeback_franka/panda_link2/visuals/Looks/RubberGray
*  **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_link2/visuals/Looks/RubberGray
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_link2/visuals/Looks/RubberGray/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/ridgeback_franka/panda_link2/visuals/Looks/RubberGray/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.050, 0.050, 0.050)'


---


### /World/ridgeback_franka/panda_link2/visuals/Looks/RubberLightGray
*  **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_link2/visuals/Looks/RubberLightGray
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_link2/visuals/Looks/RubberLightGray/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/ridgeback_franka/panda_link2/visuals/Looks/RubberLightGray/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')


---


### /World/ridgeback_franka/panda_link2/visuals/Looks/AluminumRough
*  **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_link2/visuals/Looks/AluminumRough
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_link2/visuals/Looks/AluminumRough/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/ridgeback_franka/panda_link2/visuals/Looks/AluminumRough/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.400, 0.400, 0.400)'
           *   'metallic_constant' [float] = '0.399'
           *   'reflection_roughness_constant' [float] = '0.202'


---


### /World/ridgeback_franka/panda_link2/visuals/Looks/rubber_cable
*  **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_link2/visuals/Looks/rubber_cable
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_link2/visuals/Looks/rubber_cable/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/ridgeback_franka/panda_link2/visuals/Looks/rubber_cable/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.050, 0.050, 0.050)'
           *   'metallic_constant' [float] = '0'
           *   'reflection_roughness_constant' [float] = '0.5'
           *   'specular_level' [float] = '0'


---


### /World/ridgeback_franka/panda_link2/visuals/Looks/PlasticWhite
*  **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_link2/visuals/Looks/PlasticWhite
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_link2/visuals/Looks/PlasticWhite/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/ridgeback_franka/panda_link2/visuals/Looks/PlasticWhite/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.700, 0.700, 0.700)'
           *   'reflection_roughness_constant' [float] = '0.18'


---


### /World/ridgeback_franka/panda_link3/visuals/Looks/EmissiveBlue
*  **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_link3/visuals/Looks/EmissiveBlue
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_link3/visuals/Looks/EmissiveBlue/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/ridgeback_franka/panda_link3/visuals/Looks/EmissiveBlue/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(1.000, 1.000, 1.000)'
           *   'emissive_color' [color3f] = '(0.000, 0.100, 1.000)'
           *   'emissive_intensity' [float] = '29000'
           *   'reflection_roughness_constant' [float] = '0.298'


---


### /World/ridgeback_franka/panda_link3/visuals/Looks/PlasticGray
*  **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_link3/visuals/Looks/PlasticGray
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_link3/visuals/Looks/PlasticGray/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/ridgeback_franka/panda_link3/visuals/Looks/PlasticGray/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.100, 0.100, 0.100)'
           *   'reflection_roughness_constant' [float] = '0.292'


---


### /World/ridgeback_franka/panda_link3/visuals/Looks/Aluminum
*  **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_link3/visuals/Looks/Aluminum
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_link3/visuals/Looks/Aluminum/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/ridgeback_franka/panda_link3/visuals/Looks/Aluminum/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.900, 0.900, 0.900)'
           *   'metallic_constant' [float] = '0.899'
           *   'reflection_roughness_constant' [float] = '0.101'


---


### /World/ridgeback_franka/panda_link3/visuals/Looks/PlasticBlack
*  **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_link3/visuals/Looks/PlasticBlack
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_link3/visuals/Looks/PlasticBlack/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/ridgeback_franka/panda_link3/visuals/Looks/PlasticBlack/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.000, 0.000, 0.000)'
           *   'reflection_roughness_constant' [float] = '0'


---


### /World/ridgeback_franka/panda_link3/visuals/Looks/RubberGreen
*  **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_link3/visuals/Looks/RubberGreen
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_link3/visuals/Looks/RubberGreen/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/ridgeback_franka/panda_link3/visuals/Looks/RubberGreen/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.000, 0.500, 0.000)'


---


### /World/ridgeback_franka/panda_link3/visuals/Looks/RubberRed
*  **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_link3/visuals/Looks/RubberRed
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_link3/visuals/Looks/RubberRed/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/ridgeback_franka/panda_link3/visuals/Looks/RubberRed/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.500, 0.000, 0.000)'


---


### /World/ridgeback_franka/panda_link3/visuals/Looks/RubberWhite
*  **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_link3/visuals/Looks/RubberWhite
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_link3/visuals/Looks/RubberWhite/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/ridgeback_franka/panda_link3/visuals/Looks/RubberWhite/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.900, 0.900, 0.900)'


---


### /World/ridgeback_franka/panda_link3/visuals/Looks/RubberGray
*  **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_link3/visuals/Looks/RubberGray
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_link3/visuals/Looks/RubberGray/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/ridgeback_franka/panda_link3/visuals/Looks/RubberGray/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.050, 0.050, 0.050)'


---


### /World/ridgeback_franka/panda_link3/visuals/Looks/RubberLightGray
*  **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_link3/visuals/Looks/RubberLightGray
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_link3/visuals/Looks/RubberLightGray/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/ridgeback_franka/panda_link3/visuals/Looks/RubberLightGray/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')


---


### /World/ridgeback_franka/panda_link3/visuals/Looks/AluminumRough
*  **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_link3/visuals/Looks/AluminumRough
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_link3/visuals/Looks/AluminumRough/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/ridgeback_franka/panda_link3/visuals/Looks/AluminumRough/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.400, 0.400, 0.400)'
           *   'metallic_constant' [float] = '0.399'
           *   'reflection_roughness_constant' [float] = '0.202'


---


### /World/ridgeback_franka/panda_link3/visuals/Looks/rubber_cable
*  **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_link3/visuals/Looks/rubber_cable
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_link3/visuals/Looks/rubber_cable/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/ridgeback_franka/panda_link3/visuals/Looks/rubber_cable/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.050, 0.050, 0.050)'
           *   'metallic_constant' [float] = '0'
           *   'reflection_roughness_constant' [float] = '0.5'
           *   'specular_level' [float] = '0'


---


### /World/ridgeback_franka/panda_link3/visuals/Looks/PlasticWhite
*  **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_link3/visuals/Looks/PlasticWhite
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_link3/visuals/Looks/PlasticWhite/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/ridgeback_franka/panda_link3/visuals/Looks/PlasticWhite/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.700, 0.700, 0.700)'
           *   'reflection_roughness_constant' [float] = '0.18'


---


### /World/ridgeback_franka/panda_link4/visuals/Looks/EmissiveBlue
*  **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_link4/visuals/Looks/EmissiveBlue
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_link4/visuals/Looks/EmissiveBlue/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/ridgeback_franka/panda_link4/visuals/Looks/EmissiveBlue/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(1.000, 1.000, 1.000)'
           *   'emissive_color' [color3f] = '(0.000, 0.100, 1.000)'
           *   'emissive_intensity' [float] = '29000'
           *   'reflection_roughness_constant' [float] = '0.298'


---


### /World/ridgeback_franka/panda_link4/visuals/Looks/PlasticGray
*  **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_link4/visuals/Looks/PlasticGray
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_link4/visuals/Looks/PlasticGray/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/ridgeback_franka/panda_link4/visuals/Looks/PlasticGray/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.100, 0.100, 0.100)'
           *   'reflection_roughness_constant' [float] = '0.292'


---


### /World/ridgeback_franka/panda_link4/visuals/Looks/Aluminum
*  **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_link4/visuals/Looks/Aluminum
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_link4/visuals/Looks/Aluminum/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/ridgeback_franka/panda_link4/visuals/Looks/Aluminum/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.900, 0.900, 0.900)'
           *   'metallic_constant' [float] = '0.899'
           *   'reflection_roughness_constant' [float] = '0.101'


---


### /World/ridgeback_franka/panda_link4/visuals/Looks/PlasticBlack
*  **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_link4/visuals/Looks/PlasticBlack
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_link4/visuals/Looks/PlasticBlack/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/ridgeback_franka/panda_link4/visuals/Looks/PlasticBlack/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.000, 0.000, 0.000)'
           *   'reflection_roughness_constant' [float] = '0'


---


### /World/ridgeback_franka/panda_link4/visuals/Looks/RubberGreen
*  **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_link4/visuals/Looks/RubberGreen
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_link4/visuals/Looks/RubberGreen/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/ridgeback_franka/panda_link4/visuals/Looks/RubberGreen/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.000, 0.500, 0.000)'


---


### /World/ridgeback_franka/panda_link4/visuals/Looks/RubberRed
*  **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_link4/visuals/Looks/RubberRed
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_link4/visuals/Looks/RubberRed/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/ridgeback_franka/panda_link4/visuals/Looks/RubberRed/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.500, 0.000, 0.000)'


---


### /World/ridgeback_franka/panda_link4/visuals/Looks/RubberWhite
*  **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_link4/visuals/Looks/RubberWhite
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_link4/visuals/Looks/RubberWhite/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/ridgeback_franka/panda_link4/visuals/Looks/RubberWhite/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.900, 0.900, 0.900)'


---


### /World/ridgeback_franka/panda_link4/visuals/Looks/RubberGray
*  **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_link4/visuals/Looks/RubberGray
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_link4/visuals/Looks/RubberGray/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/ridgeback_franka/panda_link4/visuals/Looks/RubberGray/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.050, 0.050, 0.050)'


---


### /World/ridgeback_franka/panda_link4/visuals/Looks/RubberLightGray
*  **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_link4/visuals/Looks/RubberLightGray
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_link4/visuals/Looks/RubberLightGray/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/ridgeback_franka/panda_link4/visuals/Looks/RubberLightGray/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')


---


### /World/ridgeback_franka/panda_link4/visuals/Looks/AluminumRough
*  **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_link4/visuals/Looks/AluminumRough
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_link4/visuals/Looks/AluminumRough/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/ridgeback_franka/panda_link4/visuals/Looks/AluminumRough/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.400, 0.400, 0.400)'
           *   'metallic_constant' [float] = '0.399'
           *   'reflection_roughness_constant' [float] = '0.202'


---


### /World/ridgeback_franka/panda_link4/visuals/Looks/rubber_cable
*  **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_link4/visuals/Looks/rubber_cable
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_link4/visuals/Looks/rubber_cable/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/ridgeback_franka/panda_link4/visuals/Looks/rubber_cable/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.050, 0.050, 0.050)'
           *   'metallic_constant' [float] = '0'
           *   'reflection_roughness_constant' [float] = '0.5'
           *   'specular_level' [float] = '0'


---


### /World/ridgeback_franka/panda_link4/visuals/Looks/PlasticWhite
*  **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_link4/visuals/Looks/PlasticWhite
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_link4/visuals/Looks/PlasticWhite/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/ridgeback_franka/panda_link4/visuals/Looks/PlasticWhite/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.700, 0.700, 0.700)'
           *   'reflection_roughness_constant' [float] = '0.18'


---


### /World/ridgeback_franka/panda_link5/visuals/Looks/EmissiveBlue
*  **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_link5/visuals/Looks/EmissiveBlue
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_link5/visuals/Looks/EmissiveBlue/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/ridgeback_franka/panda_link5/visuals/Looks/EmissiveBlue/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(1.000, 1.000, 1.000)'
           *   'emissive_color' [color3f] = '(0.000, 0.100, 1.000)'
           *   'emissive_intensity' [float] = '29000'
           *   'reflection_roughness_constant' [float] = '0.298'


---


### /World/ridgeback_franka/panda_link5/visuals/Looks/PlasticGray
*  **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_link5/visuals/Looks/PlasticGray
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_link5/visuals/Looks/PlasticGray/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/ridgeback_franka/panda_link5/visuals/Looks/PlasticGray/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.100, 0.100, 0.100)'
           *   'reflection_roughness_constant' [float] = '0.292'


---


### /World/ridgeback_franka/panda_link5/visuals/Looks/Aluminum
*  **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_link5/visuals/Looks/Aluminum
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_link5/visuals/Looks/Aluminum/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/ridgeback_franka/panda_link5/visuals/Looks/Aluminum/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.900, 0.900, 0.900)'
           *   'metallic_constant' [float] = '0.899'
           *   'reflection_roughness_constant' [float] = '0.101'


---


### /World/ridgeback_franka/panda_link5/visuals/Looks/PlasticBlack
*  **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_link5/visuals/Looks/PlasticBlack
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_link5/visuals/Looks/PlasticBlack/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/ridgeback_franka/panda_link5/visuals/Looks/PlasticBlack/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.000, 0.000, 0.000)'
           *   'reflection_roughness_constant' [float] = '0'


---


### /World/ridgeback_franka/panda_link5/visuals/Looks/RubberGreen
*  **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_link5/visuals/Looks/RubberGreen
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_link5/visuals/Looks/RubberGreen/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/ridgeback_franka/panda_link5/visuals/Looks/RubberGreen/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.000, 0.500, 0.000)'


---


### /World/ridgeback_franka/panda_link5/visuals/Looks/RubberRed
*  **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_link5/visuals/Looks/RubberRed
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_link5/visuals/Looks/RubberRed/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/ridgeback_franka/panda_link5/visuals/Looks/RubberRed/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.500, 0.000, 0.000)'


---


### /World/ridgeback_franka/panda_link5/visuals/Looks/RubberWhite
*  **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_link5/visuals/Looks/RubberWhite
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_link5/visuals/Looks/RubberWhite/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/ridgeback_franka/panda_link5/visuals/Looks/RubberWhite/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.900, 0.900, 0.900)'


---


### /World/ridgeback_franka/panda_link5/visuals/Looks/RubberGray
*  **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_link5/visuals/Looks/RubberGray
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_link5/visuals/Looks/RubberGray/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/ridgeback_franka/panda_link5/visuals/Looks/RubberGray/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.050, 0.050, 0.050)'


---


### /World/ridgeback_franka/panda_link5/visuals/Looks/RubberLightGray
*  **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_link5/visuals/Looks/RubberLightGray
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_link5/visuals/Looks/RubberLightGray/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/ridgeback_franka/panda_link5/visuals/Looks/RubberLightGray/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')


---


### /World/ridgeback_franka/panda_link5/visuals/Looks/AluminumRough
*  **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_link5/visuals/Looks/AluminumRough
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_link5/visuals/Looks/AluminumRough/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/ridgeback_franka/panda_link5/visuals/Looks/AluminumRough/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.400, 0.400, 0.400)'
           *   'metallic_constant' [float] = '0.399'
           *   'reflection_roughness_constant' [float] = '0.202'


---


### /World/ridgeback_franka/panda_link5/visuals/Looks/rubber_cable
*  **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_link5/visuals/Looks/rubber_cable
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_link5/visuals/Looks/rubber_cable/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/ridgeback_franka/panda_link5/visuals/Looks/rubber_cable/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.050, 0.050, 0.050)'
           *   'metallic_constant' [float] = '0'
           *   'reflection_roughness_constant' [float] = '0.5'
           *   'specular_level' [float] = '0'


---


### /World/ridgeback_franka/panda_link5/visuals/Looks/PlasticWhite
*  **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_link5/visuals/Looks/PlasticWhite
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_link5/visuals/Looks/PlasticWhite/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/ridgeback_franka/panda_link5/visuals/Looks/PlasticWhite/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.700, 0.700, 0.700)'
           *   'reflection_roughness_constant' [float] = '0.18'


---


### /World/ridgeback_franka/panda_link6/visuals/Looks/EmissiveBlue
*  **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_link6/visuals/Looks/EmissiveBlue
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_link6/visuals/Looks/EmissiveBlue/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/ridgeback_franka/panda_link6/visuals/Looks/EmissiveBlue/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(1.000, 1.000, 1.000)'
           *   'emissive_color' [color3f] = '(0.000, 0.100, 1.000)'
           *   'emissive_intensity' [float] = '29000'
           *   'reflection_roughness_constant' [float] = '0.298'


---


### /World/ridgeback_franka/panda_link6/visuals/Looks/PlasticGray
*  **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_link6/visuals/Looks/PlasticGray
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_link6/visuals/Looks/PlasticGray/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/ridgeback_franka/panda_link6/visuals/Looks/PlasticGray/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.100, 0.100, 0.100)'
           *   'reflection_roughness_constant' [float] = '0.292'


---


### /World/ridgeback_franka/panda_link6/visuals/Looks/Aluminum
*  **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_link6/visuals/Looks/Aluminum
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_link6/visuals/Looks/Aluminum/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/ridgeback_franka/panda_link6/visuals/Looks/Aluminum/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.900, 0.900, 0.900)'
           *   'metallic_constant' [float] = '0.899'
           *   'reflection_roughness_constant' [float] = '0.101'


---


### /World/ridgeback_franka/panda_link6/visuals/Looks/PlasticBlack
*  **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_link6/visuals/Looks/PlasticBlack
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_link6/visuals/Looks/PlasticBlack/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/ridgeback_franka/panda_link6/visuals/Looks/PlasticBlack/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.000, 0.000, 0.000)'
           *   'reflection_roughness_constant' [float] = '0'


---


### /World/ridgeback_franka/panda_link6/visuals/Looks/RubberGreen
*  **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_link6/visuals/Looks/RubberGreen
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_link6/visuals/Looks/RubberGreen/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/ridgeback_franka/panda_link6/visuals/Looks/RubberGreen/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.000, 0.500, 0.000)'


---


### /World/ridgeback_franka/panda_link6/visuals/Looks/RubberRed
*  **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_link6/visuals/Looks/RubberRed
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_link6/visuals/Looks/RubberRed/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/ridgeback_franka/panda_link6/visuals/Looks/RubberRed/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.500, 0.000, 0.000)'


---


### /World/ridgeback_franka/panda_link6/visuals/Looks/RubberWhite
*  **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_link6/visuals/Looks/RubberWhite
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_link6/visuals/Looks/RubberWhite/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/ridgeback_franka/panda_link6/visuals/Looks/RubberWhite/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.900, 0.900, 0.900)'


---


### /World/ridgeback_franka/panda_link6/visuals/Looks/RubberGray
*  **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_link6/visuals/Looks/RubberGray
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_link6/visuals/Looks/RubberGray/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/ridgeback_franka/panda_link6/visuals/Looks/RubberGray/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.050, 0.050, 0.050)'


---


### /World/ridgeback_franka/panda_link6/visuals/Looks/RubberLightGray
*  **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_link6/visuals/Looks/RubberLightGray
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_link6/visuals/Looks/RubberLightGray/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/ridgeback_franka/panda_link6/visuals/Looks/RubberLightGray/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')


---


### /World/ridgeback_franka/panda_link6/visuals/Looks/AluminumRough
*  **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_link6/visuals/Looks/AluminumRough
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_link6/visuals/Looks/AluminumRough/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/ridgeback_franka/panda_link6/visuals/Looks/AluminumRough/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.400, 0.400, 0.400)'
           *   'metallic_constant' [float] = '0.399'
           *   'reflection_roughness_constant' [float] = '0.202'


---


### /World/ridgeback_franka/panda_link6/visuals/Looks/rubber_cable
*  **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_link6/visuals/Looks/rubber_cable
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_link6/visuals/Looks/rubber_cable/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/ridgeback_franka/panda_link6/visuals/Looks/rubber_cable/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.050, 0.050, 0.050)'
           *   'metallic_constant' [float] = '0'
           *   'reflection_roughness_constant' [float] = '0.5'
           *   'specular_level' [float] = '0'


---


### /World/ridgeback_franka/panda_link6/visuals/Looks/PlasticWhite
*  **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_link6/visuals/Looks/PlasticWhite
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_link6/visuals/Looks/PlasticWhite/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/ridgeback_franka/panda_link6/visuals/Looks/PlasticWhite/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.700, 0.700, 0.700)'
           *   'reflection_roughness_constant' [float] = '0.18'


---


### /World/ridgeback_franka/panda_link7/visuals/Looks/EmissiveBlue
*  **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_link7/visuals/Looks/EmissiveBlue
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_link7/visuals/Looks/EmissiveBlue/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/ridgeback_franka/panda_link7/visuals/Looks/EmissiveBlue/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(1.000, 1.000, 1.000)'
           *   'emissive_color' [color3f] = '(0.000, 0.100, 1.000)'
           *   'emissive_intensity' [float] = '29000'
           *   'reflection_roughness_constant' [float] = '0.298'


---


### /World/ridgeback_franka/panda_link7/visuals/Looks/PlasticGray
*  **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_link7/visuals/Looks/PlasticGray
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_link7/visuals/Looks/PlasticGray/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/ridgeback_franka/panda_link7/visuals/Looks/PlasticGray/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.100, 0.100, 0.100)'
           *   'reflection_roughness_constant' [float] = '0.292'


---


### /World/ridgeback_franka/panda_link7/visuals/Looks/Aluminum
*  **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_link7/visuals/Looks/Aluminum
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_link7/visuals/Looks/Aluminum/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/ridgeback_franka/panda_link7/visuals/Looks/Aluminum/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.900, 0.900, 0.900)'
           *   'metallic_constant' [float] = '0.899'
           *   'reflection_roughness_constant' [float] = '0.101'


---


### /World/ridgeback_franka/panda_link7/visuals/Looks/PlasticBlack
*  **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_link7/visuals/Looks/PlasticBlack
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_link7/visuals/Looks/PlasticBlack/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/ridgeback_franka/panda_link7/visuals/Looks/PlasticBlack/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.000, 0.000, 0.000)'
           *   'reflection_roughness_constant' [float] = '0'


---


### /World/ridgeback_franka/panda_link7/visuals/Looks/RubberGreen
*  **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_link7/visuals/Looks/RubberGreen
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_link7/visuals/Looks/RubberGreen/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/ridgeback_franka/panda_link7/visuals/Looks/RubberGreen/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.000, 0.500, 0.000)'


---


### /World/ridgeback_franka/panda_link7/visuals/Looks/RubberRed
*  **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_link7/visuals/Looks/RubberRed
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_link7/visuals/Looks/RubberRed/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/ridgeback_franka/panda_link7/visuals/Looks/RubberRed/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.500, 0.000, 0.000)'


---


### /World/ridgeback_franka/panda_link7/visuals/Looks/RubberWhite
*  **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_link7/visuals/Looks/RubberWhite
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_link7/visuals/Looks/RubberWhite/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/ridgeback_franka/panda_link7/visuals/Looks/RubberWhite/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.900, 0.900, 0.900)'


---


### /World/ridgeback_franka/panda_link7/visuals/Looks/RubberGray
*  **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_link7/visuals/Looks/RubberGray
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_link7/visuals/Looks/RubberGray/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/ridgeback_franka/panda_link7/visuals/Looks/RubberGray/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.050, 0.050, 0.050)'


---


### /World/ridgeback_franka/panda_link7/visuals/Looks/RubberLightGray
*  **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_link7/visuals/Looks/RubberLightGray
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_link7/visuals/Looks/RubberLightGray/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/ridgeback_franka/panda_link7/visuals/Looks/RubberLightGray/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')


---


### /World/ridgeback_franka/panda_link7/visuals/Looks/AluminumRough
*  **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_link7/visuals/Looks/AluminumRough
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_link7/visuals/Looks/AluminumRough/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/ridgeback_franka/panda_link7/visuals/Looks/AluminumRough/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.400, 0.400, 0.400)'
           *   'metallic_constant' [float] = '0.399'
           *   'reflection_roughness_constant' [float] = '0.202'


---


### /World/ridgeback_franka/panda_link7/visuals/Looks/rubber_cable
*  **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_link7/visuals/Looks/rubber_cable
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_link7/visuals/Looks/rubber_cable/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/ridgeback_franka/panda_link7/visuals/Looks/rubber_cable/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.050, 0.050, 0.050)'
           *   'metallic_constant' [float] = '0'
           *   'reflection_roughness_constant' [float] = '0.5'
           *   'specular_level' [float] = '0'


---


### /World/ridgeback_franka/panda_link7/visuals/Looks/PlasticWhite
*  **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_link7/visuals/Looks/PlasticWhite
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_link7/visuals/Looks/PlasticWhite/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/ridgeback_franka/panda_link7/visuals/Looks/PlasticWhite/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.700, 0.700, 0.700)'
           *   'reflection_roughness_constant' [float] = '0.18'


---


### /World/ridgeback_franka/panda_hand/visuals/Looks/EmissiveBlue
*  **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_hand/visuals/Looks/EmissiveBlue
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_hand/visuals/Looks/EmissiveBlue/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/ridgeback_franka/panda_hand/visuals/Looks/EmissiveBlue/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(1.000, 1.000, 1.000)'
           *   'emissive_color' [color3f] = '(0.000, 0.100, 1.000)'
           *   'emissive_intensity' [float] = '29000'
           *   'reflection_roughness_constant' [float] = '0.298'


---


### /World/ridgeback_franka/panda_hand/visuals/Looks/PlasticGray
*  **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_hand/visuals/Looks/PlasticGray
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_hand/visuals/Looks/PlasticGray/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/ridgeback_franka/panda_hand/visuals/Looks/PlasticGray/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.100, 0.100, 0.100)'
           *   'reflection_roughness_constant' [float] = '0.292'


---


### /World/ridgeback_franka/panda_hand/visuals/Looks/Aluminum
*  **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_hand/visuals/Looks/Aluminum
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_hand/visuals/Looks/Aluminum/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/ridgeback_franka/panda_hand/visuals/Looks/Aluminum/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.900, 0.900, 0.900)'
           *   'metallic_constant' [float] = '0.899'
           *   'reflection_roughness_constant' [float] = '0.101'


---


### /World/ridgeback_franka/panda_hand/visuals/Looks/PlasticBlack
*  **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_hand/visuals/Looks/PlasticBlack
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_hand/visuals/Looks/PlasticBlack/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/ridgeback_franka/panda_hand/visuals/Looks/PlasticBlack/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.000, 0.000, 0.000)'
           *   'reflection_roughness_constant' [float] = '0'


---


### /World/ridgeback_franka/panda_hand/visuals/Looks/RubberGreen
*  **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_hand/visuals/Looks/RubberGreen
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_hand/visuals/Looks/RubberGreen/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/ridgeback_franka/panda_hand/visuals/Looks/RubberGreen/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.000, 0.500, 0.000)'


---


### /World/ridgeback_franka/panda_hand/visuals/Looks/RubberRed
*  **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_hand/visuals/Looks/RubberRed
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_hand/visuals/Looks/RubberRed/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/ridgeback_franka/panda_hand/visuals/Looks/RubberRed/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.500, 0.000, 0.000)'


---


### /World/ridgeback_franka/panda_hand/visuals/Looks/RubberWhite
*  **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_hand/visuals/Looks/RubberWhite
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_hand/visuals/Looks/RubberWhite/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/ridgeback_franka/panda_hand/visuals/Looks/RubberWhite/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.900, 0.900, 0.900)'


---


### /World/ridgeback_franka/panda_hand/visuals/Looks/RubberGray
*  **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_hand/visuals/Looks/RubberGray
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_hand/visuals/Looks/RubberGray/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/ridgeback_franka/panda_hand/visuals/Looks/RubberGray/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.050, 0.050, 0.050)'


---


### /World/ridgeback_franka/panda_hand/visuals/Looks/RubberLightGray
*  **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_hand/visuals/Looks/RubberLightGray
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_hand/visuals/Looks/RubberLightGray/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/ridgeback_franka/panda_hand/visuals/Looks/RubberLightGray/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')


---


### /World/ridgeback_franka/panda_hand/visuals/Looks/AluminumRough
*  **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_hand/visuals/Looks/AluminumRough
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_hand/visuals/Looks/AluminumRough/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/ridgeback_franka/panda_hand/visuals/Looks/AluminumRough/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.400, 0.400, 0.400)'
           *   'metallic_constant' [float] = '0.399'
           *   'reflection_roughness_constant' [float] = '0.202'


---


### /World/ridgeback_franka/panda_hand/visuals/Looks/rubber_cable
*  **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_hand/visuals/Looks/rubber_cable
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_hand/visuals/Looks/rubber_cable/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/ridgeback_franka/panda_hand/visuals/Looks/rubber_cable/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.050, 0.050, 0.050)'
           *   'metallic_constant' [float] = '0'
           *   'reflection_roughness_constant' [float] = '0.5'
           *   'specular_level' [float] = '0'


---


### /World/ridgeback_franka/panda_hand/visuals/Looks/PlasticWhite
*  **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_hand/visuals/Looks/PlasticWhite
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_hand/visuals/Looks/PlasticWhite/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/ridgeback_franka/panda_hand/visuals/Looks/PlasticWhite/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.700, 0.700, 0.700)'
           *   'reflection_roughness_constant' [float] = '0.18'


---


### /World/ridgeback_franka/panda_leftfinger/visuals/Looks/EmissiveBlue
*  **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_leftfinger/visuals/Looks/EmissiveBlue
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_leftfinger/visuals/Looks/EmissiveBlue/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/ridgeback_franka/panda_leftfinger/visuals/Looks/EmissiveBlue/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(1.000, 1.000, 1.000)'
           *   'emissive_color' [color3f] = '(0.000, 0.100, 1.000)'
           *   'emissive_intensity' [float] = '29000'
           *   'reflection_roughness_constant' [float] = '0.298'


---


### /World/ridgeback_franka/panda_leftfinger/visuals/Looks/PlasticGray
*  **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_leftfinger/visuals/Looks/PlasticGray
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_leftfinger/visuals/Looks/PlasticGray/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/ridgeback_franka/panda_leftfinger/visuals/Looks/PlasticGray/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.100, 0.100, 0.100)'
           *   'reflection_roughness_constant' [float] = '0.292'


---


### /World/ridgeback_franka/panda_leftfinger/visuals/Looks/Aluminum
*  **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_leftfinger/visuals/Looks/Aluminum
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_leftfinger/visuals/Looks/Aluminum/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/ridgeback_franka/panda_leftfinger/visuals/Looks/Aluminum/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.900, 0.900, 0.900)'
           *   'metallic_constant' [float] = '0.899'
           *   'reflection_roughness_constant' [float] = '0.101'


---


### /World/ridgeback_franka/panda_leftfinger/visuals/Looks/PlasticBlack
*  **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_leftfinger/visuals/Looks/PlasticBlack
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_leftfinger/visuals/Looks/PlasticBlack/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/ridgeback_franka/panda_leftfinger/visuals/Looks/PlasticBlack/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.000, 0.000, 0.000)'
           *   'reflection_roughness_constant' [float] = '0'


---


### /World/ridgeback_franka/panda_leftfinger/visuals/Looks/RubberGreen
*  **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_leftfinger/visuals/Looks/RubberGreen
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_leftfinger/visuals/Looks/RubberGreen/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/ridgeback_franka/panda_leftfinger/visuals/Looks/RubberGreen/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.000, 0.500, 0.000)'


---


### /World/ridgeback_franka/panda_leftfinger/visuals/Looks/RubberRed
*  **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_leftfinger/visuals/Looks/RubberRed
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_leftfinger/visuals/Looks/RubberRed/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/ridgeback_franka/panda_leftfinger/visuals/Looks/RubberRed/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.500, 0.000, 0.000)'


---


### /World/ridgeback_franka/panda_leftfinger/visuals/Looks/RubberWhite
*  **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_leftfinger/visuals/Looks/RubberWhite
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_leftfinger/visuals/Looks/RubberWhite/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/ridgeback_franka/panda_leftfinger/visuals/Looks/RubberWhite/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.900, 0.900, 0.900)'


---


### /World/ridgeback_franka/panda_leftfinger/visuals/Looks/RubberGray
*  **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_leftfinger/visuals/Looks/RubberGray
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_leftfinger/visuals/Looks/RubberGray/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/ridgeback_franka/panda_leftfinger/visuals/Looks/RubberGray/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.050, 0.050, 0.050)'


---


### /World/ridgeback_franka/panda_leftfinger/visuals/Looks/RubberLightGray
*  **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_leftfinger/visuals/Looks/RubberLightGray
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_leftfinger/visuals/Looks/RubberLightGray/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/ridgeback_franka/panda_leftfinger/visuals/Looks/RubberLightGray/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')


---


### /World/ridgeback_franka/panda_leftfinger/visuals/Looks/AluminumRough
*  **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_leftfinger/visuals/Looks/AluminumRough
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_leftfinger/visuals/Looks/AluminumRough/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/ridgeback_franka/panda_leftfinger/visuals/Looks/AluminumRough/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.400, 0.400, 0.400)'
           *   'metallic_constant' [float] = '0.399'
           *   'reflection_roughness_constant' [float] = '0.202'


---


### /World/ridgeback_franka/panda_leftfinger/visuals/Looks/rubber_cable
*  **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_leftfinger/visuals/Looks/rubber_cable
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_leftfinger/visuals/Looks/rubber_cable/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/ridgeback_franka/panda_leftfinger/visuals/Looks/rubber_cable/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.050, 0.050, 0.050)'
           *   'metallic_constant' [float] = '0'
           *   'reflection_roughness_constant' [float] = '0.5'
           *   'specular_level' [float] = '0'


---


### /World/ridgeback_franka/panda_leftfinger/visuals/Looks/PlasticWhite
*  **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_leftfinger/visuals/Looks/PlasticWhite
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_leftfinger/visuals/Looks/PlasticWhite/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/ridgeback_franka/panda_leftfinger/visuals/Looks/PlasticWhite/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.700, 0.700, 0.700)'
           *   'reflection_roughness_constant' [float] = '0.18'


---


### /World/ridgeback_franka/panda_rightfinger/visuals/Looks/EmissiveBlue
*  **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_rightfinger/visuals/Looks/EmissiveBlue
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_rightfinger/visuals/Looks/EmissiveBlue/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/ridgeback_franka/panda_rightfinger/visuals/Looks/EmissiveBlue/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(1.000, 1.000, 1.000)'
           *   'emissive_color' [color3f] = '(0.000, 0.100, 1.000)'
           *   'emissive_intensity' [float] = '29000'
           *   'reflection_roughness_constant' [float] = '0.298'


---


### /World/ridgeback_franka/panda_rightfinger/visuals/Looks/PlasticGray
*  **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_rightfinger/visuals/Looks/PlasticGray
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_rightfinger/visuals/Looks/PlasticGray/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/ridgeback_franka/panda_rightfinger/visuals/Looks/PlasticGray/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.100, 0.100, 0.100)'
           *   'reflection_roughness_constant' [float] = '0.292'


---


### /World/ridgeback_franka/panda_rightfinger/visuals/Looks/Aluminum
*  **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_rightfinger/visuals/Looks/Aluminum
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_rightfinger/visuals/Looks/Aluminum/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/ridgeback_franka/panda_rightfinger/visuals/Looks/Aluminum/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.900, 0.900, 0.900)'
           *   'metallic_constant' [float] = '0.899'
           *   'reflection_roughness_constant' [float] = '0.101'


---


### /World/ridgeback_franka/panda_rightfinger/visuals/Looks/PlasticBlack
*  **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_rightfinger/visuals/Looks/PlasticBlack
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_rightfinger/visuals/Looks/PlasticBlack/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/ridgeback_franka/panda_rightfinger/visuals/Looks/PlasticBlack/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.000, 0.000, 0.000)'
           *   'reflection_roughness_constant' [float] = '0'


---


### /World/ridgeback_franka/panda_rightfinger/visuals/Looks/RubberGreen
*  **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_rightfinger/visuals/Looks/RubberGreen
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_rightfinger/visuals/Looks/RubberGreen/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/ridgeback_franka/panda_rightfinger/visuals/Looks/RubberGreen/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.000, 0.500, 0.000)'


---


### /World/ridgeback_franka/panda_rightfinger/visuals/Looks/RubberRed
*  **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_rightfinger/visuals/Looks/RubberRed
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_rightfinger/visuals/Looks/RubberRed/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/ridgeback_franka/panda_rightfinger/visuals/Looks/RubberRed/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.500, 0.000, 0.000)'


---


### /World/ridgeback_franka/panda_rightfinger/visuals/Looks/RubberWhite
*  **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_rightfinger/visuals/Looks/RubberWhite
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_rightfinger/visuals/Looks/RubberWhite/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/ridgeback_franka/panda_rightfinger/visuals/Looks/RubberWhite/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.900, 0.900, 0.900)'


---


### /World/ridgeback_franka/panda_rightfinger/visuals/Looks/RubberGray
*  **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_rightfinger/visuals/Looks/RubberGray
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_rightfinger/visuals/Looks/RubberGray/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/ridgeback_franka/panda_rightfinger/visuals/Looks/RubberGray/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.050, 0.050, 0.050)'


---


### /World/ridgeback_franka/panda_rightfinger/visuals/Looks/RubberLightGray
*  **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_rightfinger/visuals/Looks/RubberLightGray
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_rightfinger/visuals/Looks/RubberLightGray/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/ridgeback_franka/panda_rightfinger/visuals/Looks/RubberLightGray/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')


---


### /World/ridgeback_franka/panda_rightfinger/visuals/Looks/AluminumRough
*  **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_rightfinger/visuals/Looks/AluminumRough
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_rightfinger/visuals/Looks/AluminumRough/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/ridgeback_franka/panda_rightfinger/visuals/Looks/AluminumRough/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.400, 0.400, 0.400)'
           *   'metallic_constant' [float] = '0.399'
           *   'reflection_roughness_constant' [float] = '0.202'


---


### /World/ridgeback_franka/panda_rightfinger/visuals/Looks/rubber_cable
*  **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_rightfinger/visuals/Looks/rubber_cable
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_rightfinger/visuals/Looks/rubber_cable/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/ridgeback_franka/panda_rightfinger/visuals/Looks/rubber_cable/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.050, 0.050, 0.050)'
           *   'metallic_constant' [float] = '0'
           *   'reflection_roughness_constant' [float] = '0.5'
           *   'specular_level' [float] = '0'


---


### /World/ridgeback_franka/panda_rightfinger/visuals/Looks/PlasticWhite
*  **Prim路径 (Prim Path):**/World/ridgeback_franka/panda_rightfinger/visuals/Looks/PlasticWhite
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/ridgeback_franka/panda_rightfinger/visuals/Looks/PlasticWhite/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/ridgeback_franka/panda_rightfinger/visuals/Looks/PlasticWhite/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.700, 0.700, 0.700)'
           *   'reflection_roughness_constant' [float] = '0.18'


---


### /World/ridgeback_franka/Looks/material_black
*  **Prim路径 (Prim Path):**/World/ridgeback_franka/Looks/material_black
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/ridgeback_franka/Looks/material_black/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/ridgeback_franka/Looks/material_black/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_tint' [color3f] = '(0.194, 0.194, 0.194)'
           *   'diffuse_color_constant' [color3f] = '(0.150, 0.150, 0.150)'


---


### /World/ridgeback_franka/Looks/material_dark_grey
*  **Prim路径 (Prim Path):**/World/ridgeback_franka/Looks/material_dark_grey
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/ridgeback_franka/Looks/material_dark_grey/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/ridgeback_franka/Looks/material_dark_grey/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.200, 0.200, 0.200)'


---


### /World/ridgeback_franka/Looks/material_grasp_loc_color
*  **Prim路径 (Prim Path):**/World/ridgeback_franka/Looks/material_grasp_loc_color
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/ridgeback_franka/Looks/material_grasp_loc_color/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/ridgeback_franka/Looks/material_grasp_loc_color/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.900, 0.000, 0.000)'


---


### /World/ridgeback_franka/Looks/material_light_grey
*  **Prim路径 (Prim Path):**/World/ridgeback_franka/Looks/material_light_grey
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/ridgeback_franka/Looks/material_light_grey/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/ridgeback_franka/Looks/material_light_grey/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.400, 0.400, 0.400)'


---


### /World/ridgeback_franka/Looks/material_panda_white
*  **Prim路径 (Prim Path):**/World/ridgeback_franka/Looks/material_panda_white
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/ridgeback_franka/Looks/material_panda_white/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/ridgeback_franka/Looks/material_panda_white/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.900, 0.900, 0.900)'


---


### /World/ridgeback_franka/Looks/material_red
*  **Prim路径 (Prim Path):**/World/ridgeback_franka/Looks/material_red
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/ridgeback_franka/Looks/material_red/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/ridgeback_franka/Looks/material_red/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.800, 0.000, 0.000)'


---


### /World/ridgeback_franka/Looks/material_white
*  **Prim路径 (Prim Path):**/World/ridgeback_franka/Looks/material_white
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/ridgeback_franka/Looks/material_white/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/ridgeback_franka/Looks/material_white/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.900, 0.900, 0.900)'


---


### /World/ridgeback_franka/Looks/material_yellow
*  **Prim路径 (Prim Path):**/World/ridgeback_franka/Looks/material_yellow
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/ridgeback_franka/Looks/material_yellow/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/ridgeback_franka/Looks/material_yellow/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_tint' [color3f] = '(0.679, 0.679, 0.679)'
           *   'diffuse_color_constant' [color3f] = '(0.800, 0.800, 0.000)'


---


### /World/ridgeback_franka/Looks/material_Face636_001
*  **Prim路径 (Prim Path):**/World/ridgeback_franka/Looks/material_Face636_001
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/ridgeback_franka/Looks/material_Face636_001/Shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/ridgeback_franka/Looks/material_Face636_001/Shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.902, 0.922, 0.929)'
           *   'emissive_color' [color3f] = '(0.000, 0.000, 0.000)'


---


### /World/ridgeback_franka/Looks/material_Part__Feature017_001
*  **Prim路径 (Prim Path):**/World/ridgeback_franka/Looks/material_Part__Feature017_001
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/ridgeback_franka/Looks/material_Part__Feature017_001/Shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/ridgeback_franka/Looks/material_Part__Feature017_001/Shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(1.000, 1.000, 1.000)'
           *   'emissive_color' [color3f] = '(0.000, 0.000, 0.000)'


---


### /World/ridgeback_franka/Looks/material_Part__Feature019_001
*  **Prim路径 (Prim Path):**/World/ridgeback_franka/Looks/material_Part__Feature019_001
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/ridgeback_franka/Looks/material_Part__Feature019_001/Shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/ridgeback_franka/Looks/material_Part__Feature019_001/Shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(1.000, 1.000, 1.000)'
           *   'emissive_color' [color3f] = '(0.000, 0.000, 0.000)'


---


### /World/ridgeback_franka/Looks/material_Part__Feature023_001
*  **Prim路径 (Prim Path):**/World/ridgeback_franka/Looks/material_Part__Feature023_001
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/ridgeback_franka/Looks/material_Part__Feature023_001/Shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/ridgeback_franka/Looks/material_Part__Feature023_001/Shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.251, 0.251, 0.251)'
           *   'emissive_color' [color3f] = '(0.000, 0.000, 0.000)'


---


### /World/ridgeback_franka/Looks/material_Part__Feature_001
*  **Prim路径 (Prim Path):**/World/ridgeback_franka/Looks/material_Part__Feature_001
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/ridgeback_franka/Looks/material_Part__Feature_001/Shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/ridgeback_franka/Looks/material_Part__Feature_001/Shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(1.000, 1.000, 1.000)'
           *   'emissive_color' [color3f] = '(0.000, 0.000, 0.000)'


---


### /World/ridgeback_franka/Looks/material_Part__Feature024
*  **Prim路径 (Prim Path):**/World/ridgeback_franka/Looks/material_Part__Feature024
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/ridgeback_franka/Looks/material_Part__Feature024/Shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/ridgeback_franka/Looks/material_Part__Feature024/Shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(1.000, 1.000, 1.000)'
           *   'emissive_color' [color3f] = '(0.000, 0.000, 0.000)'


---


### /World/ridgeback_franka/Looks/material_Part__Feature001_010_001_002
*  **Prim路径 (Prim Path):**/World/ridgeback_franka/Looks/material_Part__Feature001_010_001_002
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/ridgeback_franka/Looks/material_Part__Feature001_010_001_002/Shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/ridgeback_franka/Looks/material_Part__Feature001_010_001_002/Shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(1.000, 1.000, 1.000)'
           *   'emissive_color' [color3f] = '(0.000, 0.000, 0.000)'


---


### /World/ridgeback_franka/Looks/material_Part__Feature_001_001_001_002
*  **Prim路径 (Prim Path):**/World/ridgeback_franka/Looks/material_Part__Feature_001_001_001_002
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/ridgeback_franka/Looks/material_Part__Feature_001_001_001_002/Shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/ridgeback_franka/Looks/material_Part__Feature_001_001_001_002/Shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.251, 0.251, 0.251)'
           *   'emissive_color' [color3f] = '(0.000, 0.000, 0.000)'


---


### /World/ridgeback_franka/Looks/material_Part__Feature001_001_003_001
*  **Prim路径 (Prim Path):**/World/ridgeback_franka/Looks/material_Part__Feature001_001_003_001
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/ridgeback_franka/Looks/material_Part__Feature001_001_003_001/Shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/ridgeback_franka/Looks/material_Part__Feature001_001_003_001/Shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(1.000, 1.000, 1.000)'
           *   'emissive_color' [color3f] = '(0.000, 0.000, 0.000)'


---


### /World/ridgeback_franka/Looks/material_Part__Feature002_001_003_001
*  **Prim路径 (Prim Path):**/World/ridgeback_franka/Looks/material_Part__Feature002_001_003_001
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/ridgeback_franka/Looks/material_Part__Feature002_001_003_001/Shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/ridgeback_franka/Looks/material_Part__Feature002_001_003_001/Shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.251, 0.251, 0.251)'
           *   'emissive_color' [color3f] = '(0.000, 0.000, 0.000)'


---


### /World/ridgeback_franka/Looks/material_Part__Feature_002_004_003
*  **Prim路径 (Prim Path):**/World/ridgeback_franka/Looks/material_Part__Feature_002_004_003
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/ridgeback_franka/Looks/material_Part__Feature_002_004_003/Shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/ridgeback_franka/Looks/material_Part__Feature_002_004_003/Shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(1.000, 1.000, 1.000)'
           *   'emissive_color' [color3f] = '(0.000, 0.000, 0.000)'


---


### /World/ridgeback_franka/Looks/material_Shell001_001_001_003
*  **Prim路径 (Prim Path):**/World/ridgeback_franka/Looks/material_Shell001_001_001_003
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/ridgeback_franka/Looks/material_Shell001_001_001_003/Shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/ridgeback_franka/Looks/material_Shell001_001_001_003/Shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.250, 0.250, 0.250)'
           *   'emissive_color' [color3f] = '(0.000, 0.000, 0.000)'


---


### /World/ridgeback_franka/Looks/material_Face064_002_001_002_001
*  **Prim路径 (Prim Path):**/World/ridgeback_franka/Looks/material_Face064_002_001_002_001
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/ridgeback_franka/Looks/material_Face064_002_001_002_001/Shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/ridgeback_franka/Looks/material_Face064_002_001_002_001/Shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(1.000, 0.000, 0.000)'
           *   'emissive_color' [color3f] = '(0.000, 0.000, 0.000)'


---


### /World/ridgeback_franka/Looks/material_Face065_002_001_002_001
*  **Prim路径 (Prim Path):**/World/ridgeback_franka/Looks/material_Face065_002_001_002_001
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/ridgeback_franka/Looks/material_Face065_002_001_002_001/Shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/ridgeback_franka/Looks/material_Face065_002_001_002_001/Shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.000, 1.000, 0.000)'
           *   'emissive_color' [color3f] = '(0.000, 0.000, 0.000)'


---


### /World/ridgeback_franka/Looks/material_Face374_002_001_002_001
*  **Prim路径 (Prim Path):**/World/ridgeback_franka/Looks/material_Face374_002_001_002_001
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/ridgeback_franka/Looks/material_Face374_002_001_002_001/Shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/ridgeback_franka/Looks/material_Face374_002_001_002_001/Shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(1.000, 1.000, 1.000)'
           *   'emissive_color' [color3f] = '(0.000, 0.000, 0.000)'


---


### /World/ridgeback_franka/Looks/material_Face539_002_001_002_001
*  **Prim路径 (Prim Path):**/World/ridgeback_franka/Looks/material_Face539_002_001_002_001
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/ridgeback_franka/Looks/material_Face539_002_001_002_001/Shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/ridgeback_franka/Looks/material_Face539_002_001_002_001/Shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.251, 0.251, 0.251)'
           *   'emissive_color' [color3f] = '(0.000, 0.000, 0.000)'


---


### /World/ridgeback_franka/Looks/material_Shell006_003_002_001
*  **Prim路径 (Prim Path):**/World/ridgeback_franka/Looks/material_Shell006_003_002_001
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/ridgeback_franka/Looks/material_Shell006_003_002_001/Shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/ridgeback_franka/Looks/material_Shell006_003_002_001/Shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.902, 0.922, 0.929)'
           *   'emissive_color' [color3f] = '(0.000, 0.000, 0.000)'


---


### /World/ridgeback_franka/Looks/material_Shell007_002_002_001
*  **Prim路径 (Prim Path):**/World/ridgeback_franka/Looks/material_Shell007_002_002_001
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/ridgeback_franka/Looks/material_Shell007_002_002_001/Shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/ridgeback_franka/Looks/material_Shell007_002_002_001/Shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.250, 0.250, 0.250)'
           *   'emissive_color' [color3f] = '(0.000, 0.000, 0.000)'


---


### /World/ridgeback_franka/Looks/material_Union001_001_001_002_001
*  **Prim路径 (Prim Path):**/World/ridgeback_franka/Looks/material_Union001_001_001_002_001
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/ridgeback_franka/Looks/material_Union001_001_001_002_001/Shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/ridgeback_franka/Looks/material_Union001_001_001_002_001/Shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.039, 0.541, 0.780)'
           *   'emissive_color' [color3f] = '(0.000, 0.000, 0.000)'


---


### /World/ridgeback_franka/Looks/material_Part__Mirroring001_004_002
*  **Prim路径 (Prim Path):**/World/ridgeback_franka/Looks/material_Part__Mirroring001_004_002
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/ridgeback_franka/Looks/material_Part__Mirroring001_004_002/Shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/ridgeback_franka/Looks/material_Part__Mirroring001_004_002/Shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.251, 0.251, 0.251)'
           *   'emissive_color' [color3f] = '(0.000, 0.000, 0.000)'


---


### /World/ridgeback_franka/Looks/material_Part__Mirroring002_004_001
*  **Prim路径 (Prim Path):**/World/ridgeback_franka/Looks/material_Part__Mirroring002_004_001
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/ridgeback_franka/Looks/material_Part__Mirroring002_004_001/Shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/ridgeback_franka/Looks/material_Part__Mirroring002_004_001/Shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.251, 0.251, 0.251)'
           *   'emissive_color' [color3f] = '(0.000, 0.000, 0.000)'


---


### /World/ridgeback_franka/Looks/material_Part__Mirroring004_004_002
*  **Prim路径 (Prim Path):**/World/ridgeback_franka/Looks/material_Part__Mirroring004_004_002
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/ridgeback_franka/Looks/material_Part__Mirroring004_004_002/Shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/ridgeback_franka/Looks/material_Part__Mirroring004_004_002/Shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(1.000, 1.000, 1.000)'
           *   'emissive_color' [color3f] = '(0.000, 0.000, 0.000)'


---


### /World/ridgeback_franka/Looks/material_Part__Mirroring_004_001
*  **Prim路径 (Prim Path):**/World/ridgeback_franka/Looks/material_Part__Mirroring_004_001
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/ridgeback_franka/Looks/material_Part__Mirroring_004_001/Shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/ridgeback_franka/Looks/material_Part__Mirroring_004_001/Shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.898, 0.918, 0.929)'
           *   'emissive_color' [color3f] = '(0.000, 0.000, 0.000)'


---


### /World/ridgeback_franka/Looks/material_Part__Feature001_008_005
*  **Prim路径 (Prim Path):**/World/ridgeback_franka/Looks/material_Part__Feature001_008_005
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/ridgeback_franka/Looks/material_Part__Feature001_008_005/Shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/ridgeback_franka/Looks/material_Part__Feature001_008_005/Shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.251, 0.251, 0.251)'
           *   'emissive_color' [color3f] = '(0.000, 0.000, 0.000)'


---


### /World/ridgeback_franka/Looks/material_Part__Feature002_005_005
*  **Prim路径 (Prim Path):**/World/ridgeback_franka/Looks/material_Part__Feature002_005_005
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/ridgeback_franka/Looks/material_Part__Feature002_005_005/Shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/ridgeback_franka/Looks/material_Part__Feature002_005_005/Shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.902, 0.922, 0.929)'
           *   'emissive_color' [color3f] = '(0.000, 0.000, 0.000)'


---


### /World/ridgeback_franka/Looks/material_Part__Feature005_001_005
*  **Prim路径 (Prim Path):**/World/ridgeback_franka/Looks/material_Part__Feature005_001_005
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/ridgeback_franka/Looks/material_Part__Feature005_001_005/Shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/ridgeback_franka/Looks/material_Part__Feature005_001_005/Shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(1.000, 1.000, 1.000)'
           *   'emissive_color' [color3f] = '(0.000, 0.000, 0.000)'


---


### /World/ridgeback_franka/Looks/material_Part__Feature_009_005
*  **Prim路径 (Prim Path):**/World/ridgeback_franka/Looks/material_Part__Feature_009_005
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/ridgeback_franka/Looks/material_Part__Feature_009_005/Shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/ridgeback_franka/Looks/material_Part__Feature_009_005/Shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.251, 0.251, 0.251)'
           *   'emissive_color' [color3f] = '(0.000, 0.000, 0.000)'


---


### /World/ridgeback_franka/Looks/material_Part__Feature001_006
*  **Prim路径 (Prim Path):**/World/ridgeback_franka/Looks/material_Part__Feature001_006
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/ridgeback_franka/Looks/material_Part__Feature001_006/Shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/ridgeback_franka/Looks/material_Part__Feature001_006/Shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.902, 0.922, 0.929)'
           *   'emissive_color' [color3f] = '(0.000, 0.000, 0.000)'


---


### /World/ridgeback_franka/Looks/material_Part__Feature_007
*  **Prim路径 (Prim Path):**/World/ridgeback_franka/Looks/material_Part__Feature_007
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/ridgeback_franka/Looks/material_Part__Feature_007/Shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/ridgeback_franka/Looks/material_Part__Feature_007/Shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.251, 0.251, 0.251)'
           *   'emissive_color' [color3f] = '(0.000, 0.000, 0.000)'


---
