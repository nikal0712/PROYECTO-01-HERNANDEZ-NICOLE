#INICIA CÓDIGO
import os
from lifestore_saleslist import lifestore_products, lifestore_sales, lifestore_searches

#DEFINICIÓN DE FUNCIONES
#1ER MENÚ: INICIO DE SESIÓN O REGISTRO
def menu1():
  choice = 0
  while choice != 1 or choice != 2:
    os.system("clear")
    print("      LIFESTORE\n   Administrador\n\nBienvenido a LifeStore\n\n")
    print("Elija entre las siguientes opciones:\n1. Iniciar sesión\n2. Registrarme")
    choice = int(input("Introduzca el número de la opción elegida: "))
    if choice == 1 or choice == 2:
      return choice
    else:
      print("Opción no válida.")
      input("Pulse enter para continuar")

#2DO MENÚ: REPORTES
def menu2():
  choice = 0
  while 1>choice or choice>5:
    os.system("clear")
    print("       LIFESTORE\n     Administrador\n\nBienvenido al analizador\n de datos de LifeStore\n\n")
    print("MENÚ:\n\nVisualizar\n1. Productos más vendidos y productos rezagados\n2. Productos por reseña en el servicio\n3. Total de ingresos y ventas\n4. Sugerencia de estrategia\n\no\n5. Cerrar sesión\n")
    choice = int(input("Introduzca el número de la opción elegida: "))
    if 1<=choice and choice<=5:
      return choice
    else:
      print("Opción no válida.")
      input("Pulse enter para continuar")

#DENTRO DEL MENÚ 1
def options1():
    choice = menu1()
    # INICIO DE SESIÓN
    if choice == 1:
      go_back = ""
      while go_back != "si" or go_back != "no":
        log_in = 0
        error = 0
        os.system("clear")
        print("      LIFESTORE\n    Administrador\n\n   Inicio de sesión\n\n")
        go_back = input("Regresar al menú anterior si/no: ")
        if go_back == "si":
          break
        elif go_back == "no": 
          user_loc = 0
          pss_loc = 0
          while user_loc == 0 or pss_loc == 0:
            i = 0
            tentative_user = input("Usuario: ")
            tentative_pss = input("Contraseña: ")
            for user in users:
                i += 1
                if user == tentative_user:
                  user_loc = i
            if user_loc == 0:
              print("Usuario no existente. ")
              input("Presione enter para continuar. ")
              error = 1
              break
            else:
              i = 0
              for pss in passwords:
                i += 1
                if pss == tentative_pss:
                  pss_loc = i
              if pss_loc == 0 or pss_loc != user_loc:
                print("Contraseña incorrecta. ")
                input("Presione enter para continuar. ")
                error = 1
                break
              elif user_loc == pss_loc:
                log_in = 1
                break
            if error == 1:
              break
          if log_in == 1:
            print("Iniciando sesión.")
            input("Pulse enter para continuar. ")
            break
        else:
          print("Opción no válida.")
          input("Pulse enter para continuar")
      return(log_in)

    #REGISTRO DE USUARIO
    elif choice == 2:
      go_back = ""
      while go_back != "si" or go_back != "no":
        os.system("clear")
        print("      LIFESTORE\n    Administrador\n\n      Registro\n\n")
        go_back = input("Regresar al menú anterior si/no: ")
        if go_back == "si":
          break
        elif go_back == "no": 
          user_name = input("Nombre(s): ")
          #validación: nombre de usuario disponible
          repeated = 1
          while repeated == 1:
            for user in users:
              tentative_user = input("Nombre de usuario: ")
              if user == tentative_user:
                print(f"El nombre de usuario '{tentative_user}' no está disponible. ")
                input("Pulse enter para continuar. ")
              else:
                repeated = 0
                break

          if repeated == 0:
            print("Nombre de usuario disponible. ")
            error = 1
            while error == 1:
              pss1 = input("\nContraseña: ")
              pss2 = input("Confirma tu contraseña: ")
              if pss1 == pss2:
                user_names.append(user_name)
                users.append(tentative_user)
                passwords.append(pss1)
                print("Has sido registrado. ")
                #print("Lista de nombres de los usuarios: ", user_names)
                #print("Lista de usuarios: ", users)
                #print("Lista de contraseñas: ", passwords)
                input("Pulse enter para continuar. ")
                error = 0
              else:
                print("Las contraseñas no son iguales. Vuelve a intentarlo")
                continue
          if error == 0:
            break
        #Opción no válida
        else:
          print("Opción no válida.")
          input("Pulse enter para continuar")
      return(0)
#FIN DE DEFINICIÓN DE FUNCIONES

#INICIO DE SESIÓN Y REGISTRO
user_names = ["Nicole Hernández", "Gabriela Montoya"]
users = ["Nicole", "Gaby"]
passwords = ["0712", "1234"]

x = 0
while x == 0: 
  #REPORTES
  #This is the LifeStore_SalesList data:
    #lifestore_products = [0 id_product, 1 name, 2 price, 3 category, 4 stock]
    #lifestore_searches = [0 id_search, 1 id product]
    #lifestore_sales = [0 id_sale, 1 id_product, 2 score (from 1 to 5), 3 date, 4 refund (1 for true or 0 to false)]

  #1. PRODUCTOS MÁS VENDIDOS Y PRODUCTOS REZAGADOS
    #1.1 Top 10 Productos más vendidos
    #1.2 Top 3 por categoría de Productos más vendidos
    #1.3 Top 10 Productos menos vendidos
    #1.4 Top 3 por categoría de Productos menos vendidos
    #1.5 Top 10 Productos más buscados
    #1.6 Top 3 por categoría de Productos más buscados
    #1.7 Top 10 Productos menos buscados
    #1.8 Top 3 por categoría de Productos menos buscados

  #1.3
  #Construyendo lista sales_count = [id_product, name, qty_sales]
  sales_count = []
  for product in lifestore_products:
    sales_count.append([product[0], product[1], 0])
  for sale in lifestore_sales:
    for count in sales_count:
      if sale[1] == count[0]:
        count[2] += 1
    
  #Convirtiendo sales_count en lista de diccionarios sales_count_as_dict
  sales_count_as_dict = list()
  for sale in sales_count:
    sales_count_as_dict.append({"id_product": sale[0], "name": sale[1], "qty_sales": sale[2]})
  
  sorted_sales_count_reversed = sorted(sales_count_as_dict, key = lambda i: i['qty_sales'])
  #Invirtiendo orden para que queden de mayor a menor número de ventas
  #1.1
  sorted_sales_count = sorted_sales_count_reversed[::-1]
  
  #1.2
  #CATEGORÍAS: procesadores, tarjetas de video, tarjetas madre, discos duros, memorias usb, pantallas, bocinas, audifonos.
  sales_in_procesadores = []
  sales_in_tarjetas_video = []
  sales_in_tarjetas_madre = []
  sales_in_discos_duros = []
  sales_in_memorias_usb = []
  sales_in_pantallas = []
  sales_in_bocinas = []
  sales_in_audifonos = []

  #Clasificando los productos vendidos por categoría
  for sorted_sale in sorted_sales_count:
    for product in lifestore_products:
      #Si el id del producto vendido es igual al id del producto, se recorre entonces la información del producto para clasificarlo en la categoría correspondiente
      if sorted_sale["id_product"] == product[0]:
        if product[3] == "procesadores":
          sales_in_procesadores.append(sorted_sale)
        elif product[3] == "tarjetas de video":
          sales_in_tarjetas_video.append(sorted_sale)
        elif product[3] == "tarjetas madre":
          sales_in_tarjetas_madre.append(sorted_sale)
        elif product[3] == "discos duros":
          sales_in_discos_duros.append(sorted_sale)
        elif product[3] == "memorias usb":
          sales_in_memorias_usb.append(sorted_sale)
        elif product[3] == "pantallas":
          sales_in_pantallas.append(sorted_sale)
        elif product[3] == "bocinas":
          sales_in_bocinas.append(sorted_sale)
        elif product[3] == "audifonos":
          sales_in_audifonos.append(sorted_sale)
        else:
          print("no hubo coincidencia en las categorías")
      else:
        continue
  #1.4
  #Volteando las listas de productos por categorías
  sales_in_procesadores_reversed = sales_in_procesadores[::-1]
  sales_in_tarjetas_video_reversed = sales_in_tarjetas_video[::-1]
  sales_in_tarjetas_madre_reversed = sales_in_tarjetas_madre[::-1]
  sales_in_discos_duros_reversed = sales_in_discos_duros[::-1]  
  sales_in_memorias_usb_reversed = sales_in_memorias_usb[::-1]
  sales_in_pantallas_reversed = sales_in_pantallas[::-1]
  sales_in_bocinas_reversed = sales_in_bocinas[::-1]
  sales_in_audifonos_reversed = sales_in_audifonos[::-1]

  #1.7
  #Construyendo lista search_count = [id_product, name, qty_searches]
  search_count = []
  for product in lifestore_products:
    search_count.append([product[0], product[1], 0])
  for search in lifestore_searches:
    for count in search_count:
      if search[1] == count[0]:
        count[2] += 1
    
  #Convirtiendo search_count en lista de diccionarios search_count_as_dict
  search_count_as_dict = list()
  for search in search_count:
    search_count_as_dict.append({"id_product": search[0], "name": search[1], "qty_searches": search[2]})
    
  sorted_search_count_reversed = sorted(search_count_as_dict, key = lambda i: i['qty_searches'])
  #1.5
  #Invietiendo la lista para tener de mayor a menor número de búsquedas
  sorted_search_count = sorted_search_count_reversed[::-1]
  
  #1.6
  searches_in_procesadores = []
  searches_in_tarjetas_video = []
  searches_in_tarjetas_madre = []
  searches_in_discos_duros = []
  searches_in_memorias_usb = []
  searches_in_pantallas = []
  searches_in_bocinas = []
  searches_in_audifonos = []

  for sorted_search in sorted_search_count:
    for product in lifestore_products:
      if sorted_search["id_product"] == product[0]:
        if product[3] == "procesadores":
          searches_in_procesadores.append(sorted_search)
        elif product[3] == "tarjetas de video":
          searches_in_tarjetas_video.append(sorted_search)
        elif product[3] == "tarjetas madre":
          searches_in_tarjetas_madre.append(sorted_search)
        elif product[3] == "discos duros":
          searches_in_discos_duros.append(sorted_search)
        elif product[3] == "memorias usb":
          searches_in_memorias_usb.append(sorted_search)
        elif product[3] == "pantallas":
          searches_in_pantallas.append(sorted_search)
        elif product[3] == "bocinas":
          searches_in_bocinas.append(sorted_search)
        elif product[3] == "audifonos":
          searches_in_audifonos.append(sorted_search)
        else:
          print("no hubo coincidencia en las categorías")
      else:
        continue
  #1.8
  #Volteando las listas de productos por categorías
  searches_in_procesadores_reversed = searches_in_procesadores[::-1]
  searches_in_tarjetas_video_reversed = searches_in_tarjetas_video[::-1]
  searches_in_tarjetas_madre_reversed = searches_in_tarjetas_madre[::-1]
  searches_in_discos_duros_reversed = searches_in_discos_duros[::-1] 
  searches_in_memorias_usb_reversed = searches_in_memorias_usb[::-1]
  searches_in_pantallas_reversed = searches_in_pantallas[::-1]
  searches_in_bocinas_reversed = searches_in_bocinas[::-1]
  searches_in_audifonos_reversed = searches_in_audifonos[::-1]

  #2. PRODUCTOS POR RESEÑA EN EL SERVICIO
    #2.1 Top 10 Productos mejor reseñados (considerando los devueltos)
    #2.2 Top 10 Productos peor reseñados (considerando los devueltos)
  #2.2
  #Construyendo lista de reseñas por producto 
  scores = [] #scores = [0 id_product, 1 name, 2 avrg_score]
  for product in lifestore_products:
    scores.append([product[0], product[1]])
  for score in scores:
    added_scores = 0
    score_count = 0
    avrg_score = 0
    for sale in lifestore_sales:
      if score[0] == sale[1]:
        added_scores += sale[2]
        score_count += 1
    if score_count == 0:
      score.append(-1) #La reseña = -1 indica que el producto no tiene reseñas
    else:
      avrg_score = added_scores/score_count
      score.append(avrg_score)
    
  #Convirtiendo la lista scores en una lista de diccionarios
  scores_as_dict = list()
  for score in scores:
    scores_as_dict.append({'id_product': score[0], 'name': score[1], 'avrg_score': score[2]})

  #Ordenando la lista scores por "avrg_score"
  sorted_scores_reversed = sorted(scores_as_dict, key = lambda i: i['avrg_score'])
  
  #2.2
  #Invirtiendo lista para tenerla de peor a mejor reseña
  sorted_scores = sorted_scores_reversed[::-1]

  #3. TOTAL DE INGRESOS Y VENTAS
    #3.1 Ingresos promedio mensuales
    #3.2 Total anual de ingresos
    #3.3 Número de ventas promedio mensuales
    #3.4 Total anual de número de ventas
    #3.5 Top 3 meses con más número de ventas en el año
  #Construyendo lista de ventas válidas (sin devolución)
  sales = []
  for sale in lifestore_sales:
    refund = sale[4]
    if refund == 1:
      continue
    else:
      sales.append(sale)
    
  months = ['/01/', '/02/', '/03/', '/04/', '/05/', '/06/', '/07/', '/08/', '/09/', '/10/', '/11/', '/12/']
  month_names = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]

  #Construyendo lista sales_per_month
  sales_per_month = []
  count = 0
  for month in months:
    empty_list = []
    sales_per_month.append(empty_list)

  #Clasificando ventas por meses
  for sale in sales:
    #Datos de la venta
    id_sale = sale[0]
    date_sale = sale[3]
    #Clasificar en mes
    #Comienzo en el mes 0 ('1. Enero')
    month_count = 0
    for month in months:
      if month in date_sale:
        sales_per_month[month_count].append(id_sale)
        continue
      month_count += 1
  monthly_income = []
  price = 0
  for month in sales_per_month: #Consulta los id_sales de c/mes
    income = 0
    num_sales = len(month)
    for i in range(num_sales):
      for sale in lifestore_sales: #Extrae info de la venta (id_producto)
        if month[i] == sale[0]:
          id_product = sale[1]
          for product in lifestore_products:
            if id_product == product[0]:
              price = product[2]
      income += price
      i += 1
    monthly_income.append(income)
    
  #Obtenemos ingresos anuales y promedio mensual
  annual_income = 0
  avrg_income = 0
  for income in monthly_income:
    annual_income += income
  avrg_income = int(annual_income/len(monthly_income))
  monthly_num_sales = []
  for month in sales_per_month:
    monthly_num_sales.append(len(month))
    
  annual_num_sales = 0
  avrg_num_sales = 0
  for num_sales in monthly_num_sales:
    annual_num_sales += num_sales
  avrg_num_sales = int(annual_num_sales/len(monthly_num_sales))
  monthly_num_sales_as_dict = list()
  for i in range(12):
    monthly_num_sales_as_dict.append({'month': month_names[i], 'qty_sales': monthly_num_sales[i]})

  #Ordenamos de mayor a menor el número de ventas por mes
  sorted_monthly_sales_reversed = sorted(monthly_num_sales_as_dict, key = lambda i: i['qty_sales'])
  sorted_monthly_sales = sorted_monthly_sales_reversed[::-1]

  log_in = 0
  while log_in == 0:
    log_in = options1()
  
  choice2 = 0
  while choice2 != 5:
    choice2 = menu2()
    if choice2 == 1:
      os.system("clear")
      print("       LIFESTORE\n     Administrador\n")
      print("TOP 10 PRODUCTOS MÁS VENDIDOS")    
      count = 0
      for sorted_sale in sorted_sales_count:
        count += 1
        if count <= 10:
          print(count, ".",sorted_sale["name"], "\nNo. de ventas:", sorted_sale["qty_sales"], "\n")
        else:
          break  

      print("TOP 3 POR CATEGORÍA")
      print("PROCESADORES: ")
      count = 0
      for procesador in sales_in_procesadores:
        count += 1
        if count <= 3:
          print(count, ".", procesador["name"], "\nNo. de ventas: ", procesador["qty_sales"])
        else:
          break
      
      print("\nTARJETAS DE VIDEO: ")
      count = 0
      for tarjeta_video in sales_in_tarjetas_video:
        count += 1
        if count <= 3:
          print(count, ".", tarjeta_video["name"], "\nNo. de ventas: ", tarjeta_video["qty_sales"])
        else:
          break

      print("\nTARJETAS MADRE: ")
      count = 0
      for tarjeta_madre in sales_in_tarjetas_madre:
        count += 1
        if count <= 3:
          print(count, ".", tarjeta_madre["name"], "\nNo. de ventas: ", tarjeta_madre["qty_sales"])
        else:
          break
      
      print("\nDISCOS DUROS: ")
      count = 0
      for disco_duros in sales_in_discos_duros:
        count += 1
        if count <= 3:
          print(count, ".", disco_duros["name"], "\nNo. de ventas: ", disco_duros["qty_sales"])
        else:
          break
      
      print("\nMEMORIAS USB: ")
      count = 0
      for memoria_usb in sales_in_memorias_usb:
        count += 1
        if count <= 3:
          print(count, ".", memoria_usb["name"], "\nNo. de ventas: ", memoria_usb["qty_sales"])
        else:
          break
      
      print("\nPANTALLAS: ")
      count = 0
      for pantalla in sales_in_pantallas:
        count += 1
        if count <= 3:
          print(count, ".", pantalla["name"], "\nNo. de ventas: ", pantalla["qty_sales"])
        else:
          break
      
      print("\nBOCINAS: ")
      count = 0
      for bocina in sales_in_bocinas:
        count += 1
        if count <= 3:
          print(count, ".", bocina["name"], "\nNo. de ventas: ", bocina["qty_sales"])
        else:
          break
      
      print("\nAUDÍFONOS: ")
      count = 0
      for audifono in sales_in_audifonos:
        count += 1
        if count <= 3:
          print(count, ".", audifono["name"], "\nNo. de ventas: ", audifono["qty_sales"])
        else:
          break
      input("Pulse enter para ver los productos menos vendidos")

      os.system("clear")
      print("       LIFESTORE\n     Administrador\n")
      print("PRODUCTOS MENOS VENDIDOS")
      count = 0
      #Se imprime el Top 10 productos menos vendidos
      for sorted_sale in sorted_sales_count_reversed:
        count += 1
        if count <=10:
          print(count, ".", sorted_sale["name"], "\nNo. de ventas:", sorted_sale["qty_sales"], "\n")
      
      print("TOP 3 POR CATEGORÍA")
      print("PROCESADORES: ")
      count = 0
      for procesador in sales_in_procesadores_reversed:
        count += 1
        if count <= 3:
          print(count, ".", procesador["name"], "\nNo. de ventas: ", procesador["qty_sales"])
        else:
          break
      
      print("\nTARJETAS DE VIDEO: ")
      count = 0
      for tarjeta_video in sales_in_tarjetas_video_reversed:
        count += 1
        if count <= 3:
          print(count, ".", tarjeta_video["name"], "\nNo. de ventas: ", tarjeta_video["qty_sales"])
        else:
          break

      print("\nTARJETAS MADRE: ")
      count = 0
      for tarjeta_madre in sales_in_tarjetas_madre_reversed:
        count += 1
        if count <= 3:
          print(count, ".", tarjeta_madre["name"], "\nNo. de ventas: ", tarjeta_madre["qty_sales"])
        else:
          break
      
      print("\nDISCOS DUROS: ")
      count = 0
      for disco_duros in sales_in_discos_duros_reversed:
        count += 1
        if count <= 3:
          print(count, ".", disco_duros["name"], "\nNo. de ventas: ", disco_duros["qty_sales"])
        else:
          break
      
      print("\nMEMORIAS USB: ")
      count = 0
      for memoria_usb in sales_in_memorias_usb_reversed:
        count += 1
        if count <= 3:
          print(count, ".", memoria_usb["name"], "\nNo. de ventas: ", memoria_usb["qty_sales"])
        else:
          break
      
      print("\nPANTALLAS: ")
      count = 0
      for pantalla in sales_in_pantallas_reversed:
        count += 1
        if count <= 3:
          print(count, ".", pantalla["name"], "\nNo. de ventas: ", pantalla["qty_sales"])
        else:
          break
      
      print("\nBOCINAS: ")
      count = 0
      for bocina in sales_in_bocinas_reversed:
        count += 1
        if count <= 3:
          print(count, ".", bocina["name"], "\nNo. de ventas: ", bocina["qty_sales"])
        else:
          break
      
      print("\nAUDÍFONOS: ")
      count = 0
      for audifono in sales_in_audifonos_reversed:
        count += 1
        if count <= 3:
          print(count, ".", audifono["name"], "\nNo. de ventas: ", audifono["qty_sales"])
        else:
          break
      input("Pulse enter para ver los productos más buscados")

      os.system("clear")
      print("       LIFESTORE\n     Administrador\n")
      print("PRODUCTOS MÁS BUSCADOS")
      count = 0
      for sorted_search in sorted_search_count:
        count += 1
        if count<= 10:
          print(count, ".",sorted_search["name"], "\nNo. de búsquedas:", sorted_search["qty_searches"], "\n")
        else:
          break
      
      print("TOP 3 POR CATEGORÍA")
      print("PROCESADORES: ")
      count = 0
      for procesador in searches_in_procesadores:
        count += 1
        if count <= 3:
          print(count, ".", procesador["name"], "\nNo. de búsquedas: ", procesador["qty_searches"])
        else:
          break
      
      print("\nTARJETAS DE VIDEO: ")
      count = 0
      for tarjeta_video in searches_in_tarjetas_video:
        count += 1
        if count <= 3:
          print(count, ".", tarjeta_video["name"], "\nNo. de búsquedas: ", tarjeta_video["qty_searches"])
        else:
          break

      print("\nTARJETAS MADRE: ")
      count = 0
      for tarjeta_madre in searches_in_tarjetas_madre:
        count += 1
        if count <= 3:
          print(count, ".", tarjeta_madre["name"], "\nNo. de búsquedas: ", tarjeta_madre["qty_searches"])
        else:
          break
      
      print("\nDISCOS DUROS: ")
      count = 0
      for disco_duros in searches_in_discos_duros:
        count += 1
        if count <= 3:
          print(count, ".", disco_duros["name"], "\nNo. de búsquedas: ", disco_duros["qty_searches"])
        else:
          break
      
      print("\nMEMORIAS USB: ")
      count = 0
      for memoria_usb in searches_in_memorias_usb:
        count += 1
        if count <= 3:
          print(count, ".", memoria_usb["name"], "\nNo. de búsquedas: ", memoria_usb["qty_searches"])
        else:
          break
      
      print("\nPANTALLAS: ")
      count = 0
      for pantalla in searches_in_pantallas:
        count += 1
        if count <= 3:
          print(count, ".", pantalla["name"], "\nNo. de búsquedas: ", pantalla["qty_searches"])
        else:
          break
      
      print("\nBOCINAS: ")
      count = 0
      for bocina in searches_in_bocinas:
        count += 1
        if count <= 3:
          print(count, ".", bocina["name"], "\nNo. de búsquedas: ", bocina["qty_searches"])
        else:
          break
      
      print("\nAUDÍFONOS: ")
      count = 0
      for audifono in searches_in_audifonos:
        count += 1
        if count <= 3:
          print(count, ".", audifono["name"], "\nNo. de búsquedas: ", audifono["qty_searches"])
        else:
          break
      input("Pulse enter para ver los productos menos buscados")

      os.system("clear")
      print("       LIFESTORE\n     Administrador\n")
      print("PRODUCTOS MENOS BUSCADOS")
      count = 0
      for sorted_search in sorted_search_count_reversed:
        count += 1
        if count<= 10:
          print(count, ".",sorted_search["name"], "\nNo. de búsquedas:", sorted_search["qty_searches"], "\n")
        else:
          break

      print("TOP 3 POR CATEGORÍA")
      print("PROCESADORES: ")
      count = 0
      for procesador in searches_in_procesadores_reversed:
        count += 1
        if count <= 3:
          print(count, ".", procesador["name"], "\nNo. de búsquedas: ", procesador["qty_searches"])
        else:
          break
      
      print("\nTARJETAS DE VIDEO: ")
      count = 0
      for tarjeta_video in searches_in_tarjetas_video_reversed:
        count += 1
        if count <= 3:
          print(count, ".", tarjeta_video["name"], "\nNo. de búsquedas: ", tarjeta_video["qty_searches"])
        else:
          break

      print("\nTARJETAS MADRE: ")
      count = 0
      for tarjeta_madre in searches_in_tarjetas_madre_reversed:
        count += 1
        if count <= 3:
          print(count, ".", tarjeta_madre["name"], "\nNo. de búsquedas: ", tarjeta_madre["qty_searches"])
        else:
          break
      
      print("\nDISCOS DUROS: ")
      count = 0
      for disco_duros in searches_in_discos_duros_reversed:
        count += 1
        if count <= 3:
          print(count, ".", disco_duros["name"], "\nNo. de búsquedas: ", disco_duros["qty_searches"])
        else:
          break
      
      print("\nMEMORIAS USB: ")
      count = 0
      for memoria_usb in searches_in_memorias_usb_reversed:
        count += 1
        if count <= 3:
          print(count, ".", memoria_usb["name"], "\nNo. de búsquedas: ", memoria_usb["qty_searches"])
        else:
          break
      
      print("\nPANTALLAS: ")
      count = 0
      for pantalla in searches_in_pantallas_reversed:
        count += 1
        if count <= 3:
          print(count, ".", pantalla["name"], "\nNo. de búsquedas: ", pantalla["qty_searches"])
        else:
          break
      
      print("\nBOCINAS: ")
      count = 0
      for bocina in searches_in_bocinas_reversed:
        count += 1
        if count <= 3:
          print(count, ".", bocina["name"], "\nNo. de búsquedas: ", bocina["qty_searches"])
        else:
          break
      
      print("\nAUDÍFONOS: ")
      count = 0
      for audifono in searches_in_audifonos_reversed:
        count += 1
        if count <= 3:
          print(count, ".", audifono["name"], "\nNo. de búsquedas: ", audifono["qty_searches"])
        else:
          break
      input("Pulse enter para continuar")

    elif choice2 == 2:
      os.system("clear")
      print("       LIFESTORE\n     Administrador\n")
      print("        RESEÑAS\n\n")    
      print("TOP 10 PRODUCTOS MEJOR RESEÑADOS")
      count = 0
      for sorted_score in sorted_scores:
        if sorted_score["avrg_score"] >= 0:
          count += 1
          print(count, ".", sorted_score["name"], "\nReseña:", sorted_score["avrg_score"], "\n")
          if count == 10:
            break
        else:
          continue

      print("\nTOP 10 PRODUCTOS PEOR RESEÑADOS")
      count = 0
      for sorted_score in sorted_scores_reversed:
        if sorted_score["avrg_score"] >= 0:
          count += 1
          print(count, ".", sorted_score["name"], "\nReseña:", sorted_score["avrg_score"], "\n")
          if count == 10:
            break
        else:
          continue
      input("Pulse enter para continuar")

    elif choice2 == 3:
      os.system("clear")
      print("       LIFESTORE\n     Administrador\n")
      print("\nINGRESOS")
      print(f"Ingresos promedio mensuales: ${avrg_income}") 
      print(f"Total anual de ingresos: ${annual_income}")
      print("\n\nVENTAS")
      print(f"Número de ventas promedio mensuales: {avrg_num_sales} ventas")
      print(f"Total anual de ventas: {annual_num_sales} ventas")
      print("Meses con mayor número de ventas: ")
      count = 0
      for sorted_sale in sorted_monthly_sales:
        count += 1
        if count <= 3:
          print(count, ".", sorted_sale["month"], ":", sorted_sale["qty_sales"])
        else:
          break
      input("Pulse enter para continuar")

    #4. SUGERENCIA DE ESTRATEGIA
      #Productos a retirar del mercado
      #Cómo reducir acumulación del inventario considerando datos de ingresos y número de ventas mensuales
    elif choice2 == 4:
      os.system("clear")
      print("       LIFESTORE\n     Administrador\n")
      print("SUGERENCIA DE ESTRATEGIA\n\n")
      print("Se sugiere eliminar del inventario aquellos productos con reseñas menores a 2.5 para asegurar que sólo productos de calidad se ofrezcan al cliente.\nEstos productos son:")
      count = 0
      for sorted_score in sorted_scores_reversed:
        if sorted_score["avrg_score"] >= 0 and sorted_score["avrg_score"] < 2.5:
          count += 1
          print(count, ". ID:", sorted_score["id_product"], "\nNombre:", sorted_score["name"], "\nReseña:", sorted_score["avrg_score"], "\n")
        else:
          continue
      print("Asimismo, basados en el número de ventas por producto, se recomienda eliminar del inventario los productos que hayan tenido 0 ventas en los últimos meses.\nEstos productos son:")
      count = 0
      for sorted_sale in sorted_sales_count:
        if sorted_sale["qty_sales"] == 0:
          count += 1
          print(count, ". ID:", sorted_sale["id_product"], "\nNombre:", sorted_sale["name"], "\nNo. de ventas:", sorted_sale["qty_sales"], "\n")
        else:
          continue
      print("También se analizaron el número de ventas por meses y se sugiere implementar dinámicas como descuentos y promociones en los 4 meses con menores ventas.\nEstos meses son:")
      count = 0
      for monthly_sales in sorted_monthly_sales_reversed:
        count += 1
        if count <= 4:
            print(count, ".", monthly_sales["month"], "\nNo. de ventas:", monthly_sales["qty_sales"], "\n")
        else: 
          break
      print("Por último, se sugiere detener la adquisición de productos poco buscados hasta ver un aumento en sus búsquedas y ventas.\nEstos productos son:")
      count = 0
      for sorted_search in sorted_search_count:
        if sorted_search["qty_searches"] <= 10:
          count += 1
          print(count, ". ID:", sorted_search["id_product"], "\nProducto:", sorted_search["name"], "\nNo. de búsquedas:", sorted_search["qty_searches"])
      input("Pulse enter para continuar")
    #5. CERRAR SESIÓN
    elif choice2 == 5:
      print("Cerrando sesión.")
      input("Pulse enter para continuar")
    #Opción nó válida
    else:
      print("Opción no válida.")
      input("Pulse enter para continuar")
