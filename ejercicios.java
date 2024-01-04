public class ejercicios {
    public static void main(String[] args) {
        int matriz[][] = {
            {2, 4, 6, 8},
            {10, 12, 14, 16},
            {18, 20, 22, 24},
            {26, 28, 30, 32}
        };

        for (int i = 0; i < matriz.length; i++) {
            for (int j = 0; j < matriz[i].length; j++) {
                System.out.print(matriz[i][j] + " ");
            }
            System.out.println();
        }
    }
}