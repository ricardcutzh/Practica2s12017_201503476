/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package edd_practica2_201503476;
import WebServiceCon.WebServiceConection;

import GUI.Principal;
/**
 *
 * @author ricar
 */
public class EDD_Practica2_201503476 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        WebServiceConection web = new WebServiceConection();
        String r = web.conectarAWebService();
        System.out.println(r);
        if(r.equals("Conección Fallida a Web Service")){
            System.out.println("NO SE HABRIRÁ LA APLICACIÓN");
        }
        else{
            Principal ventana = new Principal();
            ventana.setVisible(true);   
        }
        
    }
    
}
