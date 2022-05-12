package solvedAc.bronze2;

import java.util.Scanner;

public class Ex1075 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int i = 0;
        int plus = 0;
        int sol = 0;
        int x = 0;
            System.out.print("큰 정수를 입력하시오: ");
            i = scanner.nextInt();
            i = i/100;

            System.out.print("나눌 정수를 입력하시오: ");
            sol = scanner.nextInt();

            x = ((i*100)+x)%sol;

        System.out.println(x);

    }
}
