package solvedAc.bronze1;

import java.util.Scanner;

public class Ex1110 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("정수를 입력하시오: ");
        int putIn = scanner.nextInt();

        String str = Integer.toString(putIn);
        String[] Arr = str.split("");

        int sol = Integer.parseInt(Arr[0]) + Integer.parseInt(Arr[1]);
        System.out.println("답: "+sol);
    }
}
