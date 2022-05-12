package solvedAc.bronze3;



public class Ex13311 {
    public static void main(String[] args) {



        for (int i = 0; i < 10; i++) {

            double a = (Math.random()*1000)+2;
            long n = (long)((a-1)%a);
            System.out.println(n);
        }

    }

}
