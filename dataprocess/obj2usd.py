import asyncio
import os

from isaacsim import SimulationApp


async def convert(in_file, out_file, load_materials=False):
    import omni.kit.asset_converter

    def progress_callback(progress, total_steps):
        print(f"Progress: {progress}/{total_steps}")

    converter_context = omni.kit.asset_converter.AssetConverterContext()
    converter_context.ignore_materials = not load_materials

    instance = omni.kit.asset_converter.get_instance()
    task = instance.create_converter_task(in_file, out_file, progress_callback, converter_context)

    while True:
        success = await task.wait_until_finished()
        if success:
            break
        await asyncio.sleep(0.1)
    return success


def asset_convert(folders, max_models=9999, load_materials=True):
    supported_file_formats = ["obj"]   # ✅ 只保留 OBJ
    for folder in folders:
        local_asset_output = folder + "_converted"
        omni.client.create_folder(f"{local_asset_output}")

    for folder in folders:
        print(f"\nConverting folder {folder}...")

        (result, models) = omni.client.list(folder)
        for i, entry in enumerate(models):
            if i >= max_models:
                print(f"max models ({max_models}) reached, exiting conversion")
                break

            model = str(entry.relative_path)
            model_name, ext = os.path.splitext(model)
            model_format = ext[1:].lower()

            if model_format in supported_file_formats:
                input_model_path = folder + "/" + model
                converted_model_path = folder + "_converted/" + model_name + ".usd"

                if not os.path.exists(converted_model_path):
                    print(f"Converting {input_model_path} -> {converted_model_path}")
                    status = asyncio.get_event_loop().run_until_complete(
                        convert(input_model_path, converted_model_path, load_materials)
                    )
                    if not status:
                        print(f"❌ ERROR converting {input_model_path}")
                    else:
                        print(f"✅ Added {converted_model_path}")


if __name__ == "__main__":
    kit = SimulationApp()

    import omni
    from isaacsim.core.utils.extensions import enable_extension

    enable_extension("omni.kit.asset_converter")

    # ✅ 直接在这里定义参数
    folders = [
        "/media/simple/another_Documents/isaacsim_assets/obj-20260107/_Qie_Xiang_Jian/chip key GB",

        # 可以继续添加多个文件夹
    ]
    max_models = 9999
    load_materials = True

    asset_convert(folders, max_models, load_materials)

    kit.close()
