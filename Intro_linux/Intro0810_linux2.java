package doc;

public class Intro0810_linux2 {
/*
 * ## 리눅스 시스템관리
 * 
 * cron   ::http://it-korea-class.blogspot.kr/2012/11/cron.html
 * cron: 시스템에서 백업등 주기적인 작업처리용.   
 * 활용법: .crond 데몬서비스로 움직임.
 * 작동확인: service crond status
 * 내부정의 확인 : cat /etc/crontab  >> *분 *시 *일 *달 *week번호 사용자명명령어 실행내용
 * /etc/cron.monthly  : 백업명령 수행하는 스크립트파일 생성, 속성실행
 * 
 * AT설정.
 * 주기적으로 반복되는 작업의 예약이 아닌 일회성 약속등의 작업을 예약할때 사용됨. 주의! 일회성.
 * ex) 내일새벽 03:00에 시스템을 최신패키지로 업데이트하고, 업데이트 완료시 시스템 재부팅되는 at작업?
 * 시간설정: rdate -s time.bora.net
 * 예약시간: at 3:00 tomorrow
 * 
 * 
 * su -
 * root~ #cd /etc
 * chmod 755 cron.monthly
 * su vagrant
 * cd /etc/cron.monthly
 * touch my_backup.sh
 * vi my_backup.sh
 * ....
 * 
 * 
 * -----Prac
 * /etc/crontabl 예약파일 처리
 * 매월 26일 새벽 5:01dp /home 디렉터리와 하위디렉터리를 /backup2에 저장
 * /etc/cron.monthly
 * my_backup2.sh 위 내용처리.
 * 
 * 확인방법::
 * tail /etc/cron.monthly
 * >01 5 26 * * root run-parts /etc/cron.monthly
 * 
 * tail my_backup2.sh
 * >set $(date)
 * >fname ="back-up-$2$3.tar.bz2"
 * >tar cfj /backup/$fname /home
 * 
 * cd ~ 
 * date 012605002023
 * 
 * service crond restart
 * 
 * 
 * 
 * 
 * ##### 답안  #######
 * 1. /etc/crontab에 시간등록
 * 01 5 26 * * root run-parts /etc/cron.monthly  ##매월 26일 새벽 5시 1분 
 * ## SHELL : 실행명령을 실행할 쉘의 종류
	# PATH : 실행파일을 검색할 PATH
	# MAILTO : 실행결과를 보고하는데 사용할 주소
 * 2. /etc/cron.monthly에서 실행파일 (*.sh)
 * vi my_backup2.sh
 * set $(date)
 * fname="back-up-$2$3.tar.bz"
 * tar cfj /backup/$fname /home
 * 
 * 3. mkdir /backup :: 백업폴드만들기
 * 
 * 4. 현재시간 변경. 매월 26일 새벽05:00
 * date 012604002023  ## Jan 26, 2023, 04:00이란 뜻.
 * 
 * 5. 크론잡 재실행
 * service crond restart
 * #########################

 * ==================== 네트워크
 * 네트워크 핵심요소
 * 서버/클라이언트
 * 
 * # TCP/IP
 * TCP(transmission control protocol : 전송조종규약)
 * -네트워크의 정보전달을 통제하는 프로토콜(통신규약) 
 * -데이터의 전달을 보증하고 보낸 순서대로 받게한다. 
 * -IP(internet protocol)위에서 동작하는 프로토콜
 * 
 * 패킷의 교환을 근간하는 IP를 기반으로 작동
 * 패킷(head+body) 바이트 단위의 짧은 신호.
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
