# Repositorio de algoritmo RSA en Python

Este es un repositorio personal con el propósito de practicar algoritmos y Python.
En YouTube vi una serie de videos que explicaban como funcionaba el método de encriptación
[RSA](https://es.wikipedia.org/wiki/RSA "Wikipedia") y decidí intentar hacerlo con Python.

### Algunos de los videos que revisé

- [Derivando](https://www.youtube.com/channel/UCH-Z8ya93m7_RD02WsCSZYA "Canal de YouTube") | *Este fue el primero que ví*
  - [Cómo funciona la criptografía](https://www.youtube.com/watch?v=Q8K311s7EiM&t=143s "YouTube")

- Píldora informativa | UPM
  - [¿Cómo funciona el algoritmo RSA?](https://www.youtube.com/watch?v=CMe0COxZxb0 "YouTube")

- Por Sara Ali Hamed
  - [Cifrado RSA | Matemáticas discretas](https://www.youtube.com/watch?v=pvC6MxK5i2s&t=532s "YouTube")

- Por David Alejandro Nina Rojas
  - [Método de cifrado RSA](https://www.youtube.com/watch?v=XOz0NWxIakQ "YouTube")
  - [Cifrado y descifrado usando Python](https://www.youtube.com/watch?v=kiowXySiuP8&t=232s "YouTube")

- Por Juan Manuel Ramirez
  - [Criptografía: Método RSA | Parte 1](https://www.youtube.com/watch?v=AjaMZddJIK0 "YouTube")
  - [Criptografía: Método RSA | Parte 2](https://www.youtube.com/watch?v=AliXPLkzxJE "YouTube")
  - [Criptografía: Método RSA | Parte 3](https://www.youtube.com/watch?v=Pl7dfr-GYDE "YouTube")

- Por Ket.G
  - [El sistema RSA](https://www.youtube.com/watch?v=tZKuRkIrdtM&t=585s "YouTube")

- Por Kratosrazziel186
  - [Algoritmo RSA ejemplo (en excel)](https://www.youtube.com/watch?v=7mtah9jdtvQ&t=5s "YouTube")

- Por Unidad de Innovación UMU
  - [Módulo 2 - El sistema RSA](https://www.youtube.com/watch?v=C2-kLqWfBaE "YouTube")

### Páginas de referencia

- [El algoritmo RSA](http://bitybyte.github.io/Algoritmo-RSA/ "Link a blog")
- [Código en repositorio de la librería "pycrypto"](https://github.com/pycrypto/pycrypto/blob/7acba5f3a6ff10f1424c309d0d34d2b713233019/lib/Crypto/PublicKey/RSA.py "Github")

---

## Encriptación Asímetrica | RSA 

El método de encriptación [RSA](https://es.wikipedia.org/wiki/RSA "Wikipedia")
es un algoritmo para enviar un mensaje encriptado sin necesidad de que el emisor le haya transferido la llave de antemano al receptor.
Esto puede ser muy útil si consideramos que la red puede ser insegura y terceros pueden leer la información.

## *Encriptación Simétrica* vs *Encriptación Asimétrica*

Existen dos tipos generales de encriptación, la **encriptación simétrica** y la **encriptación asimétrica**.

- Por un lado la **encriptación simétrica** utiliza una misma llave para encriptar el mensaje y para desencriptarlo.
- Por otro lado, la **encriptación asimétrica** utiliza dos llaves

  - Una llave para encriptar el mensaje (**La llave pública**)
  - Y una llave para desencriptar el mensaje (**La llave privada**)
---
## La llave privada y la llave pública

### Estas dos llaves se determinan en conjunto

Estas dos llaves se crean en el mismo proceso y comparten en común una cualidad criptográfica. Esta es que cada **llave pública**
puede encriptar un mensaje que sólo una **llave privada** puede descifrar. 

La **llave pública** es la llave que el usuario puede compartir libremente en la red.
Imaginémos que **Pedro** quiere que se comuniquen con él. **Pedro** compartirá su **llave pública** a la red,
entre ellas a la persona que quiere que le envíe un mensaje.
Esta llave será utilizada para poder *encriptar* el mensaje, es decir, transformarla ilegible.

Luego, **Pedro** utilizará su **llave privada** para desencriptar el mensaje, la cual no debe compartir con nadie,
ya que es la única llave capaz de *desencriptar* el mensaje *encriptado* con esa única **llave pública**.

Finalmente **Pedro** utilizará la **llave pública** de la persona que le escribió para responderle, y esa persona utilizará
su **llave privada** para *desencriptar* el mensaje.

### Resúmen

Resumiendo el proceso sería el siguiente:

- Pedro comparte su **llave pública**



---
##








