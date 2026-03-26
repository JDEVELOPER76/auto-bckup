import datetime
import os 
import shutil 
import time

DIAS = {
    0: "lunes",
    1: "martes",
    2: "miercoles",
    3: "jueves",
    4: "viernes",
    5: "sabado",
    6: "domingo"
}

class Respaldo:
    def __init__(self, ruta_origen, ruta_destino):
        self.ruta_origen = ruta_origen
        self.ruta_destino = ruta_destino
        self.dias_respaldo = []  # Lista de días
        self.hora_respaldo = None  # Hora única
        self.horas_respaldo = list(range(24))  # Todas las horas del día (0-23)
        self.ultimos_respaldos = {}  # Trackear respaldos por hora
        self.ultimo_respaldo = None  # <--- INICIALIZADO para respaldo_cada_hora()
    
    def establecer_dia(self, dia:str):
        """Agrega un día para el respaldo"""
        if dia.lower() in DIAS.values():
            self.dias_respaldo.append(dia.lower())
            print(f"Días configurados: {self.dias_respaldo}")
    
    def establecer_hora(self, hora:str): 
        """Establece la hora para el respaldo"""
        self.hora_respaldo = datetime.datetime.strptime(hora, "%H:%M").time()
        print(f"Hora configurada: {self.hora_respaldo}")
    
    def respaldo(self, existe:bool):
        """Ejecuta el respaldo"""
        if os.path.exists(self.ruta_origen):
            try:
                shutil.copytree(self.ruta_origen, self.ruta_destino, dirs_exist_ok=existe)
                print(f" Respaldo realizado con éxito a las {datetime.datetime.now()}")
            except Exception as e:
                print(f" Error en respaldo: {e}")
        else:
            print(f" La ruta de origen no existe: {self.ruta_origen}")
    
    def configurar_horas(self, horas:list):
        """Configura horas específicas para respaldar"""
        self.horas_respaldo = horas
        print(f"Horas configuradas: {self.horas_respaldo}")
    
    def respaldo_programado_dias(self, espera:int=60):
        """Ejecuta respaldo según días y hora configurada"""
        if not self.dias_respaldo:
            print("Error: No has configurado ningún día")
            return
        if not self.hora_respaldo:
            print("Error: No has configurado la hora")
            return
        
        print(f" Respaldo programado para: {self.dias_respaldo} a las {self.hora_respaldo}")
        ultimo_respaldo = None
        
        try:
            while True:
                ahora = datetime.datetime.now()
                dia_actual = DIAS[ahora.weekday()]
                
                if dia_actual in self.dias_respaldo:
                    if ahora.time() >= self.hora_respaldo:
                        if ultimo_respaldo != ahora.date():
                            print(f" Ejecutando respaldo programado...")
                            self.respaldo(existe=True)
                            ultimo_respaldo = ahora.date()
                
                time.sleep(espera)
                
        except KeyboardInterrupt:
            print("\n Respaldo programado detenido por el usuario")
    
    def respaldo_cada_hora(self, espera:int=60):
        """Ejecuta respaldo cada 60 minutos desde que se inicializó el script"""
        print(" Iniciando respaldos automáticos cada hora...")
        self.ultimo_respaldo = None  # Reiniciar al iniciar el método
        
        try:
            while True:
                ahora = datetime.datetime.now()
                
                # Verificar si pasó 1 hora desde el último respaldo
                if (self.ultimo_respaldo is None or 
                    (ahora - self.ultimo_respaldo).total_seconds() >= 3600):
                    
                    print(f" Ejecutando respaldo de las {ahora.strftime('%H:%M')}")
                    self.respaldo(existe=True)
                    self.ultimo_respaldo = ahora
                
                time.sleep(espera)
        except KeyboardInterrupt:
            print("\n Respaldo cada hora detenido por el usuario")
    
    def respaldo_por_horas(self, espera:int=30):
        """Ejecuta respaldo en las horas configuradas (en punto exacto)"""
        print(f" Respaldos programados para las horas: {self.horas_respaldo}")
        
        try:
            while True:
                ahora = datetime.datetime.now()
                hora_actual = ahora.hour
                minuto_actual = ahora.minute
                
                # Verificar si la hora actual está en la lista de horas programadas
                if hora_actual in self.horas_respaldo:
                    # Verificar si es minuto 0 y no se ha respaldado esta hora hoy
                    if minuto_actual == 0:
                        clave = f"{ahora.date()}_{hora_actual}"
                        if self.ultimos_respaldos.get(clave) != hora_actual:
                            print(f" Ejecutando respaldo de las {ahora.strftime('%H:%M')}")
                            self.respaldo(existe=True)
                            self.ultimos_respaldos[clave] = hora_actual
                
                time.sleep(espera)
        except KeyboardInterrupt:
            print("\n Respaldo por horas detenido por el usuario")
    
    def respaldo_continuo_historial(self):
        """Crea respaldos por hora en carpetas separadas (mantiene historial)"""
        print(" Iniciando respaldos horarios con historial...")
        ultima_hora = -1
        
        try:
            while True:
                ahora = datetime.datetime.now()
                hora_actual = ahora.hour
                minuto_actual = ahora.minute
                
                if hora_actual != ultima_hora and minuto_actual == 0:
                    # Crear carpeta con fecha y hora
                    carpeta_horario = ahora.strftime("%Y-%m-%d_%H-%M")
                    ruta_destino_horario = os.path.join(self.ruta_destino, carpeta_horario)
                    
                    print(f" Ejecutando respaldo horario: {carpeta_horario}")
                    
                    if os.path.exists(self.ruta_origen):
                        try:
                            shutil.copytree(self.ruta_origen, ruta_destino_horario, dirs_exist_ok=True)
                            print(f" Respaldo guardado en: {ruta_destino_horario}")
                        except Exception as e:
                            print(f" Error en respaldo: {e}")
                    else:
                        print(f" La ruta de origen no existe: {self.ruta_origen}")
                    
                    ultima_hora = hora_actual
                
                time.sleep(30)
        except KeyboardInterrupt:
            print("\n Respaldo con historial detenido por el usuario")

