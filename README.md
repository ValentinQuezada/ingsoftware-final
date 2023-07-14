# Examen Final: Ingeniería de Software 1
### Datos
- **Nombre del docente:** Christian Paz
- **Alumno:** Quezada Amour, Héctor Valentín
- **Código:** 202120750
- **Sección:** 1
- **Fecha:** 13/07/2023
## Pregunta 3
*Se requiere realizar un cambio en el software para que soporte un valor máximo de 200 soles a
transferir por día.*
- **¿Qué cambiaría en el código?**
1. Agregaría a la clase `Cuenta` un atributo `transf` (diccionario) que determine cuánto se ha transferido desde esa cuenta en cada día.
2. En el método `realizar_operacion()` validaría que para la cuenta remitente, el valor de su diccionario `transf` en el día actual no sea mayor a 200. En caso se cumpla la condición, actualizaría ese mismo valor con el de la operación realizada (validando también que el nuevo valor no supere a 200). Caso contrario, devolvería un mensaje de error indicando que se ha superado el monto máximo de transacciones diarias.
- **Nuevos casos de prueba a adicionar.**
