public class EjemploOPPConLoop {

    // Clase abstracta Animal (Abstracción + Encapsulamiento)
    abstract static class Animal {
        private String nombre;

        public Animal(String nombre) {
            this.nombre = nombre;
        }

        public String getNombre() {
            return nombre;
        }

        public void setNombre(String nombre) {
            this.nombre = nombre;
        }

        public abstract void sonido(); // Método abstracto (Abstracción)
    }

    // Clase Perro hereda Animal (Herencia)
    static class Perro extends Animal {
        public Perro(String nombre) {
            super(nombre);
        }

        @Override
        public void sonido() { // Polimorfismo (sobrescritura)
            System.out.println(getNombre() + " dice: Guau!");
        }
    }

    // Clase Gato hereda Animal (Herencia)
    static class Gato extends Animal {
        public Gato(String nombre) {
            super(nombre);
        }

        @Override
        public void sonido() { // Polimorfismo (sobrescritura)
            System.out.println(getNombre() + " dice: Miau!");
        }
    }

    public static void main(String[] args) {
        // Crear un arreglo de Animal (Perro y Gato) - Polimorfismo con array
        Animal[] animales = new Animal[3];
        animales[0] = new Perro("Rex");
        animales[1] = new Gato("Luna");
        animales[2] = new Perro("Max");

        // Loop para recorrer el arreglo y llamar al método sonido()
        for (int i = 0; i < animales.length; i++) {
            animales[i].sonido();
        }
    }
}

