# USDA场景描述文档:assembly.usda

## 1.场景元数据(Scene Metadata)

* **USDA文件路径(USDA File Path):**`/media/simple/another_Documents/isaacsim_assets/scenedata/assembly.usda`
* **默认Prim (Default Prim):**'World'
* **单位与坐标系 (Units & Coordinate System):**

  * **米(Meters Per Unit):**1.0
  * **Up Axis:**Z
* **场景描述(Scene Describe):** 该工业场景呈现为一个高度规整、模块化的自动化装配作业单元，其整体布局遵循现代工业工程中的“线性流向与集群作业”原则，空间格局开阔且功能区域划分明确。在厂区平面规划中，核心区域由一套高度集成的输送与抓取系统构成，整体空间呈长方形延伸，地面采用了深灰色的环氧树脂耐磨涂层，平整度极高且具有低反射率特征，为工业机器人的精密定位提供了稳定的物理基础。墙体结构为浅灰白色的工业预制板，在墙体上缘约三米处设有一条平行的红色安全警示带，形成了空间上的水平视觉基准，同时也界定了作业区的安全边界。在设备排布方面，场景的中轴线由一条重型直线带式输送机定义，该输送装置长度约为6至8米，宽度约为600mm，其主体框架采用银灰色的阳极氧化铝型材，侧向分布有标准的T型安装槽，体现了极强的扩展性。输送皮带表面为黑色抗静电复合材质，并压印有密集的菱形防滑花纹（Diamond PlateTexture），旨在增强物料在高速输送或启停过程中的稳定性。输送机由八至十根竖向支撑腿支撑，每根支撑腿底部均配有大直径的圆盘状可调节水平地脚，确保了输送平面在三维坐标系中的绝对水平。与输送机平行且紧密相邻的是机器人作业集群，该集群包含两台完全对称的六轴多关节工业机器人及一台中央协作工作台。这两台机器人分布在工作台的两侧，其底座通过重型螺栓垂直锚定于地面。机器人机身采用纯白色哑光喷涂，外形圆润且关节模组化程度高，展现出协作型机器人的工业设计美学。其中，位于左侧的机器人处于向输送线延伸的工作位姿，其六个自由度的关节（J1-J6）呈现出复杂的空间扭转，末端执行器配备了一套二指平动电控夹爪，正准备从输送带上抓取或放置物料；位于右侧的机器人则处于相对收缩的待机或协同位姿，其末端同样配备了同规格的夹爪执行器。两台机器人的作业范围精确覆盖了输送机的特定段位以及中心工作台的全部表面，形成了一个闭环的物料处理循环。位于两台机器人中心位置的仓储与控制工装设备是一个多层级的纯白色组合台。该设备结合了作业平台与控制柜的功能，顶部作业面平滑且宽大，侧方箱体结构规整，内部预留了线缆走线孔位与散热栅格细节。从相互排布关系来看，该工站与输送机保持约300mm的安全间隙，确保了机器人末端在旋转过程中不会产生物理干涉。整个设备集群的排布方式呈现出极高的对称性与逻辑性：输送机负责物料的长程位移，机器人负责物料的垂直抓取与精确落位，而中心工作台则作为工艺加工或临时暂存的核心节点。在3D场景合成与虚拟搭建中，这种布局提供了明确的坐标参照。所有设备均严格遵循垂直于地面、平行于主轴的几何逻辑。材质表现上，铝型材的金属拉丝感、黑色橡胶皮带的颗粒感、机器人漆面的半哑光感以及环氧地坪的漫反射感共同构成了真实的工业视觉层次。光影环境模拟了厂房顶部的均匀漫反射光，没有强烈的直射光源，但在设备底部与地面的接触面产生了细微的环境光遮蔽（AO）阴影，这种阴影不仅增强了设备的体积感，也为虚拟搭建提供了真实的“落地点”参考。整个场景无任何冗余装饰，每一个工业元件的排布均处于功能最优化的空间节点上，完整体现了一个精密、高效、无人化的现代装配车间实景。
* **设备数量(Device Number):**
  * **Scene: 1**
  * **IndustrialRobot: 2**
  * **Workbench: 1**
  * **Conveyor: 1**
  * **AGV: 0**
  * **Forklift: 0**
  * **Box: 0**
  * **Rack: 0**
  * **Pallet: 0**
  * **Part: 0**
  * **Decoration: 0**

## 2.场景对象层级(Scene Hierarchy)

* World (Xform)
  * Factory (Xform)
    * Materials (Scope)
      * material_4 (Material)
        * pbr_shader (Shader)
        * uvset0 (Shader)
        * tex_base (Shader)
      * material_2 (Material)
        * pbr_shader (Shader)
        * uvset0 (Shader)
        * tex_base (Shader)
      * Structure (Material)
        * pbr_shader (Shader)
      * material (Material)
        * pbr_shader (Shader)
      * Long_Walls (Material)
        * pbr_shader (Shader)
      * Wall_Horizon (Material)
        * pbr_shader (Shader)
      * Walls (Material)
        * pbr_shader (Shader)
      * Red_Lamp (Material)
        * pbr_shader (Shader)
      * Grey (Material)
        * pbr_shader (Shader)
      * Chris_Shirt (Material)
        * pbr_shader (Shader)
      * Chris_Shoe (Material)
        * pbr_shader (Shader)
      * Chris_Skin (Material)
        * pbr_shader (Shader)
      * Chris_Shoe_Sole (Material)
        * pbr_shader (Shader)
      * Chris_Hair (Material)
        * pbr_shader (Shader)
      * Chris_Pants (Material)
        * pbr_shader (Shader)
    * Meshes (Xform)
      * Sketchfab_model (Xform)
        * Collada_visual_scene_group (Xform)
          * SketchUp (Xform)
            * Material2 (Xform)
              * Material2 (Mesh)
            * Material2_1 (Xform)
            * Material2_2 (Xform)
              * Material2 (Mesh)
            * Material2_3 (Xform)
              * Material2 (Mesh)
            * Material2_4 (Xform)
              * Material2 (Mesh)
            * Material2_5 (Xform)
              * Material2 (Mesh)
            * Material2_6 (Xform)
              * Material2 (Mesh)
            * Material2_7 (Xform)
              * Material2 (Mesh)
            * Material2_8 (Xform)
              * Material2 (Mesh)
            * Material3 (Xform)
              * Material3 (Mesh)
            * Material3_1 (Xform)
              * Material3 (Mesh)
            * Material2_9 (Xform)
    * GroundPlane (Xform)
      * CollisionMesh (Mesh)
      * CollisionPlane (Plane)
  * Conveyor_Belt (Xform)
    * Materials (Scope)
      * Material_0 (Material)
        * pbr_shader (Shader)
        * uvset0 (Shader)
        * tex_base (Shader)
    * Meshes (Xform)
      * Sketchfab_model (Xform)
        * _aaef2bbe46a4470bc765b4ce24a8c4c_fbx (Xform)
          * RootNode (Xform)
            * Cylinder001 (Xform)
              * Cylinder001_Material__0_0 (Xform)
                * Cylinder001_Material__0_0 (Mesh)
  * Workbench_2 (Xform)
    * Materials (Scope)
      * Scratched_wood (Material)
        * pbr_shader (Shader)
      * Wood_144 (Material)
        * pbr_shader (Shader)
      * Blueprint_Grid (Material)
        * pbr_shader (Shader)
    * Meshes (Xform)
      * Sketchfab_model (Xform)
        * c32e2987487143319e4b2f288b75227a_fbx (Xform)
          * RootNode (Xform)
            * Cube (Xform)
              * Cube_Scratched_wood_0 (Xform)
                * Cube_Scratched_wood_0 (Mesh)
            * Cube_001 (Xform)
              * Cube_001_Scratched_wood_0 (Xform)
                * Cube_001_Scratched_wood_0 (Mesh)
            * Cube_002 (Xform)
              * Cube_002_Scratched_wood_0 (Xform)
                * Cube_002_Scratched_wood_0 (Mesh)
            * Cube_003 (Xform)
              * Cube_003_Scratched_wood_0 (Xform)
                * Cube_003_Scratched_wood_0 (Mesh)
            * Cube_004 (Xform)
              * Cube_004_Scratched_wood_0 (Xform)
                * Cube_004_Scratched_wood_0 (Mesh)
            * Cube_005 (Xform)
              * Cube_005_Scratched_wood_0 (Xform)
                * Cube_005_Scratched_wood_0 (Mesh)
            * Cube_006 (Xform)
              * Cube_006_Rusty_metal_001_0 (Xform)
                * Cube_006_Rusty_metal_001_0 (Mesh)
            * Cube_007 (Xform)
              * Cube_007_Rusty_metal_001_0 (Xform)
                * Cube_007_Rusty_metal_001_0 (Mesh)
            * Cube_008 (Xform)
              * Cube_008_Wood_144_0 (Xform)
                * Cube_008_Wood_144_0 (Mesh)
            * Cube_009 (Xform)
              * Cube_009_Wood_144_0 (Xform)
                * Cube_009_Wood_144_0 (Mesh)
            * Cube_010 (Xform)
              * Cube_010_Wood_144_0 (Xform)
                * Cube_010_Wood_144_0 (Mesh)
            * Cube_011 (Xform)
              * Cube_011_Rusty_metal_002_0 (Xform)
                * Cube_011_Rusty_metal_002_0 (Mesh)
            * Plane (Xform)
              * Plane_Blueprint_Grid_0 (Xform)
                * Plane_Blueprint_Grid_0 (Mesh)
  * INDUSTRIAL_ROBOTIC_ARM (Xform)
    * Materials (Scope)
      * Brass___Polished (Material)
        * pbr_shader (Shader)
      * Aluminum___Anodized_Glossy_Grey (Material)
        * pbr_shader (Shader)
      * Paint___Enamel_Glossy_Yellow (Material)
        * pbr_shader (Shader)
      * Body1__0 (Material)
        * pbr_shader (Shader)
      * Steel___Satin (Material)
        * pbr_shader (Shader)
      * Paint___Enamel_Glossy_Black (Material)
        * pbr_shader (Shader)
    * Meshes (Xform)
      * Sketchfab_model (Xform)
        * c87c2a6ebd5447f7ac496076c3c610d3_fbx (Xform)
          * RootNode (Xform)
            * PDM_INDUSTRIAL_ROBOTIC_ARM_PROJECT_v84 (Xform)
              * Component_1_Base_1 (Xform)
                * Component_1_Base (Xform)
                  * Component2_1 (Xform)
                    * Component2 (Xform)
                      * Body1 (Xform)
                        * Body1_Brass___Polished_0 (Xform)
                          * Body1_Brass___Polished_0 (Mesh)
                  * Component24_1 (Xform)
                    * Component24 (Xform)
                      * Body1 (Xform)
                        * Body1_Aluminum___Anodized_Glossy__Grey__0 (Xform)
                          * Body1_Aluminum___Anodized_Glossy__Grey__0 (Mesh)
                  * Component25_1 (Xform)
                    * Component25 (Xform)
                      * Body1 (Xform)
                        * Body1_Aluminum___Anodized_Glossy__Grey__0 (Xform)
                          * Body1_Aluminum___Anodized_Glossy__Grey__0 (Mesh)
                  * Component26_1 (Xform)
                    * Component26 (Xform)
                      * Body1 (Xform)
                        * Body1_Aluminum___Anodized_Glossy__Grey__0 (Xform)
                          * Body1_Aluminum___Anodized_Glossy__Grey__0 (Mesh)
                  * Component27_1 (Xform)
                    * Component27 (Xform)
                      * Body1 (Xform)
                        * Body1_Aluminum___Anodized_Glossy__Grey__0 (Xform)
                          * Body1_Aluminum___Anodized_Glossy__Grey__0 (Mesh)
                  * Component28_1 (Xform)
                    * Component28 (Xform)
                      * Body1 (Xform)
                        * Body1_Brass___Polished_0 (Xform)
                          * Body1_Brass___Polished_0 (Mesh)
              * Component_2_Jaw_1_1 (Xform)
                * Component_2_Jaw_1 (Xform)
                  * Component4_1 (Xform)
                    * Component4 (Xform)
                      * Body1 (Xform)
                        * Body1_Aluminum___Anodized_Glossy__Grey__0 (Xform)
                          * Body1_Aluminum___Anodized_Glossy__Grey__0 (Mesh)
                  * Component17_1 (Xform)
                    * Component17 (Xform)
                      * Body1 (Xform)
                        * Body1_Brass___Polished_0 (Xform)
                          * Body1_Brass___Polished_0 (Mesh)
              * Component_3_Jaw_2_1 (Xform)
                * Component_3_Jaw_2 (Xform)
                  * Component6_1 (Xform)
                    * Component6 (Xform)
                      * Body1 (Xform)
                        * Body1_Paint___Enamel_Glossy__Yellow__0 (Xform)
                          * Body1_Paint___Enamel_Glossy__Yellow__0 (Mesh)
                        * Body1__0 (Xform)
                          * Body1__0 (Mesh)
                  * Component29_1 (Xform)
                    * Component29 (Xform)
                      * Body1 (Xform)
                        * Body1_Aluminum___Anodized_Glossy__Grey__0 (Xform)
                          * Body1_Aluminum___Anodized_Glossy__Grey__0 (Mesh)
                  * Component30_1 (Xform)
                    * Component30 (Xform)
                      * Body1 (Xform)
                        * Body1_Steel___Satin_0 (Xform)
                          * Body1_Steel___Satin_0 (Mesh)
                  * Component31_1 (Xform)
                    * Component31 (Xform)
                      * Body1 (Xform)
                        * Body1_Steel___Satin_0 (Xform)
                          * Body1_Steel___Satin_0 (Mesh)
                  * Component32_1 (Xform)
                    * Component32 (Xform)
                      * Body1 (Xform)
                        * Body1_Steel___Satin_0 (Xform)
                          * Body1_Steel___Satin_0 (Mesh)
                  * Component33_1 (Xform)
                    * Component33 (Xform)
                      * Body1 (Xform)
                        * Body1_Steel___Satin_0 (Xform)
                          * Body1_Steel___Satin_0 (Mesh)
                  * Component34_1 (Xform)
                    * Component34 (Xform)
                      * Body1 (Xform)
                        * Body1_Steel___Satin_0 (Xform)
                          * Body1_Steel___Satin_0 (Mesh)
                  * Component35_1 (Xform)
                    * Component35 (Xform)
                      * Body1 (Xform)
                        * Body1_Steel___Satin_0 (Xform)
                          * Body1_Steel___Satin_0 (Mesh)
                  * Component36_1 (Xform)
                    * Component36 (Xform)
                      * Body1 (Xform)
                        * Body1_Steel___Satin_0 (Xform)
                          * Body1_Steel___Satin_0 (Mesh)
                  * Component37_1 (Xform)
                    * Component37 (Xform)
                      * Body1 (Xform)
                        * Body1_Steel___Satin_0 (Xform)
                          * Body1_Steel___Satin_0 (Mesh)
                  * Component38_1 (Xform)
                    * Component38 (Xform)
                      * Body1 (Xform)
                        * Body1_Steel___Satin_0 (Xform)
                          * Body1_Steel___Satin_0 (Mesh)
                  * Component39_1 (Xform)
                    * Component39 (Xform)
                      * Body1 (Xform)
                        * Body1_Steel___Satin_0 (Xform)
                          * Body1_Steel___Satin_0 (Mesh)
                  * Component40_1 (Xform)
                    * Component40 (Xform)
                      * Body1 (Xform)
                        * Body1_Steel___Satin_0 (Xform)
                          * Body1_Steel___Satin_0 (Mesh)
                  * Component41_1 (Xform)
                    * Component41 (Xform)
                      * Body1 (Xform)
                        * Body1_Steel___Satin_0 (Xform)
                          * Body1_Steel___Satin_0 (Mesh)
                  * Component42_1 (Xform)
                    * Component42 (Xform)
                      * Body1 (Xform)
                        * Body1_Steel___Satin_0 (Xform)
                          * Body1_Steel___Satin_0 (Mesh)
              * Component_4_Jaw_3_1 (Xform)
                * Component_4_Jaw_3 (Xform)
                  * Component8_1 (Xform)
                    * Component8 (Xform)
                      * Body1 (Xform)
                        * Body1_Brass___Polished_0 (Xform)
                          * Body1_Brass___Polished_0 (Mesh)
                  * Component22_1 (Xform)
                    * Component22 (Xform)
                      * Body1 (Xform)
                        * Body1_Brass___Polished_0 (Xform)
                          * Body1_Brass___Polished_0 (Mesh)
                  * Component23_1 (Xform)
                    * Component23 (Xform)
                      * Body1 (Xform)
                        * Body1_Brass___Polished_0 (Xform)
                          * Body1_Brass___Polished_0 (Mesh)
              * Component_5_Jaw_4_1 (Xform)
                * Component_5_Jaw_4 (Xform)
                  * Component10_1 (Xform)
                    * Component10 (Xform)
                      * Body1 (Xform)
                        * Body1_Paint___Enamel_Glossy__Black__0 (Xform)
                          * Body1_Paint___Enamel_Glossy__Black__0 (Mesh)
                        * Body1__0 (Xform)
                          * Body1__0 (Mesh)
                  * Component20_1 (Xform)
                    * Component20 (Xform)
                      * Body1 (Xform)
                        * Body1_Aluminum___Anodized_Glossy__Grey__0 (Xform)
                          * Body1_Aluminum___Anodized_Glossy__Grey__0 (Mesh)
                  * Component21_1 (Xform)
                    * Component21 (Xform)
                      * Body1 (Xform)
                        * Body1_Steel___Satin_0 (Xform)
                          * Body1_Steel___Satin_0 (Mesh)
              * Component_6_Jaw_5_1 (Xform)
                * Component_6_Jaw_5 (Xform)
                  * Component12_1 (Xform)
                    * Component12 (Xform)
                      * Body1 (Xform)
                        * Body1_Brass___Polished_0 (Xform)
                          * Body1_Brass___Polished_0 (Mesh)
                  * Component18_1 (Xform)
                    * Component18 (Xform)
                      * Body1 (Xform)
                        * Body1_Brass___Polished_0 (Xform)
                          * Body1_Brass___Polished_0 (Mesh)
                  * Component19_1 (Xform)
                    * Component19 (Xform)
                      * Body1 (Xform)
                        * Body1_Paint___Enamel_Glossy__Yellow__0 (Xform)
                          * Body1_Paint___Enamel_Glossy__Yellow__0 (Mesh)
              * Component_7_Jaw_6_1 (Xform)
                * Component_7_Jaw_6 (Xform)
                  * Component14_1 (Xform)
                    * Component14 (Xform)
                      * Body1 (Xform)
                        * Body1_Brass___Polished_0 (Xform)
                          * Body1_Brass___Polished_0 (Mesh)
                  * Component43_1 (Xform)
                    * Component43 (Xform)
                      * Body1 (Xform)
                        * Body1_Aluminum___Anodized_Glossy__Grey__0 (Xform)
                          * Body1_Aluminum___Anodized_Glossy__Grey__0 (Mesh)
              * Component_8_Jaw_7_1 (Xform)
                * Component_8_Jaw_7 (Xform)
                  * Component16_1 (Xform)
                    * Component16 (Xform)
                      * Body1 (Xform)
                        * Body1_Aluminum___Anodized_Glossy__Grey__0 (Xform)
                          * Body1_Aluminum___Anodized_Glossy__Grey__0 (Mesh)
                  * Component16_2 (Xform)
                    * Component16 (Xform)
                      * Body1 (Xform)
                        * Body1_Aluminum___Anodized_Glossy__Grey__0 (Xform)
                          * Body1_Aluminum___Anodized_Glossy__Grey__0 (Mesh)
  * INDUSTRIAL_ROBOTIC_ARM_01 (Xform)
    * Materials (Scope)
      * Brass___Polished (Material)
        * pbr_shader (Shader)
      * Aluminum___Anodized_Glossy_Grey (Material)
        * pbr_shader (Shader)
      * Paint___Enamel_Glossy_Yellow (Material)
        * pbr_shader (Shader)
      * Body1__0 (Material)
        * pbr_shader (Shader)
      * Steel___Satin (Material)
        * pbr_shader (Shader)
      * Paint___Enamel_Glossy_Black (Material)
        * pbr_shader (Shader)
    * Meshes (Xform)
      * Sketchfab_model (Xform)
        * c87c2a6ebd5447f7ac496076c3c610d3_fbx (Xform)
          * RootNode (Xform)
            * PDM_INDUSTRIAL_ROBOTIC_ARM_PROJECT_v84 (Xform)
              * Component_1_Base_1 (Xform)
                * Component_1_Base (Xform)
                  * Component2_1 (Xform)
                    * Component2 (Xform)
                      * Body1 (Xform)
                        * Body1_Brass___Polished_0 (Xform)
                          * Body1_Brass___Polished_0 (Mesh)
                  * Component24_1 (Xform)
                    * Component24 (Xform)
                      * Body1 (Xform)
                        * Body1_Aluminum___Anodized_Glossy__Grey__0 (Xform)
                          * Body1_Aluminum___Anodized_Glossy__Grey__0 (Mesh)
                  * Component25_1 (Xform)
                    * Component25 (Xform)
                      * Body1 (Xform)
                        * Body1_Aluminum___Anodized_Glossy__Grey__0 (Xform)
                          * Body1_Aluminum___Anodized_Glossy__Grey__0 (Mesh)
                  * Component26_1 (Xform)
                    * Component26 (Xform)
                      * Body1 (Xform)
                        * Body1_Aluminum___Anodized_Glossy__Grey__0 (Xform)
                          * Body1_Aluminum___Anodized_Glossy__Grey__0 (Mesh)
                  * Component27_1 (Xform)
                    * Component27 (Xform)
                      * Body1 (Xform)
                        * Body1_Aluminum___Anodized_Glossy__Grey__0 (Xform)
                          * Body1_Aluminum___Anodized_Glossy__Grey__0 (Mesh)
                  * Component28_1 (Xform)
                    * Component28 (Xform)
                      * Body1 (Xform)
                        * Body1_Brass___Polished_0 (Xform)
                          * Body1_Brass___Polished_0 (Mesh)
              * Component_2_Jaw_1_1 (Xform)
                * Component_2_Jaw_1 (Xform)
                  * Component4_1 (Xform)
                    * Component4 (Xform)
                      * Body1 (Xform)
                        * Body1_Aluminum___Anodized_Glossy__Grey__0 (Xform)
                          * Body1_Aluminum___Anodized_Glossy__Grey__0 (Mesh)
                  * Component17_1 (Xform)
                    * Component17 (Xform)
                      * Body1 (Xform)
                        * Body1_Brass___Polished_0 (Xform)
                          * Body1_Brass___Polished_0 (Mesh)
              * Component_3_Jaw_2_1 (Xform)
                * Component_3_Jaw_2 (Xform)
                  * Component6_1 (Xform)
                    * Component6 (Xform)
                      * Body1 (Xform)
                        * Body1_Paint___Enamel_Glossy__Yellow__0 (Xform)
                          * Body1_Paint___Enamel_Glossy__Yellow__0 (Mesh)
                        * Body1__0 (Xform)
                          * Body1__0 (Mesh)
                  * Component29_1 (Xform)
                    * Component29 (Xform)
                      * Body1 (Xform)
                        * Body1_Aluminum___Anodized_Glossy__Grey__0 (Xform)
                          * Body1_Aluminum___Anodized_Glossy__Grey__0 (Mesh)
                  * Component30_1 (Xform)
                    * Component30 (Xform)
                      * Body1 (Xform)
                        * Body1_Steel___Satin_0 (Xform)
                          * Body1_Steel___Satin_0 (Mesh)
                  * Component31_1 (Xform)
                    * Component31 (Xform)
                      * Body1 (Xform)
                        * Body1_Steel___Satin_0 (Xform)
                          * Body1_Steel___Satin_0 (Mesh)
                  * Component32_1 (Xform)
                    * Component32 (Xform)
                      * Body1 (Xform)
                        * Body1_Steel___Satin_0 (Xform)
                          * Body1_Steel___Satin_0 (Mesh)
                  * Component33_1 (Xform)
                    * Component33 (Xform)
                      * Body1 (Xform)
                        * Body1_Steel___Satin_0 (Xform)
                          * Body1_Steel___Satin_0 (Mesh)
                  * Component34_1 (Xform)
                    * Component34 (Xform)
                      * Body1 (Xform)
                        * Body1_Steel___Satin_0 (Xform)
                          * Body1_Steel___Satin_0 (Mesh)
                  * Component35_1 (Xform)
                    * Component35 (Xform)
                      * Body1 (Xform)
                        * Body1_Steel___Satin_0 (Xform)
                          * Body1_Steel___Satin_0 (Mesh)
                  * Component36_1 (Xform)
                    * Component36 (Xform)
                      * Body1 (Xform)
                        * Body1_Steel___Satin_0 (Xform)
                          * Body1_Steel___Satin_0 (Mesh)
                  * Component37_1 (Xform)
                    * Component37 (Xform)
                      * Body1 (Xform)
                        * Body1_Steel___Satin_0 (Xform)
                          * Body1_Steel___Satin_0 (Mesh)
                  * Component38_1 (Xform)
                    * Component38 (Xform)
                      * Body1 (Xform)
                        * Body1_Steel___Satin_0 (Xform)
                          * Body1_Steel___Satin_0 (Mesh)
                  * Component39_1 (Xform)
                    * Component39 (Xform)
                      * Body1 (Xform)
                        * Body1_Steel___Satin_0 (Xform)
                          * Body1_Steel___Satin_0 (Mesh)
                  * Component40_1 (Xform)
                    * Component40 (Xform)
                      * Body1 (Xform)
                        * Body1_Steel___Satin_0 (Xform)
                          * Body1_Steel___Satin_0 (Mesh)
                  * Component41_1 (Xform)
                    * Component41 (Xform)
                      * Body1 (Xform)
                        * Body1_Steel___Satin_0 (Xform)
                          * Body1_Steel___Satin_0 (Mesh)
                  * Component42_1 (Xform)
                    * Component42 (Xform)
                      * Body1 (Xform)
                        * Body1_Steel___Satin_0 (Xform)
                          * Body1_Steel___Satin_0 (Mesh)
              * Component_4_Jaw_3_1 (Xform)
                * Component_4_Jaw_3 (Xform)
                  * Component8_1 (Xform)
                    * Component8 (Xform)
                      * Body1 (Xform)
                        * Body1_Brass___Polished_0 (Xform)
                          * Body1_Brass___Polished_0 (Mesh)
                  * Component22_1 (Xform)
                    * Component22 (Xform)
                      * Body1 (Xform)
                        * Body1_Brass___Polished_0 (Xform)
                          * Body1_Brass___Polished_0 (Mesh)
                  * Component23_1 (Xform)
                    * Component23 (Xform)
                      * Body1 (Xform)
                        * Body1_Brass___Polished_0 (Xform)
                          * Body1_Brass___Polished_0 (Mesh)
              * Component_5_Jaw_4_1 (Xform)
                * Component_5_Jaw_4 (Xform)
                  * Component10_1 (Xform)
                    * Component10 (Xform)
                      * Body1 (Xform)
                        * Body1_Paint___Enamel_Glossy__Black__0 (Xform)
                          * Body1_Paint___Enamel_Glossy__Black__0 (Mesh)
                        * Body1__0 (Xform)
                          * Body1__0 (Mesh)
                  * Component20_1 (Xform)
                    * Component20 (Xform)
                      * Body1 (Xform)
                        * Body1_Aluminum___Anodized_Glossy__Grey__0 (Xform)
                          * Body1_Aluminum___Anodized_Glossy__Grey__0 (Mesh)
                  * Component21_1 (Xform)
                    * Component21 (Xform)
                      * Body1 (Xform)
                        * Body1_Steel___Satin_0 (Xform)
                          * Body1_Steel___Satin_0 (Mesh)
              * Component_6_Jaw_5_1 (Xform)
                * Component_6_Jaw_5 (Xform)
                  * Component12_1 (Xform)
                    * Component12 (Xform)
                      * Body1 (Xform)
                        * Body1_Brass___Polished_0 (Xform)
                          * Body1_Brass___Polished_0 (Mesh)
                  * Component18_1 (Xform)
                    * Component18 (Xform)
                      * Body1 (Xform)
                        * Body1_Brass___Polished_0 (Xform)
                          * Body1_Brass___Polished_0 (Mesh)
                  * Component19_1 (Xform)
                    * Component19 (Xform)
                      * Body1 (Xform)
                        * Body1_Paint___Enamel_Glossy__Yellow__0 (Xform)
                          * Body1_Paint___Enamel_Glossy__Yellow__0 (Mesh)
              * Component_7_Jaw_6_1 (Xform)
                * Component_7_Jaw_6 (Xform)
                  * Component14_1 (Xform)
                    * Component14 (Xform)
                      * Body1 (Xform)
                        * Body1_Brass___Polished_0 (Xform)
                          * Body1_Brass___Polished_0 (Mesh)
                  * Component43_1 (Xform)
                    * Component43 (Xform)
                      * Body1 (Xform)
                        * Body1_Aluminum___Anodized_Glossy__Grey__0 (Xform)
                          * Body1_Aluminum___Anodized_Glossy__Grey__0 (Mesh)
              * Component_8_Jaw_7_1 (Xform)
                * Component_8_Jaw_7 (Xform)
                  * Component16_1 (Xform)
                    * Component16 (Xform)
                      * Body1 (Xform)
                        * Body1_Aluminum___Anodized_Glossy__Grey__0 (Xform)
                          * Body1_Aluminum___Anodized_Glossy__Grey__0 (Mesh)
                  * Component16_2 (Xform)
                    * Component16 (Xform)
                      * Body1 (Xform)
                        * Body1_Aluminum___Anodized_Glossy__Grey__0 (Xform)
                          * Body1_Aluminum___Anodized_Glossy__Grey__0 (Mesh)
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

### /World/Factory

* **Prim路径 (Prim Path):**/World/Factory
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '../scene/Factory/Factory.usdc'
* **世界包围盒 (World BBox):**
  * Size: '(3501.110, 1990.477, 6653.544)'
  * Center: '(15.491, 32.688, 9.952)'

---

### /World/Conveyor_Belt

* **Prim路径 (Prim Path):**/World/Conveyor_Belt
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '../assets/Conveyor_Belt/Conveyor_Belt.usdc'
* **世界包围盒 (World BBox):**
  * Size: '(0.799, 4.204, 9.846)'
  * Center: '(16.241, 28.789, 0.471)'

---

### /World/Workbench_2

* **Prim路径 (Prim Path):**/World/Workbench_2
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '../assets/Workbench_2/Workbench_2.usdc'
* **世界包围盒 (World BBox):**
  * Size: '(200.000, 150.106, 120.478)'
  * Center: '(14.746, 31.316, 0.712)'

---

### /World/INDUSTRIAL_ROBOTIC_ARM

* **Prim路径 (Prim Path):**/World/INDUSTRIAL_ROBOTIC_ARM
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '../assets/INDUSTRIAL_ROBOTIC_ARM/INDUSTRIAL_ROBOTIC_ARM.usdc'
* **世界包围盒 (World BBox):**
  * Size: '(1.171, 1.898, 1.690)'
  * Center: '(14.808, 28.956, 0.952)'

---

### /World/INDUSTRIAL_ROBOTIC_ARM_01

* **Prim路径 (Prim Path):**/World/INDUSTRIAL_ROBOTIC_ARM_01
* **Prim类型 (Prim Type):**Xform
* **外部引用 (Referenced USD Files):**
  * [reference] '../assets/INDUSTRIAL_ROBOTIC_ARM/INDUSTRIAL_ROBOTIC_ARM.usdc'
* **世界包围盒 (World BBox):**
  * Size: '(1.171, 1.898, 1.690)'
  * Center: '(15.127, 32.537, 0.952)'

---

## 4. 材质库 (Material Library)

### /World/Factory/Materials/material_4

* **Prim路径 (Prim Path):**/World/Factory/Materials/material_4
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/Factory/Materials/material_4/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Factory/Materials/material_4/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f]
        * Connected: '/World/Factory/Materials/material_4/tex_base.outputs:rgb' @ '/World/Factory/Materials/material_4/tex_base'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/material_4_baseColor.jpg'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(1.000, 1.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'
    * '/World/Factory/Materials/material_4/tex_base' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/material_4_baseColor.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'file' [asset] = '0/material_4_baseColor.jpg'
      * 'st' [float2]
        * Connected: '/World/Factory/Materials/material_4/uvset0.outputs:result' @ '/World/Factory/Materials/material_4/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/Factory/Materials/material_4/uvset0' (ID: 'UsdPrimvarReader_float2')
    * Implementation: 'id'

---

### /World/Factory/Materials/material_2

* **Prim路径 (Prim Path):**/World/Factory/Materials/material_2
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/Factory/Materials/material_2/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Factory/Materials/material_2/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f]
        * Connected: '/World/Factory/Materials/material_2/tex_base.outputs:rgb' @ '/World/Factory/Materials/material_2/tex_base'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/material_2_baseColor.jpg'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(1.000, 1.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'
    * '/World/Factory/Materials/material_2/tex_base' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/material_2_baseColor.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'file' [asset] = '0/material_2_baseColor.jpg'
      * 'st' [float2]
        * Connected: '/World/Factory/Materials/material_2/uvset0.outputs:result' @ '/World/Factory/Materials/material_2/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/Factory/Materials/material_2/uvset0' (ID: 'UsdPrimvarReader_float2')
    * Implementation: 'id'

---

### /World/Factory/Materials/Structure

* **Prim路径 (Prim Path):**/World/Factory/Materials/Structure
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/Factory/Materials/Structure/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Factory/Materials/Structure/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.473, 0.511, 0.476)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0.657424'
      * 'normal' [normal3f] = '(1.000, 1.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0'

---

### /World/Factory/Materials/material

* **Prim路径 (Prim Path):**/World/Factory/Materials/material
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/Factory/Materials/material/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Factory/Materials/material/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(1.000, 1.000, 1.000)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(1.000, 1.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0.845303'

---

### /World/Factory/Materials/Long_Walls

* **Prim路径 (Prim Path):**/World/Factory/Materials/Long_Walls
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/Factory/Materials/Long_Walls/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Factory/Materials/Long_Walls/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.576, 0.576, 0.576)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(1.000, 1.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0.6'

---

### /World/Factory/Materials/Wall_Horizon

* **Prim路径 (Prim Path):**/World/Factory/Materials/Wall_Horizon
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/Factory/Materials/Wall_Horizon/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Factory/Materials/Wall_Horizon/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.369, 0.341, 0.349)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(1.000, 1.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0.6'

---

### /World/Factory/Materials/Walls

* **Prim路径 (Prim Path):**/World/Factory/Materials/Walls
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/Factory/Materials/Walls/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Factory/Materials/Walls/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.718, 0.718, 0.718)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(1.000, 1.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0.6'

---

### /World/Factory/Materials/Red_Lamp

* **Prim路径 (Prim Path):**/World/Factory/Materials/Red_Lamp
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/Factory/Materials/Red_Lamp/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Factory/Materials/Red_Lamp/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'emissiveColor' [color3f] = '(1.000, 1.000, 1.000)'
      * 'metallic' [float] = '0.548333'
      * 'normal' [normal3f] = '(1.000, 1.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/Factory/Materials/Grey

* **Prim路径 (Prim Path):**/World/Factory/Materials/Grey
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/Factory/Materials/Grey/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Factory/Materials/Grey/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.686, 0.663, 0.596)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '1'
      * 'normal' [normal3f] = '(1.000, 1.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0'

---

### /World/Factory/Materials/Chris_Shirt

* **Prim路径 (Prim Path):**/World/Factory/Materials/Chris_Shirt
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/Factory/Materials/Chris_Shirt/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Factory/Materials/Chris_Shirt/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.157, 0.149, 0.204)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(1.000, 1.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0.6'

---

### /World/Factory/Materials/Chris_Shoe

* **Prim路径 (Prim Path):**/World/Factory/Materials/Chris_Shoe
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/Factory/Materials/Chris_Shoe/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Factory/Materials/Chris_Shoe/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.090, 0.086, 0.086)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(1.000, 1.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0.6'

---

### /World/Factory/Materials/Chris_Skin

* **Prim路径 (Prim Path):**/World/Factory/Materials/Chris_Skin
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/Factory/Materials/Chris_Skin/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Factory/Materials/Chris_Skin/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.753, 0.643, 0.451)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(1.000, 1.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0.6'

---

### /World/Factory/Materials/Chris_Shoe_Sole

* **Prim路径 (Prim Path):**/World/Factory/Materials/Chris_Shoe_Sole
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/Factory/Materials/Chris_Shoe_Sole/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Factory/Materials/Chris_Shoe_Sole/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.557, 0.533, 0.533)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(1.000, 1.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0.6'

---

### /World/Factory/Materials/Chris_Hair

* **Prim路径 (Prim Path):**/World/Factory/Materials/Chris_Hair
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/Factory/Materials/Chris_Hair/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Factory/Materials/Chris_Hair/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.278, 0.298, 0.290)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(1.000, 1.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0.6'

---

### /World/Factory/Materials/Chris_Pants

* **Prim路径 (Prim Path):**/World/Factory/Materials/Chris_Pants
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/Factory/Materials/Chris_Pants/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Factory/Materials/Chris_Pants/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.439, 0.392, 0.290)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(1.000, 1.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0.6'

---

### /World/Conveyor_Belt/Materials/Material_0

* **Prim路径 (Prim Path):**/World/Conveyor_Belt/Materials/Material_0
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/Conveyor_Belt/Materials/Material_0/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Conveyor_Belt/Materials/Material_0/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f]
        * Connected: '/World/Conveyor_Belt/Materials/Material_0/tex_base.outputs:rgb' @ '/World/Conveyor_Belt/Materials/Material_0/tex_base'
          * Shader ID: 'UsdUVTexture'
          * Texture: '0/Material_0_baseColor.jpg'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(1.000, 1.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0.892971'
    * '/World/Conveyor_Belt/Materials/Material_0/tex_base' (ID: 'UsdUVTexture')
    * Implementation: 'id'
    * 纹理引用 (Texture Assets):
      * '0/Material_0_baseColor.jpg'
    * Inputs:
      * 'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
      * 'file' [asset] = '0/Material_0_baseColor.jpg'
      * 'st' [float2]
        * Connected: '/World/Conveyor_Belt/Materials/Material_0/uvset0.outputs:result' @ '/World/Conveyor_Belt/Materials/Material_0/uvset0'
          * Shader ID: 'UsdPrimvarReader_float2'
    * '/World/Conveyor_Belt/Materials/Material_0/uvset0' (ID: 'UsdPrimvarReader_float2')
    * Implementation: 'id'

---

### /World/Workbench_2/Materials/Scratched_wood

* **Prim路径 (Prim Path):**/World/Workbench_2/Materials/Scratched_wood
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/Workbench_2/Materials/Scratched_wood/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Workbench_2/Materials/Scratched_wood/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.800, 0.800, 0.800)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0.821115'

---

### /World/Workbench_2/Materials/Wood_144

* **Prim路径 (Prim Path):**/World/Workbench_2/Materials/Wood_144
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/Workbench_2/Materials/Wood_144/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Workbench_2/Materials/Wood_144/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.800, 0.800, 0.800)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0.747018'

---

### /World/Workbench_2/Materials/Blueprint_Grid

* **Prim路径 (Prim Path):**/World/Workbench_2/Materials/Blueprint_Grid
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/Workbench_2/Materials/Blueprint_Grid/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/Workbench_2/Materials/Blueprint_Grid/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.800, 0.800, 0.800)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '1'

---

### /World/INDUSTRIAL_ROBOTIC_ARM/Materials/Brass___Polished

* **Prim路径 (Prim Path):**/World/INDUSTRIAL_ROBOTIC_ARM/Materials/Brass___Polished
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/INDUSTRIAL_ROBOTIC_ARM/Materials/Brass___Polished/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/INDUSTRIAL_ROBOTIC_ARM/Materials/Brass___Polished/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.953, 0.796, 0.486)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0.957705'

---

### /World/INDUSTRIAL_ROBOTIC_ARM/Materials/Aluminum___Anodized_Glossy_Grey

* **Prim路径 (Prim Path):**/World/INDUSTRIAL_ROBOTIC_ARM/Materials/Aluminum___Anodized_Glossy_Grey
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/INDUSTRIAL_ROBOTIC_ARM/Materials/Aluminum___Anodized_Glossy_Grey/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/INDUSTRIAL_ROBOTIC_ARM/Materials/Aluminum___Anodized_Glossy_Grey/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.537, 0.537, 0.537)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0.957705'

---

### /World/INDUSTRIAL_ROBOTIC_ARM/Materials/Paint___Enamel_Glossy_Yellow

* **Prim路径 (Prim Path):**/World/INDUSTRIAL_ROBOTIC_ARM/Materials/Paint___Enamel_Glossy_Yellow
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/INDUSTRIAL_ROBOTIC_ARM/Materials/Paint___Enamel_Glossy_Yellow/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/INDUSTRIAL_ROBOTIC_ARM/Materials/Paint___Enamel_Glossy_Yellow/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.910, 0.678, 0.137)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0.957705'

---

### /World/INDUSTRIAL_ROBOTIC_ARM/Materials/Body1__0

* **Prim路径 (Prim Path):**/World/INDUSTRIAL_ROBOTIC_ARM/Materials/Body1__0
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/INDUSTRIAL_ROBOTIC_ARM/Materials/Body1__0/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/INDUSTRIAL_ROBOTIC_ARM/Materials/Body1__0/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(1.000, 1.000, 1.000)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0.6'

---

### /World/INDUSTRIAL_ROBOTIC_ARM/Materials/Steel___Satin

* **Prim路径 (Prim Path):**/World/INDUSTRIAL_ROBOTIC_ARM/Materials/Steel___Satin
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/INDUSTRIAL_ROBOTIC_ARM/Materials/Steel___Satin/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/INDUSTRIAL_ROBOTIC_ARM/Materials/Steel___Satin/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.627, 0.627, 0.627)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0.957705'

---

### /World/INDUSTRIAL_ROBOTIC_ARM/Materials/Paint___Enamel_Glossy_Black

* **Prim路径 (Prim Path):**/World/INDUSTRIAL_ROBOTIC_ARM/Materials/Paint___Enamel_Glossy_Black
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/INDUSTRIAL_ROBOTIC_ARM/Materials/Paint___Enamel_Glossy_Black/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/INDUSTRIAL_ROBOTIC_ARM/Materials/Paint___Enamel_Glossy_Black/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.098, 0.098, 0.098)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0.957705'

---

### /World/INDUSTRIAL_ROBOTIC_ARM_01/Materials/Brass___Polished

* **Prim路径 (Prim Path):**/World/INDUSTRIAL_ROBOTIC_ARM_01/Materials/Brass___Polished
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/INDUSTRIAL_ROBOTIC_ARM_01/Materials/Brass___Polished/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/INDUSTRIAL_ROBOTIC_ARM_01/Materials/Brass___Polished/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.953, 0.796, 0.486)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0.957705'

---

### /World/INDUSTRIAL_ROBOTIC_ARM_01/Materials/Aluminum___Anodized_Glossy_Grey

* **Prim路径 (Prim Path):**/World/INDUSTRIAL_ROBOTIC_ARM_01/Materials/Aluminum___Anodized_Glossy_Grey
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/INDUSTRIAL_ROBOTIC_ARM_01/Materials/Aluminum___Anodized_Glossy_Grey/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/INDUSTRIAL_ROBOTIC_ARM_01/Materials/Aluminum___Anodized_Glossy_Grey/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.537, 0.537, 0.537)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0.957705'

---

### /World/INDUSTRIAL_ROBOTIC_ARM_01/Materials/Paint___Enamel_Glossy_Yellow

* **Prim路径 (Prim Path):**/World/INDUSTRIAL_ROBOTIC_ARM_01/Materials/Paint___Enamel_Glossy_Yellow
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/INDUSTRIAL_ROBOTIC_ARM_01/Materials/Paint___Enamel_Glossy_Yellow/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/INDUSTRIAL_ROBOTIC_ARM_01/Materials/Paint___Enamel_Glossy_Yellow/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.910, 0.678, 0.137)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0.957705'

---

### /World/INDUSTRIAL_ROBOTIC_ARM_01/Materials/Body1__0

* **Prim路径 (Prim Path):**/World/INDUSTRIAL_ROBOTIC_ARM_01/Materials/Body1__0
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/INDUSTRIAL_ROBOTIC_ARM_01/Materials/Body1__0/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/INDUSTRIAL_ROBOTIC_ARM_01/Materials/Body1__0/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(1.000, 1.000, 1.000)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0.6'

---

### /World/INDUSTRIAL_ROBOTIC_ARM_01/Materials/Steel___Satin

* **Prim路径 (Prim Path):**/World/INDUSTRIAL_ROBOTIC_ARM_01/Materials/Steel___Satin
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/INDUSTRIAL_ROBOTIC_ARM_01/Materials/Steel___Satin/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/INDUSTRIAL_ROBOTIC_ARM_01/Materials/Steel___Satin/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.627, 0.627, 0.627)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0.957705'

---

### /World/INDUSTRIAL_ROBOTIC_ARM_01/Materials/Paint___Enamel_Glossy_Black

* **Prim路径 (Prim Path):**/World/INDUSTRIAL_ROBOTIC_ARM_01/Materials/Paint___Enamel_Glossy_Black
* **Prim类型 (Prim Type):**Material
* **材质网络 (Material & Shader Details):**
  * **Surface Outputs:**
    * 'outputs:surface' -> '/World/INDUSTRIAL_ROBOTIC_ARM_01/Materials/Paint___Enamel_Glossy_Black/pbr_shader'
    * Shader ID: 'UsdPreviewSurface'
    * Connection: 'surface' (Output)'
  * **Shader 节点 (Shader Nodes):**
    * '/World/INDUSTRIAL_ROBOTIC_ARM_01/Materials/Paint___Enamel_Glossy_Black/pbr_shader' (ID: 'UsdPreviewSurface')
    * Implementation: 'id'
    * Inputs:
      * 'diffuseColor' [color3f] = '(0.098, 0.098, 0.098)'
      * 'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
      * 'metallic' [float] = '0'
      * 'normal' [normal3f] = '(0.000, 0.000, 1.000)'
      * 'occlusion' [float] = '1'
      * 'roughness' [float] = '0.957705'

---
