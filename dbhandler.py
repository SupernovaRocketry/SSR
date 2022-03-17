import sqlite3
from threading import Lock

class DBHandler():
    """
    Classe para a manipulação do banco de dados
    """

    def __init__(self,tablename):
        """
        Construtor
        :param tablename: Nome da tabela (Nome da missão)
        """
        self._dbpath = 'db\\scada.db'
        self._tablename = tablename
        self._col_names = ["Altitude", 
                        "Latitude", 
                        "Longitude", 
                        "Principal_Paraquedas_Estabilizador",
                        "Redundancia_Paraquedas_Estabilizador",
                        "Comercial_Paraquedas_Estabilizador",
                        "Principal_Paraquedas_Principal",
                        "Comercial_Paraquedas_Principal",
                        "Acelerometro_X",
                        "Acelerometro_Y",
                        "Acelerometro_Z",
                        "Giroscopio_Roll",
                        "Giroscopio_Pitch",
                        "Giroscopio_Yaw",
                        "RSSI"
        ]
        

    def conect(self):
        self._con = sqlite3.connect(self._dbpath, check_same_thread = False)
        self._cursor = self._con.cursor()
        self._lock = Lock()
        self._createTable()

    def __del__(self):
        self._con.close()

    def _createTable(self):
        """
        Método que cria a tabela para armazenamento dos dados caso ela não exista
        """
        try:
            sql_str = f"""
            CREATE TABLE IF NOT EXISTS {self._tablename} (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                timestamp TEXT NOT NULL,
                """
            for n in self._col_names:
                sql_str += f'{n} REAL,'
            
            sql_str = sql_str[:-1]
            sql_str += ');'
            self._lock.acquire()
            self._cursor.execute(sql_str)
            self._con.commit()            
        except Exception as e:
            print("Erro CreateTable: ",e.args)
        finally:
            self._lock.release()

    def insertData(self, data):
        """
        Método para a inserção de dados no banco de dados
        :param data: json ou dicionario contendo todos os dados para a inserção
        """
        try:
            self._lock.acquire()
            self._data = self._handleData(data)
            timestamp = str(data['timestamp'])
            str_cols = 'timestamp,' + ','.join(data.keys())
            str_values = f"'{timestamp}'," + ','.join(str(data[k]) for k in data.keys())
            sql_str = f'INSERT INTO {self._tablename} ({str_cols} VALUES {str_values})'
            self._cursor.execute(sql_str)
            self._con.commit()            
        except Exception as e:
            print("Erro insertData: ",e.args())
        finally:
            self._lock.release()


    def _handleData(self, data):
        try:
            newData = {"Altitude" : data['Altitude'], 
                        "Latitude" : data['Latitude'], 
                        "Longitude" : data['Longitude'], 
                        "Principal Paraquedas Estabilizador" : data['Principal Paraquedas Estabilizador'],
                        "Redundancia Paraquedas Estabilizador" : data['Redundancia Paraquedas Estabilizador'],
                        "Comercial Paraquedas Estabilizador" : data['Comercial Paraquedas Estabilizador'],
                        "Principal Paraquedas Principal" : data['Principal Paraquedas Principal'],
                        "Comercial Paraquedas Principal" : data['Comercial Paraquedas Principal'],
                        "Acelerometro_X" : data['Acelerometro']['x'],
                        "Acelerometro_Y" : data['Acelerometro']['y'],
                        "Acelerometro_Z" : data['Acelerometro']['z'],
                        "Giroscopio_Roll" : data['Giroscopio']['x'],
                        "Giroscopio_Pitch" : data['Giroscopio']['y'],
                        "Giroscopio_Yaw" : data['Giroscopio']['z'],
                        "RSSI" : data['RSSI']}
        
            return newData
        except Exception as e:
            print("Falha ao tratar dados: ",e.args())

    def selectData(self, cols):
        """
        Método que realiza a busca no BD para utilizar nos relatorios automatizados
        """
        try:
            self._lock.acquire()

            self._cursor.execute(sql_str)
            self._con.commit()
            self._lock.release()
        except Exception as e:
            print("Erro: ",e.args())