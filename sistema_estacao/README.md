# AquaGuard IoT (Django)

Sistema Django para monitoramento de qualidade da agua com leitura real do ESP32 via USB serial.

## Funcionalidades

- Dashboard em tempo real com atualizacao a cada 5 segundos
- Graficos de pH e turbidez (Chart.js)
- Historico tabular com status de anomalia
- Central de alertas
- Exportacao CSV
- Ingestao de dados reais recebidos da porta serial do ESP32

## Como executar

```bash
python -m pip install -r requirements.txt
python manage.py runserver
```

Configure as variaveis de ambiente antes de subir o servidor (Windows PowerShell):

```powershell
$env:ESP32_SERIAL_PORT = "/dev/ttyACM0"
$env:ESP32_BAUDRATE = "115200"
python manage.py runserver
```

Formato esperado por linha enviada pelo ESP32:

- JSON: {"ph":7.1,"turbidity":2.8,"temperature":25.3,"tds":310}
- Chave/valor: ph=7.1,turbidity=2.8,temperature=25.3,tds=310

Acesse:

- Dashboard: `http://127.0.0.1:8000/dashboard/`

## Estrutura principal

- `monitoring/simulator.py`: buffer de leituras, regras de alerta e snapshot da API
- `monitoring/serial_reader.py`: leitura serial do ESP32 e ingestao no sistema
- `monitoring/views.py`: dashboard, APIs e CSV
- `templates/dashboard.html`: tela principal
- `static/js/app.js`: atualizacao, renderizacao de cards/tabela/alertas/graficos
- `static/css/app.css`: estilos
