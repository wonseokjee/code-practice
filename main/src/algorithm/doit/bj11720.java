package algorithm.doit;

import java.util.Arrays;
import java.util.List;
import java.util.Scanner;
import java.util.stream.Collectors;

    public class bj11720 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int ans = 0;
        String[] num = sc.next().split("");
        List<String> strList = Arrays.asList(num);
        List<Integer> numList = strList.stream().map(s -> Integer.parseInt(s)).collect(Collectors.toList());
        for (int i = 0; i < numList.size(); i++) {
            ans += numList.get(i);
        }
        System.out.println(ans);
    }
}
