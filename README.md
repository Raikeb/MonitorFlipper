---

# MonitorFlipper 🖥️🔄  

A simple tool to rotate your secondary monitor (e.g., `\\.\DISPLAY5`) between **landscape** and **portrait** modes.  

---

## 📦 **Contents**  
- `dist/MonitorFlipper.exe`: Ready-to-use executable (no Python required).  
- `MonitorFlipper.py`: Source code (modifiable).  
- `CheckActiveMonitors.py`: Helper script to identify active monitors.  

---

## 🚀 **How to Use**  

### For End Users (No Python Needed):  
1. Download the `MonitorFlipper.exe` from the `dist` folder.  
2. Double-click to run.  
   - *It will automatically toggle the **other monitor** (if match default: `DISPLAY5`).*  

### For Advanced Users (Customization):  
1. **Identify your target monitor**:  
   - Run `CheckActiveMonitors.py` to list active displays (e.g., `DISPLAY1`, `DISPLAY5`, etc).  
   - Note the device name (e.g., `\\.\DISPLAY5`).  

2. **Modify the script**:  
   - Open `MonitorFlipper.py` and replace `\\.\DISPLAY5` with your monitor’s name.  

3. **Rebuild the executable**:  
   ```sh
   pip install pyinstaller
   pyinstaller --onefile --windowed MonitorFlipper.py
   ```  
   - The new `.exe` will be in `dist/`.  

---

## ⚙️ **Development Requirements**  
To edit the script or rebuild:  
- **Python 3.8+** (recommended for compatibility).  
- Dependencies:  
  ```sh
  pip install pywin32 pyinstaller
  ```  

---

## ❓ **Troubleshooting**  
- **"Monitor not found"**: Ensure the monitor is active (use `CheckActiveMonitors.py`).  
- **Antivirus blocks .exe**: Add an exception or rebuild on the target PC.  
- **No rotation support**: Some monitors/drivers may restrict orientation changes.  

---

# MonitorFlipper (Português) 🖥️🔄  

Programa simples para alternar o monitor secundário (ex.: `\\.\DISPLAY5`) entre **paisagem** e **retrato**.  

---

## 📦 **Conteúdo**  
- `dist/MonitorFlipper.exe`: Executável pronto para uso (não requer Python).  
- `MonitorFlipper.py`: Código-fonte (personalizável).  
- `CheckActiveMonitors.py`: Script auxiliar para identificar monitores ativos.  

---

## 🚀 **Como Usar**  

### Para Usuários Comuns (Sem Python):  
1. Baixe o `MonitorFlipper.exe` na pasta `dist`.  
2. Execute com dois cliques.  
   - *Ele alternará automaticamente o **outro monitor** (se corresponder ao padrão: `DISPLAY5`).*  

### Para Personalização:  
1. **Identifique seu monitor**:  
   - Execute `CheckActiveMonitors.py` para listar monitores ativos (ex.: `DISPLAY1`, `DISPLAY5`, etc).  
   - Anote o nome do dispositivo (ex.: `\\.\DISPLAY5`).  

2. **Edite o script**:  
   - Abra `MonitorFlipper.py` e substitua `\\.\DISPLAY5` pelo nome do seu monitor.  

3. **Recrie o executável**:  
   ```sh
   pip install pyinstaller
   pyinstaller --onefile --windowed MonitorFlipper.py
   ```  
   - O novo `.exe` estará em `dist/`.  

---

## ⚙️ **Requisitos para Desenvolvimento**  
Para editar ou recompilar:  
- **Python 3.8+** (recomendado para compatibilidade).  
- Dependências:  
  ```sh
  pip install pywin32 pyinstaller
  ```  

---

## ❓ **Solução de Problemas**  
- **"Monitor não encontrado"**: Verifique se o monitor está ativo (use `CheckActiveMonitors.py`).  
- **Antivírus bloqueia o .exe**: Adicione uma exceção ou recompile no PC alvo.  
- **Sem suporte a rotação**: Alguns monitores/drivers não permitem mudanças de orientação.  

--- 

