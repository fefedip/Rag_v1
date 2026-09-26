import chunking
import pytest

def test_chunk_text_overlap_invalido():
    with pytest.raises(ValueError):
        chunking.chunk_text("ABCDEFGHIJ", "Test", chunk_size=10, overlap=10)
    
    

def test_chunk_text():
    testo = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    nome = "Test"
    chunk_size = 10
    overlap = 3

    chunk_list = chunking.chunk_text(testo, nome, chunk_size, overlap)

    assert len(chunk_list) == 4

    assert chunk_list[0].testo == "ABCDEFGHIJ"
    assert chunk_list[1].testo == "HIJKLMNOPQ"
    assert chunk_list[2].testo == "OPQRSTUVWX"
    assert chunk_list[3].testo == "VWXYZ"

    assert len(chunk_list[0].testo) == 10
    assert len(chunk_list[1].testo) == 10
    assert len(chunk_list[2].testo) == 10
    assert len(chunk_list[3].testo) == 5

    assert chunk_list[0].documento == "Test"

    assert chunk_list[0].indice == 0
    assert chunk_list[1].indice == 1
    assert chunk_list[2].indice == 2
    assert chunk_list[3].indice == 3

def test_chunk_text_empty():
    testo = ""
    nome = "Test"
    chunk_size = 10
    overlap = 3

    chunk_list = chunking.chunk_text(testo, nome, chunk_size, overlap)

    assert len(chunk_list) == 0
    assert chunk_list == []
