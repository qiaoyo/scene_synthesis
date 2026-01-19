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


### /World/RobotArm_1
*  **Prim路径 (Prim Path):**/World/RobotArm_1
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/5.0/Isaac/Robots/Kawasaki/RS007L/rs007l_onrobot_rg2.usd'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.572, 0.478, 2.377)'
   *   Center: '(-19.903, 28.984, 1.349)'


---


### /World/RobotArm_2
*  **Prim路径 (Prim Path):**/World/RobotArm_2
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/5.0/Isaac/Robots/Kawasaki/RS007L/rs007l_onrobot_rg2.usd'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.572, 0.478, 2.377)'
   *   Center: '(-14.903, 28.984, 1.349)'


---


### /World/RobotArm_3
*  **Prim路径 (Prim Path):**/World/RobotArm_3
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/5.0/Isaac/Robots/Kawasaki/RS007L/rs007l_onrobot_rg2.usd'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.572, 0.478, 2.377)'
   *   Center: '(-9.903, 28.984, 1.349)'


---


### /World/RobotArm_4
*  **Prim路径 (Prim Path):**/World/RobotArm_4
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/5.0/Isaac/Robots/Kawasaki/RS007L/rs007l_onrobot_rg2.usd'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.572, 0.478, 2.377)'
   *   Center: '(-4.903, 28.984, 1.349)'


---


### /World/RobotArm_5
*  **Prim路径 (Prim Path):**/World/RobotArm_5
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/5.0/Isaac/Robots/Kawasaki/RS007L/rs007l_onrobot_rg2.usd'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.572, 0.478, 2.377)'
   *   Center: '(0.097, 28.984, 1.349)'


---


### /World/RobotArm_6
*  **Prim路径 (Prim Path):**/World/RobotArm_6
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/5.0/Isaac/Robots/Kawasaki/RS007L/rs007l_onrobot_rg2.usd'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.572, 0.478, 2.377)'
   *   Center: '(5.097, 28.984, 1.349)'


---


### /World/RobotArm_7
*  **Prim路径 (Prim Path):**/World/RobotArm_7
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/5.0/Isaac/Robots/Kawasaki/RS007L/rs007l_onrobot_rg2.usd'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.572, 0.478, 2.377)'
   *   Center: '(10.097, 28.984, 1.349)'


---


### /World/RobotArm_8
*  **Prim路径 (Prim Path):**/World/RobotArm_8
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/5.0/Isaac/Robots/Kawasaki/RS007L/rs007l_onrobot_rg2.usd'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.572, 0.478, 2.377)'
   *   Center: '(15.097, 28.984, 1.349)'


---


### /World/RobotArm1_1
*  **Prim路径 (Prim Path):**/World/RobotArm1_1
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/5.0/Isaac/Robots/Ufactory/xarm7/xarm7.usd'
       *   [reference] './configuration/xarm7_physics.usd'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.616, 0.455, 1.292)'
   *   Center: '(-17.318, 29.010, 0.723)'


---


### /World/RobotArm1_1/gripper
*  **Prim路径 (Prim Path):**/World/RobotArm1_1/gripper
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '../xarm_gripper/xarm_gripper.usd'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.150, 0.346, 0.324)'
   *   Center: '(-17.088, 29.000, 0.239)'


---


### /World/RobotArm1_1/gripper/xarm_gripper_base_link/visuals
*  **Prim路径 (Prim Path):**/World/RobotArm1_1/gripper/xarm_gripper_base_link/visuals
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/visuals/xarm_gripper_base_link'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.150, 0.213, 0.209)'
   *   Center: '(-17.088, 29.000, 0.297)'


---


### /World/RobotArm1_1/gripper/xarm_gripper_base_link/collisions
*  **Prim路径 (Prim Path):**/World/RobotArm1_1/gripper/xarm_gripper_base_link/collisions
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/colliders/xarm_gripper_base_link'
*  **世界包围盒 (World BBox):**
   *   Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
   *   Center: '(-17.088, 29.000, 0.401)'
*  **物理属性 (Physics):**
   *   **Collider:** True


---


### /World/RobotArm1_1/gripper/left_outer_knuckle/visuals
*  **Prim路径 (Prim Path):**/World/RobotArm1_1/gripper/left_outer_knuckle/visuals
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/visuals/left_outer_knuckle'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.024, 0.155, 0.111)'
   *   Center: '(-17.088, 28.904, 0.242)'


---


### /World/RobotArm1_1/gripper/left_outer_knuckle/collisions
*  **Prim路径 (Prim Path):**/World/RobotArm1_1/gripper/left_outer_knuckle/collisions
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/colliders/left_outer_knuckle'
*  **世界包围盒 (World BBox):**
   *   Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
   *   Center: '(-17.088, 28.930, 0.283)'
*  **物理属性 (Physics):**
   *   **Collider:** True


---


### /World/RobotArm1_1/gripper/left_finger/visuals
*  **Prim路径 (Prim Path):**/World/RobotArm1_1/gripper/left_finger/visuals
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/visuals/left_finger'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.064, 0.064, 0.134)'
   *   Center: '(-17.088, 28.879, 0.144)'


---


### /World/RobotArm1_1/gripper/left_finger/collisions
*  **Prim路径 (Prim Path):**/World/RobotArm1_1/gripper/left_finger/collisions
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/colliders/left_finger'
*  **世界包围盒 (World BBox):**
   *   Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
   *   Center: '(-17.088, 28.859, 0.199)'
*  **物理属性 (Physics):**
   *   **Collider:** True


---


### /World/RobotArm1_1/gripper/left_inner_knuckle/visuals
*  **Prim路径 (Prim Path):**/World/RobotArm1_1/gripper/left_inner_knuckle/visuals
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/visuals/left_inner_knuckle'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.056, 0.095, 0.108)'
   *   Center: '(-17.088, 28.925, 0.211)'


---


### /World/RobotArm1_1/gripper/left_inner_knuckle/collisions
*  **Prim路径 (Prim Path):**/World/RobotArm1_1/gripper/left_inner_knuckle/collisions
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/colliders/left_inner_knuckle'
*  **世界包围盒 (World BBox):**
   *   Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
   *   Center: '(-17.088, 28.960, 0.253)'
*  **物理属性 (Physics):**
   *   **Collider:** True


---


### /World/RobotArm1_1/gripper/right_inner_knuckle/visuals
*  **Prim路径 (Prim Path):**/World/RobotArm1_1/gripper/right_inner_knuckle/visuals
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/visuals/right_inner_knuckle'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.056, 0.095, 0.108)'
   *   Center: '(-17.088, 29.075, 0.211)'


---


### /World/RobotArm1_1/gripper/right_inner_knuckle/collisions
*  **Prim路径 (Prim Path):**/World/RobotArm1_1/gripper/right_inner_knuckle/collisions
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/colliders/right_inner_knuckle'
*  **世界包围盒 (World BBox):**
   *   Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
   *   Center: '(-17.088, 29.040, 0.253)'
*  **物理属性 (Physics):**
   *   **Collider:** True


---


### /World/RobotArm1_1/gripper/right_outer_knuckle/visuals
*  **Prim路径 (Prim Path):**/World/RobotArm1_1/gripper/right_outer_knuckle/visuals
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/visuals/right_outer_knuckle'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.024, 0.155, 0.111)'
   *   Center: '(-17.088, 29.096, 0.242)'


---


### /World/RobotArm1_1/gripper/right_outer_knuckle/collisions
*  **Prim路径 (Prim Path):**/World/RobotArm1_1/gripper/right_outer_knuckle/collisions
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/colliders/right_outer_knuckle'
*  **世界包围盒 (World BBox):**
   *   Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
   *   Center: '(-17.088, 29.070, 0.283)'
*  **物理属性 (Physics):**
   *   **Collider:** True


---


### /World/RobotArm1_1/gripper/right_finger/visuals
*  **Prim路径 (Prim Path):**/World/RobotArm1_1/gripper/right_finger/visuals
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/visuals/right_finger'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.064, 0.064, 0.134)'
   *   Center: '(-17.088, 29.121, 0.144)'


---


### /World/RobotArm1_1/gripper/right_finger/collisions
*  **Prim路径 (Prim Path):**/World/RobotArm1_1/gripper/right_finger/collisions
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/colliders/right_finger'
*  **世界包围盒 (World BBox):**
   *   Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
   *   Center: '(-17.088, 29.141, 0.199)'
*  **物理属性 (Physics):**
   *   **Collider:** True


---


### /World/RobotArm1_1/world/visuals
*  **Prim路径 (Prim Path):**/World/RobotArm1_1/world/visuals
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/visuals/world'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.252, 0.252, 0.301)'
   *   Center: '(-17.500, 29.000, 0.310)'


---


### /World/RobotArm1_1/world/collisions
*  **Prim路径 (Prim Path):**/World/RobotArm1_1/world/collisions
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/colliders/world'
*  **世界包围盒 (World BBox):**
   *   Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
   *   Center: '(-17.500, 29.000, 0.160)'
*  **物理属性 (Physics):**
   *   **Collider:** True


---


### /World/RobotArm1_1/link1/visuals
*  **Prim路径 (Prim Path):**/World/RobotArm1_1/link1/visuals
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/visuals/link1'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.194, 0.232, 0.329)'
   *   Center: '(-17.500, 29.002, 0.627)'


---


### /World/RobotArm1_1/link1/collisions
*  **Prim路径 (Prim Path):**/World/RobotArm1_1/link1/collisions
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/colliders/link1'
*  **世界包围盒 (World BBox):**
   *   Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
   *   Center: '(-17.500, 29.000, 0.694)'
*  **物理属性 (Physics):**
   *   **Collider:** True


---


### /World/RobotArm1_1/link2/visuals
*  **Prim路径 (Prim Path):**/World/RobotArm1_1/link2/visuals
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/visuals/link2'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.194, 0.326, 0.463)'
   *   Center: '(-17.500, 29.074, 0.828)'


---


### /World/RobotArm1_1/link2/collisions
*  **Prim路径 (Prim Path):**/World/RobotArm1_1/link2/collisions
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/colliders/link2'
*  **世界包围盒 (World BBox):**
   *   Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
   *   Center: '(-17.500, 29.000, 0.694)'
*  **物理属性 (Physics):**
   *   **Collider:** True


---


### /World/RobotArm1_1/link3/visuals
*  **Prim路径 (Prim Path):**/World/RobotArm1_1/link3/visuals
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/visuals/link3'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.283, 0.229, 0.309)'
   *   Center: '(-17.448, 29.023, 1.215)'


---


### /World/RobotArm1_1/link3/collisions
*  **Prim路径 (Prim Path):**/World/RobotArm1_1/link3/collisions
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/colliders/link3'
*  **世界包围盒 (World BBox):**
   *   Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
   *   Center: '(-17.500, 29.000, 1.280)'
*  **物理属性 (Physics):**
   *   **Collider:** True


---


### /World/RobotArm1_1/link4/visuals
*  **Prim路径 (Prim Path):**/World/RobotArm1_1/link4/visuals
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/visuals/link4'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.334, 0.308, 0.414)'
   *   Center: '(-17.317, 28.936, 1.162)'


---


### /World/RobotArm1_1/link4/collisions
*  **Prim路径 (Prim Path):**/World/RobotArm1_1/link4/collisions
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/colliders/link4'
*  **世界包围盒 (World BBox):**
   *   Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
   *   Center: '(-17.395, 29.000, 1.280)'
*  **物理属性 (Physics):**
   *   **Collider:** True


---


### /World/RobotArm1_1/link5/visuals
*  **Prim路径 (Prim Path):**/World/RobotArm1_1/link5/visuals
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/visuals/link5'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.180, 0.262, 0.440)'
   *   Center: '(-17.240, 28.959, 0.738)'


---


### /World/RobotArm1_1/link5/collisions
*  **Prim路径 (Prim Path):**/World/RobotArm1_1/link5/collisions
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/colliders/link5'
*  **世界包围盒 (World BBox):**
   *   Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
   *   Center: '(-17.240, 29.000, 0.595)'
*  **物理属性 (Physics):**
   *   **Collider:** True


---


### /World/RobotArm1_1/link6/visuals
*  **Prim路径 (Prim Path):**/World/RobotArm1_1/link6/visuals
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/visuals/link6'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.307, 0.200, 0.212)'
   *   Center: '(-17.164, 29.022, 0.566)'


---


### /World/RobotArm1_1/link6/collisions
*  **Prim路径 (Prim Path):**/World/RobotArm1_1/link6/collisions
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/colliders/link6'
*  **世界包围盒 (World BBox):**
   *   Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
   *   Center: '(-17.240, 29.000, 0.595)'
*  **物理属性 (Physics):**
   *   **Collider:** True


---


### /World/RobotArm1_1/link7/visuals
*  **Prim路径 (Prim Path):**/World/RobotArm1_1/link7/visuals
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/visuals/link7'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.156, 0.186, 0.066)'
   *   Center: '(-17.088, 29.015, 0.434)'


---


### /World/RobotArm1_1/link7/collisions
*  **Prim路径 (Prim Path):**/World/RobotArm1_1/link7/collisions
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/colliders/link7'
*  **世界包围盒 (World BBox):**
   *   Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
   *   Center: '(-17.088, 29.000, 0.401)'
*  **物理属性 (Physics):**
   *   **Collider:** True


---


### /World/RobotArm1_2
*  **Prim路径 (Prim Path):**/World/RobotArm1_2
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/5.0/Isaac/Robots/Ufactory/xarm7/xarm7.usd'
       *   [reference] './configuration/xarm7_physics.usd'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.616, 0.455, 1.292)'
   *   Center: '(-12.318, 29.010, 0.723)'


---


### /World/RobotArm1_2/gripper
*  **Prim路径 (Prim Path):**/World/RobotArm1_2/gripper
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '../xarm_gripper/xarm_gripper.usd'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.150, 0.346, 0.324)'
   *   Center: '(-12.088, 29.000, 0.239)'


---


### /World/RobotArm1_2/gripper/xarm_gripper_base_link/visuals
*  **Prim路径 (Prim Path):**/World/RobotArm1_2/gripper/xarm_gripper_base_link/visuals
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/visuals/xarm_gripper_base_link'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.150, 0.213, 0.209)'
   *   Center: '(-12.088, 29.000, 0.297)'


---


### /World/RobotArm1_2/gripper/xarm_gripper_base_link/collisions
*  **Prim路径 (Prim Path):**/World/RobotArm1_2/gripper/xarm_gripper_base_link/collisions
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/colliders/xarm_gripper_base_link'
*  **世界包围盒 (World BBox):**
   *   Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
   *   Center: '(-12.088, 29.000, 0.401)'
*  **物理属性 (Physics):**
   *   **Collider:** True


---


### /World/RobotArm1_2/gripper/left_outer_knuckle/visuals
*  **Prim路径 (Prim Path):**/World/RobotArm1_2/gripper/left_outer_knuckle/visuals
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/visuals/left_outer_knuckle'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.024, 0.155, 0.111)'
   *   Center: '(-12.088, 28.904, 0.242)'


---


### /World/RobotArm1_2/gripper/left_outer_knuckle/collisions
*  **Prim路径 (Prim Path):**/World/RobotArm1_2/gripper/left_outer_knuckle/collisions
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/colliders/left_outer_knuckle'
*  **世界包围盒 (World BBox):**
   *   Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
   *   Center: '(-12.088, 28.930, 0.283)'
*  **物理属性 (Physics):**
   *   **Collider:** True


---


### /World/RobotArm1_2/gripper/left_finger/visuals
*  **Prim路径 (Prim Path):**/World/RobotArm1_2/gripper/left_finger/visuals
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/visuals/left_finger'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.064, 0.064, 0.134)'
   *   Center: '(-12.088, 28.879, 0.144)'


---


### /World/RobotArm1_2/gripper/left_finger/collisions
*  **Prim路径 (Prim Path):**/World/RobotArm1_2/gripper/left_finger/collisions
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/colliders/left_finger'
*  **世界包围盒 (World BBox):**
   *   Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
   *   Center: '(-12.088, 28.859, 0.199)'
*  **物理属性 (Physics):**
   *   **Collider:** True


---


### /World/RobotArm1_2/gripper/left_inner_knuckle/visuals
*  **Prim路径 (Prim Path):**/World/RobotArm1_2/gripper/left_inner_knuckle/visuals
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/visuals/left_inner_knuckle'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.056, 0.095, 0.108)'
   *   Center: '(-12.088, 28.925, 0.211)'


---


### /World/RobotArm1_2/gripper/left_inner_knuckle/collisions
*  **Prim路径 (Prim Path):**/World/RobotArm1_2/gripper/left_inner_knuckle/collisions
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/colliders/left_inner_knuckle'
*  **世界包围盒 (World BBox):**
   *   Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
   *   Center: '(-12.088, 28.960, 0.253)'
*  **物理属性 (Physics):**
   *   **Collider:** True


---


### /World/RobotArm1_2/gripper/right_inner_knuckle/visuals
*  **Prim路径 (Prim Path):**/World/RobotArm1_2/gripper/right_inner_knuckle/visuals
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/visuals/right_inner_knuckle'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.056, 0.095, 0.108)'
   *   Center: '(-12.088, 29.075, 0.211)'


---


### /World/RobotArm1_2/gripper/right_inner_knuckle/collisions
*  **Prim路径 (Prim Path):**/World/RobotArm1_2/gripper/right_inner_knuckle/collisions
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/colliders/right_inner_knuckle'
*  **世界包围盒 (World BBox):**
   *   Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
   *   Center: '(-12.088, 29.040, 0.253)'
*  **物理属性 (Physics):**
   *   **Collider:** True


---


### /World/RobotArm1_2/gripper/right_outer_knuckle/visuals
*  **Prim路径 (Prim Path):**/World/RobotArm1_2/gripper/right_outer_knuckle/visuals
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/visuals/right_outer_knuckle'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.024, 0.155, 0.111)'
   *   Center: '(-12.088, 29.096, 0.242)'


---


### /World/RobotArm1_2/gripper/right_outer_knuckle/collisions
*  **Prim路径 (Prim Path):**/World/RobotArm1_2/gripper/right_outer_knuckle/collisions
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/colliders/right_outer_knuckle'
*  **世界包围盒 (World BBox):**
   *   Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
   *   Center: '(-12.088, 29.070, 0.283)'
*  **物理属性 (Physics):**
   *   **Collider:** True


---


### /World/RobotArm1_2/gripper/right_finger/visuals
*  **Prim路径 (Prim Path):**/World/RobotArm1_2/gripper/right_finger/visuals
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/visuals/right_finger'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.064, 0.064, 0.134)'
   *   Center: '(-12.088, 29.121, 0.144)'


---


### /World/RobotArm1_2/gripper/right_finger/collisions
*  **Prim路径 (Prim Path):**/World/RobotArm1_2/gripper/right_finger/collisions
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/colliders/right_finger'
*  **世界包围盒 (World BBox):**
   *   Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
   *   Center: '(-12.088, 29.141, 0.199)'
*  **物理属性 (Physics):**
   *   **Collider:** True


---


### /World/RobotArm1_2/world/visuals
*  **Prim路径 (Prim Path):**/World/RobotArm1_2/world/visuals
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/visuals/world'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.252, 0.252, 0.301)'
   *   Center: '(-12.500, 29.000, 0.310)'


---


### /World/RobotArm1_2/world/collisions
*  **Prim路径 (Prim Path):**/World/RobotArm1_2/world/collisions
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/colliders/world'
*  **世界包围盒 (World BBox):**
   *   Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
   *   Center: '(-12.500, 29.000, 0.160)'
*  **物理属性 (Physics):**
   *   **Collider:** True


---


### /World/RobotArm1_2/link1/visuals
*  **Prim路径 (Prim Path):**/World/RobotArm1_2/link1/visuals
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/visuals/link1'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.194, 0.232, 0.329)'
   *   Center: '(-12.500, 29.002, 0.627)'


---


### /World/RobotArm1_2/link1/collisions
*  **Prim路径 (Prim Path):**/World/RobotArm1_2/link1/collisions
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/colliders/link1'
*  **世界包围盒 (World BBox):**
   *   Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
   *   Center: '(-12.500, 29.000, 0.694)'
*  **物理属性 (Physics):**
   *   **Collider:** True


---


### /World/RobotArm1_2/link2/visuals
*  **Prim路径 (Prim Path):**/World/RobotArm1_2/link2/visuals
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/visuals/link2'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.194, 0.326, 0.463)'
   *   Center: '(-12.500, 29.074, 0.828)'


---


### /World/RobotArm1_2/link2/collisions
*  **Prim路径 (Prim Path):**/World/RobotArm1_2/link2/collisions
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/colliders/link2'
*  **世界包围盒 (World BBox):**
   *   Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
   *   Center: '(-12.500, 29.000, 0.694)'
*  **物理属性 (Physics):**
   *   **Collider:** True


---


### /World/RobotArm1_2/link3/visuals
*  **Prim路径 (Prim Path):**/World/RobotArm1_2/link3/visuals
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/visuals/link3'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.283, 0.229, 0.309)'
   *   Center: '(-12.448, 29.023, 1.215)'


---


### /World/RobotArm1_2/link3/collisions
*  **Prim路径 (Prim Path):**/World/RobotArm1_2/link3/collisions
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/colliders/link3'
*  **世界包围盒 (World BBox):**
   *   Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
   *   Center: '(-12.500, 29.000, 1.280)'
*  **物理属性 (Physics):**
   *   **Collider:** True


---


### /World/RobotArm1_2/link4/visuals
*  **Prim路径 (Prim Path):**/World/RobotArm1_2/link4/visuals
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/visuals/link4'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.334, 0.308, 0.414)'
   *   Center: '(-12.317, 28.936, 1.162)'


---


### /World/RobotArm1_2/link4/collisions
*  **Prim路径 (Prim Path):**/World/RobotArm1_2/link4/collisions
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/colliders/link4'
*  **世界包围盒 (World BBox):**
   *   Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
   *   Center: '(-12.395, 29.000, 1.280)'
*  **物理属性 (Physics):**
   *   **Collider:** True


---


### /World/RobotArm1_2/link5/visuals
*  **Prim路径 (Prim Path):**/World/RobotArm1_2/link5/visuals
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/visuals/link5'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.180, 0.262, 0.440)'
   *   Center: '(-12.240, 28.959, 0.738)'


---


### /World/RobotArm1_2/link5/collisions
*  **Prim路径 (Prim Path):**/World/RobotArm1_2/link5/collisions
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/colliders/link5'
*  **世界包围盒 (World BBox):**
   *   Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
   *   Center: '(-12.240, 29.000, 0.595)'
*  **物理属性 (Physics):**
   *   **Collider:** True


---


### /World/RobotArm1_2/link6/visuals
*  **Prim路径 (Prim Path):**/World/RobotArm1_2/link6/visuals
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/visuals/link6'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.307, 0.200, 0.212)'
   *   Center: '(-12.164, 29.022, 0.566)'


---


### /World/RobotArm1_2/link6/collisions
*  **Prim路径 (Prim Path):**/World/RobotArm1_2/link6/collisions
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/colliders/link6'
*  **世界包围盒 (World BBox):**
   *   Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
   *   Center: '(-12.240, 29.000, 0.595)'
*  **物理属性 (Physics):**
   *   **Collider:** True


---


### /World/RobotArm1_2/link7/visuals
*  **Prim路径 (Prim Path):**/World/RobotArm1_2/link7/visuals
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/visuals/link7'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.156, 0.186, 0.066)'
   *   Center: '(-12.088, 29.015, 0.434)'


---


### /World/RobotArm1_2/link7/collisions
*  **Prim路径 (Prim Path):**/World/RobotArm1_2/link7/collisions
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/colliders/link7'
*  **世界包围盒 (World BBox):**
   *   Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
   *   Center: '(-12.088, 29.000, 0.401)'
*  **物理属性 (Physics):**
   *   **Collider:** True


---


### /World/RobotArm1_3
*  **Prim路径 (Prim Path):**/World/RobotArm1_3
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/5.0/Isaac/Robots/Ufactory/xarm7/xarm7.usd'
       *   [reference] './configuration/xarm7_physics.usd'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.616, 0.455, 1.292)'
   *   Center: '(-7.318, 29.010, 0.723)'


---


### /World/RobotArm1_3/gripper
*  **Prim路径 (Prim Path):**/World/RobotArm1_3/gripper
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '../xarm_gripper/xarm_gripper.usd'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.150, 0.346, 0.324)'
   *   Center: '(-7.088, 29.000, 0.239)'


---


### /World/RobotArm1_3/gripper/xarm_gripper_base_link/visuals
*  **Prim路径 (Prim Path):**/World/RobotArm1_3/gripper/xarm_gripper_base_link/visuals
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/visuals/xarm_gripper_base_link'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.150, 0.213, 0.209)'
   *   Center: '(-7.088, 29.000, 0.297)'


---


### /World/RobotArm1_3/gripper/xarm_gripper_base_link/collisions
*  **Prim路径 (Prim Path):**/World/RobotArm1_3/gripper/xarm_gripper_base_link/collisions
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/colliders/xarm_gripper_base_link'
*  **世界包围盒 (World BBox):**
   *   Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
   *   Center: '(-7.088, 29.000, 0.401)'
*  **物理属性 (Physics):**
   *   **Collider:** True


---


### /World/RobotArm1_3/gripper/left_outer_knuckle/visuals
*  **Prim路径 (Prim Path):**/World/RobotArm1_3/gripper/left_outer_knuckle/visuals
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/visuals/left_outer_knuckle'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.024, 0.155, 0.111)'
   *   Center: '(-7.088, 28.904, 0.242)'


---


### /World/RobotArm1_3/gripper/left_outer_knuckle/collisions
*  **Prim路径 (Prim Path):**/World/RobotArm1_3/gripper/left_outer_knuckle/collisions
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/colliders/left_outer_knuckle'
*  **世界包围盒 (World BBox):**
   *   Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
   *   Center: '(-7.088, 28.930, 0.283)'
*  **物理属性 (Physics):**
   *   **Collider:** True


---


### /World/RobotArm1_3/gripper/left_finger/visuals
*  **Prim路径 (Prim Path):**/World/RobotArm1_3/gripper/left_finger/visuals
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/visuals/left_finger'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.064, 0.064, 0.134)'
   *   Center: '(-7.088, 28.879, 0.144)'


---


### /World/RobotArm1_3/gripper/left_finger/collisions
*  **Prim路径 (Prim Path):**/World/RobotArm1_3/gripper/left_finger/collisions
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/colliders/left_finger'
*  **世界包围盒 (World BBox):**
   *   Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
   *   Center: '(-7.088, 28.859, 0.199)'
*  **物理属性 (Physics):**
   *   **Collider:** True


---


### /World/RobotArm1_3/gripper/left_inner_knuckle/visuals
*  **Prim路径 (Prim Path):**/World/RobotArm1_3/gripper/left_inner_knuckle/visuals
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/visuals/left_inner_knuckle'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.056, 0.095, 0.108)'
   *   Center: '(-7.088, 28.925, 0.211)'


---


### /World/RobotArm1_3/gripper/left_inner_knuckle/collisions
*  **Prim路径 (Prim Path):**/World/RobotArm1_3/gripper/left_inner_knuckle/collisions
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/colliders/left_inner_knuckle'
*  **世界包围盒 (World BBox):**
   *   Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
   *   Center: '(-7.088, 28.960, 0.253)'
*  **物理属性 (Physics):**
   *   **Collider:** True


---


### /World/RobotArm1_3/gripper/right_inner_knuckle/visuals
*  **Prim路径 (Prim Path):**/World/RobotArm1_3/gripper/right_inner_knuckle/visuals
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/visuals/right_inner_knuckle'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.056, 0.095, 0.108)'
   *   Center: '(-7.088, 29.075, 0.211)'


---


### /World/RobotArm1_3/gripper/right_inner_knuckle/collisions
*  **Prim路径 (Prim Path):**/World/RobotArm1_3/gripper/right_inner_knuckle/collisions
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/colliders/right_inner_knuckle'
*  **世界包围盒 (World BBox):**
   *   Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
   *   Center: '(-7.088, 29.040, 0.253)'
*  **物理属性 (Physics):**
   *   **Collider:** True


---


### /World/RobotArm1_3/gripper/right_outer_knuckle/visuals
*  **Prim路径 (Prim Path):**/World/RobotArm1_3/gripper/right_outer_knuckle/visuals
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/visuals/right_outer_knuckle'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.024, 0.155, 0.111)'
   *   Center: '(-7.088, 29.096, 0.242)'


---


### /World/RobotArm1_3/gripper/right_outer_knuckle/collisions
*  **Prim路径 (Prim Path):**/World/RobotArm1_3/gripper/right_outer_knuckle/collisions
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/colliders/right_outer_knuckle'
*  **世界包围盒 (World BBox):**
   *   Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
   *   Center: '(-7.088, 29.070, 0.283)'
*  **物理属性 (Physics):**
   *   **Collider:** True


---


### /World/RobotArm1_3/gripper/right_finger/visuals
*  **Prim路径 (Prim Path):**/World/RobotArm1_3/gripper/right_finger/visuals
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/visuals/right_finger'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.064, 0.064, 0.134)'
   *   Center: '(-7.088, 29.121, 0.144)'


---


### /World/RobotArm1_3/gripper/right_finger/collisions
*  **Prim路径 (Prim Path):**/World/RobotArm1_3/gripper/right_finger/collisions
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/colliders/right_finger'
*  **世界包围盒 (World BBox):**
   *   Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
   *   Center: '(-7.088, 29.141, 0.199)'
*  **物理属性 (Physics):**
   *   **Collider:** True


---


### /World/RobotArm1_3/world/visuals
*  **Prim路径 (Prim Path):**/World/RobotArm1_3/world/visuals
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/visuals/world'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.252, 0.252, 0.301)'
   *   Center: '(-7.500, 29.000, 0.310)'


---


### /World/RobotArm1_3/world/collisions
*  **Prim路径 (Prim Path):**/World/RobotArm1_3/world/collisions
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/colliders/world'
*  **世界包围盒 (World BBox):**
   *   Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
   *   Center: '(-7.500, 29.000, 0.160)'
*  **物理属性 (Physics):**
   *   **Collider:** True


---


### /World/RobotArm1_3/link1/visuals
*  **Prim路径 (Prim Path):**/World/RobotArm1_3/link1/visuals
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/visuals/link1'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.194, 0.232, 0.329)'
   *   Center: '(-7.500, 29.002, 0.627)'


---


### /World/RobotArm1_3/link1/collisions
*  **Prim路径 (Prim Path):**/World/RobotArm1_3/link1/collisions
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/colliders/link1'
*  **世界包围盒 (World BBox):**
   *   Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
   *   Center: '(-7.500, 29.000, 0.694)'
*  **物理属性 (Physics):**
   *   **Collider:** True


---


### /World/RobotArm1_3/link2/visuals
*  **Prim路径 (Prim Path):**/World/RobotArm1_3/link2/visuals
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/visuals/link2'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.194, 0.326, 0.463)'
   *   Center: '(-7.500, 29.074, 0.828)'


---


### /World/RobotArm1_3/link2/collisions
*  **Prim路径 (Prim Path):**/World/RobotArm1_3/link2/collisions
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/colliders/link2'
*  **世界包围盒 (World BBox):**
   *   Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
   *   Center: '(-7.500, 29.000, 0.694)'
*  **物理属性 (Physics):**
   *   **Collider:** True


---


### /World/RobotArm1_3/link3/visuals
*  **Prim路径 (Prim Path):**/World/RobotArm1_3/link3/visuals
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/visuals/link3'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.283, 0.229, 0.309)'
   *   Center: '(-7.448, 29.023, 1.215)'


---


### /World/RobotArm1_3/link3/collisions
*  **Prim路径 (Prim Path):**/World/RobotArm1_3/link3/collisions
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/colliders/link3'
*  **世界包围盒 (World BBox):**
   *   Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
   *   Center: '(-7.500, 29.000, 1.280)'
*  **物理属性 (Physics):**
   *   **Collider:** True


---


### /World/RobotArm1_3/link4/visuals
*  **Prim路径 (Prim Path):**/World/RobotArm1_3/link4/visuals
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/visuals/link4'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.334, 0.308, 0.414)'
   *   Center: '(-7.317, 28.936, 1.162)'


---


### /World/RobotArm1_3/link4/collisions
*  **Prim路径 (Prim Path):**/World/RobotArm1_3/link4/collisions
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/colliders/link4'
*  **世界包围盒 (World BBox):**
   *   Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
   *   Center: '(-7.395, 29.000, 1.280)'
*  **物理属性 (Physics):**
   *   **Collider:** True


---


### /World/RobotArm1_3/link5/visuals
*  **Prim路径 (Prim Path):**/World/RobotArm1_3/link5/visuals
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/visuals/link5'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.180, 0.262, 0.440)'
   *   Center: '(-7.240, 28.959, 0.738)'


---


### /World/RobotArm1_3/link5/collisions
*  **Prim路径 (Prim Path):**/World/RobotArm1_3/link5/collisions
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/colliders/link5'
*  **世界包围盒 (World BBox):**
   *   Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
   *   Center: '(-7.240, 29.000, 0.595)'
*  **物理属性 (Physics):**
   *   **Collider:** True


---


### /World/RobotArm1_3/link6/visuals
*  **Prim路径 (Prim Path):**/World/RobotArm1_3/link6/visuals
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/visuals/link6'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.307, 0.200, 0.212)'
   *   Center: '(-7.164, 29.022, 0.566)'


---


### /World/RobotArm1_3/link6/collisions
*  **Prim路径 (Prim Path):**/World/RobotArm1_3/link6/collisions
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/colliders/link6'
*  **世界包围盒 (World BBox):**
   *   Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
   *   Center: '(-7.240, 29.000, 0.595)'
*  **物理属性 (Physics):**
   *   **Collider:** True


---


### /World/RobotArm1_3/link7/visuals
*  **Prim路径 (Prim Path):**/World/RobotArm1_3/link7/visuals
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/visuals/link7'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.156, 0.186, 0.066)'
   *   Center: '(-7.088, 29.015, 0.434)'


---


### /World/RobotArm1_3/link7/collisions
*  **Prim路径 (Prim Path):**/World/RobotArm1_3/link7/collisions
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/colliders/link7'
*  **世界包围盒 (World BBox):**
   *   Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
   *   Center: '(-7.088, 29.000, 0.401)'
*  **物理属性 (Physics):**
   *   **Collider:** True


---


### /World/RobotArm1_4
*  **Prim路径 (Prim Path):**/World/RobotArm1_4
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/5.0/Isaac/Robots/Ufactory/xarm7/xarm7.usd'
       *   [reference] './configuration/xarm7_physics.usd'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.616, 0.455, 1.292)'
   *   Center: '(-2.318, 29.010, 0.723)'


---


### /World/RobotArm1_4/gripper
*  **Prim路径 (Prim Path):**/World/RobotArm1_4/gripper
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '../xarm_gripper/xarm_gripper.usd'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.150, 0.346, 0.324)'
   *   Center: '(-2.088, 29.000, 0.239)'


---


### /World/RobotArm1_4/gripper/xarm_gripper_base_link/visuals
*  **Prim路径 (Prim Path):**/World/RobotArm1_4/gripper/xarm_gripper_base_link/visuals
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/visuals/xarm_gripper_base_link'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.150, 0.213, 0.209)'
   *   Center: '(-2.088, 29.000, 0.297)'


---


### /World/RobotArm1_4/gripper/xarm_gripper_base_link/collisions
*  **Prim路径 (Prim Path):**/World/RobotArm1_4/gripper/xarm_gripper_base_link/collisions
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/colliders/xarm_gripper_base_link'
*  **世界包围盒 (World BBox):**
   *   Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
   *   Center: '(-2.088, 29.000, 0.401)'
*  **物理属性 (Physics):**
   *   **Collider:** True


---


### /World/RobotArm1_4/gripper/left_outer_knuckle/visuals
*  **Prim路径 (Prim Path):**/World/RobotArm1_4/gripper/left_outer_knuckle/visuals
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/visuals/left_outer_knuckle'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.024, 0.155, 0.111)'
   *   Center: '(-2.088, 28.904, 0.242)'


---


### /World/RobotArm1_4/gripper/left_outer_knuckle/collisions
*  **Prim路径 (Prim Path):**/World/RobotArm1_4/gripper/left_outer_knuckle/collisions
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/colliders/left_outer_knuckle'
*  **世界包围盒 (World BBox):**
   *   Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
   *   Center: '(-2.088, 28.930, 0.283)'
*  **物理属性 (Physics):**
   *   **Collider:** True


---


### /World/RobotArm1_4/gripper/left_finger/visuals
*  **Prim路径 (Prim Path):**/World/RobotArm1_4/gripper/left_finger/visuals
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/visuals/left_finger'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.064, 0.064, 0.134)'
   *   Center: '(-2.088, 28.879, 0.144)'


---


### /World/RobotArm1_4/gripper/left_finger/collisions
*  **Prim路径 (Prim Path):**/World/RobotArm1_4/gripper/left_finger/collisions
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/colliders/left_finger'
*  **世界包围盒 (World BBox):**
   *   Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
   *   Center: '(-2.088, 28.859, 0.199)'
*  **物理属性 (Physics):**
   *   **Collider:** True


---


### /World/RobotArm1_4/gripper/left_inner_knuckle/visuals
*  **Prim路径 (Prim Path):**/World/RobotArm1_4/gripper/left_inner_knuckle/visuals
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/visuals/left_inner_knuckle'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.056, 0.095, 0.108)'
   *   Center: '(-2.088, 28.925, 0.211)'


---


### /World/RobotArm1_4/gripper/left_inner_knuckle/collisions
*  **Prim路径 (Prim Path):**/World/RobotArm1_4/gripper/left_inner_knuckle/collisions
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/colliders/left_inner_knuckle'
*  **世界包围盒 (World BBox):**
   *   Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
   *   Center: '(-2.088, 28.960, 0.253)'
*  **物理属性 (Physics):**
   *   **Collider:** True


---


### /World/RobotArm1_4/gripper/right_inner_knuckle/visuals
*  **Prim路径 (Prim Path):**/World/RobotArm1_4/gripper/right_inner_knuckle/visuals
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/visuals/right_inner_knuckle'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.056, 0.095, 0.108)'
   *   Center: '(-2.088, 29.075, 0.211)'


---


### /World/RobotArm1_4/gripper/right_inner_knuckle/collisions
*  **Prim路径 (Prim Path):**/World/RobotArm1_4/gripper/right_inner_knuckle/collisions
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/colliders/right_inner_knuckle'
*  **世界包围盒 (World BBox):**
   *   Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
   *   Center: '(-2.088, 29.040, 0.253)'
*  **物理属性 (Physics):**
   *   **Collider:** True


---


### /World/RobotArm1_4/gripper/right_outer_knuckle/visuals
*  **Prim路径 (Prim Path):**/World/RobotArm1_4/gripper/right_outer_knuckle/visuals
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/visuals/right_outer_knuckle'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.024, 0.155, 0.111)'
   *   Center: '(-2.088, 29.096, 0.242)'


---


### /World/RobotArm1_4/gripper/right_outer_knuckle/collisions
*  **Prim路径 (Prim Path):**/World/RobotArm1_4/gripper/right_outer_knuckle/collisions
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/colliders/right_outer_knuckle'
*  **世界包围盒 (World BBox):**
   *   Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
   *   Center: '(-2.088, 29.070, 0.283)'
*  **物理属性 (Physics):**
   *   **Collider:** True


---


### /World/RobotArm1_4/gripper/right_finger/visuals
*  **Prim路径 (Prim Path):**/World/RobotArm1_4/gripper/right_finger/visuals
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/visuals/right_finger'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.064, 0.064, 0.134)'
   *   Center: '(-2.088, 29.121, 0.144)'


---


### /World/RobotArm1_4/gripper/right_finger/collisions
*  **Prim路径 (Prim Path):**/World/RobotArm1_4/gripper/right_finger/collisions
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/colliders/right_finger'
*  **世界包围盒 (World BBox):**
   *   Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
   *   Center: '(-2.088, 29.141, 0.199)'
*  **物理属性 (Physics):**
   *   **Collider:** True


---


### /World/RobotArm1_4/world/visuals
*  **Prim路径 (Prim Path):**/World/RobotArm1_4/world/visuals
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/visuals/world'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.252, 0.252, 0.301)'
   *   Center: '(-2.500, 29.000, 0.310)'


---


### /World/RobotArm1_4/world/collisions
*  **Prim路径 (Prim Path):**/World/RobotArm1_4/world/collisions
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/colliders/world'
*  **世界包围盒 (World BBox):**
   *   Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
   *   Center: '(-2.500, 29.000, 0.160)'
*  **物理属性 (Physics):**
   *   **Collider:** True


---


### /World/RobotArm1_4/link1/visuals
*  **Prim路径 (Prim Path):**/World/RobotArm1_4/link1/visuals
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/visuals/link1'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.194, 0.232, 0.329)'
   *   Center: '(-2.500, 29.002, 0.627)'


---


### /World/RobotArm1_4/link1/collisions
*  **Prim路径 (Prim Path):**/World/RobotArm1_4/link1/collisions
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/colliders/link1'
*  **世界包围盒 (World BBox):**
   *   Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
   *   Center: '(-2.500, 29.000, 0.694)'
*  **物理属性 (Physics):**
   *   **Collider:** True


---


### /World/RobotArm1_4/link2/visuals
*  **Prim路径 (Prim Path):**/World/RobotArm1_4/link2/visuals
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/visuals/link2'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.194, 0.326, 0.463)'
   *   Center: '(-2.500, 29.074, 0.828)'


---


### /World/RobotArm1_4/link2/collisions
*  **Prim路径 (Prim Path):**/World/RobotArm1_4/link2/collisions
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/colliders/link2'
*  **世界包围盒 (World BBox):**
   *   Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
   *   Center: '(-2.500, 29.000, 0.694)'
*  **物理属性 (Physics):**
   *   **Collider:** True


---


### /World/RobotArm1_4/link3/visuals
*  **Prim路径 (Prim Path):**/World/RobotArm1_4/link3/visuals
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/visuals/link3'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.283, 0.229, 0.309)'
   *   Center: '(-2.448, 29.023, 1.215)'


---


### /World/RobotArm1_4/link3/collisions
*  **Prim路径 (Prim Path):**/World/RobotArm1_4/link3/collisions
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/colliders/link3'
*  **世界包围盒 (World BBox):**
   *   Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
   *   Center: '(-2.500, 29.000, 1.280)'
*  **物理属性 (Physics):**
   *   **Collider:** True


---


### /World/RobotArm1_4/link4/visuals
*  **Prim路径 (Prim Path):**/World/RobotArm1_4/link4/visuals
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/visuals/link4'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.334, 0.308, 0.414)'
   *   Center: '(-2.317, 28.936, 1.162)'


---


### /World/RobotArm1_4/link4/collisions
*  **Prim路径 (Prim Path):**/World/RobotArm1_4/link4/collisions
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/colliders/link4'
*  **世界包围盒 (World BBox):**
   *   Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
   *   Center: '(-2.395, 29.000, 1.280)'
*  **物理属性 (Physics):**
   *   **Collider:** True


---


### /World/RobotArm1_4/link5/visuals
*  **Prim路径 (Prim Path):**/World/RobotArm1_4/link5/visuals
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/visuals/link5'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.180, 0.262, 0.440)'
   *   Center: '(-2.240, 28.959, 0.738)'


---


### /World/RobotArm1_4/link5/collisions
*  **Prim路径 (Prim Path):**/World/RobotArm1_4/link5/collisions
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/colliders/link5'
*  **世界包围盒 (World BBox):**
   *   Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
   *   Center: '(-2.240, 29.000, 0.595)'
*  **物理属性 (Physics):**
   *   **Collider:** True


---


### /World/RobotArm1_4/link6/visuals
*  **Prim路径 (Prim Path):**/World/RobotArm1_4/link6/visuals
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/visuals/link6'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.307, 0.200, 0.212)'
   *   Center: '(-2.164, 29.022, 0.566)'


---


### /World/RobotArm1_4/link6/collisions
*  **Prim路径 (Prim Path):**/World/RobotArm1_4/link6/collisions
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/colliders/link6'
*  **世界包围盒 (World BBox):**
   *   Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
   *   Center: '(-2.240, 29.000, 0.595)'
*  **物理属性 (Physics):**
   *   **Collider:** True


---


### /World/RobotArm1_4/link7/visuals
*  **Prim路径 (Prim Path):**/World/RobotArm1_4/link7/visuals
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/visuals/link7'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.156, 0.186, 0.066)'
   *   Center: '(-2.088, 29.015, 0.434)'


---


### /World/RobotArm1_4/link7/collisions
*  **Prim路径 (Prim Path):**/World/RobotArm1_4/link7/collisions
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/colliders/link7'
*  **世界包围盒 (World BBox):**
   *   Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
   *   Center: '(-2.088, 29.000, 0.401)'
*  **物理属性 (Physics):**
   *   **Collider:** True


---


### /World/RobotArm1_5
*  **Prim路径 (Prim Path):**/World/RobotArm1_5
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/5.0/Isaac/Robots/Ufactory/xarm7/xarm7.usd'
       *   [reference] './configuration/xarm7_physics.usd'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.616, 0.455, 1.292)'
   *   Center: '(2.682, 29.010, 0.723)'


---


### /World/RobotArm1_5/gripper
*  **Prim路径 (Prim Path):**/World/RobotArm1_5/gripper
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '../xarm_gripper/xarm_gripper.usd'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.150, 0.346, 0.324)'
   *   Center: '(2.912, 29.000, 0.239)'


---


### /World/RobotArm1_5/gripper/xarm_gripper_base_link/visuals
*  **Prim路径 (Prim Path):**/World/RobotArm1_5/gripper/xarm_gripper_base_link/visuals
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/visuals/xarm_gripper_base_link'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.150, 0.213, 0.209)'
   *   Center: '(2.912, 29.000, 0.297)'


---


### /World/RobotArm1_5/gripper/xarm_gripper_base_link/collisions
*  **Prim路径 (Prim Path):**/World/RobotArm1_5/gripper/xarm_gripper_base_link/collisions
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/colliders/xarm_gripper_base_link'
*  **世界包围盒 (World BBox):**
   *   Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
   *   Center: '(2.912, 29.000, 0.401)'
*  **物理属性 (Physics):**
   *   **Collider:** True


---


### /World/RobotArm1_5/gripper/left_outer_knuckle/visuals
*  **Prim路径 (Prim Path):**/World/RobotArm1_5/gripper/left_outer_knuckle/visuals
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/visuals/left_outer_knuckle'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.024, 0.155, 0.111)'
   *   Center: '(2.912, 28.904, 0.242)'


---


### /World/RobotArm1_5/gripper/left_outer_knuckle/collisions
*  **Prim路径 (Prim Path):**/World/RobotArm1_5/gripper/left_outer_knuckle/collisions
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/colliders/left_outer_knuckle'
*  **世界包围盒 (World BBox):**
   *   Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
   *   Center: '(2.912, 28.930, 0.283)'
*  **物理属性 (Physics):**
   *   **Collider:** True


---


### /World/RobotArm1_5/gripper/left_finger/visuals
*  **Prim路径 (Prim Path):**/World/RobotArm1_5/gripper/left_finger/visuals
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/visuals/left_finger'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.064, 0.064, 0.134)'
   *   Center: '(2.912, 28.879, 0.144)'


---


### /World/RobotArm1_5/gripper/left_finger/collisions
*  **Prim路径 (Prim Path):**/World/RobotArm1_5/gripper/left_finger/collisions
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/colliders/left_finger'
*  **世界包围盒 (World BBox):**
   *   Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
   *   Center: '(2.912, 28.859, 0.199)'
*  **物理属性 (Physics):**
   *   **Collider:** True


---


### /World/RobotArm1_5/gripper/left_inner_knuckle/visuals
*  **Prim路径 (Prim Path):**/World/RobotArm1_5/gripper/left_inner_knuckle/visuals
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/visuals/left_inner_knuckle'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.056, 0.095, 0.108)'
   *   Center: '(2.912, 28.925, 0.211)'


---


### /World/RobotArm1_5/gripper/left_inner_knuckle/collisions
*  **Prim路径 (Prim Path):**/World/RobotArm1_5/gripper/left_inner_knuckle/collisions
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/colliders/left_inner_knuckle'
*  **世界包围盒 (World BBox):**
   *   Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
   *   Center: '(2.912, 28.960, 0.253)'
*  **物理属性 (Physics):**
   *   **Collider:** True


---


### /World/RobotArm1_5/gripper/right_inner_knuckle/visuals
*  **Prim路径 (Prim Path):**/World/RobotArm1_5/gripper/right_inner_knuckle/visuals
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/visuals/right_inner_knuckle'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.056, 0.095, 0.108)'
   *   Center: '(2.912, 29.075, 0.211)'


---


### /World/RobotArm1_5/gripper/right_inner_knuckle/collisions
*  **Prim路径 (Prim Path):**/World/RobotArm1_5/gripper/right_inner_knuckle/collisions
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/colliders/right_inner_knuckle'
*  **世界包围盒 (World BBox):**
   *   Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
   *   Center: '(2.912, 29.040, 0.253)'
*  **物理属性 (Physics):**
   *   **Collider:** True


---


### /World/RobotArm1_5/gripper/right_outer_knuckle/visuals
*  **Prim路径 (Prim Path):**/World/RobotArm1_5/gripper/right_outer_knuckle/visuals
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/visuals/right_outer_knuckle'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.024, 0.155, 0.111)'
   *   Center: '(2.912, 29.096, 0.242)'


---


### /World/RobotArm1_5/gripper/right_outer_knuckle/collisions
*  **Prim路径 (Prim Path):**/World/RobotArm1_5/gripper/right_outer_knuckle/collisions
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/colliders/right_outer_knuckle'
*  **世界包围盒 (World BBox):**
   *   Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
   *   Center: '(2.912, 29.070, 0.283)'
*  **物理属性 (Physics):**
   *   **Collider:** True


---


### /World/RobotArm1_5/gripper/right_finger/visuals
*  **Prim路径 (Prim Path):**/World/RobotArm1_5/gripper/right_finger/visuals
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/visuals/right_finger'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.064, 0.064, 0.134)'
   *   Center: '(2.912, 29.121, 0.144)'


---


### /World/RobotArm1_5/gripper/right_finger/collisions
*  **Prim路径 (Prim Path):**/World/RobotArm1_5/gripper/right_finger/collisions
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/colliders/right_finger'
*  **世界包围盒 (World BBox):**
   *   Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
   *   Center: '(2.912, 29.141, 0.199)'
*  **物理属性 (Physics):**
   *   **Collider:** True


---


### /World/RobotArm1_5/world/visuals
*  **Prim路径 (Prim Path):**/World/RobotArm1_5/world/visuals
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/visuals/world'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.252, 0.252, 0.301)'
   *   Center: '(2.500, 29.000, 0.310)'


---


### /World/RobotArm1_5/world/collisions
*  **Prim路径 (Prim Path):**/World/RobotArm1_5/world/collisions
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/colliders/world'
*  **世界包围盒 (World BBox):**
   *   Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
   *   Center: '(2.500, 29.000, 0.160)'
*  **物理属性 (Physics):**
   *   **Collider:** True


---


### /World/RobotArm1_5/link1/visuals
*  **Prim路径 (Prim Path):**/World/RobotArm1_5/link1/visuals
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/visuals/link1'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.194, 0.232, 0.329)'
   *   Center: '(2.500, 29.002, 0.627)'


---


### /World/RobotArm1_5/link1/collisions
*  **Prim路径 (Prim Path):**/World/RobotArm1_5/link1/collisions
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/colliders/link1'
*  **世界包围盒 (World BBox):**
   *   Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
   *   Center: '(2.500, 29.000, 0.694)'
*  **物理属性 (Physics):**
   *   **Collider:** True


---


### /World/RobotArm1_5/link2/visuals
*  **Prim路径 (Prim Path):**/World/RobotArm1_5/link2/visuals
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/visuals/link2'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.194, 0.326, 0.463)'
   *   Center: '(2.500, 29.074, 0.828)'


---


### /World/RobotArm1_5/link2/collisions
*  **Prim路径 (Prim Path):**/World/RobotArm1_5/link2/collisions
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/colliders/link2'
*  **世界包围盒 (World BBox):**
   *   Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
   *   Center: '(2.500, 29.000, 0.694)'
*  **物理属性 (Physics):**
   *   **Collider:** True


---


### /World/RobotArm1_5/link3/visuals
*  **Prim路径 (Prim Path):**/World/RobotArm1_5/link3/visuals
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/visuals/link3'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.283, 0.229, 0.309)'
   *   Center: '(2.552, 29.023, 1.215)'


---


### /World/RobotArm1_5/link3/collisions
*  **Prim路径 (Prim Path):**/World/RobotArm1_5/link3/collisions
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/colliders/link3'
*  **世界包围盒 (World BBox):**
   *   Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
   *   Center: '(2.500, 29.000, 1.280)'
*  **物理属性 (Physics):**
   *   **Collider:** True


---


### /World/RobotArm1_5/link4/visuals
*  **Prim路径 (Prim Path):**/World/RobotArm1_5/link4/visuals
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/visuals/link4'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.334, 0.308, 0.414)'
   *   Center: '(2.683, 28.936, 1.162)'


---


### /World/RobotArm1_5/link4/collisions
*  **Prim路径 (Prim Path):**/World/RobotArm1_5/link4/collisions
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/colliders/link4'
*  **世界包围盒 (World BBox):**
   *   Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
   *   Center: '(2.605, 29.000, 1.280)'
*  **物理属性 (Physics):**
   *   **Collider:** True


---


### /World/RobotArm1_5/link5/visuals
*  **Prim路径 (Prim Path):**/World/RobotArm1_5/link5/visuals
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/visuals/link5'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.180, 0.262, 0.440)'
   *   Center: '(2.760, 28.959, 0.738)'


---


### /World/RobotArm1_5/link5/collisions
*  **Prim路径 (Prim Path):**/World/RobotArm1_5/link5/collisions
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/colliders/link5'
*  **世界包围盒 (World BBox):**
   *   Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
   *   Center: '(2.760, 29.000, 0.595)'
*  **物理属性 (Physics):**
   *   **Collider:** True


---


### /World/RobotArm1_5/link6/visuals
*  **Prim路径 (Prim Path):**/World/RobotArm1_5/link6/visuals
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/visuals/link6'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.307, 0.200, 0.212)'
   *   Center: '(2.836, 29.022, 0.566)'


---


### /World/RobotArm1_5/link6/collisions
*  **Prim路径 (Prim Path):**/World/RobotArm1_5/link6/collisions
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/colliders/link6'
*  **世界包围盒 (World BBox):**
   *   Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
   *   Center: '(2.760, 29.000, 0.595)'
*  **物理属性 (Physics):**
   *   **Collider:** True


---


### /World/RobotArm1_5/link7/visuals
*  **Prim路径 (Prim Path):**/World/RobotArm1_5/link7/visuals
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/visuals/link7'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.156, 0.186, 0.066)'
   *   Center: '(2.912, 29.015, 0.434)'


---


### /World/RobotArm1_5/link7/collisions
*  **Prim路径 (Prim Path):**/World/RobotArm1_5/link7/collisions
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/colliders/link7'
*  **世界包围盒 (World BBox):**
   *   Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
   *   Center: '(2.912, 29.000, 0.401)'
*  **物理属性 (Physics):**
   *   **Collider:** True


---


### /World/RobotArm1_6
*  **Prim路径 (Prim Path):**/World/RobotArm1_6
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/5.0/Isaac/Robots/Ufactory/xarm7/xarm7.usd'
       *   [reference] './configuration/xarm7_physics.usd'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.616, 0.455, 1.292)'
   *   Center: '(7.682, 29.010, 0.723)'


---


### /World/RobotArm1_6/gripper
*  **Prim路径 (Prim Path):**/World/RobotArm1_6/gripper
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '../xarm_gripper/xarm_gripper.usd'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.150, 0.346, 0.324)'
   *   Center: '(7.912, 29.000, 0.239)'


---


### /World/RobotArm1_6/gripper/xarm_gripper_base_link/visuals
*  **Prim路径 (Prim Path):**/World/RobotArm1_6/gripper/xarm_gripper_base_link/visuals
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/visuals/xarm_gripper_base_link'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.150, 0.213, 0.209)'
   *   Center: '(7.912, 29.000, 0.297)'


---


### /World/RobotArm1_6/gripper/xarm_gripper_base_link/collisions
*  **Prim路径 (Prim Path):**/World/RobotArm1_6/gripper/xarm_gripper_base_link/collisions
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/colliders/xarm_gripper_base_link'
*  **世界包围盒 (World BBox):**
   *   Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
   *   Center: '(7.912, 29.000, 0.401)'
*  **物理属性 (Physics):**
   *   **Collider:** True


---


### /World/RobotArm1_6/gripper/left_outer_knuckle/visuals
*  **Prim路径 (Prim Path):**/World/RobotArm1_6/gripper/left_outer_knuckle/visuals
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/visuals/left_outer_knuckle'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.024, 0.155, 0.111)'
   *   Center: '(7.912, 28.904, 0.242)'


---


### /World/RobotArm1_6/gripper/left_outer_knuckle/collisions
*  **Prim路径 (Prim Path):**/World/RobotArm1_6/gripper/left_outer_knuckle/collisions
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/colliders/left_outer_knuckle'
*  **世界包围盒 (World BBox):**
   *   Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
   *   Center: '(7.912, 28.930, 0.283)'
*  **物理属性 (Physics):**
   *   **Collider:** True


---


### /World/RobotArm1_6/gripper/left_finger/visuals
*  **Prim路径 (Prim Path):**/World/RobotArm1_6/gripper/left_finger/visuals
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/visuals/left_finger'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.064, 0.064, 0.134)'
   *   Center: '(7.912, 28.879, 0.144)'


---


### /World/RobotArm1_6/gripper/left_finger/collisions
*  **Prim路径 (Prim Path):**/World/RobotArm1_6/gripper/left_finger/collisions
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/colliders/left_finger'
*  **世界包围盒 (World BBox):**
   *   Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
   *   Center: '(7.912, 28.859, 0.199)'
*  **物理属性 (Physics):**
   *   **Collider:** True


---


### /World/RobotArm1_6/gripper/left_inner_knuckle/visuals
*  **Prim路径 (Prim Path):**/World/RobotArm1_6/gripper/left_inner_knuckle/visuals
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/visuals/left_inner_knuckle'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.056, 0.095, 0.108)'
   *   Center: '(7.912, 28.925, 0.211)'


---


### /World/RobotArm1_6/gripper/left_inner_knuckle/collisions
*  **Prim路径 (Prim Path):**/World/RobotArm1_6/gripper/left_inner_knuckle/collisions
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/colliders/left_inner_knuckle'
*  **世界包围盒 (World BBox):**
   *   Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
   *   Center: '(7.912, 28.960, 0.253)'
*  **物理属性 (Physics):**
   *   **Collider:** True


---


### /World/RobotArm1_6/gripper/right_inner_knuckle/visuals
*  **Prim路径 (Prim Path):**/World/RobotArm1_6/gripper/right_inner_knuckle/visuals
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/visuals/right_inner_knuckle'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.056, 0.095, 0.108)'
   *   Center: '(7.912, 29.075, 0.211)'


---


### /World/RobotArm1_6/gripper/right_inner_knuckle/collisions
*  **Prim路径 (Prim Path):**/World/RobotArm1_6/gripper/right_inner_knuckle/collisions
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/colliders/right_inner_knuckle'
*  **世界包围盒 (World BBox):**
   *   Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
   *   Center: '(7.912, 29.040, 0.253)'
*  **物理属性 (Physics):**
   *   **Collider:** True


---


### /World/RobotArm1_6/gripper/right_outer_knuckle/visuals
*  **Prim路径 (Prim Path):**/World/RobotArm1_6/gripper/right_outer_knuckle/visuals
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/visuals/right_outer_knuckle'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.024, 0.155, 0.111)'
   *   Center: '(7.912, 29.096, 0.242)'


---


### /World/RobotArm1_6/gripper/right_outer_knuckle/collisions
*  **Prim路径 (Prim Path):**/World/RobotArm1_6/gripper/right_outer_knuckle/collisions
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/colliders/right_outer_knuckle'
*  **世界包围盒 (World BBox):**
   *   Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
   *   Center: '(7.912, 29.070, 0.283)'
*  **物理属性 (Physics):**
   *   **Collider:** True


---


### /World/RobotArm1_6/gripper/right_finger/visuals
*  **Prim路径 (Prim Path):**/World/RobotArm1_6/gripper/right_finger/visuals
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/visuals/right_finger'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.064, 0.064, 0.134)'
   *   Center: '(7.912, 29.121, 0.144)'


---


### /World/RobotArm1_6/gripper/right_finger/collisions
*  **Prim路径 (Prim Path):**/World/RobotArm1_6/gripper/right_finger/collisions
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/colliders/right_finger'
*  **世界包围盒 (World BBox):**
   *   Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
   *   Center: '(7.912, 29.141, 0.199)'
*  **物理属性 (Physics):**
   *   **Collider:** True


---


### /World/RobotArm1_6/world/visuals
*  **Prim路径 (Prim Path):**/World/RobotArm1_6/world/visuals
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/visuals/world'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.252, 0.252, 0.301)'
   *   Center: '(7.500, 29.000, 0.310)'


---


### /World/RobotArm1_6/world/collisions
*  **Prim路径 (Prim Path):**/World/RobotArm1_6/world/collisions
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/colliders/world'
*  **世界包围盒 (World BBox):**
   *   Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
   *   Center: '(7.500, 29.000, 0.160)'
*  **物理属性 (Physics):**
   *   **Collider:** True


---


### /World/RobotArm1_6/link1/visuals
*  **Prim路径 (Prim Path):**/World/RobotArm1_6/link1/visuals
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/visuals/link1'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.194, 0.232, 0.329)'
   *   Center: '(7.500, 29.002, 0.627)'


---


### /World/RobotArm1_6/link1/collisions
*  **Prim路径 (Prim Path):**/World/RobotArm1_6/link1/collisions
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/colliders/link1'
*  **世界包围盒 (World BBox):**
   *   Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
   *   Center: '(7.500, 29.000, 0.694)'
*  **物理属性 (Physics):**
   *   **Collider:** True


---


### /World/RobotArm1_6/link2/visuals
*  **Prim路径 (Prim Path):**/World/RobotArm1_6/link2/visuals
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/visuals/link2'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.194, 0.326, 0.463)'
   *   Center: '(7.500, 29.074, 0.828)'


---


### /World/RobotArm1_6/link2/collisions
*  **Prim路径 (Prim Path):**/World/RobotArm1_6/link2/collisions
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/colliders/link2'
*  **世界包围盒 (World BBox):**
   *   Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
   *   Center: '(7.500, 29.000, 0.694)'
*  **物理属性 (Physics):**
   *   **Collider:** True


---


### /World/RobotArm1_6/link3/visuals
*  **Prim路径 (Prim Path):**/World/RobotArm1_6/link3/visuals
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/visuals/link3'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.283, 0.229, 0.309)'
   *   Center: '(7.552, 29.023, 1.215)'


---


### /World/RobotArm1_6/link3/collisions
*  **Prim路径 (Prim Path):**/World/RobotArm1_6/link3/collisions
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/colliders/link3'
*  **世界包围盒 (World BBox):**
   *   Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
   *   Center: '(7.500, 29.000, 1.280)'
*  **物理属性 (Physics):**
   *   **Collider:** True


---


### /World/RobotArm1_6/link4/visuals
*  **Prim路径 (Prim Path):**/World/RobotArm1_6/link4/visuals
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/visuals/link4'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.334, 0.308, 0.414)'
   *   Center: '(7.683, 28.936, 1.162)'


---


### /World/RobotArm1_6/link4/collisions
*  **Prim路径 (Prim Path):**/World/RobotArm1_6/link4/collisions
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/colliders/link4'
*  **世界包围盒 (World BBox):**
   *   Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
   *   Center: '(7.605, 29.000, 1.280)'
*  **物理属性 (Physics):**
   *   **Collider:** True


---


### /World/RobotArm1_6/link5/visuals
*  **Prim路径 (Prim Path):**/World/RobotArm1_6/link5/visuals
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/visuals/link5'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.180, 0.262, 0.440)'
   *   Center: '(7.760, 28.959, 0.738)'


---


### /World/RobotArm1_6/link5/collisions
*  **Prim路径 (Prim Path):**/World/RobotArm1_6/link5/collisions
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/colliders/link5'
*  **世界包围盒 (World BBox):**
   *   Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
   *   Center: '(7.760, 29.000, 0.595)'
*  **物理属性 (Physics):**
   *   **Collider:** True


---


### /World/RobotArm1_6/link6/visuals
*  **Prim路径 (Prim Path):**/World/RobotArm1_6/link6/visuals
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/visuals/link6'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.307, 0.200, 0.212)'
   *   Center: '(7.836, 29.022, 0.566)'


---


### /World/RobotArm1_6/link6/collisions
*  **Prim路径 (Prim Path):**/World/RobotArm1_6/link6/collisions
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/colliders/link6'
*  **世界包围盒 (World BBox):**
   *   Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
   *   Center: '(7.760, 29.000, 0.595)'
*  **物理属性 (Physics):**
   *   **Collider:** True


---


### /World/RobotArm1_6/link7/visuals
*  **Prim路径 (Prim Path):**/World/RobotArm1_6/link7/visuals
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/visuals/link7'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.156, 0.186, 0.066)'
   *   Center: '(7.912, 29.015, 0.434)'


---


### /World/RobotArm1_6/link7/collisions
*  **Prim路径 (Prim Path):**/World/RobotArm1_6/link7/collisions
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/colliders/link7'
*  **世界包围盒 (World BBox):**
   *   Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
   *   Center: '(7.912, 29.000, 0.401)'
*  **物理属性 (Physics):**
   *   **Collider:** True


---


### /World/RobotArm1_7
*  **Prim路径 (Prim Path):**/World/RobotArm1_7
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/5.0/Isaac/Robots/Ufactory/xarm7/xarm7.usd'
       *   [reference] './configuration/xarm7_physics.usd'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.616, 0.455, 1.292)'
   *   Center: '(12.682, 29.010, 0.723)'


---


### /World/RobotArm1_7/gripper
*  **Prim路径 (Prim Path):**/World/RobotArm1_7/gripper
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '../xarm_gripper/xarm_gripper.usd'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.150, 0.346, 0.324)'
   *   Center: '(12.912, 29.000, 0.239)'


---


### /World/RobotArm1_7/gripper/xarm_gripper_base_link/visuals
*  **Prim路径 (Prim Path):**/World/RobotArm1_7/gripper/xarm_gripper_base_link/visuals
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/visuals/xarm_gripper_base_link'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.150, 0.213, 0.209)'
   *   Center: '(12.912, 29.000, 0.297)'


---


### /World/RobotArm1_7/gripper/xarm_gripper_base_link/collisions
*  **Prim路径 (Prim Path):**/World/RobotArm1_7/gripper/xarm_gripper_base_link/collisions
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/colliders/xarm_gripper_base_link'
*  **世界包围盒 (World BBox):**
   *   Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
   *   Center: '(12.912, 29.000, 0.401)'
*  **物理属性 (Physics):**
   *   **Collider:** True


---


### /World/RobotArm1_7/gripper/left_outer_knuckle/visuals
*  **Prim路径 (Prim Path):**/World/RobotArm1_7/gripper/left_outer_knuckle/visuals
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/visuals/left_outer_knuckle'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.024, 0.155, 0.111)'
   *   Center: '(12.912, 28.904, 0.242)'


---


### /World/RobotArm1_7/gripper/left_outer_knuckle/collisions
*  **Prim路径 (Prim Path):**/World/RobotArm1_7/gripper/left_outer_knuckle/collisions
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/colliders/left_outer_knuckle'
*  **世界包围盒 (World BBox):**
   *   Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
   *   Center: '(12.912, 28.930, 0.283)'
*  **物理属性 (Physics):**
   *   **Collider:** True


---


### /World/RobotArm1_7/gripper/left_finger/visuals
*  **Prim路径 (Prim Path):**/World/RobotArm1_7/gripper/left_finger/visuals
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/visuals/left_finger'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.064, 0.064, 0.134)'
   *   Center: '(12.912, 28.879, 0.144)'


---


### /World/RobotArm1_7/gripper/left_finger/collisions
*  **Prim路径 (Prim Path):**/World/RobotArm1_7/gripper/left_finger/collisions
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/colliders/left_finger'
*  **世界包围盒 (World BBox):**
   *   Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
   *   Center: '(12.912, 28.859, 0.199)'
*  **物理属性 (Physics):**
   *   **Collider:** True


---


### /World/RobotArm1_7/gripper/left_inner_knuckle/visuals
*  **Prim路径 (Prim Path):**/World/RobotArm1_7/gripper/left_inner_knuckle/visuals
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/visuals/left_inner_knuckle'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.056, 0.095, 0.108)'
   *   Center: '(12.912, 28.925, 0.211)'


---


### /World/RobotArm1_7/gripper/left_inner_knuckle/collisions
*  **Prim路径 (Prim Path):**/World/RobotArm1_7/gripper/left_inner_knuckle/collisions
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/colliders/left_inner_knuckle'
*  **世界包围盒 (World BBox):**
   *   Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
   *   Center: '(12.912, 28.960, 0.253)'
*  **物理属性 (Physics):**
   *   **Collider:** True


---


### /World/RobotArm1_7/gripper/right_inner_knuckle/visuals
*  **Prim路径 (Prim Path):**/World/RobotArm1_7/gripper/right_inner_knuckle/visuals
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/visuals/right_inner_knuckle'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.056, 0.095, 0.108)'
   *   Center: '(12.912, 29.075, 0.211)'


---


### /World/RobotArm1_7/gripper/right_inner_knuckle/collisions
*  **Prim路径 (Prim Path):**/World/RobotArm1_7/gripper/right_inner_knuckle/collisions
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/colliders/right_inner_knuckle'
*  **世界包围盒 (World BBox):**
   *   Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
   *   Center: '(12.912, 29.040, 0.253)'
*  **物理属性 (Physics):**
   *   **Collider:** True


---


### /World/RobotArm1_7/gripper/right_outer_knuckle/visuals
*  **Prim路径 (Prim Path):**/World/RobotArm1_7/gripper/right_outer_knuckle/visuals
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/visuals/right_outer_knuckle'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.024, 0.155, 0.111)'
   *   Center: '(12.912, 29.096, 0.242)'


---


### /World/RobotArm1_7/gripper/right_outer_knuckle/collisions
*  **Prim路径 (Prim Path):**/World/RobotArm1_7/gripper/right_outer_knuckle/collisions
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/colliders/right_outer_knuckle'
*  **世界包围盒 (World BBox):**
   *   Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
   *   Center: '(12.912, 29.070, 0.283)'
*  **物理属性 (Physics):**
   *   **Collider:** True


---


### /World/RobotArm1_7/gripper/right_finger/visuals
*  **Prim路径 (Prim Path):**/World/RobotArm1_7/gripper/right_finger/visuals
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/visuals/right_finger'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.064, 0.064, 0.134)'
   *   Center: '(12.912, 29.121, 0.144)'


---


### /World/RobotArm1_7/gripper/right_finger/collisions
*  **Prim路径 (Prim Path):**/World/RobotArm1_7/gripper/right_finger/collisions
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/colliders/right_finger'
*  **世界包围盒 (World BBox):**
   *   Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
   *   Center: '(12.912, 29.141, 0.199)'
*  **物理属性 (Physics):**
   *   **Collider:** True


---


### /World/RobotArm1_7/world/visuals
*  **Prim路径 (Prim Path):**/World/RobotArm1_7/world/visuals
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/visuals/world'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.252, 0.252, 0.301)'
   *   Center: '(12.500, 29.000, 0.310)'


---


### /World/RobotArm1_7/world/collisions
*  **Prim路径 (Prim Path):**/World/RobotArm1_7/world/collisions
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/colliders/world'
*  **世界包围盒 (World BBox):**
   *   Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
   *   Center: '(12.500, 29.000, 0.160)'
*  **物理属性 (Physics):**
   *   **Collider:** True


---


### /World/RobotArm1_7/link1/visuals
*  **Prim路径 (Prim Path):**/World/RobotArm1_7/link1/visuals
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/visuals/link1'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.194, 0.232, 0.329)'
   *   Center: '(12.500, 29.002, 0.627)'


---


### /World/RobotArm1_7/link1/collisions
*  **Prim路径 (Prim Path):**/World/RobotArm1_7/link1/collisions
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/colliders/link1'
*  **世界包围盒 (World BBox):**
   *   Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
   *   Center: '(12.500, 29.000, 0.694)'
*  **物理属性 (Physics):**
   *   **Collider:** True


---


### /World/RobotArm1_7/link2/visuals
*  **Prim路径 (Prim Path):**/World/RobotArm1_7/link2/visuals
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/visuals/link2'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.194, 0.326, 0.463)'
   *   Center: '(12.500, 29.074, 0.828)'


---


### /World/RobotArm1_7/link2/collisions
*  **Prim路径 (Prim Path):**/World/RobotArm1_7/link2/collisions
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/colliders/link2'
*  **世界包围盒 (World BBox):**
   *   Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
   *   Center: '(12.500, 29.000, 0.694)'
*  **物理属性 (Physics):**
   *   **Collider:** True


---


### /World/RobotArm1_7/link3/visuals
*  **Prim路径 (Prim Path):**/World/RobotArm1_7/link3/visuals
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/visuals/link3'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.283, 0.229, 0.309)'
   *   Center: '(12.552, 29.023, 1.215)'


---


### /World/RobotArm1_7/link3/collisions
*  **Prim路径 (Prim Path):**/World/RobotArm1_7/link3/collisions
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/colliders/link3'
*  **世界包围盒 (World BBox):**
   *   Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
   *   Center: '(12.500, 29.000, 1.280)'
*  **物理属性 (Physics):**
   *   **Collider:** True


---


### /World/RobotArm1_7/link4/visuals
*  **Prim路径 (Prim Path):**/World/RobotArm1_7/link4/visuals
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/visuals/link4'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.334, 0.308, 0.414)'
   *   Center: '(12.683, 28.936, 1.162)'


---


### /World/RobotArm1_7/link4/collisions
*  **Prim路径 (Prim Path):**/World/RobotArm1_7/link4/collisions
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/colliders/link4'
*  **世界包围盒 (World BBox):**
   *   Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
   *   Center: '(12.605, 29.000, 1.280)'
*  **物理属性 (Physics):**
   *   **Collider:** True


---


### /World/RobotArm1_7/link5/visuals
*  **Prim路径 (Prim Path):**/World/RobotArm1_7/link5/visuals
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/visuals/link5'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.180, 0.262, 0.440)'
   *   Center: '(12.760, 28.959, 0.738)'


---


### /World/RobotArm1_7/link5/collisions
*  **Prim路径 (Prim Path):**/World/RobotArm1_7/link5/collisions
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/colliders/link5'
*  **世界包围盒 (World BBox):**
   *   Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
   *   Center: '(12.760, 29.000, 0.595)'
*  **物理属性 (Physics):**
   *   **Collider:** True


---


### /World/RobotArm1_7/link6/visuals
*  **Prim路径 (Prim Path):**/World/RobotArm1_7/link6/visuals
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/visuals/link6'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.307, 0.200, 0.212)'
   *   Center: '(12.836, 29.022, 0.566)'


---


### /World/RobotArm1_7/link6/collisions
*  **Prim路径 (Prim Path):**/World/RobotArm1_7/link6/collisions
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/colliders/link6'
*  **世界包围盒 (World BBox):**
   *   Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
   *   Center: '(12.760, 29.000, 0.595)'
*  **物理属性 (Physics):**
   *   **Collider:** True


---


### /World/RobotArm1_7/link7/visuals
*  **Prim路径 (Prim Path):**/World/RobotArm1_7/link7/visuals
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/visuals/link7'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.156, 0.186, 0.066)'
   *   Center: '(12.912, 29.015, 0.434)'


---


### /World/RobotArm1_7/link7/collisions
*  **Prim路径 (Prim Path):**/World/RobotArm1_7/link7/collisions
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/colliders/link7'
*  **世界包围盒 (World BBox):**
   *   Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
   *   Center: '(12.912, 29.000, 0.401)'
*  **物理属性 (Physics):**
   *   **Collider:** True


---


### /World/RobotArm1_8
*  **Prim路径 (Prim Path):**/World/RobotArm1_8
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '/media/simple/another_Documents/isaacsim_assets/Assets/Isaac/5.0/Isaac/Robots/Ufactory/xarm7/xarm7.usd'
       *   [reference] './configuration/xarm7_physics.usd'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.616, 0.455, 1.292)'
   *   Center: '(17.682, 29.010, 0.723)'


---


### /World/RobotArm1_8/gripper
*  **Prim路径 (Prim Path):**/World/RobotArm1_8/gripper
*  **Prim类型 (Prim Type):**Xform
*  **外部引用 (Referenced USD Files):**
       *   [reference] '../xarm_gripper/xarm_gripper.usd'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.150, 0.346, 0.324)'
   *   Center: '(17.912, 29.000, 0.239)'


---


### /World/RobotArm1_8/gripper/xarm_gripper_base_link/visuals
*  **Prim路径 (Prim Path):**/World/RobotArm1_8/gripper/xarm_gripper_base_link/visuals
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/visuals/xarm_gripper_base_link'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.150, 0.213, 0.209)'
   *   Center: '(17.912, 29.000, 0.297)'


---


### /World/RobotArm1_8/gripper/xarm_gripper_base_link/collisions
*  **Prim路径 (Prim Path):**/World/RobotArm1_8/gripper/xarm_gripper_base_link/collisions
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/colliders/xarm_gripper_base_link'
*  **世界包围盒 (World BBox):**
   *   Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
   *   Center: '(17.912, 29.000, 0.401)'
*  **物理属性 (Physics):**
   *   **Collider:** True


---


### /World/RobotArm1_8/gripper/left_outer_knuckle/visuals
*  **Prim路径 (Prim Path):**/World/RobotArm1_8/gripper/left_outer_knuckle/visuals
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/visuals/left_outer_knuckle'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.024, 0.155, 0.111)'
   *   Center: '(17.912, 28.904, 0.242)'


---


### /World/RobotArm1_8/gripper/left_outer_knuckle/collisions
*  **Prim路径 (Prim Path):**/World/RobotArm1_8/gripper/left_outer_knuckle/collisions
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/colliders/left_outer_knuckle'
*  **世界包围盒 (World BBox):**
   *   Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
   *   Center: '(17.912, 28.930, 0.283)'
*  **物理属性 (Physics):**
   *   **Collider:** True


---


### /World/RobotArm1_8/gripper/left_finger/visuals
*  **Prim路径 (Prim Path):**/World/RobotArm1_8/gripper/left_finger/visuals
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/visuals/left_finger'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.064, 0.064, 0.134)'
   *   Center: '(17.912, 28.879, 0.144)'


---


### /World/RobotArm1_8/gripper/left_finger/collisions
*  **Prim路径 (Prim Path):**/World/RobotArm1_8/gripper/left_finger/collisions
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/colliders/left_finger'
*  **世界包围盒 (World BBox):**
   *   Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
   *   Center: '(17.912, 28.859, 0.199)'
*  **物理属性 (Physics):**
   *   **Collider:** True


---


### /World/RobotArm1_8/gripper/left_inner_knuckle/visuals
*  **Prim路径 (Prim Path):**/World/RobotArm1_8/gripper/left_inner_knuckle/visuals
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/visuals/left_inner_knuckle'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.056, 0.095, 0.108)'
   *   Center: '(17.912, 28.925, 0.211)'


---


### /World/RobotArm1_8/gripper/left_inner_knuckle/collisions
*  **Prim路径 (Prim Path):**/World/RobotArm1_8/gripper/left_inner_knuckle/collisions
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/colliders/left_inner_knuckle'
*  **世界包围盒 (World BBox):**
   *   Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
   *   Center: '(17.912, 28.960, 0.253)'
*  **物理属性 (Physics):**
   *   **Collider:** True


---


### /World/RobotArm1_8/gripper/right_inner_knuckle/visuals
*  **Prim路径 (Prim Path):**/World/RobotArm1_8/gripper/right_inner_knuckle/visuals
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/visuals/right_inner_knuckle'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.056, 0.095, 0.108)'
   *   Center: '(17.912, 29.075, 0.211)'


---


### /World/RobotArm1_8/gripper/right_inner_knuckle/collisions
*  **Prim路径 (Prim Path):**/World/RobotArm1_8/gripper/right_inner_knuckle/collisions
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/colliders/right_inner_knuckle'
*  **世界包围盒 (World BBox):**
   *   Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
   *   Center: '(17.912, 29.040, 0.253)'
*  **物理属性 (Physics):**
   *   **Collider:** True


---


### /World/RobotArm1_8/gripper/right_outer_knuckle/visuals
*  **Prim路径 (Prim Path):**/World/RobotArm1_8/gripper/right_outer_knuckle/visuals
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/visuals/right_outer_knuckle'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.024, 0.155, 0.111)'
   *   Center: '(17.912, 29.096, 0.242)'


---


### /World/RobotArm1_8/gripper/right_outer_knuckle/collisions
*  **Prim路径 (Prim Path):**/World/RobotArm1_8/gripper/right_outer_knuckle/collisions
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/colliders/right_outer_knuckle'
*  **世界包围盒 (World BBox):**
   *   Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
   *   Center: '(17.912, 29.070, 0.283)'
*  **物理属性 (Physics):**
   *   **Collider:** True


---


### /World/RobotArm1_8/gripper/right_finger/visuals
*  **Prim路径 (Prim Path):**/World/RobotArm1_8/gripper/right_finger/visuals
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/visuals/right_finger'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.064, 0.064, 0.134)'
   *   Center: '(17.912, 29.121, 0.144)'


---


### /World/RobotArm1_8/gripper/right_finger/collisions
*  **Prim路径 (Prim Path):**/World/RobotArm1_8/gripper/right_finger/collisions
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/colliders/right_finger'
*  **世界包围盒 (World BBox):**
   *   Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
   *   Center: '(17.912, 29.141, 0.199)'
*  **物理属性 (Physics):**
   *   **Collider:** True


---


### /World/RobotArm1_8/world/visuals
*  **Prim路径 (Prim Path):**/World/RobotArm1_8/world/visuals
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/visuals/world'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.252, 0.252, 0.301)'
   *   Center: '(17.500, 29.000, 0.310)'


---


### /World/RobotArm1_8/world/collisions
*  **Prim路径 (Prim Path):**/World/RobotArm1_8/world/collisions
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/colliders/world'
*  **世界包围盒 (World BBox):**
   *   Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
   *   Center: '(17.500, 29.000, 0.160)'
*  **物理属性 (Physics):**
   *   **Collider:** True


---


### /World/RobotArm1_8/link1/visuals
*  **Prim路径 (Prim Path):**/World/RobotArm1_8/link1/visuals
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/visuals/link1'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.194, 0.232, 0.329)'
   *   Center: '(17.500, 29.002, 0.627)'


---


### /World/RobotArm1_8/link1/collisions
*  **Prim路径 (Prim Path):**/World/RobotArm1_8/link1/collisions
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/colliders/link1'
*  **世界包围盒 (World BBox):**
   *   Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
   *   Center: '(17.500, 29.000, 0.694)'
*  **物理属性 (Physics):**
   *   **Collider:** True


---


### /World/RobotArm1_8/link2/visuals
*  **Prim路径 (Prim Path):**/World/RobotArm1_8/link2/visuals
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/visuals/link2'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.194, 0.326, 0.463)'
   *   Center: '(17.500, 29.074, 0.828)'


---


### /World/RobotArm1_8/link2/collisions
*  **Prim路径 (Prim Path):**/World/RobotArm1_8/link2/collisions
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/colliders/link2'
*  **世界包围盒 (World BBox):**
   *   Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
   *   Center: '(17.500, 29.000, 0.694)'
*  **物理属性 (Physics):**
   *   **Collider:** True


---


### /World/RobotArm1_8/link3/visuals
*  **Prim路径 (Prim Path):**/World/RobotArm1_8/link3/visuals
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/visuals/link3'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.283, 0.229, 0.309)'
   *   Center: '(17.552, 29.023, 1.215)'


---


### /World/RobotArm1_8/link3/collisions
*  **Prim路径 (Prim Path):**/World/RobotArm1_8/link3/collisions
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/colliders/link3'
*  **世界包围盒 (World BBox):**
   *   Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
   *   Center: '(17.500, 29.000, 1.280)'
*  **物理属性 (Physics):**
   *   **Collider:** True


---


### /World/RobotArm1_8/link4/visuals
*  **Prim路径 (Prim Path):**/World/RobotArm1_8/link4/visuals
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/visuals/link4'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.334, 0.308, 0.414)'
   *   Center: '(17.683, 28.936, 1.162)'


---


### /World/RobotArm1_8/link4/collisions
*  **Prim路径 (Prim Path):**/World/RobotArm1_8/link4/collisions
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/colliders/link4'
*  **世界包围盒 (World BBox):**
   *   Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
   *   Center: '(17.605, 29.000, 1.280)'
*  **物理属性 (Physics):**
   *   **Collider:** True


---


### /World/RobotArm1_8/link5/visuals
*  **Prim路径 (Prim Path):**/World/RobotArm1_8/link5/visuals
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/visuals/link5'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.180, 0.262, 0.440)'
   *   Center: '(17.760, 28.959, 0.738)'


---


### /World/RobotArm1_8/link5/collisions
*  **Prim路径 (Prim Path):**/World/RobotArm1_8/link5/collisions
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/colliders/link5'
*  **世界包围盒 (World BBox):**
   *   Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
   *   Center: '(17.760, 29.000, 0.595)'
*  **物理属性 (Physics):**
   *   **Collider:** True


---


### /World/RobotArm1_8/link6/visuals
*  **Prim路径 (Prim Path):**/World/RobotArm1_8/link6/visuals
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/visuals/link6'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.307, 0.200, 0.212)'
   *   Center: '(17.836, 29.022, 0.566)'


---


### /World/RobotArm1_8/link6/collisions
*  **Prim路径 (Prim Path):**/World/RobotArm1_8/link6/collisions
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/colliders/link6'
*  **世界包围盒 (World BBox):**
   *   Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
   *   Center: '(17.760, 29.000, 0.595)'
*  **物理属性 (Physics):**
   *   **Collider:** True


---


### /World/RobotArm1_8/link7/visuals
*  **Prim路径 (Prim Path):**/World/RobotArm1_8/link7/visuals
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/visuals/link7'
*  **世界包围盒 (World BBox):**
   *   Size: '(0.156, 0.186, 0.066)'
   *   Center: '(17.912, 29.015, 0.434)'


---


### /World/RobotArm1_8/link7/collisions
*  **Prim路径 (Prim Path):**/World/RobotArm1_8/link7/collisions
*  **Prim类型 (Prim Type):**Xform
*  **变换信息 (Transform):**
   *   **平移 (Translate):**'(0.000, 0.000, 0.000)'
   *   **旋转 (Rotate XYZ, Degrees):**'(0.000, 0.000, 0.000)'
   *   **缩放 (Scale):**'(1.000, 1.000, 1.000)'
*  **外部引用 (Referenced USD Files):**
       *   [reference] 'Reference 1'
       *   Prim Path: '/colliders/link7'
*  **世界包围盒 (World BBox):**
   *   Size: '(-680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000, -680564693277057719623408366969033850880.000)'
   *   Center: '(17.912, 29.000, 0.401)'
*  **物理属性 (Physics):**
   *   **Collider:** True


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


### /World/RobotArm_1/Looks/material_Black
*  **Prim路径 (Prim Path):**/World/RobotArm_1/Looks/material_Black
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/RobotArm_1/Looks/material_Black/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/RobotArm_1/Looks/material_Black/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.000, 0.000, 0.000)'


---


### /World/RobotArm_1/Looks/material_White
*  **Prim路径 (Prim Path):**/World/RobotArm_1/Looks/material_White
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/RobotArm_1/Looks/material_White/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/RobotArm_1/Looks/material_White/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(1.000, 1.000, 1.000)'


---


### /World/RobotArm_1/Looks/material_CCCCCC
*  **Prim路径 (Prim Path):**/World/RobotArm_1/Looks/material_CCCCCC
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/RobotArm_1/Looks/material_CCCCCC/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/RobotArm_1/Looks/material_CCCCCC/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.800, 0.800, 0.800)'


---


### /World/RobotArm_1/Looks/material_191919
*  **Prim路径 (Prim Path):**/World/RobotArm_1/Looks/material_191919
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/RobotArm_1/Looks/material_191919/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/RobotArm_1/Looks/material_191919/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.100, 0.100, 0.100)'


---


### /World/RobotArm_2/Looks/material_Black
*  **Prim路径 (Prim Path):**/World/RobotArm_2/Looks/material_Black
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/RobotArm_2/Looks/material_Black/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/RobotArm_2/Looks/material_Black/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.000, 0.000, 0.000)'


---


### /World/RobotArm_2/Looks/material_White
*  **Prim路径 (Prim Path):**/World/RobotArm_2/Looks/material_White
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/RobotArm_2/Looks/material_White/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/RobotArm_2/Looks/material_White/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(1.000, 1.000, 1.000)'


---


### /World/RobotArm_2/Looks/material_CCCCCC
*  **Prim路径 (Prim Path):**/World/RobotArm_2/Looks/material_CCCCCC
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/RobotArm_2/Looks/material_CCCCCC/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/RobotArm_2/Looks/material_CCCCCC/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.800, 0.800, 0.800)'


---


### /World/RobotArm_2/Looks/material_191919
*  **Prim路径 (Prim Path):**/World/RobotArm_2/Looks/material_191919
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/RobotArm_2/Looks/material_191919/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/RobotArm_2/Looks/material_191919/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.100, 0.100, 0.100)'


---


### /World/RobotArm_3/Looks/material_Black
*  **Prim路径 (Prim Path):**/World/RobotArm_3/Looks/material_Black
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/RobotArm_3/Looks/material_Black/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/RobotArm_3/Looks/material_Black/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.000, 0.000, 0.000)'


---


### /World/RobotArm_3/Looks/material_White
*  **Prim路径 (Prim Path):**/World/RobotArm_3/Looks/material_White
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/RobotArm_3/Looks/material_White/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/RobotArm_3/Looks/material_White/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(1.000, 1.000, 1.000)'


---


### /World/RobotArm_3/Looks/material_CCCCCC
*  **Prim路径 (Prim Path):**/World/RobotArm_3/Looks/material_CCCCCC
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/RobotArm_3/Looks/material_CCCCCC/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/RobotArm_3/Looks/material_CCCCCC/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.800, 0.800, 0.800)'


---


### /World/RobotArm_3/Looks/material_191919
*  **Prim路径 (Prim Path):**/World/RobotArm_3/Looks/material_191919
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/RobotArm_3/Looks/material_191919/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/RobotArm_3/Looks/material_191919/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.100, 0.100, 0.100)'


---


### /World/RobotArm_4/Looks/material_Black
*  **Prim路径 (Prim Path):**/World/RobotArm_4/Looks/material_Black
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/RobotArm_4/Looks/material_Black/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/RobotArm_4/Looks/material_Black/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.000, 0.000, 0.000)'


---


### /World/RobotArm_4/Looks/material_White
*  **Prim路径 (Prim Path):**/World/RobotArm_4/Looks/material_White
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/RobotArm_4/Looks/material_White/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/RobotArm_4/Looks/material_White/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(1.000, 1.000, 1.000)'


---


### /World/RobotArm_4/Looks/material_CCCCCC
*  **Prim路径 (Prim Path):**/World/RobotArm_4/Looks/material_CCCCCC
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/RobotArm_4/Looks/material_CCCCCC/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/RobotArm_4/Looks/material_CCCCCC/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.800, 0.800, 0.800)'


---


### /World/RobotArm_4/Looks/material_191919
*  **Prim路径 (Prim Path):**/World/RobotArm_4/Looks/material_191919
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/RobotArm_4/Looks/material_191919/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/RobotArm_4/Looks/material_191919/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.100, 0.100, 0.100)'


---


### /World/RobotArm_5/Looks/material_Black
*  **Prim路径 (Prim Path):**/World/RobotArm_5/Looks/material_Black
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/RobotArm_5/Looks/material_Black/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/RobotArm_5/Looks/material_Black/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.000, 0.000, 0.000)'


---


### /World/RobotArm_5/Looks/material_White
*  **Prim路径 (Prim Path):**/World/RobotArm_5/Looks/material_White
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/RobotArm_5/Looks/material_White/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/RobotArm_5/Looks/material_White/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(1.000, 1.000, 1.000)'


---


### /World/RobotArm_5/Looks/material_CCCCCC
*  **Prim路径 (Prim Path):**/World/RobotArm_5/Looks/material_CCCCCC
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/RobotArm_5/Looks/material_CCCCCC/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/RobotArm_5/Looks/material_CCCCCC/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.800, 0.800, 0.800)'


---


### /World/RobotArm_5/Looks/material_191919
*  **Prim路径 (Prim Path):**/World/RobotArm_5/Looks/material_191919
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/RobotArm_5/Looks/material_191919/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/RobotArm_5/Looks/material_191919/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.100, 0.100, 0.100)'


---


### /World/RobotArm_6/Looks/material_Black
*  **Prim路径 (Prim Path):**/World/RobotArm_6/Looks/material_Black
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/RobotArm_6/Looks/material_Black/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/RobotArm_6/Looks/material_Black/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.000, 0.000, 0.000)'


---


### /World/RobotArm_6/Looks/material_White
*  **Prim路径 (Prim Path):**/World/RobotArm_6/Looks/material_White
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/RobotArm_6/Looks/material_White/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/RobotArm_6/Looks/material_White/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(1.000, 1.000, 1.000)'


---


### /World/RobotArm_6/Looks/material_CCCCCC
*  **Prim路径 (Prim Path):**/World/RobotArm_6/Looks/material_CCCCCC
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/RobotArm_6/Looks/material_CCCCCC/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/RobotArm_6/Looks/material_CCCCCC/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.800, 0.800, 0.800)'


---


### /World/RobotArm_6/Looks/material_191919
*  **Prim路径 (Prim Path):**/World/RobotArm_6/Looks/material_191919
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/RobotArm_6/Looks/material_191919/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/RobotArm_6/Looks/material_191919/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.100, 0.100, 0.100)'


---


### /World/RobotArm_7/Looks/material_Black
*  **Prim路径 (Prim Path):**/World/RobotArm_7/Looks/material_Black
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/RobotArm_7/Looks/material_Black/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/RobotArm_7/Looks/material_Black/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.000, 0.000, 0.000)'


---


### /World/RobotArm_7/Looks/material_White
*  **Prim路径 (Prim Path):**/World/RobotArm_7/Looks/material_White
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/RobotArm_7/Looks/material_White/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/RobotArm_7/Looks/material_White/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(1.000, 1.000, 1.000)'


---


### /World/RobotArm_7/Looks/material_CCCCCC
*  **Prim路径 (Prim Path):**/World/RobotArm_7/Looks/material_CCCCCC
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/RobotArm_7/Looks/material_CCCCCC/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/RobotArm_7/Looks/material_CCCCCC/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.800, 0.800, 0.800)'


---


### /World/RobotArm_7/Looks/material_191919
*  **Prim路径 (Prim Path):**/World/RobotArm_7/Looks/material_191919
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/RobotArm_7/Looks/material_191919/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/RobotArm_7/Looks/material_191919/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.100, 0.100, 0.100)'


---


### /World/RobotArm_8/Looks/material_Black
*  **Prim路径 (Prim Path):**/World/RobotArm_8/Looks/material_Black
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/RobotArm_8/Looks/material_Black/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/RobotArm_8/Looks/material_Black/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.000, 0.000, 0.000)'


---


### /World/RobotArm_8/Looks/material_White
*  **Prim路径 (Prim Path):**/World/RobotArm_8/Looks/material_White
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/RobotArm_8/Looks/material_White/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/RobotArm_8/Looks/material_White/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(1.000, 1.000, 1.000)'


---


### /World/RobotArm_8/Looks/material_CCCCCC
*  **Prim路径 (Prim Path):**/World/RobotArm_8/Looks/material_CCCCCC
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/RobotArm_8/Looks/material_CCCCCC/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/RobotArm_8/Looks/material_CCCCCC/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.800, 0.800, 0.800)'


---


### /World/RobotArm_8/Looks/material_191919
*  **Prim路径 (Prim Path):**/World/RobotArm_8/Looks/material_191919
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/RobotArm_8/Looks/material_191919/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/RobotArm_8/Looks/material_191919/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.100, 0.100, 0.100)'


---


### /World/RobotArm1_1/gripper/Looks/DefaultMaterial
*  **Prim路径 (Prim Path):**/World/RobotArm1_1/gripper/Looks/DefaultMaterial
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/RobotArm1_1/gripper/Looks/DefaultMaterial/DefaultMaterial'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/RobotArm1_1/gripper/Looks/DefaultMaterial/DefaultMaterial'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(1.000, 1.000, 1.000)'
           *   'emissive_color' [color3f] = '(1.000, 1.000, 1.000)'
           *   'emissive_intensity' [float] = '10000'
           *   'opacity_constant' [float] = '1'
           *   'opacity_threshold' [float] = '0'
           *   'texture_rotate' [float] = '0'
           *   'texture_scale' [float2] = '(1.000, 1.000)'
           *   'texture_translate' [float2] = '(0.000, 0.000)'


---


### /World/RobotArm1_1/gripper/Looks/j____________
*  **Prim路径 (Prim Path):**/World/RobotArm1_1/gripper/Looks/j____________
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/RobotArm1_1/gripper/Looks/j____________/j____________'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/RobotArm1_1/gripper/Looks/j____________/j____________'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.000, 0.000, 0.000)'
           *   'emissive_color' [color3f] = '(1.000, 1.000, 1.000)'
           *   'emissive_intensity' [float] = '10000'
           *   'opacity_constant' [float] = '1'
           *   'opacity_threshold' [float] = '0'
           *   'texture_rotate' [float] = '0'
           *   'texture_scale' [float2] = '(1.000, 1.000)'
           *   'texture_translate' [float2] = '(0.000, 0.000)'


---


### /World/RobotArm1_1/Looks/material_Black
*  **Prim路径 (Prim Path):**/World/RobotArm1_1/Looks/material_Black
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/RobotArm1_1/Looks/material_Black/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/RobotArm1_1/Looks/material_Black/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.000, 0.000, 0.000)'


---


### /World/RobotArm1_1/Looks/material_Red
*  **Prim路径 (Prim Path):**/World/RobotArm1_1/Looks/material_Red
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/RobotArm1_1/Looks/material_Red/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/RobotArm1_1/Looks/material_Red/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.800, 0.000, 0.000)'


---


### /World/RobotArm1_1/Looks/material_Silver
*  **Prim路径 (Prim Path):**/World/RobotArm1_1/Looks/material_Silver
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/RobotArm1_1/Looks/material_Silver/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/RobotArm1_1/Looks/material_Silver/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.753, 0.753, 0.753)'


---


### /World/RobotArm1_1/Looks/material_White
*  **Prim路径 (Prim Path):**/World/RobotArm1_1/Looks/material_White
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/RobotArm1_1/Looks/material_White/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/RobotArm1_1/Looks/material_White/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(1.000, 1.000, 1.000)'


---


### /World/RobotArm1_1/Looks/material_______________
*  **Prim路径 (Prim Path):**/World/RobotArm1_1/Looks/material_______________
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/RobotArm1_1/Looks/material_______________/material_______________'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/RobotArm1_1/Looks/material_______________/material_______________'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.500, 0.500, 0.500)'
           *   'emissive_color' [color3f] = '(1.000, 1.000, 1.000)'
           *   'emissive_intensity' [float] = '10000'
           *   'opacity_constant' [float] = '1'
           *   'opacity_threshold' [float] = '0'
           *   'texture_rotate' [float] = '0'
           *   'texture_scale' [float2] = '(1.000, 1.000)'
           *   'texture_translate' [float2] = '(0.000, 0.000)'


---


### /World/RobotArm1_1/Looks/material____________
*  **Prim路径 (Prim Path):**/World/RobotArm1_1/Looks/material____________
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/RobotArm1_1/Looks/material____________/material____________'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/RobotArm1_1/Looks/material____________/material____________'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(1.000, 1.000, 1.000)'
           *   'emissive_color' [color3f] = '(1.000, 1.000, 1.000)'
           *   'emissive_intensity' [float] = '10000'
           *   'opacity_constant' [float] = '1'
           *   'opacity_threshold' [float] = '0'
           *   'texture_rotate' [float] = '0'
           *   'texture_scale' [float2] = '(1.000, 1.000)'
           *   'texture_translate' [float2] = '(0.000, 0.000)'


---


### /World/RobotArm1_2/gripper/Looks/DefaultMaterial
*  **Prim路径 (Prim Path):**/World/RobotArm1_2/gripper/Looks/DefaultMaterial
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/RobotArm1_2/gripper/Looks/DefaultMaterial/DefaultMaterial'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/RobotArm1_2/gripper/Looks/DefaultMaterial/DefaultMaterial'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(1.000, 1.000, 1.000)'
           *   'emissive_color' [color3f] = '(1.000, 1.000, 1.000)'
           *   'emissive_intensity' [float] = '10000'
           *   'opacity_constant' [float] = '1'
           *   'opacity_threshold' [float] = '0'
           *   'texture_rotate' [float] = '0'
           *   'texture_scale' [float2] = '(1.000, 1.000)'
           *   'texture_translate' [float2] = '(0.000, 0.000)'


---


### /World/RobotArm1_2/gripper/Looks/j____________
*  **Prim路径 (Prim Path):**/World/RobotArm1_2/gripper/Looks/j____________
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/RobotArm1_2/gripper/Looks/j____________/j____________'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/RobotArm1_2/gripper/Looks/j____________/j____________'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.000, 0.000, 0.000)'
           *   'emissive_color' [color3f] = '(1.000, 1.000, 1.000)'
           *   'emissive_intensity' [float] = '10000'
           *   'opacity_constant' [float] = '1'
           *   'opacity_threshold' [float] = '0'
           *   'texture_rotate' [float] = '0'
           *   'texture_scale' [float2] = '(1.000, 1.000)'
           *   'texture_translate' [float2] = '(0.000, 0.000)'


---


### /World/RobotArm1_2/Looks/material_Black
*  **Prim路径 (Prim Path):**/World/RobotArm1_2/Looks/material_Black
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/RobotArm1_2/Looks/material_Black/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/RobotArm1_2/Looks/material_Black/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.000, 0.000, 0.000)'


---


### /World/RobotArm1_2/Looks/material_Red
*  **Prim路径 (Prim Path):**/World/RobotArm1_2/Looks/material_Red
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/RobotArm1_2/Looks/material_Red/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/RobotArm1_2/Looks/material_Red/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.800, 0.000, 0.000)'


---


### /World/RobotArm1_2/Looks/material_Silver
*  **Prim路径 (Prim Path):**/World/RobotArm1_2/Looks/material_Silver
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/RobotArm1_2/Looks/material_Silver/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/RobotArm1_2/Looks/material_Silver/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.753, 0.753, 0.753)'


---


### /World/RobotArm1_2/Looks/material_White
*  **Prim路径 (Prim Path):**/World/RobotArm1_2/Looks/material_White
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/RobotArm1_2/Looks/material_White/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/RobotArm1_2/Looks/material_White/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(1.000, 1.000, 1.000)'


---


### /World/RobotArm1_2/Looks/material_______________
*  **Prim路径 (Prim Path):**/World/RobotArm1_2/Looks/material_______________
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/RobotArm1_2/Looks/material_______________/material_______________'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/RobotArm1_2/Looks/material_______________/material_______________'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.500, 0.500, 0.500)'
           *   'emissive_color' [color3f] = '(1.000, 1.000, 1.000)'
           *   'emissive_intensity' [float] = '10000'
           *   'opacity_constant' [float] = '1'
           *   'opacity_threshold' [float] = '0'
           *   'texture_rotate' [float] = '0'
           *   'texture_scale' [float2] = '(1.000, 1.000)'
           *   'texture_translate' [float2] = '(0.000, 0.000)'


---


### /World/RobotArm1_2/Looks/material____________
*  **Prim路径 (Prim Path):**/World/RobotArm1_2/Looks/material____________
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/RobotArm1_2/Looks/material____________/material____________'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/RobotArm1_2/Looks/material____________/material____________'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(1.000, 1.000, 1.000)'
           *   'emissive_color' [color3f] = '(1.000, 1.000, 1.000)'
           *   'emissive_intensity' [float] = '10000'
           *   'opacity_constant' [float] = '1'
           *   'opacity_threshold' [float] = '0'
           *   'texture_rotate' [float] = '0'
           *   'texture_scale' [float2] = '(1.000, 1.000)'
           *   'texture_translate' [float2] = '(0.000, 0.000)'


---


### /World/RobotArm1_3/gripper/Looks/DefaultMaterial
*  **Prim路径 (Prim Path):**/World/RobotArm1_3/gripper/Looks/DefaultMaterial
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/RobotArm1_3/gripper/Looks/DefaultMaterial/DefaultMaterial'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/RobotArm1_3/gripper/Looks/DefaultMaterial/DefaultMaterial'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(1.000, 1.000, 1.000)'
           *   'emissive_color' [color3f] = '(1.000, 1.000, 1.000)'
           *   'emissive_intensity' [float] = '10000'
           *   'opacity_constant' [float] = '1'
           *   'opacity_threshold' [float] = '0'
           *   'texture_rotate' [float] = '0'
           *   'texture_scale' [float2] = '(1.000, 1.000)'
           *   'texture_translate' [float2] = '(0.000, 0.000)'


---


### /World/RobotArm1_3/gripper/Looks/j____________
*  **Prim路径 (Prim Path):**/World/RobotArm1_3/gripper/Looks/j____________
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/RobotArm1_3/gripper/Looks/j____________/j____________'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/RobotArm1_3/gripper/Looks/j____________/j____________'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.000, 0.000, 0.000)'
           *   'emissive_color' [color3f] = '(1.000, 1.000, 1.000)'
           *   'emissive_intensity' [float] = '10000'
           *   'opacity_constant' [float] = '1'
           *   'opacity_threshold' [float] = '0'
           *   'texture_rotate' [float] = '0'
           *   'texture_scale' [float2] = '(1.000, 1.000)'
           *   'texture_translate' [float2] = '(0.000, 0.000)'


---


### /World/RobotArm1_3/Looks/material_Black
*  **Prim路径 (Prim Path):**/World/RobotArm1_3/Looks/material_Black
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/RobotArm1_3/Looks/material_Black/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/RobotArm1_3/Looks/material_Black/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.000, 0.000, 0.000)'


---


### /World/RobotArm1_3/Looks/material_Red
*  **Prim路径 (Prim Path):**/World/RobotArm1_3/Looks/material_Red
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/RobotArm1_3/Looks/material_Red/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/RobotArm1_3/Looks/material_Red/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.800, 0.000, 0.000)'


---


### /World/RobotArm1_3/Looks/material_Silver
*  **Prim路径 (Prim Path):**/World/RobotArm1_3/Looks/material_Silver
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/RobotArm1_3/Looks/material_Silver/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/RobotArm1_3/Looks/material_Silver/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.753, 0.753, 0.753)'


---


### /World/RobotArm1_3/Looks/material_White
*  **Prim路径 (Prim Path):**/World/RobotArm1_3/Looks/material_White
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/RobotArm1_3/Looks/material_White/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/RobotArm1_3/Looks/material_White/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(1.000, 1.000, 1.000)'


---


### /World/RobotArm1_3/Looks/material_______________
*  **Prim路径 (Prim Path):**/World/RobotArm1_3/Looks/material_______________
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/RobotArm1_3/Looks/material_______________/material_______________'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/RobotArm1_3/Looks/material_______________/material_______________'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.500, 0.500, 0.500)'
           *   'emissive_color' [color3f] = '(1.000, 1.000, 1.000)'
           *   'emissive_intensity' [float] = '10000'
           *   'opacity_constant' [float] = '1'
           *   'opacity_threshold' [float] = '0'
           *   'texture_rotate' [float] = '0'
           *   'texture_scale' [float2] = '(1.000, 1.000)'
           *   'texture_translate' [float2] = '(0.000, 0.000)'


---


### /World/RobotArm1_3/Looks/material____________
*  **Prim路径 (Prim Path):**/World/RobotArm1_3/Looks/material____________
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/RobotArm1_3/Looks/material____________/material____________'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/RobotArm1_3/Looks/material____________/material____________'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(1.000, 1.000, 1.000)'
           *   'emissive_color' [color3f] = '(1.000, 1.000, 1.000)'
           *   'emissive_intensity' [float] = '10000'
           *   'opacity_constant' [float] = '1'
           *   'opacity_threshold' [float] = '0'
           *   'texture_rotate' [float] = '0'
           *   'texture_scale' [float2] = '(1.000, 1.000)'
           *   'texture_translate' [float2] = '(0.000, 0.000)'


---


### /World/RobotArm1_4/gripper/Looks/DefaultMaterial
*  **Prim路径 (Prim Path):**/World/RobotArm1_4/gripper/Looks/DefaultMaterial
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/RobotArm1_4/gripper/Looks/DefaultMaterial/DefaultMaterial'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/RobotArm1_4/gripper/Looks/DefaultMaterial/DefaultMaterial'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(1.000, 1.000, 1.000)'
           *   'emissive_color' [color3f] = '(1.000, 1.000, 1.000)'
           *   'emissive_intensity' [float] = '10000'
           *   'opacity_constant' [float] = '1'
           *   'opacity_threshold' [float] = '0'
           *   'texture_rotate' [float] = '0'
           *   'texture_scale' [float2] = '(1.000, 1.000)'
           *   'texture_translate' [float2] = '(0.000, 0.000)'


---


### /World/RobotArm1_4/gripper/Looks/j____________
*  **Prim路径 (Prim Path):**/World/RobotArm1_4/gripper/Looks/j____________
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/RobotArm1_4/gripper/Looks/j____________/j____________'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/RobotArm1_4/gripper/Looks/j____________/j____________'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.000, 0.000, 0.000)'
           *   'emissive_color' [color3f] = '(1.000, 1.000, 1.000)'
           *   'emissive_intensity' [float] = '10000'
           *   'opacity_constant' [float] = '1'
           *   'opacity_threshold' [float] = '0'
           *   'texture_rotate' [float] = '0'
           *   'texture_scale' [float2] = '(1.000, 1.000)'
           *   'texture_translate' [float2] = '(0.000, 0.000)'


---


### /World/RobotArm1_4/Looks/material_Black
*  **Prim路径 (Prim Path):**/World/RobotArm1_4/Looks/material_Black
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/RobotArm1_4/Looks/material_Black/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/RobotArm1_4/Looks/material_Black/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.000, 0.000, 0.000)'


---


### /World/RobotArm1_4/Looks/material_Red
*  **Prim路径 (Prim Path):**/World/RobotArm1_4/Looks/material_Red
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/RobotArm1_4/Looks/material_Red/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/RobotArm1_4/Looks/material_Red/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.800, 0.000, 0.000)'


---


### /World/RobotArm1_4/Looks/material_Silver
*  **Prim路径 (Prim Path):**/World/RobotArm1_4/Looks/material_Silver
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/RobotArm1_4/Looks/material_Silver/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/RobotArm1_4/Looks/material_Silver/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.753, 0.753, 0.753)'


---


### /World/RobotArm1_4/Looks/material_White
*  **Prim路径 (Prim Path):**/World/RobotArm1_4/Looks/material_White
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/RobotArm1_4/Looks/material_White/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/RobotArm1_4/Looks/material_White/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(1.000, 1.000, 1.000)'


---


### /World/RobotArm1_4/Looks/material_______________
*  **Prim路径 (Prim Path):**/World/RobotArm1_4/Looks/material_______________
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/RobotArm1_4/Looks/material_______________/material_______________'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/RobotArm1_4/Looks/material_______________/material_______________'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.500, 0.500, 0.500)'
           *   'emissive_color' [color3f] = '(1.000, 1.000, 1.000)'
           *   'emissive_intensity' [float] = '10000'
           *   'opacity_constant' [float] = '1'
           *   'opacity_threshold' [float] = '0'
           *   'texture_rotate' [float] = '0'
           *   'texture_scale' [float2] = '(1.000, 1.000)'
           *   'texture_translate' [float2] = '(0.000, 0.000)'


---


### /World/RobotArm1_4/Looks/material____________
*  **Prim路径 (Prim Path):**/World/RobotArm1_4/Looks/material____________
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/RobotArm1_4/Looks/material____________/material____________'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/RobotArm1_4/Looks/material____________/material____________'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(1.000, 1.000, 1.000)'
           *   'emissive_color' [color3f] = '(1.000, 1.000, 1.000)'
           *   'emissive_intensity' [float] = '10000'
           *   'opacity_constant' [float] = '1'
           *   'opacity_threshold' [float] = '0'
           *   'texture_rotate' [float] = '0'
           *   'texture_scale' [float2] = '(1.000, 1.000)'
           *   'texture_translate' [float2] = '(0.000, 0.000)'


---


### /World/RobotArm1_5/gripper/Looks/DefaultMaterial
*  **Prim路径 (Prim Path):**/World/RobotArm1_5/gripper/Looks/DefaultMaterial
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/RobotArm1_5/gripper/Looks/DefaultMaterial/DefaultMaterial'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/RobotArm1_5/gripper/Looks/DefaultMaterial/DefaultMaterial'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(1.000, 1.000, 1.000)'
           *   'emissive_color' [color3f] = '(1.000, 1.000, 1.000)'
           *   'emissive_intensity' [float] = '10000'
           *   'opacity_constant' [float] = '1'
           *   'opacity_threshold' [float] = '0'
           *   'texture_rotate' [float] = '0'
           *   'texture_scale' [float2] = '(1.000, 1.000)'
           *   'texture_translate' [float2] = '(0.000, 0.000)'


---


### /World/RobotArm1_5/gripper/Looks/j____________
*  **Prim路径 (Prim Path):**/World/RobotArm1_5/gripper/Looks/j____________
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/RobotArm1_5/gripper/Looks/j____________/j____________'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/RobotArm1_5/gripper/Looks/j____________/j____________'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.000, 0.000, 0.000)'
           *   'emissive_color' [color3f] = '(1.000, 1.000, 1.000)'
           *   'emissive_intensity' [float] = '10000'
           *   'opacity_constant' [float] = '1'
           *   'opacity_threshold' [float] = '0'
           *   'texture_rotate' [float] = '0'
           *   'texture_scale' [float2] = '(1.000, 1.000)'
           *   'texture_translate' [float2] = '(0.000, 0.000)'


---


### /World/RobotArm1_5/Looks/material_Black
*  **Prim路径 (Prim Path):**/World/RobotArm1_5/Looks/material_Black
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/RobotArm1_5/Looks/material_Black/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/RobotArm1_5/Looks/material_Black/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.000, 0.000, 0.000)'


---


### /World/RobotArm1_5/Looks/material_Red
*  **Prim路径 (Prim Path):**/World/RobotArm1_5/Looks/material_Red
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/RobotArm1_5/Looks/material_Red/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/RobotArm1_5/Looks/material_Red/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.800, 0.000, 0.000)'


---


### /World/RobotArm1_5/Looks/material_Silver
*  **Prim路径 (Prim Path):**/World/RobotArm1_5/Looks/material_Silver
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/RobotArm1_5/Looks/material_Silver/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/RobotArm1_5/Looks/material_Silver/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.753, 0.753, 0.753)'


---


### /World/RobotArm1_5/Looks/material_White
*  **Prim路径 (Prim Path):**/World/RobotArm1_5/Looks/material_White
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/RobotArm1_5/Looks/material_White/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/RobotArm1_5/Looks/material_White/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(1.000, 1.000, 1.000)'


---


### /World/RobotArm1_5/Looks/material_______________
*  **Prim路径 (Prim Path):**/World/RobotArm1_5/Looks/material_______________
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/RobotArm1_5/Looks/material_______________/material_______________'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/RobotArm1_5/Looks/material_______________/material_______________'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.500, 0.500, 0.500)'
           *   'emissive_color' [color3f] = '(1.000, 1.000, 1.000)'
           *   'emissive_intensity' [float] = '10000'
           *   'opacity_constant' [float] = '1'
           *   'opacity_threshold' [float] = '0'
           *   'texture_rotate' [float] = '0'
           *   'texture_scale' [float2] = '(1.000, 1.000)'
           *   'texture_translate' [float2] = '(0.000, 0.000)'


---


### /World/RobotArm1_5/Looks/material____________
*  **Prim路径 (Prim Path):**/World/RobotArm1_5/Looks/material____________
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/RobotArm1_5/Looks/material____________/material____________'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/RobotArm1_5/Looks/material____________/material____________'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(1.000, 1.000, 1.000)'
           *   'emissive_color' [color3f] = '(1.000, 1.000, 1.000)'
           *   'emissive_intensity' [float] = '10000'
           *   'opacity_constant' [float] = '1'
           *   'opacity_threshold' [float] = '0'
           *   'texture_rotate' [float] = '0'
           *   'texture_scale' [float2] = '(1.000, 1.000)'
           *   'texture_translate' [float2] = '(0.000, 0.000)'


---


### /World/RobotArm1_6/gripper/Looks/DefaultMaterial
*  **Prim路径 (Prim Path):**/World/RobotArm1_6/gripper/Looks/DefaultMaterial
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/RobotArm1_6/gripper/Looks/DefaultMaterial/DefaultMaterial'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/RobotArm1_6/gripper/Looks/DefaultMaterial/DefaultMaterial'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(1.000, 1.000, 1.000)'
           *   'emissive_color' [color3f] = '(1.000, 1.000, 1.000)'
           *   'emissive_intensity' [float] = '10000'
           *   'opacity_constant' [float] = '1'
           *   'opacity_threshold' [float] = '0'
           *   'texture_rotate' [float] = '0'
           *   'texture_scale' [float2] = '(1.000, 1.000)'
           *   'texture_translate' [float2] = '(0.000, 0.000)'


---


### /World/RobotArm1_6/gripper/Looks/j____________
*  **Prim路径 (Prim Path):**/World/RobotArm1_6/gripper/Looks/j____________
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/RobotArm1_6/gripper/Looks/j____________/j____________'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/RobotArm1_6/gripper/Looks/j____________/j____________'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.000, 0.000, 0.000)'
           *   'emissive_color' [color3f] = '(1.000, 1.000, 1.000)'
           *   'emissive_intensity' [float] = '10000'
           *   'opacity_constant' [float] = '1'
           *   'opacity_threshold' [float] = '0'
           *   'texture_rotate' [float] = '0'
           *   'texture_scale' [float2] = '(1.000, 1.000)'
           *   'texture_translate' [float2] = '(0.000, 0.000)'


---


### /World/RobotArm1_6/Looks/material_Black
*  **Prim路径 (Prim Path):**/World/RobotArm1_6/Looks/material_Black
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/RobotArm1_6/Looks/material_Black/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/RobotArm1_6/Looks/material_Black/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.000, 0.000, 0.000)'


---


### /World/RobotArm1_6/Looks/material_Red
*  **Prim路径 (Prim Path):**/World/RobotArm1_6/Looks/material_Red
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/RobotArm1_6/Looks/material_Red/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/RobotArm1_6/Looks/material_Red/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.800, 0.000, 0.000)'


---


### /World/RobotArm1_6/Looks/material_Silver
*  **Prim路径 (Prim Path):**/World/RobotArm1_6/Looks/material_Silver
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/RobotArm1_6/Looks/material_Silver/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/RobotArm1_6/Looks/material_Silver/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.753, 0.753, 0.753)'


---


### /World/RobotArm1_6/Looks/material_White
*  **Prim路径 (Prim Path):**/World/RobotArm1_6/Looks/material_White
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/RobotArm1_6/Looks/material_White/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/RobotArm1_6/Looks/material_White/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(1.000, 1.000, 1.000)'


---


### /World/RobotArm1_6/Looks/material_______________
*  **Prim路径 (Prim Path):**/World/RobotArm1_6/Looks/material_______________
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/RobotArm1_6/Looks/material_______________/material_______________'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/RobotArm1_6/Looks/material_______________/material_______________'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.500, 0.500, 0.500)'
           *   'emissive_color' [color3f] = '(1.000, 1.000, 1.000)'
           *   'emissive_intensity' [float] = '10000'
           *   'opacity_constant' [float] = '1'
           *   'opacity_threshold' [float] = '0'
           *   'texture_rotate' [float] = '0'
           *   'texture_scale' [float2] = '(1.000, 1.000)'
           *   'texture_translate' [float2] = '(0.000, 0.000)'


---


### /World/RobotArm1_6/Looks/material____________
*  **Prim路径 (Prim Path):**/World/RobotArm1_6/Looks/material____________
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/RobotArm1_6/Looks/material____________/material____________'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/RobotArm1_6/Looks/material____________/material____________'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(1.000, 1.000, 1.000)'
           *   'emissive_color' [color3f] = '(1.000, 1.000, 1.000)'
           *   'emissive_intensity' [float] = '10000'
           *   'opacity_constant' [float] = '1'
           *   'opacity_threshold' [float] = '0'
           *   'texture_rotate' [float] = '0'
           *   'texture_scale' [float2] = '(1.000, 1.000)'
           *   'texture_translate' [float2] = '(0.000, 0.000)'


---


### /World/RobotArm1_7/gripper/Looks/DefaultMaterial
*  **Prim路径 (Prim Path):**/World/RobotArm1_7/gripper/Looks/DefaultMaterial
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/RobotArm1_7/gripper/Looks/DefaultMaterial/DefaultMaterial'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/RobotArm1_7/gripper/Looks/DefaultMaterial/DefaultMaterial'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(1.000, 1.000, 1.000)'
           *   'emissive_color' [color3f] = '(1.000, 1.000, 1.000)'
           *   'emissive_intensity' [float] = '10000'
           *   'opacity_constant' [float] = '1'
           *   'opacity_threshold' [float] = '0'
           *   'texture_rotate' [float] = '0'
           *   'texture_scale' [float2] = '(1.000, 1.000)'
           *   'texture_translate' [float2] = '(0.000, 0.000)'


---


### /World/RobotArm1_7/gripper/Looks/j____________
*  **Prim路径 (Prim Path):**/World/RobotArm1_7/gripper/Looks/j____________
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/RobotArm1_7/gripper/Looks/j____________/j____________'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/RobotArm1_7/gripper/Looks/j____________/j____________'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.000, 0.000, 0.000)'
           *   'emissive_color' [color3f] = '(1.000, 1.000, 1.000)'
           *   'emissive_intensity' [float] = '10000'
           *   'opacity_constant' [float] = '1'
           *   'opacity_threshold' [float] = '0'
           *   'texture_rotate' [float] = '0'
           *   'texture_scale' [float2] = '(1.000, 1.000)'
           *   'texture_translate' [float2] = '(0.000, 0.000)'


---


### /World/RobotArm1_7/Looks/material_Black
*  **Prim路径 (Prim Path):**/World/RobotArm1_7/Looks/material_Black
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/RobotArm1_7/Looks/material_Black/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/RobotArm1_7/Looks/material_Black/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.000, 0.000, 0.000)'


---


### /World/RobotArm1_7/Looks/material_Red
*  **Prim路径 (Prim Path):**/World/RobotArm1_7/Looks/material_Red
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/RobotArm1_7/Looks/material_Red/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/RobotArm1_7/Looks/material_Red/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.800, 0.000, 0.000)'


---


### /World/RobotArm1_7/Looks/material_Silver
*  **Prim路径 (Prim Path):**/World/RobotArm1_7/Looks/material_Silver
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/RobotArm1_7/Looks/material_Silver/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/RobotArm1_7/Looks/material_Silver/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.753, 0.753, 0.753)'


---


### /World/RobotArm1_7/Looks/material_White
*  **Prim路径 (Prim Path):**/World/RobotArm1_7/Looks/material_White
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/RobotArm1_7/Looks/material_White/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/RobotArm1_7/Looks/material_White/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(1.000, 1.000, 1.000)'


---


### /World/RobotArm1_7/Looks/material_______________
*  **Prim路径 (Prim Path):**/World/RobotArm1_7/Looks/material_______________
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/RobotArm1_7/Looks/material_______________/material_______________'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/RobotArm1_7/Looks/material_______________/material_______________'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.500, 0.500, 0.500)'
           *   'emissive_color' [color3f] = '(1.000, 1.000, 1.000)'
           *   'emissive_intensity' [float] = '10000'
           *   'opacity_constant' [float] = '1'
           *   'opacity_threshold' [float] = '0'
           *   'texture_rotate' [float] = '0'
           *   'texture_scale' [float2] = '(1.000, 1.000)'
           *   'texture_translate' [float2] = '(0.000, 0.000)'


---


### /World/RobotArm1_7/Looks/material____________
*  **Prim路径 (Prim Path):**/World/RobotArm1_7/Looks/material____________
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/RobotArm1_7/Looks/material____________/material____________'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/RobotArm1_7/Looks/material____________/material____________'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(1.000, 1.000, 1.000)'
           *   'emissive_color' [color3f] = '(1.000, 1.000, 1.000)'
           *   'emissive_intensity' [float] = '10000'
           *   'opacity_constant' [float] = '1'
           *   'opacity_threshold' [float] = '0'
           *   'texture_rotate' [float] = '0'
           *   'texture_scale' [float2] = '(1.000, 1.000)'
           *   'texture_translate' [float2] = '(0.000, 0.000)'


---


### /World/RobotArm1_8/gripper/Looks/DefaultMaterial
*  **Prim路径 (Prim Path):**/World/RobotArm1_8/gripper/Looks/DefaultMaterial
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/RobotArm1_8/gripper/Looks/DefaultMaterial/DefaultMaterial'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/RobotArm1_8/gripper/Looks/DefaultMaterial/DefaultMaterial'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(1.000, 1.000, 1.000)'
           *   'emissive_color' [color3f] = '(1.000, 1.000, 1.000)'
           *   'emissive_intensity' [float] = '10000'
           *   'opacity_constant' [float] = '1'
           *   'opacity_threshold' [float] = '0'
           *   'texture_rotate' [float] = '0'
           *   'texture_scale' [float2] = '(1.000, 1.000)'
           *   'texture_translate' [float2] = '(0.000, 0.000)'


---


### /World/RobotArm1_8/gripper/Looks/j____________
*  **Prim路径 (Prim Path):**/World/RobotArm1_8/gripper/Looks/j____________
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/RobotArm1_8/gripper/Looks/j____________/j____________'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/RobotArm1_8/gripper/Looks/j____________/j____________'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.000, 0.000, 0.000)'
           *   'emissive_color' [color3f] = '(1.000, 1.000, 1.000)'
           *   'emissive_intensity' [float] = '10000'
           *   'opacity_constant' [float] = '1'
           *   'opacity_threshold' [float] = '0'
           *   'texture_rotate' [float] = '0'
           *   'texture_scale' [float2] = '(1.000, 1.000)'
           *   'texture_translate' [float2] = '(0.000, 0.000)'


---


### /World/RobotArm1_8/Looks/material_Black
*  **Prim路径 (Prim Path):**/World/RobotArm1_8/Looks/material_Black
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/RobotArm1_8/Looks/material_Black/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/RobotArm1_8/Looks/material_Black/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.000, 0.000, 0.000)'


---


### /World/RobotArm1_8/Looks/material_Red
*  **Prim路径 (Prim Path):**/World/RobotArm1_8/Looks/material_Red
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/RobotArm1_8/Looks/material_Red/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/RobotArm1_8/Looks/material_Red/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.800, 0.000, 0.000)'


---


### /World/RobotArm1_8/Looks/material_Silver
*  **Prim路径 (Prim Path):**/World/RobotArm1_8/Looks/material_Silver
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/RobotArm1_8/Looks/material_Silver/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/RobotArm1_8/Looks/material_Silver/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.753, 0.753, 0.753)'


---


### /World/RobotArm1_8/Looks/material_White
*  **Prim路径 (Prim Path):**/World/RobotArm1_8/Looks/material_White
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/RobotArm1_8/Looks/material_White/Shader'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/RobotArm1_8/Looks/material_White/Shader'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(1.000, 1.000, 1.000)'


---


### /World/RobotArm1_8/Looks/material_______________
*  **Prim路径 (Prim Path):**/World/RobotArm1_8/Looks/material_______________
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/RobotArm1_8/Looks/material_______________/material_______________'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/RobotArm1_8/Looks/material_______________/material_______________'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(0.500, 0.500, 0.500)'
           *   'emissive_color' [color3f] = '(1.000, 1.000, 1.000)'
           *   'emissive_intensity' [float] = '10000'
           *   'opacity_constant' [float] = '1'
           *   'opacity_threshold' [float] = '0'
           *   'texture_rotate' [float] = '0'
           *   'texture_scale' [float2] = '(1.000, 1.000)'
           *   'texture_translate' [float2] = '(0.000, 0.000)'


---


### /World/RobotArm1_8/Looks/material____________
*  **Prim路径 (Prim Path):**/World/RobotArm1_8/Looks/material____________
*  **Prim类型 (Prim Type):**Material
*  **材质网络 (Material & Shader Details):**
   *   **Surface Outputs:**
       *   'outputs:surface'
       *   'outputs:mdl:surface' -> '/World/RobotArm1_8/Looks/material____________/material____________'
       *   Connection: 'out' (Output)'
   *   **Shader 节点 (Shader Nodes):**
       *   '/World/RobotArm1_8/Looks/material____________/material____________'
       *   Implementation: 'sourceAsset'
       *   Source Assets:
           *   [mdl] 'OmniPBR.mdl' (Sub Id: 'OmniPBR')
       *   Inputs:
           *   'diffuse_color_constant' [color3f] = '(1.000, 1.000, 1.000)'
           *   'emissive_color' [color3f] = '(1.000, 1.000, 1.000)'
           *   'emissive_intensity' [float] = '10000'
           *   'opacity_constant' [float] = '1'
           *   'opacity_threshold' [float] = '0'
           *   'texture_rotate' [float] = '0'
           *   'texture_scale' [float2] = '(1.000, 1.000)'
           *   'texture_translate' [float2] = '(0.000, 0.000)'


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
