# Datos

El archivo `Hurto_a_personas.csv.gz` en la raíz contiene el CSV del análisis comprimido con gzip (38,2 MB sin comprimir), con datos de 2019–2025. pandas puede leerlo directamente. Se obtuvo de las estadísticas de hurto a personas publicadas por la Policía Nacional y se limita a Bogotá para el análisis.

Para reconstruirlo, descarga los libros Excel anuales de 2019–2025 desde la [página de estadísticas delictivas](https://www.policia.gov.co/delitos-de-impacto/hurto-personas), colócalos en `data/raw/` y ejecuta `python scripts/prepare_data.py`. El preparador espera las columnas `Año`, `Mes`, `Departamento` y `Cantidad`; si cambia el esquema oficial, actualiza el preparador.

Las cifras son estadísticas administrativas sujetas a revisión. No son antecedentes judiciales ni tasas poblacionales.
