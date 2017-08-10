package doc;

public class Intro0808_linux2 {
/*
 * ############사용자 계정관리.
 * 리눅스 최상위 관리자 : root
 * 계정관련 정보파일들
 * cat /etc/passwd : 사용자 계정정보
 * 사용자이름:암호:사용자id:그룹id:전체이름:사용자 홈디렉터리/로그인시 사용되는 셀

 * cat /etc/group : 사용자계정 그룹정보
 * cat /etc/shadow : 사용자계정 암호정보
 * 
 * 새로운 사용자 계정생성 useradd
 * useradd @@@
 * passwd userName @@@
 * 
 * useradd -option @@@ @@@
 * -g 사용자와 그룹동시 등록: 그룹명 사용자
 * ex) useradd -g grp01 user01
 * 사용자를 등록하는데 그룹명을 grp01이고 사용자명은 user01이다.
 * -u 사용자와 사용자고유id를 설정 : id 사용자명
 * ex) useradd -u 505 user02
 * -d 사용자와 사용자의 디렉터리설정: 디렉터리 사용자명
 * ex) useradd -d /userhome user03
 * -s 사용자의 기술셀과 함께 생성: 셀디렉터리 사용자명
 * ex) useradd -s /bin/usshell01 user04
 * 
 * 암호설정
 * passwd 사용자명
 *  /etc/shadow
 * 
 * 암호를 주기적으로 변경
 * chage -opt 계정명
 * -l : 해당계정의 기본사항을 확인
 * -E : 계정의 만료기간명시
 * 	ex) chage -E 2017/08/09 user01
 * -M : 설정된 암호를 @@일까지 사용
 * 	ex) chage -M 20 user01 # 최대 20일 사용
 * -m : 암호를 주기적으로 변경
 * 	ex) chage -m 7 user01 # 최소 7일 사용
 * -W : 설정된 암호의 만료 @@전부터 warning 설정.
 * 	ex) chage -W 5 user01  ## 만료 5일전부터 알람.
 * 
 * 사용자 속성중 그룹관련처리
 * usermod -g 그룹명 그룹변경계정
 * eX) usermod -g root user01
 * groups 계정명 :: 소속그룹명 조회
 * 
 * 그룹추가
 * groupaddd 그룹명
 * 그룹이름변경
 * groupmod -n 바꿀이름 현재이름  ex) groupmod -n neogp newgp
 * 그룹삭제
 * groupdel 삭제할이름
 * 
 * #### 그룹의 암호화설정+관리
 * gpasswd 그룹명
 * 특정 사용자를 그룹에서 제거
 * gpasswd -d 사용자  그룹명 
 * 특정 사용자를 그룹에 추가.
 * gpasswd -a 사용자 그룹명	
 * 
 * -------Prac
 * 임의의 계정 6개 만들고
 * grpA
 * grpB
 * grpC설정후 각각 2개씩 소유하게.
 * 해당그룹중 첫번쨰 계정을 뽑아 grpD설정, 추가.
 * 
 * #### 참고:
 * useradd -g grpA user001  ## grpA가 존재해야함.
 * tail /etc/group
 * >> 그룹명, 그룹id만뜸

 * gpasswd -a user001 grpA ## user001과 grpA가 존재해야함.
 * tail /etc/group
 * >> 그룹명, 그룹id, 소속user 모두 뜸.
 * 
 * 
 * 
 * 
 * 
 * 
 * 
 * 
 * 
 * 
 * 
 * 
 * 
 * 
 * 
 * 
 * 
 * 
 * 
 * 
 * 
 * 
 * 
 * 
 * 
 * 
 * 
 * 
 * 
 * 
 * 
 */
	
	
	
}
