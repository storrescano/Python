/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package práctica3ejercicio2;

import java.util.ArrayList;
import java.util.Scanner;

/**
 *
 * @author Alumnat
 */
public class Orc {
    static Scanner lector = new Scanner (System.in);
    private String name;
    private int strength;
    private int wisdom;
    private int intelligence;
    private int dexterity;
    private int agility;
    private int power;

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getStrength() {
        return strength;
    }

    public void setStrength(int strength) {
        this.strength = strength;
    }

    public int getWisdom() {
        return wisdom;
    }

    public void setWisdom(int wisdom) {
        this.wisdom = wisdom;
    }

    public int getIntelligence() {
        return intelligence;
    }

    public void setIntelligence(int intelligence) {
        this.intelligence = intelligence;
    }

    public int getDexterity() {
        return dexterity;
    }

    public void setDexterity(int dexterity) {
        this.dexterity = dexterity;
    }

    public int getAgility() {
        return agility;
    }

    public void setAgility(int agility) {
        this.agility = agility;
    }

    public int getPower() {
        return power;
    }

    public void setPower(int power) {
        this.power = power;
    }

    public Orc(String name) {
        this.name = name;
    }
    
    public static void solicitarCaracteristicasOrcos(ArrayList <Orc> orcos){
        System.out.println("Dame el nombre del orco: ");
        Orc o1 = new Orc(lector.nextLine());
        System.out.println("Dame la característica de fuerza:");
        o1.setStrength(lector.nextInt());
        System.out.println("Dame la característica de agilidad:");
        o1.setAgility(lector.nextInt());
        System.out.println("Dame la característica de destreza:");
        o1.setDexterity(lector.nextInt());
        System.out.println("Dame la característica de inteligencia:");
        o1.setIntelligence(lector.nextInt());
        System.out.println("Dame la caracterísitca de sabiduria:");
        o1.setWisdom(lector.nextInt());
        System.out.println("Dame la característica de poder:");
        o1.setPower(lector.nextInt());
        orcos.add(o1);
    }
    public static void mostrarDatosOrco(ArrayList <Orc> orcos){
        System.out.println("Elija un orco entre 0-" + (orcos.size()-1));
        int eleccion = lector.nextInt();
        System.out.println("Característica fuerza: " + orcos.get(eleccion).getStrength());
        System.out.println("Característica agilidad: " + orcos.get(eleccion).getAgility());
        System.out.println("Característica destreza: " + orcos.get(eleccion).getDexterity());
        System.out.println("Característica inteligencia: " + orcos.get(eleccion).getIntelligence());
        System.out.println("Característica sabiduria: " + orcos.get(eleccion).getWisdom());
        System.out.println("Característica poder: " + orcos.get(eleccion).getPower());
    }
}
