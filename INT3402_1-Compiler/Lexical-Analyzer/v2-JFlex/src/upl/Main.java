package upl;


import java.io.*;


public class Main{
    public static void main(String[] args) throws Exception{
      
       Scanner s=null;
	    if (args.length==0) 
            s= new Scanner(new InputStreamReader(System.in));
	    else 
            s = new Scanner(new InputStreamReader(new java.io.FileInputStream(args[0])));
        
        int status=1;
        do{
            status=s.yylex();
            
        }while(status==0);
        
        //s.yylex();
    }
}