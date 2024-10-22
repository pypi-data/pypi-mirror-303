# neowg

# ВАЖНО, БИБЛИОТЕКА РАБОТАЕТ ТОЛЬКО СО СВОИМ ФОРМАТОМ КОНФИГОВ

## Примеры использования:

### Создание нового конфига

```python
from neowg import WgServerConfig

config = WgServerConfig.new(
    server_ip="<YOUR_WG_SERVER_IP>",
    net_adapter="<YOUR_WG_SERVER_NET_ADAPTER>",
    clients_count=100,
) # Создание объекта конфига
config.dump("wg.conf") # Запись конфига в файл
```

### Чтение конфига из файла.

```python
from neowg import WgServerConfig

config = WgServerConfig.from_file("wg.conf") # Создание объекта конфига
```

### Изменения пары ключей

```python
from neowg import WgServerConfig

config = WgServerConfig.from_file("wg.conf") # Создание объекта конфига
config.update_keys("10.0.0.2")
config.dump("wg.conf")
```
