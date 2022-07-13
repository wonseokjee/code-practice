package swea.d1;

import java.util.Arrays;
import java.util.Scanner;

public class Ex2063 {
    //버블 정렬 이용해서 해결할 수 있을듯. 삽입정렬이 더욱 편할 듯
    //하나씩 집어 넣는게 가능하니까 삽입정렬-> 내가 생각한 방식이
    // 삽입정렬알고리즘에는 해당 안되는 듯?
    //일단 삽입정렬로 해보고 발전사항에 버블정렬, 퀵정렬
    //swea 완료
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("범위 안의 홀수를 입력하시오: ");
        int n = sc.nextInt();
        System.out.println(n);
        if (n%2!=0&&n>=9&&n<=199) {
            int[] nums = new int[n];
            for (int i = 0; i < n; i++) {
                System.out.println(n+"개의 점수를 입력하시오: ");
                int a = sc.nextInt();
                nums[i] = a;
            }
            System.out.println("<정렬 전>");
            System.out.println(Arrays.toString(nums));

            /*삽입정렬 진행*/
            for (int j = 1; j < nums.length; j++) {
                //현재 선택된 원소의 값을 임시 변수에 저장해준다.
                int temp = nums[j];
                //현재 원소를 기준으로 이전 원소를 탐색하기 위한 index 변수
                int prev = j - 1;
                //현재 선택된 원소가 이전 원소보다 작은 경우가지만 반복. 단 0번째 원소까지만 비교된다.
                while (prev >= 0 && nums[prev] > temp) {
                    //현재 선택된 원소가 현재 탐색중인 원소보다 작다면, 해당 원소는 다음 인덱스로 미뤄버린다.
                    nums[prev + 1] = nums[prev];
                    // 다음 대상 원소를 탐색한다.
                    prev--;
                }
                //탐색이 종료된 지점에 현재 선택되었던 변수의 값을 삽입해준다.
                nums[prev + 1] = temp;
            }
            System.out.println("<정렬 후>");
            System.out.println(Arrays.toString(nums));
            System.out.print("중간값: ");
            System.out.println(nums[n/2]);
        }
    }
}
