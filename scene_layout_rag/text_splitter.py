"""Utility helpers for chunking markdown or CSV derived documents."""
from __future__ import annotations

from itertools import islice
from typing import Iterable, Iterator, List, Sequence


def _grouper(iterable: Iterable[str], size: int) -> Iterator[List[str]]:
    iterator = iter(iterable)
    while True:
        block = list(islice(iterator, size))
        if not block:
            return
        yield block


def simple_sentence_split(text: str) -> List[str]:
    separators = ["。", "！", "？", ".", "!", "?"]
    pieces: List[str] = []
    buff = ""
    for ch in text:
        buff += ch
        if ch in separators and len(buff.strip()) > 0:
            pieces.append(buff.strip())
            buff = ""
    if buff.strip():
        pieces.append(buff.strip())
    return pieces


def chunk_text(text: str, chunk_size: int = 512, overlap: int = 64) -> List[str]:
    sentences = simple_sentence_split(text)
    if not sentences:
        sentences = [text]

    chunks: List[str] = []
    idx = 0
    while idx < len(sentences):
        window = sentences[idx : idx + chunk_size]
        chunk = " ".join(window).strip()
        if chunk:
            chunks.append(chunk)
        if overlap == 0:
            idx += chunk_size
        else:
            idx += max(1, chunk_size - overlap)
    return chunks


def chunk_by_paragraph(text: str, block_size: int = 3) -> List[str]:
    paragraphs = [p.strip() for p in text.split("\n\n") if p.strip()]
    return ["\n\n".join(block) for block in _grouper(paragraphs, block_size)]


__all__ = ["chunk_text", "chunk_by_paragraph", "simple_sentence_split"]
