package algorithm.doit;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;


public class bj2750 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        List<Integer> arr = new ArrayList<>();
        for (int i = 0; i < N; i++) {
            int num = sc.nextInt();
            arr.add(num);
        }
/*      방법 1*/
        /*
        int[] result = new int[arr.size()];
        for (int j = 0; j < arr.size(); j++) {
            result[j] = arr.get(j).intValue();
        }
        */
        /*방법 2*/
        int[] result2 = arr.stream().mapToInt(i -> i).toArray();
        Arrays.sort(result2);
        for (int a : result2) {
            System.out.println(a);
        }
    }

}
