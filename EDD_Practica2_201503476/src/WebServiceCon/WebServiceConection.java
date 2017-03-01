/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package WebServiceCon;

import com.squareup.okhttp.OkHttpClient;
import com.squareup.okhttp.Request;
import com.squareup.okhttp.RequestBody;
import com.squareup.okhttp.Response;

import java.net.MalformedURLException;
import java.net.URL;


import java.net.URL;

/**
 *
 * @author ricar
 */
public class WebServiceConection {
    public static OkHttpClient webClient = new OkHttpClient();
    URL url;
    Request request;
    Response response;
    public WebServiceConection(){
        //CONSTRUCTOR DE CONEXIÓN AL SERVIDOR WEB
    }
    
    public String prueba(String metodo){
        String retorno = "";
        try{
            url = new URL("http://0.0.0.0:5000/"+metodo);
            request = new Request.Builder().url(url).build();
            response = webClient.newCall(request).execute();
            String response_string = response.body().string();
            return response_string;
        }
        catch(Exception e){
            System.out.println(e.getMessage());
        }
        return null;
    }
    
    public String encolar(String metodo, RequestBody body){
        String confirmacion = "";
        try{
            url = new URL("http://0.0.0.0:5000/"+metodo);
            request = new Request.Builder().url(url).post(body).build();
            response = webClient.newCall(request).execute();
            confirmacion = response.body().string();
        }
        catch(Exception e){
            confirmacion = "Hubo un Error";
        }
        return confirmacion;
    }
    
    public Object verCola(){
        Object retorno=null;
        try{
            url = new URL("http://0.0.0.0:5000/VerCola");
            request = new Request.Builder().url(url).build();
            response = webClient.newCall(request).execute();
            retorno = response.body().string();
        }
        catch(Exception e){
            System.out.print(e.getMessage());
        }
        return retorno;
    }
    
    public Object desencolar(){
        Object confirmacion;
        try{
            url = new URL("http://0.0.0.0:5000/DesEncolar");
            request = new Request.Builder().url(url).build();
            response = webClient.newCall(request).execute();
            confirmacion = response.body().string();
        }
        catch(Exception e){
            confirmacion = "No se Desencolo...";
        }
        return confirmacion;
    }
    
    public Object realizarOperacion(String metodo, RequestBody body){
        Object retorno = null;
        String pr = "";
        try{
           //System.out.println("ESTOY EN METODO "+metodo);
           url = new URL("http://0.0.0.0:5000/"+metodo);
           request = new Request.Builder().url(url).post(body).build();
           response = webClient.newCall(request).execute();
           retorno = response.body().string();
        }
        catch(Exception e){
            System.out.println("Ocurrio un Error en Metodo: "+metodo);
        }
        return retorno;
    }
    
    public Object consultar(String metodo){
        Object retorno = null;
        try{
            url = new URL("http://0.0.0.0:5000/"+metodo);
            request = new Request.Builder().url(url).build();
            response = webClient.newCall(request).execute();
            retorno = response.body().string();
        }
        catch(Exception e){
            System.out.println("Hubo Error al realizar consulta al metodo: "+metodo);
        }
        return retorno;
    }
    
    public String conectarAWebService(){
        String confirmacion = "";
        try{
            url = new URL("http://0.0.0.0:5000/Conectar");
            request = new Request.Builder().url(url).build();
            response = webClient.newCall(request).execute();
            confirmacion = response.body().string();
        }
        catch(Exception e){
            confirmacion = "Conección Fallida a Web Service";
        }
        return confirmacion;
    }
    
}
