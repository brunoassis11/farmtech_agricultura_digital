import os
import sys

#classes para organização
class Data:
    def __init__(self, id_cultura, area, quantidade_insumo):
        self.id_cultura = id_cultura
        self.area = area
        self.quantidade_insumo = quantidade_insumo

class DataConfig:
    def __init__(self, nome_cultura, tipo_area, tipo_insumo,quantidade_metro_quadrado):
        self.nome_cultura = nome_cultura
        self.tipo_area = tipo_area
        self.tipo_insumo = tipo_insumo
        self.quantidade_metro_quadrado = quantidade_metro_quadrado

#variaveis para configuração pre definida pelo grupo
tipo_area = ["Retângulo","Quadrado"]
data_config = [DataConfig("Café", tipo_area[0], "Adubo", 200), DataConfig("Soja", tipo_area[1], "Inoculante", 100)]

#vetor principal da memoria
datas = []


def main():
    main_menu()


def main_menu():
    clear_screen()
    while True:
        print("=== FarmTech - Agricultura Digital ===")
        print("--- MENU PRINCIPAL---")
        print("1. Cadastrar dados")
        print("2. Listar dados")
        print("3. Atualizar item")
        print("4. Deletar item")
        print("0. Sair")

        option = input("Escolha uma opção: ")
        if (option == "0"):
            if (close() == "S"):
                sys.exit()
        elif (option == "1"):
            create()
        elif (option == "2"):
            read()     
        elif (option == "3"):
            update()   
        elif (option == "4"):
            delete()
        else:
            print(f"Opção {option} é inválida, digite uma opção entre 0 e 4.")


def close() -> str:
    clear_screen()
    while True:
        print("Tem certeza que deseja sair?")
        print("1. Sim")
        print("2. Não")
        option = input("Escolha uma opção: ")
        if(option == "1"):
            return "S"
        elif (option == "2"):
            return "N"
        else:
            print(f"Opção {option} é inválida, digite uma opção entre 1 e 2.")


def create():
    clear_screen()
    data = process()
    # Finaliza salvando objeto
    datas.append(data)
    return


def read():    
    clear_screen()
    if len(datas) == 0:
        print(f"Nenhum dado gravado, volte ao menu principal e selecione a opção '1' para cadastrar.")
    else:
        for indice, data in enumerate(datas):
            print(f"{indice}. O plantio da cultura {data_config[data.id_cultura].nome_cultura} na área do tipo {data_config[data.id_cultura].tipo_area} do total de {data.area}m² precisa de {data.quantidade_insumo} litros/kg de {data_config[data.id_cultura].tipo_insumo}")
 
    input("Pressione Enter para voltar...")
    return


def update():    
    clear_screen()
    if len(datas) == 0:
        print(f"Nenhum dado gravado, volte ao menu principal e selecione a opção '1' para cadastrar.")
        input("Pressione Enter para voltar...")
        return
    else:
        for indice, data in enumerate(datas):
            print(f"{indice}. O plantio da cultura {data_config[data.id_cultura].nome_cultura} na área do tipo {data_config[data.id_cultura].tipo_area} do total de {data.area}m² precisa de {data.quantidade_insumo} litros/kg de {data_config[data.id_cultura].tipo_insumo}")
    
    option_int = 0
    while True:  
        option = input("Escolha uma opção ou digite 'voltar' para voltar ao menu principal: ")
        if(option.lower() == 'voltar'):
            return              
        elif option.isdigit():
            option_int = int(option)
            if 0 <= option_int < len(datas):
                print(f"Selecionado opção {option_int} para atualizar. (valores atuais: de cultura {data_config[datas[option_int].id_cultura].nome_cultura}, área {data_config[datas[option_int].id_cultura].tipo_area} com {datas[option_int].area}m², insumo {datas[option_int].quantidade_insumo} litros/kg de {data_config[datas[option_int].id_cultura].tipo_insumo})")
                break
            else:
                print(f"Opção {option} é inválida, digite uma opção entre 0 e {len(datas) - 1}.")
        else:
            print(f"Opção {option} não é um número válido, digite uma opção entre 0 e {len(datas) - 1}.")

    dados_atualizados = process()
    # Finaliza atualizando objeto por posição
    datas[option_int] = dados_atualizados
    print("Dados atualizados com sucesso!")
    input("Pressione Enter para continuar...")
    return


def delete():    
    clear_screen()
    if len(datas) == 0:
        print(f"Nenhum dado gravado, volte ao menu principal e selecione a opção '1' para cadastrar.")
        input("Pressione Enter para voltar...")
        return
    else:
        for indice, data in enumerate(datas):
            print(f"{indice}. O plantio da cultura {data_config[data.id_cultura].nome_cultura} na área do tipo {data_config[data.id_cultura].tipo_area} do total de {data.area}m² precisa de {data.quantidade_insumo} litros/kg de {data_config[data.id_cultura].tipo_insumo}")
    
    option_int = 0
    while True:  
        option = input("Escolha uma opção ou digite 'voltar' para voltar ao menu principal: ")
        if(option.lower() == 'voltar'):
            return              
        elif option.isdigit():
            option_int = int(option)
            if 0 <= option_int < len(datas):
                cultura_deletada = data_config[datas[option_int].id_cultura].nome_cultura
                del datas[option_int]
                print(f"O registro do plantio de {cultura_deletada} foi deletado com sucesso.")
                input("Pressione Enter para continuar...")
                break
            else:
                print(f"Opção {option} é inválida, digite uma opção entre 0 e {len(datas) - 1}.")
        else:
            print(f"Opção {option} não é um número válido, digite uma opção entre 0 e {len(datas) - 1}.")


def process() -> Data:
    id_cultura = -1
    area = 0.0
    quantidade_insumo = 0.0
    # Selecionar Cultura
    while True:
        print("As culturas disponíveis:")
        for indice, config_item in enumerate(data_config):
            print(f"{indice}. {config_item.nome_cultura}")

        option = input("Escolha uma opção: ")
        if option.isdigit():
            option_int = int(option)
            if 0 <= option_int < len(data_config):
                print(f"Selecionado {data_config[option_int].nome_cultura}")
                id_cultura = option_int
                break
            else:
                print(f"Opção {option} é inválida, digite uma opção entre 0 e {len(data_config) - 1}.")
        else:
            print(f"Opção {option} não é um número válido, digite uma opção entre 0 e {len(data_config) - 1}.")
    
    # Calcular area
    clear_screen()
    print(f"O plantio da cultura {data_config[id_cultura].nome_cultura} será feito em uma área do tipo {data_config[id_cultura].tipo_area}, por favor infome as medidas para obter a aréa do local.")
    if data_config[id_cultura].tipo_area == "Retângulo":
        comprimento = 0.0
        largura = 0.0
        while True:            
            entrada = input("Por favor informe o comprimento:")
            try:
                comprimento = float(entrada)
                break
            except ValueError:
                print(f"Valor {entrada} digitado é inválido, por favor digite apenas um número.")
        while True:            
            entrada = input("Por favor informe a largura:")
            try:
                largura = float(entrada)
                break
            except ValueError:
                print(f"Valor {entrada} digitado é inválido, por favor digite apenas um número.")
        area = comprimento * largura
    elif data_config[id_cultura].tipo_area == "Quadrado":
        lado = 0.0
        while True:            
            entrada = input("Por favor informe a medida do lado:")
            try:
                lado = float(entrada)
                break
            except ValueError:
                print(f"Valor {entrada} digitado é inválido, por favor digite apenas um número.")
        area = lado  ** 2

    # Calcular Insumo
    clear_screen()
    print(f"O plantio da cultura {data_config[id_cultura].nome_cultura} será feito em uma área do tipo {data_config[id_cultura].tipo_area} do total de {area}m² com insumo {data_config[id_cultura].tipo_insumo}")
    numero_total_ruas = 0
    while True:            
        entrada = input("Por favor informe o número total de ruas:")
        try:
            numero_total_ruas = int(entrada)
            break
        except ValueError:
            print(f"Valor {entrada} digitado é inválido, por favor digite apenas um número inteiro.")
    
    quantidade_insumo = data_config[id_cultura].quantidade_metro_quadrado * area * numero_total_ruas
    print(f"O plantio da cultura {data_config[id_cultura].nome_cultura} na área do tipo {data_config[id_cultura].tipo_area} do total de {area}m² precisa de {quantidade_insumo} litros/kg de {data_config[id_cultura].tipo_insumo}")
    return Data(id_cultura, area, quantidade_insumo)

def clear_screen():
    #limpa terminal (windows ou unix)
    os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
    main()