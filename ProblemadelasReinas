#include <iostream>
#include <vector>
#include <string>
#include <cmath> // Para abs()

// Función para imprimir un tablero de ajedrez
void imprimirTablero(const std::vector<int>& solucion, int n_reinas) {
    /**
     * Imprime una representación visual de una única solución del problema de las N-Reinas.
     *
     * @param solucion: Un vector que representa la colocación de las reinas (ej., {1, 3, 0, 2}).
     * @param n_reinas: El tamaño del tablero.
     */
    std::string linea_horizontal = "";
    for (int i = 0; i < n_reinas; ++i) {
        linea_horizontal += "--";
    }
    linea_horizontal += "-"; // Para el borde final

    std::cout << linea_horizontal << std::endl;
    for (int fila = 0; fila < n_reinas; ++fila) {
        std::cout << "|";
        for (int columna = 0; columna < n_reinas; ++columna) {
            if (solucion[fila] == columna) {
                std::cout << "Q|"; // Reina
            } else {
                std::cout << " |"; // Espacio vacío
            }
        }
        std::cout << std::endl;
        std::cout << linea_horizontal << std::endl;
    }
    std::cout << std::endl;
}

// Función auxiliar para verificar si es seguro colocar una reina en (fila, columna)
bool esSeguro(int fila_actual, int columna_actual, const std::vector<int>& colocacion_actual) {
    /**
     * Verifica si colocar una reina en (fila_actual, columna_actual) es seguro
     * de reinas colocadas previamente.
     *
     * @param fila_actual: La fila actual a verificar.
     * @param columna_actual: La columna actual a verificar.
     * @param colocacion_actual: El vector con las posiciones de las columnas de las reinas
     * colocadas previamente (colocacion_actual[r] = c).
     * @return bool: Verdadero si es seguro, Falso en caso contrario.
     */
    for (int fila_anterior = 0; fila_anterior < fila_actual; ++fila_anterior) {
        int columna_anterior = colocacion_actual[fila_anterior];

        // 1. Comprobar si hay una reina en la misma columna
        if (columna_anterior == columna_actual) {
            return false;
        }

        // 2. Comprobar si hay una reina en la misma diagonal
        // abs(fila_actual - fila_anterior) == abs(columna_actual - columna_anterior)
        // significa que están en la misma diagonal (izquierda-derecha o derecha-izquierda).
        if (std::abs(fila_actual - fila_anterior) == std::abs(columna_actual - columna_anterior)) {
            return false;
        }
    }
    return true; // Es seguro colocar la reina
}

// Función recursiva de backtracking para resolver N-Reinas
void resolverNReinasBT(int fila_actual, int n_reinas, std::vector<int>& colocacion_actual, std::vector<std::vector<int>>& soluciones) {
    /**
     * Intenta recursivamente colocar reinas, fila por fila.
     *
     * @param fila_actual: La fila actual en la que estamos intentando colocar una reina.
     * @param n_reinas: El tamaño del tablero (N x N).
     * @param colocacion_actual: Un vector donde colocacion_actual[r] = c significa
     * que una reina está en (r, c).
     * @param soluciones: Un vector de vectores para almacenar todas las soluciones válidas encontradas.
     */

    // Caso base: Si todas las reinas han sido colocadas con éxito
    if (fila_actual == n_reinas) {
        soluciones.push_back(colocacion_actual); // Añadir la solución actual
        return;
    }

    // Intentar colocar una reina en cada columna de la fila actual
    for (int columna_actual = 0; columna_actual < n_reinas; ++columna_actual) {
        if (esSeguro(fila_actual, columna_actual, colocacion_actual)) {
            colocacion_actual[fila_actual] = columna_actual; // Colocar la reina
            
            // Llamada recursiva para la siguiente fila
            resolverNReinasBT(fila_actual + 1, n_reinas, colocacion_actual, soluciones);

            // Backtrack: Si la llamada recursiva no lleva a una solución,
            // la reina en esta posición no es la correcta.
            // (En C++ con vector<int>, no es estrictamente necesario "deshacer"
            // ya que la asignación en la siguiente iteración o el retorno de la función
            // se encargarán, pero conceptualmente es importante).
            // colocacion_actual[fila_actual] = -1; // O algún valor centinela
        }
    }
}

// Función principal para resolver el problema de las N-Reinas
std::vector<std::vector<int>> resolverNReinas(int n_reinas) {
    /**
     * Encuentra todas las soluciones posibles para colocar N reinas no atacantes
     * en un tablero de ajedrez N x N.
     *
     * @param n_reinas: El tamaño del tablero (N x N).
     * @return std::vector<std::vector<int>>: Una lista de listas, donde cada lista interna
     * representa una configuración de tablero válida.
     */
    std::vector<std::vector<int>> soluciones;
    std::vector<int> colocacion_inicial(n_reinas, -1); // -1 indica que no hay reina colocada aún

    // Iniciar el proceso de backtracking desde la primera fila (fila 0)
    resolverNReinasBT(0, n_reinas, colocacion_inicial, soluciones);

    return soluciones;
}

// --- Cómo usarlo ---
int main() {
    // Para N=4
    std::cout << "--- Problema de las N-Reinas (N=4) ---" << std::endl;
    std::vector<std::vector<int>> soluciones_4_reinas = resolverNReinas(4);
    if (!soluciones_4_reinas.empty()) {
        std::cout << "Se encontraron " << soluciones_4_reinas.size() << " soluciones para N=4:" << std::endl;
        for (size_t i = 0; i < soluciones_4_reinas.size(); ++i) {
            std::cout << "Solucion " << i + 1 << ": ";
            for (int col : soluciones_4_reinas[i]) {
                std::cout << col << " ";
            }
            std::cout << std::endl;
            imprimirTablero(soluciones_4_reinas[i], 4);
        }
    } else {
        std::cout << "No se encontraron soluciones para N=4." << std::endl;
    }

    // Para N=8 (puede tardar un momento en calcularse)
    std::cout << "\n--- Problema de las N-Reinas (N=8) ---" << std::endl;
    std::vector<std::vector<int>> soluciones_8_reinas = resolverNReinas(8);
    if (!soluciones_8_reinas.empty()) {
        std::cout << "Se encontraron " << soluciones_8_reinas.size() << " soluciones para N=8." << std::endl;
        // Para brevedad, solo imprimiremos la primera solución para N=8
        if (!soluciones_8_reinas.empty()) {
            std::cout << "Primera solucion para N=8:" << std::endl;
            imprimirTablero(soluciones_8_reinas[0], 8);
        }
    } else {
        std::cout << "No se encontraron soluciones para N=8." << std::endl;
    }

    return 0;
}
