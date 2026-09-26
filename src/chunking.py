from dataclasses import dataclass

@dataclass
class Chunk:
    testo: str
    documento: str
    indice: int

def chunk_text(testo: str, nome_documento: str, chunk_size: int, overlap: int) -> list[Chunk]:
    if overlap >= chunk_size:
        raise ValueError("ERRORE")

    chunk_list = []
    i = 0
    for start in range(0, len(testo), chunk_size - overlap):
        stringa = testo[start : start + chunk_size]
        new_chunk = Chunk(stringa, nome_documento, i)
        i += 1
        chunk_list.append(new_chunk)
    return chunk_list

