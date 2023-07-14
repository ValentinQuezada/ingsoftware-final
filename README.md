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
1. Verificar que el monto transferido en ese día sea el correcto. *(éxito)*
2. Verificar que al realizar una operación, el monto transferido en ese día no supere los 200. *(éxito)*
3. Verificar que al realizar una operación, el monto de transferencia haga que el monto transferido en ese día supere los 200. *(error)*

- **¿Cuánto riesgo hay de "romper" lo que ya funciona?**

Hemos de tener bastante cuidado al momento de implementar la nueva validación mencionada debido a que podrían interrumpirse los flujos de las demás funciones ya establecidas en el código. Por ejemplo, la actualización de saldos o el registro de operaciones pueden ser funcionalidades que lleguen a ser alteradas por la incorporación del nuevo diccionario `trans` y su constante actualización. Es más, esta misma actualización del diccionario podría incluso ser costosa si no se implementa de forma eficiente, haciendo que la API corra más lento y se pierda tiempo de respuesta en los accesos a sus endpoints. Pra ello, trabajar con un diccionario podría facilitar las actualizaciones, pero de todas formas habría que verificar que nada esté roto luego de ello.
