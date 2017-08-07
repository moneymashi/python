package doc;

public class Intro0614_linux {
/*
 * 
 *   //터미널에서 us - 는 수퍼유저
 *   //바로 root/ 에서 cd /home/Server01/Desktop 하면  바탕화면에서 처리하는 작업들을 확인가능.
 * 
 * mv: move 파일이나 디렉터리의 이름을 변경하거나 다른 디렉터리로 옮길떄 사용.
 * 기본형식:
 *  mv 원본파일명/이동할 디렉터리명
 *  	ex) mv abc.txt /etc/sysconfig/    //abc -> /etc/sysconfig디렉토리로 이동.
 *  mv 원본파일명 변경할파일명
 *  	ex) mv abc.txt ccc.txt   //abc -> ccc
 *  mv 이동할파일1 이동할파일2... 저장할디렉터리명
 * 		ex) abc.txt def.txt abcd
 * 
 * mkdir: 디렉터리 생성명령
 * rmdir: 해당 디렉터리 삭제권한으로 삭제처리
 *  // 파일포함은 rm -r로 처리.
 * ....?
 * 
 * head, tail: 텍스트 형식으로 작성된 파일. 앞10행 뒤10행을 화면에 출력할떄 활용.
 * head -라인수  파일명 // 텍스트 라인수.
 * 	ex) head abc.txt : 해당파일 앞 10행출력
 * 		head -5 abc.txt: 파일 앞 5행출력
 * 		tail -3 abc.txt: 파일 뒤 3행출력
 * 
 * more : 텍스트 형식으로 작성된 파일을 페이지 단위로 화면에 출력할떄 활용.
 * space를 누르면 다음페이지 이동, Backspace누르면 앞페이지로 이동.
 * Q를 누르면 종료
 *  more aaaa.txt
 *  more +시작행번호 aaaa.txt : 해당 행 번호부터 출력
 * 
 * less : 텍스트형식으롱작성된 파일을 페이지단위로 화면에 출력할떄 활용.
 * 	more 활용되는 key+..
 * 	[pageup],[pagedown]
 * 	 ex_) less +10 abc.txt
 * file: 해당 파일이 어떤 종류의 파일인지 표시.
 * 
 * 
 * 
 *   ///////////////////////////
 *   리눅스 운영시
 *   ///////////////////////////
 *   
 * 프로그램 - 보조프로그램 - 지에디트
 * 저장: 컴퓨터 / home / Server01 / Desktop 등등
 *   cmd> gedit으로하면 영문작성으로만 가능. 한글작성은 위의 디렉터리대로 한다.
 * vi 에디터 실습하기
 *  ex1) vi
 *   Esc + :q(저장안하고 종료하기)
 *  
 *  ex2) vi new.txt
 *   a 글자입력
 *   Esc + :wq(저장하고 종료)
 *  ex3) vi
 *   a 글자입력
 *   Esc + :wq test3.txt(해당파일명으로 종료)
 * 
 * 
 * 
 * 
 */
}
