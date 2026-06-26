# USDA场景描述文档:transport.usda

## 1.场景元数据(Scene Metadata)
*  **USDA文件路径(USDA File Path):**`/media/simple/another_Documents/isaacsim_assets/scenedata/transport.usda`
*  **默认Prim (Default Prim):**'World'
*  **单位与坐标系 (Units & Coordinate System):**
   *   **米(Meters Per Unit):**1.0
   *   **Up Axis:**Z
*  **场景描述(Scene Describe):** 该场景呈现出一个高度秩序化、矩阵式排布的现代化工业转运与自动化分拣中心，整体规划严谨地遵循了“标准化单元并行”的设计原则，展现了一个极具规模感的无人化作业空间。从厂区的空间格局来看，地面铺设了具有大理石质感的深灰色瓷砖，瓷砖表面带有自然分布的浅红色纹理，不仅提升了车间的视觉品质，也为自动化设备的平稳运行提供了极佳的水平基准。整个车间被划分为多个重复的自动化分拣作业集群，这些集群在空间上呈纵向等间距排列，形成了一个强大的物料处理矩阵。核心工业设备由至少四组完全一致的“输送-分拣”单元构成，每一组单元内部都包含两个关键模块：首先是作为物料主脉络的带式输送机，这些输送装置采用了银灰色的精钢架构支撑，支腿呈细长的“H”型分布，其上方安装有黑色的耐磨橡胶传送带。在传送带面上，可以清晰地观察到多个呈等距分布的圆形白色工件，正由输送机向作业端稳步推进。其次是紧邻每一条输送机首端部署的独立分拣基座，该基座采用了醒目的深蓝色箱体式结构，底部配有微型滑轮，暗示其具备一定的位移灵活性。在每一个蓝色基座顶部，均垂直安装了一台修长的白色六轴协作机器人，这些机器人处于统一的待命或抓取姿态，其机械臂线条圆润且关节灵活，专门负责从相邻的输送带上精准提取工件。在设备排布方式上，该场景采用了典型的“线性输送+端点处理”的一对一耦合结构。四组机器人作业站呈直线方阵在车间内铺开，每一组机器人阵列都精准地对应着一条独立的物流输送线。在机器人与输送线之间的空旷地面上，散落分布着多个淡蓝色的镂空塑料周转筐，这些容器被放置在机器人的作业半径内，用于暂存已分类的工件或作为废品收集箱。场景的背景处可见由深褐色金属质感板材构成的防护墙，墙面上带有细密的横向凹槽纹理，为整个自动化区域提供了物理隔离，墙脚处还可见一条醒目的黄色安全警示线，划定了明确的人机作业边界。从整体规划结构分析，该场景巧妙地将“分布式单元”与“标准化模块”深度融合。每一组蓝色基座与白色机械臂的组合都是一个独立的逻辑节点，而多条并行的银灰色输送链则构成了车间的吞吐枢纽。这种重复性的矩阵式布局具有极强的可扩展性，可以根据产线的实际负荷需求进行灵活的模块增减。设备间的间距经过了精密的空间冗余计算，确保了每一台六轴机器人在执行大幅度挥转动作时，其工作包络圆不会与相邻的输送架发生任何物理干涉。整个车间内没有任何杂乱的电缆或冗余的控制屏显，暗示所有工业机械均通过集中的地下总线或工业无线网络接入了顶层的制造执行系统。这种由深蓝色、银灰色、白色和瓷砖质感构成的工业景观，不仅在视觉上层次分明，更在功能上诠释了现代工厂追求极致效率、高度柔性以及无人化作业的规划哲学。该场景中，每一处设备的分布位置、每一个周转筐的摆放细节，都标志着一个处于极佳运行状态、具备高度协同能力的自动化转运示范工程模型。
* **设备数量(Device Number):**
  * **Scene: 1**
  * **IndustrialRobot: 6**
  * **Workbench: 6**
  * **Conveyor: 9**
  * **AGV: 0**
  * **Forklift: 0**
  * **Box: 6**
  * **Rack: 0**
  * **Pallet: 0**
  * **Part: 24**
  * **Decoration: 0**

## 2.场景对象层级(Scene Hierarchy)
*   World (Xform)
    *   factory (Xform)
        *   Materials (Scope)
            *   WindowsIndustrial_frontSolid_OpenWindows_Mat (Material)
                *   pbr_shader (Shader)
                *   uvset0 (Shader)
                *   tex_base (Shader)
            *   WindowsIndustrial_frontSolid_Mat (Material)
                *   pbr_shader (Shader)
                *   uvset0 (Shader)
                *   tex_base (Shader)
            *   WindowsIndustrial_frontDoorclosed_Mat (Material)
                *   pbr_shader (Shader)
                *   uvset0 (Shader)
                *   tex_base (Shader)
            *   WindowsIndustrial_frontDoorOpen_Mat (Material)
                *   pbr_shader (Shader)
                *   uvset0 (Shader)
                *   tex_base (Shader)
            *   WindowsIndustrial_front_Mat (Material)
                *   pbr_shader (Shader)
                *   uvset0 (Shader)
                *   tex_base (Shader)
            *   _1___Default (Material)
                *   pbr_shader (Shader)
                *   uvset0 (Shader)
                *   tex_base (Shader)
            *   _0___Default (Material)
                *   pbr_shader (Shader)
                *   uvset0 (Shader)
                *   tex_base (Shader)
        *   Meshes (Xform)
            *   Sketchfab_model (Xform)
                *   cc020ec10d3e484ab6eb350963eb38d0_fbx (Xform)
                    *   RootNode (Xform)
                        *   Factory002 (Xform)
                            *   Factory002_WindowsIndustrial_frontSolid_OpenWindows_Mat_0 (Xform)
                                *   Factory002_WindowsIndustrial_frontSolid_OpenWindows_Mat_0 (Mesh)
                            *   Factory002_WindowsIndustrial_frontSolid_Mat_0 (Xform)
                                *   Factory002_WindowsIndustrial_frontSolid_Mat_0 (Mesh)
                            *   Factory002_WindowsIndustrial_frontDoorclosed_Mat_0 (Xform)
                                *   Factory002_WindowsIndustrial_frontDoorclosed_Mat_0 (Mesh)
                            *   Factory002_WindowsIndustrial_frontDoorOpen_Mat_0 (Xform)
                                *   Factory002_WindowsIndustrial_frontDoorOpen_Mat_0 (Mesh)
                            *   Factory002_WindowsIndustrial_front_Mat_0 (Xform)
                                *   Factory002_WindowsIndustrial_front_Mat_0 (Mesh)
                            *   Factory002_11___Default_0 (Xform)
                                *   Factory002_11___Default_0 (Mesh)
                        *   Object001 (Xform)
                            *   Object001_20___Default_0 (Xform)
                                *   Object001_20___Default_0 (Mesh)
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
    *   Conveyor_Belt_01 (Xform)
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
    *   Conveyor_Belt_02 (Xform)
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
    *   Conveyor_Belt_03 (Xform)
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
    *   Conveyor_Belt_04 (Xform)
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
    *   Conveyor_Belt_05 (Xform)
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
    *   AGV_ready_03 (Xform)
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
    *   AGV_ready_04 (Xform)
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
    *   AGV_ready_05 (Xform)
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
    *   AGV_ready_06 (Xform)
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
    *   Plastic_Crate_1_ (Xform)
        *   Materials (Scope)
            *   Material_1 (Material)
                *   pbr_shader (Shader)
                *   uvset0 (Shader)
                *   tex_base (Shader)
        *   Meshes (Xform)
            *   Sketchfab_model (Xform)
                *   Plastic_Crate_FBX (Xform)
                    *   RootNode (Xform)
                        *   Box003 (Xform)
                            *   Object_4 (Xform)
                                *   Box003_Material__1_0 (Xform)
                                    *   Box003_Material__1_0 (Mesh)
    *   Plastic_Crate_1__01 (Xform)
        *   Materials (Scope)
            *   Material_1 (Material)
                *   pbr_shader (Shader)
                *   uvset0 (Shader)
                *   tex_base (Shader)
        *   Meshes (Xform)
            *   Sketchfab_model (Xform)
                *   Plastic_Crate_FBX (Xform)
                    *   RootNode (Xform)
                        *   Box003 (Xform)
                            *   Object_4 (Xform)
                                *   Box003_Material__1_0 (Xform)
                                    *   Box003_Material__1_0 (Mesh)
    *   Plastic_Crate_1__02 (Xform)
        *   Materials (Scope)
            *   Material_1 (Material)
                *   pbr_shader (Shader)
                *   uvset0 (Shader)
                *   tex_base (Shader)
        *   Meshes (Xform)
            *   Sketchfab_model (Xform)
                *   Plastic_Crate_FBX (Xform)
                    *   RootNode (Xform)
                        *   Box003 (Xform)
                            *   Object_4 (Xform)
                                *   Box003_Material__1_0 (Xform)
                                    *   Box003_Material__1_0 (Mesh)
    *   Plastic_Crate_1__03 (Xform)
        *   Materials (Scope)
            *   Material_1 (Material)
                *   pbr_shader (Shader)
                *   uvset0 (Shader)
                *   tex_base (Shader)
        *   Meshes (Xform)
            *   Sketchfab_model (Xform)
                *   Plastic_Crate_FBX (Xform)
                    *   RootNode (Xform)
                        *   Box003 (Xform)
                            *   Object_4 (Xform)
                                *   Box003_Material__1_0 (Xform)
                                    *   Box003_Material__1_0 (Mesh)
    *   Plastic_Crate_1__04 (Xform)
        *   Materials (Scope)
            *   Material_1 (Material)
                *   pbr_shader (Shader)
                *   uvset0 (Shader)
                *   tex_base (Shader)
        *   Meshes (Xform)
            *   Sketchfab_model (Xform)
                *   Plastic_Crate_FBX (Xform)
                    *   RootNode (Xform)
                        *   Box003 (Xform)
                            *   Object_4 (Xform)
                                *   Box003_Material__1_0 (Xform)
                                    *   Box003_Material__1_0 (Mesh)
    *   Plastic_Crate_1__05 (Xform)
        *   Materials (Scope)
            *   Material_1 (Material)
                *   pbr_shader (Shader)
                *   uvset0 (Shader)
                *   tex_base (Shader)
        *   Meshes (Xform)
            *   Sketchfab_model (Xform)
                *   Plastic_Crate_FBX (Xform)
                    *   RootNode (Xform)
                        *   Box003 (Xform)
                            *   Object_4 (Xform)
                                *   Box003_Material__1_0 (Xform)
                                    *   Box003_Material__1_0 (Mesh)
    *   Conveyor_Belt_06 (Xform)
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
    *   Conveyor_Belt_07 (Prim)
    *   part (Xform)
        *   node_36_Size_10x112x120x18_Length_38_SUPPRESSION_Default (Xform)
            *   geometry_1 (Mesh)
    *   part_01 (Prim)
    *   part_02 (Prim)
    *   part_03 (Prim)
    *   part_04 (Prim)
    *   Conveyor_Belt_08 (Prim)
    *   part_05 (Prim)
    *   part_06 (Prim)
    *   part_07 (Prim)
    *   part_08 (Prim)
    *   part_09 (Prim)
    *   part_10 (Prim)
    *   part_23 (Prim)
    *   part_22 (Prim)
    *   part_21 (Prim)
    *   part_20 (Prim)
    *   part_19 (Prim)
    *   part_18 (Prim)
    *   part_17 (Prim)
    *   part_16 (Prim)
    *   part_15 (Prim)
    *   part_14 (Prim)
    *   part_13 (Prim)
    *   part_12 (Prim)
    *   part_11 (Prim)
    *   part_24 (Prim)
    *   MobileShopDesk_A01_Blue_01 (Xform)
        *   SM_MobileShopDesk_A01_01 (Mesh)
            *   M_MobileShopDesk_A01_Body (GeomSubset)
            *   M_MobileShopDesk_A01_Caps (GeomSubset)
            *   M_MobileShopDesk_A01_LocksBoltsHandlesKeys (GeomSubset)
            *   SM_MobileShopDesk_A01_FrontJointWheelLeft_01 (Mesh)
                *   SM_MobileShopDesk_A01_FrontWheelLeft_01 (Mesh)
                    *   M_MobileShopDesk_A01_Wheels (GeomSubset)
                    *   M_MobileShopDesk_A01_WheelsBody (GeomSubset)
            *   SM_MobileShopDesk_A01_BackJointWheelLeft_01 (Mesh)
                *   SM_MobileShopDesk_A01_BackWheelLeft_01 (Mesh)
                    *   M_MobileShopDesk_A01_Wheels (GeomSubset)
                    *   M_MobileShopDesk_A01_WheelsBody (GeomSubset)
            *   SM_MobileShopDesk_A01_BackJointWheelRight_01 (Mesh)
                *   SM_MobileShopDesk_A01_BackWheelRight_01 (Mesh)
                    *   M_MobileShopDesk_A01_Wheels (GeomSubset)
                    *   M_MobileShopDesk_A01_WheelsBody (GeomSubset)
            *   SM_MobileShopDesk_A01_FrontJointWheelRight_01 (Mesh)
                *   SM_MobileShopDesk_A01_FrontWheelRight_01 (Mesh)
                    *   M_MobileShopDesk_A01_Wheels (GeomSubset)
                    *   M_MobileShopDesk_A01_WheelsBody (GeomSubset)
            *   SM_MobileShopDesk_A01_Door_01 (Mesh)
                *   M_MobileShopDesk_A01_Body (GeomSubset)
                *   M_MobileShopDesk_A01_LocksBoltsHandlesKeys (GeomSubset)
            *   SM_MobileShopDesk_A01_SlidingRails_01 (Mesh)
                *   M_MobileShopDesk_A01_Caps (GeomSubset)
                *   M_MobileShopDesk_A01_LocksBoltsHandlesKeys (GeomSubset)
                *   SM_MobileShopDesk_A01_Drawer_01 (Mesh)
                    *   M_MobileShopDesk_A01_Body (GeomSubset)
                    *   M_MobileShopDesk_A01_LocksBoltsHandlesKeys (GeomSubset)
        *   Looks (Scope)
            *   Metal_Glossy_A_MobileShopDesk_A (Material)
                *   Shader (Shader)
            *   Metal_Rough_A_MobileShopDesk_A (Material)
                *   Shader (Shader)
            *   Plastic_Black_A_MobileShopDesk_A (Material)
                *   Shader (Shader)
            *   Rubber_Gray_Glossy_A_MobileShopDesk_A (Material)
                *   Shader (Shader)
            *   Metal_Painted_Blue_Glossy_A_MobileShopDesk_A (Material)
                *   Shader (Shader)
    *   panda_instanceable1 (Xform)
        *   Group (Xform)
            *   panda_hand (Xform)
                *   visuals (Xform)
                *   collisions (Xform)
                *   panda_finger_joint1 (PhysicsPrismaticJoint)
                *   panda_finger_joint2 (PhysicsPrismaticJoint)
            *   panda_leftfinger (Xform)
                *   visuals (Xform)
                *   collisions (Xform)
            *   panda_link0 (Xform)
                *   visuals (Xform)
                *   collisions (Xform)
                *   panda_joint1 (PhysicsRevoluteJoint)
            *   panda_link1 (Xform)
                *   visuals (Xform)
                *   collisions (Xform)
                *   panda_joint2 (PhysicsRevoluteJoint)
            *   panda_link2 (Xform)
                *   visuals (Xform)
                *   collisions (Xform)
                *   panda_joint3 (PhysicsRevoluteJoint)
            *   panda_link3 (Xform)
                *   visuals (Xform)
                *   collisions (Xform)
                *   panda_joint4 (PhysicsRevoluteJoint)
            *   panda_link4 (Xform)
                *   visuals (Xform)
                *   collisions (Xform)
                *   panda_joint5 (PhysicsRevoluteJoint)
            *   panda_link5 (Xform)
                *   visuals (Xform)
                *   collisions (Xform)
                *   panda_joint6 (PhysicsRevoluteJoint)
            *   panda_link6 (Xform)
                *   visuals (Xform)
                *   collisions (Xform)
                *   panda_joint7 (PhysicsRevoluteJoint)
            *   panda_link7 (Xform)
                *   visuals (Xform)
                *   collisions (Xform)
                *   panda_hand_joint (PhysicsFixedJoint)
            *   panda_rightfinger (Xform)
                *   visuals (Xform)
                *   collisions (Xform)
            *   rootJoint (PhysicsFixedJoint)
    *   MobileShopDesk_A01_Blue_02 (Prim)
    *   panda_instanceable1_01 (Prim)
    *   MobileShopDesk_A01_Blue_03 (Prim)
    *   panda_instanceable1_02 (Prim)
    *   MobileShopDesk_A01_Blue_04 (Prim)
    *   panda_instanceable1_03 (Prim)
    *   MobileShopDesk_A01_Blue_05 (Prim)
    *   panda_instanceable1_04 (Prim)
    *   MobileShopDesk_A01_Blue_06 (Prim)
    *   panda_instanceable1_05 (Prim)
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

### /World/factory
*  **Prim路径 (Prim Path):**/World/factory
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '../scene/factory/factory.usdc'
*  **世界包围盒 (World BBox):**
   *   Size: '(49.139, 19.897, 67.754)'
   *   Center: '(3.074, -0.468, 9.470)'


---


### /World/Conveyor_Belt
*  **Prim路径 (Prim Path):**/World/Conveyor_Belt
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '../assets/Conveyor_Belt/Conveyor_Belt.usdc'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.799, 4.204, 9.846)'
   *   Center: '(0.283, -8.092, 0.641)'


---


### /World/Conveyor_Belt_01
*  **Prim路径 (Prim Path):**/World/Conveyor_Belt_01
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '../assets/Conveyor_Belt/Conveyor_Belt.usdc'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.799, 4.204, 9.846)'
   *   Center: '(5.283, -8.092, 0.641)'


---


### /World/Conveyor_Belt_02
*  **Prim路径 (Prim Path):**/World/Conveyor_Belt_02
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '../assets/Conveyor_Belt/Conveyor_Belt.usdc'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.799, 4.204, 9.846)'
   *   Center: '(10.283, -8.092, 0.641)'


---


### /World/Conveyor_Belt_03
*  **Prim路径 (Prim Path):**/World/Conveyor_Belt_03
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '../assets/Conveyor_Belt/Conveyor_Belt.usdc'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.799, 4.204, 9.846)'
   *   Center: '(-4.717, -8.092, 0.641)'


---


### /World/Conveyor_Belt_04
*  **Prim路径 (Prim Path):**/World/Conveyor_Belt_04
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '../assets/Conveyor_Belt/Conveyor_Belt.usdc'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.799, 4.204, 9.846)'
   *   Center: '(-9.717, -8.092, 0.641)'


---


### /World/Conveyor_Belt_05
*  **Prim路径 (Prim Path):**/World/Conveyor_Belt_05
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '../assets/Conveyor_Belt/Conveyor_Belt.usdc'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.799, 4.204, 9.846)'
   *   Center: '(-14.717, -8.092, 0.641)'


---


### /World/AGV_ready_1
*  **Prim路径 (Prim Path):**/World/AGV_ready_1
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '../assets/AGV_ready_1/AGV_ready_1.usdc'
*  **世界包围盒 (World BBox):**
   *   Size: '(1.457, 0.340, 0.669)'
   *   Center: '(3.497, -15.184, 0.155)'


---


### /World/AGV_ready_02
*  **Prim路径 (Prim Path):**/World/AGV_ready_02
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '../assets/AGV_ready_1/AGV_ready_1.usdc'
*  **世界包围盒 (World BBox):**
   *   Size: '(1.457, 0.340, 0.669)'
   *   Center: '(-1.503, -15.184, 0.155)'


---


### /World/AGV_ready_03
*  **Prim路径 (Prim Path):**/World/AGV_ready_03
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '../assets/AGV_ready_1/AGV_ready_1.usdc'
*  **世界包围盒 (World BBox):**
   *   Size: '(1.457, 0.340, 0.669)'
   *   Center: '(-6.503, -15.184, 0.155)'


---


### /World/AGV_ready_04
*  **Prim路径 (Prim Path):**/World/AGV_ready_04
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '../assets/AGV_ready_1/AGV_ready_1.usdc'
*  **世界包围盒 (World BBox):**
   *   Size: '(1.457, 0.340, 0.669)'
   *   Center: '(-11.503, -15.184, 0.155)'


---


### /World/AGV_ready_05
*  **Prim路径 (Prim Path):**/World/AGV_ready_05
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '../assets/AGV_ready_1/AGV_ready_1.usdc'
*  **世界包围盒 (World BBox):**
   *   Size: '(1.457, 0.340, 0.669)'
   *   Center: '(8.497, -15.184, 0.155)'


---


### /World/AGV_ready_06
*  **Prim路径 (Prim Path):**/World/AGV_ready_06
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '../assets/AGV_ready_1/AGV_ready_1.usdc'
*  **世界包围盒 (World BBox):**
   *   Size: '(1.457, 0.340, 0.669)'
   *   Center: '(-16.503, -15.184, 0.155)'


---


### /World/Plastic_Crate_1_
*  **Prim路径 (Prim Path):**/World/Plastic_Crate_1_
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '../assets/Plastic_Crate(1)/Plastic_Crate.usdc'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.424, 0.365, 0.421)'
   *   Center: '(9.217, -14.477, 0.549)'


---


### /World/Plastic_Crate_1__01
*  **Prim路径 (Prim Path):**/World/Plastic_Crate_1__01
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '../assets/Plastic_Crate(1)/Plastic_Crate.usdc'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.424, 0.365, 0.421)'
   *   Center: '(4.217, -14.477, 0.549)'


---


### /World/Plastic_Crate_1__02
*  **Prim路径 (Prim Path):**/World/Plastic_Crate_1__02
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '../assets/Plastic_Crate(1)/Plastic_Crate.usdc'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.424, 0.365, 0.421)'
   *   Center: '(-0.783, -14.477, 0.549)'


---


### /World/Plastic_Crate_1__03
*  **Prim路径 (Prim Path):**/World/Plastic_Crate_1__03
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '../assets/Plastic_Crate(1)/Plastic_Crate.usdc'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.424, 0.365, 0.421)'
   *   Center: '(-5.783, -14.477, 0.549)'


---


### /World/Plastic_Crate_1__04
*  **Prim路径 (Prim Path):**/World/Plastic_Crate_1__04
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '../assets/Plastic_Crate(1)/Plastic_Crate.usdc'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.424, 0.365, 0.421)'
   *   Center: '(-10.783, -14.477, 0.549)'


---


### /World/Plastic_Crate_1__05
*  **Prim路径 (Prim Path):**/World/Plastic_Crate_1__05
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '../assets/Plastic_Crate(1)/Plastic_Crate.usdc'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.424, 0.365, 0.421)'
   *   Center: '(-15.783, -14.477, 0.549)'


---


### /World/Conveyor_Belt_06
*  **Prim路径 (Prim Path):**/World/Conveyor_Belt_06
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '../device_data/usdz/Conveyor/Conveyor_Belt.usdz'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.799, 4.204, 9.846)'
   *   Center: '(-10.302, -2.983, 0.641)'


---


### /World/part
*  **Prim路径 (Prim Path):**/World/part
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '../device_data/usdz/Part/hua.usd'
*  **世界包围盒 (World BBox):**
   *   Size: '(11.840, 11.998, 3.800)'
   *   Center: '(5.310, -12.000, 1.157)'


---


### /World/MobileShopDesk_A01_Blue_01
*  **Prim路径 (Prim Path):**/World/MobileShopDesk_A01_Blue_01
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '../device_data/usdz/Workbench/MobileShopDesk_A01_Blue_01.usdz'
*  **世界包围盒 (World BBox):**
   *   Size: '(61.575, 57.307, 103.782)'
   *   Center: '(-14.529, -13.413, 0.768)'


---


### /World/panda_instanceable1
*  **Prim路径 (Prim Path):**/World/panda_instanceable1
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '../device_data/usdz/IndustrialRobot/panda_instanceable1.usdz'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.503, 0.389, 1.672)'
   *   Center: '(-14.432, -13.514, 1.947)'


---


### /World/panda_instanceable1/Group/panda_hand/visuals
*  **Prim路径 (Prim Path):**/World/panda_instanceable1/Group/panda_hand/visuals
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/Flattened_Prototype_6'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.063, 0.205, 0.092)'
   *   Center: '(-14.322, -13.513, 2.470)'


---


### /World/panda_instanceable1/Group/panda_hand/collisions
*  **Prim路径 (Prim Path):**/World/panda_instanceable1/Group/panda_hand/collisions
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/Flattened_Prototype_13'
*  **世界包围盒 (World BBox):**
   *   Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
   *   Center: '(-14.321, -13.515, 2.500)'


---


### /World/panda_instanceable1/Group/panda_leftfinger/visuals
*  **Prim路径 (Prim Path):**/World/panda_instanceable1/Group/panda_leftfinger/visuals
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/Flattened_Prototype_2'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.021, 0.026, 0.054)'
   *   Center: '(-14.307, -13.529, 2.372)'


---


### /World/panda_instanceable1/Group/panda_leftfinger/collisions
*  **Prim路径 (Prim Path):**/World/panda_instanceable1/Group/panda_leftfinger/collisions
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/Flattened_Prototype_22'
*  **世界包围盒 (World BBox):**
   *   Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
   *   Center: '(-14.321, -13.515, 2.412)'


---


### /World/panda_instanceable1/Group/panda_link0/visuals
*  **Prim路径 (Prim Path):**/World/panda_instanceable1/Group/panda_link0/visuals
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/Flattened_Prototype_5'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.226, 0.189, 0.140)'
   *   Center: '(-14.515, -13.515, 1.216)'


---


### /World/panda_instanceable1/Group/panda_link0/collisions
*  **Prim路径 (Prim Path):**/World/panda_instanceable1/Group/panda_link0/collisions
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/Flattened_Prototype_19'
*  **世界包围盒 (World BBox):**
   *   Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
   *   Center: '(-14.453, -13.515, 1.111)'


---


### /World/panda_instanceable1/Group/panda_link1/visuals
*  **Prim路径 (Prim Path):**/World/panda_instanceable1/Group/panda_link1/visuals
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/Flattened_Prototype_16'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.110, 0.184, 0.247)'
   *   Center: '(-14.453, -13.571, 1.507)'


---


### /World/panda_instanceable1/Group/panda_link1/collisions
*  **Prim路径 (Prim Path):**/World/panda_instanceable1/Group/panda_link1/collisions
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/Flattened_Prototype_18'
*  **世界包围盒 (World BBox):**
   *   Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
   *   Center: '(-14.453, -13.515, 1.610)'


---


### /World/panda_instanceable1/Group/panda_link2/visuals
*  **Prim路径 (Prim Path):**/World/panda_instanceable1/Group/panda_link2/visuals
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/Flattened_Prototype_1'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.110, 0.249, 0.184)'
   *   Center: '(-14.453, -13.459, 1.715)'


---


### /World/panda_instanceable1/Group/panda_link2/collisions
*  **Prim路径 (Prim Path):**/World/panda_instanceable1/Group/panda_link2/collisions
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/Flattened_Prototype_12'
*  **世界包围盒 (World BBox):**
   *   Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
   *   Center: '(-14.453, -13.515, 1.610)'


---


### /World/panda_instanceable1/Group/panda_link3/visuals
*  **Prim路径 (Prim Path):**/World/panda_instanceable1/Group/panda_link3/visuals
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/Flattened_Prototype_14'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.193, 0.166, 0.176)'
   *   Center: '(-14.391, -13.473, 2.035)'


---


### /World/panda_instanceable1/Group/panda_link3/collisions
*  **Prim路径 (Prim Path):**/World/panda_instanceable1/Group/panda_link3/collisions
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/Flattened_Prototype_15'
*  **世界包围盒 (World BBox):**
   *   Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
   *   Center: '(-14.453, -13.515, 2.084)'


---


### /World/panda_instanceable1/Group/panda_link4/visuals
*  **Prim路径 (Prim Path):**/World/panda_instanceable1/Group/panda_link4/visuals
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/Flattened_Prototype_8'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.193, 0.179, 0.166)'
   *   Center: '(-14.391, -13.557, 2.136)'


---


### /World/panda_instanceable1/Group/panda_link4/collisions
*  **Prim路径 (Prim Path):**/World/panda_instanceable1/Group/panda_link4/collisions
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/Flattened_Prototype_3'
*  **世界包围盒 (World BBox):**
   *   Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
   *   Center: '(-14.329, -13.515, 2.084)'


---


### /World/panda_instanceable1/Group/panda_link5/visuals
*  **Prim路径 (Prim Path):**/World/panda_instanceable1/Group/panda_link5/visuals
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/Flattened_Prototype_10'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.110, 0.185, 0.311)'
   *   Center: '(-14.453, -13.459, 2.505)'


---


### /World/panda_instanceable1/Group/panda_link5/collisions
*  **Prim路径 (Prim Path):**/World/panda_instanceable1/Group/panda_link5/collisions
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/Flattened_Prototype_4'
*  **世界包围盒 (World BBox):**
   *   Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
   *   Center: '(-14.453, -13.515, 2.660)'


---


### /World/panda_instanceable1/Group/panda_link6/visuals
*  **Prim路径 (Prim Path):**/World/panda_instanceable1/Group/panda_link6/visuals
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/Flattened_Prototype_9'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.180, 0.133, 0.100)'
   *   Center: '(-14.390, -13.524, 2.683)'


---


### /World/panda_instanceable1/Group/panda_link6/collisions
*  **Prim路径 (Prim Path):**/World/panda_instanceable1/Group/panda_link6/collisions
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/Flattened_Prototype_11'
*  **世界包围盒 (World BBox):**
   *   Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
   *   Center: '(-14.453, -13.515, 2.660)'


---


### /World/panda_instanceable1/Group/panda_link7/visuals
*  **Prim路径 (Prim Path):**/World/panda_instanceable1/Group/panda_link7/visuals
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/Flattened_Prototype_17'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.125, 0.125, 0.055)'
   *   Center: '(-14.293, -13.543, 2.541)'


---


### /World/panda_instanceable1/Group/panda_link7/collisions
*  **Prim路径 (Prim Path):**/World/panda_instanceable1/Group/panda_link7/collisions
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/Flattened_Prototype_21'
*  **世界包围盒 (World BBox):**
   *   Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
   *   Center: '(-14.321, -13.515, 2.660)'


---


### /World/panda_instanceable1/Group/panda_rightfinger/visuals
*  **Prim路径 (Prim Path):**/World/panda_instanceable1/Group/panda_rightfinger/visuals
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/Flattened_Prototype_7'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.021, 0.026, 0.054)'
   *   Center: '(-14.335, -13.501, 2.372)'


---


### /World/panda_instanceable1/Group/panda_rightfinger/collisions
*  **Prim路径 (Prim Path):**/World/panda_instanceable1/Group/panda_rightfinger/collisions
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/Flattened_Prototype_20'
*  **世界包围盒 (World BBox):**
   *   Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
   *   Center: '(-14.321, -13.515, 2.412)'


---


## 4. 材质库 (Material Library)

### /World/factory/Materials/WindowsIndustrial_frontSolid_OpenWindows_Mat
*  **Prim路径 (Prim Path):**/World/factory/Materials/WindowsIndustrial_frontSolid_OpenWindows_Mat
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/factory/Materials/WindowsIndustrial_frontSolid_OpenWindows_Mat/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/factory/Materials/WindowsIndustrial_frontSolid_OpenWindows_Mat/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f]
               *   Connected: '/World/factory/Materials/WindowsIndustrial_frontSolid_OpenWindows_Mat/tex_base.outputs:rgb' @ '/World/factory/Materials/WindowsIndustrial_frontSolid_OpenWindows_Mat/tex_base'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/WindowsIndustrial-frontSolid-OpenWindows_Mat_baseColor.jpg'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(1.000, 1.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0.957705'
       *   '/World/factory/Materials/WindowsIndustrial_frontSolid_OpenWindows_Mat/tex_base' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/WindowsIndustrial-frontSolid-OpenWindows_Mat_baseColor.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
           *   'file' [asset] = '0/WindowsIndustrial-frontSolid-OpenWindows_Mat_baseColor.jpg'
           *   'st' [float2]
               *   Connected: '/World/factory/Materials/WindowsIndustrial_frontSolid_OpenWindows_Mat/uvset0.outputs:result' @ '/World/factory/Materials/WindowsIndustrial_frontSolid_OpenWindows_Mat/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/factory/Materials/WindowsIndustrial_frontSolid_OpenWindows_Mat/uvset0' (ID: 'UsdPrimvarReader_float2')
       *   Implementation: 'id'


---


### /World/factory/Materials/WindowsIndustrial_frontSolid_Mat
*  **Prim路径 (Prim Path):**/World/factory/Materials/WindowsIndustrial_frontSolid_Mat
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/factory/Materials/WindowsIndustrial_frontSolid_Mat/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/factory/Materials/WindowsIndustrial_frontSolid_Mat/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f]
               *   Connected: '/World/factory/Materials/WindowsIndustrial_frontSolid_Mat/tex_base.outputs:rgb' @ '/World/factory/Materials/WindowsIndustrial_frontSolid_Mat/tex_base'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/WindowsIndustrial-frontSolid_Mat_baseColor.jpg'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(1.000, 1.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0.957705'
       *   '/World/factory/Materials/WindowsIndustrial_frontSolid_Mat/tex_base' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/WindowsIndustrial-frontSolid_Mat_baseColor.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
           *   'file' [asset] = '0/WindowsIndustrial-frontSolid_Mat_baseColor.jpg'
           *   'st' [float2]
               *   Connected: '/World/factory/Materials/WindowsIndustrial_frontSolid_Mat/uvset0.outputs:result' @ '/World/factory/Materials/WindowsIndustrial_frontSolid_Mat/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/factory/Materials/WindowsIndustrial_frontSolid_Mat/uvset0' (ID: 'UsdPrimvarReader_float2')
       *   Implementation: 'id'


---


### /World/factory/Materials/WindowsIndustrial_frontDoorclosed_Mat
*  **Prim路径 (Prim Path):**/World/factory/Materials/WindowsIndustrial_frontDoorclosed_Mat
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/factory/Materials/WindowsIndustrial_frontDoorclosed_Mat/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/factory/Materials/WindowsIndustrial_frontDoorclosed_Mat/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f]
               *   Connected: '/World/factory/Materials/WindowsIndustrial_frontDoorclosed_Mat/tex_base.outputs:rgb' @ '/World/factory/Materials/WindowsIndustrial_frontDoorclosed_Mat/tex_base'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/WindowsIndustrial-frontDoorclosed_Mat_baseColor.jpg'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(1.000, 1.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0.957705'
       *   '/World/factory/Materials/WindowsIndustrial_frontDoorclosed_Mat/tex_base' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/WindowsIndustrial-frontDoorclosed_Mat_baseColor.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
           *   'file' [asset] = '0/WindowsIndustrial-frontDoorclosed_Mat_baseColor.jpg'
           *   'st' [float2]
               *   Connected: '/World/factory/Materials/WindowsIndustrial_frontDoorclosed_Mat/uvset0.outputs:result' @ '/World/factory/Materials/WindowsIndustrial_frontDoorclosed_Mat/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/factory/Materials/WindowsIndustrial_frontDoorclosed_Mat/uvset0' (ID: 'UsdPrimvarReader_float2')
       *   Implementation: 'id'


---


### /World/factory/Materials/WindowsIndustrial_frontDoorOpen_Mat
*  **Prim路径 (Prim Path):**/World/factory/Materials/WindowsIndustrial_frontDoorOpen_Mat
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/factory/Materials/WindowsIndustrial_frontDoorOpen_Mat/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/factory/Materials/WindowsIndustrial_frontDoorOpen_Mat/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f]
               *   Connected: '/World/factory/Materials/WindowsIndustrial_frontDoorOpen_Mat/tex_base.outputs:rgb' @ '/World/factory/Materials/WindowsIndustrial_frontDoorOpen_Mat/tex_base'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/WindowsIndustrial-frontDoorOpen_Mat_baseColor.jpg'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(1.000, 1.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0.957705'
       *   '/World/factory/Materials/WindowsIndustrial_frontDoorOpen_Mat/tex_base' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/WindowsIndustrial-frontDoorOpen_Mat_baseColor.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
           *   'file' [asset] = '0/WindowsIndustrial-frontDoorOpen_Mat_baseColor.jpg'
           *   'st' [float2]
               *   Connected: '/World/factory/Materials/WindowsIndustrial_frontDoorOpen_Mat/uvset0.outputs:result' @ '/World/factory/Materials/WindowsIndustrial_frontDoorOpen_Mat/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/factory/Materials/WindowsIndustrial_frontDoorOpen_Mat/uvset0' (ID: 'UsdPrimvarReader_float2')
       *   Implementation: 'id'


---


### /World/factory/Materials/WindowsIndustrial_front_Mat
*  **Prim路径 (Prim Path):**/World/factory/Materials/WindowsIndustrial_front_Mat
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/factory/Materials/WindowsIndustrial_front_Mat/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/factory/Materials/WindowsIndustrial_front_Mat/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f]
               *   Connected: '/World/factory/Materials/WindowsIndustrial_front_Mat/tex_base.outputs:rgb' @ '/World/factory/Materials/WindowsIndustrial_front_Mat/tex_base'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/WindowsIndustrial-front_Mat_baseColor.jpg'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(1.000, 1.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0.957705'
       *   '/World/factory/Materials/WindowsIndustrial_front_Mat/tex_base' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/WindowsIndustrial-front_Mat_baseColor.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
           *   'file' [asset] = '0/WindowsIndustrial-front_Mat_baseColor.jpg'
           *   'st' [float2]
               *   Connected: '/World/factory/Materials/WindowsIndustrial_front_Mat/uvset0.outputs:result' @ '/World/factory/Materials/WindowsIndustrial_front_Mat/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/factory/Materials/WindowsIndustrial_front_Mat/uvset0' (ID: 'UsdPrimvarReader_float2')
       *   Implementation: 'id'


---


### /World/factory/Materials/_1___Default
*  **Prim路径 (Prim Path):**/World/factory/Materials/_1___Default
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/factory/Materials/_1___Default/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/factory/Materials/_1___Default/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f]
               *   Connected: '/World/factory/Materials/_1___Default/tex_base.outputs:rgb' @ '/World/factory/Materials/_1___Default/tex_base'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/11_-_Default_baseColor.jpg'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(1.000, 1.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0.892971'
       *   '/World/factory/Materials/_1___Default/tex_base' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/11_-_Default_baseColor.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
           *   'file' [asset] = '0/11_-_Default_baseColor.jpg'
           *   'st' [float2]
               *   Connected: '/World/factory/Materials/_1___Default/uvset0.outputs:result' @ '/World/factory/Materials/_1___Default/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/factory/Materials/_1___Default/uvset0' (ID: 'UsdPrimvarReader_float2')
       *   Implementation: 'id'


---


### /World/factory/Materials/_0___Default
*  **Prim路径 (Prim Path):**/World/factory/Materials/_0___Default
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/factory/Materials/_0___Default/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/factory/Materials/_0___Default/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f]
               *   Connected: '/World/factory/Materials/_0___Default/tex_base.outputs:rgb' @ '/World/factory/Materials/_0___Default/tex_base'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/20_-_Default_baseColor.jpg'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(1.000, 1.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0.892971'
       *   '/World/factory/Materials/_0___Default/tex_base' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/20_-_Default_baseColor.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
           *   'file' [asset] = '0/20_-_Default_baseColor.jpg'
           *   'st' [float2]
               *   Connected: '/World/factory/Materials/_0___Default/uvset0.outputs:result' @ '/World/factory/Materials/_0___Default/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/factory/Materials/_0___Default/uvset0' (ID: 'UsdPrimvarReader_float2')
       *   Implementation: 'id'


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


### /World/Conveyor_Belt_01/Materials/Material_0
*  **Prim路径 (Prim Path):**/World/Conveyor_Belt_01/Materials/Material_0
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/Conveyor_Belt_01/Materials/Material_0/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/Conveyor_Belt_01/Materials/Material_0/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f]
               *   Connected: '/World/Conveyor_Belt_01/Materials/Material_0/tex_base.outputs:rgb' @ '/World/Conveyor_Belt_01/Materials/Material_0/tex_base'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/Material_0_baseColor.jpg'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(1.000, 1.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0.892971'
       *   '/World/Conveyor_Belt_01/Materials/Material_0/tex_base' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/Material_0_baseColor.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
           *   'file' [asset] = '0/Material_0_baseColor.jpg'
           *   'st' [float2]
               *   Connected: '/World/Conveyor_Belt_01/Materials/Material_0/uvset0.outputs:result' @ '/World/Conveyor_Belt_01/Materials/Material_0/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/Conveyor_Belt_01/Materials/Material_0/uvset0' (ID: 'UsdPrimvarReader_float2')
       *   Implementation: 'id'


---


### /World/Conveyor_Belt_02/Materials/Material_0
*  **Prim路径 (Prim Path):**/World/Conveyor_Belt_02/Materials/Material_0
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/Conveyor_Belt_02/Materials/Material_0/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/Conveyor_Belt_02/Materials/Material_0/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f]
               *   Connected: '/World/Conveyor_Belt_02/Materials/Material_0/tex_base.outputs:rgb' @ '/World/Conveyor_Belt_02/Materials/Material_0/tex_base'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/Material_0_baseColor.jpg'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(1.000, 1.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0.892971'
       *   '/World/Conveyor_Belt_02/Materials/Material_0/tex_base' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/Material_0_baseColor.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
           *   'file' [asset] = '0/Material_0_baseColor.jpg'
           *   'st' [float2]
               *   Connected: '/World/Conveyor_Belt_02/Materials/Material_0/uvset0.outputs:result' @ '/World/Conveyor_Belt_02/Materials/Material_0/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/Conveyor_Belt_02/Materials/Material_0/uvset0' (ID: 'UsdPrimvarReader_float2')
       *   Implementation: 'id'


---


### /World/Conveyor_Belt_03/Materials/Material_0
*  **Prim路径 (Prim Path):**/World/Conveyor_Belt_03/Materials/Material_0
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/Conveyor_Belt_03/Materials/Material_0/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/Conveyor_Belt_03/Materials/Material_0/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f]
               *   Connected: '/World/Conveyor_Belt_03/Materials/Material_0/tex_base.outputs:rgb' @ '/World/Conveyor_Belt_03/Materials/Material_0/tex_base'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/Material_0_baseColor.jpg'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(1.000, 1.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0.892971'
       *   '/World/Conveyor_Belt_03/Materials/Material_0/tex_base' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/Material_0_baseColor.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
           *   'file' [asset] = '0/Material_0_baseColor.jpg'
           *   'st' [float2]
               *   Connected: '/World/Conveyor_Belt_03/Materials/Material_0/uvset0.outputs:result' @ '/World/Conveyor_Belt_03/Materials/Material_0/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/Conveyor_Belt_03/Materials/Material_0/uvset0' (ID: 'UsdPrimvarReader_float2')
       *   Implementation: 'id'


---


### /World/Conveyor_Belt_04/Materials/Material_0
*  **Prim路径 (Prim Path):**/World/Conveyor_Belt_04/Materials/Material_0
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/Conveyor_Belt_04/Materials/Material_0/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/Conveyor_Belt_04/Materials/Material_0/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f]
               *   Connected: '/World/Conveyor_Belt_04/Materials/Material_0/tex_base.outputs:rgb' @ '/World/Conveyor_Belt_04/Materials/Material_0/tex_base'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/Material_0_baseColor.jpg'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(1.000, 1.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0.892971'
       *   '/World/Conveyor_Belt_04/Materials/Material_0/tex_base' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/Material_0_baseColor.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
           *   'file' [asset] = '0/Material_0_baseColor.jpg'
           *   'st' [float2]
               *   Connected: '/World/Conveyor_Belt_04/Materials/Material_0/uvset0.outputs:result' @ '/World/Conveyor_Belt_04/Materials/Material_0/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/Conveyor_Belt_04/Materials/Material_0/uvset0' (ID: 'UsdPrimvarReader_float2')
       *   Implementation: 'id'


---


### /World/Conveyor_Belt_05/Materials/Material_0
*  **Prim路径 (Prim Path):**/World/Conveyor_Belt_05/Materials/Material_0
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/Conveyor_Belt_05/Materials/Material_0/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/Conveyor_Belt_05/Materials/Material_0/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f]
               *   Connected: '/World/Conveyor_Belt_05/Materials/Material_0/tex_base.outputs:rgb' @ '/World/Conveyor_Belt_05/Materials/Material_0/tex_base'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/Material_0_baseColor.jpg'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(1.000, 1.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0.892971'
       *   '/World/Conveyor_Belt_05/Materials/Material_0/tex_base' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/Material_0_baseColor.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
           *   'file' [asset] = '0/Material_0_baseColor.jpg'
           *   'st' [float2]
               *   Connected: '/World/Conveyor_Belt_05/Materials/Material_0/uvset0.outputs:result' @ '/World/Conveyor_Belt_05/Materials/Material_0/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/Conveyor_Belt_05/Materials/Material_0/uvset0' (ID: 'UsdPrimvarReader_float2')
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


### /World/AGV_ready_03/Materials/ASELSAN_CATS_04
*  **Prim路径 (Prim Path):**/World/AGV_ready_03/Materials/ASELSAN_CATS_04
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_03/Materials/ASELSAN_CATS_04/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_03/Materials/ASELSAN_CATS_04/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.158, 0.158, 0.158)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_03/Materials/ASELSAN_CATS_04_2
*  **Prim路径 (Prim Path):**/World/AGV_ready_03/Materials/ASELSAN_CATS_04_2
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_03/Materials/ASELSAN_CATS_04_2/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_03/Materials/ASELSAN_CATS_04_2/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.769, 0.773, 0.749)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_03/Materials/ASELSAN_CATS_13
*  **Prim路径 (Prim Path):**/World/AGV_ready_03/Materials/ASELSAN_CATS_13
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_03/Materials/ASELSAN_CATS_13/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_03/Materials/ASELSAN_CATS_13/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.706, 0.718, 0.729)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_03/Materials/Color_000
*  **Prim路径 (Prim Path):**/World/AGV_ready_03/Materials/Color_000
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_03/Materials/Color_000/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_03/Materials/Color_000/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(1.000, 1.000, 1.000)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_03/Materials/Color_A05
*  **Prim路径 (Prim Path):**/World/AGV_ready_03/Materials/Color_A05
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_03/Materials/Color_A05/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_03/Materials/Color_A05/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(1.000, 0.000, 0.000)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0.959234'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0'


---


### /World/AGV_ready_03/Materials/Color_A06
*  **Prim路径 (Prim Path):**/World/AGV_ready_03/Materials/Color_A06
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_03/Materials/Color_A06/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_03/Materials/Color_A06/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.800, 0.000, 0.000)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_03/Materials/Color_B05
*  **Prim路径 (Prim Path):**/World/AGV_ready_03/Materials/Color_B05
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_03/Materials/Color_B05/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_03/Materials/Color_B05/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(1.000, 0.247, 0.000)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '1'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0'


---


### /World/AGV_ready_03/Materials/Color_E02
*  **Prim路径 (Prim Path):**/World/AGV_ready_03/Materials/Color_E02
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_03/Materials/Color_E02/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_03/Materials/Color_E02/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(1.000, 1.000, 0.196)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_03/Materials/Color_E05
*  **Prim路径 (Prim Path):**/World/AGV_ready_03/Materials/Color_E05
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_03/Materials/Color_E05/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_03/Materials/Color_E05/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(1.000, 0.910, 0.000)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0.625455'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0.133891'


---


### /World/AGV_ready_03/Materials/Color_F06
*  **Prim路径 (Prim Path):**/World/AGV_ready_03/Materials/Color_F06
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_03/Materials/Color_F06/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_03/Materials/Color_F06/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.400, 0.800, 0.000)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_03/Materials/Color_G03
*  **Prim路径 (Prim Path):**/World/AGV_ready_03/Materials/Color_G03
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_03/Materials/Color_G03/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_03/Materials/Color_G03/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.396, 1.000, 0.396)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_03/Materials/Color_M02
*  **Prim路径 (Prim Path):**/World/AGV_ready_03/Materials/Color_M02
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_03/Materials/Color_M02/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_03/Materials/Color_M02/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.776, 0.776, 0.776)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_03/Materials/Color_M03
*  **Prim路径 (Prim Path):**/World/AGV_ready_03/Materials/Color_M03
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_03/Materials/Color_M03/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_03/Materials/Color_M03/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.667, 0.667, 0.667)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_03/Materials/Mtl39
*  **Prim路径 (Prim Path):**/World/AGV_ready_03/Materials/Mtl39
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_03/Materials/Mtl39/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_03/Materials/Mtl39/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.494, 0.494, 0.494)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_03/Materials/Mtl6
*  **Prim路径 (Prim Path):**/World/AGV_ready_03/Materials/Mtl6
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_03/Materials/Mtl6/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_03/Materials/Mtl6/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f]
               *   Connected: '/World/AGV_ready_03/Materials/Mtl6/tex_base.outputs:rgb' @ '/World/AGV_ready_03/Materials/Mtl6/tex_base'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/Mtl6_baseColor.jpg'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'
       *   '/World/AGV_ready_03/Materials/Mtl6/tex_base' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/Mtl6_baseColor.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
           *   'file' [asset] = '0/Mtl6_baseColor.jpg'
           *   'st' [float2]
               *   Connected: '/World/AGV_ready_03/Materials/Mtl6/uvset0.outputs:result' @ '/World/AGV_ready_03/Materials/Mtl6/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/AGV_ready_03/Materials/Mtl6/uvset0' (ID: 'UsdPrimvarReader_float2')
       *   Implementation: 'id'


---


### /World/AGV_ready_03/Materials/Mtl9
*  **Prim路径 (Prim Path):**/World/AGV_ready_03/Materials/Mtl9
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_03/Materials/Mtl9/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_03/Materials/Mtl9/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.514, 1.000, 0.000)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_03/Materials/Silver
*  **Prim路径 (Prim Path):**/World/AGV_ready_03/Materials/Silver
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_03/Materials/Silver/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_03/Materials/Silver/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.753, 0.753, 0.753)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_03/Materials/material
*  **Prim路径 (Prim Path):**/World/AGV_ready_03/Materials/material
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_03/Materials/material/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_03/Materials/material/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f]
               *   Connected: '/World/AGV_ready_03/Materials/material/tex_base.outputs:rgb' @ '/World/AGV_ready_03/Materials/material/tex_base'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/material_baseColor.jpg'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'
       *   '/World/AGV_ready_03/Materials/material/tex_base' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/material_baseColor.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
           *   'file' [asset] = '0/material_baseColor.jpg'
           *   'st' [float2]
               *   Connected: '/World/AGV_ready_03/Materials/material/uvset0.outputs:result' @ '/World/AGV_ready_03/Materials/material/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/AGV_ready_03/Materials/material/uvset0' (ID: 'UsdPrimvarReader_float2')
       *   Implementation: 'id'


---


### /World/AGV_ready_03/Materials/cash_register_keys
*  **Prim路径 (Prim Path):**/World/AGV_ready_03/Materials/cash_register_keys
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_03/Materials/cash_register_keys/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_03/Materials/cash_register_keys/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.976, 0.992, 0.973)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_03/Materials/Chris_Shoe_Sole
*  **Prim路径 (Prim Path):**/World/AGV_ready_03/Materials/Chris_Shoe_Sole
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_03/Materials/Chris_Shoe_Sole/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_03/Materials/Chris_Shoe_Sole/pbr_shader' (ID: 'UsdPreviewSurface')
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


### /World/AGV_ready_03/Materials/Color_002
*  **Prim路径 (Prim Path):**/World/AGV_ready_03/Materials/Color_002
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_03/Materials/Color_002/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_03/Materials/Color_002/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.217, 0.217, 0.217)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0.570837'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0'


---


### /World/AGV_ready_03/Materials/Color_005
*  **Prim路径 (Prim Path):**/World/AGV_ready_03/Materials/Color_005
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_03/Materials/Color_005/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_03/Materials/Color_005/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.130, 0.130, 0.130)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0.710417'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0'


---


### /World/AGV_ready_03/Materials/Color_006
*  **Prim路径 (Prim Path):**/World/AGV_ready_03/Materials/Color_006
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_03/Materials/Color_006/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_03/Materials/Color_006/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0.237059'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0'


---


### /World/AGV_ready_03/Materials/Color_008
*  **Prim路径 (Prim Path):**/World/AGV_ready_03/Materials/Color_008
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_03/Materials/Color_008/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_03/Materials/Color_008/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.118, 0.118, 0.118)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0.941027'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0'


---


### /World/AGV_ready_03/Materials/Color_A01
*  **Prim路径 (Prim Path):**/World/AGV_ready_03/Materials/Color_A01
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_03/Materials/Color_A01/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_03/Materials/Color_A01/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(1.000, 0.000, 0.000)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0.965302'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0'


---


### /World/AGV_ready_03/Materials/Color_A11
*  **Prim路径 (Prim Path):**/World/AGV_ready_03/Materials/Color_A11
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_03/Materials/Color_A11/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_03/Materials/Color_A11/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.600, 0.000, 0.000)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_03/Materials/Color_M04
*  **Prim路径 (Prim Path):**/World/AGV_ready_03/Materials/Color_M04
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_03/Materials/Color_M04/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_03/Materials/Color_M04/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.557, 0.557, 0.557)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_03/Materials/Color_M05
*  **Prim路径 (Prim Path):**/World/AGV_ready_03/Materials/Color_M05
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_03/Materials/Color_M05/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_03/Materials/Color_M05/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.447, 0.447, 0.447)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_03/Materials/Color_M06
*  **Prim路径 (Prim Path):**/World/AGV_ready_03/Materials/Color_M06
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_03/Materials/Color_M06/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_03/Materials/Color_M06/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_03/Materials/Color_M07
*  **Prim路径 (Prim Path):**/World/AGV_ready_03/Materials/Color_M07
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_03/Materials/Color_M07/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_03/Materials/Color_M07/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.227, 0.227, 0.227)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_03/Materials/Color_M09
*  **Prim路径 (Prim Path):**/World/AGV_ready_03/Materials/Color_M09
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_03/Materials/Color_M09/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_03/Materials/Color_M09/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0.340226'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0.085341'


---


### /World/AGV_ready_03/Materials/FCP_Charcoal_v2
*  **Prim路径 (Prim Path):**/World/AGV_ready_03/Materials/FCP_Charcoal_v2
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_03/Materials/FCP_Charcoal_v2/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_03/Materials/FCP_Charcoal_v2/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.216, 0.216, 0.216)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_03/Materials/FrontColor
*  **Prim路径 (Prim Path):**/World/AGV_ready_03/Materials/FrontColor
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_03/Materials/FrontColor/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_03/Materials/FrontColor/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.504, 0.504, 0.504)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0.637593'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0.218852'


---


### /World/AGV_ready_03/Materials/Light_Blue
*  **Prim路径 (Prim Path):**/World/AGV_ready_03/Materials/Light_Blue
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_03/Materials/Light_Blue/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_03/Materials/Light_Blue/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.601, 0.601, 0.601)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '1'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0.170303'


---


### /World/AGV_ready_03/Materials/M_0011_Seashell
*  **Prim路径 (Prim Path):**/World/AGV_ready_03/Materials/M_0011_Seashell
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_03/Materials/M_0011_Seashell/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_03/Materials/M_0011_Seashell/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(1.000, 0.961, 0.933)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_03/Materials/M_0131_Silver
*  **Prim路径 (Prim Path):**/World/AGV_ready_03/Materials/M_0131_Silver
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_03/Materials/M_0131_Silver/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_03/Materials/M_0131_Silver/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.242, 0.242, 0.242)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0.613318'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0'


---


### /World/AGV_ready_03/Materials/M_0134_DimGray
*  **Prim路径 (Prim Path):**/World/AGV_ready_03/Materials/M_0134_DimGray
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_03/Materials/M_0134_DimGray/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_03/Materials/M_0134_DimGray/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.412, 0.412, 0.412)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_03/Materials/M_0135_DarkGray
*  **Prim路径 (Prim Path):**/World/AGV_ready_03/Materials/M_0135_DarkGray
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_03/Materials/M_0135_DarkGray/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_03/Materials/M_0135_DarkGray/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.318, 0.318, 0.318)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_03/Materials/Metal_Silver
*  **Prim路径 (Prim Path):**/World/AGV_ready_03/Materials/Metal_Silver
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_03/Materials/Metal_Silver/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_03/Materials/Metal_Silver/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.918, 0.914, 0.933)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_03/Materials/Mtl1
*  **Prim路径 (Prim Path):**/World/AGV_ready_03/Materials/Mtl1
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_03/Materials/Mtl1/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_03/Materials/Mtl1/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.015, 0.015, 0.015)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0.255265'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_03/Materials/Mtl10
*  **Prim路径 (Prim Path):**/World/AGV_ready_03/Materials/Mtl10
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_03/Materials/Mtl10/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_03/Materials/Mtl10/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.322, 0.322, 0.322)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_03/Materials/Mtl11
*  **Prim路径 (Prim Path):**/World/AGV_ready_03/Materials/Mtl11
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_03/Materials/Mtl11/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_03/Materials/Mtl11/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.067, 0.757, 0.329)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_03/Materials/Mtl12
*  **Prim路径 (Prim Path):**/World/AGV_ready_03/Materials/Mtl12
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_03/Materials/Mtl12/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_03/Materials/Mtl12/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.502, 0.502, 0.502)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_03/Materials/Mtl13
*  **Prim路径 (Prim Path):**/World/AGV_ready_03/Materials/Mtl13
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_03/Materials/Mtl13/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_03/Materials/Mtl13/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.008, 0.514, 0.816)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_03/Materials/Mtl14
*  **Prim路径 (Prim Path):**/World/AGV_ready_03/Materials/Mtl14
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_03/Materials/Mtl14/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_03/Materials/Mtl14/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.310, 0.310, 0.310)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_03/Materials/Mtl15
*  **Prim路径 (Prim Path):**/World/AGV_ready_03/Materials/Mtl15
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_03/Materials/Mtl15/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_03/Materials/Mtl15/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.263, 0.275, 0.275)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_03/Materials/Mtl16
*  **Prim路径 (Prim Path):**/World/AGV_ready_03/Materials/Mtl16
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_03/Materials/Mtl16/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_03/Materials/Mtl16/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.698, 0.698, 0.000)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_03/Materials/Mtl17
*  **Prim路径 (Prim Path):**/World/AGV_ready_03/Materials/Mtl17
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_03/Materials/Mtl17/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_03/Materials/Mtl17/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.000, 0.863, 1.000)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_03/Materials/Mtl3
*  **Prim路径 (Prim Path):**/World/AGV_ready_03/Materials/Mtl3
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_03/Materials/Mtl3/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_03/Materials/Mtl3/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.431, 0.455, 0.498)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_03/Materials/Mtl35
*  **Prim路径 (Prim Path):**/World/AGV_ready_03/Materials/Mtl35
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_03/Materials/Mtl35/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_03/Materials/Mtl35/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.792, 0.820, 0.933)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_03/Materials/Mtl36
*  **Prim路径 (Prim Path):**/World/AGV_ready_03/Materials/Mtl36
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_03/Materials/Mtl36/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_03/Materials/Mtl36/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.667, 0.698, 0.765)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_03/Materials/Mtl37
*  **Prim路径 (Prim Path):**/World/AGV_ready_03/Materials/Mtl37
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_03/Materials/Mtl37/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_03/Materials/Mtl37/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.098, 0.098, 0.098)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_03/Materials/Mtl3a
*  **Prim路径 (Prim Path):**/World/AGV_ready_03/Materials/Mtl3a
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_03/Materials/Mtl3a/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_03/Materials/Mtl3a/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.388, 0.369, 0.322)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_03/Materials/Mtl3b
*  **Prim路径 (Prim Path):**/World/AGV_ready_03/Materials/Mtl3b
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_03/Materials/Mtl3b/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_03/Materials/Mtl3b/pbr_shader' (ID: 'UsdPreviewSurface')
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


### /World/AGV_ready_03/Materials/Mtl5
*  **Prim路径 (Prim Path):**/World/AGV_ready_03/Materials/Mtl5
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_03/Materials/Mtl5/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_03/Materials/Mtl5/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.396, 0.408, 0.467)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_03/Materials/Mtl7
*  **Prim路径 (Prim Path):**/World/AGV_ready_03/Materials/Mtl7
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_03/Materials/Mtl7/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_03/Materials/Mtl7/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.376, 0.376, 0.376)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_03/Materials/Mtl8
*  **Prim路径 (Prim Path):**/World/AGV_ready_03/Materials/Mtl8
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_03/Materials/Mtl8/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_03/Materials/Mtl8/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.173, 0.173, 0.173)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_03/Materials/Mtla
*  **Prim路径 (Prim Path):**/World/AGV_ready_03/Materials/Mtla
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_03/Materials/Mtla/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_03/Materials/Mtla/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.612, 0.725, 0.745)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_03/Materials/Mtlb1
*  **Prim路径 (Prim Path):**/World/AGV_ready_03/Materials/Mtlb1
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_03/Materials/Mtlb1/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_03/Materials/Mtlb1/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.949, 0.925, 0.933)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_03/Materials/Stainless_Steel
*  **Prim路径 (Prim Path):**/World/AGV_ready_03/Materials/Stainless_Steel
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_03/Materials/Stainless_Steel/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_03/Materials/Stainless_Steel/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.292, 0.294, 0.284)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0.431257'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_03/Materials/Metal_Aluminum_Anodized_1
*  **Prim路径 (Prim Path):**/World/AGV_ready_03/Materials/Metal_Aluminum_Anodized_1
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_03/Materials/Metal_Aluminum_Anodized_1/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_03/Materials/Metal_Aluminum_Anodized_1/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.260, 0.269, 0.282)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0.309883'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0'


---


### /World/AGV_ready_03/Materials/Metal_Aluminum_Anodized_2
*  **Prim路径 (Prim Path):**/World/AGV_ready_03/Materials/Metal_Aluminum_Anodized_2
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_03/Materials/Metal_Aluminum_Anodized_2/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_03/Materials/Metal_Aluminum_Anodized_2/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.792, 0.820, 0.859)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_03/Materials/basic_gray_plastic
*  **Prim路径 (Prim Path):**/World/AGV_ready_03/Materials/basic_gray_plastic
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_03/Materials/basic_gray_plastic/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_03/Materials/basic_gray_plastic/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0.297745'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0.115685'


---


### /World/AGV_ready_03/Materials/texture
*  **Prim路径 (Prim Path):**/World/AGV_ready_03/Materials/texture
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_03/Materials/texture/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_03/Materials/texture/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.294, 0.294, 0.294)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_04/Materials/ASELSAN_CATS_04
*  **Prim路径 (Prim Path):**/World/AGV_ready_04/Materials/ASELSAN_CATS_04
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_04/Materials/ASELSAN_CATS_04/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_04/Materials/ASELSAN_CATS_04/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.158, 0.158, 0.158)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_04/Materials/ASELSAN_CATS_04_2
*  **Prim路径 (Prim Path):**/World/AGV_ready_04/Materials/ASELSAN_CATS_04_2
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_04/Materials/ASELSAN_CATS_04_2/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_04/Materials/ASELSAN_CATS_04_2/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.769, 0.773, 0.749)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_04/Materials/ASELSAN_CATS_13
*  **Prim路径 (Prim Path):**/World/AGV_ready_04/Materials/ASELSAN_CATS_13
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_04/Materials/ASELSAN_CATS_13/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_04/Materials/ASELSAN_CATS_13/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.706, 0.718, 0.729)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_04/Materials/Color_000
*  **Prim路径 (Prim Path):**/World/AGV_ready_04/Materials/Color_000
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_04/Materials/Color_000/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_04/Materials/Color_000/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(1.000, 1.000, 1.000)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_04/Materials/Color_A05
*  **Prim路径 (Prim Path):**/World/AGV_ready_04/Materials/Color_A05
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_04/Materials/Color_A05/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_04/Materials/Color_A05/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(1.000, 0.000, 0.000)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0.959234'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0'


---


### /World/AGV_ready_04/Materials/Color_A06
*  **Prim路径 (Prim Path):**/World/AGV_ready_04/Materials/Color_A06
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_04/Materials/Color_A06/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_04/Materials/Color_A06/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.800, 0.000, 0.000)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_04/Materials/Color_B05
*  **Prim路径 (Prim Path):**/World/AGV_ready_04/Materials/Color_B05
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_04/Materials/Color_B05/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_04/Materials/Color_B05/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(1.000, 0.247, 0.000)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '1'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0'


---


### /World/AGV_ready_04/Materials/Color_E02
*  **Prim路径 (Prim Path):**/World/AGV_ready_04/Materials/Color_E02
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_04/Materials/Color_E02/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_04/Materials/Color_E02/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(1.000, 1.000, 0.196)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_04/Materials/Color_E05
*  **Prim路径 (Prim Path):**/World/AGV_ready_04/Materials/Color_E05
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_04/Materials/Color_E05/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_04/Materials/Color_E05/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(1.000, 0.910, 0.000)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0.625455'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0.133891'


---


### /World/AGV_ready_04/Materials/Color_F06
*  **Prim路径 (Prim Path):**/World/AGV_ready_04/Materials/Color_F06
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_04/Materials/Color_F06/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_04/Materials/Color_F06/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.400, 0.800, 0.000)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_04/Materials/Color_G03
*  **Prim路径 (Prim Path):**/World/AGV_ready_04/Materials/Color_G03
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_04/Materials/Color_G03/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_04/Materials/Color_G03/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.396, 1.000, 0.396)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_04/Materials/Color_M02
*  **Prim路径 (Prim Path):**/World/AGV_ready_04/Materials/Color_M02
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_04/Materials/Color_M02/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_04/Materials/Color_M02/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.776, 0.776, 0.776)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_04/Materials/Color_M03
*  **Prim路径 (Prim Path):**/World/AGV_ready_04/Materials/Color_M03
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_04/Materials/Color_M03/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_04/Materials/Color_M03/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.667, 0.667, 0.667)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_04/Materials/Mtl39
*  **Prim路径 (Prim Path):**/World/AGV_ready_04/Materials/Mtl39
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_04/Materials/Mtl39/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_04/Materials/Mtl39/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.494, 0.494, 0.494)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_04/Materials/Mtl6
*  **Prim路径 (Prim Path):**/World/AGV_ready_04/Materials/Mtl6
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_04/Materials/Mtl6/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_04/Materials/Mtl6/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f]
               *   Connected: '/World/AGV_ready_04/Materials/Mtl6/tex_base.outputs:rgb' @ '/World/AGV_ready_04/Materials/Mtl6/tex_base'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/Mtl6_baseColor.jpg'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'
       *   '/World/AGV_ready_04/Materials/Mtl6/tex_base' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/Mtl6_baseColor.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
           *   'file' [asset] = '0/Mtl6_baseColor.jpg'
           *   'st' [float2]
               *   Connected: '/World/AGV_ready_04/Materials/Mtl6/uvset0.outputs:result' @ '/World/AGV_ready_04/Materials/Mtl6/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/AGV_ready_04/Materials/Mtl6/uvset0' (ID: 'UsdPrimvarReader_float2')
       *   Implementation: 'id'


---


### /World/AGV_ready_04/Materials/Mtl9
*  **Prim路径 (Prim Path):**/World/AGV_ready_04/Materials/Mtl9
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_04/Materials/Mtl9/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_04/Materials/Mtl9/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.514, 1.000, 0.000)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_04/Materials/Silver
*  **Prim路径 (Prim Path):**/World/AGV_ready_04/Materials/Silver
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_04/Materials/Silver/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_04/Materials/Silver/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.753, 0.753, 0.753)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_04/Materials/material
*  **Prim路径 (Prim Path):**/World/AGV_ready_04/Materials/material
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_04/Materials/material/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_04/Materials/material/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f]
               *   Connected: '/World/AGV_ready_04/Materials/material/tex_base.outputs:rgb' @ '/World/AGV_ready_04/Materials/material/tex_base'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/material_baseColor.jpg'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'
       *   '/World/AGV_ready_04/Materials/material/tex_base' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/material_baseColor.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
           *   'file' [asset] = '0/material_baseColor.jpg'
           *   'st' [float2]
               *   Connected: '/World/AGV_ready_04/Materials/material/uvset0.outputs:result' @ '/World/AGV_ready_04/Materials/material/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/AGV_ready_04/Materials/material/uvset0' (ID: 'UsdPrimvarReader_float2')
       *   Implementation: 'id'


---


### /World/AGV_ready_04/Materials/cash_register_keys
*  **Prim路径 (Prim Path):**/World/AGV_ready_04/Materials/cash_register_keys
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_04/Materials/cash_register_keys/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_04/Materials/cash_register_keys/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.976, 0.992, 0.973)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_04/Materials/Chris_Shoe_Sole
*  **Prim路径 (Prim Path):**/World/AGV_ready_04/Materials/Chris_Shoe_Sole
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_04/Materials/Chris_Shoe_Sole/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_04/Materials/Chris_Shoe_Sole/pbr_shader' (ID: 'UsdPreviewSurface')
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


### /World/AGV_ready_04/Materials/Color_002
*  **Prim路径 (Prim Path):**/World/AGV_ready_04/Materials/Color_002
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_04/Materials/Color_002/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_04/Materials/Color_002/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.217, 0.217, 0.217)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0.570837'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0'


---


### /World/AGV_ready_04/Materials/Color_005
*  **Prim路径 (Prim Path):**/World/AGV_ready_04/Materials/Color_005
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_04/Materials/Color_005/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_04/Materials/Color_005/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.130, 0.130, 0.130)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0.710417'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0'


---


### /World/AGV_ready_04/Materials/Color_006
*  **Prim路径 (Prim Path):**/World/AGV_ready_04/Materials/Color_006
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_04/Materials/Color_006/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_04/Materials/Color_006/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0.237059'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0'


---


### /World/AGV_ready_04/Materials/Color_008
*  **Prim路径 (Prim Path):**/World/AGV_ready_04/Materials/Color_008
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_04/Materials/Color_008/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_04/Materials/Color_008/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.118, 0.118, 0.118)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0.941027'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0'


---


### /World/AGV_ready_04/Materials/Color_A01
*  **Prim路径 (Prim Path):**/World/AGV_ready_04/Materials/Color_A01
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_04/Materials/Color_A01/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_04/Materials/Color_A01/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(1.000, 0.000, 0.000)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0.965302'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0'


---


### /World/AGV_ready_04/Materials/Color_A11
*  **Prim路径 (Prim Path):**/World/AGV_ready_04/Materials/Color_A11
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_04/Materials/Color_A11/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_04/Materials/Color_A11/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.600, 0.000, 0.000)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_04/Materials/Color_M04
*  **Prim路径 (Prim Path):**/World/AGV_ready_04/Materials/Color_M04
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_04/Materials/Color_M04/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_04/Materials/Color_M04/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.557, 0.557, 0.557)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_04/Materials/Color_M05
*  **Prim路径 (Prim Path):**/World/AGV_ready_04/Materials/Color_M05
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_04/Materials/Color_M05/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_04/Materials/Color_M05/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.447, 0.447, 0.447)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_04/Materials/Color_M06
*  **Prim路径 (Prim Path):**/World/AGV_ready_04/Materials/Color_M06
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_04/Materials/Color_M06/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_04/Materials/Color_M06/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_04/Materials/Color_M07
*  **Prim路径 (Prim Path):**/World/AGV_ready_04/Materials/Color_M07
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_04/Materials/Color_M07/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_04/Materials/Color_M07/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.227, 0.227, 0.227)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_04/Materials/Color_M09
*  **Prim路径 (Prim Path):**/World/AGV_ready_04/Materials/Color_M09
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_04/Materials/Color_M09/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_04/Materials/Color_M09/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0.340226'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0.085341'


---


### /World/AGV_ready_04/Materials/FCP_Charcoal_v2
*  **Prim路径 (Prim Path):**/World/AGV_ready_04/Materials/FCP_Charcoal_v2
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_04/Materials/FCP_Charcoal_v2/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_04/Materials/FCP_Charcoal_v2/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.216, 0.216, 0.216)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_04/Materials/FrontColor
*  **Prim路径 (Prim Path):**/World/AGV_ready_04/Materials/FrontColor
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_04/Materials/FrontColor/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_04/Materials/FrontColor/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.504, 0.504, 0.504)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0.637593'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0.218852'


---


### /World/AGV_ready_04/Materials/Light_Blue
*  **Prim路径 (Prim Path):**/World/AGV_ready_04/Materials/Light_Blue
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_04/Materials/Light_Blue/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_04/Materials/Light_Blue/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.601, 0.601, 0.601)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '1'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0.170303'


---


### /World/AGV_ready_04/Materials/M_0011_Seashell
*  **Prim路径 (Prim Path):**/World/AGV_ready_04/Materials/M_0011_Seashell
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_04/Materials/M_0011_Seashell/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_04/Materials/M_0011_Seashell/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(1.000, 0.961, 0.933)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_04/Materials/M_0131_Silver
*  **Prim路径 (Prim Path):**/World/AGV_ready_04/Materials/M_0131_Silver
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_04/Materials/M_0131_Silver/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_04/Materials/M_0131_Silver/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.242, 0.242, 0.242)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0.613318'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0'


---


### /World/AGV_ready_04/Materials/M_0134_DimGray
*  **Prim路径 (Prim Path):**/World/AGV_ready_04/Materials/M_0134_DimGray
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_04/Materials/M_0134_DimGray/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_04/Materials/M_0134_DimGray/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.412, 0.412, 0.412)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_04/Materials/M_0135_DarkGray
*  **Prim路径 (Prim Path):**/World/AGV_ready_04/Materials/M_0135_DarkGray
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_04/Materials/M_0135_DarkGray/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_04/Materials/M_0135_DarkGray/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.318, 0.318, 0.318)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_04/Materials/Metal_Silver
*  **Prim路径 (Prim Path):**/World/AGV_ready_04/Materials/Metal_Silver
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_04/Materials/Metal_Silver/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_04/Materials/Metal_Silver/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.918, 0.914, 0.933)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_04/Materials/Mtl1
*  **Prim路径 (Prim Path):**/World/AGV_ready_04/Materials/Mtl1
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_04/Materials/Mtl1/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_04/Materials/Mtl1/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.015, 0.015, 0.015)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0.255265'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_04/Materials/Mtl10
*  **Prim路径 (Prim Path):**/World/AGV_ready_04/Materials/Mtl10
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_04/Materials/Mtl10/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_04/Materials/Mtl10/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.322, 0.322, 0.322)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_04/Materials/Mtl11
*  **Prim路径 (Prim Path):**/World/AGV_ready_04/Materials/Mtl11
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_04/Materials/Mtl11/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_04/Materials/Mtl11/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.067, 0.757, 0.329)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_04/Materials/Mtl12
*  **Prim路径 (Prim Path):**/World/AGV_ready_04/Materials/Mtl12
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_04/Materials/Mtl12/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_04/Materials/Mtl12/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.502, 0.502, 0.502)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_04/Materials/Mtl13
*  **Prim路径 (Prim Path):**/World/AGV_ready_04/Materials/Mtl13
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_04/Materials/Mtl13/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_04/Materials/Mtl13/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.008, 0.514, 0.816)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_04/Materials/Mtl14
*  **Prim路径 (Prim Path):**/World/AGV_ready_04/Materials/Mtl14
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_04/Materials/Mtl14/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_04/Materials/Mtl14/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.310, 0.310, 0.310)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_04/Materials/Mtl15
*  **Prim路径 (Prim Path):**/World/AGV_ready_04/Materials/Mtl15
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_04/Materials/Mtl15/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_04/Materials/Mtl15/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.263, 0.275, 0.275)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_04/Materials/Mtl16
*  **Prim路径 (Prim Path):**/World/AGV_ready_04/Materials/Mtl16
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_04/Materials/Mtl16/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_04/Materials/Mtl16/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.698, 0.698, 0.000)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_04/Materials/Mtl17
*  **Prim路径 (Prim Path):**/World/AGV_ready_04/Materials/Mtl17
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_04/Materials/Mtl17/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_04/Materials/Mtl17/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.000, 0.863, 1.000)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_04/Materials/Mtl3
*  **Prim路径 (Prim Path):**/World/AGV_ready_04/Materials/Mtl3
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_04/Materials/Mtl3/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_04/Materials/Mtl3/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.431, 0.455, 0.498)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_04/Materials/Mtl35
*  **Prim路径 (Prim Path):**/World/AGV_ready_04/Materials/Mtl35
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_04/Materials/Mtl35/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_04/Materials/Mtl35/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.792, 0.820, 0.933)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_04/Materials/Mtl36
*  **Prim路径 (Prim Path):**/World/AGV_ready_04/Materials/Mtl36
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_04/Materials/Mtl36/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_04/Materials/Mtl36/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.667, 0.698, 0.765)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_04/Materials/Mtl37
*  **Prim路径 (Prim Path):**/World/AGV_ready_04/Materials/Mtl37
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_04/Materials/Mtl37/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_04/Materials/Mtl37/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.098, 0.098, 0.098)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_04/Materials/Mtl3a
*  **Prim路径 (Prim Path):**/World/AGV_ready_04/Materials/Mtl3a
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_04/Materials/Mtl3a/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_04/Materials/Mtl3a/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.388, 0.369, 0.322)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_04/Materials/Mtl3b
*  **Prim路径 (Prim Path):**/World/AGV_ready_04/Materials/Mtl3b
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_04/Materials/Mtl3b/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_04/Materials/Mtl3b/pbr_shader' (ID: 'UsdPreviewSurface')
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


### /World/AGV_ready_04/Materials/Mtl5
*  **Prim路径 (Prim Path):**/World/AGV_ready_04/Materials/Mtl5
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_04/Materials/Mtl5/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_04/Materials/Mtl5/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.396, 0.408, 0.467)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_04/Materials/Mtl7
*  **Prim路径 (Prim Path):**/World/AGV_ready_04/Materials/Mtl7
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_04/Materials/Mtl7/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_04/Materials/Mtl7/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.376, 0.376, 0.376)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_04/Materials/Mtl8
*  **Prim路径 (Prim Path):**/World/AGV_ready_04/Materials/Mtl8
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_04/Materials/Mtl8/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_04/Materials/Mtl8/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.173, 0.173, 0.173)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_04/Materials/Mtla
*  **Prim路径 (Prim Path):**/World/AGV_ready_04/Materials/Mtla
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_04/Materials/Mtla/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_04/Materials/Mtla/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.612, 0.725, 0.745)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_04/Materials/Mtlb1
*  **Prim路径 (Prim Path):**/World/AGV_ready_04/Materials/Mtlb1
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_04/Materials/Mtlb1/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_04/Materials/Mtlb1/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.949, 0.925, 0.933)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_04/Materials/Stainless_Steel
*  **Prim路径 (Prim Path):**/World/AGV_ready_04/Materials/Stainless_Steel
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_04/Materials/Stainless_Steel/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_04/Materials/Stainless_Steel/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.292, 0.294, 0.284)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0.431257'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_04/Materials/Metal_Aluminum_Anodized_1
*  **Prim路径 (Prim Path):**/World/AGV_ready_04/Materials/Metal_Aluminum_Anodized_1
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_04/Materials/Metal_Aluminum_Anodized_1/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_04/Materials/Metal_Aluminum_Anodized_1/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.260, 0.269, 0.282)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0.309883'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0'


---


### /World/AGV_ready_04/Materials/Metal_Aluminum_Anodized_2
*  **Prim路径 (Prim Path):**/World/AGV_ready_04/Materials/Metal_Aluminum_Anodized_2
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_04/Materials/Metal_Aluminum_Anodized_2/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_04/Materials/Metal_Aluminum_Anodized_2/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.792, 0.820, 0.859)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_04/Materials/basic_gray_plastic
*  **Prim路径 (Prim Path):**/World/AGV_ready_04/Materials/basic_gray_plastic
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_04/Materials/basic_gray_plastic/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_04/Materials/basic_gray_plastic/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0.297745'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0.115685'


---


### /World/AGV_ready_04/Materials/texture
*  **Prim路径 (Prim Path):**/World/AGV_ready_04/Materials/texture
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_04/Materials/texture/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_04/Materials/texture/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.294, 0.294, 0.294)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_05/Materials/ASELSAN_CATS_04
*  **Prim路径 (Prim Path):**/World/AGV_ready_05/Materials/ASELSAN_CATS_04
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_05/Materials/ASELSAN_CATS_04/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_05/Materials/ASELSAN_CATS_04/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.158, 0.158, 0.158)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_05/Materials/ASELSAN_CATS_04_2
*  **Prim路径 (Prim Path):**/World/AGV_ready_05/Materials/ASELSAN_CATS_04_2
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_05/Materials/ASELSAN_CATS_04_2/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_05/Materials/ASELSAN_CATS_04_2/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.769, 0.773, 0.749)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_05/Materials/ASELSAN_CATS_13
*  **Prim路径 (Prim Path):**/World/AGV_ready_05/Materials/ASELSAN_CATS_13
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_05/Materials/ASELSAN_CATS_13/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_05/Materials/ASELSAN_CATS_13/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.706, 0.718, 0.729)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_05/Materials/Color_000
*  **Prim路径 (Prim Path):**/World/AGV_ready_05/Materials/Color_000
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_05/Materials/Color_000/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_05/Materials/Color_000/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(1.000, 1.000, 1.000)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_05/Materials/Color_A05
*  **Prim路径 (Prim Path):**/World/AGV_ready_05/Materials/Color_A05
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_05/Materials/Color_A05/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_05/Materials/Color_A05/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(1.000, 0.000, 0.000)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0.959234'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0'


---


### /World/AGV_ready_05/Materials/Color_A06
*  **Prim路径 (Prim Path):**/World/AGV_ready_05/Materials/Color_A06
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_05/Materials/Color_A06/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_05/Materials/Color_A06/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.800, 0.000, 0.000)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_05/Materials/Color_B05
*  **Prim路径 (Prim Path):**/World/AGV_ready_05/Materials/Color_B05
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_05/Materials/Color_B05/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_05/Materials/Color_B05/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(1.000, 0.247, 0.000)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '1'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0'


---


### /World/AGV_ready_05/Materials/Color_E02
*  **Prim路径 (Prim Path):**/World/AGV_ready_05/Materials/Color_E02
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_05/Materials/Color_E02/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_05/Materials/Color_E02/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(1.000, 1.000, 0.196)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_05/Materials/Color_E05
*  **Prim路径 (Prim Path):**/World/AGV_ready_05/Materials/Color_E05
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_05/Materials/Color_E05/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_05/Materials/Color_E05/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(1.000, 0.910, 0.000)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0.625455'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0.133891'


---


### /World/AGV_ready_05/Materials/Color_F06
*  **Prim路径 (Prim Path):**/World/AGV_ready_05/Materials/Color_F06
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_05/Materials/Color_F06/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_05/Materials/Color_F06/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.400, 0.800, 0.000)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_05/Materials/Color_G03
*  **Prim路径 (Prim Path):**/World/AGV_ready_05/Materials/Color_G03
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_05/Materials/Color_G03/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_05/Materials/Color_G03/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.396, 1.000, 0.396)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_05/Materials/Color_M02
*  **Prim路径 (Prim Path):**/World/AGV_ready_05/Materials/Color_M02
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_05/Materials/Color_M02/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_05/Materials/Color_M02/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.776, 0.776, 0.776)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_05/Materials/Color_M03
*  **Prim路径 (Prim Path):**/World/AGV_ready_05/Materials/Color_M03
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_05/Materials/Color_M03/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_05/Materials/Color_M03/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.667, 0.667, 0.667)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_05/Materials/Mtl39
*  **Prim路径 (Prim Path):**/World/AGV_ready_05/Materials/Mtl39
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_05/Materials/Mtl39/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_05/Materials/Mtl39/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.494, 0.494, 0.494)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_05/Materials/Mtl6
*  **Prim路径 (Prim Path):**/World/AGV_ready_05/Materials/Mtl6
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_05/Materials/Mtl6/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_05/Materials/Mtl6/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f]
               *   Connected: '/World/AGV_ready_05/Materials/Mtl6/tex_base.outputs:rgb' @ '/World/AGV_ready_05/Materials/Mtl6/tex_base'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/Mtl6_baseColor.jpg'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'
       *   '/World/AGV_ready_05/Materials/Mtl6/tex_base' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/Mtl6_baseColor.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
           *   'file' [asset] = '0/Mtl6_baseColor.jpg'
           *   'st' [float2]
               *   Connected: '/World/AGV_ready_05/Materials/Mtl6/uvset0.outputs:result' @ '/World/AGV_ready_05/Materials/Mtl6/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/AGV_ready_05/Materials/Mtl6/uvset0' (ID: 'UsdPrimvarReader_float2')
       *   Implementation: 'id'


---


### /World/AGV_ready_05/Materials/Mtl9
*  **Prim路径 (Prim Path):**/World/AGV_ready_05/Materials/Mtl9
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_05/Materials/Mtl9/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_05/Materials/Mtl9/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.514, 1.000, 0.000)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_05/Materials/Silver
*  **Prim路径 (Prim Path):**/World/AGV_ready_05/Materials/Silver
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_05/Materials/Silver/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_05/Materials/Silver/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.753, 0.753, 0.753)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_05/Materials/material
*  **Prim路径 (Prim Path):**/World/AGV_ready_05/Materials/material
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_05/Materials/material/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_05/Materials/material/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f]
               *   Connected: '/World/AGV_ready_05/Materials/material/tex_base.outputs:rgb' @ '/World/AGV_ready_05/Materials/material/tex_base'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/material_baseColor.jpg'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'
       *   '/World/AGV_ready_05/Materials/material/tex_base' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/material_baseColor.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
           *   'file' [asset] = '0/material_baseColor.jpg'
           *   'st' [float2]
               *   Connected: '/World/AGV_ready_05/Materials/material/uvset0.outputs:result' @ '/World/AGV_ready_05/Materials/material/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/AGV_ready_05/Materials/material/uvset0' (ID: 'UsdPrimvarReader_float2')
       *   Implementation: 'id'


---


### /World/AGV_ready_05/Materials/cash_register_keys
*  **Prim路径 (Prim Path):**/World/AGV_ready_05/Materials/cash_register_keys
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_05/Materials/cash_register_keys/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_05/Materials/cash_register_keys/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.976, 0.992, 0.973)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_05/Materials/Chris_Shoe_Sole
*  **Prim路径 (Prim Path):**/World/AGV_ready_05/Materials/Chris_Shoe_Sole
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_05/Materials/Chris_Shoe_Sole/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_05/Materials/Chris_Shoe_Sole/pbr_shader' (ID: 'UsdPreviewSurface')
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


### /World/AGV_ready_05/Materials/Color_002
*  **Prim路径 (Prim Path):**/World/AGV_ready_05/Materials/Color_002
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_05/Materials/Color_002/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_05/Materials/Color_002/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.217, 0.217, 0.217)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0.570837'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0'


---


### /World/AGV_ready_05/Materials/Color_005
*  **Prim路径 (Prim Path):**/World/AGV_ready_05/Materials/Color_005
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_05/Materials/Color_005/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_05/Materials/Color_005/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.130, 0.130, 0.130)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0.710417'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0'


---


### /World/AGV_ready_05/Materials/Color_006
*  **Prim路径 (Prim Path):**/World/AGV_ready_05/Materials/Color_006
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_05/Materials/Color_006/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_05/Materials/Color_006/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0.237059'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0'


---


### /World/AGV_ready_05/Materials/Color_008
*  **Prim路径 (Prim Path):**/World/AGV_ready_05/Materials/Color_008
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_05/Materials/Color_008/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_05/Materials/Color_008/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.118, 0.118, 0.118)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0.941027'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0'


---


### /World/AGV_ready_05/Materials/Color_A01
*  **Prim路径 (Prim Path):**/World/AGV_ready_05/Materials/Color_A01
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_05/Materials/Color_A01/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_05/Materials/Color_A01/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(1.000, 0.000, 0.000)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0.965302'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0'


---


### /World/AGV_ready_05/Materials/Color_A11
*  **Prim路径 (Prim Path):**/World/AGV_ready_05/Materials/Color_A11
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_05/Materials/Color_A11/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_05/Materials/Color_A11/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.600, 0.000, 0.000)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_05/Materials/Color_M04
*  **Prim路径 (Prim Path):**/World/AGV_ready_05/Materials/Color_M04
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_05/Materials/Color_M04/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_05/Materials/Color_M04/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.557, 0.557, 0.557)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_05/Materials/Color_M05
*  **Prim路径 (Prim Path):**/World/AGV_ready_05/Materials/Color_M05
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_05/Materials/Color_M05/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_05/Materials/Color_M05/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.447, 0.447, 0.447)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_05/Materials/Color_M06
*  **Prim路径 (Prim Path):**/World/AGV_ready_05/Materials/Color_M06
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_05/Materials/Color_M06/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_05/Materials/Color_M06/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_05/Materials/Color_M07
*  **Prim路径 (Prim Path):**/World/AGV_ready_05/Materials/Color_M07
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_05/Materials/Color_M07/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_05/Materials/Color_M07/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.227, 0.227, 0.227)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_05/Materials/Color_M09
*  **Prim路径 (Prim Path):**/World/AGV_ready_05/Materials/Color_M09
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_05/Materials/Color_M09/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_05/Materials/Color_M09/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0.340226'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0.085341'


---


### /World/AGV_ready_05/Materials/FCP_Charcoal_v2
*  **Prim路径 (Prim Path):**/World/AGV_ready_05/Materials/FCP_Charcoal_v2
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_05/Materials/FCP_Charcoal_v2/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_05/Materials/FCP_Charcoal_v2/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.216, 0.216, 0.216)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_05/Materials/FrontColor
*  **Prim路径 (Prim Path):**/World/AGV_ready_05/Materials/FrontColor
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_05/Materials/FrontColor/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_05/Materials/FrontColor/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.504, 0.504, 0.504)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0.637593'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0.218852'


---


### /World/AGV_ready_05/Materials/Light_Blue
*  **Prim路径 (Prim Path):**/World/AGV_ready_05/Materials/Light_Blue
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_05/Materials/Light_Blue/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_05/Materials/Light_Blue/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.601, 0.601, 0.601)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '1'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0.170303'


---


### /World/AGV_ready_05/Materials/M_0011_Seashell
*  **Prim路径 (Prim Path):**/World/AGV_ready_05/Materials/M_0011_Seashell
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_05/Materials/M_0011_Seashell/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_05/Materials/M_0011_Seashell/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(1.000, 0.961, 0.933)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_05/Materials/M_0131_Silver
*  **Prim路径 (Prim Path):**/World/AGV_ready_05/Materials/M_0131_Silver
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_05/Materials/M_0131_Silver/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_05/Materials/M_0131_Silver/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.242, 0.242, 0.242)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0.613318'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0'


---


### /World/AGV_ready_05/Materials/M_0134_DimGray
*  **Prim路径 (Prim Path):**/World/AGV_ready_05/Materials/M_0134_DimGray
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_05/Materials/M_0134_DimGray/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_05/Materials/M_0134_DimGray/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.412, 0.412, 0.412)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_05/Materials/M_0135_DarkGray
*  **Prim路径 (Prim Path):**/World/AGV_ready_05/Materials/M_0135_DarkGray
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_05/Materials/M_0135_DarkGray/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_05/Materials/M_0135_DarkGray/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.318, 0.318, 0.318)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_05/Materials/Metal_Silver
*  **Prim路径 (Prim Path):**/World/AGV_ready_05/Materials/Metal_Silver
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_05/Materials/Metal_Silver/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_05/Materials/Metal_Silver/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.918, 0.914, 0.933)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_05/Materials/Mtl1
*  **Prim路径 (Prim Path):**/World/AGV_ready_05/Materials/Mtl1
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_05/Materials/Mtl1/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_05/Materials/Mtl1/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.015, 0.015, 0.015)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0.255265'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_05/Materials/Mtl10
*  **Prim路径 (Prim Path):**/World/AGV_ready_05/Materials/Mtl10
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_05/Materials/Mtl10/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_05/Materials/Mtl10/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.322, 0.322, 0.322)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_05/Materials/Mtl11
*  **Prim路径 (Prim Path):**/World/AGV_ready_05/Materials/Mtl11
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_05/Materials/Mtl11/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_05/Materials/Mtl11/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.067, 0.757, 0.329)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_05/Materials/Mtl12
*  **Prim路径 (Prim Path):**/World/AGV_ready_05/Materials/Mtl12
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_05/Materials/Mtl12/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_05/Materials/Mtl12/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.502, 0.502, 0.502)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_05/Materials/Mtl13
*  **Prim路径 (Prim Path):**/World/AGV_ready_05/Materials/Mtl13
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_05/Materials/Mtl13/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_05/Materials/Mtl13/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.008, 0.514, 0.816)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_05/Materials/Mtl14
*  **Prim路径 (Prim Path):**/World/AGV_ready_05/Materials/Mtl14
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_05/Materials/Mtl14/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_05/Materials/Mtl14/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.310, 0.310, 0.310)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_05/Materials/Mtl15
*  **Prim路径 (Prim Path):**/World/AGV_ready_05/Materials/Mtl15
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_05/Materials/Mtl15/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_05/Materials/Mtl15/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.263, 0.275, 0.275)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_05/Materials/Mtl16
*  **Prim路径 (Prim Path):**/World/AGV_ready_05/Materials/Mtl16
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_05/Materials/Mtl16/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_05/Materials/Mtl16/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.698, 0.698, 0.000)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_05/Materials/Mtl17
*  **Prim路径 (Prim Path):**/World/AGV_ready_05/Materials/Mtl17
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_05/Materials/Mtl17/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_05/Materials/Mtl17/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.000, 0.863, 1.000)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_05/Materials/Mtl3
*  **Prim路径 (Prim Path):**/World/AGV_ready_05/Materials/Mtl3
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_05/Materials/Mtl3/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_05/Materials/Mtl3/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.431, 0.455, 0.498)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_05/Materials/Mtl35
*  **Prim路径 (Prim Path):**/World/AGV_ready_05/Materials/Mtl35
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_05/Materials/Mtl35/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_05/Materials/Mtl35/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.792, 0.820, 0.933)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_05/Materials/Mtl36
*  **Prim路径 (Prim Path):**/World/AGV_ready_05/Materials/Mtl36
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_05/Materials/Mtl36/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_05/Materials/Mtl36/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.667, 0.698, 0.765)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_05/Materials/Mtl37
*  **Prim路径 (Prim Path):**/World/AGV_ready_05/Materials/Mtl37
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_05/Materials/Mtl37/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_05/Materials/Mtl37/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.098, 0.098, 0.098)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_05/Materials/Mtl3a
*  **Prim路径 (Prim Path):**/World/AGV_ready_05/Materials/Mtl3a
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_05/Materials/Mtl3a/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_05/Materials/Mtl3a/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.388, 0.369, 0.322)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_05/Materials/Mtl3b
*  **Prim路径 (Prim Path):**/World/AGV_ready_05/Materials/Mtl3b
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_05/Materials/Mtl3b/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_05/Materials/Mtl3b/pbr_shader' (ID: 'UsdPreviewSurface')
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


### /World/AGV_ready_05/Materials/Mtl5
*  **Prim路径 (Prim Path):**/World/AGV_ready_05/Materials/Mtl5
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_05/Materials/Mtl5/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_05/Materials/Mtl5/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.396, 0.408, 0.467)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_05/Materials/Mtl7
*  **Prim路径 (Prim Path):**/World/AGV_ready_05/Materials/Mtl7
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_05/Materials/Mtl7/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_05/Materials/Mtl7/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.376, 0.376, 0.376)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_05/Materials/Mtl8
*  **Prim路径 (Prim Path):**/World/AGV_ready_05/Materials/Mtl8
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_05/Materials/Mtl8/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_05/Materials/Mtl8/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.173, 0.173, 0.173)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_05/Materials/Mtla
*  **Prim路径 (Prim Path):**/World/AGV_ready_05/Materials/Mtla
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_05/Materials/Mtla/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_05/Materials/Mtla/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.612, 0.725, 0.745)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_05/Materials/Mtlb1
*  **Prim路径 (Prim Path):**/World/AGV_ready_05/Materials/Mtlb1
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_05/Materials/Mtlb1/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_05/Materials/Mtlb1/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.949, 0.925, 0.933)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_05/Materials/Stainless_Steel
*  **Prim路径 (Prim Path):**/World/AGV_ready_05/Materials/Stainless_Steel
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_05/Materials/Stainless_Steel/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_05/Materials/Stainless_Steel/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.292, 0.294, 0.284)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0.431257'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_05/Materials/Metal_Aluminum_Anodized_1
*  **Prim路径 (Prim Path):**/World/AGV_ready_05/Materials/Metal_Aluminum_Anodized_1
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_05/Materials/Metal_Aluminum_Anodized_1/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_05/Materials/Metal_Aluminum_Anodized_1/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.260, 0.269, 0.282)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0.309883'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0'


---


### /World/AGV_ready_05/Materials/Metal_Aluminum_Anodized_2
*  **Prim路径 (Prim Path):**/World/AGV_ready_05/Materials/Metal_Aluminum_Anodized_2
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_05/Materials/Metal_Aluminum_Anodized_2/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_05/Materials/Metal_Aluminum_Anodized_2/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.792, 0.820, 0.859)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_05/Materials/basic_gray_plastic
*  **Prim路径 (Prim Path):**/World/AGV_ready_05/Materials/basic_gray_plastic
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_05/Materials/basic_gray_plastic/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_05/Materials/basic_gray_plastic/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0.297745'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0.115685'


---


### /World/AGV_ready_05/Materials/texture
*  **Prim路径 (Prim Path):**/World/AGV_ready_05/Materials/texture
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_05/Materials/texture/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_05/Materials/texture/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.294, 0.294, 0.294)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_06/Materials/ASELSAN_CATS_04
*  **Prim路径 (Prim Path):**/World/AGV_ready_06/Materials/ASELSAN_CATS_04
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_06/Materials/ASELSAN_CATS_04/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_06/Materials/ASELSAN_CATS_04/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.158, 0.158, 0.158)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_06/Materials/ASELSAN_CATS_04_2
*  **Prim路径 (Prim Path):**/World/AGV_ready_06/Materials/ASELSAN_CATS_04_2
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_06/Materials/ASELSAN_CATS_04_2/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_06/Materials/ASELSAN_CATS_04_2/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.769, 0.773, 0.749)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_06/Materials/ASELSAN_CATS_13
*  **Prim路径 (Prim Path):**/World/AGV_ready_06/Materials/ASELSAN_CATS_13
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_06/Materials/ASELSAN_CATS_13/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_06/Materials/ASELSAN_CATS_13/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.706, 0.718, 0.729)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_06/Materials/Color_000
*  **Prim路径 (Prim Path):**/World/AGV_ready_06/Materials/Color_000
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_06/Materials/Color_000/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_06/Materials/Color_000/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(1.000, 1.000, 1.000)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_06/Materials/Color_A05
*  **Prim路径 (Prim Path):**/World/AGV_ready_06/Materials/Color_A05
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_06/Materials/Color_A05/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_06/Materials/Color_A05/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(1.000, 0.000, 0.000)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0.959234'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0'


---


### /World/AGV_ready_06/Materials/Color_A06
*  **Prim路径 (Prim Path):**/World/AGV_ready_06/Materials/Color_A06
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_06/Materials/Color_A06/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_06/Materials/Color_A06/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.800, 0.000, 0.000)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_06/Materials/Color_B05
*  **Prim路径 (Prim Path):**/World/AGV_ready_06/Materials/Color_B05
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_06/Materials/Color_B05/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_06/Materials/Color_B05/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(1.000, 0.247, 0.000)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '1'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0'


---


### /World/AGV_ready_06/Materials/Color_E02
*  **Prim路径 (Prim Path):**/World/AGV_ready_06/Materials/Color_E02
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_06/Materials/Color_E02/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_06/Materials/Color_E02/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(1.000, 1.000, 0.196)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_06/Materials/Color_E05
*  **Prim路径 (Prim Path):**/World/AGV_ready_06/Materials/Color_E05
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_06/Materials/Color_E05/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_06/Materials/Color_E05/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(1.000, 0.910, 0.000)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0.625455'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0.133891'


---


### /World/AGV_ready_06/Materials/Color_F06
*  **Prim路径 (Prim Path):**/World/AGV_ready_06/Materials/Color_F06
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_06/Materials/Color_F06/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_06/Materials/Color_F06/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.400, 0.800, 0.000)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_06/Materials/Color_G03
*  **Prim路径 (Prim Path):**/World/AGV_ready_06/Materials/Color_G03
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_06/Materials/Color_G03/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_06/Materials/Color_G03/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.396, 1.000, 0.396)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_06/Materials/Color_M02
*  **Prim路径 (Prim Path):**/World/AGV_ready_06/Materials/Color_M02
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_06/Materials/Color_M02/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_06/Materials/Color_M02/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.776, 0.776, 0.776)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_06/Materials/Color_M03
*  **Prim路径 (Prim Path):**/World/AGV_ready_06/Materials/Color_M03
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_06/Materials/Color_M03/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_06/Materials/Color_M03/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.667, 0.667, 0.667)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_06/Materials/Mtl39
*  **Prim路径 (Prim Path):**/World/AGV_ready_06/Materials/Mtl39
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_06/Materials/Mtl39/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_06/Materials/Mtl39/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.494, 0.494, 0.494)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_06/Materials/Mtl6
*  **Prim路径 (Prim Path):**/World/AGV_ready_06/Materials/Mtl6
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_06/Materials/Mtl6/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_06/Materials/Mtl6/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f]
               *   Connected: '/World/AGV_ready_06/Materials/Mtl6/tex_base.outputs:rgb' @ '/World/AGV_ready_06/Materials/Mtl6/tex_base'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/Mtl6_baseColor.jpg'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'
       *   '/World/AGV_ready_06/Materials/Mtl6/tex_base' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/Mtl6_baseColor.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
           *   'file' [asset] = '0/Mtl6_baseColor.jpg'
           *   'st' [float2]
               *   Connected: '/World/AGV_ready_06/Materials/Mtl6/uvset0.outputs:result' @ '/World/AGV_ready_06/Materials/Mtl6/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/AGV_ready_06/Materials/Mtl6/uvset0' (ID: 'UsdPrimvarReader_float2')
       *   Implementation: 'id'


---


### /World/AGV_ready_06/Materials/Mtl9
*  **Prim路径 (Prim Path):**/World/AGV_ready_06/Materials/Mtl9
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_06/Materials/Mtl9/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_06/Materials/Mtl9/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.514, 1.000, 0.000)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_06/Materials/Silver
*  **Prim路径 (Prim Path):**/World/AGV_ready_06/Materials/Silver
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_06/Materials/Silver/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_06/Materials/Silver/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.753, 0.753, 0.753)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_06/Materials/material
*  **Prim路径 (Prim Path):**/World/AGV_ready_06/Materials/material
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_06/Materials/material/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_06/Materials/material/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f]
               *   Connected: '/World/AGV_ready_06/Materials/material/tex_base.outputs:rgb' @ '/World/AGV_ready_06/Materials/material/tex_base'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/material_baseColor.jpg'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'
       *   '/World/AGV_ready_06/Materials/material/tex_base' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/material_baseColor.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
           *   'file' [asset] = '0/material_baseColor.jpg'
           *   'st' [float2]
               *   Connected: '/World/AGV_ready_06/Materials/material/uvset0.outputs:result' @ '/World/AGV_ready_06/Materials/material/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/AGV_ready_06/Materials/material/uvset0' (ID: 'UsdPrimvarReader_float2')
       *   Implementation: 'id'


---


### /World/AGV_ready_06/Materials/cash_register_keys
*  **Prim路径 (Prim Path):**/World/AGV_ready_06/Materials/cash_register_keys
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_06/Materials/cash_register_keys/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_06/Materials/cash_register_keys/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.976, 0.992, 0.973)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_06/Materials/Chris_Shoe_Sole
*  **Prim路径 (Prim Path):**/World/AGV_ready_06/Materials/Chris_Shoe_Sole
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_06/Materials/Chris_Shoe_Sole/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_06/Materials/Chris_Shoe_Sole/pbr_shader' (ID: 'UsdPreviewSurface')
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


### /World/AGV_ready_06/Materials/Color_002
*  **Prim路径 (Prim Path):**/World/AGV_ready_06/Materials/Color_002
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_06/Materials/Color_002/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_06/Materials/Color_002/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.217, 0.217, 0.217)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0.570837'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0'


---


### /World/AGV_ready_06/Materials/Color_005
*  **Prim路径 (Prim Path):**/World/AGV_ready_06/Materials/Color_005
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_06/Materials/Color_005/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_06/Materials/Color_005/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.130, 0.130, 0.130)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0.710417'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0'


---


### /World/AGV_ready_06/Materials/Color_006
*  **Prim路径 (Prim Path):**/World/AGV_ready_06/Materials/Color_006
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_06/Materials/Color_006/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_06/Materials/Color_006/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0.237059'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0'


---


### /World/AGV_ready_06/Materials/Color_008
*  **Prim路径 (Prim Path):**/World/AGV_ready_06/Materials/Color_008
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_06/Materials/Color_008/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_06/Materials/Color_008/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.118, 0.118, 0.118)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0.941027'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0'


---


### /World/AGV_ready_06/Materials/Color_A01
*  **Prim路径 (Prim Path):**/World/AGV_ready_06/Materials/Color_A01
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_06/Materials/Color_A01/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_06/Materials/Color_A01/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(1.000, 0.000, 0.000)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0.965302'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0'


---


### /World/AGV_ready_06/Materials/Color_A11
*  **Prim路径 (Prim Path):**/World/AGV_ready_06/Materials/Color_A11
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_06/Materials/Color_A11/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_06/Materials/Color_A11/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.600, 0.000, 0.000)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_06/Materials/Color_M04
*  **Prim路径 (Prim Path):**/World/AGV_ready_06/Materials/Color_M04
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_06/Materials/Color_M04/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_06/Materials/Color_M04/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.557, 0.557, 0.557)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_06/Materials/Color_M05
*  **Prim路径 (Prim Path):**/World/AGV_ready_06/Materials/Color_M05
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_06/Materials/Color_M05/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_06/Materials/Color_M05/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.447, 0.447, 0.447)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_06/Materials/Color_M06
*  **Prim路径 (Prim Path):**/World/AGV_ready_06/Materials/Color_M06
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_06/Materials/Color_M06/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_06/Materials/Color_M06/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_06/Materials/Color_M07
*  **Prim路径 (Prim Path):**/World/AGV_ready_06/Materials/Color_M07
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_06/Materials/Color_M07/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_06/Materials/Color_M07/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.227, 0.227, 0.227)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_06/Materials/Color_M09
*  **Prim路径 (Prim Path):**/World/AGV_ready_06/Materials/Color_M09
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_06/Materials/Color_M09/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_06/Materials/Color_M09/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0.340226'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0.085341'


---


### /World/AGV_ready_06/Materials/FCP_Charcoal_v2
*  **Prim路径 (Prim Path):**/World/AGV_ready_06/Materials/FCP_Charcoal_v2
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_06/Materials/FCP_Charcoal_v2/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_06/Materials/FCP_Charcoal_v2/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.216, 0.216, 0.216)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_06/Materials/FrontColor
*  **Prim路径 (Prim Path):**/World/AGV_ready_06/Materials/FrontColor
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_06/Materials/FrontColor/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_06/Materials/FrontColor/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.504, 0.504, 0.504)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0.637593'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0.218852'


---


### /World/AGV_ready_06/Materials/Light_Blue
*  **Prim路径 (Prim Path):**/World/AGV_ready_06/Materials/Light_Blue
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_06/Materials/Light_Blue/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_06/Materials/Light_Blue/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.601, 0.601, 0.601)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '1'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0.170303'


---


### /World/AGV_ready_06/Materials/M_0011_Seashell
*  **Prim路径 (Prim Path):**/World/AGV_ready_06/Materials/M_0011_Seashell
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_06/Materials/M_0011_Seashell/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_06/Materials/M_0011_Seashell/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(1.000, 0.961, 0.933)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_06/Materials/M_0131_Silver
*  **Prim路径 (Prim Path):**/World/AGV_ready_06/Materials/M_0131_Silver
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_06/Materials/M_0131_Silver/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_06/Materials/M_0131_Silver/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.242, 0.242, 0.242)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0.613318'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0'


---


### /World/AGV_ready_06/Materials/M_0134_DimGray
*  **Prim路径 (Prim Path):**/World/AGV_ready_06/Materials/M_0134_DimGray
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_06/Materials/M_0134_DimGray/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_06/Materials/M_0134_DimGray/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.412, 0.412, 0.412)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_06/Materials/M_0135_DarkGray
*  **Prim路径 (Prim Path):**/World/AGV_ready_06/Materials/M_0135_DarkGray
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_06/Materials/M_0135_DarkGray/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_06/Materials/M_0135_DarkGray/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.318, 0.318, 0.318)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_06/Materials/Metal_Silver
*  **Prim路径 (Prim Path):**/World/AGV_ready_06/Materials/Metal_Silver
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_06/Materials/Metal_Silver/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_06/Materials/Metal_Silver/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.918, 0.914, 0.933)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_06/Materials/Mtl1
*  **Prim路径 (Prim Path):**/World/AGV_ready_06/Materials/Mtl1
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_06/Materials/Mtl1/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_06/Materials/Mtl1/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.015, 0.015, 0.015)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0.255265'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_06/Materials/Mtl10
*  **Prim路径 (Prim Path):**/World/AGV_ready_06/Materials/Mtl10
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_06/Materials/Mtl10/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_06/Materials/Mtl10/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.322, 0.322, 0.322)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_06/Materials/Mtl11
*  **Prim路径 (Prim Path):**/World/AGV_ready_06/Materials/Mtl11
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_06/Materials/Mtl11/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_06/Materials/Mtl11/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.067, 0.757, 0.329)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_06/Materials/Mtl12
*  **Prim路径 (Prim Path):**/World/AGV_ready_06/Materials/Mtl12
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_06/Materials/Mtl12/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_06/Materials/Mtl12/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.502, 0.502, 0.502)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_06/Materials/Mtl13
*  **Prim路径 (Prim Path):**/World/AGV_ready_06/Materials/Mtl13
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_06/Materials/Mtl13/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_06/Materials/Mtl13/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.008, 0.514, 0.816)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_06/Materials/Mtl14
*  **Prim路径 (Prim Path):**/World/AGV_ready_06/Materials/Mtl14
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_06/Materials/Mtl14/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_06/Materials/Mtl14/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.310, 0.310, 0.310)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_06/Materials/Mtl15
*  **Prim路径 (Prim Path):**/World/AGV_ready_06/Materials/Mtl15
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_06/Materials/Mtl15/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_06/Materials/Mtl15/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.263, 0.275, 0.275)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_06/Materials/Mtl16
*  **Prim路径 (Prim Path):**/World/AGV_ready_06/Materials/Mtl16
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_06/Materials/Mtl16/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_06/Materials/Mtl16/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.698, 0.698, 0.000)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_06/Materials/Mtl17
*  **Prim路径 (Prim Path):**/World/AGV_ready_06/Materials/Mtl17
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_06/Materials/Mtl17/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_06/Materials/Mtl17/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.000, 0.863, 1.000)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_06/Materials/Mtl3
*  **Prim路径 (Prim Path):**/World/AGV_ready_06/Materials/Mtl3
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_06/Materials/Mtl3/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_06/Materials/Mtl3/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.431, 0.455, 0.498)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_06/Materials/Mtl35
*  **Prim路径 (Prim Path):**/World/AGV_ready_06/Materials/Mtl35
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_06/Materials/Mtl35/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_06/Materials/Mtl35/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.792, 0.820, 0.933)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_06/Materials/Mtl36
*  **Prim路径 (Prim Path):**/World/AGV_ready_06/Materials/Mtl36
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_06/Materials/Mtl36/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_06/Materials/Mtl36/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.667, 0.698, 0.765)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_06/Materials/Mtl37
*  **Prim路径 (Prim Path):**/World/AGV_ready_06/Materials/Mtl37
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_06/Materials/Mtl37/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_06/Materials/Mtl37/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.098, 0.098, 0.098)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_06/Materials/Mtl3a
*  **Prim路径 (Prim Path):**/World/AGV_ready_06/Materials/Mtl3a
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_06/Materials/Mtl3a/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_06/Materials/Mtl3a/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.388, 0.369, 0.322)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_06/Materials/Mtl3b
*  **Prim路径 (Prim Path):**/World/AGV_ready_06/Materials/Mtl3b
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_06/Materials/Mtl3b/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_06/Materials/Mtl3b/pbr_shader' (ID: 'UsdPreviewSurface')
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


### /World/AGV_ready_06/Materials/Mtl5
*  **Prim路径 (Prim Path):**/World/AGV_ready_06/Materials/Mtl5
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_06/Materials/Mtl5/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_06/Materials/Mtl5/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.396, 0.408, 0.467)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_06/Materials/Mtl7
*  **Prim路径 (Prim Path):**/World/AGV_ready_06/Materials/Mtl7
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_06/Materials/Mtl7/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_06/Materials/Mtl7/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.376, 0.376, 0.376)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_06/Materials/Mtl8
*  **Prim路径 (Prim Path):**/World/AGV_ready_06/Materials/Mtl8
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_06/Materials/Mtl8/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_06/Materials/Mtl8/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.173, 0.173, 0.173)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_06/Materials/Mtla
*  **Prim路径 (Prim Path):**/World/AGV_ready_06/Materials/Mtla
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_06/Materials/Mtla/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_06/Materials/Mtla/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.612, 0.725, 0.745)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_06/Materials/Mtlb1
*  **Prim路径 (Prim Path):**/World/AGV_ready_06/Materials/Mtlb1
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_06/Materials/Mtlb1/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_06/Materials/Mtlb1/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.949, 0.925, 0.933)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_06/Materials/Stainless_Steel
*  **Prim路径 (Prim Path):**/World/AGV_ready_06/Materials/Stainless_Steel
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_06/Materials/Stainless_Steel/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_06/Materials/Stainless_Steel/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.292, 0.294, 0.284)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0.431257'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_06/Materials/Metal_Aluminum_Anodized_1
*  **Prim路径 (Prim Path):**/World/AGV_ready_06/Materials/Metal_Aluminum_Anodized_1
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_06/Materials/Metal_Aluminum_Anodized_1/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_06/Materials/Metal_Aluminum_Anodized_1/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.260, 0.269, 0.282)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0.309883'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0'


---


### /World/AGV_ready_06/Materials/Metal_Aluminum_Anodized_2
*  **Prim路径 (Prim Path):**/World/AGV_ready_06/Materials/Metal_Aluminum_Anodized_2
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_06/Materials/Metal_Aluminum_Anodized_2/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_06/Materials/Metal_Aluminum_Anodized_2/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.792, 0.820, 0.859)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/AGV_ready_06/Materials/basic_gray_plastic
*  **Prim路径 (Prim Path):**/World/AGV_ready_06/Materials/basic_gray_plastic
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_06/Materials/basic_gray_plastic/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_06/Materials/basic_gray_plastic/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0.297745'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0.115685'


---


### /World/AGV_ready_06/Materials/texture
*  **Prim路径 (Prim Path):**/World/AGV_ready_06/Materials/texture
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/AGV_ready_06/Materials/texture/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/AGV_ready_06/Materials/texture/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.294, 0.294, 0.294)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '1'


---


### /World/Plastic_Crate_1_/Materials/Material_1
*  **Prim路径 (Prim Path):**/World/Plastic_Crate_1_/Materials/Material_1
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/Plastic_Crate_1_/Materials/Material_1/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/Plastic_Crate_1_/Materials/Material_1/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f]
               *   Connected: '/World/Plastic_Crate_1_/Materials/Material_1/tex_base.outputs:rgb' @ '/World/Plastic_Crate_1_/Materials/Material_1/tex_base'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/Material_1_baseColor_cutoff173.png'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(1.000, 1.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'opacity' [float]
               *   Connected: '/World/Plastic_Crate_1_/Materials/Material_1/tex_base.outputs:a' @ '/World/Plastic_Crate_1_/Materials/Material_1/tex_base'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/Material_1_baseColor_cutoff173.png'
           *   'roughness' [float] = '0.6'
       *   '/World/Plastic_Crate_1_/Materials/Material_1/tex_base' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/Material_1_baseColor_cutoff173.png'
       *   Inputs:
           *   'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
           *   'file' [asset] = '0/Material_1_baseColor_cutoff173.png'
           *   'st' [float2]
               *   Connected: '/World/Plastic_Crate_1_/Materials/Material_1/uvset0.outputs:result' @ '/World/Plastic_Crate_1_/Materials/Material_1/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/Plastic_Crate_1_/Materials/Material_1/uvset0' (ID: 'UsdPrimvarReader_float2')
       *   Implementation: 'id'


---


### /World/Plastic_Crate_1__01/Materials/Material_1
*  **Prim路径 (Prim Path):**/World/Plastic_Crate_1__01/Materials/Material_1
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/Plastic_Crate_1__01/Materials/Material_1/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/Plastic_Crate_1__01/Materials/Material_1/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f]
               *   Connected: '/World/Plastic_Crate_1__01/Materials/Material_1/tex_base.outputs:rgb' @ '/World/Plastic_Crate_1__01/Materials/Material_1/tex_base'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/Material_1_baseColor_cutoff173.png'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(1.000, 1.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'opacity' [float]
               *   Connected: '/World/Plastic_Crate_1__01/Materials/Material_1/tex_base.outputs:a' @ '/World/Plastic_Crate_1__01/Materials/Material_1/tex_base'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/Material_1_baseColor_cutoff173.png'
           *   'roughness' [float] = '0.6'
       *   '/World/Plastic_Crate_1__01/Materials/Material_1/tex_base' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/Material_1_baseColor_cutoff173.png'
       *   Inputs:
           *   'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
           *   'file' [asset] = '0/Material_1_baseColor_cutoff173.png'
           *   'st' [float2]
               *   Connected: '/World/Plastic_Crate_1__01/Materials/Material_1/uvset0.outputs:result' @ '/World/Plastic_Crate_1__01/Materials/Material_1/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/Plastic_Crate_1__01/Materials/Material_1/uvset0' (ID: 'UsdPrimvarReader_float2')
       *   Implementation: 'id'


---


### /World/Plastic_Crate_1__02/Materials/Material_1
*  **Prim路径 (Prim Path):**/World/Plastic_Crate_1__02/Materials/Material_1
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/Plastic_Crate_1__02/Materials/Material_1/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/Plastic_Crate_1__02/Materials/Material_1/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f]
               *   Connected: '/World/Plastic_Crate_1__02/Materials/Material_1/tex_base.outputs:rgb' @ '/World/Plastic_Crate_1__02/Materials/Material_1/tex_base'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/Material_1_baseColor_cutoff173.png'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(1.000, 1.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'opacity' [float]
               *   Connected: '/World/Plastic_Crate_1__02/Materials/Material_1/tex_base.outputs:a' @ '/World/Plastic_Crate_1__02/Materials/Material_1/tex_base'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/Material_1_baseColor_cutoff173.png'
           *   'roughness' [float] = '0.6'
       *   '/World/Plastic_Crate_1__02/Materials/Material_1/tex_base' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/Material_1_baseColor_cutoff173.png'
       *   Inputs:
           *   'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
           *   'file' [asset] = '0/Material_1_baseColor_cutoff173.png'
           *   'st' [float2]
               *   Connected: '/World/Plastic_Crate_1__02/Materials/Material_1/uvset0.outputs:result' @ '/World/Plastic_Crate_1__02/Materials/Material_1/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/Plastic_Crate_1__02/Materials/Material_1/uvset0' (ID: 'UsdPrimvarReader_float2')
       *   Implementation: 'id'


---


### /World/Plastic_Crate_1__03/Materials/Material_1
*  **Prim路径 (Prim Path):**/World/Plastic_Crate_1__03/Materials/Material_1
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/Plastic_Crate_1__03/Materials/Material_1/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/Plastic_Crate_1__03/Materials/Material_1/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f]
               *   Connected: '/World/Plastic_Crate_1__03/Materials/Material_1/tex_base.outputs:rgb' @ '/World/Plastic_Crate_1__03/Materials/Material_1/tex_base'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/Material_1_baseColor_cutoff173.png'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(1.000, 1.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'opacity' [float]
               *   Connected: '/World/Plastic_Crate_1__03/Materials/Material_1/tex_base.outputs:a' @ '/World/Plastic_Crate_1__03/Materials/Material_1/tex_base'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/Material_1_baseColor_cutoff173.png'
           *   'roughness' [float] = '0.6'
       *   '/World/Plastic_Crate_1__03/Materials/Material_1/tex_base' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/Material_1_baseColor_cutoff173.png'
       *   Inputs:
           *   'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
           *   'file' [asset] = '0/Material_1_baseColor_cutoff173.png'
           *   'st' [float2]
               *   Connected: '/World/Plastic_Crate_1__03/Materials/Material_1/uvset0.outputs:result' @ '/World/Plastic_Crate_1__03/Materials/Material_1/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/Plastic_Crate_1__03/Materials/Material_1/uvset0' (ID: 'UsdPrimvarReader_float2')
       *   Implementation: 'id'


---


### /World/Plastic_Crate_1__04/Materials/Material_1
*  **Prim路径 (Prim Path):**/World/Plastic_Crate_1__04/Materials/Material_1
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/Plastic_Crate_1__04/Materials/Material_1/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/Plastic_Crate_1__04/Materials/Material_1/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f]
               *   Connected: '/World/Plastic_Crate_1__04/Materials/Material_1/tex_base.outputs:rgb' @ '/World/Plastic_Crate_1__04/Materials/Material_1/tex_base'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/Material_1_baseColor_cutoff173.png'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(1.000, 1.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'opacity' [float]
               *   Connected: '/World/Plastic_Crate_1__04/Materials/Material_1/tex_base.outputs:a' @ '/World/Plastic_Crate_1__04/Materials/Material_1/tex_base'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/Material_1_baseColor_cutoff173.png'
           *   'roughness' [float] = '0.6'
       *   '/World/Plastic_Crate_1__04/Materials/Material_1/tex_base' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/Material_1_baseColor_cutoff173.png'
       *   Inputs:
           *   'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
           *   'file' [asset] = '0/Material_1_baseColor_cutoff173.png'
           *   'st' [float2]
               *   Connected: '/World/Plastic_Crate_1__04/Materials/Material_1/uvset0.outputs:result' @ '/World/Plastic_Crate_1__04/Materials/Material_1/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/Plastic_Crate_1__04/Materials/Material_1/uvset0' (ID: 'UsdPrimvarReader_float2')
       *   Implementation: 'id'


---


### /World/Plastic_Crate_1__05/Materials/Material_1
*  **Prim路径 (Prim Path):**/World/Plastic_Crate_1__05/Materials/Material_1
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/Plastic_Crate_1__05/Materials/Material_1/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/Plastic_Crate_1__05/Materials/Material_1/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f]
               *   Connected: '/World/Plastic_Crate_1__05/Materials/Material_1/tex_base.outputs:rgb' @ '/World/Plastic_Crate_1__05/Materials/Material_1/tex_base'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/Material_1_baseColor_cutoff173.png'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(1.000, 1.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'opacity' [float]
               *   Connected: '/World/Plastic_Crate_1__05/Materials/Material_1/tex_base.outputs:a' @ '/World/Plastic_Crate_1__05/Materials/Material_1/tex_base'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/Material_1_baseColor_cutoff173.png'
           *   'roughness' [float] = '0.6'
       *   '/World/Plastic_Crate_1__05/Materials/Material_1/tex_base' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/Material_1_baseColor_cutoff173.png'
       *   Inputs:
           *   'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
           *   'file' [asset] = '0/Material_1_baseColor_cutoff173.png'
           *   'st' [float2]
               *   Connected: '/World/Plastic_Crate_1__05/Materials/Material_1/uvset0.outputs:result' @ '/World/Plastic_Crate_1__05/Materials/Material_1/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/Plastic_Crate_1__05/Materials/Material_1/uvset0' (ID: 'UsdPrimvarReader_float2')
       *   Implementation: 'id'


---


### /World/Conveyor_Belt_06/Materials/Material_0
*  **Prim路径 (Prim Path):**/World/Conveyor_Belt_06/Materials/Material_0
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/Conveyor_Belt_06/Materials/Material_0/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/Conveyor_Belt_06/Materials/Material_0/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f]
               *   Connected: '/World/Conveyor_Belt_06/Materials/Material_0/tex_base.outputs:rgb' @ '/World/Conveyor_Belt_06/Materials/Material_0/tex_base'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/Material_0_baseColor.jpg'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(1.000, 1.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0.892971'
       *   '/World/Conveyor_Belt_06/Materials/Material_0/tex_base' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/Material_0_baseColor.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
           *   'file' [asset] = '0/Material_0_baseColor.jpg'
           *   'st' [float2]
               *   Connected: '/World/Conveyor_Belt_06/Materials/Material_0/uvset0.outputs:result' @ '/World/Conveyor_Belt_06/Materials/Material_0/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/Conveyor_Belt_06/Materials/Material_0/uvset0' (ID: 'UsdPrimvarReader_float2')
       *   Implementation: 'id'


---


### /World/MobileShopDesk_A01_Blue_01/Looks/Metal_Glossy_A_MobileShopDesk_A
*  **Prim路径 (Prim Path):**/World/MobileShopDesk_A01_Blue_01/Looks/Metal_Glossy_A_MobileShopDesk_A
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/MobileShopDesk_A01_Blue_01/Looks/Metal_Glossy_A_MobileShopDesk_A/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/MobileShopDesk_A01_Blue_01/Looks/Metal_Glossy_A_MobileShopDesk_A/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] '0/Metal_Glossy_A.mdl' (Sub Id: 'Metal_Glossy_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/device_data/usdz/Workbench/MobileShopDesk_A01_Blue_01.usdz[0/Metal_Glossy_A.mdl]'


---


### /World/MobileShopDesk_A01_Blue_01/Looks/Metal_Rough_A_MobileShopDesk_A
*  **Prim路径 (Prim Path):**/World/MobileShopDesk_A01_Blue_01/Looks/Metal_Rough_A_MobileShopDesk_A
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/MobileShopDesk_A01_Blue_01/Looks/Metal_Rough_A_MobileShopDesk_A/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/MobileShopDesk_A01_Blue_01/Looks/Metal_Rough_A_MobileShopDesk_A/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] '0/Metal_Rough_A.mdl' (Sub Id: 'Metal_Rough_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/device_data/usdz/Workbench/MobileShopDesk_A01_Blue_01.usdz[0/Metal_Rough_A.mdl]'


---


### /World/MobileShopDesk_A01_Blue_01/Looks/Plastic_Black_A_MobileShopDesk_A
*  **Prim路径 (Prim Path):**/World/MobileShopDesk_A01_Blue_01/Looks/Plastic_Black_A_MobileShopDesk_A
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/MobileShopDesk_A01_Blue_01/Looks/Plastic_Black_A_MobileShopDesk_A/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/MobileShopDesk_A01_Blue_01/Looks/Plastic_Black_A_MobileShopDesk_A/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] '2/Plastic_Black_A.mdl' (Sub Id: 'Plastic_Black_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/device_data/usdz/Workbench/MobileShopDesk_A01_Blue_01.usdz[2/Plastic_Black_A.mdl]'


---


### /World/MobileShopDesk_A01_Blue_01/Looks/Rubber_Gray_Glossy_A_MobileShopDesk_A
*  **Prim路径 (Prim Path):**/World/MobileShopDesk_A01_Blue_01/Looks/Rubber_Gray_Glossy_A_MobileShopDesk_A
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/MobileShopDesk_A01_Blue_01/Looks/Rubber_Gray_Glossy_A_MobileShopDesk_A/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/MobileShopDesk_A01_Blue_01/Looks/Rubber_Gray_Glossy_A_MobileShopDesk_A/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] '1/Rubber_Black_Glossy_A.mdl' (Sub Id: 'Rubber_Black_Glossy_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/device_data/usdz/Workbench/MobileShopDesk_A01_Blue_01.usdz[1/Rubber_Black_Glossy_A.mdl]'
       *   Inputs:
           *   'diffuse_tint' [color3f] = '(0.293, 0.268, 0.250)'
           *   'reflection_roughness_texture_influence' [float] = '1'


---


### /World/MobileShopDesk_A01_Blue_01/Looks/Metal_Painted_Blue_Glossy_A_MobileShopDesk_A
*  **Prim路径 (Prim Path):**/World/MobileShopDesk_A01_Blue_01/Looks/Metal_Painted_Blue_Glossy_A_MobileShopDesk_A
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/MobileShopDesk_A01_Blue_01/Looks/Metal_Painted_Blue_Glossy_A_MobileShopDesk_A/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/MobileShopDesk_A01_Blue_01/Looks/Metal_Painted_Blue_Glossy_A_MobileShopDesk_A/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] '0/Metal_Painted_White_Glossy_A.mdl' (Sub Id: 'Metal_Painted_White_Glossy_A')  | Resolved: '/media/simple/another_Documents/isaacsim_assets/device_data/usdz/Workbench/MobileShopDesk_A01_Blue_01.usdz[0/Metal_Painted_White_Glossy_A.mdl]'
       *   Inputs:
           *   'diffuse_tint' [color3f] = '(0.078, 0.121, 0.479)'


---
