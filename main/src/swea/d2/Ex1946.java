package swea.d2;

import java.util.Scanner;

public class Ex1946 {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        //System.out.print("테스트케이스 번호를 입력하시오: ");
        int t = sc.nextInt();
       // System.out.print("테스트케이스 반복횟수: ");
        int count = sc.nextInt();
        /*케이스 반복횟수가 1이상 10이하*/
        if (count >= 1 && count <= 10) {
            int div_ten = 0;
            System.out.println("#"+t);
            for (int i = 0; i < count; i++) {
               // System.out.print("알파벳을 입력하시오:");
                String alp = sc.next();
                //System.out.print("연속된 갯수를 입력하시오:");
                /*알파벳 개수 20개 이하로 지정 */
                int num = sc.nextInt();
                for (int j = 0; j < num; j++) {
                    System.out.print(alp); //알파벳 찍기
                    div_ten++; //나누기 카운트 올리기
                    /*10개씩 쪼개기*/
                    if (div_ten % 10 == 0) {
                        System.out.println();
                    }
                }
            }
        }

    }

}
