package Programmers.Level1;

public class AlertAnswerRefactoring {

    public static void main(String[] args) {
/*        String[] id_list = {"muzi", "frodo", "apeach", "neo"};
        String[] report = {"muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi", "apeach muzi"};
        solution(id_list, report, 2);*/

        String[] id_list = {"ryan", "con"};
        String[] report = {"ryan con","ryan con","ryan con","ryan con"};
        solution(id_list, report, 3);
    }

    public static int[] solution(String[] id_list, String[] report, int k) {
        System.out.println("1. id_list 잘 들어갔는지 출력: " + id_list[0]);//id_list[0] 출력해보기

        int[] answer = {};
        return answer;
    }

}
