# Raíces - Diseño de producto

## Propósito

Raíces será la plataforma digital permanente de la Red de Jóvenes de Iglesia El Renuevo. Su objetivo es ayudar a jóvenes mayores de 18 años a sostener prácticas de lectura bíblica, oración y aplicación cotidiana mediante planes temáticos, recordatorios, acompañamiento humano y una experiencia visual inspirada en juegos.

La aplicación debe motivar sin presentar el crecimiento espiritual como una competencia. El progreso personal será privado; la comunidad celebrará únicamente resultados colectivos.

## Audiencia y escala inicial

- 30 jóvenes activos, todos mayores de 18 años.
- 10 líderes acompañantes.
- Aproximadamente tres jóvenes asignados a cada líder.
- Un administrador asigna manualmente el líder principal de cada joven.
- Lanzamiento como PWA instalable en Android y iPhone.

## Principios del producto

1. **Volver también es avanzar.** La inactividad nunca mata la planta, rompe una racha ni elimina progreso.
2. **Orientar, no diagnosticar.** El onboarding recomienda un camino que la persona puede aceptar o modificar.
3. **Privacidad por defecto.** El diario es privado y el progreso individual no se publica.
4. **Celebración colectiva.** Las métricas públicas representan el aporte de toda la Red.
5. **IA bajo revisión humana.** Ningún contenido generado se publica sin aprobación administrativa.
6. **Una acción principal por día.** La aplicación evita tableros saturados y presión innecesaria.

## Metáfora visual y gamificación

Cada joven tendrá una planta-compañera que representa un proceso vivo. Las prácticas de Palabra, oración y acción la nutren y permiten avanzar por etapas visuales.

Las misiones otorgan puntos que sirven únicamente para:

- hacer crecer la planta;
- abrir nuevas etapas;
- desbloquear cartas, insignias, historietas y fondos de pantalla.

Los puntos no son moneda, no miden la espiritualidad y no producen rankings individuales. Habrá fondos disponibles desde el inicio y otros desbloqueables, para que las recompensas no excluyan a quien recién comienza.

## Navegación principal

La PWA tendrá cinco accesos persistentes:

1. **Inicio:** planta, misión recomendada y colección activa.
2. **Camino:** planes temáticos, misiones y progreso personal.
3. **Oración:** muro comunitario y oraciones guiadas.
4. **Colecciones:** cartas, insignias, «Verdad en dibujo» y fondos descargables.
5. **Más:** biblioteca, diario, comunidad y configuración.

Los mockups y el wireflow aprobados están en `output/mockups/raices/`.

## Registro y roles

El registro será obligatorio. Se podrá ingresar con Google o con correo y contraseña.

### Joven

- Administra su perfil, preferencias y recorrido.
- Ve su progreso, diario y colecciones.
- Decide si comparte una nota con su líder.
- Publica peticiones según el nivel de privacidad elegido.

### Líder

- Ve progreso y alertas únicamente de sus jóvenes asignados.
- Recibe notas compartidas explícitamente.
- Puede acompañar de forma privada.
- No accede automáticamente al diario.

### Administrador

- Gestiona usuarios, roles y asignaciones.
- Revisa, edita, regenera y publica contenido.
- Sube libros PDF.
- Ve métricas generales.
- No accede al diario privado de los jóvenes.

## Onboarding y plan personal

El onboarding preguntará solamente:

- experiencia con lectura bíblica;
- frecuencia actual de oración;
- áreas en las que desea crecer;
- tiempo disponible por día;
- horario de recordatorio;
- intensidad preferida.

La aplicación recomendará un camino construido con contenido ya aprobado. El usuario podrá confirmarlo o ajustarlo. No se preguntará por pecados, diagnósticos emocionales ni situaciones íntimas.

Las notificaciones push solo se activarán después de instalar la PWA y conceder permiso. Si el usuario no lo hace, Inicio seguirá mostrando la misión pendiente sin bloquear el recorrido.

Un futuro «Análisis profundo» queda fuera del MVP. Solo se diseñará cuando exista un especialista responsable, junto con nuevos mecanismos de consentimiento y privacidad.

## Planes y ciclo semanal

La biblioteca ofrecerá planes sobre temas específicos. Cada semana tendrá cinco misiones breves y dos días flexibles para descansar o recuperar una misión.

Una misión podrá incluir:

- lectura bíblica;
- reflexión o escritura privada;
- oración guiada con audio;
- acción práctica;
- desafío de aplicación.

El flujo diario será:

1. El usuario recibe un recordatorio configurable y sin lenguaje de culpa.
2. Inicio muestra una única misión recomendada.
3. El usuario elige la versión normal o un paso breve de recuperación.
4. Puede guardar una reflexión privada.
5. La práctica nutre la planta y puede desbloquear una recompensa.

## Recuperación y acompañamiento

Si una persona deja de avanzar, Raíces ofrece primero ayuda automática:

- misión de aproximadamente dos minutos;
- reprogramación;
- continuidad sin pérdida de puntos ni etapas.

Si la dificultad persiste, el líder asignado recibe una señal privada para acompañar. La alerta no incluye notas del diario ni expone detalles sensibles.

## Diario personal

Las reflexiones escritas dentro de las misiones forman un diario personal.

- Es privado por defecto.
- Administradores y líderes no pueden leerlo automáticamente.
- El joven puede compartir una nota concreta con su acompañante.
- El permiso para esa nota es explícito y reversible.

## Muro de oración

Cada petición se presenta visualmente como un post-it. Al publicar, el usuario elige entre:

- visible para toda la Red con nombre;
- visible para toda la Red de forma anónima;
- visible solo para los líderes y administradores de la Red.

Las interacciones del MVP serán «Oré por esto», cantidad de acompañamientos, «Respondida» y reporte. No habrá comentarios públicos ni mensajes directos.

## Métricas comunitarias

La aplicación mostrará únicamente resultados colectivos:

- misiones completadas por toda la Red;
- peticiones acompañadas con «Oré por esto»;
- progreso de una planta comunitaria.

No mostrará nombres, rankings, minutos de lectura ni porcentajes públicos de personas atrasadas.

## Colecciones y contenido visual

Las cartas representan verdades bíblicas, prácticas, desafíos e hitos. Permanecen en la colección aunque la persona interrumpa su actividad.

«Verdad en dibujo» será una imagen o tira breve con humor y una verdad bíblica aplicada. Los fondos descargables usarán frases o versículos como recordatorio. La PWA permitirá descargarlos, pero no podrá cambiar automáticamente la pantalla de bloqueo.

## Biblioteca y lectura adaptable

Solo los administradores podrán subir libros PDF. Cada libro tendrá:

- vista original continua o por página;
- progreso y última posición;
- modo opcional de lectura adaptable con tamaño y espaciado configurables.

El PDF se procesa una vez al subirlo. Si la extracción estructurada falla por escaneo, cifrado o diseño complejo, se conserva la vista original y no se bloquea la publicación.

## Generación de contenido con IA

La IA tomará como referencia doctrinal, lingüística y editorial las prédicas y materiales existentes de la Red. Sin requerir un tema inicial, propondrá un calendario y paquetes completos con:

- series y planes;
- lecturas, devocionales y misiones;
- versiones breves de recuperación;
- cartas e insignias;
- guiones de oración y audio;
- «Verdad en dibujo»;
- frases y fondos.

Todo resultado comienza como borrador. El administrador revisa el paquete completo, puede editar o regenerar elementos y luego lo publica. El texto y el audio deben revisarse antes de aprobarse. Los usuarios solo reciben contenido publicado.

Antes de la primera generación, la IA resumirá la línea doctrinal y editorial inferida de los materiales existentes y un administrador la confirmará una sola vez. La propuesta inicial se inicia sin tema obligatorio; más adelante el administrador podrá aportar temas opcionales.

El MVP integrará un único proveedor de IA directamente desde funciones del servidor; no se construirá una capa multi-proveedor. La elección concreta del proveedor y modelo se resolverá en el plan de implementación según costo, calidad en español y capacidad de texto, imagen y voz.

## Arquitectura

- **Vercel:** alojamiento de la PWA.
- **Supabase Auth:** Google y correo/contraseña.
- **Supabase Postgres:** perfiles, planes, misiones, progreso, contenido, acompañamiento y métricas.
- **Supabase Storage:** PDF, audio, cartas y fondos.
- **Supabase Row Level Security:** aislamiento por rol y propiedad.
- **Supabase Functions:** llamadas a IA, notificaciones y procesamiento externo.
- **Adobe PDF Extract:** conversión adaptable cuando el documento sea compatible.

Railway no formará parte del MVP. Se añadirá únicamente si existe un proceso prolongado que no pueda resolverse mediante las funciones y APIs externas actuales.

## Flujo de datos y permisos

1. El usuario inicia sesión y Supabase entrega su identidad y rol.
2. La PWA consulta únicamente datos autorizados por políticas de filas.
3. Completar una misión registra progreso, actualiza la planta y evalúa el desbloqueo correspondiente.
4. Las métricas públicas se calculan como agregados sin exponer identidades.
5. Las solicitudes de IA se ejecutan en servidor; las credenciales nunca llegan al navegador.
6. El contenido generado permanece separado del contenido publicado.
7. Compartir una nota crea un permiso explícito para esa nota, no para el diario completo.

## Errores y degradación

- Si falla la IA, la solicitud queda fallida o reintentable y no se publica contenido parcial.
- Si falla el audio, el texto aprobado sigue disponible.
- Si falla la conversión adaptable, se muestra el PDF original.
- Si falla una notificación, la misión permanece accesible desde Inicio.
- Si una escritura de progreso falla, la interfaz no muestra puntos ni recompensas hasta recibir confirmación del servidor.
- Los reportes del muro quedan visibles para administradores y permiten retirar contenido.

## Prueba inicial y lanzamiento

La primera prueba puede realizarse con dos personas:

- un líder que también opera una cuenta administrativa de prueba;
- un joven voluntario.

Se usarán tres cuentas para comprobar por separado los permisos de administrador, líder y joven. Durante una semana se validará:

- registro y onboarding;
- asignación líder-joven;
- misión normal y versión breve;
- puntos, planta y desbloqueos;
- diario privado y nota compartida;
- niveles de privacidad del muro;
- audio guiado;
- PDF original y lectura adaptable;
- alertas y acompañamiento.

La prueba de dos personas no valida comportamiento colectivo ni variedad de dispositivos. Esos aspectos se observarán durante el lanzamiento beta a los 30 jóvenes y 10 líderes. La primera semana pública tendrá monitoreo cercano y corrección prioritaria de errores, confusión y privacidad.

## Criterios de lanzamiento

- Los tres roles solo acceden a la información permitida.
- No existe acceso involuntario al diario.
- El contenido de IA no puede publicarse sin acción administrativa.
- El recorrido principal puede completarse en móvil sin ayuda.
- La recuperación breve no borra progreso.
- El muro respeta los tres niveles de privacidad.
- Las funciones esenciales siguen disponibles cuando fallan IA, audio, notificaciones o conversión PDF.

## Fuera del MVP

- Aplicaciones móviles nativas.
- Cambio automático de pantalla de bloqueo.
- Análisis profundo sin especialista.
- Rankings individuales.
- Comentarios públicos y mensajería directa.
- Mercado o gasto de puntos.
- Múltiples proveedores de IA.
- Railway u otros workers permanentes.
