# Parrcial3 Sistemas Operativos
Demostrar si la premisa:
Si el orden de Encriptar y Comprimir es afectado y dependen del tipo de archivo.
Tipo formato de archivod: Plano, Binario, imagen o sonido.
Compresion : LZ77, LZ78, Huffman, LZW
Encriptacion: cesar, RSA

## Conclusion
En base al codigo demostramos que el orden de encriptar y comprimir afectan el archivo, la explicación de esto es que si realizamos la compresion luego de encriptar el archivo, el archivo al estar encriptado no tendra patrones que el algoritmo de compresion pueda usar de manera eficiente, por lo que podra comprimir mucho menos de lo que podria de un archivo normal. 

Mientras que si realizamos el orden Comprimir > Encriptar, ambos algoritmos podran funcionar de manera eficiente. Esto se ve demostrado en los tamaños de los archivos
![image](https://github.com/user-attachments/assets/9a1a33c3-fbf1-473c-a1bc-089c15ec3459)
