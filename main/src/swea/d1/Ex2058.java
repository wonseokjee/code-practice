package swea.d1;

import java.util.Scanner;

public class Ex2058 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("자연수를 입력하시오: ");
        int num = sc.nextInt();
        if (num<=9999 && num>=1) {
            String str = String.valueOf(num);
            String[] arr = str.split("");
            int b = 0;
            for (int i = 0; i < arr.length; i++) {
                b += Integer.parseInt(arr[i]);
            }
            System.out.println(b);
        }else{
            System.out.println("범위값이 아닙니다.");
        }

    }

}
