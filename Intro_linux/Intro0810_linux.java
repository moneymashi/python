package doc;

public class Intro0810_linux {
/*
 * a06_관리자를위한명령어
 * --------- RPM(redhat package manager)
 *  RPM기반 배포판사용.
 *  윈도우체제의 setup.exe와 비슷한 프로그램 설치후 바로실행할수잇는 설치파일제작.
 *  rpm --version  ::버전확인
 *  [:][q]로 종료처리
 * 옵션: 형식: rpm -opt 패키지이름
 * -qa :시스템에 설치된 패키지확인
 * -ql : 특정패키지의 파일확인
 * -qi : 설치된 패키지의 상세정보확인
 * -qf <파일절대경로>: 이미 설치된 파일이 어느패키지에 포함된건지 확인.
 * 
 * 아직 설치안된 패키지 질의
 * rpm -qlp <패키지이름(*.rpm)> : 패키지파일에 어떤파일이 포함되어잇는지 확인.
 * rpm -qip <패키지이름>: 설치할 패키지 상세정보
 * 
 * 설치옵션:
 * rpm -Uvh 패키지명
 * -U : update 상위버전 패키지업데이트
 * -v: verbose 설치시, 상태를 화면출력
 * -h: 설치할떄, 설치되는 정도를 #로표시
 * -i: 기존에 설치되지않앗던 패키지를 설치할때 사용.
 * 
 * 패키지삭제:
 * rpm -e
 * 
 * rpm옵션:
 * 설치 -i/ -U :: install, update
 * 제거 -e ::erase
 * 질의 -q :: query
 * 검증 -v :: verify
 * 패키지제작모드 : -b :: build
 * 
 * ---------------- yum
 * yum(yellowdog update modified)  ::듀크대 프로젝트의 일부개발.
 * 역할: 특정 패키지를 설치시, 다른패키지를 자동으로 먼저설치. --> 의존성 문제해결.
 * 모듈:: calc -> plus, minus, div, multi (네트웤상 특정저장)
 * 사용방법: 
 * 패키지검색: 
 *  yum search @@@ ex) yum search mysql
 * 업데이트 목록확인:
 *  현재 업데이트 서버의 패키지목록확인: yum check-update
 *  설치되지않는 패키지목록확인 : yum list | more ==> :q
 *  현재 클라이언트 시스템에 설치된 패키지목록확인: yum list installed | less
 * 업데이트,설치
 *  yum info 패키지이름, yum info updates
 * 삭제
 *  yum remove 패키지이름
 * 
 * ----- 파일 압축, 풀기
 * 압축
 * compress :: 가장오래된 압축유틸
 * gzip :: 압축효율이 좋음.
 * bzip2: gzip을 개선. 현재 트렌드.
 * tar: 여러개 파일과 디렉터리를 하나로묶음.
 * 압축효율: compress < gzip < bzip2
 * 
 * 형식: 
 * compress (.Z)
 *  compress <압축할 파일이름>
 *  uncompress <압축풀 zip이름.Z>
 * gzip/gunzip (.gz)
 *  gzip <압축할 파일이름>
 *  gzip -d <압축된 파일이름>
 * bzip2/bunzip2(.bz2)
 *  bzip2 <압축파일이름>
 *  bzip2 -d <압축된 파일이름>
 *  
 * 
 * 파일묶음
 *  리눅스/ 유닉스에서는 파일압축/파일묶음별개 프로그램 수행.
 *  사용자 편의를 위해 압축과 묶음을 할수있게 옵션제공
 *   옵션: 묶기:: tar -cvf
 *   	   풀기:: tar -xvf
 *   파일묶고 압축 : tar cvfj <압축파일 이름.tar.bz2> <압축대상 파일/디렉터리>
 *   		풀기: tar xvfj <압축된 파일 이름.tar.bz2>
 *   	
 * tar 동작: tar -@xx
 * -c: 새로묶음
 * -x: 묶인파일풀기
 * -t: 묶음을 풀기전 묶인경로 보여줌
 * 			tar -x@@
 * -f(필수) : 묶음파일이름지정
 * -v: 파일 묶음/해제과정 visual하게 보여줌.
 * -z: tar+gzip( GNU only)
 * -j: tar+bzip2( GNU only)
 * 
 * ------- Prac
 *  /home/vagrant/b02_comExp 디렉터리에 파일 exp01.txt 02 03생성.
 *  exp01.txt에 list ctrl c+v.
 *  계정을 su - 변경
 *  root경로에 exp01.tar묶음.
 *  		exp01.tar.bz2 묶음+압축
 *  묶음 압축 해제.
 *  
 *  >
 *  touch exp01.txt
 *  vi exp01.txt 적당히 해주고
 *  tar -cvjf Compact.tar.bz2 /root 
 * 	tar -xcjf Compact.tar.bz2
 * 
 * ---------Prac
 * 1. 패키지 프로그램을 설치하기위해 가장많이 사용되는건 (rpm) 과 
 * RPM기반의 시스템을 위한 자동업데이트 겸 패키지 설치/제거도구인 (yum)가 있다
 * 
 * 2. 패키지 설치 옵션에 대한 의미
 * -rpm -Uvh
 * U: Upgrade
 * v: verbose(설치시,상태출력)
 * h: 설치시 설치정도를 #로 표시
 * -rpm -e mysql의미
 * :mysql패키지 제거.
 * 
 * tar동작옵션과 의미. tar -@@@@ ##### $$$$$$
 * ex) tar -cjvf Compact.tar.bz2 /root
 * 		:: tar + bzip2로 새로묶고 압축. 
 * 			출력과정 보여주고, 이름: Compact.tar.bz2, 압축결과 위치는 /root에 저장.
 * @xxx
 * c: 새로묶기
 * x: 묶인파일풀기
 * t: 묶음풀기전 묶인경로 출력
 * 
 * x@xx
 * f: 필수- 묶음파일 이름지정.
 * v: 파일 묶기/풀기 과정을 출력
 * z: tar+gzip(GNU only)
 * j: tar + bzip2(GNU only)
 * 
 * --------- 정리
 * rpm: red hat package mannager
 * yum : rpm기반의 시스템위한 자동 업뎃겸 패키지설치/제거도구
 * rpm 장점: s/w설치 및 업데이터 편리
 * 패키지 설치/삭제옵션
 * 	rpm -Uvh 패키지명
 *  rpm -e 패키지명
 * RPM 옵션 : i/U - 설치,업뎃.
 * 			e -제거
 * 			v - 검증
 * 			q - 질의
 * 			패키지 제작.
 * 
 * yum 사용:
 *  yum -y insall @@@@
 *  yum info @@@
 *  yum update @@@
 *  yum remove @@@
 * 
 * 압축: compress < gzip <bzip2
 * tar: 묶기 + 압축(cvjf) ==> @@@.tar.bz2
 * 			풀기(xvjf)
 * 
 * 
 * 
 */
}
