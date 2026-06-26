# USDA场景描述文档:assembly.usda

## 1.场景元数据(Scene Metadata)
*  **USDA文件路径(USDA File Path):**`/media/simple/another_Documents/isaacsim_assets/scenedata/assembly.usda`
*  **默认Prim (Default Prim):**'World'
*  **单位与坐标系 (Units & Coordinate System):**
   *   **米(Meters Per Unit):**1.0
   *   **Up Axis:**Z
* **场景描述(Scene Describe):** 该工业场景呈现为一个高度规整、模块化的自动化装配作业单元，整个车间采用极简的空间格局规划，地面呈均匀的浅灰色，视野开阔且无杂物堆积，体现了工业4.0时代对作业环境清洁度与逻辑性的严苛要求。车间的核心区域由一条横贯画面的黑色长程输送线构成，该输送装置采用高架式设计，通过一系列银灰色的“H”型支撑腿稳固支撑，输送带表面分布着等间距的横向挡板，用于精确分隔和定位在制品。紧邻输送线的一侧，对称排布着两台大型白色的六轴工业机器人，它们分别安装在独立的矩形白色工作站基座上，机械臂处于待命或作业姿态，其末端执行器指向输送带上方，暗示着它们负责对流水线上的部件进行抓取、装配或检测。这两个机器人站台之间以及下方配备了白色的模块化控制柜或储物单元，形成了一个集中的工艺处理中心。在输送线前方的开阔区域，布置了一套先进的柔性物流系统，由多台自动导引运输车（AGV）或自主移动机器人（AMR）组成。其中，三台醒目的红色扁平化移动平台各自承载着一个淡蓝色的镂空塑料周转筐，这些筐内可能装载着待装配的零部件或已完成的半成品，它们分布在车间平面的不同位置，呈现出动态运输的路径布局。除此之外，现场还部署了一台黑色的大型移动作业机器人，其底盘厚实并贴有醒目的黄色安全警示标识，该机器人顶部集成了一个小型白色的协作机器人手臂，正处于与其中一个红色载物平台或中央工作站进行交互的位置，这种“复合型机器人”的设计极大提升了物料转运与工位对接的智能化水平。整体来看，该装配区的规划遵循了直线型生产流与网格化物流相结合的原则，设备排布紧凑且预留了充足的机器人运行包络空间与移动机器人行驶路径。这种由固定式输送线作为生产骨干，配合多台灵活移动机器人进行物料接驳的布局方式，充分展示了现代工厂追求高柔性、高效率以及无人化作业的规划逻辑。所有工业设备——从复杂的六轴机械臂到精密的移动平台，再到基础的输送装置与周转容器——在空间上形成了互联互通的有机整体，各司其职且相互协作，共同构成了一个闭环的自动化生产生态系统。
* **设备数量(Device Number):**
  * **Scene: 1**
  * **IndustrialRobot: 3**
  * **Workbench: 3**
  * **Conveyor: 1**
  * **AGV: 3**
  * **Forklift: 0**
  * **Box: 3**
  * **Rack: 0**
  * **Pallet: 0**
  * **Part: 11**
  * **Decoration: 0**

## 2.场景对象层级(Scene Hierarchy)
*   World (Xform)
    *   Factory (Xform)
        *   Materials (Scope)
            *   material_4 (Material)
                *   pbr_shader (Shader)
                *   uvset0 (Shader)
                *   tex_base (Shader)
            *   material_2 (Material)
                *   pbr_shader (Shader)
                *   uvset0 (Shader)
                *   tex_base (Shader)
            *   Structure (Material)
                *   pbr_shader (Shader)
            *   material (Material)
                *   pbr_shader (Shader)
            *   Long_Walls (Material)
                *   pbr_shader (Shader)
            *   Wall_Horizon (Material)
                *   pbr_shader (Shader)
            *   Walls (Material)
                *   pbr_shader (Shader)
            *   Red_Lamp (Material)
                *   pbr_shader (Shader)
            *   Grey (Material)
                *   pbr_shader (Shader)
            *   Chris_Shirt (Material)
                *   pbr_shader (Shader)
            *   Chris_Shoe (Material)
                *   pbr_shader (Shader)
            *   Chris_Skin (Material)
                *   pbr_shader (Shader)
            *   Chris_Shoe_Sole (Material)
                *   pbr_shader (Shader)
            *   Chris_Hair (Material)
                *   pbr_shader (Shader)
            *   Chris_Pants (Material)
                *   pbr_shader (Shader)
        *   Meshes (Xform)
            *   Sketchfab_model (Xform)
                *   Collada_visual_scene_group (Xform)
                    *   SketchUp (Xform)
                        *   Material2 (Xform)
                            *   Material2 (Mesh)
                        *   Material2_1 (Xform)
                        *   Material2_2 (Xform)
                            *   Material2 (Mesh)
                        *   Material2_3 (Xform)
                            *   Material2 (Mesh)
                        *   Material2_4 (Xform)
                            *   Material2 (Mesh)
                        *   Material2_5 (Xform)
                            *   Material2 (Mesh)
                        *   Material2_6 (Xform)
                            *   Material2 (Mesh)
                        *   Material2_7 (Xform)
                            *   Material2 (Mesh)
                        *   Material2_8 (Xform)
                            *   Material2 (Mesh)
                        *   Material3 (Xform)
                            *   Material3 (Mesh)
                        *   Material3_1 (Xform)
                            *   Material3 (Mesh)
                        *   Material2_9 (Xform)
        *   GroundPlane (Xform)
            *   CollisionMesh (Mesh)
            *   CollisionPlane (Plane)
    *   Conveyor_Belt (Xform)
        *   Materials (Scope)
            *   Material_0 (Material)
                *   pbr_shader (Shader)
                *   uvset0 (Shader)
                *   tex_base (Shader)
        *   Meshes (Xform)
            *   Sketchfab_model (Xform)
                *   _aaef2bbe46a4470bc765b4ce24a8c4c_fbx (Xform)
                    *   RootNode (Xform)
                        *   Cylinder001 (Xform)
                            *   Cylinder001_Material__0_0 (Xform)
                                *   Cylinder001_Material__0_0 (Mesh)
    *   Workbench_2 (Xform)
        *   Materials (Scope)
            *   Scratched_wood (Material)
                *   pbr_shader (Shader)
            *   Wood_144 (Material)
                *   pbr_shader (Shader)
            *   Blueprint_Grid (Material)
                *   pbr_shader (Shader)
        *   Meshes (Xform)
            *   Sketchfab_model (Xform)
                *   c32e2987487143319e4b2f288b75227a_fbx (Xform)
                    *   RootNode (Xform)
                        *   Cube (Xform)
                            *   Cube_Scratched_wood_0 (Xform)
                                *   Cube_Scratched_wood_0 (Mesh)
                        *   Cube_001 (Xform)
                            *   Cube_001_Scratched_wood_0 (Xform)
                                *   Cube_001_Scratched_wood_0 (Mesh)
                        *   Cube_002 (Xform)
                            *   Cube_002_Scratched_wood_0 (Xform)
                                *   Cube_002_Scratched_wood_0 (Mesh)
                        *   Cube_003 (Xform)
                            *   Cube_003_Scratched_wood_0 (Xform)
                                *   Cube_003_Scratched_wood_0 (Mesh)
                        *   Cube_004 (Xform)
                            *   Cube_004_Scratched_wood_0 (Xform)
                                *   Cube_004_Scratched_wood_0 (Mesh)
                        *   Cube_005 (Xform)
                            *   Cube_005_Scratched_wood_0 (Xform)
                                *   Cube_005_Scratched_wood_0 (Mesh)
                        *   Cube_006 (Xform)
                            *   Cube_006_Rusty_metal_001_0 (Xform)
                                *   Cube_006_Rusty_metal_001_0 (Mesh)
                        *   Cube_007 (Xform)
                            *   Cube_007_Rusty_metal_001_0 (Xform)
                                *   Cube_007_Rusty_metal_001_0 (Mesh)
                        *   Cube_008 (Xform)
                            *   Cube_008_Wood_144_0 (Xform)
                                *   Cube_008_Wood_144_0 (Mesh)
                        *   Cube_009 (Xform)
                            *   Cube_009_Wood_144_0 (Xform)
                                *   Cube_009_Wood_144_0 (Mesh)
                        *   Cube_010 (Xform)
                            *   Cube_010_Wood_144_0 (Xform)
                                *   Cube_010_Wood_144_0 (Mesh)
                        *   Cube_011 (Xform)
                            *   Cube_011_Rusty_metal_002_0 (Xform)
                                *   Cube_011_Rusty_metal_002_0 (Mesh)
                        *   Plane (Xform)
                            *   Plane_Blueprint_Grid_0 (Xform)
                                *   Plane_Blueprint_Grid_0 (Mesh)
    *   part (Xform)
        *   node_68_Size_100_Length_500_SUPPRESSION_C (Xform)
            *   geometry_1 (Mesh)
    *   part_01 (Prim)
    *   part_09 (Prim)
    *   part_08 (Prim)
    *   part_07 (Prim)
    *   part_06 (Prim)
    *   part_05 (Prim)
    *   part_04 (Prim)
    *   part_03 (Prim)
    *   part_02 (Prim)
    *   part_10 (Prim)
    *   model_AGV_4 (Xform)
        *   materials (Scope)
            *   mat_0 (Material)
                *   PBRShader (Shader)
            *   mat_79 (Material)
                *   PBRShader (Shader)
            *   mat_76 (Material)
                *   PBRShader (Shader)
            *   mat_73 (Material)
                *   PBRShader (Shader)
            *   mat_70 (Material)
                *   PBRShader (Shader)
            *   mat_82 (Material)
                *   PBRShader (Shader)
            *   mat_85 (Material)
                *   PBRShader (Shader)
            *   mat_98 (Material)
                *   PBRShader (Shader)
            *   mat_88 (Material)
                *   PBRShader (Shader)
        *   E_wheel_1 (Xform)
            *   E_foreign_wheel_2 (Xform)
                *   P_327ff64b7998a93f (Mesh)
            *   E_inner_wheel_3 (Xform)
                *   P_40ce45c3b59bbd3f (Mesh)
                *   P_8f5f6350cd7bbd3f (Mesh)
            *   RevoluteJoint_AGV_01 (PhysicsRevoluteJoint)
        *   E_wheel_10 (Xform)
            *   E_foreign_wheel_11 (Xform)
                *   P_bd884f301df5953f (Mesh)
            *   E_inner_wheel_12 (Xform)
                *   P_277e4948f501bd3f (Mesh)
                *   P_a8887da197a14d3f (Mesh)
            *   RevoluteJoint_AGV_02 (PhysicsRevoluteJoint)
        *   E_gear_lever_1_13 (Xform)
            *   P_3a72df48d7099491 (Mesh)
            *   RevoluteJoint_AGV_05 (PhysicsRevoluteJoint)
        *   E_gear_lever_2_14 (Xform)
            *   P_7679a97c96bcac91 (Mesh)
            *   RevoluteJoint_AGV_06 (PhysicsRevoluteJoint)
        *   E_gear_lever_3_15 (Xform)
            *   P_c6c272da45f99491 (Mesh)
            *   RevoluteJoint_AGV_07 (PhysicsRevoluteJoint)
        *   E_gear_lever_4_16 (Xform)
            *   P_c876da0232299491 (Mesh)
            *   RevoluteJoint_AGV_08 (PhysicsRevoluteJoint)
        *   E_knob1_17 (Xform)
            *   P_476976e931804491 (Mesh)
            *   RevoluteJoint_AGV_09 (PhysicsRevoluteJoint)
        *   E_body_18 (Xform)
            *   E_3d66MEdi721835_19 (Xform)
                *   P_4b60b3c9a679491 (Mesh)
            *   E_3d66MEdi525195_20 (Xform)
                *   P_7840e056747d3491 (Mesh)
            *   E_3d66MEdi951578_21 (Xform)
                *   P_12e79a59c3df9491 (Mesh)
            *   E_3d66MEdi735037_22 (Xform)
                *   P_848c18f1931f9491 (Mesh)
            *   E_3d66MEdi994952_23 (Xform)
                *   P_b46a3ab87504fc91 (Mesh)
            *   E_3d66MEdi608491_24 (Xform)
                *   P_d8834c3c827f1491 (Mesh)
            *   E_3d66MEdi800988_25 (Xform)
                *   P_cb52a1c0fe52c411 (Mesh)
            *   E_rod_26 (Xform)
                *   E_3d66MEdi175708_27 (Xform)
                    *   P_feeb25b8aaf9491 (Mesh)
                *   E_rod2_28 (Xform)
                    *   P_57ba6a13584e9591 (Mesh)
            *   E_rod1_29 (Xform)
                *   E_rod2_30 (Xform)
                    *   P_2b80bd55ecf4b491 (Mesh)
                *   E_3d66MEdi957657_31 (Xform)
                    *   P_1a44488c7abc2d88 (Mesh)
            *   E_board_32 (Xform)
                *   P_9c46b630540d6d88 (Mesh)
            *   E_board3_33 (Xform)
                *   P_f8bbd68d87076d88 (Mesh)
            *   E_board2_34 (Xform)
                *   P_ede1a0a046576d88 (Mesh)
            *   E_board5_35 (Xform)
                *   P_7b575fced3d36d88 (Mesh)
            *   E_board1_36 (Xform)
                *   P_f101fe623bb86d88 (Mesh)
            *   E_board4_37 (Xform)
                *   P_b5f9bcb2da476d88 (Mesh)
        *   E_wheel_4 (Xform)
            *   E_foreign_wheel_5 (Xform)
                *   P_fd9dc21277d5d73f (Mesh)
            *   E_inner_wheel_6 (Xform)
                *   P_d7ff06612b4cfd3f (Mesh)
                *   P_5e4517ed3a692d3f (Mesh)
            *   RevoluteJoint_AGV_03 (PhysicsRevoluteJoint)
        *   E_wheel_7 (Xform)
            *   E_foreign_wheel_8 (Xform)
                *   P_de9a6fc3b9cebd3f (Mesh)
            *   E_inner_wheel_9 (Xform)
                *   P_fe2ba1f25879bd3f (Mesh)
                *   P_fa9a0746cef3bd3f (Mesh)
            *   RevoluteJoint_AGV_04 (PhysicsRevoluteJoint)
        *   PhysicsMaterial (Material)
        *   PhysicsMaterial_01 (Material)
    *   Plastic_Crate (Xform)
        *   Materials (Scope)
            *   Crate (Material)
                *   pbr_shader (Shader)
                *   uvset0 (Shader)
                *   tex_base (Shader)
                *   tex_metallic (Shader)
                *   tex_roughness (Shader)
                *   tex_normal (Shader)
        *   Meshes (Xform)
            *   Sketchfab_model (Xform)
                *   _04449d6b57f43e4a66c142c8bf4355d_fbx (Xform)
                    *   RootNode (Xform)
                        *   PlasticCrate (Xform)
                            *   PlasticCrate_Crate_0 (Xform)
                                *   PlasticCrate_Crate_0 (Mesh)
    *   model_AGV_05 (Prim)
    *   Plastic_Crate_01 (Prim)
    *   model_AGV_06 (Prim)
    *   Plastic_Crate_02 (Prim)
    *   PedestalWorkbench_A05_01 (Xform)
        *   SM_PedestalWorkbench_A05_Body_01 (Mesh)
            *   M_PedestalWorkbench_A01_Body (GeomSubset)
            *   M_PedestalWorkbench_A01_KeyHole (GeomSubset)
            *   M_PedestalWorkbench_A01_Slides (GeomSubset)
            *   M_PedestalWorkbench_A01_TableTop (GeomSubset)
            *   SM_PedestalWorkbench_A05_DrawerRails01_01 (Mesh)
                *   M_PedestalWorkbench_A01_Slides (GeomSubset)
                *   M_PedestalWorkbench_A01_SlidesBumper (GeomSubset)
                *   SM_PedestalWorkbench_A05_Drawer01_01 (Mesh)
                    *   M_PedestalWorkbench_A01_Body (GeomSubset)
                    *   M_PedestalWorkbench_A01_DrawerDivider (GeomSubset)
                    *   M_PedestalWorkbench_A01_Slides (GeomSubset)
            *   SM_PedestalWorkbench_A05_DrawerRails02_01 (Mesh)
                *   M_PedestalWorkbench_A01_Slides (GeomSubset)
                *   M_PedestalWorkbench_A01_SlidesBumper (GeomSubset)
                *   SM_PedestalWorkbench_A05_Drawer02_01 (Mesh)
                    *   M_PedestalWorkbench_A01_Body (GeomSubset)
                    *   M_PedestalWorkbench_A01_DrawerDivider (GeomSubset)
                    *   M_PedestalWorkbench_A01_Slides (GeomSubset)
            *   SM_PedestalWorkbench_A05_DrawerRails03_01 (Mesh)
                *   M_PedestalWorkbench_A01_Slides (GeomSubset)
                *   M_PedestalWorkbench_A01_SlidesBumper (GeomSubset)
                *   SM_PedestalWorkbench_A05_Drawer03_01 (Mesh)
                    *   M_PedestalWorkbench_A01_Body (GeomSubset)
                    *   M_PedestalWorkbench_A01_DrawerDivider (GeomSubset)
                    *   M_PedestalWorkbench_A01_Slides (GeomSubset)
            *   SM_PedestalWorkbench_A05_DrawerRails04_01 (Mesh)
                *   M_PedestalWorkbench_A01_Slides (GeomSubset)
                *   M_PedestalWorkbench_A01_SlidesBumper (GeomSubset)
                *   SM_PedestalWorkbench_A05_Drawer04_01 (Mesh)
                    *   M_PedestalWorkbench_A01_Body (GeomSubset)
                    *   M_PedestalWorkbench_A01_DrawerDivider (GeomSubset)
                    *   M_PedestalWorkbench_A01_Slides (GeomSubset)
            *   SM_PedestalWorkbench_A05_Door_01 (Mesh)
                *   M_PedestalWorkbench_A01_Body (GeomSubset)
                *   M_PedestalWorkbench_A01_Case (GeomSubset)
                *   M_PedestalWorkbench_A01_KeyHole (GeomSubset)
                *   M_PedestalWorkbench_A01_NutsBoltsLocks (GeomSubset)
        *   Looks (Scope)
            *   Metal_Glossy_A_PedestalWorkbench_A (Material)
                *   Shader (Shader)
            *   Plastic_Black_A_PedestalWorkbench_A (Material)
                *   Shader (Shader)
            *   MetalPainted_DarkGray_Glossy_A_PedestalWorkbench_A (Material)
                *   Shader (Shader)
            *   MetalPainted_LightGray_Glossy_A_PedestalWorkbench_A (Material)
                *   Shader (Shader)
    *   INDUSTRIAL_ROBOTIC_ARM_01 (Xform)
        *   Materials (Scope)
            *   Brass___Polished (Material)
                *   pbr_shader (Shader)
            *   Aluminum___Anodized_Glossy_Grey (Material)
                *   pbr_shader (Shader)
            *   Paint___Enamel_Glossy_Yellow (Material)
                *   pbr_shader (Shader)
            *   Body1__0 (Material)
                *   pbr_shader (Shader)
            *   Steel___Satin (Material)
                *   pbr_shader (Shader)
            *   Paint___Enamel_Glossy_Black (Material)
                *   pbr_shader (Shader)
        *   Meshes (Xform)
            *   Sketchfab_model (Xform)
                *   c87c2a6ebd5447f7ac496076c3c610d3_fbx (Xform)
                    *   RootNode (Xform)
                        *   PDM_INDUSTRIAL_ROBOTIC_ARM_PROJECT_v84 (Xform)
                            *   Component_1_Base_1 (Xform)
                                *   Component_1_Base (Xform)
                                    *   Component2_1 (Xform)
                                        *   Component2 (Xform)
                                            *   Body1 (Xform)
                                                *   Body1_Brass___Polished_0 (Xform)
                                                    *   Body1_Brass___Polished_0 (Mesh)
                                    *   Component24_1 (Xform)
                                        *   Component24 (Xform)
                                            *   Body1 (Xform)
                                                *   Body1_Aluminum___Anodized_Glossy__Grey__0 (Xform)
                                                    *   Body1_Aluminum___Anodized_Glossy__Grey__0 (Mesh)
                                    *   Component25_1 (Xform)
                                        *   Component25 (Xform)
                                            *   Body1 (Xform)
                                                *   Body1_Aluminum___Anodized_Glossy__Grey__0 (Xform)
                                                    *   Body1_Aluminum___Anodized_Glossy__Grey__0 (Mesh)
                                    *   Component26_1 (Xform)
                                        *   Component26 (Xform)
                                            *   Body1 (Xform)
                                                *   Body1_Aluminum___Anodized_Glossy__Grey__0 (Xform)
                                                    *   Body1_Aluminum___Anodized_Glossy__Grey__0 (Mesh)
                                    *   Component27_1 (Xform)
                                        *   Component27 (Xform)
                                            *   Body1 (Xform)
                                                *   Body1_Aluminum___Anodized_Glossy__Grey__0 (Xform)
                                                    *   Body1_Aluminum___Anodized_Glossy__Grey__0 (Mesh)
                                    *   Component28_1 (Xform)
                                        *   Component28 (Xform)
                                            *   Body1 (Xform)
                                                *   Body1_Brass___Polished_0 (Xform)
                                                    *   Body1_Brass___Polished_0 (Mesh)
                            *   Component_2_Jaw_1_1 (Xform)
                                *   Component_2_Jaw_1 (Xform)
                                    *   Component4_1 (Xform)
                                        *   Component4 (Xform)
                                            *   Body1 (Xform)
                                                *   Body1_Aluminum___Anodized_Glossy__Grey__0 (Xform)
                                                    *   Body1_Aluminum___Anodized_Glossy__Grey__0 (Mesh)
                                    *   Component17_1 (Xform)
                                        *   Component17 (Xform)
                                            *   Body1 (Xform)
                                                *   Body1_Brass___Polished_0 (Xform)
                                                    *   Body1_Brass___Polished_0 (Mesh)
                            *   Component_3_Jaw_2_1 (Xform)
                                *   Component_3_Jaw_2 (Xform)
                                    *   Component6_1 (Xform)
                                        *   Component6 (Xform)
                                            *   Body1 (Xform)
                                                *   Body1_Paint___Enamel_Glossy__Yellow__0 (Xform)
                                                    *   Body1_Paint___Enamel_Glossy__Yellow__0 (Mesh)
                                                *   Body1__0 (Xform)
                                                    *   Body1__0 (Mesh)
                                    *   Component29_1 (Xform)
                                        *   Component29 (Xform)
                                            *   Body1 (Xform)
                                                *   Body1_Aluminum___Anodized_Glossy__Grey__0 (Xform)
                                                    *   Body1_Aluminum___Anodized_Glossy__Grey__0 (Mesh)
                                    *   Component30_1 (Xform)
                                        *   Component30 (Xform)
                                            *   Body1 (Xform)
                                                *   Body1_Steel___Satin_0 (Xform)
                                                    *   Body1_Steel___Satin_0 (Mesh)
                                    *   Component31_1 (Xform)
                                        *   Component31 (Xform)
                                            *   Body1 (Xform)
                                                *   Body1_Steel___Satin_0 (Xform)
                                                    *   Body1_Steel___Satin_0 (Mesh)
                                    *   Component32_1 (Xform)
                                        *   Component32 (Xform)
                                            *   Body1 (Xform)
                                                *   Body1_Steel___Satin_0 (Xform)
                                                    *   Body1_Steel___Satin_0 (Mesh)
                                    *   Component33_1 (Xform)
                                        *   Component33 (Xform)
                                            *   Body1 (Xform)
                                                *   Body1_Steel___Satin_0 (Xform)
                                                    *   Body1_Steel___Satin_0 (Mesh)
                                    *   Component34_1 (Xform)
                                        *   Component34 (Xform)
                                            *   Body1 (Xform)
                                                *   Body1_Steel___Satin_0 (Xform)
                                                    *   Body1_Steel___Satin_0 (Mesh)
                                    *   Component35_1 (Xform)
                                        *   Component35 (Xform)
                                            *   Body1 (Xform)
                                                *   Body1_Steel___Satin_0 (Xform)
                                                    *   Body1_Steel___Satin_0 (Mesh)
                                    *   Component36_1 (Xform)
                                        *   Component36 (Xform)
                                            *   Body1 (Xform)
                                                *   Body1_Steel___Satin_0 (Xform)
                                                    *   Body1_Steel___Satin_0 (Mesh)
                                    *   Component37_1 (Xform)
                                        *   Component37 (Xform)
                                            *   Body1 (Xform)
                                                *   Body1_Steel___Satin_0 (Xform)
                                                    *   Body1_Steel___Satin_0 (Mesh)
                                    *   Component38_1 (Xform)
                                        *   Component38 (Xform)
                                            *   Body1 (Xform)
                                                *   Body1_Steel___Satin_0 (Xform)
                                                    *   Body1_Steel___Satin_0 (Mesh)
                                    *   Component39_1 (Xform)
                                        *   Component39 (Xform)
                                            *   Body1 (Xform)
                                                *   Body1_Steel___Satin_0 (Xform)
                                                    *   Body1_Steel___Satin_0 (Mesh)
                                    *   Component40_1 (Xform)
                                        *   Component40 (Xform)
                                            *   Body1 (Xform)
                                                *   Body1_Steel___Satin_0 (Xform)
                                                    *   Body1_Steel___Satin_0 (Mesh)
                                    *   Component41_1 (Xform)
                                        *   Component41 (Xform)
                                            *   Body1 (Xform)
                                                *   Body1_Steel___Satin_0 (Xform)
                                                    *   Body1_Steel___Satin_0 (Mesh)
                                    *   Component42_1 (Xform)
                                        *   Component42 (Xform)
                                            *   Body1 (Xform)
                                                *   Body1_Steel___Satin_0 (Xform)
                                                    *   Body1_Steel___Satin_0 (Mesh)
                            *   Component_4_Jaw_3_1 (Xform)
                                *   Component_4_Jaw_3 (Xform)
                                    *   Component8_1 (Xform)
                                        *   Component8 (Xform)
                                            *   Body1 (Xform)
                                                *   Body1_Brass___Polished_0 (Xform)
                                                    *   Body1_Brass___Polished_0 (Mesh)
                                    *   Component22_1 (Xform)
                                        *   Component22 (Xform)
                                            *   Body1 (Xform)
                                                *   Body1_Brass___Polished_0 (Xform)
                                                    *   Body1_Brass___Polished_0 (Mesh)
                                    *   Component23_1 (Xform)
                                        *   Component23 (Xform)
                                            *   Body1 (Xform)
                                                *   Body1_Brass___Polished_0 (Xform)
                                                    *   Body1_Brass___Polished_0 (Mesh)
                            *   Component_5_Jaw_4_1 (Xform)
                                *   Component_5_Jaw_4 (Xform)
                                    *   Component10_1 (Xform)
                                        *   Component10 (Xform)
                                            *   Body1 (Xform)
                                                *   Body1_Paint___Enamel_Glossy__Black__0 (Xform)
                                                    *   Body1_Paint___Enamel_Glossy__Black__0 (Mesh)
                                                *   Body1__0 (Xform)
                                                    *   Body1__0 (Mesh)
                                    *   Component20_1 (Xform)
                                        *   Component20 (Xform)
                                            *   Body1 (Xform)
                                                *   Body1_Aluminum___Anodized_Glossy__Grey__0 (Xform)
                                                    *   Body1_Aluminum___Anodized_Glossy__Grey__0 (Mesh)
                                    *   Component21_1 (Xform)
                                        *   Component21 (Xform)
                                            *   Body1 (Xform)
                                                *   Body1_Steel___Satin_0 (Xform)
                                                    *   Body1_Steel___Satin_0 (Mesh)
                            *   Component_6_Jaw_5_1 (Xform)
                                *   Component_6_Jaw_5 (Xform)
                                    *   Component12_1 (Xform)
                                        *   Component12 (Xform)
                                            *   Body1 (Xform)
                                                *   Body1_Brass___Polished_0 (Xform)
                                                    *   Body1_Brass___Polished_0 (Mesh)
                                    *   Component18_1 (Xform)
                                        *   Component18 (Xform)
                                            *   Body1 (Xform)
                                                *   Body1_Brass___Polished_0 (Xform)
                                                    *   Body1_Brass___Polished_0 (Mesh)
                                    *   Component19_1 (Xform)
                                        *   Component19 (Xform)
                                            *   Body1 (Xform)
                                                *   Body1_Paint___Enamel_Glossy__Yellow__0 (Xform)
                                                    *   Body1_Paint___Enamel_Glossy__Yellow__0 (Mesh)
                            *   Component_7_Jaw_6_1 (Xform)
                                *   Component_7_Jaw_6 (Xform)
                                    *   Component14_1 (Xform)
                                        *   Component14 (Xform)
                                            *   Body1 (Xform)
                                                *   Body1_Brass___Polished_0 (Xform)
                                                    *   Body1_Brass___Polished_0 (Mesh)
                                    *   Component43_1 (Xform)
                                        *   Component43 (Xform)
                                            *   Body1 (Xform)
                                                *   Body1_Aluminum___Anodized_Glossy__Grey__0 (Xform)
                                                    *   Body1_Aluminum___Anodized_Glossy__Grey__0 (Mesh)
                            *   Component_8_Jaw_7_1 (Xform)
                                *   Component_8_Jaw_7 (Xform)
                                    *   Component16_1 (Xform)
                                        *   Component16 (Xform)
                                            *   Body1 (Xform)
                                                *   Body1_Aluminum___Anodized_Glossy__Grey__0 (Xform)
                                                    *   Body1_Aluminum___Anodized_Glossy__Grey__0 (Mesh)
                                    *   Component16_2 (Xform)
                                        *   Component16 (Xform)
                                            *   Body1 (Xform)
                                                *   Body1_Aluminum___Anodized_Glossy__Grey__0 (Xform)
                                                    *   Body1_Aluminum___Anodized_Glossy__Grey__0 (Mesh)
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
    *   INDUSTRIAL_ROBOTIC_ARM_02 (Prim)
    *   PedestalWorkbench_A05_02 (Prim)
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

### /World/Factory
*  **Prim路径 (Prim Path):**/World/Factory
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '../scene/Factory/Factory.usdc'
*  **世界包围盒 (World BBox):**
   *   Size: '(3501.110, 1990.477, 6653.544)'
   *   Center: '(15.491, 32.688, 9.952)'


---


### /World/Conveyor_Belt
*  **Prim路径 (Prim Path):**/World/Conveyor_Belt
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '../assets/Conveyor_Belt/Conveyor_Belt.usdc'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.799, 4.204, 9.846)'
   *   Center: '(16.241, 28.789, 0.471)'


---


### /World/Workbench_2
*  **Prim路径 (Prim Path):**/World/Workbench_2
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '../assets/Workbench_2/Workbench_2.usdc'
*  **世界包围盒 (World BBox):**
   *   Size: '(200.000, 150.106, 120.478)'
   *   Center: '(14.746, 31.316, 0.712)'


---


### /World/part
*  **Prim路径 (Prim Path):**/World/part
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '../device_data/usdz/Part/xie.usd'
*  **世界包围盒 (World BBox):**
   *   Size: '(50.000, 10.000, 5.000)'
   *   Center: '(16.255, 32.000, 1.017)'


---


### /World/model_AGV_4
*  **Prim路径 (Prim Path):**/World/model_AGV_4
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '../device_data/usdz/AGV/model_AGV_4.usdz'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.639, 0.940, 0.240)'
   *   Center: '(11.488, 34.473, 0.127)'


---


### /World/Plastic_Crate
*  **Prim路径 (Prim Path):**/World/Plastic_Crate
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '../device_data/usdz/Box/Plastic_Crate.usdz'
*  **世界包围盒 (World BBox):**
   *   Size: '(68.986, 38.096, 45.367)'
   *   Center: '(11.554, 34.416, 0.237)'


---


### /World/PedestalWorkbench_A05_01
*  **Prim路径 (Prim Path):**/World/PedestalWorkbench_A05_01
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '../device_data/usdz/Workbench/PedestalWorkbench_A05_01.usdz'
*  **世界包围盒 (World BBox):**
   *   Size: '(152.403, 74.742, 86.064)'
   *   Center: '(14.754, 32.495, 0.430)'


---


### /World/INDUSTRIAL_ROBOTIC_ARM_01
*  **Prim路径 (Prim Path):**/World/INDUSTRIAL_ROBOTIC_ARM_01
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '../device_data/usdz/IndustrialRobot/INDUSTRIAL_ROBOTIC_ARM.usdz'
*  **世界包围盒 (World BBox):**
   *   Size: '(78.095, 126.534, 112.695)'
   *   Center: '(14.791, 32.328, 1.495)'


---


### /World/ridgeback_franka
*  **Prim路径 (Prim Path):**/World/ridgeback_franka
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '../device_data/usdz/IndustrialRobot/ridgeback_franka.usdz'
*  **世界包围盒 (World BBox):**
   *   Size: '(1.543, 0.793, 1.134)'
   *   Center: '(12.137, 31.132, 0.571)'


---


## 4. 材质库 (Material Library)

### /World/Factory/Materials/material_4
*  **Prim路径 (Prim Path):**/World/Factory/Materials/material_4
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/Factory/Materials/material_4/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/Factory/Materials/material_4/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f]
               *   Connected: '/World/Factory/Materials/material_4/tex_base.outputs:rgb' @ '/World/Factory/Materials/material_4/tex_base'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/material_4_baseColor.jpg'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(1.000, 1.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'
       *   '/World/Factory/Materials/material_4/tex_base' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/material_4_baseColor.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
           *   'file' [asset] = '0/material_4_baseColor.jpg'
           *   'st' [float2]
               *   Connected: '/World/Factory/Materials/material_4/uvset0.outputs:result' @ '/World/Factory/Materials/material_4/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/Factory/Materials/material_4/uvset0' (ID: 'UsdPrimvarReader_float2')
       *   Implementation: 'id'


---


### /World/Factory/Materials/material_2
*  **Prim路径 (Prim Path):**/World/Factory/Materials/material_2
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/Factory/Materials/material_2/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/Factory/Materials/material_2/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f]
               *   Connected: '/World/Factory/Materials/material_2/tex_base.outputs:rgb' @ '/World/Factory/Materials/material_2/tex_base'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/material_2_baseColor.jpg'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(1.000, 1.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'
       *   '/World/Factory/Materials/material_2/tex_base' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/material_2_baseColor.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
           *   'file' [asset] = '0/material_2_baseColor.jpg'
           *   'st' [float2]
               *   Connected: '/World/Factory/Materials/material_2/uvset0.outputs:result' @ '/World/Factory/Materials/material_2/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/Factory/Materials/material_2/uvset0' (ID: 'UsdPrimvarReader_float2')
       *   Implementation: 'id'


---


### /World/Factory/Materials/Structure
*  **Prim路径 (Prim Path):**/World/Factory/Materials/Structure
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/Factory/Materials/Structure/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/Factory/Materials/Structure/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.473, 0.511, 0.476)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0.657424'
           *   'normal' [normal3f] = '(1.000, 1.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0'


---


### /World/Factory/Materials/material
*  **Prim路径 (Prim Path):**/World/Factory/Materials/material
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/Factory/Materials/material/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/Factory/Materials/material/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(1.000, 1.000, 1.000)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(1.000, 1.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0.845303'


---


### /World/Factory/Materials/Long_Walls
*  **Prim路径 (Prim Path):**/World/Factory/Materials/Long_Walls
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/Factory/Materials/Long_Walls/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/Factory/Materials/Long_Walls/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.576, 0.576, 0.576)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(1.000, 1.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0.6'


---


### /World/Factory/Materials/Wall_Horizon
*  **Prim路径 (Prim Path):**/World/Factory/Materials/Wall_Horizon
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/Factory/Materials/Wall_Horizon/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/Factory/Materials/Wall_Horizon/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.369, 0.341, 0.349)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(1.000, 1.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0.6'


---


### /World/Factory/Materials/Walls
*  **Prim路径 (Prim Path):**/World/Factory/Materials/Walls
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/Factory/Materials/Walls/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/Factory/Materials/Walls/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.718, 0.718, 0.718)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(1.000, 1.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0.6'


---


### /World/Factory/Materials/Red_Lamp
*  **Prim路径 (Prim Path):**/World/Factory/Materials/Red_Lamp
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/Factory/Materials/Red_Lamp/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/Factory/Materials/Red_Lamp/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'emissiveColor' [color3f] = '(1.000, 1.000, 1.000)'
           *   'metallic' [float] = '0.548333'
           *   'normal' [normal3f] = '(1.000, 1.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/Factory/Materials/Grey
*  **Prim路径 (Prim Path):**/World/Factory/Materials/Grey
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/Factory/Materials/Grey/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/Factory/Materials/Grey/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.686, 0.663, 0.596)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '1'
           *   'normal' [normal3f] = '(1.000, 1.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0'


---


### /World/Factory/Materials/Chris_Shirt
*  **Prim路径 (Prim Path):**/World/Factory/Materials/Chris_Shirt
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/Factory/Materials/Chris_Shirt/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/Factory/Materials/Chris_Shirt/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.157, 0.149, 0.204)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(1.000, 1.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0.6'


---


### /World/Factory/Materials/Chris_Shoe
*  **Prim路径 (Prim Path):**/World/Factory/Materials/Chris_Shoe
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/Factory/Materials/Chris_Shoe/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/Factory/Materials/Chris_Shoe/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.090, 0.086, 0.086)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(1.000, 1.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0.6'


---


### /World/Factory/Materials/Chris_Skin
*  **Prim路径 (Prim Path):**/World/Factory/Materials/Chris_Skin
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/Factory/Materials/Chris_Skin/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/Factory/Materials/Chris_Skin/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.753, 0.643, 0.451)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(1.000, 1.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0.6'


---


### /World/Factory/Materials/Chris_Shoe_Sole
*  **Prim路径 (Prim Path):**/World/Factory/Materials/Chris_Shoe_Sole
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/Factory/Materials/Chris_Shoe_Sole/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/Factory/Materials/Chris_Shoe_Sole/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.557, 0.533, 0.533)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(1.000, 1.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0.6'


---


### /World/Factory/Materials/Chris_Hair
*  **Prim路径 (Prim Path):**/World/Factory/Materials/Chris_Hair
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/Factory/Materials/Chris_Hair/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/Factory/Materials/Chris_Hair/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.278, 0.298, 0.290)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(1.000, 1.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0.6'


---


### /World/Factory/Materials/Chris_Pants
*  **Prim路径 (Prim Path):**/World/Factory/Materials/Chris_Pants
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/Factory/Materials/Chris_Pants/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/Factory/Materials/Chris_Pants/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.439, 0.392, 0.290)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(1.000, 1.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0.6'


---


### /World/Conveyor_Belt/Materials/Material_0
*  **Prim路径 (Prim Path):**/World/Conveyor_Belt/Materials/Material_0
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/Conveyor_Belt/Materials/Material_0/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/Conveyor_Belt/Materials/Material_0/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f]
               *   Connected: '/World/Conveyor_Belt/Materials/Material_0/tex_base.outputs:rgb' @ '/World/Conveyor_Belt/Materials/Material_0/tex_base'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/Material_0_baseColor.jpg'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(1.000, 1.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0.892971'
       *   '/World/Conveyor_Belt/Materials/Material_0/tex_base' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/Material_0_baseColor.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
           *   'file' [asset] = '0/Material_0_baseColor.jpg'
           *   'st' [float2]
               *   Connected: '/World/Conveyor_Belt/Materials/Material_0/uvset0.outputs:result' @ '/World/Conveyor_Belt/Materials/Material_0/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/Conveyor_Belt/Materials/Material_0/uvset0' (ID: 'UsdPrimvarReader_float2')
       *   Implementation: 'id'


---


### /World/Workbench_2/Materials/Scratched_wood
*  **Prim路径 (Prim Path):**/World/Workbench_2/Materials/Scratched_wood
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/Workbench_2/Materials/Scratched_wood/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/Workbench_2/Materials/Scratched_wood/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.800, 0.800, 0.800)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0.821115'


---


### /World/Workbench_2/Materials/Wood_144
*  **Prim路径 (Prim Path):**/World/Workbench_2/Materials/Wood_144
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/Workbench_2/Materials/Wood_144/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/Workbench_2/Materials/Wood_144/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.800, 0.800, 0.800)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0.747018'


---


### /World/Workbench_2/Materials/Blueprint_Grid
*  **Prim路径 (Prim Path):**/World/Workbench_2/Materials/Blueprint_Grid
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/Workbench_2/Materials/Blueprint_Grid/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/Workbench_2/Materials/Blueprint_Grid/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.800, 0.800, 0.800)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/model_AGV_4/materials/mat_0
*  **Prim路径 (Prim Path):**/World/model_AGV_4/materials/mat_0
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/model_AGV_4/materials/mat_0/PBRShader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/model_AGV_4/materials/mat_0/PBRShader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'clearcoat' [float] = '0.05'
           *   'clearcoatRoughness' [float] = '0.05'
           *   'diffuseColor' [color3f] = '(0.939, 0.965, 1.000)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'ior' [float] = '1'
           *   'opacity' [float] = '1'
           *   'roughness' [float] = '0.5'
           *   'specularColor' [color3f] = '(0.000, 0.000, 0.000)'


---


### /World/model_AGV_4/materials/mat_79
*  **Prim路径 (Prim Path):**/World/model_AGV_4/materials/mat_79
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/model_AGV_4/materials/mat_79/PBRShader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/model_AGV_4/materials/mat_79/PBRShader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'clearcoat' [float] = '0.3'
           *   'clearcoatRoughness' [float] = '0.05'
           *   'diffuseColor' [color3f] = '(0.150, 0.000, 0.000)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'ior' [float] = '1'
           *   'metallic' [float] = '0.08'
           *   'opacity' [float] = '1'
           *   'roughness' [float] = '0.3'
           *   'specularColor' [color3f] = '(0.000, 0.000, 0.000)'


---


### /World/model_AGV_4/materials/mat_76
*  **Prim路径 (Prim Path):**/World/model_AGV_4/materials/mat_76
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/model_AGV_4/materials/mat_76/PBRShader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/model_AGV_4/materials/mat_76/PBRShader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'clearcoat' [float] = '0.2'
           *   'clearcoatRoughness' [float] = '0.05'
           *   'diffuseColor' [color3f] = '(0.351, 0.346, 0.346)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'ior' [float] = '1'
           *   'metallic' [float] = '0.4'
           *   'opacity' [float] = '1'
           *   'roughness' [float] = '0.2'
           *   'specularColor' [color3f] = '(0.000, 0.000, 0.000)'


---


### /World/model_AGV_4/materials/mat_73
*  **Prim路径 (Prim Path):**/World/model_AGV_4/materials/mat_73
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/model_AGV_4/materials/mat_73/PBRShader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/model_AGV_4/materials/mat_73/PBRShader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'clearcoat' [float] = '0.2'
           *   'clearcoatRoughness' [float] = '0.05'
           *   'diffuseColor' [color3f] = '(0.319, 0.319, 0.319)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'ior' [float] = '1'
           *   'metallic' [float] = '0.4'
           *   'opacity' [float] = '1'
           *   'roughness' [float] = '0.2'
           *   'specularColor' [color3f] = '(0.000, 0.000, 0.000)'


---


### /World/model_AGV_4/materials/mat_70
*  **Prim路径 (Prim Path):**/World/model_AGV_4/materials/mat_70
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/model_AGV_4/materials/mat_70/PBRShader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/model_AGV_4/materials/mat_70/PBRShader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'clearcoat' [float] = '0.2'
           *   'clearcoatRoughness' [float] = '0.05'
           *   'diffuseColor' [color3f] = '(0.287, 0.287, 0.287)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'ior' [float] = '1'
           *   'metallic' [float] = '0.4'
           *   'opacity' [float] = '1'
           *   'roughness' [float] = '0.2'
           *   'specularColor' [color3f] = '(0.000, 0.000, 0.000)'


---


### /World/model_AGV_4/materials/mat_82
*  **Prim路径 (Prim Path):**/World/model_AGV_4/materials/mat_82
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/model_AGV_4/materials/mat_82/PBRShader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/model_AGV_4/materials/mat_82/PBRShader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'clearcoat' [float] = '0.3'
           *   'clearcoatRoughness' [float] = '0.05'
           *   'diffuseColor' [color3f] = '(0.056, 0.056, 0.056)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'ior' [float] = '1'
           *   'metallic' [float] = '0.15'
           *   'opacity' [float] = '1'
           *   'roughness' [float] = '0.3'
           *   'specularColor' [color3f] = '(0.000, 0.000, 0.000)'


---


### /World/model_AGV_4/materials/mat_85
*  **Prim路径 (Prim Path):**/World/model_AGV_4/materials/mat_85
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/model_AGV_4/materials/mat_85/PBRShader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/model_AGV_4/materials/mat_85/PBRShader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'clearcoat' [float] = '0.05'
           *   'clearcoatRoughness' [float] = '0.05'
           *   'diffuseColor' [color3f] = '(0.002, 0.002, 0.002)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'ior' [float] = '1'
           *   'opacity' [float] = '1'
           *   'roughness' [float] = '0.5'
           *   'specularColor' [color3f] = '(0.000, 0.000, 0.000)'


---


### /World/model_AGV_4/materials/mat_98
*  **Prim路径 (Prim Path):**/World/model_AGV_4/materials/mat_98
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/model_AGV_4/materials/mat_98/PBRShader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/model_AGV_4/materials/mat_98/PBRShader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'clearcoat' [float] = '0.3'
           *   'clearcoatRoughness' [float] = '0.05'
           *   'diffuseColor' [color3f] = '(0.394, 0.000, 0.000)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'ior' [float] = '1'
           *   'metallic' [float] = '0.15'
           *   'opacity' [float] = '1'
           *   'roughness' [float] = '0.3'
           *   'specularColor' [color3f] = '(0.000, 0.000, 0.000)'


---


### /World/model_AGV_4/materials/mat_88
*  **Prim路径 (Prim Path):**/World/model_AGV_4/materials/mat_88
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/model_AGV_4/materials/mat_88/PBRShader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/model_AGV_4/materials/mat_88/PBRShader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'clearcoat' [float] = '0.2'
           *   'clearcoatRoughness' [float] = '0.05'
           *   'diffuseColor' [color3f] = '(0.000, 0.687, 1.000)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'ior' [float] = '1'
           *   'metallic' [float] = '0.15'
           *   'opacity' [float] = '1'
           *   'roughness' [float] = '0.2'
           *   'specularColor' [color3f] = '(0.000, 0.000, 0.000)'


---


### /World/model_AGV_4/PhysicsMaterial
*  **Prim路径 (Prim Path):**/World/model_AGV_4/PhysicsMaterial
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'


---


### /World/model_AGV_4/PhysicsMaterial_01
*  **Prim路径 (Prim Path):**/World/model_AGV_4/PhysicsMaterial_01
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'


---


### /World/Plastic_Crate/Materials/Crate
*  **Prim路径 (Prim Path):**/World/Plastic_Crate/Materials/Crate
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/Plastic_Crate/Materials/Crate/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/Plastic_Crate/Materials/Crate/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f]
               *   Connected: '/World/Plastic_Crate/Materials/Crate/tex_base.outputs:rgb' @ '/World/Plastic_Crate/Materials/Crate/tex_base'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/Crate_baseColor.jpg'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float]
               *   Connected: '/World/Plastic_Crate/Materials/Crate/tex_metallic.outputs:r' @ '/World/Plastic_Crate/Materials/Crate/tex_metallic'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/Crate_metallicRoughness_metal_scale0.jpg'
           *   'normal' [normal3f]
               *   Connected: '/World/Plastic_Crate/Materials/Crate/tex_normal.outputs:rgb' @ '/World/Plastic_Crate/Materials/Crate/tex_normal'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/Crate_normal.jpg'
           *   'occlusion' [float] = '1'
           *   'roughness' [float]
               *   Connected: '/World/Plastic_Crate/Materials/Crate/tex_roughness.outputs:r' @ '/World/Plastic_Crate/Materials/Crate/tex_roughness'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/Crate_metallicRoughness_rough.jpg'
       *   '/World/Plastic_Crate/Materials/Crate/tex_base' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/Crate_baseColor.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
           *   'file' [asset] = '0/Crate_baseColor.jpg'
           *   'st' [float2]
               *   Connected: '/World/Plastic_Crate/Materials/Crate/uvset0.outputs:result' @ '/World/Plastic_Crate/Materials/Crate/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/Plastic_Crate/Materials/Crate/uvset0' (ID: 'UsdPrimvarReader_float2')
       *   Implementation: 'id'
       *   '/World/Plastic_Crate/Materials/Crate/tex_metallic' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/Crate_metallicRoughness_metal_scale0.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(0.000, 0.000, 0.000, 1.000)'
           *   'file' [asset] = '0/Crate_metallicRoughness_metal_scale0.jpg'
           *   'st' [float2]
               *   Connected: '/World/Plastic_Crate/Materials/Crate/uvset0.outputs:result' @ '/World/Plastic_Crate/Materials/Crate/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/Plastic_Crate/Materials/Crate/tex_normal' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/Crate_normal.jpg'
       *   Inputs:
           *   'bias' [float4] = '(-1.000, -1.000, -1.000, -1.000)'
           *   'fallback' [float4] = '(0.000, 0.000, 1.000, 1.000)'
           *   'file' [asset] = '0/Crate_normal.jpg'
           *   'scale' [float4] = '(2.000, 2.000, 2.000, 2.000)'
           *   'st' [float2]
               *   Connected: '/World/Plastic_Crate/Materials/Crate/uvset0.outputs:result' @ '/World/Plastic_Crate/Materials/Crate/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/Plastic_Crate/Materials/Crate/tex_roughness' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/Crate_metallicRoughness_rough.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(1.000, 0.000, 0.000, 1.000)'
           *   'file' [asset] = '0/Crate_metallicRoughness_rough.jpg'
           *   'st' [float2]
               *   Connected: '/World/Plastic_Crate/Materials/Crate/uvset0.outputs:result' @ '/World/Plastic_Crate/Materials/Crate/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'


---


### /World/PedestalWorkbench_A05_01/Looks/Metal_Glossy_A_PedestalWorkbench_A
*  **Prim路径 (Prim Path):**/World/PedestalWorkbench_A05_01/Looks/Metal_Glossy_A_PedestalWorkbench_A
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/PedestalWorkbench_A05_01/Looks/Metal_Glossy_A_PedestalWorkbench_A/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/PedestalWorkbench_A05_01/Looks/Metal_Glossy_A_PedestalWorkbench_A/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] '0/Metal_Glossy_A.mdl' (Sub Id: 'Metal_Glossy_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/device_data/usdz/Workbench/PedestalWorkbench_A05_01.usdz[0/Metal_Glossy_A.mdl]'


---


### /World/PedestalWorkbench_A05_01/Looks/Plastic_Black_A_PedestalWorkbench_A
*  **Prim路径 (Prim Path):**/World/PedestalWorkbench_A05_01/Looks/Plastic_Black_A_PedestalWorkbench_A
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/PedestalWorkbench_A05_01/Looks/Plastic_Black_A_PedestalWorkbench_A/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/PedestalWorkbench_A05_01/Looks/Plastic_Black_A_PedestalWorkbench_A/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] '1/Plastic_Black_A.mdl' (Sub Id: 'Plastic_Black_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/device_data/usdz/Workbench/PedestalWorkbench_A05_01.usdz[1/Plastic_Black_A.mdl]'


---


### /World/PedestalWorkbench_A05_01/Looks/MetalPainted_DarkGray_Glossy_A_PedestalWorkbench_A
*  **Prim路径 (Prim Path):**/World/PedestalWorkbench_A05_01/Looks/MetalPainted_DarkGray_Glossy_A_PedestalWorkbench_A
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface'


---


### /World/PedestalWorkbench_A05_01/Looks/MetalPainted_LightGray_Glossy_A_PedestalWorkbench_A
*  **Prim路径 (Prim Path):**/World/PedestalWorkbench_A05_01/Looks/MetalPainted_LightGray_Glossy_A_PedestalWorkbench_A
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface'


---


### /World/INDUSTRIAL_ROBOTIC_ARM_01/Materials/Brass___Polished
*  **Prim路径 (Prim Path):**/World/INDUSTRIAL_ROBOTIC_ARM_01/Materials/Brass___Polished
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/INDUSTRIAL_ROBOTIC_ARM_01/Materials/Brass___Polished/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/INDUSTRIAL_ROBOTIC_ARM_01/Materials/Brass___Polished/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.953, 0.796, 0.486)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0.957705'


---


### /World/INDUSTRIAL_ROBOTIC_ARM_01/Materials/Aluminum___Anodized_Glossy_Grey
*  **Prim路径 (Prim Path):**/World/INDUSTRIAL_ROBOTIC_ARM_01/Materials/Aluminum___Anodized_Glossy_Grey
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/INDUSTRIAL_ROBOTIC_ARM_01/Materials/Aluminum___Anodized_Glossy_Grey/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/INDUSTRIAL_ROBOTIC_ARM_01/Materials/Aluminum___Anodized_Glossy_Grey/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.537, 0.537, 0.537)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0.957705'


---


### /World/INDUSTRIAL_ROBOTIC_ARM_01/Materials/Paint___Enamel_Glossy_Yellow
*  **Prim路径 (Prim Path):**/World/INDUSTRIAL_ROBOTIC_ARM_01/Materials/Paint___Enamel_Glossy_Yellow
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/INDUSTRIAL_ROBOTIC_ARM_01/Materials/Paint___Enamel_Glossy_Yellow/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/INDUSTRIAL_ROBOTIC_ARM_01/Materials/Paint___Enamel_Glossy_Yellow/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.910, 0.678, 0.137)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0.957705'


---


### /World/INDUSTRIAL_ROBOTIC_ARM_01/Materials/Body1__0
*  **Prim路径 (Prim Path):**/World/INDUSTRIAL_ROBOTIC_ARM_01/Materials/Body1__0
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/INDUSTRIAL_ROBOTIC_ARM_01/Materials/Body1__0/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/INDUSTRIAL_ROBOTIC_ARM_01/Materials/Body1__0/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(1.000, 1.000, 1.000)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0.6'


---


### /World/INDUSTRIAL_ROBOTIC_ARM_01/Materials/Steel___Satin
*  **Prim路径 (Prim Path):**/World/INDUSTRIAL_ROBOTIC_ARM_01/Materials/Steel___Satin
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/INDUSTRIAL_ROBOTIC_ARM_01/Materials/Steel___Satin/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/INDUSTRIAL_ROBOTIC_ARM_01/Materials/Steel___Satin/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.627, 0.627, 0.627)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0.957705'


---


### /World/INDUSTRIAL_ROBOTIC_ARM_01/Materials/Paint___Enamel_Glossy_Black
*  **Prim路径 (Prim Path):**/World/INDUSTRIAL_ROBOTIC_ARM_01/Materials/Paint___Enamel_Glossy_Black
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/INDUSTRIAL_ROBOTIC_ARM_01/Materials/Paint___Enamel_Glossy_Black/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/INDUSTRIAL_ROBOTIC_ARM_01/Materials/Paint___Enamel_Glossy_Black/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.098, 0.098, 0.098)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0.957705'


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
