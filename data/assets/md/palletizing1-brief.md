# USDA场景描述文档:palletizing1.usda

## 1.场景元数据(Scene Metadata)
*  **USDA文件路径(USDA File Path):**`/media/simple/another_Documents/isaacsim_assets/scenedata/palletizing1.usda`
*  **默认Prim (Default Prim):**'Not Set'
*  **单位与坐标系 (Units & Coordinate System):**
   *   **米(Meters Per Unit):**1.0
   *   **Up Axis:**Z

## 2.场景对象层级(Scene Hierarchy)
*   World (Prim)
    *   DomeLight (DomeLight)
    *   SunLight (DistantLight)
    *   IndoorLight (SphereLight)
    *   Ground (Xform)
        *   geom (Mesh)
        *   collisionPlane (Plane)
    *   Physics_Materials (Prim)
        *   physics_material (Material)
    *   Looks (Prim)
        *   visual_material (Material)
            *   shader (Shader)
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
    *   RobotArm_1 (Xform)
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
    *   RobotArm_2 (Xform)
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
    *   RobotArm_3 (Xform)
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
    *   RobotArm_4 (Xform)
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
    *   RobotArm_5 (Xform)
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
    *   RobotArm_6 (Xform)
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
    *   RobotArm_7 (Xform)
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
    *   RobotArm_8 (Xform)
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
    *   agv_1 (Xform)
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
    *   agv_2 (Xform)
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
    *   agv_3 (Xform)
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
    *   agv_4 (Xform)
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
    *   agv_5 (Xform)
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
    *   agv_6 (Xform)
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
    *   agv_7 (Xform)
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
    *   agv_8 (Xform)
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
    *   Conveyor_1 (Xform)
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
    *   Conveyor_2 (Xform)
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
    *   Conveyor_3 (Xform)
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
    *   Conveyor_4 (Xform)
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
    *   Conveyor_5 (Xform)
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
    *   Conveyor_6 (Xform)
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
    *   Conveyor_7 (Xform)
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
    *   Conveyor_8 (Xform)
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
    *   BoxOnConveyor_1_1 (Xform)
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
    *   BoxOnConveyor_1_2 (Xform)
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
    *   BoxOnConveyor_1_3 (Xform)
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
    *   BoxOnConveyor_1_4 (Xform)
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
    *   BoxOnConveyor_1_5 (Xform)
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
    *   BoxOnConveyor_1_6 (Xform)
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
    *   BoxOnConveyor_1_7 (Xform)
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
    *   BoxOnConveyor_1_8 (Xform)
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
    *   BoxOnConveyor_2_1 (Xform)
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
    *   BoxOnConveyor_2_2 (Xform)
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
    *   BoxOnConveyor_2_3 (Xform)
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
    *   BoxOnConveyor_2_4 (Xform)
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
    *   BoxOnConveyor_2_5 (Xform)
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
    *   BoxOnConveyor_2_6 (Xform)
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
    *   BoxOnConveyor_2_7 (Xform)
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
    *   BoxOnConveyor_2_8 (Xform)
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
    *   BoxOnConveyor_3_1 (Xform)
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
    *   BoxOnConveyor_3_2 (Xform)
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
    *   BoxOnConveyor_3_3 (Xform)
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
    *   BoxOnConveyor_3_4 (Xform)
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
    *   BoxOnConveyor_3_5 (Xform)
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
    *   BoxOnConveyor_3_6 (Xform)
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
    *   BoxOnConveyor_3_7 (Xform)
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
    *   BoxOnConveyor_3_8 (Xform)
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
    *   StackedCarton_1_1 (Xform)
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
    *   StackedCarton_1_2 (Xform)
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
    *   StackedCarton_1_3 (Xform)
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
    *   StackedCarton_1_4 (Xform)
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
    *   StackedCarton_1_5 (Xform)
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
    *   StackedCarton_1_6 (Xform)
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
    *   StackedCarton_1_7 (Xform)
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
    *   StackedCarton_1_8 (Xform)
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
    *   StackedCarton_2_1 (Xform)
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
    *   StackedCarton_2_2 (Xform)
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
    *   StackedCarton_2_3 (Xform)
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
    *   StackedCarton_2_4 (Xform)
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
    *   StackedCarton_2_5 (Xform)
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
    *   StackedCarton_2_6 (Xform)
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
    *   StackedCarton_2_7 (Xform)
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
    *   StackedCarton_2_8 (Xform)
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

## 3. 外部引用Xform简报(Referenced Xforms)

### '/World/factory' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/scene/factory/factory.usdc
* BBox (world): size=(49.139, 19.897, 67.754), center=(0.761, 0.769, 9.470)
* 几何统计: Mesh=7, Vertices=2044, Faces=946
* 子Mesh材质: /World/factory/Meshes/Sketchfab_model/cc020ec10d3e484ab6eb350963eb38d0_fbx/RootNode/Factory002/Factory002_WindowsIndustrial_frontSolid_OpenWindows_Mat_0/Factory002_WindowsIndustrial_frontSolid_OpenWindows_Mat_0 -> 未绑定, /World/factory/Meshes/Sketchfab_model/cc020ec10d3e484ab6eb350963eb38d0_fbx/RootNode/Factory002/Factory002_WindowsIndustrial_frontSolid_Mat_0/Factory002_WindowsIndustrial_frontSolid_Mat_0 -> 未绑定, /World/factory/Meshes/Sketchfab_model/cc020ec10d3e484ab6eb350963eb38d0_fbx/RootNode/Factory002/Factory002_WindowsIndustrial_frontDoorclosed_Mat_0/Factory002_WindowsIndustrial_frontDoorclosed_Mat_0 -> 未绑定, /World/factory/Meshes/Sketchfab_model/cc020ec10d3e484ab6eb350963eb38d0_fbx/RootNode/Factory002/Factory002_WindowsIndustrial_frontDoorOpen_Mat_0/Factory002_WindowsIndustrial_frontDoorOpen_Mat_0 -> 未绑定, /World/factory/Meshes/Sketchfab_model/cc020ec10d3e484ab6eb350963eb38d0_fbx/RootNode/Factory002/Factory002_WindowsIndustrial_front_Mat_0/Factory002_WindowsIndustrial_front_Mat_0 -> 未绑定, /World/factory/Meshes/Sketchfab_model/cc020ec10d3e484ab6eb350963eb38d0_fbx/RootNode/Factory002/Factory002_11___Default_0/Factory002_11___Default_0 -> 未绑定, /World/factory/Meshes/Sketchfab_model/cc020ec10d3e484ab6eb350963eb38d0_fbx/RootNode/Object001/Object001_20___Default_0/Object001_20___Default_0 -> 未绑定


---


### '/World/RobotArm_1' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/5.0/Isaac/IsaacLab/Robots/FrankaEmika/panda_instanceable1.usd
* BBox (world): size=(0.755, 0.583, 2.508), center=(-19.980, 30.000, 1.577)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm_1/Group/panda_hand/visuals' (Xform)
* 引用: reference:./Props/panda_hand.usd @/Root
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.063, 0.205, 0.092), center=(-19.815, 30.002, 2.361)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm_1/Group/panda_hand/collisions' (Xform)
* 引用: reference:./Props/instanceable_collision_meshes.usd @/panda_hand_collisions
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(-19.812, 30.000, 2.406)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm_1/Group/panda_leftfinger/visuals' (Xform)
* 引用: reference:./Props/panda_leftfinger.usd @/Root
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.021, 0.026, 0.054), center=(-19.791, 29.979, 2.214)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm_1/Group/panda_leftfinger/collisions' (Xform)
* 引用: reference:./Props/instanceable_collision_meshes.usd @/panda_leftfinger_collisions
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(-19.812, 30.000, 2.275)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm_1/Group/panda_link0/visuals' (Xform)
* 引用: reference:./Props/panda_link0.usd @/Root
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.226, 0.189, 0.140), center=(-20.103, 30.000, 0.480)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm_1/Group/panda_link0/collisions' (Xform)
* 引用: reference:./Props/instanceable_collision_meshes.usd @/panda_link0_collisions
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(-20.010, 30.000, 0.323)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm_1/Group/panda_link1/visuals' (Xform)
* 引用: reference:./Props/panda_link1.usd @/Root
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.110, 0.184, 0.247), center=(-20.010, 29.916, 0.918)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm_1/Group/panda_link1/collisions' (Xform)
* 引用: reference:./Props/instanceable_collision_meshes.usd @/panda_link1_collisions
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(-20.010, 30.000, 1.072)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm_1/Group/panda_link2/visuals' (Xform)
* 引用: reference:./Props/panda_link2.usd @/Root
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.110, 0.249, 0.184), center=(-20.010, 30.083, 1.228)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm_1/Group/panda_link2/collisions' (Xform)
* 引用: reference:./Props/instanceable_collision_meshes.usd @/panda_link2_collisions
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(-20.010, 30.000, 1.072)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm_1/Group/panda_link3/visuals' (Xform)
* 引用: reference:./Props/panda_link3.usd @/Root
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.193, 0.166, 0.176), center=(-19.917, 30.063, 1.709)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm_1/Group/panda_link3/collisions' (Xform)
* 引用: reference:./Props/instanceable_collision_meshes.usd @/panda_link3_collisions
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(-20.010, 30.000, 1.783)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm_1/Group/panda_link4/visuals' (Xform)
* 引用: reference:./Props/panda_link4.usd @/Root
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.193, 0.179, 0.166), center=(-19.917, 29.937, 1.861)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm_1/Group/panda_link4/collisions' (Xform)
* 引用: reference:./Props/instanceable_collision_meshes.usd @/panda_link4_collisions
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(-19.825, 30.000, 1.783)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm_1/Group/panda_link5/visuals' (Xform)
* 引用: reference:./Props/panda_link5.usd @/Root
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.110, 0.185, 0.311), center=(-20.010, 30.084, 2.414)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm_1/Group/panda_link5/collisions' (Xform)
* 引用: reference:./Props/instanceable_collision_meshes.usd @/panda_link5_collisions
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(-20.010, 30.000, 2.647)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm_1/Group/panda_link6/visuals' (Xform)
* 引用: reference:./Props/panda_link6.usd @/Root
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.180, 0.133, 0.100), center=(-19.916, 29.986, 2.681)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm_1/Group/panda_link6/collisions' (Xform)
* 引用: reference:./Props/instanceable_collision_meshes.usd @/panda_link6_collisions
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(-20.010, 30.000, 2.647)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm_1/Group/panda_link7/visuals' (Xform)
* 引用: reference:./Props/panda_link7.usd @/Root
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.125, 0.125, 0.055), center=(-19.770, 29.958, 2.468)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm_1/Group/panda_link7/collisions' (Xform)
* 引用: reference:./Props/instanceable_collision_meshes.usd @/panda_link7_collisions
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(-19.812, 30.000, 2.647)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm_1/Group/panda_rightfinger/visuals' (Xform)
* 引用: reference:./Props/panda_rightfinger.usd @/Root
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.021, 0.026, 0.054), center=(-19.833, 30.021, 2.214)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm_1/Group/panda_rightfinger/collisions' (Xform)
* 引用: reference:./Props/instanceable_collision_meshes.usd @/panda_rightfinger_collisions
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(-19.812, 30.000, 2.275)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm_2' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/5.0/Isaac/IsaacLab/Robots/FrankaEmika/panda_instanceable1.usd
* BBox (world): size=(0.755, 0.583, 2.508), center=(-14.980, 30.000, 1.577)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm_2/Group/panda_hand/visuals' (Xform)
* 引用: reference:./Props/panda_hand.usd @/Root
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.063, 0.205, 0.092), center=(-14.815, 30.002, 2.361)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm_2/Group/panda_hand/collisions' (Xform)
* 引用: reference:./Props/instanceable_collision_meshes.usd @/panda_hand_collisions
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(-14.812, 30.000, 2.406)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm_2/Group/panda_leftfinger/visuals' (Xform)
* 引用: reference:./Props/panda_leftfinger.usd @/Root
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.021, 0.026, 0.054), center=(-14.791, 29.979, 2.214)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm_2/Group/panda_leftfinger/collisions' (Xform)
* 引用: reference:./Props/instanceable_collision_meshes.usd @/panda_leftfinger_collisions
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(-14.812, 30.000, 2.275)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm_2/Group/panda_link0/visuals' (Xform)
* 引用: reference:./Props/panda_link0.usd @/Root
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.226, 0.189, 0.140), center=(-15.103, 30.000, 0.480)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm_2/Group/panda_link0/collisions' (Xform)
* 引用: reference:./Props/instanceable_collision_meshes.usd @/panda_link0_collisions
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(-15.010, 30.000, 0.323)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm_2/Group/panda_link1/visuals' (Xform)
* 引用: reference:./Props/panda_link1.usd @/Root
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.110, 0.184, 0.247), center=(-15.010, 29.916, 0.918)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm_2/Group/panda_link1/collisions' (Xform)
* 引用: reference:./Props/instanceable_collision_meshes.usd @/panda_link1_collisions
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(-15.010, 30.000, 1.072)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm_2/Group/panda_link2/visuals' (Xform)
* 引用: reference:./Props/panda_link2.usd @/Root
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.110, 0.249, 0.184), center=(-15.010, 30.083, 1.228)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm_2/Group/panda_link2/collisions' (Xform)
* 引用: reference:./Props/instanceable_collision_meshes.usd @/panda_link2_collisions
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(-15.010, 30.000, 1.072)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm_2/Group/panda_link3/visuals' (Xform)
* 引用: reference:./Props/panda_link3.usd @/Root
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.193, 0.166, 0.176), center=(-14.917, 30.063, 1.709)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm_2/Group/panda_link3/collisions' (Xform)
* 引用: reference:./Props/instanceable_collision_meshes.usd @/panda_link3_collisions
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(-15.010, 30.000, 1.783)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm_2/Group/panda_link4/visuals' (Xform)
* 引用: reference:./Props/panda_link4.usd @/Root
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.193, 0.179, 0.166), center=(-14.917, 29.937, 1.861)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm_2/Group/panda_link4/collisions' (Xform)
* 引用: reference:./Props/instanceable_collision_meshes.usd @/panda_link4_collisions
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(-14.825, 30.000, 1.783)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm_2/Group/panda_link5/visuals' (Xform)
* 引用: reference:./Props/panda_link5.usd @/Root
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.110, 0.185, 0.311), center=(-15.010, 30.084, 2.414)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm_2/Group/panda_link5/collisions' (Xform)
* 引用: reference:./Props/instanceable_collision_meshes.usd @/panda_link5_collisions
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(-15.010, 30.000, 2.647)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm_2/Group/panda_link6/visuals' (Xform)
* 引用: reference:./Props/panda_link6.usd @/Root
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.180, 0.133, 0.100), center=(-14.916, 29.986, 2.681)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm_2/Group/panda_link6/collisions' (Xform)
* 引用: reference:./Props/instanceable_collision_meshes.usd @/panda_link6_collisions
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(-15.010, 30.000, 2.647)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm_2/Group/panda_link7/visuals' (Xform)
* 引用: reference:./Props/panda_link7.usd @/Root
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.125, 0.125, 0.055), center=(-14.770, 29.958, 2.468)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm_2/Group/panda_link7/collisions' (Xform)
* 引用: reference:./Props/instanceable_collision_meshes.usd @/panda_link7_collisions
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(-14.812, 30.000, 2.647)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm_2/Group/panda_rightfinger/visuals' (Xform)
* 引用: reference:./Props/panda_rightfinger.usd @/Root
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.021, 0.026, 0.054), center=(-14.833, 30.021, 2.214)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm_2/Group/panda_rightfinger/collisions' (Xform)
* 引用: reference:./Props/instanceable_collision_meshes.usd @/panda_rightfinger_collisions
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(-14.812, 30.000, 2.275)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm_3' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/5.0/Isaac/IsaacLab/Robots/FrankaEmika/panda_instanceable1.usd
* BBox (world): size=(0.755, 0.583, 2.508), center=(-9.980, 30.000, 1.577)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm_3/Group/panda_hand/visuals' (Xform)
* 引用: reference:./Props/panda_hand.usd @/Root
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.063, 0.205, 0.092), center=(-9.815, 30.002, 2.361)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm_3/Group/panda_hand/collisions' (Xform)
* 引用: reference:./Props/instanceable_collision_meshes.usd @/panda_hand_collisions
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(-9.812, 30.000, 2.406)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm_3/Group/panda_leftfinger/visuals' (Xform)
* 引用: reference:./Props/panda_leftfinger.usd @/Root
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.021, 0.026, 0.054), center=(-9.791, 29.979, 2.214)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm_3/Group/panda_leftfinger/collisions' (Xform)
* 引用: reference:./Props/instanceable_collision_meshes.usd @/panda_leftfinger_collisions
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(-9.812, 30.000, 2.275)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm_3/Group/panda_link0/visuals' (Xform)
* 引用: reference:./Props/panda_link0.usd @/Root
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.226, 0.189, 0.140), center=(-10.103, 30.000, 0.480)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm_3/Group/panda_link0/collisions' (Xform)
* 引用: reference:./Props/instanceable_collision_meshes.usd @/panda_link0_collisions
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(-10.010, 30.000, 0.323)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm_3/Group/panda_link1/visuals' (Xform)
* 引用: reference:./Props/panda_link1.usd @/Root
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.110, 0.184, 0.247), center=(-10.010, 29.916, 0.918)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm_3/Group/panda_link1/collisions' (Xform)
* 引用: reference:./Props/instanceable_collision_meshes.usd @/panda_link1_collisions
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(-10.010, 30.000, 1.072)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm_3/Group/panda_link2/visuals' (Xform)
* 引用: reference:./Props/panda_link2.usd @/Root
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.110, 0.249, 0.184), center=(-10.010, 30.083, 1.228)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm_3/Group/panda_link2/collisions' (Xform)
* 引用: reference:./Props/instanceable_collision_meshes.usd @/panda_link2_collisions
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(-10.010, 30.000, 1.072)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm_3/Group/panda_link3/visuals' (Xform)
* 引用: reference:./Props/panda_link3.usd @/Root
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.193, 0.166, 0.176), center=(-9.917, 30.063, 1.709)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm_3/Group/panda_link3/collisions' (Xform)
* 引用: reference:./Props/instanceable_collision_meshes.usd @/panda_link3_collisions
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(-10.010, 30.000, 1.783)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm_3/Group/panda_link4/visuals' (Xform)
* 引用: reference:./Props/panda_link4.usd @/Root
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.193, 0.179, 0.166), center=(-9.917, 29.937, 1.861)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm_3/Group/panda_link4/collisions' (Xform)
* 引用: reference:./Props/instanceable_collision_meshes.usd @/panda_link4_collisions
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(-9.825, 30.000, 1.783)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm_3/Group/panda_link5/visuals' (Xform)
* 引用: reference:./Props/panda_link5.usd @/Root
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.110, 0.185, 0.311), center=(-10.010, 30.084, 2.414)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm_3/Group/panda_link5/collisions' (Xform)
* 引用: reference:./Props/instanceable_collision_meshes.usd @/panda_link5_collisions
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(-10.010, 30.000, 2.647)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm_3/Group/panda_link6/visuals' (Xform)
* 引用: reference:./Props/panda_link6.usd @/Root
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.180, 0.133, 0.100), center=(-9.916, 29.986, 2.681)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm_3/Group/panda_link6/collisions' (Xform)
* 引用: reference:./Props/instanceable_collision_meshes.usd @/panda_link6_collisions
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(-10.010, 30.000, 2.647)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm_3/Group/panda_link7/visuals' (Xform)
* 引用: reference:./Props/panda_link7.usd @/Root
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.125, 0.125, 0.055), center=(-9.770, 29.958, 2.468)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm_3/Group/panda_link7/collisions' (Xform)
* 引用: reference:./Props/instanceable_collision_meshes.usd @/panda_link7_collisions
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(-9.812, 30.000, 2.647)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm_3/Group/panda_rightfinger/visuals' (Xform)
* 引用: reference:./Props/panda_rightfinger.usd @/Root
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.021, 0.026, 0.054), center=(-9.833, 30.021, 2.214)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm_3/Group/panda_rightfinger/collisions' (Xform)
* 引用: reference:./Props/instanceable_collision_meshes.usd @/panda_rightfinger_collisions
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(-9.812, 30.000, 2.275)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm_4' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/5.0/Isaac/IsaacLab/Robots/FrankaEmika/panda_instanceable1.usd
* BBox (world): size=(0.755, 0.583, 2.508), center=(-4.980, 30.000, 1.577)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm_4/Group/panda_hand/visuals' (Xform)
* 引用: reference:./Props/panda_hand.usd @/Root
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.063, 0.205, 0.092), center=(-4.815, 30.002, 2.361)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm_4/Group/panda_hand/collisions' (Xform)
* 引用: reference:./Props/instanceable_collision_meshes.usd @/panda_hand_collisions
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(-4.812, 30.000, 2.406)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm_4/Group/panda_leftfinger/visuals' (Xform)
* 引用: reference:./Props/panda_leftfinger.usd @/Root
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.021, 0.026, 0.054), center=(-4.791, 29.979, 2.214)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm_4/Group/panda_leftfinger/collisions' (Xform)
* 引用: reference:./Props/instanceable_collision_meshes.usd @/panda_leftfinger_collisions
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(-4.812, 30.000, 2.275)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm_4/Group/panda_link0/visuals' (Xform)
* 引用: reference:./Props/panda_link0.usd @/Root
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.226, 0.189, 0.140), center=(-5.103, 30.000, 0.480)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm_4/Group/panda_link0/collisions' (Xform)
* 引用: reference:./Props/instanceable_collision_meshes.usd @/panda_link0_collisions
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(-5.010, 30.000, 0.323)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm_4/Group/panda_link1/visuals' (Xform)
* 引用: reference:./Props/panda_link1.usd @/Root
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.110, 0.184, 0.247), center=(-5.010, 29.916, 0.918)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm_4/Group/panda_link1/collisions' (Xform)
* 引用: reference:./Props/instanceable_collision_meshes.usd @/panda_link1_collisions
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(-5.010, 30.000, 1.072)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm_4/Group/panda_link2/visuals' (Xform)
* 引用: reference:./Props/panda_link2.usd @/Root
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.110, 0.249, 0.184), center=(-5.010, 30.083, 1.228)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm_4/Group/panda_link2/collisions' (Xform)
* 引用: reference:./Props/instanceable_collision_meshes.usd @/panda_link2_collisions
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(-5.010, 30.000, 1.072)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm_4/Group/panda_link3/visuals' (Xform)
* 引用: reference:./Props/panda_link3.usd @/Root
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.193, 0.166, 0.176), center=(-4.917, 30.063, 1.709)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm_4/Group/panda_link3/collisions' (Xform)
* 引用: reference:./Props/instanceable_collision_meshes.usd @/panda_link3_collisions
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(-5.010, 30.000, 1.783)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm_4/Group/panda_link4/visuals' (Xform)
* 引用: reference:./Props/panda_link4.usd @/Root
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.193, 0.179, 0.166), center=(-4.917, 29.937, 1.861)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm_4/Group/panda_link4/collisions' (Xform)
* 引用: reference:./Props/instanceable_collision_meshes.usd @/panda_link4_collisions
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(-4.825, 30.000, 1.783)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm_4/Group/panda_link5/visuals' (Xform)
* 引用: reference:./Props/panda_link5.usd @/Root
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.110, 0.185, 0.311), center=(-5.010, 30.084, 2.414)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm_4/Group/panda_link5/collisions' (Xform)
* 引用: reference:./Props/instanceable_collision_meshes.usd @/panda_link5_collisions
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(-5.010, 30.000, 2.647)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm_4/Group/panda_link6/visuals' (Xform)
* 引用: reference:./Props/panda_link6.usd @/Root
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.180, 0.133, 0.100), center=(-4.916, 29.986, 2.681)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm_4/Group/panda_link6/collisions' (Xform)
* 引用: reference:./Props/instanceable_collision_meshes.usd @/panda_link6_collisions
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(-5.010, 30.000, 2.647)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm_4/Group/panda_link7/visuals' (Xform)
* 引用: reference:./Props/panda_link7.usd @/Root
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.125, 0.125, 0.055), center=(-4.770, 29.958, 2.468)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm_4/Group/panda_link7/collisions' (Xform)
* 引用: reference:./Props/instanceable_collision_meshes.usd @/panda_link7_collisions
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(-4.812, 30.000, 2.647)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm_4/Group/panda_rightfinger/visuals' (Xform)
* 引用: reference:./Props/panda_rightfinger.usd @/Root
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.021, 0.026, 0.054), center=(-4.833, 30.021, 2.214)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm_4/Group/panda_rightfinger/collisions' (Xform)
* 引用: reference:./Props/instanceable_collision_meshes.usd @/panda_rightfinger_collisions
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(-4.812, 30.000, 2.275)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm_5' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/5.0/Isaac/IsaacLab/Robots/FrankaEmika/panda_instanceable1.usd
* BBox (world): size=(0.755, 0.583, 2.508), center=(0.020, 30.000, 1.577)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm_5/Group/panda_hand/visuals' (Xform)
* 引用: reference:./Props/panda_hand.usd @/Root
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.063, 0.205, 0.092), center=(0.185, 30.002, 2.361)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm_5/Group/panda_hand/collisions' (Xform)
* 引用: reference:./Props/instanceable_collision_meshes.usd @/panda_hand_collisions
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(0.188, 30.000, 2.406)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm_5/Group/panda_leftfinger/visuals' (Xform)
* 引用: reference:./Props/panda_leftfinger.usd @/Root
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.021, 0.026, 0.054), center=(0.209, 29.979, 2.214)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm_5/Group/panda_leftfinger/collisions' (Xform)
* 引用: reference:./Props/instanceable_collision_meshes.usd @/panda_leftfinger_collisions
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(0.188, 30.000, 2.275)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm_5/Group/panda_link0/visuals' (Xform)
* 引用: reference:./Props/panda_link0.usd @/Root
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.226, 0.189, 0.140), center=(-0.103, 30.000, 0.480)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm_5/Group/panda_link0/collisions' (Xform)
* 引用: reference:./Props/instanceable_collision_meshes.usd @/panda_link0_collisions
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(-0.010, 30.000, 0.323)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm_5/Group/panda_link1/visuals' (Xform)
* 引用: reference:./Props/panda_link1.usd @/Root
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.110, 0.184, 0.247), center=(-0.010, 29.916, 0.918)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm_5/Group/panda_link1/collisions' (Xform)
* 引用: reference:./Props/instanceable_collision_meshes.usd @/panda_link1_collisions
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(-0.010, 30.000, 1.072)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm_5/Group/panda_link2/visuals' (Xform)
* 引用: reference:./Props/panda_link2.usd @/Root
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.110, 0.249, 0.184), center=(-0.010, 30.083, 1.228)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm_5/Group/panda_link2/collisions' (Xform)
* 引用: reference:./Props/instanceable_collision_meshes.usd @/panda_link2_collisions
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(-0.010, 30.000, 1.072)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm_5/Group/panda_link3/visuals' (Xform)
* 引用: reference:./Props/panda_link3.usd @/Root
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.193, 0.166, 0.176), center=(0.083, 30.063, 1.709)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm_5/Group/panda_link3/collisions' (Xform)
* 引用: reference:./Props/instanceable_collision_meshes.usd @/panda_link3_collisions
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(-0.010, 30.000, 1.783)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm_5/Group/panda_link4/visuals' (Xform)
* 引用: reference:./Props/panda_link4.usd @/Root
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.193, 0.179, 0.166), center=(0.083, 29.937, 1.861)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm_5/Group/panda_link4/collisions' (Xform)
* 引用: reference:./Props/instanceable_collision_meshes.usd @/panda_link4_collisions
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(0.175, 30.000, 1.783)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm_5/Group/panda_link5/visuals' (Xform)
* 引用: reference:./Props/panda_link5.usd @/Root
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.110, 0.185, 0.311), center=(-0.010, 30.084, 2.414)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm_5/Group/panda_link5/collisions' (Xform)
* 引用: reference:./Props/instanceable_collision_meshes.usd @/panda_link5_collisions
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(-0.010, 30.000, 2.647)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm_5/Group/panda_link6/visuals' (Xform)
* 引用: reference:./Props/panda_link6.usd @/Root
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.180, 0.133, 0.100), center=(0.084, 29.986, 2.681)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm_5/Group/panda_link6/collisions' (Xform)
* 引用: reference:./Props/instanceable_collision_meshes.usd @/panda_link6_collisions
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(-0.010, 30.000, 2.647)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm_5/Group/panda_link7/visuals' (Xform)
* 引用: reference:./Props/panda_link7.usd @/Root
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.125, 0.125, 0.055), center=(0.230, 29.958, 2.468)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm_5/Group/panda_link7/collisions' (Xform)
* 引用: reference:./Props/instanceable_collision_meshes.usd @/panda_link7_collisions
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(0.188, 30.000, 2.647)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm_5/Group/panda_rightfinger/visuals' (Xform)
* 引用: reference:./Props/panda_rightfinger.usd @/Root
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.021, 0.026, 0.054), center=(0.167, 30.021, 2.214)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm_5/Group/panda_rightfinger/collisions' (Xform)
* 引用: reference:./Props/instanceable_collision_meshes.usd @/panda_rightfinger_collisions
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(0.188, 30.000, 2.275)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm_6' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/5.0/Isaac/IsaacLab/Robots/FrankaEmika/panda_instanceable1.usd
* BBox (world): size=(0.755, 0.583, 2.508), center=(5.020, 30.000, 1.577)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm_6/Group/panda_hand/visuals' (Xform)
* 引用: reference:./Props/panda_hand.usd @/Root
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.063, 0.205, 0.092), center=(5.185, 30.002, 2.361)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm_6/Group/panda_hand/collisions' (Xform)
* 引用: reference:./Props/instanceable_collision_meshes.usd @/panda_hand_collisions
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(5.188, 30.000, 2.406)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm_6/Group/panda_leftfinger/visuals' (Xform)
* 引用: reference:./Props/panda_leftfinger.usd @/Root
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.021, 0.026, 0.054), center=(5.209, 29.979, 2.214)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm_6/Group/panda_leftfinger/collisions' (Xform)
* 引用: reference:./Props/instanceable_collision_meshes.usd @/panda_leftfinger_collisions
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(5.188, 30.000, 2.275)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm_6/Group/panda_link0/visuals' (Xform)
* 引用: reference:./Props/panda_link0.usd @/Root
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.226, 0.189, 0.140), center=(4.897, 30.000, 0.480)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm_6/Group/panda_link0/collisions' (Xform)
* 引用: reference:./Props/instanceable_collision_meshes.usd @/panda_link0_collisions
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(4.990, 30.000, 0.323)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm_6/Group/panda_link1/visuals' (Xform)
* 引用: reference:./Props/panda_link1.usd @/Root
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.110, 0.184, 0.247), center=(4.990, 29.916, 0.918)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm_6/Group/panda_link1/collisions' (Xform)
* 引用: reference:./Props/instanceable_collision_meshes.usd @/panda_link1_collisions
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(4.990, 30.000, 1.072)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm_6/Group/panda_link2/visuals' (Xform)
* 引用: reference:./Props/panda_link2.usd @/Root
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.110, 0.249, 0.184), center=(4.990, 30.083, 1.228)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm_6/Group/panda_link2/collisions' (Xform)
* 引用: reference:./Props/instanceable_collision_meshes.usd @/panda_link2_collisions
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(4.990, 30.000, 1.072)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm_6/Group/panda_link3/visuals' (Xform)
* 引用: reference:./Props/panda_link3.usd @/Root
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.193, 0.166, 0.176), center=(5.083, 30.063, 1.709)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm_6/Group/panda_link3/collisions' (Xform)
* 引用: reference:./Props/instanceable_collision_meshes.usd @/panda_link3_collisions
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(4.990, 30.000, 1.783)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm_6/Group/panda_link4/visuals' (Xform)
* 引用: reference:./Props/panda_link4.usd @/Root
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.193, 0.179, 0.166), center=(5.083, 29.937, 1.861)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm_6/Group/panda_link4/collisions' (Xform)
* 引用: reference:./Props/instanceable_collision_meshes.usd @/panda_link4_collisions
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(5.175, 30.000, 1.783)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm_6/Group/panda_link5/visuals' (Xform)
* 引用: reference:./Props/panda_link5.usd @/Root
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.110, 0.185, 0.311), center=(4.990, 30.084, 2.414)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm_6/Group/panda_link5/collisions' (Xform)
* 引用: reference:./Props/instanceable_collision_meshes.usd @/panda_link5_collisions
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(4.990, 30.000, 2.647)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm_6/Group/panda_link6/visuals' (Xform)
* 引用: reference:./Props/panda_link6.usd @/Root
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.180, 0.133, 0.100), center=(5.084, 29.986, 2.681)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm_6/Group/panda_link6/collisions' (Xform)
* 引用: reference:./Props/instanceable_collision_meshes.usd @/panda_link6_collisions
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(4.990, 30.000, 2.647)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm_6/Group/panda_link7/visuals' (Xform)
* 引用: reference:./Props/panda_link7.usd @/Root
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.125, 0.125, 0.055), center=(5.230, 29.958, 2.468)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm_6/Group/panda_link7/collisions' (Xform)
* 引用: reference:./Props/instanceable_collision_meshes.usd @/panda_link7_collisions
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(5.188, 30.000, 2.647)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm_6/Group/panda_rightfinger/visuals' (Xform)
* 引用: reference:./Props/panda_rightfinger.usd @/Root
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.021, 0.026, 0.054), center=(5.167, 30.021, 2.214)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm_6/Group/panda_rightfinger/collisions' (Xform)
* 引用: reference:./Props/instanceable_collision_meshes.usd @/panda_rightfinger_collisions
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(5.188, 30.000, 2.275)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm_7' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/5.0/Isaac/IsaacLab/Robots/FrankaEmika/panda_instanceable1.usd
* BBox (world): size=(0.755, 0.583, 2.508), center=(10.020, 30.000, 1.577)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm_7/Group/panda_hand/visuals' (Xform)
* 引用: reference:./Props/panda_hand.usd @/Root
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.063, 0.205, 0.092), center=(10.185, 30.002, 2.361)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm_7/Group/panda_hand/collisions' (Xform)
* 引用: reference:./Props/instanceable_collision_meshes.usd @/panda_hand_collisions
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(10.188, 30.000, 2.406)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm_7/Group/panda_leftfinger/visuals' (Xform)
* 引用: reference:./Props/panda_leftfinger.usd @/Root
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.021, 0.026, 0.054), center=(10.209, 29.979, 2.214)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm_7/Group/panda_leftfinger/collisions' (Xform)
* 引用: reference:./Props/instanceable_collision_meshes.usd @/panda_leftfinger_collisions
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(10.188, 30.000, 2.275)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm_7/Group/panda_link0/visuals' (Xform)
* 引用: reference:./Props/panda_link0.usd @/Root
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.226, 0.189, 0.140), center=(9.897, 30.000, 0.480)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm_7/Group/panda_link0/collisions' (Xform)
* 引用: reference:./Props/instanceable_collision_meshes.usd @/panda_link0_collisions
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(9.990, 30.000, 0.323)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm_7/Group/panda_link1/visuals' (Xform)
* 引用: reference:./Props/panda_link1.usd @/Root
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.110, 0.184, 0.247), center=(9.990, 29.916, 0.918)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm_7/Group/panda_link1/collisions' (Xform)
* 引用: reference:./Props/instanceable_collision_meshes.usd @/panda_link1_collisions
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(9.990, 30.000, 1.072)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm_7/Group/panda_link2/visuals' (Xform)
* 引用: reference:./Props/panda_link2.usd @/Root
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.110, 0.249, 0.184), center=(9.990, 30.083, 1.228)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm_7/Group/panda_link2/collisions' (Xform)
* 引用: reference:./Props/instanceable_collision_meshes.usd @/panda_link2_collisions
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(9.990, 30.000, 1.072)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm_7/Group/panda_link3/visuals' (Xform)
* 引用: reference:./Props/panda_link3.usd @/Root
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.193, 0.166, 0.176), center=(10.083, 30.063, 1.709)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm_7/Group/panda_link3/collisions' (Xform)
* 引用: reference:./Props/instanceable_collision_meshes.usd @/panda_link3_collisions
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(9.990, 30.000, 1.783)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm_7/Group/panda_link4/visuals' (Xform)
* 引用: reference:./Props/panda_link4.usd @/Root
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.193, 0.179, 0.166), center=(10.083, 29.937, 1.861)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm_7/Group/panda_link4/collisions' (Xform)
* 引用: reference:./Props/instanceable_collision_meshes.usd @/panda_link4_collisions
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(10.175, 30.000, 1.783)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm_7/Group/panda_link5/visuals' (Xform)
* 引用: reference:./Props/panda_link5.usd @/Root
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.110, 0.185, 0.311), center=(9.990, 30.084, 2.414)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm_7/Group/panda_link5/collisions' (Xform)
* 引用: reference:./Props/instanceable_collision_meshes.usd @/panda_link5_collisions
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(9.990, 30.000, 2.647)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm_7/Group/panda_link6/visuals' (Xform)
* 引用: reference:./Props/panda_link6.usd @/Root
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.180, 0.133, 0.100), center=(10.084, 29.986, 2.681)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm_7/Group/panda_link6/collisions' (Xform)
* 引用: reference:./Props/instanceable_collision_meshes.usd @/panda_link6_collisions
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(9.990, 30.000, 2.647)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm_7/Group/panda_link7/visuals' (Xform)
* 引用: reference:./Props/panda_link7.usd @/Root
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.125, 0.125, 0.055), center=(10.230, 29.958, 2.468)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm_7/Group/panda_link7/collisions' (Xform)
* 引用: reference:./Props/instanceable_collision_meshes.usd @/panda_link7_collisions
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(10.188, 30.000, 2.647)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm_7/Group/panda_rightfinger/visuals' (Xform)
* 引用: reference:./Props/panda_rightfinger.usd @/Root
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.021, 0.026, 0.054), center=(10.167, 30.021, 2.214)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm_7/Group/panda_rightfinger/collisions' (Xform)
* 引用: reference:./Props/instanceable_collision_meshes.usd @/panda_rightfinger_collisions
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(10.188, 30.000, 2.275)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm_8' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/5.0/Isaac/IsaacLab/Robots/FrankaEmika/panda_instanceable1.usd
* BBox (world): size=(0.755, 0.583, 2.508), center=(15.020, 30.000, 1.577)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm_8/Group/panda_hand/visuals' (Xform)
* 引用: reference:./Props/panda_hand.usd @/Root
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.063, 0.205, 0.092), center=(15.185, 30.002, 2.361)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm_8/Group/panda_hand/collisions' (Xform)
* 引用: reference:./Props/instanceable_collision_meshes.usd @/panda_hand_collisions
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(15.188, 30.000, 2.406)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm_8/Group/panda_leftfinger/visuals' (Xform)
* 引用: reference:./Props/panda_leftfinger.usd @/Root
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.021, 0.026, 0.054), center=(15.209, 29.979, 2.214)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm_8/Group/panda_leftfinger/collisions' (Xform)
* 引用: reference:./Props/instanceable_collision_meshes.usd @/panda_leftfinger_collisions
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(15.188, 30.000, 2.275)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm_8/Group/panda_link0/visuals' (Xform)
* 引用: reference:./Props/panda_link0.usd @/Root
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.226, 0.189, 0.140), center=(14.897, 30.000, 0.480)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm_8/Group/panda_link0/collisions' (Xform)
* 引用: reference:./Props/instanceable_collision_meshes.usd @/panda_link0_collisions
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(14.990, 30.000, 0.323)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm_8/Group/panda_link1/visuals' (Xform)
* 引用: reference:./Props/panda_link1.usd @/Root
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.110, 0.184, 0.247), center=(14.990, 29.916, 0.918)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm_8/Group/panda_link1/collisions' (Xform)
* 引用: reference:./Props/instanceable_collision_meshes.usd @/panda_link1_collisions
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(14.990, 30.000, 1.072)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm_8/Group/panda_link2/visuals' (Xform)
* 引用: reference:./Props/panda_link2.usd @/Root
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.110, 0.249, 0.184), center=(14.990, 30.083, 1.228)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm_8/Group/panda_link2/collisions' (Xform)
* 引用: reference:./Props/instanceable_collision_meshes.usd @/panda_link2_collisions
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(14.990, 30.000, 1.072)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm_8/Group/panda_link3/visuals' (Xform)
* 引用: reference:./Props/panda_link3.usd @/Root
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.193, 0.166, 0.176), center=(15.083, 30.063, 1.709)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm_8/Group/panda_link3/collisions' (Xform)
* 引用: reference:./Props/instanceable_collision_meshes.usd @/panda_link3_collisions
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(14.990, 30.000, 1.783)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm_8/Group/panda_link4/visuals' (Xform)
* 引用: reference:./Props/panda_link4.usd @/Root
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.193, 0.179, 0.166), center=(15.083, 29.937, 1.861)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm_8/Group/panda_link4/collisions' (Xform)
* 引用: reference:./Props/instanceable_collision_meshes.usd @/panda_link4_collisions
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(15.175, 30.000, 1.783)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm_8/Group/panda_link5/visuals' (Xform)
* 引用: reference:./Props/panda_link5.usd @/Root
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.110, 0.185, 0.311), center=(14.990, 30.084, 2.414)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm_8/Group/panda_link5/collisions' (Xform)
* 引用: reference:./Props/instanceable_collision_meshes.usd @/panda_link5_collisions
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(14.990, 30.000, 2.647)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm_8/Group/panda_link6/visuals' (Xform)
* 引用: reference:./Props/panda_link6.usd @/Root
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.180, 0.133, 0.100), center=(15.084, 29.986, 2.681)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm_8/Group/panda_link6/collisions' (Xform)
* 引用: reference:./Props/instanceable_collision_meshes.usd @/panda_link6_collisions
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(14.990, 30.000, 2.647)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm_8/Group/panda_link7/visuals' (Xform)
* 引用: reference:./Props/panda_link7.usd @/Root
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.125, 0.125, 0.055), center=(15.230, 29.958, 2.468)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm_8/Group/panda_link7/collisions' (Xform)
* 引用: reference:./Props/instanceable_collision_meshes.usd @/panda_link7_collisions
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(15.188, 30.000, 2.647)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm_8/Group/panda_rightfinger/visuals' (Xform)
* 引用: reference:./Props/panda_rightfinger.usd @/Root
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.021, 0.026, 0.054), center=(15.167, 30.021, 2.214)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm_8/Group/panda_rightfinger/collisions' (Xform)
* 引用: reference:./Props/instanceable_collision_meshes.usd @/panda_rightfinger_collisions
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(15.188, 30.000, 2.275)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/agv_1' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/AGV_ready_1/AGV_ready_1.usdc
* BBox (world): size=(1.457, 0.340, 0.669), center=(-18.818, 29.714, 0.279)
* 几何统计: Mesh=171, Vertices=1634024, Faces=683203
* 子Mesh材质: /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_2/Object_0 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_3/Object_1 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_4/Object_2 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_5/Object_3 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_6/Object_4 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_7/Object_5 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_8/Object_6 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_9/Object_7 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_10/Object_8 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_11/Object_9 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_12/Object_10 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_13/Object_11 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_14/Object_12 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_15/Object_13 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_16/Object_14 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_17/Object_15 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_18/Object_16 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_19/Object_17 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_20/Object_18 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_21/Object_19 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_22/Object_20 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_23/Object_21 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_24/Object_22 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_25/Object_23 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_26/Object_24 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_27/Object_25 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_28/Object_26 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_29/Object_27 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_30/Object_28 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_31/Object_29 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_32/Object_30 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_33/Object_31 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_34/Object_32 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_35/Object_33 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_36/Object_34 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_37/Object_35 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_38/Object_36 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_39/Object_37 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_40/Object_38 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_41/Object_39 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_42/Object_40 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_43/Object_41 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_44/Object_42 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_45/Object_43 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_46/Object_44 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_47/Object_45 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_48/Object_46 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_49/Object_47 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_50/Object_48 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_51/Object_49 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_52/Object_50 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_53/Object_51 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_54/Object_52 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_55/Object_53 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_56/Object_54 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_57/Object_55 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_58/Object_56 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_59/Object_57 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_60/Object_58 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_61/Object_59 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_62/Object_60 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_63/Object_61 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_64/Object_62 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_65/Object_63 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_66/Object_64 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_67/Object_65 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_68/Object_66 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_69/Object_67 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_70/Object_68 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_71/Object_69 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_72/Object_70 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_73/Object_71 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_74/Object_72 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_75/Object_73 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_76/Object_74 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_77/Object_75 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_78/Object_76 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_79/Object_77 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_80/Object_78 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_81/Object_79 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_82/Object_80 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_83/Object_81 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_84/Object_82 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_85/Object_83 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_86/Object_84 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_87/Object_85 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_88/Object_86 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_89/Object_87 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_90/Object_88 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_91/Object_89 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_92/Object_90 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_93/Object_91 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_94/Object_92 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_95/Object_93 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_96/Object_94 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_97/Object_95 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_98/Object_96 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_99/Object_97 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_100/Object_98 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_101/Object_99 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_102/Object_100 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_103/Object_101 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_104/Object_102 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_105/Object_103 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_106/Object_104 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_107/Object_105 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_108/Object_106 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_109/Object_107 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_110/Object_108 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_111/Object_109 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_112/Object_110 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_113/Object_111 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_114/Object_112 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_115/Object_113 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_116/Object_114 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_117/Object_115 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_118/Object_116 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_119/Object_117 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_120/Object_118 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_121/Object_119 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_122/Object_120 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_123/Object_121 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_124/Object_122 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_125/Object_123 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_126/Object_124 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_127/Object_125 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_128/Object_126 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_129/Object_127 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_130/Object_128 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_131/Object_129 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_132/Object_130 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_133/Object_131 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_134/Object_132 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_135/Object_133 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_136/Object_134 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_137/Object_135 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_138/Object_136 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_139/Object_137 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_140/Object_138 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_141/Object_139 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_142/Object_140 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_143/Object_141 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_144/Object_142 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_145/Object_143 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_146/Object_144 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_147/Object_145 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_148/Object_146 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_149/Object_147 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_150/Object_148 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_151/Object_149 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_152/Object_150 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_153/Object_151 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_154/Object_152 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_155/Object_153 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_156/Object_154 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_157/Object_155 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_158/Object_156 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_159/Object_157 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_160/Object_158 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_161/Object_159 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_162/Object_160 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_163/Object_161 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_164/Object_162 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_165/Object_163 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_166/Object_164 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_167/Object_165 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_168/Object_166 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_169/Object_167 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_170/Object_168 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_171/Object_169 -> 未绑定, /World/agv_1/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_172/Object_170 -> 未绑定


---


### '/World/agv_2' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/AGV_ready_1/AGV_ready_1.usdc
* BBox (world): size=(1.457, 0.340, 0.669), center=(-13.818, 29.714, 0.279)
* 几何统计: Mesh=171, Vertices=1634024, Faces=683203
* 子Mesh材质: /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_2/Object_0 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_3/Object_1 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_4/Object_2 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_5/Object_3 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_6/Object_4 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_7/Object_5 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_8/Object_6 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_9/Object_7 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_10/Object_8 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_11/Object_9 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_12/Object_10 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_13/Object_11 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_14/Object_12 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_15/Object_13 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_16/Object_14 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_17/Object_15 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_18/Object_16 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_19/Object_17 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_20/Object_18 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_21/Object_19 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_22/Object_20 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_23/Object_21 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_24/Object_22 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_25/Object_23 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_26/Object_24 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_27/Object_25 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_28/Object_26 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_29/Object_27 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_30/Object_28 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_31/Object_29 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_32/Object_30 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_33/Object_31 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_34/Object_32 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_35/Object_33 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_36/Object_34 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_37/Object_35 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_38/Object_36 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_39/Object_37 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_40/Object_38 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_41/Object_39 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_42/Object_40 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_43/Object_41 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_44/Object_42 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_45/Object_43 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_46/Object_44 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_47/Object_45 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_48/Object_46 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_49/Object_47 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_50/Object_48 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_51/Object_49 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_52/Object_50 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_53/Object_51 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_54/Object_52 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_55/Object_53 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_56/Object_54 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_57/Object_55 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_58/Object_56 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_59/Object_57 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_60/Object_58 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_61/Object_59 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_62/Object_60 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_63/Object_61 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_64/Object_62 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_65/Object_63 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_66/Object_64 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_67/Object_65 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_68/Object_66 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_69/Object_67 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_70/Object_68 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_71/Object_69 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_72/Object_70 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_73/Object_71 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_74/Object_72 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_75/Object_73 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_76/Object_74 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_77/Object_75 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_78/Object_76 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_79/Object_77 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_80/Object_78 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_81/Object_79 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_82/Object_80 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_83/Object_81 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_84/Object_82 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_85/Object_83 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_86/Object_84 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_87/Object_85 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_88/Object_86 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_89/Object_87 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_90/Object_88 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_91/Object_89 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_92/Object_90 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_93/Object_91 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_94/Object_92 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_95/Object_93 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_96/Object_94 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_97/Object_95 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_98/Object_96 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_99/Object_97 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_100/Object_98 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_101/Object_99 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_102/Object_100 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_103/Object_101 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_104/Object_102 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_105/Object_103 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_106/Object_104 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_107/Object_105 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_108/Object_106 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_109/Object_107 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_110/Object_108 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_111/Object_109 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_112/Object_110 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_113/Object_111 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_114/Object_112 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_115/Object_113 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_116/Object_114 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_117/Object_115 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_118/Object_116 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_119/Object_117 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_120/Object_118 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_121/Object_119 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_122/Object_120 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_123/Object_121 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_124/Object_122 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_125/Object_123 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_126/Object_124 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_127/Object_125 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_128/Object_126 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_129/Object_127 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_130/Object_128 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_131/Object_129 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_132/Object_130 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_133/Object_131 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_134/Object_132 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_135/Object_133 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_136/Object_134 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_137/Object_135 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_138/Object_136 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_139/Object_137 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_140/Object_138 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_141/Object_139 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_142/Object_140 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_143/Object_141 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_144/Object_142 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_145/Object_143 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_146/Object_144 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_147/Object_145 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_148/Object_146 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_149/Object_147 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_150/Object_148 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_151/Object_149 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_152/Object_150 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_153/Object_151 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_154/Object_152 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_155/Object_153 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_156/Object_154 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_157/Object_155 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_158/Object_156 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_159/Object_157 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_160/Object_158 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_161/Object_159 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_162/Object_160 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_163/Object_161 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_164/Object_162 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_165/Object_163 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_166/Object_164 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_167/Object_165 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_168/Object_166 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_169/Object_167 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_170/Object_168 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_171/Object_169 -> 未绑定, /World/agv_2/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_172/Object_170 -> 未绑定


---


### '/World/agv_3' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/AGV_ready_1/AGV_ready_1.usdc
* BBox (world): size=(1.457, 0.340, 0.669), center=(-8.818, 29.714, 0.279)
* 几何统计: Mesh=171, Vertices=1634024, Faces=683203
* 子Mesh材质: /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_2/Object_0 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_3/Object_1 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_4/Object_2 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_5/Object_3 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_6/Object_4 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_7/Object_5 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_8/Object_6 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_9/Object_7 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_10/Object_8 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_11/Object_9 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_12/Object_10 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_13/Object_11 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_14/Object_12 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_15/Object_13 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_16/Object_14 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_17/Object_15 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_18/Object_16 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_19/Object_17 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_20/Object_18 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_21/Object_19 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_22/Object_20 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_23/Object_21 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_24/Object_22 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_25/Object_23 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_26/Object_24 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_27/Object_25 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_28/Object_26 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_29/Object_27 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_30/Object_28 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_31/Object_29 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_32/Object_30 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_33/Object_31 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_34/Object_32 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_35/Object_33 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_36/Object_34 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_37/Object_35 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_38/Object_36 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_39/Object_37 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_40/Object_38 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_41/Object_39 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_42/Object_40 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_43/Object_41 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_44/Object_42 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_45/Object_43 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_46/Object_44 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_47/Object_45 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_48/Object_46 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_49/Object_47 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_50/Object_48 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_51/Object_49 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_52/Object_50 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_53/Object_51 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_54/Object_52 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_55/Object_53 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_56/Object_54 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_57/Object_55 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_58/Object_56 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_59/Object_57 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_60/Object_58 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_61/Object_59 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_62/Object_60 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_63/Object_61 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_64/Object_62 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_65/Object_63 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_66/Object_64 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_67/Object_65 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_68/Object_66 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_69/Object_67 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_70/Object_68 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_71/Object_69 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_72/Object_70 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_73/Object_71 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_74/Object_72 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_75/Object_73 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_76/Object_74 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_77/Object_75 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_78/Object_76 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_79/Object_77 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_80/Object_78 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_81/Object_79 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_82/Object_80 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_83/Object_81 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_84/Object_82 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_85/Object_83 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_86/Object_84 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_87/Object_85 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_88/Object_86 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_89/Object_87 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_90/Object_88 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_91/Object_89 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_92/Object_90 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_93/Object_91 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_94/Object_92 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_95/Object_93 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_96/Object_94 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_97/Object_95 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_98/Object_96 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_99/Object_97 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_100/Object_98 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_101/Object_99 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_102/Object_100 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_103/Object_101 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_104/Object_102 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_105/Object_103 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_106/Object_104 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_107/Object_105 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_108/Object_106 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_109/Object_107 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_110/Object_108 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_111/Object_109 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_112/Object_110 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_113/Object_111 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_114/Object_112 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_115/Object_113 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_116/Object_114 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_117/Object_115 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_118/Object_116 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_119/Object_117 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_120/Object_118 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_121/Object_119 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_122/Object_120 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_123/Object_121 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_124/Object_122 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_125/Object_123 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_126/Object_124 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_127/Object_125 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_128/Object_126 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_129/Object_127 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_130/Object_128 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_131/Object_129 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_132/Object_130 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_133/Object_131 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_134/Object_132 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_135/Object_133 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_136/Object_134 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_137/Object_135 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_138/Object_136 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_139/Object_137 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_140/Object_138 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_141/Object_139 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_142/Object_140 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_143/Object_141 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_144/Object_142 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_145/Object_143 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_146/Object_144 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_147/Object_145 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_148/Object_146 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_149/Object_147 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_150/Object_148 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_151/Object_149 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_152/Object_150 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_153/Object_151 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_154/Object_152 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_155/Object_153 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_156/Object_154 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_157/Object_155 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_158/Object_156 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_159/Object_157 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_160/Object_158 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_161/Object_159 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_162/Object_160 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_163/Object_161 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_164/Object_162 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_165/Object_163 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_166/Object_164 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_167/Object_165 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_168/Object_166 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_169/Object_167 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_170/Object_168 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_171/Object_169 -> 未绑定, /World/agv_3/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_172/Object_170 -> 未绑定


---


### '/World/agv_4' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/AGV_ready_1/AGV_ready_1.usdc
* BBox (world): size=(1.457, 0.340, 0.669), center=(-3.818, 29.714, 0.279)
* 几何统计: Mesh=171, Vertices=1634024, Faces=683203
* 子Mesh材质: /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_2/Object_0 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_3/Object_1 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_4/Object_2 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_5/Object_3 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_6/Object_4 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_7/Object_5 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_8/Object_6 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_9/Object_7 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_10/Object_8 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_11/Object_9 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_12/Object_10 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_13/Object_11 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_14/Object_12 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_15/Object_13 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_16/Object_14 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_17/Object_15 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_18/Object_16 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_19/Object_17 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_20/Object_18 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_21/Object_19 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_22/Object_20 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_23/Object_21 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_24/Object_22 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_25/Object_23 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_26/Object_24 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_27/Object_25 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_28/Object_26 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_29/Object_27 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_30/Object_28 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_31/Object_29 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_32/Object_30 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_33/Object_31 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_34/Object_32 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_35/Object_33 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_36/Object_34 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_37/Object_35 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_38/Object_36 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_39/Object_37 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_40/Object_38 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_41/Object_39 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_42/Object_40 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_43/Object_41 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_44/Object_42 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_45/Object_43 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_46/Object_44 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_47/Object_45 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_48/Object_46 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_49/Object_47 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_50/Object_48 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_51/Object_49 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_52/Object_50 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_53/Object_51 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_54/Object_52 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_55/Object_53 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_56/Object_54 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_57/Object_55 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_58/Object_56 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_59/Object_57 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_60/Object_58 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_61/Object_59 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_62/Object_60 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_63/Object_61 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_64/Object_62 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_65/Object_63 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_66/Object_64 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_67/Object_65 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_68/Object_66 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_69/Object_67 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_70/Object_68 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_71/Object_69 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_72/Object_70 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_73/Object_71 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_74/Object_72 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_75/Object_73 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_76/Object_74 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_77/Object_75 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_78/Object_76 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_79/Object_77 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_80/Object_78 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_81/Object_79 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_82/Object_80 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_83/Object_81 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_84/Object_82 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_85/Object_83 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_86/Object_84 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_87/Object_85 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_88/Object_86 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_89/Object_87 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_90/Object_88 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_91/Object_89 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_92/Object_90 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_93/Object_91 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_94/Object_92 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_95/Object_93 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_96/Object_94 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_97/Object_95 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_98/Object_96 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_99/Object_97 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_100/Object_98 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_101/Object_99 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_102/Object_100 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_103/Object_101 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_104/Object_102 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_105/Object_103 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_106/Object_104 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_107/Object_105 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_108/Object_106 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_109/Object_107 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_110/Object_108 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_111/Object_109 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_112/Object_110 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_113/Object_111 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_114/Object_112 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_115/Object_113 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_116/Object_114 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_117/Object_115 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_118/Object_116 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_119/Object_117 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_120/Object_118 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_121/Object_119 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_122/Object_120 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_123/Object_121 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_124/Object_122 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_125/Object_123 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_126/Object_124 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_127/Object_125 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_128/Object_126 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_129/Object_127 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_130/Object_128 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_131/Object_129 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_132/Object_130 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_133/Object_131 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_134/Object_132 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_135/Object_133 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_136/Object_134 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_137/Object_135 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_138/Object_136 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_139/Object_137 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_140/Object_138 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_141/Object_139 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_142/Object_140 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_143/Object_141 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_144/Object_142 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_145/Object_143 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_146/Object_144 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_147/Object_145 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_148/Object_146 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_149/Object_147 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_150/Object_148 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_151/Object_149 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_152/Object_150 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_153/Object_151 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_154/Object_152 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_155/Object_153 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_156/Object_154 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_157/Object_155 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_158/Object_156 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_159/Object_157 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_160/Object_158 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_161/Object_159 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_162/Object_160 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_163/Object_161 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_164/Object_162 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_165/Object_163 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_166/Object_164 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_167/Object_165 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_168/Object_166 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_169/Object_167 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_170/Object_168 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_171/Object_169 -> 未绑定, /World/agv_4/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_172/Object_170 -> 未绑定


---


### '/World/agv_5' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/AGV_ready_1/AGV_ready_1.usdc
* BBox (world): size=(1.457, 0.340, 0.669), center=(1.182, 29.714, 0.279)
* 几何统计: Mesh=171, Vertices=1634024, Faces=683203
* 子Mesh材质: /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_2/Object_0 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_3/Object_1 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_4/Object_2 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_5/Object_3 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_6/Object_4 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_7/Object_5 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_8/Object_6 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_9/Object_7 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_10/Object_8 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_11/Object_9 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_12/Object_10 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_13/Object_11 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_14/Object_12 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_15/Object_13 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_16/Object_14 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_17/Object_15 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_18/Object_16 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_19/Object_17 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_20/Object_18 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_21/Object_19 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_22/Object_20 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_23/Object_21 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_24/Object_22 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_25/Object_23 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_26/Object_24 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_27/Object_25 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_28/Object_26 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_29/Object_27 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_30/Object_28 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_31/Object_29 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_32/Object_30 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_33/Object_31 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_34/Object_32 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_35/Object_33 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_36/Object_34 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_37/Object_35 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_38/Object_36 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_39/Object_37 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_40/Object_38 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_41/Object_39 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_42/Object_40 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_43/Object_41 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_44/Object_42 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_45/Object_43 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_46/Object_44 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_47/Object_45 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_48/Object_46 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_49/Object_47 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_50/Object_48 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_51/Object_49 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_52/Object_50 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_53/Object_51 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_54/Object_52 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_55/Object_53 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_56/Object_54 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_57/Object_55 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_58/Object_56 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_59/Object_57 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_60/Object_58 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_61/Object_59 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_62/Object_60 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_63/Object_61 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_64/Object_62 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_65/Object_63 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_66/Object_64 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_67/Object_65 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_68/Object_66 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_69/Object_67 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_70/Object_68 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_71/Object_69 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_72/Object_70 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_73/Object_71 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_74/Object_72 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_75/Object_73 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_76/Object_74 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_77/Object_75 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_78/Object_76 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_79/Object_77 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_80/Object_78 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_81/Object_79 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_82/Object_80 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_83/Object_81 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_84/Object_82 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_85/Object_83 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_86/Object_84 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_87/Object_85 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_88/Object_86 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_89/Object_87 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_90/Object_88 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_91/Object_89 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_92/Object_90 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_93/Object_91 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_94/Object_92 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_95/Object_93 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_96/Object_94 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_97/Object_95 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_98/Object_96 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_99/Object_97 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_100/Object_98 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_101/Object_99 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_102/Object_100 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_103/Object_101 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_104/Object_102 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_105/Object_103 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_106/Object_104 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_107/Object_105 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_108/Object_106 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_109/Object_107 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_110/Object_108 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_111/Object_109 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_112/Object_110 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_113/Object_111 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_114/Object_112 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_115/Object_113 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_116/Object_114 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_117/Object_115 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_118/Object_116 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_119/Object_117 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_120/Object_118 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_121/Object_119 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_122/Object_120 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_123/Object_121 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_124/Object_122 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_125/Object_123 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_126/Object_124 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_127/Object_125 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_128/Object_126 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_129/Object_127 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_130/Object_128 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_131/Object_129 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_132/Object_130 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_133/Object_131 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_134/Object_132 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_135/Object_133 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_136/Object_134 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_137/Object_135 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_138/Object_136 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_139/Object_137 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_140/Object_138 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_141/Object_139 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_142/Object_140 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_143/Object_141 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_144/Object_142 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_145/Object_143 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_146/Object_144 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_147/Object_145 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_148/Object_146 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_149/Object_147 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_150/Object_148 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_151/Object_149 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_152/Object_150 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_153/Object_151 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_154/Object_152 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_155/Object_153 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_156/Object_154 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_157/Object_155 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_158/Object_156 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_159/Object_157 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_160/Object_158 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_161/Object_159 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_162/Object_160 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_163/Object_161 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_164/Object_162 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_165/Object_163 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_166/Object_164 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_167/Object_165 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_168/Object_166 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_169/Object_167 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_170/Object_168 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_171/Object_169 -> 未绑定, /World/agv_5/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_172/Object_170 -> 未绑定


---


### '/World/agv_6' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/AGV_ready_1/AGV_ready_1.usdc
* BBox (world): size=(1.457, 0.340, 0.669), center=(6.182, 29.714, 0.279)
* 几何统计: Mesh=171, Vertices=1634024, Faces=683203
* 子Mesh材质: /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_2/Object_0 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_3/Object_1 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_4/Object_2 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_5/Object_3 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_6/Object_4 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_7/Object_5 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_8/Object_6 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_9/Object_7 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_10/Object_8 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_11/Object_9 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_12/Object_10 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_13/Object_11 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_14/Object_12 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_15/Object_13 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_16/Object_14 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_17/Object_15 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_18/Object_16 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_19/Object_17 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_20/Object_18 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_21/Object_19 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_22/Object_20 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_23/Object_21 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_24/Object_22 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_25/Object_23 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_26/Object_24 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_27/Object_25 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_28/Object_26 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_29/Object_27 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_30/Object_28 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_31/Object_29 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_32/Object_30 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_33/Object_31 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_34/Object_32 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_35/Object_33 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_36/Object_34 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_37/Object_35 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_38/Object_36 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_39/Object_37 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_40/Object_38 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_41/Object_39 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_42/Object_40 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_43/Object_41 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_44/Object_42 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_45/Object_43 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_46/Object_44 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_47/Object_45 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_48/Object_46 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_49/Object_47 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_50/Object_48 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_51/Object_49 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_52/Object_50 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_53/Object_51 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_54/Object_52 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_55/Object_53 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_56/Object_54 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_57/Object_55 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_58/Object_56 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_59/Object_57 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_60/Object_58 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_61/Object_59 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_62/Object_60 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_63/Object_61 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_64/Object_62 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_65/Object_63 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_66/Object_64 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_67/Object_65 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_68/Object_66 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_69/Object_67 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_70/Object_68 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_71/Object_69 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_72/Object_70 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_73/Object_71 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_74/Object_72 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_75/Object_73 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_76/Object_74 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_77/Object_75 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_78/Object_76 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_79/Object_77 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_80/Object_78 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_81/Object_79 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_82/Object_80 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_83/Object_81 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_84/Object_82 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_85/Object_83 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_86/Object_84 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_87/Object_85 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_88/Object_86 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_89/Object_87 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_90/Object_88 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_91/Object_89 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_92/Object_90 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_93/Object_91 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_94/Object_92 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_95/Object_93 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_96/Object_94 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_97/Object_95 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_98/Object_96 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_99/Object_97 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_100/Object_98 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_101/Object_99 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_102/Object_100 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_103/Object_101 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_104/Object_102 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_105/Object_103 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_106/Object_104 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_107/Object_105 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_108/Object_106 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_109/Object_107 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_110/Object_108 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_111/Object_109 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_112/Object_110 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_113/Object_111 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_114/Object_112 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_115/Object_113 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_116/Object_114 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_117/Object_115 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_118/Object_116 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_119/Object_117 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_120/Object_118 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_121/Object_119 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_122/Object_120 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_123/Object_121 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_124/Object_122 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_125/Object_123 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_126/Object_124 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_127/Object_125 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_128/Object_126 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_129/Object_127 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_130/Object_128 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_131/Object_129 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_132/Object_130 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_133/Object_131 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_134/Object_132 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_135/Object_133 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_136/Object_134 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_137/Object_135 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_138/Object_136 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_139/Object_137 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_140/Object_138 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_141/Object_139 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_142/Object_140 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_143/Object_141 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_144/Object_142 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_145/Object_143 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_146/Object_144 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_147/Object_145 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_148/Object_146 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_149/Object_147 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_150/Object_148 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_151/Object_149 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_152/Object_150 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_153/Object_151 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_154/Object_152 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_155/Object_153 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_156/Object_154 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_157/Object_155 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_158/Object_156 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_159/Object_157 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_160/Object_158 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_161/Object_159 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_162/Object_160 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_163/Object_161 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_164/Object_162 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_165/Object_163 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_166/Object_164 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_167/Object_165 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_168/Object_166 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_169/Object_167 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_170/Object_168 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_171/Object_169 -> 未绑定, /World/agv_6/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_172/Object_170 -> 未绑定


---


### '/World/agv_7' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/AGV_ready_1/AGV_ready_1.usdc
* BBox (world): size=(1.457, 0.340, 0.669), center=(11.182, 29.714, 0.279)
* 几何统计: Mesh=171, Vertices=1634024, Faces=683203
* 子Mesh材质: /World/agv_7/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_2/Object_0 -> 未绑定, /World/agv_7/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_3/Object_1 -> 未绑定, /World/agv_7/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_4/Object_2 -> 未绑定, /World/agv_7/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_5/Object_3 -> 未绑定, /World/agv_7/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_6/Object_4 -> 未绑定, /World/agv_7/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_7/Object_5 -> 未绑定, /World/agv_7/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_8/Object_6 -> 未绑定, /World/agv_7/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_9/Object_7 -> 未绑定, /World/agv_7/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_10/Object_8 -> 未绑定, /World/agv_7/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_11/Object_9 -> 未绑定, /World/agv_7/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_12/Object_10 -> 未绑定, /World/agv_7/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_13/Object_11 -> 未绑定, /World/agv_7/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_14/Object_12 -> 未绑定, /World/agv_7/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_15/Object_13 -> 未绑定, /World/agv_7/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_16/Object_14 -> 未绑定, /World/agv_7/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_17/Object_15 -> 未绑定, /World/agv_7/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_18/Object_16 -> 未绑定, /World/agv_7/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_19/Object_17 -> 未绑定, /World/agv_7/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_20/Object_18 -> 未绑定, /World/agv_7/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_21/Object_19 -> 未绑定, /World/agv_7/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_22/Object_20 -> 未绑定, /World/agv_7/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_23/Object_21 -> 未绑定, /World/agv_7/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_24/Object_22 -> 未绑定, /World/agv_7/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_25/Object_23 -> 未绑定, /World/agv_7/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_26/Object_24 -> 未绑定, /World/agv_7/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_27/Object_25 -> 未绑定, /World/agv_7/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_28/Object_26 -> 未绑定, /World/agv_7/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_29/Object_27 -> 未绑定, /World/agv_7/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_30/Object_28 -> 未绑定, /World/agv_7/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_31/Object_29 -> 未绑定, /World/agv_7/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_32/Object_30 -> 未绑定, /World/agv_7/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_33/Object_31 -> 未绑定, /World/agv_7/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_34/Object_32 -> 未绑定, /World/agv_7/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_35/Object_33 -> 未绑定, /World/agv_7/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_36/Object_34 -> 未绑定, /World/agv_7/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_37/Object_35 -> 未绑定, /World/agv_7/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_38/Object_36 -> 未绑定, /World/agv_7/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_39/Object_37 -> 未绑定, /World/agv_7/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_40/Object_38 -> 未绑定, /World/agv_7/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_41/Object_39 -> 未绑定, /World/agv_7/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_42/Object_40 -> 未绑定, /World/agv_7/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_43/Object_41 -> 未绑定, /World/agv_7/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_44/Object_42 -> 未绑定, /World/agv_7/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_45/Object_43 -> 未绑定, /World/agv_7/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_46/Object_44 -> 未绑定, /World/agv_7/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_47/Object_45 -> 未绑定, /World/agv_7/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_48/Object_46 -> 未绑定, /World/agv_7/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_49/Object_47 -> 未绑定, /World/agv_7/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_50/Object_48 -> 未绑定, /World/agv_7/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_51/Object_49 -> 未绑定, /World/agv_7/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_52/Object_50 -> 未绑定, /World/agv_7/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_53/Object_51 -> 未绑定, /World/agv_7/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_54/Object_52 -> 未绑定, /World/agv_7/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_55/Object_53 -> 未绑定, /World/agv_7/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_56/Object_54 -> 未绑定, /World/agv_7/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_57/Object_55 -> 未绑定, /World/agv_7/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_58/Object_56 -> 未绑定, /World/agv_7/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_59/Object_57 -> 未绑定, /World/agv_7/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_60/Object_58 -> 未绑定, /World/agv_7/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_61/Object_59 -> 未绑定, /World/agv_7/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_62/Object_60 -> 未绑定, /World/agv_7/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_63/Object_61 -> 未绑定, /World/agv_7/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_64/Object_62 -> 未绑定, /World/agv_7/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_65/Object_63 -> 未绑定, /World/agv_7/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_66/Object_64 -> 未绑定, /World/agv_7/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_67/Object_65 -> 未绑定, /World/agv_7/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_68/Object_66 -> 未绑定, /World/agv_7/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_69/Object_67 -> 未绑定, /World/agv_7/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_70/Object_68 -> 未绑定, /World/agv_7/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_71/Object_69 -> 未绑定, /World/agv_7/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_72/Object_70 -> 未绑定, /World/agv_7/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_73/Object_71 -> 未绑定, /World/agv_7/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_74/Object_72 -> 未绑定, /World/agv_7/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_75/Object_73 -> 未绑定, /World/agv_7/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_76/Object_74 -> 未绑定, /World/agv_7/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_77/Object_75 -> 未绑定, /World/agv_7/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_78/Object_76 -> 未绑定, /World/agv_7/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_79/Object_77 -> 未绑定, /World/agv_7/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_80/Object_78 -> 未绑定, /World/agv_7/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_81/Object_79 -> 未绑定, /World/agv_7/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_82/Object_80 -> 未绑定, /World/agv_7/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_83/Object_81 -> 未绑定, /World/agv_7/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_84/Object_82 -> 未绑定, /World/agv_7/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_85/Object_83 -> 未绑定, /World/agv_7/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_86/Object_84 -> 未绑定, /World/agv_7/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_87/Object_85 -> 未绑定, /World/agv_7/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_88/Object_86 -> 未绑定, /World/agv_7/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_89/Object_87 -> 未绑定, /World/agv_7/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_90/Object_88 -> 未绑定, /World/agv_7/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_91/Object_89 -> 未绑定, /World/agv_7/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_92/Object_90 -> 未绑定, /World/agv_7/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_93/Object_91 -> 未绑定, /World/agv_7/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_94/Object_92 -> 未绑定, /World/agv_7/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_95/Object_93 -> 未绑定, /World/agv_7/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_96/Object_94 -> 未绑定, /World/agv_7/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_97/Object_95 -> 未绑定, /World/agv_7/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_98/Object_96 -> 未绑定, /World/agv_7/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_99/Object_97 -> 未绑定, /World/agv_7/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_100/Object_98 -> 未绑定, /World/agv_7/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_101/Object_99 -> 未绑定, /World/agv_7/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_102/Object_100 -> 未绑定, /World/agv_7/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_103/Object_101 -> 未绑定, /World/agv_7/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_104/Object_102 -> 未绑定, /World/agv_7/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_105/Object_103 -> 未绑定, /World/agv_7/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_106/Object_104 -> 未绑定, /World/agv_7/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_107/Object_105 -> 未绑定, /World/agv_7/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_108/Object_106 -> 未绑定, /World/agv_7/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_109/Object_107 -> 未绑定, /World/agv_7/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_110/Object_108 -> 未绑定, /World/agv_7/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_111/Object_109 -> 未绑定, /World/agv_7/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_112/Object_110 -> 未绑定, /World/agv_7/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_113/Object_111 -> 未绑定, /World/agv_7/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_114/Object_112 -> 未绑定, /World/agv_7/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_115/Object_113 -> 未绑定, /World/agv_7/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_116/Object_114 -> 未绑定, /World/agv_7/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_117/Object_115 -> 未绑定, /World/agv_7/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_118/Object_116 -> 未绑定, /World/agv_7/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_119/Object_117 -> 未绑定, /World/agv_7/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_120/Object_118 -> 未绑定, /World/agv_7/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_121/Object_119 -> 未绑定, /World/agv_7/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_122/Object_120 -> 未绑定, /World/agv_7/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_123/Object_121 -> 未绑定, /World/agv_7/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_124/Object_122 -> 未绑定, /World/agv_7/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_125/Object_123 -> 未绑定, /World/agv_7/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_126/Object_124 -> 未绑定, /World/agv_7/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_127/Object_125 -> 未绑定, /World/agv_7/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_128/Object_126 -> 未绑定, /World/agv_7/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_129/Object_127 -> 未绑定, /World/agv_7/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_130/Object_128 -> 未绑定, /World/agv_7/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_131/Object_129 -> 未绑定, /World/agv_7/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_132/Object_130 -> 未绑定, /World/agv_7/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_133/Object_131 -> 未绑定, /World/agv_7/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_134/Object_132 -> 未绑定, /World/agv_7/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_135/Object_133 -> 未绑定, /World/agv_7/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_136/Object_134 -> 未绑定, /World/agv_7/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_137/Object_135 -> 未绑定, /World/agv_7/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_138/Object_136 -> 未绑定, /World/agv_7/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_139/Object_137 -> 未绑定, /World/agv_7/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_140/Object_138 -> 未绑定, /World/agv_7/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_141/Object_139 -> 未绑定, /World/agv_7/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_142/Object_140 -> 未绑定, /World/agv_7/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_143/Object_141 -> 未绑定, /World/agv_7/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_144/Object_142 -> 未绑定, /World/agv_7/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_145/Object_143 -> 未绑定, /World/agv_7/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_146/Object_144 -> 未绑定, /World/agv_7/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_147/Object_145 -> 未绑定, /World/agv_7/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_148/Object_146 -> 未绑定, /World/agv_7/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_149/Object_147 -> 未绑定, /World/agv_7/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_150/Object_148 -> 未绑定, /World/agv_7/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_151/Object_149 -> 未绑定, /World/agv_7/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_152/Object_150 -> 未绑定, /World/agv_7/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_153/Object_151 -> 未绑定, /World/agv_7/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_154/Object_152 -> 未绑定, /World/agv_7/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_155/Object_153 -> 未绑定, /World/agv_7/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_156/Object_154 -> 未绑定, /World/agv_7/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_157/Object_155 -> 未绑定, /World/agv_7/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_158/Object_156 -> 未绑定, /World/agv_7/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_159/Object_157 -> 未绑定, /World/agv_7/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_160/Object_158 -> 未绑定, /World/agv_7/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_161/Object_159 -> 未绑定, /World/agv_7/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_162/Object_160 -> 未绑定, /World/agv_7/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_163/Object_161 -> 未绑定, /World/agv_7/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_164/Object_162 -> 未绑定, /World/agv_7/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_165/Object_163 -> 未绑定, /World/agv_7/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_166/Object_164 -> 未绑定, /World/agv_7/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_167/Object_165 -> 未绑定, /World/agv_7/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_168/Object_166 -> 未绑定, /World/agv_7/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_169/Object_167 -> 未绑定, /World/agv_7/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_170/Object_168 -> 未绑定, /World/agv_7/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_171/Object_169 -> 未绑定, /World/agv_7/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_172/Object_170 -> 未绑定


---


### '/World/agv_8' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/AGV_ready_1/AGV_ready_1.usdc
* BBox (world): size=(1.457, 0.340, 0.669), center=(16.182, 29.714, 0.279)
* 几何统计: Mesh=171, Vertices=1634024, Faces=683203
* 子Mesh材质: /World/agv_8/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_2/Object_0 -> 未绑定, /World/agv_8/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_3/Object_1 -> 未绑定, /World/agv_8/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_4/Object_2 -> 未绑定, /World/agv_8/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_5/Object_3 -> 未绑定, /World/agv_8/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_6/Object_4 -> 未绑定, /World/agv_8/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_7/Object_5 -> 未绑定, /World/agv_8/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_8/Object_6 -> 未绑定, /World/agv_8/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_9/Object_7 -> 未绑定, /World/agv_8/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_10/Object_8 -> 未绑定, /World/agv_8/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_11/Object_9 -> 未绑定, /World/agv_8/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_12/Object_10 -> 未绑定, /World/agv_8/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_13/Object_11 -> 未绑定, /World/agv_8/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_14/Object_12 -> 未绑定, /World/agv_8/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_15/Object_13 -> 未绑定, /World/agv_8/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_16/Object_14 -> 未绑定, /World/agv_8/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_17/Object_15 -> 未绑定, /World/agv_8/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_18/Object_16 -> 未绑定, /World/agv_8/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_19/Object_17 -> 未绑定, /World/agv_8/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_20/Object_18 -> 未绑定, /World/agv_8/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_21/Object_19 -> 未绑定, /World/agv_8/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_22/Object_20 -> 未绑定, /World/agv_8/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_23/Object_21 -> 未绑定, /World/agv_8/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_24/Object_22 -> 未绑定, /World/agv_8/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_25/Object_23 -> 未绑定, /World/agv_8/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_26/Object_24 -> 未绑定, /World/agv_8/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_27/Object_25 -> 未绑定, /World/agv_8/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_28/Object_26 -> 未绑定, /World/agv_8/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_29/Object_27 -> 未绑定, /World/agv_8/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_30/Object_28 -> 未绑定, /World/agv_8/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_31/Object_29 -> 未绑定, /World/agv_8/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_32/Object_30 -> 未绑定, /World/agv_8/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_33/Object_31 -> 未绑定, /World/agv_8/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_34/Object_32 -> 未绑定, /World/agv_8/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_35/Object_33 -> 未绑定, /World/agv_8/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_36/Object_34 -> 未绑定, /World/agv_8/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_37/Object_35 -> 未绑定, /World/agv_8/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_38/Object_36 -> 未绑定, /World/agv_8/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_39/Object_37 -> 未绑定, /World/agv_8/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_40/Object_38 -> 未绑定, /World/agv_8/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_41/Object_39 -> 未绑定, /World/agv_8/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_42/Object_40 -> 未绑定, /World/agv_8/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_43/Object_41 -> 未绑定, /World/agv_8/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_44/Object_42 -> 未绑定, /World/agv_8/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_45/Object_43 -> 未绑定, /World/agv_8/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_46/Object_44 -> 未绑定, /World/agv_8/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_47/Object_45 -> 未绑定, /World/agv_8/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_48/Object_46 -> 未绑定, /World/agv_8/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_49/Object_47 -> 未绑定, /World/agv_8/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_50/Object_48 -> 未绑定, /World/agv_8/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_51/Object_49 -> 未绑定, /World/agv_8/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_52/Object_50 -> 未绑定, /World/agv_8/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_53/Object_51 -> 未绑定, /World/agv_8/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_54/Object_52 -> 未绑定, /World/agv_8/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_55/Object_53 -> 未绑定, /World/agv_8/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_56/Object_54 -> 未绑定, /World/agv_8/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_57/Object_55 -> 未绑定, /World/agv_8/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_58/Object_56 -> 未绑定, /World/agv_8/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_59/Object_57 -> 未绑定, /World/agv_8/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_60/Object_58 -> 未绑定, /World/agv_8/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_61/Object_59 -> 未绑定, /World/agv_8/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_62/Object_60 -> 未绑定, /World/agv_8/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_63/Object_61 -> 未绑定, /World/agv_8/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_64/Object_62 -> 未绑定, /World/agv_8/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_65/Object_63 -> 未绑定, /World/agv_8/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_66/Object_64 -> 未绑定, /World/agv_8/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_67/Object_65 -> 未绑定, /World/agv_8/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_68/Object_66 -> 未绑定, /World/agv_8/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_69/Object_67 -> 未绑定, /World/agv_8/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_70/Object_68 -> 未绑定, /World/agv_8/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_71/Object_69 -> 未绑定, /World/agv_8/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_72/Object_70 -> 未绑定, /World/agv_8/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_73/Object_71 -> 未绑定, /World/agv_8/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_74/Object_72 -> 未绑定, /World/agv_8/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_75/Object_73 -> 未绑定, /World/agv_8/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_76/Object_74 -> 未绑定, /World/agv_8/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_77/Object_75 -> 未绑定, /World/agv_8/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_78/Object_76 -> 未绑定, /World/agv_8/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_79/Object_77 -> 未绑定, /World/agv_8/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_80/Object_78 -> 未绑定, /World/agv_8/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_81/Object_79 -> 未绑定, /World/agv_8/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_82/Object_80 -> 未绑定, /World/agv_8/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_83/Object_81 -> 未绑定, /World/agv_8/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_84/Object_82 -> 未绑定, /World/agv_8/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_85/Object_83 -> 未绑定, /World/agv_8/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_86/Object_84 -> 未绑定, /World/agv_8/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_87/Object_85 -> 未绑定, /World/agv_8/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_88/Object_86 -> 未绑定, /World/agv_8/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_89/Object_87 -> 未绑定, /World/agv_8/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_90/Object_88 -> 未绑定, /World/agv_8/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_91/Object_89 -> 未绑定, /World/agv_8/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_92/Object_90 -> 未绑定, /World/agv_8/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_93/Object_91 -> 未绑定, /World/agv_8/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_94/Object_92 -> 未绑定, /World/agv_8/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_95/Object_93 -> 未绑定, /World/agv_8/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_96/Object_94 -> 未绑定, /World/agv_8/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_97/Object_95 -> 未绑定, /World/agv_8/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_98/Object_96 -> 未绑定, /World/agv_8/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_99/Object_97 -> 未绑定, /World/agv_8/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_100/Object_98 -> 未绑定, /World/agv_8/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_101/Object_99 -> 未绑定, /World/agv_8/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_102/Object_100 -> 未绑定, /World/agv_8/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_103/Object_101 -> 未绑定, /World/agv_8/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_104/Object_102 -> 未绑定, /World/agv_8/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_105/Object_103 -> 未绑定, /World/agv_8/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_106/Object_104 -> 未绑定, /World/agv_8/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_107/Object_105 -> 未绑定, /World/agv_8/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_108/Object_106 -> 未绑定, /World/agv_8/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_109/Object_107 -> 未绑定, /World/agv_8/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_110/Object_108 -> 未绑定, /World/agv_8/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_111/Object_109 -> 未绑定, /World/agv_8/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_112/Object_110 -> 未绑定, /World/agv_8/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_113/Object_111 -> 未绑定, /World/agv_8/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_114/Object_112 -> 未绑定, /World/agv_8/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_115/Object_113 -> 未绑定, /World/agv_8/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_116/Object_114 -> 未绑定, /World/agv_8/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_117/Object_115 -> 未绑定, /World/agv_8/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_118/Object_116 -> 未绑定, /World/agv_8/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_119/Object_117 -> 未绑定, /World/agv_8/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_120/Object_118 -> 未绑定, /World/agv_8/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_121/Object_119 -> 未绑定, /World/agv_8/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_122/Object_120 -> 未绑定, /World/agv_8/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_123/Object_121 -> 未绑定, /World/agv_8/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_124/Object_122 -> 未绑定, /World/agv_8/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_125/Object_123 -> 未绑定, /World/agv_8/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_126/Object_124 -> 未绑定, /World/agv_8/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_127/Object_125 -> 未绑定, /World/agv_8/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_128/Object_126 -> 未绑定, /World/agv_8/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_129/Object_127 -> 未绑定, /World/agv_8/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_130/Object_128 -> 未绑定, /World/agv_8/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_131/Object_129 -> 未绑定, /World/agv_8/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_132/Object_130 -> 未绑定, /World/agv_8/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_133/Object_131 -> 未绑定, /World/agv_8/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_134/Object_132 -> 未绑定, /World/agv_8/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_135/Object_133 -> 未绑定, /World/agv_8/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_136/Object_134 -> 未绑定, /World/agv_8/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_137/Object_135 -> 未绑定, /World/agv_8/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_138/Object_136 -> 未绑定, /World/agv_8/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_139/Object_137 -> 未绑定, /World/agv_8/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_140/Object_138 -> 未绑定, /World/agv_8/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_141/Object_139 -> 未绑定, /World/agv_8/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_142/Object_140 -> 未绑定, /World/agv_8/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_143/Object_141 -> 未绑定, /World/agv_8/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_144/Object_142 -> 未绑定, /World/agv_8/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_145/Object_143 -> 未绑定, /World/agv_8/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_146/Object_144 -> 未绑定, /World/agv_8/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_147/Object_145 -> 未绑定, /World/agv_8/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_148/Object_146 -> 未绑定, /World/agv_8/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_149/Object_147 -> 未绑定, /World/agv_8/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_150/Object_148 -> 未绑定, /World/agv_8/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_151/Object_149 -> 未绑定, /World/agv_8/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_152/Object_150 -> 未绑定, /World/agv_8/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_153/Object_151 -> 未绑定, /World/agv_8/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_154/Object_152 -> 未绑定, /World/agv_8/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_155/Object_153 -> 未绑定, /World/agv_8/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_156/Object_154 -> 未绑定, /World/agv_8/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_157/Object_155 -> 未绑定, /World/agv_8/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_158/Object_156 -> 未绑定, /World/agv_8/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_159/Object_157 -> 未绑定, /World/agv_8/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_160/Object_158 -> 未绑定, /World/agv_8/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_161/Object_159 -> 未绑定, /World/agv_8/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_162/Object_160 -> 未绑定, /World/agv_8/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_163/Object_161 -> 未绑定, /World/agv_8/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_164/Object_162 -> 未绑定, /World/agv_8/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_165/Object_163 -> 未绑定, /World/agv_8/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_166/Object_164 -> 未绑定, /World/agv_8/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_167/Object_165 -> 未绑定, /World/agv_8/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_168/Object_166 -> 未绑定, /World/agv_8/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_169/Object_167 -> 未绑定, /World/agv_8/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_170/Object_168 -> 未绑定, /World/agv_8/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_171/Object_169 -> 未绑定, /World/agv_8/Meshes/Sketchfab_model/AGV_ready_1_obj_cleaner_materialmerger_gles/Object_172/Object_170 -> 未绑定


---


### '/World/Conveyor_1' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/Simple_rubber_conveyor/Simple_rubber_conveyor.usdc
* BBox (world): size=(188.440, 149.880, 400.080), center=(-19.029, 26.500, 0.889)
* 几何统计: Mesh=5, Vertices=11335, Faces=9195
* 子Mesh材质: /World/Conveyor_1/Meshes/Sketchfab_model/Conveyor_FBX/RootNode/Conveyor01Frame/Conveyor01Frame_Conveyor_0/Conveyor01Frame_Conveyor_0 -> 未绑定, /World/Conveyor_1/Meshes/Sketchfab_model/Conveyor_FBX/RootNode/Conveyor01Frame01/Conveyor01Frame01_Conveyor_0/Conveyor01Frame01_Conveyor_0 -> 未绑定, /World/Conveyor_1/Meshes/Sketchfab_model/Conveyor_FBX/RootNode/Conveyor01Frame02/Conveyor01Frame02_Conveyor_0/Conveyor01Frame02_Conveyor_0 -> 未绑定, /World/Conveyor_1/Meshes/Sketchfab_model/Conveyor_FBX/RootNode/Conveyor01Legs/Conveyor01Legs_Conveyor_0/Conveyor01Legs_Conveyor_0 -> 未绑定, /World/Conveyor_1/Meshes/Sketchfab_model/Conveyor_FBX/RootNode/Conveyor01Belt/Conveyor01Belt_Belt_0/Conveyor01Belt_Belt_0 -> 未绑定


---


### '/World/Conveyor_2' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/Simple_rubber_conveyor/Simple_rubber_conveyor.usdc
* BBox (world): size=(188.440, 149.880, 400.080), center=(-14.029, 26.500, 0.889)
* 几何统计: Mesh=5, Vertices=11335, Faces=9195
* 子Mesh材质: /World/Conveyor_2/Meshes/Sketchfab_model/Conveyor_FBX/RootNode/Conveyor01Frame/Conveyor01Frame_Conveyor_0/Conveyor01Frame_Conveyor_0 -> 未绑定, /World/Conveyor_2/Meshes/Sketchfab_model/Conveyor_FBX/RootNode/Conveyor01Frame01/Conveyor01Frame01_Conveyor_0/Conveyor01Frame01_Conveyor_0 -> 未绑定, /World/Conveyor_2/Meshes/Sketchfab_model/Conveyor_FBX/RootNode/Conveyor01Frame02/Conveyor01Frame02_Conveyor_0/Conveyor01Frame02_Conveyor_0 -> 未绑定, /World/Conveyor_2/Meshes/Sketchfab_model/Conveyor_FBX/RootNode/Conveyor01Legs/Conveyor01Legs_Conveyor_0/Conveyor01Legs_Conveyor_0 -> 未绑定, /World/Conveyor_2/Meshes/Sketchfab_model/Conveyor_FBX/RootNode/Conveyor01Belt/Conveyor01Belt_Belt_0/Conveyor01Belt_Belt_0 -> 未绑定


---


### '/World/Conveyor_3' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/Simple_rubber_conveyor/Simple_rubber_conveyor.usdc
* BBox (world): size=(188.440, 149.880, 400.080), center=(-9.029, 26.500, 0.889)
* 几何统计: Mesh=5, Vertices=11335, Faces=9195
* 子Mesh材质: /World/Conveyor_3/Meshes/Sketchfab_model/Conveyor_FBX/RootNode/Conveyor01Frame/Conveyor01Frame_Conveyor_0/Conveyor01Frame_Conveyor_0 -> 未绑定, /World/Conveyor_3/Meshes/Sketchfab_model/Conveyor_FBX/RootNode/Conveyor01Frame01/Conveyor01Frame01_Conveyor_0/Conveyor01Frame01_Conveyor_0 -> 未绑定, /World/Conveyor_3/Meshes/Sketchfab_model/Conveyor_FBX/RootNode/Conveyor01Frame02/Conveyor01Frame02_Conveyor_0/Conveyor01Frame02_Conveyor_0 -> 未绑定, /World/Conveyor_3/Meshes/Sketchfab_model/Conveyor_FBX/RootNode/Conveyor01Legs/Conveyor01Legs_Conveyor_0/Conveyor01Legs_Conveyor_0 -> 未绑定, /World/Conveyor_3/Meshes/Sketchfab_model/Conveyor_FBX/RootNode/Conveyor01Belt/Conveyor01Belt_Belt_0/Conveyor01Belt_Belt_0 -> 未绑定


---


### '/World/Conveyor_4' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/Simple_rubber_conveyor/Simple_rubber_conveyor.usdc
* BBox (world): size=(188.440, 149.880, 400.080), center=(-4.029, 26.500, 0.889)
* 几何统计: Mesh=5, Vertices=11335, Faces=9195
* 子Mesh材质: /World/Conveyor_4/Meshes/Sketchfab_model/Conveyor_FBX/RootNode/Conveyor01Frame/Conveyor01Frame_Conveyor_0/Conveyor01Frame_Conveyor_0 -> 未绑定, /World/Conveyor_4/Meshes/Sketchfab_model/Conveyor_FBX/RootNode/Conveyor01Frame01/Conveyor01Frame01_Conveyor_0/Conveyor01Frame01_Conveyor_0 -> 未绑定, /World/Conveyor_4/Meshes/Sketchfab_model/Conveyor_FBX/RootNode/Conveyor01Frame02/Conveyor01Frame02_Conveyor_0/Conveyor01Frame02_Conveyor_0 -> 未绑定, /World/Conveyor_4/Meshes/Sketchfab_model/Conveyor_FBX/RootNode/Conveyor01Legs/Conveyor01Legs_Conveyor_0/Conveyor01Legs_Conveyor_0 -> 未绑定, /World/Conveyor_4/Meshes/Sketchfab_model/Conveyor_FBX/RootNode/Conveyor01Belt/Conveyor01Belt_Belt_0/Conveyor01Belt_Belt_0 -> 未绑定


---


### '/World/Conveyor_5' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/Simple_rubber_conveyor/Simple_rubber_conveyor.usdc
* BBox (world): size=(188.440, 149.880, 400.080), center=(0.971, 26.500, 0.889)
* 几何统计: Mesh=5, Vertices=11335, Faces=9195
* 子Mesh材质: /World/Conveyor_5/Meshes/Sketchfab_model/Conveyor_FBX/RootNode/Conveyor01Frame/Conveyor01Frame_Conveyor_0/Conveyor01Frame_Conveyor_0 -> 未绑定, /World/Conveyor_5/Meshes/Sketchfab_model/Conveyor_FBX/RootNode/Conveyor01Frame01/Conveyor01Frame01_Conveyor_0/Conveyor01Frame01_Conveyor_0 -> 未绑定, /World/Conveyor_5/Meshes/Sketchfab_model/Conveyor_FBX/RootNode/Conveyor01Frame02/Conveyor01Frame02_Conveyor_0/Conveyor01Frame02_Conveyor_0 -> 未绑定, /World/Conveyor_5/Meshes/Sketchfab_model/Conveyor_FBX/RootNode/Conveyor01Legs/Conveyor01Legs_Conveyor_0/Conveyor01Legs_Conveyor_0 -> 未绑定, /World/Conveyor_5/Meshes/Sketchfab_model/Conveyor_FBX/RootNode/Conveyor01Belt/Conveyor01Belt_Belt_0/Conveyor01Belt_Belt_0 -> 未绑定


---


### '/World/Conveyor_6' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/Simple_rubber_conveyor/Simple_rubber_conveyor.usdc
* BBox (world): size=(188.440, 149.880, 400.080), center=(5.971, 26.500, 0.889)
* 几何统计: Mesh=5, Vertices=11335, Faces=9195
* 子Mesh材质: /World/Conveyor_6/Meshes/Sketchfab_model/Conveyor_FBX/RootNode/Conveyor01Frame/Conveyor01Frame_Conveyor_0/Conveyor01Frame_Conveyor_0 -> 未绑定, /World/Conveyor_6/Meshes/Sketchfab_model/Conveyor_FBX/RootNode/Conveyor01Frame01/Conveyor01Frame01_Conveyor_0/Conveyor01Frame01_Conveyor_0 -> 未绑定, /World/Conveyor_6/Meshes/Sketchfab_model/Conveyor_FBX/RootNode/Conveyor01Frame02/Conveyor01Frame02_Conveyor_0/Conveyor01Frame02_Conveyor_0 -> 未绑定, /World/Conveyor_6/Meshes/Sketchfab_model/Conveyor_FBX/RootNode/Conveyor01Legs/Conveyor01Legs_Conveyor_0/Conveyor01Legs_Conveyor_0 -> 未绑定, /World/Conveyor_6/Meshes/Sketchfab_model/Conveyor_FBX/RootNode/Conveyor01Belt/Conveyor01Belt_Belt_0/Conveyor01Belt_Belt_0 -> 未绑定


---


### '/World/Conveyor_7' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/Simple_rubber_conveyor/Simple_rubber_conveyor.usdc
* BBox (world): size=(188.440, 149.880, 400.080), center=(10.971, 26.500, 0.889)
* 几何统计: Mesh=5, Vertices=11335, Faces=9195
* 子Mesh材质: /World/Conveyor_7/Meshes/Sketchfab_model/Conveyor_FBX/RootNode/Conveyor01Frame/Conveyor01Frame_Conveyor_0/Conveyor01Frame_Conveyor_0 -> 未绑定, /World/Conveyor_7/Meshes/Sketchfab_model/Conveyor_FBX/RootNode/Conveyor01Frame01/Conveyor01Frame01_Conveyor_0/Conveyor01Frame01_Conveyor_0 -> 未绑定, /World/Conveyor_7/Meshes/Sketchfab_model/Conveyor_FBX/RootNode/Conveyor01Frame02/Conveyor01Frame02_Conveyor_0/Conveyor01Frame02_Conveyor_0 -> 未绑定, /World/Conveyor_7/Meshes/Sketchfab_model/Conveyor_FBX/RootNode/Conveyor01Legs/Conveyor01Legs_Conveyor_0/Conveyor01Legs_Conveyor_0 -> 未绑定, /World/Conveyor_7/Meshes/Sketchfab_model/Conveyor_FBX/RootNode/Conveyor01Belt/Conveyor01Belt_Belt_0/Conveyor01Belt_Belt_0 -> 未绑定


---


### '/World/Conveyor_8' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/Simple_rubber_conveyor/Simple_rubber_conveyor.usdc
* BBox (world): size=(188.440, 149.880, 400.080), center=(15.971, 26.500, 0.889)
* 几何统计: Mesh=5, Vertices=11335, Faces=9195
* 子Mesh材质: /World/Conveyor_8/Meshes/Sketchfab_model/Conveyor_FBX/RootNode/Conveyor01Frame/Conveyor01Frame_Conveyor_0/Conveyor01Frame_Conveyor_0 -> 未绑定, /World/Conveyor_8/Meshes/Sketchfab_model/Conveyor_FBX/RootNode/Conveyor01Frame01/Conveyor01Frame01_Conveyor_0/Conveyor01Frame01_Conveyor_0 -> 未绑定, /World/Conveyor_8/Meshes/Sketchfab_model/Conveyor_FBX/RootNode/Conveyor01Frame02/Conveyor01Frame02_Conveyor_0/Conveyor01Frame02_Conveyor_0 -> 未绑定, /World/Conveyor_8/Meshes/Sketchfab_model/Conveyor_FBX/RootNode/Conveyor01Legs/Conveyor01Legs_Conveyor_0/Conveyor01Legs_Conveyor_0 -> 未绑定, /World/Conveyor_8/Meshes/Sketchfab_model/Conveyor_FBX/RootNode/Conveyor01Belt/Conveyor01Belt_Belt_0/Conveyor01Belt_Belt_0 -> 未绑定


---


### '/World/BoxOnConveyor_1' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc
* BBox (world): size=(35.888, 35.888, 35.888), center=(-19.000, 25.600, 1.751)
* 几何统计: Mesh=1, Vertices=56, Faces=44
* 子Mesh材质: /World/BoxOnConveyor_1/Meshes/Sketchfab_model/f49ad5edc352496894d3a02181012422_fbx/RootNode/Box072/Box072_06___Default_0/Box072_06___Default_0 -> 未绑定


---


### '/World/BoxOnConveyor_2' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc
* BBox (world): size=(35.888, 35.888, 35.888), center=(-14.000, 25.600, 1.751)
* 几何统计: Mesh=1, Vertices=56, Faces=44
* 子Mesh材质: /World/BoxOnConveyor_2/Meshes/Sketchfab_model/f49ad5edc352496894d3a02181012422_fbx/RootNode/Box072/Box072_06___Default_0/Box072_06___Default_0 -> 未绑定


---


### '/World/BoxOnConveyor_3' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc
* BBox (world): size=(35.888, 35.888, 35.888), center=(-9.000, 25.600, 1.751)
* 几何统计: Mesh=1, Vertices=56, Faces=44
* 子Mesh材质: /World/BoxOnConveyor_3/Meshes/Sketchfab_model/f49ad5edc352496894d3a02181012422_fbx/RootNode/Box072/Box072_06___Default_0/Box072_06___Default_0 -> 未绑定


---


### '/World/BoxOnConveyor_4' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc
* BBox (world): size=(35.888, 35.888, 35.888), center=(-4.000, 25.600, 1.751)
* 几何统计: Mesh=1, Vertices=56, Faces=44
* 子Mesh材质: /World/BoxOnConveyor_4/Meshes/Sketchfab_model/f49ad5edc352496894d3a02181012422_fbx/RootNode/Box072/Box072_06___Default_0/Box072_06___Default_0 -> 未绑定


---


### '/World/BoxOnConveyor_5' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc
* BBox (world): size=(35.888, 35.888, 35.888), center=(1.000, 25.600, 1.751)
* 几何统计: Mesh=1, Vertices=56, Faces=44
* 子Mesh材质: /World/BoxOnConveyor_5/Meshes/Sketchfab_model/f49ad5edc352496894d3a02181012422_fbx/RootNode/Box072/Box072_06___Default_0/Box072_06___Default_0 -> 未绑定


---


### '/World/BoxOnConveyor_6' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc
* BBox (world): size=(35.888, 35.888, 35.888), center=(6.000, 25.600, 1.751)
* 几何统计: Mesh=1, Vertices=56, Faces=44
* 子Mesh材质: /World/BoxOnConveyor_6/Meshes/Sketchfab_model/f49ad5edc352496894d3a02181012422_fbx/RootNode/Box072/Box072_06___Default_0/Box072_06___Default_0 -> 未绑定


---


### '/World/BoxOnConveyor_7' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc
* BBox (world): size=(35.888, 35.888, 35.888), center=(11.000, 25.600, 1.751)
* 几何统计: Mesh=1, Vertices=56, Faces=44
* 子Mesh材质: /World/BoxOnConveyor_7/Meshes/Sketchfab_model/f49ad5edc352496894d3a02181012422_fbx/RootNode/Box072/Box072_06___Default_0/Box072_06___Default_0 -> 未绑定


---


### '/World/BoxOnConveyor_8' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc
* BBox (world): size=(35.888, 35.888, 35.888), center=(16.000, 25.600, 1.751)
* 几何统计: Mesh=1, Vertices=56, Faces=44
* 子Mesh材质: /World/BoxOnConveyor_8/Meshes/Sketchfab_model/f49ad5edc352496894d3a02181012422_fbx/RootNode/Box072/Box072_06___Default_0/Box072_06___Default_0 -> 未绑定


---


### '/World/BoxOnConveyor_1_1' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc
* BBox (world): size=(35.888, 35.888, 35.888), center=(-19.000, 26.500, 1.751)
* 几何统计: Mesh=1, Vertices=56, Faces=44
* 子Mesh材质: /World/BoxOnConveyor_1_1/Meshes/Sketchfab_model/f49ad5edc352496894d3a02181012422_fbx/RootNode/Box072/Box072_06___Default_0/Box072_06___Default_0 -> 未绑定


---


### '/World/BoxOnConveyor_1_2' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc
* BBox (world): size=(35.888, 35.888, 35.888), center=(-14.000, 26.500, 1.751)
* 几何统计: Mesh=1, Vertices=56, Faces=44
* 子Mesh材质: /World/BoxOnConveyor_1_2/Meshes/Sketchfab_model/f49ad5edc352496894d3a02181012422_fbx/RootNode/Box072/Box072_06___Default_0/Box072_06___Default_0 -> 未绑定


---


### '/World/BoxOnConveyor_1_3' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc
* BBox (world): size=(35.888, 35.888, 35.888), center=(-9.000, 26.500, 1.751)
* 几何统计: Mesh=1, Vertices=56, Faces=44
* 子Mesh材质: /World/BoxOnConveyor_1_3/Meshes/Sketchfab_model/f49ad5edc352496894d3a02181012422_fbx/RootNode/Box072/Box072_06___Default_0/Box072_06___Default_0 -> 未绑定


---


### '/World/BoxOnConveyor_1_4' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc
* BBox (world): size=(35.888, 35.888, 35.888), center=(-4.000, 26.500, 1.751)
* 几何统计: Mesh=1, Vertices=56, Faces=44
* 子Mesh材质: /World/BoxOnConveyor_1_4/Meshes/Sketchfab_model/f49ad5edc352496894d3a02181012422_fbx/RootNode/Box072/Box072_06___Default_0/Box072_06___Default_0 -> 未绑定


---


### '/World/BoxOnConveyor_1_5' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc
* BBox (world): size=(35.888, 35.888, 35.888), center=(1.000, 26.500, 1.751)
* 几何统计: Mesh=1, Vertices=56, Faces=44
* 子Mesh材质: /World/BoxOnConveyor_1_5/Meshes/Sketchfab_model/f49ad5edc352496894d3a02181012422_fbx/RootNode/Box072/Box072_06___Default_0/Box072_06___Default_0 -> 未绑定


---


### '/World/BoxOnConveyor_1_6' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc
* BBox (world): size=(35.888, 35.888, 35.888), center=(6.000, 26.500, 1.751)
* 几何统计: Mesh=1, Vertices=56, Faces=44
* 子Mesh材质: /World/BoxOnConveyor_1_6/Meshes/Sketchfab_model/f49ad5edc352496894d3a02181012422_fbx/RootNode/Box072/Box072_06___Default_0/Box072_06___Default_0 -> 未绑定


---


### '/World/BoxOnConveyor_1_7' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc
* BBox (world): size=(35.888, 35.888, 35.888), center=(11.000, 26.500, 1.751)
* 几何统计: Mesh=1, Vertices=56, Faces=44
* 子Mesh材质: /World/BoxOnConveyor_1_7/Meshes/Sketchfab_model/f49ad5edc352496894d3a02181012422_fbx/RootNode/Box072/Box072_06___Default_0/Box072_06___Default_0 -> 未绑定


---


### '/World/BoxOnConveyor_1_8' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc
* BBox (world): size=(35.888, 35.888, 35.888), center=(16.000, 26.500, 1.751)
* 几何统计: Mesh=1, Vertices=56, Faces=44
* 子Mesh材质: /World/BoxOnConveyor_1_8/Meshes/Sketchfab_model/f49ad5edc352496894d3a02181012422_fbx/RootNode/Box072/Box072_06___Default_0/Box072_06___Default_0 -> 未绑定


---


### '/World/BoxOnConveyor_2_1' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc
* BBox (world): size=(35.888, 35.888, 35.888), center=(-19.000, 27.400, 1.751)
* 几何统计: Mesh=1, Vertices=56, Faces=44
* 子Mesh材质: /World/BoxOnConveyor_2_1/Meshes/Sketchfab_model/f49ad5edc352496894d3a02181012422_fbx/RootNode/Box072/Box072_06___Default_0/Box072_06___Default_0 -> 未绑定


---


### '/World/BoxOnConveyor_2_2' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc
* BBox (world): size=(35.888, 35.888, 35.888), center=(-14.000, 27.400, 1.751)
* 几何统计: Mesh=1, Vertices=56, Faces=44
* 子Mesh材质: /World/BoxOnConveyor_2_2/Meshes/Sketchfab_model/f49ad5edc352496894d3a02181012422_fbx/RootNode/Box072/Box072_06___Default_0/Box072_06___Default_0 -> 未绑定


---


### '/World/BoxOnConveyor_2_3' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc
* BBox (world): size=(35.888, 35.888, 35.888), center=(-9.000, 27.400, 1.751)
* 几何统计: Mesh=1, Vertices=56, Faces=44
* 子Mesh材质: /World/BoxOnConveyor_2_3/Meshes/Sketchfab_model/f49ad5edc352496894d3a02181012422_fbx/RootNode/Box072/Box072_06___Default_0/Box072_06___Default_0 -> 未绑定


---


### '/World/BoxOnConveyor_2_4' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc
* BBox (world): size=(35.888, 35.888, 35.888), center=(-4.000, 27.400, 1.751)
* 几何统计: Mesh=1, Vertices=56, Faces=44
* 子Mesh材质: /World/BoxOnConveyor_2_4/Meshes/Sketchfab_model/f49ad5edc352496894d3a02181012422_fbx/RootNode/Box072/Box072_06___Default_0/Box072_06___Default_0 -> 未绑定


---


### '/World/BoxOnConveyor_2_5' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc
* BBox (world): size=(35.888, 35.888, 35.888), center=(1.000, 27.400, 1.751)
* 几何统计: Mesh=1, Vertices=56, Faces=44
* 子Mesh材质: /World/BoxOnConveyor_2_5/Meshes/Sketchfab_model/f49ad5edc352496894d3a02181012422_fbx/RootNode/Box072/Box072_06___Default_0/Box072_06___Default_0 -> 未绑定


---


### '/World/BoxOnConveyor_2_6' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc
* BBox (world): size=(35.888, 35.888, 35.888), center=(6.000, 27.400, 1.751)
* 几何统计: Mesh=1, Vertices=56, Faces=44
* 子Mesh材质: /World/BoxOnConveyor_2_6/Meshes/Sketchfab_model/f49ad5edc352496894d3a02181012422_fbx/RootNode/Box072/Box072_06___Default_0/Box072_06___Default_0 -> 未绑定


---


### '/World/BoxOnConveyor_2_7' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc
* BBox (world): size=(35.888, 35.888, 35.888), center=(11.000, 27.400, 1.751)
* 几何统计: Mesh=1, Vertices=56, Faces=44
* 子Mesh材质: /World/BoxOnConveyor_2_7/Meshes/Sketchfab_model/f49ad5edc352496894d3a02181012422_fbx/RootNode/Box072/Box072_06___Default_0/Box072_06___Default_0 -> 未绑定


---


### '/World/BoxOnConveyor_2_8' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc
* BBox (world): size=(35.888, 35.888, 35.888), center=(16.000, 27.400, 1.751)
* 几何统计: Mesh=1, Vertices=56, Faces=44
* 子Mesh材质: /World/BoxOnConveyor_2_8/Meshes/Sketchfab_model/f49ad5edc352496894d3a02181012422_fbx/RootNode/Box072/Box072_06___Default_0/Box072_06___Default_0 -> 未绑定


---


### '/World/BoxOnConveyor_3_1' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc
* BBox (world): size=(35.888, 35.888, 35.888), center=(-19.000, 28.300, 1.751)
* 几何统计: Mesh=1, Vertices=56, Faces=44
* 子Mesh材质: /World/BoxOnConveyor_3_1/Meshes/Sketchfab_model/f49ad5edc352496894d3a02181012422_fbx/RootNode/Box072/Box072_06___Default_0/Box072_06___Default_0 -> 未绑定


---


### '/World/BoxOnConveyor_3_2' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc
* BBox (world): size=(35.888, 35.888, 35.888), center=(-14.000, 28.300, 1.751)
* 几何统计: Mesh=1, Vertices=56, Faces=44
* 子Mesh材质: /World/BoxOnConveyor_3_2/Meshes/Sketchfab_model/f49ad5edc352496894d3a02181012422_fbx/RootNode/Box072/Box072_06___Default_0/Box072_06___Default_0 -> 未绑定


---


### '/World/BoxOnConveyor_3_3' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc
* BBox (world): size=(35.888, 35.888, 35.888), center=(-9.000, 28.300, 1.751)
* 几何统计: Mesh=1, Vertices=56, Faces=44
* 子Mesh材质: /World/BoxOnConveyor_3_3/Meshes/Sketchfab_model/f49ad5edc352496894d3a02181012422_fbx/RootNode/Box072/Box072_06___Default_0/Box072_06___Default_0 -> 未绑定


---


### '/World/BoxOnConveyor_3_4' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc
* BBox (world): size=(35.888, 35.888, 35.888), center=(-4.000, 28.300, 1.751)
* 几何统计: Mesh=1, Vertices=56, Faces=44
* 子Mesh材质: /World/BoxOnConveyor_3_4/Meshes/Sketchfab_model/f49ad5edc352496894d3a02181012422_fbx/RootNode/Box072/Box072_06___Default_0/Box072_06___Default_0 -> 未绑定


---


### '/World/BoxOnConveyor_3_5' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc
* BBox (world): size=(35.888, 35.888, 35.888), center=(1.000, 28.300, 1.751)
* 几何统计: Mesh=1, Vertices=56, Faces=44
* 子Mesh材质: /World/BoxOnConveyor_3_5/Meshes/Sketchfab_model/f49ad5edc352496894d3a02181012422_fbx/RootNode/Box072/Box072_06___Default_0/Box072_06___Default_0 -> 未绑定


---


### '/World/BoxOnConveyor_3_6' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc
* BBox (world): size=(35.888, 35.888, 35.888), center=(6.000, 28.300, 1.751)
* 几何统计: Mesh=1, Vertices=56, Faces=44
* 子Mesh材质: /World/BoxOnConveyor_3_6/Meshes/Sketchfab_model/f49ad5edc352496894d3a02181012422_fbx/RootNode/Box072/Box072_06___Default_0/Box072_06___Default_0 -> 未绑定


---


### '/World/BoxOnConveyor_3_7' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc
* BBox (world): size=(35.888, 35.888, 35.888), center=(11.000, 28.300, 1.751)
* 几何统计: Mesh=1, Vertices=56, Faces=44
* 子Mesh材质: /World/BoxOnConveyor_3_7/Meshes/Sketchfab_model/f49ad5edc352496894d3a02181012422_fbx/RootNode/Box072/Box072_06___Default_0/Box072_06___Default_0 -> 未绑定


---


### '/World/BoxOnConveyor_3_8' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc
* BBox (world): size=(35.888, 35.888, 35.888), center=(16.000, 28.300, 1.751)
* 几何统计: Mesh=1, Vertices=56, Faces=44
* 子Mesh材质: /World/BoxOnConveyor_3_8/Meshes/Sketchfab_model/f49ad5edc352496894d3a02181012422_fbx/RootNode/Box072/Box072_06___Default_0/Box072_06___Default_0 -> 未绑定


---


### '/World/StackedCarton_1' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc
* BBox (world): size=(35.888, 35.888, 35.888), center=(-18.800, 29.300, 0.631)
* 几何统计: Mesh=1, Vertices=56, Faces=44
* 子Mesh材质: /World/StackedCarton_1/Meshes/Sketchfab_model/f49ad5edc352496894d3a02181012422_fbx/RootNode/Box072/Box072_06___Default_0/Box072_06___Default_0 -> 未绑定


---


### '/World/StackedCarton_2' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc
* BBox (world): size=(35.888, 35.888, 35.888), center=(-13.800, 29.300, 0.631)
* 几何统计: Mesh=1, Vertices=56, Faces=44
* 子Mesh材质: /World/StackedCarton_2/Meshes/Sketchfab_model/f49ad5edc352496894d3a02181012422_fbx/RootNode/Box072/Box072_06___Default_0/Box072_06___Default_0 -> 未绑定


---


### '/World/StackedCarton_3' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc
* BBox (world): size=(35.888, 35.888, 35.888), center=(-8.800, 29.300, 0.631)
* 几何统计: Mesh=1, Vertices=56, Faces=44
* 子Mesh材质: /World/StackedCarton_3/Meshes/Sketchfab_model/f49ad5edc352496894d3a02181012422_fbx/RootNode/Box072/Box072_06___Default_0/Box072_06___Default_0 -> 未绑定


---


### '/World/StackedCarton_4' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc
* BBox (world): size=(35.888, 35.888, 35.888), center=(-3.800, 29.300, 0.631)
* 几何统计: Mesh=1, Vertices=56, Faces=44
* 子Mesh材质: /World/StackedCarton_4/Meshes/Sketchfab_model/f49ad5edc352496894d3a02181012422_fbx/RootNode/Box072/Box072_06___Default_0/Box072_06___Default_0 -> 未绑定


---


### '/World/StackedCarton_5' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc
* BBox (world): size=(35.888, 35.888, 35.888), center=(1.200, 29.300, 0.631)
* 几何统计: Mesh=1, Vertices=56, Faces=44
* 子Mesh材质: /World/StackedCarton_5/Meshes/Sketchfab_model/f49ad5edc352496894d3a02181012422_fbx/RootNode/Box072/Box072_06___Default_0/Box072_06___Default_0 -> 未绑定


---


### '/World/StackedCarton_6' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc
* BBox (world): size=(35.888, 35.888, 35.888), center=(6.200, 29.300, 0.631)
* 几何统计: Mesh=1, Vertices=56, Faces=44
* 子Mesh材质: /World/StackedCarton_6/Meshes/Sketchfab_model/f49ad5edc352496894d3a02181012422_fbx/RootNode/Box072/Box072_06___Default_0/Box072_06___Default_0 -> 未绑定


---


### '/World/StackedCarton_7' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc
* BBox (world): size=(35.888, 35.888, 35.888), center=(11.200, 29.300, 0.631)
* 几何统计: Mesh=1, Vertices=56, Faces=44
* 子Mesh材质: /World/StackedCarton_7/Meshes/Sketchfab_model/f49ad5edc352496894d3a02181012422_fbx/RootNode/Box072/Box072_06___Default_0/Box072_06___Default_0 -> 未绑定


---


### '/World/StackedCarton_8' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc
* BBox (world): size=(35.888, 35.888, 35.888), center=(16.200, 29.300, 0.631)
* 几何统计: Mesh=1, Vertices=56, Faces=44
* 子Mesh材质: /World/StackedCarton_8/Meshes/Sketchfab_model/f49ad5edc352496894d3a02181012422_fbx/RootNode/Box072/Box072_06___Default_0/Box072_06___Default_0 -> 未绑定


---


### '/World/StackedCarton_1_1' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc
* BBox (world): size=(35.888, 35.888, 35.888), center=(-18.800, 29.700, 0.631)
* 几何统计: Mesh=1, Vertices=56, Faces=44
* 子Mesh材质: /World/StackedCarton_1_1/Meshes/Sketchfab_model/f49ad5edc352496894d3a02181012422_fbx/RootNode/Box072/Box072_06___Default_0/Box072_06___Default_0 -> 未绑定


---


### '/World/StackedCarton_1_2' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc
* BBox (world): size=(35.888, 35.888, 35.888), center=(-13.800, 29.700, 0.631)
* 几何统计: Mesh=1, Vertices=56, Faces=44
* 子Mesh材质: /World/StackedCarton_1_2/Meshes/Sketchfab_model/f49ad5edc352496894d3a02181012422_fbx/RootNode/Box072/Box072_06___Default_0/Box072_06___Default_0 -> 未绑定


---


### '/World/StackedCarton_1_3' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc
* BBox (world): size=(35.888, 35.888, 35.888), center=(-8.800, 29.700, 0.631)
* 几何统计: Mesh=1, Vertices=56, Faces=44
* 子Mesh材质: /World/StackedCarton_1_3/Meshes/Sketchfab_model/f49ad5edc352496894d3a02181012422_fbx/RootNode/Box072/Box072_06___Default_0/Box072_06___Default_0 -> 未绑定


---


### '/World/StackedCarton_1_4' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc
* BBox (world): size=(35.888, 35.888, 35.888), center=(-3.800, 29.700, 0.631)
* 几何统计: Mesh=1, Vertices=56, Faces=44
* 子Mesh材质: /World/StackedCarton_1_4/Meshes/Sketchfab_model/f49ad5edc352496894d3a02181012422_fbx/RootNode/Box072/Box072_06___Default_0/Box072_06___Default_0 -> 未绑定


---


### '/World/StackedCarton_1_5' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc
* BBox (world): size=(35.888, 35.888, 35.888), center=(1.200, 29.700, 0.631)
* 几何统计: Mesh=1, Vertices=56, Faces=44
* 子Mesh材质: /World/StackedCarton_1_5/Meshes/Sketchfab_model/f49ad5edc352496894d3a02181012422_fbx/RootNode/Box072/Box072_06___Default_0/Box072_06___Default_0 -> 未绑定


---


### '/World/StackedCarton_1_6' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc
* BBox (world): size=(35.888, 35.888, 35.888), center=(6.200, 29.700, 0.631)
* 几何统计: Mesh=1, Vertices=56, Faces=44
* 子Mesh材质: /World/StackedCarton_1_6/Meshes/Sketchfab_model/f49ad5edc352496894d3a02181012422_fbx/RootNode/Box072/Box072_06___Default_0/Box072_06___Default_0 -> 未绑定


---


### '/World/StackedCarton_1_7' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc
* BBox (world): size=(35.888, 35.888, 35.888), center=(11.200, 29.700, 0.631)
* 几何统计: Mesh=1, Vertices=56, Faces=44
* 子Mesh材质: /World/StackedCarton_1_7/Meshes/Sketchfab_model/f49ad5edc352496894d3a02181012422_fbx/RootNode/Box072/Box072_06___Default_0/Box072_06___Default_0 -> 未绑定


---


### '/World/StackedCarton_1_8' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc
* BBox (world): size=(35.888, 35.888, 35.888), center=(16.200, 29.700, 0.631)
* 几何统计: Mesh=1, Vertices=56, Faces=44
* 子Mesh材质: /World/StackedCarton_1_8/Meshes/Sketchfab_model/f49ad5edc352496894d3a02181012422_fbx/RootNode/Box072/Box072_06___Default_0/Box072_06___Default_0 -> 未绑定


---


### '/World/StackedCarton_2_1' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc
* BBox (world): size=(35.888, 35.888, 35.888), center=(-18.800, 29.500, 0.996)
* 几何统计: Mesh=1, Vertices=56, Faces=44
* 子Mesh材质: /World/StackedCarton_2_1/Meshes/Sketchfab_model/f49ad5edc352496894d3a02181012422_fbx/RootNode/Box072/Box072_06___Default_0/Box072_06___Default_0 -> 未绑定


---


### '/World/StackedCarton_2_2' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc
* BBox (world): size=(35.888, 35.888, 35.888), center=(-13.800, 29.500, 0.996)
* 几何统计: Mesh=1, Vertices=56, Faces=44
* 子Mesh材质: /World/StackedCarton_2_2/Meshes/Sketchfab_model/f49ad5edc352496894d3a02181012422_fbx/RootNode/Box072/Box072_06___Default_0/Box072_06___Default_0 -> 未绑定


---


### '/World/StackedCarton_2_3' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc
* BBox (world): size=(35.888, 35.888, 35.888), center=(-8.800, 29.500, 0.996)
* 几何统计: Mesh=1, Vertices=56, Faces=44
* 子Mesh材质: /World/StackedCarton_2_3/Meshes/Sketchfab_model/f49ad5edc352496894d3a02181012422_fbx/RootNode/Box072/Box072_06___Default_0/Box072_06___Default_0 -> 未绑定


---


### '/World/StackedCarton_2_4' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc
* BBox (world): size=(35.888, 35.888, 35.888), center=(-3.800, 29.500, 0.996)
* 几何统计: Mesh=1, Vertices=56, Faces=44
* 子Mesh材质: /World/StackedCarton_2_4/Meshes/Sketchfab_model/f49ad5edc352496894d3a02181012422_fbx/RootNode/Box072/Box072_06___Default_0/Box072_06___Default_0 -> 未绑定


---


### '/World/StackedCarton_2_5' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc
* BBox (world): size=(35.888, 35.888, 35.888), center=(1.200, 29.500, 0.996)
* 几何统计: Mesh=1, Vertices=56, Faces=44
* 子Mesh材质: /World/StackedCarton_2_5/Meshes/Sketchfab_model/f49ad5edc352496894d3a02181012422_fbx/RootNode/Box072/Box072_06___Default_0/Box072_06___Default_0 -> 未绑定


---


### '/World/StackedCarton_2_6' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc
* BBox (world): size=(35.888, 35.888, 35.888), center=(6.200, 29.500, 0.996)
* 几何统计: Mesh=1, Vertices=56, Faces=44
* 子Mesh材质: /World/StackedCarton_2_6/Meshes/Sketchfab_model/f49ad5edc352496894d3a02181012422_fbx/RootNode/Box072/Box072_06___Default_0/Box072_06___Default_0 -> 未绑定


---


### '/World/StackedCarton_2_7' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc
* BBox (world): size=(35.888, 35.888, 35.888), center=(11.200, 29.500, 0.996)
* 几何统计: Mesh=1, Vertices=56, Faces=44
* 子Mesh材质: /World/StackedCarton_2_7/Meshes/Sketchfab_model/f49ad5edc352496894d3a02181012422_fbx/RootNode/Box072/Box072_06___Default_0/Box072_06___Default_0 -> 未绑定


---


### '/World/StackedCarton_2_8' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/assets/carton/carton.usdc
* BBox (world): size=(35.888, 35.888, 35.888), center=(16.200, 29.500, 0.996)
* 几何统计: Mesh=1, Vertices=56, Faces=44
* 子Mesh材质: /World/StackedCarton_2_8/Meshes/Sketchfab_model/f49ad5edc352496894d3a02181012422_fbx/RootNode/Box072/Box072_06___Default_0/Box072_06___Default_0 -> 未绑定


---
