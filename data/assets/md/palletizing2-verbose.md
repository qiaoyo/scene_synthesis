# USDA场景描述文档:palletizing2.usda

## 1.场景元数据(Scene Metadata)
*  **USDA文件路径(USDA File Path):**`/media/simple/another_Documents/isaacsim_assets/scenedata/palletizing2.usda`
*  **默认Prim (Default Prim):**'Not Set'
*  **单位与坐标系 (Units & Coordinate System):**
   *   **米(Meters Per Unit):**1.0
   *   **Up Axis:**Z
* **场景描述(Scene Describe):** 该场景展现了一个高度密集且极具规模感的智能化码垛流水线矩阵，整体规划深刻体现了现代工业对并行处理效率与空间极致利用的追求。从空间格局上看，车间地面铺设了具有大理石质感的灰色宽幅瓷砖，砖面光洁且缝隙齐整，为底层移动设备的精确定位提供了理想的物理基础。厂区整体被划分为多个重复的自动化作业带，这些作业带在空间上呈严格的等间距平行排布，形成了一个壮观的工业矩阵。核心设备由多达五组以上的标准化作业单元构成，每一组单元都采用了高度一致的配置：首先是作为物料主轴的带式输送机，这些输送机采用亮银色的金属框架支撑，支腿纤细而稳固，黑色防滑皮带上正密集载运着淡黄色的方形纸质包装箱，工件流动方向整齐划一。紧邻每一条输送机的末端，都配套部署了一个白色的模块化工作站，该工作站由一个带有抽屉的白色控制柜体和浅木纹顶面的操作台组成，台面上安装有一台修长的白色六轴协作机器人。这些机器人的机械臂在不同工位呈现出各异的作业姿态，有的正准备抓取，有的已完成定位，这种异步并行的工作状态极大地平滑了整线的生产节奏。特别值得注意的是，部分机器人的小臂或关节处喷涂了醒目的亮黄色，这不仅起到了视觉警示作用，也便于在密集作业环境中区分不同的机械模块。在工作站的侧下方，部署了相对应的自动化物流接驳模块，由一系列亮黄色的自动导引运输车（AGV）组成。这些AGV底盘低矮，顶部载有一个黑色的承载框，框内已整齐叠放了多个已封装的纸质包装箱，标志着产品已从静态的生产线成功流转至动态的移动物流环节。从设备排布方式与整体规划结构分析，该场景采用了典型的“线性输送+单元处理+柔性接驳”的复合架构。五条或更多的输送线构成了车间的生产骨干，而与之垂直或平行排布的协作机器人工作站则是精细化操作的节点，底层的AGV集群则通过网格化的地面路径实现了各节点间物料的柔性转运。这种“蜂窝式”的布局方式通过高度重复的标准化单元消除了单点故障对整线的影响，展现了极强的产能调节灵活性。所有设备在空间上的间距经过了精密的防撞与效率计算，确保了机器人在最大包络圆内作业时互不干扰，同时也为AGV在繁忙的通道内预留了充足的避障与转向空间。整个画面色彩明快且区分度高：银灰色的输送架、白色的机器人柜体、亮黄色的移动底座以及浅木色的台面，共同构成了一个逻辑严密、秩序井然且充满了工业4.0美学的柔性制造生态系统。该场景中没有冗余的人工通道或乱堆的杂物，所有物流流向均由自动化系统闭环控制，深刻诠释了现代工厂在实现高产量与高精度平衡方面的卓越设计能力。
* **设备数量(Device Number):**
  * **Scene: 1**
  * **IndustrialRobot: 16**
  * **Workbench: 16**
  * **Conveyor: 8**
  * **AGV: 8**
  * **Forklift: 0**
  * **Box: 104**
  * **Rack: 0**
  * **Pallet: 0**
  * **Part: 0**
  * **Decoration: 0**

## 2.场景对象层级(Scene Hierarchy)
*   Render (Prim)
    *   OmniverseKit (Prim)
        *   HydraTextures (Prim)
            *   omni_kit_widget_viewport_ViewportTexture_0 (RenderProduct)
    *   OmniverseGlobalRenderSettings (RenderSettings)
    *   Vars (Prim)
        *   LdrColor (RenderVar)
*   World (Prim)
    *   DomeLight (DomeLight)
    *   SunLight (DistantLight)
    *   IndoorLight (SphereLight)
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
    *   agv_1 (Xform)
        *   chassis (Xform)
            *   Collision (Cube)
            *   Collision_01 (Cube)
            *   Body (Xform)
                *   Looks (Scope)
                    *   Robot (Material)
                        *   Robot (Shader)
                *   Body (Xform)
                    *   Mesh (Mesh)
        *   left_wheel (Xform)
            *   Left_Wheel (Xform)
                *   Looks (Scope)
                    *   Robot (Material)
                        *   Robot (Shader)
                *   Left_Wheel (Xform)
                    *   Mesh_002 (Mesh)
            *   Cylinder (Cylinder)
        *   right_wheel (Xform)
            *   Right_Wheel (Xform)
                *   Looks (Scope)
                    *   Robot (Material)
                        *   Robot (Shader)
                *   Right_Wheel (Xform)
                    *   Mesh_005 (Mesh)
            *   Cylinder (Cylinder)
        *   lift (Xform)
            *   Collision (Cube)
            *   Lift (Xform)
                *   Looks (Scope)
                    *   Robot (Material)
                        *   Robot (Shader)
                *   Lift (Xform)
                    *   Mesh_012 (Mesh)
        *   left_swivel (Xform)
            *   Collision (Cube)
            *   Left_Swivel (Xform)
                *   STR_Left_Swivel (Mesh)
                *   materials (Xform)
                    *   Looks (Scope)
                        *   Robot (Material)
                            *   Robot (Shader)
        *   right_swivel (Xform)
            *   Collision (Cube)
            *   Right_Swivel (Xform)
                *   STR_Right_Swivel (Mesh)
                *   materials (Xform)
                    *   Looks (Scope)
                        *   Robot (Material)
                            *   Robot (Shader)
        *   left_caster (Xform)
            *   Collision (Sphere)
            *   Inner_Left_Wheel (Xform)
                *   STR_Inner_Left_Wheel (Mesh)
                *   materials (Xform)
                    *   Looks (Scope)
                        *   Robot (Material)
                            *   Robot (Shader)
        *   right_caster (Xform)
            *   Collision (Sphere)
            *   Inner_Right_Wheel (Xform)
                *   STR_Inner_Right_Wheel (Mesh)
                *   materials (Xform)
                    *   Looks (Scope)
                        *   Robot (Material)
                            *   Robot (Shader)
        *   left_wheel_joint (PhysicsRevoluteJoint)
        *   right_wheel_joint (PhysicsRevoluteJoint)
        *   left_swivel_joint (PhysicsRevoluteJoint)
        *   right_swivel_joint (PhysicsRevoluteJoint)
        *   left_caster_joint (PhysicsRevoluteJoint)
        *   right_caster_joint (PhysicsRevoluteJoint)
        *   lift_joint (PhysicsPrismaticJoint)
        *   wheel_material (Material)
        *   caster_material (Material)
    *   agv_2 (Xform)
        *   chassis (Xform)
            *   Collision (Cube)
            *   Collision_01 (Cube)
            *   Body (Xform)
                *   Looks (Scope)
                    *   Robot (Material)
                        *   Robot (Shader)
                *   Body (Xform)
                    *   Mesh (Mesh)
        *   left_wheel (Xform)
            *   Left_Wheel (Xform)
                *   Looks (Scope)
                    *   Robot (Material)
                        *   Robot (Shader)
                *   Left_Wheel (Xform)
                    *   Mesh_002 (Mesh)
            *   Cylinder (Cylinder)
        *   right_wheel (Xform)
            *   Right_Wheel (Xform)
                *   Looks (Scope)
                    *   Robot (Material)
                        *   Robot (Shader)
                *   Right_Wheel (Xform)
                    *   Mesh_005 (Mesh)
            *   Cylinder (Cylinder)
        *   lift (Xform)
            *   Collision (Cube)
            *   Lift (Xform)
                *   Looks (Scope)
                    *   Robot (Material)
                        *   Robot (Shader)
                *   Lift (Xform)
                    *   Mesh_012 (Mesh)
        *   left_swivel (Xform)
            *   Collision (Cube)
            *   Left_Swivel (Xform)
                *   STR_Left_Swivel (Mesh)
                *   materials (Xform)
                    *   Looks (Scope)
                        *   Robot (Material)
                            *   Robot (Shader)
        *   right_swivel (Xform)
            *   Collision (Cube)
            *   Right_Swivel (Xform)
                *   STR_Right_Swivel (Mesh)
                *   materials (Xform)
                    *   Looks (Scope)
                        *   Robot (Material)
                            *   Robot (Shader)
        *   left_caster (Xform)
            *   Collision (Sphere)
            *   Inner_Left_Wheel (Xform)
                *   STR_Inner_Left_Wheel (Mesh)
                *   materials (Xform)
                    *   Looks (Scope)
                        *   Robot (Material)
                            *   Robot (Shader)
        *   right_caster (Xform)
            *   Collision (Sphere)
            *   Inner_Right_Wheel (Xform)
                *   STR_Inner_Right_Wheel (Mesh)
                *   materials (Xform)
                    *   Looks (Scope)
                        *   Robot (Material)
                            *   Robot (Shader)
        *   left_wheel_joint (PhysicsRevoluteJoint)
        *   right_wheel_joint (PhysicsRevoluteJoint)
        *   left_swivel_joint (PhysicsRevoluteJoint)
        *   right_swivel_joint (PhysicsRevoluteJoint)
        *   left_caster_joint (PhysicsRevoluteJoint)
        *   right_caster_joint (PhysicsRevoluteJoint)
        *   lift_joint (PhysicsPrismaticJoint)
        *   wheel_material (Material)
        *   caster_material (Material)
    *   agv_3 (Xform)
        *   chassis (Xform)
            *   Collision (Cube)
            *   Collision_01 (Cube)
            *   Body (Xform)
                *   Looks (Scope)
                    *   Robot (Material)
                        *   Robot (Shader)
                *   Body (Xform)
                    *   Mesh (Mesh)
        *   left_wheel (Xform)
            *   Left_Wheel (Xform)
                *   Looks (Scope)
                    *   Robot (Material)
                        *   Robot (Shader)
                *   Left_Wheel (Xform)
                    *   Mesh_002 (Mesh)
            *   Cylinder (Cylinder)
        *   right_wheel (Xform)
            *   Right_Wheel (Xform)
                *   Looks (Scope)
                    *   Robot (Material)
                        *   Robot (Shader)
                *   Right_Wheel (Xform)
                    *   Mesh_005 (Mesh)
            *   Cylinder (Cylinder)
        *   lift (Xform)
            *   Collision (Cube)
            *   Lift (Xform)
                *   Looks (Scope)
                    *   Robot (Material)
                        *   Robot (Shader)
                *   Lift (Xform)
                    *   Mesh_012 (Mesh)
        *   left_swivel (Xform)
            *   Collision (Cube)
            *   Left_Swivel (Xform)
                *   STR_Left_Swivel (Mesh)
                *   materials (Xform)
                    *   Looks (Scope)
                        *   Robot (Material)
                            *   Robot (Shader)
        *   right_swivel (Xform)
            *   Collision (Cube)
            *   Right_Swivel (Xform)
                *   STR_Right_Swivel (Mesh)
                *   materials (Xform)
                    *   Looks (Scope)
                        *   Robot (Material)
                            *   Robot (Shader)
        *   left_caster (Xform)
            *   Collision (Sphere)
            *   Inner_Left_Wheel (Xform)
                *   STR_Inner_Left_Wheel (Mesh)
                *   materials (Xform)
                    *   Looks (Scope)
                        *   Robot (Material)
                            *   Robot (Shader)
        *   right_caster (Xform)
            *   Collision (Sphere)
            *   Inner_Right_Wheel (Xform)
                *   STR_Inner_Right_Wheel (Mesh)
                *   materials (Xform)
                    *   Looks (Scope)
                        *   Robot (Material)
                            *   Robot (Shader)
        *   left_wheel_joint (PhysicsRevoluteJoint)
        *   right_wheel_joint (PhysicsRevoluteJoint)
        *   left_swivel_joint (PhysicsRevoluteJoint)
        *   right_swivel_joint (PhysicsRevoluteJoint)
        *   left_caster_joint (PhysicsRevoluteJoint)
        *   right_caster_joint (PhysicsRevoluteJoint)
        *   lift_joint (PhysicsPrismaticJoint)
        *   wheel_material (Material)
        *   caster_material (Material)
    *   agv_4 (Xform)
        *   chassis (Xform)
            *   Collision (Cube)
            *   Collision_01 (Cube)
            *   Body (Xform)
                *   Looks (Scope)
                    *   Robot (Material)
                        *   Robot (Shader)
                *   Body (Xform)
                    *   Mesh (Mesh)
        *   left_wheel (Xform)
            *   Left_Wheel (Xform)
                *   Looks (Scope)
                    *   Robot (Material)
                        *   Robot (Shader)
                *   Left_Wheel (Xform)
                    *   Mesh_002 (Mesh)
            *   Cylinder (Cylinder)
        *   right_wheel (Xform)
            *   Right_Wheel (Xform)
                *   Looks (Scope)
                    *   Robot (Material)
                        *   Robot (Shader)
                *   Right_Wheel (Xform)
                    *   Mesh_005 (Mesh)
            *   Cylinder (Cylinder)
        *   lift (Xform)
            *   Collision (Cube)
            *   Lift (Xform)
                *   Looks (Scope)
                    *   Robot (Material)
                        *   Robot (Shader)
                *   Lift (Xform)
                    *   Mesh_012 (Mesh)
        *   left_swivel (Xform)
            *   Collision (Cube)
            *   Left_Swivel (Xform)
                *   STR_Left_Swivel (Mesh)
                *   materials (Xform)
                    *   Looks (Scope)
                        *   Robot (Material)
                            *   Robot (Shader)
        *   right_swivel (Xform)
            *   Collision (Cube)
            *   Right_Swivel (Xform)
                *   STR_Right_Swivel (Mesh)
                *   materials (Xform)
                    *   Looks (Scope)
                        *   Robot (Material)
                            *   Robot (Shader)
        *   left_caster (Xform)
            *   Collision (Sphere)
            *   Inner_Left_Wheel (Xform)
                *   STR_Inner_Left_Wheel (Mesh)
                *   materials (Xform)
                    *   Looks (Scope)
                        *   Robot (Material)
                            *   Robot (Shader)
        *   right_caster (Xform)
            *   Collision (Sphere)
            *   Inner_Right_Wheel (Xform)
                *   STR_Inner_Right_Wheel (Mesh)
                *   materials (Xform)
                    *   Looks (Scope)
                        *   Robot (Material)
                            *   Robot (Shader)
        *   left_wheel_joint (PhysicsRevoluteJoint)
        *   right_wheel_joint (PhysicsRevoluteJoint)
        *   left_swivel_joint (PhysicsRevoluteJoint)
        *   right_swivel_joint (PhysicsRevoluteJoint)
        *   left_caster_joint (PhysicsRevoluteJoint)
        *   right_caster_joint (PhysicsRevoluteJoint)
        *   lift_joint (PhysicsPrismaticJoint)
        *   wheel_material (Material)
        *   caster_material (Material)
    *   agv_5 (Xform)
        *   chassis (Xform)
            *   Collision (Cube)
            *   Collision_01 (Cube)
            *   Body (Xform)
                *   Looks (Scope)
                    *   Robot (Material)
                        *   Robot (Shader)
                *   Body (Xform)
                    *   Mesh (Mesh)
        *   left_wheel (Xform)
            *   Left_Wheel (Xform)
                *   Looks (Scope)
                    *   Robot (Material)
                        *   Robot (Shader)
                *   Left_Wheel (Xform)
                    *   Mesh_002 (Mesh)
            *   Cylinder (Cylinder)
        *   right_wheel (Xform)
            *   Right_Wheel (Xform)
                *   Looks (Scope)
                    *   Robot (Material)
                        *   Robot (Shader)
                *   Right_Wheel (Xform)
                    *   Mesh_005 (Mesh)
            *   Cylinder (Cylinder)
        *   lift (Xform)
            *   Collision (Cube)
            *   Lift (Xform)
                *   Looks (Scope)
                    *   Robot (Material)
                        *   Robot (Shader)
                *   Lift (Xform)
                    *   Mesh_012 (Mesh)
        *   left_swivel (Xform)
            *   Collision (Cube)
            *   Left_Swivel (Xform)
                *   STR_Left_Swivel (Mesh)
                *   materials (Xform)
                    *   Looks (Scope)
                        *   Robot (Material)
                            *   Robot (Shader)
        *   right_swivel (Xform)
            *   Collision (Cube)
            *   Right_Swivel (Xform)
                *   STR_Right_Swivel (Mesh)
                *   materials (Xform)
                    *   Looks (Scope)
                        *   Robot (Material)
                            *   Robot (Shader)
        *   left_caster (Xform)
            *   Collision (Sphere)
            *   Inner_Left_Wheel (Xform)
                *   STR_Inner_Left_Wheel (Mesh)
                *   materials (Xform)
                    *   Looks (Scope)
                        *   Robot (Material)
                            *   Robot (Shader)
        *   right_caster (Xform)
            *   Collision (Sphere)
            *   Inner_Right_Wheel (Xform)
                *   STR_Inner_Right_Wheel (Mesh)
                *   materials (Xform)
                    *   Looks (Scope)
                        *   Robot (Material)
                            *   Robot (Shader)
        *   left_wheel_joint (PhysicsRevoluteJoint)
        *   right_wheel_joint (PhysicsRevoluteJoint)
        *   left_swivel_joint (PhysicsRevoluteJoint)
        *   right_swivel_joint (PhysicsRevoluteJoint)
        *   left_caster_joint (PhysicsRevoluteJoint)
        *   right_caster_joint (PhysicsRevoluteJoint)
        *   lift_joint (PhysicsPrismaticJoint)
        *   wheel_material (Material)
        *   caster_material (Material)
    *   agv_6 (Xform)
        *   chassis (Xform)
            *   Collision (Cube)
            *   Collision_01 (Cube)
            *   Body (Xform)
                *   Looks (Scope)
                    *   Robot (Material)
                        *   Robot (Shader)
                *   Body (Xform)
                    *   Mesh (Mesh)
        *   left_wheel (Xform)
            *   Left_Wheel (Xform)
                *   Looks (Scope)
                    *   Robot (Material)
                        *   Robot (Shader)
                *   Left_Wheel (Xform)
                    *   Mesh_002 (Mesh)
            *   Cylinder (Cylinder)
        *   right_wheel (Xform)
            *   Right_Wheel (Xform)
                *   Looks (Scope)
                    *   Robot (Material)
                        *   Robot (Shader)
                *   Right_Wheel (Xform)
                    *   Mesh_005 (Mesh)
            *   Cylinder (Cylinder)
        *   lift (Xform)
            *   Collision (Cube)
            *   Lift (Xform)
                *   Looks (Scope)
                    *   Robot (Material)
                        *   Robot (Shader)
                *   Lift (Xform)
                    *   Mesh_012 (Mesh)
        *   left_swivel (Xform)
            *   Collision (Cube)
            *   Left_Swivel (Xform)
                *   STR_Left_Swivel (Mesh)
                *   materials (Xform)
                    *   Looks (Scope)
                        *   Robot (Material)
                            *   Robot (Shader)
        *   right_swivel (Xform)
            *   Collision (Cube)
            *   Right_Swivel (Xform)
                *   STR_Right_Swivel (Mesh)
                *   materials (Xform)
                    *   Looks (Scope)
                        *   Robot (Material)
                            *   Robot (Shader)
        *   left_caster (Xform)
            *   Collision (Sphere)
            *   Inner_Left_Wheel (Xform)
                *   STR_Inner_Left_Wheel (Mesh)
                *   materials (Xform)
                    *   Looks (Scope)
                        *   Robot (Material)
                            *   Robot (Shader)
        *   right_caster (Xform)
            *   Collision (Sphere)
            *   Inner_Right_Wheel (Xform)
                *   STR_Inner_Right_Wheel (Mesh)
                *   materials (Xform)
                    *   Looks (Scope)
                        *   Robot (Material)
                            *   Robot (Shader)
        *   left_wheel_joint (PhysicsRevoluteJoint)
        *   right_wheel_joint (PhysicsRevoluteJoint)
        *   left_swivel_joint (PhysicsRevoluteJoint)
        *   right_swivel_joint (PhysicsRevoluteJoint)
        *   left_caster_joint (PhysicsRevoluteJoint)
        *   right_caster_joint (PhysicsRevoluteJoint)
        *   lift_joint (PhysicsPrismaticJoint)
        *   wheel_material (Material)
        *   caster_material (Material)
    *   agv_7 (Xform)
        *   chassis (Xform)
            *   Collision (Cube)
            *   Collision_01 (Cube)
            *   Body (Xform)
                *   Looks (Scope)
                    *   Robot (Material)
                        *   Robot (Shader)
                *   Body (Xform)
                    *   Mesh (Mesh)
        *   left_wheel (Xform)
            *   Left_Wheel (Xform)
                *   Looks (Scope)
                    *   Robot (Material)
                        *   Robot (Shader)
                *   Left_Wheel (Xform)
                    *   Mesh_002 (Mesh)
            *   Cylinder (Cylinder)
        *   right_wheel (Xform)
            *   Right_Wheel (Xform)
                *   Looks (Scope)
                    *   Robot (Material)
                        *   Robot (Shader)
                *   Right_Wheel (Xform)
                    *   Mesh_005 (Mesh)
            *   Cylinder (Cylinder)
        *   lift (Xform)
            *   Collision (Cube)
            *   Lift (Xform)
                *   Looks (Scope)
                    *   Robot (Material)
                        *   Robot (Shader)
                *   Lift (Xform)
                    *   Mesh_012 (Mesh)
        *   left_swivel (Xform)
            *   Collision (Cube)
            *   Left_Swivel (Xform)
                *   STR_Left_Swivel (Mesh)
                *   materials (Xform)
                    *   Looks (Scope)
                        *   Robot (Material)
                            *   Robot (Shader)
        *   right_swivel (Xform)
            *   Collision (Cube)
            *   Right_Swivel (Xform)
                *   STR_Right_Swivel (Mesh)
                *   materials (Xform)
                    *   Looks (Scope)
                        *   Robot (Material)
                            *   Robot (Shader)
        *   left_caster (Xform)
            *   Collision (Sphere)
            *   Inner_Left_Wheel (Xform)
                *   STR_Inner_Left_Wheel (Mesh)
                *   materials (Xform)
                    *   Looks (Scope)
                        *   Robot (Material)
                            *   Robot (Shader)
        *   right_caster (Xform)
            *   Collision (Sphere)
            *   Inner_Right_Wheel (Xform)
                *   STR_Inner_Right_Wheel (Mesh)
                *   materials (Xform)
                    *   Looks (Scope)
                        *   Robot (Material)
                            *   Robot (Shader)
        *   left_wheel_joint (PhysicsRevoluteJoint)
        *   right_wheel_joint (PhysicsRevoluteJoint)
        *   left_swivel_joint (PhysicsRevoluteJoint)
        *   right_swivel_joint (PhysicsRevoluteJoint)
        *   left_caster_joint (PhysicsRevoluteJoint)
        *   right_caster_joint (PhysicsRevoluteJoint)
        *   lift_joint (PhysicsPrismaticJoint)
        *   wheel_material (Material)
        *   caster_material (Material)
    *   agv_8 (Xform)
        *   chassis (Xform)
            *   Collision (Cube)
            *   Collision_01 (Cube)
            *   Body (Xform)
                *   Looks (Scope)
                    *   Robot (Material)
                        *   Robot (Shader)
                *   Body (Xform)
                    *   Mesh (Mesh)
        *   left_wheel (Xform)
            *   Left_Wheel (Xform)
                *   Looks (Scope)
                    *   Robot (Material)
                        *   Robot (Shader)
                *   Left_Wheel (Xform)
                    *   Mesh_002 (Mesh)
            *   Cylinder (Cylinder)
        *   right_wheel (Xform)
            *   Right_Wheel (Xform)
                *   Looks (Scope)
                    *   Robot (Material)
                        *   Robot (Shader)
                *   Right_Wheel (Xform)
                    *   Mesh_005 (Mesh)
            *   Cylinder (Cylinder)
        *   lift (Xform)
            *   Collision (Cube)
            *   Lift (Xform)
                *   Looks (Scope)
                    *   Robot (Material)
                        *   Robot (Shader)
                *   Lift (Xform)
                    *   Mesh_012 (Mesh)
        *   left_swivel (Xform)
            *   Collision (Cube)
            *   Left_Swivel (Xform)
                *   STR_Left_Swivel (Mesh)
                *   materials (Xform)
                    *   Looks (Scope)
                        *   Robot (Material)
                            *   Robot (Shader)
        *   right_swivel (Xform)
            *   Collision (Cube)
            *   Right_Swivel (Xform)
                *   STR_Right_Swivel (Mesh)
                *   materials (Xform)
                    *   Looks (Scope)
                        *   Robot (Material)
                            *   Robot (Shader)
        *   left_caster (Xform)
            *   Collision (Sphere)
            *   Inner_Left_Wheel (Xform)
                *   STR_Inner_Left_Wheel (Mesh)
                *   materials (Xform)
                    *   Looks (Scope)
                        *   Robot (Material)
                            *   Robot (Shader)
        *   right_caster (Xform)
            *   Collision (Sphere)
            *   Inner_Right_Wheel (Xform)
                *   STR_Inner_Right_Wheel (Mesh)
                *   materials (Xform)
                    *   Looks (Scope)
                        *   Robot (Material)
                            *   Robot (Shader)
        *   left_wheel_joint (PhysicsRevoluteJoint)
        *   right_wheel_joint (PhysicsRevoluteJoint)
        *   left_swivel_joint (PhysicsRevoluteJoint)
        *   right_swivel_joint (PhysicsRevoluteJoint)
        *   left_caster_joint (PhysicsRevoluteJoint)
        *   right_caster_joint (PhysicsRevoluteJoint)
        *   lift_joint (PhysicsPrismaticJoint)
        *   wheel_material (Material)
        *   caster_material (Material)
    *   Conveyor_1 (Xform)
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
    *   Conveyor_2 (Xform)
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
    *   Conveyor_3 (Xform)
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
    *   Conveyor_4 (Xform)
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
    *   Conveyor_5 (Xform)
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
    *   Conveyor_6 (Xform)
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
    *   Conveyor_7 (Xform)
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
    *   Conveyor_8 (Xform)
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
    *   BoxOnConveyor_1 (Xform)
        *   Materials (Scope)
            *   _6___Default (Material)
                *   pbr_shader (Shader)
                *   uvset0 (Shader)
                *   tex_base (Shader)
        *   Meshes (Xform)
            *   Sketchfab_model (Xform)
                *   f49ad5edc352496894d3a02181012422_fbx (Xform)
                    *   RootNode (Xform)
                        *   Box072 (Xform)
                            *   Box072_06___Default_0 (Xform)
                                *   Box072_06___Default_0 (Mesh)
    *   BoxOnConveyor_2 (Xform)
        *   Materials (Scope)
            *   _6___Default (Material)
                *   pbr_shader (Shader)
                *   uvset0 (Shader)
                *   tex_base (Shader)
        *   Meshes (Xform)
            *   Sketchfab_model (Xform)
                *   f49ad5edc352496894d3a02181012422_fbx (Xform)
                    *   RootNode (Xform)
                        *   Box072 (Xform)
                            *   Box072_06___Default_0 (Xform)
                                *   Box072_06___Default_0 (Mesh)
    *   BoxOnConveyor_3 (Xform)
        *   Materials (Scope)
            *   _6___Default (Material)
                *   pbr_shader (Shader)
                *   uvset0 (Shader)
                *   tex_base (Shader)
        *   Meshes (Xform)
            *   Sketchfab_model (Xform)
                *   f49ad5edc352496894d3a02181012422_fbx (Xform)
                    *   RootNode (Xform)
                        *   Box072 (Xform)
                            *   Box072_06___Default_0 (Xform)
                                *   Box072_06___Default_0 (Mesh)
    *   BoxOnConveyor_4 (Xform)
        *   Materials (Scope)
            *   _6___Default (Material)
                *   pbr_shader (Shader)
                *   uvset0 (Shader)
                *   tex_base (Shader)
        *   Meshes (Xform)
            *   Sketchfab_model (Xform)
                *   f49ad5edc352496894d3a02181012422_fbx (Xform)
                    *   RootNode (Xform)
                        *   Box072 (Xform)
                            *   Box072_06___Default_0 (Xform)
                                *   Box072_06___Default_0 (Mesh)
    *   BoxOnConveyor_5 (Xform)
        *   Materials (Scope)
            *   _6___Default (Material)
                *   pbr_shader (Shader)
                *   uvset0 (Shader)
                *   tex_base (Shader)
        *   Meshes (Xform)
            *   Sketchfab_model (Xform)
                *   f49ad5edc352496894d3a02181012422_fbx (Xform)
                    *   RootNode (Xform)
                        *   Box072 (Xform)
                            *   Box072_06___Default_0 (Xform)
                                *   Box072_06___Default_0 (Mesh)
    *   BoxOnConveyor_6 (Xform)
        *   Materials (Scope)
            *   _6___Default (Material)
                *   pbr_shader (Shader)
                *   uvset0 (Shader)
                *   tex_base (Shader)
        *   Meshes (Xform)
            *   Sketchfab_model (Xform)
                *   f49ad5edc352496894d3a02181012422_fbx (Xform)
                    *   RootNode (Xform)
                        *   Box072 (Xform)
                            *   Box072_06___Default_0 (Xform)
                                *   Box072_06___Default_0 (Mesh)
    *   BoxOnConveyor_7 (Xform)
        *   Materials (Scope)
            *   _6___Default (Material)
                *   pbr_shader (Shader)
                *   uvset0 (Shader)
                *   tex_base (Shader)
        *   Meshes (Xform)
            *   Sketchfab_model (Xform)
                *   f49ad5edc352496894d3a02181012422_fbx (Xform)
                    *   RootNode (Xform)
                        *   Box072 (Xform)
                            *   Box072_06___Default_0 (Xform)
                                *   Box072_06___Default_0 (Mesh)
    *   BoxOnConveyor_8 (Xform)
        *   Materials (Scope)
            *   _6___Default (Material)
                *   pbr_shader (Shader)
                *   uvset0 (Shader)
                *   tex_base (Shader)
        *   Meshes (Xform)
            *   Sketchfab_model (Xform)
                *   f49ad5edc352496894d3a02181012422_fbx (Xform)
                    *   RootNode (Xform)
                        *   Box072 (Xform)
                            *   Box072_06___Default_0 (Xform)
                                *   Box072_06___Default_0 (Mesh)
    *   BoxOnConveyor_9 (Xform)
        *   Materials (Scope)
            *   _6___Default (Material)
                *   pbr_shader (Shader)
                *   uvset0 (Shader)
                *   tex_base (Shader)
        *   Meshes (Xform)
            *   Sketchfab_model (Xform)
                *   f49ad5edc352496894d3a02181012422_fbx (Xform)
                    *   RootNode (Xform)
                        *   Box072 (Xform)
                            *   Box072_06___Default_0 (Xform)
                                *   Box072_06___Default_0 (Mesh)
    *   BoxOnConveyor_10 (Xform)
        *   Materials (Scope)
            *   _6___Default (Material)
                *   pbr_shader (Shader)
                *   uvset0 (Shader)
                *   tex_base (Shader)
        *   Meshes (Xform)
            *   Sketchfab_model (Xform)
                *   f49ad5edc352496894d3a02181012422_fbx (Xform)
                    *   RootNode (Xform)
                        *   Box072 (Xform)
                            *   Box072_06___Default_0 (Xform)
                                *   Box072_06___Default_0 (Mesh)
    *   BoxOnConveyor_11 (Xform)
        *   Materials (Scope)
            *   _6___Default (Material)
                *   pbr_shader (Shader)
                *   uvset0 (Shader)
                *   tex_base (Shader)
        *   Meshes (Xform)
            *   Sketchfab_model (Xform)
                *   f49ad5edc352496894d3a02181012422_fbx (Xform)
                    *   RootNode (Xform)
                        *   Box072 (Xform)
                            *   Box072_06___Default_0 (Xform)
                                *   Box072_06___Default_0 (Mesh)
    *   BoxOnConveyor_12 (Xform)
        *   Materials (Scope)
            *   _6___Default (Material)
                *   pbr_shader (Shader)
                *   uvset0 (Shader)
                *   tex_base (Shader)
        *   Meshes (Xform)
            *   Sketchfab_model (Xform)
                *   f49ad5edc352496894d3a02181012422_fbx (Xform)
                    *   RootNode (Xform)
                        *   Box072 (Xform)
                            *   Box072_06___Default_0 (Xform)
                                *   Box072_06___Default_0 (Mesh)
    *   BoxOnConveyor_13 (Xform)
        *   Materials (Scope)
            *   _6___Default (Material)
                *   pbr_shader (Shader)
                *   uvset0 (Shader)
                *   tex_base (Shader)
        *   Meshes (Xform)
            *   Sketchfab_model (Xform)
                *   f49ad5edc352496894d3a02181012422_fbx (Xform)
                    *   RootNode (Xform)
                        *   Box072 (Xform)
                            *   Box072_06___Default_0 (Xform)
                                *   Box072_06___Default_0 (Mesh)
    *   BoxOnConveyor_14 (Xform)
        *   Materials (Scope)
            *   _6___Default (Material)
                *   pbr_shader (Shader)
                *   uvset0 (Shader)
                *   tex_base (Shader)
        *   Meshes (Xform)
            *   Sketchfab_model (Xform)
                *   f49ad5edc352496894d3a02181012422_fbx (Xform)
                    *   RootNode (Xform)
                        *   Box072 (Xform)
                            *   Box072_06___Default_0 (Xform)
                                *   Box072_06___Default_0 (Mesh)
    *   BoxOnConveyor_15 (Xform)
        *   Materials (Scope)
            *   _6___Default (Material)
                *   pbr_shader (Shader)
                *   uvset0 (Shader)
                *   tex_base (Shader)
        *   Meshes (Xform)
            *   Sketchfab_model (Xform)
                *   f49ad5edc352496894d3a02181012422_fbx (Xform)
                    *   RootNode (Xform)
                        *   Box072 (Xform)
                            *   Box072_06___Default_0 (Xform)
                                *   Box072_06___Default_0 (Mesh)
    *   BoxOnConveyor_16 (Xform)
        *   Materials (Scope)
            *   _6___Default (Material)
                *   pbr_shader (Shader)
                *   uvset0 (Shader)
                *   tex_base (Shader)
        *   Meshes (Xform)
            *   Sketchfab_model (Xform)
                *   f49ad5edc352496894d3a02181012422_fbx (Xform)
                    *   RootNode (Xform)
                        *   Box072 (Xform)
                            *   Box072_06___Default_0 (Xform)
                                *   Box072_06___Default_0 (Mesh)
    *   BoxOnConveyor_17 (Xform)
        *   Materials (Scope)
            *   _6___Default (Material)
                *   pbr_shader (Shader)
                *   uvset0 (Shader)
                *   tex_base (Shader)
        *   Meshes (Xform)
            *   Sketchfab_model (Xform)
                *   f49ad5edc352496894d3a02181012422_fbx (Xform)
                    *   RootNode (Xform)
                        *   Box072 (Xform)
                            *   Box072_06___Default_0 (Xform)
                                *   Box072_06___Default_0 (Mesh)
    *   BoxOnConveyor_18 (Xform)
        *   Materials (Scope)
            *   _6___Default (Material)
                *   pbr_shader (Shader)
                *   uvset0 (Shader)
                *   tex_base (Shader)
        *   Meshes (Xform)
            *   Sketchfab_model (Xform)
                *   f49ad5edc352496894d3a02181012422_fbx (Xform)
                    *   RootNode (Xform)
                        *   Box072 (Xform)
                            *   Box072_06___Default_0 (Xform)
                                *   Box072_06___Default_0 (Mesh)
    *   BoxOnConveyor_19 (Xform)
        *   Materials (Scope)
            *   _6___Default (Material)
                *   pbr_shader (Shader)
                *   uvset0 (Shader)
                *   tex_base (Shader)
        *   Meshes (Xform)
            *   Sketchfab_model (Xform)
                *   f49ad5edc352496894d3a02181012422_fbx (Xform)
                    *   RootNode (Xform)
                        *   Box072 (Xform)
                            *   Box072_06___Default_0 (Xform)
                                *   Box072_06___Default_0 (Mesh)
    *   BoxOnConveyor_20 (Xform)
        *   Materials (Scope)
            *   _6___Default (Material)
                *   pbr_shader (Shader)
                *   uvset0 (Shader)
                *   tex_base (Shader)
        *   Meshes (Xform)
            *   Sketchfab_model (Xform)
                *   f49ad5edc352496894d3a02181012422_fbx (Xform)
                    *   RootNode (Xform)
                        *   Box072 (Xform)
                            *   Box072_06___Default_0 (Xform)
                                *   Box072_06___Default_0 (Mesh)
    *   BoxOnConveyor_21 (Xform)
        *   Materials (Scope)
            *   _6___Default (Material)
                *   pbr_shader (Shader)
                *   uvset0 (Shader)
                *   tex_base (Shader)
        *   Meshes (Xform)
            *   Sketchfab_model (Xform)
                *   f49ad5edc352496894d3a02181012422_fbx (Xform)
                    *   RootNode (Xform)
                        *   Box072 (Xform)
                            *   Box072_06___Default_0 (Xform)
                                *   Box072_06___Default_0 (Mesh)
    *   BoxOnConveyor_22 (Xform)
        *   Materials (Scope)
            *   _6___Default (Material)
                *   pbr_shader (Shader)
                *   uvset0 (Shader)
                *   tex_base (Shader)
        *   Meshes (Xform)
            *   Sketchfab_model (Xform)
                *   f49ad5edc352496894d3a02181012422_fbx (Xform)
                    *   RootNode (Xform)
                        *   Box072 (Xform)
                            *   Box072_06___Default_0 (Xform)
                                *   Box072_06___Default_0 (Mesh)
    *   BoxOnConveyor_23 (Xform)
        *   Materials (Scope)
            *   _6___Default (Material)
                *   pbr_shader (Shader)
                *   uvset0 (Shader)
                *   tex_base (Shader)
        *   Meshes (Xform)
            *   Sketchfab_model (Xform)
                *   f49ad5edc352496894d3a02181012422_fbx (Xform)
                    *   RootNode (Xform)
                        *   Box072 (Xform)
                            *   Box072_06___Default_0 (Xform)
                                *   Box072_06___Default_0 (Mesh)
    *   BoxOnConveyor_24 (Xform)
        *   Materials (Scope)
            *   _6___Default (Material)
                *   pbr_shader (Shader)
                *   uvset0 (Shader)
                *   tex_base (Shader)
        *   Meshes (Xform)
            *   Sketchfab_model (Xform)
                *   f49ad5edc352496894d3a02181012422_fbx (Xform)
                    *   RootNode (Xform)
                        *   Box072 (Xform)
                            *   Box072_06___Default_0 (Xform)
                                *   Box072_06___Default_0 (Mesh)
    *   BoxOnConveyor_25 (Xform)
        *   Materials (Scope)
            *   _6___Default (Material)
                *   pbr_shader (Shader)
                *   uvset0 (Shader)
                *   tex_base (Shader)
        *   Meshes (Xform)
            *   Sketchfab_model (Xform)
                *   f49ad5edc352496894d3a02181012422_fbx (Xform)
                    *   RootNode (Xform)
                        *   Box072 (Xform)
                            *   Box072_06___Default_0 (Xform)
                                *   Box072_06___Default_0 (Mesh)
    *   BoxOnConveyor_26 (Xform)
        *   Materials (Scope)
            *   _6___Default (Material)
                *   pbr_shader (Shader)
                *   uvset0 (Shader)
                *   tex_base (Shader)
        *   Meshes (Xform)
            *   Sketchfab_model (Xform)
                *   f49ad5edc352496894d3a02181012422_fbx (Xform)
                    *   RootNode (Xform)
                        *   Box072 (Xform)
                            *   Box072_06___Default_0 (Xform)
                                *   Box072_06___Default_0 (Mesh)
    *   BoxOnConveyor_27 (Xform)
        *   Materials (Scope)
            *   _6___Default (Material)
                *   pbr_shader (Shader)
                *   uvset0 (Shader)
                *   tex_base (Shader)
        *   Meshes (Xform)
            *   Sketchfab_model (Xform)
                *   f49ad5edc352496894d3a02181012422_fbx (Xform)
                    *   RootNode (Xform)
                        *   Box072 (Xform)
                            *   Box072_06___Default_0 (Xform)
                                *   Box072_06___Default_0 (Mesh)
    *   BoxOnConveyor_28 (Xform)
        *   Materials (Scope)
            *   _6___Default (Material)
                *   pbr_shader (Shader)
                *   uvset0 (Shader)
                *   tex_base (Shader)
        *   Meshes (Xform)
            *   Sketchfab_model (Xform)
                *   f49ad5edc352496894d3a02181012422_fbx (Xform)
                    *   RootNode (Xform)
                        *   Box072 (Xform)
                            *   Box072_06___Default_0 (Xform)
                                *   Box072_06___Default_0 (Mesh)
    *   BoxOnConveyor_29 (Xform)
        *   Materials (Scope)
            *   _6___Default (Material)
                *   pbr_shader (Shader)
                *   uvset0 (Shader)
                *   tex_base (Shader)
        *   Meshes (Xform)
            *   Sketchfab_model (Xform)
                *   f49ad5edc352496894d3a02181012422_fbx (Xform)
                    *   RootNode (Xform)
                        *   Box072 (Xform)
                            *   Box072_06___Default_0 (Xform)
                                *   Box072_06___Default_0 (Mesh)
    *   BoxOnConveyor_30 (Xform)
        *   Materials (Scope)
            *   _6___Default (Material)
                *   pbr_shader (Shader)
                *   uvset0 (Shader)
                *   tex_base (Shader)
        *   Meshes (Xform)
            *   Sketchfab_model (Xform)
                *   f49ad5edc352496894d3a02181012422_fbx (Xform)
                    *   RootNode (Xform)
                        *   Box072 (Xform)
                            *   Box072_06___Default_0 (Xform)
                                *   Box072_06___Default_0 (Mesh)
    *   BoxOnConveyor_31 (Xform)
        *   Materials (Scope)
            *   _6___Default (Material)
                *   pbr_shader (Shader)
                *   uvset0 (Shader)
                *   tex_base (Shader)
        *   Meshes (Xform)
            *   Sketchfab_model (Xform)
                *   f49ad5edc352496894d3a02181012422_fbx (Xform)
                    *   RootNode (Xform)
                        *   Box072 (Xform)
                            *   Box072_06___Default_0 (Xform)
                                *   Box072_06___Default_0 (Mesh)
    *   BoxOnConveyor_32 (Xform)
        *   Materials (Scope)
            *   _6___Default (Material)
                *   pbr_shader (Shader)
                *   uvset0 (Shader)
                *   tex_base (Shader)
        *   Meshes (Xform)
            *   Sketchfab_model (Xform)
                *   f49ad5edc352496894d3a02181012422_fbx (Xform)
                    *   RootNode (Xform)
                        *   Box072 (Xform)
                            *   Box072_06___Default_0 (Xform)
                                *   Box072_06___Default_0 (Mesh)
    *   BoxOnConveyor_33 (Xform)
        *   Materials (Scope)
            *   _6___Default (Material)
                *   pbr_shader (Shader)
                *   uvset0 (Shader)
                *   tex_base (Shader)
        *   Meshes (Xform)
            *   Sketchfab_model (Xform)
                *   f49ad5edc352496894d3a02181012422_fbx (Xform)
                    *   RootNode (Xform)
                        *   Box072 (Xform)
                            *   Box072_06___Default_0 (Xform)
                                *   Box072_06___Default_0 (Mesh)
    *   BoxOnConveyor_34 (Xform)
        *   Materials (Scope)
            *   _6___Default (Material)
                *   pbr_shader (Shader)
                *   uvset0 (Shader)
                *   tex_base (Shader)
        *   Meshes (Xform)
            *   Sketchfab_model (Xform)
                *   f49ad5edc352496894d3a02181012422_fbx (Xform)
                    *   RootNode (Xform)
                        *   Box072 (Xform)
                            *   Box072_06___Default_0 (Xform)
                                *   Box072_06___Default_0 (Mesh)
    *   BoxOnConveyor_35 (Xform)
        *   Materials (Scope)
            *   _6___Default (Material)
                *   pbr_shader (Shader)
                *   uvset0 (Shader)
                *   tex_base (Shader)
        *   Meshes (Xform)
            *   Sketchfab_model (Xform)
                *   f49ad5edc352496894d3a02181012422_fbx (Xform)
                    *   RootNode (Xform)
                        *   Box072 (Xform)
                            *   Box072_06___Default_0 (Xform)
                                *   Box072_06___Default_0 (Mesh)
    *   BoxOnConveyor_36 (Xform)
        *   Materials (Scope)
            *   _6___Default (Material)
                *   pbr_shader (Shader)
                *   uvset0 (Shader)
                *   tex_base (Shader)
        *   Meshes (Xform)
            *   Sketchfab_model (Xform)
                *   f49ad5edc352496894d3a02181012422_fbx (Xform)
                    *   RootNode (Xform)
                        *   Box072 (Xform)
                            *   Box072_06___Default_0 (Xform)
                                *   Box072_06___Default_0 (Mesh)
    *   BoxOnConveyor_37 (Xform)
        *   Materials (Scope)
            *   _6___Default (Material)
                *   pbr_shader (Shader)
                *   uvset0 (Shader)
                *   tex_base (Shader)
        *   Meshes (Xform)
            *   Sketchfab_model (Xform)
                *   f49ad5edc352496894d3a02181012422_fbx (Xform)
                    *   RootNode (Xform)
                        *   Box072 (Xform)
                            *   Box072_06___Default_0 (Xform)
                                *   Box072_06___Default_0 (Mesh)
    *   BoxOnConveyor_38 (Xform)
        *   Materials (Scope)
            *   _6___Default (Material)
                *   pbr_shader (Shader)
                *   uvset0 (Shader)
                *   tex_base (Shader)
        *   Meshes (Xform)
            *   Sketchfab_model (Xform)
                *   f49ad5edc352496894d3a02181012422_fbx (Xform)
                    *   RootNode (Xform)
                        *   Box072 (Xform)
                            *   Box072_06___Default_0 (Xform)
                                *   Box072_06___Default_0 (Mesh)
    *   BoxOnConveyor_39 (Xform)
        *   Materials (Scope)
            *   _6___Default (Material)
                *   pbr_shader (Shader)
                *   uvset0 (Shader)
                *   tex_base (Shader)
        *   Meshes (Xform)
            *   Sketchfab_model (Xform)
                *   f49ad5edc352496894d3a02181012422_fbx (Xform)
                    *   RootNode (Xform)
                        *   Box072 (Xform)
                            *   Box072_06___Default_0 (Xform)
                                *   Box072_06___Default_0 (Mesh)
    *   BoxOnConveyor_40 (Xform)
        *   Materials (Scope)
            *   _6___Default (Material)
                *   pbr_shader (Shader)
                *   uvset0 (Shader)
                *   tex_base (Shader)
        *   Meshes (Xform)
            *   Sketchfab_model (Xform)
                *   f49ad5edc352496894d3a02181012422_fbx (Xform)
                    *   RootNode (Xform)
                        *   Box072 (Xform)
                            *   Box072_06___Default_0 (Xform)
                                *   Box072_06___Default_0 (Mesh)
    *   BoxOnConveyor_41 (Xform)
        *   Materials (Scope)
            *   _6___Default (Material)
                *   pbr_shader (Shader)
                *   uvset0 (Shader)
                *   tex_base (Shader)
        *   Meshes (Xform)
            *   Sketchfab_model (Xform)
                *   f49ad5edc352496894d3a02181012422_fbx (Xform)
                    *   RootNode (Xform)
                        *   Box072 (Xform)
                            *   Box072_06___Default_0 (Xform)
                                *   Box072_06___Default_0 (Mesh)
    *   BoxOnConveyor_42 (Xform)
        *   Materials (Scope)
            *   _6___Default (Material)
                *   pbr_shader (Shader)
                *   uvset0 (Shader)
                *   tex_base (Shader)
        *   Meshes (Xform)
            *   Sketchfab_model (Xform)
                *   f49ad5edc352496894d3a02181012422_fbx (Xform)
                    *   RootNode (Xform)
                        *   Box072 (Xform)
                            *   Box072_06___Default_0 (Xform)
                                *   Box072_06___Default_0 (Mesh)
    *   BoxOnConveyor_43 (Xform)
        *   Materials (Scope)
            *   _6___Default (Material)
                *   pbr_shader (Shader)
                *   uvset0 (Shader)
                *   tex_base (Shader)
        *   Meshes (Xform)
            *   Sketchfab_model (Xform)
                *   f49ad5edc352496894d3a02181012422_fbx (Xform)
                    *   RootNode (Xform)
                        *   Box072 (Xform)
                            *   Box072_06___Default_0 (Xform)
                                *   Box072_06___Default_0 (Mesh)
    *   BoxOnConveyor_44 (Xform)
        *   Materials (Scope)
            *   _6___Default (Material)
                *   pbr_shader (Shader)
                *   uvset0 (Shader)
                *   tex_base (Shader)
        *   Meshes (Xform)
            *   Sketchfab_model (Xform)
                *   f49ad5edc352496894d3a02181012422_fbx (Xform)
                    *   RootNode (Xform)
                        *   Box072 (Xform)
                            *   Box072_06___Default_0 (Xform)
                                *   Box072_06___Default_0 (Mesh)
    *   BoxOnConveyor_45 (Xform)
        *   Materials (Scope)
            *   _6___Default (Material)
                *   pbr_shader (Shader)
                *   uvset0 (Shader)
                *   tex_base (Shader)
        *   Meshes (Xform)
            *   Sketchfab_model (Xform)
                *   f49ad5edc352496894d3a02181012422_fbx (Xform)
                    *   RootNode (Xform)
                        *   Box072 (Xform)
                            *   Box072_06___Default_0 (Xform)
                                *   Box072_06___Default_0 (Mesh)
    *   BoxOnConveyor_46 (Xform)
        *   Materials (Scope)
            *   _6___Default (Material)
                *   pbr_shader (Shader)
                *   uvset0 (Shader)
                *   tex_base (Shader)
        *   Meshes (Xform)
            *   Sketchfab_model (Xform)
                *   f49ad5edc352496894d3a02181012422_fbx (Xform)
                    *   RootNode (Xform)
                        *   Box072 (Xform)
                            *   Box072_06___Default_0 (Xform)
                                *   Box072_06___Default_0 (Mesh)
    *   BoxOnConveyor_47 (Xform)
        *   Materials (Scope)
            *   _6___Default (Material)
                *   pbr_shader (Shader)
                *   uvset0 (Shader)
                *   tex_base (Shader)
        *   Meshes (Xform)
            *   Sketchfab_model (Xform)
                *   f49ad5edc352496894d3a02181012422_fbx (Xform)
                    *   RootNode (Xform)
                        *   Box072 (Xform)
                            *   Box072_06___Default_0 (Xform)
                                *   Box072_06___Default_0 (Mesh)
    *   BoxOnConveyor_48 (Xform)
        *   Materials (Scope)
            *   _6___Default (Material)
                *   pbr_shader (Shader)
                *   uvset0 (Shader)
                *   tex_base (Shader)
        *   Meshes (Xform)
            *   Sketchfab_model (Xform)
                *   f49ad5edc352496894d3a02181012422_fbx (Xform)
                    *   RootNode (Xform)
                        *   Box072 (Xform)
                            *   Box072_06___Default_0 (Xform)
                                *   Box072_06___Default_0 (Mesh)
    *   BoxOnConveyor_49 (Xform)
        *   Materials (Scope)
            *   _6___Default (Material)
                *   pbr_shader (Shader)
                *   uvset0 (Shader)
                *   tex_base (Shader)
        *   Meshes (Xform)
            *   Sketchfab_model (Xform)
                *   f49ad5edc352496894d3a02181012422_fbx (Xform)
                    *   RootNode (Xform)
                        *   Box072 (Xform)
                            *   Box072_06___Default_0 (Xform)
                                *   Box072_06___Default_0 (Mesh)
    *   BoxOnConveyor_50 (Xform)
        *   Materials (Scope)
            *   _6___Default (Material)
                *   pbr_shader (Shader)
                *   uvset0 (Shader)
                *   tex_base (Shader)
        *   Meshes (Xform)
            *   Sketchfab_model (Xform)
                *   f49ad5edc352496894d3a02181012422_fbx (Xform)
                    *   RootNode (Xform)
                        *   Box072 (Xform)
                            *   Box072_06___Default_0 (Xform)
                                *   Box072_06___Default_0 (Mesh)
    *   BoxOnConveyor_51 (Xform)
        *   Materials (Scope)
            *   _6___Default (Material)
                *   pbr_shader (Shader)
                *   uvset0 (Shader)
                *   tex_base (Shader)
        *   Meshes (Xform)
            *   Sketchfab_model (Xform)
                *   f49ad5edc352496894d3a02181012422_fbx (Xform)
                    *   RootNode (Xform)
                        *   Box072 (Xform)
                            *   Box072_06___Default_0 (Xform)
                                *   Box072_06___Default_0 (Mesh)
    *   BoxOnConveyor_52 (Xform)
        *   Materials (Scope)
            *   _6___Default (Material)
                *   pbr_shader (Shader)
                *   uvset0 (Shader)
                *   tex_base (Shader)
        *   Meshes (Xform)
            *   Sketchfab_model (Xform)
                *   f49ad5edc352496894d3a02181012422_fbx (Xform)
                    *   RootNode (Xform)
                        *   Box072 (Xform)
                            *   Box072_06___Default_0 (Xform)
                                *   Box072_06___Default_0 (Mesh)
    *   BoxOnConveyor_53 (Xform)
        *   Materials (Scope)
            *   _6___Default (Material)
                *   pbr_shader (Shader)
                *   uvset0 (Shader)
                *   tex_base (Shader)
        *   Meshes (Xform)
            *   Sketchfab_model (Xform)
                *   f49ad5edc352496894d3a02181012422_fbx (Xform)
                    *   RootNode (Xform)
                        *   Box072 (Xform)
                            *   Box072_06___Default_0 (Xform)
                                *   Box072_06___Default_0 (Mesh)
    *   BoxOnConveyor_54 (Xform)
        *   Materials (Scope)
            *   _6___Default (Material)
                *   pbr_shader (Shader)
                *   uvset0 (Shader)
                *   tex_base (Shader)
        *   Meshes (Xform)
            *   Sketchfab_model (Xform)
                *   f49ad5edc352496894d3a02181012422_fbx (Xform)
                    *   RootNode (Xform)
                        *   Box072 (Xform)
                            *   Box072_06___Default_0 (Xform)
                                *   Box072_06___Default_0 (Mesh)
    *   BoxOnConveyor_55 (Xform)
        *   Materials (Scope)
            *   _6___Default (Material)
                *   pbr_shader (Shader)
                *   uvset0 (Shader)
                *   tex_base (Shader)
        *   Meshes (Xform)
            *   Sketchfab_model (Xform)
                *   f49ad5edc352496894d3a02181012422_fbx (Xform)
                    *   RootNode (Xform)
                        *   Box072 (Xform)
                            *   Box072_06___Default_0 (Xform)
                                *   Box072_06___Default_0 (Mesh)
    *   BoxOnConveyor_56 (Xform)
        *   Materials (Scope)
            *   _6___Default (Material)
                *   pbr_shader (Shader)
                *   uvset0 (Shader)
                *   tex_base (Shader)
        *   Meshes (Xform)
            *   Sketchfab_model (Xform)
                *   f49ad5edc352496894d3a02181012422_fbx (Xform)
                    *   RootNode (Xform)
                        *   Box072 (Xform)
                            *   Box072_06___Default_0 (Xform)
                                *   Box072_06___Default_0 (Mesh)
    *   BoxOnConveyor_57 (Xform)
        *   Materials (Scope)
            *   _6___Default (Material)
                *   pbr_shader (Shader)
                *   uvset0 (Shader)
                *   tex_base (Shader)
        *   Meshes (Xform)
            *   Sketchfab_model (Xform)
                *   f49ad5edc352496894d3a02181012422_fbx (Xform)
                    *   RootNode (Xform)
                        *   Box072 (Xform)
                            *   Box072_06___Default_0 (Xform)
                                *   Box072_06___Default_0 (Mesh)
    *   BoxOnConveyor_58 (Xform)
        *   Materials (Scope)
            *   _6___Default (Material)
                *   pbr_shader (Shader)
                *   uvset0 (Shader)
                *   tex_base (Shader)
        *   Meshes (Xform)
            *   Sketchfab_model (Xform)
                *   f49ad5edc352496894d3a02181012422_fbx (Xform)
                    *   RootNode (Xform)
                        *   Box072 (Xform)
                            *   Box072_06___Default_0 (Xform)
                                *   Box072_06___Default_0 (Mesh)
    *   BoxOnConveyor_59 (Xform)
        *   Materials (Scope)
            *   _6___Default (Material)
                *   pbr_shader (Shader)
                *   uvset0 (Shader)
                *   tex_base (Shader)
        *   Meshes (Xform)
            *   Sketchfab_model (Xform)
                *   f49ad5edc352496894d3a02181012422_fbx (Xform)
                    *   RootNode (Xform)
                        *   Box072 (Xform)
                            *   Box072_06___Default_0 (Xform)
                                *   Box072_06___Default_0 (Mesh)
    *   BoxOnConveyor_60 (Xform)
        *   Materials (Scope)
            *   _6___Default (Material)
                *   pbr_shader (Shader)
                *   uvset0 (Shader)
                *   tex_base (Shader)
        *   Meshes (Xform)
            *   Sketchfab_model (Xform)
                *   f49ad5edc352496894d3a02181012422_fbx (Xform)
                    *   RootNode (Xform)
                        *   Box072 (Xform)
                            *   Box072_06___Default_0 (Xform)
                                *   Box072_06___Default_0 (Mesh)
    *   BoxOnConveyor_61 (Xform)
        *   Materials (Scope)
            *   _6___Default (Material)
                *   pbr_shader (Shader)
                *   uvset0 (Shader)
                *   tex_base (Shader)
        *   Meshes (Xform)
            *   Sketchfab_model (Xform)
                *   f49ad5edc352496894d3a02181012422_fbx (Xform)
                    *   RootNode (Xform)
                        *   Box072 (Xform)
                            *   Box072_06___Default_0 (Xform)
                                *   Box072_06___Default_0 (Mesh)
    *   BoxOnConveyor_62 (Xform)
        *   Materials (Scope)
            *   _6___Default (Material)
                *   pbr_shader (Shader)
                *   uvset0 (Shader)
                *   tex_base (Shader)
        *   Meshes (Xform)
            *   Sketchfab_model (Xform)
                *   f49ad5edc352496894d3a02181012422_fbx (Xform)
                    *   RootNode (Xform)
                        *   Box072 (Xform)
                            *   Box072_06___Default_0 (Xform)
                                *   Box072_06___Default_0 (Mesh)
    *   BoxOnConveyor_63 (Xform)
        *   Materials (Scope)
            *   _6___Default (Material)
                *   pbr_shader (Shader)
                *   uvset0 (Shader)
                *   tex_base (Shader)
        *   Meshes (Xform)
            *   Sketchfab_model (Xform)
                *   f49ad5edc352496894d3a02181012422_fbx (Xform)
                    *   RootNode (Xform)
                        *   Box072 (Xform)
                            *   Box072_06___Default_0 (Xform)
                                *   Box072_06___Default_0 (Mesh)
    *   BoxOnConveyor_64 (Xform)
        *   Materials (Scope)
            *   _6___Default (Material)
                *   pbr_shader (Shader)
                *   uvset0 (Shader)
                *   tex_base (Shader)
        *   Meshes (Xform)
            *   Sketchfab_model (Xform)
                *   f49ad5edc352496894d3a02181012422_fbx (Xform)
                    *   RootNode (Xform)
                        *   Box072 (Xform)
                            *   Box072_06___Default_0 (Xform)
                                *   Box072_06___Default_0 (Mesh)
    *   BoxOnConveyor_65 (Xform)
        *   Materials (Scope)
            *   _6___Default (Material)
                *   pbr_shader (Shader)
                *   uvset0 (Shader)
                *   tex_base (Shader)
        *   Meshes (Xform)
            *   Sketchfab_model (Xform)
                *   f49ad5edc352496894d3a02181012422_fbx (Xform)
                    *   RootNode (Xform)
                        *   Box072 (Xform)
                            *   Box072_06___Default_0 (Xform)
                                *   Box072_06___Default_0 (Mesh)
    *   BoxOnConveyor_66 (Xform)
        *   Materials (Scope)
            *   _6___Default (Material)
                *   pbr_shader (Shader)
                *   uvset0 (Shader)
                *   tex_base (Shader)
        *   Meshes (Xform)
            *   Sketchfab_model (Xform)
                *   f49ad5edc352496894d3a02181012422_fbx (Xform)
                    *   RootNode (Xform)
                        *   Box072 (Xform)
                            *   Box072_06___Default_0 (Xform)
                                *   Box072_06___Default_0 (Mesh)
    *   BoxOnConveyor_67 (Xform)
        *   Materials (Scope)
            *   _6___Default (Material)
                *   pbr_shader (Shader)
                *   uvset0 (Shader)
                *   tex_base (Shader)
        *   Meshes (Xform)
            *   Sketchfab_model (Xform)
                *   f49ad5edc352496894d3a02181012422_fbx (Xform)
                    *   RootNode (Xform)
                        *   Box072 (Xform)
                            *   Box072_06___Default_0 (Xform)
                                *   Box072_06___Default_0 (Mesh)
    *   BoxOnConveyor_68 (Xform)
        *   Materials (Scope)
            *   _6___Default (Material)
                *   pbr_shader (Shader)
                *   uvset0 (Shader)
                *   tex_base (Shader)
        *   Meshes (Xform)
            *   Sketchfab_model (Xform)
                *   f49ad5edc352496894d3a02181012422_fbx (Xform)
                    *   RootNode (Xform)
                        *   Box072 (Xform)
                            *   Box072_06___Default_0 (Xform)
                                *   Box072_06___Default_0 (Mesh)
    *   BoxOnConveyor_69 (Xform)
        *   Materials (Scope)
            *   _6___Default (Material)
                *   pbr_shader (Shader)
                *   uvset0 (Shader)
                *   tex_base (Shader)
        *   Meshes (Xform)
            *   Sketchfab_model (Xform)
                *   f49ad5edc352496894d3a02181012422_fbx (Xform)
                    *   RootNode (Xform)
                        *   Box072 (Xform)
                            *   Box072_06___Default_0 (Xform)
                                *   Box072_06___Default_0 (Mesh)
    *   BoxOnConveyor_70 (Xform)
        *   Materials (Scope)
            *   _6___Default (Material)
                *   pbr_shader (Shader)
                *   uvset0 (Shader)
                *   tex_base (Shader)
        *   Meshes (Xform)
            *   Sketchfab_model (Xform)
                *   f49ad5edc352496894d3a02181012422_fbx (Xform)
                    *   RootNode (Xform)
                        *   Box072 (Xform)
                            *   Box072_06___Default_0 (Xform)
                                *   Box072_06___Default_0 (Mesh)
    *   BoxOnConveyor_71 (Xform)
        *   Materials (Scope)
            *   _6___Default (Material)
                *   pbr_shader (Shader)
                *   uvset0 (Shader)
                *   tex_base (Shader)
        *   Meshes (Xform)
            *   Sketchfab_model (Xform)
                *   f49ad5edc352496894d3a02181012422_fbx (Xform)
                    *   RootNode (Xform)
                        *   Box072 (Xform)
                            *   Box072_06___Default_0 (Xform)
                                *   Box072_06___Default_0 (Mesh)
    *   BoxOnConveyor_72 (Xform)
        *   Materials (Scope)
            *   _6___Default (Material)
                *   pbr_shader (Shader)
                *   uvset0 (Shader)
                *   tex_base (Shader)
        *   Meshes (Xform)
            *   Sketchfab_model (Xform)
                *   f49ad5edc352496894d3a02181012422_fbx (Xform)
                    *   RootNode (Xform)
                        *   Box072 (Xform)
                            *   Box072_06___Default_0 (Xform)
                                *   Box072_06___Default_0 (Mesh)
    *   BoxOnConveyor_73 (Xform)
        *   Materials (Scope)
            *   _6___Default (Material)
                *   pbr_shader (Shader)
                *   uvset0 (Shader)
                *   tex_base (Shader)
        *   Meshes (Xform)
            *   Sketchfab_model (Xform)
                *   f49ad5edc352496894d3a02181012422_fbx (Xform)
                    *   RootNode (Xform)
                        *   Box072 (Xform)
                            *   Box072_06___Default_0 (Xform)
                                *   Box072_06___Default_0 (Mesh)
    *   BoxOnConveyor_74 (Xform)
        *   Materials (Scope)
            *   _6___Default (Material)
                *   pbr_shader (Shader)
                *   uvset0 (Shader)
                *   tex_base (Shader)
        *   Meshes (Xform)
            *   Sketchfab_model (Xform)
                *   f49ad5edc352496894d3a02181012422_fbx (Xform)
                    *   RootNode (Xform)
                        *   Box072 (Xform)
                            *   Box072_06___Default_0 (Xform)
                                *   Box072_06___Default_0 (Mesh)
    *   BoxOnConveyor_75 (Xform)
        *   Materials (Scope)
            *   _6___Default (Material)
                *   pbr_shader (Shader)
                *   uvset0 (Shader)
                *   tex_base (Shader)
        *   Meshes (Xform)
            *   Sketchfab_model (Xform)
                *   f49ad5edc352496894d3a02181012422_fbx (Xform)
                    *   RootNode (Xform)
                        *   Box072 (Xform)
                            *   Box072_06___Default_0 (Xform)
                                *   Box072_06___Default_0 (Mesh)
    *   BoxOnConveyor_76 (Xform)
        *   Materials (Scope)
            *   _6___Default (Material)
                *   pbr_shader (Shader)
                *   uvset0 (Shader)
                *   tex_base (Shader)
        *   Meshes (Xform)
            *   Sketchfab_model (Xform)
                *   f49ad5edc352496894d3a02181012422_fbx (Xform)
                    *   RootNode (Xform)
                        *   Box072 (Xform)
                            *   Box072_06___Default_0 (Xform)
                                *   Box072_06___Default_0 (Mesh)
    *   BoxOnConveyor_77 (Xform)
        *   Materials (Scope)
            *   _6___Default (Material)
                *   pbr_shader (Shader)
                *   uvset0 (Shader)
                *   tex_base (Shader)
        *   Meshes (Xform)
            *   Sketchfab_model (Xform)
                *   f49ad5edc352496894d3a02181012422_fbx (Xform)
                    *   RootNode (Xform)
                        *   Box072 (Xform)
                            *   Box072_06___Default_0 (Xform)
                                *   Box072_06___Default_0 (Mesh)
    *   BoxOnConveyor_78 (Xform)
        *   Materials (Scope)
            *   _6___Default (Material)
                *   pbr_shader (Shader)
                *   uvset0 (Shader)
                *   tex_base (Shader)
        *   Meshes (Xform)
            *   Sketchfab_model (Xform)
                *   f49ad5edc352496894d3a02181012422_fbx (Xform)
                    *   RootNode (Xform)
                        *   Box072 (Xform)
                            *   Box072_06___Default_0 (Xform)
                                *   Box072_06___Default_0 (Mesh)
    *   BoxOnConveyor_79 (Xform)
        *   Materials (Scope)
            *   _6___Default (Material)
                *   pbr_shader (Shader)
                *   uvset0 (Shader)
                *   tex_base (Shader)
        *   Meshes (Xform)
            *   Sketchfab_model (Xform)
                *   f49ad5edc352496894d3a02181012422_fbx (Xform)
                    *   RootNode (Xform)
                        *   Box072 (Xform)
                            *   Box072_06___Default_0 (Xform)
                                *   Box072_06___Default_0 (Mesh)
    *   BoxOnConveyor_80 (Xform)
        *   Materials (Scope)
            *   _6___Default (Material)
                *   pbr_shader (Shader)
                *   uvset0 (Shader)
                *   tex_base (Shader)
        *   Meshes (Xform)
            *   Sketchfab_model (Xform)
                *   f49ad5edc352496894d3a02181012422_fbx (Xform)
                    *   RootNode (Xform)
                        *   Box072 (Xform)
                            *   Box072_06___Default_0 (Xform)
                                *   Box072_06___Default_0 (Mesh)
    *   StackedCarton_1 (Xform)
        *   Materials (Scope)
            *   _6___Default (Material)
                *   pbr_shader (Shader)
                *   uvset0 (Shader)
                *   tex_base (Shader)
        *   Meshes (Xform)
            *   Sketchfab_model (Xform)
                *   f49ad5edc352496894d3a02181012422_fbx (Xform)
                    *   RootNode (Xform)
                        *   Box072 (Xform)
                            *   Box072_06___Default_0 (Xform)
                                *   Box072_06___Default_0 (Mesh)
    *   StackedCarton_2 (Xform)
        *   Materials (Scope)
            *   _6___Default (Material)
                *   pbr_shader (Shader)
                *   uvset0 (Shader)
                *   tex_base (Shader)
        *   Meshes (Xform)
            *   Sketchfab_model (Xform)
                *   f49ad5edc352496894d3a02181012422_fbx (Xform)
                    *   RootNode (Xform)
                        *   Box072 (Xform)
                            *   Box072_06___Default_0 (Xform)
                                *   Box072_06___Default_0 (Mesh)
    *   StackedCarton_3 (Xform)
        *   Materials (Scope)
            *   _6___Default (Material)
                *   pbr_shader (Shader)
                *   uvset0 (Shader)
                *   tex_base (Shader)
        *   Meshes (Xform)
            *   Sketchfab_model (Xform)
                *   f49ad5edc352496894d3a02181012422_fbx (Xform)
                    *   RootNode (Xform)
                        *   Box072 (Xform)
                            *   Box072_06___Default_0 (Xform)
                                *   Box072_06___Default_0 (Mesh)
    *   StackedCarton_4 (Xform)
        *   Materials (Scope)
            *   _6___Default (Material)
                *   pbr_shader (Shader)
                *   uvset0 (Shader)
                *   tex_base (Shader)
        *   Meshes (Xform)
            *   Sketchfab_model (Xform)
                *   f49ad5edc352496894d3a02181012422_fbx (Xform)
                    *   RootNode (Xform)
                        *   Box072 (Xform)
                            *   Box072_06___Default_0 (Xform)
                                *   Box072_06___Default_0 (Mesh)
    *   StackedCarton_5 (Xform)
        *   Materials (Scope)
            *   _6___Default (Material)
                *   pbr_shader (Shader)
                *   uvset0 (Shader)
                *   tex_base (Shader)
        *   Meshes (Xform)
            *   Sketchfab_model (Xform)
                *   f49ad5edc352496894d3a02181012422_fbx (Xform)
                    *   RootNode (Xform)
                        *   Box072 (Xform)
                            *   Box072_06___Default_0 (Xform)
                                *   Box072_06___Default_0 (Mesh)
    *   StackedCarton_6 (Xform)
        *   Materials (Scope)
            *   _6___Default (Material)
                *   pbr_shader (Shader)
                *   uvset0 (Shader)
                *   tex_base (Shader)
        *   Meshes (Xform)
            *   Sketchfab_model (Xform)
                *   f49ad5edc352496894d3a02181012422_fbx (Xform)
                    *   RootNode (Xform)
                        *   Box072 (Xform)
                            *   Box072_06___Default_0 (Xform)
                                *   Box072_06___Default_0 (Mesh)
    *   StackedCarton_7 (Xform)
        *   Materials (Scope)
            *   _6___Default (Material)
                *   pbr_shader (Shader)
                *   uvset0 (Shader)
                *   tex_base (Shader)
        *   Meshes (Xform)
            *   Sketchfab_model (Xform)
                *   f49ad5edc352496894d3a02181012422_fbx (Xform)
                    *   RootNode (Xform)
                        *   Box072 (Xform)
                            *   Box072_06___Default_0 (Xform)
                                *   Box072_06___Default_0 (Mesh)
    *   StackedCarton_8 (Xform)
        *   Materials (Scope)
            *   _6___Default (Material)
                *   pbr_shader (Shader)
                *   uvset0 (Shader)
                *   tex_base (Shader)
        *   Meshes (Xform)
            *   Sketchfab_model (Xform)
                *   f49ad5edc352496894d3a02181012422_fbx (Xform)
                    *   RootNode (Xform)
                        *   Box072 (Xform)
                            *   Box072_06___Default_0 (Xform)
                                *   Box072_06___Default_0 (Mesh)
    *   StackedCarton1_1 (Xform)
        *   Materials (Scope)
            *   _6___Default (Material)
                *   pbr_shader (Shader)
                *   uvset0 (Shader)
                *   tex_base (Shader)
        *   Meshes (Xform)
            *   Sketchfab_model (Xform)
                *   f49ad5edc352496894d3a02181012422_fbx (Xform)
                    *   RootNode (Xform)
                        *   Box072 (Xform)
                            *   Box072_06___Default_0 (Xform)
                                *   Box072_06___Default_0 (Mesh)
    *   StackedCarton1_2 (Xform)
        *   Materials (Scope)
            *   _6___Default (Material)
                *   pbr_shader (Shader)
                *   uvset0 (Shader)
                *   tex_base (Shader)
        *   Meshes (Xform)
            *   Sketchfab_model (Xform)
                *   f49ad5edc352496894d3a02181012422_fbx (Xform)
                    *   RootNode (Xform)
                        *   Box072 (Xform)
                            *   Box072_06___Default_0 (Xform)
                                *   Box072_06___Default_0 (Mesh)
    *   StackedCarton1_3 (Xform)
        *   Materials (Scope)
            *   _6___Default (Material)
                *   pbr_shader (Shader)
                *   uvset0 (Shader)
                *   tex_base (Shader)
        *   Meshes (Xform)
            *   Sketchfab_model (Xform)
                *   f49ad5edc352496894d3a02181012422_fbx (Xform)
                    *   RootNode (Xform)
                        *   Box072 (Xform)
                            *   Box072_06___Default_0 (Xform)
                                *   Box072_06___Default_0 (Mesh)
    *   StackedCarton1_4 (Xform)
        *   Materials (Scope)
            *   _6___Default (Material)
                *   pbr_shader (Shader)
                *   uvset0 (Shader)
                *   tex_base (Shader)
        *   Meshes (Xform)
            *   Sketchfab_model (Xform)
                *   f49ad5edc352496894d3a02181012422_fbx (Xform)
                    *   RootNode (Xform)
                        *   Box072 (Xform)
                            *   Box072_06___Default_0 (Xform)
                                *   Box072_06___Default_0 (Mesh)
    *   StackedCarton1_5 (Xform)
        *   Materials (Scope)
            *   _6___Default (Material)
                *   pbr_shader (Shader)
                *   uvset0 (Shader)
                *   tex_base (Shader)
        *   Meshes (Xform)
            *   Sketchfab_model (Xform)
                *   f49ad5edc352496894d3a02181012422_fbx (Xform)
                    *   RootNode (Xform)
                        *   Box072 (Xform)
                            *   Box072_06___Default_0 (Xform)
                                *   Box072_06___Default_0 (Mesh)
    *   StackedCarton1_6 (Xform)
        *   Materials (Scope)
            *   _6___Default (Material)
                *   pbr_shader (Shader)
                *   uvset0 (Shader)
                *   tex_base (Shader)
        *   Meshes (Xform)
            *   Sketchfab_model (Xform)
                *   f49ad5edc352496894d3a02181012422_fbx (Xform)
                    *   RootNode (Xform)
                        *   Box072 (Xform)
                            *   Box072_06___Default_0 (Xform)
                                *   Box072_06___Default_0 (Mesh)
    *   StackedCarton1_7 (Xform)
        *   Materials (Scope)
            *   _6___Default (Material)
                *   pbr_shader (Shader)
                *   uvset0 (Shader)
                *   tex_base (Shader)
        *   Meshes (Xform)
            *   Sketchfab_model (Xform)
                *   f49ad5edc352496894d3a02181012422_fbx (Xform)
                    *   RootNode (Xform)
                        *   Box072 (Xform)
                            *   Box072_06___Default_0 (Xform)
                                *   Box072_06___Default_0 (Mesh)
    *   StackedCarton1_8 (Xform)
        *   Materials (Scope)
            *   _6___Default (Material)
                *   pbr_shader (Shader)
                *   uvset0 (Shader)
                *   tex_base (Shader)
        *   Meshes (Xform)
            *   Sketchfab_model (Xform)
                *   f49ad5edc352496894d3a02181012422_fbx (Xform)
                    *   RootNode (Xform)
                        *   Box072 (Xform)
                            *   Box072_06___Default_0 (Xform)
                                *   Box072_06___Default_0 (Mesh)
    *   StackedCarton2_1 (Xform)
        *   Materials (Scope)
            *   _6___Default (Material)
                *   pbr_shader (Shader)
                *   uvset0 (Shader)
                *   tex_base (Shader)
        *   Meshes (Xform)
            *   Sketchfab_model (Xform)
                *   f49ad5edc352496894d3a02181012422_fbx (Xform)
                    *   RootNode (Xform)
                        *   Box072 (Xform)
                            *   Box072_06___Default_0 (Xform)
                                *   Box072_06___Default_0 (Mesh)
    *   StackedCarton2_2 (Xform)
        *   Materials (Scope)
            *   _6___Default (Material)
                *   pbr_shader (Shader)
                *   uvset0 (Shader)
                *   tex_base (Shader)
        *   Meshes (Xform)
            *   Sketchfab_model (Xform)
                *   f49ad5edc352496894d3a02181012422_fbx (Xform)
                    *   RootNode (Xform)
                        *   Box072 (Xform)
                            *   Box072_06___Default_0 (Xform)
                                *   Box072_06___Default_0 (Mesh)
    *   StackedCarton2_3 (Xform)
        *   Materials (Scope)
            *   _6___Default (Material)
                *   pbr_shader (Shader)
                *   uvset0 (Shader)
                *   tex_base (Shader)
        *   Meshes (Xform)
            *   Sketchfab_model (Xform)
                *   f49ad5edc352496894d3a02181012422_fbx (Xform)
                    *   RootNode (Xform)
                        *   Box072 (Xform)
                            *   Box072_06___Default_0 (Xform)
                                *   Box072_06___Default_0 (Mesh)
    *   StackedCarton2_4 (Xform)
        *   Materials (Scope)
            *   _6___Default (Material)
                *   pbr_shader (Shader)
                *   uvset0 (Shader)
                *   tex_base (Shader)
        *   Meshes (Xform)
            *   Sketchfab_model (Xform)
                *   f49ad5edc352496894d3a02181012422_fbx (Xform)
                    *   RootNode (Xform)
                        *   Box072 (Xform)
                            *   Box072_06___Default_0 (Xform)
                                *   Box072_06___Default_0 (Mesh)
    *   StackedCarton2_5 (Xform)
        *   Materials (Scope)
            *   _6___Default (Material)
                *   pbr_shader (Shader)
                *   uvset0 (Shader)
                *   tex_base (Shader)
        *   Meshes (Xform)
            *   Sketchfab_model (Xform)
                *   f49ad5edc352496894d3a02181012422_fbx (Xform)
                    *   RootNode (Xform)
                        *   Box072 (Xform)
                            *   Box072_06___Default_0 (Xform)
                                *   Box072_06___Default_0 (Mesh)
    *   StackedCarton2_6 (Xform)
        *   Materials (Scope)
            *   _6___Default (Material)
                *   pbr_shader (Shader)
                *   uvset0 (Shader)
                *   tex_base (Shader)
        *   Meshes (Xform)
            *   Sketchfab_model (Xform)
                *   f49ad5edc352496894d3a02181012422_fbx (Xform)
                    *   RootNode (Xform)
                        *   Box072 (Xform)
                            *   Box072_06___Default_0 (Xform)
                                *   Box072_06___Default_0 (Mesh)
    *   StackedCarton2_7 (Xform)
        *   Materials (Scope)
            *   _6___Default (Material)
                *   pbr_shader (Shader)
                *   uvset0 (Shader)
                *   tex_base (Shader)
        *   Meshes (Xform)
            *   Sketchfab_model (Xform)
                *   f49ad5edc352496894d3a02181012422_fbx (Xform)
                    *   RootNode (Xform)
                        *   Box072 (Xform)
                            *   Box072_06___Default_0 (Xform)
                                *   Box072_06___Default_0 (Mesh)
    *   StackedCarton2_8 (Xform)
        *   Materials (Scope)
            *   _6___Default (Material)
                *   pbr_shader (Shader)
                *   uvset0 (Shader)
                *   tex_base (Shader)
        *   Meshes (Xform)
            *   Sketchfab_model (Xform)
                *   f49ad5edc352496894d3a02181012422_fbx (Xform)
                    *   RootNode (Xform)
                        *   Box072 (Xform)
                            *   Box072_06___Default_0 (Xform)
                                *   Box072_06___Default_0 (Mesh)
    *   model_desk008 (Xform)
        *   materials (Scope)
            *   mat_0 (Material)
                *   PBRShader (Shader)
            *   mat_10782663 (Material)
                *   PBRShader (Shader)
            *   mat_10782673 (Material)
                *   PBRShader (Shader)
                *   stReader (Shader)
                *   transform_st (Shader)
                *   diffuseTexture (Shader)
            *   mat_10782839 (Material)
                *   PBRShader (Shader)
            *   mat_10782842 (Material)
                *   PBRShader (Shader)
        *   E_table_1 (Xform)
            *   E_leg_2 (Xform)
                *   P_fb8b1935d6745084 (Mesh)
            *   E_cabinet_3 (Xform)
                *   P_d903d9aeeb215084 (Mesh)
                *   P_644a7b35134a084 (Mesh)
            *   E_tabletop_4 (Xform)
                *   P_76c05a9963150084 (Mesh)
        *   E_drawer_5 (Xform)
            *   P_9b591a0a5294a084 (Mesh)
            *   P_b5fc1b49d1858784 (Mesh)
            *   PrismaticJoint_desk008_down (PhysicsPrismaticJoint)
        *   E_drawer_6 (Xform)
            *   P_c45acc40a35b2084 (Mesh)
            *   P_6dd5c29b55f96c84 (Mesh)
            *   PrismaticJoint_desk008_middle (PhysicsPrismaticJoint)
        *   E_drawer_7 (Xform)
            *   P_a37d90f1fd08a084 (Mesh)
            *   P_9b2777dbd9d2c084 (Mesh)
            *   PrismaticJoint_desk008_up (PhysicsPrismaticJoint)
        *   PhysicsMaterial (Material)
        *   PhysicsMaterial_01 (Material)
    *   INDUSTRIAL_ROBOTIC_ARM (Xform)
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
    *   model_desk008_01 (Prim)
    *   processed_Robotic_Manipulator_low_poly (Xform)
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
    *   INDUSTRIAL_ROBOTIC_ARM_01 (Prim)
    *   model_desk008_02 (Prim)
    *   model_desk008_03 (Prim)
    *   processed_Robotic_Manipulator_low_poly_01 (Prim)
    *   INDUSTRIAL_ROBOTIC_ARM_02 (Prim)
    *   model_desk008_04 (Prim)
    *   model_desk008_05 (Prim)
    *   processed_Robotic_Manipulator_low_poly_02 (Prim)
    *   INDUSTRIAL_ROBOTIC_ARM_03 (Prim)
    *   model_desk008_06 (Prim)
    *   model_desk008_07 (Prim)
    *   processed_Robotic_Manipulator_low_poly_03 (Prim)
    *   INDUSTRIAL_ROBOTIC_ARM_04 (Prim)
    *   model_desk008_08 (Prim)
    *   model_desk008_09 (Prim)
    *   processed_Robotic_Manipulator_low_poly_04 (Prim)
    *   INDUSTRIAL_ROBOTIC_ARM_05 (Prim)
    *   model_desk008_10 (Prim)
    *   model_desk008_11 (Prim)
    *   processed_Robotic_Manipulator_low_poly_05 (Prim)
    *   INDUSTRIAL_ROBOTIC_ARM_06 (Prim)
    *   model_desk008_12 (Prim)
    *   model_desk008_13 (Prim)
    *   processed_Robotic_Manipulator_low_poly_06 (Prim)
    *   INDUSTRIAL_ROBOTIC_ARM_07 (Prim)
    *   model_desk008_14 (Prim)
    *   model_desk008_15 (Prim)
    *   processed_Robotic_Manipulator_low_poly_07 (Prim)

## 3. 对象详细描述 (Detailed Prim Descriptions)

### /World/factory
*  **Prim路径 (Prim Path):**/World/factory
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '/media/simple/another_Documents/isaacsim_assets/scene/factory/factory.usdc'
*  **世界包围盒 (World BBox):**
   *   Size: '(49.139, 19.897, 67.754)'
   *   Center: '(0.761, 0.769, 9.470)'


---


### /World/agv_1
*  **Prim路径 (Prim Path):**/World/agv_1
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/5.0/Isaac/Robots/Idealworks/iwhub/iw_hub.usd'
*  **世界包围盒 (World BBox):**
   *   Size: '(1.431, 0.659, 0.231)'
   *   Center: '(-18.718, 29.251, 0.275)'


---


### /World/agv_1/chassis/Body
*  **Prim路径 (Prim Path):**/World/agv_1/chassis/Body
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'HighResProps/Body_v2.usd'
*  **世界包围盒 (World BBox):**
   *   Size: '(1.431, 0.652, 0.197)'
   *   Center: '(-18.718, 29.250, 0.289)'


---


### /World/agv_1/left_wheel/Left_Wheel
*  **Prim路径 (Prim Path):**/World/agv_1/left_wheel/Left_Wheel
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'HighResProps/Left_Wheel.usd'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.162, 0.057, 0.162)'
   *   Center: '(-18.400, 29.540, 0.240)'


---


### /World/agv_1/right_wheel/Right_Wheel
*  **Prim路径 (Prim Path):**/World/agv_1/right_wheel/Right_Wheel
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'HighResProps/Right_Wheel.usd'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.162, 0.057, 0.162)'
   *   Center: '(-18.400, 28.960, 0.240)'


---


### /World/agv_1/lift/Lift
*  **Prim路径 (Prim Path):**/World/agv_1/lift/Lift
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'HighResProps/Lift_v2.usd'
*  **世界包围盒 (World BBox):**
   *   Size: '(1.023, 0.659, 0.169)'
   *   Center: '(-18.656, 29.251, 0.306)'


---


### /World/agv_1/left_swivel/Left_Swivel
*  **Prim路径 (Prim Path):**/World/agv_1/left_swivel/Left_Swivel
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'HighResProps/Left_Swivel.usd'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.095, 0.033, 0.111)'
   *   Center: '(-19.077, 29.343, 0.263)'


---


### /World/agv_1/left_swivel/Left_Swivel/materials
*  **Prim路径 (Prim Path):**/World/agv_1/left_swivel/Left_Swivel/materials
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] './materials.usd'
*  **世界包围盒 (World BBox):**
   *   Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
   *   Center: '(0.000, 0.000, 0.000)'


---


### /World/agv_1/right_swivel/Right_Swivel
*  **Prim路径 (Prim Path):**/World/agv_1/right_swivel/Right_Swivel
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'HighResProps/Right_Swivel.usd'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.095, 0.033, 0.111)'
   *   Center: '(-19.077, 29.157, 0.263)'


---


### /World/agv_1/right_swivel/Right_Swivel/materials
*  **Prim路径 (Prim Path):**/World/agv_1/right_swivel/Right_Swivel/materials
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] './materials.usd'
*  **世界包围盒 (World BBox):**
   *   Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
   *   Center: '(0.000, 0.000, 0.000)'


---


### /World/agv_1/left_caster/Inner_Left_Wheel
*  **Prim路径 (Prim Path):**/World/agv_1/left_caster/Inner_Left_Wheel
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'HighResProps/Inner_Left_Wheel.usd'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.135, 0.029, 0.135)'
   *   Center: '(-19.077, 29.343, 0.230)'


---


### /World/agv_1/left_caster/Inner_Left_Wheel/materials
*  **Prim路径 (Prim Path):**/World/agv_1/left_caster/Inner_Left_Wheel/materials
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] './materials.usd'
*  **世界包围盒 (World BBox):**
   *   Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
   *   Center: '(0.000, 0.000, 0.000)'


---


### /World/agv_1/right_caster/Inner_Right_Wheel
*  **Prim路径 (Prim Path):**/World/agv_1/right_caster/Inner_Right_Wheel
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'HighResProps/Inner_Right_Wheel.usd'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.135, 0.029, 0.135)'
   *   Center: '(-19.077, 29.157, 0.230)'


---


### /World/agv_1/right_caster/Inner_Right_Wheel/materials
*  **Prim路径 (Prim Path):**/World/agv_1/right_caster/Inner_Right_Wheel/materials
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] './materials.usd'
*  **世界包围盒 (World BBox):**
   *   Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
   *   Center: '(0.000, 0.000, 0.000)'


---


### /World/agv_2
*  **Prim路径 (Prim Path):**/World/agv_2
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/5.0/Isaac/Robots/Idealworks/iwhub/iw_hub.usd'
*  **世界包围盒 (World BBox):**
   *   Size: '(1.431, 0.659, 0.231)'
   *   Center: '(-13.718, 29.251, 0.275)'


---


### /World/agv_2/chassis/Body
*  **Prim路径 (Prim Path):**/World/agv_2/chassis/Body
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'HighResProps/Body_v2.usd'
*  **世界包围盒 (World BBox):**
   *   Size: '(1.431, 0.652, 0.197)'
   *   Center: '(-13.718, 29.250, 0.289)'


---


### /World/agv_2/left_wheel/Left_Wheel
*  **Prim路径 (Prim Path):**/World/agv_2/left_wheel/Left_Wheel
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'HighResProps/Left_Wheel.usd'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.162, 0.057, 0.162)'
   *   Center: '(-13.400, 29.540, 0.240)'


---


### /World/agv_2/right_wheel/Right_Wheel
*  **Prim路径 (Prim Path):**/World/agv_2/right_wheel/Right_Wheel
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'HighResProps/Right_Wheel.usd'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.162, 0.057, 0.162)'
   *   Center: '(-13.400, 28.960, 0.240)'


---


### /World/agv_2/lift/Lift
*  **Prim路径 (Prim Path):**/World/agv_2/lift/Lift
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'HighResProps/Lift_v2.usd'
*  **世界包围盒 (World BBox):**
   *   Size: '(1.023, 0.659, 0.169)'
   *   Center: '(-13.656, 29.251, 0.306)'


---


### /World/agv_2/left_swivel/Left_Swivel
*  **Prim路径 (Prim Path):**/World/agv_2/left_swivel/Left_Swivel
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'HighResProps/Left_Swivel.usd'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.095, 0.033, 0.111)'
   *   Center: '(-14.077, 29.343, 0.263)'


---


### /World/agv_2/left_swivel/Left_Swivel/materials
*  **Prim路径 (Prim Path):**/World/agv_2/left_swivel/Left_Swivel/materials
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] './materials.usd'
*  **世界包围盒 (World BBox):**
   *   Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
   *   Center: '(0.000, 0.000, 0.000)'


---


### /World/agv_2/right_swivel/Right_Swivel
*  **Prim路径 (Prim Path):**/World/agv_2/right_swivel/Right_Swivel
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'HighResProps/Right_Swivel.usd'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.095, 0.033, 0.111)'
   *   Center: '(-14.077, 29.157, 0.263)'


---


### /World/agv_2/right_swivel/Right_Swivel/materials
*  **Prim路径 (Prim Path):**/World/agv_2/right_swivel/Right_Swivel/materials
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] './materials.usd'
*  **世界包围盒 (World BBox):**
   *   Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
   *   Center: '(0.000, 0.000, 0.000)'


---


### /World/agv_2/left_caster/Inner_Left_Wheel
*  **Prim路径 (Prim Path):**/World/agv_2/left_caster/Inner_Left_Wheel
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'HighResProps/Inner_Left_Wheel.usd'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.135, 0.029, 0.135)'
   *   Center: '(-14.077, 29.343, 0.230)'


---


### /World/agv_2/left_caster/Inner_Left_Wheel/materials
*  **Prim路径 (Prim Path):**/World/agv_2/left_caster/Inner_Left_Wheel/materials
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] './materials.usd'
*  **世界包围盒 (World BBox):**
   *   Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
   *   Center: '(0.000, 0.000, 0.000)'


---


### /World/agv_2/right_caster/Inner_Right_Wheel
*  **Prim路径 (Prim Path):**/World/agv_2/right_caster/Inner_Right_Wheel
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'HighResProps/Inner_Right_Wheel.usd'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.135, 0.029, 0.135)'
   *   Center: '(-14.077, 29.157, 0.230)'


---


### /World/agv_2/right_caster/Inner_Right_Wheel/materials
*  **Prim路径 (Prim Path):**/World/agv_2/right_caster/Inner_Right_Wheel/materials
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] './materials.usd'
*  **世界包围盒 (World BBox):**
   *   Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
   *   Center: '(0.000, 0.000, 0.000)'


---


### /World/agv_3
*  **Prim路径 (Prim Path):**/World/agv_3
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/5.0/Isaac/Robots/Idealworks/iwhub/iw_hub.usd'
*  **世界包围盒 (World BBox):**
   *   Size: '(1.431, 0.659, 0.231)'
   *   Center: '(-8.718, 29.251, 0.275)'


---


### /World/agv_3/chassis/Body
*  **Prim路径 (Prim Path):**/World/agv_3/chassis/Body
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'HighResProps/Body_v2.usd'
*  **世界包围盒 (World BBox):**
   *   Size: '(1.431, 0.652, 0.197)'
   *   Center: '(-8.718, 29.250, 0.289)'


---


### /World/agv_3/left_wheel/Left_Wheel
*  **Prim路径 (Prim Path):**/World/agv_3/left_wheel/Left_Wheel
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'HighResProps/Left_Wheel.usd'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.162, 0.057, 0.162)'
   *   Center: '(-8.400, 29.540, 0.240)'


---


### /World/agv_3/right_wheel/Right_Wheel
*  **Prim路径 (Prim Path):**/World/agv_3/right_wheel/Right_Wheel
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'HighResProps/Right_Wheel.usd'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.162, 0.057, 0.162)'
   *   Center: '(-8.400, 28.960, 0.240)'


---


### /World/agv_3/lift/Lift
*  **Prim路径 (Prim Path):**/World/agv_3/lift/Lift
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'HighResProps/Lift_v2.usd'
*  **世界包围盒 (World BBox):**
   *   Size: '(1.023, 0.659, 0.169)'
   *   Center: '(-8.656, 29.251, 0.306)'


---


### /World/agv_3/left_swivel/Left_Swivel
*  **Prim路径 (Prim Path):**/World/agv_3/left_swivel/Left_Swivel
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'HighResProps/Left_Swivel.usd'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.095, 0.033, 0.111)'
   *   Center: '(-9.077, 29.343, 0.263)'


---


### /World/agv_3/left_swivel/Left_Swivel/materials
*  **Prim路径 (Prim Path):**/World/agv_3/left_swivel/Left_Swivel/materials
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] './materials.usd'
*  **世界包围盒 (World BBox):**
   *   Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
   *   Center: '(0.000, 0.000, 0.000)'


---


### /World/agv_3/right_swivel/Right_Swivel
*  **Prim路径 (Prim Path):**/World/agv_3/right_swivel/Right_Swivel
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'HighResProps/Right_Swivel.usd'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.095, 0.033, 0.111)'
   *   Center: '(-9.077, 29.157, 0.263)'


---


### /World/agv_3/right_swivel/Right_Swivel/materials
*  **Prim路径 (Prim Path):**/World/agv_3/right_swivel/Right_Swivel/materials
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] './materials.usd'
*  **世界包围盒 (World BBox):**
   *   Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
   *   Center: '(0.000, 0.000, 0.000)'


---


### /World/agv_3/left_caster/Inner_Left_Wheel
*  **Prim路径 (Prim Path):**/World/agv_3/left_caster/Inner_Left_Wheel
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'HighResProps/Inner_Left_Wheel.usd'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.135, 0.029, 0.135)'
   *   Center: '(-9.077, 29.343, 0.230)'


---


### /World/agv_3/left_caster/Inner_Left_Wheel/materials
*  **Prim路径 (Prim Path):**/World/agv_3/left_caster/Inner_Left_Wheel/materials
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] './materials.usd'
*  **世界包围盒 (World BBox):**
   *   Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
   *   Center: '(0.000, 0.000, 0.000)'


---


### /World/agv_3/right_caster/Inner_Right_Wheel
*  **Prim路径 (Prim Path):**/World/agv_3/right_caster/Inner_Right_Wheel
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'HighResProps/Inner_Right_Wheel.usd'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.135, 0.029, 0.135)'
   *   Center: '(-9.077, 29.157, 0.230)'


---


### /World/agv_3/right_caster/Inner_Right_Wheel/materials
*  **Prim路径 (Prim Path):**/World/agv_3/right_caster/Inner_Right_Wheel/materials
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] './materials.usd'
*  **世界包围盒 (World BBox):**
   *   Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
   *   Center: '(0.000, 0.000, 0.000)'


---


### /World/agv_4
*  **Prim路径 (Prim Path):**/World/agv_4
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/5.0/Isaac/Robots/Idealworks/iwhub/iw_hub.usd'
*  **世界包围盒 (World BBox):**
   *   Size: '(1.431, 0.659, 0.231)'
   *   Center: '(-3.718, 29.251, 0.275)'


---


### /World/agv_4/chassis/Body
*  **Prim路径 (Prim Path):**/World/agv_4/chassis/Body
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'HighResProps/Body_v2.usd'
*  **世界包围盒 (World BBox):**
   *   Size: '(1.431, 0.652, 0.197)'
   *   Center: '(-3.718, 29.250, 0.289)'


---


### /World/agv_4/left_wheel/Left_Wheel
*  **Prim路径 (Prim Path):**/World/agv_4/left_wheel/Left_Wheel
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'HighResProps/Left_Wheel.usd'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.162, 0.057, 0.162)'
   *   Center: '(-3.400, 29.540, 0.240)'


---


### /World/agv_4/right_wheel/Right_Wheel
*  **Prim路径 (Prim Path):**/World/agv_4/right_wheel/Right_Wheel
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'HighResProps/Right_Wheel.usd'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.162, 0.057, 0.162)'
   *   Center: '(-3.400, 28.960, 0.240)'


---


### /World/agv_4/lift/Lift
*  **Prim路径 (Prim Path):**/World/agv_4/lift/Lift
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'HighResProps/Lift_v2.usd'
*  **世界包围盒 (World BBox):**
   *   Size: '(1.023, 0.659, 0.169)'
   *   Center: '(-3.656, 29.251, 0.306)'


---


### /World/agv_4/left_swivel/Left_Swivel
*  **Prim路径 (Prim Path):**/World/agv_4/left_swivel/Left_Swivel
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'HighResProps/Left_Swivel.usd'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.095, 0.033, 0.111)'
   *   Center: '(-4.077, 29.343, 0.263)'


---


### /World/agv_4/left_swivel/Left_Swivel/materials
*  **Prim路径 (Prim Path):**/World/agv_4/left_swivel/Left_Swivel/materials
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] './materials.usd'
*  **世界包围盒 (World BBox):**
   *   Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
   *   Center: '(0.000, 0.000, 0.000)'


---


### /World/agv_4/right_swivel/Right_Swivel
*  **Prim路径 (Prim Path):**/World/agv_4/right_swivel/Right_Swivel
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'HighResProps/Right_Swivel.usd'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.095, 0.033, 0.111)'
   *   Center: '(-4.077, 29.157, 0.263)'


---


### /World/agv_4/right_swivel/Right_Swivel/materials
*  **Prim路径 (Prim Path):**/World/agv_4/right_swivel/Right_Swivel/materials
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] './materials.usd'
*  **世界包围盒 (World BBox):**
   *   Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
   *   Center: '(0.000, 0.000, 0.000)'


---


### /World/agv_4/left_caster/Inner_Left_Wheel
*  **Prim路径 (Prim Path):**/World/agv_4/left_caster/Inner_Left_Wheel
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'HighResProps/Inner_Left_Wheel.usd'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.135, 0.029, 0.135)'
   *   Center: '(-4.077, 29.343, 0.230)'


---


### /World/agv_4/left_caster/Inner_Left_Wheel/materials
*  **Prim路径 (Prim Path):**/World/agv_4/left_caster/Inner_Left_Wheel/materials
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] './materials.usd'
*  **世界包围盒 (World BBox):**
   *   Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
   *   Center: '(0.000, 0.000, 0.000)'


---


### /World/agv_4/right_caster/Inner_Right_Wheel
*  **Prim路径 (Prim Path):**/World/agv_4/right_caster/Inner_Right_Wheel
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'HighResProps/Inner_Right_Wheel.usd'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.135, 0.029, 0.135)'
   *   Center: '(-4.077, 29.157, 0.230)'


---


### /World/agv_4/right_caster/Inner_Right_Wheel/materials
*  **Prim路径 (Prim Path):**/World/agv_4/right_caster/Inner_Right_Wheel/materials
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] './materials.usd'
*  **世界包围盒 (World BBox):**
   *   Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
   *   Center: '(0.000, 0.000, 0.000)'


---


### /World/agv_5
*  **Prim路径 (Prim Path):**/World/agv_5
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/5.0/Isaac/Robots/Idealworks/iwhub/iw_hub.usd'
*  **世界包围盒 (World BBox):**
   *   Size: '(1.431, 0.659, 0.231)'
   *   Center: '(1.282, 29.251, 0.275)'


---


### /World/agv_5/chassis/Body
*  **Prim路径 (Prim Path):**/World/agv_5/chassis/Body
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'HighResProps/Body_v2.usd'
*  **世界包围盒 (World BBox):**
   *   Size: '(1.431, 0.652, 0.197)'
   *   Center: '(1.282, 29.250, 0.289)'


---


### /World/agv_5/left_wheel/Left_Wheel
*  **Prim路径 (Prim Path):**/World/agv_5/left_wheel/Left_Wheel
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'HighResProps/Left_Wheel.usd'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.162, 0.057, 0.162)'
   *   Center: '(1.600, 29.540, 0.240)'


---


### /World/agv_5/right_wheel/Right_Wheel
*  **Prim路径 (Prim Path):**/World/agv_5/right_wheel/Right_Wheel
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'HighResProps/Right_Wheel.usd'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.162, 0.057, 0.162)'
   *   Center: '(1.600, 28.960, 0.240)'


---


### /World/agv_5/lift/Lift
*  **Prim路径 (Prim Path):**/World/agv_5/lift/Lift
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'HighResProps/Lift_v2.usd'
*  **世界包围盒 (World BBox):**
   *   Size: '(1.023, 0.659, 0.169)'
   *   Center: '(1.344, 29.251, 0.306)'


---


### /World/agv_5/left_swivel/Left_Swivel
*  **Prim路径 (Prim Path):**/World/agv_5/left_swivel/Left_Swivel
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'HighResProps/Left_Swivel.usd'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.095, 0.033, 0.111)'
   *   Center: '(0.923, 29.343, 0.263)'


---


### /World/agv_5/left_swivel/Left_Swivel/materials
*  **Prim路径 (Prim Path):**/World/agv_5/left_swivel/Left_Swivel/materials
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] './materials.usd'
*  **世界包围盒 (World BBox):**
   *   Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
   *   Center: '(0.000, 0.000, 0.000)'


---


### /World/agv_5/right_swivel/Right_Swivel
*  **Prim路径 (Prim Path):**/World/agv_5/right_swivel/Right_Swivel
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'HighResProps/Right_Swivel.usd'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.095, 0.033, 0.111)'
   *   Center: '(0.923, 29.157, 0.263)'


---


### /World/agv_5/right_swivel/Right_Swivel/materials
*  **Prim路径 (Prim Path):**/World/agv_5/right_swivel/Right_Swivel/materials
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] './materials.usd'
*  **世界包围盒 (World BBox):**
   *   Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
   *   Center: '(0.000, 0.000, 0.000)'


---


### /World/agv_5/left_caster/Inner_Left_Wheel
*  **Prim路径 (Prim Path):**/World/agv_5/left_caster/Inner_Left_Wheel
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'HighResProps/Inner_Left_Wheel.usd'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.135, 0.029, 0.135)'
   *   Center: '(0.923, 29.343, 0.230)'


---


### /World/agv_5/left_caster/Inner_Left_Wheel/materials
*  **Prim路径 (Prim Path):**/World/agv_5/left_caster/Inner_Left_Wheel/materials
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] './materials.usd'
*  **世界包围盒 (World BBox):**
   *   Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
   *   Center: '(0.000, 0.000, 0.000)'


---


### /World/agv_5/right_caster/Inner_Right_Wheel
*  **Prim路径 (Prim Path):**/World/agv_5/right_caster/Inner_Right_Wheel
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'HighResProps/Inner_Right_Wheel.usd'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.135, 0.029, 0.135)'
   *   Center: '(0.923, 29.157, 0.230)'


---


### /World/agv_5/right_caster/Inner_Right_Wheel/materials
*  **Prim路径 (Prim Path):**/World/agv_5/right_caster/Inner_Right_Wheel/materials
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] './materials.usd'
*  **世界包围盒 (World BBox):**
   *   Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
   *   Center: '(0.000, 0.000, 0.000)'


---


### /World/agv_6
*  **Prim路径 (Prim Path):**/World/agv_6
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/5.0/Isaac/Robots/Idealworks/iwhub/iw_hub.usd'
*  **世界包围盒 (World BBox):**
   *   Size: '(1.431, 0.659, 0.231)'
   *   Center: '(6.282, 29.251, 0.275)'


---


### /World/agv_6/chassis/Body
*  **Prim路径 (Prim Path):**/World/agv_6/chassis/Body
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'HighResProps/Body_v2.usd'
*  **世界包围盒 (World BBox):**
   *   Size: '(1.431, 0.652, 0.197)'
   *   Center: '(6.282, 29.250, 0.289)'


---


### /World/agv_6/left_wheel/Left_Wheel
*  **Prim路径 (Prim Path):**/World/agv_6/left_wheel/Left_Wheel
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'HighResProps/Left_Wheel.usd'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.162, 0.057, 0.162)'
   *   Center: '(6.600, 29.540, 0.240)'


---


### /World/agv_6/right_wheel/Right_Wheel
*  **Prim路径 (Prim Path):**/World/agv_6/right_wheel/Right_Wheel
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'HighResProps/Right_Wheel.usd'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.162, 0.057, 0.162)'
   *   Center: '(6.600, 28.960, 0.240)'


---


### /World/agv_6/lift/Lift
*  **Prim路径 (Prim Path):**/World/agv_6/lift/Lift
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'HighResProps/Lift_v2.usd'
*  **世界包围盒 (World BBox):**
   *   Size: '(1.023, 0.659, 0.169)'
   *   Center: '(6.344, 29.251, 0.306)'


---


### /World/agv_6/left_swivel/Left_Swivel
*  **Prim路径 (Prim Path):**/World/agv_6/left_swivel/Left_Swivel
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'HighResProps/Left_Swivel.usd'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.095, 0.033, 0.111)'
   *   Center: '(5.923, 29.343, 0.263)'


---


### /World/agv_6/left_swivel/Left_Swivel/materials
*  **Prim路径 (Prim Path):**/World/agv_6/left_swivel/Left_Swivel/materials
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] './materials.usd'
*  **世界包围盒 (World BBox):**
   *   Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
   *   Center: '(0.000, 0.000, 0.000)'


---


### /World/agv_6/right_swivel/Right_Swivel
*  **Prim路径 (Prim Path):**/World/agv_6/right_swivel/Right_Swivel
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'HighResProps/Right_Swivel.usd'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.095, 0.033, 0.111)'
   *   Center: '(5.923, 29.157, 0.263)'


---


### /World/agv_6/right_swivel/Right_Swivel/materials
*  **Prim路径 (Prim Path):**/World/agv_6/right_swivel/Right_Swivel/materials
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] './materials.usd'
*  **世界包围盒 (World BBox):**
   *   Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
   *   Center: '(0.000, 0.000, 0.000)'


---


### /World/agv_6/left_caster/Inner_Left_Wheel
*  **Prim路径 (Prim Path):**/World/agv_6/left_caster/Inner_Left_Wheel
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'HighResProps/Inner_Left_Wheel.usd'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.135, 0.029, 0.135)'
   *   Center: '(5.923, 29.343, 0.230)'


---


### /World/agv_6/left_caster/Inner_Left_Wheel/materials
*  **Prim路径 (Prim Path):**/World/agv_6/left_caster/Inner_Left_Wheel/materials
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] './materials.usd'
*  **世界包围盒 (World BBox):**
   *   Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
   *   Center: '(0.000, 0.000, 0.000)'


---


### /World/agv_6/right_caster/Inner_Right_Wheel
*  **Prim路径 (Prim Path):**/World/agv_6/right_caster/Inner_Right_Wheel
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'HighResProps/Inner_Right_Wheel.usd'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.135, 0.029, 0.135)'
   *   Center: '(5.923, 29.157, 0.230)'


---


### /World/agv_6/right_caster/Inner_Right_Wheel/materials
*  **Prim路径 (Prim Path):**/World/agv_6/right_caster/Inner_Right_Wheel/materials
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] './materials.usd'
*  **世界包围盒 (World BBox):**
   *   Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
   *   Center: '(0.000, 0.000, 0.000)'


---


### /World/agv_7
*  **Prim路径 (Prim Path):**/World/agv_7
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/5.0/Isaac/Robots/Idealworks/iwhub/iw_hub.usd'
*  **世界包围盒 (World BBox):**
   *   Size: '(1.431, 0.659, 0.231)'
   *   Center: '(11.282, 29.251, 0.275)'


---


### /World/agv_7/chassis/Body
*  **Prim路径 (Prim Path):**/World/agv_7/chassis/Body
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'HighResProps/Body_v2.usd'
*  **世界包围盒 (World BBox):**
   *   Size: '(1.431, 0.652, 0.197)'
   *   Center: '(11.282, 29.250, 0.289)'


---


### /World/agv_7/left_wheel/Left_Wheel
*  **Prim路径 (Prim Path):**/World/agv_7/left_wheel/Left_Wheel
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'HighResProps/Left_Wheel.usd'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.162, 0.057, 0.162)'
   *   Center: '(11.600, 29.540, 0.240)'


---


### /World/agv_7/right_wheel/Right_Wheel
*  **Prim路径 (Prim Path):**/World/agv_7/right_wheel/Right_Wheel
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'HighResProps/Right_Wheel.usd'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.162, 0.057, 0.162)'
   *   Center: '(11.600, 28.960, 0.240)'


---


### /World/agv_7/lift/Lift
*  **Prim路径 (Prim Path):**/World/agv_7/lift/Lift
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'HighResProps/Lift_v2.usd'
*  **世界包围盒 (World BBox):**
   *   Size: '(1.023, 0.659, 0.169)'
   *   Center: '(11.344, 29.251, 0.306)'


---


### /World/agv_7/left_swivel/Left_Swivel
*  **Prim路径 (Prim Path):**/World/agv_7/left_swivel/Left_Swivel
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'HighResProps/Left_Swivel.usd'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.095, 0.033, 0.111)'
   *   Center: '(10.923, 29.343, 0.263)'


---


### /World/agv_7/left_swivel/Left_Swivel/materials
*  **Prim路径 (Prim Path):**/World/agv_7/left_swivel/Left_Swivel/materials
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] './materials.usd'
*  **世界包围盒 (World BBox):**
   *   Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
   *   Center: '(0.000, 0.000, 0.000)'


---


### /World/agv_7/right_swivel/Right_Swivel
*  **Prim路径 (Prim Path):**/World/agv_7/right_swivel/Right_Swivel
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'HighResProps/Right_Swivel.usd'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.095, 0.033, 0.111)'
   *   Center: '(10.923, 29.157, 0.263)'


---


### /World/agv_7/right_swivel/Right_Swivel/materials
*  **Prim路径 (Prim Path):**/World/agv_7/right_swivel/Right_Swivel/materials
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] './materials.usd'
*  **世界包围盒 (World BBox):**
   *   Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
   *   Center: '(0.000, 0.000, 0.000)'


---


### /World/agv_7/left_caster/Inner_Left_Wheel
*  **Prim路径 (Prim Path):**/World/agv_7/left_caster/Inner_Left_Wheel
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'HighResProps/Inner_Left_Wheel.usd'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.135, 0.029, 0.135)'
   *   Center: '(10.923, 29.343, 0.230)'


---


### /World/agv_7/left_caster/Inner_Left_Wheel/materials
*  **Prim路径 (Prim Path):**/World/agv_7/left_caster/Inner_Left_Wheel/materials
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] './materials.usd'
*  **世界包围盒 (World BBox):**
   *   Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
   *   Center: '(0.000, 0.000, 0.000)'


---


### /World/agv_7/right_caster/Inner_Right_Wheel
*  **Prim路径 (Prim Path):**/World/agv_7/right_caster/Inner_Right_Wheel
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'HighResProps/Inner_Right_Wheel.usd'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.135, 0.029, 0.135)'
   *   Center: '(10.923, 29.157, 0.230)'


---


### /World/agv_7/right_caster/Inner_Right_Wheel/materials
*  **Prim路径 (Prim Path):**/World/agv_7/right_caster/Inner_Right_Wheel/materials
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] './materials.usd'
*  **世界包围盒 (World BBox):**
   *   Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
   *   Center: '(0.000, 0.000, 0.000)'


---


### /World/agv_8
*  **Prim路径 (Prim Path):**/World/agv_8
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/5.0/Isaac/Robots/Idealworks/iwhub/iw_hub.usd'
*  **世界包围盒 (World BBox):**
   *   Size: '(1.431, 0.659, 0.231)'
   *   Center: '(16.282, 29.251, 0.275)'


---


### /World/agv_8/chassis/Body
*  **Prim路径 (Prim Path):**/World/agv_8/chassis/Body
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'HighResProps/Body_v2.usd'
*  **世界包围盒 (World BBox):**
   *   Size: '(1.431, 0.652, 0.197)'
   *   Center: '(16.282, 29.250, 0.289)'


---


### /World/agv_8/left_wheel/Left_Wheel
*  **Prim路径 (Prim Path):**/World/agv_8/left_wheel/Left_Wheel
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'HighResProps/Left_Wheel.usd'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.162, 0.057, 0.162)'
   *   Center: '(16.600, 29.540, 0.240)'


---


### /World/agv_8/right_wheel/Right_Wheel
*  **Prim路径 (Prim Path):**/World/agv_8/right_wheel/Right_Wheel
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'HighResProps/Right_Wheel.usd'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.162, 0.057, 0.162)'
   *   Center: '(16.600, 28.960, 0.240)'


---


### /World/agv_8/lift/Lift
*  **Prim路径 (Prim Path):**/World/agv_8/lift/Lift
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'HighResProps/Lift_v2.usd'
*  **世界包围盒 (World BBox):**
   *   Size: '(1.023, 0.659, 0.169)'
   *   Center: '(16.344, 29.251, 0.306)'


---


### /World/agv_8/left_swivel/Left_Swivel
*  **Prim路径 (Prim Path):**/World/agv_8/left_swivel/Left_Swivel
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'HighResProps/Left_Swivel.usd'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.095, 0.033, 0.111)'
   *   Center: '(15.923, 29.343, 0.263)'


---


### /World/agv_8/left_swivel/Left_Swivel/materials
*  **Prim路径 (Prim Path):**/World/agv_8/left_swivel/Left_Swivel/materials
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] './materials.usd'
*  **世界包围盒 (World BBox):**
   *   Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
   *   Center: '(0.000, 0.000, 0.000)'


---


### /World/agv_8/right_swivel/Right_Swivel
*  **Prim路径 (Prim Path):**/World/agv_8/right_swivel/Right_Swivel
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'HighResProps/Right_Swivel.usd'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.095, 0.033, 0.111)'
   *   Center: '(15.923, 29.157, 0.263)'


---


### /World/agv_8/right_swivel/Right_Swivel/materials
*  **Prim路径 (Prim Path):**/World/agv_8/right_swivel/Right_Swivel/materials
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] './materials.usd'
*  **世界包围盒 (World BBox):**
   *   Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
   *   Center: '(0.000, 0.000, 0.000)'


---


### /World/agv_8/left_caster/Inner_Left_Wheel
*  **Prim路径 (Prim Path):**/World/agv_8/left_caster/Inner_Left_Wheel
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'HighResProps/Inner_Left_Wheel.usd'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.135, 0.029, 0.135)'
   *   Center: '(15.923, 29.343, 0.230)'


---


### /World/agv_8/left_caster/Inner_Left_Wheel/materials
*  **Prim路径 (Prim Path):**/World/agv_8/left_caster/Inner_Left_Wheel/materials
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] './materials.usd'
*  **世界包围盒 (World BBox):**
   *   Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
   *   Center: '(0.000, 0.000, 0.000)'


---


### /World/agv_8/right_caster/Inner_Right_Wheel
*  **Prim路径 (Prim Path):**/World/agv_8/right_caster/Inner_Right_Wheel
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'HighResProps/Inner_Right_Wheel.usd'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.135, 0.029, 0.135)'
   *   Center: '(15.923, 29.157, 0.230)'


---


### /World/agv_8/right_caster/Inner_Right_Wheel/materials
*  **Prim路径 (Prim Path):**/World/agv_8/right_caster/Inner_Right_Wheel/materials
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] './materials.usd'
*  **世界包围盒 (World BBox):**
   *   Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
   *   Center: '(0.000, 0.000, 0.000)'


---


### /World/Conveyor_1
*  **Prim路径 (Prim Path):**/World/Conveyor_1
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '/media/simple/another_Documents/isaacsim_assets/assets/Conveyor_Belt/Conveyor_Belt.usdc'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.799, 4.204, 9.846)'
   *   Center: '(-18.717, 23.877, 0.611)'


---


### /World/Conveyor_2
*  **Prim路径 (Prim Path):**/World/Conveyor_2
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '/media/simple/another_Documents/isaacsim_assets/assets/Conveyor_Belt/Conveyor_Belt.usdc'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.799, 4.204, 9.846)'
   *   Center: '(-13.717, 23.877, 0.611)'


---


### /World/Conveyor_3
*  **Prim路径 (Prim Path):**/World/Conveyor_3
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '/media/simple/another_Documents/isaacsim_assets/assets/Conveyor_Belt/Conveyor_Belt.usdc'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.799, 4.204, 9.846)'
   *   Center: '(-8.717, 23.877, 0.611)'


---


### /World/Conveyor_4
*  **Prim路径 (Prim Path):**/World/Conveyor_4
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '/media/simple/another_Documents/isaacsim_assets/assets/Conveyor_Belt/Conveyor_Belt.usdc'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.799, 4.204, 9.846)'
   *   Center: '(-3.717, 23.877, 0.611)'


---


### /World/Conveyor_5
*  **Prim路径 (Prim Path):**/World/Conveyor_5
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '/media/simple/another_Documents/isaacsim_assets/assets/Conveyor_Belt/Conveyor_Belt.usdc'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.799, 4.204, 9.846)'
   *   Center: '(1.283, 23.877, 0.611)'


---


### /World/Conveyor_6
*  **Prim路径 (Prim Path):**/World/Conveyor_6
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '/media/simple/another_Documents/isaacsim_assets/assets/Conveyor_Belt/Conveyor_Belt.usdc'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.799, 4.204, 9.846)'
   *   Center: '(6.283, 23.877, 0.611)'


---


### /World/Conveyor_7
*  **Prim路径 (Prim Path):**/World/Conveyor_7
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '/media/simple/another_Documents/isaacsim_assets/assets/Conveyor_Belt/Conveyor_Belt.usdc'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.799, 4.204, 9.846)'
   *   Center: '(11.283, 23.877, 0.611)'


---


### /World/Conveyor_8
*  **Prim路径 (Prim Path):**/World/Conveyor_8
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '/media/simple/another_Documents/isaacsim_assets/assets/Conveyor_Belt/Conveyor_Belt.usdc'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.799, 4.204, 9.846)'
   *   Center: '(16.283, 23.877, 0.611)'


---


### /World/BoxOnConveyor_1
*  **Prim路径 (Prim Path):**/World/BoxOnConveyor_1
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc'
*  **世界包围盒 (World BBox):**
   *   Size: '(35.888, 35.888, 35.888)'
   *   Center: '(-18.700, 19.500, 1.279)'


---


### /World/BoxOnConveyor_2
*  **Prim路径 (Prim Path):**/World/BoxOnConveyor_2
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc'
*  **世界包围盒 (World BBox):**
   *   Size: '(35.888, 35.888, 35.888)'
   *   Center: '(-13.700, 19.500, 1.279)'


---


### /World/BoxOnConveyor_3
*  **Prim路径 (Prim Path):**/World/BoxOnConveyor_3
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc'
*  **世界包围盒 (World BBox):**
   *   Size: '(35.888, 35.888, 35.888)'
   *   Center: '(-8.700, 19.500, 1.279)'


---


### /World/BoxOnConveyor_4
*  **Prim路径 (Prim Path):**/World/BoxOnConveyor_4
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc'
*  **世界包围盒 (World BBox):**
   *   Size: '(35.888, 35.888, 35.888)'
   *   Center: '(-3.700, 19.500, 1.279)'


---


### /World/BoxOnConveyor_5
*  **Prim路径 (Prim Path):**/World/BoxOnConveyor_5
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc'
*  **世界包围盒 (World BBox):**
   *   Size: '(35.888, 35.888, 35.888)'
   *   Center: '(1.300, 19.500, 1.279)'


---


### /World/BoxOnConveyor_6
*  **Prim路径 (Prim Path):**/World/BoxOnConveyor_6
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc'
*  **世界包围盒 (World BBox):**
   *   Size: '(35.888, 35.888, 35.888)'
   *   Center: '(6.300, 19.500, 1.279)'


---


### /World/BoxOnConveyor_7
*  **Prim路径 (Prim Path):**/World/BoxOnConveyor_7
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc'
*  **世界包围盒 (World BBox):**
   *   Size: '(35.888, 35.888, 35.888)'
   *   Center: '(11.300, 19.500, 1.279)'


---


### /World/BoxOnConveyor_8
*  **Prim路径 (Prim Path):**/World/BoxOnConveyor_8
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc'
*  **世界包围盒 (World BBox):**
   *   Size: '(35.888, 35.888, 35.888)'
   *   Center: '(16.300, 19.500, 1.279)'


---


### /World/BoxOnConveyor_9
*  **Prim路径 (Prim Path):**/World/BoxOnConveyor_9
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc'
*  **世界包围盒 (World BBox):**
   *   Size: '(35.888, 35.888, 35.888)'
   *   Center: '(-18.700, 20.400, 1.279)'


---


### /World/BoxOnConveyor_10
*  **Prim路径 (Prim Path):**/World/BoxOnConveyor_10
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc'
*  **世界包围盒 (World BBox):**
   *   Size: '(35.888, 35.888, 35.888)'
   *   Center: '(-13.700, 20.400, 1.279)'


---


### /World/BoxOnConveyor_11
*  **Prim路径 (Prim Path):**/World/BoxOnConveyor_11
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc'
*  **世界包围盒 (World BBox):**
   *   Size: '(35.888, 35.888, 35.888)'
   *   Center: '(-8.700, 20.400, 1.279)'


---


### /World/BoxOnConveyor_12
*  **Prim路径 (Prim Path):**/World/BoxOnConveyor_12
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc'
*  **世界包围盒 (World BBox):**
   *   Size: '(35.888, 35.888, 35.888)'
   *   Center: '(-3.700, 20.400, 1.279)'


---


### /World/BoxOnConveyor_13
*  **Prim路径 (Prim Path):**/World/BoxOnConveyor_13
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc'
*  **世界包围盒 (World BBox):**
   *   Size: '(35.888, 35.888, 35.888)'
   *   Center: '(1.300, 20.400, 1.279)'


---


### /World/BoxOnConveyor_14
*  **Prim路径 (Prim Path):**/World/BoxOnConveyor_14
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc'
*  **世界包围盒 (World BBox):**
   *   Size: '(35.888, 35.888, 35.888)'
   *   Center: '(6.300, 20.400, 1.279)'


---


### /World/BoxOnConveyor_15
*  **Prim路径 (Prim Path):**/World/BoxOnConveyor_15
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc'
*  **世界包围盒 (World BBox):**
   *   Size: '(35.888, 35.888, 35.888)'
   *   Center: '(11.300, 20.400, 1.279)'


---


### /World/BoxOnConveyor_16
*  **Prim路径 (Prim Path):**/World/BoxOnConveyor_16
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc'
*  **世界包围盒 (World BBox):**
   *   Size: '(35.888, 35.888, 35.888)'
   *   Center: '(16.300, 20.400, 1.279)'


---


### /World/BoxOnConveyor_17
*  **Prim路径 (Prim Path):**/World/BoxOnConveyor_17
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc'
*  **世界包围盒 (World BBox):**
   *   Size: '(35.888, 35.888, 35.888)'
   *   Center: '(-18.700, 21.300, 1.279)'


---


### /World/BoxOnConveyor_18
*  **Prim路径 (Prim Path):**/World/BoxOnConveyor_18
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc'
*  **世界包围盒 (World BBox):**
   *   Size: '(35.888, 35.888, 35.888)'
   *   Center: '(-13.700, 21.300, 1.279)'


---


### /World/BoxOnConveyor_19
*  **Prim路径 (Prim Path):**/World/BoxOnConveyor_19
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc'
*  **世界包围盒 (World BBox):**
   *   Size: '(35.888, 35.888, 35.888)'
   *   Center: '(-8.700, 21.300, 1.279)'


---


### /World/BoxOnConveyor_20
*  **Prim路径 (Prim Path):**/World/BoxOnConveyor_20
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc'
*  **世界包围盒 (World BBox):**
   *   Size: '(35.888, 35.888, 35.888)'
   *   Center: '(-3.700, 21.300, 1.279)'


---


### /World/BoxOnConveyor_21
*  **Prim路径 (Prim Path):**/World/BoxOnConveyor_21
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc'
*  **世界包围盒 (World BBox):**
   *   Size: '(35.888, 35.888, 35.888)'
   *   Center: '(1.300, 21.300, 1.279)'


---


### /World/BoxOnConveyor_22
*  **Prim路径 (Prim Path):**/World/BoxOnConveyor_22
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc'
*  **世界包围盒 (World BBox):**
   *   Size: '(35.888, 35.888, 35.888)'
   *   Center: '(6.300, 21.300, 1.279)'


---


### /World/BoxOnConveyor_23
*  **Prim路径 (Prim Path):**/World/BoxOnConveyor_23
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc'
*  **世界包围盒 (World BBox):**
   *   Size: '(35.888, 35.888, 35.888)'
   *   Center: '(11.300, 21.300, 1.279)'


---


### /World/BoxOnConveyor_24
*  **Prim路径 (Prim Path):**/World/BoxOnConveyor_24
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc'
*  **世界包围盒 (World BBox):**
   *   Size: '(35.888, 35.888, 35.888)'
   *   Center: '(16.300, 21.300, 1.279)'


---


### /World/BoxOnConveyor_25
*  **Prim路径 (Prim Path):**/World/BoxOnConveyor_25
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc'
*  **世界包围盒 (World BBox):**
   *   Size: '(35.888, 35.888, 35.888)'
   *   Center: '(-18.700, 22.200, 1.279)'


---


### /World/BoxOnConveyor_26
*  **Prim路径 (Prim Path):**/World/BoxOnConveyor_26
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc'
*  **世界包围盒 (World BBox):**
   *   Size: '(35.888, 35.888, 35.888)'
   *   Center: '(-13.700, 22.200, 1.279)'


---


### /World/BoxOnConveyor_27
*  **Prim路径 (Prim Path):**/World/BoxOnConveyor_27
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc'
*  **世界包围盒 (World BBox):**
   *   Size: '(35.888, 35.888, 35.888)'
   *   Center: '(-8.700, 22.200, 1.279)'


---


### /World/BoxOnConveyor_28
*  **Prim路径 (Prim Path):**/World/BoxOnConveyor_28
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc'
*  **世界包围盒 (World BBox):**
   *   Size: '(35.888, 35.888, 35.888)'
   *   Center: '(-3.700, 22.200, 1.279)'


---


### /World/BoxOnConveyor_29
*  **Prim路径 (Prim Path):**/World/BoxOnConveyor_29
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc'
*  **世界包围盒 (World BBox):**
   *   Size: '(35.888, 35.888, 35.888)'
   *   Center: '(1.300, 22.200, 1.279)'


---


### /World/BoxOnConveyor_30
*  **Prim路径 (Prim Path):**/World/BoxOnConveyor_30
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc'
*  **世界包围盒 (World BBox):**
   *   Size: '(35.888, 35.888, 35.888)'
   *   Center: '(6.300, 22.200, 1.279)'


---


### /World/BoxOnConveyor_31
*  **Prim路径 (Prim Path):**/World/BoxOnConveyor_31
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc'
*  **世界包围盒 (World BBox):**
   *   Size: '(35.888, 35.888, 35.888)'
   *   Center: '(11.300, 22.200, 1.279)'


---


### /World/BoxOnConveyor_32
*  **Prim路径 (Prim Path):**/World/BoxOnConveyor_32
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc'
*  **世界包围盒 (World BBox):**
   *   Size: '(35.888, 35.888, 35.888)'
   *   Center: '(16.300, 22.200, 1.279)'


---


### /World/BoxOnConveyor_33
*  **Prim路径 (Prim Path):**/World/BoxOnConveyor_33
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc'
*  **世界包围盒 (World BBox):**
   *   Size: '(35.888, 35.888, 35.888)'
   *   Center: '(-18.700, 23.100, 1.279)'


---


### /World/BoxOnConveyor_34
*  **Prim路径 (Prim Path):**/World/BoxOnConveyor_34
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc'
*  **世界包围盒 (World BBox):**
   *   Size: '(35.888, 35.888, 35.888)'
   *   Center: '(-13.700, 23.100, 1.279)'


---


### /World/BoxOnConveyor_35
*  **Prim路径 (Prim Path):**/World/BoxOnConveyor_35
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc'
*  **世界包围盒 (World BBox):**
   *   Size: '(35.888, 35.888, 35.888)'
   *   Center: '(-8.700, 23.100, 1.279)'


---


### /World/BoxOnConveyor_36
*  **Prim路径 (Prim Path):**/World/BoxOnConveyor_36
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc'
*  **世界包围盒 (World BBox):**
   *   Size: '(35.888, 35.888, 35.888)'
   *   Center: '(-3.700, 23.100, 1.279)'


---


### /World/BoxOnConveyor_37
*  **Prim路径 (Prim Path):**/World/BoxOnConveyor_37
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc'
*  **世界包围盒 (World BBox):**
   *   Size: '(35.888, 35.888, 35.888)'
   *   Center: '(1.300, 23.100, 1.279)'


---


### /World/BoxOnConveyor_38
*  **Prim路径 (Prim Path):**/World/BoxOnConveyor_38
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc'
*  **世界包围盒 (World BBox):**
   *   Size: '(35.888, 35.888, 35.888)'
   *   Center: '(6.300, 23.100, 1.279)'


---


### /World/BoxOnConveyor_39
*  **Prim路径 (Prim Path):**/World/BoxOnConveyor_39
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc'
*  **世界包围盒 (World BBox):**
   *   Size: '(35.888, 35.888, 35.888)'
   *   Center: '(11.300, 23.100, 1.279)'


---


### /World/BoxOnConveyor_40
*  **Prim路径 (Prim Path):**/World/BoxOnConveyor_40
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc'
*  **世界包围盒 (World BBox):**
   *   Size: '(35.888, 35.888, 35.888)'
   *   Center: '(16.300, 23.100, 1.279)'


---


### /World/BoxOnConveyor_41
*  **Prim路径 (Prim Path):**/World/BoxOnConveyor_41
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc'
*  **世界包围盒 (World BBox):**
   *   Size: '(35.888, 35.888, 35.888)'
   *   Center: '(-18.700, 24.000, 1.279)'


---


### /World/BoxOnConveyor_42
*  **Prim路径 (Prim Path):**/World/BoxOnConveyor_42
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc'
*  **世界包围盒 (World BBox):**
   *   Size: '(35.888, 35.888, 35.888)'
   *   Center: '(-13.700, 24.000, 1.279)'


---


### /World/BoxOnConveyor_43
*  **Prim路径 (Prim Path):**/World/BoxOnConveyor_43
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc'
*  **世界包围盒 (World BBox):**
   *   Size: '(35.888, 35.888, 35.888)'
   *   Center: '(-8.700, 24.000, 1.279)'


---


### /World/BoxOnConveyor_44
*  **Prim路径 (Prim Path):**/World/BoxOnConveyor_44
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc'
*  **世界包围盒 (World BBox):**
   *   Size: '(35.888, 35.888, 35.888)'
   *   Center: '(-3.700, 24.000, 1.279)'


---


### /World/BoxOnConveyor_45
*  **Prim路径 (Prim Path):**/World/BoxOnConveyor_45
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc'
*  **世界包围盒 (World BBox):**
   *   Size: '(35.888, 35.888, 35.888)'
   *   Center: '(1.300, 24.000, 1.279)'


---


### /World/BoxOnConveyor_46
*  **Prim路径 (Prim Path):**/World/BoxOnConveyor_46
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc'
*  **世界包围盒 (World BBox):**
   *   Size: '(35.888, 35.888, 35.888)'
   *   Center: '(6.300, 24.000, 1.279)'


---


### /World/BoxOnConveyor_47
*  **Prim路径 (Prim Path):**/World/BoxOnConveyor_47
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc'
*  **世界包围盒 (World BBox):**
   *   Size: '(35.888, 35.888, 35.888)'
   *   Center: '(11.300, 24.000, 1.279)'


---


### /World/BoxOnConveyor_48
*  **Prim路径 (Prim Path):**/World/BoxOnConveyor_48
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc'
*  **世界包围盒 (World BBox):**
   *   Size: '(35.888, 35.888, 35.888)'
   *   Center: '(16.300, 24.000, 1.279)'


---


### /World/BoxOnConveyor_49
*  **Prim路径 (Prim Path):**/World/BoxOnConveyor_49
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc'
*  **世界包围盒 (World BBox):**
   *   Size: '(35.888, 35.888, 35.888)'
   *   Center: '(-18.700, 24.900, 1.279)'


---


### /World/BoxOnConveyor_50
*  **Prim路径 (Prim Path):**/World/BoxOnConveyor_50
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc'
*  **世界包围盒 (World BBox):**
   *   Size: '(35.888, 35.888, 35.888)'
   *   Center: '(-13.700, 24.900, 1.279)'


---


### /World/BoxOnConveyor_51
*  **Prim路径 (Prim Path):**/World/BoxOnConveyor_51
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc'
*  **世界包围盒 (World BBox):**
   *   Size: '(35.888, 35.888, 35.888)'
   *   Center: '(-8.700, 24.900, 1.279)'


---


### /World/BoxOnConveyor_52
*  **Prim路径 (Prim Path):**/World/BoxOnConveyor_52
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc'
*  **世界包围盒 (World BBox):**
   *   Size: '(35.888, 35.888, 35.888)'
   *   Center: '(-3.700, 24.900, 1.279)'


---


### /World/BoxOnConveyor_53
*  **Prim路径 (Prim Path):**/World/BoxOnConveyor_53
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc'
*  **世界包围盒 (World BBox):**
   *   Size: '(35.888, 35.888, 35.888)'
   *   Center: '(1.300, 24.900, 1.279)'


---


### /World/BoxOnConveyor_54
*  **Prim路径 (Prim Path):**/World/BoxOnConveyor_54
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc'
*  **世界包围盒 (World BBox):**
   *   Size: '(35.888, 35.888, 35.888)'
   *   Center: '(6.300, 24.900, 1.279)'


---


### /World/BoxOnConveyor_55
*  **Prim路径 (Prim Path):**/World/BoxOnConveyor_55
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc'
*  **世界包围盒 (World BBox):**
   *   Size: '(35.888, 35.888, 35.888)'
   *   Center: '(11.300, 24.900, 1.279)'


---


### /World/BoxOnConveyor_56
*  **Prim路径 (Prim Path):**/World/BoxOnConveyor_56
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc'
*  **世界包围盒 (World BBox):**
   *   Size: '(35.888, 35.888, 35.888)'
   *   Center: '(16.300, 24.900, 1.279)'


---


### /World/BoxOnConveyor_57
*  **Prim路径 (Prim Path):**/World/BoxOnConveyor_57
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc'
*  **世界包围盒 (World BBox):**
   *   Size: '(35.888, 35.888, 35.888)'
   *   Center: '(-18.700, 25.800, 1.279)'


---


### /World/BoxOnConveyor_58
*  **Prim路径 (Prim Path):**/World/BoxOnConveyor_58
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc'
*  **世界包围盒 (World BBox):**
   *   Size: '(35.888, 35.888, 35.888)'
   *   Center: '(-13.700, 25.800, 1.279)'


---


### /World/BoxOnConveyor_59
*  **Prim路径 (Prim Path):**/World/BoxOnConveyor_59
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc'
*  **世界包围盒 (World BBox):**
   *   Size: '(35.888, 35.888, 35.888)'
   *   Center: '(-8.700, 25.800, 1.279)'


---


### /World/BoxOnConveyor_60
*  **Prim路径 (Prim Path):**/World/BoxOnConveyor_60
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc'
*  **世界包围盒 (World BBox):**
   *   Size: '(35.888, 35.888, 35.888)'
   *   Center: '(-3.700, 25.800, 1.279)'


---


### /World/BoxOnConveyor_61
*  **Prim路径 (Prim Path):**/World/BoxOnConveyor_61
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc'
*  **世界包围盒 (World BBox):**
   *   Size: '(35.888, 35.888, 35.888)'
   *   Center: '(1.300, 25.800, 1.279)'


---


### /World/BoxOnConveyor_62
*  **Prim路径 (Prim Path):**/World/BoxOnConveyor_62
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc'
*  **世界包围盒 (World BBox):**
   *   Size: '(35.888, 35.888, 35.888)'
   *   Center: '(6.300, 25.800, 1.279)'


---


### /World/BoxOnConveyor_63
*  **Prim路径 (Prim Path):**/World/BoxOnConveyor_63
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc'
*  **世界包围盒 (World BBox):**
   *   Size: '(35.888, 35.888, 35.888)'
   *   Center: '(11.300, 25.800, 1.279)'


---


### /World/BoxOnConveyor_64
*  **Prim路径 (Prim Path):**/World/BoxOnConveyor_64
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc'
*  **世界包围盒 (World BBox):**
   *   Size: '(35.888, 35.888, 35.888)'
   *   Center: '(16.300, 25.800, 1.279)'


---


### /World/BoxOnConveyor_65
*  **Prim路径 (Prim Path):**/World/BoxOnConveyor_65
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc'
*  **世界包围盒 (World BBox):**
   *   Size: '(35.888, 35.888, 35.888)'
   *   Center: '(-18.700, 26.700, 1.279)'


---


### /World/BoxOnConveyor_66
*  **Prim路径 (Prim Path):**/World/BoxOnConveyor_66
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc'
*  **世界包围盒 (World BBox):**
   *   Size: '(35.888, 35.888, 35.888)'
   *   Center: '(-13.700, 26.700, 1.279)'


---


### /World/BoxOnConveyor_67
*  **Prim路径 (Prim Path):**/World/BoxOnConveyor_67
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc'
*  **世界包围盒 (World BBox):**
   *   Size: '(35.888, 35.888, 35.888)'
   *   Center: '(-8.700, 26.700, 1.279)'


---


### /World/BoxOnConveyor_68
*  **Prim路径 (Prim Path):**/World/BoxOnConveyor_68
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc'
*  **世界包围盒 (World BBox):**
   *   Size: '(35.888, 35.888, 35.888)'
   *   Center: '(-3.700, 26.700, 1.279)'


---


### /World/BoxOnConveyor_69
*  **Prim路径 (Prim Path):**/World/BoxOnConveyor_69
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc'
*  **世界包围盒 (World BBox):**
   *   Size: '(35.888, 35.888, 35.888)'
   *   Center: '(1.300, 26.700, 1.279)'


---


### /World/BoxOnConveyor_70
*  **Prim路径 (Prim Path):**/World/BoxOnConveyor_70
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc'
*  **世界包围盒 (World BBox):**
   *   Size: '(35.888, 35.888, 35.888)'
   *   Center: '(6.300, 26.700, 1.279)'


---


### /World/BoxOnConveyor_71
*  **Prim路径 (Prim Path):**/World/BoxOnConveyor_71
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc'
*  **世界包围盒 (World BBox):**
   *   Size: '(35.888, 35.888, 35.888)'
   *   Center: '(11.300, 26.700, 1.279)'


---


### /World/BoxOnConveyor_72
*  **Prim路径 (Prim Path):**/World/BoxOnConveyor_72
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc'
*  **世界包围盒 (World BBox):**
   *   Size: '(35.888, 35.888, 35.888)'
   *   Center: '(16.300, 26.700, 1.279)'


---


### /World/BoxOnConveyor_73
*  **Prim路径 (Prim Path):**/World/BoxOnConveyor_73
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc'
*  **世界包围盒 (World BBox):**
   *   Size: '(35.888, 35.888, 35.888)'
   *   Center: '(-18.700, 27.600, 1.279)'


---


### /World/BoxOnConveyor_74
*  **Prim路径 (Prim Path):**/World/BoxOnConveyor_74
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc'
*  **世界包围盒 (World BBox):**
   *   Size: '(35.888, 35.888, 35.888)'
   *   Center: '(-13.700, 27.600, 1.279)'


---


### /World/BoxOnConveyor_75
*  **Prim路径 (Prim Path):**/World/BoxOnConveyor_75
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc'
*  **世界包围盒 (World BBox):**
   *   Size: '(35.888, 35.888, 35.888)'
   *   Center: '(-8.700, 27.600, 1.279)'


---


### /World/BoxOnConveyor_76
*  **Prim路径 (Prim Path):**/World/BoxOnConveyor_76
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc'
*  **世界包围盒 (World BBox):**
   *   Size: '(35.888, 35.888, 35.888)'
   *   Center: '(-3.700, 27.600, 1.279)'


---


### /World/BoxOnConveyor_77
*  **Prim路径 (Prim Path):**/World/BoxOnConveyor_77
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc'
*  **世界包围盒 (World BBox):**
   *   Size: '(35.888, 35.888, 35.888)'
   *   Center: '(1.300, 27.600, 1.279)'


---


### /World/BoxOnConveyor_78
*  **Prim路径 (Prim Path):**/World/BoxOnConveyor_78
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc'
*  **世界包围盒 (World BBox):**
   *   Size: '(35.888, 35.888, 35.888)'
   *   Center: '(6.300, 27.600, 1.279)'


---


### /World/BoxOnConveyor_79
*  **Prim路径 (Prim Path):**/World/BoxOnConveyor_79
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc'
*  **世界包围盒 (World BBox):**
   *   Size: '(35.888, 35.888, 35.888)'
   *   Center: '(11.300, 27.600, 1.279)'


---


### /World/BoxOnConveyor_80
*  **Prim路径 (Prim Path):**/World/BoxOnConveyor_80
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc'
*  **世界包围盒 (World BBox):**
   *   Size: '(35.888, 35.888, 35.888)'
   *   Center: '(16.300, 27.600, 1.279)'


---


### /World/StackedCarton_1
*  **Prim路径 (Prim Path):**/World/StackedCarton_1
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc'
*  **世界包围盒 (World BBox):**
   *   Size: '(35.888, 35.888, 35.888)'
   *   Center: '(-18.500, 29.250, 0.562)'


---


### /World/StackedCarton_2
*  **Prim路径 (Prim Path):**/World/StackedCarton_2
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc'
*  **世界包围盒 (World BBox):**
   *   Size: '(35.888, 35.888, 35.888)'
   *   Center: '(-13.500, 29.250, 0.562)'


---


### /World/StackedCarton_3
*  **Prim路径 (Prim Path):**/World/StackedCarton_3
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc'
*  **世界包围盒 (World BBox):**
   *   Size: '(35.888, 35.888, 35.888)'
   *   Center: '(-8.500, 29.250, 0.562)'


---


### /World/StackedCarton_4
*  **Prim路径 (Prim Path):**/World/StackedCarton_4
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc'
*  **世界包围盒 (World BBox):**
   *   Size: '(35.888, 35.888, 35.888)'
   *   Center: '(-3.500, 29.250, 0.562)'


---


### /World/StackedCarton_5
*  **Prim路径 (Prim Path):**/World/StackedCarton_5
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc'
*  **世界包围盒 (World BBox):**
   *   Size: '(35.888, 35.888, 35.888)'
   *   Center: '(1.500, 29.250, 0.562)'


---


### /World/StackedCarton_6
*  **Prim路径 (Prim Path):**/World/StackedCarton_6
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc'
*  **世界包围盒 (World BBox):**
   *   Size: '(35.888, 35.888, 35.888)'
   *   Center: '(6.500, 29.250, 0.562)'


---


### /World/StackedCarton_7
*  **Prim路径 (Prim Path):**/World/StackedCarton_7
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc'
*  **世界包围盒 (World BBox):**
   *   Size: '(35.888, 35.888, 35.888)'
   *   Center: '(11.500, 29.250, 0.562)'


---


### /World/StackedCarton_8
*  **Prim路径 (Prim Path):**/World/StackedCarton_8
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc'
*  **世界包围盒 (World BBox):**
   *   Size: '(35.888, 35.888, 35.888)'
   *   Center: '(16.500, 29.250, 0.562)'


---


### /World/StackedCarton1_1
*  **Prim路径 (Prim Path):**/World/StackedCarton1_1
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc'
*  **世界包围盒 (World BBox):**
   *   Size: '(35.888, 35.888, 35.888)'
   *   Center: '(-18.900, 29.250, 0.562)'


---


### /World/StackedCarton1_2
*  **Prim路径 (Prim Path):**/World/StackedCarton1_2
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc'
*  **世界包围盒 (World BBox):**
   *   Size: '(35.888, 35.888, 35.888)'
   *   Center: '(-13.900, 29.250, 0.562)'


---


### /World/StackedCarton1_3
*  **Prim路径 (Prim Path):**/World/StackedCarton1_3
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc'
*  **世界包围盒 (World BBox):**
   *   Size: '(35.888, 35.888, 35.888)'
   *   Center: '(-8.900, 29.250, 0.562)'


---


### /World/StackedCarton1_4
*  **Prim路径 (Prim Path):**/World/StackedCarton1_4
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc'
*  **世界包围盒 (World BBox):**
   *   Size: '(35.888, 35.888, 35.888)'
   *   Center: '(-3.900, 29.250, 0.562)'


---


### /World/StackedCarton1_5
*  **Prim路径 (Prim Path):**/World/StackedCarton1_5
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc'
*  **世界包围盒 (World BBox):**
   *   Size: '(35.888, 35.888, 35.888)'
   *   Center: '(1.100, 29.250, 0.562)'


---


### /World/StackedCarton1_6
*  **Prim路径 (Prim Path):**/World/StackedCarton1_6
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc'
*  **世界包围盒 (World BBox):**
   *   Size: '(35.888, 35.888, 35.888)'
   *   Center: '(6.100, 29.250, 0.562)'


---


### /World/StackedCarton1_7
*  **Prim路径 (Prim Path):**/World/StackedCarton1_7
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc'
*  **世界包围盒 (World BBox):**
   *   Size: '(35.888, 35.888, 35.888)'
   *   Center: '(11.100, 29.250, 0.562)'


---


### /World/StackedCarton1_8
*  **Prim路径 (Prim Path):**/World/StackedCarton1_8
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc'
*  **世界包围盒 (World BBox):**
   *   Size: '(35.888, 35.888, 35.888)'
   *   Center: '(16.100, 29.250, 0.562)'


---


### /World/StackedCarton2_1
*  **Prim路径 (Prim Path):**/World/StackedCarton2_1
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc'
*  **世界包围盒 (World BBox):**
   *   Size: '(35.888, 35.888, 35.888)'
   *   Center: '(-18.700, 29.250, 0.919)'


---


### /World/StackedCarton2_2
*  **Prim路径 (Prim Path):**/World/StackedCarton2_2
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc'
*  **世界包围盒 (World BBox):**
   *   Size: '(35.888, 35.888, 35.888)'
   *   Center: '(-13.700, 29.250, 0.919)'


---


### /World/StackedCarton2_3
*  **Prim路径 (Prim Path):**/World/StackedCarton2_3
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc'
*  **世界包围盒 (World BBox):**
   *   Size: '(35.888, 35.888, 35.888)'
   *   Center: '(-8.700, 29.250, 0.919)'


---


### /World/StackedCarton2_4
*  **Prim路径 (Prim Path):**/World/StackedCarton2_4
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc'
*  **世界包围盒 (World BBox):**
   *   Size: '(35.888, 35.888, 35.888)'
   *   Center: '(-3.700, 29.250, 0.919)'


---


### /World/StackedCarton2_5
*  **Prim路径 (Prim Path):**/World/StackedCarton2_5
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc'
*  **世界包围盒 (World BBox):**
   *   Size: '(35.888, 35.888, 35.888)'
   *   Center: '(1.300, 29.250, 0.919)'


---


### /World/StackedCarton2_6
*  **Prim路径 (Prim Path):**/World/StackedCarton2_6
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc'
*  **世界包围盒 (World BBox):**
   *   Size: '(35.888, 35.888, 35.888)'
   *   Center: '(6.300, 29.250, 0.919)'


---


### /World/StackedCarton2_7
*  **Prim路径 (Prim Path):**/World/StackedCarton2_7
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc'
*  **世界包围盒 (World BBox):**
   *   Size: '(35.888, 35.888, 35.888)'
   *   Center: '(11.300, 29.250, 0.919)'


---


### /World/StackedCarton2_8
*  **Prim路径 (Prim Path):**/World/StackedCarton2_8
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc'
*  **世界包围盒 (World BBox):**
   *   Size: '(35.888, 35.888, 35.888)'
   *   Center: '(16.300, 29.250, 0.919)'


---


### /World/model_desk008
*  **Prim路径 (Prim Path):**/World/model_desk008
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '../device_data/usdz/Workbench/model_desk008.usdz'
*  **世界包围盒 (World BBox):**
   *   Size: '(1.969, 0.959, 0.655)'
   *   Center: '(17.323, 27.806, 0.482)'


---


### /World/INDUSTRIAL_ROBOTIC_ARM
*  **Prim路径 (Prim Path):**/World/INDUSTRIAL_ROBOTIC_ARM
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '../device_data/usdz/IndustrialRobot/INDUSTRIAL_ROBOTIC_ARM.usdz'
*  **世界包围盒 (World BBox):**
   *   Size: '(78.095, 126.534, 112.695)'
   *   Center: '(17.321, 27.961, 1.423)'


---


### /World/processed_Robotic_Manipulator_low_poly
*  **Prim路径 (Prim Path):**/World/processed_Robotic_Manipulator_low_poly
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '../device_data/usdz/IndustrialRobot/processed_Robotic_Manipulator_low_poly.usdz'
*  **世界包围盒 (World BBox):**
   *   Size: '(117.387, 95.149, 72.734)'
   *   Center: '(15.617, 28.476, 1.285)'


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


### /World/agv_1/chassis/Body/Looks/Robot
*  **Prim路径 (Prim Path):**/World/agv_1/chassis/Body/Looks/Robot
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/agv_1/chassis/Body/Looks/Robot/Robot'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/agv_1/chassis/Body/Looks/Robot/Robot'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   纹理引用 (Texture Assets):
           *   'Textures/STL_Robot_albedo.<UDIM>.png'
           *   'Textures/STL_Robot_emissive.<UDIM>.png'
           *   'Textures/STL_Robot_normal.<UDIM>.png'
           *   'Textures/STL_Robot_orm.<UDIM>.png'
       *   Inputs:
           *   'diffuse_color_constant' [color3f]
               *   Connected: '/World/agv_1/chassis/Body/Looks/Robot.inputs:diffuse_color_constant' @ '/World/agv_1/chassis/Body/Looks/Robot'
           *   'diffuse_texture' [asset] = 'Textures/STL_Robot_albedo.<UDIM>.png'
           *   'emissive_color' [color3f]
               *   Connected: '/World/agv_1/chassis/Body/Looks/Robot.inputs:emissive_color' @ '/World/agv_1/chassis/Body/Looks/Robot'
           *   'emissive_intensity' [float] = '8000'
           *   'emissive_mask_texture' [asset] = 'Textures/STL_Robot_emissive.<UDIM>.png'
           *   'metallic_texture_influence' [float] = '0.9'
           *   'normalmap_texture' [asset] = 'Textures/STL_Robot_normal.<UDIM>.png'
           *   'ORM_texture' [asset] = 'Textures/STL_Robot_orm.<UDIM>.png'
           *   'reflection_roughness_texture_influence' [float] = '1'
           *   'uv_space_index' [int]
               *   Connected: '/World/agv_1/chassis/Body/Looks/Robot.inputs:uv_space_index' @ '/World/agv_1/chassis/Body/Looks/Robot'


---


### /World/agv_1/left_wheel/Left_Wheel/Looks/Robot
*  **Prim路径 (Prim Path):**/World/agv_1/left_wheel/Left_Wheel/Looks/Robot
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/agv_1/left_wheel/Left_Wheel/Looks/Robot/Robot'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/agv_1/left_wheel/Left_Wheel/Looks/Robot/Robot'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   纹理引用 (Texture Assets):
           *   'Textures/STL_Robot_albedo.<UDIM>.png'
           *   'Textures/STL_Robot_normal.<UDIM>.png'
           *   'Textures/STL_Robot_orm.<UDIM>.png'
       *   Inputs:
           *   'diffuse_color_constant' [color3f]
               *   Connected: '/World/agv_1/left_wheel/Left_Wheel/Looks/Robot.inputs:diffuse_color_constant' @ '/World/agv_1/left_wheel/Left_Wheel/Looks/Robot'
           *   'diffuse_texture' [asset] = 'Textures/STL_Robot_albedo.<UDIM>.png'
           *   'emissive_color' [color3f]
               *   Connected: '/World/agv_1/left_wheel/Left_Wheel/Looks/Robot.inputs:emissive_color' @ '/World/agv_1/left_wheel/Left_Wheel/Looks/Robot'
           *   'metallic_texture_influence' [float] = '1'
           *   'normalmap_texture' [asset] = 'Textures/STL_Robot_normal.<UDIM>.png'
           *   'ORM_texture' [asset] = 'Textures/STL_Robot_orm.<UDIM>.png'
           *   'reflection_roughness_texture_influence' [float] = '1'
           *   'uv_space_index' [int]
               *   Connected: '/World/agv_1/left_wheel/Left_Wheel/Looks/Robot.inputs:uv_space_index' @ '/World/agv_1/left_wheel/Left_Wheel/Looks/Robot'


---


### /World/agv_1/right_wheel/Right_Wheel/Looks/Robot
*  **Prim路径 (Prim Path):**/World/agv_1/right_wheel/Right_Wheel/Looks/Robot
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/agv_1/right_wheel/Right_Wheel/Looks/Robot/Robot'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/agv_1/right_wheel/Right_Wheel/Looks/Robot/Robot'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   纹理引用 (Texture Assets):
           *   'Textures/STL_Robot_albedo.<UDIM>.png'
           *   'Textures/STL_Robot_normal.<UDIM>.png'
           *   'Textures/STL_Robot_orm.<UDIM>.png'
       *   Inputs:
           *   'diffuse_color_constant' [color3f]
               *   Connected: '/World/agv_1/right_wheel/Right_Wheel/Looks/Robot.inputs:diffuse_color_constant' @ '/World/agv_1/right_wheel/Right_Wheel/Looks/Robot'
           *   'diffuse_texture' [asset] = 'Textures/STL_Robot_albedo.<UDIM>.png'
           *   'emissive_color' [color3f]
               *   Connected: '/World/agv_1/right_wheel/Right_Wheel/Looks/Robot.inputs:emissive_color' @ '/World/agv_1/right_wheel/Right_Wheel/Looks/Robot'
           *   'metallic_texture_influence' [float] = '1'
           *   'normalmap_texture' [asset] = 'Textures/STL_Robot_normal.<UDIM>.png'
           *   'ORM_texture' [asset] = 'Textures/STL_Robot_orm.<UDIM>.png'
           *   'reflection_roughness_texture_influence' [float] = '1'
           *   'uv_space_index' [int]
               *   Connected: '/World/agv_1/right_wheel/Right_Wheel/Looks/Robot.inputs:uv_space_index' @ '/World/agv_1/right_wheel/Right_Wheel/Looks/Robot'


---


### /World/agv_1/lift/Lift/Looks/Robot
*  **Prim路径 (Prim Path):**/World/agv_1/lift/Lift/Looks/Robot
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/agv_1/lift/Lift/Looks/Robot/Robot'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/agv_1/lift/Lift/Looks/Robot/Robot'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   纹理引用 (Texture Assets):
           *   'Textures/STL_Robot_albedo.<UDIM>.png'
           *   'Textures/STL_Robot_normal.<UDIM>.png'
           *   'Textures/STL_Robot_orm.<UDIM>.png'
       *   Inputs:
           *   'diffuse_color_constant' [color3f]
               *   Connected: '/World/agv_1/lift/Lift/Looks/Robot.inputs:diffuse_color_constant' @ '/World/agv_1/lift/Lift/Looks/Robot'
           *   'diffuse_texture' [asset] = 'Textures/STL_Robot_albedo.<UDIM>.png'
           *   'emissive_color' [color3f]
               *   Connected: '/World/agv_1/lift/Lift/Looks/Robot.inputs:emissive_color' @ '/World/agv_1/lift/Lift/Looks/Robot'
           *   'metallic_texture_influence' [float] = '0.901'
           *   'normalmap_texture' [asset] = 'Textures/STL_Robot_normal.<UDIM>.png'
           *   'ORM_texture' [asset] = 'Textures/STL_Robot_orm.<UDIM>.png'
           *   'reflection_roughness_texture_influence' [float] = '1'
           *   'uv_space_index' [int]
               *   Connected: '/World/agv_1/lift/Lift/Looks/Robot.inputs:uv_space_index' @ '/World/agv_1/lift/Lift/Looks/Robot'


---


### /World/agv_1/left_swivel/Left_Swivel/materials/Looks/Robot
*  **Prim路径 (Prim Path):**/World/agv_1/left_swivel/Left_Swivel/materials/Looks/Robot
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/agv_1/left_swivel/Left_Swivel/materials/Looks/Robot/Robot'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/agv_1/left_swivel/Left_Swivel/materials/Looks/Robot/Robot'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   纹理引用 (Texture Assets):
           *   'Textures/STL_Robot_albedo.%3CUDIM%3E.png'
           *   'Textures/STL_Robot_normal.%3CUDIM%3E.png'
           *   'Textures/STL_Robot_orm.%3CUDIM%3E.png'
       *   Inputs:
           *   'diffuse_color_constant' [color3f]
               *   Connected: '/World/agv_1/left_swivel/Left_Swivel/materials/Looks/Robot.inputs:diffuse_color_constant' @ '/World/agv_1/left_swivel/Left_Swivel/materials/Looks/Robot'
           *   'diffuse_texture' [asset] = 'Textures/STL_Robot_albedo.%3CUDIM%3E.png'
           *   'emissive_color' [color3f]
               *   Connected: '/World/agv_1/left_swivel/Left_Swivel/materials/Looks/Robot.inputs:emissive_color' @ '/World/agv_1/left_swivel/Left_Swivel/materials/Looks/Robot'
           *   'metallic_texture_influence' [float] = '1'
           *   'normalmap_texture' [asset] = 'Textures/STL_Robot_normal.%3CUDIM%3E.png'
           *   'ORM_texture' [asset] = 'Textures/STL_Robot_orm.%3CUDIM%3E.png'
           *   'reflection_roughness_texture_influence' [float] = '1'
           *   'uv_space_index' [int]
               *   Connected: '/World/agv_1/left_swivel/Left_Swivel/materials/Looks/Robot.inputs:uv_space_index' @ '/World/agv_1/left_swivel/Left_Swivel/materials/Looks/Robot'


---


### /World/agv_1/right_swivel/Right_Swivel/materials/Looks/Robot
*  **Prim路径 (Prim Path):**/World/agv_1/right_swivel/Right_Swivel/materials/Looks/Robot
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/agv_1/right_swivel/Right_Swivel/materials/Looks/Robot/Robot'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/agv_1/right_swivel/Right_Swivel/materials/Looks/Robot/Robot'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   纹理引用 (Texture Assets):
           *   'Textures/STL_Robot_albedo.%3CUDIM%3E.png'
           *   'Textures/STL_Robot_normal.%3CUDIM%3E.png'
           *   'Textures/STL_Robot_orm.%3CUDIM%3E.png'
       *   Inputs:
           *   'diffuse_color_constant' [color3f]
               *   Connected: '/World/agv_1/right_swivel/Right_Swivel/materials/Looks/Robot.inputs:diffuse_color_constant' @ '/World/agv_1/right_swivel/Right_Swivel/materials/Looks/Robot'
           *   'diffuse_texture' [asset] = 'Textures/STL_Robot_albedo.%3CUDIM%3E.png'
           *   'emissive_color' [color3f]
               *   Connected: '/World/agv_1/right_swivel/Right_Swivel/materials/Looks/Robot.inputs:emissive_color' @ '/World/agv_1/right_swivel/Right_Swivel/materials/Looks/Robot'
           *   'metallic_texture_influence' [float] = '1'
           *   'normalmap_texture' [asset] = 'Textures/STL_Robot_normal.%3CUDIM%3E.png'
           *   'ORM_texture' [asset] = 'Textures/STL_Robot_orm.%3CUDIM%3E.png'
           *   'reflection_roughness_texture_influence' [float] = '1'
           *   'uv_space_index' [int]
               *   Connected: '/World/agv_1/right_swivel/Right_Swivel/materials/Looks/Robot.inputs:uv_space_index' @ '/World/agv_1/right_swivel/Right_Swivel/materials/Looks/Robot'


---


### /World/agv_1/left_caster/Inner_Left_Wheel/materials/Looks/Robot
*  **Prim路径 (Prim Path):**/World/agv_1/left_caster/Inner_Left_Wheel/materials/Looks/Robot
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/agv_1/left_caster/Inner_Left_Wheel/materials/Looks/Robot/Robot'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/agv_1/left_caster/Inner_Left_Wheel/materials/Looks/Robot/Robot'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   纹理引用 (Texture Assets):
           *   'Textures/STL_Robot_albedo.%3CUDIM%3E.png'
           *   'Textures/STL_Robot_normal.%3CUDIM%3E.png'
           *   'Textures/STL_Robot_orm.%3CUDIM%3E.png'
       *   Inputs:
           *   'diffuse_color_constant' [color3f]
               *   Connected: '/World/agv_1/left_caster/Inner_Left_Wheel/materials/Looks/Robot.inputs:diffuse_color_constant' @ '/World/agv_1/left_caster/Inner_Left_Wheel/materials/Looks/Robot'
           *   'diffuse_texture' [asset] = 'Textures/STL_Robot_albedo.%3CUDIM%3E.png'
           *   'emissive_color' [color3f]
               *   Connected: '/World/agv_1/left_caster/Inner_Left_Wheel/materials/Looks/Robot.inputs:emissive_color' @ '/World/agv_1/left_caster/Inner_Left_Wheel/materials/Looks/Robot'
           *   'metallic_texture_influence' [float] = '1'
           *   'normalmap_texture' [asset] = 'Textures/STL_Robot_normal.%3CUDIM%3E.png'
           *   'ORM_texture' [asset] = 'Textures/STL_Robot_orm.%3CUDIM%3E.png'
           *   'reflection_roughness_texture_influence' [float] = '1'
           *   'uv_space_index' [int]
               *   Connected: '/World/agv_1/left_caster/Inner_Left_Wheel/materials/Looks/Robot.inputs:uv_space_index' @ '/World/agv_1/left_caster/Inner_Left_Wheel/materials/Looks/Robot'


---


### /World/agv_1/right_caster/Inner_Right_Wheel/materials/Looks/Robot
*  **Prim路径 (Prim Path):**/World/agv_1/right_caster/Inner_Right_Wheel/materials/Looks/Robot
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/agv_1/right_caster/Inner_Right_Wheel/materials/Looks/Robot/Robot'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/agv_1/right_caster/Inner_Right_Wheel/materials/Looks/Robot/Robot'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   纹理引用 (Texture Assets):
           *   'Textures/STL_Robot_albedo.%3CUDIM%3E.png'
           *   'Textures/STL_Robot_normal.%3CUDIM%3E.png'
           *   'Textures/STL_Robot_orm.%3CUDIM%3E.png'
       *   Inputs:
           *   'diffuse_color_constant' [color3f]
               *   Connected: '/World/agv_1/right_caster/Inner_Right_Wheel/materials/Looks/Robot.inputs:diffuse_color_constant' @ '/World/agv_1/right_caster/Inner_Right_Wheel/materials/Looks/Robot'
           *   'diffuse_texture' [asset] = 'Textures/STL_Robot_albedo.%3CUDIM%3E.png'
           *   'emissive_color' [color3f]
               *   Connected: '/World/agv_1/right_caster/Inner_Right_Wheel/materials/Looks/Robot.inputs:emissive_color' @ '/World/agv_1/right_caster/Inner_Right_Wheel/materials/Looks/Robot'
           *   'metallic_texture_influence' [float] = '1'
           *   'normalmap_texture' [asset] = 'Textures/STL_Robot_normal.%3CUDIM%3E.png'
           *   'ORM_texture' [asset] = 'Textures/STL_Robot_orm.%3CUDIM%3E.png'
           *   'reflection_roughness_texture_influence' [float] = '1'
           *   'uv_space_index' [int]
               *   Connected: '/World/agv_1/right_caster/Inner_Right_Wheel/materials/Looks/Robot.inputs:uv_space_index' @ '/World/agv_1/right_caster/Inner_Right_Wheel/materials/Looks/Robot'


---


### /World/agv_1/wheel_material
*  **Prim路径 (Prim Path):**/World/agv_1/wheel_material
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'


---


### /World/agv_1/caster_material
*  **Prim路径 (Prim Path):**/World/agv_1/caster_material
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'


---


### /World/agv_2/chassis/Body/Looks/Robot
*  **Prim路径 (Prim Path):**/World/agv_2/chassis/Body/Looks/Robot
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/agv_2/chassis/Body/Looks/Robot/Robot'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/agv_2/chassis/Body/Looks/Robot/Robot'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   纹理引用 (Texture Assets):
           *   'Textures/STL_Robot_albedo.<UDIM>.png'
           *   'Textures/STL_Robot_emissive.<UDIM>.png'
           *   'Textures/STL_Robot_normal.<UDIM>.png'
           *   'Textures/STL_Robot_orm.<UDIM>.png'
       *   Inputs:
           *   'diffuse_color_constant' [color3f]
               *   Connected: '/World/agv_2/chassis/Body/Looks/Robot.inputs:diffuse_color_constant' @ '/World/agv_2/chassis/Body/Looks/Robot'
           *   'diffuse_texture' [asset] = 'Textures/STL_Robot_albedo.<UDIM>.png'
           *   'emissive_color' [color3f]
               *   Connected: '/World/agv_2/chassis/Body/Looks/Robot.inputs:emissive_color' @ '/World/agv_2/chassis/Body/Looks/Robot'
           *   'emissive_intensity' [float] = '8000'
           *   'emissive_mask_texture' [asset] = 'Textures/STL_Robot_emissive.<UDIM>.png'
           *   'metallic_texture_influence' [float] = '0.9'
           *   'normalmap_texture' [asset] = 'Textures/STL_Robot_normal.<UDIM>.png'
           *   'ORM_texture' [asset] = 'Textures/STL_Robot_orm.<UDIM>.png'
           *   'reflection_roughness_texture_influence' [float] = '1'
           *   'uv_space_index' [int]
               *   Connected: '/World/agv_2/chassis/Body/Looks/Robot.inputs:uv_space_index' @ '/World/agv_2/chassis/Body/Looks/Robot'


---


### /World/agv_2/left_wheel/Left_Wheel/Looks/Robot
*  **Prim路径 (Prim Path):**/World/agv_2/left_wheel/Left_Wheel/Looks/Robot
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/agv_2/left_wheel/Left_Wheel/Looks/Robot/Robot'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/agv_2/left_wheel/Left_Wheel/Looks/Robot/Robot'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   纹理引用 (Texture Assets):
           *   'Textures/STL_Robot_albedo.<UDIM>.png'
           *   'Textures/STL_Robot_normal.<UDIM>.png'
           *   'Textures/STL_Robot_orm.<UDIM>.png'
       *   Inputs:
           *   'diffuse_color_constant' [color3f]
               *   Connected: '/World/agv_2/left_wheel/Left_Wheel/Looks/Robot.inputs:diffuse_color_constant' @ '/World/agv_2/left_wheel/Left_Wheel/Looks/Robot'
           *   'diffuse_texture' [asset] = 'Textures/STL_Robot_albedo.<UDIM>.png'
           *   'emissive_color' [color3f]
               *   Connected: '/World/agv_2/left_wheel/Left_Wheel/Looks/Robot.inputs:emissive_color' @ '/World/agv_2/left_wheel/Left_Wheel/Looks/Robot'
           *   'metallic_texture_influence' [float] = '1'
           *   'normalmap_texture' [asset] = 'Textures/STL_Robot_normal.<UDIM>.png'
           *   'ORM_texture' [asset] = 'Textures/STL_Robot_orm.<UDIM>.png'
           *   'reflection_roughness_texture_influence' [float] = '1'
           *   'uv_space_index' [int]
               *   Connected: '/World/agv_2/left_wheel/Left_Wheel/Looks/Robot.inputs:uv_space_index' @ '/World/agv_2/left_wheel/Left_Wheel/Looks/Robot'


---


### /World/agv_2/right_wheel/Right_Wheel/Looks/Robot
*  **Prim路径 (Prim Path):**/World/agv_2/right_wheel/Right_Wheel/Looks/Robot
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/agv_2/right_wheel/Right_Wheel/Looks/Robot/Robot'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/agv_2/right_wheel/Right_Wheel/Looks/Robot/Robot'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   纹理引用 (Texture Assets):
           *   'Textures/STL_Robot_albedo.<UDIM>.png'
           *   'Textures/STL_Robot_normal.<UDIM>.png'
           *   'Textures/STL_Robot_orm.<UDIM>.png'
       *   Inputs:
           *   'diffuse_color_constant' [color3f]
               *   Connected: '/World/agv_2/right_wheel/Right_Wheel/Looks/Robot.inputs:diffuse_color_constant' @ '/World/agv_2/right_wheel/Right_Wheel/Looks/Robot'
           *   'diffuse_texture' [asset] = 'Textures/STL_Robot_albedo.<UDIM>.png'
           *   'emissive_color' [color3f]
               *   Connected: '/World/agv_2/right_wheel/Right_Wheel/Looks/Robot.inputs:emissive_color' @ '/World/agv_2/right_wheel/Right_Wheel/Looks/Robot'
           *   'metallic_texture_influence' [float] = '1'
           *   'normalmap_texture' [asset] = 'Textures/STL_Robot_normal.<UDIM>.png'
           *   'ORM_texture' [asset] = 'Textures/STL_Robot_orm.<UDIM>.png'
           *   'reflection_roughness_texture_influence' [float] = '1'
           *   'uv_space_index' [int]
               *   Connected: '/World/agv_2/right_wheel/Right_Wheel/Looks/Robot.inputs:uv_space_index' @ '/World/agv_2/right_wheel/Right_Wheel/Looks/Robot'


---


### /World/agv_2/lift/Lift/Looks/Robot
*  **Prim路径 (Prim Path):**/World/agv_2/lift/Lift/Looks/Robot
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/agv_2/lift/Lift/Looks/Robot/Robot'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/agv_2/lift/Lift/Looks/Robot/Robot'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   纹理引用 (Texture Assets):
           *   'Textures/STL_Robot_albedo.<UDIM>.png'
           *   'Textures/STL_Robot_normal.<UDIM>.png'
           *   'Textures/STL_Robot_orm.<UDIM>.png'
       *   Inputs:
           *   'diffuse_color_constant' [color3f]
               *   Connected: '/World/agv_2/lift/Lift/Looks/Robot.inputs:diffuse_color_constant' @ '/World/agv_2/lift/Lift/Looks/Robot'
           *   'diffuse_texture' [asset] = 'Textures/STL_Robot_albedo.<UDIM>.png'
           *   'emissive_color' [color3f]
               *   Connected: '/World/agv_2/lift/Lift/Looks/Robot.inputs:emissive_color' @ '/World/agv_2/lift/Lift/Looks/Robot'
           *   'metallic_texture_influence' [float] = '0.901'
           *   'normalmap_texture' [asset] = 'Textures/STL_Robot_normal.<UDIM>.png'
           *   'ORM_texture' [asset] = 'Textures/STL_Robot_orm.<UDIM>.png'
           *   'reflection_roughness_texture_influence' [float] = '1'
           *   'uv_space_index' [int]
               *   Connected: '/World/agv_2/lift/Lift/Looks/Robot.inputs:uv_space_index' @ '/World/agv_2/lift/Lift/Looks/Robot'


---


### /World/agv_2/left_swivel/Left_Swivel/materials/Looks/Robot
*  **Prim路径 (Prim Path):**/World/agv_2/left_swivel/Left_Swivel/materials/Looks/Robot
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/agv_2/left_swivel/Left_Swivel/materials/Looks/Robot/Robot'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/agv_2/left_swivel/Left_Swivel/materials/Looks/Robot/Robot'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   纹理引用 (Texture Assets):
           *   'Textures/STL_Robot_albedo.%3CUDIM%3E.png'
           *   'Textures/STL_Robot_normal.%3CUDIM%3E.png'
           *   'Textures/STL_Robot_orm.%3CUDIM%3E.png'
       *   Inputs:
           *   'diffuse_color_constant' [color3f]
               *   Connected: '/World/agv_2/left_swivel/Left_Swivel/materials/Looks/Robot.inputs:diffuse_color_constant' @ '/World/agv_2/left_swivel/Left_Swivel/materials/Looks/Robot'
           *   'diffuse_texture' [asset] = 'Textures/STL_Robot_albedo.%3CUDIM%3E.png'
           *   'emissive_color' [color3f]
               *   Connected: '/World/agv_2/left_swivel/Left_Swivel/materials/Looks/Robot.inputs:emissive_color' @ '/World/agv_2/left_swivel/Left_Swivel/materials/Looks/Robot'
           *   'metallic_texture_influence' [float] = '1'
           *   'normalmap_texture' [asset] = 'Textures/STL_Robot_normal.%3CUDIM%3E.png'
           *   'ORM_texture' [asset] = 'Textures/STL_Robot_orm.%3CUDIM%3E.png'
           *   'reflection_roughness_texture_influence' [float] = '1'
           *   'uv_space_index' [int]
               *   Connected: '/World/agv_2/left_swivel/Left_Swivel/materials/Looks/Robot.inputs:uv_space_index' @ '/World/agv_2/left_swivel/Left_Swivel/materials/Looks/Robot'


---


### /World/agv_2/right_swivel/Right_Swivel/materials/Looks/Robot
*  **Prim路径 (Prim Path):**/World/agv_2/right_swivel/Right_Swivel/materials/Looks/Robot
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/agv_2/right_swivel/Right_Swivel/materials/Looks/Robot/Robot'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/agv_2/right_swivel/Right_Swivel/materials/Looks/Robot/Robot'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   纹理引用 (Texture Assets):
           *   'Textures/STL_Robot_albedo.%3CUDIM%3E.png'
           *   'Textures/STL_Robot_normal.%3CUDIM%3E.png'
           *   'Textures/STL_Robot_orm.%3CUDIM%3E.png'
       *   Inputs:
           *   'diffuse_color_constant' [color3f]
               *   Connected: '/World/agv_2/right_swivel/Right_Swivel/materials/Looks/Robot.inputs:diffuse_color_constant' @ '/World/agv_2/right_swivel/Right_Swivel/materials/Looks/Robot'
           *   'diffuse_texture' [asset] = 'Textures/STL_Robot_albedo.%3CUDIM%3E.png'
           *   'emissive_color' [color3f]
               *   Connected: '/World/agv_2/right_swivel/Right_Swivel/materials/Looks/Robot.inputs:emissive_color' @ '/World/agv_2/right_swivel/Right_Swivel/materials/Looks/Robot'
           *   'metallic_texture_influence' [float] = '1'
           *   'normalmap_texture' [asset] = 'Textures/STL_Robot_normal.%3CUDIM%3E.png'
           *   'ORM_texture' [asset] = 'Textures/STL_Robot_orm.%3CUDIM%3E.png'
           *   'reflection_roughness_texture_influence' [float] = '1'
           *   'uv_space_index' [int]
               *   Connected: '/World/agv_2/right_swivel/Right_Swivel/materials/Looks/Robot.inputs:uv_space_index' @ '/World/agv_2/right_swivel/Right_Swivel/materials/Looks/Robot'


---


### /World/agv_2/left_caster/Inner_Left_Wheel/materials/Looks/Robot
*  **Prim路径 (Prim Path):**/World/agv_2/left_caster/Inner_Left_Wheel/materials/Looks/Robot
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/agv_2/left_caster/Inner_Left_Wheel/materials/Looks/Robot/Robot'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/agv_2/left_caster/Inner_Left_Wheel/materials/Looks/Robot/Robot'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   纹理引用 (Texture Assets):
           *   'Textures/STL_Robot_albedo.%3CUDIM%3E.png'
           *   'Textures/STL_Robot_normal.%3CUDIM%3E.png'
           *   'Textures/STL_Robot_orm.%3CUDIM%3E.png'
       *   Inputs:
           *   'diffuse_color_constant' [color3f]
               *   Connected: '/World/agv_2/left_caster/Inner_Left_Wheel/materials/Looks/Robot.inputs:diffuse_color_constant' @ '/World/agv_2/left_caster/Inner_Left_Wheel/materials/Looks/Robot'
           *   'diffuse_texture' [asset] = 'Textures/STL_Robot_albedo.%3CUDIM%3E.png'
           *   'emissive_color' [color3f]
               *   Connected: '/World/agv_2/left_caster/Inner_Left_Wheel/materials/Looks/Robot.inputs:emissive_color' @ '/World/agv_2/left_caster/Inner_Left_Wheel/materials/Looks/Robot'
           *   'metallic_texture_influence' [float] = '1'
           *   'normalmap_texture' [asset] = 'Textures/STL_Robot_normal.%3CUDIM%3E.png'
           *   'ORM_texture' [asset] = 'Textures/STL_Robot_orm.%3CUDIM%3E.png'
           *   'reflection_roughness_texture_influence' [float] = '1'
           *   'uv_space_index' [int]
               *   Connected: '/World/agv_2/left_caster/Inner_Left_Wheel/materials/Looks/Robot.inputs:uv_space_index' @ '/World/agv_2/left_caster/Inner_Left_Wheel/materials/Looks/Robot'


---


### /World/agv_2/right_caster/Inner_Right_Wheel/materials/Looks/Robot
*  **Prim路径 (Prim Path):**/World/agv_2/right_caster/Inner_Right_Wheel/materials/Looks/Robot
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/agv_2/right_caster/Inner_Right_Wheel/materials/Looks/Robot/Robot'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/agv_2/right_caster/Inner_Right_Wheel/materials/Looks/Robot/Robot'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   纹理引用 (Texture Assets):
           *   'Textures/STL_Robot_albedo.%3CUDIM%3E.png'
           *   'Textures/STL_Robot_normal.%3CUDIM%3E.png'
           *   'Textures/STL_Robot_orm.%3CUDIM%3E.png'
       *   Inputs:
           *   'diffuse_color_constant' [color3f]
               *   Connected: '/World/agv_2/right_caster/Inner_Right_Wheel/materials/Looks/Robot.inputs:diffuse_color_constant' @ '/World/agv_2/right_caster/Inner_Right_Wheel/materials/Looks/Robot'
           *   'diffuse_texture' [asset] = 'Textures/STL_Robot_albedo.%3CUDIM%3E.png'
           *   'emissive_color' [color3f]
               *   Connected: '/World/agv_2/right_caster/Inner_Right_Wheel/materials/Looks/Robot.inputs:emissive_color' @ '/World/agv_2/right_caster/Inner_Right_Wheel/materials/Looks/Robot'
           *   'metallic_texture_influence' [float] = '1'
           *   'normalmap_texture' [asset] = 'Textures/STL_Robot_normal.%3CUDIM%3E.png'
           *   'ORM_texture' [asset] = 'Textures/STL_Robot_orm.%3CUDIM%3E.png'
           *   'reflection_roughness_texture_influence' [float] = '1'
           *   'uv_space_index' [int]
               *   Connected: '/World/agv_2/right_caster/Inner_Right_Wheel/materials/Looks/Robot.inputs:uv_space_index' @ '/World/agv_2/right_caster/Inner_Right_Wheel/materials/Looks/Robot'


---


### /World/agv_2/wheel_material
*  **Prim路径 (Prim Path):**/World/agv_2/wheel_material
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'


---


### /World/agv_2/caster_material
*  **Prim路径 (Prim Path):**/World/agv_2/caster_material
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'


---


### /World/agv_3/chassis/Body/Looks/Robot
*  **Prim路径 (Prim Path):**/World/agv_3/chassis/Body/Looks/Robot
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/agv_3/chassis/Body/Looks/Robot/Robot'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/agv_3/chassis/Body/Looks/Robot/Robot'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   纹理引用 (Texture Assets):
           *   'Textures/STL_Robot_albedo.<UDIM>.png'
           *   'Textures/STL_Robot_emissive.<UDIM>.png'
           *   'Textures/STL_Robot_normal.<UDIM>.png'
           *   'Textures/STL_Robot_orm.<UDIM>.png'
       *   Inputs:
           *   'diffuse_color_constant' [color3f]
               *   Connected: '/World/agv_3/chassis/Body/Looks/Robot.inputs:diffuse_color_constant' @ '/World/agv_3/chassis/Body/Looks/Robot'
           *   'diffuse_texture' [asset] = 'Textures/STL_Robot_albedo.<UDIM>.png'
           *   'emissive_color' [color3f]
               *   Connected: '/World/agv_3/chassis/Body/Looks/Robot.inputs:emissive_color' @ '/World/agv_3/chassis/Body/Looks/Robot'
           *   'emissive_intensity' [float] = '8000'
           *   'emissive_mask_texture' [asset] = 'Textures/STL_Robot_emissive.<UDIM>.png'
           *   'metallic_texture_influence' [float] = '0.9'
           *   'normalmap_texture' [asset] = 'Textures/STL_Robot_normal.<UDIM>.png'
           *   'ORM_texture' [asset] = 'Textures/STL_Robot_orm.<UDIM>.png'
           *   'reflection_roughness_texture_influence' [float] = '1'
           *   'uv_space_index' [int]
               *   Connected: '/World/agv_3/chassis/Body/Looks/Robot.inputs:uv_space_index' @ '/World/agv_3/chassis/Body/Looks/Robot'


---


### /World/agv_3/left_wheel/Left_Wheel/Looks/Robot
*  **Prim路径 (Prim Path):**/World/agv_3/left_wheel/Left_Wheel/Looks/Robot
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/agv_3/left_wheel/Left_Wheel/Looks/Robot/Robot'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/agv_3/left_wheel/Left_Wheel/Looks/Robot/Robot'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   纹理引用 (Texture Assets):
           *   'Textures/STL_Robot_albedo.<UDIM>.png'
           *   'Textures/STL_Robot_normal.<UDIM>.png'
           *   'Textures/STL_Robot_orm.<UDIM>.png'
       *   Inputs:
           *   'diffuse_color_constant' [color3f]
               *   Connected: '/World/agv_3/left_wheel/Left_Wheel/Looks/Robot.inputs:diffuse_color_constant' @ '/World/agv_3/left_wheel/Left_Wheel/Looks/Robot'
           *   'diffuse_texture' [asset] = 'Textures/STL_Robot_albedo.<UDIM>.png'
           *   'emissive_color' [color3f]
               *   Connected: '/World/agv_3/left_wheel/Left_Wheel/Looks/Robot.inputs:emissive_color' @ '/World/agv_3/left_wheel/Left_Wheel/Looks/Robot'
           *   'metallic_texture_influence' [float] = '1'
           *   'normalmap_texture' [asset] = 'Textures/STL_Robot_normal.<UDIM>.png'
           *   'ORM_texture' [asset] = 'Textures/STL_Robot_orm.<UDIM>.png'
           *   'reflection_roughness_texture_influence' [float] = '1'
           *   'uv_space_index' [int]
               *   Connected: '/World/agv_3/left_wheel/Left_Wheel/Looks/Robot.inputs:uv_space_index' @ '/World/agv_3/left_wheel/Left_Wheel/Looks/Robot'


---


### /World/agv_3/right_wheel/Right_Wheel/Looks/Robot
*  **Prim路径 (Prim Path):**/World/agv_3/right_wheel/Right_Wheel/Looks/Robot
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/agv_3/right_wheel/Right_Wheel/Looks/Robot/Robot'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/agv_3/right_wheel/Right_Wheel/Looks/Robot/Robot'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   纹理引用 (Texture Assets):
           *   'Textures/STL_Robot_albedo.<UDIM>.png'
           *   'Textures/STL_Robot_normal.<UDIM>.png'
           *   'Textures/STL_Robot_orm.<UDIM>.png'
       *   Inputs:
           *   'diffuse_color_constant' [color3f]
               *   Connected: '/World/agv_3/right_wheel/Right_Wheel/Looks/Robot.inputs:diffuse_color_constant' @ '/World/agv_3/right_wheel/Right_Wheel/Looks/Robot'
           *   'diffuse_texture' [asset] = 'Textures/STL_Robot_albedo.<UDIM>.png'
           *   'emissive_color' [color3f]
               *   Connected: '/World/agv_3/right_wheel/Right_Wheel/Looks/Robot.inputs:emissive_color' @ '/World/agv_3/right_wheel/Right_Wheel/Looks/Robot'
           *   'metallic_texture_influence' [float] = '1'
           *   'normalmap_texture' [asset] = 'Textures/STL_Robot_normal.<UDIM>.png'
           *   'ORM_texture' [asset] = 'Textures/STL_Robot_orm.<UDIM>.png'
           *   'reflection_roughness_texture_influence' [float] = '1'
           *   'uv_space_index' [int]
               *   Connected: '/World/agv_3/right_wheel/Right_Wheel/Looks/Robot.inputs:uv_space_index' @ '/World/agv_3/right_wheel/Right_Wheel/Looks/Robot'


---


### /World/agv_3/lift/Lift/Looks/Robot
*  **Prim路径 (Prim Path):**/World/agv_3/lift/Lift/Looks/Robot
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/agv_3/lift/Lift/Looks/Robot/Robot'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/agv_3/lift/Lift/Looks/Robot/Robot'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   纹理引用 (Texture Assets):
           *   'Textures/STL_Robot_albedo.<UDIM>.png'
           *   'Textures/STL_Robot_normal.<UDIM>.png'
           *   'Textures/STL_Robot_orm.<UDIM>.png'
       *   Inputs:
           *   'diffuse_color_constant' [color3f]
               *   Connected: '/World/agv_3/lift/Lift/Looks/Robot.inputs:diffuse_color_constant' @ '/World/agv_3/lift/Lift/Looks/Robot'
           *   'diffuse_texture' [asset] = 'Textures/STL_Robot_albedo.<UDIM>.png'
           *   'emissive_color' [color3f]
               *   Connected: '/World/agv_3/lift/Lift/Looks/Robot.inputs:emissive_color' @ '/World/agv_3/lift/Lift/Looks/Robot'
           *   'metallic_texture_influence' [float] = '0.901'
           *   'normalmap_texture' [asset] = 'Textures/STL_Robot_normal.<UDIM>.png'
           *   'ORM_texture' [asset] = 'Textures/STL_Robot_orm.<UDIM>.png'
           *   'reflection_roughness_texture_influence' [float] = '1'
           *   'uv_space_index' [int]
               *   Connected: '/World/agv_3/lift/Lift/Looks/Robot.inputs:uv_space_index' @ '/World/agv_3/lift/Lift/Looks/Robot'


---


### /World/agv_3/left_swivel/Left_Swivel/materials/Looks/Robot
*  **Prim路径 (Prim Path):**/World/agv_3/left_swivel/Left_Swivel/materials/Looks/Robot
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/agv_3/left_swivel/Left_Swivel/materials/Looks/Robot/Robot'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/agv_3/left_swivel/Left_Swivel/materials/Looks/Robot/Robot'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   纹理引用 (Texture Assets):
           *   'Textures/STL_Robot_albedo.%3CUDIM%3E.png'
           *   'Textures/STL_Robot_normal.%3CUDIM%3E.png'
           *   'Textures/STL_Robot_orm.%3CUDIM%3E.png'
       *   Inputs:
           *   'diffuse_color_constant' [color3f]
               *   Connected: '/World/agv_3/left_swivel/Left_Swivel/materials/Looks/Robot.inputs:diffuse_color_constant' @ '/World/agv_3/left_swivel/Left_Swivel/materials/Looks/Robot'
           *   'diffuse_texture' [asset] = 'Textures/STL_Robot_albedo.%3CUDIM%3E.png'
           *   'emissive_color' [color3f]
               *   Connected: '/World/agv_3/left_swivel/Left_Swivel/materials/Looks/Robot.inputs:emissive_color' @ '/World/agv_3/left_swivel/Left_Swivel/materials/Looks/Robot'
           *   'metallic_texture_influence' [float] = '1'
           *   'normalmap_texture' [asset] = 'Textures/STL_Robot_normal.%3CUDIM%3E.png'
           *   'ORM_texture' [asset] = 'Textures/STL_Robot_orm.%3CUDIM%3E.png'
           *   'reflection_roughness_texture_influence' [float] = '1'
           *   'uv_space_index' [int]
               *   Connected: '/World/agv_3/left_swivel/Left_Swivel/materials/Looks/Robot.inputs:uv_space_index' @ '/World/agv_3/left_swivel/Left_Swivel/materials/Looks/Robot'


---


### /World/agv_3/right_swivel/Right_Swivel/materials/Looks/Robot
*  **Prim路径 (Prim Path):**/World/agv_3/right_swivel/Right_Swivel/materials/Looks/Robot
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/agv_3/right_swivel/Right_Swivel/materials/Looks/Robot/Robot'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/agv_3/right_swivel/Right_Swivel/materials/Looks/Robot/Robot'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   纹理引用 (Texture Assets):
           *   'Textures/STL_Robot_albedo.%3CUDIM%3E.png'
           *   'Textures/STL_Robot_normal.%3CUDIM%3E.png'
           *   'Textures/STL_Robot_orm.%3CUDIM%3E.png'
       *   Inputs:
           *   'diffuse_color_constant' [color3f]
               *   Connected: '/World/agv_3/right_swivel/Right_Swivel/materials/Looks/Robot.inputs:diffuse_color_constant' @ '/World/agv_3/right_swivel/Right_Swivel/materials/Looks/Robot'
           *   'diffuse_texture' [asset] = 'Textures/STL_Robot_albedo.%3CUDIM%3E.png'
           *   'emissive_color' [color3f]
               *   Connected: '/World/agv_3/right_swivel/Right_Swivel/materials/Looks/Robot.inputs:emissive_color' @ '/World/agv_3/right_swivel/Right_Swivel/materials/Looks/Robot'
           *   'metallic_texture_influence' [float] = '1'
           *   'normalmap_texture' [asset] = 'Textures/STL_Robot_normal.%3CUDIM%3E.png'
           *   'ORM_texture' [asset] = 'Textures/STL_Robot_orm.%3CUDIM%3E.png'
           *   'reflection_roughness_texture_influence' [float] = '1'
           *   'uv_space_index' [int]
               *   Connected: '/World/agv_3/right_swivel/Right_Swivel/materials/Looks/Robot.inputs:uv_space_index' @ '/World/agv_3/right_swivel/Right_Swivel/materials/Looks/Robot'


---


### /World/agv_3/left_caster/Inner_Left_Wheel/materials/Looks/Robot
*  **Prim路径 (Prim Path):**/World/agv_3/left_caster/Inner_Left_Wheel/materials/Looks/Robot
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/agv_3/left_caster/Inner_Left_Wheel/materials/Looks/Robot/Robot'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/agv_3/left_caster/Inner_Left_Wheel/materials/Looks/Robot/Robot'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   纹理引用 (Texture Assets):
           *   'Textures/STL_Robot_albedo.%3CUDIM%3E.png'
           *   'Textures/STL_Robot_normal.%3CUDIM%3E.png'
           *   'Textures/STL_Robot_orm.%3CUDIM%3E.png'
       *   Inputs:
           *   'diffuse_color_constant' [color3f]
               *   Connected: '/World/agv_3/left_caster/Inner_Left_Wheel/materials/Looks/Robot.inputs:diffuse_color_constant' @ '/World/agv_3/left_caster/Inner_Left_Wheel/materials/Looks/Robot'
           *   'diffuse_texture' [asset] = 'Textures/STL_Robot_albedo.%3CUDIM%3E.png'
           *   'emissive_color' [color3f]
               *   Connected: '/World/agv_3/left_caster/Inner_Left_Wheel/materials/Looks/Robot.inputs:emissive_color' @ '/World/agv_3/left_caster/Inner_Left_Wheel/materials/Looks/Robot'
           *   'metallic_texture_influence' [float] = '1'
           *   'normalmap_texture' [asset] = 'Textures/STL_Robot_normal.%3CUDIM%3E.png'
           *   'ORM_texture' [asset] = 'Textures/STL_Robot_orm.%3CUDIM%3E.png'
           *   'reflection_roughness_texture_influence' [float] = '1'
           *   'uv_space_index' [int]
               *   Connected: '/World/agv_3/left_caster/Inner_Left_Wheel/materials/Looks/Robot.inputs:uv_space_index' @ '/World/agv_3/left_caster/Inner_Left_Wheel/materials/Looks/Robot'


---


### /World/agv_3/right_caster/Inner_Right_Wheel/materials/Looks/Robot
*  **Prim路径 (Prim Path):**/World/agv_3/right_caster/Inner_Right_Wheel/materials/Looks/Robot
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/agv_3/right_caster/Inner_Right_Wheel/materials/Looks/Robot/Robot'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/agv_3/right_caster/Inner_Right_Wheel/materials/Looks/Robot/Robot'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   纹理引用 (Texture Assets):
           *   'Textures/STL_Robot_albedo.%3CUDIM%3E.png'
           *   'Textures/STL_Robot_normal.%3CUDIM%3E.png'
           *   'Textures/STL_Robot_orm.%3CUDIM%3E.png'
       *   Inputs:
           *   'diffuse_color_constant' [color3f]
               *   Connected: '/World/agv_3/right_caster/Inner_Right_Wheel/materials/Looks/Robot.inputs:diffuse_color_constant' @ '/World/agv_3/right_caster/Inner_Right_Wheel/materials/Looks/Robot'
           *   'diffuse_texture' [asset] = 'Textures/STL_Robot_albedo.%3CUDIM%3E.png'
           *   'emissive_color' [color3f]
               *   Connected: '/World/agv_3/right_caster/Inner_Right_Wheel/materials/Looks/Robot.inputs:emissive_color' @ '/World/agv_3/right_caster/Inner_Right_Wheel/materials/Looks/Robot'
           *   'metallic_texture_influence' [float] = '1'
           *   'normalmap_texture' [asset] = 'Textures/STL_Robot_normal.%3CUDIM%3E.png'
           *   'ORM_texture' [asset] = 'Textures/STL_Robot_orm.%3CUDIM%3E.png'
           *   'reflection_roughness_texture_influence' [float] = '1'
           *   'uv_space_index' [int]
               *   Connected: '/World/agv_3/right_caster/Inner_Right_Wheel/materials/Looks/Robot.inputs:uv_space_index' @ '/World/agv_3/right_caster/Inner_Right_Wheel/materials/Looks/Robot'


---


### /World/agv_3/wheel_material
*  **Prim路径 (Prim Path):**/World/agv_3/wheel_material
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'


---


### /World/agv_3/caster_material
*  **Prim路径 (Prim Path):**/World/agv_3/caster_material
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'


---


### /World/agv_4/chassis/Body/Looks/Robot
*  **Prim路径 (Prim Path):**/World/agv_4/chassis/Body/Looks/Robot
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/agv_4/chassis/Body/Looks/Robot/Robot'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/agv_4/chassis/Body/Looks/Robot/Robot'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   纹理引用 (Texture Assets):
           *   'Textures/STL_Robot_albedo.<UDIM>.png'
           *   'Textures/STL_Robot_emissive.<UDIM>.png'
           *   'Textures/STL_Robot_normal.<UDIM>.png'
           *   'Textures/STL_Robot_orm.<UDIM>.png'
       *   Inputs:
           *   'diffuse_color_constant' [color3f]
               *   Connected: '/World/agv_4/chassis/Body/Looks/Robot.inputs:diffuse_color_constant' @ '/World/agv_4/chassis/Body/Looks/Robot'
           *   'diffuse_texture' [asset] = 'Textures/STL_Robot_albedo.<UDIM>.png'
           *   'emissive_color' [color3f]
               *   Connected: '/World/agv_4/chassis/Body/Looks/Robot.inputs:emissive_color' @ '/World/agv_4/chassis/Body/Looks/Robot'
           *   'emissive_intensity' [float] = '8000'
           *   'emissive_mask_texture' [asset] = 'Textures/STL_Robot_emissive.<UDIM>.png'
           *   'metallic_texture_influence' [float] = '0.9'
           *   'normalmap_texture' [asset] = 'Textures/STL_Robot_normal.<UDIM>.png'
           *   'ORM_texture' [asset] = 'Textures/STL_Robot_orm.<UDIM>.png'
           *   'reflection_roughness_texture_influence' [float] = '1'
           *   'uv_space_index' [int]
               *   Connected: '/World/agv_4/chassis/Body/Looks/Robot.inputs:uv_space_index' @ '/World/agv_4/chassis/Body/Looks/Robot'


---


### /World/agv_4/left_wheel/Left_Wheel/Looks/Robot
*  **Prim路径 (Prim Path):**/World/agv_4/left_wheel/Left_Wheel/Looks/Robot
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/agv_4/left_wheel/Left_Wheel/Looks/Robot/Robot'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/agv_4/left_wheel/Left_Wheel/Looks/Robot/Robot'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   纹理引用 (Texture Assets):
           *   'Textures/STL_Robot_albedo.<UDIM>.png'
           *   'Textures/STL_Robot_normal.<UDIM>.png'
           *   'Textures/STL_Robot_orm.<UDIM>.png'
       *   Inputs:
           *   'diffuse_color_constant' [color3f]
               *   Connected: '/World/agv_4/left_wheel/Left_Wheel/Looks/Robot.inputs:diffuse_color_constant' @ '/World/agv_4/left_wheel/Left_Wheel/Looks/Robot'
           *   'diffuse_texture' [asset] = 'Textures/STL_Robot_albedo.<UDIM>.png'
           *   'emissive_color' [color3f]
               *   Connected: '/World/agv_4/left_wheel/Left_Wheel/Looks/Robot.inputs:emissive_color' @ '/World/agv_4/left_wheel/Left_Wheel/Looks/Robot'
           *   'metallic_texture_influence' [float] = '1'
           *   'normalmap_texture' [asset] = 'Textures/STL_Robot_normal.<UDIM>.png'
           *   'ORM_texture' [asset] = 'Textures/STL_Robot_orm.<UDIM>.png'
           *   'reflection_roughness_texture_influence' [float] = '1'
           *   'uv_space_index' [int]
               *   Connected: '/World/agv_4/left_wheel/Left_Wheel/Looks/Robot.inputs:uv_space_index' @ '/World/agv_4/left_wheel/Left_Wheel/Looks/Robot'


---


### /World/agv_4/right_wheel/Right_Wheel/Looks/Robot
*  **Prim路径 (Prim Path):**/World/agv_4/right_wheel/Right_Wheel/Looks/Robot
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/agv_4/right_wheel/Right_Wheel/Looks/Robot/Robot'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/agv_4/right_wheel/Right_Wheel/Looks/Robot/Robot'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   纹理引用 (Texture Assets):
           *   'Textures/STL_Robot_albedo.<UDIM>.png'
           *   'Textures/STL_Robot_normal.<UDIM>.png'
           *   'Textures/STL_Robot_orm.<UDIM>.png'
       *   Inputs:
           *   'diffuse_color_constant' [color3f]
               *   Connected: '/World/agv_4/right_wheel/Right_Wheel/Looks/Robot.inputs:diffuse_color_constant' @ '/World/agv_4/right_wheel/Right_Wheel/Looks/Robot'
           *   'diffuse_texture' [asset] = 'Textures/STL_Robot_albedo.<UDIM>.png'
           *   'emissive_color' [color3f]
               *   Connected: '/World/agv_4/right_wheel/Right_Wheel/Looks/Robot.inputs:emissive_color' @ '/World/agv_4/right_wheel/Right_Wheel/Looks/Robot'
           *   'metallic_texture_influence' [float] = '1'
           *   'normalmap_texture' [asset] = 'Textures/STL_Robot_normal.<UDIM>.png'
           *   'ORM_texture' [asset] = 'Textures/STL_Robot_orm.<UDIM>.png'
           *   'reflection_roughness_texture_influence' [float] = '1'
           *   'uv_space_index' [int]
               *   Connected: '/World/agv_4/right_wheel/Right_Wheel/Looks/Robot.inputs:uv_space_index' @ '/World/agv_4/right_wheel/Right_Wheel/Looks/Robot'


---


### /World/agv_4/lift/Lift/Looks/Robot
*  **Prim路径 (Prim Path):**/World/agv_4/lift/Lift/Looks/Robot
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/agv_4/lift/Lift/Looks/Robot/Robot'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/agv_4/lift/Lift/Looks/Robot/Robot'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   纹理引用 (Texture Assets):
           *   'Textures/STL_Robot_albedo.<UDIM>.png'
           *   'Textures/STL_Robot_normal.<UDIM>.png'
           *   'Textures/STL_Robot_orm.<UDIM>.png'
       *   Inputs:
           *   'diffuse_color_constant' [color3f]
               *   Connected: '/World/agv_4/lift/Lift/Looks/Robot.inputs:diffuse_color_constant' @ '/World/agv_4/lift/Lift/Looks/Robot'
           *   'diffuse_texture' [asset] = 'Textures/STL_Robot_albedo.<UDIM>.png'
           *   'emissive_color' [color3f]
               *   Connected: '/World/agv_4/lift/Lift/Looks/Robot.inputs:emissive_color' @ '/World/agv_4/lift/Lift/Looks/Robot'
           *   'metallic_texture_influence' [float] = '0.901'
           *   'normalmap_texture' [asset] = 'Textures/STL_Robot_normal.<UDIM>.png'
           *   'ORM_texture' [asset] = 'Textures/STL_Robot_orm.<UDIM>.png'
           *   'reflection_roughness_texture_influence' [float] = '1'
           *   'uv_space_index' [int]
               *   Connected: '/World/agv_4/lift/Lift/Looks/Robot.inputs:uv_space_index' @ '/World/agv_4/lift/Lift/Looks/Robot'


---


### /World/agv_4/left_swivel/Left_Swivel/materials/Looks/Robot
*  **Prim路径 (Prim Path):**/World/agv_4/left_swivel/Left_Swivel/materials/Looks/Robot
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/agv_4/left_swivel/Left_Swivel/materials/Looks/Robot/Robot'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/agv_4/left_swivel/Left_Swivel/materials/Looks/Robot/Robot'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   纹理引用 (Texture Assets):
           *   'Textures/STL_Robot_albedo.%3CUDIM%3E.png'
           *   'Textures/STL_Robot_normal.%3CUDIM%3E.png'
           *   'Textures/STL_Robot_orm.%3CUDIM%3E.png'
       *   Inputs:
           *   'diffuse_color_constant' [color3f]
               *   Connected: '/World/agv_4/left_swivel/Left_Swivel/materials/Looks/Robot.inputs:diffuse_color_constant' @ '/World/agv_4/left_swivel/Left_Swivel/materials/Looks/Robot'
           *   'diffuse_texture' [asset] = 'Textures/STL_Robot_albedo.%3CUDIM%3E.png'
           *   'emissive_color' [color3f]
               *   Connected: '/World/agv_4/left_swivel/Left_Swivel/materials/Looks/Robot.inputs:emissive_color' @ '/World/agv_4/left_swivel/Left_Swivel/materials/Looks/Robot'
           *   'metallic_texture_influence' [float] = '1'
           *   'normalmap_texture' [asset] = 'Textures/STL_Robot_normal.%3CUDIM%3E.png'
           *   'ORM_texture' [asset] = 'Textures/STL_Robot_orm.%3CUDIM%3E.png'
           *   'reflection_roughness_texture_influence' [float] = '1'
           *   'uv_space_index' [int]
               *   Connected: '/World/agv_4/left_swivel/Left_Swivel/materials/Looks/Robot.inputs:uv_space_index' @ '/World/agv_4/left_swivel/Left_Swivel/materials/Looks/Robot'


---


### /World/agv_4/right_swivel/Right_Swivel/materials/Looks/Robot
*  **Prim路径 (Prim Path):**/World/agv_4/right_swivel/Right_Swivel/materials/Looks/Robot
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/agv_4/right_swivel/Right_Swivel/materials/Looks/Robot/Robot'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/agv_4/right_swivel/Right_Swivel/materials/Looks/Robot/Robot'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   纹理引用 (Texture Assets):
           *   'Textures/STL_Robot_albedo.%3CUDIM%3E.png'
           *   'Textures/STL_Robot_normal.%3CUDIM%3E.png'
           *   'Textures/STL_Robot_orm.%3CUDIM%3E.png'
       *   Inputs:
           *   'diffuse_color_constant' [color3f]
               *   Connected: '/World/agv_4/right_swivel/Right_Swivel/materials/Looks/Robot.inputs:diffuse_color_constant' @ '/World/agv_4/right_swivel/Right_Swivel/materials/Looks/Robot'
           *   'diffuse_texture' [asset] = 'Textures/STL_Robot_albedo.%3CUDIM%3E.png'
           *   'emissive_color' [color3f]
               *   Connected: '/World/agv_4/right_swivel/Right_Swivel/materials/Looks/Robot.inputs:emissive_color' @ '/World/agv_4/right_swivel/Right_Swivel/materials/Looks/Robot'
           *   'metallic_texture_influence' [float] = '1'
           *   'normalmap_texture' [asset] = 'Textures/STL_Robot_normal.%3CUDIM%3E.png'
           *   'ORM_texture' [asset] = 'Textures/STL_Robot_orm.%3CUDIM%3E.png'
           *   'reflection_roughness_texture_influence' [float] = '1'
           *   'uv_space_index' [int]
               *   Connected: '/World/agv_4/right_swivel/Right_Swivel/materials/Looks/Robot.inputs:uv_space_index' @ '/World/agv_4/right_swivel/Right_Swivel/materials/Looks/Robot'


---


### /World/agv_4/left_caster/Inner_Left_Wheel/materials/Looks/Robot
*  **Prim路径 (Prim Path):**/World/agv_4/left_caster/Inner_Left_Wheel/materials/Looks/Robot
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/agv_4/left_caster/Inner_Left_Wheel/materials/Looks/Robot/Robot'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/agv_4/left_caster/Inner_Left_Wheel/materials/Looks/Robot/Robot'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   纹理引用 (Texture Assets):
           *   'Textures/STL_Robot_albedo.%3CUDIM%3E.png'
           *   'Textures/STL_Robot_normal.%3CUDIM%3E.png'
           *   'Textures/STL_Robot_orm.%3CUDIM%3E.png'
       *   Inputs:
           *   'diffuse_color_constant' [color3f]
               *   Connected: '/World/agv_4/left_caster/Inner_Left_Wheel/materials/Looks/Robot.inputs:diffuse_color_constant' @ '/World/agv_4/left_caster/Inner_Left_Wheel/materials/Looks/Robot'
           *   'diffuse_texture' [asset] = 'Textures/STL_Robot_albedo.%3CUDIM%3E.png'
           *   'emissive_color' [color3f]
               *   Connected: '/World/agv_4/left_caster/Inner_Left_Wheel/materials/Looks/Robot.inputs:emissive_color' @ '/World/agv_4/left_caster/Inner_Left_Wheel/materials/Looks/Robot'
           *   'metallic_texture_influence' [float] = '1'
           *   'normalmap_texture' [asset] = 'Textures/STL_Robot_normal.%3CUDIM%3E.png'
           *   'ORM_texture' [asset] = 'Textures/STL_Robot_orm.%3CUDIM%3E.png'
           *   'reflection_roughness_texture_influence' [float] = '1'
           *   'uv_space_index' [int]
               *   Connected: '/World/agv_4/left_caster/Inner_Left_Wheel/materials/Looks/Robot.inputs:uv_space_index' @ '/World/agv_4/left_caster/Inner_Left_Wheel/materials/Looks/Robot'


---


### /World/agv_4/right_caster/Inner_Right_Wheel/materials/Looks/Robot
*  **Prim路径 (Prim Path):**/World/agv_4/right_caster/Inner_Right_Wheel/materials/Looks/Robot
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/agv_4/right_caster/Inner_Right_Wheel/materials/Looks/Robot/Robot'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/agv_4/right_caster/Inner_Right_Wheel/materials/Looks/Robot/Robot'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   纹理引用 (Texture Assets):
           *   'Textures/STL_Robot_albedo.%3CUDIM%3E.png'
           *   'Textures/STL_Robot_normal.%3CUDIM%3E.png'
           *   'Textures/STL_Robot_orm.%3CUDIM%3E.png'
       *   Inputs:
           *   'diffuse_color_constant' [color3f]
               *   Connected: '/World/agv_4/right_caster/Inner_Right_Wheel/materials/Looks/Robot.inputs:diffuse_color_constant' @ '/World/agv_4/right_caster/Inner_Right_Wheel/materials/Looks/Robot'
           *   'diffuse_texture' [asset] = 'Textures/STL_Robot_albedo.%3CUDIM%3E.png'
           *   'emissive_color' [color3f]
               *   Connected: '/World/agv_4/right_caster/Inner_Right_Wheel/materials/Looks/Robot.inputs:emissive_color' @ '/World/agv_4/right_caster/Inner_Right_Wheel/materials/Looks/Robot'
           *   'metallic_texture_influence' [float] = '1'
           *   'normalmap_texture' [asset] = 'Textures/STL_Robot_normal.%3CUDIM%3E.png'
           *   'ORM_texture' [asset] = 'Textures/STL_Robot_orm.%3CUDIM%3E.png'
           *   'reflection_roughness_texture_influence' [float] = '1'
           *   'uv_space_index' [int]
               *   Connected: '/World/agv_4/right_caster/Inner_Right_Wheel/materials/Looks/Robot.inputs:uv_space_index' @ '/World/agv_4/right_caster/Inner_Right_Wheel/materials/Looks/Robot'


---


### /World/agv_4/wheel_material
*  **Prim路径 (Prim Path):**/World/agv_4/wheel_material
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'


---


### /World/agv_4/caster_material
*  **Prim路径 (Prim Path):**/World/agv_4/caster_material
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'


---


### /World/agv_5/chassis/Body/Looks/Robot
*  **Prim路径 (Prim Path):**/World/agv_5/chassis/Body/Looks/Robot
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/agv_5/chassis/Body/Looks/Robot/Robot'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/agv_5/chassis/Body/Looks/Robot/Robot'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   纹理引用 (Texture Assets):
           *   'Textures/STL_Robot_albedo.<UDIM>.png'
           *   'Textures/STL_Robot_emissive.<UDIM>.png'
           *   'Textures/STL_Robot_normal.<UDIM>.png'
           *   'Textures/STL_Robot_orm.<UDIM>.png'
       *   Inputs:
           *   'diffuse_color_constant' [color3f]
               *   Connected: '/World/agv_5/chassis/Body/Looks/Robot.inputs:diffuse_color_constant' @ '/World/agv_5/chassis/Body/Looks/Robot'
           *   'diffuse_texture' [asset] = 'Textures/STL_Robot_albedo.<UDIM>.png'
           *   'emissive_color' [color3f]
               *   Connected: '/World/agv_5/chassis/Body/Looks/Robot.inputs:emissive_color' @ '/World/agv_5/chassis/Body/Looks/Robot'
           *   'emissive_intensity' [float] = '8000'
           *   'emissive_mask_texture' [asset] = 'Textures/STL_Robot_emissive.<UDIM>.png'
           *   'metallic_texture_influence' [float] = '0.9'
           *   'normalmap_texture' [asset] = 'Textures/STL_Robot_normal.<UDIM>.png'
           *   'ORM_texture' [asset] = 'Textures/STL_Robot_orm.<UDIM>.png'
           *   'reflection_roughness_texture_influence' [float] = '1'
           *   'uv_space_index' [int]
               *   Connected: '/World/agv_5/chassis/Body/Looks/Robot.inputs:uv_space_index' @ '/World/agv_5/chassis/Body/Looks/Robot'


---


### /World/agv_5/left_wheel/Left_Wheel/Looks/Robot
*  **Prim路径 (Prim Path):**/World/agv_5/left_wheel/Left_Wheel/Looks/Robot
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/agv_5/left_wheel/Left_Wheel/Looks/Robot/Robot'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/agv_5/left_wheel/Left_Wheel/Looks/Robot/Robot'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   纹理引用 (Texture Assets):
           *   'Textures/STL_Robot_albedo.<UDIM>.png'
           *   'Textures/STL_Robot_normal.<UDIM>.png'
           *   'Textures/STL_Robot_orm.<UDIM>.png'
       *   Inputs:
           *   'diffuse_color_constant' [color3f]
               *   Connected: '/World/agv_5/left_wheel/Left_Wheel/Looks/Robot.inputs:diffuse_color_constant' @ '/World/agv_5/left_wheel/Left_Wheel/Looks/Robot'
           *   'diffuse_texture' [asset] = 'Textures/STL_Robot_albedo.<UDIM>.png'
           *   'emissive_color' [color3f]
               *   Connected: '/World/agv_5/left_wheel/Left_Wheel/Looks/Robot.inputs:emissive_color' @ '/World/agv_5/left_wheel/Left_Wheel/Looks/Robot'
           *   'metallic_texture_influence' [float] = '1'
           *   'normalmap_texture' [asset] = 'Textures/STL_Robot_normal.<UDIM>.png'
           *   'ORM_texture' [asset] = 'Textures/STL_Robot_orm.<UDIM>.png'
           *   'reflection_roughness_texture_influence' [float] = '1'
           *   'uv_space_index' [int]
               *   Connected: '/World/agv_5/left_wheel/Left_Wheel/Looks/Robot.inputs:uv_space_index' @ '/World/agv_5/left_wheel/Left_Wheel/Looks/Robot'


---


### /World/agv_5/right_wheel/Right_Wheel/Looks/Robot
*  **Prim路径 (Prim Path):**/World/agv_5/right_wheel/Right_Wheel/Looks/Robot
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/agv_5/right_wheel/Right_Wheel/Looks/Robot/Robot'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/agv_5/right_wheel/Right_Wheel/Looks/Robot/Robot'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   纹理引用 (Texture Assets):
           *   'Textures/STL_Robot_albedo.<UDIM>.png'
           *   'Textures/STL_Robot_normal.<UDIM>.png'
           *   'Textures/STL_Robot_orm.<UDIM>.png'
       *   Inputs:
           *   'diffuse_color_constant' [color3f]
               *   Connected: '/World/agv_5/right_wheel/Right_Wheel/Looks/Robot.inputs:diffuse_color_constant' @ '/World/agv_5/right_wheel/Right_Wheel/Looks/Robot'
           *   'diffuse_texture' [asset] = 'Textures/STL_Robot_albedo.<UDIM>.png'
           *   'emissive_color' [color3f]
               *   Connected: '/World/agv_5/right_wheel/Right_Wheel/Looks/Robot.inputs:emissive_color' @ '/World/agv_5/right_wheel/Right_Wheel/Looks/Robot'
           *   'metallic_texture_influence' [float] = '1'
           *   'normalmap_texture' [asset] = 'Textures/STL_Robot_normal.<UDIM>.png'
           *   'ORM_texture' [asset] = 'Textures/STL_Robot_orm.<UDIM>.png'
           *   'reflection_roughness_texture_influence' [float] = '1'
           *   'uv_space_index' [int]
               *   Connected: '/World/agv_5/right_wheel/Right_Wheel/Looks/Robot.inputs:uv_space_index' @ '/World/agv_5/right_wheel/Right_Wheel/Looks/Robot'


---


### /World/agv_5/lift/Lift/Looks/Robot
*  **Prim路径 (Prim Path):**/World/agv_5/lift/Lift/Looks/Robot
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/agv_5/lift/Lift/Looks/Robot/Robot'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/agv_5/lift/Lift/Looks/Robot/Robot'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   纹理引用 (Texture Assets):
           *   'Textures/STL_Robot_albedo.<UDIM>.png'
           *   'Textures/STL_Robot_normal.<UDIM>.png'
           *   'Textures/STL_Robot_orm.<UDIM>.png'
       *   Inputs:
           *   'diffuse_color_constant' [color3f]
               *   Connected: '/World/agv_5/lift/Lift/Looks/Robot.inputs:diffuse_color_constant' @ '/World/agv_5/lift/Lift/Looks/Robot'
           *   'diffuse_texture' [asset] = 'Textures/STL_Robot_albedo.<UDIM>.png'
           *   'emissive_color' [color3f]
               *   Connected: '/World/agv_5/lift/Lift/Looks/Robot.inputs:emissive_color' @ '/World/agv_5/lift/Lift/Looks/Robot'
           *   'metallic_texture_influence' [float] = '0.901'
           *   'normalmap_texture' [asset] = 'Textures/STL_Robot_normal.<UDIM>.png'
           *   'ORM_texture' [asset] = 'Textures/STL_Robot_orm.<UDIM>.png'
           *   'reflection_roughness_texture_influence' [float] = '1'
           *   'uv_space_index' [int]
               *   Connected: '/World/agv_5/lift/Lift/Looks/Robot.inputs:uv_space_index' @ '/World/agv_5/lift/Lift/Looks/Robot'


---


### /World/agv_5/left_swivel/Left_Swivel/materials/Looks/Robot
*  **Prim路径 (Prim Path):**/World/agv_5/left_swivel/Left_Swivel/materials/Looks/Robot
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/agv_5/left_swivel/Left_Swivel/materials/Looks/Robot/Robot'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/agv_5/left_swivel/Left_Swivel/materials/Looks/Robot/Robot'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   纹理引用 (Texture Assets):
           *   'Textures/STL_Robot_albedo.%3CUDIM%3E.png'
           *   'Textures/STL_Robot_normal.%3CUDIM%3E.png'
           *   'Textures/STL_Robot_orm.%3CUDIM%3E.png'
       *   Inputs:
           *   'diffuse_color_constant' [color3f]
               *   Connected: '/World/agv_5/left_swivel/Left_Swivel/materials/Looks/Robot.inputs:diffuse_color_constant' @ '/World/agv_5/left_swivel/Left_Swivel/materials/Looks/Robot'
           *   'diffuse_texture' [asset] = 'Textures/STL_Robot_albedo.%3CUDIM%3E.png'
           *   'emissive_color' [color3f]
               *   Connected: '/World/agv_5/left_swivel/Left_Swivel/materials/Looks/Robot.inputs:emissive_color' @ '/World/agv_5/left_swivel/Left_Swivel/materials/Looks/Robot'
           *   'metallic_texture_influence' [float] = '1'
           *   'normalmap_texture' [asset] = 'Textures/STL_Robot_normal.%3CUDIM%3E.png'
           *   'ORM_texture' [asset] = 'Textures/STL_Robot_orm.%3CUDIM%3E.png'
           *   'reflection_roughness_texture_influence' [float] = '1'
           *   'uv_space_index' [int]
               *   Connected: '/World/agv_5/left_swivel/Left_Swivel/materials/Looks/Robot.inputs:uv_space_index' @ '/World/agv_5/left_swivel/Left_Swivel/materials/Looks/Robot'


---


### /World/agv_5/right_swivel/Right_Swivel/materials/Looks/Robot
*  **Prim路径 (Prim Path):**/World/agv_5/right_swivel/Right_Swivel/materials/Looks/Robot
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/agv_5/right_swivel/Right_Swivel/materials/Looks/Robot/Robot'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/agv_5/right_swivel/Right_Swivel/materials/Looks/Robot/Robot'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   纹理引用 (Texture Assets):
           *   'Textures/STL_Robot_albedo.%3CUDIM%3E.png'
           *   'Textures/STL_Robot_normal.%3CUDIM%3E.png'
           *   'Textures/STL_Robot_orm.%3CUDIM%3E.png'
       *   Inputs:
           *   'diffuse_color_constant' [color3f]
               *   Connected: '/World/agv_5/right_swivel/Right_Swivel/materials/Looks/Robot.inputs:diffuse_color_constant' @ '/World/agv_5/right_swivel/Right_Swivel/materials/Looks/Robot'
           *   'diffuse_texture' [asset] = 'Textures/STL_Robot_albedo.%3CUDIM%3E.png'
           *   'emissive_color' [color3f]
               *   Connected: '/World/agv_5/right_swivel/Right_Swivel/materials/Looks/Robot.inputs:emissive_color' @ '/World/agv_5/right_swivel/Right_Swivel/materials/Looks/Robot'
           *   'metallic_texture_influence' [float] = '1'
           *   'normalmap_texture' [asset] = 'Textures/STL_Robot_normal.%3CUDIM%3E.png'
           *   'ORM_texture' [asset] = 'Textures/STL_Robot_orm.%3CUDIM%3E.png'
           *   'reflection_roughness_texture_influence' [float] = '1'
           *   'uv_space_index' [int]
               *   Connected: '/World/agv_5/right_swivel/Right_Swivel/materials/Looks/Robot.inputs:uv_space_index' @ '/World/agv_5/right_swivel/Right_Swivel/materials/Looks/Robot'


---


### /World/agv_5/left_caster/Inner_Left_Wheel/materials/Looks/Robot
*  **Prim路径 (Prim Path):**/World/agv_5/left_caster/Inner_Left_Wheel/materials/Looks/Robot
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/agv_5/left_caster/Inner_Left_Wheel/materials/Looks/Robot/Robot'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/agv_5/left_caster/Inner_Left_Wheel/materials/Looks/Robot/Robot'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   纹理引用 (Texture Assets):
           *   'Textures/STL_Robot_albedo.%3CUDIM%3E.png'
           *   'Textures/STL_Robot_normal.%3CUDIM%3E.png'
           *   'Textures/STL_Robot_orm.%3CUDIM%3E.png'
       *   Inputs:
           *   'diffuse_color_constant' [color3f]
               *   Connected: '/World/agv_5/left_caster/Inner_Left_Wheel/materials/Looks/Robot.inputs:diffuse_color_constant' @ '/World/agv_5/left_caster/Inner_Left_Wheel/materials/Looks/Robot'
           *   'diffuse_texture' [asset] = 'Textures/STL_Robot_albedo.%3CUDIM%3E.png'
           *   'emissive_color' [color3f]
               *   Connected: '/World/agv_5/left_caster/Inner_Left_Wheel/materials/Looks/Robot.inputs:emissive_color' @ '/World/agv_5/left_caster/Inner_Left_Wheel/materials/Looks/Robot'
           *   'metallic_texture_influence' [float] = '1'
           *   'normalmap_texture' [asset] = 'Textures/STL_Robot_normal.%3CUDIM%3E.png'
           *   'ORM_texture' [asset] = 'Textures/STL_Robot_orm.%3CUDIM%3E.png'
           *   'reflection_roughness_texture_influence' [float] = '1'
           *   'uv_space_index' [int]
               *   Connected: '/World/agv_5/left_caster/Inner_Left_Wheel/materials/Looks/Robot.inputs:uv_space_index' @ '/World/agv_5/left_caster/Inner_Left_Wheel/materials/Looks/Robot'


---


### /World/agv_5/right_caster/Inner_Right_Wheel/materials/Looks/Robot
*  **Prim路径 (Prim Path):**/World/agv_5/right_caster/Inner_Right_Wheel/materials/Looks/Robot
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/agv_5/right_caster/Inner_Right_Wheel/materials/Looks/Robot/Robot'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/agv_5/right_caster/Inner_Right_Wheel/materials/Looks/Robot/Robot'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   纹理引用 (Texture Assets):
           *   'Textures/STL_Robot_albedo.%3CUDIM%3E.png'
           *   'Textures/STL_Robot_normal.%3CUDIM%3E.png'
           *   'Textures/STL_Robot_orm.%3CUDIM%3E.png'
       *   Inputs:
           *   'diffuse_color_constant' [color3f]
               *   Connected: '/World/agv_5/right_caster/Inner_Right_Wheel/materials/Looks/Robot.inputs:diffuse_color_constant' @ '/World/agv_5/right_caster/Inner_Right_Wheel/materials/Looks/Robot'
           *   'diffuse_texture' [asset] = 'Textures/STL_Robot_albedo.%3CUDIM%3E.png'
           *   'emissive_color' [color3f]
               *   Connected: '/World/agv_5/right_caster/Inner_Right_Wheel/materials/Looks/Robot.inputs:emissive_color' @ '/World/agv_5/right_caster/Inner_Right_Wheel/materials/Looks/Robot'
           *   'metallic_texture_influence' [float] = '1'
           *   'normalmap_texture' [asset] = 'Textures/STL_Robot_normal.%3CUDIM%3E.png'
           *   'ORM_texture' [asset] = 'Textures/STL_Robot_orm.%3CUDIM%3E.png'
           *   'reflection_roughness_texture_influence' [float] = '1'
           *   'uv_space_index' [int]
               *   Connected: '/World/agv_5/right_caster/Inner_Right_Wheel/materials/Looks/Robot.inputs:uv_space_index' @ '/World/agv_5/right_caster/Inner_Right_Wheel/materials/Looks/Robot'


---


### /World/agv_5/wheel_material
*  **Prim路径 (Prim Path):**/World/agv_5/wheel_material
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'


---


### /World/agv_5/caster_material
*  **Prim路径 (Prim Path):**/World/agv_5/caster_material
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'


---


### /World/agv_6/chassis/Body/Looks/Robot
*  **Prim路径 (Prim Path):**/World/agv_6/chassis/Body/Looks/Robot
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/agv_6/chassis/Body/Looks/Robot/Robot'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/agv_6/chassis/Body/Looks/Robot/Robot'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   纹理引用 (Texture Assets):
           *   'Textures/STL_Robot_albedo.<UDIM>.png'
           *   'Textures/STL_Robot_emissive.<UDIM>.png'
           *   'Textures/STL_Robot_normal.<UDIM>.png'
           *   'Textures/STL_Robot_orm.<UDIM>.png'
       *   Inputs:
           *   'diffuse_color_constant' [color3f]
               *   Connected: '/World/agv_6/chassis/Body/Looks/Robot.inputs:diffuse_color_constant' @ '/World/agv_6/chassis/Body/Looks/Robot'
           *   'diffuse_texture' [asset] = 'Textures/STL_Robot_albedo.<UDIM>.png'
           *   'emissive_color' [color3f]
               *   Connected: '/World/agv_6/chassis/Body/Looks/Robot.inputs:emissive_color' @ '/World/agv_6/chassis/Body/Looks/Robot'
           *   'emissive_intensity' [float] = '8000'
           *   'emissive_mask_texture' [asset] = 'Textures/STL_Robot_emissive.<UDIM>.png'
           *   'metallic_texture_influence' [float] = '0.9'
           *   'normalmap_texture' [asset] = 'Textures/STL_Robot_normal.<UDIM>.png'
           *   'ORM_texture' [asset] = 'Textures/STL_Robot_orm.<UDIM>.png'
           *   'reflection_roughness_texture_influence' [float] = '1'
           *   'uv_space_index' [int]
               *   Connected: '/World/agv_6/chassis/Body/Looks/Robot.inputs:uv_space_index' @ '/World/agv_6/chassis/Body/Looks/Robot'


---


### /World/agv_6/left_wheel/Left_Wheel/Looks/Robot
*  **Prim路径 (Prim Path):**/World/agv_6/left_wheel/Left_Wheel/Looks/Robot
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/agv_6/left_wheel/Left_Wheel/Looks/Robot/Robot'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/agv_6/left_wheel/Left_Wheel/Looks/Robot/Robot'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   纹理引用 (Texture Assets):
           *   'Textures/STL_Robot_albedo.<UDIM>.png'
           *   'Textures/STL_Robot_normal.<UDIM>.png'
           *   'Textures/STL_Robot_orm.<UDIM>.png'
       *   Inputs:
           *   'diffuse_color_constant' [color3f]
               *   Connected: '/World/agv_6/left_wheel/Left_Wheel/Looks/Robot.inputs:diffuse_color_constant' @ '/World/agv_6/left_wheel/Left_Wheel/Looks/Robot'
           *   'diffuse_texture' [asset] = 'Textures/STL_Robot_albedo.<UDIM>.png'
           *   'emissive_color' [color3f]
               *   Connected: '/World/agv_6/left_wheel/Left_Wheel/Looks/Robot.inputs:emissive_color' @ '/World/agv_6/left_wheel/Left_Wheel/Looks/Robot'
           *   'metallic_texture_influence' [float] = '1'
           *   'normalmap_texture' [asset] = 'Textures/STL_Robot_normal.<UDIM>.png'
           *   'ORM_texture' [asset] = 'Textures/STL_Robot_orm.<UDIM>.png'
           *   'reflection_roughness_texture_influence' [float] = '1'
           *   'uv_space_index' [int]
               *   Connected: '/World/agv_6/left_wheel/Left_Wheel/Looks/Robot.inputs:uv_space_index' @ '/World/agv_6/left_wheel/Left_Wheel/Looks/Robot'


---


### /World/agv_6/right_wheel/Right_Wheel/Looks/Robot
*  **Prim路径 (Prim Path):**/World/agv_6/right_wheel/Right_Wheel/Looks/Robot
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/agv_6/right_wheel/Right_Wheel/Looks/Robot/Robot'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/agv_6/right_wheel/Right_Wheel/Looks/Robot/Robot'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   纹理引用 (Texture Assets):
           *   'Textures/STL_Robot_albedo.<UDIM>.png'
           *   'Textures/STL_Robot_normal.<UDIM>.png'
           *   'Textures/STL_Robot_orm.<UDIM>.png'
       *   Inputs:
           *   'diffuse_color_constant' [color3f]
               *   Connected: '/World/agv_6/right_wheel/Right_Wheel/Looks/Robot.inputs:diffuse_color_constant' @ '/World/agv_6/right_wheel/Right_Wheel/Looks/Robot'
           *   'diffuse_texture' [asset] = 'Textures/STL_Robot_albedo.<UDIM>.png'
           *   'emissive_color' [color3f]
               *   Connected: '/World/agv_6/right_wheel/Right_Wheel/Looks/Robot.inputs:emissive_color' @ '/World/agv_6/right_wheel/Right_Wheel/Looks/Robot'
           *   'metallic_texture_influence' [float] = '1'
           *   'normalmap_texture' [asset] = 'Textures/STL_Robot_normal.<UDIM>.png'
           *   'ORM_texture' [asset] = 'Textures/STL_Robot_orm.<UDIM>.png'
           *   'reflection_roughness_texture_influence' [float] = '1'
           *   'uv_space_index' [int]
               *   Connected: '/World/agv_6/right_wheel/Right_Wheel/Looks/Robot.inputs:uv_space_index' @ '/World/agv_6/right_wheel/Right_Wheel/Looks/Robot'


---


### /World/agv_6/lift/Lift/Looks/Robot
*  **Prim路径 (Prim Path):**/World/agv_6/lift/Lift/Looks/Robot
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/agv_6/lift/Lift/Looks/Robot/Robot'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/agv_6/lift/Lift/Looks/Robot/Robot'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   纹理引用 (Texture Assets):
           *   'Textures/STL_Robot_albedo.<UDIM>.png'
           *   'Textures/STL_Robot_normal.<UDIM>.png'
           *   'Textures/STL_Robot_orm.<UDIM>.png'
       *   Inputs:
           *   'diffuse_color_constant' [color3f]
               *   Connected: '/World/agv_6/lift/Lift/Looks/Robot.inputs:diffuse_color_constant' @ '/World/agv_6/lift/Lift/Looks/Robot'
           *   'diffuse_texture' [asset] = 'Textures/STL_Robot_albedo.<UDIM>.png'
           *   'emissive_color' [color3f]
               *   Connected: '/World/agv_6/lift/Lift/Looks/Robot.inputs:emissive_color' @ '/World/agv_6/lift/Lift/Looks/Robot'
           *   'metallic_texture_influence' [float] = '0.901'
           *   'normalmap_texture' [asset] = 'Textures/STL_Robot_normal.<UDIM>.png'
           *   'ORM_texture' [asset] = 'Textures/STL_Robot_orm.<UDIM>.png'
           *   'reflection_roughness_texture_influence' [float] = '1'
           *   'uv_space_index' [int]
               *   Connected: '/World/agv_6/lift/Lift/Looks/Robot.inputs:uv_space_index' @ '/World/agv_6/lift/Lift/Looks/Robot'


---


### /World/agv_6/left_swivel/Left_Swivel/materials/Looks/Robot
*  **Prim路径 (Prim Path):**/World/agv_6/left_swivel/Left_Swivel/materials/Looks/Robot
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/agv_6/left_swivel/Left_Swivel/materials/Looks/Robot/Robot'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/agv_6/left_swivel/Left_Swivel/materials/Looks/Robot/Robot'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   纹理引用 (Texture Assets):
           *   'Textures/STL_Robot_albedo.%3CUDIM%3E.png'
           *   'Textures/STL_Robot_normal.%3CUDIM%3E.png'
           *   'Textures/STL_Robot_orm.%3CUDIM%3E.png'
       *   Inputs:
           *   'diffuse_color_constant' [color3f]
               *   Connected: '/World/agv_6/left_swivel/Left_Swivel/materials/Looks/Robot.inputs:diffuse_color_constant' @ '/World/agv_6/left_swivel/Left_Swivel/materials/Looks/Robot'
           *   'diffuse_texture' [asset] = 'Textures/STL_Robot_albedo.%3CUDIM%3E.png'
           *   'emissive_color' [color3f]
               *   Connected: '/World/agv_6/left_swivel/Left_Swivel/materials/Looks/Robot.inputs:emissive_color' @ '/World/agv_6/left_swivel/Left_Swivel/materials/Looks/Robot'
           *   'metallic_texture_influence' [float] = '1'
           *   'normalmap_texture' [asset] = 'Textures/STL_Robot_normal.%3CUDIM%3E.png'
           *   'ORM_texture' [asset] = 'Textures/STL_Robot_orm.%3CUDIM%3E.png'
           *   'reflection_roughness_texture_influence' [float] = '1'
           *   'uv_space_index' [int]
               *   Connected: '/World/agv_6/left_swivel/Left_Swivel/materials/Looks/Robot.inputs:uv_space_index' @ '/World/agv_6/left_swivel/Left_Swivel/materials/Looks/Robot'


---


### /World/agv_6/right_swivel/Right_Swivel/materials/Looks/Robot
*  **Prim路径 (Prim Path):**/World/agv_6/right_swivel/Right_Swivel/materials/Looks/Robot
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/agv_6/right_swivel/Right_Swivel/materials/Looks/Robot/Robot'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/agv_6/right_swivel/Right_Swivel/materials/Looks/Robot/Robot'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   纹理引用 (Texture Assets):
           *   'Textures/STL_Robot_albedo.%3CUDIM%3E.png'
           *   'Textures/STL_Robot_normal.%3CUDIM%3E.png'
           *   'Textures/STL_Robot_orm.%3CUDIM%3E.png'
       *   Inputs:
           *   'diffuse_color_constant' [color3f]
               *   Connected: '/World/agv_6/right_swivel/Right_Swivel/materials/Looks/Robot.inputs:diffuse_color_constant' @ '/World/agv_6/right_swivel/Right_Swivel/materials/Looks/Robot'
           *   'diffuse_texture' [asset] = 'Textures/STL_Robot_albedo.%3CUDIM%3E.png'
           *   'emissive_color' [color3f]
               *   Connected: '/World/agv_6/right_swivel/Right_Swivel/materials/Looks/Robot.inputs:emissive_color' @ '/World/agv_6/right_swivel/Right_Swivel/materials/Looks/Robot'
           *   'metallic_texture_influence' [float] = '1'
           *   'normalmap_texture' [asset] = 'Textures/STL_Robot_normal.%3CUDIM%3E.png'
           *   'ORM_texture' [asset] = 'Textures/STL_Robot_orm.%3CUDIM%3E.png'
           *   'reflection_roughness_texture_influence' [float] = '1'
           *   'uv_space_index' [int]
               *   Connected: '/World/agv_6/right_swivel/Right_Swivel/materials/Looks/Robot.inputs:uv_space_index' @ '/World/agv_6/right_swivel/Right_Swivel/materials/Looks/Robot'


---


### /World/agv_6/left_caster/Inner_Left_Wheel/materials/Looks/Robot
*  **Prim路径 (Prim Path):**/World/agv_6/left_caster/Inner_Left_Wheel/materials/Looks/Robot
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/agv_6/left_caster/Inner_Left_Wheel/materials/Looks/Robot/Robot'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/agv_6/left_caster/Inner_Left_Wheel/materials/Looks/Robot/Robot'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   纹理引用 (Texture Assets):
           *   'Textures/STL_Robot_albedo.%3CUDIM%3E.png'
           *   'Textures/STL_Robot_normal.%3CUDIM%3E.png'
           *   'Textures/STL_Robot_orm.%3CUDIM%3E.png'
       *   Inputs:
           *   'diffuse_color_constant' [color3f]
               *   Connected: '/World/agv_6/left_caster/Inner_Left_Wheel/materials/Looks/Robot.inputs:diffuse_color_constant' @ '/World/agv_6/left_caster/Inner_Left_Wheel/materials/Looks/Robot'
           *   'diffuse_texture' [asset] = 'Textures/STL_Robot_albedo.%3CUDIM%3E.png'
           *   'emissive_color' [color3f]
               *   Connected: '/World/agv_6/left_caster/Inner_Left_Wheel/materials/Looks/Robot.inputs:emissive_color' @ '/World/agv_6/left_caster/Inner_Left_Wheel/materials/Looks/Robot'
           *   'metallic_texture_influence' [float] = '1'
           *   'normalmap_texture' [asset] = 'Textures/STL_Robot_normal.%3CUDIM%3E.png'
           *   'ORM_texture' [asset] = 'Textures/STL_Robot_orm.%3CUDIM%3E.png'
           *   'reflection_roughness_texture_influence' [float] = '1'
           *   'uv_space_index' [int]
               *   Connected: '/World/agv_6/left_caster/Inner_Left_Wheel/materials/Looks/Robot.inputs:uv_space_index' @ '/World/agv_6/left_caster/Inner_Left_Wheel/materials/Looks/Robot'


---


### /World/agv_6/right_caster/Inner_Right_Wheel/materials/Looks/Robot
*  **Prim路径 (Prim Path):**/World/agv_6/right_caster/Inner_Right_Wheel/materials/Looks/Robot
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/agv_6/right_caster/Inner_Right_Wheel/materials/Looks/Robot/Robot'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/agv_6/right_caster/Inner_Right_Wheel/materials/Looks/Robot/Robot'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   纹理引用 (Texture Assets):
           *   'Textures/STL_Robot_albedo.%3CUDIM%3E.png'
           *   'Textures/STL_Robot_normal.%3CUDIM%3E.png'
           *   'Textures/STL_Robot_orm.%3CUDIM%3E.png'
       *   Inputs:
           *   'diffuse_color_constant' [color3f]
               *   Connected: '/World/agv_6/right_caster/Inner_Right_Wheel/materials/Looks/Robot.inputs:diffuse_color_constant' @ '/World/agv_6/right_caster/Inner_Right_Wheel/materials/Looks/Robot'
           *   'diffuse_texture' [asset] = 'Textures/STL_Robot_albedo.%3CUDIM%3E.png'
           *   'emissive_color' [color3f]
               *   Connected: '/World/agv_6/right_caster/Inner_Right_Wheel/materials/Looks/Robot.inputs:emissive_color' @ '/World/agv_6/right_caster/Inner_Right_Wheel/materials/Looks/Robot'
           *   'metallic_texture_influence' [float] = '1'
           *   'normalmap_texture' [asset] = 'Textures/STL_Robot_normal.%3CUDIM%3E.png'
           *   'ORM_texture' [asset] = 'Textures/STL_Robot_orm.%3CUDIM%3E.png'
           *   'reflection_roughness_texture_influence' [float] = '1'
           *   'uv_space_index' [int]
               *   Connected: '/World/agv_6/right_caster/Inner_Right_Wheel/materials/Looks/Robot.inputs:uv_space_index' @ '/World/agv_6/right_caster/Inner_Right_Wheel/materials/Looks/Robot'


---


### /World/agv_6/wheel_material
*  **Prim路径 (Prim Path):**/World/agv_6/wheel_material
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'


---


### /World/agv_6/caster_material
*  **Prim路径 (Prim Path):**/World/agv_6/caster_material
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'


---


### /World/agv_7/chassis/Body/Looks/Robot
*  **Prim路径 (Prim Path):**/World/agv_7/chassis/Body/Looks/Robot
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/agv_7/chassis/Body/Looks/Robot/Robot'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/agv_7/chassis/Body/Looks/Robot/Robot'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   纹理引用 (Texture Assets):
           *   'Textures/STL_Robot_albedo.<UDIM>.png'
           *   'Textures/STL_Robot_emissive.<UDIM>.png'
           *   'Textures/STL_Robot_normal.<UDIM>.png'
           *   'Textures/STL_Robot_orm.<UDIM>.png'
       *   Inputs:
           *   'diffuse_color_constant' [color3f]
               *   Connected: '/World/agv_7/chassis/Body/Looks/Robot.inputs:diffuse_color_constant' @ '/World/agv_7/chassis/Body/Looks/Robot'
           *   'diffuse_texture' [asset] = 'Textures/STL_Robot_albedo.<UDIM>.png'
           *   'emissive_color' [color3f]
               *   Connected: '/World/agv_7/chassis/Body/Looks/Robot.inputs:emissive_color' @ '/World/agv_7/chassis/Body/Looks/Robot'
           *   'emissive_intensity' [float] = '8000'
           *   'emissive_mask_texture' [asset] = 'Textures/STL_Robot_emissive.<UDIM>.png'
           *   'metallic_texture_influence' [float] = '0.9'
           *   'normalmap_texture' [asset] = 'Textures/STL_Robot_normal.<UDIM>.png'
           *   'ORM_texture' [asset] = 'Textures/STL_Robot_orm.<UDIM>.png'
           *   'reflection_roughness_texture_influence' [float] = '1'
           *   'uv_space_index' [int]
               *   Connected: '/World/agv_7/chassis/Body/Looks/Robot.inputs:uv_space_index' @ '/World/agv_7/chassis/Body/Looks/Robot'


---


### /World/agv_7/left_wheel/Left_Wheel/Looks/Robot
*  **Prim路径 (Prim Path):**/World/agv_7/left_wheel/Left_Wheel/Looks/Robot
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/agv_7/left_wheel/Left_Wheel/Looks/Robot/Robot'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/agv_7/left_wheel/Left_Wheel/Looks/Robot/Robot'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   纹理引用 (Texture Assets):
           *   'Textures/STL_Robot_albedo.<UDIM>.png'
           *   'Textures/STL_Robot_normal.<UDIM>.png'
           *   'Textures/STL_Robot_orm.<UDIM>.png'
       *   Inputs:
           *   'diffuse_color_constant' [color3f]
               *   Connected: '/World/agv_7/left_wheel/Left_Wheel/Looks/Robot.inputs:diffuse_color_constant' @ '/World/agv_7/left_wheel/Left_Wheel/Looks/Robot'
           *   'diffuse_texture' [asset] = 'Textures/STL_Robot_albedo.<UDIM>.png'
           *   'emissive_color' [color3f]
               *   Connected: '/World/agv_7/left_wheel/Left_Wheel/Looks/Robot.inputs:emissive_color' @ '/World/agv_7/left_wheel/Left_Wheel/Looks/Robot'
           *   'metallic_texture_influence' [float] = '1'
           *   'normalmap_texture' [asset] = 'Textures/STL_Robot_normal.<UDIM>.png'
           *   'ORM_texture' [asset] = 'Textures/STL_Robot_orm.<UDIM>.png'
           *   'reflection_roughness_texture_influence' [float] = '1'
           *   'uv_space_index' [int]
               *   Connected: '/World/agv_7/left_wheel/Left_Wheel/Looks/Robot.inputs:uv_space_index' @ '/World/agv_7/left_wheel/Left_Wheel/Looks/Robot'


---


### /World/agv_7/right_wheel/Right_Wheel/Looks/Robot
*  **Prim路径 (Prim Path):**/World/agv_7/right_wheel/Right_Wheel/Looks/Robot
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/agv_7/right_wheel/Right_Wheel/Looks/Robot/Robot'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/agv_7/right_wheel/Right_Wheel/Looks/Robot/Robot'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   纹理引用 (Texture Assets):
           *   'Textures/STL_Robot_albedo.<UDIM>.png'
           *   'Textures/STL_Robot_normal.<UDIM>.png'
           *   'Textures/STL_Robot_orm.<UDIM>.png'
       *   Inputs:
           *   'diffuse_color_constant' [color3f]
               *   Connected: '/World/agv_7/right_wheel/Right_Wheel/Looks/Robot.inputs:diffuse_color_constant' @ '/World/agv_7/right_wheel/Right_Wheel/Looks/Robot'
           *   'diffuse_texture' [asset] = 'Textures/STL_Robot_albedo.<UDIM>.png'
           *   'emissive_color' [color3f]
               *   Connected: '/World/agv_7/right_wheel/Right_Wheel/Looks/Robot.inputs:emissive_color' @ '/World/agv_7/right_wheel/Right_Wheel/Looks/Robot'
           *   'metallic_texture_influence' [float] = '1'
           *   'normalmap_texture' [asset] = 'Textures/STL_Robot_normal.<UDIM>.png'
           *   'ORM_texture' [asset] = 'Textures/STL_Robot_orm.<UDIM>.png'
           *   'reflection_roughness_texture_influence' [float] = '1'
           *   'uv_space_index' [int]
               *   Connected: '/World/agv_7/right_wheel/Right_Wheel/Looks/Robot.inputs:uv_space_index' @ '/World/agv_7/right_wheel/Right_Wheel/Looks/Robot'


---


### /World/agv_7/lift/Lift/Looks/Robot
*  **Prim路径 (Prim Path):**/World/agv_7/lift/Lift/Looks/Robot
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/agv_7/lift/Lift/Looks/Robot/Robot'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/agv_7/lift/Lift/Looks/Robot/Robot'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   纹理引用 (Texture Assets):
           *   'Textures/STL_Robot_albedo.<UDIM>.png'
           *   'Textures/STL_Robot_normal.<UDIM>.png'
           *   'Textures/STL_Robot_orm.<UDIM>.png'
       *   Inputs:
           *   'diffuse_color_constant' [color3f]
               *   Connected: '/World/agv_7/lift/Lift/Looks/Robot.inputs:diffuse_color_constant' @ '/World/agv_7/lift/Lift/Looks/Robot'
           *   'diffuse_texture' [asset] = 'Textures/STL_Robot_albedo.<UDIM>.png'
           *   'emissive_color' [color3f]
               *   Connected: '/World/agv_7/lift/Lift/Looks/Robot.inputs:emissive_color' @ '/World/agv_7/lift/Lift/Looks/Robot'
           *   'metallic_texture_influence' [float] = '0.901'
           *   'normalmap_texture' [asset] = 'Textures/STL_Robot_normal.<UDIM>.png'
           *   'ORM_texture' [asset] = 'Textures/STL_Robot_orm.<UDIM>.png'
           *   'reflection_roughness_texture_influence' [float] = '1'
           *   'uv_space_index' [int]
               *   Connected: '/World/agv_7/lift/Lift/Looks/Robot.inputs:uv_space_index' @ '/World/agv_7/lift/Lift/Looks/Robot'


---


### /World/agv_7/left_swivel/Left_Swivel/materials/Looks/Robot
*  **Prim路径 (Prim Path):**/World/agv_7/left_swivel/Left_Swivel/materials/Looks/Robot
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/agv_7/left_swivel/Left_Swivel/materials/Looks/Robot/Robot'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/agv_7/left_swivel/Left_Swivel/materials/Looks/Robot/Robot'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   纹理引用 (Texture Assets):
           *   'Textures/STL_Robot_albedo.%3CUDIM%3E.png'
           *   'Textures/STL_Robot_normal.%3CUDIM%3E.png'
           *   'Textures/STL_Robot_orm.%3CUDIM%3E.png'
       *   Inputs:
           *   'diffuse_color_constant' [color3f]
               *   Connected: '/World/agv_7/left_swivel/Left_Swivel/materials/Looks/Robot.inputs:diffuse_color_constant' @ '/World/agv_7/left_swivel/Left_Swivel/materials/Looks/Robot'
           *   'diffuse_texture' [asset] = 'Textures/STL_Robot_albedo.%3CUDIM%3E.png'
           *   'emissive_color' [color3f]
               *   Connected: '/World/agv_7/left_swivel/Left_Swivel/materials/Looks/Robot.inputs:emissive_color' @ '/World/agv_7/left_swivel/Left_Swivel/materials/Looks/Robot'
           *   'metallic_texture_influence' [float] = '1'
           *   'normalmap_texture' [asset] = 'Textures/STL_Robot_normal.%3CUDIM%3E.png'
           *   'ORM_texture' [asset] = 'Textures/STL_Robot_orm.%3CUDIM%3E.png'
           *   'reflection_roughness_texture_influence' [float] = '1'
           *   'uv_space_index' [int]
               *   Connected: '/World/agv_7/left_swivel/Left_Swivel/materials/Looks/Robot.inputs:uv_space_index' @ '/World/agv_7/left_swivel/Left_Swivel/materials/Looks/Robot'


---


### /World/agv_7/right_swivel/Right_Swivel/materials/Looks/Robot
*  **Prim路径 (Prim Path):**/World/agv_7/right_swivel/Right_Swivel/materials/Looks/Robot
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/agv_7/right_swivel/Right_Swivel/materials/Looks/Robot/Robot'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/agv_7/right_swivel/Right_Swivel/materials/Looks/Robot/Robot'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   纹理引用 (Texture Assets):
           *   'Textures/STL_Robot_albedo.%3CUDIM%3E.png'
           *   'Textures/STL_Robot_normal.%3CUDIM%3E.png'
           *   'Textures/STL_Robot_orm.%3CUDIM%3E.png'
       *   Inputs:
           *   'diffuse_color_constant' [color3f]
               *   Connected: '/World/agv_7/right_swivel/Right_Swivel/materials/Looks/Robot.inputs:diffuse_color_constant' @ '/World/agv_7/right_swivel/Right_Swivel/materials/Looks/Robot'
           *   'diffuse_texture' [asset] = 'Textures/STL_Robot_albedo.%3CUDIM%3E.png'
           *   'emissive_color' [color3f]
               *   Connected: '/World/agv_7/right_swivel/Right_Swivel/materials/Looks/Robot.inputs:emissive_color' @ '/World/agv_7/right_swivel/Right_Swivel/materials/Looks/Robot'
           *   'metallic_texture_influence' [float] = '1'
           *   'normalmap_texture' [asset] = 'Textures/STL_Robot_normal.%3CUDIM%3E.png'
           *   'ORM_texture' [asset] = 'Textures/STL_Robot_orm.%3CUDIM%3E.png'
           *   'reflection_roughness_texture_influence' [float] = '1'
           *   'uv_space_index' [int]
               *   Connected: '/World/agv_7/right_swivel/Right_Swivel/materials/Looks/Robot.inputs:uv_space_index' @ '/World/agv_7/right_swivel/Right_Swivel/materials/Looks/Robot'


---


### /World/agv_7/left_caster/Inner_Left_Wheel/materials/Looks/Robot
*  **Prim路径 (Prim Path):**/World/agv_7/left_caster/Inner_Left_Wheel/materials/Looks/Robot
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/agv_7/left_caster/Inner_Left_Wheel/materials/Looks/Robot/Robot'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/agv_7/left_caster/Inner_Left_Wheel/materials/Looks/Robot/Robot'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   纹理引用 (Texture Assets):
           *   'Textures/STL_Robot_albedo.%3CUDIM%3E.png'
           *   'Textures/STL_Robot_normal.%3CUDIM%3E.png'
           *   'Textures/STL_Robot_orm.%3CUDIM%3E.png'
       *   Inputs:
           *   'diffuse_color_constant' [color3f]
               *   Connected: '/World/agv_7/left_caster/Inner_Left_Wheel/materials/Looks/Robot.inputs:diffuse_color_constant' @ '/World/agv_7/left_caster/Inner_Left_Wheel/materials/Looks/Robot'
           *   'diffuse_texture' [asset] = 'Textures/STL_Robot_albedo.%3CUDIM%3E.png'
           *   'emissive_color' [color3f]
               *   Connected: '/World/agv_7/left_caster/Inner_Left_Wheel/materials/Looks/Robot.inputs:emissive_color' @ '/World/agv_7/left_caster/Inner_Left_Wheel/materials/Looks/Robot'
           *   'metallic_texture_influence' [float] = '1'
           *   'normalmap_texture' [asset] = 'Textures/STL_Robot_normal.%3CUDIM%3E.png'
           *   'ORM_texture' [asset] = 'Textures/STL_Robot_orm.%3CUDIM%3E.png'
           *   'reflection_roughness_texture_influence' [float] = '1'
           *   'uv_space_index' [int]
               *   Connected: '/World/agv_7/left_caster/Inner_Left_Wheel/materials/Looks/Robot.inputs:uv_space_index' @ '/World/agv_7/left_caster/Inner_Left_Wheel/materials/Looks/Robot'


---


### /World/agv_7/right_caster/Inner_Right_Wheel/materials/Looks/Robot
*  **Prim路径 (Prim Path):**/World/agv_7/right_caster/Inner_Right_Wheel/materials/Looks/Robot
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/agv_7/right_caster/Inner_Right_Wheel/materials/Looks/Robot/Robot'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/agv_7/right_caster/Inner_Right_Wheel/materials/Looks/Robot/Robot'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   纹理引用 (Texture Assets):
           *   'Textures/STL_Robot_albedo.%3CUDIM%3E.png'
           *   'Textures/STL_Robot_normal.%3CUDIM%3E.png'
           *   'Textures/STL_Robot_orm.%3CUDIM%3E.png'
       *   Inputs:
           *   'diffuse_color_constant' [color3f]
               *   Connected: '/World/agv_7/right_caster/Inner_Right_Wheel/materials/Looks/Robot.inputs:diffuse_color_constant' @ '/World/agv_7/right_caster/Inner_Right_Wheel/materials/Looks/Robot'
           *   'diffuse_texture' [asset] = 'Textures/STL_Robot_albedo.%3CUDIM%3E.png'
           *   'emissive_color' [color3f]
               *   Connected: '/World/agv_7/right_caster/Inner_Right_Wheel/materials/Looks/Robot.inputs:emissive_color' @ '/World/agv_7/right_caster/Inner_Right_Wheel/materials/Looks/Robot'
           *   'metallic_texture_influence' [float] = '1'
           *   'normalmap_texture' [asset] = 'Textures/STL_Robot_normal.%3CUDIM%3E.png'
           *   'ORM_texture' [asset] = 'Textures/STL_Robot_orm.%3CUDIM%3E.png'
           *   'reflection_roughness_texture_influence' [float] = '1'
           *   'uv_space_index' [int]
               *   Connected: '/World/agv_7/right_caster/Inner_Right_Wheel/materials/Looks/Robot.inputs:uv_space_index' @ '/World/agv_7/right_caster/Inner_Right_Wheel/materials/Looks/Robot'


---


### /World/agv_7/wheel_material
*  **Prim路径 (Prim Path):**/World/agv_7/wheel_material
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'


---


### /World/agv_7/caster_material
*  **Prim路径 (Prim Path):**/World/agv_7/caster_material
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'


---


### /World/agv_8/chassis/Body/Looks/Robot
*  **Prim路径 (Prim Path):**/World/agv_8/chassis/Body/Looks/Robot
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/agv_8/chassis/Body/Looks/Robot/Robot'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/agv_8/chassis/Body/Looks/Robot/Robot'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   纹理引用 (Texture Assets):
           *   'Textures/STL_Robot_albedo.<UDIM>.png'
           *   'Textures/STL_Robot_emissive.<UDIM>.png'
           *   'Textures/STL_Robot_normal.<UDIM>.png'
           *   'Textures/STL_Robot_orm.<UDIM>.png'
       *   Inputs:
           *   'diffuse_color_constant' [color3f]
               *   Connected: '/World/agv_8/chassis/Body/Looks/Robot.inputs:diffuse_color_constant' @ '/World/agv_8/chassis/Body/Looks/Robot'
           *   'diffuse_texture' [asset] = 'Textures/STL_Robot_albedo.<UDIM>.png'
           *   'emissive_color' [color3f]
               *   Connected: '/World/agv_8/chassis/Body/Looks/Robot.inputs:emissive_color' @ '/World/agv_8/chassis/Body/Looks/Robot'
           *   'emissive_intensity' [float] = '8000'
           *   'emissive_mask_texture' [asset] = 'Textures/STL_Robot_emissive.<UDIM>.png'
           *   'metallic_texture_influence' [float] = '0.9'
           *   'normalmap_texture' [asset] = 'Textures/STL_Robot_normal.<UDIM>.png'
           *   'ORM_texture' [asset] = 'Textures/STL_Robot_orm.<UDIM>.png'
           *   'reflection_roughness_texture_influence' [float] = '1'
           *   'uv_space_index' [int]
               *   Connected: '/World/agv_8/chassis/Body/Looks/Robot.inputs:uv_space_index' @ '/World/agv_8/chassis/Body/Looks/Robot'


---


### /World/agv_8/left_wheel/Left_Wheel/Looks/Robot
*  **Prim路径 (Prim Path):**/World/agv_8/left_wheel/Left_Wheel/Looks/Robot
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/agv_8/left_wheel/Left_Wheel/Looks/Robot/Robot'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/agv_8/left_wheel/Left_Wheel/Looks/Robot/Robot'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   纹理引用 (Texture Assets):
           *   'Textures/STL_Robot_albedo.<UDIM>.png'
           *   'Textures/STL_Robot_normal.<UDIM>.png'
           *   'Textures/STL_Robot_orm.<UDIM>.png'
       *   Inputs:
           *   'diffuse_color_constant' [color3f]
               *   Connected: '/World/agv_8/left_wheel/Left_Wheel/Looks/Robot.inputs:diffuse_color_constant' @ '/World/agv_8/left_wheel/Left_Wheel/Looks/Robot'
           *   'diffuse_texture' [asset] = 'Textures/STL_Robot_albedo.<UDIM>.png'
           *   'emissive_color' [color3f]
               *   Connected: '/World/agv_8/left_wheel/Left_Wheel/Looks/Robot.inputs:emissive_color' @ '/World/agv_8/left_wheel/Left_Wheel/Looks/Robot'
           *   'metallic_texture_influence' [float] = '1'
           *   'normalmap_texture' [asset] = 'Textures/STL_Robot_normal.<UDIM>.png'
           *   'ORM_texture' [asset] = 'Textures/STL_Robot_orm.<UDIM>.png'
           *   'reflection_roughness_texture_influence' [float] = '1'
           *   'uv_space_index' [int]
               *   Connected: '/World/agv_8/left_wheel/Left_Wheel/Looks/Robot.inputs:uv_space_index' @ '/World/agv_8/left_wheel/Left_Wheel/Looks/Robot'


---


### /World/agv_8/right_wheel/Right_Wheel/Looks/Robot
*  **Prim路径 (Prim Path):**/World/agv_8/right_wheel/Right_Wheel/Looks/Robot
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/agv_8/right_wheel/Right_Wheel/Looks/Robot/Robot'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/agv_8/right_wheel/Right_Wheel/Looks/Robot/Robot'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   纹理引用 (Texture Assets):
           *   'Textures/STL_Robot_albedo.<UDIM>.png'
           *   'Textures/STL_Robot_normal.<UDIM>.png'
           *   'Textures/STL_Robot_orm.<UDIM>.png'
       *   Inputs:
           *   'diffuse_color_constant' [color3f]
               *   Connected: '/World/agv_8/right_wheel/Right_Wheel/Looks/Robot.inputs:diffuse_color_constant' @ '/World/agv_8/right_wheel/Right_Wheel/Looks/Robot'
           *   'diffuse_texture' [asset] = 'Textures/STL_Robot_albedo.<UDIM>.png'
           *   'emissive_color' [color3f]
               *   Connected: '/World/agv_8/right_wheel/Right_Wheel/Looks/Robot.inputs:emissive_color' @ '/World/agv_8/right_wheel/Right_Wheel/Looks/Robot'
           *   'metallic_texture_influence' [float] = '1'
           *   'normalmap_texture' [asset] = 'Textures/STL_Robot_normal.<UDIM>.png'
           *   'ORM_texture' [asset] = 'Textures/STL_Robot_orm.<UDIM>.png'
           *   'reflection_roughness_texture_influence' [float] = '1'
           *   'uv_space_index' [int]
               *   Connected: '/World/agv_8/right_wheel/Right_Wheel/Looks/Robot.inputs:uv_space_index' @ '/World/agv_8/right_wheel/Right_Wheel/Looks/Robot'


---


### /World/agv_8/lift/Lift/Looks/Robot
*  **Prim路径 (Prim Path):**/World/agv_8/lift/Lift/Looks/Robot
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/agv_8/lift/Lift/Looks/Robot/Robot'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/agv_8/lift/Lift/Looks/Robot/Robot'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   纹理引用 (Texture Assets):
           *   'Textures/STL_Robot_albedo.<UDIM>.png'
           *   'Textures/STL_Robot_normal.<UDIM>.png'
           *   'Textures/STL_Robot_orm.<UDIM>.png'
       *   Inputs:
           *   'diffuse_color_constant' [color3f]
               *   Connected: '/World/agv_8/lift/Lift/Looks/Robot.inputs:diffuse_color_constant' @ '/World/agv_8/lift/Lift/Looks/Robot'
           *   'diffuse_texture' [asset] = 'Textures/STL_Robot_albedo.<UDIM>.png'
           *   'emissive_color' [color3f]
               *   Connected: '/World/agv_8/lift/Lift/Looks/Robot.inputs:emissive_color' @ '/World/agv_8/lift/Lift/Looks/Robot'
           *   'metallic_texture_influence' [float] = '0.901'
           *   'normalmap_texture' [asset] = 'Textures/STL_Robot_normal.<UDIM>.png'
           *   'ORM_texture' [asset] = 'Textures/STL_Robot_orm.<UDIM>.png'
           *   'reflection_roughness_texture_influence' [float] = '1'
           *   'uv_space_index' [int]
               *   Connected: '/World/agv_8/lift/Lift/Looks/Robot.inputs:uv_space_index' @ '/World/agv_8/lift/Lift/Looks/Robot'


---


### /World/agv_8/left_swivel/Left_Swivel/materials/Looks/Robot
*  **Prim路径 (Prim Path):**/World/agv_8/left_swivel/Left_Swivel/materials/Looks/Robot
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/agv_8/left_swivel/Left_Swivel/materials/Looks/Robot/Robot'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/agv_8/left_swivel/Left_Swivel/materials/Looks/Robot/Robot'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   纹理引用 (Texture Assets):
           *   'Textures/STL_Robot_albedo.%3CUDIM%3E.png'
           *   'Textures/STL_Robot_normal.%3CUDIM%3E.png'
           *   'Textures/STL_Robot_orm.%3CUDIM%3E.png'
       *   Inputs:
           *   'diffuse_color_constant' [color3f]
               *   Connected: '/World/agv_8/left_swivel/Left_Swivel/materials/Looks/Robot.inputs:diffuse_color_constant' @ '/World/agv_8/left_swivel/Left_Swivel/materials/Looks/Robot'
           *   'diffuse_texture' [asset] = 'Textures/STL_Robot_albedo.%3CUDIM%3E.png'
           *   'emissive_color' [color3f]
               *   Connected: '/World/agv_8/left_swivel/Left_Swivel/materials/Looks/Robot.inputs:emissive_color' @ '/World/agv_8/left_swivel/Left_Swivel/materials/Looks/Robot'
           *   'metallic_texture_influence' [float] = '1'
           *   'normalmap_texture' [asset] = 'Textures/STL_Robot_normal.%3CUDIM%3E.png'
           *   'ORM_texture' [asset] = 'Textures/STL_Robot_orm.%3CUDIM%3E.png'
           *   'reflection_roughness_texture_influence' [float] = '1'
           *   'uv_space_index' [int]
               *   Connected: '/World/agv_8/left_swivel/Left_Swivel/materials/Looks/Robot.inputs:uv_space_index' @ '/World/agv_8/left_swivel/Left_Swivel/materials/Looks/Robot'


---


### /World/agv_8/right_swivel/Right_Swivel/materials/Looks/Robot
*  **Prim路径 (Prim Path):**/World/agv_8/right_swivel/Right_Swivel/materials/Looks/Robot
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/agv_8/right_swivel/Right_Swivel/materials/Looks/Robot/Robot'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/agv_8/right_swivel/Right_Swivel/materials/Looks/Robot/Robot'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   纹理引用 (Texture Assets):
           *   'Textures/STL_Robot_albedo.%3CUDIM%3E.png'
           *   'Textures/STL_Robot_normal.%3CUDIM%3E.png'
           *   'Textures/STL_Robot_orm.%3CUDIM%3E.png'
       *   Inputs:
           *   'diffuse_color_constant' [color3f]
               *   Connected: '/World/agv_8/right_swivel/Right_Swivel/materials/Looks/Robot.inputs:diffuse_color_constant' @ '/World/agv_8/right_swivel/Right_Swivel/materials/Looks/Robot'
           *   'diffuse_texture' [asset] = 'Textures/STL_Robot_albedo.%3CUDIM%3E.png'
           *   'emissive_color' [color3f]
               *   Connected: '/World/agv_8/right_swivel/Right_Swivel/materials/Looks/Robot.inputs:emissive_color' @ '/World/agv_8/right_swivel/Right_Swivel/materials/Looks/Robot'
           *   'metallic_texture_influence' [float] = '1'
           *   'normalmap_texture' [asset] = 'Textures/STL_Robot_normal.%3CUDIM%3E.png'
           *   'ORM_texture' [asset] = 'Textures/STL_Robot_orm.%3CUDIM%3E.png'
           *   'reflection_roughness_texture_influence' [float] = '1'
           *   'uv_space_index' [int]
               *   Connected: '/World/agv_8/right_swivel/Right_Swivel/materials/Looks/Robot.inputs:uv_space_index' @ '/World/agv_8/right_swivel/Right_Swivel/materials/Looks/Robot'


---


### /World/agv_8/left_caster/Inner_Left_Wheel/materials/Looks/Robot
*  **Prim路径 (Prim Path):**/World/agv_8/left_caster/Inner_Left_Wheel/materials/Looks/Robot
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/agv_8/left_caster/Inner_Left_Wheel/materials/Looks/Robot/Robot'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/agv_8/left_caster/Inner_Left_Wheel/materials/Looks/Robot/Robot'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   纹理引用 (Texture Assets):
           *   'Textures/STL_Robot_albedo.%3CUDIM%3E.png'
           *   'Textures/STL_Robot_normal.%3CUDIM%3E.png'
           *   'Textures/STL_Robot_orm.%3CUDIM%3E.png'
       *   Inputs:
           *   'diffuse_color_constant' [color3f]
               *   Connected: '/World/agv_8/left_caster/Inner_Left_Wheel/materials/Looks/Robot.inputs:diffuse_color_constant' @ '/World/agv_8/left_caster/Inner_Left_Wheel/materials/Looks/Robot'
           *   'diffuse_texture' [asset] = 'Textures/STL_Robot_albedo.%3CUDIM%3E.png'
           *   'emissive_color' [color3f]
               *   Connected: '/World/agv_8/left_caster/Inner_Left_Wheel/materials/Looks/Robot.inputs:emissive_color' @ '/World/agv_8/left_caster/Inner_Left_Wheel/materials/Looks/Robot'
           *   'metallic_texture_influence' [float] = '1'
           *   'normalmap_texture' [asset] = 'Textures/STL_Robot_normal.%3CUDIM%3E.png'
           *   'ORM_texture' [asset] = 'Textures/STL_Robot_orm.%3CUDIM%3E.png'
           *   'reflection_roughness_texture_influence' [float] = '1'
           *   'uv_space_index' [int]
               *   Connected: '/World/agv_8/left_caster/Inner_Left_Wheel/materials/Looks/Robot.inputs:uv_space_index' @ '/World/agv_8/left_caster/Inner_Left_Wheel/materials/Looks/Robot'


---


### /World/agv_8/right_caster/Inner_Right_Wheel/materials/Looks/Robot
*  **Prim路径 (Prim Path):**/World/agv_8/right_caster/Inner_Right_Wheel/materials/Looks/Robot
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/agv_8/right_caster/Inner_Right_Wheel/materials/Looks/Robot/Robot'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/agv_8/right_caster/Inner_Right_Wheel/materials/Looks/Robot/Robot'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   纹理引用 (Texture Assets):
           *   'Textures/STL_Robot_albedo.%3CUDIM%3E.png'
           *   'Textures/STL_Robot_normal.%3CUDIM%3E.png'
           *   'Textures/STL_Robot_orm.%3CUDIM%3E.png'
       *   Inputs:
           *   'diffuse_color_constant' [color3f]
               *   Connected: '/World/agv_8/right_caster/Inner_Right_Wheel/materials/Looks/Robot.inputs:diffuse_color_constant' @ '/World/agv_8/right_caster/Inner_Right_Wheel/materials/Looks/Robot'
           *   'diffuse_texture' [asset] = 'Textures/STL_Robot_albedo.%3CUDIM%3E.png'
           *   'emissive_color' [color3f]
               *   Connected: '/World/agv_8/right_caster/Inner_Right_Wheel/materials/Looks/Robot.inputs:emissive_color' @ '/World/agv_8/right_caster/Inner_Right_Wheel/materials/Looks/Robot'
           *   'metallic_texture_influence' [float] = '1'
           *   'normalmap_texture' [asset] = 'Textures/STL_Robot_normal.%3CUDIM%3E.png'
           *   'ORM_texture' [asset] = 'Textures/STL_Robot_orm.%3CUDIM%3E.png'
           *   'reflection_roughness_texture_influence' [float] = '1'
           *   'uv_space_index' [int]
               *   Connected: '/World/agv_8/right_caster/Inner_Right_Wheel/materials/Looks/Robot.inputs:uv_space_index' @ '/World/agv_8/right_caster/Inner_Right_Wheel/materials/Looks/Robot'


---


### /World/agv_8/wheel_material
*  **Prim路径 (Prim Path):**/World/agv_8/wheel_material
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'


---


### /World/agv_8/caster_material
*  **Prim路径 (Prim Path):**/World/agv_8/caster_material
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'


---


### /World/Conveyor_1/Materials/Material_0
*  **Prim路径 (Prim Path):**/World/Conveyor_1/Materials/Material_0
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/Conveyor_1/Materials/Material_0/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/Conveyor_1/Materials/Material_0/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f]
               *   Connected: '/World/Conveyor_1/Materials/Material_0/tex_base.outputs:rgb' @ '/World/Conveyor_1/Materials/Material_0/tex_base'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/Material_0_baseColor.jpg'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(1.000, 1.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0.892971'
       *   '/World/Conveyor_1/Materials/Material_0/tex_base' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/Material_0_baseColor.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
           *   'file' [asset] = '0/Material_0_baseColor.jpg'
           *   'st' [float2]
               *   Connected: '/World/Conveyor_1/Materials/Material_0/uvset0.outputs:result' @ '/World/Conveyor_1/Materials/Material_0/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/Conveyor_1/Materials/Material_0/uvset0' (ID: 'UsdPrimvarReader_float2')
       *   Implementation: 'id'


---


### /World/Conveyor_2/Materials/Material_0
*  **Prim路径 (Prim Path):**/World/Conveyor_2/Materials/Material_0
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/Conveyor_2/Materials/Material_0/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/Conveyor_2/Materials/Material_0/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f]
               *   Connected: '/World/Conveyor_2/Materials/Material_0/tex_base.outputs:rgb' @ '/World/Conveyor_2/Materials/Material_0/tex_base'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/Material_0_baseColor.jpg'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(1.000, 1.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0.892971'
       *   '/World/Conveyor_2/Materials/Material_0/tex_base' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/Material_0_baseColor.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
           *   'file' [asset] = '0/Material_0_baseColor.jpg'
           *   'st' [float2]
               *   Connected: '/World/Conveyor_2/Materials/Material_0/uvset0.outputs:result' @ '/World/Conveyor_2/Materials/Material_0/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/Conveyor_2/Materials/Material_0/uvset0' (ID: 'UsdPrimvarReader_float2')
       *   Implementation: 'id'


---


### /World/Conveyor_3/Materials/Material_0
*  **Prim路径 (Prim Path):**/World/Conveyor_3/Materials/Material_0
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/Conveyor_3/Materials/Material_0/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/Conveyor_3/Materials/Material_0/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f]
               *   Connected: '/World/Conveyor_3/Materials/Material_0/tex_base.outputs:rgb' @ '/World/Conveyor_3/Materials/Material_0/tex_base'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/Material_0_baseColor.jpg'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(1.000, 1.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0.892971'
       *   '/World/Conveyor_3/Materials/Material_0/tex_base' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/Material_0_baseColor.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
           *   'file' [asset] = '0/Material_0_baseColor.jpg'
           *   'st' [float2]
               *   Connected: '/World/Conveyor_3/Materials/Material_0/uvset0.outputs:result' @ '/World/Conveyor_3/Materials/Material_0/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/Conveyor_3/Materials/Material_0/uvset0' (ID: 'UsdPrimvarReader_float2')
       *   Implementation: 'id'


---


### /World/Conveyor_4/Materials/Material_0
*  **Prim路径 (Prim Path):**/World/Conveyor_4/Materials/Material_0
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/Conveyor_4/Materials/Material_0/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/Conveyor_4/Materials/Material_0/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f]
               *   Connected: '/World/Conveyor_4/Materials/Material_0/tex_base.outputs:rgb' @ '/World/Conveyor_4/Materials/Material_0/tex_base'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/Material_0_baseColor.jpg'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(1.000, 1.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0.892971'
       *   '/World/Conveyor_4/Materials/Material_0/tex_base' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/Material_0_baseColor.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
           *   'file' [asset] = '0/Material_0_baseColor.jpg'
           *   'st' [float2]
               *   Connected: '/World/Conveyor_4/Materials/Material_0/uvset0.outputs:result' @ '/World/Conveyor_4/Materials/Material_0/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/Conveyor_4/Materials/Material_0/uvset0' (ID: 'UsdPrimvarReader_float2')
       *   Implementation: 'id'


---


### /World/Conveyor_5/Materials/Material_0
*  **Prim路径 (Prim Path):**/World/Conveyor_5/Materials/Material_0
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/Conveyor_5/Materials/Material_0/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/Conveyor_5/Materials/Material_0/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f]
               *   Connected: '/World/Conveyor_5/Materials/Material_0/tex_base.outputs:rgb' @ '/World/Conveyor_5/Materials/Material_0/tex_base'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/Material_0_baseColor.jpg'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(1.000, 1.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0.892971'
       *   '/World/Conveyor_5/Materials/Material_0/tex_base' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/Material_0_baseColor.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
           *   'file' [asset] = '0/Material_0_baseColor.jpg'
           *   'st' [float2]
               *   Connected: '/World/Conveyor_5/Materials/Material_0/uvset0.outputs:result' @ '/World/Conveyor_5/Materials/Material_0/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/Conveyor_5/Materials/Material_0/uvset0' (ID: 'UsdPrimvarReader_float2')
       *   Implementation: 'id'


---


### /World/Conveyor_6/Materials/Material_0
*  **Prim路径 (Prim Path):**/World/Conveyor_6/Materials/Material_0
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/Conveyor_6/Materials/Material_0/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/Conveyor_6/Materials/Material_0/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f]
               *   Connected: '/World/Conveyor_6/Materials/Material_0/tex_base.outputs:rgb' @ '/World/Conveyor_6/Materials/Material_0/tex_base'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/Material_0_baseColor.jpg'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(1.000, 1.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0.892971'
       *   '/World/Conveyor_6/Materials/Material_0/tex_base' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/Material_0_baseColor.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
           *   'file' [asset] = '0/Material_0_baseColor.jpg'
           *   'st' [float2]
               *   Connected: '/World/Conveyor_6/Materials/Material_0/uvset0.outputs:result' @ '/World/Conveyor_6/Materials/Material_0/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/Conveyor_6/Materials/Material_0/uvset0' (ID: 'UsdPrimvarReader_float2')
       *   Implementation: 'id'


---


### /World/Conveyor_7/Materials/Material_0
*  **Prim路径 (Prim Path):**/World/Conveyor_7/Materials/Material_0
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/Conveyor_7/Materials/Material_0/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/Conveyor_7/Materials/Material_0/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f]
               *   Connected: '/World/Conveyor_7/Materials/Material_0/tex_base.outputs:rgb' @ '/World/Conveyor_7/Materials/Material_0/tex_base'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/Material_0_baseColor.jpg'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(1.000, 1.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0.892971'
       *   '/World/Conveyor_7/Materials/Material_0/tex_base' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/Material_0_baseColor.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
           *   'file' [asset] = '0/Material_0_baseColor.jpg'
           *   'st' [float2]
               *   Connected: '/World/Conveyor_7/Materials/Material_0/uvset0.outputs:result' @ '/World/Conveyor_7/Materials/Material_0/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/Conveyor_7/Materials/Material_0/uvset0' (ID: 'UsdPrimvarReader_float2')
       *   Implementation: 'id'


---


### /World/Conveyor_8/Materials/Material_0
*  **Prim路径 (Prim Path):**/World/Conveyor_8/Materials/Material_0
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/Conveyor_8/Materials/Material_0/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/Conveyor_8/Materials/Material_0/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f]
               *   Connected: '/World/Conveyor_8/Materials/Material_0/tex_base.outputs:rgb' @ '/World/Conveyor_8/Materials/Material_0/tex_base'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/Material_0_baseColor.jpg'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(1.000, 1.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0.892971'
       *   '/World/Conveyor_8/Materials/Material_0/tex_base' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/Material_0_baseColor.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
           *   'file' [asset] = '0/Material_0_baseColor.jpg'
           *   'st' [float2]
               *   Connected: '/World/Conveyor_8/Materials/Material_0/uvset0.outputs:result' @ '/World/Conveyor_8/Materials/Material_0/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/Conveyor_8/Materials/Material_0/uvset0' (ID: 'UsdPrimvarReader_float2')
       *   Implementation: 'id'


---


### /World/BoxOnConveyor_1/Materials/_6___Default
*  **Prim路径 (Prim Path):**/World/BoxOnConveyor_1/Materials/_6___Default
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/BoxOnConveyor_1/Materials/_6___Default/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/BoxOnConveyor_1/Materials/_6___Default/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f]
               *   Connected: '/World/BoxOnConveyor_1/Materials/_6___Default/tex_base.outputs:rgb' @ '/World/BoxOnConveyor_1/Materials/_6___Default/tex_base'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/06_-_Default_baseColor.jpg'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(1.000, 1.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0.892971'
       *   '/World/BoxOnConveyor_1/Materials/_6___Default/tex_base' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/06_-_Default_baseColor.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
           *   'file' [asset] = '0/06_-_Default_baseColor.jpg'
           *   'st' [float2]
               *   Connected: '/World/BoxOnConveyor_1/Materials/_6___Default/uvset0.outputs:result' @ '/World/BoxOnConveyor_1/Materials/_6___Default/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/BoxOnConveyor_1/Materials/_6___Default/uvset0' (ID: 'UsdPrimvarReader_float2')
       *   Implementation: 'id'


---


### /World/BoxOnConveyor_2/Materials/_6___Default
*  **Prim路径 (Prim Path):**/World/BoxOnConveyor_2/Materials/_6___Default
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/BoxOnConveyor_2/Materials/_6___Default/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/BoxOnConveyor_2/Materials/_6___Default/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f]
               *   Connected: '/World/BoxOnConveyor_2/Materials/_6___Default/tex_base.outputs:rgb' @ '/World/BoxOnConveyor_2/Materials/_6___Default/tex_base'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/06_-_Default_baseColor.jpg'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(1.000, 1.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0.892971'
       *   '/World/BoxOnConveyor_2/Materials/_6___Default/tex_base' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/06_-_Default_baseColor.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
           *   'file' [asset] = '0/06_-_Default_baseColor.jpg'
           *   'st' [float2]
               *   Connected: '/World/BoxOnConveyor_2/Materials/_6___Default/uvset0.outputs:result' @ '/World/BoxOnConveyor_2/Materials/_6___Default/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/BoxOnConveyor_2/Materials/_6___Default/uvset0' (ID: 'UsdPrimvarReader_float2')
       *   Implementation: 'id'


---


### /World/BoxOnConveyor_3/Materials/_6___Default
*  **Prim路径 (Prim Path):**/World/BoxOnConveyor_3/Materials/_6___Default
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/BoxOnConveyor_3/Materials/_6___Default/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/BoxOnConveyor_3/Materials/_6___Default/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f]
               *   Connected: '/World/BoxOnConveyor_3/Materials/_6___Default/tex_base.outputs:rgb' @ '/World/BoxOnConveyor_3/Materials/_6___Default/tex_base'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/06_-_Default_baseColor.jpg'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(1.000, 1.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0.892971'
       *   '/World/BoxOnConveyor_3/Materials/_6___Default/tex_base' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/06_-_Default_baseColor.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
           *   'file' [asset] = '0/06_-_Default_baseColor.jpg'
           *   'st' [float2]
               *   Connected: '/World/BoxOnConveyor_3/Materials/_6___Default/uvset0.outputs:result' @ '/World/BoxOnConveyor_3/Materials/_6___Default/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/BoxOnConveyor_3/Materials/_6___Default/uvset0' (ID: 'UsdPrimvarReader_float2')
       *   Implementation: 'id'


---


### /World/BoxOnConveyor_4/Materials/_6___Default
*  **Prim路径 (Prim Path):**/World/BoxOnConveyor_4/Materials/_6___Default
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/BoxOnConveyor_4/Materials/_6___Default/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/BoxOnConveyor_4/Materials/_6___Default/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f]
               *   Connected: '/World/BoxOnConveyor_4/Materials/_6___Default/tex_base.outputs:rgb' @ '/World/BoxOnConveyor_4/Materials/_6___Default/tex_base'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/06_-_Default_baseColor.jpg'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(1.000, 1.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0.892971'
       *   '/World/BoxOnConveyor_4/Materials/_6___Default/tex_base' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/06_-_Default_baseColor.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
           *   'file' [asset] = '0/06_-_Default_baseColor.jpg'
           *   'st' [float2]
               *   Connected: '/World/BoxOnConveyor_4/Materials/_6___Default/uvset0.outputs:result' @ '/World/BoxOnConveyor_4/Materials/_6___Default/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/BoxOnConveyor_4/Materials/_6___Default/uvset0' (ID: 'UsdPrimvarReader_float2')
       *   Implementation: 'id'


---


### /World/BoxOnConveyor_5/Materials/_6___Default
*  **Prim路径 (Prim Path):**/World/BoxOnConveyor_5/Materials/_6___Default
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/BoxOnConveyor_5/Materials/_6___Default/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/BoxOnConveyor_5/Materials/_6___Default/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f]
               *   Connected: '/World/BoxOnConveyor_5/Materials/_6___Default/tex_base.outputs:rgb' @ '/World/BoxOnConveyor_5/Materials/_6___Default/tex_base'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/06_-_Default_baseColor.jpg'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(1.000, 1.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0.892971'
       *   '/World/BoxOnConveyor_5/Materials/_6___Default/tex_base' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/06_-_Default_baseColor.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
           *   'file' [asset] = '0/06_-_Default_baseColor.jpg'
           *   'st' [float2]
               *   Connected: '/World/BoxOnConveyor_5/Materials/_6___Default/uvset0.outputs:result' @ '/World/BoxOnConveyor_5/Materials/_6___Default/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/BoxOnConveyor_5/Materials/_6___Default/uvset0' (ID: 'UsdPrimvarReader_float2')
       *   Implementation: 'id'


---


### /World/BoxOnConveyor_6/Materials/_6___Default
*  **Prim路径 (Prim Path):**/World/BoxOnConveyor_6/Materials/_6___Default
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/BoxOnConveyor_6/Materials/_6___Default/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/BoxOnConveyor_6/Materials/_6___Default/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f]
               *   Connected: '/World/BoxOnConveyor_6/Materials/_6___Default/tex_base.outputs:rgb' @ '/World/BoxOnConveyor_6/Materials/_6___Default/tex_base'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/06_-_Default_baseColor.jpg'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(1.000, 1.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0.892971'
       *   '/World/BoxOnConveyor_6/Materials/_6___Default/tex_base' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/06_-_Default_baseColor.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
           *   'file' [asset] = '0/06_-_Default_baseColor.jpg'
           *   'st' [float2]
               *   Connected: '/World/BoxOnConveyor_6/Materials/_6___Default/uvset0.outputs:result' @ '/World/BoxOnConveyor_6/Materials/_6___Default/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/BoxOnConveyor_6/Materials/_6___Default/uvset0' (ID: 'UsdPrimvarReader_float2')
       *   Implementation: 'id'


---


### /World/BoxOnConveyor_7/Materials/_6___Default
*  **Prim路径 (Prim Path):**/World/BoxOnConveyor_7/Materials/_6___Default
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/BoxOnConveyor_7/Materials/_6___Default/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/BoxOnConveyor_7/Materials/_6___Default/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f]
               *   Connected: '/World/BoxOnConveyor_7/Materials/_6___Default/tex_base.outputs:rgb' @ '/World/BoxOnConveyor_7/Materials/_6___Default/tex_base'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/06_-_Default_baseColor.jpg'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(1.000, 1.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0.892971'
       *   '/World/BoxOnConveyor_7/Materials/_6___Default/tex_base' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/06_-_Default_baseColor.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
           *   'file' [asset] = '0/06_-_Default_baseColor.jpg'
           *   'st' [float2]
               *   Connected: '/World/BoxOnConveyor_7/Materials/_6___Default/uvset0.outputs:result' @ '/World/BoxOnConveyor_7/Materials/_6___Default/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/BoxOnConveyor_7/Materials/_6___Default/uvset0' (ID: 'UsdPrimvarReader_float2')
       *   Implementation: 'id'


---


### /World/BoxOnConveyor_8/Materials/_6___Default
*  **Prim路径 (Prim Path):**/World/BoxOnConveyor_8/Materials/_6___Default
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/BoxOnConveyor_8/Materials/_6___Default/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/BoxOnConveyor_8/Materials/_6___Default/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f]
               *   Connected: '/World/BoxOnConveyor_8/Materials/_6___Default/tex_base.outputs:rgb' @ '/World/BoxOnConveyor_8/Materials/_6___Default/tex_base'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/06_-_Default_baseColor.jpg'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(1.000, 1.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0.892971'
       *   '/World/BoxOnConveyor_8/Materials/_6___Default/tex_base' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/06_-_Default_baseColor.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
           *   'file' [asset] = '0/06_-_Default_baseColor.jpg'
           *   'st' [float2]
               *   Connected: '/World/BoxOnConveyor_8/Materials/_6___Default/uvset0.outputs:result' @ '/World/BoxOnConveyor_8/Materials/_6___Default/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/BoxOnConveyor_8/Materials/_6___Default/uvset0' (ID: 'UsdPrimvarReader_float2')
       *   Implementation: 'id'


---


### /World/BoxOnConveyor_9/Materials/_6___Default
*  **Prim路径 (Prim Path):**/World/BoxOnConveyor_9/Materials/_6___Default
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/BoxOnConveyor_9/Materials/_6___Default/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/BoxOnConveyor_9/Materials/_6___Default/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f]
               *   Connected: '/World/BoxOnConveyor_9/Materials/_6___Default/tex_base.outputs:rgb' @ '/World/BoxOnConveyor_9/Materials/_6___Default/tex_base'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/06_-_Default_baseColor.jpg'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(1.000, 1.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0.892971'
       *   '/World/BoxOnConveyor_9/Materials/_6___Default/tex_base' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/06_-_Default_baseColor.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
           *   'file' [asset] = '0/06_-_Default_baseColor.jpg'
           *   'st' [float2]
               *   Connected: '/World/BoxOnConveyor_9/Materials/_6___Default/uvset0.outputs:result' @ '/World/BoxOnConveyor_9/Materials/_6___Default/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/BoxOnConveyor_9/Materials/_6___Default/uvset0' (ID: 'UsdPrimvarReader_float2')
       *   Implementation: 'id'


---


### /World/BoxOnConveyor_10/Materials/_6___Default
*  **Prim路径 (Prim Path):**/World/BoxOnConveyor_10/Materials/_6___Default
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/BoxOnConveyor_10/Materials/_6___Default/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/BoxOnConveyor_10/Materials/_6___Default/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f]
               *   Connected: '/World/BoxOnConveyor_10/Materials/_6___Default/tex_base.outputs:rgb' @ '/World/BoxOnConveyor_10/Materials/_6___Default/tex_base'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/06_-_Default_baseColor.jpg'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(1.000, 1.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0.892971'
       *   '/World/BoxOnConveyor_10/Materials/_6___Default/tex_base' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/06_-_Default_baseColor.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
           *   'file' [asset] = '0/06_-_Default_baseColor.jpg'
           *   'st' [float2]
               *   Connected: '/World/BoxOnConveyor_10/Materials/_6___Default/uvset0.outputs:result' @ '/World/BoxOnConveyor_10/Materials/_6___Default/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/BoxOnConveyor_10/Materials/_6___Default/uvset0' (ID: 'UsdPrimvarReader_float2')
       *   Implementation: 'id'


---


### /World/BoxOnConveyor_11/Materials/_6___Default
*  **Prim路径 (Prim Path):**/World/BoxOnConveyor_11/Materials/_6___Default
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/BoxOnConveyor_11/Materials/_6___Default/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/BoxOnConveyor_11/Materials/_6___Default/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f]
               *   Connected: '/World/BoxOnConveyor_11/Materials/_6___Default/tex_base.outputs:rgb' @ '/World/BoxOnConveyor_11/Materials/_6___Default/tex_base'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/06_-_Default_baseColor.jpg'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(1.000, 1.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0.892971'
       *   '/World/BoxOnConveyor_11/Materials/_6___Default/tex_base' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/06_-_Default_baseColor.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
           *   'file' [asset] = '0/06_-_Default_baseColor.jpg'
           *   'st' [float2]
               *   Connected: '/World/BoxOnConveyor_11/Materials/_6___Default/uvset0.outputs:result' @ '/World/BoxOnConveyor_11/Materials/_6___Default/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/BoxOnConveyor_11/Materials/_6___Default/uvset0' (ID: 'UsdPrimvarReader_float2')
       *   Implementation: 'id'


---


### /World/BoxOnConveyor_12/Materials/_6___Default
*  **Prim路径 (Prim Path):**/World/BoxOnConveyor_12/Materials/_6___Default
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/BoxOnConveyor_12/Materials/_6___Default/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/BoxOnConveyor_12/Materials/_6___Default/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f]
               *   Connected: '/World/BoxOnConveyor_12/Materials/_6___Default/tex_base.outputs:rgb' @ '/World/BoxOnConveyor_12/Materials/_6___Default/tex_base'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/06_-_Default_baseColor.jpg'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(1.000, 1.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0.892971'
       *   '/World/BoxOnConveyor_12/Materials/_6___Default/tex_base' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/06_-_Default_baseColor.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
           *   'file' [asset] = '0/06_-_Default_baseColor.jpg'
           *   'st' [float2]
               *   Connected: '/World/BoxOnConveyor_12/Materials/_6___Default/uvset0.outputs:result' @ '/World/BoxOnConveyor_12/Materials/_6___Default/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/BoxOnConveyor_12/Materials/_6___Default/uvset0' (ID: 'UsdPrimvarReader_float2')
       *   Implementation: 'id'


---


### /World/BoxOnConveyor_13/Materials/_6___Default
*  **Prim路径 (Prim Path):**/World/BoxOnConveyor_13/Materials/_6___Default
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/BoxOnConveyor_13/Materials/_6___Default/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/BoxOnConveyor_13/Materials/_6___Default/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f]
               *   Connected: '/World/BoxOnConveyor_13/Materials/_6___Default/tex_base.outputs:rgb' @ '/World/BoxOnConveyor_13/Materials/_6___Default/tex_base'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/06_-_Default_baseColor.jpg'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(1.000, 1.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0.892971'
       *   '/World/BoxOnConveyor_13/Materials/_6___Default/tex_base' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/06_-_Default_baseColor.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
           *   'file' [asset] = '0/06_-_Default_baseColor.jpg'
           *   'st' [float2]
               *   Connected: '/World/BoxOnConveyor_13/Materials/_6___Default/uvset0.outputs:result' @ '/World/BoxOnConveyor_13/Materials/_6___Default/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/BoxOnConveyor_13/Materials/_6___Default/uvset0' (ID: 'UsdPrimvarReader_float2')
       *   Implementation: 'id'


---


### /World/BoxOnConveyor_14/Materials/_6___Default
*  **Prim路径 (Prim Path):**/World/BoxOnConveyor_14/Materials/_6___Default
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/BoxOnConveyor_14/Materials/_6___Default/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/BoxOnConveyor_14/Materials/_6___Default/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f]
               *   Connected: '/World/BoxOnConveyor_14/Materials/_6___Default/tex_base.outputs:rgb' @ '/World/BoxOnConveyor_14/Materials/_6___Default/tex_base'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/06_-_Default_baseColor.jpg'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(1.000, 1.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0.892971'
       *   '/World/BoxOnConveyor_14/Materials/_6___Default/tex_base' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/06_-_Default_baseColor.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
           *   'file' [asset] = '0/06_-_Default_baseColor.jpg'
           *   'st' [float2]
               *   Connected: '/World/BoxOnConveyor_14/Materials/_6___Default/uvset0.outputs:result' @ '/World/BoxOnConveyor_14/Materials/_6___Default/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/BoxOnConveyor_14/Materials/_6___Default/uvset0' (ID: 'UsdPrimvarReader_float2')
       *   Implementation: 'id'


---


### /World/BoxOnConveyor_15/Materials/_6___Default
*  **Prim路径 (Prim Path):**/World/BoxOnConveyor_15/Materials/_6___Default
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/BoxOnConveyor_15/Materials/_6___Default/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/BoxOnConveyor_15/Materials/_6___Default/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f]
               *   Connected: '/World/BoxOnConveyor_15/Materials/_6___Default/tex_base.outputs:rgb' @ '/World/BoxOnConveyor_15/Materials/_6___Default/tex_base'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/06_-_Default_baseColor.jpg'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(1.000, 1.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0.892971'
       *   '/World/BoxOnConveyor_15/Materials/_6___Default/tex_base' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/06_-_Default_baseColor.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
           *   'file' [asset] = '0/06_-_Default_baseColor.jpg'
           *   'st' [float2]
               *   Connected: '/World/BoxOnConveyor_15/Materials/_6___Default/uvset0.outputs:result' @ '/World/BoxOnConveyor_15/Materials/_6___Default/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/BoxOnConveyor_15/Materials/_6___Default/uvset0' (ID: 'UsdPrimvarReader_float2')
       *   Implementation: 'id'


---


### /World/BoxOnConveyor_16/Materials/_6___Default
*  **Prim路径 (Prim Path):**/World/BoxOnConveyor_16/Materials/_6___Default
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/BoxOnConveyor_16/Materials/_6___Default/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/BoxOnConveyor_16/Materials/_6___Default/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f]
               *   Connected: '/World/BoxOnConveyor_16/Materials/_6___Default/tex_base.outputs:rgb' @ '/World/BoxOnConveyor_16/Materials/_6___Default/tex_base'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/06_-_Default_baseColor.jpg'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(1.000, 1.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0.892971'
       *   '/World/BoxOnConveyor_16/Materials/_6___Default/tex_base' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/06_-_Default_baseColor.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
           *   'file' [asset] = '0/06_-_Default_baseColor.jpg'
           *   'st' [float2]
               *   Connected: '/World/BoxOnConveyor_16/Materials/_6___Default/uvset0.outputs:result' @ '/World/BoxOnConveyor_16/Materials/_6___Default/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/BoxOnConveyor_16/Materials/_6___Default/uvset0' (ID: 'UsdPrimvarReader_float2')
       *   Implementation: 'id'


---


### /World/BoxOnConveyor_17/Materials/_6___Default
*  **Prim路径 (Prim Path):**/World/BoxOnConveyor_17/Materials/_6___Default
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/BoxOnConveyor_17/Materials/_6___Default/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/BoxOnConveyor_17/Materials/_6___Default/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f]
               *   Connected: '/World/BoxOnConveyor_17/Materials/_6___Default/tex_base.outputs:rgb' @ '/World/BoxOnConveyor_17/Materials/_6___Default/tex_base'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/06_-_Default_baseColor.jpg'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(1.000, 1.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0.892971'
       *   '/World/BoxOnConveyor_17/Materials/_6___Default/tex_base' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/06_-_Default_baseColor.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
           *   'file' [asset] = '0/06_-_Default_baseColor.jpg'
           *   'st' [float2]
               *   Connected: '/World/BoxOnConveyor_17/Materials/_6___Default/uvset0.outputs:result' @ '/World/BoxOnConveyor_17/Materials/_6___Default/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/BoxOnConveyor_17/Materials/_6___Default/uvset0' (ID: 'UsdPrimvarReader_float2')
       *   Implementation: 'id'


---


### /World/BoxOnConveyor_18/Materials/_6___Default
*  **Prim路径 (Prim Path):**/World/BoxOnConveyor_18/Materials/_6___Default
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/BoxOnConveyor_18/Materials/_6___Default/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/BoxOnConveyor_18/Materials/_6___Default/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f]
               *   Connected: '/World/BoxOnConveyor_18/Materials/_6___Default/tex_base.outputs:rgb' @ '/World/BoxOnConveyor_18/Materials/_6___Default/tex_base'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/06_-_Default_baseColor.jpg'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(1.000, 1.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0.892971'
       *   '/World/BoxOnConveyor_18/Materials/_6___Default/tex_base' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/06_-_Default_baseColor.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
           *   'file' [asset] = '0/06_-_Default_baseColor.jpg'
           *   'st' [float2]
               *   Connected: '/World/BoxOnConveyor_18/Materials/_6___Default/uvset0.outputs:result' @ '/World/BoxOnConveyor_18/Materials/_6___Default/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/BoxOnConveyor_18/Materials/_6___Default/uvset0' (ID: 'UsdPrimvarReader_float2')
       *   Implementation: 'id'


---


### /World/BoxOnConveyor_19/Materials/_6___Default
*  **Prim路径 (Prim Path):**/World/BoxOnConveyor_19/Materials/_6___Default
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/BoxOnConveyor_19/Materials/_6___Default/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/BoxOnConveyor_19/Materials/_6___Default/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f]
               *   Connected: '/World/BoxOnConveyor_19/Materials/_6___Default/tex_base.outputs:rgb' @ '/World/BoxOnConveyor_19/Materials/_6___Default/tex_base'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/06_-_Default_baseColor.jpg'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(1.000, 1.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0.892971'
       *   '/World/BoxOnConveyor_19/Materials/_6___Default/tex_base' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/06_-_Default_baseColor.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
           *   'file' [asset] = '0/06_-_Default_baseColor.jpg'
           *   'st' [float2]
               *   Connected: '/World/BoxOnConveyor_19/Materials/_6___Default/uvset0.outputs:result' @ '/World/BoxOnConveyor_19/Materials/_6___Default/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/BoxOnConveyor_19/Materials/_6___Default/uvset0' (ID: 'UsdPrimvarReader_float2')
       *   Implementation: 'id'


---


### /World/BoxOnConveyor_20/Materials/_6___Default
*  **Prim路径 (Prim Path):**/World/BoxOnConveyor_20/Materials/_6___Default
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/BoxOnConveyor_20/Materials/_6___Default/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/BoxOnConveyor_20/Materials/_6___Default/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f]
               *   Connected: '/World/BoxOnConveyor_20/Materials/_6___Default/tex_base.outputs:rgb' @ '/World/BoxOnConveyor_20/Materials/_6___Default/tex_base'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/06_-_Default_baseColor.jpg'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(1.000, 1.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0.892971'
       *   '/World/BoxOnConveyor_20/Materials/_6___Default/tex_base' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/06_-_Default_baseColor.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
           *   'file' [asset] = '0/06_-_Default_baseColor.jpg'
           *   'st' [float2]
               *   Connected: '/World/BoxOnConveyor_20/Materials/_6___Default/uvset0.outputs:result' @ '/World/BoxOnConveyor_20/Materials/_6___Default/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/BoxOnConveyor_20/Materials/_6___Default/uvset0' (ID: 'UsdPrimvarReader_float2')
       *   Implementation: 'id'


---


### /World/BoxOnConveyor_21/Materials/_6___Default
*  **Prim路径 (Prim Path):**/World/BoxOnConveyor_21/Materials/_6___Default
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/BoxOnConveyor_21/Materials/_6___Default/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/BoxOnConveyor_21/Materials/_6___Default/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f]
               *   Connected: '/World/BoxOnConveyor_21/Materials/_6___Default/tex_base.outputs:rgb' @ '/World/BoxOnConveyor_21/Materials/_6___Default/tex_base'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/06_-_Default_baseColor.jpg'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(1.000, 1.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0.892971'
       *   '/World/BoxOnConveyor_21/Materials/_6___Default/tex_base' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/06_-_Default_baseColor.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
           *   'file' [asset] = '0/06_-_Default_baseColor.jpg'
           *   'st' [float2]
               *   Connected: '/World/BoxOnConveyor_21/Materials/_6___Default/uvset0.outputs:result' @ '/World/BoxOnConveyor_21/Materials/_6___Default/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/BoxOnConveyor_21/Materials/_6___Default/uvset0' (ID: 'UsdPrimvarReader_float2')
       *   Implementation: 'id'


---


### /World/BoxOnConveyor_22/Materials/_6___Default
*  **Prim路径 (Prim Path):**/World/BoxOnConveyor_22/Materials/_6___Default
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/BoxOnConveyor_22/Materials/_6___Default/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/BoxOnConveyor_22/Materials/_6___Default/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f]
               *   Connected: '/World/BoxOnConveyor_22/Materials/_6___Default/tex_base.outputs:rgb' @ '/World/BoxOnConveyor_22/Materials/_6___Default/tex_base'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/06_-_Default_baseColor.jpg'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(1.000, 1.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0.892971'
       *   '/World/BoxOnConveyor_22/Materials/_6___Default/tex_base' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/06_-_Default_baseColor.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
           *   'file' [asset] = '0/06_-_Default_baseColor.jpg'
           *   'st' [float2]
               *   Connected: '/World/BoxOnConveyor_22/Materials/_6___Default/uvset0.outputs:result' @ '/World/BoxOnConveyor_22/Materials/_6___Default/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/BoxOnConveyor_22/Materials/_6___Default/uvset0' (ID: 'UsdPrimvarReader_float2')
       *   Implementation: 'id'


---


### /World/BoxOnConveyor_23/Materials/_6___Default
*  **Prim路径 (Prim Path):**/World/BoxOnConveyor_23/Materials/_6___Default
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/BoxOnConveyor_23/Materials/_6___Default/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/BoxOnConveyor_23/Materials/_6___Default/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f]
               *   Connected: '/World/BoxOnConveyor_23/Materials/_6___Default/tex_base.outputs:rgb' @ '/World/BoxOnConveyor_23/Materials/_6___Default/tex_base'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/06_-_Default_baseColor.jpg'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(1.000, 1.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0.892971'
       *   '/World/BoxOnConveyor_23/Materials/_6___Default/tex_base' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/06_-_Default_baseColor.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
           *   'file' [asset] = '0/06_-_Default_baseColor.jpg'
           *   'st' [float2]
               *   Connected: '/World/BoxOnConveyor_23/Materials/_6___Default/uvset0.outputs:result' @ '/World/BoxOnConveyor_23/Materials/_6___Default/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/BoxOnConveyor_23/Materials/_6___Default/uvset0' (ID: 'UsdPrimvarReader_float2')
       *   Implementation: 'id'


---


### /World/BoxOnConveyor_24/Materials/_6___Default
*  **Prim路径 (Prim Path):**/World/BoxOnConveyor_24/Materials/_6___Default
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/BoxOnConveyor_24/Materials/_6___Default/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/BoxOnConveyor_24/Materials/_6___Default/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f]
               *   Connected: '/World/BoxOnConveyor_24/Materials/_6___Default/tex_base.outputs:rgb' @ '/World/BoxOnConveyor_24/Materials/_6___Default/tex_base'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/06_-_Default_baseColor.jpg'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(1.000, 1.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0.892971'
       *   '/World/BoxOnConveyor_24/Materials/_6___Default/tex_base' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/06_-_Default_baseColor.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
           *   'file' [asset] = '0/06_-_Default_baseColor.jpg'
           *   'st' [float2]
               *   Connected: '/World/BoxOnConveyor_24/Materials/_6___Default/uvset0.outputs:result' @ '/World/BoxOnConveyor_24/Materials/_6___Default/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/BoxOnConveyor_24/Materials/_6___Default/uvset0' (ID: 'UsdPrimvarReader_float2')
       *   Implementation: 'id'


---


### /World/BoxOnConveyor_25/Materials/_6___Default
*  **Prim路径 (Prim Path):**/World/BoxOnConveyor_25/Materials/_6___Default
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/BoxOnConveyor_25/Materials/_6___Default/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/BoxOnConveyor_25/Materials/_6___Default/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f]
               *   Connected: '/World/BoxOnConveyor_25/Materials/_6___Default/tex_base.outputs:rgb' @ '/World/BoxOnConveyor_25/Materials/_6___Default/tex_base'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/06_-_Default_baseColor.jpg'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(1.000, 1.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0.892971'
       *   '/World/BoxOnConveyor_25/Materials/_6___Default/tex_base' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/06_-_Default_baseColor.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
           *   'file' [asset] = '0/06_-_Default_baseColor.jpg'
           *   'st' [float2]
               *   Connected: '/World/BoxOnConveyor_25/Materials/_6___Default/uvset0.outputs:result' @ '/World/BoxOnConveyor_25/Materials/_6___Default/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/BoxOnConveyor_25/Materials/_6___Default/uvset0' (ID: 'UsdPrimvarReader_float2')
       *   Implementation: 'id'


---


### /World/BoxOnConveyor_26/Materials/_6___Default
*  **Prim路径 (Prim Path):**/World/BoxOnConveyor_26/Materials/_6___Default
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/BoxOnConveyor_26/Materials/_6___Default/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/BoxOnConveyor_26/Materials/_6___Default/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f]
               *   Connected: '/World/BoxOnConveyor_26/Materials/_6___Default/tex_base.outputs:rgb' @ '/World/BoxOnConveyor_26/Materials/_6___Default/tex_base'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/06_-_Default_baseColor.jpg'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(1.000, 1.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0.892971'
       *   '/World/BoxOnConveyor_26/Materials/_6___Default/tex_base' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/06_-_Default_baseColor.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
           *   'file' [asset] = '0/06_-_Default_baseColor.jpg'
           *   'st' [float2]
               *   Connected: '/World/BoxOnConveyor_26/Materials/_6___Default/uvset0.outputs:result' @ '/World/BoxOnConveyor_26/Materials/_6___Default/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/BoxOnConveyor_26/Materials/_6___Default/uvset0' (ID: 'UsdPrimvarReader_float2')
       *   Implementation: 'id'


---


### /World/BoxOnConveyor_27/Materials/_6___Default
*  **Prim路径 (Prim Path):**/World/BoxOnConveyor_27/Materials/_6___Default
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/BoxOnConveyor_27/Materials/_6___Default/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/BoxOnConveyor_27/Materials/_6___Default/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f]
               *   Connected: '/World/BoxOnConveyor_27/Materials/_6___Default/tex_base.outputs:rgb' @ '/World/BoxOnConveyor_27/Materials/_6___Default/tex_base'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/06_-_Default_baseColor.jpg'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(1.000, 1.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0.892971'
       *   '/World/BoxOnConveyor_27/Materials/_6___Default/tex_base' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/06_-_Default_baseColor.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
           *   'file' [asset] = '0/06_-_Default_baseColor.jpg'
           *   'st' [float2]
               *   Connected: '/World/BoxOnConveyor_27/Materials/_6___Default/uvset0.outputs:result' @ '/World/BoxOnConveyor_27/Materials/_6___Default/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/BoxOnConveyor_27/Materials/_6___Default/uvset0' (ID: 'UsdPrimvarReader_float2')
       *   Implementation: 'id'


---


### /World/BoxOnConveyor_28/Materials/_6___Default
*  **Prim路径 (Prim Path):**/World/BoxOnConveyor_28/Materials/_6___Default
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/BoxOnConveyor_28/Materials/_6___Default/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/BoxOnConveyor_28/Materials/_6___Default/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f]
               *   Connected: '/World/BoxOnConveyor_28/Materials/_6___Default/tex_base.outputs:rgb' @ '/World/BoxOnConveyor_28/Materials/_6___Default/tex_base'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/06_-_Default_baseColor.jpg'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(1.000, 1.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0.892971'
       *   '/World/BoxOnConveyor_28/Materials/_6___Default/tex_base' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/06_-_Default_baseColor.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
           *   'file' [asset] = '0/06_-_Default_baseColor.jpg'
           *   'st' [float2]
               *   Connected: '/World/BoxOnConveyor_28/Materials/_6___Default/uvset0.outputs:result' @ '/World/BoxOnConveyor_28/Materials/_6___Default/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/BoxOnConveyor_28/Materials/_6___Default/uvset0' (ID: 'UsdPrimvarReader_float2')
       *   Implementation: 'id'


---


### /World/BoxOnConveyor_29/Materials/_6___Default
*  **Prim路径 (Prim Path):**/World/BoxOnConveyor_29/Materials/_6___Default
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/BoxOnConveyor_29/Materials/_6___Default/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/BoxOnConveyor_29/Materials/_6___Default/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f]
               *   Connected: '/World/BoxOnConveyor_29/Materials/_6___Default/tex_base.outputs:rgb' @ '/World/BoxOnConveyor_29/Materials/_6___Default/tex_base'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/06_-_Default_baseColor.jpg'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(1.000, 1.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0.892971'
       *   '/World/BoxOnConveyor_29/Materials/_6___Default/tex_base' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/06_-_Default_baseColor.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
           *   'file' [asset] = '0/06_-_Default_baseColor.jpg'
           *   'st' [float2]
               *   Connected: '/World/BoxOnConveyor_29/Materials/_6___Default/uvset0.outputs:result' @ '/World/BoxOnConveyor_29/Materials/_6___Default/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/BoxOnConveyor_29/Materials/_6___Default/uvset0' (ID: 'UsdPrimvarReader_float2')
       *   Implementation: 'id'


---


### /World/BoxOnConveyor_30/Materials/_6___Default
*  **Prim路径 (Prim Path):**/World/BoxOnConveyor_30/Materials/_6___Default
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/BoxOnConveyor_30/Materials/_6___Default/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/BoxOnConveyor_30/Materials/_6___Default/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f]
               *   Connected: '/World/BoxOnConveyor_30/Materials/_6___Default/tex_base.outputs:rgb' @ '/World/BoxOnConveyor_30/Materials/_6___Default/tex_base'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/06_-_Default_baseColor.jpg'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(1.000, 1.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0.892971'
       *   '/World/BoxOnConveyor_30/Materials/_6___Default/tex_base' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/06_-_Default_baseColor.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
           *   'file' [asset] = '0/06_-_Default_baseColor.jpg'
           *   'st' [float2]
               *   Connected: '/World/BoxOnConveyor_30/Materials/_6___Default/uvset0.outputs:result' @ '/World/BoxOnConveyor_30/Materials/_6___Default/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/BoxOnConveyor_30/Materials/_6___Default/uvset0' (ID: 'UsdPrimvarReader_float2')
       *   Implementation: 'id'


---


### /World/BoxOnConveyor_31/Materials/_6___Default
*  **Prim路径 (Prim Path):**/World/BoxOnConveyor_31/Materials/_6___Default
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/BoxOnConveyor_31/Materials/_6___Default/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/BoxOnConveyor_31/Materials/_6___Default/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f]
               *   Connected: '/World/BoxOnConveyor_31/Materials/_6___Default/tex_base.outputs:rgb' @ '/World/BoxOnConveyor_31/Materials/_6___Default/tex_base'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/06_-_Default_baseColor.jpg'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(1.000, 1.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0.892971'
       *   '/World/BoxOnConveyor_31/Materials/_6___Default/tex_base' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/06_-_Default_baseColor.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
           *   'file' [asset] = '0/06_-_Default_baseColor.jpg'
           *   'st' [float2]
               *   Connected: '/World/BoxOnConveyor_31/Materials/_6___Default/uvset0.outputs:result' @ '/World/BoxOnConveyor_31/Materials/_6___Default/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/BoxOnConveyor_31/Materials/_6___Default/uvset0' (ID: 'UsdPrimvarReader_float2')
       *   Implementation: 'id'


---


### /World/BoxOnConveyor_32/Materials/_6___Default
*  **Prim路径 (Prim Path):**/World/BoxOnConveyor_32/Materials/_6___Default
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/BoxOnConveyor_32/Materials/_6___Default/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/BoxOnConveyor_32/Materials/_6___Default/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f]
               *   Connected: '/World/BoxOnConveyor_32/Materials/_6___Default/tex_base.outputs:rgb' @ '/World/BoxOnConveyor_32/Materials/_6___Default/tex_base'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/06_-_Default_baseColor.jpg'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(1.000, 1.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0.892971'
       *   '/World/BoxOnConveyor_32/Materials/_6___Default/tex_base' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/06_-_Default_baseColor.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
           *   'file' [asset] = '0/06_-_Default_baseColor.jpg'
           *   'st' [float2]
               *   Connected: '/World/BoxOnConveyor_32/Materials/_6___Default/uvset0.outputs:result' @ '/World/BoxOnConveyor_32/Materials/_6___Default/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/BoxOnConveyor_32/Materials/_6___Default/uvset0' (ID: 'UsdPrimvarReader_float2')
       *   Implementation: 'id'


---


### /World/BoxOnConveyor_33/Materials/_6___Default
*  **Prim路径 (Prim Path):**/World/BoxOnConveyor_33/Materials/_6___Default
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/BoxOnConveyor_33/Materials/_6___Default/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/BoxOnConveyor_33/Materials/_6___Default/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f]
               *   Connected: '/World/BoxOnConveyor_33/Materials/_6___Default/tex_base.outputs:rgb' @ '/World/BoxOnConveyor_33/Materials/_6___Default/tex_base'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/06_-_Default_baseColor.jpg'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(1.000, 1.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0.892971'
       *   '/World/BoxOnConveyor_33/Materials/_6___Default/tex_base' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/06_-_Default_baseColor.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
           *   'file' [asset] = '0/06_-_Default_baseColor.jpg'
           *   'st' [float2]
               *   Connected: '/World/BoxOnConveyor_33/Materials/_6___Default/uvset0.outputs:result' @ '/World/BoxOnConveyor_33/Materials/_6___Default/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/BoxOnConveyor_33/Materials/_6___Default/uvset0' (ID: 'UsdPrimvarReader_float2')
       *   Implementation: 'id'


---


### /World/BoxOnConveyor_34/Materials/_6___Default
*  **Prim路径 (Prim Path):**/World/BoxOnConveyor_34/Materials/_6___Default
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/BoxOnConveyor_34/Materials/_6___Default/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/BoxOnConveyor_34/Materials/_6___Default/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f]
               *   Connected: '/World/BoxOnConveyor_34/Materials/_6___Default/tex_base.outputs:rgb' @ '/World/BoxOnConveyor_34/Materials/_6___Default/tex_base'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/06_-_Default_baseColor.jpg'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(1.000, 1.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0.892971'
       *   '/World/BoxOnConveyor_34/Materials/_6___Default/tex_base' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/06_-_Default_baseColor.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
           *   'file' [asset] = '0/06_-_Default_baseColor.jpg'
           *   'st' [float2]
               *   Connected: '/World/BoxOnConveyor_34/Materials/_6___Default/uvset0.outputs:result' @ '/World/BoxOnConveyor_34/Materials/_6___Default/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/BoxOnConveyor_34/Materials/_6___Default/uvset0' (ID: 'UsdPrimvarReader_float2')
       *   Implementation: 'id'


---


### /World/BoxOnConveyor_35/Materials/_6___Default
*  **Prim路径 (Prim Path):**/World/BoxOnConveyor_35/Materials/_6___Default
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/BoxOnConveyor_35/Materials/_6___Default/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/BoxOnConveyor_35/Materials/_6___Default/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f]
               *   Connected: '/World/BoxOnConveyor_35/Materials/_6___Default/tex_base.outputs:rgb' @ '/World/BoxOnConveyor_35/Materials/_6___Default/tex_base'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/06_-_Default_baseColor.jpg'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(1.000, 1.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0.892971'
       *   '/World/BoxOnConveyor_35/Materials/_6___Default/tex_base' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/06_-_Default_baseColor.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
           *   'file' [asset] = '0/06_-_Default_baseColor.jpg'
           *   'st' [float2]
               *   Connected: '/World/BoxOnConveyor_35/Materials/_6___Default/uvset0.outputs:result' @ '/World/BoxOnConveyor_35/Materials/_6___Default/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/BoxOnConveyor_35/Materials/_6___Default/uvset0' (ID: 'UsdPrimvarReader_float2')
       *   Implementation: 'id'


---


### /World/BoxOnConveyor_36/Materials/_6___Default
*  **Prim路径 (Prim Path):**/World/BoxOnConveyor_36/Materials/_6___Default
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/BoxOnConveyor_36/Materials/_6___Default/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/BoxOnConveyor_36/Materials/_6___Default/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f]
               *   Connected: '/World/BoxOnConveyor_36/Materials/_6___Default/tex_base.outputs:rgb' @ '/World/BoxOnConveyor_36/Materials/_6___Default/tex_base'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/06_-_Default_baseColor.jpg'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(1.000, 1.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0.892971'
       *   '/World/BoxOnConveyor_36/Materials/_6___Default/tex_base' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/06_-_Default_baseColor.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
           *   'file' [asset] = '0/06_-_Default_baseColor.jpg'
           *   'st' [float2]
               *   Connected: '/World/BoxOnConveyor_36/Materials/_6___Default/uvset0.outputs:result' @ '/World/BoxOnConveyor_36/Materials/_6___Default/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/BoxOnConveyor_36/Materials/_6___Default/uvset0' (ID: 'UsdPrimvarReader_float2')
       *   Implementation: 'id'


---


### /World/BoxOnConveyor_37/Materials/_6___Default
*  **Prim路径 (Prim Path):**/World/BoxOnConveyor_37/Materials/_6___Default
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/BoxOnConveyor_37/Materials/_6___Default/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/BoxOnConveyor_37/Materials/_6___Default/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f]
               *   Connected: '/World/BoxOnConveyor_37/Materials/_6___Default/tex_base.outputs:rgb' @ '/World/BoxOnConveyor_37/Materials/_6___Default/tex_base'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/06_-_Default_baseColor.jpg'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(1.000, 1.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0.892971'
       *   '/World/BoxOnConveyor_37/Materials/_6___Default/tex_base' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/06_-_Default_baseColor.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
           *   'file' [asset] = '0/06_-_Default_baseColor.jpg'
           *   'st' [float2]
               *   Connected: '/World/BoxOnConveyor_37/Materials/_6___Default/uvset0.outputs:result' @ '/World/BoxOnConveyor_37/Materials/_6___Default/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/BoxOnConveyor_37/Materials/_6___Default/uvset0' (ID: 'UsdPrimvarReader_float2')
       *   Implementation: 'id'


---


### /World/BoxOnConveyor_38/Materials/_6___Default
*  **Prim路径 (Prim Path):**/World/BoxOnConveyor_38/Materials/_6___Default
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/BoxOnConveyor_38/Materials/_6___Default/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/BoxOnConveyor_38/Materials/_6___Default/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f]
               *   Connected: '/World/BoxOnConveyor_38/Materials/_6___Default/tex_base.outputs:rgb' @ '/World/BoxOnConveyor_38/Materials/_6___Default/tex_base'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/06_-_Default_baseColor.jpg'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(1.000, 1.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0.892971'
       *   '/World/BoxOnConveyor_38/Materials/_6___Default/tex_base' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/06_-_Default_baseColor.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
           *   'file' [asset] = '0/06_-_Default_baseColor.jpg'
           *   'st' [float2]
               *   Connected: '/World/BoxOnConveyor_38/Materials/_6___Default/uvset0.outputs:result' @ '/World/BoxOnConveyor_38/Materials/_6___Default/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/BoxOnConveyor_38/Materials/_6___Default/uvset0' (ID: 'UsdPrimvarReader_float2')
       *   Implementation: 'id'


---


### /World/BoxOnConveyor_39/Materials/_6___Default
*  **Prim路径 (Prim Path):**/World/BoxOnConveyor_39/Materials/_6___Default
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/BoxOnConveyor_39/Materials/_6___Default/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/BoxOnConveyor_39/Materials/_6___Default/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f]
               *   Connected: '/World/BoxOnConveyor_39/Materials/_6___Default/tex_base.outputs:rgb' @ '/World/BoxOnConveyor_39/Materials/_6___Default/tex_base'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/06_-_Default_baseColor.jpg'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(1.000, 1.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0.892971'
       *   '/World/BoxOnConveyor_39/Materials/_6___Default/tex_base' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/06_-_Default_baseColor.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
           *   'file' [asset] = '0/06_-_Default_baseColor.jpg'
           *   'st' [float2]
               *   Connected: '/World/BoxOnConveyor_39/Materials/_6___Default/uvset0.outputs:result' @ '/World/BoxOnConveyor_39/Materials/_6___Default/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/BoxOnConveyor_39/Materials/_6___Default/uvset0' (ID: 'UsdPrimvarReader_float2')
       *   Implementation: 'id'


---


### /World/BoxOnConveyor_40/Materials/_6___Default
*  **Prim路径 (Prim Path):**/World/BoxOnConveyor_40/Materials/_6___Default
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/BoxOnConveyor_40/Materials/_6___Default/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/BoxOnConveyor_40/Materials/_6___Default/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f]
               *   Connected: '/World/BoxOnConveyor_40/Materials/_6___Default/tex_base.outputs:rgb' @ '/World/BoxOnConveyor_40/Materials/_6___Default/tex_base'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/06_-_Default_baseColor.jpg'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(1.000, 1.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0.892971'
       *   '/World/BoxOnConveyor_40/Materials/_6___Default/tex_base' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/06_-_Default_baseColor.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
           *   'file' [asset] = '0/06_-_Default_baseColor.jpg'
           *   'st' [float2]
               *   Connected: '/World/BoxOnConveyor_40/Materials/_6___Default/uvset0.outputs:result' @ '/World/BoxOnConveyor_40/Materials/_6___Default/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/BoxOnConveyor_40/Materials/_6___Default/uvset0' (ID: 'UsdPrimvarReader_float2')
       *   Implementation: 'id'


---


### /World/BoxOnConveyor_41/Materials/_6___Default
*  **Prim路径 (Prim Path):**/World/BoxOnConveyor_41/Materials/_6___Default
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/BoxOnConveyor_41/Materials/_6___Default/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/BoxOnConveyor_41/Materials/_6___Default/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f]
               *   Connected: '/World/BoxOnConveyor_41/Materials/_6___Default/tex_base.outputs:rgb' @ '/World/BoxOnConveyor_41/Materials/_6___Default/tex_base'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/06_-_Default_baseColor.jpg'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(1.000, 1.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0.892971'
       *   '/World/BoxOnConveyor_41/Materials/_6___Default/tex_base' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/06_-_Default_baseColor.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
           *   'file' [asset] = '0/06_-_Default_baseColor.jpg'
           *   'st' [float2]
               *   Connected: '/World/BoxOnConveyor_41/Materials/_6___Default/uvset0.outputs:result' @ '/World/BoxOnConveyor_41/Materials/_6___Default/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/BoxOnConveyor_41/Materials/_6___Default/uvset0' (ID: 'UsdPrimvarReader_float2')
       *   Implementation: 'id'


---


### /World/BoxOnConveyor_42/Materials/_6___Default
*  **Prim路径 (Prim Path):**/World/BoxOnConveyor_42/Materials/_6___Default
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/BoxOnConveyor_42/Materials/_6___Default/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/BoxOnConveyor_42/Materials/_6___Default/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f]
               *   Connected: '/World/BoxOnConveyor_42/Materials/_6___Default/tex_base.outputs:rgb' @ '/World/BoxOnConveyor_42/Materials/_6___Default/tex_base'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/06_-_Default_baseColor.jpg'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(1.000, 1.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0.892971'
       *   '/World/BoxOnConveyor_42/Materials/_6___Default/tex_base' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/06_-_Default_baseColor.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
           *   'file' [asset] = '0/06_-_Default_baseColor.jpg'
           *   'st' [float2]
               *   Connected: '/World/BoxOnConveyor_42/Materials/_6___Default/uvset0.outputs:result' @ '/World/BoxOnConveyor_42/Materials/_6___Default/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/BoxOnConveyor_42/Materials/_6___Default/uvset0' (ID: 'UsdPrimvarReader_float2')
       *   Implementation: 'id'


---


### /World/BoxOnConveyor_43/Materials/_6___Default
*  **Prim路径 (Prim Path):**/World/BoxOnConveyor_43/Materials/_6___Default
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/BoxOnConveyor_43/Materials/_6___Default/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/BoxOnConveyor_43/Materials/_6___Default/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f]
               *   Connected: '/World/BoxOnConveyor_43/Materials/_6___Default/tex_base.outputs:rgb' @ '/World/BoxOnConveyor_43/Materials/_6___Default/tex_base'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/06_-_Default_baseColor.jpg'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(1.000, 1.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0.892971'
       *   '/World/BoxOnConveyor_43/Materials/_6___Default/tex_base' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/06_-_Default_baseColor.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
           *   'file' [asset] = '0/06_-_Default_baseColor.jpg'
           *   'st' [float2]
               *   Connected: '/World/BoxOnConveyor_43/Materials/_6___Default/uvset0.outputs:result' @ '/World/BoxOnConveyor_43/Materials/_6___Default/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/BoxOnConveyor_43/Materials/_6___Default/uvset0' (ID: 'UsdPrimvarReader_float2')
       *   Implementation: 'id'


---


### /World/BoxOnConveyor_44/Materials/_6___Default
*  **Prim路径 (Prim Path):**/World/BoxOnConveyor_44/Materials/_6___Default
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/BoxOnConveyor_44/Materials/_6___Default/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/BoxOnConveyor_44/Materials/_6___Default/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f]
               *   Connected: '/World/BoxOnConveyor_44/Materials/_6___Default/tex_base.outputs:rgb' @ '/World/BoxOnConveyor_44/Materials/_6___Default/tex_base'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/06_-_Default_baseColor.jpg'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(1.000, 1.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0.892971'
       *   '/World/BoxOnConveyor_44/Materials/_6___Default/tex_base' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/06_-_Default_baseColor.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
           *   'file' [asset] = '0/06_-_Default_baseColor.jpg'
           *   'st' [float2]
               *   Connected: '/World/BoxOnConveyor_44/Materials/_6___Default/uvset0.outputs:result' @ '/World/BoxOnConveyor_44/Materials/_6___Default/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/BoxOnConveyor_44/Materials/_6___Default/uvset0' (ID: 'UsdPrimvarReader_float2')
       *   Implementation: 'id'


---


### /World/BoxOnConveyor_45/Materials/_6___Default
*  **Prim路径 (Prim Path):**/World/BoxOnConveyor_45/Materials/_6___Default
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/BoxOnConveyor_45/Materials/_6___Default/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/BoxOnConveyor_45/Materials/_6___Default/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f]
               *   Connected: '/World/BoxOnConveyor_45/Materials/_6___Default/tex_base.outputs:rgb' @ '/World/BoxOnConveyor_45/Materials/_6___Default/tex_base'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/06_-_Default_baseColor.jpg'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(1.000, 1.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0.892971'
       *   '/World/BoxOnConveyor_45/Materials/_6___Default/tex_base' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/06_-_Default_baseColor.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
           *   'file' [asset] = '0/06_-_Default_baseColor.jpg'
           *   'st' [float2]
               *   Connected: '/World/BoxOnConveyor_45/Materials/_6___Default/uvset0.outputs:result' @ '/World/BoxOnConveyor_45/Materials/_6___Default/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/BoxOnConveyor_45/Materials/_6___Default/uvset0' (ID: 'UsdPrimvarReader_float2')
       *   Implementation: 'id'


---


### /World/BoxOnConveyor_46/Materials/_6___Default
*  **Prim路径 (Prim Path):**/World/BoxOnConveyor_46/Materials/_6___Default
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/BoxOnConveyor_46/Materials/_6___Default/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/BoxOnConveyor_46/Materials/_6___Default/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f]
               *   Connected: '/World/BoxOnConveyor_46/Materials/_6___Default/tex_base.outputs:rgb' @ '/World/BoxOnConveyor_46/Materials/_6___Default/tex_base'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/06_-_Default_baseColor.jpg'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(1.000, 1.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0.892971'
       *   '/World/BoxOnConveyor_46/Materials/_6___Default/tex_base' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/06_-_Default_baseColor.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
           *   'file' [asset] = '0/06_-_Default_baseColor.jpg'
           *   'st' [float2]
               *   Connected: '/World/BoxOnConveyor_46/Materials/_6___Default/uvset0.outputs:result' @ '/World/BoxOnConveyor_46/Materials/_6___Default/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/BoxOnConveyor_46/Materials/_6___Default/uvset0' (ID: 'UsdPrimvarReader_float2')
       *   Implementation: 'id'


---


### /World/BoxOnConveyor_47/Materials/_6___Default
*  **Prim路径 (Prim Path):**/World/BoxOnConveyor_47/Materials/_6___Default
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/BoxOnConveyor_47/Materials/_6___Default/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/BoxOnConveyor_47/Materials/_6___Default/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f]
               *   Connected: '/World/BoxOnConveyor_47/Materials/_6___Default/tex_base.outputs:rgb' @ '/World/BoxOnConveyor_47/Materials/_6___Default/tex_base'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/06_-_Default_baseColor.jpg'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(1.000, 1.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0.892971'
       *   '/World/BoxOnConveyor_47/Materials/_6___Default/tex_base' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/06_-_Default_baseColor.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
           *   'file' [asset] = '0/06_-_Default_baseColor.jpg'
           *   'st' [float2]
               *   Connected: '/World/BoxOnConveyor_47/Materials/_6___Default/uvset0.outputs:result' @ '/World/BoxOnConveyor_47/Materials/_6___Default/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/BoxOnConveyor_47/Materials/_6___Default/uvset0' (ID: 'UsdPrimvarReader_float2')
       *   Implementation: 'id'


---


### /World/BoxOnConveyor_48/Materials/_6___Default
*  **Prim路径 (Prim Path):**/World/BoxOnConveyor_48/Materials/_6___Default
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/BoxOnConveyor_48/Materials/_6___Default/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/BoxOnConveyor_48/Materials/_6___Default/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f]
               *   Connected: '/World/BoxOnConveyor_48/Materials/_6___Default/tex_base.outputs:rgb' @ '/World/BoxOnConveyor_48/Materials/_6___Default/tex_base'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/06_-_Default_baseColor.jpg'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(1.000, 1.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0.892971'
       *   '/World/BoxOnConveyor_48/Materials/_6___Default/tex_base' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/06_-_Default_baseColor.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
           *   'file' [asset] = '0/06_-_Default_baseColor.jpg'
           *   'st' [float2]
               *   Connected: '/World/BoxOnConveyor_48/Materials/_6___Default/uvset0.outputs:result' @ '/World/BoxOnConveyor_48/Materials/_6___Default/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/BoxOnConveyor_48/Materials/_6___Default/uvset0' (ID: 'UsdPrimvarReader_float2')
       *   Implementation: 'id'


---


### /World/BoxOnConveyor_49/Materials/_6___Default
*  **Prim路径 (Prim Path):**/World/BoxOnConveyor_49/Materials/_6___Default
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/BoxOnConveyor_49/Materials/_6___Default/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/BoxOnConveyor_49/Materials/_6___Default/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f]
               *   Connected: '/World/BoxOnConveyor_49/Materials/_6___Default/tex_base.outputs:rgb' @ '/World/BoxOnConveyor_49/Materials/_6___Default/tex_base'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/06_-_Default_baseColor.jpg'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(1.000, 1.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0.892971'
       *   '/World/BoxOnConveyor_49/Materials/_6___Default/tex_base' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/06_-_Default_baseColor.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
           *   'file' [asset] = '0/06_-_Default_baseColor.jpg'
           *   'st' [float2]
               *   Connected: '/World/BoxOnConveyor_49/Materials/_6___Default/uvset0.outputs:result' @ '/World/BoxOnConveyor_49/Materials/_6___Default/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/BoxOnConveyor_49/Materials/_6___Default/uvset0' (ID: 'UsdPrimvarReader_float2')
       *   Implementation: 'id'


---


### /World/BoxOnConveyor_50/Materials/_6___Default
*  **Prim路径 (Prim Path):**/World/BoxOnConveyor_50/Materials/_6___Default
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/BoxOnConveyor_50/Materials/_6___Default/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/BoxOnConveyor_50/Materials/_6___Default/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f]
               *   Connected: '/World/BoxOnConveyor_50/Materials/_6___Default/tex_base.outputs:rgb' @ '/World/BoxOnConveyor_50/Materials/_6___Default/tex_base'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/06_-_Default_baseColor.jpg'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(1.000, 1.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0.892971'
       *   '/World/BoxOnConveyor_50/Materials/_6___Default/tex_base' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/06_-_Default_baseColor.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
           *   'file' [asset] = '0/06_-_Default_baseColor.jpg'
           *   'st' [float2]
               *   Connected: '/World/BoxOnConveyor_50/Materials/_6___Default/uvset0.outputs:result' @ '/World/BoxOnConveyor_50/Materials/_6___Default/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/BoxOnConveyor_50/Materials/_6___Default/uvset0' (ID: 'UsdPrimvarReader_float2')
       *   Implementation: 'id'


---


### /World/BoxOnConveyor_51/Materials/_6___Default
*  **Prim路径 (Prim Path):**/World/BoxOnConveyor_51/Materials/_6___Default
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/BoxOnConveyor_51/Materials/_6___Default/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/BoxOnConveyor_51/Materials/_6___Default/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f]
               *   Connected: '/World/BoxOnConveyor_51/Materials/_6___Default/tex_base.outputs:rgb' @ '/World/BoxOnConveyor_51/Materials/_6___Default/tex_base'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/06_-_Default_baseColor.jpg'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(1.000, 1.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0.892971'
       *   '/World/BoxOnConveyor_51/Materials/_6___Default/tex_base' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/06_-_Default_baseColor.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
           *   'file' [asset] = '0/06_-_Default_baseColor.jpg'
           *   'st' [float2]
               *   Connected: '/World/BoxOnConveyor_51/Materials/_6___Default/uvset0.outputs:result' @ '/World/BoxOnConveyor_51/Materials/_6___Default/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/BoxOnConveyor_51/Materials/_6___Default/uvset0' (ID: 'UsdPrimvarReader_float2')
       *   Implementation: 'id'


---


### /World/BoxOnConveyor_52/Materials/_6___Default
*  **Prim路径 (Prim Path):**/World/BoxOnConveyor_52/Materials/_6___Default
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/BoxOnConveyor_52/Materials/_6___Default/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/BoxOnConveyor_52/Materials/_6___Default/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f]
               *   Connected: '/World/BoxOnConveyor_52/Materials/_6___Default/tex_base.outputs:rgb' @ '/World/BoxOnConveyor_52/Materials/_6___Default/tex_base'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/06_-_Default_baseColor.jpg'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(1.000, 1.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0.892971'
       *   '/World/BoxOnConveyor_52/Materials/_6___Default/tex_base' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/06_-_Default_baseColor.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
           *   'file' [asset] = '0/06_-_Default_baseColor.jpg'
           *   'st' [float2]
               *   Connected: '/World/BoxOnConveyor_52/Materials/_6___Default/uvset0.outputs:result' @ '/World/BoxOnConveyor_52/Materials/_6___Default/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/BoxOnConveyor_52/Materials/_6___Default/uvset0' (ID: 'UsdPrimvarReader_float2')
       *   Implementation: 'id'


---


### /World/BoxOnConveyor_53/Materials/_6___Default
*  **Prim路径 (Prim Path):**/World/BoxOnConveyor_53/Materials/_6___Default
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/BoxOnConveyor_53/Materials/_6___Default/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/BoxOnConveyor_53/Materials/_6___Default/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f]
               *   Connected: '/World/BoxOnConveyor_53/Materials/_6___Default/tex_base.outputs:rgb' @ '/World/BoxOnConveyor_53/Materials/_6___Default/tex_base'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/06_-_Default_baseColor.jpg'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(1.000, 1.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0.892971'
       *   '/World/BoxOnConveyor_53/Materials/_6___Default/tex_base' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/06_-_Default_baseColor.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
           *   'file' [asset] = '0/06_-_Default_baseColor.jpg'
           *   'st' [float2]
               *   Connected: '/World/BoxOnConveyor_53/Materials/_6___Default/uvset0.outputs:result' @ '/World/BoxOnConveyor_53/Materials/_6___Default/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/BoxOnConveyor_53/Materials/_6___Default/uvset0' (ID: 'UsdPrimvarReader_float2')
       *   Implementation: 'id'


---


### /World/BoxOnConveyor_54/Materials/_6___Default
*  **Prim路径 (Prim Path):**/World/BoxOnConveyor_54/Materials/_6___Default
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/BoxOnConveyor_54/Materials/_6___Default/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/BoxOnConveyor_54/Materials/_6___Default/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f]
               *   Connected: '/World/BoxOnConveyor_54/Materials/_6___Default/tex_base.outputs:rgb' @ '/World/BoxOnConveyor_54/Materials/_6___Default/tex_base'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/06_-_Default_baseColor.jpg'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(1.000, 1.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0.892971'
       *   '/World/BoxOnConveyor_54/Materials/_6___Default/tex_base' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/06_-_Default_baseColor.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
           *   'file' [asset] = '0/06_-_Default_baseColor.jpg'
           *   'st' [float2]
               *   Connected: '/World/BoxOnConveyor_54/Materials/_6___Default/uvset0.outputs:result' @ '/World/BoxOnConveyor_54/Materials/_6___Default/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/BoxOnConveyor_54/Materials/_6___Default/uvset0' (ID: 'UsdPrimvarReader_float2')
       *   Implementation: 'id'


---


### /World/BoxOnConveyor_55/Materials/_6___Default
*  **Prim路径 (Prim Path):**/World/BoxOnConveyor_55/Materials/_6___Default
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/BoxOnConveyor_55/Materials/_6___Default/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/BoxOnConveyor_55/Materials/_6___Default/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f]
               *   Connected: '/World/BoxOnConveyor_55/Materials/_6___Default/tex_base.outputs:rgb' @ '/World/BoxOnConveyor_55/Materials/_6___Default/tex_base'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/06_-_Default_baseColor.jpg'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(1.000, 1.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0.892971'
       *   '/World/BoxOnConveyor_55/Materials/_6___Default/tex_base' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/06_-_Default_baseColor.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
           *   'file' [asset] = '0/06_-_Default_baseColor.jpg'
           *   'st' [float2]
               *   Connected: '/World/BoxOnConveyor_55/Materials/_6___Default/uvset0.outputs:result' @ '/World/BoxOnConveyor_55/Materials/_6___Default/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/BoxOnConveyor_55/Materials/_6___Default/uvset0' (ID: 'UsdPrimvarReader_float2')
       *   Implementation: 'id'


---


### /World/BoxOnConveyor_56/Materials/_6___Default
*  **Prim路径 (Prim Path):**/World/BoxOnConveyor_56/Materials/_6___Default
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/BoxOnConveyor_56/Materials/_6___Default/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/BoxOnConveyor_56/Materials/_6___Default/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f]
               *   Connected: '/World/BoxOnConveyor_56/Materials/_6___Default/tex_base.outputs:rgb' @ '/World/BoxOnConveyor_56/Materials/_6___Default/tex_base'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/06_-_Default_baseColor.jpg'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(1.000, 1.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0.892971'
       *   '/World/BoxOnConveyor_56/Materials/_6___Default/tex_base' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/06_-_Default_baseColor.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
           *   'file' [asset] = '0/06_-_Default_baseColor.jpg'
           *   'st' [float2]
               *   Connected: '/World/BoxOnConveyor_56/Materials/_6___Default/uvset0.outputs:result' @ '/World/BoxOnConveyor_56/Materials/_6___Default/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/BoxOnConveyor_56/Materials/_6___Default/uvset0' (ID: 'UsdPrimvarReader_float2')
       *   Implementation: 'id'


---


### /World/BoxOnConveyor_57/Materials/_6___Default
*  **Prim路径 (Prim Path):**/World/BoxOnConveyor_57/Materials/_6___Default
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/BoxOnConveyor_57/Materials/_6___Default/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/BoxOnConveyor_57/Materials/_6___Default/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f]
               *   Connected: '/World/BoxOnConveyor_57/Materials/_6___Default/tex_base.outputs:rgb' @ '/World/BoxOnConveyor_57/Materials/_6___Default/tex_base'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/06_-_Default_baseColor.jpg'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(1.000, 1.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0.892971'
       *   '/World/BoxOnConveyor_57/Materials/_6___Default/tex_base' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/06_-_Default_baseColor.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
           *   'file' [asset] = '0/06_-_Default_baseColor.jpg'
           *   'st' [float2]
               *   Connected: '/World/BoxOnConveyor_57/Materials/_6___Default/uvset0.outputs:result' @ '/World/BoxOnConveyor_57/Materials/_6___Default/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/BoxOnConveyor_57/Materials/_6___Default/uvset0' (ID: 'UsdPrimvarReader_float2')
       *   Implementation: 'id'


---


### /World/BoxOnConveyor_58/Materials/_6___Default
*  **Prim路径 (Prim Path):**/World/BoxOnConveyor_58/Materials/_6___Default
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/BoxOnConveyor_58/Materials/_6___Default/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/BoxOnConveyor_58/Materials/_6___Default/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f]
               *   Connected: '/World/BoxOnConveyor_58/Materials/_6___Default/tex_base.outputs:rgb' @ '/World/BoxOnConveyor_58/Materials/_6___Default/tex_base'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/06_-_Default_baseColor.jpg'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(1.000, 1.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0.892971'
       *   '/World/BoxOnConveyor_58/Materials/_6___Default/tex_base' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/06_-_Default_baseColor.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
           *   'file' [asset] = '0/06_-_Default_baseColor.jpg'
           *   'st' [float2]
               *   Connected: '/World/BoxOnConveyor_58/Materials/_6___Default/uvset0.outputs:result' @ '/World/BoxOnConveyor_58/Materials/_6___Default/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/BoxOnConveyor_58/Materials/_6___Default/uvset0' (ID: 'UsdPrimvarReader_float2')
       *   Implementation: 'id'


---


### /World/BoxOnConveyor_59/Materials/_6___Default
*  **Prim路径 (Prim Path):**/World/BoxOnConveyor_59/Materials/_6___Default
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/BoxOnConveyor_59/Materials/_6___Default/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/BoxOnConveyor_59/Materials/_6___Default/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f]
               *   Connected: '/World/BoxOnConveyor_59/Materials/_6___Default/tex_base.outputs:rgb' @ '/World/BoxOnConveyor_59/Materials/_6___Default/tex_base'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/06_-_Default_baseColor.jpg'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(1.000, 1.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0.892971'
       *   '/World/BoxOnConveyor_59/Materials/_6___Default/tex_base' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/06_-_Default_baseColor.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
           *   'file' [asset] = '0/06_-_Default_baseColor.jpg'
           *   'st' [float2]
               *   Connected: '/World/BoxOnConveyor_59/Materials/_6___Default/uvset0.outputs:result' @ '/World/BoxOnConveyor_59/Materials/_6___Default/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/BoxOnConveyor_59/Materials/_6___Default/uvset0' (ID: 'UsdPrimvarReader_float2')
       *   Implementation: 'id'


---


### /World/BoxOnConveyor_60/Materials/_6___Default
*  **Prim路径 (Prim Path):**/World/BoxOnConveyor_60/Materials/_6___Default
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/BoxOnConveyor_60/Materials/_6___Default/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/BoxOnConveyor_60/Materials/_6___Default/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f]
               *   Connected: '/World/BoxOnConveyor_60/Materials/_6___Default/tex_base.outputs:rgb' @ '/World/BoxOnConveyor_60/Materials/_6___Default/tex_base'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/06_-_Default_baseColor.jpg'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(1.000, 1.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0.892971'
       *   '/World/BoxOnConveyor_60/Materials/_6___Default/tex_base' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/06_-_Default_baseColor.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
           *   'file' [asset] = '0/06_-_Default_baseColor.jpg'
           *   'st' [float2]
               *   Connected: '/World/BoxOnConveyor_60/Materials/_6___Default/uvset0.outputs:result' @ '/World/BoxOnConveyor_60/Materials/_6___Default/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/BoxOnConveyor_60/Materials/_6___Default/uvset0' (ID: 'UsdPrimvarReader_float2')
       *   Implementation: 'id'


---


### /World/BoxOnConveyor_61/Materials/_6___Default
*  **Prim路径 (Prim Path):**/World/BoxOnConveyor_61/Materials/_6___Default
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/BoxOnConveyor_61/Materials/_6___Default/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/BoxOnConveyor_61/Materials/_6___Default/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f]
               *   Connected: '/World/BoxOnConveyor_61/Materials/_6___Default/tex_base.outputs:rgb' @ '/World/BoxOnConveyor_61/Materials/_6___Default/tex_base'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/06_-_Default_baseColor.jpg'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(1.000, 1.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0.892971'
       *   '/World/BoxOnConveyor_61/Materials/_6___Default/tex_base' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/06_-_Default_baseColor.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
           *   'file' [asset] = '0/06_-_Default_baseColor.jpg'
           *   'st' [float2]
               *   Connected: '/World/BoxOnConveyor_61/Materials/_6___Default/uvset0.outputs:result' @ '/World/BoxOnConveyor_61/Materials/_6___Default/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/BoxOnConveyor_61/Materials/_6___Default/uvset0' (ID: 'UsdPrimvarReader_float2')
       *   Implementation: 'id'


---


### /World/BoxOnConveyor_62/Materials/_6___Default
*  **Prim路径 (Prim Path):**/World/BoxOnConveyor_62/Materials/_6___Default
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/BoxOnConveyor_62/Materials/_6___Default/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/BoxOnConveyor_62/Materials/_6___Default/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f]
               *   Connected: '/World/BoxOnConveyor_62/Materials/_6___Default/tex_base.outputs:rgb' @ '/World/BoxOnConveyor_62/Materials/_6___Default/tex_base'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/06_-_Default_baseColor.jpg'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(1.000, 1.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0.892971'
       *   '/World/BoxOnConveyor_62/Materials/_6___Default/tex_base' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/06_-_Default_baseColor.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
           *   'file' [asset] = '0/06_-_Default_baseColor.jpg'
           *   'st' [float2]
               *   Connected: '/World/BoxOnConveyor_62/Materials/_6___Default/uvset0.outputs:result' @ '/World/BoxOnConveyor_62/Materials/_6___Default/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/BoxOnConveyor_62/Materials/_6___Default/uvset0' (ID: 'UsdPrimvarReader_float2')
       *   Implementation: 'id'


---


### /World/BoxOnConveyor_63/Materials/_6___Default
*  **Prim路径 (Prim Path):**/World/BoxOnConveyor_63/Materials/_6___Default
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/BoxOnConveyor_63/Materials/_6___Default/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/BoxOnConveyor_63/Materials/_6___Default/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f]
               *   Connected: '/World/BoxOnConveyor_63/Materials/_6___Default/tex_base.outputs:rgb' @ '/World/BoxOnConveyor_63/Materials/_6___Default/tex_base'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/06_-_Default_baseColor.jpg'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(1.000, 1.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0.892971'
       *   '/World/BoxOnConveyor_63/Materials/_6___Default/tex_base' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/06_-_Default_baseColor.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
           *   'file' [asset] = '0/06_-_Default_baseColor.jpg'
           *   'st' [float2]
               *   Connected: '/World/BoxOnConveyor_63/Materials/_6___Default/uvset0.outputs:result' @ '/World/BoxOnConveyor_63/Materials/_6___Default/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/BoxOnConveyor_63/Materials/_6___Default/uvset0' (ID: 'UsdPrimvarReader_float2')
       *   Implementation: 'id'


---


### /World/BoxOnConveyor_64/Materials/_6___Default
*  **Prim路径 (Prim Path):**/World/BoxOnConveyor_64/Materials/_6___Default
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/BoxOnConveyor_64/Materials/_6___Default/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/BoxOnConveyor_64/Materials/_6___Default/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f]
               *   Connected: '/World/BoxOnConveyor_64/Materials/_6___Default/tex_base.outputs:rgb' @ '/World/BoxOnConveyor_64/Materials/_6___Default/tex_base'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/06_-_Default_baseColor.jpg'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(1.000, 1.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0.892971'
       *   '/World/BoxOnConveyor_64/Materials/_6___Default/tex_base' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/06_-_Default_baseColor.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
           *   'file' [asset] = '0/06_-_Default_baseColor.jpg'
           *   'st' [float2]
               *   Connected: '/World/BoxOnConveyor_64/Materials/_6___Default/uvset0.outputs:result' @ '/World/BoxOnConveyor_64/Materials/_6___Default/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/BoxOnConveyor_64/Materials/_6___Default/uvset0' (ID: 'UsdPrimvarReader_float2')
       *   Implementation: 'id'


---


### /World/BoxOnConveyor_65/Materials/_6___Default
*  **Prim路径 (Prim Path):**/World/BoxOnConveyor_65/Materials/_6___Default
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/BoxOnConveyor_65/Materials/_6___Default/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/BoxOnConveyor_65/Materials/_6___Default/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f]
               *   Connected: '/World/BoxOnConveyor_65/Materials/_6___Default/tex_base.outputs:rgb' @ '/World/BoxOnConveyor_65/Materials/_6___Default/tex_base'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/06_-_Default_baseColor.jpg'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(1.000, 1.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0.892971'
       *   '/World/BoxOnConveyor_65/Materials/_6___Default/tex_base' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/06_-_Default_baseColor.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
           *   'file' [asset] = '0/06_-_Default_baseColor.jpg'
           *   'st' [float2]
               *   Connected: '/World/BoxOnConveyor_65/Materials/_6___Default/uvset0.outputs:result' @ '/World/BoxOnConveyor_65/Materials/_6___Default/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/BoxOnConveyor_65/Materials/_6___Default/uvset0' (ID: 'UsdPrimvarReader_float2')
       *   Implementation: 'id'


---


### /World/BoxOnConveyor_66/Materials/_6___Default
*  **Prim路径 (Prim Path):**/World/BoxOnConveyor_66/Materials/_6___Default
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/BoxOnConveyor_66/Materials/_6___Default/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/BoxOnConveyor_66/Materials/_6___Default/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f]
               *   Connected: '/World/BoxOnConveyor_66/Materials/_6___Default/tex_base.outputs:rgb' @ '/World/BoxOnConveyor_66/Materials/_6___Default/tex_base'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/06_-_Default_baseColor.jpg'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(1.000, 1.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0.892971'
       *   '/World/BoxOnConveyor_66/Materials/_6___Default/tex_base' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/06_-_Default_baseColor.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
           *   'file' [asset] = '0/06_-_Default_baseColor.jpg'
           *   'st' [float2]
               *   Connected: '/World/BoxOnConveyor_66/Materials/_6___Default/uvset0.outputs:result' @ '/World/BoxOnConveyor_66/Materials/_6___Default/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/BoxOnConveyor_66/Materials/_6___Default/uvset0' (ID: 'UsdPrimvarReader_float2')
       *   Implementation: 'id'


---


### /World/BoxOnConveyor_67/Materials/_6___Default
*  **Prim路径 (Prim Path):**/World/BoxOnConveyor_67/Materials/_6___Default
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/BoxOnConveyor_67/Materials/_6___Default/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/BoxOnConveyor_67/Materials/_6___Default/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f]
               *   Connected: '/World/BoxOnConveyor_67/Materials/_6___Default/tex_base.outputs:rgb' @ '/World/BoxOnConveyor_67/Materials/_6___Default/tex_base'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/06_-_Default_baseColor.jpg'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(1.000, 1.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0.892971'
       *   '/World/BoxOnConveyor_67/Materials/_6___Default/tex_base' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/06_-_Default_baseColor.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
           *   'file' [asset] = '0/06_-_Default_baseColor.jpg'
           *   'st' [float2]
               *   Connected: '/World/BoxOnConveyor_67/Materials/_6___Default/uvset0.outputs:result' @ '/World/BoxOnConveyor_67/Materials/_6___Default/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/BoxOnConveyor_67/Materials/_6___Default/uvset0' (ID: 'UsdPrimvarReader_float2')
       *   Implementation: 'id'


---


### /World/BoxOnConveyor_68/Materials/_6___Default
*  **Prim路径 (Prim Path):**/World/BoxOnConveyor_68/Materials/_6___Default
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/BoxOnConveyor_68/Materials/_6___Default/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/BoxOnConveyor_68/Materials/_6___Default/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f]
               *   Connected: '/World/BoxOnConveyor_68/Materials/_6___Default/tex_base.outputs:rgb' @ '/World/BoxOnConveyor_68/Materials/_6___Default/tex_base'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/06_-_Default_baseColor.jpg'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(1.000, 1.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0.892971'
       *   '/World/BoxOnConveyor_68/Materials/_6___Default/tex_base' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/06_-_Default_baseColor.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
           *   'file' [asset] = '0/06_-_Default_baseColor.jpg'
           *   'st' [float2]
               *   Connected: '/World/BoxOnConveyor_68/Materials/_6___Default/uvset0.outputs:result' @ '/World/BoxOnConveyor_68/Materials/_6___Default/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/BoxOnConveyor_68/Materials/_6___Default/uvset0' (ID: 'UsdPrimvarReader_float2')
       *   Implementation: 'id'


---


### /World/BoxOnConveyor_69/Materials/_6___Default
*  **Prim路径 (Prim Path):**/World/BoxOnConveyor_69/Materials/_6___Default
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/BoxOnConveyor_69/Materials/_6___Default/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/BoxOnConveyor_69/Materials/_6___Default/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f]
               *   Connected: '/World/BoxOnConveyor_69/Materials/_6___Default/tex_base.outputs:rgb' @ '/World/BoxOnConveyor_69/Materials/_6___Default/tex_base'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/06_-_Default_baseColor.jpg'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(1.000, 1.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0.892971'
       *   '/World/BoxOnConveyor_69/Materials/_6___Default/tex_base' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/06_-_Default_baseColor.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
           *   'file' [asset] = '0/06_-_Default_baseColor.jpg'
           *   'st' [float2]
               *   Connected: '/World/BoxOnConveyor_69/Materials/_6___Default/uvset0.outputs:result' @ '/World/BoxOnConveyor_69/Materials/_6___Default/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/BoxOnConveyor_69/Materials/_6___Default/uvset0' (ID: 'UsdPrimvarReader_float2')
       *   Implementation: 'id'


---


### /World/BoxOnConveyor_70/Materials/_6___Default
*  **Prim路径 (Prim Path):**/World/BoxOnConveyor_70/Materials/_6___Default
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/BoxOnConveyor_70/Materials/_6___Default/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/BoxOnConveyor_70/Materials/_6___Default/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f]
               *   Connected: '/World/BoxOnConveyor_70/Materials/_6___Default/tex_base.outputs:rgb' @ '/World/BoxOnConveyor_70/Materials/_6___Default/tex_base'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/06_-_Default_baseColor.jpg'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(1.000, 1.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0.892971'
       *   '/World/BoxOnConveyor_70/Materials/_6___Default/tex_base' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/06_-_Default_baseColor.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
           *   'file' [asset] = '0/06_-_Default_baseColor.jpg'
           *   'st' [float2]
               *   Connected: '/World/BoxOnConveyor_70/Materials/_6___Default/uvset0.outputs:result' @ '/World/BoxOnConveyor_70/Materials/_6___Default/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/BoxOnConveyor_70/Materials/_6___Default/uvset0' (ID: 'UsdPrimvarReader_float2')
       *   Implementation: 'id'


---


### /World/BoxOnConveyor_71/Materials/_6___Default
*  **Prim路径 (Prim Path):**/World/BoxOnConveyor_71/Materials/_6___Default
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/BoxOnConveyor_71/Materials/_6___Default/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/BoxOnConveyor_71/Materials/_6___Default/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f]
               *   Connected: '/World/BoxOnConveyor_71/Materials/_6___Default/tex_base.outputs:rgb' @ '/World/BoxOnConveyor_71/Materials/_6___Default/tex_base'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/06_-_Default_baseColor.jpg'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(1.000, 1.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0.892971'
       *   '/World/BoxOnConveyor_71/Materials/_6___Default/tex_base' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/06_-_Default_baseColor.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
           *   'file' [asset] = '0/06_-_Default_baseColor.jpg'
           *   'st' [float2]
               *   Connected: '/World/BoxOnConveyor_71/Materials/_6___Default/uvset0.outputs:result' @ '/World/BoxOnConveyor_71/Materials/_6___Default/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/BoxOnConveyor_71/Materials/_6___Default/uvset0' (ID: 'UsdPrimvarReader_float2')
       *   Implementation: 'id'


---


### /World/BoxOnConveyor_72/Materials/_6___Default
*  **Prim路径 (Prim Path):**/World/BoxOnConveyor_72/Materials/_6___Default
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/BoxOnConveyor_72/Materials/_6___Default/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/BoxOnConveyor_72/Materials/_6___Default/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f]
               *   Connected: '/World/BoxOnConveyor_72/Materials/_6___Default/tex_base.outputs:rgb' @ '/World/BoxOnConveyor_72/Materials/_6___Default/tex_base'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/06_-_Default_baseColor.jpg'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(1.000, 1.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0.892971'
       *   '/World/BoxOnConveyor_72/Materials/_6___Default/tex_base' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/06_-_Default_baseColor.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
           *   'file' [asset] = '0/06_-_Default_baseColor.jpg'
           *   'st' [float2]
               *   Connected: '/World/BoxOnConveyor_72/Materials/_6___Default/uvset0.outputs:result' @ '/World/BoxOnConveyor_72/Materials/_6___Default/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/BoxOnConveyor_72/Materials/_6___Default/uvset0' (ID: 'UsdPrimvarReader_float2')
       *   Implementation: 'id'


---


### /World/BoxOnConveyor_73/Materials/_6___Default
*  **Prim路径 (Prim Path):**/World/BoxOnConveyor_73/Materials/_6___Default
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/BoxOnConveyor_73/Materials/_6___Default/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/BoxOnConveyor_73/Materials/_6___Default/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f]
               *   Connected: '/World/BoxOnConveyor_73/Materials/_6___Default/tex_base.outputs:rgb' @ '/World/BoxOnConveyor_73/Materials/_6___Default/tex_base'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/06_-_Default_baseColor.jpg'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(1.000, 1.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0.892971'
       *   '/World/BoxOnConveyor_73/Materials/_6___Default/tex_base' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/06_-_Default_baseColor.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
           *   'file' [asset] = '0/06_-_Default_baseColor.jpg'
           *   'st' [float2]
               *   Connected: '/World/BoxOnConveyor_73/Materials/_6___Default/uvset0.outputs:result' @ '/World/BoxOnConveyor_73/Materials/_6___Default/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/BoxOnConveyor_73/Materials/_6___Default/uvset0' (ID: 'UsdPrimvarReader_float2')
       *   Implementation: 'id'


---


### /World/BoxOnConveyor_74/Materials/_6___Default
*  **Prim路径 (Prim Path):**/World/BoxOnConveyor_74/Materials/_6___Default
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/BoxOnConveyor_74/Materials/_6___Default/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/BoxOnConveyor_74/Materials/_6___Default/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f]
               *   Connected: '/World/BoxOnConveyor_74/Materials/_6___Default/tex_base.outputs:rgb' @ '/World/BoxOnConveyor_74/Materials/_6___Default/tex_base'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/06_-_Default_baseColor.jpg'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(1.000, 1.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0.892971'
       *   '/World/BoxOnConveyor_74/Materials/_6___Default/tex_base' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/06_-_Default_baseColor.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
           *   'file' [asset] = '0/06_-_Default_baseColor.jpg'
           *   'st' [float2]
               *   Connected: '/World/BoxOnConveyor_74/Materials/_6___Default/uvset0.outputs:result' @ '/World/BoxOnConveyor_74/Materials/_6___Default/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/BoxOnConveyor_74/Materials/_6___Default/uvset0' (ID: 'UsdPrimvarReader_float2')
       *   Implementation: 'id'


---


### /World/BoxOnConveyor_75/Materials/_6___Default
*  **Prim路径 (Prim Path):**/World/BoxOnConveyor_75/Materials/_6___Default
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/BoxOnConveyor_75/Materials/_6___Default/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/BoxOnConveyor_75/Materials/_6___Default/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f]
               *   Connected: '/World/BoxOnConveyor_75/Materials/_6___Default/tex_base.outputs:rgb' @ '/World/BoxOnConveyor_75/Materials/_6___Default/tex_base'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/06_-_Default_baseColor.jpg'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(1.000, 1.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0.892971'
       *   '/World/BoxOnConveyor_75/Materials/_6___Default/tex_base' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/06_-_Default_baseColor.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
           *   'file' [asset] = '0/06_-_Default_baseColor.jpg'
           *   'st' [float2]
               *   Connected: '/World/BoxOnConveyor_75/Materials/_6___Default/uvset0.outputs:result' @ '/World/BoxOnConveyor_75/Materials/_6___Default/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/BoxOnConveyor_75/Materials/_6___Default/uvset0' (ID: 'UsdPrimvarReader_float2')
       *   Implementation: 'id'


---


### /World/BoxOnConveyor_76/Materials/_6___Default
*  **Prim路径 (Prim Path):**/World/BoxOnConveyor_76/Materials/_6___Default
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/BoxOnConveyor_76/Materials/_6___Default/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/BoxOnConveyor_76/Materials/_6___Default/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f]
               *   Connected: '/World/BoxOnConveyor_76/Materials/_6___Default/tex_base.outputs:rgb' @ '/World/BoxOnConveyor_76/Materials/_6___Default/tex_base'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/06_-_Default_baseColor.jpg'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(1.000, 1.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0.892971'
       *   '/World/BoxOnConveyor_76/Materials/_6___Default/tex_base' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/06_-_Default_baseColor.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
           *   'file' [asset] = '0/06_-_Default_baseColor.jpg'
           *   'st' [float2]
               *   Connected: '/World/BoxOnConveyor_76/Materials/_6___Default/uvset0.outputs:result' @ '/World/BoxOnConveyor_76/Materials/_6___Default/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/BoxOnConveyor_76/Materials/_6___Default/uvset0' (ID: 'UsdPrimvarReader_float2')
       *   Implementation: 'id'


---


### /World/BoxOnConveyor_77/Materials/_6___Default
*  **Prim路径 (Prim Path):**/World/BoxOnConveyor_77/Materials/_6___Default
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/BoxOnConveyor_77/Materials/_6___Default/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/BoxOnConveyor_77/Materials/_6___Default/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f]
               *   Connected: '/World/BoxOnConveyor_77/Materials/_6___Default/tex_base.outputs:rgb' @ '/World/BoxOnConveyor_77/Materials/_6___Default/tex_base'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/06_-_Default_baseColor.jpg'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(1.000, 1.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0.892971'
       *   '/World/BoxOnConveyor_77/Materials/_6___Default/tex_base' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/06_-_Default_baseColor.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
           *   'file' [asset] = '0/06_-_Default_baseColor.jpg'
           *   'st' [float2]
               *   Connected: '/World/BoxOnConveyor_77/Materials/_6___Default/uvset0.outputs:result' @ '/World/BoxOnConveyor_77/Materials/_6___Default/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/BoxOnConveyor_77/Materials/_6___Default/uvset0' (ID: 'UsdPrimvarReader_float2')
       *   Implementation: 'id'


---


### /World/BoxOnConveyor_78/Materials/_6___Default
*  **Prim路径 (Prim Path):**/World/BoxOnConveyor_78/Materials/_6___Default
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/BoxOnConveyor_78/Materials/_6___Default/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/BoxOnConveyor_78/Materials/_6___Default/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f]
               *   Connected: '/World/BoxOnConveyor_78/Materials/_6___Default/tex_base.outputs:rgb' @ '/World/BoxOnConveyor_78/Materials/_6___Default/tex_base'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/06_-_Default_baseColor.jpg'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(1.000, 1.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0.892971'
       *   '/World/BoxOnConveyor_78/Materials/_6___Default/tex_base' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/06_-_Default_baseColor.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
           *   'file' [asset] = '0/06_-_Default_baseColor.jpg'
           *   'st' [float2]
               *   Connected: '/World/BoxOnConveyor_78/Materials/_6___Default/uvset0.outputs:result' @ '/World/BoxOnConveyor_78/Materials/_6___Default/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/BoxOnConveyor_78/Materials/_6___Default/uvset0' (ID: 'UsdPrimvarReader_float2')
       *   Implementation: 'id'


---


### /World/BoxOnConveyor_79/Materials/_6___Default
*  **Prim路径 (Prim Path):**/World/BoxOnConveyor_79/Materials/_6___Default
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/BoxOnConveyor_79/Materials/_6___Default/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/BoxOnConveyor_79/Materials/_6___Default/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f]
               *   Connected: '/World/BoxOnConveyor_79/Materials/_6___Default/tex_base.outputs:rgb' @ '/World/BoxOnConveyor_79/Materials/_6___Default/tex_base'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/06_-_Default_baseColor.jpg'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(1.000, 1.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0.892971'
       *   '/World/BoxOnConveyor_79/Materials/_6___Default/tex_base' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/06_-_Default_baseColor.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
           *   'file' [asset] = '0/06_-_Default_baseColor.jpg'
           *   'st' [float2]
               *   Connected: '/World/BoxOnConveyor_79/Materials/_6___Default/uvset0.outputs:result' @ '/World/BoxOnConveyor_79/Materials/_6___Default/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/BoxOnConveyor_79/Materials/_6___Default/uvset0' (ID: 'UsdPrimvarReader_float2')
       *   Implementation: 'id'


---


### /World/BoxOnConveyor_80/Materials/_6___Default
*  **Prim路径 (Prim Path):**/World/BoxOnConveyor_80/Materials/_6___Default
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/BoxOnConveyor_80/Materials/_6___Default/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/BoxOnConveyor_80/Materials/_6___Default/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f]
               *   Connected: '/World/BoxOnConveyor_80/Materials/_6___Default/tex_base.outputs:rgb' @ '/World/BoxOnConveyor_80/Materials/_6___Default/tex_base'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/06_-_Default_baseColor.jpg'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(1.000, 1.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0.892971'
       *   '/World/BoxOnConveyor_80/Materials/_6___Default/tex_base' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/06_-_Default_baseColor.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
           *   'file' [asset] = '0/06_-_Default_baseColor.jpg'
           *   'st' [float2]
               *   Connected: '/World/BoxOnConveyor_80/Materials/_6___Default/uvset0.outputs:result' @ '/World/BoxOnConveyor_80/Materials/_6___Default/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/BoxOnConveyor_80/Materials/_6___Default/uvset0' (ID: 'UsdPrimvarReader_float2')
       *   Implementation: 'id'


---


### /World/StackedCarton_1/Materials/_6___Default
*  **Prim路径 (Prim Path):**/World/StackedCarton_1/Materials/_6___Default
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/StackedCarton_1/Materials/_6___Default/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/StackedCarton_1/Materials/_6___Default/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f]
               *   Connected: '/World/StackedCarton_1/Materials/_6___Default/tex_base.outputs:rgb' @ '/World/StackedCarton_1/Materials/_6___Default/tex_base'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/06_-_Default_baseColor.jpg'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(1.000, 1.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0.892971'
       *   '/World/StackedCarton_1/Materials/_6___Default/tex_base' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/06_-_Default_baseColor.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
           *   'file' [asset] = '0/06_-_Default_baseColor.jpg'
           *   'st' [float2]
               *   Connected: '/World/StackedCarton_1/Materials/_6___Default/uvset0.outputs:result' @ '/World/StackedCarton_1/Materials/_6___Default/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/StackedCarton_1/Materials/_6___Default/uvset0' (ID: 'UsdPrimvarReader_float2')
       *   Implementation: 'id'


---


### /World/StackedCarton_2/Materials/_6___Default
*  **Prim路径 (Prim Path):**/World/StackedCarton_2/Materials/_6___Default
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/StackedCarton_2/Materials/_6___Default/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/StackedCarton_2/Materials/_6___Default/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f]
               *   Connected: '/World/StackedCarton_2/Materials/_6___Default/tex_base.outputs:rgb' @ '/World/StackedCarton_2/Materials/_6___Default/tex_base'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/06_-_Default_baseColor.jpg'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(1.000, 1.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0.892971'
       *   '/World/StackedCarton_2/Materials/_6___Default/tex_base' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/06_-_Default_baseColor.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
           *   'file' [asset] = '0/06_-_Default_baseColor.jpg'
           *   'st' [float2]
               *   Connected: '/World/StackedCarton_2/Materials/_6___Default/uvset0.outputs:result' @ '/World/StackedCarton_2/Materials/_6___Default/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/StackedCarton_2/Materials/_6___Default/uvset0' (ID: 'UsdPrimvarReader_float2')
       *   Implementation: 'id'


---


### /World/StackedCarton_3/Materials/_6___Default
*  **Prim路径 (Prim Path):**/World/StackedCarton_3/Materials/_6___Default
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/StackedCarton_3/Materials/_6___Default/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/StackedCarton_3/Materials/_6___Default/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f]
               *   Connected: '/World/StackedCarton_3/Materials/_6___Default/tex_base.outputs:rgb' @ '/World/StackedCarton_3/Materials/_6___Default/tex_base'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/06_-_Default_baseColor.jpg'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(1.000, 1.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0.892971'
       *   '/World/StackedCarton_3/Materials/_6___Default/tex_base' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/06_-_Default_baseColor.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
           *   'file' [asset] = '0/06_-_Default_baseColor.jpg'
           *   'st' [float2]
               *   Connected: '/World/StackedCarton_3/Materials/_6___Default/uvset0.outputs:result' @ '/World/StackedCarton_3/Materials/_6___Default/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/StackedCarton_3/Materials/_6___Default/uvset0' (ID: 'UsdPrimvarReader_float2')
       *   Implementation: 'id'


---


### /World/StackedCarton_4/Materials/_6___Default
*  **Prim路径 (Prim Path):**/World/StackedCarton_4/Materials/_6___Default
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/StackedCarton_4/Materials/_6___Default/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/StackedCarton_4/Materials/_6___Default/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f]
               *   Connected: '/World/StackedCarton_4/Materials/_6___Default/tex_base.outputs:rgb' @ '/World/StackedCarton_4/Materials/_6___Default/tex_base'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/06_-_Default_baseColor.jpg'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(1.000, 1.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0.892971'
       *   '/World/StackedCarton_4/Materials/_6___Default/tex_base' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/06_-_Default_baseColor.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
           *   'file' [asset] = '0/06_-_Default_baseColor.jpg'
           *   'st' [float2]
               *   Connected: '/World/StackedCarton_4/Materials/_6___Default/uvset0.outputs:result' @ '/World/StackedCarton_4/Materials/_6___Default/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/StackedCarton_4/Materials/_6___Default/uvset0' (ID: 'UsdPrimvarReader_float2')
       *   Implementation: 'id'


---


### /World/StackedCarton_5/Materials/_6___Default
*  **Prim路径 (Prim Path):**/World/StackedCarton_5/Materials/_6___Default
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/StackedCarton_5/Materials/_6___Default/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/StackedCarton_5/Materials/_6___Default/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f]
               *   Connected: '/World/StackedCarton_5/Materials/_6___Default/tex_base.outputs:rgb' @ '/World/StackedCarton_5/Materials/_6___Default/tex_base'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/06_-_Default_baseColor.jpg'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(1.000, 1.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0.892971'
       *   '/World/StackedCarton_5/Materials/_6___Default/tex_base' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/06_-_Default_baseColor.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
           *   'file' [asset] = '0/06_-_Default_baseColor.jpg'
           *   'st' [float2]
               *   Connected: '/World/StackedCarton_5/Materials/_6___Default/uvset0.outputs:result' @ '/World/StackedCarton_5/Materials/_6___Default/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/StackedCarton_5/Materials/_6___Default/uvset0' (ID: 'UsdPrimvarReader_float2')
       *   Implementation: 'id'


---


### /World/StackedCarton_6/Materials/_6___Default
*  **Prim路径 (Prim Path):**/World/StackedCarton_6/Materials/_6___Default
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/StackedCarton_6/Materials/_6___Default/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/StackedCarton_6/Materials/_6___Default/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f]
               *   Connected: '/World/StackedCarton_6/Materials/_6___Default/tex_base.outputs:rgb' @ '/World/StackedCarton_6/Materials/_6___Default/tex_base'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/06_-_Default_baseColor.jpg'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(1.000, 1.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0.892971'
       *   '/World/StackedCarton_6/Materials/_6___Default/tex_base' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/06_-_Default_baseColor.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
           *   'file' [asset] = '0/06_-_Default_baseColor.jpg'
           *   'st' [float2]
               *   Connected: '/World/StackedCarton_6/Materials/_6___Default/uvset0.outputs:result' @ '/World/StackedCarton_6/Materials/_6___Default/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/StackedCarton_6/Materials/_6___Default/uvset0' (ID: 'UsdPrimvarReader_float2')
       *   Implementation: 'id'


---


### /World/StackedCarton_7/Materials/_6___Default
*  **Prim路径 (Prim Path):**/World/StackedCarton_7/Materials/_6___Default
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/StackedCarton_7/Materials/_6___Default/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/StackedCarton_7/Materials/_6___Default/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f]
               *   Connected: '/World/StackedCarton_7/Materials/_6___Default/tex_base.outputs:rgb' @ '/World/StackedCarton_7/Materials/_6___Default/tex_base'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/06_-_Default_baseColor.jpg'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(1.000, 1.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0.892971'
       *   '/World/StackedCarton_7/Materials/_6___Default/tex_base' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/06_-_Default_baseColor.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
           *   'file' [asset] = '0/06_-_Default_baseColor.jpg'
           *   'st' [float2]
               *   Connected: '/World/StackedCarton_7/Materials/_6___Default/uvset0.outputs:result' @ '/World/StackedCarton_7/Materials/_6___Default/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/StackedCarton_7/Materials/_6___Default/uvset0' (ID: 'UsdPrimvarReader_float2')
       *   Implementation: 'id'


---


### /World/StackedCarton_8/Materials/_6___Default
*  **Prim路径 (Prim Path):**/World/StackedCarton_8/Materials/_6___Default
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/StackedCarton_8/Materials/_6___Default/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/StackedCarton_8/Materials/_6___Default/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f]
               *   Connected: '/World/StackedCarton_8/Materials/_6___Default/tex_base.outputs:rgb' @ '/World/StackedCarton_8/Materials/_6___Default/tex_base'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/06_-_Default_baseColor.jpg'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(1.000, 1.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0.892971'
       *   '/World/StackedCarton_8/Materials/_6___Default/tex_base' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/06_-_Default_baseColor.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
           *   'file' [asset] = '0/06_-_Default_baseColor.jpg'
           *   'st' [float2]
               *   Connected: '/World/StackedCarton_8/Materials/_6___Default/uvset0.outputs:result' @ '/World/StackedCarton_8/Materials/_6___Default/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/StackedCarton_8/Materials/_6___Default/uvset0' (ID: 'UsdPrimvarReader_float2')
       *   Implementation: 'id'


---


### /World/StackedCarton1_1/Materials/_6___Default
*  **Prim路径 (Prim Path):**/World/StackedCarton1_1/Materials/_6___Default
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/StackedCarton1_1/Materials/_6___Default/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/StackedCarton1_1/Materials/_6___Default/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f]
               *   Connected: '/World/StackedCarton1_1/Materials/_6___Default/tex_base.outputs:rgb' @ '/World/StackedCarton1_1/Materials/_6___Default/tex_base'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/06_-_Default_baseColor.jpg'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(1.000, 1.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0.892971'
       *   '/World/StackedCarton1_1/Materials/_6___Default/tex_base' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/06_-_Default_baseColor.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
           *   'file' [asset] = '0/06_-_Default_baseColor.jpg'
           *   'st' [float2]
               *   Connected: '/World/StackedCarton1_1/Materials/_6___Default/uvset0.outputs:result' @ '/World/StackedCarton1_1/Materials/_6___Default/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/StackedCarton1_1/Materials/_6___Default/uvset0' (ID: 'UsdPrimvarReader_float2')
       *   Implementation: 'id'


---


### /World/StackedCarton1_2/Materials/_6___Default
*  **Prim路径 (Prim Path):**/World/StackedCarton1_2/Materials/_6___Default
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/StackedCarton1_2/Materials/_6___Default/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/StackedCarton1_2/Materials/_6___Default/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f]
               *   Connected: '/World/StackedCarton1_2/Materials/_6___Default/tex_base.outputs:rgb' @ '/World/StackedCarton1_2/Materials/_6___Default/tex_base'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/06_-_Default_baseColor.jpg'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(1.000, 1.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0.892971'
       *   '/World/StackedCarton1_2/Materials/_6___Default/tex_base' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/06_-_Default_baseColor.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
           *   'file' [asset] = '0/06_-_Default_baseColor.jpg'
           *   'st' [float2]
               *   Connected: '/World/StackedCarton1_2/Materials/_6___Default/uvset0.outputs:result' @ '/World/StackedCarton1_2/Materials/_6___Default/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/StackedCarton1_2/Materials/_6___Default/uvset0' (ID: 'UsdPrimvarReader_float2')
       *   Implementation: 'id'


---


### /World/StackedCarton1_3/Materials/_6___Default
*  **Prim路径 (Prim Path):**/World/StackedCarton1_3/Materials/_6___Default
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/StackedCarton1_3/Materials/_6___Default/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/StackedCarton1_3/Materials/_6___Default/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f]
               *   Connected: '/World/StackedCarton1_3/Materials/_6___Default/tex_base.outputs:rgb' @ '/World/StackedCarton1_3/Materials/_6___Default/tex_base'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/06_-_Default_baseColor.jpg'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(1.000, 1.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0.892971'
       *   '/World/StackedCarton1_3/Materials/_6___Default/tex_base' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/06_-_Default_baseColor.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
           *   'file' [asset] = '0/06_-_Default_baseColor.jpg'
           *   'st' [float2]
               *   Connected: '/World/StackedCarton1_3/Materials/_6___Default/uvset0.outputs:result' @ '/World/StackedCarton1_3/Materials/_6___Default/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/StackedCarton1_3/Materials/_6___Default/uvset0' (ID: 'UsdPrimvarReader_float2')
       *   Implementation: 'id'


---


### /World/StackedCarton1_4/Materials/_6___Default
*  **Prim路径 (Prim Path):**/World/StackedCarton1_4/Materials/_6___Default
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/StackedCarton1_4/Materials/_6___Default/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/StackedCarton1_4/Materials/_6___Default/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f]
               *   Connected: '/World/StackedCarton1_4/Materials/_6___Default/tex_base.outputs:rgb' @ '/World/StackedCarton1_4/Materials/_6___Default/tex_base'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/06_-_Default_baseColor.jpg'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(1.000, 1.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0.892971'
       *   '/World/StackedCarton1_4/Materials/_6___Default/tex_base' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/06_-_Default_baseColor.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
           *   'file' [asset] = '0/06_-_Default_baseColor.jpg'
           *   'st' [float2]
               *   Connected: '/World/StackedCarton1_4/Materials/_6___Default/uvset0.outputs:result' @ '/World/StackedCarton1_4/Materials/_6___Default/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/StackedCarton1_4/Materials/_6___Default/uvset0' (ID: 'UsdPrimvarReader_float2')
       *   Implementation: 'id'


---


### /World/StackedCarton1_5/Materials/_6___Default
*  **Prim路径 (Prim Path):**/World/StackedCarton1_5/Materials/_6___Default
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/StackedCarton1_5/Materials/_6___Default/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/StackedCarton1_5/Materials/_6___Default/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f]
               *   Connected: '/World/StackedCarton1_5/Materials/_6___Default/tex_base.outputs:rgb' @ '/World/StackedCarton1_5/Materials/_6___Default/tex_base'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/06_-_Default_baseColor.jpg'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(1.000, 1.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0.892971'
       *   '/World/StackedCarton1_5/Materials/_6___Default/tex_base' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/06_-_Default_baseColor.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
           *   'file' [asset] = '0/06_-_Default_baseColor.jpg'
           *   'st' [float2]
               *   Connected: '/World/StackedCarton1_5/Materials/_6___Default/uvset0.outputs:result' @ '/World/StackedCarton1_5/Materials/_6___Default/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/StackedCarton1_5/Materials/_6___Default/uvset0' (ID: 'UsdPrimvarReader_float2')
       *   Implementation: 'id'


---


### /World/StackedCarton1_6/Materials/_6___Default
*  **Prim路径 (Prim Path):**/World/StackedCarton1_6/Materials/_6___Default
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/StackedCarton1_6/Materials/_6___Default/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/StackedCarton1_6/Materials/_6___Default/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f]
               *   Connected: '/World/StackedCarton1_6/Materials/_6___Default/tex_base.outputs:rgb' @ '/World/StackedCarton1_6/Materials/_6___Default/tex_base'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/06_-_Default_baseColor.jpg'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(1.000, 1.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0.892971'
       *   '/World/StackedCarton1_6/Materials/_6___Default/tex_base' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/06_-_Default_baseColor.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
           *   'file' [asset] = '0/06_-_Default_baseColor.jpg'
           *   'st' [float2]
               *   Connected: '/World/StackedCarton1_6/Materials/_6___Default/uvset0.outputs:result' @ '/World/StackedCarton1_6/Materials/_6___Default/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/StackedCarton1_6/Materials/_6___Default/uvset0' (ID: 'UsdPrimvarReader_float2')
       *   Implementation: 'id'


---


### /World/StackedCarton1_7/Materials/_6___Default
*  **Prim路径 (Prim Path):**/World/StackedCarton1_7/Materials/_6___Default
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/StackedCarton1_7/Materials/_6___Default/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/StackedCarton1_7/Materials/_6___Default/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f]
               *   Connected: '/World/StackedCarton1_7/Materials/_6___Default/tex_base.outputs:rgb' @ '/World/StackedCarton1_7/Materials/_6___Default/tex_base'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/06_-_Default_baseColor.jpg'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(1.000, 1.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0.892971'
       *   '/World/StackedCarton1_7/Materials/_6___Default/tex_base' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/06_-_Default_baseColor.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
           *   'file' [asset] = '0/06_-_Default_baseColor.jpg'
           *   'st' [float2]
               *   Connected: '/World/StackedCarton1_7/Materials/_6___Default/uvset0.outputs:result' @ '/World/StackedCarton1_7/Materials/_6___Default/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/StackedCarton1_7/Materials/_6___Default/uvset0' (ID: 'UsdPrimvarReader_float2')
       *   Implementation: 'id'


---


### /World/StackedCarton1_8/Materials/_6___Default
*  **Prim路径 (Prim Path):**/World/StackedCarton1_8/Materials/_6___Default
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/StackedCarton1_8/Materials/_6___Default/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/StackedCarton1_8/Materials/_6___Default/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f]
               *   Connected: '/World/StackedCarton1_8/Materials/_6___Default/tex_base.outputs:rgb' @ '/World/StackedCarton1_8/Materials/_6___Default/tex_base'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/06_-_Default_baseColor.jpg'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(1.000, 1.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0.892971'
       *   '/World/StackedCarton1_8/Materials/_6___Default/tex_base' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/06_-_Default_baseColor.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
           *   'file' [asset] = '0/06_-_Default_baseColor.jpg'
           *   'st' [float2]
               *   Connected: '/World/StackedCarton1_8/Materials/_6___Default/uvset0.outputs:result' @ '/World/StackedCarton1_8/Materials/_6___Default/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/StackedCarton1_8/Materials/_6___Default/uvset0' (ID: 'UsdPrimvarReader_float2')
       *   Implementation: 'id'


---


### /World/StackedCarton2_1/Materials/_6___Default
*  **Prim路径 (Prim Path):**/World/StackedCarton2_1/Materials/_6___Default
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/StackedCarton2_1/Materials/_6___Default/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/StackedCarton2_1/Materials/_6___Default/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f]
               *   Connected: '/World/StackedCarton2_1/Materials/_6___Default/tex_base.outputs:rgb' @ '/World/StackedCarton2_1/Materials/_6___Default/tex_base'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/06_-_Default_baseColor.jpg'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(1.000, 1.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0.892971'
       *   '/World/StackedCarton2_1/Materials/_6___Default/tex_base' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/06_-_Default_baseColor.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
           *   'file' [asset] = '0/06_-_Default_baseColor.jpg'
           *   'st' [float2]
               *   Connected: '/World/StackedCarton2_1/Materials/_6___Default/uvset0.outputs:result' @ '/World/StackedCarton2_1/Materials/_6___Default/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/StackedCarton2_1/Materials/_6___Default/uvset0' (ID: 'UsdPrimvarReader_float2')
       *   Implementation: 'id'


---


### /World/StackedCarton2_2/Materials/_6___Default
*  **Prim路径 (Prim Path):**/World/StackedCarton2_2/Materials/_6___Default
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/StackedCarton2_2/Materials/_6___Default/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/StackedCarton2_2/Materials/_6___Default/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f]
               *   Connected: '/World/StackedCarton2_2/Materials/_6___Default/tex_base.outputs:rgb' @ '/World/StackedCarton2_2/Materials/_6___Default/tex_base'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/06_-_Default_baseColor.jpg'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(1.000, 1.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0.892971'
       *   '/World/StackedCarton2_2/Materials/_6___Default/tex_base' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/06_-_Default_baseColor.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
           *   'file' [asset] = '0/06_-_Default_baseColor.jpg'
           *   'st' [float2]
               *   Connected: '/World/StackedCarton2_2/Materials/_6___Default/uvset0.outputs:result' @ '/World/StackedCarton2_2/Materials/_6___Default/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/StackedCarton2_2/Materials/_6___Default/uvset0' (ID: 'UsdPrimvarReader_float2')
       *   Implementation: 'id'


---


### /World/StackedCarton2_3/Materials/_6___Default
*  **Prim路径 (Prim Path):**/World/StackedCarton2_3/Materials/_6___Default
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/StackedCarton2_3/Materials/_6___Default/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/StackedCarton2_3/Materials/_6___Default/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f]
               *   Connected: '/World/StackedCarton2_3/Materials/_6___Default/tex_base.outputs:rgb' @ '/World/StackedCarton2_3/Materials/_6___Default/tex_base'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/06_-_Default_baseColor.jpg'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(1.000, 1.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0.892971'
       *   '/World/StackedCarton2_3/Materials/_6___Default/tex_base' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/06_-_Default_baseColor.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
           *   'file' [asset] = '0/06_-_Default_baseColor.jpg'
           *   'st' [float2]
               *   Connected: '/World/StackedCarton2_3/Materials/_6___Default/uvset0.outputs:result' @ '/World/StackedCarton2_3/Materials/_6___Default/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/StackedCarton2_3/Materials/_6___Default/uvset0' (ID: 'UsdPrimvarReader_float2')
       *   Implementation: 'id'


---


### /World/StackedCarton2_4/Materials/_6___Default
*  **Prim路径 (Prim Path):**/World/StackedCarton2_4/Materials/_6___Default
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/StackedCarton2_4/Materials/_6___Default/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/StackedCarton2_4/Materials/_6___Default/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f]
               *   Connected: '/World/StackedCarton2_4/Materials/_6___Default/tex_base.outputs:rgb' @ '/World/StackedCarton2_4/Materials/_6___Default/tex_base'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/06_-_Default_baseColor.jpg'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(1.000, 1.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0.892971'
       *   '/World/StackedCarton2_4/Materials/_6___Default/tex_base' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/06_-_Default_baseColor.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
           *   'file' [asset] = '0/06_-_Default_baseColor.jpg'
           *   'st' [float2]
               *   Connected: '/World/StackedCarton2_4/Materials/_6___Default/uvset0.outputs:result' @ '/World/StackedCarton2_4/Materials/_6___Default/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/StackedCarton2_4/Materials/_6___Default/uvset0' (ID: 'UsdPrimvarReader_float2')
       *   Implementation: 'id'


---


### /World/StackedCarton2_5/Materials/_6___Default
*  **Prim路径 (Prim Path):**/World/StackedCarton2_5/Materials/_6___Default
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/StackedCarton2_5/Materials/_6___Default/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/StackedCarton2_5/Materials/_6___Default/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f]
               *   Connected: '/World/StackedCarton2_5/Materials/_6___Default/tex_base.outputs:rgb' @ '/World/StackedCarton2_5/Materials/_6___Default/tex_base'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/06_-_Default_baseColor.jpg'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(1.000, 1.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0.892971'
       *   '/World/StackedCarton2_5/Materials/_6___Default/tex_base' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/06_-_Default_baseColor.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
           *   'file' [asset] = '0/06_-_Default_baseColor.jpg'
           *   'st' [float2]
               *   Connected: '/World/StackedCarton2_5/Materials/_6___Default/uvset0.outputs:result' @ '/World/StackedCarton2_5/Materials/_6___Default/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/StackedCarton2_5/Materials/_6___Default/uvset0' (ID: 'UsdPrimvarReader_float2')
       *   Implementation: 'id'


---


### /World/StackedCarton2_6/Materials/_6___Default
*  **Prim路径 (Prim Path):**/World/StackedCarton2_6/Materials/_6___Default
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/StackedCarton2_6/Materials/_6___Default/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/StackedCarton2_6/Materials/_6___Default/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f]
               *   Connected: '/World/StackedCarton2_6/Materials/_6___Default/tex_base.outputs:rgb' @ '/World/StackedCarton2_6/Materials/_6___Default/tex_base'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/06_-_Default_baseColor.jpg'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(1.000, 1.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0.892971'
       *   '/World/StackedCarton2_6/Materials/_6___Default/tex_base' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/06_-_Default_baseColor.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
           *   'file' [asset] = '0/06_-_Default_baseColor.jpg'
           *   'st' [float2]
               *   Connected: '/World/StackedCarton2_6/Materials/_6___Default/uvset0.outputs:result' @ '/World/StackedCarton2_6/Materials/_6___Default/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/StackedCarton2_6/Materials/_6___Default/uvset0' (ID: 'UsdPrimvarReader_float2')
       *   Implementation: 'id'


---


### /World/StackedCarton2_7/Materials/_6___Default
*  **Prim路径 (Prim Path):**/World/StackedCarton2_7/Materials/_6___Default
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/StackedCarton2_7/Materials/_6___Default/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/StackedCarton2_7/Materials/_6___Default/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f]
               *   Connected: '/World/StackedCarton2_7/Materials/_6___Default/tex_base.outputs:rgb' @ '/World/StackedCarton2_7/Materials/_6___Default/tex_base'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/06_-_Default_baseColor.jpg'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(1.000, 1.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0.892971'
       *   '/World/StackedCarton2_7/Materials/_6___Default/tex_base' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/06_-_Default_baseColor.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
           *   'file' [asset] = '0/06_-_Default_baseColor.jpg'
           *   'st' [float2]
               *   Connected: '/World/StackedCarton2_7/Materials/_6___Default/uvset0.outputs:result' @ '/World/StackedCarton2_7/Materials/_6___Default/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/StackedCarton2_7/Materials/_6___Default/uvset0' (ID: 'UsdPrimvarReader_float2')
       *   Implementation: 'id'


---


### /World/StackedCarton2_8/Materials/_6___Default
*  **Prim路径 (Prim Path):**/World/StackedCarton2_8/Materials/_6___Default
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/StackedCarton2_8/Materials/_6___Default/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/StackedCarton2_8/Materials/_6___Default/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f]
               *   Connected: '/World/StackedCarton2_8/Materials/_6___Default/tex_base.outputs:rgb' @ '/World/StackedCarton2_8/Materials/_6___Default/tex_base'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/06_-_Default_baseColor.jpg'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(1.000, 1.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0.892971'
       *   '/World/StackedCarton2_8/Materials/_6___Default/tex_base' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/06_-_Default_baseColor.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
           *   'file' [asset] = '0/06_-_Default_baseColor.jpg'
           *   'st' [float2]
               *   Connected: '/World/StackedCarton2_8/Materials/_6___Default/uvset0.outputs:result' @ '/World/StackedCarton2_8/Materials/_6___Default/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/StackedCarton2_8/Materials/_6___Default/uvset0' (ID: 'UsdPrimvarReader_float2')
       *   Implementation: 'id'


---


### /World/model_desk008/materials/mat_0
*  **Prim路径 (Prim Path):**/World/model_desk008/materials/mat_0
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/model_desk008/materials/mat_0/PBRShader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/model_desk008/materials/mat_0/PBRShader' (ID: 'UsdPreviewSurface')
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


### /World/model_desk008/materials/mat_10782663
*  **Prim路径 (Prim Path):**/World/model_desk008/materials/mat_10782663
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/model_desk008/materials/mat_10782663/PBRShader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/model_desk008/materials/mat_10782663/PBRShader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'clearcoat' [float] = '0.05'
           *   'clearcoatRoughness' [float] = '0.05'
           *   'diffuseColor' [color3f] = '(0.515, 0.515, 0.515)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'ior' [float] = '1'
           *   'metallic' [float] = '0.12'
           *   'opacity' [float] = '1'
           *   'roughness' [float] = '0.09'
           *   'specularColor' [color3f] = '(0.000, 0.000, 0.000)'


---


### /World/model_desk008/materials/mat_10782673
*  **Prim路径 (Prim Path):**/World/model_desk008/materials/mat_10782673
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/model_desk008/materials/mat_10782673/PBRShader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/model_desk008/materials/mat_10782673/PBRShader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'clearcoat' [float] = '0.05'
           *   'clearcoatRoughness' [float] = '0.05'
           *   'diffuseColor' [color3f]
               *   Connected: '/World/model_desk008/materials/mat_10782673/diffuseTexture.outputs:rgb' @ '/World/model_desk008/materials/mat_10782673/diffuseTexture'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/0a01a4f7d6ec62fdb62fdd571ea34f89.png'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'ior' [float] = '1'
           *   'metallic' [float] = '0.17'
           *   'opacity' [float] = '1'
           *   'roughness' [float] = '0.12'
           *   'specularColor' [color3f] = '(0.000, 0.000, 0.000)'
       *   '/World/model_desk008/materials/mat_10782673/diffuseTexture' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/0a01a4f7d6ec62fdb62fdd571ea34f89.png'
       *   Inputs:
           *   'file' [asset] = '0/0a01a4f7d6ec62fdb62fdd571ea34f89.png'
           *   'st' [float2]
               *   Connected: '/World/model_desk008/materials/mat_10782673/transform_st.outputs:result' @ '/World/model_desk008/materials/mat_10782673/transform_st'
                   *   Shader ID: 'UsdTransform2d'
       *   '/World/model_desk008/materials/mat_10782673/transform_st' (ID: 'UsdTransform2d')
       *   Implementation: 'id'
       *   Inputs:
           *   'in' [float2]
               *   Connected: '/World/model_desk008/materials/mat_10782673/stReader.outputs:result' @ '/World/model_desk008/materials/mat_10782673/stReader'
                   *   Shader ID: 'UsdPrimvarReader_float2'
           *   'rotation' [float] = '0'
           *   'scale' [float2] = '(39.370, 39.370)'
           *   'translation' [float2] = '(0.000, 0.000)'
       *   '/World/model_desk008/materials/mat_10782673/stReader' (ID: 'UsdPrimvarReader_float2')
       *   Implementation: 'id'
       *   Inputs:
           *   'varname' [string]
               *   Connected: '/World/model_desk008/materials/mat_10782673.inputs:frame:stPrimvarName' @ '/World/model_desk008/materials/mat_10782673'


---


### /World/model_desk008/materials/mat_10782839
*  **Prim路径 (Prim Path):**/World/model_desk008/materials/mat_10782839
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/model_desk008/materials/mat_10782839/PBRShader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/model_desk008/materials/mat_10782839/PBRShader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'clearcoat' [float] = '0.05'
           *   'clearcoatRoughness' [float] = '0.05'
           *   'diffuseColor' [color3f] = '(0.497, 0.451, 0.413)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'ior' [float] = '1'
           *   'metallic' [float] = '0.16'
           *   'opacity' [float] = '1'
           *   'roughness' [float] = '0.14'
           *   'specularColor' [color3f] = '(0.000, 0.000, 0.000)'


---


### /World/model_desk008/materials/mat_10782842
*  **Prim路径 (Prim Path):**/World/model_desk008/materials/mat_10782842
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/model_desk008/materials/mat_10782842/PBRShader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/model_desk008/materials/mat_10782842/PBRShader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'clearcoat' [float] = '0.05'
           *   'clearcoatRoughness' [float] = '0.05'
           *   'diffuseColor' [color3f] = '(0.913, 0.913, 0.913)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'ior' [float] = '1'
           *   'metallic' [float] = '0.14'
           *   'opacity' [float] = '1'
           *   'roughness' [float] = '0.09'
           *   'specularColor' [color3f] = '(0.000, 0.000, 0.000)'


---


### /World/model_desk008/PhysicsMaterial
*  **Prim路径 (Prim Path):**/World/model_desk008/PhysicsMaterial
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'


---


### /World/model_desk008/PhysicsMaterial_01
*  **Prim路径 (Prim Path):**/World/model_desk008/PhysicsMaterial_01
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'


---


### /World/INDUSTRIAL_ROBOTIC_ARM/Materials/Brass___Polished
*  **Prim路径 (Prim Path):**/World/INDUSTRIAL_ROBOTIC_ARM/Materials/Brass___Polished
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/INDUSTRIAL_ROBOTIC_ARM/Materials/Brass___Polished/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/INDUSTRIAL_ROBOTIC_ARM/Materials/Brass___Polished/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.953, 0.796, 0.486)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0.957705'


---


### /World/INDUSTRIAL_ROBOTIC_ARM/Materials/Aluminum___Anodized_Glossy_Grey
*  **Prim路径 (Prim Path):**/World/INDUSTRIAL_ROBOTIC_ARM/Materials/Aluminum___Anodized_Glossy_Grey
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/INDUSTRIAL_ROBOTIC_ARM/Materials/Aluminum___Anodized_Glossy_Grey/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/INDUSTRIAL_ROBOTIC_ARM/Materials/Aluminum___Anodized_Glossy_Grey/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.537, 0.537, 0.537)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0.957705'


---


### /World/INDUSTRIAL_ROBOTIC_ARM/Materials/Paint___Enamel_Glossy_Yellow
*  **Prim路径 (Prim Path):**/World/INDUSTRIAL_ROBOTIC_ARM/Materials/Paint___Enamel_Glossy_Yellow
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/INDUSTRIAL_ROBOTIC_ARM/Materials/Paint___Enamel_Glossy_Yellow/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/INDUSTRIAL_ROBOTIC_ARM/Materials/Paint___Enamel_Glossy_Yellow/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.910, 0.678, 0.137)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0.957705'


---


### /World/INDUSTRIAL_ROBOTIC_ARM/Materials/Body1__0
*  **Prim路径 (Prim Path):**/World/INDUSTRIAL_ROBOTIC_ARM/Materials/Body1__0
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/INDUSTRIAL_ROBOTIC_ARM/Materials/Body1__0/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/INDUSTRIAL_ROBOTIC_ARM/Materials/Body1__0/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(1.000, 1.000, 1.000)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0.6'


---


### /World/INDUSTRIAL_ROBOTIC_ARM/Materials/Steel___Satin
*  **Prim路径 (Prim Path):**/World/INDUSTRIAL_ROBOTIC_ARM/Materials/Steel___Satin
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/INDUSTRIAL_ROBOTIC_ARM/Materials/Steel___Satin/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/INDUSTRIAL_ROBOTIC_ARM/Materials/Steel___Satin/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.627, 0.627, 0.627)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0.957705'


---


### /World/INDUSTRIAL_ROBOTIC_ARM/Materials/Paint___Enamel_Glossy_Black
*  **Prim路径 (Prim Path):**/World/INDUSTRIAL_ROBOTIC_ARM/Materials/Paint___Enamel_Glossy_Black
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/INDUSTRIAL_ROBOTIC_ARM/Materials/Paint___Enamel_Glossy_Black/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/INDUSTRIAL_ROBOTIC_ARM/Materials/Paint___Enamel_Glossy_Black/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f] = '(0.098, 0.098, 0.098)'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float] = '0'
           *   'normal' [normal3f] = '(0.000, 0.000, 1.000)'
           *   'occlusion' [float] = '1'
           *   'roughness' [float] = '0.957705'


---


### /World/processed_Robotic_Manipulator_low_poly/Materials/Robot_hand
*  **Prim路径 (Prim Path):**/World/processed_Robotic_Manipulator_low_poly/Materials/Robot_hand
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/processed_Robotic_Manipulator_low_poly/Materials/Robot_hand/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/processed_Robotic_Manipulator_low_poly/Materials/Robot_hand/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f]
               *   Connected: '/World/processed_Robotic_Manipulator_low_poly/Materials/Robot_hand/tex_base.outputs:rgb' @ '/World/processed_Robotic_Manipulator_low_poly/Materials/Robot_hand/tex_base'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/Robot_hand_baseColor.jpg'
           *   'emissiveColor' [color3f] = '(0.000, 0.000, 0.000)'
           *   'metallic' [float]
               *   Connected: '/World/processed_Robotic_Manipulator_low_poly/Materials/Robot_hand/tex_metallic.outputs:r' @ '/World/processed_Robotic_Manipulator_low_poly/Materials/Robot_hand/tex_metallic'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/Robot_hand_metallicRoughness_metal.jpg'
           *   'normal' [normal3f]
               *   Connected: '/World/processed_Robotic_Manipulator_low_poly/Materials/Robot_hand/tex_normal.outputs:rgb' @ '/World/processed_Robotic_Manipulator_low_poly/Materials/Robot_hand/tex_normal'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/Robot_hand_normal.jpg'
           *   'occlusion' [float]
               *   Connected: '/World/processed_Robotic_Manipulator_low_poly/Materials/Robot_hand/tex_occlusion.outputs:r' @ '/World/processed_Robotic_Manipulator_low_poly/Materials/Robot_hand/tex_occlusion'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/Robot_hand_metallicRoughness_occl.jpg'
           *   'roughness' [float]
               *   Connected: '/World/processed_Robotic_Manipulator_low_poly/Materials/Robot_hand/tex_roughness.outputs:r' @ '/World/processed_Robotic_Manipulator_low_poly/Materials/Robot_hand/tex_roughness'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/Robot_hand_metallicRoughness_rough.jpg'
       *   '/World/processed_Robotic_Manipulator_low_poly/Materials/Robot_hand/tex_base' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/Robot_hand_baseColor.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
           *   'file' [asset] = '0/Robot_hand_baseColor.jpg'
           *   'st' [float2]
               *   Connected: '/World/processed_Robotic_Manipulator_low_poly/Materials/Robot_hand/uvset0.outputs:result' @ '/World/processed_Robotic_Manipulator_low_poly/Materials/Robot_hand/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/processed_Robotic_Manipulator_low_poly/Materials/Robot_hand/uvset0' (ID: 'UsdPrimvarReader_float2')
       *   Implementation: 'id'
       *   '/World/processed_Robotic_Manipulator_low_poly/Materials/Robot_hand/tex_metallic' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/Robot_hand_metallicRoughness_metal.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(0.000, 0.000, 0.000, 1.000)'
           *   'file' [asset] = '0/Robot_hand_metallicRoughness_metal.jpg'
           *   'st' [float2]
               *   Connected: '/World/processed_Robotic_Manipulator_low_poly/Materials/Robot_hand/uvset0.outputs:result' @ '/World/processed_Robotic_Manipulator_low_poly/Materials/Robot_hand/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/processed_Robotic_Manipulator_low_poly/Materials/Robot_hand/tex_normal' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/Robot_hand_normal.jpg'
       *   Inputs:
           *   'bias' [float4] = '(-1.000, -1.000, -1.000, -1.000)'
           *   'fallback' [float4] = '(0.000, 0.000, 1.000, 1.000)'
           *   'file' [asset] = '0/Robot_hand_normal.jpg'
           *   'scale' [float4] = '(2.000, 2.000, 2.000, 2.000)'
           *   'st' [float2]
               *   Connected: '/World/processed_Robotic_Manipulator_low_poly/Materials/Robot_hand/uvset0.outputs:result' @ '/World/processed_Robotic_Manipulator_low_poly/Materials/Robot_hand/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/processed_Robotic_Manipulator_low_poly/Materials/Robot_hand/tex_occlusion' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/Robot_hand_metallicRoughness_occl.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(1.000, 0.000, 0.000, 1.000)'
           *   'file' [asset] = '0/Robot_hand_metallicRoughness_occl.jpg'
           *   'st' [float2]
               *   Connected: '/World/processed_Robotic_Manipulator_low_poly/Materials/Robot_hand/uvset0.outputs:result' @ '/World/processed_Robotic_Manipulator_low_poly/Materials/Robot_hand/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/processed_Robotic_Manipulator_low_poly/Materials/Robot_hand/tex_roughness' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/Robot_hand_metallicRoughness_rough.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(1.000, 0.000, 0.000, 1.000)'
           *   'file' [asset] = '0/Robot_hand_metallicRoughness_rough.jpg'
           *   'st' [float2]
               *   Connected: '/World/processed_Robotic_Manipulator_low_poly/Materials/Robot_hand/uvset0.outputs:result' @ '/World/processed_Robotic_Manipulator_low_poly/Materials/Robot_hand/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'


---


### /World/processed_Robotic_Manipulator_low_poly/Materials/Stand
*  **Prim路径 (Prim Path):**/World/processed_Robotic_Manipulator_low_poly/Materials/Stand
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface' -> '/World/processed_Robotic_Manipulator_low_poly/Materials/Stand/pbr_shader'
       *   Shader ID: 'UsdPreviewSurface'
       *   Connection: 'surface' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/processed_Robotic_Manipulator_low_poly/Materials/Stand/pbr_shader' (ID: 'UsdPreviewSurface')
       *   Implementation: 'id'
       *   Inputs:
           *   'diffuseColor' [color3f]
               *   Connected: '/World/processed_Robotic_Manipulator_low_poly/Materials/Stand/tex_base.outputs:rgb' @ '/World/processed_Robotic_Manipulator_low_poly/Materials/Stand/tex_base'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/Stand_baseColor.jpg'
           *   'emissiveColor' [color3f]
               *   Connected: '/World/processed_Robotic_Manipulator_low_poly/Materials/Stand/tex_emissive.outputs:rgb' @ '/World/processed_Robotic_Manipulator_low_poly/Materials/Stand/tex_emissive'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/Stand_emissive.jpg'
           *   'metallic' [float]
               *   Connected: '/World/processed_Robotic_Manipulator_low_poly/Materials/Stand/tex_metallic.outputs:r' @ '/World/processed_Robotic_Manipulator_low_poly/Materials/Stand/tex_metallic'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/Stand_metallicRoughness_metal.jpg'
           *   'normal' [normal3f]
               *   Connected: '/World/processed_Robotic_Manipulator_low_poly/Materials/Stand/tex_normal.outputs:rgb' @ '/World/processed_Robotic_Manipulator_low_poly/Materials/Stand/tex_normal'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/Stand_normal.jpg'
           *   'occlusion' [float]
               *   Connected: '/World/processed_Robotic_Manipulator_low_poly/Materials/Stand/tex_occlusion.outputs:r' @ '/World/processed_Robotic_Manipulator_low_poly/Materials/Stand/tex_occlusion'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/Stand_metallicRoughness_occl.jpg'
           *   'roughness' [float]
               *   Connected: '/World/processed_Robotic_Manipulator_low_poly/Materials/Stand/tex_roughness.outputs:r' @ '/World/processed_Robotic_Manipulator_low_poly/Materials/Stand/tex_roughness'
                   *   Shader ID: 'UsdUVTexture'
                   *   Texture: '0/Stand_metallicRoughness_rough.jpg'
       *   '/World/processed_Robotic_Manipulator_low_poly/Materials/Stand/tex_base' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/Stand_baseColor.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(1.000, 1.000, 1.000, 1.000)'
           *   'file' [asset] = '0/Stand_baseColor.jpg'
           *   'st' [float2]
               *   Connected: '/World/processed_Robotic_Manipulator_low_poly/Materials/Stand/uvset0.outputs:result' @ '/World/processed_Robotic_Manipulator_low_poly/Materials/Stand/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/processed_Robotic_Manipulator_low_poly/Materials/Stand/uvset0' (ID: 'UsdPrimvarReader_float2')
       *   Implementation: 'id'
       *   '/World/processed_Robotic_Manipulator_low_poly/Materials/Stand/tex_emissive' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/Stand_emissive.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(0.000, 0.000, 0.000, 1.000)'
           *   'file' [asset] = '0/Stand_emissive.jpg'
           *   'st' [float2]
               *   Connected: '/World/processed_Robotic_Manipulator_low_poly/Materials/Stand/uvset0.outputs:result' @ '/World/processed_Robotic_Manipulator_low_poly/Materials/Stand/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/processed_Robotic_Manipulator_low_poly/Materials/Stand/tex_metallic' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/Stand_metallicRoughness_metal.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(0.000, 0.000, 0.000, 1.000)'
           *   'file' [asset] = '0/Stand_metallicRoughness_metal.jpg'
           *   'st' [float2]
               *   Connected: '/World/processed_Robotic_Manipulator_low_poly/Materials/Stand/uvset0.outputs:result' @ '/World/processed_Robotic_Manipulator_low_poly/Materials/Stand/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/processed_Robotic_Manipulator_low_poly/Materials/Stand/tex_normal' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/Stand_normal.jpg'
       *   Inputs:
           *   'bias' [float4] = '(-1.000, -1.000, -1.000, -1.000)'
           *   'fallback' [float4] = '(0.000, 0.000, 1.000, 1.000)'
           *   'file' [asset] = '0/Stand_normal.jpg'
           *   'scale' [float4] = '(2.000, 2.000, 2.000, 2.000)'
           *   'st' [float2]
               *   Connected: '/World/processed_Robotic_Manipulator_low_poly/Materials/Stand/uvset0.outputs:result' @ '/World/processed_Robotic_Manipulator_low_poly/Materials/Stand/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/processed_Robotic_Manipulator_low_poly/Materials/Stand/tex_occlusion' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/Stand_metallicRoughness_occl.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(1.000, 0.000, 0.000, 1.000)'
           *   'file' [asset] = '0/Stand_metallicRoughness_occl.jpg'
           *   'st' [float2]
               *   Connected: '/World/processed_Robotic_Manipulator_low_poly/Materials/Stand/uvset0.outputs:result' @ '/World/processed_Robotic_Manipulator_low_poly/Materials/Stand/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'
       *   '/World/processed_Robotic_Manipulator_low_poly/Materials/Stand/tex_roughness' (ID: 'UsdUVTexture')
       *   Implementation: 'id'
       *   纹理引用 (Texture Assets):
           *   '0/Stand_metallicRoughness_rough.jpg'
       *   Inputs:
           *   'fallback' [float4] = '(1.000, 0.000, 0.000, 1.000)'
           *   'file' [asset] = '0/Stand_metallicRoughness_rough.jpg'
           *   'st' [float2]
               *   Connected: '/World/processed_Robotic_Manipulator_low_poly/Materials/Stand/uvset0.outputs:result' @ '/World/processed_Robotic_Manipulator_low_poly/Materials/Stand/uvset0'
                   *   Shader ID: 'UsdPrimvarReader_float2'


---
