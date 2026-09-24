import fastf1

# Sesion: GP de Japon 2025, Clasificacion
# Comparando a NOR (McLaren) vs VER (Red Bull)

fastf1.Cache.enable_cache('cache')
session = fastf1.get_session(2025, 'Japan', 'Q')
session.load() 
print("Evento:", session.event['EventName'])
print("Fecha:", session.date)
print("Numero total de vueltas registradas:", len(session.laps))   
print("Pilotos disponibles en la sesion:", session.laps['Driver'].unique())
print("Columnas disponibles en laps:", list(session.laps.columns)) 
nor_Laps = session.laps.pick_driver('NOR') 
ver_laps = session.laps.pick_driver('VER')
print("Vueltas de NOR:", len(nor_Laps))
print("Vueltas de VER:", len(ver_laps))
q1, q2, q3 = session.laps.split_qualifying_sessions()
columnas = ['Driver', 'LapNumber', 'LapTime', 'Compound', 'Stint', 'FreshTyre', 'TrackStatus'] 
q3_nor = q3.pick_driver('NOR') 
q3_ver = q3.pick_driver('VER') 
print("\n--- Vueltas de NOR en Q3 ---")
print(q3_nor[columnas])
print("\n--- Vueltas de VER en Q3 ---")
print(q3_ver[columnas])
nor_pole_lap = q3_nor.pick_fastest() 
ver_pole_lap = q3_ver.pick_fastest()
print("\nVuelta de pole NOR:", nor_pole_lap['LapNumber'], nor_pole_lap['LapTime'])
print("Vuelta de pole VER:", ver_pole_lap['LapNumber'], ver_pole_lap['LapTime'])