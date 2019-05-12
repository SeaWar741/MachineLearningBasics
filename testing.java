public class testing{
    public static void main(String args[]) {
        int lol = 20;
        System.out.println("hola"+lol);
        holis(40);
    }
    public static void holis(int pablo){
        do{
        System.out.println("no");
        holis(pablo);
        }while(pablo <30);
    }
    
}