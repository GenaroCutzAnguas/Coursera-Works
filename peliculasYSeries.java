public class peliculasYSeries {
    public static void main(String[] args) {
        // Crear arrays de 5 elementos
        Pelicula[] peliculas = new Pelicula[5];
        Serie[] series = new Serie[5];

        // Instanciar objetos y asignar valores
        peliculas[0] = new Pelicula("Pelicula1", "Director1");
        peliculas[1] = new Pelicula("Pelicula2", "Accion", "Director2", 2022, 120);
        // ... (continuar con las instancias de películas)

        series[0] = new Serie("Serie1", "Creador1");
        series[1] = new Serie("Serie2", 5, "Drama", "Creador2", 40);
        // ... (continuar con las instancias de series)

        // Marcar como visto algunas películas y series
        peliculas[0].marcarVisto();
        peliculas[2].marcarVisto();
        series[1].marcarVisto();
        series[3].marcarVisto();

        // Mostrar lista de películas visualizadas
        System.out.println("Películas Visualizadas:");
        for (Pelicula pelicula : peliculas) {
            if (pelicula != null && pelicula.esVisto()) {
                System.out.println(pelicula);
                System.out.println(pelicula.tiempoVisto());
            }
        }

        // Mostrar lista de series visualizadas
        System.out.println("\nSeries Visualizadas:");
        for (Serie serie : series) {
            if (serie != null && serie.esVisto()) {
                System.out.println(serie);
                System.out.println(serie.tiempoVisto());
            }
        }

        // Encontrar la serie con más temporadas
        Serie serieMasTemporadas = series[0];
        for (Serie serie : series) {
            if (serie != null && serie.numTemporadas > serieMasTemporadas.numTemporadas) {
                serieMasTemporadas = serie;
            }
        }
        System.out.println("\nSerie con más temporadas:\n" + serieMasTemporadas);

        // Encontrar la película del año más reciente
        Pelicula peliculaMasReciente = peliculas[0];
        for (Pelicula pelicula : peliculas) {
            if (pelicula != null && pelicula.año > peliculaMasReciente.año) {
                peliculaMasReciente = pelicula;
            }
        }
        System.out.println("\nPelícula del año más reciente:\n" + peliculaMasReciente);
    }

    public static class Pelicula implements Visualizable {
        // ... (código anterior)

        // Implementación de los métodos de la interfaz Visualizable
        @Override
        public void marcarVisto() {
            this.visto = true;
        }

        @Override
        public boolean esVisto() {
            return visto;
        }

        @Override
        public String tiempoVisto() {
            return "Tiempo total visto: " + duracion + " minutos";
        }

        // Sobrescribir el método toString
        @Override
        public String toString() {
            return "Pelicula: " + titulo + ", Año: " + año + ", Duración: " + duracion + " minutos";
        }
    }

    public static class Serie implements Visualizable {
        // ... (código anterior)

        // Implementación de los métodos de la interfaz Visualizable
        @Override
        public void marcarVisto() {
            this.visto = true;
        }

        @Override
        public boolean esVisto() {
            return visto;
        }

        @Override
        public String tiempoVisto() {
            return "Tiempo total visto: " + duracion + " minutos";
        }

        // Sobrescribir el método toString
        @Override
        public String toString() {
            return "Serie: " + titulo + ", Temporadas: " + numTemporadas + ", Duración: " + duracion + " minutos";
        }
    }

    public interface Visualizable {
        void marcarVisto();

        boolean esVisto();

        String tiempoVisto();
    }
}
