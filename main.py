
#LOJA DE CARROS - SOLARIUM
marcas = ("Audi", "Bugatti", "Chevrolet", "Dodge", "Ferrari", "Hyundai", "Jaguar", "Koenigsegg", "Lamborghini", "Mercedes", "Nissan", "Pagani", "Range Rover", "Subaru", "Toyota", "Volvo")

catalogo = {"Audi": ["A3", "A4", "A5", "A7", "RS3", "RS4", "RS5", "RS6", "Q3", "Q5", "Q7", "Q8", "RSQ8", "TT", "TTRS"]
, "Bugatti": ["Chiron", "Bolide", "Divo", "Veyron", "Tourbillion"]
, "Chevrolet": ["Camaro ZL1", "Camaro ZLE", "Corvette C6", "Corvette C7", "Corvette C8"]
, "Dodge": ["Charger", "Challenger", "Demon", "Viper"]
, "Ferrari": ["330 California", "458 GTB", "458 Pista", "812 Superfast", "LaFerrari", "PuroSangue"]
, "Hyundai": ["Creta", "Elantra", "HB20", "HB20s", "Veloster"]
, "Jaguar": ["F-Type", "E-Pace", "F-Pace", "I-Pace"]
, "Koenigsegg": ["Agera", "Agera RS", "CC8S", "CCGT", "Gemera", "Jesko", "Jesko Absolut", "One:1", "Regera"]
, "Lamborghini": ["Aventador", "Aventador SV", "Aventador SVJ", "Centenário", "Countach", "Diablo", "Gallardo", "Huracán", "Murciélago", "Revuelto", "Sesto Elemento", "Sián", "Urus", "Veneno"]
, "Mercedes": ["AMG GT", "AMG ONE", "CLA", "CLE", "CLS", "G63", "GLA", "GLC", "GLE", "SLC", "SLK", "SLR", "SLS"]
, "Nissan": ["350z", "360z", "370z", "400z","Silvia S13", "Silvia S14", "Silvia S15", "Skyline R33", "Skyline R34", "Skyline R35"]
, "Pagani": ["Huayra", "Huayra Imola", "Huayra R", "Huayra R Evo", "Huayra Roadster", "Utopia", "Zonda F"]
, "Range Rover": ["Evoque", "Velar", "Vogue"]
, "Subaru": ["BRZ", "WRX", "WRX STI"]
, "Toyota": ["Camry", "Celica", "Corolla", "Corolla Cros", "Étios", "GR Corolla", "GR Supra", "GR Yaris", "Hillux", "Prius", "RAV4", "Supra", "SW4", "Tacoma", "Tundra", "Yaris", "Yaris Cross"]
, "Volvo": ["XC 40", "XC 50", "XC 60", "XC 70", "XC 80"]}

print("Seja bem vindo à SOLARIUM!")
def visualizarLoja():
   
    for marca in marcas:
        print(marca)
    carroUsuario = str(input("Qual marca você deseja analisar? "))
    if carroUsuario == "Audi":
        print("Esses são os modelos disponíveis atualmente:\n")
        print(catalogo["Audi"])
    if carroUsuario == "Bugatti":
        print("Esses são os modelos disponíveis atualmente:\n")
        print(catalogo["Bugatti"])
    if carroUsuario == "Chevrolet":
        print("Esses são os modelos disponíveis atualmente:\n")
        print(catalogo["Chevrolet"])
    if carroUsuario == "Dodge":
        print("Esses são os modelos disponíveis atualmente:\n")
        print(catalogo["Dodge"])
    if carroUsuario == "Ferrari":
        print("Esses são os modelos disponíveis atualmente:\n")
        print(catalogo["Ferrari"])
    if carroUsuario == "Hyundai":
        print("Esses são os modelos disponíveis atualmente:\n")
        print(catalogo["Hyundai"])
    if carroUsuario == "Jaguar":
        print("Esses são os modelos disponíveis atualmente:\n")
        print(catalogo["Koenigsegg"])
    if carroUsuario == "Dodge":
        print("Esses são os modelos disponíveis atualmente:\n")
        print(catalogo["Koenigsegg"])
    if carroUsuario == "Lamborghini":
        print("Esses são os modelos disponíveis atualmente:\n")
        print(catalogo["Lamborghini"])
    if carroUsuario == "Mercedes":
        print("Esses são os modelos disponíveis atualmente:\n")
        print(catalogo["Mercedes"])
    if carroUsuario == "Nissan":
        print("Esses são os modelos disponíveis atualmente:\n")
        print(catalogo["Nissan"])
    if carroUsuario == "Pagani":
        print("Esses são os modelos disponíveis atualmente:\n")
        print(catalogo["Pagani"])
    if carroUsuario == "Range Rover":
        print("Esses são os modelos disponíveis atualmente:\n")
        print(catalogo["Range Rover"])
    if carroUsuario == "Subaru":
        print("Esses são os modelos disponíveis atualmente:\n")
        print(catalogo["Subaru"])
    if carroUsuario == "Toyota":
        print("Esses são os modelos disponíveis atualmente:\n")
        print(catalogo["Toyota"])
    if carroUsuario == "Volvo":
        print("Esses são os modelos disponíveis atualmente:\n")
        print(catalogo["Volvo"])
    print("\n")
    voltar = str(input("Deseja voltar ao catálogo? S/N \n"))
    if voltar == "S":
        print(visualizarLoja())
   
       
   
print(visualizarLoja())