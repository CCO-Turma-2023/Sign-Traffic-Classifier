import os
import torch
from ultralytics import YOLO

# A lista de classes é uma boa referência, mas o script usará o que estiver no seu 'data.yaml'
classes = ['(A-18)', '(A-2a)', '(A-2b)', '(A-32a)', '(A-32b)', '(Del)', '(I-4)', '(MA)', '(MP-3)', '(R-1)', '(R-15)', '(R-19)30', '(R-19)40', '(R-19)50', '(R-19)60', '(R-19)70', '(R-19)80', '(R-19)90', '(R-2)', '(R-24a)', '(R-4a)', '(R-5a)', '(R-6a)', '(R-6c)']

# --- CONFIGURAÇÕES CENTRALIZADAS PARA OTIMIZAÇÃO ---
CONFIG = {
    # Modelo: 'yolov8n.pt' é o mais rápido para mobile.
    "model_name": 'yolov8n.pt',

    # Caminho para o seu arquivo data.yaml.
    # O script assume que ele está na mesma pasta, mas você pode mudar.
    "dataset_path": os.path.abspath("data.yaml"),

    # Tamanho da Imagem: Reduzido para 320. Esta é a otimização de maior impacto!
    "imgsz": 320,

    # Parâmetros de Treinamento
    "epochs": 50,
    "batch_size": 16,
    "patience": 20, # Para o treinamento se não houver melhora, economizando tempo.

    # Otimizações de Exportação para ONNX
    "opset": 12,
    "simplify": True
}

def check_device():
    """Verifica a disponibilidade de GPU CUDA para o treinamento."""
    if torch.cuda.is_available():
        print("INFO: GPU CUDA encontrada! Usando dispositivo 0.")
        return 0
    else:
        print("AVISO: GPU CUDA não encontrada. Treinando na CPU, o que será muito mais lento.")
        return 'cpu'

def train_and_export_optimized_model():
    """
    Função principal que treina o modelo de forma otimizada e depois o exporta para ONNX.
    """
    
    # 1. CARREGAR O MODELO
    print(f"Carregando modelo base: {CONFIG['model_name']}")
    model = YOLO(CONFIG['model_name'])

    # 2. TREINAR O MODELO
    print(f"--- Iniciando Treinamento Otimizado (imgsz={CONFIG['imgsz']}) ---")
    training_device = check_device()
    
    results = model.train(
        data=CONFIG['dataset_path'],
        epochs=CONFIG['epochs'],
        imgsz=CONFIG['imgsz'],
        batch=CONFIG['batch_size'],
        patience=CONFIG['patience'],
        device=training_device
    )

    # 3. AVALIAR O MODELO (Opcional, mas bom para verificar a precisão)
    print("--- Avaliando a precisão do modelo treinado ---")
    metrics = model.val()
    print(f"Métricas de precisão (mAP50-95): {metrics.box.map}")

    # 4. EXPORTAR PARA ONNX COM OTIMIZAÇÕES
    print("--- Exportando o melhor modelo para ONNX com otimizações ---")
    # O ultralytics salva o melhor modelo em '.../weights/best.pt'
    # Não precisamos recarregar, podemos exportar diretamente.
    onnx_path = model.export(
        format='onnx',
        imgsz=CONFIG['imgsz'],
        opset=CONFIG['opset'],
        simplify=CONFIG['simplify']
    )

    print("\n--- PROCESSO CONCLUÍDO ---")
    print(f"Modelo treinado e avaliado com sucesso.")
    print(f"Modelo ONNX otimizado foi salvo em: {onnx_path}")


if __name__ == "__main__":
    train_and_export_optimized_model()