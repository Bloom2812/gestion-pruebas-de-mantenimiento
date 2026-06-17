# Manual de Usuario - CMMS Corinfar

**Sistema de Gestión de Mantenimiento Integral**  
Versión 2.0 | Documentación confidencial | Actualizado: junio de 2026

---

## Índice

1. [Introducción](#1-introducción)
2. [Primer ingreso y definición de contraseña](#2-primer-ingreso-y-definición-de-contraseña)
3. [Acceso al sistema](#3-acceso-al-sistema)
4. [Conceptos básicos](#4-conceptos-básicos)
5. [Guía para el Operario](#5-guía-para-el-operario)
6. [Guía para el Técnico](#6-guía-para-el-técnico)
7. [Guía para el Supervisor de Área](#7-guía-para-el-supervisor-de-área)
8. [Guía para el Jefe de Área](#8-guía-para-el-jefe-de-área)
9. [Administración, roles y permisos](#9-administración-roles-y-permisos)
10. [Órdenes de Trabajo](#10-órdenes-de-trabajo)
11. [Inventario, repuestos e insumos](#11-inventario-repuestos-e-insumos)
12. [Dashboard y KPIs](#12-dashboard-y-kpis)
13. [Seguridad y firmas electrónicas](#13-seguridad-y-firmas-electrónicas)
14. [Integración con Odoo](#14-integración-con-odoo)
15. [Uso en móvil o tablet](#15-uso-en-móvil-o-tablet)
16. [Buenas prácticas y solución de problemas](#16-buenas-prácticas-y-solución-de-problemas)

---

## 1. Introducción

El CMMS Corinfar centraliza la gestión de mantenimiento preventivo y correctivo, la administración de activos, el control de repuestos, la evaluación de trabajos y la trazabilidad requerida por calidad. La aplicación está diseñada para que cada rol vea únicamente la información y las acciones que necesita.

![Dashboard principal](manual_images/dashboard_light.png)

El sistema permite:

- Reportar fallas y solicitudes de insumos desde planta.
- Convertir solicitudes en Órdenes de Trabajo (OT).
- Programar y ejecutar mantenimientos preventivos.
- Registrar tiempos, repuestos, observaciones y firmas.
- Evaluar la calidad del trabajo realizado.
- Consultar KPIs como MTBF, MTTR, disponibilidad, costos y cumplimiento.
- Mantener evidencia trazable para auditorías.

---

## 2. Primer ingreso y definición de contraseña

Cuando el administrador crea un usuario nuevo, el sistema genera un enlace de activación para que el usuario defina su propia contraseña. La contraseña solo debe conocerla el usuario; no debe ser creada, solicitada ni compartida por otra persona.

Ejemplo del enlace que recibirá el usuario:

<https://gestion-de-mantenimeinto.web.app/index.htmltoken=j67ysqdfzyci4liu36xe>

### 2.1 Definir la contraseña por primera vez

1. Abra el enlace de activación recibido.
2. Verifique que la pantalla muestre **Definir Contraseña** y su nombre de usuario.
3. Escriba su nueva contraseña en el campo **Nueva Contraseña**.
4. Vuelva a escribir la misma contraseña en **Confirmar Contraseña**.
5. Presione **Guardar Contraseña**.
6. Una vez guardada, use esa contraseña para ingresar normalmente al sistema.

![Pantalla para definir contraseña](manual_images/definir_contrasena.png)

Use una contraseña personal. No la comparta, porque también funciona como firma electrónica en acciones críticas del sistema.

---

## 3. Acceso al sistema

### 3.1 Iniciar sesión

1. Abra el navegador e ingrese a la dirección indicada por IT: <https://gestion-de-mantenimeinto.web.app/index.html>.
2. Escriba su usuario con el formato **Primer Nombre + espacio + Primer Apellido**. La primera letra del nombre y del apellido debe ir en mayúscula, y no debe dejar espacios al final. Ejemplo: **Ana Martinez**.
3. Ingrese su contraseña.
4. Presione **Iniciar Sesión**.

![Pantalla de acceso](manual_images/acceso_sistema.png)

### 3.2 Recuperar contraseña

1. En la pantalla de inicio, seleccione **¿Olvidó su contraseña**.
2. Escriba su usuario.
3. Presione **Notificar al Administrador**.
4. Espere el enlace seguro de recuperación.

![Recuperación de contraseña](manual_images/olvido_contrasena_modal.png)

---

## 4. Conceptos básicos

### 4.1 Solicitud

Una solicitud es un reporte inicial creado por Operarios, Supervisores o usuarios autorizados. Puede ser una falla de máquina, una necesidad de mantenimiento o un pedido de repuestos/insumos.

### 4.2 Orden de Trabajo (OT)

La OT es el registro formal del trabajo técnico. Contiene el equipo, descripción, responsable, fechas, tiempos, repuestos, evidencias, firmas y cierre.

### 4.3 Mantenimiento preventivo (MP)

Es un trabajo programado para evitar fallas. Normalmente nace desde un plan de mantenimiento y requiere validaciones formales al finalizar.

### 4.4 Mantenimiento correctivo

Es una intervención generada por una falla o condición inesperada. Puede iniciar desde una solicitud de mantenimiento.

### 4.5 Estados habituales

| Estado | Significado |
| --- | --- |
| Pendiente | La solicitud fue creada y espera revisión. |
| Planificada | Ya existe programación, responsable o fecha tentativa. |
| En Ejecución | El técnico está trabajando en la OT. |
| Pausada | El trabajo se detuvo temporalmente por repuestos, turno, terceros u otra causa. |
| Pendiente de Evaluación | El técnico finalizó y el usuario responsable debe validar el resultado. |
| Evaluada / Finalizada | El trabajo fue revisado y cerrado. |
| Cancelada | La solicitud u OT no procede o fue anulada. |

---

## 5. Guía para el Operario

El Operario reporta fallas, solicita insumos y valida si el trabajo realizado resolvió la necesidad de planta.

### 5.1 Crear una solicitud de mantenimiento

1. Ingrese al módulo **Solicitudes** desde el menú lateral.
2. Presione **Nueva Solicitud**.
3. Seleccione el tipo **Mantenimiento**.
4. Busque y seleccione la máquina afectada.
5. Describa el problema de forma clara: qué ocurre, cuándo inició, ruido, fuga, alarma, parada, producto afectado u otra evidencia.
6. Seleccione la urgencia.
7. Guarde o envíe la solicitud.

![Ubicación del módulo Solicitudes](manual_images/sidebar_solicitudes.png)

![Ejemplo de solicitud llena](manual_images/nueva_solicitud_llena.png)

### 5.2 Solicitar repuestos, accesorios o consumibles

1. Presione **Nueva Solicitud**.
2. Seleccione **Insumos / Accesorios**.
3. Busque el ítem por nombre, código o descripción.
4. Agregue cantidad y motivo.
5. Revise el detalle antes de enviar.
6. Envíe la solicitud para revisión y aprobación.

![Búsqueda de repuestos](manual_images/busqueda_repuestos.png)

![Detalle de solicitud](manual_images/solicitud_detalle.png)

### 5.3 Revisar mis solicitudes

En **Mis Solicitudes** puede ver:

- Número de solicitud.
- Máquina o insumo relacionado.
- Estado actual.
- OT vinculada, si ya fue generada.
- Técnico responsable, cuando aplique.
- Fechas y avance.

![Panel de solicitudes del operario](manual_images/solicitudes_operario.png)

### 5.4 Evaluar el trabajo realizado

Cuando el técnico marque el trabajo como terminado:

1. Busque la solicitud con estado **Pendiente de Evaluación**.
2. Presione **Evaluar**.
3. Revise que la máquina opere correctamente.
4. Marque los criterios solicitados.
5. Califique con estrellas cuando el sistema lo solicite.
6. Agregue un comentario si hubo observaciones.
7. Confirme con su contraseña para firmar electrónicamente.

![Firma de seguridad](manual_images/firma_seguridad.png)

### 5.5 Ficha del equipo

La ficha del equipo reúne información técnica y documental de la máquina. Puede abrirla al hacer clic sobre el nombre del equipo en listas, solicitudes, OT o tableros.

![Ficha del equipo y documentación](manual_images/ficha_equipo_documentacion.png)

En la ficha encontrará:

- Datos técnicos, marca, modelo, serie y ubicación.
- Clasificación técnica y regulatoria.
- Estado de calificación IQ/OQ/PQ.
- Historial de mantenimientos.
- Repuestos vinculados.
- Manual de usuario y manual técnico, si están cargados.

---

## 6. Guía para el Técnico

El Técnico ejecuta las OT, registra evidencias, controla repuestos y mantiene actualizado el estado del trabajo.

### 6.1 Revisar trabajos asignados

Ingrese a **Trabajo Activo**, **Planificador** o el módulo asignado por su perfil para ver las OT pendientes, planificadas o en ejecución.

![Trabajo activo técnico](manual_images/tecnico_trabajo_activo.png)

### 6.2 Iniciar una OT

1. Abra la OT asignada.
2. Revise máquina, prioridad, descripción, plan y repuestos sugeridos.
3. Verifique condiciones de seguridad antes de intervenir.
4. Presione la acción de inicio disponible.
5. Si el sistema solicita repuestos iniciales, confirme o genere la solicitud correspondiente.

![Detalle de OT técnico](manual_images/tecnico_ot_detalles.png)

### 6.3 Registrar avances, pausas y observaciones

Durante la ejecución:

- Registre observaciones relevantes.
- Pause la OT si debe esperar repuestos, permisos, terceros o liberación de producción.
- Reanude cuando el impedimento termine.
- Mantenga actualizada la información para que Operarios, Supervisores y Jefes vean el avance real.

### 6.4 Gestionar repuestos e insumos

Si la OT requiere materiales:

1. Abra la sección de repuestos de la OT.
2. Busque el repuesto en inventario.
3. Agregue cantidad solicitada o usada.
4. Genere la solicitud si requiere aprobación.
5. Confirme el consumo real al cierre.

![Repuestos externos en OT](manual_images/tecnico_ot_repuestos_externos.png)

### 6.5 Ejecutar planes de mantenimiento

Para trabajos preventivos:

1. Abra el plan programado.
2. Revise actividades, frecuencia, equipo y responsable.
3. Ejecute cada tarea según el procedimiento.
4. Marque actividades realizadas.
5. Registre hallazgos, mediciones, repuestos y recomendaciones.
6. Finalice la OT para activar la evaluación del área correspondiente.

![Ejecución de plan de mantenimiento](manual_images/tecnico_ejecucion_plan_osmosis.png)

### 6.6 Finalizar una OT

Antes de finalizar:

- Confirme que el equipo quedó operativo o deje documentada la condición final.
- Registre repuestos consumidos.
- Complete observaciones técnicas.
- Adjunte evidencia si aplica.
- Revise tiempos reales de intervención.
- Marque la OT como finalizada.

![Evaluación con estrellas](manual_images/tecnico_evaluacion_estrellas.png)

### 6.7 Notificaciones

El sistema puede enviar avisos por Telegram para eventos como solicitudes, alertas de monitoreo, recepción de materiales o acciones administrativas.

![Notificación de Telegram](manual_images/tecnico_telegram_notif.png)

---

## 7. Guía para el Supervisor de Área

El Supervisor controla los trabajos asociados a los equipos de su área, confirma recepciones y participa en la evaluación final.

### 7.1 Tablero de control

Use el tablero para ver solicitudes y OT por estado:

- Solicitudes pendientes.
- Trabajos planificados.
- Trabajos en ejecución.
- Trabajos pausados.
- Pendientes de evaluación.
- Evaluados.
- Cancelados.

![Tablero supervisor](manual_images/supervisor_kanban.png)

### 7.2 Planificación y seguimiento

Revise el planificador para anticipar mantenimientos, coordinar ventanas de producción y detectar atrasos.

![Planificador supervisor](manual_images/supervisor_planificador.png)

### 7.3 Solicitudes de insumos y recepción

Cuando una solicitud de insumos sea aprobada y entregada:

1. Abra la solicitud correspondiente.
2. Revise ítems, cantidades y referencia.
3. Presione **Confirmar Recepción**.
4. Ingrese su contraseña para firmar.
5. Verifique el PDF generado o el registro de recepción.

![Confirmación de recepción](manual_images/supervisor_recepcion_modal.png)

![Formato PDF generado](manual_images/formato_pdf_lleno.png)

### 7.4 Evaluación final

El Supervisor puede completar criterios de calidad, limpieza, operatividad, seguridad y cumplimiento. En algunos casos la evaluación se complementa con la firma del Operario o Jefe de Área.

![Evaluación supervisor](manual_images/supervisor_evaluacion_modal.png)

Si una parte ya evaluó y falta la segunda, el sistema mostrará un estado parcial.

![Evaluación parcial](manual_images/supervisor_parcialmente_evaluado.png)

---

## 8. Guía para el Jefe de Área

El Jefe de Área supervisa disponibilidad, aprueba recursos y valida trabajos críticos o preventivos en su área.

### 8.1 Equipos a cargo

Su vista se filtra según los activos asignados. Desde allí puede consultar estado, historial, planificación y KPIs de sus máquinas.

### 8.2 Aprobación de repuestos e insumos

1. Ingrese a **Solicitudes de Repuestos**.
2. Revise las solicitudes en estado pendiente.
3. Verifique motivo, cantidad, equipo y prioridad.
4. Apruebe o rechace según corresponda.
5. Si rechaza, agregue una razón clara.

![Aprobación de insumos por jefe](manual_images/jefe_aprobacion_insumos.png)

### 8.3 Evaluación de mantenimientos preventivos

En mantenimientos preventivos, la firma del Jefe de Área certifica que el equipo puede continuar operación bajo los estándares definidos.

1. Abra el trabajo pendiente de evaluación.
2. Revise actividades realizadas y observaciones técnicas.
3. Complete criterios de evaluación.
4. Agregue comentario si aplica.
5. Confirme con contraseña.

![Evaluación jefe de área](manual_images/jefe_evaluacion_modal.png)

### 8.4 Control de planificación y KPIs

Use el planificador para controlar cumplimiento de MP, atrasos, carga de trabajo, costos y disponibilidad.

![Planificador jefe](manual_images/jefe_planificador.png)

---

## 9. Administración, roles y permisos

| Rol | Funciones principales |
| --- | --- |
| Admin | Control total, usuarios, configuración, auditoría, seguridad y reportes. |
| Planificador | Programación de trabajos, seguimiento de planes y coordinación de OT. |
| Jefe de Área | Supervisión de activos, aprobación de insumos y evaluación de MP. |
| Supervisor de Área | Seguimiento operativo, recepción de materiales y evaluación final. |
| Técnico | Ejecución de OT, registro de tiempos, repuestos y observaciones. |
| Operario | Reporte de fallas, solicitudes de insumos y evaluación de trabajos. |

Los permisos pueden variar según la configuración del administrador. Si no ve un módulo o botón, valide primero que su rol tenga acceso.

---

## 10. Órdenes de Trabajo

Una OT contiene la información formal de una intervención de mantenimiento.

![Detalle de OT](manual_images/modal_ot.png)

### 10.1 Datos habituales de una OT

- ID o número de OT.
- Tipo: preventiva, correctiva u otra clasificación definida.
- Máquina o activo.
- Descripción del problema o plan.
- Técnico líder y técnicos de apoyo.
- Fechas planificadas y reales.
- Estado.
- Repuestos solicitados o consumidos.
- Evidencia, observaciones y firmas.

### 10.2 Ciclo recomendado

1. Creación o generación desde solicitud/plan.
2. Planificación y asignación.
3. Inicio de trabajo.
4. Ejecución y registro de datos.
5. Pausa/reanudación si aplica.
6. Finalización técnica.
7. Evaluación del área.
8. Cierre con trazabilidad.

---

## 11. Inventario, repuestos e insumos

El inventario permite consultar disponibilidad, solicitar materiales y registrar movimientos.

### 11.1 Solicitud de materiales

- Busque el repuesto por nombre, código o descripción.
- Revise stock disponible antes de solicitar.
- Indique cantidad real necesaria.
- Relacione la solicitud con una OT cuando corresponda.

### 11.2 Recepción y consumo

- La recepción debe confirmarse con firma cuando el sistema lo solicite.
- El consumo debe quedar vinculado a la OT para que los costos y reportes sean confiables.
- Las devoluciones o ajustes deben tener una razón documentada.

---

## 12. Dashboard y KPIs

El Dashboard resume el estado del mantenimiento y ayuda a tomar decisiones.

![Dashboard modo oscuro](manual_images/dashboard_dark.png)

### 12.1 Indicadores principales

| Indicador | Qué significa |
| --- | --- |
| Máquinas por criticidad | Cantidad de equipos clasificados por impacto operativo. |
| Preventivos del mes | MP programados o ejecutados en el periodo. |
| Correctivos del mes | Fallas o reparaciones no planificadas. |
| Solicitudes pendientes | Reportes aún no convertidos o cerrados. |
| Gasto planificado | Costo estimado de trabajos y materiales. |
| Gasto ejecutado | Costo real ya registrado. |
| MTBF | Tiempo medio entre fallas. |
| MTTR | Tiempo medio de reparación. |
| Disponibilidad | Porcentaje de tiempo operativo del activo. |

### 12.2 Filtros

Use los filtros por fecha, periodo, máquina o técnico para analizar información específica. Los usuarios con rol restringido verán datos asociados a sus equipos asignados.

---

## 13. Seguridad y firmas electrónicas

El sistema incorpora controles orientados al cumplimiento de 21 CFR Part 11.

![Firma electrónica](manual_images/firma_seguridad.png)

### 13.1 Acciones que pueden requerir firma

- Evaluar trabajos.
- Confirmar recepción de materiales.
- Cerrar OT.
- Validar mantenimientos preventivos.
- Realizar acciones administrativas críticas.

### 13.2 Reglas de uso

- La contraseña es personal e intransferible.
- Cada firma queda asociada al usuario, fecha, hora y acción.
- No firme por otra persona.
- Revise la información antes de confirmar.
- Si detecta un error después de firmar, notifique al administrador o responsable de calidad.

### 13.3 Auditoría

El sistema registra cambios relevantes en un historial de auditoría: usuario, acción, entidad afectada, fecha y datos modificados. Esto permite reconstruir el ciclo de vida de solicitudes, OT, inventario y evaluaciones.

---

## 14. Integración con Odoo

La integración con Odoo permite sincronizar inventario, costos, equipos y datos relacionados con mantenimiento.

![Configuración Odoo](manual_images/odoo_config.png)

### 14.1 Información sincronizable

- Equipos o activos.
- Repuestos e insumos.
- Stock y costos.
- Referencias de órdenes o solicitudes, según configuración.

### 14.2 Recomendaciones

- Verifique credenciales antes de sincronizar.
- Evite editar el mismo dato en dos sistemas al mismo tiempo.
- Revise mensajes de error de sincronización.
- Confirme que códigos, series y nombres sean consistentes.

---

## 15. Uso en móvil o tablet

La aplicación es responsiva y puede usarse desde celulares o tablets para trabajo en planta.

![Vista móvil](manual_images/dashboard_mobile.png)

Recomendaciones:

- Use el móvil para reportar fallas cerca de la máquina.
- Tome fotografías cuando ayuden a explicar el problema.
- Revise que la conexión sea estable antes de firmar.
- Cierre sesión al terminar.

---

## 16. Buenas prácticas y solución de problemas

### 16.1 Buenas prácticas

- Describa fallas con lenguaje claro y específico.
- Seleccione siempre la máquina correcta.
- No deje solicitudes duplicadas; revise primero si ya existe una solicitud abierta.
- Registre repuestos reales, no estimados, al cerrar trabajos.
- Use comentarios para explicar atrasos, rechazos o condiciones especiales.
- Cierre sesión en equipos compartidos.

### 16.2 Problemas frecuentes

| Problema | Qué hacer |
| --- | --- |
| No puedo ingresar | Verifique usuario y contraseña. Si persiste, use **¿Olvidó su contraseña**. |
| No veo una máquina | Puede no estar asignada a su perfil. Solicite revisión al administrador. |
| No aparece un botón | Su rol puede no tener permiso o el registro no está en el estado correcto. |
| No encuentro un repuesto | Busque por código, nombre parcial o descripción. Si no existe, solicite alta en inventario. |
| La firma falla | Revise que su contraseña sea correcta y que tenga conexión. |
| El PDF no se genera | Actualice la página e intente nuevamente. Si continúa, reporte el caso con el número de solicitud u OT. |
| Odoo no sincroniza | Verifique configuración, credenciales y conexión con el ERP. |

### 16.3 Qué información enviar al pedir soporte

Cuando reporte un problema al administrador o a IT, incluya:

- Usuario afectado.
- Rol.
- Módulo donde ocurrió.
- Número de solicitud, OT o equipo.
- Fecha y hora aproximada.
- Captura de pantalla, si es posible.
- Mensaje de error mostrado por el sistema.

---

© 2026 Corinfar CMMS - Documentación confidencial.
