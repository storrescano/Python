/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package práctica3ejercicio2;

import java.util.Scanner;
import java.util.ArrayList;
/**
 *
 * @author Alumnat
 */
class Hibrid {
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

    public Hibrid(String name) {
        this.name = name;
    }

    
    public static void solicitarCaracteristicasHibrido(ArrayList <Hibrid> hibridos,ArrayList <Human> humanos, ArrayList <Orc> orcos){
        System.out.println("Dame el nombre del híbrido: ");
        Hibrid hb1 = new Hibrid(lector.nextLine());
        System.out.println("Dime un numero para un humano entre 0-" + (humanos.size()-1));
        int eleccionhumano = lector.nextInt();
        System.out.println("Y otra vez para un orco entre 0-" + (orcos.size()-1));
        int eleccionorco = lector.nextInt();
        hb1.setStrength((humanos.get(eleccionhumano).getStrength()+orcos.get(eleccionorco).getStrength())/2);
        hb1.setAgility((humanos.get(eleccionhumano).getAgility()+orcos.get(eleccionorco).getAgility())/2);
        hb1.setDexterity((humanos.get(eleccionhumano).getDexterity()+orcos.get(eleccionorco).getDexterity())/2);
        hb1.setIntelligence((humanos.get(eleccionhumano).getIntelligence()+orcos.get(eleccionorco).getIntelligence())/2);
        hb1.setWisdom((humanos.get(eleccionhumano).getWisdom()+orcos.get(eleccionorco).getWisdom())/2);
        hb1.setPower((humanos.get(eleccionhumano).getPower()+orcos.get(eleccionorco).getPower())/2);
        hibridos.add(hb1);
    }
    
    public static void mostrarDatosHibrido(ArrayList <Hibrid> hibridos){
        System.out.println("Elija un hibrido entre 0-" + (hibridos.size()-1));
        int eleccion = lector.nextInt();
        System.out.println("Característica fuerza: " + hibridos.get(eleccion).getStrength());
        System.out.println("Característica agilidad: " + hibridos.get(eleccion).getAgility());
        System.out.println("Característica destreza: " + hibridos.get(eleccion).getDexterity());
        System.out.println("Característica inteligencia: " + hibridos.get(eleccion).getIntelligence());
        System.out.println("Característica sabiduria: " + hibridos.get(eleccion).getWisdom());
        System.out.println("Característica poder: " + hibridos.get(eleccion).getPower());
    }
}
