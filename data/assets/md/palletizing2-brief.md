# USDA场景描述文档:palletizing2.usda

## 1.场景元数据(Scene Metadata)
*  **USDA文件路径(USDA File Path):**`/media/simple/another_Documents/isaacsim_assets/scenedata/palletizing2.usda`
*  **默认Prim (Default Prim):**'Not Set'
*  **单位与坐标系 (Units & Coordinate System):**
   *   **米(Meters Per Unit):**1.0
   *   **Up Axis:**Z
* **场景描述(Scene Describe):** 该码垛车间呈现出规模宏大的矩阵式布局，由五组以上并行的标准化单元协同作业。每一单元由银色高架输送线、集成了六轴协作机器人的白色工作站及亮黄色AGV构成。物料通过输送带密集输入，由白色机器人精准分拣并堆叠至AGV载货框中。整体规划采用“线性输送+单元处理+柔性接驳”的复合架构，以大理石纹地面为基准，通过高度重复的模块化设计实现了空间极致利用与产能灵活调节，深刻诠释了工业4.0高精度、无人化的柔性制造逻辑。
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

## 3. 外部引用Xform简报(Referenced Xforms)

### '/World/factory' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/scene/factory/factory.usdc
* BBox (world): size=(49.139, 19.897, 67.754), center=(0.761, 0.769, 9.470)
* 几何统计: Mesh=7, Vertices=2044, Faces=946
* 子Mesh材质: /World/factory/Meshes/Sketchfab_model/cc020ec10d3e484ab6eb350963eb38d0_fbx/RootNode/Factory002/Factory002_WindowsIndustrial_frontSolid_OpenWindows_Mat_0/Factory002_WindowsIndustrial_frontSolid_OpenWindows_Mat_0 -> 未绑定, /World/factory/Meshes/Sketchfab_model/cc020ec10d3e484ab6eb350963eb38d0_fbx/RootNode/Factory002/Factory002_WindowsIndustrial_frontSolid_Mat_0/Factory002_WindowsIndustrial_frontSolid_Mat_0 -> 未绑定, /World/factory/Meshes/Sketchfab_model/cc020ec10d3e484ab6eb350963eb38d0_fbx/RootNode/Factory002/Factory002_WindowsIndustrial_frontDoorclosed_Mat_0/Factory002_WindowsIndustrial_frontDoorclosed_Mat_0 -> 未绑定, /World/factory/Meshes/Sketchfab_model/cc020ec10d3e484ab6eb350963eb38d0_fbx/RootNode/Factory002/Factory002_WindowsIndustrial_frontDoorOpen_Mat_0/Factory002_WindowsIndustrial_frontDoorOpen_Mat_0 -> 未绑定, /World/factory/Meshes/Sketchfab_model/cc020ec10d3e484ab6eb350963eb38d0_fbx/RootNode/Factory002/Factory002_WindowsIndustrial_front_Mat_0/Factory002_WindowsIndustrial_front_Mat_0 -> 未绑定, /World/factory/Meshes/Sketchfab_model/cc020ec10d3e484ab6eb350963eb38d0_fbx/RootNode/Factory002/Factory002_11___Default_0/Factory002_11___Default_0 -> 未绑定, /World/factory/Meshes/Sketchfab_model/cc020ec10d3e484ab6eb350963eb38d0_fbx/RootNode/Object001/Object001_20___Default_0/Object001_20___Default_0 -> 未绑定


---


### '/World/agv_1' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/5.0/Isaac/Robots/Idealworks/iwhub/iw_hub.usd
* BBox (world): size=(1.431, 0.659, 0.231), center=(-18.718, 29.251, 0.275)
* 几何统计: Mesh=8, Vertices=388563, Faces=382917
* 子Mesh材质: /World/agv_1/chassis/Body/Body/Mesh -> /World/agv_1/chassis/Body/Looks/Robot, /World/agv_1/left_wheel/Left_Wheel/Left_Wheel/Mesh_002 -> /World/agv_1/left_wheel/Left_Wheel/Looks/Robot, /World/agv_1/right_wheel/Right_Wheel/Right_Wheel/Mesh_005 -> /World/agv_1/right_wheel/Right_Wheel/Looks/Robot, /World/agv_1/lift/Lift/Lift/Mesh_012 -> /World/agv_1/lift/Lift/Looks/Robot, /World/agv_1/left_swivel/Left_Swivel/STR_Left_Swivel -> /World/agv_1/left_swivel/Left_Swivel/materials/Looks/Robot, /World/agv_1/right_swivel/Right_Swivel/STR_Right_Swivel -> /World/agv_1/right_swivel/Right_Swivel/materials/Looks/Robot, /World/agv_1/left_caster/Inner_Left_Wheel/STR_Inner_Left_Wheel -> /World/agv_1/left_caster/Inner_Left_Wheel/materials/Looks/Robot, /World/agv_1/right_caster/Inner_Right_Wheel/STR_Inner_Right_Wheel -> /World/agv_1/right_caster/Inner_Right_Wheel/materials/Looks/Robot
* 材质摘要:
 * /World/agv_1/chassis/Body/Looks/Robot -> Inputs: 'emissive_intensity=8000', 'metallic_texture_influence=0.9', 'reflection_roughness_texture_influence=1', Textures: 'Textures/STL_Robot_albedo.<UDIM>.png', 'Textures/STL_Robot_emissive.<UDIM>.png', 'Textures/STL_Robot_normal.<UDIM>.png', 'Textures/STL_Robot_orm.<UDIM>.png'
 * /World/agv_1/left_caster/Inner_Left_Wheel/materials/Looks/Robot -> Inputs: 'metallic_texture_influence=1', 'reflection_roughness_texture_influence=1', Textures: 'Textures/STL_Robot_albedo.%3CUDIM%3E.png', 'Textures/STL_Robot_normal.%3CUDIM%3E.png', 'Textures/STL_Robot_orm.%3CUDIM%3E.png'
 * /World/agv_1/left_swivel/Left_Swivel/materials/Looks/Robot -> Inputs: 'metallic_texture_influence=1', 'reflection_roughness_texture_influence=1', Textures: 'Textures/STL_Robot_albedo.%3CUDIM%3E.png', 'Textures/STL_Robot_normal.%3CUDIM%3E.png', 'Textures/STL_Robot_orm.%3CUDIM%3E.png'
 * /World/agv_1/left_wheel/Left_Wheel/Looks/Robot -> Inputs: 'metallic_texture_influence=1', 'reflection_roughness_texture_influence=1', Textures: 'Textures/STL_Robot_albedo.<UDIM>.png', 'Textures/STL_Robot_normal.<UDIM>.png', 'Textures/STL_Robot_orm.<UDIM>.png'
 * /World/agv_1/lift/Lift/Looks/Robot -> Inputs: 'metallic_texture_influence=0.901', 'reflection_roughness_texture_influence=1', Textures: 'Textures/STL_Robot_albedo.<UDIM>.png', 'Textures/STL_Robot_normal.<UDIM>.png', 'Textures/STL_Robot_orm.<UDIM>.png'
 * /World/agv_1/right_caster/Inner_Right_Wheel/materials/Looks/Robot -> Inputs: 'metallic_texture_influence=1', 'reflection_roughness_texture_influence=1', Textures: 'Textures/STL_Robot_albedo.%3CUDIM%3E.png', 'Textures/STL_Robot_normal.%3CUDIM%3E.png', 'Textures/STL_Robot_orm.%3CUDIM%3E.png'
 * /World/agv_1/right_swivel/Right_Swivel/materials/Looks/Robot -> Inputs: 'metallic_texture_influence=1', 'reflection_roughness_texture_influence=1', Textures: 'Textures/STL_Robot_albedo.%3CUDIM%3E.png', 'Textures/STL_Robot_normal.%3CUDIM%3E.png', 'Textures/STL_Robot_orm.%3CUDIM%3E.png'
 * /World/agv_1/right_wheel/Right_Wheel/Looks/Robot -> Inputs: 'metallic_texture_influence=1', 'reflection_roughness_texture_influence=1', Textures: 'Textures/STL_Robot_albedo.<UDIM>.png', 'Textures/STL_Robot_normal.<UDIM>.png', 'Textures/STL_Robot_orm.<UDIM>.png'


---


### '/World/agv_1/chassis/Body' (Xform)
* 引用: reference:HighResProps/Body_v2.usd
* BBox (world): size=(1.431, 0.652, 0.197), center=(-18.718, 29.250, 0.289)
* 几何统计: Mesh=1, Vertices=277878, Faces=273290
* 子Mesh材质: /World/agv_1/chassis/Body/Body/Mesh -> /World/agv_1/chassis/Body/Looks/Robot
* 材质摘要:
 * /World/agv_1/chassis/Body/Looks/Robot -> Inputs: 'emissive_intensity=8000', 'metallic_texture_influence=0.9', 'reflection_roughness_texture_influence=1', Textures: 'Textures/STL_Robot_albedo.<UDIM>.png', 'Textures/STL_Robot_emissive.<UDIM>.png', 'Textures/STL_Robot_normal.<UDIM>.png', 'Textures/STL_Robot_orm.<UDIM>.png'


---


### '/World/agv_1/left_wheel/Left_Wheel' (Xform)
* 引用: reference:HighResProps/Left_Wheel.usd
* BBox (world): size=(0.162, 0.057, 0.162), center=(-18.400, 29.540, 0.240)
* 几何统计: Mesh=1, Vertices=15925, Faces=15672
* 子Mesh材质: /World/agv_1/left_wheel/Left_Wheel/Left_Wheel/Mesh_002 -> /World/agv_1/left_wheel/Left_Wheel/Looks/Robot
* 材质摘要:
 * /World/agv_1/left_wheel/Left_Wheel/Looks/Robot -> Inputs: 'metallic_texture_influence=1', 'reflection_roughness_texture_influence=1', Textures: 'Textures/STL_Robot_albedo.<UDIM>.png', 'Textures/STL_Robot_normal.<UDIM>.png', 'Textures/STL_Robot_orm.<UDIM>.png'


---


### '/World/agv_1/right_wheel/Right_Wheel' (Xform)
* 引用: reference:HighResProps/Right_Wheel.usd
* BBox (world): size=(0.162, 0.057, 0.162), center=(-18.400, 28.960, 0.240)
* 几何统计: Mesh=1, Vertices=15925, Faces=15672
* 子Mesh材质: /World/agv_1/right_wheel/Right_Wheel/Right_Wheel/Mesh_005 -> /World/agv_1/right_wheel/Right_Wheel/Looks/Robot
* 材质摘要:
 * /World/agv_1/right_wheel/Right_Wheel/Looks/Robot -> Inputs: 'metallic_texture_influence=1', 'reflection_roughness_texture_influence=1', Textures: 'Textures/STL_Robot_albedo.<UDIM>.png', 'Textures/STL_Robot_normal.<UDIM>.png', 'Textures/STL_Robot_orm.<UDIM>.png'


---


### '/World/agv_1/lift/Lift' (Xform)
* 引用: reference:HighResProps/Lift_v2.usd
* BBox (world): size=(1.023, 0.659, 0.169), center=(-18.656, 29.251, 0.306)
* 几何统计: Mesh=1, Vertices=78479, Faces=77595
* 子Mesh材质: /World/agv_1/lift/Lift/Lift/Mesh_012 -> /World/agv_1/lift/Lift/Looks/Robot
* 材质摘要:
 * /World/agv_1/lift/Lift/Looks/Robot -> Inputs: 'metallic_texture_influence=0.901', 'reflection_roughness_texture_influence=1', Textures: 'Textures/STL_Robot_albedo.<UDIM>.png', 'Textures/STL_Robot_normal.<UDIM>.png', 'Textures/STL_Robot_orm.<UDIM>.png'


---


### '/World/agv_1/left_swivel/Left_Swivel' (Xform)
* 引用: reference:HighResProps/Left_Swivel.usd
* BBox (world): size=(0.095, 0.033, 0.111), center=(-19.077, 29.343, 0.263)
* 几何统计: Mesh=1, Vertices=16, Faces=24
* 子Mesh材质: /World/agv_1/left_swivel/Left_Swivel/STR_Left_Swivel -> /World/agv_1/left_swivel/Left_Swivel/materials/Looks/Robot
* 材质摘要:
 * /World/agv_1/left_swivel/Left_Swivel/materials/Looks/Robot -> Inputs: 'metallic_texture_influence=1', 'reflection_roughness_texture_influence=1', Textures: 'Textures/STL_Robot_albedo.%3CUDIM%3E.png', 'Textures/STL_Robot_normal.%3CUDIM%3E.png', 'Textures/STL_Robot_orm.%3CUDIM%3E.png'


---


### '/World/agv_1/left_swivel/Left_Swivel/materials' (Xform)
* 引用: payload:./materials.usd
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(0.000, 0.000, 0.000)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/agv_1/right_swivel/Right_Swivel' (Xform)
* 引用: reference:HighResProps/Right_Swivel.usd
* BBox (world): size=(0.095, 0.033, 0.111), center=(-19.077, 29.157, 0.263)
* 几何统计: Mesh=1, Vertices=16, Faces=24
* 子Mesh材质: /World/agv_1/right_swivel/Right_Swivel/STR_Right_Swivel -> /World/agv_1/right_swivel/Right_Swivel/materials/Looks/Robot
* 材质摘要:
 * /World/agv_1/right_swivel/Right_Swivel/materials/Looks/Robot -> Inputs: 'metallic_texture_influence=1', 'reflection_roughness_texture_influence=1', Textures: 'Textures/STL_Robot_albedo.%3CUDIM%3E.png', 'Textures/STL_Robot_normal.%3CUDIM%3E.png', 'Textures/STL_Robot_orm.%3CUDIM%3E.png'


---


### '/World/agv_1/right_swivel/Right_Swivel/materials' (Xform)
* 引用: payload:./materials.usd
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(0.000, 0.000, 0.000)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/agv_1/left_caster/Inner_Left_Wheel' (Xform)
* 引用: reference:HighResProps/Inner_Left_Wheel.usd
* BBox (world): size=(0.135, 0.029, 0.135), center=(-19.077, 29.343, 0.230)
* 几何统计: Mesh=1, Vertices=162, Faces=320
* 子Mesh材质: /World/agv_1/left_caster/Inner_Left_Wheel/STR_Inner_Left_Wheel -> /World/agv_1/left_caster/Inner_Left_Wheel/materials/Looks/Robot
* 材质摘要:
 * /World/agv_1/left_caster/Inner_Left_Wheel/materials/Looks/Robot -> Inputs: 'metallic_texture_influence=1', 'reflection_roughness_texture_influence=1', Textures: 'Textures/STL_Robot_albedo.%3CUDIM%3E.png', 'Textures/STL_Robot_normal.%3CUDIM%3E.png', 'Textures/STL_Robot_orm.%3CUDIM%3E.png'


---


### '/World/agv_1/left_caster/Inner_Left_Wheel/materials' (Xform)
* 引用: payload:./materials.usd
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(0.000, 0.000, 0.000)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/agv_1/right_caster/Inner_Right_Wheel' (Xform)
* 引用: reference:HighResProps/Inner_Right_Wheel.usd
* BBox (world): size=(0.135, 0.029, 0.135), center=(-19.077, 29.157, 0.230)
* 几何统计: Mesh=1, Vertices=162, Faces=320
* 子Mesh材质: /World/agv_1/right_caster/Inner_Right_Wheel/STR_Inner_Right_Wheel -> /World/agv_1/right_caster/Inner_Right_Wheel/materials/Looks/Robot
* 材质摘要:
 * /World/agv_1/right_caster/Inner_Right_Wheel/materials/Looks/Robot -> Inputs: 'metallic_texture_influence=1', 'reflection_roughness_texture_influence=1', Textures: 'Textures/STL_Robot_albedo.%3CUDIM%3E.png', 'Textures/STL_Robot_normal.%3CUDIM%3E.png', 'Textures/STL_Robot_orm.%3CUDIM%3E.png'


---


### '/World/agv_1/right_caster/Inner_Right_Wheel/materials' (Xform)
* 引用: payload:./materials.usd
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(0.000, 0.000, 0.000)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/agv_2' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/5.0/Isaac/Robots/Idealworks/iwhub/iw_hub.usd
* BBox (world): size=(1.431, 0.659, 0.231), center=(-13.718, 29.251, 0.275)
* 几何统计: Mesh=8, Vertices=388563, Faces=382917
* 子Mesh材质: /World/agv_2/chassis/Body/Body/Mesh -> /World/agv_2/chassis/Body/Looks/Robot, /World/agv_2/left_wheel/Left_Wheel/Left_Wheel/Mesh_002 -> /World/agv_2/left_wheel/Left_Wheel/Looks/Robot, /World/agv_2/right_wheel/Right_Wheel/Right_Wheel/Mesh_005 -> /World/agv_2/right_wheel/Right_Wheel/Looks/Robot, /World/agv_2/lift/Lift/Lift/Mesh_012 -> /World/agv_2/lift/Lift/Looks/Robot, /World/agv_2/left_swivel/Left_Swivel/STR_Left_Swivel -> /World/agv_2/left_swivel/Left_Swivel/materials/Looks/Robot, /World/agv_2/right_swivel/Right_Swivel/STR_Right_Swivel -> /World/agv_2/right_swivel/Right_Swivel/materials/Looks/Robot, /World/agv_2/left_caster/Inner_Left_Wheel/STR_Inner_Left_Wheel -> /World/agv_2/left_caster/Inner_Left_Wheel/materials/Looks/Robot, /World/agv_2/right_caster/Inner_Right_Wheel/STR_Inner_Right_Wheel -> /World/agv_2/right_caster/Inner_Right_Wheel/materials/Looks/Robot
* 材质摘要:
 * /World/agv_2/chassis/Body/Looks/Robot -> Inputs: 'emissive_intensity=8000', 'metallic_texture_influence=0.9', 'reflection_roughness_texture_influence=1', Textures: 'Textures/STL_Robot_albedo.<UDIM>.png', 'Textures/STL_Robot_emissive.<UDIM>.png', 'Textures/STL_Robot_normal.<UDIM>.png', 'Textures/STL_Robot_orm.<UDIM>.png'
 * /World/agv_2/left_caster/Inner_Left_Wheel/materials/Looks/Robot -> Inputs: 'metallic_texture_influence=1', 'reflection_roughness_texture_influence=1', Textures: 'Textures/STL_Robot_albedo.%3CUDIM%3E.png', 'Textures/STL_Robot_normal.%3CUDIM%3E.png', 'Textures/STL_Robot_orm.%3CUDIM%3E.png'
 * /World/agv_2/left_swivel/Left_Swivel/materials/Looks/Robot -> Inputs: 'metallic_texture_influence=1', 'reflection_roughness_texture_influence=1', Textures: 'Textures/STL_Robot_albedo.%3CUDIM%3E.png', 'Textures/STL_Robot_normal.%3CUDIM%3E.png', 'Textures/STL_Robot_orm.%3CUDIM%3E.png'
 * /World/agv_2/left_wheel/Left_Wheel/Looks/Robot -> Inputs: 'metallic_texture_influence=1', 'reflection_roughness_texture_influence=1', Textures: 'Textures/STL_Robot_albedo.<UDIM>.png', 'Textures/STL_Robot_normal.<UDIM>.png', 'Textures/STL_Robot_orm.<UDIM>.png'
 * /World/agv_2/lift/Lift/Looks/Robot -> Inputs: 'metallic_texture_influence=0.901', 'reflection_roughness_texture_influence=1', Textures: 'Textures/STL_Robot_albedo.<UDIM>.png', 'Textures/STL_Robot_normal.<UDIM>.png', 'Textures/STL_Robot_orm.<UDIM>.png'
 * /World/agv_2/right_caster/Inner_Right_Wheel/materials/Looks/Robot -> Inputs: 'metallic_texture_influence=1', 'reflection_roughness_texture_influence=1', Textures: 'Textures/STL_Robot_albedo.%3CUDIM%3E.png', 'Textures/STL_Robot_normal.%3CUDIM%3E.png', 'Textures/STL_Robot_orm.%3CUDIM%3E.png'
 * /World/agv_2/right_swivel/Right_Swivel/materials/Looks/Robot -> Inputs: 'metallic_texture_influence=1', 'reflection_roughness_texture_influence=1', Textures: 'Textures/STL_Robot_albedo.%3CUDIM%3E.png', 'Textures/STL_Robot_normal.%3CUDIM%3E.png', 'Textures/STL_Robot_orm.%3CUDIM%3E.png'
 * /World/agv_2/right_wheel/Right_Wheel/Looks/Robot -> Inputs: 'metallic_texture_influence=1', 'reflection_roughness_texture_influence=1', Textures: 'Textures/STL_Robot_albedo.<UDIM>.png', 'Textures/STL_Robot_normal.<UDIM>.png', 'Textures/STL_Robot_orm.<UDIM>.png'


---


### '/World/agv_2/chassis/Body' (Xform)
* 引用: reference:HighResProps/Body_v2.usd
* BBox (world): size=(1.431, 0.652, 0.197), center=(-13.718, 29.250, 0.289)
* 几何统计: Mesh=1, Vertices=277878, Faces=273290
* 子Mesh材质: /World/agv_2/chassis/Body/Body/Mesh -> /World/agv_2/chassis/Body/Looks/Robot
* 材质摘要:
 * /World/agv_2/chassis/Body/Looks/Robot -> Inputs: 'emissive_intensity=8000', 'metallic_texture_influence=0.9', 'reflection_roughness_texture_influence=1', Textures: 'Textures/STL_Robot_albedo.<UDIM>.png', 'Textures/STL_Robot_emissive.<UDIM>.png', 'Textures/STL_Robot_normal.<UDIM>.png', 'Textures/STL_Robot_orm.<UDIM>.png'


---


### '/World/agv_2/left_wheel/Left_Wheel' (Xform)
* 引用: reference:HighResProps/Left_Wheel.usd
* BBox (world): size=(0.162, 0.057, 0.162), center=(-13.400, 29.540, 0.240)
* 几何统计: Mesh=1, Vertices=15925, Faces=15672
* 子Mesh材质: /World/agv_2/left_wheel/Left_Wheel/Left_Wheel/Mesh_002 -> /World/agv_2/left_wheel/Left_Wheel/Looks/Robot
* 材质摘要:
 * /World/agv_2/left_wheel/Left_Wheel/Looks/Robot -> Inputs: 'metallic_texture_influence=1', 'reflection_roughness_texture_influence=1', Textures: 'Textures/STL_Robot_albedo.<UDIM>.png', 'Textures/STL_Robot_normal.<UDIM>.png', 'Textures/STL_Robot_orm.<UDIM>.png'


---


### '/World/agv_2/right_wheel/Right_Wheel' (Xform)
* 引用: reference:HighResProps/Right_Wheel.usd
* BBox (world): size=(0.162, 0.057, 0.162), center=(-13.400, 28.960, 0.240)
* 几何统计: Mesh=1, Vertices=15925, Faces=15672
* 子Mesh材质: /World/agv_2/right_wheel/Right_Wheel/Right_Wheel/Mesh_005 -> /World/agv_2/right_wheel/Right_Wheel/Looks/Robot
* 材质摘要:
 * /World/agv_2/right_wheel/Right_Wheel/Looks/Robot -> Inputs: 'metallic_texture_influence=1', 'reflection_roughness_texture_influence=1', Textures: 'Textures/STL_Robot_albedo.<UDIM>.png', 'Textures/STL_Robot_normal.<UDIM>.png', 'Textures/STL_Robot_orm.<UDIM>.png'


---


### '/World/agv_2/lift/Lift' (Xform)
* 引用: reference:HighResProps/Lift_v2.usd
* BBox (world): size=(1.023, 0.659, 0.169), center=(-13.656, 29.251, 0.306)
* 几何统计: Mesh=1, Vertices=78479, Faces=77595
* 子Mesh材质: /World/agv_2/lift/Lift/Lift/Mesh_012 -> /World/agv_2/lift/Lift/Looks/Robot
* 材质摘要:
 * /World/agv_2/lift/Lift/Looks/Robot -> Inputs: 'metallic_texture_influence=0.901', 'reflection_roughness_texture_influence=1', Textures: 'Textures/STL_Robot_albedo.<UDIM>.png', 'Textures/STL_Robot_normal.<UDIM>.png', 'Textures/STL_Robot_orm.<UDIM>.png'


---


### '/World/agv_2/left_swivel/Left_Swivel' (Xform)
* 引用: reference:HighResProps/Left_Swivel.usd
* BBox (world): size=(0.095, 0.033, 0.111), center=(-14.077, 29.343, 0.263)
* 几何统计: Mesh=1, Vertices=16, Faces=24
* 子Mesh材质: /World/agv_2/left_swivel/Left_Swivel/STR_Left_Swivel -> /World/agv_2/left_swivel/Left_Swivel/materials/Looks/Robot
* 材质摘要:
 * /World/agv_2/left_swivel/Left_Swivel/materials/Looks/Robot -> Inputs: 'metallic_texture_influence=1', 'reflection_roughness_texture_influence=1', Textures: 'Textures/STL_Robot_albedo.%3CUDIM%3E.png', 'Textures/STL_Robot_normal.%3CUDIM%3E.png', 'Textures/STL_Robot_orm.%3CUDIM%3E.png'


---


### '/World/agv_2/left_swivel/Left_Swivel/materials' (Xform)
* 引用: payload:./materials.usd
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(0.000, 0.000, 0.000)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/agv_2/right_swivel/Right_Swivel' (Xform)
* 引用: reference:HighResProps/Right_Swivel.usd
* BBox (world): size=(0.095, 0.033, 0.111), center=(-14.077, 29.157, 0.263)
* 几何统计: Mesh=1, Vertices=16, Faces=24
* 子Mesh材质: /World/agv_2/right_swivel/Right_Swivel/STR_Right_Swivel -> /World/agv_2/right_swivel/Right_Swivel/materials/Looks/Robot
* 材质摘要:
 * /World/agv_2/right_swivel/Right_Swivel/materials/Looks/Robot -> Inputs: 'metallic_texture_influence=1', 'reflection_roughness_texture_influence=1', Textures: 'Textures/STL_Robot_albedo.%3CUDIM%3E.png', 'Textures/STL_Robot_normal.%3CUDIM%3E.png', 'Textures/STL_Robot_orm.%3CUDIM%3E.png'


---


### '/World/agv_2/right_swivel/Right_Swivel/materials' (Xform)
* 引用: payload:./materials.usd
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(0.000, 0.000, 0.000)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/agv_2/left_caster/Inner_Left_Wheel' (Xform)
* 引用: reference:HighResProps/Inner_Left_Wheel.usd
* BBox (world): size=(0.135, 0.029, 0.135), center=(-14.077, 29.343, 0.230)
* 几何统计: Mesh=1, Vertices=162, Faces=320
* 子Mesh材质: /World/agv_2/left_caster/Inner_Left_Wheel/STR_Inner_Left_Wheel -> /World/agv_2/left_caster/Inner_Left_Wheel/materials/Looks/Robot
* 材质摘要:
 * /World/agv_2/left_caster/Inner_Left_Wheel/materials/Looks/Robot -> Inputs: 'metallic_texture_influence=1', 'reflection_roughness_texture_influence=1', Textures: 'Textures/STL_Robot_albedo.%3CUDIM%3E.png', 'Textures/STL_Robot_normal.%3CUDIM%3E.png', 'Textures/STL_Robot_orm.%3CUDIM%3E.png'


---


### '/World/agv_2/left_caster/Inner_Left_Wheel/materials' (Xform)
* 引用: payload:./materials.usd
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(0.000, 0.000, 0.000)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/agv_2/right_caster/Inner_Right_Wheel' (Xform)
* 引用: reference:HighResProps/Inner_Right_Wheel.usd
* BBox (world): size=(0.135, 0.029, 0.135), center=(-14.077, 29.157, 0.230)
* 几何统计: Mesh=1, Vertices=162, Faces=320
* 子Mesh材质: /World/agv_2/right_caster/Inner_Right_Wheel/STR_Inner_Right_Wheel -> /World/agv_2/right_caster/Inner_Right_Wheel/materials/Looks/Robot
* 材质摘要:
 * /World/agv_2/right_caster/Inner_Right_Wheel/materials/Looks/Robot -> Inputs: 'metallic_texture_influence=1', 'reflection_roughness_texture_influence=1', Textures: 'Textures/STL_Robot_albedo.%3CUDIM%3E.png', 'Textures/STL_Robot_normal.%3CUDIM%3E.png', 'Textures/STL_Robot_orm.%3CUDIM%3E.png'


---


### '/World/agv_2/right_caster/Inner_Right_Wheel/materials' (Xform)
* 引用: payload:./materials.usd
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(0.000, 0.000, 0.000)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/agv_3' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/5.0/Isaac/Robots/Idealworks/iwhub/iw_hub.usd
* BBox (world): size=(1.431, 0.659, 0.231), center=(-8.718, 29.251, 0.275)
* 几何统计: Mesh=8, Vertices=388563, Faces=382917
* 子Mesh材质: /World/agv_3/chassis/Body/Body/Mesh -> /World/agv_3/chassis/Body/Looks/Robot, /World/agv_3/left_wheel/Left_Wheel/Left_Wheel/Mesh_002 -> /World/agv_3/left_wheel/Left_Wheel/Looks/Robot, /World/agv_3/right_wheel/Right_Wheel/Right_Wheel/Mesh_005 -> /World/agv_3/right_wheel/Right_Wheel/Looks/Robot, /World/agv_3/lift/Lift/Lift/Mesh_012 -> /World/agv_3/lift/Lift/Looks/Robot, /World/agv_3/left_swivel/Left_Swivel/STR_Left_Swivel -> /World/agv_3/left_swivel/Left_Swivel/materials/Looks/Robot, /World/agv_3/right_swivel/Right_Swivel/STR_Right_Swivel -> /World/agv_3/right_swivel/Right_Swivel/materials/Looks/Robot, /World/agv_3/left_caster/Inner_Left_Wheel/STR_Inner_Left_Wheel -> /World/agv_3/left_caster/Inner_Left_Wheel/materials/Looks/Robot, /World/agv_3/right_caster/Inner_Right_Wheel/STR_Inner_Right_Wheel -> /World/agv_3/right_caster/Inner_Right_Wheel/materials/Looks/Robot
* 材质摘要:
 * /World/agv_3/chassis/Body/Looks/Robot -> Inputs: 'emissive_intensity=8000', 'metallic_texture_influence=0.9', 'reflection_roughness_texture_influence=1', Textures: 'Textures/STL_Robot_albedo.<UDIM>.png', 'Textures/STL_Robot_emissive.<UDIM>.png', 'Textures/STL_Robot_normal.<UDIM>.png', 'Textures/STL_Robot_orm.<UDIM>.png'
 * /World/agv_3/left_caster/Inner_Left_Wheel/materials/Looks/Robot -> Inputs: 'metallic_texture_influence=1', 'reflection_roughness_texture_influence=1', Textures: 'Textures/STL_Robot_albedo.%3CUDIM%3E.png', 'Textures/STL_Robot_normal.%3CUDIM%3E.png', 'Textures/STL_Robot_orm.%3CUDIM%3E.png'
 * /World/agv_3/left_swivel/Left_Swivel/materials/Looks/Robot -> Inputs: 'metallic_texture_influence=1', 'reflection_roughness_texture_influence=1', Textures: 'Textures/STL_Robot_albedo.%3CUDIM%3E.png', 'Textures/STL_Robot_normal.%3CUDIM%3E.png', 'Textures/STL_Robot_orm.%3CUDIM%3E.png'
 * /World/agv_3/left_wheel/Left_Wheel/Looks/Robot -> Inputs: 'metallic_texture_influence=1', 'reflection_roughness_texture_influence=1', Textures: 'Textures/STL_Robot_albedo.<UDIM>.png', 'Textures/STL_Robot_normal.<UDIM>.png', 'Textures/STL_Robot_orm.<UDIM>.png'
 * /World/agv_3/lift/Lift/Looks/Robot -> Inputs: 'metallic_texture_influence=0.901', 'reflection_roughness_texture_influence=1', Textures: 'Textures/STL_Robot_albedo.<UDIM>.png', 'Textures/STL_Robot_normal.<UDIM>.png', 'Textures/STL_Robot_orm.<UDIM>.png'
 * /World/agv_3/right_caster/Inner_Right_Wheel/materials/Looks/Robot -> Inputs: 'metallic_texture_influence=1', 'reflection_roughness_texture_influence=1', Textures: 'Textures/STL_Robot_albedo.%3CUDIM%3E.png', 'Textures/STL_Robot_normal.%3CUDIM%3E.png', 'Textures/STL_Robot_orm.%3CUDIM%3E.png'
 * /World/agv_3/right_swivel/Right_Swivel/materials/Looks/Robot -> Inputs: 'metallic_texture_influence=1', 'reflection_roughness_texture_influence=1', Textures: 'Textures/STL_Robot_albedo.%3CUDIM%3E.png', 'Textures/STL_Robot_normal.%3CUDIM%3E.png', 'Textures/STL_Robot_orm.%3CUDIM%3E.png'
 * /World/agv_3/right_wheel/Right_Wheel/Looks/Robot -> Inputs: 'metallic_texture_influence=1', 'reflection_roughness_texture_influence=1', Textures: 'Textures/STL_Robot_albedo.<UDIM>.png', 'Textures/STL_Robot_normal.<UDIM>.png', 'Textures/STL_Robot_orm.<UDIM>.png'


---


### '/World/agv_3/chassis/Body' (Xform)
* 引用: reference:HighResProps/Body_v2.usd
* BBox (world): size=(1.431, 0.652, 0.197), center=(-8.718, 29.250, 0.289)
* 几何统计: Mesh=1, Vertices=277878, Faces=273290
* 子Mesh材质: /World/agv_3/chassis/Body/Body/Mesh -> /World/agv_3/chassis/Body/Looks/Robot
* 材质摘要:
 * /World/agv_3/chassis/Body/Looks/Robot -> Inputs: 'emissive_intensity=8000', 'metallic_texture_influence=0.9', 'reflection_roughness_texture_influence=1', Textures: 'Textures/STL_Robot_albedo.<UDIM>.png', 'Textures/STL_Robot_emissive.<UDIM>.png', 'Textures/STL_Robot_normal.<UDIM>.png', 'Textures/STL_Robot_orm.<UDIM>.png'


---


### '/World/agv_3/left_wheel/Left_Wheel' (Xform)
* 引用: reference:HighResProps/Left_Wheel.usd
* BBox (world): size=(0.162, 0.057, 0.162), center=(-8.400, 29.540, 0.240)
* 几何统计: Mesh=1, Vertices=15925, Faces=15672
* 子Mesh材质: /World/agv_3/left_wheel/Left_Wheel/Left_Wheel/Mesh_002 -> /World/agv_3/left_wheel/Left_Wheel/Looks/Robot
* 材质摘要:
 * /World/agv_3/left_wheel/Left_Wheel/Looks/Robot -> Inputs: 'metallic_texture_influence=1', 'reflection_roughness_texture_influence=1', Textures: 'Textures/STL_Robot_albedo.<UDIM>.png', 'Textures/STL_Robot_normal.<UDIM>.png', 'Textures/STL_Robot_orm.<UDIM>.png'


---


### '/World/agv_3/right_wheel/Right_Wheel' (Xform)
* 引用: reference:HighResProps/Right_Wheel.usd
* BBox (world): size=(0.162, 0.057, 0.162), center=(-8.400, 28.960, 0.240)
* 几何统计: Mesh=1, Vertices=15925, Faces=15672
* 子Mesh材质: /World/agv_3/right_wheel/Right_Wheel/Right_Wheel/Mesh_005 -> /World/agv_3/right_wheel/Right_Wheel/Looks/Robot
* 材质摘要:
 * /World/agv_3/right_wheel/Right_Wheel/Looks/Robot -> Inputs: 'metallic_texture_influence=1', 'reflection_roughness_texture_influence=1', Textures: 'Textures/STL_Robot_albedo.<UDIM>.png', 'Textures/STL_Robot_normal.<UDIM>.png', 'Textures/STL_Robot_orm.<UDIM>.png'


---


### '/World/agv_3/lift/Lift' (Xform)
* 引用: reference:HighResProps/Lift_v2.usd
* BBox (world): size=(1.023, 0.659, 0.169), center=(-8.656, 29.251, 0.306)
* 几何统计: Mesh=1, Vertices=78479, Faces=77595
* 子Mesh材质: /World/agv_3/lift/Lift/Lift/Mesh_012 -> /World/agv_3/lift/Lift/Looks/Robot
* 材质摘要:
 * /World/agv_3/lift/Lift/Looks/Robot -> Inputs: 'metallic_texture_influence=0.901', 'reflection_roughness_texture_influence=1', Textures: 'Textures/STL_Robot_albedo.<UDIM>.png', 'Textures/STL_Robot_normal.<UDIM>.png', 'Textures/STL_Robot_orm.<UDIM>.png'


---


### '/World/agv_3/left_swivel/Left_Swivel' (Xform)
* 引用: reference:HighResProps/Left_Swivel.usd
* BBox (world): size=(0.095, 0.033, 0.111), center=(-9.077, 29.343, 0.263)
* 几何统计: Mesh=1, Vertices=16, Faces=24
* 子Mesh材质: /World/agv_3/left_swivel/Left_Swivel/STR_Left_Swivel -> /World/agv_3/left_swivel/Left_Swivel/materials/Looks/Robot
* 材质摘要:
 * /World/agv_3/left_swivel/Left_Swivel/materials/Looks/Robot -> Inputs: 'metallic_texture_influence=1', 'reflection_roughness_texture_influence=1', Textures: 'Textures/STL_Robot_albedo.%3CUDIM%3E.png', 'Textures/STL_Robot_normal.%3CUDIM%3E.png', 'Textures/STL_Robot_orm.%3CUDIM%3E.png'


---


### '/World/agv_3/left_swivel/Left_Swivel/materials' (Xform)
* 引用: payload:./materials.usd
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(0.000, 0.000, 0.000)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/agv_3/right_swivel/Right_Swivel' (Xform)
* 引用: reference:HighResProps/Right_Swivel.usd
* BBox (world): size=(0.095, 0.033, 0.111), center=(-9.077, 29.157, 0.263)
* 几何统计: Mesh=1, Vertices=16, Faces=24
* 子Mesh材质: /World/agv_3/right_swivel/Right_Swivel/STR_Right_Swivel -> /World/agv_3/right_swivel/Right_Swivel/materials/Looks/Robot
* 材质摘要:
 * /World/agv_3/right_swivel/Right_Swivel/materials/Looks/Robot -> Inputs: 'metallic_texture_influence=1', 'reflection_roughness_texture_influence=1', Textures: 'Textures/STL_Robot_albedo.%3CUDIM%3E.png', 'Textures/STL_Robot_normal.%3CUDIM%3E.png', 'Textures/STL_Robot_orm.%3CUDIM%3E.png'


---


### '/World/agv_3/right_swivel/Right_Swivel/materials' (Xform)
* 引用: payload:./materials.usd
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(0.000, 0.000, 0.000)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/agv_3/left_caster/Inner_Left_Wheel' (Xform)
* 引用: reference:HighResProps/Inner_Left_Wheel.usd
* BBox (world): size=(0.135, 0.029, 0.135), center=(-9.077, 29.343, 0.230)
* 几何统计: Mesh=1, Vertices=162, Faces=320
* 子Mesh材质: /World/agv_3/left_caster/Inner_Left_Wheel/STR_Inner_Left_Wheel -> /World/agv_3/left_caster/Inner_Left_Wheel/materials/Looks/Robot
* 材质摘要:
 * /World/agv_3/left_caster/Inner_Left_Wheel/materials/Looks/Robot -> Inputs: 'metallic_texture_influence=1', 'reflection_roughness_texture_influence=1', Textures: 'Textures/STL_Robot_albedo.%3CUDIM%3E.png', 'Textures/STL_Robot_normal.%3CUDIM%3E.png', 'Textures/STL_Robot_orm.%3CUDIM%3E.png'


---


### '/World/agv_3/left_caster/Inner_Left_Wheel/materials' (Xform)
* 引用: payload:./materials.usd
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(0.000, 0.000, 0.000)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/agv_3/right_caster/Inner_Right_Wheel' (Xform)
* 引用: reference:HighResProps/Inner_Right_Wheel.usd
* BBox (world): size=(0.135, 0.029, 0.135), center=(-9.077, 29.157, 0.230)
* 几何统计: Mesh=1, Vertices=162, Faces=320
* 子Mesh材质: /World/agv_3/right_caster/Inner_Right_Wheel/STR_Inner_Right_Wheel -> /World/agv_3/right_caster/Inner_Right_Wheel/materials/Looks/Robot
* 材质摘要:
 * /World/agv_3/right_caster/Inner_Right_Wheel/materials/Looks/Robot -> Inputs: 'metallic_texture_influence=1', 'reflection_roughness_texture_influence=1', Textures: 'Textures/STL_Robot_albedo.%3CUDIM%3E.png', 'Textures/STL_Robot_normal.%3CUDIM%3E.png', 'Textures/STL_Robot_orm.%3CUDIM%3E.png'


---


### '/World/agv_3/right_caster/Inner_Right_Wheel/materials' (Xform)
* 引用: payload:./materials.usd
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(0.000, 0.000, 0.000)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/agv_4' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/5.0/Isaac/Robots/Idealworks/iwhub/iw_hub.usd
* BBox (world): size=(1.431, 0.659, 0.231), center=(-3.718, 29.251, 0.275)
* 几何统计: Mesh=8, Vertices=388563, Faces=382917
* 子Mesh材质: /World/agv_4/chassis/Body/Body/Mesh -> /World/agv_4/chassis/Body/Looks/Robot, /World/agv_4/left_wheel/Left_Wheel/Left_Wheel/Mesh_002 -> /World/agv_4/left_wheel/Left_Wheel/Looks/Robot, /World/agv_4/right_wheel/Right_Wheel/Right_Wheel/Mesh_005 -> /World/agv_4/right_wheel/Right_Wheel/Looks/Robot, /World/agv_4/lift/Lift/Lift/Mesh_012 -> /World/agv_4/lift/Lift/Looks/Robot, /World/agv_4/left_swivel/Left_Swivel/STR_Left_Swivel -> /World/agv_4/left_swivel/Left_Swivel/materials/Looks/Robot, /World/agv_4/right_swivel/Right_Swivel/STR_Right_Swivel -> /World/agv_4/right_swivel/Right_Swivel/materials/Looks/Robot, /World/agv_4/left_caster/Inner_Left_Wheel/STR_Inner_Left_Wheel -> /World/agv_4/left_caster/Inner_Left_Wheel/materials/Looks/Robot, /World/agv_4/right_caster/Inner_Right_Wheel/STR_Inner_Right_Wheel -> /World/agv_4/right_caster/Inner_Right_Wheel/materials/Looks/Robot
* 材质摘要:
 * /World/agv_4/chassis/Body/Looks/Robot -> Inputs: 'emissive_intensity=8000', 'metallic_texture_influence=0.9', 'reflection_roughness_texture_influence=1', Textures: 'Textures/STL_Robot_albedo.<UDIM>.png', 'Textures/STL_Robot_emissive.<UDIM>.png', 'Textures/STL_Robot_normal.<UDIM>.png', 'Textures/STL_Robot_orm.<UDIM>.png'
 * /World/agv_4/left_caster/Inner_Left_Wheel/materials/Looks/Robot -> Inputs: 'metallic_texture_influence=1', 'reflection_roughness_texture_influence=1', Textures: 'Textures/STL_Robot_albedo.%3CUDIM%3E.png', 'Textures/STL_Robot_normal.%3CUDIM%3E.png', 'Textures/STL_Robot_orm.%3CUDIM%3E.png'
 * /World/agv_4/left_swivel/Left_Swivel/materials/Looks/Robot -> Inputs: 'metallic_texture_influence=1', 'reflection_roughness_texture_influence=1', Textures: 'Textures/STL_Robot_albedo.%3CUDIM%3E.png', 'Textures/STL_Robot_normal.%3CUDIM%3E.png', 'Textures/STL_Robot_orm.%3CUDIM%3E.png'
 * /World/agv_4/left_wheel/Left_Wheel/Looks/Robot -> Inputs: 'metallic_texture_influence=1', 'reflection_roughness_texture_influence=1', Textures: 'Textures/STL_Robot_albedo.<UDIM>.png', 'Textures/STL_Robot_normal.<UDIM>.png', 'Textures/STL_Robot_orm.<UDIM>.png'
 * /World/agv_4/lift/Lift/Looks/Robot -> Inputs: 'metallic_texture_influence=0.901', 'reflection_roughness_texture_influence=1', Textures: 'Textures/STL_Robot_albedo.<UDIM>.png', 'Textures/STL_Robot_normal.<UDIM>.png', 'Textures/STL_Robot_orm.<UDIM>.png'
 * /World/agv_4/right_caster/Inner_Right_Wheel/materials/Looks/Robot -> Inputs: 'metallic_texture_influence=1', 'reflection_roughness_texture_influence=1', Textures: 'Textures/STL_Robot_albedo.%3CUDIM%3E.png', 'Textures/STL_Robot_normal.%3CUDIM%3E.png', 'Textures/STL_Robot_orm.%3CUDIM%3E.png'
 * /World/agv_4/right_swivel/Right_Swivel/materials/Looks/Robot -> Inputs: 'metallic_texture_influence=1', 'reflection_roughness_texture_influence=1', Textures: 'Textures/STL_Robot_albedo.%3CUDIM%3E.png', 'Textures/STL_Robot_normal.%3CUDIM%3E.png', 'Textures/STL_Robot_orm.%3CUDIM%3E.png'
 * /World/agv_4/right_wheel/Right_Wheel/Looks/Robot -> Inputs: 'metallic_texture_influence=1', 'reflection_roughness_texture_influence=1', Textures: 'Textures/STL_Robot_albedo.<UDIM>.png', 'Textures/STL_Robot_normal.<UDIM>.png', 'Textures/STL_Robot_orm.<UDIM>.png'


---


### '/World/agv_4/chassis/Body' (Xform)
* 引用: reference:HighResProps/Body_v2.usd
* BBox (world): size=(1.431, 0.652, 0.197), center=(-3.718, 29.250, 0.289)
* 几何统计: Mesh=1, Vertices=277878, Faces=273290
* 子Mesh材质: /World/agv_4/chassis/Body/Body/Mesh -> /World/agv_4/chassis/Body/Looks/Robot
* 材质摘要:
 * /World/agv_4/chassis/Body/Looks/Robot -> Inputs: 'emissive_intensity=8000', 'metallic_texture_influence=0.9', 'reflection_roughness_texture_influence=1', Textures: 'Textures/STL_Robot_albedo.<UDIM>.png', 'Textures/STL_Robot_emissive.<UDIM>.png', 'Textures/STL_Robot_normal.<UDIM>.png', 'Textures/STL_Robot_orm.<UDIM>.png'


---


### '/World/agv_4/left_wheel/Left_Wheel' (Xform)
* 引用: reference:HighResProps/Left_Wheel.usd
* BBox (world): size=(0.162, 0.057, 0.162), center=(-3.400, 29.540, 0.240)
* 几何统计: Mesh=1, Vertices=15925, Faces=15672
* 子Mesh材质: /World/agv_4/left_wheel/Left_Wheel/Left_Wheel/Mesh_002 -> /World/agv_4/left_wheel/Left_Wheel/Looks/Robot
* 材质摘要:
 * /World/agv_4/left_wheel/Left_Wheel/Looks/Robot -> Inputs: 'metallic_texture_influence=1', 'reflection_roughness_texture_influence=1', Textures: 'Textures/STL_Robot_albedo.<UDIM>.png', 'Textures/STL_Robot_normal.<UDIM>.png', 'Textures/STL_Robot_orm.<UDIM>.png'


---


### '/World/agv_4/right_wheel/Right_Wheel' (Xform)
* 引用: reference:HighResProps/Right_Wheel.usd
* BBox (world): size=(0.162, 0.057, 0.162), center=(-3.400, 28.960, 0.240)
* 几何统计: Mesh=1, Vertices=15925, Faces=15672
* 子Mesh材质: /World/agv_4/right_wheel/Right_Wheel/Right_Wheel/Mesh_005 -> /World/agv_4/right_wheel/Right_Wheel/Looks/Robot
* 材质摘要:
 * /World/agv_4/right_wheel/Right_Wheel/Looks/Robot -> Inputs: 'metallic_texture_influence=1', 'reflection_roughness_texture_influence=1', Textures: 'Textures/STL_Robot_albedo.<UDIM>.png', 'Textures/STL_Robot_normal.<UDIM>.png', 'Textures/STL_Robot_orm.<UDIM>.png'


---


### '/World/agv_4/lift/Lift' (Xform)
* 引用: reference:HighResProps/Lift_v2.usd
* BBox (world): size=(1.023, 0.659, 0.169), center=(-3.656, 29.251, 0.306)
* 几何统计: Mesh=1, Vertices=78479, Faces=77595
* 子Mesh材质: /World/agv_4/lift/Lift/Lift/Mesh_012 -> /World/agv_4/lift/Lift/Looks/Robot
* 材质摘要:
 * /World/agv_4/lift/Lift/Looks/Robot -> Inputs: 'metallic_texture_influence=0.901', 'reflection_roughness_texture_influence=1', Textures: 'Textures/STL_Robot_albedo.<UDIM>.png', 'Textures/STL_Robot_normal.<UDIM>.png', 'Textures/STL_Robot_orm.<UDIM>.png'


---


### '/World/agv_4/left_swivel/Left_Swivel' (Xform)
* 引用: reference:HighResProps/Left_Swivel.usd
* BBox (world): size=(0.095, 0.033, 0.111), center=(-4.077, 29.343, 0.263)
* 几何统计: Mesh=1, Vertices=16, Faces=24
* 子Mesh材质: /World/agv_4/left_swivel/Left_Swivel/STR_Left_Swivel -> /World/agv_4/left_swivel/Left_Swivel/materials/Looks/Robot
* 材质摘要:
 * /World/agv_4/left_swivel/Left_Swivel/materials/Looks/Robot -> Inputs: 'metallic_texture_influence=1', 'reflection_roughness_texture_influence=1', Textures: 'Textures/STL_Robot_albedo.%3CUDIM%3E.png', 'Textures/STL_Robot_normal.%3CUDIM%3E.png', 'Textures/STL_Robot_orm.%3CUDIM%3E.png'


---


### '/World/agv_4/left_swivel/Left_Swivel/materials' (Xform)
* 引用: payload:./materials.usd
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(0.000, 0.000, 0.000)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/agv_4/right_swivel/Right_Swivel' (Xform)
* 引用: reference:HighResProps/Right_Swivel.usd
* BBox (world): size=(0.095, 0.033, 0.111), center=(-4.077, 29.157, 0.263)
* 几何统计: Mesh=1, Vertices=16, Faces=24
* 子Mesh材质: /World/agv_4/right_swivel/Right_Swivel/STR_Right_Swivel -> /World/agv_4/right_swivel/Right_Swivel/materials/Looks/Robot
* 材质摘要:
 * /World/agv_4/right_swivel/Right_Swivel/materials/Looks/Robot -> Inputs: 'metallic_texture_influence=1', 'reflection_roughness_texture_influence=1', Textures: 'Textures/STL_Robot_albedo.%3CUDIM%3E.png', 'Textures/STL_Robot_normal.%3CUDIM%3E.png', 'Textures/STL_Robot_orm.%3CUDIM%3E.png'


---


### '/World/agv_4/right_swivel/Right_Swivel/materials' (Xform)
* 引用: payload:./materials.usd
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(0.000, 0.000, 0.000)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/agv_4/left_caster/Inner_Left_Wheel' (Xform)
* 引用: reference:HighResProps/Inner_Left_Wheel.usd
* BBox (world): size=(0.135, 0.029, 0.135), center=(-4.077, 29.343, 0.230)
* 几何统计: Mesh=1, Vertices=162, Faces=320
* 子Mesh材质: /World/agv_4/left_caster/Inner_Left_Wheel/STR_Inner_Left_Wheel -> /World/agv_4/left_caster/Inner_Left_Wheel/materials/Looks/Robot
* 材质摘要:
 * /World/agv_4/left_caster/Inner_Left_Wheel/materials/Looks/Robot -> Inputs: 'metallic_texture_influence=1', 'reflection_roughness_texture_influence=1', Textures: 'Textures/STL_Robot_albedo.%3CUDIM%3E.png', 'Textures/STL_Robot_normal.%3CUDIM%3E.png', 'Textures/STL_Robot_orm.%3CUDIM%3E.png'


---


### '/World/agv_4/left_caster/Inner_Left_Wheel/materials' (Xform)
* 引用: payload:./materials.usd
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(0.000, 0.000, 0.000)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/agv_4/right_caster/Inner_Right_Wheel' (Xform)
* 引用: reference:HighResProps/Inner_Right_Wheel.usd
* BBox (world): size=(0.135, 0.029, 0.135), center=(-4.077, 29.157, 0.230)
* 几何统计: Mesh=1, Vertices=162, Faces=320
* 子Mesh材质: /World/agv_4/right_caster/Inner_Right_Wheel/STR_Inner_Right_Wheel -> /World/agv_4/right_caster/Inner_Right_Wheel/materials/Looks/Robot
* 材质摘要:
 * /World/agv_4/right_caster/Inner_Right_Wheel/materials/Looks/Robot -> Inputs: 'metallic_texture_influence=1', 'reflection_roughness_texture_influence=1', Textures: 'Textures/STL_Robot_albedo.%3CUDIM%3E.png', 'Textures/STL_Robot_normal.%3CUDIM%3E.png', 'Textures/STL_Robot_orm.%3CUDIM%3E.png'


---


### '/World/agv_4/right_caster/Inner_Right_Wheel/materials' (Xform)
* 引用: payload:./materials.usd
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(0.000, 0.000, 0.000)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/agv_5' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/5.0/Isaac/Robots/Idealworks/iwhub/iw_hub.usd
* BBox (world): size=(1.431, 0.659, 0.231), center=(1.282, 29.251, 0.275)
* 几何统计: Mesh=8, Vertices=388563, Faces=382917
* 子Mesh材质: /World/agv_5/chassis/Body/Body/Mesh -> /World/agv_5/chassis/Body/Looks/Robot, /World/agv_5/left_wheel/Left_Wheel/Left_Wheel/Mesh_002 -> /World/agv_5/left_wheel/Left_Wheel/Looks/Robot, /World/agv_5/right_wheel/Right_Wheel/Right_Wheel/Mesh_005 -> /World/agv_5/right_wheel/Right_Wheel/Looks/Robot, /World/agv_5/lift/Lift/Lift/Mesh_012 -> /World/agv_5/lift/Lift/Looks/Robot, /World/agv_5/left_swivel/Left_Swivel/STR_Left_Swivel -> /World/agv_5/left_swivel/Left_Swivel/materials/Looks/Robot, /World/agv_5/right_swivel/Right_Swivel/STR_Right_Swivel -> /World/agv_5/right_swivel/Right_Swivel/materials/Looks/Robot, /World/agv_5/left_caster/Inner_Left_Wheel/STR_Inner_Left_Wheel -> /World/agv_5/left_caster/Inner_Left_Wheel/materials/Looks/Robot, /World/agv_5/right_caster/Inner_Right_Wheel/STR_Inner_Right_Wheel -> /World/agv_5/right_caster/Inner_Right_Wheel/materials/Looks/Robot
* 材质摘要:
 * /World/agv_5/chassis/Body/Looks/Robot -> Inputs: 'emissive_intensity=8000', 'metallic_texture_influence=0.9', 'reflection_roughness_texture_influence=1', Textures: 'Textures/STL_Robot_albedo.<UDIM>.png', 'Textures/STL_Robot_emissive.<UDIM>.png', 'Textures/STL_Robot_normal.<UDIM>.png', 'Textures/STL_Robot_orm.<UDIM>.png'
 * /World/agv_5/left_caster/Inner_Left_Wheel/materials/Looks/Robot -> Inputs: 'metallic_texture_influence=1', 'reflection_roughness_texture_influence=1', Textures: 'Textures/STL_Robot_albedo.%3CUDIM%3E.png', 'Textures/STL_Robot_normal.%3CUDIM%3E.png', 'Textures/STL_Robot_orm.%3CUDIM%3E.png'
 * /World/agv_5/left_swivel/Left_Swivel/materials/Looks/Robot -> Inputs: 'metallic_texture_influence=1', 'reflection_roughness_texture_influence=1', Textures: 'Textures/STL_Robot_albedo.%3CUDIM%3E.png', 'Textures/STL_Robot_normal.%3CUDIM%3E.png', 'Textures/STL_Robot_orm.%3CUDIM%3E.png'
 * /World/agv_5/left_wheel/Left_Wheel/Looks/Robot -> Inputs: 'metallic_texture_influence=1', 'reflection_roughness_texture_influence=1', Textures: 'Textures/STL_Robot_albedo.<UDIM>.png', 'Textures/STL_Robot_normal.<UDIM>.png', 'Textures/STL_Robot_orm.<UDIM>.png'
 * /World/agv_5/lift/Lift/Looks/Robot -> Inputs: 'metallic_texture_influence=0.901', 'reflection_roughness_texture_influence=1', Textures: 'Textures/STL_Robot_albedo.<UDIM>.png', 'Textures/STL_Robot_normal.<UDIM>.png', 'Textures/STL_Robot_orm.<UDIM>.png'
 * /World/agv_5/right_caster/Inner_Right_Wheel/materials/Looks/Robot -> Inputs: 'metallic_texture_influence=1', 'reflection_roughness_texture_influence=1', Textures: 'Textures/STL_Robot_albedo.%3CUDIM%3E.png', 'Textures/STL_Robot_normal.%3CUDIM%3E.png', 'Textures/STL_Robot_orm.%3CUDIM%3E.png'
 * /World/agv_5/right_swivel/Right_Swivel/materials/Looks/Robot -> Inputs: 'metallic_texture_influence=1', 'reflection_roughness_texture_influence=1', Textures: 'Textures/STL_Robot_albedo.%3CUDIM%3E.png', 'Textures/STL_Robot_normal.%3CUDIM%3E.png', 'Textures/STL_Robot_orm.%3CUDIM%3E.png'
 * /World/agv_5/right_wheel/Right_Wheel/Looks/Robot -> Inputs: 'metallic_texture_influence=1', 'reflection_roughness_texture_influence=1', Textures: 'Textures/STL_Robot_albedo.<UDIM>.png', 'Textures/STL_Robot_normal.<UDIM>.png', 'Textures/STL_Robot_orm.<UDIM>.png'


---


### '/World/agv_5/chassis/Body' (Xform)
* 引用: reference:HighResProps/Body_v2.usd
* BBox (world): size=(1.431, 0.652, 0.197), center=(1.282, 29.250, 0.289)
* 几何统计: Mesh=1, Vertices=277878, Faces=273290
* 子Mesh材质: /World/agv_5/chassis/Body/Body/Mesh -> /World/agv_5/chassis/Body/Looks/Robot
* 材质摘要:
 * /World/agv_5/chassis/Body/Looks/Robot -> Inputs: 'emissive_intensity=8000', 'metallic_texture_influence=0.9', 'reflection_roughness_texture_influence=1', Textures: 'Textures/STL_Robot_albedo.<UDIM>.png', 'Textures/STL_Robot_emissive.<UDIM>.png', 'Textures/STL_Robot_normal.<UDIM>.png', 'Textures/STL_Robot_orm.<UDIM>.png'


---


### '/World/agv_5/left_wheel/Left_Wheel' (Xform)
* 引用: reference:HighResProps/Left_Wheel.usd
* BBox (world): size=(0.162, 0.057, 0.162), center=(1.600, 29.540, 0.240)
* 几何统计: Mesh=1, Vertices=15925, Faces=15672
* 子Mesh材质: /World/agv_5/left_wheel/Left_Wheel/Left_Wheel/Mesh_002 -> /World/agv_5/left_wheel/Left_Wheel/Looks/Robot
* 材质摘要:
 * /World/agv_5/left_wheel/Left_Wheel/Looks/Robot -> Inputs: 'metallic_texture_influence=1', 'reflection_roughness_texture_influence=1', Textures: 'Textures/STL_Robot_albedo.<UDIM>.png', 'Textures/STL_Robot_normal.<UDIM>.png', 'Textures/STL_Robot_orm.<UDIM>.png'


---


### '/World/agv_5/right_wheel/Right_Wheel' (Xform)
* 引用: reference:HighResProps/Right_Wheel.usd
* BBox (world): size=(0.162, 0.057, 0.162), center=(1.600, 28.960, 0.240)
* 几何统计: Mesh=1, Vertices=15925, Faces=15672
* 子Mesh材质: /World/agv_5/right_wheel/Right_Wheel/Right_Wheel/Mesh_005 -> /World/agv_5/right_wheel/Right_Wheel/Looks/Robot
* 材质摘要:
 * /World/agv_5/right_wheel/Right_Wheel/Looks/Robot -> Inputs: 'metallic_texture_influence=1', 'reflection_roughness_texture_influence=1', Textures: 'Textures/STL_Robot_albedo.<UDIM>.png', 'Textures/STL_Robot_normal.<UDIM>.png', 'Textures/STL_Robot_orm.<UDIM>.png'


---


### '/World/agv_5/lift/Lift' (Xform)
* 引用: reference:HighResProps/Lift_v2.usd
* BBox (world): size=(1.023, 0.659, 0.169), center=(1.344, 29.251, 0.306)
* 几何统计: Mesh=1, Vertices=78479, Faces=77595
* 子Mesh材质: /World/agv_5/lift/Lift/Lift/Mesh_012 -> /World/agv_5/lift/Lift/Looks/Robot
* 材质摘要:
 * /World/agv_5/lift/Lift/Looks/Robot -> Inputs: 'metallic_texture_influence=0.901', 'reflection_roughness_texture_influence=1', Textures: 'Textures/STL_Robot_albedo.<UDIM>.png', 'Textures/STL_Robot_normal.<UDIM>.png', 'Textures/STL_Robot_orm.<UDIM>.png'


---


### '/World/agv_5/left_swivel/Left_Swivel' (Xform)
* 引用: reference:HighResProps/Left_Swivel.usd
* BBox (world): size=(0.095, 0.033, 0.111), center=(0.923, 29.343, 0.263)
* 几何统计: Mesh=1, Vertices=16, Faces=24
* 子Mesh材质: /World/agv_5/left_swivel/Left_Swivel/STR_Left_Swivel -> /World/agv_5/left_swivel/Left_Swivel/materials/Looks/Robot
* 材质摘要:
 * /World/agv_5/left_swivel/Left_Swivel/materials/Looks/Robot -> Inputs: 'metallic_texture_influence=1', 'reflection_roughness_texture_influence=1', Textures: 'Textures/STL_Robot_albedo.%3CUDIM%3E.png', 'Textures/STL_Robot_normal.%3CUDIM%3E.png', 'Textures/STL_Robot_orm.%3CUDIM%3E.png'


---


### '/World/agv_5/left_swivel/Left_Swivel/materials' (Xform)
* 引用: payload:./materials.usd
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(0.000, 0.000, 0.000)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/agv_5/right_swivel/Right_Swivel' (Xform)
* 引用: reference:HighResProps/Right_Swivel.usd
* BBox (world): size=(0.095, 0.033, 0.111), center=(0.923, 29.157, 0.263)
* 几何统计: Mesh=1, Vertices=16, Faces=24
* 子Mesh材质: /World/agv_5/right_swivel/Right_Swivel/STR_Right_Swivel -> /World/agv_5/right_swivel/Right_Swivel/materials/Looks/Robot
* 材质摘要:
 * /World/agv_5/right_swivel/Right_Swivel/materials/Looks/Robot -> Inputs: 'metallic_texture_influence=1', 'reflection_roughness_texture_influence=1', Textures: 'Textures/STL_Robot_albedo.%3CUDIM%3E.png', 'Textures/STL_Robot_normal.%3CUDIM%3E.png', 'Textures/STL_Robot_orm.%3CUDIM%3E.png'


---


### '/World/agv_5/right_swivel/Right_Swivel/materials' (Xform)
* 引用: payload:./materials.usd
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(0.000, 0.000, 0.000)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/agv_5/left_caster/Inner_Left_Wheel' (Xform)
* 引用: reference:HighResProps/Inner_Left_Wheel.usd
* BBox (world): size=(0.135, 0.029, 0.135), center=(0.923, 29.343, 0.230)
* 几何统计: Mesh=1, Vertices=162, Faces=320
* 子Mesh材质: /World/agv_5/left_caster/Inner_Left_Wheel/STR_Inner_Left_Wheel -> /World/agv_5/left_caster/Inner_Left_Wheel/materials/Looks/Robot
* 材质摘要:
 * /World/agv_5/left_caster/Inner_Left_Wheel/materials/Looks/Robot -> Inputs: 'metallic_texture_influence=1', 'reflection_roughness_texture_influence=1', Textures: 'Textures/STL_Robot_albedo.%3CUDIM%3E.png', 'Textures/STL_Robot_normal.%3CUDIM%3E.png', 'Textures/STL_Robot_orm.%3CUDIM%3E.png'


---


### '/World/agv_5/left_caster/Inner_Left_Wheel/materials' (Xform)
* 引用: payload:./materials.usd
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(0.000, 0.000, 0.000)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/agv_5/right_caster/Inner_Right_Wheel' (Xform)
* 引用: reference:HighResProps/Inner_Right_Wheel.usd
* BBox (world): size=(0.135, 0.029, 0.135), center=(0.923, 29.157, 0.230)
* 几何统计: Mesh=1, Vertices=162, Faces=320
* 子Mesh材质: /World/agv_5/right_caster/Inner_Right_Wheel/STR_Inner_Right_Wheel -> /World/agv_5/right_caster/Inner_Right_Wheel/materials/Looks/Robot
* 材质摘要:
 * /World/agv_5/right_caster/Inner_Right_Wheel/materials/Looks/Robot -> Inputs: 'metallic_texture_influence=1', 'reflection_roughness_texture_influence=1', Textures: 'Textures/STL_Robot_albedo.%3CUDIM%3E.png', 'Textures/STL_Robot_normal.%3CUDIM%3E.png', 'Textures/STL_Robot_orm.%3CUDIM%3E.png'


---


### '/World/agv_5/right_caster/Inner_Right_Wheel/materials' (Xform)
* 引用: payload:./materials.usd
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(0.000, 0.000, 0.000)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/agv_6' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/5.0/Isaac/Robots/Idealworks/iwhub/iw_hub.usd
* BBox (world): size=(1.431, 0.659, 0.231), center=(6.282, 29.251, 0.275)
* 几何统计: Mesh=8, Vertices=388563, Faces=382917
* 子Mesh材质: /World/agv_6/chassis/Body/Body/Mesh -> /World/agv_6/chassis/Body/Looks/Robot, /World/agv_6/left_wheel/Left_Wheel/Left_Wheel/Mesh_002 -> /World/agv_6/left_wheel/Left_Wheel/Looks/Robot, /World/agv_6/right_wheel/Right_Wheel/Right_Wheel/Mesh_005 -> /World/agv_6/right_wheel/Right_Wheel/Looks/Robot, /World/agv_6/lift/Lift/Lift/Mesh_012 -> /World/agv_6/lift/Lift/Looks/Robot, /World/agv_6/left_swivel/Left_Swivel/STR_Left_Swivel -> /World/agv_6/left_swivel/Left_Swivel/materials/Looks/Robot, /World/agv_6/right_swivel/Right_Swivel/STR_Right_Swivel -> /World/agv_6/right_swivel/Right_Swivel/materials/Looks/Robot, /World/agv_6/left_caster/Inner_Left_Wheel/STR_Inner_Left_Wheel -> /World/agv_6/left_caster/Inner_Left_Wheel/materials/Looks/Robot, /World/agv_6/right_caster/Inner_Right_Wheel/STR_Inner_Right_Wheel -> /World/agv_6/right_caster/Inner_Right_Wheel/materials/Looks/Robot
* 材质摘要:
 * /World/agv_6/chassis/Body/Looks/Robot -> Inputs: 'emissive_intensity=8000', 'metallic_texture_influence=0.9', 'reflection_roughness_texture_influence=1', Textures: 'Textures/STL_Robot_albedo.<UDIM>.png', 'Textures/STL_Robot_emissive.<UDIM>.png', 'Textures/STL_Robot_normal.<UDIM>.png', 'Textures/STL_Robot_orm.<UDIM>.png'
 * /World/agv_6/left_caster/Inner_Left_Wheel/materials/Looks/Robot -> Inputs: 'metallic_texture_influence=1', 'reflection_roughness_texture_influence=1', Textures: 'Textures/STL_Robot_albedo.%3CUDIM%3E.png', 'Textures/STL_Robot_normal.%3CUDIM%3E.png', 'Textures/STL_Robot_orm.%3CUDIM%3E.png'
 * /World/agv_6/left_swivel/Left_Swivel/materials/Looks/Robot -> Inputs: 'metallic_texture_influence=1', 'reflection_roughness_texture_influence=1', Textures: 'Textures/STL_Robot_albedo.%3CUDIM%3E.png', 'Textures/STL_Robot_normal.%3CUDIM%3E.png', 'Textures/STL_Robot_orm.%3CUDIM%3E.png'
 * /World/agv_6/left_wheel/Left_Wheel/Looks/Robot -> Inputs: 'metallic_texture_influence=1', 'reflection_roughness_texture_influence=1', Textures: 'Textures/STL_Robot_albedo.<UDIM>.png', 'Textures/STL_Robot_normal.<UDIM>.png', 'Textures/STL_Robot_orm.<UDIM>.png'
 * /World/agv_6/lift/Lift/Looks/Robot -> Inputs: 'metallic_texture_influence=0.901', 'reflection_roughness_texture_influence=1', Textures: 'Textures/STL_Robot_albedo.<UDIM>.png', 'Textures/STL_Robot_normal.<UDIM>.png', 'Textures/STL_Robot_orm.<UDIM>.png'
 * /World/agv_6/right_caster/Inner_Right_Wheel/materials/Looks/Robot -> Inputs: 'metallic_texture_influence=1', 'reflection_roughness_texture_influence=1', Textures: 'Textures/STL_Robot_albedo.%3CUDIM%3E.png', 'Textures/STL_Robot_normal.%3CUDIM%3E.png', 'Textures/STL_Robot_orm.%3CUDIM%3E.png'
 * /World/agv_6/right_swivel/Right_Swivel/materials/Looks/Robot -> Inputs: 'metallic_texture_influence=1', 'reflection_roughness_texture_influence=1', Textures: 'Textures/STL_Robot_albedo.%3CUDIM%3E.png', 'Textures/STL_Robot_normal.%3CUDIM%3E.png', 'Textures/STL_Robot_orm.%3CUDIM%3E.png'
 * /World/agv_6/right_wheel/Right_Wheel/Looks/Robot -> Inputs: 'metallic_texture_influence=1', 'reflection_roughness_texture_influence=1', Textures: 'Textures/STL_Robot_albedo.<UDIM>.png', 'Textures/STL_Robot_normal.<UDIM>.png', 'Textures/STL_Robot_orm.<UDIM>.png'


---


### '/World/agv_6/chassis/Body' (Xform)
* 引用: reference:HighResProps/Body_v2.usd
* BBox (world): size=(1.431, 0.652, 0.197), center=(6.282, 29.250, 0.289)
* 几何统计: Mesh=1, Vertices=277878, Faces=273290
* 子Mesh材质: /World/agv_6/chassis/Body/Body/Mesh -> /World/agv_6/chassis/Body/Looks/Robot
* 材质摘要:
 * /World/agv_6/chassis/Body/Looks/Robot -> Inputs: 'emissive_intensity=8000', 'metallic_texture_influence=0.9', 'reflection_roughness_texture_influence=1', Textures: 'Textures/STL_Robot_albedo.<UDIM>.png', 'Textures/STL_Robot_emissive.<UDIM>.png', 'Textures/STL_Robot_normal.<UDIM>.png', 'Textures/STL_Robot_orm.<UDIM>.png'


---


### '/World/agv_6/left_wheel/Left_Wheel' (Xform)
* 引用: reference:HighResProps/Left_Wheel.usd
* BBox (world): size=(0.162, 0.057, 0.162), center=(6.600, 29.540, 0.240)
* 几何统计: Mesh=1, Vertices=15925, Faces=15672
* 子Mesh材质: /World/agv_6/left_wheel/Left_Wheel/Left_Wheel/Mesh_002 -> /World/agv_6/left_wheel/Left_Wheel/Looks/Robot
* 材质摘要:
 * /World/agv_6/left_wheel/Left_Wheel/Looks/Robot -> Inputs: 'metallic_texture_influence=1', 'reflection_roughness_texture_influence=1', Textures: 'Textures/STL_Robot_albedo.<UDIM>.png', 'Textures/STL_Robot_normal.<UDIM>.png', 'Textures/STL_Robot_orm.<UDIM>.png'


---


### '/World/agv_6/right_wheel/Right_Wheel' (Xform)
* 引用: reference:HighResProps/Right_Wheel.usd
* BBox (world): size=(0.162, 0.057, 0.162), center=(6.600, 28.960, 0.240)
* 几何统计: Mesh=1, Vertices=15925, Faces=15672
* 子Mesh材质: /World/agv_6/right_wheel/Right_Wheel/Right_Wheel/Mesh_005 -> /World/agv_6/right_wheel/Right_Wheel/Looks/Robot
* 材质摘要:
 * /World/agv_6/right_wheel/Right_Wheel/Looks/Robot -> Inputs: 'metallic_texture_influence=1', 'reflection_roughness_texture_influence=1', Textures: 'Textures/STL_Robot_albedo.<UDIM>.png', 'Textures/STL_Robot_normal.<UDIM>.png', 'Textures/STL_Robot_orm.<UDIM>.png'


---


### '/World/agv_6/lift/Lift' (Xform)
* 引用: reference:HighResProps/Lift_v2.usd
* BBox (world): size=(1.023, 0.659, 0.169), center=(6.344, 29.251, 0.306)
* 几何统计: Mesh=1, Vertices=78479, Faces=77595
* 子Mesh材质: /World/agv_6/lift/Lift/Lift/Mesh_012 -> /World/agv_6/lift/Lift/Looks/Robot
* 材质摘要:
 * /World/agv_6/lift/Lift/Looks/Robot -> Inputs: 'metallic_texture_influence=0.901', 'reflection_roughness_texture_influence=1', Textures: 'Textures/STL_Robot_albedo.<UDIM>.png', 'Textures/STL_Robot_normal.<UDIM>.png', 'Textures/STL_Robot_orm.<UDIM>.png'


---


### '/World/agv_6/left_swivel/Left_Swivel' (Xform)
* 引用: reference:HighResProps/Left_Swivel.usd
* BBox (world): size=(0.095, 0.033, 0.111), center=(5.923, 29.343, 0.263)
* 几何统计: Mesh=1, Vertices=16, Faces=24
* 子Mesh材质: /World/agv_6/left_swivel/Left_Swivel/STR_Left_Swivel -> /World/agv_6/left_swivel/Left_Swivel/materials/Looks/Robot
* 材质摘要:
 * /World/agv_6/left_swivel/Left_Swivel/materials/Looks/Robot -> Inputs: 'metallic_texture_influence=1', 'reflection_roughness_texture_influence=1', Textures: 'Textures/STL_Robot_albedo.%3CUDIM%3E.png', 'Textures/STL_Robot_normal.%3CUDIM%3E.png', 'Textures/STL_Robot_orm.%3CUDIM%3E.png'


---


### '/World/agv_6/left_swivel/Left_Swivel/materials' (Xform)
* 引用: payload:./materials.usd
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(0.000, 0.000, 0.000)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/agv_6/right_swivel/Right_Swivel' (Xform)
* 引用: reference:HighResProps/Right_Swivel.usd
* BBox (world): size=(0.095, 0.033, 0.111), center=(5.923, 29.157, 0.263)
* 几何统计: Mesh=1, Vertices=16, Faces=24
* 子Mesh材质: /World/agv_6/right_swivel/Right_Swivel/STR_Right_Swivel -> /World/agv_6/right_swivel/Right_Swivel/materials/Looks/Robot
* 材质摘要:
 * /World/agv_6/right_swivel/Right_Swivel/materials/Looks/Robot -> Inputs: 'metallic_texture_influence=1', 'reflection_roughness_texture_influence=1', Textures: 'Textures/STL_Robot_albedo.%3CUDIM%3E.png', 'Textures/STL_Robot_normal.%3CUDIM%3E.png', 'Textures/STL_Robot_orm.%3CUDIM%3E.png'


---


### '/World/agv_6/right_swivel/Right_Swivel/materials' (Xform)
* 引用: payload:./materials.usd
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(0.000, 0.000, 0.000)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/agv_6/left_caster/Inner_Left_Wheel' (Xform)
* 引用: reference:HighResProps/Inner_Left_Wheel.usd
* BBox (world): size=(0.135, 0.029, 0.135), center=(5.923, 29.343, 0.230)
* 几何统计: Mesh=1, Vertices=162, Faces=320
* 子Mesh材质: /World/agv_6/left_caster/Inner_Left_Wheel/STR_Inner_Left_Wheel -> /World/agv_6/left_caster/Inner_Left_Wheel/materials/Looks/Robot
* 材质摘要:
 * /World/agv_6/left_caster/Inner_Left_Wheel/materials/Looks/Robot -> Inputs: 'metallic_texture_influence=1', 'reflection_roughness_texture_influence=1', Textures: 'Textures/STL_Robot_albedo.%3CUDIM%3E.png', 'Textures/STL_Robot_normal.%3CUDIM%3E.png', 'Textures/STL_Robot_orm.%3CUDIM%3E.png'


---


### '/World/agv_6/left_caster/Inner_Left_Wheel/materials' (Xform)
* 引用: payload:./materials.usd
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(0.000, 0.000, 0.000)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/agv_6/right_caster/Inner_Right_Wheel' (Xform)
* 引用: reference:HighResProps/Inner_Right_Wheel.usd
* BBox (world): size=(0.135, 0.029, 0.135), center=(5.923, 29.157, 0.230)
* 几何统计: Mesh=1, Vertices=162, Faces=320
* 子Mesh材质: /World/agv_6/right_caster/Inner_Right_Wheel/STR_Inner_Right_Wheel -> /World/agv_6/right_caster/Inner_Right_Wheel/materials/Looks/Robot
* 材质摘要:
 * /World/agv_6/right_caster/Inner_Right_Wheel/materials/Looks/Robot -> Inputs: 'metallic_texture_influence=1', 'reflection_roughness_texture_influence=1', Textures: 'Textures/STL_Robot_albedo.%3CUDIM%3E.png', 'Textures/STL_Robot_normal.%3CUDIM%3E.png', 'Textures/STL_Robot_orm.%3CUDIM%3E.png'


---


### '/World/agv_6/right_caster/Inner_Right_Wheel/materials' (Xform)
* 引用: payload:./materials.usd
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(0.000, 0.000, 0.000)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/agv_7' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/5.0/Isaac/Robots/Idealworks/iwhub/iw_hub.usd
* BBox (world): size=(1.431, 0.659, 0.231), center=(11.282, 29.251, 0.275)
* 几何统计: Mesh=8, Vertices=388563, Faces=382917
* 子Mesh材质: /World/agv_7/chassis/Body/Body/Mesh -> /World/agv_7/chassis/Body/Looks/Robot, /World/agv_7/left_wheel/Left_Wheel/Left_Wheel/Mesh_002 -> /World/agv_7/left_wheel/Left_Wheel/Looks/Robot, /World/agv_7/right_wheel/Right_Wheel/Right_Wheel/Mesh_005 -> /World/agv_7/right_wheel/Right_Wheel/Looks/Robot, /World/agv_7/lift/Lift/Lift/Mesh_012 -> /World/agv_7/lift/Lift/Looks/Robot, /World/agv_7/left_swivel/Left_Swivel/STR_Left_Swivel -> /World/agv_7/left_swivel/Left_Swivel/materials/Looks/Robot, /World/agv_7/right_swivel/Right_Swivel/STR_Right_Swivel -> /World/agv_7/right_swivel/Right_Swivel/materials/Looks/Robot, /World/agv_7/left_caster/Inner_Left_Wheel/STR_Inner_Left_Wheel -> /World/agv_7/left_caster/Inner_Left_Wheel/materials/Looks/Robot, /World/agv_7/right_caster/Inner_Right_Wheel/STR_Inner_Right_Wheel -> /World/agv_7/right_caster/Inner_Right_Wheel/materials/Looks/Robot
* 材质摘要:
 * /World/agv_7/chassis/Body/Looks/Robot -> Inputs: 'emissive_intensity=8000', 'metallic_texture_influence=0.9', 'reflection_roughness_texture_influence=1', Textures: 'Textures/STL_Robot_albedo.<UDIM>.png', 'Textures/STL_Robot_emissive.<UDIM>.png', 'Textures/STL_Robot_normal.<UDIM>.png', 'Textures/STL_Robot_orm.<UDIM>.png'
 * /World/agv_7/left_caster/Inner_Left_Wheel/materials/Looks/Robot -> Inputs: 'metallic_texture_influence=1', 'reflection_roughness_texture_influence=1', Textures: 'Textures/STL_Robot_albedo.%3CUDIM%3E.png', 'Textures/STL_Robot_normal.%3CUDIM%3E.png', 'Textures/STL_Robot_orm.%3CUDIM%3E.png'
 * /World/agv_7/left_swivel/Left_Swivel/materials/Looks/Robot -> Inputs: 'metallic_texture_influence=1', 'reflection_roughness_texture_influence=1', Textures: 'Textures/STL_Robot_albedo.%3CUDIM%3E.png', 'Textures/STL_Robot_normal.%3CUDIM%3E.png', 'Textures/STL_Robot_orm.%3CUDIM%3E.png'
 * /World/agv_7/left_wheel/Left_Wheel/Looks/Robot -> Inputs: 'metallic_texture_influence=1', 'reflection_roughness_texture_influence=1', Textures: 'Textures/STL_Robot_albedo.<UDIM>.png', 'Textures/STL_Robot_normal.<UDIM>.png', 'Textures/STL_Robot_orm.<UDIM>.png'
 * /World/agv_7/lift/Lift/Looks/Robot -> Inputs: 'metallic_texture_influence=0.901', 'reflection_roughness_texture_influence=1', Textures: 'Textures/STL_Robot_albedo.<UDIM>.png', 'Textures/STL_Robot_normal.<UDIM>.png', 'Textures/STL_Robot_orm.<UDIM>.png'
 * /World/agv_7/right_caster/Inner_Right_Wheel/materials/Looks/Robot -> Inputs: 'metallic_texture_influence=1', 'reflection_roughness_texture_influence=1', Textures: 'Textures/STL_Robot_albedo.%3CUDIM%3E.png', 'Textures/STL_Robot_normal.%3CUDIM%3E.png', 'Textures/STL_Robot_orm.%3CUDIM%3E.png'
 * /World/agv_7/right_swivel/Right_Swivel/materials/Looks/Robot -> Inputs: 'metallic_texture_influence=1', 'reflection_roughness_texture_influence=1', Textures: 'Textures/STL_Robot_albedo.%3CUDIM%3E.png', 'Textures/STL_Robot_normal.%3CUDIM%3E.png', 'Textures/STL_Robot_orm.%3CUDIM%3E.png'
 * /World/agv_7/right_wheel/Right_Wheel/Looks/Robot -> Inputs: 'metallic_texture_influence=1', 'reflection_roughness_texture_influence=1', Textures: 'Textures/STL_Robot_albedo.<UDIM>.png', 'Textures/STL_Robot_normal.<UDIM>.png', 'Textures/STL_Robot_orm.<UDIM>.png'


---


### '/World/agv_7/chassis/Body' (Xform)
* 引用: reference:HighResProps/Body_v2.usd
* BBox (world): size=(1.431, 0.652, 0.197), center=(11.282, 29.250, 0.289)
* 几何统计: Mesh=1, Vertices=277878, Faces=273290
* 子Mesh材质: /World/agv_7/chassis/Body/Body/Mesh -> /World/agv_7/chassis/Body/Looks/Robot
* 材质摘要:
 * /World/agv_7/chassis/Body/Looks/Robot -> Inputs: 'emissive_intensity=8000', 'metallic_texture_influence=0.9', 'reflection_roughness_texture_influence=1', Textures: 'Textures/STL_Robot_albedo.<UDIM>.png', 'Textures/STL_Robot_emissive.<UDIM>.png', 'Textures/STL_Robot_normal.<UDIM>.png', 'Textures/STL_Robot_orm.<UDIM>.png'


---


### '/World/agv_7/left_wheel/Left_Wheel' (Xform)
* 引用: reference:HighResProps/Left_Wheel.usd
* BBox (world): size=(0.162, 0.057, 0.162), center=(11.600, 29.540, 0.240)
* 几何统计: Mesh=1, Vertices=15925, Faces=15672
* 子Mesh材质: /World/agv_7/left_wheel/Left_Wheel/Left_Wheel/Mesh_002 -> /World/agv_7/left_wheel/Left_Wheel/Looks/Robot
* 材质摘要:
 * /World/agv_7/left_wheel/Left_Wheel/Looks/Robot -> Inputs: 'metallic_texture_influence=1', 'reflection_roughness_texture_influence=1', Textures: 'Textures/STL_Robot_albedo.<UDIM>.png', 'Textures/STL_Robot_normal.<UDIM>.png', 'Textures/STL_Robot_orm.<UDIM>.png'


---


### '/World/agv_7/right_wheel/Right_Wheel' (Xform)
* 引用: reference:HighResProps/Right_Wheel.usd
* BBox (world): size=(0.162, 0.057, 0.162), center=(11.600, 28.960, 0.240)
* 几何统计: Mesh=1, Vertices=15925, Faces=15672
* 子Mesh材质: /World/agv_7/right_wheel/Right_Wheel/Right_Wheel/Mesh_005 -> /World/agv_7/right_wheel/Right_Wheel/Looks/Robot
* 材质摘要:
 * /World/agv_7/right_wheel/Right_Wheel/Looks/Robot -> Inputs: 'metallic_texture_influence=1', 'reflection_roughness_texture_influence=1', Textures: 'Textures/STL_Robot_albedo.<UDIM>.png', 'Textures/STL_Robot_normal.<UDIM>.png', 'Textures/STL_Robot_orm.<UDIM>.png'


---


### '/World/agv_7/lift/Lift' (Xform)
* 引用: reference:HighResProps/Lift_v2.usd
* BBox (world): size=(1.023, 0.659, 0.169), center=(11.344, 29.251, 0.306)
* 几何统计: Mesh=1, Vertices=78479, Faces=77595
* 子Mesh材质: /World/agv_7/lift/Lift/Lift/Mesh_012 -> /World/agv_7/lift/Lift/Looks/Robot
* 材质摘要:
 * /World/agv_7/lift/Lift/Looks/Robot -> Inputs: 'metallic_texture_influence=0.901', 'reflection_roughness_texture_influence=1', Textures: 'Textures/STL_Robot_albedo.<UDIM>.png', 'Textures/STL_Robot_normal.<UDIM>.png', 'Textures/STL_Robot_orm.<UDIM>.png'


---


### '/World/agv_7/left_swivel/Left_Swivel' (Xform)
* 引用: reference:HighResProps/Left_Swivel.usd
* BBox (world): size=(0.095, 0.033, 0.111), center=(10.923, 29.343, 0.263)
* 几何统计: Mesh=1, Vertices=16, Faces=24
* 子Mesh材质: /World/agv_7/left_swivel/Left_Swivel/STR_Left_Swivel -> /World/agv_7/left_swivel/Left_Swivel/materials/Looks/Robot
* 材质摘要:
 * /World/agv_7/left_swivel/Left_Swivel/materials/Looks/Robot -> Inputs: 'metallic_texture_influence=1', 'reflection_roughness_texture_influence=1', Textures: 'Textures/STL_Robot_albedo.%3CUDIM%3E.png', 'Textures/STL_Robot_normal.%3CUDIM%3E.png', 'Textures/STL_Robot_orm.%3CUDIM%3E.png'


---


### '/World/agv_7/left_swivel/Left_Swivel/materials' (Xform)
* 引用: payload:./materials.usd
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(0.000, 0.000, 0.000)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/agv_7/right_swivel/Right_Swivel' (Xform)
* 引用: reference:HighResProps/Right_Swivel.usd
* BBox (world): size=(0.095, 0.033, 0.111), center=(10.923, 29.157, 0.263)
* 几何统计: Mesh=1, Vertices=16, Faces=24
* 子Mesh材质: /World/agv_7/right_swivel/Right_Swivel/STR_Right_Swivel -> /World/agv_7/right_swivel/Right_Swivel/materials/Looks/Robot
* 材质摘要:
 * /World/agv_7/right_swivel/Right_Swivel/materials/Looks/Robot -> Inputs: 'metallic_texture_influence=1', 'reflection_roughness_texture_influence=1', Textures: 'Textures/STL_Robot_albedo.%3CUDIM%3E.png', 'Textures/STL_Robot_normal.%3CUDIM%3E.png', 'Textures/STL_Robot_orm.%3CUDIM%3E.png'


---


### '/World/agv_7/right_swivel/Right_Swivel/materials' (Xform)
* 引用: payload:./materials.usd
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(0.000, 0.000, 0.000)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/agv_7/left_caster/Inner_Left_Wheel' (Xform)
* 引用: reference:HighResProps/Inner_Left_Wheel.usd
* BBox (world): size=(0.135, 0.029, 0.135), center=(10.923, 29.343, 0.230)
* 几何统计: Mesh=1, Vertices=162, Faces=320
* 子Mesh材质: /World/agv_7/left_caster/Inner_Left_Wheel/STR_Inner_Left_Wheel -> /World/agv_7/left_caster/Inner_Left_Wheel/materials/Looks/Robot
* 材质摘要:
 * /World/agv_7/left_caster/Inner_Left_Wheel/materials/Looks/Robot -> Inputs: 'metallic_texture_influence=1', 'reflection_roughness_texture_influence=1', Textures: 'Textures/STL_Robot_albedo.%3CUDIM%3E.png', 'Textures/STL_Robot_normal.%3CUDIM%3E.png', 'Textures/STL_Robot_orm.%3CUDIM%3E.png'


---


### '/World/agv_7/left_caster/Inner_Left_Wheel/materials' (Xform)
* 引用: payload:./materials.usd
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(0.000, 0.000, 0.000)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/agv_7/right_caster/Inner_Right_Wheel' (Xform)
* 引用: reference:HighResProps/Inner_Right_Wheel.usd
* BBox (world): size=(0.135, 0.029, 0.135), center=(10.923, 29.157, 0.230)
* 几何统计: Mesh=1, Vertices=162, Faces=320
* 子Mesh材质: /World/agv_7/right_caster/Inner_Right_Wheel/STR_Inner_Right_Wheel -> /World/agv_7/right_caster/Inner_Right_Wheel/materials/Looks/Robot
* 材质摘要:
 * /World/agv_7/right_caster/Inner_Right_Wheel/materials/Looks/Robot -> Inputs: 'metallic_texture_influence=1', 'reflection_roughness_texture_influence=1', Textures: 'Textures/STL_Robot_albedo.%3CUDIM%3E.png', 'Textures/STL_Robot_normal.%3CUDIM%3E.png', 'Textures/STL_Robot_orm.%3CUDIM%3E.png'


---


### '/World/agv_7/right_caster/Inner_Right_Wheel/materials' (Xform)
* 引用: payload:./materials.usd
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(0.000, 0.000, 0.000)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/agv_8' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/5.0/Isaac/Robots/Idealworks/iwhub/iw_hub.usd
* BBox (world): size=(1.431, 0.659, 0.231), center=(16.282, 29.251, 0.275)
* 几何统计: Mesh=8, Vertices=388563, Faces=382917
* 子Mesh材质: /World/agv_8/chassis/Body/Body/Mesh -> /World/agv_8/chassis/Body/Looks/Robot, /World/agv_8/left_wheel/Left_Wheel/Left_Wheel/Mesh_002 -> /World/agv_8/left_wheel/Left_Wheel/Looks/Robot, /World/agv_8/right_wheel/Right_Wheel/Right_Wheel/Mesh_005 -> /World/agv_8/right_wheel/Right_Wheel/Looks/Robot, /World/agv_8/lift/Lift/Lift/Mesh_012 -> /World/agv_8/lift/Lift/Looks/Robot, /World/agv_8/left_swivel/Left_Swivel/STR_Left_Swivel -> /World/agv_8/left_swivel/Left_Swivel/materials/Looks/Robot, /World/agv_8/right_swivel/Right_Swivel/STR_Right_Swivel -> /World/agv_8/right_swivel/Right_Swivel/materials/Looks/Robot, /World/agv_8/left_caster/Inner_Left_Wheel/STR_Inner_Left_Wheel -> /World/agv_8/left_caster/Inner_Left_Wheel/materials/Looks/Robot, /World/agv_8/right_caster/Inner_Right_Wheel/STR_Inner_Right_Wheel -> /World/agv_8/right_caster/Inner_Right_Wheel/materials/Looks/Robot
* 材质摘要:
 * /World/agv_8/chassis/Body/Looks/Robot -> Inputs: 'emissive_intensity=8000', 'metallic_texture_influence=0.9', 'reflection_roughness_texture_influence=1', Textures: 'Textures/STL_Robot_albedo.<UDIM>.png', 'Textures/STL_Robot_emissive.<UDIM>.png', 'Textures/STL_Robot_normal.<UDIM>.png', 'Textures/STL_Robot_orm.<UDIM>.png'
 * /World/agv_8/left_caster/Inner_Left_Wheel/materials/Looks/Robot -> Inputs: 'metallic_texture_influence=1', 'reflection_roughness_texture_influence=1', Textures: 'Textures/STL_Robot_albedo.%3CUDIM%3E.png', 'Textures/STL_Robot_normal.%3CUDIM%3E.png', 'Textures/STL_Robot_orm.%3CUDIM%3E.png'
 * /World/agv_8/left_swivel/Left_Swivel/materials/Looks/Robot -> Inputs: 'metallic_texture_influence=1', 'reflection_roughness_texture_influence=1', Textures: 'Textures/STL_Robot_albedo.%3CUDIM%3E.png', 'Textures/STL_Robot_normal.%3CUDIM%3E.png', 'Textures/STL_Robot_orm.%3CUDIM%3E.png'
 * /World/agv_8/left_wheel/Left_Wheel/Looks/Robot -> Inputs: 'metallic_texture_influence=1', 'reflection_roughness_texture_influence=1', Textures: 'Textures/STL_Robot_albedo.<UDIM>.png', 'Textures/STL_Robot_normal.<UDIM>.png', 'Textures/STL_Robot_orm.<UDIM>.png'
 * /World/agv_8/lift/Lift/Looks/Robot -> Inputs: 'metallic_texture_influence=0.901', 'reflection_roughness_texture_influence=1', Textures: 'Textures/STL_Robot_albedo.<UDIM>.png', 'Textures/STL_Robot_normal.<UDIM>.png', 'Textures/STL_Robot_orm.<UDIM>.png'
 * /World/agv_8/right_caster/Inner_Right_Wheel/materials/Looks/Robot -> Inputs: 'metallic_texture_influence=1', 'reflection_roughness_texture_influence=1', Textures: 'Textures/STL_Robot_albedo.%3CUDIM%3E.png', 'Textures/STL_Robot_normal.%3CUDIM%3E.png', 'Textures/STL_Robot_orm.%3CUDIM%3E.png'
 * /World/agv_8/right_swivel/Right_Swivel/materials/Looks/Robot -> Inputs: 'metallic_texture_influence=1', 'reflection_roughness_texture_influence=1', Textures: 'Textures/STL_Robot_albedo.%3CUDIM%3E.png', 'Textures/STL_Robot_normal.%3CUDIM%3E.png', 'Textures/STL_Robot_orm.%3CUDIM%3E.png'
 * /World/agv_8/right_wheel/Right_Wheel/Looks/Robot -> Inputs: 'metallic_texture_influence=1', 'reflection_roughness_texture_influence=1', Textures: 'Textures/STL_Robot_albedo.<UDIM>.png', 'Textures/STL_Robot_normal.<UDIM>.png', 'Textures/STL_Robot_orm.<UDIM>.png'


---


### '/World/agv_8/chassis/Body' (Xform)
* 引用: reference:HighResProps/Body_v2.usd
* BBox (world): size=(1.431, 0.652, 0.197), center=(16.282, 29.250, 0.289)
* 几何统计: Mesh=1, Vertices=277878, Faces=273290
* 子Mesh材质: /World/agv_8/chassis/Body/Body/Mesh -> /World/agv_8/chassis/Body/Looks/Robot
* 材质摘要:
 * /World/agv_8/chassis/Body/Looks/Robot -> Inputs: 'emissive_intensity=8000', 'metallic_texture_influence=0.9', 'reflection_roughness_texture_influence=1', Textures: 'Textures/STL_Robot_albedo.<UDIM>.png', 'Textures/STL_Robot_emissive.<UDIM>.png', 'Textures/STL_Robot_normal.<UDIM>.png', 'Textures/STL_Robot_orm.<UDIM>.png'


---


### '/World/agv_8/left_wheel/Left_Wheel' (Xform)
* 引用: reference:HighResProps/Left_Wheel.usd
* BBox (world): size=(0.162, 0.057, 0.162), center=(16.600, 29.540, 0.240)
* 几何统计: Mesh=1, Vertices=15925, Faces=15672
* 子Mesh材质: /World/agv_8/left_wheel/Left_Wheel/Left_Wheel/Mesh_002 -> /World/agv_8/left_wheel/Left_Wheel/Looks/Robot
* 材质摘要:
 * /World/agv_8/left_wheel/Left_Wheel/Looks/Robot -> Inputs: 'metallic_texture_influence=1', 'reflection_roughness_texture_influence=1', Textures: 'Textures/STL_Robot_albedo.<UDIM>.png', 'Textures/STL_Robot_normal.<UDIM>.png', 'Textures/STL_Robot_orm.<UDIM>.png'


---


### '/World/agv_8/right_wheel/Right_Wheel' (Xform)
* 引用: reference:HighResProps/Right_Wheel.usd
* BBox (world): size=(0.162, 0.057, 0.162), center=(16.600, 28.960, 0.240)
* 几何统计: Mesh=1, Vertices=15925, Faces=15672
* 子Mesh材质: /World/agv_8/right_wheel/Right_Wheel/Right_Wheel/Mesh_005 -> /World/agv_8/right_wheel/Right_Wheel/Looks/Robot
* 材质摘要:
 * /World/agv_8/right_wheel/Right_Wheel/Looks/Robot -> Inputs: 'metallic_texture_influence=1', 'reflection_roughness_texture_influence=1', Textures: 'Textures/STL_Robot_albedo.<UDIM>.png', 'Textures/STL_Robot_normal.<UDIM>.png', 'Textures/STL_Robot_orm.<UDIM>.png'


---


### '/World/agv_8/lift/Lift' (Xform)
* 引用: reference:HighResProps/Lift_v2.usd
* BBox (world): size=(1.023, 0.659, 0.169), center=(16.344, 29.251, 0.306)
* 几何统计: Mesh=1, Vertices=78479, Faces=77595
* 子Mesh材质: /World/agv_8/lift/Lift/Lift/Mesh_012 -> /World/agv_8/lift/Lift/Looks/Robot
* 材质摘要:
 * /World/agv_8/lift/Lift/Looks/Robot -> Inputs: 'metallic_texture_influence=0.901', 'reflection_roughness_texture_influence=1', Textures: 'Textures/STL_Robot_albedo.<UDIM>.png', 'Textures/STL_Robot_normal.<UDIM>.png', 'Textures/STL_Robot_orm.<UDIM>.png'


---


### '/World/agv_8/left_swivel/Left_Swivel' (Xform)
* 引用: reference:HighResProps/Left_Swivel.usd
* BBox (world): size=(0.095, 0.033, 0.111), center=(15.923, 29.343, 0.263)
* 几何统计: Mesh=1, Vertices=16, Faces=24
* 子Mesh材质: /World/agv_8/left_swivel/Left_Swivel/STR_Left_Swivel -> /World/agv_8/left_swivel/Left_Swivel/materials/Looks/Robot
* 材质摘要:
 * /World/agv_8/left_swivel/Left_Swivel/materials/Looks/Robot -> Inputs: 'metallic_texture_influence=1', 'reflection_roughness_texture_influence=1', Textures: 'Textures/STL_Robot_albedo.%3CUDIM%3E.png', 'Textures/STL_Robot_normal.%3CUDIM%3E.png', 'Textures/STL_Robot_orm.%3CUDIM%3E.png'


---


### '/World/agv_8/left_swivel/Left_Swivel/materials' (Xform)
* 引用: payload:./materials.usd
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(0.000, 0.000, 0.000)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/agv_8/right_swivel/Right_Swivel' (Xform)
* 引用: reference:HighResProps/Right_Swivel.usd
* BBox (world): size=(0.095, 0.033, 0.111), center=(15.923, 29.157, 0.263)
* 几何统计: Mesh=1, Vertices=16, Faces=24
* 子Mesh材质: /World/agv_8/right_swivel/Right_Swivel/STR_Right_Swivel -> /World/agv_8/right_swivel/Right_Swivel/materials/Looks/Robot
* 材质摘要:
 * /World/agv_8/right_swivel/Right_Swivel/materials/Looks/Robot -> Inputs: 'metallic_texture_influence=1', 'reflection_roughness_texture_influence=1', Textures: 'Textures/STL_Robot_albedo.%3CUDIM%3E.png', 'Textures/STL_Robot_normal.%3CUDIM%3E.png', 'Textures/STL_Robot_orm.%3CUDIM%3E.png'


---


### '/World/agv_8/right_swivel/Right_Swivel/materials' (Xform)
* 引用: payload:./materials.usd
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(0.000, 0.000, 0.000)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/agv_8/left_caster/Inner_Left_Wheel' (Xform)
* 引用: reference:HighResProps/Inner_Left_Wheel.usd
* BBox (world): size=(0.135, 0.029, 0.135), center=(15.923, 29.343, 0.230)
* 几何统计: Mesh=1, Vertices=162, Faces=320
* 子Mesh材质: /World/agv_8/left_caster/Inner_Left_Wheel/STR_Inner_Left_Wheel -> /World/agv_8/left_caster/Inner_Left_Wheel/materials/Looks/Robot
* 材质摘要:
 * /World/agv_8/left_caster/Inner_Left_Wheel/materials/Looks/Robot -> Inputs: 'metallic_texture_influence=1', 'reflection_roughness_texture_influence=1', Textures: 'Textures/STL_Robot_albedo.%3CUDIM%3E.png', 'Textures/STL_Robot_normal.%3CUDIM%3E.png', 'Textures/STL_Robot_orm.%3CUDIM%3E.png'


---


### '/World/agv_8/left_caster/Inner_Left_Wheel/materials' (Xform)
* 引用: payload:./materials.usd
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(0.000, 0.000, 0.000)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/agv_8/right_caster/Inner_Right_Wheel' (Xform)
* 引用: reference:HighResProps/Inner_Right_Wheel.usd
* BBox (world): size=(0.135, 0.029, 0.135), center=(15.923, 29.157, 0.230)
* 几何统计: Mesh=1, Vertices=162, Faces=320
* 子Mesh材质: /World/agv_8/right_caster/Inner_Right_Wheel/STR_Inner_Right_Wheel -> /World/agv_8/right_caster/Inner_Right_Wheel/materials/Looks/Robot
* 材质摘要:
 * /World/agv_8/right_caster/Inner_Right_Wheel/materials/Looks/Robot -> Inputs: 'metallic_texture_influence=1', 'reflection_roughness_texture_influence=1', Textures: 'Textures/STL_Robot_albedo.%3CUDIM%3E.png', 'Textures/STL_Robot_normal.%3CUDIM%3E.png', 'Textures/STL_Robot_orm.%3CUDIM%3E.png'


---


### '/World/agv_8/right_caster/Inner_Right_Wheel/materials' (Xform)
* 引用: payload:./materials.usd
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(0.000, 0.000, 0.000)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/Conveyor_1' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/Conveyor_Belt/Conveyor_Belt.usdc
* BBox (world): size=(0.799, 4.204, 9.846), center=(-18.717, 23.877, 0.611)
* 几何统计: Mesh=1, Vertices=3764, Faces=2876
* 子Mesh材质: /World/Conveyor_1/Meshes/Sketchfab_model/_aaef2bbe46a4470bc765b4ce24a8c4c_fbx/RootNode/Cylinder001/Cylinder001_Material__0_0/Cylinder001_Material__0_0 -> 未绑定


---


### '/World/Conveyor_2' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/Conveyor_Belt/Conveyor_Belt.usdc
* BBox (world): size=(0.799, 4.204, 9.846), center=(-13.717, 23.877, 0.611)
* 几何统计: Mesh=1, Vertices=3764, Faces=2876
* 子Mesh材质: /World/Conveyor_2/Meshes/Sketchfab_model/_aaef2bbe46a4470bc765b4ce24a8c4c_fbx/RootNode/Cylinder001/Cylinder001_Material__0_0/Cylinder001_Material__0_0 -> 未绑定


---


### '/World/Conveyor_3' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/Conveyor_Belt/Conveyor_Belt.usdc
* BBox (world): size=(0.799, 4.204, 9.846), center=(-8.717, 23.877, 0.611)
* 几何统计: Mesh=1, Vertices=3764, Faces=2876
* 子Mesh材质: /World/Conveyor_3/Meshes/Sketchfab_model/_aaef2bbe46a4470bc765b4ce24a8c4c_fbx/RootNode/Cylinder001/Cylinder001_Material__0_0/Cylinder001_Material__0_0 -> 未绑定


---


### '/World/Conveyor_4' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/Conveyor_Belt/Conveyor_Belt.usdc
* BBox (world): size=(0.799, 4.204, 9.846), center=(-3.717, 23.877, 0.611)
* 几何统计: Mesh=1, Vertices=3764, Faces=2876
* 子Mesh材质: /World/Conveyor_4/Meshes/Sketchfab_model/_aaef2bbe46a4470bc765b4ce24a8c4c_fbx/RootNode/Cylinder001/Cylinder001_Material__0_0/Cylinder001_Material__0_0 -> 未绑定


---


### '/World/Conveyor_5' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/Conveyor_Belt/Conveyor_Belt.usdc
* BBox (world): size=(0.799, 4.204, 9.846), center=(1.283, 23.877, 0.611)
* 几何统计: Mesh=1, Vertices=3764, Faces=2876
* 子Mesh材质: /World/Conveyor_5/Meshes/Sketchfab_model/_aaef2bbe46a4470bc765b4ce24a8c4c_fbx/RootNode/Cylinder001/Cylinder001_Material__0_0/Cylinder001_Material__0_0 -> 未绑定


---


### '/World/Conveyor_6' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/Conveyor_Belt/Conveyor_Belt.usdc
* BBox (world): size=(0.799, 4.204, 9.846), center=(6.283, 23.877, 0.611)
* 几何统计: Mesh=1, Vertices=3764, Faces=2876
* 子Mesh材质: /World/Conveyor_6/Meshes/Sketchfab_model/_aaef2bbe46a4470bc765b4ce24a8c4c_fbx/RootNode/Cylinder001/Cylinder001_Material__0_0/Cylinder001_Material__0_0 -> 未绑定


---


### '/World/Conveyor_7' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/Conveyor_Belt/Conveyor_Belt.usdc
* BBox (world): size=(0.799, 4.204, 9.846), center=(11.283, 23.877, 0.611)
* 几何统计: Mesh=1, Vertices=3764, Faces=2876
* 子Mesh材质: /World/Conveyor_7/Meshes/Sketchfab_model/_aaef2bbe46a4470bc765b4ce24a8c4c_fbx/RootNode/Cylinder001/Cylinder001_Material__0_0/Cylinder001_Material__0_0 -> 未绑定


---


### '/World/Conveyor_8' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/Conveyor_Belt/Conveyor_Belt.usdc
* BBox (world): size=(0.799, 4.204, 9.846), center=(16.283, 23.877, 0.611)
* 几何统计: Mesh=1, Vertices=3764, Faces=2876
* 子Mesh材质: /World/Conveyor_8/Meshes/Sketchfab_model/_aaef2bbe46a4470bc765b4ce24a8c4c_fbx/RootNode/Cylinder001/Cylinder001_Material__0_0/Cylinder001_Material__0_0 -> 未绑定


---


### '/World/BoxOnConveyor_1' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc
* BBox (world): size=(35.888, 35.888, 35.888), center=(-18.700, 19.500, 1.279)
* 几何统计: Mesh=1, Vertices=56, Faces=44
* 子Mesh材质: /World/BoxOnConveyor_1/Meshes/Sketchfab_model/f49ad5edc352496894d3a02181012422_fbx/RootNode/Box072/Box072_06___Default_0/Box072_06___Default_0 -> 未绑定


---


### '/World/BoxOnConveyor_2' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc
* BBox (world): size=(35.888, 35.888, 35.888), center=(-13.700, 19.500, 1.279)
* 几何统计: Mesh=1, Vertices=56, Faces=44
* 子Mesh材质: /World/BoxOnConveyor_2/Meshes/Sketchfab_model/f49ad5edc352496894d3a02181012422_fbx/RootNode/Box072/Box072_06___Default_0/Box072_06___Default_0 -> 未绑定


---


### '/World/BoxOnConveyor_3' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc
* BBox (world): size=(35.888, 35.888, 35.888), center=(-8.700, 19.500, 1.279)
* 几何统计: Mesh=1, Vertices=56, Faces=44
* 子Mesh材质: /World/BoxOnConveyor_3/Meshes/Sketchfab_model/f49ad5edc352496894d3a02181012422_fbx/RootNode/Box072/Box072_06___Default_0/Box072_06___Default_0 -> 未绑定


---


### '/World/BoxOnConveyor_4' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc
* BBox (world): size=(35.888, 35.888, 35.888), center=(-3.700, 19.500, 1.279)
* 几何统计: Mesh=1, Vertices=56, Faces=44
* 子Mesh材质: /World/BoxOnConveyor_4/Meshes/Sketchfab_model/f49ad5edc352496894d3a02181012422_fbx/RootNode/Box072/Box072_06___Default_0/Box072_06___Default_0 -> 未绑定


---


### '/World/BoxOnConveyor_5' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc
* BBox (world): size=(35.888, 35.888, 35.888), center=(1.300, 19.500, 1.279)
* 几何统计: Mesh=1, Vertices=56, Faces=44
* 子Mesh材质: /World/BoxOnConveyor_5/Meshes/Sketchfab_model/f49ad5edc352496894d3a02181012422_fbx/RootNode/Box072/Box072_06___Default_0/Box072_06___Default_0 -> 未绑定


---


### '/World/BoxOnConveyor_6' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc
* BBox (world): size=(35.888, 35.888, 35.888), center=(6.300, 19.500, 1.279)
* 几何统计: Mesh=1, Vertices=56, Faces=44
* 子Mesh材质: /World/BoxOnConveyor_6/Meshes/Sketchfab_model/f49ad5edc352496894d3a02181012422_fbx/RootNode/Box072/Box072_06___Default_0/Box072_06___Default_0 -> 未绑定


---


### '/World/BoxOnConveyor_7' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc
* BBox (world): size=(35.888, 35.888, 35.888), center=(11.300, 19.500, 1.279)
* 几何统计: Mesh=1, Vertices=56, Faces=44
* 子Mesh材质: /World/BoxOnConveyor_7/Meshes/Sketchfab_model/f49ad5edc352496894d3a02181012422_fbx/RootNode/Box072/Box072_06___Default_0/Box072_06___Default_0 -> 未绑定


---


### '/World/BoxOnConveyor_8' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc
* BBox (world): size=(35.888, 35.888, 35.888), center=(16.300, 19.500, 1.279)
* 几何统计: Mesh=1, Vertices=56, Faces=44
* 子Mesh材质: /World/BoxOnConveyor_8/Meshes/Sketchfab_model/f49ad5edc352496894d3a02181012422_fbx/RootNode/Box072/Box072_06___Default_0/Box072_06___Default_0 -> 未绑定


---


### '/World/BoxOnConveyor_9' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc
* BBox (world): size=(35.888, 35.888, 35.888), center=(-18.700, 20.400, 1.279)
* 几何统计: Mesh=1, Vertices=56, Faces=44
* 子Mesh材质: /World/BoxOnConveyor_9/Meshes/Sketchfab_model/f49ad5edc352496894d3a02181012422_fbx/RootNode/Box072/Box072_06___Default_0/Box072_06___Default_0 -> 未绑定


---


### '/World/BoxOnConveyor_10' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc
* BBox (world): size=(35.888, 35.888, 35.888), center=(-13.700, 20.400, 1.279)
* 几何统计: Mesh=1, Vertices=56, Faces=44
* 子Mesh材质: /World/BoxOnConveyor_10/Meshes/Sketchfab_model/f49ad5edc352496894d3a02181012422_fbx/RootNode/Box072/Box072_06___Default_0/Box072_06___Default_0 -> 未绑定


---


### '/World/BoxOnConveyor_11' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc
* BBox (world): size=(35.888, 35.888, 35.888), center=(-8.700, 20.400, 1.279)
* 几何统计: Mesh=1, Vertices=56, Faces=44
* 子Mesh材质: /World/BoxOnConveyor_11/Meshes/Sketchfab_model/f49ad5edc352496894d3a02181012422_fbx/RootNode/Box072/Box072_06___Default_0/Box072_06___Default_0 -> 未绑定


---


### '/World/BoxOnConveyor_12' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc
* BBox (world): size=(35.888, 35.888, 35.888), center=(-3.700, 20.400, 1.279)
* 几何统计: Mesh=1, Vertices=56, Faces=44
* 子Mesh材质: /World/BoxOnConveyor_12/Meshes/Sketchfab_model/f49ad5edc352496894d3a02181012422_fbx/RootNode/Box072/Box072_06___Default_0/Box072_06___Default_0 -> 未绑定


---


### '/World/BoxOnConveyor_13' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc
* BBox (world): size=(35.888, 35.888, 35.888), center=(1.300, 20.400, 1.279)
* 几何统计: Mesh=1, Vertices=56, Faces=44
* 子Mesh材质: /World/BoxOnConveyor_13/Meshes/Sketchfab_model/f49ad5edc352496894d3a02181012422_fbx/RootNode/Box072/Box072_06___Default_0/Box072_06___Default_0 -> 未绑定


---


### '/World/BoxOnConveyor_14' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc
* BBox (world): size=(35.888, 35.888, 35.888), center=(6.300, 20.400, 1.279)
* 几何统计: Mesh=1, Vertices=56, Faces=44
* 子Mesh材质: /World/BoxOnConveyor_14/Meshes/Sketchfab_model/f49ad5edc352496894d3a02181012422_fbx/RootNode/Box072/Box072_06___Default_0/Box072_06___Default_0 -> 未绑定


---


### '/World/BoxOnConveyor_15' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc
* BBox (world): size=(35.888, 35.888, 35.888), center=(11.300, 20.400, 1.279)
* 几何统计: Mesh=1, Vertices=56, Faces=44
* 子Mesh材质: /World/BoxOnConveyor_15/Meshes/Sketchfab_model/f49ad5edc352496894d3a02181012422_fbx/RootNode/Box072/Box072_06___Default_0/Box072_06___Default_0 -> 未绑定


---


### '/World/BoxOnConveyor_16' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc
* BBox (world): size=(35.888, 35.888, 35.888), center=(16.300, 20.400, 1.279)
* 几何统计: Mesh=1, Vertices=56, Faces=44
* 子Mesh材质: /World/BoxOnConveyor_16/Meshes/Sketchfab_model/f49ad5edc352496894d3a02181012422_fbx/RootNode/Box072/Box072_06___Default_0/Box072_06___Default_0 -> 未绑定


---


### '/World/BoxOnConveyor_17' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc
* BBox (world): size=(35.888, 35.888, 35.888), center=(-18.700, 21.300, 1.279)
* 几何统计: Mesh=1, Vertices=56, Faces=44
* 子Mesh材质: /World/BoxOnConveyor_17/Meshes/Sketchfab_model/f49ad5edc352496894d3a02181012422_fbx/RootNode/Box072/Box072_06___Default_0/Box072_06___Default_0 -> 未绑定


---


### '/World/BoxOnConveyor_18' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc
* BBox (world): size=(35.888, 35.888, 35.888), center=(-13.700, 21.300, 1.279)
* 几何统计: Mesh=1, Vertices=56, Faces=44
* 子Mesh材质: /World/BoxOnConveyor_18/Meshes/Sketchfab_model/f49ad5edc352496894d3a02181012422_fbx/RootNode/Box072/Box072_06___Default_0/Box072_06___Default_0 -> 未绑定


---


### '/World/BoxOnConveyor_19' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc
* BBox (world): size=(35.888, 35.888, 35.888), center=(-8.700, 21.300, 1.279)
* 几何统计: Mesh=1, Vertices=56, Faces=44
* 子Mesh材质: /World/BoxOnConveyor_19/Meshes/Sketchfab_model/f49ad5edc352496894d3a02181012422_fbx/RootNode/Box072/Box072_06___Default_0/Box072_06___Default_0 -> 未绑定


---


### '/World/BoxOnConveyor_20' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc
* BBox (world): size=(35.888, 35.888, 35.888), center=(-3.700, 21.300, 1.279)
* 几何统计: Mesh=1, Vertices=56, Faces=44
* 子Mesh材质: /World/BoxOnConveyor_20/Meshes/Sketchfab_model/f49ad5edc352496894d3a02181012422_fbx/RootNode/Box072/Box072_06___Default_0/Box072_06___Default_0 -> 未绑定


---


### '/World/BoxOnConveyor_21' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc
* BBox (world): size=(35.888, 35.888, 35.888), center=(1.300, 21.300, 1.279)
* 几何统计: Mesh=1, Vertices=56, Faces=44
* 子Mesh材质: /World/BoxOnConveyor_21/Meshes/Sketchfab_model/f49ad5edc352496894d3a02181012422_fbx/RootNode/Box072/Box072_06___Default_0/Box072_06___Default_0 -> 未绑定


---


### '/World/BoxOnConveyor_22' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc
* BBox (world): size=(35.888, 35.888, 35.888), center=(6.300, 21.300, 1.279)
* 几何统计: Mesh=1, Vertices=56, Faces=44
* 子Mesh材质: /World/BoxOnConveyor_22/Meshes/Sketchfab_model/f49ad5edc352496894d3a02181012422_fbx/RootNode/Box072/Box072_06___Default_0/Box072_06___Default_0 -> 未绑定


---


### '/World/BoxOnConveyor_23' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc
* BBox (world): size=(35.888, 35.888, 35.888), center=(11.300, 21.300, 1.279)
* 几何统计: Mesh=1, Vertices=56, Faces=44
* 子Mesh材质: /World/BoxOnConveyor_23/Meshes/Sketchfab_model/f49ad5edc352496894d3a02181012422_fbx/RootNode/Box072/Box072_06___Default_0/Box072_06___Default_0 -> 未绑定


---


### '/World/BoxOnConveyor_24' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc
* BBox (world): size=(35.888, 35.888, 35.888), center=(16.300, 21.300, 1.279)
* 几何统计: Mesh=1, Vertices=56, Faces=44
* 子Mesh材质: /World/BoxOnConveyor_24/Meshes/Sketchfab_model/f49ad5edc352496894d3a02181012422_fbx/RootNode/Box072/Box072_06___Default_0/Box072_06___Default_0 -> 未绑定


---


### '/World/BoxOnConveyor_25' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc
* BBox (world): size=(35.888, 35.888, 35.888), center=(-18.700, 22.200, 1.279)
* 几何统计: Mesh=1, Vertices=56, Faces=44
* 子Mesh材质: /World/BoxOnConveyor_25/Meshes/Sketchfab_model/f49ad5edc352496894d3a02181012422_fbx/RootNode/Box072/Box072_06___Default_0/Box072_06___Default_0 -> 未绑定


---


### '/World/BoxOnConveyor_26' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc
* BBox (world): size=(35.888, 35.888, 35.888), center=(-13.700, 22.200, 1.279)
* 几何统计: Mesh=1, Vertices=56, Faces=44
* 子Mesh材质: /World/BoxOnConveyor_26/Meshes/Sketchfab_model/f49ad5edc352496894d3a02181012422_fbx/RootNode/Box072/Box072_06___Default_0/Box072_06___Default_0 -> 未绑定


---


### '/World/BoxOnConveyor_27' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc
* BBox (world): size=(35.888, 35.888, 35.888), center=(-8.700, 22.200, 1.279)
* 几何统计: Mesh=1, Vertices=56, Faces=44
* 子Mesh材质: /World/BoxOnConveyor_27/Meshes/Sketchfab_model/f49ad5edc352496894d3a02181012422_fbx/RootNode/Box072/Box072_06___Default_0/Box072_06___Default_0 -> 未绑定


---


### '/World/BoxOnConveyor_28' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc
* BBox (world): size=(35.888, 35.888, 35.888), center=(-3.700, 22.200, 1.279)
* 几何统计: Mesh=1, Vertices=56, Faces=44
* 子Mesh材质: /World/BoxOnConveyor_28/Meshes/Sketchfab_model/f49ad5edc352496894d3a02181012422_fbx/RootNode/Box072/Box072_06___Default_0/Box072_06___Default_0 -> 未绑定


---


### '/World/BoxOnConveyor_29' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc
* BBox (world): size=(35.888, 35.888, 35.888), center=(1.300, 22.200, 1.279)
* 几何统计: Mesh=1, Vertices=56, Faces=44
* 子Mesh材质: /World/BoxOnConveyor_29/Meshes/Sketchfab_model/f49ad5edc352496894d3a02181012422_fbx/RootNode/Box072/Box072_06___Default_0/Box072_06___Default_0 -> 未绑定


---


### '/World/BoxOnConveyor_30' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc
* BBox (world): size=(35.888, 35.888, 35.888), center=(6.300, 22.200, 1.279)
* 几何统计: Mesh=1, Vertices=56, Faces=44
* 子Mesh材质: /World/BoxOnConveyor_30/Meshes/Sketchfab_model/f49ad5edc352496894d3a02181012422_fbx/RootNode/Box072/Box072_06___Default_0/Box072_06___Default_0 -> 未绑定


---


### '/World/BoxOnConveyor_31' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc
* BBox (world): size=(35.888, 35.888, 35.888), center=(11.300, 22.200, 1.279)
* 几何统计: Mesh=1, Vertices=56, Faces=44
* 子Mesh材质: /World/BoxOnConveyor_31/Meshes/Sketchfab_model/f49ad5edc352496894d3a02181012422_fbx/RootNode/Box072/Box072_06___Default_0/Box072_06___Default_0 -> 未绑定


---


### '/World/BoxOnConveyor_32' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc
* BBox (world): size=(35.888, 35.888, 35.888), center=(16.300, 22.200, 1.279)
* 几何统计: Mesh=1, Vertices=56, Faces=44
* 子Mesh材质: /World/BoxOnConveyor_32/Meshes/Sketchfab_model/f49ad5edc352496894d3a02181012422_fbx/RootNode/Box072/Box072_06___Default_0/Box072_06___Default_0 -> 未绑定


---


### '/World/BoxOnConveyor_33' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc
* BBox (world): size=(35.888, 35.888, 35.888), center=(-18.700, 23.100, 1.279)
* 几何统计: Mesh=1, Vertices=56, Faces=44
* 子Mesh材质: /World/BoxOnConveyor_33/Meshes/Sketchfab_model/f49ad5edc352496894d3a02181012422_fbx/RootNode/Box072/Box072_06___Default_0/Box072_06___Default_0 -> 未绑定


---


### '/World/BoxOnConveyor_34' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc
* BBox (world): size=(35.888, 35.888, 35.888), center=(-13.700, 23.100, 1.279)
* 几何统计: Mesh=1, Vertices=56, Faces=44
* 子Mesh材质: /World/BoxOnConveyor_34/Meshes/Sketchfab_model/f49ad5edc352496894d3a02181012422_fbx/RootNode/Box072/Box072_06___Default_0/Box072_06___Default_0 -> 未绑定


---


### '/World/BoxOnConveyor_35' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc
* BBox (world): size=(35.888, 35.888, 35.888), center=(-8.700, 23.100, 1.279)
* 几何统计: Mesh=1, Vertices=56, Faces=44
* 子Mesh材质: /World/BoxOnConveyor_35/Meshes/Sketchfab_model/f49ad5edc352496894d3a02181012422_fbx/RootNode/Box072/Box072_06___Default_0/Box072_06___Default_0 -> 未绑定


---


### '/World/BoxOnConveyor_36' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc
* BBox (world): size=(35.888, 35.888, 35.888), center=(-3.700, 23.100, 1.279)
* 几何统计: Mesh=1, Vertices=56, Faces=44
* 子Mesh材质: /World/BoxOnConveyor_36/Meshes/Sketchfab_model/f49ad5edc352496894d3a02181012422_fbx/RootNode/Box072/Box072_06___Default_0/Box072_06___Default_0 -> 未绑定


---


### '/World/BoxOnConveyor_37' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc
* BBox (world): size=(35.888, 35.888, 35.888), center=(1.300, 23.100, 1.279)
* 几何统计: Mesh=1, Vertices=56, Faces=44
* 子Mesh材质: /World/BoxOnConveyor_37/Meshes/Sketchfab_model/f49ad5edc352496894d3a02181012422_fbx/RootNode/Box072/Box072_06___Default_0/Box072_06___Default_0 -> 未绑定


---


### '/World/BoxOnConveyor_38' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc
* BBox (world): size=(35.888, 35.888, 35.888), center=(6.300, 23.100, 1.279)
* 几何统计: Mesh=1, Vertices=56, Faces=44
* 子Mesh材质: /World/BoxOnConveyor_38/Meshes/Sketchfab_model/f49ad5edc352496894d3a02181012422_fbx/RootNode/Box072/Box072_06___Default_0/Box072_06___Default_0 -> 未绑定


---


### '/World/BoxOnConveyor_39' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc
* BBox (world): size=(35.888, 35.888, 35.888), center=(11.300, 23.100, 1.279)
* 几何统计: Mesh=1, Vertices=56, Faces=44
* 子Mesh材质: /World/BoxOnConveyor_39/Meshes/Sketchfab_model/f49ad5edc352496894d3a02181012422_fbx/RootNode/Box072/Box072_06___Default_0/Box072_06___Default_0 -> 未绑定


---


### '/World/BoxOnConveyor_40' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc
* BBox (world): size=(35.888, 35.888, 35.888), center=(16.300, 23.100, 1.279)
* 几何统计: Mesh=1, Vertices=56, Faces=44
* 子Mesh材质: /World/BoxOnConveyor_40/Meshes/Sketchfab_model/f49ad5edc352496894d3a02181012422_fbx/RootNode/Box072/Box072_06___Default_0/Box072_06___Default_0 -> 未绑定


---


### '/World/BoxOnConveyor_41' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc
* BBox (world): size=(35.888, 35.888, 35.888), center=(-18.700, 24.000, 1.279)
* 几何统计: Mesh=1, Vertices=56, Faces=44
* 子Mesh材质: /World/BoxOnConveyor_41/Meshes/Sketchfab_model/f49ad5edc352496894d3a02181012422_fbx/RootNode/Box072/Box072_06___Default_0/Box072_06___Default_0 -> 未绑定


---


### '/World/BoxOnConveyor_42' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc
* BBox (world): size=(35.888, 35.888, 35.888), center=(-13.700, 24.000, 1.279)
* 几何统计: Mesh=1, Vertices=56, Faces=44
* 子Mesh材质: /World/BoxOnConveyor_42/Meshes/Sketchfab_model/f49ad5edc352496894d3a02181012422_fbx/RootNode/Box072/Box072_06___Default_0/Box072_06___Default_0 -> 未绑定


---


### '/World/BoxOnConveyor_43' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc
* BBox (world): size=(35.888, 35.888, 35.888), center=(-8.700, 24.000, 1.279)
* 几何统计: Mesh=1, Vertices=56, Faces=44
* 子Mesh材质: /World/BoxOnConveyor_43/Meshes/Sketchfab_model/f49ad5edc352496894d3a02181012422_fbx/RootNode/Box072/Box072_06___Default_0/Box072_06___Default_0 -> 未绑定


---


### '/World/BoxOnConveyor_44' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc
* BBox (world): size=(35.888, 35.888, 35.888), center=(-3.700, 24.000, 1.279)
* 几何统计: Mesh=1, Vertices=56, Faces=44
* 子Mesh材质: /World/BoxOnConveyor_44/Meshes/Sketchfab_model/f49ad5edc352496894d3a02181012422_fbx/RootNode/Box072/Box072_06___Default_0/Box072_06___Default_0 -> 未绑定


---


### '/World/BoxOnConveyor_45' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc
* BBox (world): size=(35.888, 35.888, 35.888), center=(1.300, 24.000, 1.279)
* 几何统计: Mesh=1, Vertices=56, Faces=44
* 子Mesh材质: /World/BoxOnConveyor_45/Meshes/Sketchfab_model/f49ad5edc352496894d3a02181012422_fbx/RootNode/Box072/Box072_06___Default_0/Box072_06___Default_0 -> 未绑定


---


### '/World/BoxOnConveyor_46' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc
* BBox (world): size=(35.888, 35.888, 35.888), center=(6.300, 24.000, 1.279)
* 几何统计: Mesh=1, Vertices=56, Faces=44
* 子Mesh材质: /World/BoxOnConveyor_46/Meshes/Sketchfab_model/f49ad5edc352496894d3a02181012422_fbx/RootNode/Box072/Box072_06___Default_0/Box072_06___Default_0 -> 未绑定


---


### '/World/BoxOnConveyor_47' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc
* BBox (world): size=(35.888, 35.888, 35.888), center=(11.300, 24.000, 1.279)
* 几何统计: Mesh=1, Vertices=56, Faces=44
* 子Mesh材质: /World/BoxOnConveyor_47/Meshes/Sketchfab_model/f49ad5edc352496894d3a02181012422_fbx/RootNode/Box072/Box072_06___Default_0/Box072_06___Default_0 -> 未绑定


---


### '/World/BoxOnConveyor_48' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc
* BBox (world): size=(35.888, 35.888, 35.888), center=(16.300, 24.000, 1.279)
* 几何统计: Mesh=1, Vertices=56, Faces=44
* 子Mesh材质: /World/BoxOnConveyor_48/Meshes/Sketchfab_model/f49ad5edc352496894d3a02181012422_fbx/RootNode/Box072/Box072_06___Default_0/Box072_06___Default_0 -> 未绑定


---


### '/World/BoxOnConveyor_49' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc
* BBox (world): size=(35.888, 35.888, 35.888), center=(-18.700, 24.900, 1.279)
* 几何统计: Mesh=1, Vertices=56, Faces=44
* 子Mesh材质: /World/BoxOnConveyor_49/Meshes/Sketchfab_model/f49ad5edc352496894d3a02181012422_fbx/RootNode/Box072/Box072_06___Default_0/Box072_06___Default_0 -> 未绑定


---


### '/World/BoxOnConveyor_50' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc
* BBox (world): size=(35.888, 35.888, 35.888), center=(-13.700, 24.900, 1.279)
* 几何统计: Mesh=1, Vertices=56, Faces=44
* 子Mesh材质: /World/BoxOnConveyor_50/Meshes/Sketchfab_model/f49ad5edc352496894d3a02181012422_fbx/RootNode/Box072/Box072_06___Default_0/Box072_06___Default_0 -> 未绑定


---


### '/World/BoxOnConveyor_51' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc
* BBox (world): size=(35.888, 35.888, 35.888), center=(-8.700, 24.900, 1.279)
* 几何统计: Mesh=1, Vertices=56, Faces=44
* 子Mesh材质: /World/BoxOnConveyor_51/Meshes/Sketchfab_model/f49ad5edc352496894d3a02181012422_fbx/RootNode/Box072/Box072_06___Default_0/Box072_06___Default_0 -> 未绑定


---


### '/World/BoxOnConveyor_52' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc
* BBox (world): size=(35.888, 35.888, 35.888), center=(-3.700, 24.900, 1.279)
* 几何统计: Mesh=1, Vertices=56, Faces=44
* 子Mesh材质: /World/BoxOnConveyor_52/Meshes/Sketchfab_model/f49ad5edc352496894d3a02181012422_fbx/RootNode/Box072/Box072_06___Default_0/Box072_06___Default_0 -> 未绑定


---


### '/World/BoxOnConveyor_53' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc
* BBox (world): size=(35.888, 35.888, 35.888), center=(1.300, 24.900, 1.279)
* 几何统计: Mesh=1, Vertices=56, Faces=44
* 子Mesh材质: /World/BoxOnConveyor_53/Meshes/Sketchfab_model/f49ad5edc352496894d3a02181012422_fbx/RootNode/Box072/Box072_06___Default_0/Box072_06___Default_0 -> 未绑定


---


### '/World/BoxOnConveyor_54' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc
* BBox (world): size=(35.888, 35.888, 35.888), center=(6.300, 24.900, 1.279)
* 几何统计: Mesh=1, Vertices=56, Faces=44
* 子Mesh材质: /World/BoxOnConveyor_54/Meshes/Sketchfab_model/f49ad5edc352496894d3a02181012422_fbx/RootNode/Box072/Box072_06___Default_0/Box072_06___Default_0 -> 未绑定


---


### '/World/BoxOnConveyor_55' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc
* BBox (world): size=(35.888, 35.888, 35.888), center=(11.300, 24.900, 1.279)
* 几何统计: Mesh=1, Vertices=56, Faces=44
* 子Mesh材质: /World/BoxOnConveyor_55/Meshes/Sketchfab_model/f49ad5edc352496894d3a02181012422_fbx/RootNode/Box072/Box072_06___Default_0/Box072_06___Default_0 -> 未绑定


---


### '/World/BoxOnConveyor_56' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc
* BBox (world): size=(35.888, 35.888, 35.888), center=(16.300, 24.900, 1.279)
* 几何统计: Mesh=1, Vertices=56, Faces=44
* 子Mesh材质: /World/BoxOnConveyor_56/Meshes/Sketchfab_model/f49ad5edc352496894d3a02181012422_fbx/RootNode/Box072/Box072_06___Default_0/Box072_06___Default_0 -> 未绑定


---


### '/World/BoxOnConveyor_57' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc
* BBox (world): size=(35.888, 35.888, 35.888), center=(-18.700, 25.800, 1.279)
* 几何统计: Mesh=1, Vertices=56, Faces=44
* 子Mesh材质: /World/BoxOnConveyor_57/Meshes/Sketchfab_model/f49ad5edc352496894d3a02181012422_fbx/RootNode/Box072/Box072_06___Default_0/Box072_06___Default_0 -> 未绑定


---


### '/World/BoxOnConveyor_58' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc
* BBox (world): size=(35.888, 35.888, 35.888), center=(-13.700, 25.800, 1.279)
* 几何统计: Mesh=1, Vertices=56, Faces=44
* 子Mesh材质: /World/BoxOnConveyor_58/Meshes/Sketchfab_model/f49ad5edc352496894d3a02181012422_fbx/RootNode/Box072/Box072_06___Default_0/Box072_06___Default_0 -> 未绑定


---


### '/World/BoxOnConveyor_59' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc
* BBox (world): size=(35.888, 35.888, 35.888), center=(-8.700, 25.800, 1.279)
* 几何统计: Mesh=1, Vertices=56, Faces=44
* 子Mesh材质: /World/BoxOnConveyor_59/Meshes/Sketchfab_model/f49ad5edc352496894d3a02181012422_fbx/RootNode/Box072/Box072_06___Default_0/Box072_06___Default_0 -> 未绑定


---


### '/World/BoxOnConveyor_60' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc
* BBox (world): size=(35.888, 35.888, 35.888), center=(-3.700, 25.800, 1.279)
* 几何统计: Mesh=1, Vertices=56, Faces=44
* 子Mesh材质: /World/BoxOnConveyor_60/Meshes/Sketchfab_model/f49ad5edc352496894d3a02181012422_fbx/RootNode/Box072/Box072_06___Default_0/Box072_06___Default_0 -> 未绑定


---


### '/World/BoxOnConveyor_61' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc
* BBox (world): size=(35.888, 35.888, 35.888), center=(1.300, 25.800, 1.279)
* 几何统计: Mesh=1, Vertices=56, Faces=44
* 子Mesh材质: /World/BoxOnConveyor_61/Meshes/Sketchfab_model/f49ad5edc352496894d3a02181012422_fbx/RootNode/Box072/Box072_06___Default_0/Box072_06___Default_0 -> 未绑定


---


### '/World/BoxOnConveyor_62' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc
* BBox (world): size=(35.888, 35.888, 35.888), center=(6.300, 25.800, 1.279)
* 几何统计: Mesh=1, Vertices=56, Faces=44
* 子Mesh材质: /World/BoxOnConveyor_62/Meshes/Sketchfab_model/f49ad5edc352496894d3a02181012422_fbx/RootNode/Box072/Box072_06___Default_0/Box072_06___Default_0 -> 未绑定


---


### '/World/BoxOnConveyor_63' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc
* BBox (world): size=(35.888, 35.888, 35.888), center=(11.300, 25.800, 1.279)
* 几何统计: Mesh=1, Vertices=56, Faces=44
* 子Mesh材质: /World/BoxOnConveyor_63/Meshes/Sketchfab_model/f49ad5edc352496894d3a02181012422_fbx/RootNode/Box072/Box072_06___Default_0/Box072_06___Default_0 -> 未绑定


---


### '/World/BoxOnConveyor_64' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc
* BBox (world): size=(35.888, 35.888, 35.888), center=(16.300, 25.800, 1.279)
* 几何统计: Mesh=1, Vertices=56, Faces=44
* 子Mesh材质: /World/BoxOnConveyor_64/Meshes/Sketchfab_model/f49ad5edc352496894d3a02181012422_fbx/RootNode/Box072/Box072_06___Default_0/Box072_06___Default_0 -> 未绑定


---


### '/World/BoxOnConveyor_65' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc
* BBox (world): size=(35.888, 35.888, 35.888), center=(-18.700, 26.700, 1.279)
* 几何统计: Mesh=1, Vertices=56, Faces=44
* 子Mesh材质: /World/BoxOnConveyor_65/Meshes/Sketchfab_model/f49ad5edc352496894d3a02181012422_fbx/RootNode/Box072/Box072_06___Default_0/Box072_06___Default_0 -> 未绑定


---


### '/World/BoxOnConveyor_66' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc
* BBox (world): size=(35.888, 35.888, 35.888), center=(-13.700, 26.700, 1.279)
* 几何统计: Mesh=1, Vertices=56, Faces=44
* 子Mesh材质: /World/BoxOnConveyor_66/Meshes/Sketchfab_model/f49ad5edc352496894d3a02181012422_fbx/RootNode/Box072/Box072_06___Default_0/Box072_06___Default_0 -> 未绑定


---


### '/World/BoxOnConveyor_67' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc
* BBox (world): size=(35.888, 35.888, 35.888), center=(-8.700, 26.700, 1.279)
* 几何统计: Mesh=1, Vertices=56, Faces=44
* 子Mesh材质: /World/BoxOnConveyor_67/Meshes/Sketchfab_model/f49ad5edc352496894d3a02181012422_fbx/RootNode/Box072/Box072_06___Default_0/Box072_06___Default_0 -> 未绑定


---


### '/World/BoxOnConveyor_68' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc
* BBox (world): size=(35.888, 35.888, 35.888), center=(-3.700, 26.700, 1.279)
* 几何统计: Mesh=1, Vertices=56, Faces=44
* 子Mesh材质: /World/BoxOnConveyor_68/Meshes/Sketchfab_model/f49ad5edc352496894d3a02181012422_fbx/RootNode/Box072/Box072_06___Default_0/Box072_06___Default_0 -> 未绑定


---


### '/World/BoxOnConveyor_69' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc
* BBox (world): size=(35.888, 35.888, 35.888), center=(1.300, 26.700, 1.279)
* 几何统计: Mesh=1, Vertices=56, Faces=44
* 子Mesh材质: /World/BoxOnConveyor_69/Meshes/Sketchfab_model/f49ad5edc352496894d3a02181012422_fbx/RootNode/Box072/Box072_06___Default_0/Box072_06___Default_0 -> 未绑定


---


### '/World/BoxOnConveyor_70' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc
* BBox (world): size=(35.888, 35.888, 35.888), center=(6.300, 26.700, 1.279)
* 几何统计: Mesh=1, Vertices=56, Faces=44
* 子Mesh材质: /World/BoxOnConveyor_70/Meshes/Sketchfab_model/f49ad5edc352496894d3a02181012422_fbx/RootNode/Box072/Box072_06___Default_0/Box072_06___Default_0 -> 未绑定


---


### '/World/BoxOnConveyor_71' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc
* BBox (world): size=(35.888, 35.888, 35.888), center=(11.300, 26.700, 1.279)
* 几何统计: Mesh=1, Vertices=56, Faces=44
* 子Mesh材质: /World/BoxOnConveyor_71/Meshes/Sketchfab_model/f49ad5edc352496894d3a02181012422_fbx/RootNode/Box072/Box072_06___Default_0/Box072_06___Default_0 -> 未绑定


---


### '/World/BoxOnConveyor_72' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc
* BBox (world): size=(35.888, 35.888, 35.888), center=(16.300, 26.700, 1.279)
* 几何统计: Mesh=1, Vertices=56, Faces=44
* 子Mesh材质: /World/BoxOnConveyor_72/Meshes/Sketchfab_model/f49ad5edc352496894d3a02181012422_fbx/RootNode/Box072/Box072_06___Default_0/Box072_06___Default_0 -> 未绑定


---


### '/World/BoxOnConveyor_73' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc
* BBox (world): size=(35.888, 35.888, 35.888), center=(-18.700, 27.600, 1.279)
* 几何统计: Mesh=1, Vertices=56, Faces=44
* 子Mesh材质: /World/BoxOnConveyor_73/Meshes/Sketchfab_model/f49ad5edc352496894d3a02181012422_fbx/RootNode/Box072/Box072_06___Default_0/Box072_06___Default_0 -> 未绑定


---


### '/World/BoxOnConveyor_74' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc
* BBox (world): size=(35.888, 35.888, 35.888), center=(-13.700, 27.600, 1.279)
* 几何统计: Mesh=1, Vertices=56, Faces=44
* 子Mesh材质: /World/BoxOnConveyor_74/Meshes/Sketchfab_model/f49ad5edc352496894d3a02181012422_fbx/RootNode/Box072/Box072_06___Default_0/Box072_06___Default_0 -> 未绑定


---


### '/World/BoxOnConveyor_75' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc
* BBox (world): size=(35.888, 35.888, 35.888), center=(-8.700, 27.600, 1.279)
* 几何统计: Mesh=1, Vertices=56, Faces=44
* 子Mesh材质: /World/BoxOnConveyor_75/Meshes/Sketchfab_model/f49ad5edc352496894d3a02181012422_fbx/RootNode/Box072/Box072_06___Default_0/Box072_06___Default_0 -> 未绑定


---


### '/World/BoxOnConveyor_76' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc
* BBox (world): size=(35.888, 35.888, 35.888), center=(-3.700, 27.600, 1.279)
* 几何统计: Mesh=1, Vertices=56, Faces=44
* 子Mesh材质: /World/BoxOnConveyor_76/Meshes/Sketchfab_model/f49ad5edc352496894d3a02181012422_fbx/RootNode/Box072/Box072_06___Default_0/Box072_06___Default_0 -> 未绑定


---


### '/World/BoxOnConveyor_77' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc
* BBox (world): size=(35.888, 35.888, 35.888), center=(1.300, 27.600, 1.279)
* 几何统计: Mesh=1, Vertices=56, Faces=44
* 子Mesh材质: /World/BoxOnConveyor_77/Meshes/Sketchfab_model/f49ad5edc352496894d3a02181012422_fbx/RootNode/Box072/Box072_06___Default_0/Box072_06___Default_0 -> 未绑定


---


### '/World/BoxOnConveyor_78' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc
* BBox (world): size=(35.888, 35.888, 35.888), center=(6.300, 27.600, 1.279)
* 几何统计: Mesh=1, Vertices=56, Faces=44
* 子Mesh材质: /World/BoxOnConveyor_78/Meshes/Sketchfab_model/f49ad5edc352496894d3a02181012422_fbx/RootNode/Box072/Box072_06___Default_0/Box072_06___Default_0 -> 未绑定


---


### '/World/BoxOnConveyor_79' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc
* BBox (world): size=(35.888, 35.888, 35.888), center=(11.300, 27.600, 1.279)
* 几何统计: Mesh=1, Vertices=56, Faces=44
* 子Mesh材质: /World/BoxOnConveyor_79/Meshes/Sketchfab_model/f49ad5edc352496894d3a02181012422_fbx/RootNode/Box072/Box072_06___Default_0/Box072_06___Default_0 -> 未绑定


---


### '/World/BoxOnConveyor_80' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc
* BBox (world): size=(35.888, 35.888, 35.888), center=(16.300, 27.600, 1.279)
* 几何统计: Mesh=1, Vertices=56, Faces=44
* 子Mesh材质: /World/BoxOnConveyor_80/Meshes/Sketchfab_model/f49ad5edc352496894d3a02181012422_fbx/RootNode/Box072/Box072_06___Default_0/Box072_06___Default_0 -> 未绑定


---


### '/World/StackedCarton_1' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc
* BBox (world): size=(35.888, 35.888, 35.888), center=(-18.500, 29.250, 0.562)
* 几何统计: Mesh=1, Vertices=56, Faces=44
* 子Mesh材质: /World/StackedCarton_1/Meshes/Sketchfab_model/f49ad5edc352496894d3a02181012422_fbx/RootNode/Box072/Box072_06___Default_0/Box072_06___Default_0 -> 未绑定


---


### '/World/StackedCarton_2' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc
* BBox (world): size=(35.888, 35.888, 35.888), center=(-13.500, 29.250, 0.562)
* 几何统计: Mesh=1, Vertices=56, Faces=44
* 子Mesh材质: /World/StackedCarton_2/Meshes/Sketchfab_model/f49ad5edc352496894d3a02181012422_fbx/RootNode/Box072/Box072_06___Default_0/Box072_06___Default_0 -> 未绑定


---


### '/World/StackedCarton_3' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc
* BBox (world): size=(35.888, 35.888, 35.888), center=(-8.500, 29.250, 0.562)
* 几何统计: Mesh=1, Vertices=56, Faces=44
* 子Mesh材质: /World/StackedCarton_3/Meshes/Sketchfab_model/f49ad5edc352496894d3a02181012422_fbx/RootNode/Box072/Box072_06___Default_0/Box072_06___Default_0 -> 未绑定


---


### '/World/StackedCarton_4' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc
* BBox (world): size=(35.888, 35.888, 35.888), center=(-3.500, 29.250, 0.562)
* 几何统计: Mesh=1, Vertices=56, Faces=44
* 子Mesh材质: /World/StackedCarton_4/Meshes/Sketchfab_model/f49ad5edc352496894d3a02181012422_fbx/RootNode/Box072/Box072_06___Default_0/Box072_06___Default_0 -> 未绑定


---


### '/World/StackedCarton_5' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc
* BBox (world): size=(35.888, 35.888, 35.888), center=(1.500, 29.250, 0.562)
* 几何统计: Mesh=1, Vertices=56, Faces=44
* 子Mesh材质: /World/StackedCarton_5/Meshes/Sketchfab_model/f49ad5edc352496894d3a02181012422_fbx/RootNode/Box072/Box072_06___Default_0/Box072_06___Default_0 -> 未绑定


---


### '/World/StackedCarton_6' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc
* BBox (world): size=(35.888, 35.888, 35.888), center=(6.500, 29.250, 0.562)
* 几何统计: Mesh=1, Vertices=56, Faces=44
* 子Mesh材质: /World/StackedCarton_6/Meshes/Sketchfab_model/f49ad5edc352496894d3a02181012422_fbx/RootNode/Box072/Box072_06___Default_0/Box072_06___Default_0 -> 未绑定


---


### '/World/StackedCarton_7' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc
* BBox (world): size=(35.888, 35.888, 35.888), center=(11.500, 29.250, 0.562)
* 几何统计: Mesh=1, Vertices=56, Faces=44
* 子Mesh材质: /World/StackedCarton_7/Meshes/Sketchfab_model/f49ad5edc352496894d3a02181012422_fbx/RootNode/Box072/Box072_06___Default_0/Box072_06___Default_0 -> 未绑定


---


### '/World/StackedCarton_8' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc
* BBox (world): size=(35.888, 35.888, 35.888), center=(16.500, 29.250, 0.562)
* 几何统计: Mesh=1, Vertices=56, Faces=44
* 子Mesh材质: /World/StackedCarton_8/Meshes/Sketchfab_model/f49ad5edc352496894d3a02181012422_fbx/RootNode/Box072/Box072_06___Default_0/Box072_06___Default_0 -> 未绑定


---


### '/World/StackedCarton1_1' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc
* BBox (world): size=(35.888, 35.888, 35.888), center=(-18.900, 29.250, 0.562)
* 几何统计: Mesh=1, Vertices=56, Faces=44
* 子Mesh材质: /World/StackedCarton1_1/Meshes/Sketchfab_model/f49ad5edc352496894d3a02181012422_fbx/RootNode/Box072/Box072_06___Default_0/Box072_06___Default_0 -> 未绑定


---


### '/World/StackedCarton1_2' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc
* BBox (world): size=(35.888, 35.888, 35.888), center=(-13.900, 29.250, 0.562)
* 几何统计: Mesh=1, Vertices=56, Faces=44
* 子Mesh材质: /World/StackedCarton1_2/Meshes/Sketchfab_model/f49ad5edc352496894d3a02181012422_fbx/RootNode/Box072/Box072_06___Default_0/Box072_06___Default_0 -> 未绑定


---


### '/World/StackedCarton1_3' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc
* BBox (world): size=(35.888, 35.888, 35.888), center=(-8.900, 29.250, 0.562)
* 几何统计: Mesh=1, Vertices=56, Faces=44
* 子Mesh材质: /World/StackedCarton1_3/Meshes/Sketchfab_model/f49ad5edc352496894d3a02181012422_fbx/RootNode/Box072/Box072_06___Default_0/Box072_06___Default_0 -> 未绑定


---


### '/World/StackedCarton1_4' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc
* BBox (world): size=(35.888, 35.888, 35.888), center=(-3.900, 29.250, 0.562)
* 几何统计: Mesh=1, Vertices=56, Faces=44
* 子Mesh材质: /World/StackedCarton1_4/Meshes/Sketchfab_model/f49ad5edc352496894d3a02181012422_fbx/RootNode/Box072/Box072_06___Default_0/Box072_06___Default_0 -> 未绑定


---


### '/World/StackedCarton1_5' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc
* BBox (world): size=(35.888, 35.888, 35.888), center=(1.100, 29.250, 0.562)
* 几何统计: Mesh=1, Vertices=56, Faces=44
* 子Mesh材质: /World/StackedCarton1_5/Meshes/Sketchfab_model/f49ad5edc352496894d3a02181012422_fbx/RootNode/Box072/Box072_06___Default_0/Box072_06___Default_0 -> 未绑定


---


### '/World/StackedCarton1_6' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc
* BBox (world): size=(35.888, 35.888, 35.888), center=(6.100, 29.250, 0.562)
* 几何统计: Mesh=1, Vertices=56, Faces=44
* 子Mesh材质: /World/StackedCarton1_6/Meshes/Sketchfab_model/f49ad5edc352496894d3a02181012422_fbx/RootNode/Box072/Box072_06___Default_0/Box072_06___Default_0 -> 未绑定


---


### '/World/StackedCarton1_7' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc
* BBox (world): size=(35.888, 35.888, 35.888), center=(11.100, 29.250, 0.562)
* 几何统计: Mesh=1, Vertices=56, Faces=44
* 子Mesh材质: /World/StackedCarton1_7/Meshes/Sketchfab_model/f49ad5edc352496894d3a02181012422_fbx/RootNode/Box072/Box072_06___Default_0/Box072_06___Default_0 -> 未绑定


---


### '/World/StackedCarton1_8' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc
* BBox (world): size=(35.888, 35.888, 35.888), center=(16.100, 29.250, 0.562)
* 几何统计: Mesh=1, Vertices=56, Faces=44
* 子Mesh材质: /World/StackedCarton1_8/Meshes/Sketchfab_model/f49ad5edc352496894d3a02181012422_fbx/RootNode/Box072/Box072_06___Default_0/Box072_06___Default_0 -> 未绑定


---


### '/World/StackedCarton2_1' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc
* BBox (world): size=(35.888, 35.888, 35.888), center=(-18.700, 29.250, 0.919)
* 几何统计: Mesh=1, Vertices=56, Faces=44
* 子Mesh材质: /World/StackedCarton2_1/Meshes/Sketchfab_model/f49ad5edc352496894d3a02181012422_fbx/RootNode/Box072/Box072_06___Default_0/Box072_06___Default_0 -> 未绑定


---


### '/World/StackedCarton2_2' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc
* BBox (world): size=(35.888, 35.888, 35.888), center=(-13.700, 29.250, 0.919)
* 几何统计: Mesh=1, Vertices=56, Faces=44
* 子Mesh材质: /World/StackedCarton2_2/Meshes/Sketchfab_model/f49ad5edc352496894d3a02181012422_fbx/RootNode/Box072/Box072_06___Default_0/Box072_06___Default_0 -> 未绑定


---


### '/World/StackedCarton2_3' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc
* BBox (world): size=(35.888, 35.888, 35.888), center=(-8.700, 29.250, 0.919)
* 几何统计: Mesh=1, Vertices=56, Faces=44
* 子Mesh材质: /World/StackedCarton2_3/Meshes/Sketchfab_model/f49ad5edc352496894d3a02181012422_fbx/RootNode/Box072/Box072_06___Default_0/Box072_06___Default_0 -> 未绑定


---


### '/World/StackedCarton2_4' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc
* BBox (world): size=(35.888, 35.888, 35.888), center=(-3.700, 29.250, 0.919)
* 几何统计: Mesh=1, Vertices=56, Faces=44
* 子Mesh材质: /World/StackedCarton2_4/Meshes/Sketchfab_model/f49ad5edc352496894d3a02181012422_fbx/RootNode/Box072/Box072_06___Default_0/Box072_06___Default_0 -> 未绑定


---


### '/World/StackedCarton2_5' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc
* BBox (world): size=(35.888, 35.888, 35.888), center=(1.300, 29.250, 0.919)
* 几何统计: Mesh=1, Vertices=56, Faces=44
* 子Mesh材质: /World/StackedCarton2_5/Meshes/Sketchfab_model/f49ad5edc352496894d3a02181012422_fbx/RootNode/Box072/Box072_06___Default_0/Box072_06___Default_0 -> 未绑定


---


### '/World/StackedCarton2_6' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc
* BBox (world): size=(35.888, 35.888, 35.888), center=(6.300, 29.250, 0.919)
* 几何统计: Mesh=1, Vertices=56, Faces=44
* 子Mesh材质: /World/StackedCarton2_6/Meshes/Sketchfab_model/f49ad5edc352496894d3a02181012422_fbx/RootNode/Box072/Box072_06___Default_0/Box072_06___Default_0 -> 未绑定


---


### '/World/StackedCarton2_7' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc
* BBox (world): size=(35.888, 35.888, 35.888), center=(11.300, 29.250, 0.919)
* 几何统计: Mesh=1, Vertices=56, Faces=44
* 子Mesh材质: /World/StackedCarton2_7/Meshes/Sketchfab_model/f49ad5edc352496894d3a02181012422_fbx/RootNode/Box072/Box072_06___Default_0/Box072_06___Default_0 -> 未绑定


---


### '/World/StackedCarton2_8' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc
* BBox (world): size=(35.888, 35.888, 35.888), center=(16.300, 29.250, 0.919)
* 几何统计: Mesh=1, Vertices=56, Faces=44
* 子Mesh材质: /World/StackedCarton2_8/Meshes/Sketchfab_model/f49ad5edc352496894d3a02181012422_fbx/RootNode/Box072/Box072_06___Default_0/Box072_06___Default_0 -> 未绑定


---


### '/World/model_desk008' (Xform)
* 引用: payload:../device_data/usdz/Workbench/model_desk008.usdz
* BBox (world): size=(1.969, 0.959, 0.655), center=(17.323, 27.806, 0.482)
* 几何统计: Mesh=10, Vertices=815281, Faces=305170
* 子Mesh材质: /World/model_desk008/E_table_1/E_leg_2/P_fb8b1935d6745084 -> /World/model_desk008/materials/mat_10782663, /World/model_desk008/E_table_1/E_cabinet_3/P_d903d9aeeb215084 -> /World/model_desk008/materials/mat_10782663, /World/model_desk008/E_table_1/E_cabinet_3/P_644a7b35134a084 -> /World/model_desk008/materials/mat_10782673, /World/model_desk008/E_table_1/E_tabletop_4/P_76c05a9963150084 -> /World/model_desk008/materials/mat_10782673, /World/model_desk008/E_drawer_5/P_9b591a0a5294a084 -> /World/model_desk008/materials/mat_10782839, /World/model_desk008/E_drawer_5/P_b5fc1b49d1858784 -> /World/model_desk008/materials/mat_10782842, /World/model_desk008/E_drawer_6/P_c45acc40a35b2084 -> /World/model_desk008/materials/mat_10782839, /World/model_desk008/E_drawer_6/P_6dd5c29b55f96c84 -> /World/model_desk008/materials/mat_10782842, /World/model_desk008/E_drawer_7/P_a37d90f1fd08a084 -> /World/model_desk008/materials/mat_10782839, /World/model_desk008/E_drawer_7/P_9b2777dbd9d2c084 -> /World/model_desk008/materials/mat_10782842
* 材质摘要:
 * /World/model_desk008/materials/mat_10782663 -> Inputs: 'clearcoat=0.05', 'clearcoatRoughness=0.05', 'diffuseColor=(0.515, 0.515, 0.515)', 'emissiveColor=(0.000, 0.000, 0.000)', 'ior=1', 'metallic=0.12', 'opacity=1', 'roughness=0.09', 'specularColor=(0.000, 0.000, 0.000)'
 * /World/model_desk008/materials/mat_10782673 -> Inputs: 'clearcoat=0.05', 'clearcoatRoughness=0.05', 'emissiveColor=(0.000, 0.000, 0.000)', 'ior=1', 'metallic=0.17', 'opacity=1', 'roughness=0.12', 'specularColor=(0.000, 0.000, 0.000)', 'rotation=0', 'scale=(39.370, 39.370)', 'translation=(0.000, 0.000)', Textures: '0/0a01a4f7d6ec62fdb62fdd571ea34f89.png'
 * /World/model_desk008/materials/mat_10782839 -> Inputs: 'clearcoat=0.05', 'clearcoatRoughness=0.05', 'diffuseColor=(0.497, 0.451, 0.413)', 'emissiveColor=(0.000, 0.000, 0.000)', 'ior=1', 'metallic=0.16', 'opacity=1', 'roughness=0.14', 'specularColor=(0.000, 0.000, 0.000)'
 * /World/model_desk008/materials/mat_10782842 -> Inputs: 'clearcoat=0.05', 'clearcoatRoughness=0.05', 'diffuseColor=(0.913, 0.913, 0.913)', 'emissiveColor=(0.000, 0.000, 0.000)', 'ior=1', 'metallic=0.14', 'opacity=1', 'roughness=0.09', 'specularColor=(0.000, 0.000, 0.000)'


---


### '/World/INDUSTRIAL_ROBOTIC_ARM' (Xform)
* 引用: payload:../device_data/usdz/IndustrialRobot/INDUSTRIAL_ROBOTIC_ARM.usdz
* BBox (world): size=(78.095, 126.534, 112.695), center=(17.321, 27.961, 1.423)
* 几何统计: Mesh=38, Vertices=45024, Faces=53168
* 子Mesh材质: /World/INDUSTRIAL_ROBOTIC_ARM/Meshes/Sketchfab_model/c87c2a6ebd5447f7ac496076c3c610d3_fbx/RootNode/PDM_INDUSTRIAL_ROBOTIC_ARM_PROJECT_v84/Component_1_Base_1/Component_1_Base/Component2_1/Component2/Body1/Body1_Brass___Polished_0/Body1_Brass___Polished_0 -> 未绑定, /World/INDUSTRIAL_ROBOTIC_ARM/Meshes/Sketchfab_model/c87c2a6ebd5447f7ac496076c3c610d3_fbx/RootNode/PDM_INDUSTRIAL_ROBOTIC_ARM_PROJECT_v84/Component_1_Base_1/Component_1_Base/Component24_1/Component24/Body1/Body1_Aluminum___Anodized_Glossy__Grey__0/Body1_Aluminum___Anodized_Glossy__Grey__0 -> 未绑定, /World/INDUSTRIAL_ROBOTIC_ARM/Meshes/Sketchfab_model/c87c2a6ebd5447f7ac496076c3c610d3_fbx/RootNode/PDM_INDUSTRIAL_ROBOTIC_ARM_PROJECT_v84/Component_1_Base_1/Component_1_Base/Component25_1/Component25/Body1/Body1_Aluminum___Anodized_Glossy__Grey__0/Body1_Aluminum___Anodized_Glossy__Grey__0 -> 未绑定, /World/INDUSTRIAL_ROBOTIC_ARM/Meshes/Sketchfab_model/c87c2a6ebd5447f7ac496076c3c610d3_fbx/RootNode/PDM_INDUSTRIAL_ROBOTIC_ARM_PROJECT_v84/Component_1_Base_1/Component_1_Base/Component26_1/Component26/Body1/Body1_Aluminum___Anodized_Glossy__Grey__0/Body1_Aluminum___Anodized_Glossy__Grey__0 -> 未绑定, /World/INDUSTRIAL_ROBOTIC_ARM/Meshes/Sketchfab_model/c87c2a6ebd5447f7ac496076c3c610d3_fbx/RootNode/PDM_INDUSTRIAL_ROBOTIC_ARM_PROJECT_v84/Component_1_Base_1/Component_1_Base/Component27_1/Component27/Body1/Body1_Aluminum___Anodized_Glossy__Grey__0/Body1_Aluminum___Anodized_Glossy__Grey__0 -> 未绑定, /World/INDUSTRIAL_ROBOTIC_ARM/Meshes/Sketchfab_model/c87c2a6ebd5447f7ac496076c3c610d3_fbx/RootNode/PDM_INDUSTRIAL_ROBOTIC_ARM_PROJECT_v84/Component_1_Base_1/Component_1_Base/Component28_1/Component28/Body1/Body1_Brass___Polished_0/Body1_Brass___Polished_0 -> 未绑定, /World/INDUSTRIAL_ROBOTIC_ARM/Meshes/Sketchfab_model/c87c2a6ebd5447f7ac496076c3c610d3_fbx/RootNode/PDM_INDUSTRIAL_ROBOTIC_ARM_PROJECT_v84/Component_2_Jaw_1_1/Component_2_Jaw_1/Component4_1/Component4/Body1/Body1_Aluminum___Anodized_Glossy__Grey__0/Body1_Aluminum___Anodized_Glossy__Grey__0 -> 未绑定, /World/INDUSTRIAL_ROBOTIC_ARM/Meshes/Sketchfab_model/c87c2a6ebd5447f7ac496076c3c610d3_fbx/RootNode/PDM_INDUSTRIAL_ROBOTIC_ARM_PROJECT_v84/Component_2_Jaw_1_1/Component_2_Jaw_1/Component17_1/Component17/Body1/Body1_Brass___Polished_0/Body1_Brass___Polished_0 -> 未绑定, /World/INDUSTRIAL_ROBOTIC_ARM/Meshes/Sketchfab_model/c87c2a6ebd5447f7ac496076c3c610d3_fbx/RootNode/PDM_INDUSTRIAL_ROBOTIC_ARM_PROJECT_v84/Component_3_Jaw_2_1/Component_3_Jaw_2/Component6_1/Component6/Body1/Body1_Paint___Enamel_Glossy__Yellow__0/Body1_Paint___Enamel_Glossy__Yellow__0 -> 未绑定, /World/INDUSTRIAL_ROBOTIC_ARM/Meshes/Sketchfab_model/c87c2a6ebd5447f7ac496076c3c610d3_fbx/RootNode/PDM_INDUSTRIAL_ROBOTIC_ARM_PROJECT_v84/Component_3_Jaw_2_1/Component_3_Jaw_2/Component6_1/Component6/Body1/Body1__0/Body1__0 -> 未绑定, /World/INDUSTRIAL_ROBOTIC_ARM/Meshes/Sketchfab_model/c87c2a6ebd5447f7ac496076c3c610d3_fbx/RootNode/PDM_INDUSTRIAL_ROBOTIC_ARM_PROJECT_v84/Component_3_Jaw_2_1/Component_3_Jaw_2/Component29_1/Component29/Body1/Body1_Aluminum___Anodized_Glossy__Grey__0/Body1_Aluminum___Anodized_Glossy__Grey__0 -> 未绑定, /World/INDUSTRIAL_ROBOTIC_ARM/Meshes/Sketchfab_model/c87c2a6ebd5447f7ac496076c3c610d3_fbx/RootNode/PDM_INDUSTRIAL_ROBOTIC_ARM_PROJECT_v84/Component_3_Jaw_2_1/Component_3_Jaw_2/Component30_1/Component30/Body1/Body1_Steel___Satin_0/Body1_Steel___Satin_0 -> 未绑定, /World/INDUSTRIAL_ROBOTIC_ARM/Meshes/Sketchfab_model/c87c2a6ebd5447f7ac496076c3c610d3_fbx/RootNode/PDM_INDUSTRIAL_ROBOTIC_ARM_PROJECT_v84/Component_3_Jaw_2_1/Component_3_Jaw_2/Component31_1/Component31/Body1/Body1_Steel___Satin_0/Body1_Steel___Satin_0 -> 未绑定, /World/INDUSTRIAL_ROBOTIC_ARM/Meshes/Sketchfab_model/c87c2a6ebd5447f7ac496076c3c610d3_fbx/RootNode/PDM_INDUSTRIAL_ROBOTIC_ARM_PROJECT_v84/Component_3_Jaw_2_1/Component_3_Jaw_2/Component32_1/Component32/Body1/Body1_Steel___Satin_0/Body1_Steel___Satin_0 -> 未绑定, /World/INDUSTRIAL_ROBOTIC_ARM/Meshes/Sketchfab_model/c87c2a6ebd5447f7ac496076c3c610d3_fbx/RootNode/PDM_INDUSTRIAL_ROBOTIC_ARM_PROJECT_v84/Component_3_Jaw_2_1/Component_3_Jaw_2/Component33_1/Component33/Body1/Body1_Steel___Satin_0/Body1_Steel___Satin_0 -> 未绑定, /World/INDUSTRIAL_ROBOTIC_ARM/Meshes/Sketchfab_model/c87c2a6ebd5447f7ac496076c3c610d3_fbx/RootNode/PDM_INDUSTRIAL_ROBOTIC_ARM_PROJECT_v84/Component_3_Jaw_2_1/Component_3_Jaw_2/Component34_1/Component34/Body1/Body1_Steel___Satin_0/Body1_Steel___Satin_0 -> 未绑定, /World/INDUSTRIAL_ROBOTIC_ARM/Meshes/Sketchfab_model/c87c2a6ebd5447f7ac496076c3c610d3_fbx/RootNode/PDM_INDUSTRIAL_ROBOTIC_ARM_PROJECT_v84/Component_3_Jaw_2_1/Component_3_Jaw_2/Component35_1/Component35/Body1/Body1_Steel___Satin_0/Body1_Steel___Satin_0 -> 未绑定, /World/INDUSTRIAL_ROBOTIC_ARM/Meshes/Sketchfab_model/c87c2a6ebd5447f7ac496076c3c610d3_fbx/RootNode/PDM_INDUSTRIAL_ROBOTIC_ARM_PROJECT_v84/Component_3_Jaw_2_1/Component_3_Jaw_2/Component36_1/Component36/Body1/Body1_Steel___Satin_0/Body1_Steel___Satin_0 -> 未绑定, /World/INDUSTRIAL_ROBOTIC_ARM/Meshes/Sketchfab_model/c87c2a6ebd5447f7ac496076c3c610d3_fbx/RootNode/PDM_INDUSTRIAL_ROBOTIC_ARM_PROJECT_v84/Component_3_Jaw_2_1/Component_3_Jaw_2/Component37_1/Component37/Body1/Body1_Steel___Satin_0/Body1_Steel___Satin_0 -> 未绑定, /World/INDUSTRIAL_ROBOTIC_ARM/Meshes/Sketchfab_model/c87c2a6ebd5447f7ac496076c3c610d3_fbx/RootNode/PDM_INDUSTRIAL_ROBOTIC_ARM_PROJECT_v84/Component_3_Jaw_2_1/Component_3_Jaw_2/Component38_1/Component38/Body1/Body1_Steel___Satin_0/Body1_Steel___Satin_0 -> 未绑定, /World/INDUSTRIAL_ROBOTIC_ARM/Meshes/Sketchfab_model/c87c2a6ebd5447f7ac496076c3c610d3_fbx/RootNode/PDM_INDUSTRIAL_ROBOTIC_ARM_PROJECT_v84/Component_3_Jaw_2_1/Component_3_Jaw_2/Component39_1/Component39/Body1/Body1_Steel___Satin_0/Body1_Steel___Satin_0 -> 未绑定, /World/INDUSTRIAL_ROBOTIC_ARM/Meshes/Sketchfab_model/c87c2a6ebd5447f7ac496076c3c610d3_fbx/RootNode/PDM_INDUSTRIAL_ROBOTIC_ARM_PROJECT_v84/Component_3_Jaw_2_1/Component_3_Jaw_2/Component40_1/Component40/Body1/Body1_Steel___Satin_0/Body1_Steel___Satin_0 -> 未绑定, /World/INDUSTRIAL_ROBOTIC_ARM/Meshes/Sketchfab_model/c87c2a6ebd5447f7ac496076c3c610d3_fbx/RootNode/PDM_INDUSTRIAL_ROBOTIC_ARM_PROJECT_v84/Component_3_Jaw_2_1/Component_3_Jaw_2/Component41_1/Component41/Body1/Body1_Steel___Satin_0/Body1_Steel___Satin_0 -> 未绑定, /World/INDUSTRIAL_ROBOTIC_ARM/Meshes/Sketchfab_model/c87c2a6ebd5447f7ac496076c3c610d3_fbx/RootNode/PDM_INDUSTRIAL_ROBOTIC_ARM_PROJECT_v84/Component_3_Jaw_2_1/Component_3_Jaw_2/Component42_1/Component42/Body1/Body1_Steel___Satin_0/Body1_Steel___Satin_0 -> 未绑定, /World/INDUSTRIAL_ROBOTIC_ARM/Meshes/Sketchfab_model/c87c2a6ebd5447f7ac496076c3c610d3_fbx/RootNode/PDM_INDUSTRIAL_ROBOTIC_ARM_PROJECT_v84/Component_4_Jaw_3_1/Component_4_Jaw_3/Component8_1/Component8/Body1/Body1_Brass___Polished_0/Body1_Brass___Polished_0 -> 未绑定, /World/INDUSTRIAL_ROBOTIC_ARM/Meshes/Sketchfab_model/c87c2a6ebd5447f7ac496076c3c610d3_fbx/RootNode/PDM_INDUSTRIAL_ROBOTIC_ARM_PROJECT_v84/Component_4_Jaw_3_1/Component_4_Jaw_3/Component22_1/Component22/Body1/Body1_Brass___Polished_0/Body1_Brass___Polished_0 -> 未绑定, /World/INDUSTRIAL_ROBOTIC_ARM/Meshes/Sketchfab_model/c87c2a6ebd5447f7ac496076c3c610d3_fbx/RootNode/PDM_INDUSTRIAL_ROBOTIC_ARM_PROJECT_v84/Component_4_Jaw_3_1/Component_4_Jaw_3/Component23_1/Component23/Body1/Body1_Brass___Polished_0/Body1_Brass___Polished_0 -> 未绑定, /World/INDUSTRIAL_ROBOTIC_ARM/Meshes/Sketchfab_model/c87c2a6ebd5447f7ac496076c3c610d3_fbx/RootNode/PDM_INDUSTRIAL_ROBOTIC_ARM_PROJECT_v84/Component_5_Jaw_4_1/Component_5_Jaw_4/Component10_1/Component10/Body1/Body1_Paint___Enamel_Glossy__Black__0/Body1_Paint___Enamel_Glossy__Black__0 -> 未绑定, /World/INDUSTRIAL_ROBOTIC_ARM/Meshes/Sketchfab_model/c87c2a6ebd5447f7ac496076c3c610d3_fbx/RootNode/PDM_INDUSTRIAL_ROBOTIC_ARM_PROJECT_v84/Component_5_Jaw_4_1/Component_5_Jaw_4/Component10_1/Component10/Body1/Body1__0/Body1__0 -> 未绑定, /World/INDUSTRIAL_ROBOTIC_ARM/Meshes/Sketchfab_model/c87c2a6ebd5447f7ac496076c3c610d3_fbx/RootNode/PDM_INDUSTRIAL_ROBOTIC_ARM_PROJECT_v84/Component_5_Jaw_4_1/Component_5_Jaw_4/Component20_1/Component20/Body1/Body1_Aluminum___Anodized_Glossy__Grey__0/Body1_Aluminum___Anodized_Glossy__Grey__0 -> 未绑定, /World/INDUSTRIAL_ROBOTIC_ARM/Meshes/Sketchfab_model/c87c2a6ebd5447f7ac496076c3c610d3_fbx/RootNode/PDM_INDUSTRIAL_ROBOTIC_ARM_PROJECT_v84/Component_5_Jaw_4_1/Component_5_Jaw_4/Component21_1/Component21/Body1/Body1_Steel___Satin_0/Body1_Steel___Satin_0 -> 未绑定, /World/INDUSTRIAL_ROBOTIC_ARM/Meshes/Sketchfab_model/c87c2a6ebd5447f7ac496076c3c610d3_fbx/RootNode/PDM_INDUSTRIAL_ROBOTIC_ARM_PROJECT_v84/Component_6_Jaw_5_1/Component_6_Jaw_5/Component12_1/Component12/Body1/Body1_Brass___Polished_0/Body1_Brass___Polished_0 -> 未绑定, /World/INDUSTRIAL_ROBOTIC_ARM/Meshes/Sketchfab_model/c87c2a6ebd5447f7ac496076c3c610d3_fbx/RootNode/PDM_INDUSTRIAL_ROBOTIC_ARM_PROJECT_v84/Component_6_Jaw_5_1/Component_6_Jaw_5/Component18_1/Component18/Body1/Body1_Brass___Polished_0/Body1_Brass___Polished_0 -> 未绑定, /World/INDUSTRIAL_ROBOTIC_ARM/Meshes/Sketchfab_model/c87c2a6ebd5447f7ac496076c3c610d3_fbx/RootNode/PDM_INDUSTRIAL_ROBOTIC_ARM_PROJECT_v84/Component_6_Jaw_5_1/Component_6_Jaw_5/Component19_1/Component19/Body1/Body1_Paint___Enamel_Glossy__Yellow__0/Body1_Paint___Enamel_Glossy__Yellow__0 -> 未绑定, /World/INDUSTRIAL_ROBOTIC_ARM/Meshes/Sketchfab_model/c87c2a6ebd5447f7ac496076c3c610d3_fbx/RootNode/PDM_INDUSTRIAL_ROBOTIC_ARM_PROJECT_v84/Component_7_Jaw_6_1/Component_7_Jaw_6/Component14_1/Component14/Body1/Body1_Brass___Polished_0/Body1_Brass___Polished_0 -> 未绑定, /World/INDUSTRIAL_ROBOTIC_ARM/Meshes/Sketchfab_model/c87c2a6ebd5447f7ac496076c3c610d3_fbx/RootNode/PDM_INDUSTRIAL_ROBOTIC_ARM_PROJECT_v84/Component_7_Jaw_6_1/Component_7_Jaw_6/Component43_1/Component43/Body1/Body1_Aluminum___Anodized_Glossy__Grey__0/Body1_Aluminum___Anodized_Glossy__Grey__0 -> 未绑定, /World/INDUSTRIAL_ROBOTIC_ARM/Meshes/Sketchfab_model/c87c2a6ebd5447f7ac496076c3c610d3_fbx/RootNode/PDM_INDUSTRIAL_ROBOTIC_ARM_PROJECT_v84/Component_8_Jaw_7_1/Component_8_Jaw_7/Component16_1/Component16/Body1/Body1_Aluminum___Anodized_Glossy__Grey__0/Body1_Aluminum___Anodized_Glossy__Grey__0 -> 未绑定, /World/INDUSTRIAL_ROBOTIC_ARM/Meshes/Sketchfab_model/c87c2a6ebd5447f7ac496076c3c610d3_fbx/RootNode/PDM_INDUSTRIAL_ROBOTIC_ARM_PROJECT_v84/Component_8_Jaw_7_1/Component_8_Jaw_7/Component16_2/Component16/Body1/Body1_Aluminum___Anodized_Glossy__Grey__0/Body1_Aluminum___Anodized_Glossy__Grey__0 -> 未绑定


---


### '/World/processed_Robotic_Manipulator_low_poly' (Xform)
* 引用: payload:../device_data/usdz/IndustrialRobot/processed_Robotic_Manipulator_low_poly.usdz
* BBox (world): size=(117.387, 95.149, 72.734), center=(15.617, 28.476, 1.285)
* 几何统计: Mesh=16, Vertices=4239, Faces=4548
* 子Mesh材质: /World/processed_Robotic_Manipulator_low_poly/Meshes/Sketchfab_model/Collada_visual_scene_group/Robotic_hand_018_low/defaultMaterial/defaultMaterial -> 未绑定, /World/processed_Robotic_Manipulator_low_poly/Meshes/Sketchfab_model/Collada_visual_scene_group/Robotic_hand_016_low/defaultMaterial/defaultMaterial -> 未绑定, /World/processed_Robotic_Manipulator_low_poly/Meshes/Sketchfab_model/Collada_visual_scene_group/Robotic_hand_015_low/defaultMaterial/defaultMaterial -> 未绑定, /World/processed_Robotic_Manipulator_low_poly/Meshes/Sketchfab_model/Collada_visual_scene_group/Robotic_hand_017_low/defaultMaterial/defaultMaterial -> 未绑定, /World/processed_Robotic_Manipulator_low_poly/Meshes/Sketchfab_model/Collada_visual_scene_group/Robotic_hand_014_low/defaultMaterial/defaultMaterial -> 未绑定, /World/processed_Robotic_Manipulator_low_poly/Meshes/Sketchfab_model/Collada_visual_scene_group/Robotic_hand_013_low/defaultMaterial/defaultMaterial -> 未绑定, /World/processed_Robotic_Manipulator_low_poly/Meshes/Sketchfab_model/Collada_visual_scene_group/Robotic_hand_012_low/defaultMaterial/defaultMaterial -> 未绑定, /World/processed_Robotic_Manipulator_low_poly/Meshes/Sketchfab_model/Collada_visual_scene_group/Robotic_hand_011_low/defaultMaterial/defaultMaterial -> 未绑定, /World/processed_Robotic_Manipulator_low_poly/Meshes/Sketchfab_model/Collada_visual_scene_group/Robotic_hand_010_low/defaultMaterial/defaultMaterial -> 未绑定, /World/processed_Robotic_Manipulator_low_poly/Meshes/Sketchfab_model/Collada_visual_scene_group/Robotic_hand_009_low/defaultMaterial/defaultMaterial -> 未绑定, /World/processed_Robotic_Manipulator_low_poly/Meshes/Sketchfab_model/Collada_visual_scene_group/Robotic_hand_008_low/defaultMaterial/defaultMaterial -> 未绑定, /World/processed_Robotic_Manipulator_low_poly/Meshes/Sketchfab_model/Collada_visual_scene_group/Robotic_hand_007_low/defaultMaterial/defaultMaterial -> 未绑定, /World/processed_Robotic_Manipulator_low_poly/Meshes/Sketchfab_model/Collada_visual_scene_group/Robotic_hand_006_low/defaultMaterial/defaultMaterial -> 未绑定, /World/processed_Robotic_Manipulator_low_poly/Meshes/Sketchfab_model/Collada_visual_scene_group/Robotic_hand_005_low/defaultMaterial/defaultMaterial -> 未绑定, /World/processed_Robotic_Manipulator_low_poly/Meshes/Sketchfab_model/Collada_visual_scene_group/Robotic_hand_004_low/defaultMaterial/defaultMaterial -> 未绑定, /World/processed_Robotic_Manipulator_low_poly/Meshes/Sketchfab_model/Collada_visual_scene_group/Robotic_hand_003_low/defaultMaterial/defaultMaterial -> 未绑定


---
