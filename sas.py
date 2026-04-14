import pandas as pd
from pathlib import Path


#Arquivo de progresso academico da pos 
#input_path = Path(r"\\172.23.91.5\sas_publico\)
#output_path = Path.home() / "Downloads" / "ac_pos_graduacao.parquet"



input_path = Path(r"\\CAMINHO DE ORIGEM.SAS7BDAT")
output_path = Path.home() / "Downloads" / "Arquivo de destino.parquet"




# Verifica se o arquivo existe e é acessível
if not input_path.exists():
    raise FileNotFoundError(f"Arquivo não encontrado: {input_path}. Verifique o caminho e permissões.")

print(f"Arquivo encontrado: {input_path}")

# Tenta várias codificações comuns para arquivos SAS até encontrar uma que funcione
encodings_to_try = ("latin1", "cp1252", "iso-8859-1", "cp850", "utf-8")
for encoding in encodings_to_try:
    try:
        df = pd.read_sas(input_path, format="sas7bdat", encoding=encoding)
        print(f"✅ Lido com encoding: {encoding}")
        break
    except (UnicodeDecodeError, UnicodeError, Exception) as e:
        print(f"❌ Falhou com {encoding}: {type(e).__name__}: {e}")
else:
    raise RuntimeError(
        "Não foi possível ler o arquivo SAS. Verifique se é um arquivo .sas7bdat válido e não corrompido."
    )

df.to_parquet(output_path, engine="pyarrow", compression="snappy")