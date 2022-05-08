package solvedAc.Bronze4;

import java.util.Scanner;

public class Ex1008 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        double sol = 0;
/*        System.out.print("숫자를 입력하시오: ");
        double a = scanner.nextInt();
        System.out.print("숫자를 입력하시오: ");
        double b = scanner.nextInt();
        sol = a / b ;
        System.out.println(sol);*/

        double[] arr = new double[2];
        for (int i = 0; i < 2; i++) {
            System.out.print("숫자를 입력하시오: ");
            arr[i] = scanner.nextInt();
        }
        sol = arr[0] / arr[1];
        System.out.println(sol);
    }
}
