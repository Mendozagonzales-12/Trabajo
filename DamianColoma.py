#Programa21-calcular el promedio de deuda de un cliente
#Declaracion
deuda_bcp=0.0
deuda_bbva=0.0
deuda_cajas=0.0
deuda_otras=0.0
deuda_promedio=0.0

#Input
deuda_bcp=243.476
deuda_bbva=84.06
deuda_cajas=142.46
deuda_otras=64.38

#Processing
deuda_promedio=(deuda_bcp+deuda_bbva+deuda_cajas+deuda_otras)/4

#Output
print("#######################")
print("#       Infocorp      #")
print("#######################")
print("# deuda_bcp: ",deuda_bcp)
print("# deuda_bbva: ",deuda_bbva)
print("# deuda_cajas: ",deuda_cajas)
print("# deuda_otras: ",deuda_otras)
print("# deuda_promedio: ",deuda_promedio)


#Programa22-calcular importe prestamo
#Declaracion
importe_desembolsado=0.0
tasa_efectiva_anual=0.0
cuotas_año=0
periodo_pago=0
tasa_mensual=0.0
penalidad=0.0
dias_año=0
dias_mes=0
tna=0.0
tda=0.0
tda_ajustada_plazo=0.0

#Input
importe_desembolsado=12000
tasa_efectiva_anual=0.35
cuotas_año=12
periodo_pago=24
tasa_mensual=0.9
penalidad=0.06
dias_año=365
dias_mes=31

#Processing
tna=(1+tasa_efectiva_anual**1/cuotas_año-1*cuotas_año*dias_año/360)
tda=(tasa_mensual*cuotas_año)
tda_ajustada_plazo=(tda/dias_año*dias_mes)

#Output
print("##########################")
print("#           BCP          #")
print("##########################")
print("# importe_desembolsado: ",importe_desembolsado)
print("# tasa_efectiva_anual: ",tasa_efectiva_anual)
print("# cuotas_año: ",cuotas_año)
print("# periodo_pago: ",periodo_pago)
print("# tasa_mensual: ",tasa_mensual)
print("# penalidad: ",penalidad)
print("# dias_año: ",dias_año)
print("# dias_mes: ",dias_mes)
print("# tna: ",tna)
print("# tda: ",tda)
print("# tda_ajustada_plazo: ",tda_ajustada_plazo)


#Programa23-calcular la cuota
monto=0.0
plazo=""
tasa_efectiva_mensual=0.0
comision=0.0
seguro_desgravamen=0.0
saldo_capital=0.0
tea=0.0
ted=0.0
suma_factores=0.0
cuota=0.0

#Input
monto=10000
plazo="36 meses"
tasa_mensual=0.05
comision=3000
seguro_desgravamen=0.09
saldo_capital=2000
suma_factores=27.8916962

#Processing
tea=(1+tasa_mensual)**12-1
ted=(1+tea)**0.0027-1
cuota=(saldo_capital/suma_factores)

#Output
print("############################")
print("#       Banco Ripley       #")
print("############################")
print("# monto: ",monto)
print("# plazo: ",plazo)
print("# tasa_efectiva_mensual: ",tasa_mensual)
print("# seguro_desgravamen: ",seguro_desgravamen)
print("# saldo_capital: ",saldo_capital)
print("# tea: ",tea)
print("# ted: ",ted)
print("# suma_factores: ",suma_factores)
print("# cuota:",cuota)


#Programa24-calcular el promedio de deuda de un cliente
#Declaracion
tasa_de_interes=0.0
capital_prestamo=0.0
plazo_num_cuotas=0
cuota=0.0

#Input
tasa_de_interes=0.028
capital_prestamo=5000
plazo_num_cuotas=12

#Processing
cuota=(capital_prestamo*(1+tasa_de_interes**plazo_num_cuotas*tasa_de_interes/(1+tasa_de_interes)**plazo_num_cuotas)-1)
#Output
print("###############################")
print("#      Caja municipal ica     #")
print("###############################")
print("# tasa_de_interes: ",tasa_de_interes)
print("# capital_prestamo: ",capital_prestamo)
print("# plaza_num_cuotas: ",plazo_num_cuotas)
print("# cuota: ",cuota)


#Programa25-calcular el producto bruto interno
#Declaracion
consumo=0.0
inversion_efectuada=0.0
gasto_publico=0.0
exportaciones=0.0
importaciones=0.0
producto_bruto_interno=0.0

#Input
consumo=600
inversion_efectuada=400
gasto_publico=200
exportaciones=150
importaciones=100

#Processing
producto_bruto_interno=(consumo+inversion_efectuada+gasto_publico+(exportaciones-importaciones))

#Output
print("#######################")
print("#       SENTINEL      #")
print("#######################")
print("# consumo: ",consumo)
print("# inversion_efectuada: ",inversion_efectuada)
print("# gasto_publico: ",gasto_publico)
print("# exportaciones: ",exportaciones)
print("# importaciones: ",importaciones)
print("# producto_bruto_interno: ",producto_bruto_interno)


#Programa26-calcular el importe de interes generado
#Declaracion
capital_inicial=0.0
tiempo=0
interes_simple=0.0
importe_interes_generado=0.0

#Input
capital_inicial=28000
tiempo=3
interes_simple=0.05

#Processing
importe_interes_generado=(capital_inicial*interes_simple*tiempo)

#Output
print("#######################")
print("#       Infocorp      #")
print("#######################")
print("# capital_inicial: ",capital_inicial)
print("# tiempo: ",tiempo)
print("# interes_simple: ",interes_simple)
print("# importe_interes_generado: ",importe_interes_generado)


#Programa27-calcular el importe de interes diario
#Declaracion
saldo_final_dia=0.0
tasa_interes_ahorro=0.0
dias_base_anual=0.0
interes_diario=0.0

#Input
saldo_final_dia=1000
tasa_interes_ahorro=0.01
dias_base_anual=865

#Processing
interes_diario=((saldo_final_dia*tasa_interes_ahorro)/dias_base_anual)

#Output
print("#################################")
print("#        Banco Interbank        #")
print("#################################")
print("# saldo_final_dia: ",saldo_final_dia)
print("# tasa_interes_ahorro: ",tasa_interes_ahorro)
print("# dias_base_anual: ",dias_base_anual)
print("# interes_diario: ",interes_diario)


#Programa28-calcular el mantenimiento de valor cuenta de ahorro
monto_principal=0.0
tipo_cambio_dia_anterior=0.0
cambio_dia_hoy=0.0
mantenimiento_valor_cuenta_de_ahorro=0.0

#Input
monto_principal=200
tipo_cambio_dia_anterior=26.0
cambio_dia_hoy=26.60

#Processing
mantenimiento_valor_cuenta_de_ahorro=(monto_principal/tipo_cambio_dia_anterior*cambio_dia_hoy-monto_principal)

#Output
print("#######################")
print("#         BCR         #")
print("#######################")
print("# monto principal: ",monto_principal)
print("# tipo_cambio_dia_anterior: ",tipo_cambio_dia_anterior)
print("# cambio_dia_hoy: ",cambio_dia_hoy)
print("# mantenimiento_valor_cuenta_de_ahorro: ",mantenimiento_valor_cuenta_de_ahorro)


#Programa29-calcular el promedio de deuda de un cliente
#Declaracion
materia_prima_directa=0.0
materia_prima_comprada=0.0
materia_prima_disponible=0.0
materia_directa_final_disponible=0.0
materia_prima_utilizada=0.0
mano_obra=0.0
costo_indirecto=0.0
producto_proceso=0.0
produc_inicial=0.0
costo_produccion=0.0

#Input
materia_prima_directa=3000
materia_prima_comprada=22000
materia_directa_final_disponible=2000
mano_obra=18000
costo_indirecto=41000
producto_proceso=13500
produc_inicial=14000

#Processing
materia_prima_disponible=(materia_prima_directa+materia_prima_comprada)
materia_prima_utilizada=(materia_prima_disponible+materia_directa_final_disponible)
costo_produccion=(produc_inicial+materia_prima_utilizada+mano_obra+costo_indirecto-producto_proceso)

#Output
print("###############################")
print("#      Caja municipal ica     #")
print("###############################")
print("# materia_prima_directa: ",materia_prima_directa)
print("# materia_prima_comprada: ",materia_prima_comprada)
print("# materia_directa_final_disponible: ",materia_directa_final_disponible)
print("# mano_obra: ",mano_obra)
print("# materia_prima_disponible: ",materia_prima_disponible)
print("# materia_prima_utilizada: ",materia_prima_utilizada)
print("# costo_produccion: ",costo_produccion)


#Programa30-calcular el costo de venta
#Declaracion
existencia_inicial=0
costo_produccion=0.0
existencia_final=0
costo_venta=0.0

#Input
existencia_inicial=3000
costo_produccion=5676
existencia_final=459

#Processing
costo_venta=(existencia_inicial+costo_produccion-existencia_final)

#Output
print("#######################")
print("#      tienda         #")
print("#######################")
print("# existencia_inicial: ",existencia_inicial)
print("# costo_produccion: ",costo_produccion)
print("# existencia_final: ",existencia_final)
print("# costo_venta: ",costo_venta)


#Programa31-calcular la ganacia de una casa comercial
#Declaracion
precio_venta=0.0
ganancia=0.0
precio_compra=0.0

#Input
precio_venta=270
precio_compra=184

#Processing
ganancia=(precio_venta-precio_compra)

#Output
print("################################")
print("#         casa comercial       #")
print("################################")
print("# precio_venta: ",precio_venta)
print("# precio_compra: ",precio_compra)
print("# ganancia: ",ganancia)


#Programa32-calcular el precio de venta
#Declaracion
precio_venta=0.0
ganancia=0.0
precio_compra=0.0

#Input
ganancia=300
precio_compra=2100

#Processing
precio_venta=(precio_compra+ganancia)

#Output
print("################################")
print("#        centro comercial      #")
print("################################")
print("# precio_compra: ",precio_compra)
print("# ganancia: ",ganancia)
print("# precio_venta: ",precio_venta)


#Programa33 calcular el igv
#Declaracion
monto_total=0.0
base=0.0
igv=0.0

#Input
monto_total=5000

#Processing
base=monto_total/(1+0.18)
igv=(monto_total-base)

#Output
print("################################")
print("#        centro comercial      #")
print("################################")
print("# monto_total: ",monto_total)
print("# base: ",base)
print("# igv: ",igv)


#Programa34-calcular el precio de venta
#Declaracion
peso=0.0
altura=0.0
masa_corporal=0.0

#Input
peso=77
altura=1.73

#Processing
masa_corporal=(peso/altura**2)

#Output
print("################################")
print("#        centro comercial      #")
print("################################")
print("# peso: ",peso)
print("# altura: ",altura)
print("# masa_corporal ",masa_corporal)


#Programa35 calcular la demanda potencial
#Declaracion
numero_personas=0
precio=0.0
numero_horas_semana=0
demanda_potencial=0.0

#Input
numero_personas=119
precio=1.43
numero_horas_semana=30


#Processing
demanda_potencial=(numero_personas*precio*numero_horas_semana)

#Output
print("################################")
print("#            Empresa           #")
print("################################")
print("# numero_personas: ",numero_personas)
print("# precio: ",precio)
print("# numero_horas_semana: ",numero_horas_semana)
print("# demanda_potencial: ",demanda_potencial)


#Programa36 calcular la demanda potencial
#Declaracion
precio_costo=0.0
utilidad=0.0
impuesto=0.0
precio_venta=0.0

#Input
precio_costo=1000
utilidad=0.25
impuesto=0.07


#Processing
precio_venta=(precio_costo/1-0.25*1+0.07)

#Output
print("################################")
print("#          minimarket          #")
print("################################")
print("# precio_costo: ",precio_costo)
print("# utilidad: ",utilidad)
print("# impuesto: ",impuesto)
print("# precio_venta: ",precio_venta)


#Programa37 calcular la utilidad bruta
#Declaracion
facturacion=0.0
sueldo=0.0
materiales=0.0
transporte=0.0
utilidad_neta=0.0

#Input
facturacion=20000
sueldo=4000
materiales=6000
transporte=500

#Processing
utilidad_neta=(facturacion-sueldo-materiales-transporte
          )
#Output
print("################################")
print("#           botica             #")
print("################################")
print("# facturacion: ",facturacion)
print("# sueldo: ",sueldo)
print("# materiales: ",materiales)
print("# transporte: ",transporte)
print("# utilidad_neta: ",utilidad_neta)


#Programa38 calcular el costo variable unitario
#Declaracion
costo_fijo_unitario=0.0
costo_variable_unitario=0.0
unidades=0
ganancia=0.0
valor_venta=0.0

#Input
costo_fijo_unitario=10
costo_variable_unitario=15
unidades=400
ganancia=500

#Processing
valor_venta=(costo_fijo_unitario*unidades+costo_variable_unitario*unidades)

#Output
print("################################")
print("#          minimarket          #")
print("################################")
print("# costo_fijo_unitario: ",costo_fijo_unitario)
print("# costo_variable_unitario: ",costo_variable_unitario)
print("# unidades: ",unidades)
print("# ganancia: ",ganancia)


#Programa39 calcular el costo variable unitario
#Declaracion
materia_prima=0.0
costo_empaques=0.0
costo_embalaje=0.0
costo_variable_unitario=0.0

#Input
materia_prima=145
costo_empaques=15
costo_embalaje=10

#Processing
costo_variable_unitario=(materia_prima+costo_embalaje+costo_empaques)

#Output
print("################################")
print("#          ferreteria          #")
print("################################")
print("# materia_prima: ",materia_prima)
print("# costo_empaques: ",costo_empaques)
print("# costo_embalaje: ",costo_embalaje)
print("# costo_variable_unitario: ",costo_variable_unitario)


#Programa20 calcular el costo variable unitario
#Declaracion
precio=0.0
costo=0.0
utilidad=0.0

#Input
precio=6000
costo=1.2

#Processing
utilidad=(precio*costo)

#Output
print("################################")
print("#          ferreteria          #")
print("################################")
print("# precio: ",precio)
print("# costo: ",costo)
print("# utilidad: ",utilidad)

