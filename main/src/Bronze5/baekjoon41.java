package Bronze5;

import java.util.Scanner;

public class baekjoon41 {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();
        System.out.println("입력된 배열 요소수: "+ n);
        int[] arr = new int[n];
        int a = -1000001;
        int b = 1000001;

        for (int i = 0; i < n; i++) {
            System.out.println("배열에 들어갈 값을 입력하시오: ");
            arr[i] = scan.nextInt();
        }
        System.out.println("배열에 들어간 값: "+arr[0]+" "+arr[1]+" "+arr[2]+" "+arr[3]+" "+arr[4]);

        for (int i = 0; i < n; i++) {
            if (a < arr[i]) {
                 a = arr[i];
            }
        }
        for (int i = 0; i < n; i++) {
            if (b > arr[i]) {
                 b = arr[i];
            }
        }
        System.out.println(b+" "+a);
    }
}
