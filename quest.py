import json
import os
import statistics

def carregar_perguntas(caminho_arquivo):

    with open(caminho_arquivo, "r", encoding="utf-8") as f:

        return json.load(f)

def salvar_resultado(nome, idade, local, acertos, total, arquivo):
    novo_dado = {
        "nome": nome,
        "idade": idade,
        "local": local,
        "acertos": acertos,
        "total_perguntas": total
    }

    if os.path.exists(arquivo):
        with open(arquivo, "r", encoding="utf-8") as f:
            try:
                dados = json.load(f)
            except json.JSONDecodeError:
                dados = []
    else:
        dados = []

    dados.append(novo_dado)

    with open(arquivo, "w", encoding="utf-8") as f:
        json.dump(dados, f, ensure_ascii=False, indent=4)

def calcular_media_acertos(arquivo, nome_nivel):
    if not os.path.exists(arquivo):
        print(f"\nNenhum dado encontrado para calcular média de acertos do nível {nome_nivel}.")
        return

    with open(arquivo, "r", encoding="utf-8") as f:
        try:
            dados = json.load(f)
        except json.JSONDecodeError:
            print("Erro ao ler os dados.")
            return

    if not dados:
        print("Nenhum participante registrado.")
        return

    total_acertos = 0
    total_questoes = 0
    for pessoa in dados:
        try:
            total_acertos += int(pessoa["acertos"])
            total_questoes += int(pessoa["total_perguntas"])
        except (KeyError, ValueError):
            print(f"Dado inválido encontrado: {pessoa}")

    if total_questoes == 0:
        print(f"Não foi possível calcular a média para o nível {nome_nivel}.")
    else:
        media = total_acertos / total_questoes * 100
        print(f"\n📊 Média de acertos no nível {nome_nivel}: {media:.2f}%")

def idade_medias_mediana(arquivo, nome_nivel):
    if not os.path.exists(arquivo):
        print("Nenhum dado encontrado para calcular estatísticas de idade.")
        return

    with open(arquivo, "r", encoding="utf-8") as f:
        try:
            dados = json.load(f)
        except json.JSONDecodeError:
            print("Erro ao ler os dados.")
            return

    if not dados:
        print("Nenhum participante registrado.")
        return

    idades = []

    for pessoa in dados:
        try:
            idades.append(int(pessoa["idade"]))
        except (KeyError, ValueError):
            print(f"Idade inválida encontrada em: {pessoa}")

    if not idades:
        print("Não foi possível calcular estatísticas de idade.")
    else:
        media = sum(idades) / len(idades)
        mediana = statistics.median(idades)
        try:
            moda = statistics.mode(idades)
        except statistics.StatisticsError:
            moda = "Sem moda (idades igualmente distribuídas)"

        print(f"\n📊 Estatísticas de idade para o nível {nome_nivel}:")
        print(f"   ➤ Média: {media:.2f} anos")
        print(f"   ➤ Mediana: {mediana:.2f} anos")
        print(f"   ➤ Moda: {moda} anos")


def entrada_segura(mensagem):

    try:

        return input(mensagem)

    except (EOFError, OSError):

        print("\nErro de entrada detectado. Encerrando programa.")

        exit()

def quest_iniciante():

    print("= Cadastro do Usuário =")

    nome = input("Digite seu nome: ")

    idade = int(input("Digite sua idade: "))

    local = input("Onde você mora? ")

    print(f"\nBem-vindo(a), {nome}! Vamos começar o questionário de tecnologia - Nível Iniciante.\n")

    questionario = carregar_perguntas("perguntas_iniciante.json")

    acertos = 0

    respostas_certas = []

    respostas_erradas = []

    opcoes_validas = {"A", "B", "C", "D"}

    for i, q in enumerate(questionario):

        print(f"\nPergunta {i + 1}: {q['pergunta']}")

        for opcao in q["opcoes"]:

            print(opcao)

        while True:

            resposta = entrada_segura("Sua resposta (A/B/C/D): ").strip().upper()

            if resposta in opcoes_validas:

                break

            else:

                print("⚠️ Resposta inválida. Por favor, digite apenas A, B, C ou D.")

        if resposta == q["resposta"]:

            print("✅ Resposta correta!")

            acertos += 1

            respostas_certas.append(q["pergunta"])

        else:

            print(f"❌ Resposta incorreta! A resposta certa era: {q['resposta']}")

            respostas_erradas.append((q["pergunta"], resposta, q["resposta"]))

    print(f"\n{nome}, você acertou {acertos} de {len(questionario)} perguntas.")

    print("\n📋 Perguntas que você ACERTOU:")

    for p in respostas_certas:

        print(f"✔️ {p}")

    print("\n📋 Perguntas que você ERROU:")

    for p, r_usuario, r_certa in respostas_erradas:

        print(f"❌ {p}")

        print(f"    ➤ Sua resposta: {r_usuario}")

        print(f"    ✅ Resposta correta: {r_certa}")

    salvar_resultado(nome, idade, local, acertos, len(questionario), "resultados_iniciante.json")

def quest_intermediario():

    print("== Cadastro do Usuário ==")

    nome = input("Digite seu nome: ")

    while True:
        try:
            idade = int(input("Digite sua idade: "))
            if idade < 0:
                print("⚠️ Idade não pode ser negativa. Tente novamente.")
            else:
                break
        except ValueError:
            print("⚠️ Entrada inválida. Por favor, digite um número inteiro para a idade.")

    local = input("Onde você mora? ")

    print(f"\nBem-vindo(a), {nome}! Vamos começar o questionário de tecnologia - Nível intermediario.\n")

    questionario = carregar_perguntas("perguntas_intermediario.json")

    acertos = 0

    respostas_certas = []

    respostas_erradas = []

    opcoes_validas = {"A", "B", "C", "D"}

    for i, q in enumerate(questionario):

        print(f"\nPergunta {i + 1}: {q['pergunta']}")

        for opcao in q["opcoes"]:

            print(opcao)

        while True:

            resposta = entrada_segura("Sua resposta (A/B/C/D): ").strip().upper()

            if resposta in opcoes_validas:

                break

            else:

                print("⚠️ Resposta inválida. Por favor, digite apenas A, B, C ou D.")

        if resposta == q["resposta"]:

            print("✅ Resposta correta!")

            acertos += 1

            respostas_certas.append(q["pergunta"])

        else:

            print(f"❌ Resposta incorreta! A resposta certa era: {q['resposta']}")

            respostas_erradas.append((q["pergunta"], resposta, q["resposta"]))

    print(f"\n{nome}, você acertou {acertos} de {len(questionario)} perguntas.")

    print("\n📋 Perguntas que você ACERTOU:")

    for p in respostas_certas:

        print(f"✔️ {p}")

    print("\n📋 Perguntas que você ERROU:")

    for p, r_usuario, r_certa in respostas_erradas:

        print(f"❌ {p}")

        print(f"    ➤ Sua resposta: {r_usuario}")

        print(f"    ✅ Resposta correta: {r_certa}")

    salvar_resultado(nome, idade, local, acertos, len(questionario), "resultados_intermediario.json")

def quest_avancado():

    print("=== Cadastro do Usuário ===")

    nome = input("Digite seu nome: ")

    while True:
        try:
            idade = int(input("Digite sua idade: "))
            if idade < 0:
                print("⚠️ Idade não pode ser negativa. Tente novamente.")
            else:
                break
        except ValueError:
            print("⚠️ Entrada inválida. Por favor, digite um número inteiro para a idade.")

    local = input("Onde você mora? ")

    print(f"\nBem-vindo(a), {nome}! Vamos começar o questionário avançado de tecnologia.\n")

    questionario = carregar_perguntas("perguntas_avancado.json")

    acertos = 0

    respostas_certas = []

    respostas_erradas = []

    opcoes_validas = {"A", "B", "C", "D"}

    for i, q in enumerate(questionario):

        print(f"\nPergunta {i + 1}: {q['pergunta']}")

        for opcao in q["opcoes"]:

            print(opcao)

        while True:

            resposta = entrada_segura("Sua resposta (A/B/C/D): ").strip().upper()

            if resposta in opcoes_validas:

                break

            else:

                print("⚠️ Resposta inválida. Por favor, digite apenas A, B, C ou D.")

        if resposta == q["resposta"]:

            print("✅ Resposta correta!")

            acertos += 1

            respostas_certas.append(q["pergunta"])

        else:

            print(f"❌ Resposta incorreta! A resposta certa era: {q['resposta']}")

            respostas_erradas.append((q["pergunta"], resposta, q["resposta"]))

    print(f"\n{nome}, você acertou {acertos} de {len(questionario)} perguntas.")

    print("\n📋 Perguntas que você ACERTOU:")

    for p in respostas_certas:

        print(f"✔️ {p}")

    print("\n📋 Perguntas que você ERROU:")

    for p, r_usuario, r_certa in respostas_erradas:

        print(f"❌ {p}")

        print(f"    ➤ Sua resposta: {r_usuario}")

        print(f"    ✅ Resposta correta: {r_certa}")

    salvar_resultado(nome, idade, local, acertos, len(questionario), "resultados_avancado.json")

def menu():
    while True:

        print("\n=== New Tech - Aprendizado seguro! ===")
        print("")
        print("1. Questionário - Iniciante")
        print("2. Questionário - Intermediário")
        print("3. Questionário - Avançado")
        print("")
        print("4. Média de acertos - Iniciante")
        print("5. Média de acertos - Intermediário")
        print("6. Média de acertos - Avançado")
        print("")
        print("7. Calcular a média e mediana de idade dos usuarios que fizeram questionário iniciante")
        print("8. Calcular a média e mediana de idade dos usuarios que fizeram questionário intermediário")
        print("9. Calcular a média e mediana de idade dos usuarios que fizeram questionário avançado")
        print("")
        print("0. Sair")

        opcao = entrada_segura("Escolha uma opção: ")

        if opcao == "1":
            quest_iniciante()
        elif opcao == "2":
            quest_intermediario()
        elif opcao == "3":
            quest_avancado()
        elif opcao == "4":
            calcular_media_acertos("resultados_iniciante.json", "Iniciante")
        elif opcao == "5":
            calcular_media_acertos("resultados_intermediario.json", "Intermediário")
        elif opcao == "6":
            calcular_media_acertos("resultados_avancado.json", "Avançado")
        elif opcao == "7":
            idade_medias_mediana("resultados_iniciante.json", "Iniciante")
        elif opcao == "8":
            idade_medias_mediana("resultados_intermediario.json", "Intermediário")
        elif opcao == "9":
            idade_medias_mediana("resultados_avancado.json", "Avançado")
        elif opcao == "0":
            print("Encerrando...")
            break
        else:
            print("Opção inválida. Tente novamente.")

def verificar_login():

    print("=== Login de Administrador ===")

    login = entrada_segura("Login: ")

    senha = entrada_segura("Senha: ")

    if login != "admin" or senha != "12345":

        print("Erro: Login ou senha incorretos. Encerrando o programa.")

        exit()

if __name__ == "__main__":

    verificar_login()

    menu() 