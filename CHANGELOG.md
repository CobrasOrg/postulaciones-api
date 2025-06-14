# Changelog

Todos los cambios notables en este proyecto serán documentados en este archivo.

El formato está basado en [Keep a Changelog](https://keepachangelog.com/es-ES/1.0.0/),
y este proyecto adhiere a [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.0] - 2025-06-12

### Added
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
