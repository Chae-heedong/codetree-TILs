import java.util.Scanner; //스캐너 클래스 임포트

public class Main {
    public static void main(String[] args) {
        int a;
        Scanner 스캔=new Scanner(System.in); //입력받는 객체생성
        a=스캔.nextInt();
        System.out.print(a*2); 
    }
}