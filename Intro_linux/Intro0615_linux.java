package doc;

public class Intro0615_linux {
/*
 * cat /etc/group  >>사용자, 그룹 상태/비밀번호 유무.
 * 
 * 
 * 그룹추가하기 groupadd 추가할그룹이름
 * 
 * useradd [-option] 신규사용자명
 * ex) useradd newuser : newuser라는이름으로 신규사용자 추가
 * useradd -u 사용ID 신규사용자명
 * ex) useradd -u 1111 newuser2   // 기존에 이 사용자이름이 없는상태여야함.
 *  ==>newuser2 사용자 생성하면서 사용자id는  1111로 한다.
 * 
 * useradd -g 그룹이름 그룹에추가할사용자
 * ex) useradd -g mygroup newuser
 * useradd -d 사용자디렉토리 추가할사용자명
 * ex) useradd -g /home/newhome newuser4
 * useradd -s 사용자셸스크립트
 * ex) useradd -s /bin/csh newuser5
 * 
 * passwd: 사용자의 비밀번호를 지정하거나 변경, 권한따른 root제한.
 * 형식: passwd 사용자명
 * ex) passwd newuser
 * usermod: 사용자 속성변경으로 useradd와 동일
 * userdel: 사용자를 삭제처리.
 * 형식: userdel [옵션-r] 사용자명
 * 
 * chage 옵션1 옵션2 사용자 - 암호주기적 변경
 * -옵션1
 * -l: 사용자 설정사항, 조회기능
 * ex)chage -l newuser03
 * -m 날수: 암호변경최소일자
 * ex)chage -m 2 newuser03 : newuser03사용자가 암호를 사용해야하는 최소일을 지정- 변경후 최소2일을 사용함.
 * -M 날수: 암호변경 최대일자
 * ex) chage -M 30 newuser03 : newuser03 사용자 설정암호의 최대일자 30일을 사용함.
 * -E yyyy/MM/dd 사용자계정 해당만료일자지정.
 * ex) chage -E 2020/12/10 newuser03
 * -W 날수: 만료예고하는 날수.
 * 
 * groups: 현재사용자가 소속된 그룹표시
 * groups 사용자 : 소속그룹조회
 * groupadd 옵션1 옵션2 추가그룹
 * 	옵션1(-g)
 * 	옵션2(id명 지정)
 * 	ex) groupadd newgroup
 * 	groupadd -g 2222 newgroup
 * groupmod 옵션1 대상그룹 변경그룹
 * groupdel
 * gpasswd 옵션1 사용자대상그룹
 * 
 * gpasswd : 그룹의 암호를 설정하거나 그룹관리를 처리
 * 형식: gpasswd [옵션1] [사용자명] 그룹명
 * 
 * gpasswd 그룹명: 그룹의 암호를 지정
 * 	ex) gpasswd newgroup
 * gpasswd -A 사용자명 그룹명: 해당사용자를 그룹에 "관리자"로 지정
 *  ex) gpasswd -A newuser newgroup
 * gpasswd -a 사용자명 그룹명: 해당 사용자를 그룹에 "사용자"로 지정
 *  ex) gpasswd -a user1 newgroup 
 * gpasswd -d 사용자명 그룹명: 해당 사용자를 그룹에서 제거.
 *  ex) gpasswd -d user1 newgroup
 * 
 * 
 * 
 * 
 */
}
