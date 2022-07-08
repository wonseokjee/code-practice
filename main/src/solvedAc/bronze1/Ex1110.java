package solvedAc.bronze1;

import java.util.Scanner;

public class Ex1110 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("정수를 입력하시오: ");
        int putIn = scanner.nextInt();

        String str = Integer.toString(putIn);
        String[] arr = str.split("");

        int sol = Integer.parseInt(arr[0]) + Integer.parseInt(arr[1]);
        System.out.println("답: "+sol);

        String str1 = Integer.toString(sol);
        String[] arr1 = str1.split("");

    }
}
