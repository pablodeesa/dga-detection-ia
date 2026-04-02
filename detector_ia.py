import pandas as pd
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# 1. Carregar os dados (O arquivo deve estar na mesma pasta no seu PC)
# Para o GitHub, usamos apenas o nome do arquivo
NOME_ARQUIVO = 'dga_data.csv'

try:
    df = pd.read_csv(NOME_ARQUIVO)
    
    # 2. Criar as características de segurança (Features)
    df['tamanho'] = df['domain'].str.len()
    df['numeros'] = df['domain'].str.count('[0-9]')
    df['alvo'] = df['isDGA'].map({'dga': 1, 'legit': 0})

    # 3. Treinar a IA
    X = df[['tamanho', 'numeros']]
    y = df['alvo']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    modelo = RandomForestClassifier(n_estimators=100)
    modelo.fit(X_train, y_train)

    # 4. Salvar o modelo (O "cérebro" que o seu bot vai usar)
    joblib.dump(modelo, 'detector_dga.pkl')
    print("Sucesso: Modelo treinado e salvo como detector_dga.pkl")

except FileNotFoundError:
    print(f"Erro: O arquivo {NOME_ARQUIVO} não foi encontrado na pasta.")
