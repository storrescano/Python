/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package práctica3ejercicio2;
import java.util.Scanner;
import java.util.ArrayList;

public class Human {
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

    public Human(String name) {
        this.name = name;
    }
    
    public static void solicitarCaracteristicasHumano(ArrayList <Human> humanos){
        System.out.println("Dame el nombre del humano: ");
        Human h1 = new Human(lector.nextLine());
        System.out.println("Dame la característica de fuerza:");
        h1.setStrength(lector.nextInt());
        System.out.println("Dame la característica de agilidad:");
        h1.setAgility(lector.nextInt());
        System.out.println("Dame la característica de destreza:");
        h1.setDexterity(lector.nextInt());
        System.out.println("Dame la característica de inteligencia:");
        h1.setIntelligence(lector.nextInt());
        System.out.println("Dame la caracterísitca de sabiduria:");
        h1.setWisdom(lector.nextInt());
        System.out.println("Dame la característica de poder:");
        h1.setPower(lector.nextInt());
        humanos.add(h1);
    }
    
    public static void mostrarDatosHumano(ArrayList <Human> humanos){
        System.out.println("Elija un humano entre 0-" + (humanos.size()-1));
        int eleccion = lector.nextInt();
        System.out.println("Característica fuerza: " + humanos.get(eleccion).getStrength());
        System.out.println("Característica agilidad: " + humanos.get(eleccion).getAgility());
        System.out.println("Característica destreza: " + humanos.get(eleccion).getDexterity());
        System.out.println("Característica inteligencia: " + humanos.get(eleccion).getIntelligence());
        System.out.println("Característica sabiduria: " + humanos.get(eleccion).getWisdom());
        System.out.println("Característica poder: " + humanos.get(eleccion).getPower());
    }
}
