package Programmers.Level1;


import java.util.*;


public class AlertAnswer {
    public static int[] solution(String[] id_list, String[] report, int k) {
        System.out.println("1. id_list 잘 들어갔는지 출력: "+id_list[0]);//id_list[0] 출력해보기

        // report 쪼개서 이차원 배열에 넣기
        String[][] arr = new String[report.length][];
        for (int i = 0; i < report.length; i++) {
            String[] reportArr = report[i].split(" ");
            arr[i] = new String[] {reportArr[0], reportArr[1]};
        }
        System.out.println("2. 이차원 배열 출력: "+arr[0][0]);//이차원배열 출력해보기
        System.out.println("3. 행으로 이차원 배열 출력 가능한지: "+ Arrays.toString(arr[0]));

        //동일한 배열 삭제하기
        //if i j 로 돌려가면서 검색해서 삭제.;
        //deepEquals는 다차원 배열에서의 비교가 가능. equals는 객체끼리의 대소비교나 다차원배열 비교는 불가능.
        // 다차원 배열의 경우 배열안에 배열이 가진 주소를 받아 비교하기 때문.
        for (int i = 0; i < report.length; i++) {
            for (int j = 0; j < report.length; j++) {
                if (Arrays.deepEquals(arr[i],arr[j])&&(i!=j)) {
                    System.out.println("4. 겹치는 배열 행 출력" + i + j);
                    arr[j][1] = "";
                }
            }
        } //진행중 null값으로 해도 잘 돌아가긴함-> 안돌아감
        System.out.println("5. 배열 다시 뽑아보기");
        for (int i = 0; i < report.length; i++) {
            System.out.println(Arrays.toString(arr[i]));
        }


        /*
        유저별 신고당한 횟수
         */
        int[] count = new int[id_list.length];
        for (int i = 0; i< id_list.length ; i++) {
            for (int j = 0; j<report.length; j++) {
                if (arr[j][1].equals(id_list[i])) {
                    count[i]+=1;
                }
            }
        }
//if 문에서 조건문을 비교할 때 String은 객체이므로 서로 주소를 비교한다. 그래서 equal()을 쓰면 문자열 비교가능
        System.out.println("6. 유저별 신고당한 횟수: "+ Arrays.toString(count)); //count int배열 출력

        /*
        신고당한 유저 찾기
        */
        int[] alert_id = new int[id_list.length];
        for (int i =0 ; i< count.length; i++) {
            if (count[i] >= k) {
                alert_id[i] = 1;
            }
        }
        System.out.println("7. 신고당한 유저 체크: "+ Arrays.toString(alert_id));

        /*
        신고당한 유저를 id로 찾기
        */
        ArrayList findUser = new ArrayList();
        for (int i = 0; i < id_list.length; i++) {
            if (alert_id[i] == 1) {
                findUser.add(id_list[i]);
            }
        }
        System.out.println("8. 정지된 유저 찾기(findUser): " + findUser);

        int[] answer = new int[id_list.length];//코테 기본 변수
        /*
        유저가 신고하여 정지된 id
         */
        for (int i = 0; i < report.length; i++) {
            if (findUser.contains(arr[i][1])) {
                //System.out.println("findUser와 arr["+i+"][1]이 잘 매칭되었는지 체크: "+ arr[i][1]);
                for (int j = 0; j < id_list.length; j++) {
                    //System.out.println(id_list[j]);
                    //System.out.println(arr[i][0]);
                    if(arr[i][0].equals(id_list[j])){
                        answer[j]+=1;
                    }
                }
            }

        }


/*        //Map에 이차원 배열 또는 report 넣기 -배열 없이 넣으면 더 좋음.
        Map<String, String> map = new HashMap<>();
        for (int i = 0; i < report.length; i++) {
            map.put(arr[i][0], arr[i][1]);
        }
        System.out.println(map.get("muzi"));//map 값 찾기
*/



        System.out.println("9. 각 유저별로 신고해서 정지된 아이디: "+ Arrays.toString(answer));
        return answer;
    }


    public static void main(String[] args) {
/*        String[] id_list = {"muzi", "frodo", "apeach", "neo"};
        String[] report = {"muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi", "apeach muzi"};
        solution(id_list, report, 2);*/

        String[] id_list = {"ryan", "con"};
        String[] report = {"ryan con","ryan con","ryan con","ryan con"};
        solution(id_list, report, 3);
    }

    /* report 배열을 쪼갠다음에 카운트가 올라가능 방식으로

     *이차원 배열로 넣어야 하나?
     쪼개서 맵에 넣기     *
     *신고할때 동일인물이 동일신고 건이면 거르게 조건문
     * k 값 넘으면
     * */
}
   