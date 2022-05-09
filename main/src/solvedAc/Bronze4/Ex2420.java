package solvedAc.Bronze4;

import java.util.Scanner;

public class Ex2420 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("첫 서브도메인: ");
        Long a = scanner.nextLong();
        System.out.print("두번째 서브도메인: ");
        Long b = scanner.nextLong();

        Long abNum = 0L;
        abNum = Math.abs(a - b);

        System.out.println(abNum);
    }
}
