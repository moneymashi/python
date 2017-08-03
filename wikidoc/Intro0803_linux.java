package doc;

public class Intro0803_linux {
/*
 * su -
 * passwd: vagrant
 * 
 * #yum install at
 * 
 * at -l   //check at installed.
 * mkdir test01
 * cd /home/vagrant/test01
 * 
 * 
 * #df (파일명)
 * 
 * #du (파일명)
 * 파일/현재 디렉터리의 모든파일의 디스크 사용량 확인. 
 * 
 * #아카이브
 * :백업또는 다른장소로의 이동.
 * 
 * #tar 명령
 * 옵션: c(create), v(verbose), f(file), x(extract), t(table of contents)
 * ex)
 * tar -cvf 타르파일 파일.
 * :여러파일들을 하나의 타르파일로 묶어 확장자 .tar
 * tar -xvf 타르파일
 * :하나의 타르파일을 풀어서 원래 파일들을 복원
 * tar -tvf 타르파일
 * : 타르파일의 내용확인
 * 
 * #prac)
 * tar -cvf src.tar
 * gzip src.tar
 * 이동 mv
 * gzip -d src.tar.gz
 * tar -xvf src.tar
 * 
 * #awk 프로그램
 * 
 * ##vi - 입력하기
 * touch a.txt
 * vi a.txt
 * i 누르고.. 입력 완료후 
 * esc누르고 :wq (저장후 닫기.)
 * 
 * check:: cat a.txt
 * 
 * #이동, 수정, 삭제.
 * 
 * #복사 붙이기
 * 
 * # 줄넘버 붙이기 :set number
 * 
 * ################################
 * 변수 지정하기
 * term=xterm   // 띄어쓰기하면 다른단어로 인식하기떄문에 하지말아야함.
 * 변수 부르기.
 * echo $term
 * 
 * export term
 * env   //환경변수 설정후 export하면 env설정완료.
 * 
 * shell builtin 함수처리확인
 * ex) cat etc/bashrc
 * 
 * 
 * 
 * ######## PRAC 
 * 1. 리눅스 명령으로 사용자계증생성후, 파일별 해당사용자권한 설정.
 * 2. 계정의 그룹변경, 변경된 그룹의 파일접근권한 만들기.
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
