package Netflix;

public class Pelicula {
    // Atributos
    private String titulo;
    private String genero;
    private String creador;
    private int año;
    private int duracion;
    private boolean visto;

    // Constructores
    public Pelicula() {
        // Constructor default
    }

    public Pelicula(String titulo, String creador) {
        this.titulo = titulo;
        this.creador = creador;
        // Resto de atributos con valores por defecto
        this.visto = false;
    }

    public Pelicula(String titulo, String genero, String creador, int año, int duracion) {
        this.titulo = titulo;
        this.genero = genero;
        this.creador = creador;
        this.año = año;
        this.duracion = duracion;
        // Atributo visto con valor por defecto
        this.visto = false;
    }

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

