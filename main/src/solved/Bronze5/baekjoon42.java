package solved.Bronze5;

import java.util.Scanner;

public class baekjoon42 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[] arr = new int[9];
        int a = 0;
        int b = 0;
        for (int i = 0; i < 9; i++) {
            System.out.print("숫자를 입력하시오: ");
            arr[i] = sc.nextInt();
            if (a < arr[i]) {
                a = arr[i];
                b = i+1;
            }
        }


        System.out.println("최대값: "+a+" 몇번째수: "+b);
        System.out.println("입력된 숫자: ");
        for (int i = 0; i < 9; i++) {
            System.out.print(arr[i]+" ");
        }

    }
}
