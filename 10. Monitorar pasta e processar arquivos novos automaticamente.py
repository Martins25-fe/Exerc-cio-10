import time
import os
import pandas as pd
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Definição da classe que irá tratar os eventos da pasta
class CSVHandler(FileSystemEventHandler):
    def on_created(self, event):
        # Verifica se o evento é para um arquivo e se o arquivo é CSV
        if event.is_directory:
            return
        if event.src_path.endswith('.csv'):
            print(f"Novo arquivo CSV detectado: {event.src_path}")
            processar_csv(event.src_path)

# Função para processar o arquivo CSV e gerar o relatório
def processar_csv(caminho_arquivo):
    try:
        # Lê o arquivo CSV
        df = pd.read_csv(caminho_arquivo)
        print(f"Analisando o arquivo: {caminho_arquivo}")
        
        # Realiza uma análise simples (pode ser adaptada para outros tipos de análise)
        relatorio = df.describe()  # Exemplo de análise simples
        
        # Caminho para salvar o relatório
        caminho_relatorio = caminho_arquivo.replace('.csv', '_relatorio.txt')
        
        # Salva o relatório em formato de texto
        with open(caminho_relatorio, 'w') as f:
            f.write(str(relatorio))
        print(f"Relatório gerado: {caminho_relatorio}")
        
    except Exception as e:
        print(f"Erro ao processar {caminho_arquivo}: {e}")

# Função para monitorar a pasta
def monitorar_pasta(pasta_a_monitorar):
    event_handler = CSVHandler()
    observer = Observer()
    observer.schedule(event_handler, pasta_a_monitorar, recursive=False)  # monitorando apenas a pasta e não subpastas
    observer.start()

    print(f"Monitorando a pasta: {pasta_a_monitorar}")
    
    try:
        while True:
            time.sleep(1)  # Aguardar e verificar novos arquivos a cada 1 segundo
    except KeyboardInterrupt:
        observer.stop()  # Interrompe o monitoramento com Ctrl+C
    observer.join()

if __name__ == "__main__":
    pasta_a_monitorar = "/caminho/para/sua/pasta"  # Substitua pelo caminho da pasta que deseja monitorar
    monitorar_pasta(pasta_a_monitorar)










