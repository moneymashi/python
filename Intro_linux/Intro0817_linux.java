package doc;

public class Intro0817_linux {
/*
 * ssh 보안
 * master와 slave1간의 명령및 파일전송
 * master에서 보안키를 생성, 각 node에 이 보안키를 전송해 master가 각 node데이터 서버에 접속할떄, 
 * 인증과정을 거치지않고도 ssh명령수행처리가능
 * 
 * 처리절차
 * master의 ~/.ssh/authorized_keys 파일의 내용에 (2번째녀석)보안키 부분을 copy한다
 * @@@주의@@@
 * linux부분 드래그+ 엔터(copy) >> edit plus >> 한 라인으로 만들어야한다. >> copy >> 
 * slave1접속 $ ssh slave1
 * vi ~/.ssh/authorized_keys  에 덧붙이기.
 * 
 * ssh slave1  >> vagrant@slave1
 * 
 * 
 * hdfs 하둡 파일시스템 명령어
 * :hdfs를 통해 data노드의 폴드와 파일을 생성
 * hdfs dfs -mkdir /user
 * 
 * vi ~/.ssh/authorized_keys
 * 
 * 
 * ------------------------
 * master에서 각 노드별로 파일전송
 * vagrant 초기위치: cd ~
 * hadoop 파일전송
 * 
 * master$ 
 * scp -drp hadoop-2.6.1 slave1:~/
 * scp ~/.bashrc slave1:~/.bashrc
 * 
 * ### 확인법
 * ssh slave1
 * vagrant@slave1 ~ $ ls
 * >> hadoop 2.6.1
 * ####
 * -----------------------------
 * 
 * ###
 * 예제인 워드카운트를 처리가능.
 * chmod 744 hadoop-mapreduce-examples-2.6.1.jar
 * 
 * 입력: 테스터할 hdfs에서 folder를 생성과 파일copy
 * hdfs dfs -put hadoop/etc/hadoop/hadoop-env.sh /user/vagrant/conf

 * 출력: 해당입력 파일로 결과folder 생성
 * ###명령: wordcount 자바파일실행
 * yarn jar hadoop-mapreduce-examples-2.6.1.jar wordcount conf output
 * 
 * 
 * vagrant@master$
 * hdfs dfs -mkdir /user
 * hdfs dfs -mkdir /user/vagrant
 * hdfs dfs -mkdir /user/vagrant/conf
 * 
 * 
 * ##  cd /home/vagrant/hadoop/share/hadoop/mapreduce
 * 
 * 
 * # MAP REDUCE
 * job : 데이터를 처리하는 mapper와 reducer들로 이루어진 프로그램 단위
 * ex)wordcount : 20개의 파일들을 입력으로 wordcount 실행
 * task : mapper나 reducer의 각각의 실행 인스턴스
 * ex) 20개의 입력파일들을 20개의 map task들과 다수의 reducer task들을 의미. 
 * task attempt : 한 머신에서 실행되는 특정 task
 * ex) 최소20개의 task attempt
 * 
 * # job 데이터분배
 * map reduce job이 실행될떄, 실행하는 jar과 옵션정보xml파일이 hdfs에 저장되고 ,
 * 이 파일의 다운로드 위치정보를 task tracker들에게 알려준다.
 * task tracker내부적으로 이 binary들을 다운받아 실행할수 있는 환경을 구성.
 * 
 * =============================이론부분설명....
 * configuration 클래스
 * mapper생성
 * writable클래스
 * 데이터읽기
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
