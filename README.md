
# 📣 Power Automate: Publicar mensajes en un canal de Microsoft Teams

Este flujo de Power Automate permite **enviar mensajes automáticamente a un chat grupal de Teams** usando la acción `Post a message in a chat or channel (V3)` y con python. Es útil para notificaciones automáticas, actualizaciones de estado o alertas.

---

## 🚀 Funcionalidad

- Publica un mensaje en un canal específico de Teams.
- Usa formato HTML para enriquecer el contenido.

---

## 🧱 Componentes del flujo

1. **Disparador**  
   Puede ser manual, al recibir una solicitud HTTP o vinculado a otro sistema (SharePoint, Power Apps, Python, etc.)

2. **Acción: `Post a message in a chat or channel (V3)`**
   - `Post as`: Flow bot
   - `Post in`: Canal
   - `Team`: Nombre del equipo
   - `Channel`: Canal deseado
   - `Message type`: HTML
   - `Message`: Texto personalizado o generado dinámicamente

---

## ✍️ Ejemplo de mensaje HTML

```html
Hola equipo,<br>
La tarea se ha completado correctamente.<br>
<strong>Responsable:</strong> Miguel Pazos
