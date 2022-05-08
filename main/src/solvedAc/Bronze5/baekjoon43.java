package solvedAc.Bronze5;

import java.util.Scanner;

public class baekjoon43 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int arr[] = new int[3];
        int n = 0;
        for (int i = 0; i < 3; i++) {
            System.out.print("숫자를 입력하시오: ");
            n = sc.nextInt();
            arr[i] = n;
        }
        System.out.println(arr[0]*arr[1]*arr[2]);
        int all = arr[0]*arr[1]*arr[2];
        String number = String.valueOf(all);
        char[] digit = number.toCharArray();
        int[] counter = new int[10];
        for (int i = 0; i < digit.length; i++) {
            counter[Character.getNumericValue(digit[i])]++;
        }
        for (int i = 0; i <10; i++) {
            System.out.println(i+"의 개수: "+ counter[i]);
        }
    }
}
