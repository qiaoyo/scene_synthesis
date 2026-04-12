import argparse
from generator import UsdaDocumentGenerator

def main():
    parser = argparse.ArgumentParser(
        description="Generate a detailed Markdown document from a USDA file."
    )
    parser.add_argument(
        "--input",
        type=str,
        required=True,
        help="Path to the input .usda file."
    )
    parser.add_argument(
        "--output",
        type=str,
        required=True,
        help="Path to the output .md file."
    )
    parser.add_argument(
        "--mode",
        type=str,
        choices=["verbose", "brief"],
        default="verbose",
        help="输出模式: verbose 生成完整文档, brief 生成简略报告."
    )
    args = parser.parse_args()

    try:
        generator = UsdaDocumentGenerator(usda_path=args.input, mode=args.mode)
        generator.write_to_file(output_path=args.output)
    except Exception as e:
        import traceback
        traceback.print_exc()
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
