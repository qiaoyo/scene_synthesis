import os
import openpyxl
import csv
import re

DNA_TAG_PATTERN = re.compile(r'(DNA\s*:\s*)D([A-Za-z0-9]+)\(([^()]*)\)')
PLAIN_TAG_PATTERN = re.compile(r'^(\s*)D([A-Za-z0-9]+)\(([^()]*)\)(\s*)$')


def normalize_tag_dna(tag_value):
    if not isinstance(tag_value, str):
        return tag_value

    def format_dna(prefix, subscript, suffix):
        return f"{prefix}D_{{{subscript}}}({suffix})"

    def replace_dna(match):
        prefix = match.group(1)
        subscript = match.group(2)
        suffix = match.group(3)
        return format_dna(prefix, subscript, suffix)

    normalized_tag = DNA_TAG_PATTERN.sub(replace_dna, tag_value)
    if normalized_tag != tag_value:
        return normalized_tag

    plain_match = PLAIN_TAG_PATTERN.fullmatch(tag_value)
    if plain_match:
        leading_space = plain_match.group(1)
        subscript = plain_match.group(2)
        suffix = plain_match.group(3)
        trailing_space = plain_match.group(4)
        return f"{leading_space}{format_dna('', subscript, suffix)}{trailing_space}"

    return tag_value


def find_tag_column_index(header_row):
    for index, header in enumerate(header_row):
        if header is None:
            continue

        normalized_header = str(header).lstrip("\ufeff").strip().lower()
        if normalized_header.startswith("tag"):
            return index

    return None


def xlsx_to_csv_with_subscript(input_folder=".", output_folder="csv_output"):
    """
    批量将xlsx转为csv，并只处理 Tag 列中的 DNA 下标：
    - DNA:DB(a) → DNA:D_{B}(a)
    - DNA:DD(y) → DNA:D_{D}(y)
    """
    os.makedirs(output_folder, exist_ok=True)

    files = sorted(f for f in os.listdir(input_folder) if f.endswith(".xlsx"))

    if not files:
        print("未找到任何 .xlsx 文件")
        return

    print(f"找到 {len(files)} 个xlsx文件，开始批量转换...")

    for filename in files:
        input_path = os.path.join(input_folder, filename)
        output_filename = os.path.splitext(filename)[0] + ".csv"
        output_path = os.path.join(output_folder, output_filename)

        try:
            wb = openpyxl.load_workbook(input_path, data_only=True)
            ws = wb.active
            rows = list(ws.iter_rows(values_only=True))
            wb.close()

            if not rows:
                data = []
                tag_column_index = None
            else:
                data = []
                tag_column_index = find_tag_column_index(rows[0])

            if rows and tag_column_index is None:
                print(f"⚠️ 未在 {filename} 中找到 Tag 列，将按原样导出")

            for row_index, row in enumerate(rows):
                new_row = []
                for column_index, cell in enumerate(row):
                    if cell is None:
                        new_row.append("")
                        continue

                    if row_index > 0 and column_index == tag_column_index:
                        new_row.append(normalize_tag_dna(cell))
                    else:
                        new_row.append(cell)
                data.append(new_row)

            with open(output_path, "w", newline="", encoding="utf-8-sig") as f:
                writer = csv.writer(f)
                writer.writerows(data)

            print(f"✅ 转换成功: {filename} → {output_filename}")

        except Exception as e:
            print(f"❌ 处理失败 {filename}: {str(e)}")

    print("\n🎉 批量转换完成！所有CSV保存在 csv_output 文件夹")

# ====================== 运行 ======================
if __name__ == "__main__":
    # 当前目录下所有xlsx → 自动生成 csv_output 文件夹
    xlsx_to_csv_with_subscript(input_folder="/home/simple/Desktop/Scene-Knowledge/xlsx/1", output_folder="/home/simple/Desktop/Scene-Knowledge/xlsx/1/csv_output")
