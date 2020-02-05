
package práctica.pkg2;
import java.util.Arrays;
import java.util.Scanner;
/**
 *
 * @author Alumnat
 */
public class Práctica2 {
    static Scanner lector = new Scanner(System.in);
    public static void Ejercicio6(){
        System.out.println("Introduzca dos números.");
        int [][] tabla = new int [lector.nextInt()][lector.nextInt()];
        for (int i=0; i<tabla.length; i++){
                if (i<tabla[i].length){
                    tabla[0][i]=1;
                    tabla[tabla.length-1][i]=1;
                } 
                tabla[i][0]=1;
                tabla[i][tabla[i].length-1]=1;
        }
        for (int i=0; i<tabla.length; i++){
            System.out.println(Arrays.toString(tabla[i]));
        }
    }
    public static void Ejercicio5(){
        int [][] tabla = new int [8][6];
        for (int i=0; i<tabla.length; i++){
                if (i<6){
                    tabla[0][i]=1;
                    tabla[tabla.length-1][i]=1;
                } 
                tabla[i][0]=1;
                tabla[i][tabla[i].length-1]=1;
        }
        for(int i=0; i<tabla.length; i++){
            System.out.println(Arrays.toString(tabla[i]));
        }
    }
    public static void Ejercicio4(){
        int [][] tabla = new int [7][7];
        for (int i=0; i<tabla.length; i++){
                tabla[i][i]=1;
        }
        for (int i=0; i<7; i++){
            System.out.println(Arrays.toString(tabla[i]));
        }

    }
    public static void Ejercicio3(){
        int [][] tabla = new int [3][3];
        int [][] tabla2 = new int [3][3];
        int [][] resultado = new int [3][3];
        for (int i=0; i<3; i++){
            for (int j=0; j<3; j++){
                tabla[i][j]=i+j;
                tabla2[i][j]=i+j;
            }
        }
        for (int i=0; i<3; i++){
            for (int j=0; j<3; j++){
                resultado[i][j]=tabla[i][j]+tabla2[i][j];
            }
        }
        for (int i=0; i<3; i++){
            System.out.println(Arrays.toString(resultado[i]));
        }
    }
    public static void Ejercicio2(){
        int [][] tabla = new int [4][4];
        boolean comprueba = true;
        for (int i=0; i<tabla.length; i++){
            for (int j=0; j<tabla.length; j++){
                tabla [i][j]=i+j;
            }
        }
        for (int i=0; i<tabla.length; i++){
            for (int j=0; i<tabla.length; i++){
                if (tabla[i][j]!=tabla[j][i]){
                    comprueba = false;
                    i=tabla.length;
                }
            }
        }
        System.out.println(comprueba);
    }
    public static void Ejercicio1(){
        int [][] tabla = new int [5][5];
        for (int i=0; i<tabla.length; i++){
            for (int j=0; j<tabla.length; j++){
                tabla [i][j]=i+j;
            }
        }
        for (int i=0; i<5; i++){
            System.out.println(Arrays.toString(tabla[i]));
        }
    }

    public static void main(String[] args) {
        
        System.out.println("Digame que metodo quiere usar: ");
        System.out.println("1.Primer ejercicio");
        System.out.println("2.Segundo ejercicio");
        System.out.println("3.Tercer ejercicio");
        System.out.println("4.Cuarto ejercicio");
        System.out.println("5.Quinto ejercicio");
        System.out.println("6.Sexto ejercicio");
        switch (lector.nextInt()){
            case 1:
                Ejercicio1();
                break;
            case 2:
                Ejercicio2();
                break;
            case 3:
                Ejercicio3();
                break;
            case 4:
                Ejercicio4();
                break;
            case 5:
                Ejercicio5();
                break;
            case 6:
                Ejercicio6();
                break;
        }
    }
}
    
