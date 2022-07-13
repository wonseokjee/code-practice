package swea.d2;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;

public class Ex1989 {
    //swea 완료
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("테스트 케이스 수를 입력하시오: ");
        int T = sc.nextInt();
        for (int i = 0; i < T; i++) {
            System.out.print("#"+(i+1));
            System.out.print("단어를 입력하시오: ");
            String text = sc.next();
            String[] str = text.split("");
            //System.out.println(Arrays.toString(str));
            int count= 0;
            for (int j = 0; j < str.length / 2; j++) {
                //System.out.print("배열 길이 절반 나눈 값:");
                //System.out.println(str.length/2);
                //System.out.println(str[j]);
                //System.out.println(str[(str.length - 1) - j]);
                if (str[j].equals(str[(str.length - 1) - j])) {
                    //System.out.println("여기 들어와!");
                    count++;
                }
            }
            //System.out.print("1이 몇개 올라갔는지: ");
            //System.out.println(count);

            if (count == str.length / 2) {
                count = 1;
            } else {
                count =0;
            }
            //System.out.print("답: ");
            System.out.println(" "+count);
        }

    }
}
