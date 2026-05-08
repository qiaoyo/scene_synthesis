import os
import csv

def clean_csv_preserve_format(folder_path):
    """
    清理CSV：删除空行 + 删除空列
    【严格保持原格式】，不会破坏分列
    """
    if not os.path.isdir(folder_path):
        print(f"文件夹不存在：{folder_path}")
        return

    # 遍历所有csv文件
    for filename in os.listdir(folder_path):
        if not filename.lower().endswith(".csv"):
            continue

        filepath = os.path.join(folder_path, filename)
        print(f"正在处理：{filename}")

        rows = []
        # 【用原生csv模块读取，保证格式不乱】
        with open(filepath, "r", encoding="utf-8", newline="") as f:
            reader = csv.reader(f)
            for row in reader:
                rows.append(row)

        if not rows:
            continue

        # ===================== 1. 删除空行 =====================
        # 空行定义：整行都是空字符串
        non_empty_rows = [r for r in rows if any(cell.strip() for cell in r)]

        # ===================== 2. 删除空列 =====================
        # 先获取所有列
        cols_count = len(non_empty_rows[0]) if non_empty_rows else 0
        keep_cols = []

        for col_idx in range(cols_count):
            # 检查这一列是否【全为空】
            col_values = [row[col_idx].strip() for row in non_empty_rows if len(row) > col_idx]
            if any(val for val in col_values):
                keep_cols.append(col_idx)

        # 只保留非空列
        cleaned_rows = []
        for row in non_empty_rows:
            new_row = [row[i] if i < len(row) else "" for i in keep_cols]
            cleaned_rows.append(new_row)

        # ===================== 保存（保持格式） =====================
        name, ext = os.path.splitext(filename)
        new_filename = f"{name}_cleaned{ext}"
        new_path = os.path.join(folder_path, new_filename)

        with open(new_path, "w", encoding="utf-8-sig", newline="") as f:
            writer = csv.writer(f)
            writer.writerows(cleaned_rows)

        print(f"✅ 处理完成：{new_filename}\n")

# ===================== 你只需要改这里 =====================
if __name__ == "__main__":
    # 改成你的CSV文件夹路径
    FOLDER = "/home/simple/Desktop/Scene-Knowledge/xlsx/csv_output"  # 相对路径（脚本同目录下的csv_files文件夹）
    
    clean_csv_preserve_format(FOLDER)
