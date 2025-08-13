# Análisis del Mercado de Airbnb en Madrid

## Descripción del Proyecto
Este proyecto realiza un análisis exhaustivo del mercado de alojamientos de Airbnb en la ciudad de Madrid, con especial atención a las variables que más influyen en la oferta, tales como el precio, la ubicación y los servicios ofrecidos.  
Se busca identificar patrones, correlaciones y tendencias que permitan comprender la dinámica del mercado y sus factores determinantes, apoyando la toma de decisiones estratégicas.

## Fuente de Datos
Los datos se han obtenido de [Inside Airbnb](https://insideairbnb.com/get-the-data/), correspondiendo a:
- **Listings**: información detallada de los anuncios activos.
- **Calendario de reservas**: disponibilidad y precios por fecha.

Período de análisis:
- **Q3 2024** (tercer trimestre del año pasado)
- **Q4 2024** (cuarto trimestre del año pasado)
- **Q1 2025** (primer trimestre del año en curso)

## Estructura del Repositorio
/data -> Datasets crudos y procesados

/jupyter -> Notebooks de análisis y limpieza de datos

/src -> Scripts y funciones auxiliares

README.md -> Documento de referencia del proyecto

requirements.txt -> Lista de dependencias necesarias

Analisis de Airbnb Madrid.md -> Conclusiones del proyecto
<<<<<<< HEAD

Dashboard.pbix -> Dashborad interactive en PowerBI

=======
Dashboard.pbix -> Dashborad interactivo en PowerBI 
>>>>>>> d2f74b9 (Correcciones menores)
Recap.md -> Desglose de las sesiones del proyecto


## Contenido de los Datos

### Lista de columnas de: [calendar_sep](data/calendar_sep.csv), [calendar_dec](data/calendar_dec.csv), [calendar_mar](data/calendar_mar.csv):

**listing_id**: Identificador único de un anuncio
**available**: Disponibilidad del Airbnb del anuncio en un día en concreto
**price**: Precio del Airbnb del anuncio
**adjusted_price**: Precio ajustado
**minimum_nights** Mínimo de noches para reservar el Airbnb
**maximum_nights** Máximo de noches para reservar el Airbnb

### Columnas creadas: 

**Trimester**: Trimestre al cual pertenece
**busy_days**: Días reservados en el trimestre
**income**: Ingresos del trimestre
**avg_day**: Media de ingresos por día alquilado
**occupancy_rate**: Porcentaje de ocupación en el trimestre




### Lista de columnas de: [airbnb_mad_sep](data/airbnb_mad_sep.csv), [airbnb_mad_dec](data/airbnb_mad_dec.csv), [airbnb_mad_mar](data/airbnb_mad_mar.csv)

**id**: Identificador único del anuncio.

**listing_url**: Enlace a la página del anuncio.

**scrape_id**: Identificador del proceso de recolección de datos.

**last_scraped**: Última fecha en que se recolectaron los datos.

**source**: Fuente de los datos (city scrape o previous scrape).

**name**: Nombre del anuncio de la propiedad.

**description**: Descripción de la propiedad proporcionada por el anfitrión.

**neighborhood_overview**: Descripción general del vecindario donde se encuentra la propiedad.

**picture_url**: URL de la foto principal de la propiedad.

**host_id**: Identificador único del anfitrión.

**host_url**: Enlace a la página del anfitrión.

**host_name**: Nombre del anfitrión.

**host_since**: Fecha en que el anfitrión se unió a la plataforma.

**host_location**: Ubicación del anfitrión.

**host_about**: Presentación del anfitrión.

**host_response_time**: Tiempo promedio de respuesta del anfitrión.

**host_response_rate**: Porcentaje de respuestas del anfitrión.

**host_acceptance_rate**: Porcentaje de aceptación de reservas del anfitrión.

**host_is_superhost**: Si el anfitrión es superhost o no.

**host_thumbnail_url**: URL de la foto de perfil del anfitrión.

**host_picture_url**: URL de la foto de perfil del anfitrión.

**host_neighbourhood**: Barrio donde vive el anfitrión.

**host_listings_count**: Número total de anuncios que tiene el anfitrión.

**host_total_listings_count**: Total de anuncios del anfitrión (privadas, compartidas, etc.).

**host_verifications**: Métodos de verificación del anfitrión (email, teléfono, etc.).

**host_has_profile_pic**: Si el anfitrión tiene foto o no.

**host_identity_verified**: Si el anfitrión tiene perfil verificado.

**neighbourhood**: Barrio donde se encuentra la propiedad.

**neighbourhood_cleansed**: Barrio donde se encuentra la propiedad (dato ya limpiado).

**neighbourhood_group_cleansed**: Distrito donde se encuentra la propiedad (dato ya limpiado).

**latitude**: Latitud de la ubicación del Airbnb.

**longitude**: Longitud de la ubicación del Airbnb.

**property_type**: Tipo de propiedad (apartamento, casa, habitación privada, etc.).

**room_type**: Tipo de habitación (entera, privada, compartida).

**accommodates**: Número de huéspedes que pueden alojarse.

**bathrooms**: Número de baños disponibles.

**bathrooms_text**: Especificación de la información de los baños.

**bedrooms**: Número de habitaciones disponibles.

**beds**: Número de camas disponibles.

**amenities**: Lista de servicios incluidas en la propiedad (Wi-Fi, cocina, etc.).

**price**: Precio por noche.

**minimum_nights**: Número mínimo de noches para reservar.

**maximum_nights**: Número máximo de noches para reservar.

**minimum_minimum_nights**: El valor más bajo de noches mínimas dentro de ese grupo (desconozco como se conforma).

**maximum_minimum_nights**: El más alto de noches mínimas dentro del grupo (desconozco como se conforma).

**minimum_maximum_nights**: El valor más bajo de noches máximas permitido del grupo (desconozco como se conforma).

**maximum_maximum_nights**: El valor más alto de noches máximas permitido del grupo (desconozco como se conforma).

**minimum_nights_avg_ntm**: Media de noches mínimas permitido del grupo (desconozco como se conforma).

**maximum_nights_avg_ntm**: Media de noches mínimas permitido del grupo (desconozco como se conforma).

**calendar_updated**: Otra información o no se proporcionó descripción específica.

**has_availability**: Si tiene disponibilidades.

**availability_30**: Días disponibles para reservar en los próximos 30 días.

**availability_60**: Días disponibles para reservar en los próximos 60 días.

**availability_90**: Días disponibles para reservar en los próximos 90 días.

**availability_365**: Días disponibles para reservar en el próximo año.

**calendar_last_scraped**: Última vez que fue actualizada la información.

**number_of_reviews**: Número total de reseñas recibidas.

**number_of_reviews_ltm**: Número de reseñas en los últimos doce meses.

**number_of_reviews_l30d**: Número de reseñas en los últimos treinta días.

**availability_eoy**: Días disponibales hasta final de año.

**number_of_reviews_ly**: Número de resñas el último año.

**estimated_occupancy_l365d**: Estimación de días ocupados los últimos 365 días.

**estimated_revenue_l365d**: Ingreso estimado de los últimos 365 días.

**first_review**: Fecha de la primera reseña.

**last_review**: Fecha de la última reseña.

**review_scores_rating**: Puntuación promedio general de la propiedad.

**review_scores_accuracy**: Puntuación de precisión de la descripción del anuncio.

**review_scores_cleanliness**: Puntuación de limpieza de la propiedad.

**review_scores_checkin**: Puntuación del proceso de check-in.

**review_scores_communication**: Puntuación de la comunicación con el anfitrión.

**review_scores_location**: Puntuación de la ubicación de la propiedad.

**review_scores_value**: Puntuación de la relación calidad-precio.

**license**: Número de licencia de la propiedad.

**instant_bookable**: Si se puede reservar de manera instantánea o no.

**calculated_host_listings_count**: Número de anuncios activos del anfitrión.

**calculated_host_listings_count_entire_homes**: Número de anuncios activos de casas o apartamentos enteros.

**calculated_host_listings_count_private_rooms**: Número de anuncios activos de habitaciones privadas.

**calculated_host_listings_count_shared_rooms**: Número de anuncios activos de habitaciones compartidas.

**reviews_per_month**: Promedio de reseñas recibidas por mes.


### Columnas eliminadas y motivo:

**listing_url**: Irrelevante

**scrape_id**: Irrelevante

**picture_url**: Irrelevante

**host_url**: Irrelevante

**host_name**: Irrelevante

**host_location**: Irrelevante

**host_about**: Irrelevante

**host_thumbnail_url**: Irrelevante

**host_picture_url**: Irrelevante

**host_neighbourhood**: Irrelevante

**neighbourhood**: Información contenida neighbourhood_cleansed

**neighbourhood_group_cleansed**: información más precisa en neighbourhood_cleansed

**latitude**: Se prefiere neighbourhood_cleansed para la ubicación

**longitude**: Se prefiere neighbourhood_cleansed para la ubicación

**bathrooms_text** : Información más fácil de tratar en bathrooms

**maximum_nights**: Poco útil

**minimum_minimum_nights**: Información no aclarada con respecto al grupo al que se refiere

**maximum_minimum_nights**: Información no aclarada con respecto al grupo al que se refiere

**minimum_maximum_nights**: Información no aclarada con respecto al grupo al que se refiere	

**maximum_maximum_nights**: Información no aclarada con respecto al grupo al que se refiere

**first_review**: Mejor trabajar con el número de reviews total

**last_review**	: Mejor trabajar con el número de reviews total

**last_scraped**: Mejor trabajar con el número de reviews total

**has_availability**: Dato más completo en el otro dataset que se une

**number_of_reviews_ltm**: Mejor trabajar con el número de reviews total

**number_of_reviews_l30d**: Mejor trabajar con el número de reviews total
**calendar_updated**: Irrelevante



### Columnas transformadas:

**amenities**: la convertiremos en las columnas ("Kitchen", "TV", "Air conditioning","Pets allowed", "Dryer", "Patio or balcony", "Iron", "Microwave", "Cooking basics", "hot tub", "Self check-in",  "Washer",   Heating, "Hair dryer")

Se transforman también algunas columnas para que sea más facil con ellas que se explican dentro del notebook 2_EDA_preliminar.ipynb

### Columnas creadas: 

**Trimester**: Trimestre al cual pertenece


## Ejecución del Proyecto
Clonar el repositorio:

git clone <https://github.com/carlosglezs/Proyecto-Final-AirBnb.git>
Crear y activar un entorno virtual (opcional pero recomendado).

Instalar dependencias:

pip install -r requirements.txt

Ejecutar los notebooks en la carpeta /jupyter en el orden sugerido:

    1_data_calendar.ipynb: carga y preprocesamiento del calendario de reservas.

    2_data_preliminar.ipynb: exploración inicial de listings.

    3_columnas_categoricas.ipynb: tratamiento de variables categóricas y nulos.

    4_KPIs.ipynb: generación de indicadores clave y visualizaciones.


## Conclusiones

Este análisis profundiza en la interpretación de las métricas del dashboard, destacando:

- **Evolución reciente**: Crecimiento de ingresos trimestrales pese a menor oferta, impulsado por mayor ocupación y precio medio por día.
- **Enfoque en ingresos**: La localización es la variable más determinante para ingresos y valoraciones.
- **Análisis por barrios**:
  - **Embajadores**: Mayor facturación por alto volumen, aunque con fuerte competencia.
  - **Atocha**: Mayor ingreso por día, pero baja ocupación.
  - **Vinateros**: Alta ocupación, público reducido.
- **Perfil de huéspedes**: Predominan propiedades para pocos huéspedes, con mayor ocupación y precio por persona.
- **Precio por noche por persona**: Segmentación por percentiles para identificar oferta más rentable.
- **Tipo de propiedad**: El marketing y la nomenclatura (“boutique”, “entire”, “shared”) influyen fuertemente en la rentabilidad.
- **Servicios**:
  - **Piscina**: Aumenta significativamente los ingresos.
  - **Calefacción**: Común pero sin impacto positivo en precios.
- **Proporción de baños/dormitorios/camas**: La disponibilidad de baños por huésped es el factor más influyente en precio.

## Licencia y Créditos

### Licencia del Proyecto
Este proyecto se distribuye bajo la licencia **MIT**, lo que permite su uso, copia, modificación y distribución con fines personales o comerciales, siempre que se mantenga la atribución al autor original.  


### Fuente de los Datos
Los datos utilizados en este análisis provienen de **[Inside Airbnb](https://insideairbnb.com)**, un proyecto independiente que proporciona datos públicos de Airbnb para fines de investigación y análisis.  
Los datasets originales son propiedad de sus respectivos creadores y están sujetos a los términos de uso y condiciones establecidos por Inside Airbnb.  
Cualquier uso posterior de estos datos debe cumplir con dichas condiciones.

**Período cubierto por los datos:**
- Tercer trimestre de 2024
- Cuarto trimestre de 2024
- Primer trimestre de 2025

**Ciudades:** Madrid, España  
**Conjuntos de datos:** Listings y Calendario de reservas

### Autor del Proyecto
- **Nombre:** Carlos González Sotelino  
- **Contacto:** https://www.linkedin.com/in/carlos-gonz%C3%A1lez-sotelino-2b10b9324/

---


