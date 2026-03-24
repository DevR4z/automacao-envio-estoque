import pandas as pd
import pyautogui as pag
import csv
import time


# Configurações de segurança
pag.PAUSE = 1      # pequena pausa entre comandos
pag.FAILSAFE = True  # mover o mouse para canto superior esquerdo interrompe


caminho_csv = "C:\\Users\\vinicius\\Documents\\Notas\\contas\\estoque.csv"


def ler_codigos(caminho_csv):
    codigos = []
    with open(caminho_csv, "r", newline="", encoding="utf-8") as f:
        leitor = csv.reader(f)
        for linha in leitor:
            if not linha:
                continue
            codigo = linha[0].strip()
            if codigo:
                codigos.append(codigo)
    return codigos


def contagem_regressiva(segundos=5):
    print(f"Iniciando em {segundos} segundos...")
    for i in range(segundos, 0, -1):
        print(i)
        time.sleep(1)
    print("Começando!")


# ====== AJUSTE ESTAS COORDENADAS PARA O SEU MONITOR ======
# Use um script separado com pyautogui.position() para descobrir
X_CAMPO_BUSCA, Y_CAMPO_BUSCA = 301, 279                           # campo onde você cola o código
X_QUADRADO, Y_QUADRADO = 257, 472                                 # quadrado de seleção
X_MAIS_ACOES, Y_MAIS_ACOES = 648, 739                             # abrir opções
X_ENVIAR_ESTOQUE, Y_ENVIAR_ESTOQUE = 555, 358                     # enviar estoque para o e-commerce
X_SELECIONE_ECOMMERCE, Y_SELECIONE_ECOMMERCE = 804, 291           # abrir seleção de e-commerce
X_ML, Y_ML = 776, 435                                             # ml
X_SHOPEE, Y_SHOPEE = 776, 458                                     # shopee
X_AMAZON, Y_AMAZON = 774, 480                                     # amazon
X_SHEIN, Y_SHEIN = 776, 504                                       # shein
X_MAGALU, Y_MAGALU = 777, 527                                     # magalu
X_SELECIONAR, Y_SELECIONAR = 796, 738                             # selecionar
X_ENVIAR, Y_ENVIAR = 796, 738                                     # enviar
X_FECHAR, Y_FECHAR = 1313, 157                                    # fechar janela de envio


# =========================================================


def processar_codigo(codigo):
    print(f"Processando código: {codigo}")
    # 1) Clicar no campo e colar o primeiro código da lista CSV e dar enter
    pag.click(X_CAMPO_BUSCA, Y_CAMPO_BUSCA)
    pag.hotkey("ctrl", "a")   # seleciona tudo, opcional
    pag.write(codigo)
    pag.press("enter")


    # Aguarda carregar resultados
    time.sleep(1)


    # 2) Clicar no quadrado de seleção
    pag.click(X_QUADRADO, Y_QUADRADO)


    # 3) Mais ações
    pag.click(X_MAIS_ACOES, Y_MAIS_ACOES)


    # 4) Enviar estoque para o e-commerce
    pag.click(X_ENVIAR_ESTOQUE, Y_ENVIAR_ESTOQUE)


    # 6) Selecionar o e-commerce
    pag.click(X_SELECIONE_ECOMMERCE, Y_SELECIONE_ECOMMERCE)


    # 7) Selecionar Mercado Livre
    pag.click(X_ML, Y_ML)


    # 8) Selecionar Shopee
    pag.click(X_SHOPEE, Y_SHOPEE)


    # 9) Selecionar Amazon
    pag.click(X_AMAZON, Y_AMAZON)


    # 10) Selecionar Shein
    pag.click(X_SHEIN, Y_SHEIN)


    # 11) Selecionar Magalu
    pag.click(X_MAGALU, Y_MAGALU)


    # 12) Clicar em selecionar
    pag.click(X_SELECIONAR, Y_SELECIONAR)
    time.sleep(4)  # aguarda processamento


    # 13) Clicar em enviar
    pag.click(X_ENVIAR, Y_ENVIAR)
    time.sleep(10)  # aguarda processamento


    # 14) Fechar janela de envio
    pag.click(X_FECHAR, Y_FECHAR)


def main():
    codigos = ler_codigos(caminho_csv)
    print(f"Total de códigos carregados: {len(codigos)}")


    if not codigos:
        print("Nenhum código encontrado no CSV.")
        return


    contagem_regressiva(5)


    for idx, codigo in enumerate(codigos, start=1):
        try:
            processar_codigo(codigo)
            print(f"[{idx}/{len(codigos)}] Código {codigo} concluído.")
        except Exception as e:
            print(f"Erro ao processar {codigo}: {e}")
            # aqui você pode registrar em um log ou continuar para o próximo
            continue


    print("Automação finalizada!")


if __name__ == "__main__":
    main()
