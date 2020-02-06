/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package práctica3ejercicio2;

import java.util.ArrayList;
import java.util.Scanner;
import static práctica3ejercicio2.Hibrid.mostrarDatosHibrido;
import static práctica3ejercicio2.Hibrid.solicitarCaracteristicasHibrido;
import static práctica3ejercicio2.Human.mostrarDatosHumano;
import static práctica3ejercicio2.Human.solicitarCaracteristicasHumano;
import static práctica3ejercicio2.Orc.mostrarDatosOrco;
import static práctica3ejercicio2.Orc.solicitarCaracteristicasOrcos;

/**
 *
 * @author Alumnat
 */
public class Práctica3Ejercicio2 {
    static Scanner lector = new Scanner (System.in);
    

    public static void main(String[] args) {
        ArrayList <Human> humanos = new ArrayList <Human> ();
        ArrayList <Orc> orcos = new ArrayList <Orc> ();
        ArrayList <Hibrid> hibridos = new ArrayList <Hibrid> ();
        String resultado = "";
        while (!"salir".equals(resultado)){
            System.out.println("1.Introducir un nuevo humano.");
            System.out.println("2.Introducir un nuevo orco.");
            System.out.println("3.Hacer un hibrido.");
            System.out.println("4.Mostrar datos de un humano.");
            System.out.println("5.Mostrar datos de un orco.");
            System.out.println("6.Mostrar datos de un hibrido.");
            System.out.println("7.Salir");
            switch (lector.nextInt()){
                case 1:
                    solicitarCaracteristicasHumano(humanos);
                    break;
                case 2:
                    solicitarCaracteristicasOrcos(orcos);
                    break;
                case 3:
                    solicitarCaracteristicasHibrido(hibridos,humanos,orcos);
                    break;
                case 4:
                    mostrarDatosHumano(humanos);
                    break;
                case 5:
                    mostrarDatosOrco(orcos);
                    break;
                case 6:
                    mostrarDatosHibrido(hibridos);
                    break;
                case 7:
                    resultado = "salir";
                    break;
            }
        }
    }
    
}
