# Distancias entre ciudades

| Test Case                             | Precondition                                                                                         | Test Steps                                                                                                                                                  | Test Data                                                                                                 | Expected Result                                                               |
|:--------------------------------------|:-----------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------|
| Ingresa dos ciudades diferentes        | El archivo CSV `worldcities.csv` debe existir y contener datos de coordenadas de las ciudades.     | 1. Crear una instancia de `Interface`. <br> 2. Llamar al método `getDistance` con los parámetros ("Cali", "Colombia", "Lima", "Peru", "CSV"). <br> 3. Buscar las coordenadas de ambas ciudades en el archivo CSV. <br> 4. Calcular la distancia usando la fórmula de Haversine. <br> 5. Comparar el resultado con el valor esperado 1722.31. | city1: Cali  <br> country1: Colombia  <br> city2: Lima  <br> country2: Peru  <br> option: CSV      | La distancia calculada entre Cali y Lima debe ser 1722.31 km.               |
| Ingresa una ciudad que no existe      | El archivo CSV `worldcities.csv` debe existir y contener la ciudad Lima (Perú) pero no Tumbes (Chile). | 1. Crear una instancia de `Interface`. <br> 2. Llamar al método `getDistance` con los parámetros ("Tumbes", "Chile", "Lima", "Peru", "CSV"). <br> 3. Intentar buscar las coordenadas de "Tumbes" en el archivo CSV. <br> 4. Verificar que el método retorna `None` si no encuentra la ciudad. | city1: Tumbes  <br> country1: Chile  <br> city2: Lima  <br> country2: Peru  <br> option: CSV       | No se encuentra la ciudad "Tumbes" en Chile, por lo tanto, el resultado debe ser `None`. |
| Ingresa la misma ciudad               | El archivo CSV `worldcities.csv` debe existir y contener la ciudad Lima (Perú).                     | 1. Crear una instancia de `Interface`. <br> 2. Llamar al método `getDistance` con los parámetros ("Lima", "Peru", "Lima", "Peru", "CSV"). <br> 3. Buscar las coordenadas de "Lima" en el archivo CSV. <br> 4. Calcular la distancia de "Lima" a sí misma. | city1: Lima  <br> country1: Peru  <br> city2: Lima  <br> country2: Peru  <br> option: CSV          | La distancia entre "Lima" y "Lima" debe ser 0 km.                           |
| La API está caída o no disponible     |             | 1. Crear una instancia de `CoordinateFinder`. <br> 2. Llamar al método `getDataFromAPI` con los parámetros ("Lima", "Peru"). <br> 3. Simular que la API está caída o no responde correctamente. <br> 4. Verificar que el método retorna `None` al no poder acceder a la API. | city: Lima  <br> country: Peru                                                                         | No se puede acceder a la API, por lo que el resultado esperado es `None`.    |
