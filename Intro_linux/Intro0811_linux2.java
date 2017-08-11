package doc;

public class Intro0811_linux2 {
/*
 * ======Shell
 * 
 * 
 * 
 * -- shell 종류
 * 
 * sh( Bourne shell) $
 * 최초개발.
 * 리눅스의 기본shell
 * 상호대화X
 * 쉘명령대본 작성.
 * 강력 명령프로그램 언어기능.
 * 
 * bash(Bourne-Again shell) #
 * 요즘 가장 일반적인 쉘.
 * 실행파일 /bin/bash
 * 최초의 쉘인 Bourne의 변종. IEEE POSIX와 호환.
 * GNU프로젝트로 배포.
 * 명령행 편집기능.
 * 
 * C shell( csh) %
 * 표준제공. c언어 유사. 프로그램 개발에 편리기능 내장.
 * 상호 대화식
 * 환경 초기: '.cshrc'
 * 
 * Korn shell(ksh) $
 * bourne shell 발전형.
 * 비대화식 사용자환경 + 대화식 환경접목
 * 유닉스 시스템의 표준쉘로 제공.
 * 환경 초기: '.kshrc'
 * 
 * 
 * ------- shell활용
 * 사용자 shell확인
 * head /etc/passwd
 * echo $shell
 * 
 * 
 * - 환경설정
 * "."(숨김) 으로 시작하는 파일들이 해당.
 * 파일 rc(resource configuration)의미로 접미로 붙음
 * 
 * - 환경설정 파일의 종류
 * .bashrc : 쉘을 위한 스크립트로 서브쉘. 비로그인 쉘이 실행될떄, 명령과 프로그램 구조로 구성할수잇음.
 * 			"비로그인" 쉘이 실행될떄, 명령과 프로그램 구조로 구성할수잇다. 
 * .bash_logout : 로그인쉘이 종료되며 처리
 *  /etc/profile : 시스템 전역에 영향 미치는설정
 *  /etc/bashrc : 시스템 전역영향, 새로운 쉘이 실행될떄마다 진행.
 * 
 * - 환경변수 ###
 * : 사용자가 사용하는 쉘의 환경을 작업환경에 맞게 설정하는데 사용되는 값.
 * $HOME : 사용자의 홈 디렉터리.
 * $LS_COLORS : ls명령을 사용할떄 파일의 종류마다 나타나는 색의 설정
 * $BASH : 사용하는 Bash 쉘경로
 * $BASH_VERSION
 * $COLUMNS: 터미널행수
 * $ENV : 환경 지정파일위치
 * $HISTFILE : hist파일경로
 * $HISTSIZE : 히스토리갯수
 * $LINES: 터미널의 라인수
 * $MANPATH : 도움날이 있는경로
 * 
 * 
 * - 표준에러파일 보내기
 * 에러나올내용 > 출력파일
 * 
 * - 표준출력을 표준에러로 보내기
 * 프로그램을 실행했을때의 표준출력을 디스크립터 대신 표준에러와 같은 방식으로 출력
 * 
 * -변수
 * 환경변수: 초기설정에 대한 정보를 저장하는 변수
 * 특수변수: 쉘프로그램에 인수로 전달될떄 사용되거나 현재쉘의 프로세스번호등으로 사용됨.
 * 
 * 조건문
 * lt <
 * gt >
 * eq ==
 * ne !=
 * ge >=
 * le <=
 * 
 * if- else::
 * if [조건1] ; 
 * 	then 문장1
 * elif [조건2] ;
 * 	then
 * else
 * 	문장2
 * fi
 * 
 * 입출력
 * echo -n 'msg~~'
 * read num
 * echo $num
 * 
 * 
 * 
 * ---------Prac 
 * 쉘 스크립트로 데이터를 입력받아 메뉴를 선택.
 * 메뉴
 * 1. 짜장면
 * 2.짬뽕
 * 3.탕슉
 * 번호를 선택하세요!!!
 * 선택한 메뉴는 @@@@ 입니다.
 * 
 * echo -s '1. 짜장'
 * echo -s '2. 짬'
 * echo -s '3. 탕'
 * echo -n 'choose the num'
 * read num
 * if [ $num -eq 1 ];
 * 	then echo '짜'
 * elif [ $num -eq 2 ];
 * 	then echo '짬'
 * else
 * 	echo '탕'
 * fi
 * 
 * --------PRac
 * 점수를 입력받아 입력한 점수에 대하여 학점 A~F로 환산해주는 .sh을 만들라.
 * 
 */
}
