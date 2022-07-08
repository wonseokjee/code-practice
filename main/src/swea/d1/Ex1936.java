package swea.d1;

import java.util.Scanner;

public class Ex1936 {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String i;
        System.out.println("숫자를 두개 입력하시오: ");
        i = scan.nextLine();
        String[] num = i.split(" ");
        int a = Integer.parseInt(num[0]);
        int b = Integer.parseInt(num[1]);
        System.out.println(a + b);
        if (a > b) {
            System.out.println(a);
        }
        if (a < b) {
            System.out.println(b);
        }

    }
}
