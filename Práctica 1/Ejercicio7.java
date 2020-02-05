/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package holamundo;
import java.util.Arrays;
import java.util.Scanner;
import java.util.ArrayList;
/**
 *
 * @author Alumnat
 */
public class Ejercicio7 {
    static Scanner lector = new Scanner(System.in);
    public static void Ejercicio1(){
        System.out.println("1. Primer ejercicio: ");
                int [] array = new int [5];
                for(int i=0 ; i<5 ; i++){
                    System.out.println("Digame un número:");
                    array[i] = lector.nextInt();  
                }
                System.out.println(Arrays.toString(array));
    }
    public static void Ejercicio2(){
        System.out.println("2. Segundo ejercicio: ");
                int [] array = new int [5];
                for (int i=0; i<5; i++){
                    System.out.println("Digame un número:");
                    array[i] = lector.nextInt(); 
                }
                for (int i=4; i>=0; i--){
                    System.out.println(array[i]);
                }
    }
    public static void Ejercicio3(){
        int [] array = new int [5];
        ArrayList<Integer> positivos = new ArrayList();
        ArrayList<Integer> negativos = new ArrayList();
        ArrayList<Integer> ceros = new ArrayList();
        int contadorceros=0;
        for (int i=0; i<5; i++){
            array[i]=lector.nextInt();
        }
        for (int i=0; i<5; i++){
            if (array[i]>0){
                positivos.add(array[i]);
            }
            else if (array[i]<0){
                negativos.add(array[i]);
            }
            else {
                ceros.add(array[i]);
            }
        }
        int mediapositivos=0;
        for (Integer positivo : positivos){
            mediapositivos+=positivo;
        }
        if (mediapositivos>0){
            mediapositivos=mediapositivos/positivos.size();
        }
        int medianegativos=0;
        for (Integer negativo : negativos){
            medianegativos+=negativo;
        }
        if (medianegativos<0){
            medianegativos=medianegativos/negativos.size();
        }
        for (int i=0; i<ceros.size();i++){
            contadorceros++;
        }
        System.out.println("Los numeros positivos son: "+ mediapositivos);
        System.out.println("Los numeros negativos son: "+ medianegativos);
        System.out.println("Hay "+contadorceros+" ceros.");
    }
    public static void Ejercicio4(){
        int contadorinicial = 0;
        int contadorfinal = 9;
        int[] array = new int[10];
        for (int i=0; i<10; i++){
            array[i]=lector.nextInt();
        }
        for (int i=0; i<5; i++){
            System.out.println(array[contadorinicial]);
            contadorinicial++;
            System.out.println(array[contadorfinal]);
            contadorfinal--;
        }
        
    }
    public static void Ejercicio5(){
        int[] array1 = new int[10];
        int[] array2 = new int[10];
        int[] array3 = new int[20];
        System.out.println("Introduzca 10 números para el primer array");
        for (int i=0; i<10; i++){
            array1[i]=lector.nextInt();
        }
        System.out.println("Introduzca otros 10 números para el segundo array");
        for (int i=0; i<10; i++){
            array2[i]=lector.nextInt();
        }
        int contador = 0;
        for (int i=0; i<10; i++){
            array3[contador]=array1[i];
            contador++;
            array3[contador]=array2[i];
            contador++;
        }
        System.out.println(Arrays.toString(array3));
    }
    public static void Ejercicio6(){
        int[] array1 = new int[12];
        int[] array2 = new int[12];
        int[] array3 = new int[24];
        System.out.println("Introduzca 12 números para el primer array");
        for (int i=0; i<12; i++){
            array1[i]=lector.nextInt();
        }
        System.out.println("Introduzca otros 12 números para el segundo array");
        for (int i=0; i<12; i++){
            array2[i]=lector.nextInt();
        }
        int contador = 0;
        for (int i=0; i<12; i=i+3){
            array3[contador]=array1[i];
            contador++;
            array3[contador]=array1[i+1];
            contador++;
            array3[contador]=array1[i+2];
            contador++;
            array3[contador]=array2[i];
            contador++;
            array3[contador]=array2[i+1];
            contador++;
            array3[contador]=array2[i+2];
            contador++;
        }
        System.out.println(Arrays.toString(array3));
    }
    public static void main(String[] args) {
        System.out.println("Digame que metodo quiere usar: ");
        Scanner opcion = new Scanner(System.in);
        System.out.println("1.Primer ejercicio");
        System.out.println("2.Segundo ejercicio");
        System.out.println("3.Tercer ejercicio");
        System.out.println("4.Cuarto ejercicio");
        System.out.println("5.Quinto ejercicio");
        System.out.println("6.Sexto ejercicio");
        int elegido = opcion.nextInt();
        switch (elegido){
            case 1:
                Ejercicio1();
            case 2:
                Ejercicio2();
            case 3:
                Ejercicio3();
            case 4:
                Ejercicio4();
            case 5:
                Ejercicio5();
            case 6:
                Ejercicio6();
        }
    }

    private static int size(ArrayList<Integer> ceros) {
        throw new UnsupportedOperationException("Not supported yet."); //To change body of generated methods, choose Tools | Templates.
    }
}
