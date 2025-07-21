# Changelog

Todos los cambios notables en este proyecto serán documentados en este archivo.

El formato está basado en [Keep a Changelog](https://keepachangelog.com/es-ES/1.0.0/),
y este proyecto adhiere a [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.0] - 2025-06-12

### Added
- Integración de Prometheus para observabilidad mediante `prometheus-fastapi-instrumentator`.
- Exposición automática del endpoint `/metrics` para monitoreo de métricas HTTP.
- Módulo de postulaciones de mascotas a solicitudes de donación
- Endpoints para gestión de postulaciones:
  - GET `/base/api/solicitudes/{id}/postulaciones` - Obtener postulaciones de la solicitud
  - GET `/base/api/solicitudes/{id}/postulaciones/{postulacionId}` - Obtener detalles de una postulación
  - POST `/base/api/solicitudes/{id}/postulaciones` - Crear una nueva postulación
  - PATCH `/base/api/solicitudes/{id}/postulaciones/{postulacionId}/status` - Actualizar el estado de una postulación
- Modelos y esquemas de validación:
  - `ApplicationCreate`, `ApplicationShort`, `ApplicationDetail`, `ApplicationStatusUpdate`
  - Validación de correo con `EmailStr`
- Personalización de ejemplos en documentación OpenAPI
- `email-validator` como dependencia requerida
- Manejo de errores 422 personalizados para validaciones
- Soporte para enums de tipo de sangre canina y felina

### Changed
- Ajustes a los modelos para incluir ejemplos explícitos (`Field(..., example=...)`)
- Mejora en la documentación Swagger para mostrar ejemplos completos de entrada y salida

### Fixed
- Corrección de errores de validación por `EmailStr` sin dependencias
- Sintaxis inválida en `return` fuera de función en `base.py`
- Corrección del tipo `species`: de `str` a `Species` (enum) para validación de valores permitidos.
- Corrección del tipo `lastVaccination`: de `str` a `date` para asegurar formato de fecha válido.
- Corrección del tipo `ownerEmail`: de `str` a `EmailStr` para validar correos electrónicos.
- Corrección del tipo `bloodType`: de `str` a `BloodType` (enum) para restringir a tipos válidos según especie.

### Security
- Dependencia `email-validator` verificada y versionada

### Pending
- Persistencia real en base de datos (actualmente uso mock/in-memory)
- Validación cruzada avanzada compatibilidad de tipo de sangre
- Tests para módulo de postulaciones:
  - Tests de creación y actualización
  - Tests de validación cruzada
  - Tests de integración con solicitudes

## [0.2.0] - 2025-07-18

### Added
- Persistencia real con base de datos MongoDB para el módulo de postulaciones.
- Inclusión de campos `solicitudId`, `mascotaId`, `ownerId` en la estructura de la postulación.
- Identificador único generado automáticamente (`uuid4`) para cada postulación.
- Verificación de token (autenticación) añadida a los endpoints de postulaciones.
- Rutas actualizadas a `/solicitudes/{solicitud_id}/postulaciones` (sin prefijo `/api`) y respuesta estructurada con `status_code` explícito.

### Changed
- Reemplazo del almacenamiento en memoria (`fake_db`) por colección MongoDB (`postulaciones_collection`).
- Refactor de los controladores para usar operaciones asincrónicas (`async def` con `await`).
- Estructura interna de documentos ajustada para alinearse con un modelo de base de datos documental (MongoDB).

### Fixed
- Corrección de generación de ID: antes se usaba una numeración simple que podía generar IDs repetidos (`APP-001`); ahora se usa `uuid4()` para asegurar unicidad global.
- Mejora en la validación y respuesta cuando se intenta postular con un correo ya registrado en la misma solicitud (ahora devuelve `409 Conflict`).
- Inclusión de timestamps consistentes (`createdAt`, `updatedAt`) generados en el servidor.

### Security
- Autenticación obligatoria mediante token en todos los endpoints protegidos.

