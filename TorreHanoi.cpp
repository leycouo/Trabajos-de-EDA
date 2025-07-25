#include <iostream>
#include <string>

// Función recursiva para resolver el problema de las Torres de Hanói
void torresDeHanoi(int n_discos, char poste_origen, char poste_auxiliar, char poste_destino) {
    /**
     * Resuelve el rompecabezas de las Torres de Hanói de forma recursiva.
     *
     * @param n_discos: El número de discos a mover.
     * @param poste_origen: El nombre del poste donde se encuentran los discos (ej., 'A').
     * @param poste_auxiliar: El nombre del poste temporal (ej., 'B').
     * @param poste_destino: El nombre del poste donde deben ir los discos (ej., 'C').
     */

    // Caso base: Si solo hay un disco, muévelo directamente del origen al destino.
    if (n_discos == 1) {
        std::cout << "Mover disco 1 de " << poste_origen << " a " << poste_destino << std::endl;
        return;
    }

    // Paso 1: Mover n-1 discos del poste_origen al poste_auxiliar,
    // usando el poste_destino como temporal.
    torresDeHanoi(n_discos - 1, poste_origen, poste_destino, poste_auxiliar);

    // Paso 2: Mover el disco más grande (el disco n) del poste_origen al poste_destino.
    std::cout << "Mover disco " << n_discos << " de " << poste_origen << " a " << poste_destino << std::endl;

    // Paso 3: Mover los n-1 discos del poste_auxiliar al poste_destino,
    // usando el poste_origen como temporal.
    torresDeHanoi(n_discos - 1, poste_auxiliar, poste_origen, poste_destino);
}

// --- Cómo usarlo ---
int main() {
    std::cout << "--- Torres de Hanói (3 Discos) ---" << std::endl;
    torresDeHanoi(3, 'A', 'B', 'C');

    std::cout << "\n--- Torres de Hanói (4 Discos) ---" << std::endl;
    torresDeHanoi(4, 'Origen', 'Auxiliar', 'Destino'); // Puedes usar nombres más descriptivos

    return 0;
}
