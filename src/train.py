from ultralytics import YOLO
import os

def TrainModel():
    data_yaml = os.path.abspath("data.yaml")

    # Carregar modelo YOLOv8 pré-treinado no COCO
    model = YOLO("yolov8n.pt")

    # --- Stage 1: Treinar apenas a cabeça ---
    # print("=" * 60)
    # print("STAGE 1: Treinando apenas a cabeça do modelo...")
    # print("=" * 60)
    
    # results_head = model.train(
    #     data=data_yaml,
    #     epochs=100,
    #     imgsz=640,
    #     batch=16,
    #     device=0,
    #     freeze=10,  # congela as primeiras 10 camadas (backbone)
    #     project="runs/train",
    #     name="stage1_head",
    #     patience=20,  # early stopping
    #     save=True,
    #     save_period=10  # salva checkpoint a cada 10 epochs
    # )
    
    # Salvar o melhor modelo da Stage 1
    best_model_stage1 = "runs/train/stage1_head3/weights/best.pt"
    #print(f"\nMelhor modelo Stage 1 salvo em: {best_model_stage1}")

    # --- Stage 2: Refinar todo o modelo ---
    #print("\n" + "=" * 60)
    print("STAGE 2: Refinando todo o modelo...")
    print("=" * 60)
    
    # Carregar o melhor modelo da Stage 1
    model = YOLO(best_model_stage1)
    
    results_full = model.train(
        data=data_yaml,
        epochs=50,
        imgsz=640,
        batch=16,
        device=0,
        freeze=0,  # descongela tudo (ou freeze=[] também funciona)
        lr0=0.001,  # learning rate inicial menor para fine-tuning
        lrf=0.01,  # learning rate final (lr0 * lrf = 0.00001)
        warmup_epochs=5,  # aquecimento gradual do LR
        project="runs/train",
        name="stage2_full",
        patience=15,
        save=True,
        save_period=10
    )
    
    # Salvar o melhor modelo final
    best_model_final = "runs/train/stage2_full/weights/best.pt"
    print(f"\nMelhor modelo final salvo em: {best_model_final}")

    # --- Avaliar modelo final ---
    print("\n" + "=" * 60)
    print("Avaliando modelo final...")
    print("=" * 60)
    
    final_model = YOLO(best_model_final)
    metrics = final_model.val(data=data_yaml)
    
    print("\n--- MÉTRICAS FINAIS ---")
    print(f"mAP50: {metrics.box.map50:.4f}")
    print(f"mAP50-95: {metrics.box.map:.4f}")
    print(f"Precision: {metrics.box.mp:.4f}")
    print(f"Recall: {metrics.box.mr:.4f}")
    
    return final_model, metrics

if __name__ == "__main__":
    TrainModel()