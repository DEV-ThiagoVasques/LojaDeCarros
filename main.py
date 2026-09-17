#  SOLARIUM - Sistema de Catálogo de Carros
# =====================================================
# Sistema interativo em terminal para gerenciar um
# catálogo de marcas e modelos de carros, com detalhes
# como potência, tração, preço, ano e combustível.
# Os dados são persistidos em um arquivo JSON, então as
# edições feitas continuam disponíveis na próxima vez
# que o programa for executado.
# =====================================================
 
import json
import os
 
ARQUIVO_DADOS = "catalogo_solarium.json"
 
# -----------------------------------------------------
# Dados iniciais (usados apenas se não existir catalogo_solarium.json)
# Cada modelo é um dicionário de atributos. Preencha ou
# edite os valores pelo próprio menu do programa (opção
# "Editar modelo"), ou diretamente aqui no código.
# -----------------------------------------------------
CATALOGO_PADRAO = {
    "Audi": ["A3", "A4", "A5", "A7", "RS3", "RS4", "RS5", "RS6", "Q3", "Q5", "Q7", "Q8", "RSQ8", "TT", "TTRS"],
    "Bugatti": ["Chiron", "Bolide", "Divo", "Veyron", "Tourbillion"],
    "Chevrolet": ["Camaro ZL1", "Camaro ZLE", "Corvette C6", "Corvette C7", "Corvette C8"],
    "Dodge": ["Charger", "Challenger", "Demon", "Viper"],
    "Ferrari": ["330 California", "458 GTB", "458 Pista", "812 Superfast", "LaFerrari", "PuroSangue"],
    "Hyundai": ["Creta", "Elantra", "HB20", "HB20s", "Veloster"],
    "Jaguar": ["F-Type", "E-Pace", "F-Pace", "I-Pace"],
    "Koenigsegg": ["Agera", "Agera RS", "CC8S", "CCGT", "Gemera", "Jesko", "Jesko Absolut", "One:1", "Regera"],
    "Lamborghini": ["Aventador", "Aventador SV", "Aventador SVJ", "Centenário", "Countach", "Diablo", "Gallardo",
                     "Huracán", "Murciélago", "Revuelto", "Sesto Elemento", "Sián", "Urus", "Veneno"],
    "Mercedes": ["AMG GT", "AMG ONE", "CLA", "CLE", "CLS", "G63", "GLA", "GLC", "GLE", "SLC", "SLK", "SLR", "SLS"],
    "Nissan": ["350z", "360z", "370z", "400z", "Silvia S13", "Silvia S14", "Silvia S15", "Skyline R33",
               "Skyline R34", "Skyline R35"],
    "Pagani": ["Huayra", "Huayra Imola", "Huayra R", "Huayra R Evo", "Huayra Roadster", "Utopia", "Zonda F"],
    "Range Rover": ["Evoque", "Velar", "Vogue"],
    "Subaru": ["BRZ", "WRX", "WRX STI"],
    "Toyota": ["Camry", "Celica", "Corolla", "Corolla Cross", "Étios", "GR Corolla", "GR Supra", "GR Yaris",
               "Hilux", "Prius", "RAV4", "Supra", "SW4", "Tacoma", "Tundra", "Yaris", "Yaris Cross"],
    "Volvo": ["XC 40", "XC 50", "XC 60", "XC 70", "XC 80"],
}
 
# Atributos que cada modelo terá. Adicione ou remova
# chaves aqui para mudar quais informações o sistema pede.
ATRIBUTOS_PADRAO = {
    "potencia_cv": "A definir",
    "tracao": "A definir",      # ex: Dianteira, Traseira, 4x4/AWD
    "preco": "A definir",
    "ano": "A definir",
    "combustivel": "A definir",  # ex: Gasolina, Elétrico, Híbrido
}
 
 
# -----------------------------------------------------
# Persistência
# -----------------------------------------------------
def montar_catalogo_inicial():
    """Transforma o catálogo padrão (marca -> lista de modelos)
    em um catálogo completo (marca -> modelo -> atributos)."""
    catalogo = {}
    for marca, modelos in CATALOGO_PADRAO.items():
        catalogo[marca] = {}
        for modelo in modelos:
            catalogo[marca][modelo] = ATRIBUTOS_PADRAO.copy()
    return catalogo
 
 
def carregar_catalogo():
    if os.path.exists(ARQUIVO_DADOS):
        with open(ARQUIVO_DADOS, "r", encoding="utf-8") as f:
            return json.load(f)
    catalogo = montar_catalogo_inicial()
    salvar_catalogo(catalogo)
    return catalogo
 
 
def salvar_catalogo(catalogo):
    with open(ARQUIVO_DADOS, "w", encoding="utf-8") as f:
        json.dump(catalogo, f, ensure_ascii=False, indent=4)
 
 
# -----------------------------------------------------
# Funções auxiliares de entrada
# -----------------------------------------------------
def escolher_marca(catalogo, permitir_cancelar=True):
    marcas = sorted(catalogo.keys())
    print("\nMarcas disponíveis:")
    for i, marca in enumerate(marcas, start=1):
        print(f"  {i}. {marca}")
    if permitir_cancelar:
        print("  0. Cancelar")
 
    while True:
        escolha = input("Digite o número (ou nome) da marca: ").strip()
        if permitir_cancelar and escolha == "0":
            return None
        if escolha.isdigit() and 1 <= int(escolha) <= len(marcas):
            return marcas[int(escolha) - 1]
        # também aceita digitar o nome diretamente
        for marca in marcas:
            if marca.lower() == escolha.lower():
                return marca
        print("Opção inválida, tente novamente.")
 
 
def escolher_modelo(catalogo, marca, permitir_cancelar=True):
    modelos = sorted(catalogo[marca].keys())
    if not modelos:
        print(f"\nA marca {marca} ainda não possui modelos cadastrados.")
        return None
 
    print(f"\nModelos de {marca}:")
    for i, modelo in enumerate(modelos, start=1):
        print(f"  {i}. {modelo}")
    if permitir_cancelar:
        print("  0. Cancelar")
 
    while True:
        escolha = input("Digite o número (ou nome) do modelo: ").strip()
        if permitir_cancelar and escolha == "0":
            return None
        if escolha.isdigit() and 1 <= int(escolha) <= len(modelos):
            return modelos[int(escolha) - 1]
        for modelo in modelos:
            if modelo.lower() == escolha.lower():
                return modelo
        print("Opção inválida, tente novamente.")
 
 
# -----------------------------------------------------
# Funcionalidades principais
# -----------------------------------------------------
def ver_marcas(catalogo):
    print("\n=== MARCAS DISPONÍVEIS ===")
    for marca in sorted(catalogo.keys()):
        print(f"- {marca} ({len(catalogo[marca])} modelo(s))")
 
 
def ver_modelos_de_marca(catalogo):
    marca = escolher_marca(catalogo)
    if marca is None:
        return
    modelos = sorted(catalogo[marca].keys())
    print(f"\n=== MODELOS - {marca.upper()} ===")
    if not modelos:
        print("Nenhum modelo cadastrado ainda.")
    for modelo in modelos:
        print(f"- {modelo}")
 
 
def ver_detalhes_modelo(catalogo):
    marca = escolher_marca(catalogo)
    if marca is None:
        return
    modelo = escolher_modelo(catalogo, marca)
    if modelo is None:
        return
    mostrar_ficha(marca, modelo, catalogo[marca][modelo])
 
 
def mostrar_ficha(marca, modelo, dados):
    print(f"\n=== {marca} {modelo} ===")
    print(f"  Potência:    {dados.get('potencia_cv', 'A definir')} cv")
    print(f"  Tração:      {dados.get('tracao', 'A definir')}")
    print(f"  Preço:       {dados.get('preco', 'A definir')}")
    print(f"  Ano:         {dados.get('ano', 'A definir')}")
    print(f"  Combustível: {dados.get('combustivel', 'A definir')}")
 
 
def adicionar_marca(catalogo):
    nome = input("\nNome da nova marca: ").strip()
    if not nome:
        print("Nome inválido.")
        return
    if nome in catalogo:
        print("Essa marca já existe.")
        return
    catalogo[nome] = {}
    salvar_catalogo(catalogo)
    print(f"Marca '{nome}' adicionada com sucesso!")
 
 
def adicionar_modelo(catalogo):
    marca = escolher_marca(catalogo)
    if marca is None:
        return
    nome_modelo = input(f"\nNome do novo modelo para {marca}: ").strip()
    if not nome_modelo:
        print("Nome inválido.")
        return
    if nome_modelo in catalogo[marca]:
        print("Esse modelo já existe nessa marca.")
        return
 
    print("Preencha os dados do modelo (deixe em branco para 'A definir'):")
    dados = {}
    for chave, rotulo in [
        ("potencia_cv", "Potência (cv)"),
        ("tracao", "Tração"),
        ("preco", "Preço"),
        ("ano", "Ano"),
        ("combustivel", "Combustível"),
    ]:
        valor = input(f"  {rotulo}: ").strip()
        dados[chave] = valor if valor else "A definir"
 
    catalogo[marca][nome_modelo] = dados
    salvar_catalogo(catalogo)
    print(f"Modelo '{nome_modelo}' adicionado a {marca} com sucesso!")
 
 
def editar_modelo(catalogo):
    marca = escolher_marca(catalogo)
    if marca is None:
        return
    modelo = escolher_modelo(catalogo, marca)
    if modelo is None:
        return
 
    dados = catalogo[marca][modelo]
    mostrar_ficha(marca, modelo, dados)
 
    campos = {
        "1": ("potencia_cv", "Potência (cv)"),
        "2": ("tracao", "Tração"),
        "3": ("preco", "Preço"),
        "4": ("ano", "Ano"),
        "5": ("combustivel", "Combustível"),
    }
 
    print("\nQual campo deseja editar?")
    for k, (_, rotulo) in campos.items():
        print(f"  {k}. {rotulo}")
    print("  0. Cancelar")
 
    escolha = input("Opção: ").strip()
    if escolha == "0" or escolha not in campos:
        print("Nenhuma alteração feita.")
        return
 
    chave, rotulo = campos[escolha]
    novo_valor = input(f"Novo valor para {rotulo}: ").strip()
    if novo_valor:
        dados[chave] = novo_valor
        salvar_catalogo(catalogo)
        print("Modelo atualizado com sucesso!")
    else:
        print("Valor vazio, nada foi alterado.")
 
 
def remover_modelo(catalogo):
    marca = escolher_marca(catalogo)
    if marca is None:
        return
    modelo = escolher_modelo(catalogo, marca)
    if modelo is None:
        return
    confirmar = input(f"Tem certeza que deseja remover {marca} {modelo}? S/N: ").strip().upper()
    if confirmar == "S":
        del catalogo[marca][modelo]
        salvar_catalogo(catalogo)
        print("Modelo removido com sucesso!")
    else:
        print("Operação cancelada.")
 
 
def remover_marca(catalogo):
    marca = escolher_marca(catalogo)
    if marca is None:
        return
    confirmar = input(f"Tem certeza que deseja remover a marca {marca} e TODOS os seus modelos? S/N: ").strip().upper()
    if confirmar == "S":
        del catalogo[marca]
        salvar_catalogo(catalogo)
        print("Marca removida com sucesso!")
    else:
        print("Operação cancelada.")
 
 
# -----------------------------------------------------
# Menu principal
# -----------------------------------------------------
def exibir_menu():
    print("\n" + "=" * 45)
    print("        SOLARIUM - CATÁLOGO DE CARROS")
    print("=" * 45)
    print("  1. Ver marcas")
    print("  2. Ver modelos de uma marca")
    print("  3. Ver detalhes de um modelo")
    print("  4. Adicionar marca")
    print("  5. Adicionar modelo")
    print("  6. Editar modelo")
    print("  7. Remover modelo")
    print("  8. Remover marca")
    print("  0. Sair")
    print("=" * 45)
 
 
def main():
    catalogo = carregar_catalogo()
    print("Seja bem-vindo à SOLARIUM!")
 
    acoes = {
        "1": ver_marcas,
        "2": ver_modelos_de_marca,
        "3": ver_detalhes_modelo,
        "4": adicionar_marca,
        "5": adicionar_modelo,
        "6": editar_modelo,
        "7": remover_modelo,
        "8": remover_marca,
    }
 
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()
 
        if opcao == "0":
            print("Obrigado por visitar a SOLARIUM. Até logo!")
            break
        elif opcao in acoes:
            acoes[opcao](catalogo)
        else:
            print("Opção inválida, tente novamente.")
 
 
if __name__ == "__main__":
    main()