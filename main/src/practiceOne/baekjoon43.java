package practiceOne;

import java.util.Scanner;

public class baekjoon43 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int arr[] = new int[3];
        int n = 0;
        Integer all = 0;
        for (int i = 0; i < 3; i++) {
            System.out.print("숫자를 입력하시오: ");
            n = sc.nextInt();
            arr[i] = n;
        }
        System.out.println(arr[0]*arr[1]*arr[2]);




    }
}
