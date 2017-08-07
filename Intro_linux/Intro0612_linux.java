package doc;


public class Intro0612_linux {
	
/*
 * Linux
 * 시작과 종료
 * X윈도우 환경 - 시작과 종료, 로그아웃
 * 
 *   // root권한으로하려면 
 *   su -
 *   pswd 는 server01 // 11111인가
 * 
 * 
 * 터미널:
 * 종료
 * 	poweroff  //종료
 *  halt -p
 *  init 0
 *  shutdown -P +10   //10분후 종료
 *  shutdown -r 22:00   //22시에 리부팅
 *  shutdown -c  // 예약된 shutdown 취소!
 *  shutdown -k +15   //15분후 종료메세지
 * 	shutdown -r now == reboot == init 6// 시스템재부팅
 *  logout, exit //로그아웃
 *  
 *  init X // 런레벨 
 *  0 종료모드
 *  1 단일사용자모드
 *  5 다중사용자모드
 *  6 재부팅모드
 * 
 * VMWARE 화면전환 escape : ctrl + alt
 * 한영변환 : window func + space
 * tab: 자동완성, 방향키 
 * history : 이떄까지 사용한 코드 확인
 * 
 * ls; list 해당 디렉토리(폴드)의 파일목록
 * ls: 현재 디렉터리 파일목록나열
 * ls 특정디렉토리 : 디렉터리의 파일나열
 * ls -a: 숨길파일을 파함한 디렉토리 리스트
 * ls -l: 자세한 모록내용
 * ls *.cfg : cfg로 끝나는 파일리스트
 * ls -l /etc/sysconfig/a* : etc/sysconfig/의 디렉토리에 a로 시작하는 파일을 자세하게 리스트.
 * 
 * 
 *   //터미널에서 us - 는 슈퍼유저행
 *   //바로  cd /home/Server01/Desktop 하면  바탕화면에서 처리하는 작업들을 확인가능.
 * 
 * 명령어와 공통option/.
 * cd: change directory. 현재위치에서 디렉터리 변경.
 * cd .. : 상위 디렉터리로 이동.
 *  su - // 관리자변경
 * 	ls
 * 	su Server02 // 사용자변경
 *  cd
 *  ls
 *  cd ~ Server02  //사용자 지정.
 * 
 *  touch 파일명
 *   파일이 없을때, 해당 파일명으로 용량0, 수정일은 현재로 생성
 *   파일이 ㅣㅆ을떈, 수정일을 현재로 바꿈
 *   ex) touch abc.txt
 *   
 *   cp: Copy 파일이낭디렉토리를 복사할떄 활용되는 명령어
 *   새로 복사한 파일은 복사한 사용자의 소유자로 된다.,
	 *   cp 복사대상파일 복사된 파일  //######
	 *   	cp abc.txt def.txt
	 *   cp -r 복사대사디렉토리 복사한디렉토리
	 *   
 *   mkdir : 디렉토리 생성하기
 *   rm : 파일지우기
 *   rm -r : 디렉터리, 하위파일지우기.
 *  
 *  
 *  
 *  
 *  
 *  
 * 
 */
	
	
}
