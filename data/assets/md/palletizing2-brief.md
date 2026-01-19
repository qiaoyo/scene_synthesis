# USDA场景描述文档:palletizing2.usda

## 1.场景元数据(Scene Metadata)
*  **USDA文件路径(USDA File Path):**`/media/simple/another_Documents/isaacsim_assets/scenedata/palletizing2.usda`
*  **默认Prim (Default Prim):**'Not Set'
*  **单位与坐标系 (Units & Coordinate System):**
   *   **米(Meters Per Unit):**1.0
   *   **Up Axis:**Z

## 2.场景对象层级(Scene Hierarchy)
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
    *   RobotArm_1 (Xform)
        *   world (Xform)
            *   world2base (PhysicsFixedJoint)
        *   root_joint (PhysicsFixedJoint)
        *   base_link (Xform)
            *   joint1 (PhysicsRevoluteJoint)
            *   visuals (Mesh)
            *   collisions (Mesh)
        *   link1 (Xform)
            *   joint2 (PhysicsRevoluteJoint)
            *   visuals (Mesh)
            *   collisions (Mesh)
        *   link2 (Xform)
            *   joint3 (PhysicsRevoluteJoint)
            *   visuals (Mesh)
            *   collisions (Mesh)
        *   link3 (Xform)
            *   joint4 (PhysicsRevoluteJoint)
            *   visuals (Mesh)
            *   collisions (Mesh)
        *   link4 (Xform)
            *   joint5 (PhysicsRevoluteJoint)
            *   visuals (Mesh)
            *   collisions (Mesh)
        *   link5 (Xform)
            *   joint6 (PhysicsRevoluteJoint)
            *   visuals (Mesh)
            *   collisions (Mesh)
        *   link6 (Xform)
            *   rs007l2rg2 (PhysicsFixedJoint)
            *   visuals (Mesh)
            *   collisions (Mesh)
        *   onrobot_rg2_base_link (Xform)
            *   finger_joint (PhysicsRevoluteJoint)
            *   gripper_center_joint (PhysicsFixedJoint)
            *   left_inner_knuckle_joint (PhysicsRevoluteJoint)
            *   right_inner_knuckle_joint (PhysicsRevoluteJoint)
            *   right_outer_knuckle_joint (PhysicsRevoluteJoint)
            *   visuals (Mesh)
            *   collisions (Mesh)
        *   left_outer_knuckle (Xform)
            *   left_inner_finger_joint (PhysicsRevoluteJoint)
            *   visuals (Mesh)
            *   collisions (Mesh)
        *   left_inner_finger (Xform)
            *   visuals (Mesh)
            *   collisions (Mesh)
        *   gripper_center (Xform)
        *   left_inner_knuckle (Xform)
            *   visuals (Mesh)
            *   collisions (Mesh)
        *   right_inner_knuckle (Xform)
            *   visuals (Mesh)
            *   collisions (Mesh)
        *   right_outer_knuckle (Xform)
            *   right_inner_finger_joint (PhysicsRevoluteJoint)
            *   visuals (Mesh)
            *   collisions (Mesh)
        *   right_inner_finger (Xform)
            *   visuals (Mesh)
            *   collisions (Mesh)
        *   Looks (Scope)
            *   material_Black (Material)
                *   Shader (Shader)
            *   material_White (Material)
                *   Shader (Shader)
            *   material_CCCCCC (Material)
                *   Shader (Shader)
            *   material_191919 (Material)
                *   Shader (Shader)
    *   RobotArm_2 (Xform)
        *   world (Xform)
            *   world2base (PhysicsFixedJoint)
        *   root_joint (PhysicsFixedJoint)
        *   base_link (Xform)
            *   joint1 (PhysicsRevoluteJoint)
            *   visuals (Mesh)
            *   collisions (Mesh)
        *   link1 (Xform)
            *   joint2 (PhysicsRevoluteJoint)
            *   visuals (Mesh)
            *   collisions (Mesh)
        *   link2 (Xform)
            *   joint3 (PhysicsRevoluteJoint)
            *   visuals (Mesh)
            *   collisions (Mesh)
        *   link3 (Xform)
            *   joint4 (PhysicsRevoluteJoint)
            *   visuals (Mesh)
            *   collisions (Mesh)
        *   link4 (Xform)
            *   joint5 (PhysicsRevoluteJoint)
            *   visuals (Mesh)
            *   collisions (Mesh)
        *   link5 (Xform)
            *   joint6 (PhysicsRevoluteJoint)
            *   visuals (Mesh)
            *   collisions (Mesh)
        *   link6 (Xform)
            *   rs007l2rg2 (PhysicsFixedJoint)
            *   visuals (Mesh)
            *   collisions (Mesh)
        *   onrobot_rg2_base_link (Xform)
            *   finger_joint (PhysicsRevoluteJoint)
            *   gripper_center_joint (PhysicsFixedJoint)
            *   left_inner_knuckle_joint (PhysicsRevoluteJoint)
            *   right_inner_knuckle_joint (PhysicsRevoluteJoint)
            *   right_outer_knuckle_joint (PhysicsRevoluteJoint)
            *   visuals (Mesh)
            *   collisions (Mesh)
        *   left_outer_knuckle (Xform)
            *   left_inner_finger_joint (PhysicsRevoluteJoint)
            *   visuals (Mesh)
            *   collisions (Mesh)
        *   left_inner_finger (Xform)
            *   visuals (Mesh)
            *   collisions (Mesh)
        *   gripper_center (Xform)
        *   left_inner_knuckle (Xform)
            *   visuals (Mesh)
            *   collisions (Mesh)
        *   right_inner_knuckle (Xform)
            *   visuals (Mesh)
            *   collisions (Mesh)
        *   right_outer_knuckle (Xform)
            *   right_inner_finger_joint (PhysicsRevoluteJoint)
            *   visuals (Mesh)
            *   collisions (Mesh)
        *   right_inner_finger (Xform)
            *   visuals (Mesh)
            *   collisions (Mesh)
        *   Looks (Scope)
            *   material_Black (Material)
                *   Shader (Shader)
            *   material_White (Material)
                *   Shader (Shader)
            *   material_CCCCCC (Material)
                *   Shader (Shader)
            *   material_191919 (Material)
                *   Shader (Shader)
    *   RobotArm_3 (Xform)
        *   world (Xform)
            *   world2base (PhysicsFixedJoint)
        *   root_joint (PhysicsFixedJoint)
        *   base_link (Xform)
            *   joint1 (PhysicsRevoluteJoint)
            *   visuals (Mesh)
            *   collisions (Mesh)
        *   link1 (Xform)
            *   joint2 (PhysicsRevoluteJoint)
            *   visuals (Mesh)
            *   collisions (Mesh)
        *   link2 (Xform)
            *   joint3 (PhysicsRevoluteJoint)
            *   visuals (Mesh)
            *   collisions (Mesh)
        *   link3 (Xform)
            *   joint4 (PhysicsRevoluteJoint)
            *   visuals (Mesh)
            *   collisions (Mesh)
        *   link4 (Xform)
            *   joint5 (PhysicsRevoluteJoint)
            *   visuals (Mesh)
            *   collisions (Mesh)
        *   link5 (Xform)
            *   joint6 (PhysicsRevoluteJoint)
            *   visuals (Mesh)
            *   collisions (Mesh)
        *   link6 (Xform)
            *   rs007l2rg2 (PhysicsFixedJoint)
            *   visuals (Mesh)
            *   collisions (Mesh)
        *   onrobot_rg2_base_link (Xform)
            *   finger_joint (PhysicsRevoluteJoint)
            *   gripper_center_joint (PhysicsFixedJoint)
            *   left_inner_knuckle_joint (PhysicsRevoluteJoint)
            *   right_inner_knuckle_joint (PhysicsRevoluteJoint)
            *   right_outer_knuckle_joint (PhysicsRevoluteJoint)
            *   visuals (Mesh)
            *   collisions (Mesh)
        *   left_outer_knuckle (Xform)
            *   left_inner_finger_joint (PhysicsRevoluteJoint)
            *   visuals (Mesh)
            *   collisions (Mesh)
        *   left_inner_finger (Xform)
            *   visuals (Mesh)
            *   collisions (Mesh)
        *   gripper_center (Xform)
        *   left_inner_knuckle (Xform)
            *   visuals (Mesh)
            *   collisions (Mesh)
        *   right_inner_knuckle (Xform)
            *   visuals (Mesh)
            *   collisions (Mesh)
        *   right_outer_knuckle (Xform)
            *   right_inner_finger_joint (PhysicsRevoluteJoint)
            *   visuals (Mesh)
            *   collisions (Mesh)
        *   right_inner_finger (Xform)
            *   visuals (Mesh)
            *   collisions (Mesh)
        *   Looks (Scope)
            *   material_Black (Material)
                *   Shader (Shader)
            *   material_White (Material)
                *   Shader (Shader)
            *   material_CCCCCC (Material)
                *   Shader (Shader)
            *   material_191919 (Material)
                *   Shader (Shader)
    *   RobotArm_4 (Xform)
        *   world (Xform)
            *   world2base (PhysicsFixedJoint)
        *   root_joint (PhysicsFixedJoint)
        *   base_link (Xform)
            *   joint1 (PhysicsRevoluteJoint)
            *   visuals (Mesh)
            *   collisions (Mesh)
        *   link1 (Xform)
            *   joint2 (PhysicsRevoluteJoint)
            *   visuals (Mesh)
            *   collisions (Mesh)
        *   link2 (Xform)
            *   joint3 (PhysicsRevoluteJoint)
            *   visuals (Mesh)
            *   collisions (Mesh)
        *   link3 (Xform)
            *   joint4 (PhysicsRevoluteJoint)
            *   visuals (Mesh)
            *   collisions (Mesh)
        *   link4 (Xform)
            *   joint5 (PhysicsRevoluteJoint)
            *   visuals (Mesh)
            *   collisions (Mesh)
        *   link5 (Xform)
            *   joint6 (PhysicsRevoluteJoint)
            *   visuals (Mesh)
            *   collisions (Mesh)
        *   link6 (Xform)
            *   rs007l2rg2 (PhysicsFixedJoint)
            *   visuals (Mesh)
            *   collisions (Mesh)
        *   onrobot_rg2_base_link (Xform)
            *   finger_joint (PhysicsRevoluteJoint)
            *   gripper_center_joint (PhysicsFixedJoint)
            *   left_inner_knuckle_joint (PhysicsRevoluteJoint)
            *   right_inner_knuckle_joint (PhysicsRevoluteJoint)
            *   right_outer_knuckle_joint (PhysicsRevoluteJoint)
            *   visuals (Mesh)
            *   collisions (Mesh)
        *   left_outer_knuckle (Xform)
            *   left_inner_finger_joint (PhysicsRevoluteJoint)
            *   visuals (Mesh)
            *   collisions (Mesh)
        *   left_inner_finger (Xform)
            *   visuals (Mesh)
            *   collisions (Mesh)
        *   gripper_center (Xform)
        *   left_inner_knuckle (Xform)
            *   visuals (Mesh)
            *   collisions (Mesh)
        *   right_inner_knuckle (Xform)
            *   visuals (Mesh)
            *   collisions (Mesh)
        *   right_outer_knuckle (Xform)
            *   right_inner_finger_joint (PhysicsRevoluteJoint)
            *   visuals (Mesh)
            *   collisions (Mesh)
        *   right_inner_finger (Xform)
            *   visuals (Mesh)
            *   collisions (Mesh)
        *   Looks (Scope)
            *   material_Black (Material)
                *   Shader (Shader)
            *   material_White (Material)
                *   Shader (Shader)
            *   material_CCCCCC (Material)
                *   Shader (Shader)
            *   material_191919 (Material)
                *   Shader (Shader)
    *   RobotArm_5 (Xform)
        *   world (Xform)
            *   world2base (PhysicsFixedJoint)
        *   root_joint (PhysicsFixedJoint)
        *   base_link (Xform)
            *   joint1 (PhysicsRevoluteJoint)
            *   visuals (Mesh)
            *   collisions (Mesh)
        *   link1 (Xform)
            *   joint2 (PhysicsRevoluteJoint)
            *   visuals (Mesh)
            *   collisions (Mesh)
        *   link2 (Xform)
            *   joint3 (PhysicsRevoluteJoint)
            *   visuals (Mesh)
            *   collisions (Mesh)
        *   link3 (Xform)
            *   joint4 (PhysicsRevoluteJoint)
            *   visuals (Mesh)
            *   collisions (Mesh)
        *   link4 (Xform)
            *   joint5 (PhysicsRevoluteJoint)
            *   visuals (Mesh)
            *   collisions (Mesh)
        *   link5 (Xform)
            *   joint6 (PhysicsRevoluteJoint)
            *   visuals (Mesh)
            *   collisions (Mesh)
        *   link6 (Xform)
            *   rs007l2rg2 (PhysicsFixedJoint)
            *   visuals (Mesh)
            *   collisions (Mesh)
        *   onrobot_rg2_base_link (Xform)
            *   finger_joint (PhysicsRevoluteJoint)
            *   gripper_center_joint (PhysicsFixedJoint)
            *   left_inner_knuckle_joint (PhysicsRevoluteJoint)
            *   right_inner_knuckle_joint (PhysicsRevoluteJoint)
            *   right_outer_knuckle_joint (PhysicsRevoluteJoint)
            *   visuals (Mesh)
            *   collisions (Mesh)
        *   left_outer_knuckle (Xform)
            *   left_inner_finger_joint (PhysicsRevoluteJoint)
            *   visuals (Mesh)
            *   collisions (Mesh)
        *   left_inner_finger (Xform)
            *   visuals (Mesh)
            *   collisions (Mesh)
        *   gripper_center (Xform)
        *   left_inner_knuckle (Xform)
            *   visuals (Mesh)
            *   collisions (Mesh)
        *   right_inner_knuckle (Xform)
            *   visuals (Mesh)
            *   collisions (Mesh)
        *   right_outer_knuckle (Xform)
            *   right_inner_finger_joint (PhysicsRevoluteJoint)
            *   visuals (Mesh)
            *   collisions (Mesh)
        *   right_inner_finger (Xform)
            *   visuals (Mesh)
            *   collisions (Mesh)
        *   Looks (Scope)
            *   material_Black (Material)
                *   Shader (Shader)
            *   material_White (Material)
                *   Shader (Shader)
            *   material_CCCCCC (Material)
                *   Shader (Shader)
            *   material_191919 (Material)
                *   Shader (Shader)
    *   RobotArm_6 (Xform)
        *   world (Xform)
            *   world2base (PhysicsFixedJoint)
        *   root_joint (PhysicsFixedJoint)
        *   base_link (Xform)
            *   joint1 (PhysicsRevoluteJoint)
            *   visuals (Mesh)
            *   collisions (Mesh)
        *   link1 (Xform)
            *   joint2 (PhysicsRevoluteJoint)
            *   visuals (Mesh)
            *   collisions (Mesh)
        *   link2 (Xform)
            *   joint3 (PhysicsRevoluteJoint)
            *   visuals (Mesh)
            *   collisions (Mesh)
        *   link3 (Xform)
            *   joint4 (PhysicsRevoluteJoint)
            *   visuals (Mesh)
            *   collisions (Mesh)
        *   link4 (Xform)
            *   joint5 (PhysicsRevoluteJoint)
            *   visuals (Mesh)
            *   collisions (Mesh)
        *   link5 (Xform)
            *   joint6 (PhysicsRevoluteJoint)
            *   visuals (Mesh)
            *   collisions (Mesh)
        *   link6 (Xform)
            *   rs007l2rg2 (PhysicsFixedJoint)
            *   visuals (Mesh)
            *   collisions (Mesh)
        *   onrobot_rg2_base_link (Xform)
            *   finger_joint (PhysicsRevoluteJoint)
            *   gripper_center_joint (PhysicsFixedJoint)
            *   left_inner_knuckle_joint (PhysicsRevoluteJoint)
            *   right_inner_knuckle_joint (PhysicsRevoluteJoint)
            *   right_outer_knuckle_joint (PhysicsRevoluteJoint)
            *   visuals (Mesh)
            *   collisions (Mesh)
        *   left_outer_knuckle (Xform)
            *   left_inner_finger_joint (PhysicsRevoluteJoint)
            *   visuals (Mesh)
            *   collisions (Mesh)
        *   left_inner_finger (Xform)
            *   visuals (Mesh)
            *   collisions (Mesh)
        *   gripper_center (Xform)
        *   left_inner_knuckle (Xform)
            *   visuals (Mesh)
            *   collisions (Mesh)
        *   right_inner_knuckle (Xform)
            *   visuals (Mesh)
            *   collisions (Mesh)
        *   right_outer_knuckle (Xform)
            *   right_inner_finger_joint (PhysicsRevoluteJoint)
            *   visuals (Mesh)
            *   collisions (Mesh)
        *   right_inner_finger (Xform)
            *   visuals (Mesh)
            *   collisions (Mesh)
        *   Looks (Scope)
            *   material_Black (Material)
                *   Shader (Shader)
            *   material_White (Material)
                *   Shader (Shader)
            *   material_CCCCCC (Material)
                *   Shader (Shader)
            *   material_191919 (Material)
                *   Shader (Shader)
    *   RobotArm_7 (Xform)
        *   world (Xform)
            *   world2base (PhysicsFixedJoint)
        *   root_joint (PhysicsFixedJoint)
        *   base_link (Xform)
            *   joint1 (PhysicsRevoluteJoint)
            *   visuals (Mesh)
            *   collisions (Mesh)
        *   link1 (Xform)
            *   joint2 (PhysicsRevoluteJoint)
            *   visuals (Mesh)
            *   collisions (Mesh)
        *   link2 (Xform)
            *   joint3 (PhysicsRevoluteJoint)
            *   visuals (Mesh)
            *   collisions (Mesh)
        *   link3 (Xform)
            *   joint4 (PhysicsRevoluteJoint)
            *   visuals (Mesh)
            *   collisions (Mesh)
        *   link4 (Xform)
            *   joint5 (PhysicsRevoluteJoint)
            *   visuals (Mesh)
            *   collisions (Mesh)
        *   link5 (Xform)
            *   joint6 (PhysicsRevoluteJoint)
            *   visuals (Mesh)
            *   collisions (Mesh)
        *   link6 (Xform)
            *   rs007l2rg2 (PhysicsFixedJoint)
            *   visuals (Mesh)
            *   collisions (Mesh)
        *   onrobot_rg2_base_link (Xform)
            *   finger_joint (PhysicsRevoluteJoint)
            *   gripper_center_joint (PhysicsFixedJoint)
            *   left_inner_knuckle_joint (PhysicsRevoluteJoint)
            *   right_inner_knuckle_joint (PhysicsRevoluteJoint)
            *   right_outer_knuckle_joint (PhysicsRevoluteJoint)
            *   visuals (Mesh)
            *   collisions (Mesh)
        *   left_outer_knuckle (Xform)
            *   left_inner_finger_joint (PhysicsRevoluteJoint)
            *   visuals (Mesh)
            *   collisions (Mesh)
        *   left_inner_finger (Xform)
            *   visuals (Mesh)
            *   collisions (Mesh)
        *   gripper_center (Xform)
        *   left_inner_knuckle (Xform)
            *   visuals (Mesh)
            *   collisions (Mesh)
        *   right_inner_knuckle (Xform)
            *   visuals (Mesh)
            *   collisions (Mesh)
        *   right_outer_knuckle (Xform)
            *   right_inner_finger_joint (PhysicsRevoluteJoint)
            *   visuals (Mesh)
            *   collisions (Mesh)
        *   right_inner_finger (Xform)
            *   visuals (Mesh)
            *   collisions (Mesh)
        *   Looks (Scope)
            *   material_Black (Material)
                *   Shader (Shader)
            *   material_White (Material)
                *   Shader (Shader)
            *   material_CCCCCC (Material)
                *   Shader (Shader)
            *   material_191919 (Material)
                *   Shader (Shader)
    *   RobotArm_8 (Xform)
        *   world (Xform)
            *   world2base (PhysicsFixedJoint)
        *   root_joint (PhysicsFixedJoint)
        *   base_link (Xform)
            *   joint1 (PhysicsRevoluteJoint)
            *   visuals (Mesh)
            *   collisions (Mesh)
        *   link1 (Xform)
            *   joint2 (PhysicsRevoluteJoint)
            *   visuals (Mesh)
            *   collisions (Mesh)
        *   link2 (Xform)
            *   joint3 (PhysicsRevoluteJoint)
            *   visuals (Mesh)
            *   collisions (Mesh)
        *   link3 (Xform)
            *   joint4 (PhysicsRevoluteJoint)
            *   visuals (Mesh)
            *   collisions (Mesh)
        *   link4 (Xform)
            *   joint5 (PhysicsRevoluteJoint)
            *   visuals (Mesh)
            *   collisions (Mesh)
        *   link5 (Xform)
            *   joint6 (PhysicsRevoluteJoint)
            *   visuals (Mesh)
            *   collisions (Mesh)
        *   link6 (Xform)
            *   rs007l2rg2 (PhysicsFixedJoint)
            *   visuals (Mesh)
            *   collisions (Mesh)
        *   onrobot_rg2_base_link (Xform)
            *   finger_joint (PhysicsRevoluteJoint)
            *   gripper_center_joint (PhysicsFixedJoint)
            *   left_inner_knuckle_joint (PhysicsRevoluteJoint)
            *   right_inner_knuckle_joint (PhysicsRevoluteJoint)
            *   right_outer_knuckle_joint (PhysicsRevoluteJoint)
            *   visuals (Mesh)
            *   collisions (Mesh)
        *   left_outer_knuckle (Xform)
            *   left_inner_finger_joint (PhysicsRevoluteJoint)
            *   visuals (Mesh)
            *   collisions (Mesh)
        *   left_inner_finger (Xform)
            *   visuals (Mesh)
            *   collisions (Mesh)
        *   gripper_center (Xform)
        *   left_inner_knuckle (Xform)
            *   visuals (Mesh)
            *   collisions (Mesh)
        *   right_inner_knuckle (Xform)
            *   visuals (Mesh)
            *   collisions (Mesh)
        *   right_outer_knuckle (Xform)
            *   right_inner_finger_joint (PhysicsRevoluteJoint)
            *   visuals (Mesh)
            *   collisions (Mesh)
        *   right_inner_finger (Xform)
            *   visuals (Mesh)
            *   collisions (Mesh)
        *   Looks (Scope)
            *   material_Black (Material)
                *   Shader (Shader)
            *   material_White (Material)
                *   Shader (Shader)
            *   material_CCCCCC (Material)
                *   Shader (Shader)
            *   material_191919 (Material)
                *   Shader (Shader)
    *   RobotArm1_1 (Xform)
        *   gripper (Xform)
            *   Looks (Scope)
                *   DefaultMaterial (Material)
                    *   DefaultMaterial (Shader)
                *   j____________ (Material)
                    *   j____________ (Shader)
            *   joints (Scope)
                *   drive_joint (PhysicsRevoluteJoint)
                *   left_finger_joint (PhysicsRevoluteJoint)
                *   left_inner_knuckle_joint (PhysicsRevoluteJoint)
                *   right_inner_knuckle_joint (PhysicsRevoluteJoint)
                *   right_outer_knuckle_joint (PhysicsRevoluteJoint)
                *   right_finger_joint (PhysicsRevoluteJoint)
            *   xarm_gripper_base_link (Xform)
                *   link_tcp (Xform)
                *   visuals (Xform)
                *   collisions (Xform)
            *   left_outer_knuckle (Xform)
                *   visuals (Xform)
                *   collisions (Xform)
            *   left_finger (Xform)
                *   visuals (Xform)
                *   collisions (Xform)
            *   left_inner_knuckle (Xform)
                *   visuals (Xform)
                *   collisions (Xform)
            *   right_inner_knuckle (Xform)
                *   visuals (Xform)
                *   collisions (Xform)
            *   right_outer_knuckle (Xform)
                *   visuals (Xform)
                *   collisions (Xform)
            *   right_finger (Xform)
                *   visuals (Xform)
                *   collisions (Xform)
            *   root_joint (PhysicsFixedJoint)
        *   Looks (Scope)
            *   material_Black (Material)
                *   Shader (Shader)
            *   material_Red (Material)
                *   Shader (Shader)
            *   material_Silver (Material)
                *   Shader (Shader)
            *   material_White (Material)
                *   Shader (Shader)
            *   material_______________ (Material)
                *   material_______________ (Shader)
            *   material____________ (Material)
                *   material____________ (Shader)
        *   joints (Scope)
            *   joint1 (PhysicsRevoluteJoint)
            *   joint2 (PhysicsRevoluteJoint)
            *   joint3 (PhysicsRevoluteJoint)
            *   joint4 (PhysicsRevoluteJoint)
            *   joint5 (PhysicsRevoluteJoint)
            *   joint6 (PhysicsRevoluteJoint)
            *   joint7 (PhysicsRevoluteJoint)
        *   world (Xform)
            *   link_base (Xform)
            *   visuals (Xform)
            *   collisions (Xform)
        *   link1 (Xform)
            *   visuals (Xform)
            *   collisions (Xform)
        *   link2 (Xform)
            *   visuals (Xform)
            *   collisions (Xform)
        *   link3 (Xform)
            *   visuals (Xform)
            *   collisions (Xform)
        *   link4 (Xform)
            *   visuals (Xform)
            *   collisions (Xform)
        *   link5 (Xform)
            *   visuals (Xform)
            *   collisions (Xform)
        *   link6 (Xform)
            *   visuals (Xform)
            *   collisions (Xform)
        *   link7 (Xform)
            *   link_eef (Xform)
            *   visuals (Xform)
            *   collisions (Xform)
        *   root_joint (PhysicsFixedJoint)
    *   RobotArm1_2 (Xform)
        *   gripper (Xform)
            *   Looks (Scope)
                *   DefaultMaterial (Material)
                    *   DefaultMaterial (Shader)
                *   j____________ (Material)
                    *   j____________ (Shader)
            *   joints (Scope)
                *   drive_joint (PhysicsRevoluteJoint)
                *   left_finger_joint (PhysicsRevoluteJoint)
                *   left_inner_knuckle_joint (PhysicsRevoluteJoint)
                *   right_inner_knuckle_joint (PhysicsRevoluteJoint)
                *   right_outer_knuckle_joint (PhysicsRevoluteJoint)
                *   right_finger_joint (PhysicsRevoluteJoint)
            *   xarm_gripper_base_link (Xform)
                *   link_tcp (Xform)
                *   visuals (Xform)
                *   collisions (Xform)
            *   left_outer_knuckle (Xform)
                *   visuals (Xform)
                *   collisions (Xform)
            *   left_finger (Xform)
                *   visuals (Xform)
                *   collisions (Xform)
            *   left_inner_knuckle (Xform)
                *   visuals (Xform)
                *   collisions (Xform)
            *   right_inner_knuckle (Xform)
                *   visuals (Xform)
                *   collisions (Xform)
            *   right_outer_knuckle (Xform)
                *   visuals (Xform)
                *   collisions (Xform)
            *   right_finger (Xform)
                *   visuals (Xform)
                *   collisions (Xform)
            *   root_joint (PhysicsFixedJoint)
        *   Looks (Scope)
            *   material_Black (Material)
                *   Shader (Shader)
            *   material_Red (Material)
                *   Shader (Shader)
            *   material_Silver (Material)
                *   Shader (Shader)
            *   material_White (Material)
                *   Shader (Shader)
            *   material_______________ (Material)
                *   material_______________ (Shader)
            *   material____________ (Material)
                *   material____________ (Shader)
        *   joints (Scope)
            *   joint1 (PhysicsRevoluteJoint)
            *   joint2 (PhysicsRevoluteJoint)
            *   joint3 (PhysicsRevoluteJoint)
            *   joint4 (PhysicsRevoluteJoint)
            *   joint5 (PhysicsRevoluteJoint)
            *   joint6 (PhysicsRevoluteJoint)
            *   joint7 (PhysicsRevoluteJoint)
        *   world (Xform)
            *   link_base (Xform)
            *   visuals (Xform)
            *   collisions (Xform)
        *   link1 (Xform)
            *   visuals (Xform)
            *   collisions (Xform)
        *   link2 (Xform)
            *   visuals (Xform)
            *   collisions (Xform)
        *   link3 (Xform)
            *   visuals (Xform)
            *   collisions (Xform)
        *   link4 (Xform)
            *   visuals (Xform)
            *   collisions (Xform)
        *   link5 (Xform)
            *   visuals (Xform)
            *   collisions (Xform)
        *   link6 (Xform)
            *   visuals (Xform)
            *   collisions (Xform)
        *   link7 (Xform)
            *   link_eef (Xform)
            *   visuals (Xform)
            *   collisions (Xform)
        *   root_joint (PhysicsFixedJoint)
    *   RobotArm1_3 (Xform)
        *   gripper (Xform)
            *   Looks (Scope)
                *   DefaultMaterial (Material)
                    *   DefaultMaterial (Shader)
                *   j____________ (Material)
                    *   j____________ (Shader)
            *   joints (Scope)
                *   drive_joint (PhysicsRevoluteJoint)
                *   left_finger_joint (PhysicsRevoluteJoint)
                *   left_inner_knuckle_joint (PhysicsRevoluteJoint)
                *   right_inner_knuckle_joint (PhysicsRevoluteJoint)
                *   right_outer_knuckle_joint (PhysicsRevoluteJoint)
                *   right_finger_joint (PhysicsRevoluteJoint)
            *   xarm_gripper_base_link (Xform)
                *   link_tcp (Xform)
                *   visuals (Xform)
                *   collisions (Xform)
            *   left_outer_knuckle (Xform)
                *   visuals (Xform)
                *   collisions (Xform)
            *   left_finger (Xform)
                *   visuals (Xform)
                *   collisions (Xform)
            *   left_inner_knuckle (Xform)
                *   visuals (Xform)
                *   collisions (Xform)
            *   right_inner_knuckle (Xform)
                *   visuals (Xform)
                *   collisions (Xform)
            *   right_outer_knuckle (Xform)
                *   visuals (Xform)
                *   collisions (Xform)
            *   right_finger (Xform)
                *   visuals (Xform)
                *   collisions (Xform)
            *   root_joint (PhysicsFixedJoint)
        *   Looks (Scope)
            *   material_Black (Material)
                *   Shader (Shader)
            *   material_Red (Material)
                *   Shader (Shader)
            *   material_Silver (Material)
                *   Shader (Shader)
            *   material_White (Material)
                *   Shader (Shader)
            *   material_______________ (Material)
                *   material_______________ (Shader)
            *   material____________ (Material)
                *   material____________ (Shader)
        *   joints (Scope)
            *   joint1 (PhysicsRevoluteJoint)
            *   joint2 (PhysicsRevoluteJoint)
            *   joint3 (PhysicsRevoluteJoint)
            *   joint4 (PhysicsRevoluteJoint)
            *   joint5 (PhysicsRevoluteJoint)
            *   joint6 (PhysicsRevoluteJoint)
            *   joint7 (PhysicsRevoluteJoint)
        *   world (Xform)
            *   link_base (Xform)
            *   visuals (Xform)
            *   collisions (Xform)
        *   link1 (Xform)
            *   visuals (Xform)
            *   collisions (Xform)
        *   link2 (Xform)
            *   visuals (Xform)
            *   collisions (Xform)
        *   link3 (Xform)
            *   visuals (Xform)
            *   collisions (Xform)
        *   link4 (Xform)
            *   visuals (Xform)
            *   collisions (Xform)
        *   link5 (Xform)
            *   visuals (Xform)
            *   collisions (Xform)
        *   link6 (Xform)
            *   visuals (Xform)
            *   collisions (Xform)
        *   link7 (Xform)
            *   link_eef (Xform)
            *   visuals (Xform)
            *   collisions (Xform)
        *   root_joint (PhysicsFixedJoint)
    *   RobotArm1_4 (Xform)
        *   gripper (Xform)
            *   Looks (Scope)
                *   DefaultMaterial (Material)
                    *   DefaultMaterial (Shader)
                *   j____________ (Material)
                    *   j____________ (Shader)
            *   joints (Scope)
                *   drive_joint (PhysicsRevoluteJoint)
                *   left_finger_joint (PhysicsRevoluteJoint)
                *   left_inner_knuckle_joint (PhysicsRevoluteJoint)
                *   right_inner_knuckle_joint (PhysicsRevoluteJoint)
                *   right_outer_knuckle_joint (PhysicsRevoluteJoint)
                *   right_finger_joint (PhysicsRevoluteJoint)
            *   xarm_gripper_base_link (Xform)
                *   link_tcp (Xform)
                *   visuals (Xform)
                *   collisions (Xform)
            *   left_outer_knuckle (Xform)
                *   visuals (Xform)
                *   collisions (Xform)
            *   left_finger (Xform)
                *   visuals (Xform)
                *   collisions (Xform)
            *   left_inner_knuckle (Xform)
                *   visuals (Xform)
                *   collisions (Xform)
            *   right_inner_knuckle (Xform)
                *   visuals (Xform)
                *   collisions (Xform)
            *   right_outer_knuckle (Xform)
                *   visuals (Xform)
                *   collisions (Xform)
            *   right_finger (Xform)
                *   visuals (Xform)
                *   collisions (Xform)
            *   root_joint (PhysicsFixedJoint)
        *   Looks (Scope)
            *   material_Black (Material)
                *   Shader (Shader)
            *   material_Red (Material)
                *   Shader (Shader)
            *   material_Silver (Material)
                *   Shader (Shader)
            *   material_White (Material)
                *   Shader (Shader)
            *   material_______________ (Material)
                *   material_______________ (Shader)
            *   material____________ (Material)
                *   material____________ (Shader)
        *   joints (Scope)
            *   joint1 (PhysicsRevoluteJoint)
            *   joint2 (PhysicsRevoluteJoint)
            *   joint3 (PhysicsRevoluteJoint)
            *   joint4 (PhysicsRevoluteJoint)
            *   joint5 (PhysicsRevoluteJoint)
            *   joint6 (PhysicsRevoluteJoint)
            *   joint7 (PhysicsRevoluteJoint)
        *   world (Xform)
            *   link_base (Xform)
            *   visuals (Xform)
            *   collisions (Xform)
        *   link1 (Xform)
            *   visuals (Xform)
            *   collisions (Xform)
        *   link2 (Xform)
            *   visuals (Xform)
            *   collisions (Xform)
        *   link3 (Xform)
            *   visuals (Xform)
            *   collisions (Xform)
        *   link4 (Xform)
            *   visuals (Xform)
            *   collisions (Xform)
        *   link5 (Xform)
            *   visuals (Xform)
            *   collisions (Xform)
        *   link6 (Xform)
            *   visuals (Xform)
            *   collisions (Xform)
        *   link7 (Xform)
            *   link_eef (Xform)
            *   visuals (Xform)
            *   collisions (Xform)
        *   root_joint (PhysicsFixedJoint)
    *   RobotArm1_5 (Xform)
        *   gripper (Xform)
            *   Looks (Scope)
                *   DefaultMaterial (Material)
                    *   DefaultMaterial (Shader)
                *   j____________ (Material)
                    *   j____________ (Shader)
            *   joints (Scope)
                *   drive_joint (PhysicsRevoluteJoint)
                *   left_finger_joint (PhysicsRevoluteJoint)
                *   left_inner_knuckle_joint (PhysicsRevoluteJoint)
                *   right_inner_knuckle_joint (PhysicsRevoluteJoint)
                *   right_outer_knuckle_joint (PhysicsRevoluteJoint)
                *   right_finger_joint (PhysicsRevoluteJoint)
            *   xarm_gripper_base_link (Xform)
                *   link_tcp (Xform)
                *   visuals (Xform)
                *   collisions (Xform)
            *   left_outer_knuckle (Xform)
                *   visuals (Xform)
                *   collisions (Xform)
            *   left_finger (Xform)
                *   visuals (Xform)
                *   collisions (Xform)
            *   left_inner_knuckle (Xform)
                *   visuals (Xform)
                *   collisions (Xform)
            *   right_inner_knuckle (Xform)
                *   visuals (Xform)
                *   collisions (Xform)
            *   right_outer_knuckle (Xform)
                *   visuals (Xform)
                *   collisions (Xform)
            *   right_finger (Xform)
                *   visuals (Xform)
                *   collisions (Xform)
            *   root_joint (PhysicsFixedJoint)
        *   Looks (Scope)
            *   material_Black (Material)
                *   Shader (Shader)
            *   material_Red (Material)
                *   Shader (Shader)
            *   material_Silver (Material)
                *   Shader (Shader)
            *   material_White (Material)
                *   Shader (Shader)
            *   material_______________ (Material)
                *   material_______________ (Shader)
            *   material____________ (Material)
                *   material____________ (Shader)
        *   joints (Scope)
            *   joint1 (PhysicsRevoluteJoint)
            *   joint2 (PhysicsRevoluteJoint)
            *   joint3 (PhysicsRevoluteJoint)
            *   joint4 (PhysicsRevoluteJoint)
            *   joint5 (PhysicsRevoluteJoint)
            *   joint6 (PhysicsRevoluteJoint)
            *   joint7 (PhysicsRevoluteJoint)
        *   world (Xform)
            *   link_base (Xform)
            *   visuals (Xform)
            *   collisions (Xform)
        *   link1 (Xform)
            *   visuals (Xform)
            *   collisions (Xform)
        *   link2 (Xform)
            *   visuals (Xform)
            *   collisions (Xform)
        *   link3 (Xform)
            *   visuals (Xform)
            *   collisions (Xform)
        *   link4 (Xform)
            *   visuals (Xform)
            *   collisions (Xform)
        *   link5 (Xform)
            *   visuals (Xform)
            *   collisions (Xform)
        *   link6 (Xform)
            *   visuals (Xform)
            *   collisions (Xform)
        *   link7 (Xform)
            *   link_eef (Xform)
            *   visuals (Xform)
            *   collisions (Xform)
        *   root_joint (PhysicsFixedJoint)
    *   RobotArm1_6 (Xform)
        *   gripper (Xform)
            *   Looks (Scope)
                *   DefaultMaterial (Material)
                    *   DefaultMaterial (Shader)
                *   j____________ (Material)
                    *   j____________ (Shader)
            *   joints (Scope)
                *   drive_joint (PhysicsRevoluteJoint)
                *   left_finger_joint (PhysicsRevoluteJoint)
                *   left_inner_knuckle_joint (PhysicsRevoluteJoint)
                *   right_inner_knuckle_joint (PhysicsRevoluteJoint)
                *   right_outer_knuckle_joint (PhysicsRevoluteJoint)
                *   right_finger_joint (PhysicsRevoluteJoint)
            *   xarm_gripper_base_link (Xform)
                *   link_tcp (Xform)
                *   visuals (Xform)
                *   collisions (Xform)
            *   left_outer_knuckle (Xform)
                *   visuals (Xform)
                *   collisions (Xform)
            *   left_finger (Xform)
                *   visuals (Xform)
                *   collisions (Xform)
            *   left_inner_knuckle (Xform)
                *   visuals (Xform)
                *   collisions (Xform)
            *   right_inner_knuckle (Xform)
                *   visuals (Xform)
                *   collisions (Xform)
            *   right_outer_knuckle (Xform)
                *   visuals (Xform)
                *   collisions (Xform)
            *   right_finger (Xform)
                *   visuals (Xform)
                *   collisions (Xform)
            *   root_joint (PhysicsFixedJoint)
        *   Looks (Scope)
            *   material_Black (Material)
                *   Shader (Shader)
            *   material_Red (Material)
                *   Shader (Shader)
            *   material_Silver (Material)
                *   Shader (Shader)
            *   material_White (Material)
                *   Shader (Shader)
            *   material_______________ (Material)
                *   material_______________ (Shader)
            *   material____________ (Material)
                *   material____________ (Shader)
        *   joints (Scope)
            *   joint1 (PhysicsRevoluteJoint)
            *   joint2 (PhysicsRevoluteJoint)
            *   joint3 (PhysicsRevoluteJoint)
            *   joint4 (PhysicsRevoluteJoint)
            *   joint5 (PhysicsRevoluteJoint)
            *   joint6 (PhysicsRevoluteJoint)
            *   joint7 (PhysicsRevoluteJoint)
        *   world (Xform)
            *   link_base (Xform)
            *   visuals (Xform)
            *   collisions (Xform)
        *   link1 (Xform)
            *   visuals (Xform)
            *   collisions (Xform)
        *   link2 (Xform)
            *   visuals (Xform)
            *   collisions (Xform)
        *   link3 (Xform)
            *   visuals (Xform)
            *   collisions (Xform)
        *   link4 (Xform)
            *   visuals (Xform)
            *   collisions (Xform)
        *   link5 (Xform)
            *   visuals (Xform)
            *   collisions (Xform)
        *   link6 (Xform)
            *   visuals (Xform)
            *   collisions (Xform)
        *   link7 (Xform)
            *   link_eef (Xform)
            *   visuals (Xform)
            *   collisions (Xform)
        *   root_joint (PhysicsFixedJoint)
    *   RobotArm1_7 (Xform)
        *   gripper (Xform)
            *   Looks (Scope)
                *   DefaultMaterial (Material)
                    *   DefaultMaterial (Shader)
                *   j____________ (Material)
                    *   j____________ (Shader)
            *   joints (Scope)
                *   drive_joint (PhysicsRevoluteJoint)
                *   left_finger_joint (PhysicsRevoluteJoint)
                *   left_inner_knuckle_joint (PhysicsRevoluteJoint)
                *   right_inner_knuckle_joint (PhysicsRevoluteJoint)
                *   right_outer_knuckle_joint (PhysicsRevoluteJoint)
                *   right_finger_joint (PhysicsRevoluteJoint)
            *   xarm_gripper_base_link (Xform)
                *   link_tcp (Xform)
                *   visuals (Xform)
                *   collisions (Xform)
            *   left_outer_knuckle (Xform)
                *   visuals (Xform)
                *   collisions (Xform)
            *   left_finger (Xform)
                *   visuals (Xform)
                *   collisions (Xform)
            *   left_inner_knuckle (Xform)
                *   visuals (Xform)
                *   collisions (Xform)
            *   right_inner_knuckle (Xform)
                *   visuals (Xform)
                *   collisions (Xform)
            *   right_outer_knuckle (Xform)
                *   visuals (Xform)
                *   collisions (Xform)
            *   right_finger (Xform)
                *   visuals (Xform)
                *   collisions (Xform)
            *   root_joint (PhysicsFixedJoint)
        *   Looks (Scope)
            *   material_Black (Material)
                *   Shader (Shader)
            *   material_Red (Material)
                *   Shader (Shader)
            *   material_Silver (Material)
                *   Shader (Shader)
            *   material_White (Material)
                *   Shader (Shader)
            *   material_______________ (Material)
                *   material_______________ (Shader)
            *   material____________ (Material)
                *   material____________ (Shader)
        *   joints (Scope)
            *   joint1 (PhysicsRevoluteJoint)
            *   joint2 (PhysicsRevoluteJoint)
            *   joint3 (PhysicsRevoluteJoint)
            *   joint4 (PhysicsRevoluteJoint)
            *   joint5 (PhysicsRevoluteJoint)
            *   joint6 (PhysicsRevoluteJoint)
            *   joint7 (PhysicsRevoluteJoint)
        *   world (Xform)
            *   link_base (Xform)
            *   visuals (Xform)
            *   collisions (Xform)
        *   link1 (Xform)
            *   visuals (Xform)
            *   collisions (Xform)
        *   link2 (Xform)
            *   visuals (Xform)
            *   collisions (Xform)
        *   link3 (Xform)
            *   visuals (Xform)
            *   collisions (Xform)
        *   link4 (Xform)
            *   visuals (Xform)
            *   collisions (Xform)
        *   link5 (Xform)
            *   visuals (Xform)
            *   collisions (Xform)
        *   link6 (Xform)
            *   visuals (Xform)
            *   collisions (Xform)
        *   link7 (Xform)
            *   link_eef (Xform)
            *   visuals (Xform)
            *   collisions (Xform)
        *   root_joint (PhysicsFixedJoint)
    *   RobotArm1_8 (Xform)
        *   gripper (Xform)
            *   Looks (Scope)
                *   DefaultMaterial (Material)
                    *   DefaultMaterial (Shader)
                *   j____________ (Material)
                    *   j____________ (Shader)
            *   joints (Scope)
                *   drive_joint (PhysicsRevoluteJoint)
                *   left_finger_joint (PhysicsRevoluteJoint)
                *   left_inner_knuckle_joint (PhysicsRevoluteJoint)
                *   right_inner_knuckle_joint (PhysicsRevoluteJoint)
                *   right_outer_knuckle_joint (PhysicsRevoluteJoint)
                *   right_finger_joint (PhysicsRevoluteJoint)
            *   xarm_gripper_base_link (Xform)
                *   link_tcp (Xform)
                *   visuals (Xform)
                *   collisions (Xform)
            *   left_outer_knuckle (Xform)
                *   visuals (Xform)
                *   collisions (Xform)
            *   left_finger (Xform)
                *   visuals (Xform)
                *   collisions (Xform)
            *   left_inner_knuckle (Xform)
                *   visuals (Xform)
                *   collisions (Xform)
            *   right_inner_knuckle (Xform)
                *   visuals (Xform)
                *   collisions (Xform)
            *   right_outer_knuckle (Xform)
                *   visuals (Xform)
                *   collisions (Xform)
            *   right_finger (Xform)
                *   visuals (Xform)
                *   collisions (Xform)
            *   root_joint (PhysicsFixedJoint)
        *   Looks (Scope)
            *   material_Black (Material)
                *   Shader (Shader)
            *   material_Red (Material)
                *   Shader (Shader)
            *   material_Silver (Material)
                *   Shader (Shader)
            *   material_White (Material)
                *   Shader (Shader)
            *   material_______________ (Material)
                *   material_______________ (Shader)
            *   material____________ (Material)
                *   material____________ (Shader)
        *   joints (Scope)
            *   joint1 (PhysicsRevoluteJoint)
            *   joint2 (PhysicsRevoluteJoint)
            *   joint3 (PhysicsRevoluteJoint)
            *   joint4 (PhysicsRevoluteJoint)
            *   joint5 (PhysicsRevoluteJoint)
            *   joint6 (PhysicsRevoluteJoint)
            *   joint7 (PhysicsRevoluteJoint)
        *   world (Xform)
            *   link_base (Xform)
            *   visuals (Xform)
            *   collisions (Xform)
        *   link1 (Xform)
            *   visuals (Xform)
            *   collisions (Xform)
        *   link2 (Xform)
            *   visuals (Xform)
            *   collisions (Xform)
        *   link3 (Xform)
            *   visuals (Xform)
            *   collisions (Xform)
        *   link4 (Xform)
            *   visuals (Xform)
            *   collisions (Xform)
        *   link5 (Xform)
            *   visuals (Xform)
            *   collisions (Xform)
        *   link6 (Xform)
            *   visuals (Xform)
            *   collisions (Xform)
        *   link7 (Xform)
            *   link_eef (Xform)
            *   visuals (Xform)
            *   collisions (Xform)
        *   root_joint (PhysicsFixedJoint)
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

## 3. 外部引用Xform简报(Referenced Xforms)

### '/World/factory' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/scene/factory/factory.usdc
* BBox (world): size=(49.139, 19.897, 67.754), center=(0.761, 0.769, 9.470)
* 几何统计: Mesh=7, Vertices=2044, Faces=946
* 子Mesh材质: /World/factory/Meshes/Sketchfab_model/cc020ec10d3e484ab6eb350963eb38d0_fbx/RootNode/Factory002/Factory002_WindowsIndustrial_frontSolid_OpenWindows_Mat_0/Factory002_WindowsIndustrial_frontSolid_OpenWindows_Mat_0 -> 未绑定, /World/factory/Meshes/Sketchfab_model/cc020ec10d3e484ab6eb350963eb38d0_fbx/RootNode/Factory002/Factory002_WindowsIndustrial_frontSolid_Mat_0/Factory002_WindowsIndustrial_frontSolid_Mat_0 -> 未绑定, /World/factory/Meshes/Sketchfab_model/cc020ec10d3e484ab6eb350963eb38d0_fbx/RootNode/Factory002/Factory002_WindowsIndustrial_frontDoorclosed_Mat_0/Factory002_WindowsIndustrial_frontDoorclosed_Mat_0 -> 未绑定, /World/factory/Meshes/Sketchfab_model/cc020ec10d3e484ab6eb350963eb38d0_fbx/RootNode/Factory002/Factory002_WindowsIndustrial_frontDoorOpen_Mat_0/Factory002_WindowsIndustrial_frontDoorOpen_Mat_0 -> 未绑定, /World/factory/Meshes/Sketchfab_model/cc020ec10d3e484ab6eb350963eb38d0_fbx/RootNode/Factory002/Factory002_WindowsIndustrial_front_Mat_0/Factory002_WindowsIndustrial_front_Mat_0 -> 未绑定, /World/factory/Meshes/Sketchfab_model/cc020ec10d3e484ab6eb350963eb38d0_fbx/RootNode/Factory002/Factory002_11___Default_0/Factory002_11___Default_0 -> 未绑定, /World/factory/Meshes/Sketchfab_model/cc020ec10d3e484ab6eb350963eb38d0_fbx/RootNode/Object001/Object001_20___Default_0/Object001_20___Default_0 -> 未绑定


---


### '/World/RobotArm_1' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/5.0/Isaac/Robots/Kawasaki/RS007L/rs007l_onrobot_rg2.usd
* BBox (world): size=(0.572, 0.478, 2.377), center=(-19.903, 28.984, 1.349)
* 几何统计: Mesh=28, Vertices=383850, Faces=127950
* 子Mesh材质: /World/RobotArm_1/base_link/visuals -> /World/RobotArm_1/Looks/material_White, /World/RobotArm_1/base_link/collisions -> 未绑定, /World/RobotArm_1/link1/visuals -> /World/RobotArm_1/Looks/material_White, /World/RobotArm_1/link1/collisions -> 未绑定, /World/RobotArm_1/link2/visuals -> /World/RobotArm_1/Looks/material_White, /World/RobotArm_1/link2/collisions -> 未绑定, /World/RobotArm_1/link3/visuals -> /World/RobotArm_1/Looks/material_White, /World/RobotArm_1/link3/collisions -> 未绑定, /World/RobotArm_1/link4/visuals -> /World/RobotArm_1/Looks/material_White, /World/RobotArm_1/link4/collisions -> 未绑定, /World/RobotArm_1/link5/visuals -> /World/RobotArm_1/Looks/material_White, /World/RobotArm_1/link5/collisions -> 未绑定, /World/RobotArm_1/link6/visuals -> /World/RobotArm_1/Looks/material_Black, /World/RobotArm_1/link6/collisions -> 未绑定, /World/RobotArm_1/onrobot_rg2_base_link/visuals -> /World/RobotArm_1/Looks/material_CCCCCC, /World/RobotArm_1/onrobot_rg2_base_link/collisions -> 未绑定, /World/RobotArm_1/left_outer_knuckle/visuals -> /World/RobotArm_1/Looks/material_CCCCCC, /World/RobotArm_1/left_outer_knuckle/collisions -> 未绑定, /World/RobotArm_1/left_inner_finger/visuals -> /World/RobotArm_1/Looks/material_191919, /World/RobotArm_1/left_inner_finger/collisions -> 未绑定, /World/RobotArm_1/left_inner_knuckle/visuals -> /World/RobotArm_1/Looks/material_CCCCCC, /World/RobotArm_1/left_inner_knuckle/collisions -> 未绑定, /World/RobotArm_1/right_inner_knuckle/visuals -> /World/RobotArm_1/Looks/material_CCCCCC, /World/RobotArm_1/right_inner_knuckle/collisions -> 未绑定, /World/RobotArm_1/right_outer_knuckle/visuals -> /World/RobotArm_1/Looks/material_CCCCCC, /World/RobotArm_1/right_outer_knuckle/collisions -> 未绑定, /World/RobotArm_1/right_inner_finger/visuals -> /World/RobotArm_1/Looks/material_191919, /World/RobotArm_1/right_inner_finger/collisions -> 未绑定
* 材质摘要:
 * /World/RobotArm_1/Looks/material_191919 -> Inputs: 'diffuse_color_constant=(0.100, 0.100, 0.100)'
 * /World/RobotArm_1/Looks/material_Black -> Inputs: 'diffuse_color_constant=(0.000, 0.000, 0.000)'
 * /World/RobotArm_1/Looks/material_CCCCCC -> Inputs: 'diffuse_color_constant=(0.800, 0.800, 0.800)'
 * /World/RobotArm_1/Looks/material_White -> Inputs: 'diffuse_color_constant=(1.000, 1.000, 1.000)'


---


### '/World/RobotArm_2' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/5.0/Isaac/Robots/Kawasaki/RS007L/rs007l_onrobot_rg2.usd
* BBox (world): size=(0.572, 0.478, 2.377), center=(-14.903, 28.984, 1.349)
* 几何统计: Mesh=28, Vertices=383850, Faces=127950
* 子Mesh材质: /World/RobotArm_2/base_link/visuals -> /World/RobotArm_2/Looks/material_White, /World/RobotArm_2/base_link/collisions -> 未绑定, /World/RobotArm_2/link1/visuals -> /World/RobotArm_2/Looks/material_White, /World/RobotArm_2/link1/collisions -> 未绑定, /World/RobotArm_2/link2/visuals -> /World/RobotArm_2/Looks/material_White, /World/RobotArm_2/link2/collisions -> 未绑定, /World/RobotArm_2/link3/visuals -> /World/RobotArm_2/Looks/material_White, /World/RobotArm_2/link3/collisions -> 未绑定, /World/RobotArm_2/link4/visuals -> /World/RobotArm_2/Looks/material_White, /World/RobotArm_2/link4/collisions -> 未绑定, /World/RobotArm_2/link5/visuals -> /World/RobotArm_2/Looks/material_White, /World/RobotArm_2/link5/collisions -> 未绑定, /World/RobotArm_2/link6/visuals -> /World/RobotArm_2/Looks/material_Black, /World/RobotArm_2/link6/collisions -> 未绑定, /World/RobotArm_2/onrobot_rg2_base_link/visuals -> /World/RobotArm_2/Looks/material_CCCCCC, /World/RobotArm_2/onrobot_rg2_base_link/collisions -> 未绑定, /World/RobotArm_2/left_outer_knuckle/visuals -> /World/RobotArm_2/Looks/material_CCCCCC, /World/RobotArm_2/left_outer_knuckle/collisions -> 未绑定, /World/RobotArm_2/left_inner_finger/visuals -> /World/RobotArm_2/Looks/material_191919, /World/RobotArm_2/left_inner_finger/collisions -> 未绑定, /World/RobotArm_2/left_inner_knuckle/visuals -> /World/RobotArm_2/Looks/material_CCCCCC, /World/RobotArm_2/left_inner_knuckle/collisions -> 未绑定, /World/RobotArm_2/right_inner_knuckle/visuals -> /World/RobotArm_2/Looks/material_CCCCCC, /World/RobotArm_2/right_inner_knuckle/collisions -> 未绑定, /World/RobotArm_2/right_outer_knuckle/visuals -> /World/RobotArm_2/Looks/material_CCCCCC, /World/RobotArm_2/right_outer_knuckle/collisions -> 未绑定, /World/RobotArm_2/right_inner_finger/visuals -> /World/RobotArm_2/Looks/material_191919, /World/RobotArm_2/right_inner_finger/collisions -> 未绑定
* 材质摘要:
 * /World/RobotArm_2/Looks/material_191919 -> Inputs: 'diffuse_color_constant=(0.100, 0.100, 0.100)'
 * /World/RobotArm_2/Looks/material_Black -> Inputs: 'diffuse_color_constant=(0.000, 0.000, 0.000)'
 * /World/RobotArm_2/Looks/material_CCCCCC -> Inputs: 'diffuse_color_constant=(0.800, 0.800, 0.800)'
 * /World/RobotArm_2/Looks/material_White -> Inputs: 'diffuse_color_constant=(1.000, 1.000, 1.000)'


---


### '/World/RobotArm_3' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/5.0/Isaac/Robots/Kawasaki/RS007L/rs007l_onrobot_rg2.usd
* BBox (world): size=(0.572, 0.478, 2.377), center=(-9.903, 28.984, 1.349)
* 几何统计: Mesh=28, Vertices=383850, Faces=127950
* 子Mesh材质: /World/RobotArm_3/base_link/visuals -> /World/RobotArm_3/Looks/material_White, /World/RobotArm_3/base_link/collisions -> 未绑定, /World/RobotArm_3/link1/visuals -> /World/RobotArm_3/Looks/material_White, /World/RobotArm_3/link1/collisions -> 未绑定, /World/RobotArm_3/link2/visuals -> /World/RobotArm_3/Looks/material_White, /World/RobotArm_3/link2/collisions -> 未绑定, /World/RobotArm_3/link3/visuals -> /World/RobotArm_3/Looks/material_White, /World/RobotArm_3/link3/collisions -> 未绑定, /World/RobotArm_3/link4/visuals -> /World/RobotArm_3/Looks/material_White, /World/RobotArm_3/link4/collisions -> 未绑定, /World/RobotArm_3/link5/visuals -> /World/RobotArm_3/Looks/material_White, /World/RobotArm_3/link5/collisions -> 未绑定, /World/RobotArm_3/link6/visuals -> /World/RobotArm_3/Looks/material_Black, /World/RobotArm_3/link6/collisions -> 未绑定, /World/RobotArm_3/onrobot_rg2_base_link/visuals -> /World/RobotArm_3/Looks/material_CCCCCC, /World/RobotArm_3/onrobot_rg2_base_link/collisions -> 未绑定, /World/RobotArm_3/left_outer_knuckle/visuals -> /World/RobotArm_3/Looks/material_CCCCCC, /World/RobotArm_3/left_outer_knuckle/collisions -> 未绑定, /World/RobotArm_3/left_inner_finger/visuals -> /World/RobotArm_3/Looks/material_191919, /World/RobotArm_3/left_inner_finger/collisions -> 未绑定, /World/RobotArm_3/left_inner_knuckle/visuals -> /World/RobotArm_3/Looks/material_CCCCCC, /World/RobotArm_3/left_inner_knuckle/collisions -> 未绑定, /World/RobotArm_3/right_inner_knuckle/visuals -> /World/RobotArm_3/Looks/material_CCCCCC, /World/RobotArm_3/right_inner_knuckle/collisions -> 未绑定, /World/RobotArm_3/right_outer_knuckle/visuals -> /World/RobotArm_3/Looks/material_CCCCCC, /World/RobotArm_3/right_outer_knuckle/collisions -> 未绑定, /World/RobotArm_3/right_inner_finger/visuals -> /World/RobotArm_3/Looks/material_191919, /World/RobotArm_3/right_inner_finger/collisions -> 未绑定
* 材质摘要:
 * /World/RobotArm_3/Looks/material_191919 -> Inputs: 'diffuse_color_constant=(0.100, 0.100, 0.100)'
 * /World/RobotArm_3/Looks/material_Black -> Inputs: 'diffuse_color_constant=(0.000, 0.000, 0.000)'
 * /World/RobotArm_3/Looks/material_CCCCCC -> Inputs: 'diffuse_color_constant=(0.800, 0.800, 0.800)'
 * /World/RobotArm_3/Looks/material_White -> Inputs: 'diffuse_color_constant=(1.000, 1.000, 1.000)'


---


### '/World/RobotArm_4' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/5.0/Isaac/Robots/Kawasaki/RS007L/rs007l_onrobot_rg2.usd
* BBox (world): size=(0.572, 0.478, 2.377), center=(-4.903, 28.984, 1.349)
* 几何统计: Mesh=28, Vertices=383850, Faces=127950
* 子Mesh材质: /World/RobotArm_4/base_link/visuals -> /World/RobotArm_4/Looks/material_White, /World/RobotArm_4/base_link/collisions -> 未绑定, /World/RobotArm_4/link1/visuals -> /World/RobotArm_4/Looks/material_White, /World/RobotArm_4/link1/collisions -> 未绑定, /World/RobotArm_4/link2/visuals -> /World/RobotArm_4/Looks/material_White, /World/RobotArm_4/link2/collisions -> 未绑定, /World/RobotArm_4/link3/visuals -> /World/RobotArm_4/Looks/material_White, /World/RobotArm_4/link3/collisions -> 未绑定, /World/RobotArm_4/link4/visuals -> /World/RobotArm_4/Looks/material_White, /World/RobotArm_4/link4/collisions -> 未绑定, /World/RobotArm_4/link5/visuals -> /World/RobotArm_4/Looks/material_White, /World/RobotArm_4/link5/collisions -> 未绑定, /World/RobotArm_4/link6/visuals -> /World/RobotArm_4/Looks/material_Black, /World/RobotArm_4/link6/collisions -> 未绑定, /World/RobotArm_4/onrobot_rg2_base_link/visuals -> /World/RobotArm_4/Looks/material_CCCCCC, /World/RobotArm_4/onrobot_rg2_base_link/collisions -> 未绑定, /World/RobotArm_4/left_outer_knuckle/visuals -> /World/RobotArm_4/Looks/material_CCCCCC, /World/RobotArm_4/left_outer_knuckle/collisions -> 未绑定, /World/RobotArm_4/left_inner_finger/visuals -> /World/RobotArm_4/Looks/material_191919, /World/RobotArm_4/left_inner_finger/collisions -> 未绑定, /World/RobotArm_4/left_inner_knuckle/visuals -> /World/RobotArm_4/Looks/material_CCCCCC, /World/RobotArm_4/left_inner_knuckle/collisions -> 未绑定, /World/RobotArm_4/right_inner_knuckle/visuals -> /World/RobotArm_4/Looks/material_CCCCCC, /World/RobotArm_4/right_inner_knuckle/collisions -> 未绑定, /World/RobotArm_4/right_outer_knuckle/visuals -> /World/RobotArm_4/Looks/material_CCCCCC, /World/RobotArm_4/right_outer_knuckle/collisions -> 未绑定, /World/RobotArm_4/right_inner_finger/visuals -> /World/RobotArm_4/Looks/material_191919, /World/RobotArm_4/right_inner_finger/collisions -> 未绑定
* 材质摘要:
 * /World/RobotArm_4/Looks/material_191919 -> Inputs: 'diffuse_color_constant=(0.100, 0.100, 0.100)'
 * /World/RobotArm_4/Looks/material_Black -> Inputs: 'diffuse_color_constant=(0.000, 0.000, 0.000)'
 * /World/RobotArm_4/Looks/material_CCCCCC -> Inputs: 'diffuse_color_constant=(0.800, 0.800, 0.800)'
 * /World/RobotArm_4/Looks/material_White -> Inputs: 'diffuse_color_constant=(1.000, 1.000, 1.000)'


---


### '/World/RobotArm_5' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/5.0/Isaac/Robots/Kawasaki/RS007L/rs007l_onrobot_rg2.usd
* BBox (world): size=(0.572, 0.478, 2.377), center=(0.097, 28.984, 1.349)
* 几何统计: Mesh=28, Vertices=383850, Faces=127950
* 子Mesh材质: /World/RobotArm_5/base_link/visuals -> /World/RobotArm_5/Looks/material_White, /World/RobotArm_5/base_link/collisions -> 未绑定, /World/RobotArm_5/link1/visuals -> /World/RobotArm_5/Looks/material_White, /World/RobotArm_5/link1/collisions -> 未绑定, /World/RobotArm_5/link2/visuals -> /World/RobotArm_5/Looks/material_White, /World/RobotArm_5/link2/collisions -> 未绑定, /World/RobotArm_5/link3/visuals -> /World/RobotArm_5/Looks/material_White, /World/RobotArm_5/link3/collisions -> 未绑定, /World/RobotArm_5/link4/visuals -> /World/RobotArm_5/Looks/material_White, /World/RobotArm_5/link4/collisions -> 未绑定, /World/RobotArm_5/link5/visuals -> /World/RobotArm_5/Looks/material_White, /World/RobotArm_5/link5/collisions -> 未绑定, /World/RobotArm_5/link6/visuals -> /World/RobotArm_5/Looks/material_Black, /World/RobotArm_5/link6/collisions -> 未绑定, /World/RobotArm_5/onrobot_rg2_base_link/visuals -> /World/RobotArm_5/Looks/material_CCCCCC, /World/RobotArm_5/onrobot_rg2_base_link/collisions -> 未绑定, /World/RobotArm_5/left_outer_knuckle/visuals -> /World/RobotArm_5/Looks/material_CCCCCC, /World/RobotArm_5/left_outer_knuckle/collisions -> 未绑定, /World/RobotArm_5/left_inner_finger/visuals -> /World/RobotArm_5/Looks/material_191919, /World/RobotArm_5/left_inner_finger/collisions -> 未绑定, /World/RobotArm_5/left_inner_knuckle/visuals -> /World/RobotArm_5/Looks/material_CCCCCC, /World/RobotArm_5/left_inner_knuckle/collisions -> 未绑定, /World/RobotArm_5/right_inner_knuckle/visuals -> /World/RobotArm_5/Looks/material_CCCCCC, /World/RobotArm_5/right_inner_knuckle/collisions -> 未绑定, /World/RobotArm_5/right_outer_knuckle/visuals -> /World/RobotArm_5/Looks/material_CCCCCC, /World/RobotArm_5/right_outer_knuckle/collisions -> 未绑定, /World/RobotArm_5/right_inner_finger/visuals -> /World/RobotArm_5/Looks/material_191919, /World/RobotArm_5/right_inner_finger/collisions -> 未绑定
* 材质摘要:
 * /World/RobotArm_5/Looks/material_191919 -> Inputs: 'diffuse_color_constant=(0.100, 0.100, 0.100)'
 * /World/RobotArm_5/Looks/material_Black -> Inputs: 'diffuse_color_constant=(0.000, 0.000, 0.000)'
 * /World/RobotArm_5/Looks/material_CCCCCC -> Inputs: 'diffuse_color_constant=(0.800, 0.800, 0.800)'
 * /World/RobotArm_5/Looks/material_White -> Inputs: 'diffuse_color_constant=(1.000, 1.000, 1.000)'


---


### '/World/RobotArm_6' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/5.0/Isaac/Robots/Kawasaki/RS007L/rs007l_onrobot_rg2.usd
* BBox (world): size=(0.572, 0.478, 2.377), center=(5.097, 28.984, 1.349)
* 几何统计: Mesh=28, Vertices=383850, Faces=127950
* 子Mesh材质: /World/RobotArm_6/base_link/visuals -> /World/RobotArm_6/Looks/material_White, /World/RobotArm_6/base_link/collisions -> 未绑定, /World/RobotArm_6/link1/visuals -> /World/RobotArm_6/Looks/material_White, /World/RobotArm_6/link1/collisions -> 未绑定, /World/RobotArm_6/link2/visuals -> /World/RobotArm_6/Looks/material_White, /World/RobotArm_6/link2/collisions -> 未绑定, /World/RobotArm_6/link3/visuals -> /World/RobotArm_6/Looks/material_White, /World/RobotArm_6/link3/collisions -> 未绑定, /World/RobotArm_6/link4/visuals -> /World/RobotArm_6/Looks/material_White, /World/RobotArm_6/link4/collisions -> 未绑定, /World/RobotArm_6/link5/visuals -> /World/RobotArm_6/Looks/material_White, /World/RobotArm_6/link5/collisions -> 未绑定, /World/RobotArm_6/link6/visuals -> /World/RobotArm_6/Looks/material_Black, /World/RobotArm_6/link6/collisions -> 未绑定, /World/RobotArm_6/onrobot_rg2_base_link/visuals -> /World/RobotArm_6/Looks/material_CCCCCC, /World/RobotArm_6/onrobot_rg2_base_link/collisions -> 未绑定, /World/RobotArm_6/left_outer_knuckle/visuals -> /World/RobotArm_6/Looks/material_CCCCCC, /World/RobotArm_6/left_outer_knuckle/collisions -> 未绑定, /World/RobotArm_6/left_inner_finger/visuals -> /World/RobotArm_6/Looks/material_191919, /World/RobotArm_6/left_inner_finger/collisions -> 未绑定, /World/RobotArm_6/left_inner_knuckle/visuals -> /World/RobotArm_6/Looks/material_CCCCCC, /World/RobotArm_6/left_inner_knuckle/collisions -> 未绑定, /World/RobotArm_6/right_inner_knuckle/visuals -> /World/RobotArm_6/Looks/material_CCCCCC, /World/RobotArm_6/right_inner_knuckle/collisions -> 未绑定, /World/RobotArm_6/right_outer_knuckle/visuals -> /World/RobotArm_6/Looks/material_CCCCCC, /World/RobotArm_6/right_outer_knuckle/collisions -> 未绑定, /World/RobotArm_6/right_inner_finger/visuals -> /World/RobotArm_6/Looks/material_191919, /World/RobotArm_6/right_inner_finger/collisions -> 未绑定
* 材质摘要:
 * /World/RobotArm_6/Looks/material_191919 -> Inputs: 'diffuse_color_constant=(0.100, 0.100, 0.100)'
 * /World/RobotArm_6/Looks/material_Black -> Inputs: 'diffuse_color_constant=(0.000, 0.000, 0.000)'
 * /World/RobotArm_6/Looks/material_CCCCCC -> Inputs: 'diffuse_color_constant=(0.800, 0.800, 0.800)'
 * /World/RobotArm_6/Looks/material_White -> Inputs: 'diffuse_color_constant=(1.000, 1.000, 1.000)'


---


### '/World/RobotArm_7' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/5.0/Isaac/Robots/Kawasaki/RS007L/rs007l_onrobot_rg2.usd
* BBox (world): size=(0.572, 0.478, 2.377), center=(10.097, 28.984, 1.349)
* 几何统计: Mesh=28, Vertices=383850, Faces=127950
* 子Mesh材质: /World/RobotArm_7/base_link/visuals -> /World/RobotArm_7/Looks/material_White, /World/RobotArm_7/base_link/collisions -> 未绑定, /World/RobotArm_7/link1/visuals -> /World/RobotArm_7/Looks/material_White, /World/RobotArm_7/link1/collisions -> 未绑定, /World/RobotArm_7/link2/visuals -> /World/RobotArm_7/Looks/material_White, /World/RobotArm_7/link2/collisions -> 未绑定, /World/RobotArm_7/link3/visuals -> /World/RobotArm_7/Looks/material_White, /World/RobotArm_7/link3/collisions -> 未绑定, /World/RobotArm_7/link4/visuals -> /World/RobotArm_7/Looks/material_White, /World/RobotArm_7/link4/collisions -> 未绑定, /World/RobotArm_7/link5/visuals -> /World/RobotArm_7/Looks/material_White, /World/RobotArm_7/link5/collisions -> 未绑定, /World/RobotArm_7/link6/visuals -> /World/RobotArm_7/Looks/material_Black, /World/RobotArm_7/link6/collisions -> 未绑定, /World/RobotArm_7/onrobot_rg2_base_link/visuals -> /World/RobotArm_7/Looks/material_CCCCCC, /World/RobotArm_7/onrobot_rg2_base_link/collisions -> 未绑定, /World/RobotArm_7/left_outer_knuckle/visuals -> /World/RobotArm_7/Looks/material_CCCCCC, /World/RobotArm_7/left_outer_knuckle/collisions -> 未绑定, /World/RobotArm_7/left_inner_finger/visuals -> /World/RobotArm_7/Looks/material_191919, /World/RobotArm_7/left_inner_finger/collisions -> 未绑定, /World/RobotArm_7/left_inner_knuckle/visuals -> /World/RobotArm_7/Looks/material_CCCCCC, /World/RobotArm_7/left_inner_knuckle/collisions -> 未绑定, /World/RobotArm_7/right_inner_knuckle/visuals -> /World/RobotArm_7/Looks/material_CCCCCC, /World/RobotArm_7/right_inner_knuckle/collisions -> 未绑定, /World/RobotArm_7/right_outer_knuckle/visuals -> /World/RobotArm_7/Looks/material_CCCCCC, /World/RobotArm_7/right_outer_knuckle/collisions -> 未绑定, /World/RobotArm_7/right_inner_finger/visuals -> /World/RobotArm_7/Looks/material_191919, /World/RobotArm_7/right_inner_finger/collisions -> 未绑定
* 材质摘要:
 * /World/RobotArm_7/Looks/material_191919 -> Inputs: 'diffuse_color_constant=(0.100, 0.100, 0.100)'
 * /World/RobotArm_7/Looks/material_Black -> Inputs: 'diffuse_color_constant=(0.000, 0.000, 0.000)'
 * /World/RobotArm_7/Looks/material_CCCCCC -> Inputs: 'diffuse_color_constant=(0.800, 0.800, 0.800)'
 * /World/RobotArm_7/Looks/material_White -> Inputs: 'diffuse_color_constant=(1.000, 1.000, 1.000)'


---


### '/World/RobotArm_8' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/5.0/Isaac/Robots/Kawasaki/RS007L/rs007l_onrobot_rg2.usd
* BBox (world): size=(0.572, 0.478, 2.377), center=(15.097, 28.984, 1.349)
* 几何统计: Mesh=28, Vertices=383850, Faces=127950
* 子Mesh材质: /World/RobotArm_8/base_link/visuals -> /World/RobotArm_8/Looks/material_White, /World/RobotArm_8/base_link/collisions -> 未绑定, /World/RobotArm_8/link1/visuals -> /World/RobotArm_8/Looks/material_White, /World/RobotArm_8/link1/collisions -> 未绑定, /World/RobotArm_8/link2/visuals -> /World/RobotArm_8/Looks/material_White, /World/RobotArm_8/link2/collisions -> 未绑定, /World/RobotArm_8/link3/visuals -> /World/RobotArm_8/Looks/material_White, /World/RobotArm_8/link3/collisions -> 未绑定, /World/RobotArm_8/link4/visuals -> /World/RobotArm_8/Looks/material_White, /World/RobotArm_8/link4/collisions -> 未绑定, /World/RobotArm_8/link5/visuals -> /World/RobotArm_8/Looks/material_White, /World/RobotArm_8/link5/collisions -> 未绑定, /World/RobotArm_8/link6/visuals -> /World/RobotArm_8/Looks/material_Black, /World/RobotArm_8/link6/collisions -> 未绑定, /World/RobotArm_8/onrobot_rg2_base_link/visuals -> /World/RobotArm_8/Looks/material_CCCCCC, /World/RobotArm_8/onrobot_rg2_base_link/collisions -> 未绑定, /World/RobotArm_8/left_outer_knuckle/visuals -> /World/RobotArm_8/Looks/material_CCCCCC, /World/RobotArm_8/left_outer_knuckle/collisions -> 未绑定, /World/RobotArm_8/left_inner_finger/visuals -> /World/RobotArm_8/Looks/material_191919, /World/RobotArm_8/left_inner_finger/collisions -> 未绑定, /World/RobotArm_8/left_inner_knuckle/visuals -> /World/RobotArm_8/Looks/material_CCCCCC, /World/RobotArm_8/left_inner_knuckle/collisions -> 未绑定, /World/RobotArm_8/right_inner_knuckle/visuals -> /World/RobotArm_8/Looks/material_CCCCCC, /World/RobotArm_8/right_inner_knuckle/collisions -> 未绑定, /World/RobotArm_8/right_outer_knuckle/visuals -> /World/RobotArm_8/Looks/material_CCCCCC, /World/RobotArm_8/right_outer_knuckle/collisions -> 未绑定, /World/RobotArm_8/right_inner_finger/visuals -> /World/RobotArm_8/Looks/material_191919, /World/RobotArm_8/right_inner_finger/collisions -> 未绑定
* 材质摘要:
 * /World/RobotArm_8/Looks/material_191919 -> Inputs: 'diffuse_color_constant=(0.100, 0.100, 0.100)'
 * /World/RobotArm_8/Looks/material_Black -> Inputs: 'diffuse_color_constant=(0.000, 0.000, 0.000)'
 * /World/RobotArm_8/Looks/material_CCCCCC -> Inputs: 'diffuse_color_constant=(0.800, 0.800, 0.800)'
 * /World/RobotArm_8/Looks/material_White -> Inputs: 'diffuse_color_constant=(1.000, 1.000, 1.000)'


---


### '/World/RobotArm1_1' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/5.0/Isaac/Robots/Ufactory/xarm7/xarm7.usd; payload:./configuration/xarm7_physics.usd
* BBox (world): size=(0.616, 0.455, 1.292), center=(-17.318, 29.010, 0.723)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_1/gripper' (Xform)
* 引用: payload:../xarm_gripper/xarm_gripper.usd
* BBox (world): size=(0.150, 0.346, 0.324), center=(-17.088, 29.000, 0.239)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_1/gripper/xarm_gripper_base_link/visuals' (Xform)
* 引用: reference:/visuals/xarm_gripper_base_link @/visuals/xarm_gripper_base_link
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.150, 0.213, 0.209), center=(-17.088, 29.000, 0.297)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_1/gripper/xarm_gripper_base_link/collisions' (Xform)
* 引用: reference:/colliders/xarm_gripper_base_link @/colliders/xarm_gripper_base_link
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(-17.088, 29.000, 0.401)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_1/gripper/left_outer_knuckle/visuals' (Xform)
* 引用: reference:/visuals/left_outer_knuckle @/visuals/left_outer_knuckle
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.024, 0.155, 0.111), center=(-17.088, 28.904, 0.242)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_1/gripper/left_outer_knuckle/collisions' (Xform)
* 引用: reference:/colliders/left_outer_knuckle @/colliders/left_outer_knuckle
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(-17.088, 28.930, 0.283)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_1/gripper/left_finger/visuals' (Xform)
* 引用: reference:/visuals/left_finger @/visuals/left_finger
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.064, 0.064, 0.134), center=(-17.088, 28.879, 0.144)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_1/gripper/left_finger/collisions' (Xform)
* 引用: reference:/colliders/left_finger @/colliders/left_finger
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(-17.088, 28.859, 0.199)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_1/gripper/left_inner_knuckle/visuals' (Xform)
* 引用: reference:/visuals/left_inner_knuckle @/visuals/left_inner_knuckle
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.056, 0.095, 0.108), center=(-17.088, 28.925, 0.211)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_1/gripper/left_inner_knuckle/collisions' (Xform)
* 引用: reference:/colliders/left_inner_knuckle @/colliders/left_inner_knuckle
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(-17.088, 28.960, 0.253)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_1/gripper/right_inner_knuckle/visuals' (Xform)
* 引用: reference:/visuals/right_inner_knuckle @/visuals/right_inner_knuckle
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.056, 0.095, 0.108), center=(-17.088, 29.075, 0.211)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_1/gripper/right_inner_knuckle/collisions' (Xform)
* 引用: reference:/colliders/right_inner_knuckle @/colliders/right_inner_knuckle
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(-17.088, 29.040, 0.253)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_1/gripper/right_outer_knuckle/visuals' (Xform)
* 引用: reference:/visuals/right_outer_knuckle @/visuals/right_outer_knuckle
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.024, 0.155, 0.111), center=(-17.088, 29.096, 0.242)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_1/gripper/right_outer_knuckle/collisions' (Xform)
* 引用: reference:/colliders/right_outer_knuckle @/colliders/right_outer_knuckle
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(-17.088, 29.070, 0.283)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_1/gripper/right_finger/visuals' (Xform)
* 引用: reference:/visuals/right_finger @/visuals/right_finger
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.064, 0.064, 0.134), center=(-17.088, 29.121, 0.144)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_1/gripper/right_finger/collisions' (Xform)
* 引用: reference:/colliders/right_finger @/colliders/right_finger
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(-17.088, 29.141, 0.199)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_1/world/visuals' (Xform)
* 引用: reference:/visuals/world @/visuals/world
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.252, 0.252, 0.301), center=(-17.500, 29.000, 0.310)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_1/world/collisions' (Xform)
* 引用: reference:/colliders/world @/colliders/world
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(-17.500, 29.000, 0.160)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_1/link1/visuals' (Xform)
* 引用: reference:/visuals/link1 @/visuals/link1
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.194, 0.232, 0.329), center=(-17.500, 29.002, 0.627)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_1/link1/collisions' (Xform)
* 引用: reference:/colliders/link1 @/colliders/link1
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(-17.500, 29.000, 0.694)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_1/link2/visuals' (Xform)
* 引用: reference:/visuals/link2 @/visuals/link2
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.194, 0.326, 0.463), center=(-17.500, 29.074, 0.828)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_1/link2/collisions' (Xform)
* 引用: reference:/colliders/link2 @/colliders/link2
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(-17.500, 29.000, 0.694)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_1/link3/visuals' (Xform)
* 引用: reference:/visuals/link3 @/visuals/link3
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.283, 0.229, 0.309), center=(-17.448, 29.023, 1.215)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_1/link3/collisions' (Xform)
* 引用: reference:/colliders/link3 @/colliders/link3
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(-17.500, 29.000, 1.280)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_1/link4/visuals' (Xform)
* 引用: reference:/visuals/link4 @/visuals/link4
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.334, 0.308, 0.414), center=(-17.317, 28.936, 1.162)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_1/link4/collisions' (Xform)
* 引用: reference:/colliders/link4 @/colliders/link4
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(-17.395, 29.000, 1.280)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_1/link5/visuals' (Xform)
* 引用: reference:/visuals/link5 @/visuals/link5
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.180, 0.262, 0.440), center=(-17.240, 28.959, 0.738)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_1/link5/collisions' (Xform)
* 引用: reference:/colliders/link5 @/colliders/link5
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(-17.240, 29.000, 0.595)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_1/link6/visuals' (Xform)
* 引用: reference:/visuals/link6 @/visuals/link6
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.307, 0.200, 0.212), center=(-17.164, 29.022, 0.566)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_1/link6/collisions' (Xform)
* 引用: reference:/colliders/link6 @/colliders/link6
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(-17.240, 29.000, 0.595)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_1/link7/visuals' (Xform)
* 引用: reference:/visuals/link7 @/visuals/link7
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.156, 0.186, 0.066), center=(-17.088, 29.015, 0.434)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_1/link7/collisions' (Xform)
* 引用: reference:/colliders/link7 @/colliders/link7
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(-17.088, 29.000, 0.401)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_2' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/5.0/Isaac/Robots/Ufactory/xarm7/xarm7.usd; payload:./configuration/xarm7_physics.usd
* BBox (world): size=(0.616, 0.455, 1.292), center=(-12.318, 29.010, 0.723)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_2/gripper' (Xform)
* 引用: payload:../xarm_gripper/xarm_gripper.usd
* BBox (world): size=(0.150, 0.346, 0.324), center=(-12.088, 29.000, 0.239)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_2/gripper/xarm_gripper_base_link/visuals' (Xform)
* 引用: reference:/visuals/xarm_gripper_base_link @/visuals/xarm_gripper_base_link
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.150, 0.213, 0.209), center=(-12.088, 29.000, 0.297)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_2/gripper/xarm_gripper_base_link/collisions' (Xform)
* 引用: reference:/colliders/xarm_gripper_base_link @/colliders/xarm_gripper_base_link
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(-12.088, 29.000, 0.401)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_2/gripper/left_outer_knuckle/visuals' (Xform)
* 引用: reference:/visuals/left_outer_knuckle @/visuals/left_outer_knuckle
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.024, 0.155, 0.111), center=(-12.088, 28.904, 0.242)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_2/gripper/left_outer_knuckle/collisions' (Xform)
* 引用: reference:/colliders/left_outer_knuckle @/colliders/left_outer_knuckle
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(-12.088, 28.930, 0.283)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_2/gripper/left_finger/visuals' (Xform)
* 引用: reference:/visuals/left_finger @/visuals/left_finger
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.064, 0.064, 0.134), center=(-12.088, 28.879, 0.144)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_2/gripper/left_finger/collisions' (Xform)
* 引用: reference:/colliders/left_finger @/colliders/left_finger
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(-12.088, 28.859, 0.199)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_2/gripper/left_inner_knuckle/visuals' (Xform)
* 引用: reference:/visuals/left_inner_knuckle @/visuals/left_inner_knuckle
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.056, 0.095, 0.108), center=(-12.088, 28.925, 0.211)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_2/gripper/left_inner_knuckle/collisions' (Xform)
* 引用: reference:/colliders/left_inner_knuckle @/colliders/left_inner_knuckle
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(-12.088, 28.960, 0.253)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_2/gripper/right_inner_knuckle/visuals' (Xform)
* 引用: reference:/visuals/right_inner_knuckle @/visuals/right_inner_knuckle
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.056, 0.095, 0.108), center=(-12.088, 29.075, 0.211)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_2/gripper/right_inner_knuckle/collisions' (Xform)
* 引用: reference:/colliders/right_inner_knuckle @/colliders/right_inner_knuckle
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(-12.088, 29.040, 0.253)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_2/gripper/right_outer_knuckle/visuals' (Xform)
* 引用: reference:/visuals/right_outer_knuckle @/visuals/right_outer_knuckle
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.024, 0.155, 0.111), center=(-12.088, 29.096, 0.242)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_2/gripper/right_outer_knuckle/collisions' (Xform)
* 引用: reference:/colliders/right_outer_knuckle @/colliders/right_outer_knuckle
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(-12.088, 29.070, 0.283)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_2/gripper/right_finger/visuals' (Xform)
* 引用: reference:/visuals/right_finger @/visuals/right_finger
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.064, 0.064, 0.134), center=(-12.088, 29.121, 0.144)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_2/gripper/right_finger/collisions' (Xform)
* 引用: reference:/colliders/right_finger @/colliders/right_finger
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(-12.088, 29.141, 0.199)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_2/world/visuals' (Xform)
* 引用: reference:/visuals/world @/visuals/world
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.252, 0.252, 0.301), center=(-12.500, 29.000, 0.310)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_2/world/collisions' (Xform)
* 引用: reference:/colliders/world @/colliders/world
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(-12.500, 29.000, 0.160)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_2/link1/visuals' (Xform)
* 引用: reference:/visuals/link1 @/visuals/link1
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.194, 0.232, 0.329), center=(-12.500, 29.002, 0.627)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_2/link1/collisions' (Xform)
* 引用: reference:/colliders/link1 @/colliders/link1
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(-12.500, 29.000, 0.694)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_2/link2/visuals' (Xform)
* 引用: reference:/visuals/link2 @/visuals/link2
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.194, 0.326, 0.463), center=(-12.500, 29.074, 0.828)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_2/link2/collisions' (Xform)
* 引用: reference:/colliders/link2 @/colliders/link2
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(-12.500, 29.000, 0.694)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_2/link3/visuals' (Xform)
* 引用: reference:/visuals/link3 @/visuals/link3
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.283, 0.229, 0.309), center=(-12.448, 29.023, 1.215)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_2/link3/collisions' (Xform)
* 引用: reference:/colliders/link3 @/colliders/link3
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(-12.500, 29.000, 1.280)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_2/link4/visuals' (Xform)
* 引用: reference:/visuals/link4 @/visuals/link4
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.334, 0.308, 0.414), center=(-12.317, 28.936, 1.162)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_2/link4/collisions' (Xform)
* 引用: reference:/colliders/link4 @/colliders/link4
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(-12.395, 29.000, 1.280)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_2/link5/visuals' (Xform)
* 引用: reference:/visuals/link5 @/visuals/link5
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.180, 0.262, 0.440), center=(-12.240, 28.959, 0.738)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_2/link5/collisions' (Xform)
* 引用: reference:/colliders/link5 @/colliders/link5
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(-12.240, 29.000, 0.595)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_2/link6/visuals' (Xform)
* 引用: reference:/visuals/link6 @/visuals/link6
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.307, 0.200, 0.212), center=(-12.164, 29.022, 0.566)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_2/link6/collisions' (Xform)
* 引用: reference:/colliders/link6 @/colliders/link6
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(-12.240, 29.000, 0.595)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_2/link7/visuals' (Xform)
* 引用: reference:/visuals/link7 @/visuals/link7
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.156, 0.186, 0.066), center=(-12.088, 29.015, 0.434)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_2/link7/collisions' (Xform)
* 引用: reference:/colliders/link7 @/colliders/link7
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(-12.088, 29.000, 0.401)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_3' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/5.0/Isaac/Robots/Ufactory/xarm7/xarm7.usd; payload:./configuration/xarm7_physics.usd
* BBox (world): size=(0.616, 0.455, 1.292), center=(-7.318, 29.010, 0.723)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_3/gripper' (Xform)
* 引用: payload:../xarm_gripper/xarm_gripper.usd
* BBox (world): size=(0.150, 0.346, 0.324), center=(-7.088, 29.000, 0.239)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_3/gripper/xarm_gripper_base_link/visuals' (Xform)
* 引用: reference:/visuals/xarm_gripper_base_link @/visuals/xarm_gripper_base_link
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.150, 0.213, 0.209), center=(-7.088, 29.000, 0.297)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_3/gripper/xarm_gripper_base_link/collisions' (Xform)
* 引用: reference:/colliders/xarm_gripper_base_link @/colliders/xarm_gripper_base_link
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(-7.088, 29.000, 0.401)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_3/gripper/left_outer_knuckle/visuals' (Xform)
* 引用: reference:/visuals/left_outer_knuckle @/visuals/left_outer_knuckle
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.024, 0.155, 0.111), center=(-7.088, 28.904, 0.242)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_3/gripper/left_outer_knuckle/collisions' (Xform)
* 引用: reference:/colliders/left_outer_knuckle @/colliders/left_outer_knuckle
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(-7.088, 28.930, 0.283)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_3/gripper/left_finger/visuals' (Xform)
* 引用: reference:/visuals/left_finger @/visuals/left_finger
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.064, 0.064, 0.134), center=(-7.088, 28.879, 0.144)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_3/gripper/left_finger/collisions' (Xform)
* 引用: reference:/colliders/left_finger @/colliders/left_finger
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(-7.088, 28.859, 0.199)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_3/gripper/left_inner_knuckle/visuals' (Xform)
* 引用: reference:/visuals/left_inner_knuckle @/visuals/left_inner_knuckle
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.056, 0.095, 0.108), center=(-7.088, 28.925, 0.211)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_3/gripper/left_inner_knuckle/collisions' (Xform)
* 引用: reference:/colliders/left_inner_knuckle @/colliders/left_inner_knuckle
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(-7.088, 28.960, 0.253)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_3/gripper/right_inner_knuckle/visuals' (Xform)
* 引用: reference:/visuals/right_inner_knuckle @/visuals/right_inner_knuckle
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.056, 0.095, 0.108), center=(-7.088, 29.075, 0.211)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_3/gripper/right_inner_knuckle/collisions' (Xform)
* 引用: reference:/colliders/right_inner_knuckle @/colliders/right_inner_knuckle
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(-7.088, 29.040, 0.253)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_3/gripper/right_outer_knuckle/visuals' (Xform)
* 引用: reference:/visuals/right_outer_knuckle @/visuals/right_outer_knuckle
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.024, 0.155, 0.111), center=(-7.088, 29.096, 0.242)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_3/gripper/right_outer_knuckle/collisions' (Xform)
* 引用: reference:/colliders/right_outer_knuckle @/colliders/right_outer_knuckle
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(-7.088, 29.070, 0.283)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_3/gripper/right_finger/visuals' (Xform)
* 引用: reference:/visuals/right_finger @/visuals/right_finger
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.064, 0.064, 0.134), center=(-7.088, 29.121, 0.144)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_3/gripper/right_finger/collisions' (Xform)
* 引用: reference:/colliders/right_finger @/colliders/right_finger
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(-7.088, 29.141, 0.199)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_3/world/visuals' (Xform)
* 引用: reference:/visuals/world @/visuals/world
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.252, 0.252, 0.301), center=(-7.500, 29.000, 0.310)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_3/world/collisions' (Xform)
* 引用: reference:/colliders/world @/colliders/world
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(-7.500, 29.000, 0.160)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_3/link1/visuals' (Xform)
* 引用: reference:/visuals/link1 @/visuals/link1
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.194, 0.232, 0.329), center=(-7.500, 29.002, 0.627)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_3/link1/collisions' (Xform)
* 引用: reference:/colliders/link1 @/colliders/link1
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(-7.500, 29.000, 0.694)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_3/link2/visuals' (Xform)
* 引用: reference:/visuals/link2 @/visuals/link2
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.194, 0.326, 0.463), center=(-7.500, 29.074, 0.828)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_3/link2/collisions' (Xform)
* 引用: reference:/colliders/link2 @/colliders/link2
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(-7.500, 29.000, 0.694)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_3/link3/visuals' (Xform)
* 引用: reference:/visuals/link3 @/visuals/link3
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.283, 0.229, 0.309), center=(-7.448, 29.023, 1.215)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_3/link3/collisions' (Xform)
* 引用: reference:/colliders/link3 @/colliders/link3
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(-7.500, 29.000, 1.280)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_3/link4/visuals' (Xform)
* 引用: reference:/visuals/link4 @/visuals/link4
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.334, 0.308, 0.414), center=(-7.317, 28.936, 1.162)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_3/link4/collisions' (Xform)
* 引用: reference:/colliders/link4 @/colliders/link4
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(-7.395, 29.000, 1.280)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_3/link5/visuals' (Xform)
* 引用: reference:/visuals/link5 @/visuals/link5
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.180, 0.262, 0.440), center=(-7.240, 28.959, 0.738)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_3/link5/collisions' (Xform)
* 引用: reference:/colliders/link5 @/colliders/link5
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(-7.240, 29.000, 0.595)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_3/link6/visuals' (Xform)
* 引用: reference:/visuals/link6 @/visuals/link6
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.307, 0.200, 0.212), center=(-7.164, 29.022, 0.566)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_3/link6/collisions' (Xform)
* 引用: reference:/colliders/link6 @/colliders/link6
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(-7.240, 29.000, 0.595)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_3/link7/visuals' (Xform)
* 引用: reference:/visuals/link7 @/visuals/link7
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.156, 0.186, 0.066), center=(-7.088, 29.015, 0.434)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_3/link7/collisions' (Xform)
* 引用: reference:/colliders/link7 @/colliders/link7
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(-7.088, 29.000, 0.401)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_4' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/5.0/Isaac/Robots/Ufactory/xarm7/xarm7.usd; payload:./configuration/xarm7_physics.usd
* BBox (world): size=(0.616, 0.455, 1.292), center=(-2.318, 29.010, 0.723)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_4/gripper' (Xform)
* 引用: payload:../xarm_gripper/xarm_gripper.usd
* BBox (world): size=(0.150, 0.346, 0.324), center=(-2.088, 29.000, 0.239)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_4/gripper/xarm_gripper_base_link/visuals' (Xform)
* 引用: reference:/visuals/xarm_gripper_base_link @/visuals/xarm_gripper_base_link
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.150, 0.213, 0.209), center=(-2.088, 29.000, 0.297)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_4/gripper/xarm_gripper_base_link/collisions' (Xform)
* 引用: reference:/colliders/xarm_gripper_base_link @/colliders/xarm_gripper_base_link
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(-2.088, 29.000, 0.401)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_4/gripper/left_outer_knuckle/visuals' (Xform)
* 引用: reference:/visuals/left_outer_knuckle @/visuals/left_outer_knuckle
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.024, 0.155, 0.111), center=(-2.088, 28.904, 0.242)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_4/gripper/left_outer_knuckle/collisions' (Xform)
* 引用: reference:/colliders/left_outer_knuckle @/colliders/left_outer_knuckle
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(-2.088, 28.930, 0.283)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_4/gripper/left_finger/visuals' (Xform)
* 引用: reference:/visuals/left_finger @/visuals/left_finger
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.064, 0.064, 0.134), center=(-2.088, 28.879, 0.144)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_4/gripper/left_finger/collisions' (Xform)
* 引用: reference:/colliders/left_finger @/colliders/left_finger
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(-2.088, 28.859, 0.199)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_4/gripper/left_inner_knuckle/visuals' (Xform)
* 引用: reference:/visuals/left_inner_knuckle @/visuals/left_inner_knuckle
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.056, 0.095, 0.108), center=(-2.088, 28.925, 0.211)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_4/gripper/left_inner_knuckle/collisions' (Xform)
* 引用: reference:/colliders/left_inner_knuckle @/colliders/left_inner_knuckle
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(-2.088, 28.960, 0.253)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_4/gripper/right_inner_knuckle/visuals' (Xform)
* 引用: reference:/visuals/right_inner_knuckle @/visuals/right_inner_knuckle
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.056, 0.095, 0.108), center=(-2.088, 29.075, 0.211)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_4/gripper/right_inner_knuckle/collisions' (Xform)
* 引用: reference:/colliders/right_inner_knuckle @/colliders/right_inner_knuckle
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(-2.088, 29.040, 0.253)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_4/gripper/right_outer_knuckle/visuals' (Xform)
* 引用: reference:/visuals/right_outer_knuckle @/visuals/right_outer_knuckle
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.024, 0.155, 0.111), center=(-2.088, 29.096, 0.242)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_4/gripper/right_outer_knuckle/collisions' (Xform)
* 引用: reference:/colliders/right_outer_knuckle @/colliders/right_outer_knuckle
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(-2.088, 29.070, 0.283)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_4/gripper/right_finger/visuals' (Xform)
* 引用: reference:/visuals/right_finger @/visuals/right_finger
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.064, 0.064, 0.134), center=(-2.088, 29.121, 0.144)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_4/gripper/right_finger/collisions' (Xform)
* 引用: reference:/colliders/right_finger @/colliders/right_finger
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(-2.088, 29.141, 0.199)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_4/world/visuals' (Xform)
* 引用: reference:/visuals/world @/visuals/world
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.252, 0.252, 0.301), center=(-2.500, 29.000, 0.310)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_4/world/collisions' (Xform)
* 引用: reference:/colliders/world @/colliders/world
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(-2.500, 29.000, 0.160)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_4/link1/visuals' (Xform)
* 引用: reference:/visuals/link1 @/visuals/link1
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.194, 0.232, 0.329), center=(-2.500, 29.002, 0.627)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_4/link1/collisions' (Xform)
* 引用: reference:/colliders/link1 @/colliders/link1
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(-2.500, 29.000, 0.694)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_4/link2/visuals' (Xform)
* 引用: reference:/visuals/link2 @/visuals/link2
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.194, 0.326, 0.463), center=(-2.500, 29.074, 0.828)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_4/link2/collisions' (Xform)
* 引用: reference:/colliders/link2 @/colliders/link2
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(-2.500, 29.000, 0.694)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_4/link3/visuals' (Xform)
* 引用: reference:/visuals/link3 @/visuals/link3
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.283, 0.229, 0.309), center=(-2.448, 29.023, 1.215)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_4/link3/collisions' (Xform)
* 引用: reference:/colliders/link3 @/colliders/link3
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(-2.500, 29.000, 1.280)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_4/link4/visuals' (Xform)
* 引用: reference:/visuals/link4 @/visuals/link4
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.334, 0.308, 0.414), center=(-2.317, 28.936, 1.162)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_4/link4/collisions' (Xform)
* 引用: reference:/colliders/link4 @/colliders/link4
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(-2.395, 29.000, 1.280)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_4/link5/visuals' (Xform)
* 引用: reference:/visuals/link5 @/visuals/link5
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.180, 0.262, 0.440), center=(-2.240, 28.959, 0.738)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_4/link5/collisions' (Xform)
* 引用: reference:/colliders/link5 @/colliders/link5
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(-2.240, 29.000, 0.595)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_4/link6/visuals' (Xform)
* 引用: reference:/visuals/link6 @/visuals/link6
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.307, 0.200, 0.212), center=(-2.164, 29.022, 0.566)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_4/link6/collisions' (Xform)
* 引用: reference:/colliders/link6 @/colliders/link6
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(-2.240, 29.000, 0.595)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_4/link7/visuals' (Xform)
* 引用: reference:/visuals/link7 @/visuals/link7
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.156, 0.186, 0.066), center=(-2.088, 29.015, 0.434)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_4/link7/collisions' (Xform)
* 引用: reference:/colliders/link7 @/colliders/link7
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(-2.088, 29.000, 0.401)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_5' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/5.0/Isaac/Robots/Ufactory/xarm7/xarm7.usd; payload:./configuration/xarm7_physics.usd
* BBox (world): size=(0.616, 0.455, 1.292), center=(2.682, 29.010, 0.723)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_5/gripper' (Xform)
* 引用: payload:../xarm_gripper/xarm_gripper.usd
* BBox (world): size=(0.150, 0.346, 0.324), center=(2.912, 29.000, 0.239)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_5/gripper/xarm_gripper_base_link/visuals' (Xform)
* 引用: reference:/visuals/xarm_gripper_base_link @/visuals/xarm_gripper_base_link
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.150, 0.213, 0.209), center=(2.912, 29.000, 0.297)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_5/gripper/xarm_gripper_base_link/collisions' (Xform)
* 引用: reference:/colliders/xarm_gripper_base_link @/colliders/xarm_gripper_base_link
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(2.912, 29.000, 0.401)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_5/gripper/left_outer_knuckle/visuals' (Xform)
* 引用: reference:/visuals/left_outer_knuckle @/visuals/left_outer_knuckle
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.024, 0.155, 0.111), center=(2.912, 28.904, 0.242)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_5/gripper/left_outer_knuckle/collisions' (Xform)
* 引用: reference:/colliders/left_outer_knuckle @/colliders/left_outer_knuckle
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(2.912, 28.930, 0.283)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_5/gripper/left_finger/visuals' (Xform)
* 引用: reference:/visuals/left_finger @/visuals/left_finger
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.064, 0.064, 0.134), center=(2.912, 28.879, 0.144)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_5/gripper/left_finger/collisions' (Xform)
* 引用: reference:/colliders/left_finger @/colliders/left_finger
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(2.912, 28.859, 0.199)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_5/gripper/left_inner_knuckle/visuals' (Xform)
* 引用: reference:/visuals/left_inner_knuckle @/visuals/left_inner_knuckle
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.056, 0.095, 0.108), center=(2.912, 28.925, 0.211)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_5/gripper/left_inner_knuckle/collisions' (Xform)
* 引用: reference:/colliders/left_inner_knuckle @/colliders/left_inner_knuckle
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(2.912, 28.960, 0.253)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_5/gripper/right_inner_knuckle/visuals' (Xform)
* 引用: reference:/visuals/right_inner_knuckle @/visuals/right_inner_knuckle
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.056, 0.095, 0.108), center=(2.912, 29.075, 0.211)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_5/gripper/right_inner_knuckle/collisions' (Xform)
* 引用: reference:/colliders/right_inner_knuckle @/colliders/right_inner_knuckle
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(2.912, 29.040, 0.253)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_5/gripper/right_outer_knuckle/visuals' (Xform)
* 引用: reference:/visuals/right_outer_knuckle @/visuals/right_outer_knuckle
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.024, 0.155, 0.111), center=(2.912, 29.096, 0.242)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_5/gripper/right_outer_knuckle/collisions' (Xform)
* 引用: reference:/colliders/right_outer_knuckle @/colliders/right_outer_knuckle
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(2.912, 29.070, 0.283)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_5/gripper/right_finger/visuals' (Xform)
* 引用: reference:/visuals/right_finger @/visuals/right_finger
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.064, 0.064, 0.134), center=(2.912, 29.121, 0.144)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_5/gripper/right_finger/collisions' (Xform)
* 引用: reference:/colliders/right_finger @/colliders/right_finger
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(2.912, 29.141, 0.199)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_5/world/visuals' (Xform)
* 引用: reference:/visuals/world @/visuals/world
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.252, 0.252, 0.301), center=(2.500, 29.000, 0.310)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_5/world/collisions' (Xform)
* 引用: reference:/colliders/world @/colliders/world
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(2.500, 29.000, 0.160)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_5/link1/visuals' (Xform)
* 引用: reference:/visuals/link1 @/visuals/link1
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.194, 0.232, 0.329), center=(2.500, 29.002, 0.627)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_5/link1/collisions' (Xform)
* 引用: reference:/colliders/link1 @/colliders/link1
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(2.500, 29.000, 0.694)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_5/link2/visuals' (Xform)
* 引用: reference:/visuals/link2 @/visuals/link2
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.194, 0.326, 0.463), center=(2.500, 29.074, 0.828)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_5/link2/collisions' (Xform)
* 引用: reference:/colliders/link2 @/colliders/link2
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(2.500, 29.000, 0.694)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_5/link3/visuals' (Xform)
* 引用: reference:/visuals/link3 @/visuals/link3
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.283, 0.229, 0.309), center=(2.552, 29.023, 1.215)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_5/link3/collisions' (Xform)
* 引用: reference:/colliders/link3 @/colliders/link3
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(2.500, 29.000, 1.280)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_5/link4/visuals' (Xform)
* 引用: reference:/visuals/link4 @/visuals/link4
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.334, 0.308, 0.414), center=(2.683, 28.936, 1.162)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_5/link4/collisions' (Xform)
* 引用: reference:/colliders/link4 @/colliders/link4
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(2.605, 29.000, 1.280)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_5/link5/visuals' (Xform)
* 引用: reference:/visuals/link5 @/visuals/link5
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.180, 0.262, 0.440), center=(2.760, 28.959, 0.738)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_5/link5/collisions' (Xform)
* 引用: reference:/colliders/link5 @/colliders/link5
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(2.760, 29.000, 0.595)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_5/link6/visuals' (Xform)
* 引用: reference:/visuals/link6 @/visuals/link6
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.307, 0.200, 0.212), center=(2.836, 29.022, 0.566)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_5/link6/collisions' (Xform)
* 引用: reference:/colliders/link6 @/colliders/link6
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(2.760, 29.000, 0.595)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_5/link7/visuals' (Xform)
* 引用: reference:/visuals/link7 @/visuals/link7
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.156, 0.186, 0.066), center=(2.912, 29.015, 0.434)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_5/link7/collisions' (Xform)
* 引用: reference:/colliders/link7 @/colliders/link7
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(2.912, 29.000, 0.401)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_6' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/5.0/Isaac/Robots/Ufactory/xarm7/xarm7.usd; payload:./configuration/xarm7_physics.usd
* BBox (world): size=(0.616, 0.455, 1.292), center=(7.682, 29.010, 0.723)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_6/gripper' (Xform)
* 引用: payload:../xarm_gripper/xarm_gripper.usd
* BBox (world): size=(0.150, 0.346, 0.324), center=(7.912, 29.000, 0.239)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_6/gripper/xarm_gripper_base_link/visuals' (Xform)
* 引用: reference:/visuals/xarm_gripper_base_link @/visuals/xarm_gripper_base_link
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.150, 0.213, 0.209), center=(7.912, 29.000, 0.297)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_6/gripper/xarm_gripper_base_link/collisions' (Xform)
* 引用: reference:/colliders/xarm_gripper_base_link @/colliders/xarm_gripper_base_link
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(7.912, 29.000, 0.401)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_6/gripper/left_outer_knuckle/visuals' (Xform)
* 引用: reference:/visuals/left_outer_knuckle @/visuals/left_outer_knuckle
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.024, 0.155, 0.111), center=(7.912, 28.904, 0.242)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_6/gripper/left_outer_knuckle/collisions' (Xform)
* 引用: reference:/colliders/left_outer_knuckle @/colliders/left_outer_knuckle
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(7.912, 28.930, 0.283)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_6/gripper/left_finger/visuals' (Xform)
* 引用: reference:/visuals/left_finger @/visuals/left_finger
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.064, 0.064, 0.134), center=(7.912, 28.879, 0.144)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_6/gripper/left_finger/collisions' (Xform)
* 引用: reference:/colliders/left_finger @/colliders/left_finger
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(7.912, 28.859, 0.199)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_6/gripper/left_inner_knuckle/visuals' (Xform)
* 引用: reference:/visuals/left_inner_knuckle @/visuals/left_inner_knuckle
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.056, 0.095, 0.108), center=(7.912, 28.925, 0.211)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_6/gripper/left_inner_knuckle/collisions' (Xform)
* 引用: reference:/colliders/left_inner_knuckle @/colliders/left_inner_knuckle
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(7.912, 28.960, 0.253)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_6/gripper/right_inner_knuckle/visuals' (Xform)
* 引用: reference:/visuals/right_inner_knuckle @/visuals/right_inner_knuckle
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.056, 0.095, 0.108), center=(7.912, 29.075, 0.211)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_6/gripper/right_inner_knuckle/collisions' (Xform)
* 引用: reference:/colliders/right_inner_knuckle @/colliders/right_inner_knuckle
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(7.912, 29.040, 0.253)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_6/gripper/right_outer_knuckle/visuals' (Xform)
* 引用: reference:/visuals/right_outer_knuckle @/visuals/right_outer_knuckle
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.024, 0.155, 0.111), center=(7.912, 29.096, 0.242)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_6/gripper/right_outer_knuckle/collisions' (Xform)
* 引用: reference:/colliders/right_outer_knuckle @/colliders/right_outer_knuckle
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(7.912, 29.070, 0.283)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_6/gripper/right_finger/visuals' (Xform)
* 引用: reference:/visuals/right_finger @/visuals/right_finger
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.064, 0.064, 0.134), center=(7.912, 29.121, 0.144)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_6/gripper/right_finger/collisions' (Xform)
* 引用: reference:/colliders/right_finger @/colliders/right_finger
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(7.912, 29.141, 0.199)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_6/world/visuals' (Xform)
* 引用: reference:/visuals/world @/visuals/world
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.252, 0.252, 0.301), center=(7.500, 29.000, 0.310)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_6/world/collisions' (Xform)
* 引用: reference:/colliders/world @/colliders/world
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(7.500, 29.000, 0.160)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_6/link1/visuals' (Xform)
* 引用: reference:/visuals/link1 @/visuals/link1
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.194, 0.232, 0.329), center=(7.500, 29.002, 0.627)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_6/link1/collisions' (Xform)
* 引用: reference:/colliders/link1 @/colliders/link1
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(7.500, 29.000, 0.694)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_6/link2/visuals' (Xform)
* 引用: reference:/visuals/link2 @/visuals/link2
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.194, 0.326, 0.463), center=(7.500, 29.074, 0.828)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_6/link2/collisions' (Xform)
* 引用: reference:/colliders/link2 @/colliders/link2
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(7.500, 29.000, 0.694)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_6/link3/visuals' (Xform)
* 引用: reference:/visuals/link3 @/visuals/link3
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.283, 0.229, 0.309), center=(7.552, 29.023, 1.215)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_6/link3/collisions' (Xform)
* 引用: reference:/colliders/link3 @/colliders/link3
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(7.500, 29.000, 1.280)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_6/link4/visuals' (Xform)
* 引用: reference:/visuals/link4 @/visuals/link4
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.334, 0.308, 0.414), center=(7.683, 28.936, 1.162)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_6/link4/collisions' (Xform)
* 引用: reference:/colliders/link4 @/colliders/link4
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(7.605, 29.000, 1.280)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_6/link5/visuals' (Xform)
* 引用: reference:/visuals/link5 @/visuals/link5
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.180, 0.262, 0.440), center=(7.760, 28.959, 0.738)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_6/link5/collisions' (Xform)
* 引用: reference:/colliders/link5 @/colliders/link5
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(7.760, 29.000, 0.595)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_6/link6/visuals' (Xform)
* 引用: reference:/visuals/link6 @/visuals/link6
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.307, 0.200, 0.212), center=(7.836, 29.022, 0.566)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_6/link6/collisions' (Xform)
* 引用: reference:/colliders/link6 @/colliders/link6
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(7.760, 29.000, 0.595)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_6/link7/visuals' (Xform)
* 引用: reference:/visuals/link7 @/visuals/link7
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.156, 0.186, 0.066), center=(7.912, 29.015, 0.434)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_6/link7/collisions' (Xform)
* 引用: reference:/colliders/link7 @/colliders/link7
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(7.912, 29.000, 0.401)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_7' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/5.0/Isaac/Robots/Ufactory/xarm7/xarm7.usd; payload:./configuration/xarm7_physics.usd
* BBox (world): size=(0.616, 0.455, 1.292), center=(12.682, 29.010, 0.723)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_7/gripper' (Xform)
* 引用: payload:../xarm_gripper/xarm_gripper.usd
* BBox (world): size=(0.150, 0.346, 0.324), center=(12.912, 29.000, 0.239)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_7/gripper/xarm_gripper_base_link/visuals' (Xform)
* 引用: reference:/visuals/xarm_gripper_base_link @/visuals/xarm_gripper_base_link
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.150, 0.213, 0.209), center=(12.912, 29.000, 0.297)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_7/gripper/xarm_gripper_base_link/collisions' (Xform)
* 引用: reference:/colliders/xarm_gripper_base_link @/colliders/xarm_gripper_base_link
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(12.912, 29.000, 0.401)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_7/gripper/left_outer_knuckle/visuals' (Xform)
* 引用: reference:/visuals/left_outer_knuckle @/visuals/left_outer_knuckle
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.024, 0.155, 0.111), center=(12.912, 28.904, 0.242)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_7/gripper/left_outer_knuckle/collisions' (Xform)
* 引用: reference:/colliders/left_outer_knuckle @/colliders/left_outer_knuckle
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(12.912, 28.930, 0.283)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_7/gripper/left_finger/visuals' (Xform)
* 引用: reference:/visuals/left_finger @/visuals/left_finger
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.064, 0.064, 0.134), center=(12.912, 28.879, 0.144)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_7/gripper/left_finger/collisions' (Xform)
* 引用: reference:/colliders/left_finger @/colliders/left_finger
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(12.912, 28.859, 0.199)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_7/gripper/left_inner_knuckle/visuals' (Xform)
* 引用: reference:/visuals/left_inner_knuckle @/visuals/left_inner_knuckle
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.056, 0.095, 0.108), center=(12.912, 28.925, 0.211)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_7/gripper/left_inner_knuckle/collisions' (Xform)
* 引用: reference:/colliders/left_inner_knuckle @/colliders/left_inner_knuckle
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(12.912, 28.960, 0.253)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_7/gripper/right_inner_knuckle/visuals' (Xform)
* 引用: reference:/visuals/right_inner_knuckle @/visuals/right_inner_knuckle
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.056, 0.095, 0.108), center=(12.912, 29.075, 0.211)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_7/gripper/right_inner_knuckle/collisions' (Xform)
* 引用: reference:/colliders/right_inner_knuckle @/colliders/right_inner_knuckle
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(12.912, 29.040, 0.253)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_7/gripper/right_outer_knuckle/visuals' (Xform)
* 引用: reference:/visuals/right_outer_knuckle @/visuals/right_outer_knuckle
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.024, 0.155, 0.111), center=(12.912, 29.096, 0.242)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_7/gripper/right_outer_knuckle/collisions' (Xform)
* 引用: reference:/colliders/right_outer_knuckle @/colliders/right_outer_knuckle
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(12.912, 29.070, 0.283)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_7/gripper/right_finger/visuals' (Xform)
* 引用: reference:/visuals/right_finger @/visuals/right_finger
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.064, 0.064, 0.134), center=(12.912, 29.121, 0.144)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_7/gripper/right_finger/collisions' (Xform)
* 引用: reference:/colliders/right_finger @/colliders/right_finger
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(12.912, 29.141, 0.199)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_7/world/visuals' (Xform)
* 引用: reference:/visuals/world @/visuals/world
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.252, 0.252, 0.301), center=(12.500, 29.000, 0.310)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_7/world/collisions' (Xform)
* 引用: reference:/colliders/world @/colliders/world
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(12.500, 29.000, 0.160)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_7/link1/visuals' (Xform)
* 引用: reference:/visuals/link1 @/visuals/link1
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.194, 0.232, 0.329), center=(12.500, 29.002, 0.627)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_7/link1/collisions' (Xform)
* 引用: reference:/colliders/link1 @/colliders/link1
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(12.500, 29.000, 0.694)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_7/link2/visuals' (Xform)
* 引用: reference:/visuals/link2 @/visuals/link2
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.194, 0.326, 0.463), center=(12.500, 29.074, 0.828)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_7/link2/collisions' (Xform)
* 引用: reference:/colliders/link2 @/colliders/link2
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(12.500, 29.000, 0.694)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_7/link3/visuals' (Xform)
* 引用: reference:/visuals/link3 @/visuals/link3
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.283, 0.229, 0.309), center=(12.552, 29.023, 1.215)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_7/link3/collisions' (Xform)
* 引用: reference:/colliders/link3 @/colliders/link3
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(12.500, 29.000, 1.280)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_7/link4/visuals' (Xform)
* 引用: reference:/visuals/link4 @/visuals/link4
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.334, 0.308, 0.414), center=(12.683, 28.936, 1.162)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_7/link4/collisions' (Xform)
* 引用: reference:/colliders/link4 @/colliders/link4
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(12.605, 29.000, 1.280)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_7/link5/visuals' (Xform)
* 引用: reference:/visuals/link5 @/visuals/link5
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.180, 0.262, 0.440), center=(12.760, 28.959, 0.738)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_7/link5/collisions' (Xform)
* 引用: reference:/colliders/link5 @/colliders/link5
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(12.760, 29.000, 0.595)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_7/link6/visuals' (Xform)
* 引用: reference:/visuals/link6 @/visuals/link6
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.307, 0.200, 0.212), center=(12.836, 29.022, 0.566)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_7/link6/collisions' (Xform)
* 引用: reference:/colliders/link6 @/colliders/link6
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(12.760, 29.000, 0.595)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_7/link7/visuals' (Xform)
* 引用: reference:/visuals/link7 @/visuals/link7
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.156, 0.186, 0.066), center=(12.912, 29.015, 0.434)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_7/link7/collisions' (Xform)
* 引用: reference:/colliders/link7 @/colliders/link7
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(12.912, 29.000, 0.401)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_8' (Xform)
* 引用: reference:/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/5.0/Isaac/Robots/Ufactory/xarm7/xarm7.usd; payload:./configuration/xarm7_physics.usd
* BBox (world): size=(0.616, 0.455, 1.292), center=(17.682, 29.010, 0.723)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_8/gripper' (Xform)
* 引用: payload:../xarm_gripper/xarm_gripper.usd
* BBox (world): size=(0.150, 0.346, 0.324), center=(17.912, 29.000, 0.239)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_8/gripper/xarm_gripper_base_link/visuals' (Xform)
* 引用: reference:/visuals/xarm_gripper_base_link @/visuals/xarm_gripper_base_link
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.150, 0.213, 0.209), center=(17.912, 29.000, 0.297)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_8/gripper/xarm_gripper_base_link/collisions' (Xform)
* 引用: reference:/colliders/xarm_gripper_base_link @/colliders/xarm_gripper_base_link
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(17.912, 29.000, 0.401)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_8/gripper/left_outer_knuckle/visuals' (Xform)
* 引用: reference:/visuals/left_outer_knuckle @/visuals/left_outer_knuckle
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.024, 0.155, 0.111), center=(17.912, 28.904, 0.242)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_8/gripper/left_outer_knuckle/collisions' (Xform)
* 引用: reference:/colliders/left_outer_knuckle @/colliders/left_outer_knuckle
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(17.912, 28.930, 0.283)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_8/gripper/left_finger/visuals' (Xform)
* 引用: reference:/visuals/left_finger @/visuals/left_finger
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.064, 0.064, 0.134), center=(17.912, 28.879, 0.144)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_8/gripper/left_finger/collisions' (Xform)
* 引用: reference:/colliders/left_finger @/colliders/left_finger
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(17.912, 28.859, 0.199)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_8/gripper/left_inner_knuckle/visuals' (Xform)
* 引用: reference:/visuals/left_inner_knuckle @/visuals/left_inner_knuckle
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.056, 0.095, 0.108), center=(17.912, 28.925, 0.211)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_8/gripper/left_inner_knuckle/collisions' (Xform)
* 引用: reference:/colliders/left_inner_knuckle @/colliders/left_inner_knuckle
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(17.912, 28.960, 0.253)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_8/gripper/right_inner_knuckle/visuals' (Xform)
* 引用: reference:/visuals/right_inner_knuckle @/visuals/right_inner_knuckle
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.056, 0.095, 0.108), center=(17.912, 29.075, 0.211)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_8/gripper/right_inner_knuckle/collisions' (Xform)
* 引用: reference:/colliders/right_inner_knuckle @/colliders/right_inner_knuckle
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(17.912, 29.040, 0.253)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_8/gripper/right_outer_knuckle/visuals' (Xform)
* 引用: reference:/visuals/right_outer_knuckle @/visuals/right_outer_knuckle
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.024, 0.155, 0.111), center=(17.912, 29.096, 0.242)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_8/gripper/right_outer_knuckle/collisions' (Xform)
* 引用: reference:/colliders/right_outer_knuckle @/colliders/right_outer_knuckle
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(17.912, 29.070, 0.283)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_8/gripper/right_finger/visuals' (Xform)
* 引用: reference:/visuals/right_finger @/visuals/right_finger
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.064, 0.064, 0.134), center=(17.912, 29.121, 0.144)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_8/gripper/right_finger/collisions' (Xform)
* 引用: reference:/colliders/right_finger @/colliders/right_finger
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(17.912, 29.141, 0.199)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_8/world/visuals' (Xform)
* 引用: reference:/visuals/world @/visuals/world
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.252, 0.252, 0.301), center=(17.500, 29.000, 0.310)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_8/world/collisions' (Xform)
* 引用: reference:/colliders/world @/colliders/world
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(17.500, 29.000, 0.160)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_8/link1/visuals' (Xform)
* 引用: reference:/visuals/link1 @/visuals/link1
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.194, 0.232, 0.329), center=(17.500, 29.002, 0.627)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_8/link1/collisions' (Xform)
* 引用: reference:/colliders/link1 @/colliders/link1
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(17.500, 29.000, 0.694)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_8/link2/visuals' (Xform)
* 引用: reference:/visuals/link2 @/visuals/link2
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.194, 0.326, 0.463), center=(17.500, 29.074, 0.828)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_8/link2/collisions' (Xform)
* 引用: reference:/colliders/link2 @/colliders/link2
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(17.500, 29.000, 0.694)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_8/link3/visuals' (Xform)
* 引用: reference:/visuals/link3 @/visuals/link3
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.283, 0.229, 0.309), center=(17.552, 29.023, 1.215)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_8/link3/collisions' (Xform)
* 引用: reference:/colliders/link3 @/colliders/link3
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(17.500, 29.000, 1.280)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_8/link4/visuals' (Xform)
* 引用: reference:/visuals/link4 @/visuals/link4
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.334, 0.308, 0.414), center=(17.683, 28.936, 1.162)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_8/link4/collisions' (Xform)
* 引用: reference:/colliders/link4 @/colliders/link4
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(17.605, 29.000, 1.280)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_8/link5/visuals' (Xform)
* 引用: reference:/visuals/link5 @/visuals/link5
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.180, 0.262, 0.440), center=(17.760, 28.959, 0.738)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_8/link5/collisions' (Xform)
* 引用: reference:/colliders/link5 @/colliders/link5
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(17.760, 29.000, 0.595)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_8/link6/visuals' (Xform)
* 引用: reference:/visuals/link6 @/visuals/link6
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.307, 0.200, 0.212), center=(17.836, 29.022, 0.566)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_8/link6/collisions' (Xform)
* 引用: reference:/colliders/link6 @/colliders/link6
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(17.760, 29.000, 0.595)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_8/link7/visuals' (Xform)
* 引用: reference:/visuals/link7 @/visuals/link7
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(0.156, 0.186, 0.066), center=(17.912, 29.015, 0.434)
* 几何统计: Mesh=0, Vertices=0, Faces=0


---


### '/World/RobotArm1_8/link7/collisions' (Xform)
* 引用: reference:/colliders/link7 @/colliders/link7
* 变换: T=(0.000, 0.000, 0.000); R=(0.000, 0.000, 0.000); S=(1.000, 1.000, 1.000)
* BBox (world): size=(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000), center=(17.912, 29.000, 0.401)
* 几何统计: Mesh=0, Vertices=0, Faces=0


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
