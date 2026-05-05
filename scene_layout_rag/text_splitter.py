"""Lightweight text splitting helpers used during corpus ingestion.

只做两件事：
- ``chunk_text``: 字符级滑窗切分，给 CSV/JSONL 的长描述用。
- ``chunk_by_paragraph``: 按 markdown 段落聚合，保留 USD 结构层级感。
"""
from __future__ import annotations

import re
from typing import List


def chunk_text(text: str, chunk_size: int, chunk_overlap: int) -> List[str]:
    """字符级滑窗切分。

    保证：当 ``len(text) <= chunk_size`` 时返回 ``[text]``，避免空 chunk。
    """
    text = text.strip()
    if not text:
        return []
    if chunk_size <= 0:
        return [text]
    if len(text) <= chunk_size:
        return [text]

    step = max(1, chunk_size - max(0, chunk_overlap))
    chunks: List[str] = []
    start = 0
    while start < len(text):
        end = min(start + chunk_size, len(text))
        chunks.append(text[start:end].strip())
        if end == len(text):
            break
        start += step
    return [c for c in chunks if c]


_PARA_SEP = re.compile(r"\n\s*\n+")


def chunk_by_paragraph(text: str, block_size: int = 3) -> List[str]:
    """按空行分段，再按 ``block_size`` 段聚合。

    block_size=3 是经验值：USD markdown 中一个层级（含元数据 + 子节点列表 +
    备注）通常落在 2–4 段之间，3 段既不会切碎层级也不会让 chunk 过长。
    """
    text = text.strip()
    if not text:
        return []
    paragraphs = [p.strip() for p in _PARA_SEP.split(text) if p.strip()]
    if not paragraphs:
        return []
    block_size = max(1, block_size)
    chunks: List[str] = []
    for i in range(0, len(paragraphs), block_size):
        block = "\n\n".join(paragraphs[i : i + block_size])
        chunks.append(block)
    return chunks


__all__ = ["chunk_text", "chunk_by_paragraph"]
