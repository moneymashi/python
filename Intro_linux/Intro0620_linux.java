package doc;

public class Intro0620_linux {

}
/*
 *  // 확인방법:  ls -l 파일명
 * 접근권한: rwx(421) 읽기허용, 쓰기허용, 실행허용
 * 허용대상: u사용자, g그룹, o기타, a전체
 * 소유자 : ~__ , 그룹 : _~_ , 공개 : __~" 
 * 
 * chown 
 * 해당파일에 대한 권한의 변경
 * 형식: chmod [권한옵션] 파일명
 * ex) chown newuser ccc.txt
 * 
 * -rw-r--r--. 1 root 	   root 16 Jun 18 19:20 new.txt
 > -rw-r--r--. 1 newuser04 root 16 Jun 18 19:20 new.txt

 * chmod
 * 해당 파일에대한 권한의 변경
 * 형식: chmod [권한옵션] 파일명
 * 권한옵션 : 777 u+x, u+wx, g+rx, o+rwx
 * ex) chmod u-x aaa.txt, chmid 777 bbb.txt
 * 
 * chgrp
 * 파일의 그룹권한을 변경
 * 형식: chgrp 변경할그룹 파일명
 * 
 * 실습-
 * whoami : 현재사용자가 누구인지
 * touch new.txt : 공백파일생성
 * ./new.txt   ==>  ./ 실행         // 처음에 실행하면 허가거부.
 * chmod 755 new.txt 		
 * 	new.txt에 대해서 사용자는 읽기쓰기 실행권한을 주고, 
 *  그룹과 다른사용자는 5(4+1) 읽기와 실행권한만 
 * ./new.txt
 * 
 * 확인예제---
 * root사용자로 로그인후
 * Person2.java파일에 "안녕하세요!"라고 실행할수있게 만든다
 * 권한내용확인.
 * Person2.java 사용자에게 rwx권한주고, 
 * java명령으로 컴파일과 실행.
 * 
 * 확인예제2----
 * Server01로 로그인.
 * test02.txt공백의 파일을 생성,
 * test02파일에 
 * 사용자권한: r,x권한
 * 그룹권한 x처리
 * 다른사용자: r권한만
 * SErver02에 추가그룹 newGroup04를 처리하고ㅡ, 
 * newGroup04에 속한 계정으로 해당파일에대한 권한별 처리를 확인
 * 
 * 확인예제
 * 소유권변경
 * ls -l new.txt
 * chown newuser04 new.tx
 * ls -l new.txt
 * 그룹변경
 * chgrp newgroup new.txt
 * 소유권과 그룹을 한꺼번에 변경
 * chown 그룹명.소유명 파일명
 * ex) chown newGroup04.Server01 new.txt
 * 
 */

