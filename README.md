# dga-detection-ia
Detecção de Domínios Maliciosos (DGA) com Machine Learning e Random Forest.

1. O que é o projeto?
"Este projeto utiliza Inteligência Artificial para identificar algoritmos de geração de domínios (DGA), uma técnica comum usada por Malwares para estabelecer comunicação com servidores de Comando e Controle (C2)."

2. Como a IA funciona? (As "Pistas")
Feature Engineering: Extração de comprimento de domínio e densidade numérica.

Algoritmo: Random Forest Classifier (Scikit-Learn).

Performance: 81.68% de acurácia em um dataset equilibrado de 160.000 amostras.

3. Como usar?
Clone o repositório.

Instale as dependências: pip install pandas scikit-learn joblib.

Execute o script de treinamento ou carregue o modelo detector_dga.pkl.
