package swea.d2;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;

public class Ex1926 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("정수를 입력하시오: ");
        int num = scanner.nextInt();
        String str = String.valueOf(num);
        String[] arr = str.split("");
        int count = 0;
        String check = "";
        for (int i = 1; i <= num; i++) {
            for (int j = 0; j < arr.length; j++) {
                System.out.println(arr[j]);
                if (Integer.parseInt(arr[j]) == 3) {
                    count++;
                }
                if (Integer.parseInt(arr[j]) == 6) {
                    count++;
                }
                if (Integer.parseInt(arr[j]) == 9) {
                    count++;
                }
            }
            if (count == 1) {
                check = "-";
            }
            if (count == 2) {
                check = "--";
            }
            if (count == 3) {
                check = "---";
            }
            System.out.println(count);

        }

    }
}
