# 🧾 GitHub Activity CLI

Consulta la actividad pública más reciente de cualquier usuario de GitHub directamente desde la terminal.  
Este proyecto es parte del reto de [roadmap.sh](https://roadmap.sh/projects/github-activity) y está diseñado para practicar el uso de APIs, manejo de datos JSON y construcción de herramientas CLI sin dependencias externas.

---

## 🚀 Características

- 🔍 Consulta eventos públicos recientes de cualquier usuario de GitHub
- 📦 Sin dependencias externas (solo módulos estándar de Python)
- 🧠 Interpreta eventos como:
  - Pushes (commits)
  - Issues
  - Stars
  - Forks
  - Pull Requests
- ⚠️ Manejo de errores para usuarios inválidos, errores de red o respuestas inesperadas

---

## 🛠️ Requisitos

- Python 3.7 o superior
- Conexión a internet

---

## 📦 Instalación

```bash
git clone https://github.com/yovidev/github-activity.git
cd github-activity
python -m venv venv
# Activar entorno virtual:
# En PowerShell (Windows):
.\venv\Scripts\Activate.ps1
# En Bash (Linux/macOS):
source venv/bin/activate
```
## Uso
```bash
python github_activity.py <nombre-de-usuario>
```
## Ejemplo
```bash
python github_activity.py kamranahmedse
```
## 🧠 Ideas para extender
- --limit: mostrar más o menos eventos
- --type: filtrar por tipo de evento (solo commits, issues, etc.)
- Cachear resultados para evitar múltiples llamadas a la API
- Mostrar información adicional del usuario (bio, repos, seguidores)
- Exportar resultados a archivo .txt o .json

## 🧪 Testing
Prueba el script con distintos nombres de usuario válidos e inválidos para verificar:
- Que se muestran eventos correctamente
- Que los errores se manejan con mensajes claros
- Que no se rompe si el usuario no tiene actividad reciente


## 🔗 Proyecto en GitHub

Puedes ver el código fuente y contribuir en:  
[https://github.com/yovidev/github-activity](https://github.com/yovidev/github-activity)

---

## 🌐 Página del Proyecto

Este proyecto también está listado en [roadmap.sh](https://roadmap.sh/projects/github-user-activity), una plataforma para descubrir y compartir proyectos prácticos de desarrollo.

¡Visítalo, deja tu feedback y comparte tu versión del GitHub User Activity CLI!








