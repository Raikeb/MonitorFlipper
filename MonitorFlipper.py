import win32api
import win32con
import pywintypes

# Constantes de orientação
DMDO_DEFAULT = 0    # 0° (paisagem)
DMDO_90 = 1         # 90° (retrato)
DMDO_180 = 2        # 180° (paisagem invertida)
DMDO_270 = 3        # 270° (retrato invertido)

def set_orientation(device_name, orientation):
    try:       
        devmode = win32api.EnumDisplaySettings(device_name, win32con.ENUM_CURRENT_SETTINGS)
		
        if orientation in [DMDO_DEFAULT, DMDO_180]:  
            if devmode.PelsHeight > devmode.PelsWidth:
                devmode.PelsWidth, devmode.PelsHeight = devmode.PelsHeight, devmode.PelsWidth
        else:  
            if devmode.PelsWidth > devmode.PelsHeight:
                devmode.PelsWidth, devmode.PelsHeight = devmode.PelsHeight, devmode.PelsWidth
        
        devmode.DisplayOrientation = orientation
        devmode.Fields = win32con.DM_DISPLAYORIENTATION | win32con.DM_PELSWIDTH | win32con.DM_PELSHEIGHT
               
        result = win32api.ChangeDisplaySettingsEx(device_name, devmode)
        
        if result == win32con.DISP_CHANGE_SUCCESSFUL:
            print(f"✔ Orientação alterada para {orientation}° no monitor {device_name}")
        else:
            print(f"✖ Falha ao alterar (Código: {result}). Talvez o monitor não suporte esta orientação.")
    except pywintypes.error as e:
        print(f"⚠ Erro grave: {e}")

def rotate_display():
    target_device = r"\\.\DISPLAY5"  # Monitor específico que você quer controlar, altere aqui
    
    try:       
        devmode = win32api.EnumDisplaySettings(target_device, win32con.ENUM_CURRENT_SETTINGS)
        current_orientation = devmode.DisplayOrientation
                
        if current_orientation in [DMDO_DEFAULT, DMDO_180]:
            new_orientation = DMDO_90  
        else:
            new_orientation = DMDO_DEFAULT  
        
        print(f"Monitor {target_device} encontrado. Orientação atual: {current_orientation}°")
        set_orientation(target_device, new_orientation)
    except pywintypes.error as e:
        print(f"✖ O monitor {target_device} não pôde ser acessado. Verifique se:")
        print("- O monitor está conectado e ligado")
        print("- O nome está correto (pode variar entre sistemas)")
        print(f"Erro detalhado: {e}")

if __name__ == "__main__":
    rotate_display()