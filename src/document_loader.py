from pypdf import PdfReader
from pathlib import Path
from chunking import chunk_text
from chunking import Chunk

def chunk_directory(path_cartella : str, chunk_size : int, overlap : int) -> list[Chunk]: 

    lista_chunk = []
    j=0
    lunghezza_caratteri = []
    cartella = Path(path_cartella)
    for file in cartella.glob("*.pdf"):
        j+=1
        reader = PdfReader(file)
        testo_completo = ""
        for pagina in reader.pages:
            testo_completo += pagina.extract_text()
            
        lunghezza_caratteri.append(testo_completo)
        testo_in_chunks = chunk_text(testo_completo, file.name, chunk_size, overlap)
        lista_chunk.extend(testo_in_chunks)

    #for chunk in lista_chunk:
        #print(chunk.testo)
    print(len(lista_chunk))
    for i in range(len(lunghezza_caratteri)):
        print(len(lunghezza_caratteri[i]))
   
    return lista_chunk

#chunk_directory()

path = str((Path(".").resolve())) 
path = path + "/data/ingegneria_software"
chunk_directory(path, 500, 200)
       