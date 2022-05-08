package Programmers.Level1;


import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

public class AlertAnswer {
    public static int[] solution(String[] id_list, String[] report, int k) {
        System.out.println(id_list[0]);//id_list[0] 출력해보기

        // report 쪼개서 이차원 배열에 넣기
        String[][] arr = new String[report.length][];
        for (int i = 0; i < report.length; i++) {
            String[] reportArr = report[i].split(" ");
            arr[i] = new String[] {reportArr[0], reportArr[1]};
        }
        System.out.println("이차원 배열 출력: "+arr[4][0]);//이차원배열 출력해보기

        //유저별 신고당한 횟수
        int[] count = new int[id_list.length];
        for (int i = 0; i< id_list.length ; i++) {
            for (int j = 0; j<report.length; j++) {
                if (arr[j][1].equals(id_list[i])) {
                    count[i]+=1;
                }
            }
        }
//if 문에서 조건문을 비교할 때 String은 객체이므로 서로 주소를 비교한다. 그래서 equal()을 쓰면 문자열 비교가능
        System.out.println("유저별 신고당한 횟수: "+ Arrays.toString(count)); //count int배열 출력

        //신고당한 유저 찾기
        int[] alert_id = new int[id_list.length];
        for (int i =0 ; i< count.length; i++) {
            if (count[i] >= k) {
                alert_id[i] = 1;
            }
        }
        System.out.println("신고당한 유저: "+ Arrays.toString(alert_id));
        //신고당한 유저를 id로 찾기

        for (int i = 0; i < id_list.length; i++) {
            if (alert_id[i] == 1) {

            }
        }


/*        //Map에 이차원 배열 또는 report 넣기 -배열 없이 넣으면 더 좋음.
        Map<String, String> map = new HashMap<>();
        for (int i = 0; i < report.length; i++) {
            map.put(arr[i][0], arr[i][1]);
        }
        System.out.println(map.get("muzi"));//map 값 찾기
*/


        int[] answer = {};
        return answer;
    }


    public static void main(String[] args) {
        String[] id_list = {"muzi", "frodo", "apeach", "neo"};
        String[] report = {"muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"};
        solution(id_list, report, 2);
    }

    /* report 배열을 쪼갠다음에 카운트가 올라가능 방식으로

     *이차원 배열로 넣어야 하나?
     쪼개서 맵에 넣기     *
     *신고할때 동일인물이 동일신고 건이면 거르게 조건문
     * k 값 넘으면
     * */
}
   