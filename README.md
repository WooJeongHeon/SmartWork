# SmartWork (스마트 병영업무시스템)

## 링크 제공
[스마트 병영업무시스템 사이트 방문하기!!](http://smartwork.woojeongheon.com/)


[프로젝트 소개 영상 보기](https://drive.google.com/file/d/1pRlh89E7J_gn7mIWNP6epT-0PQc04K0F/view?usp=sharing)

## 개발자 정보(Contact Information)
* 프로젝트명: 스마트 병영업무시스템
* 개발자: 상병 우정헌
*(진급으로 인해 명단상에는 일병으로 표기될 수 있습니다.)*
* 팀명: SmartWork
* 주요내용: 휴가를 등록하면 출타자관리, 인원현황, 부대일정, 근무교체가 자동으로 수행되고 실시간으로 알려주는 업무 서비스, 부대 환경에 특화할 수 있는 커스텀 페이지가 있다.
* 개발자 이메일: email@woojeongheon.com

## 설치 안내 (Installation Process)

### BackEnd (Django 이용)
Python Package Installer
```bash
$ apt-get install python3-pip
```
BackEnd framework
```bash
$ pip3 install Django
```
Login module
```bash
$ pip3 install django-allauth
```
form layout
```bash
$ pip3 install django-crispy-forms
```
markdown form
```bash
$ pip3 install django-markdownx
```




### 사용 버전 안내
- Django (2.2.6)
- django-allauth (0.40.0)
- django-crispy-forms (1.8.0)
- django-markdownx (2.0.28)


## 사용법 (Getting Started)
가상환경 실행
```bash
$ source venv/bin/activate
```
DB 생성
```bash
$ python3 manage.py makemigrations
```
DB migrate
```bash
$ python3 manage.py migrate
```
superuser생성 (사이트의 모든 기능 사용가능)
```bash
$ python3 manage.py createsuperuser
```
BackEnd 서버 실행
```bash
$ python3 manage.py runserver --insecure
```





## 개발 동기


군부대나 일반 회사에는 대부분 업무 처리를 할 수 있는 인트라넷 시스템들이 갖추어져 있습니다.
하지만 시스템이 해당 기관의 업무에 특화되어 있지 않은 경우가 많아 협업과 최신화에 어려움이 있으며 중복적으로 업무를 하게 되는 불편함이 생기기도 합니다. 결국 시간과 비용적으로 큰 손해를 보는 결과가 발생하게 됩니다.
이를 해결하기 위해 공유, 협업, 자동화, 맞춤성과 통합 관리 등을 극대화하여 업무를 간소화할 수 있는 신개념의 스마트 업무 처리 시스템을 기획하였습니다.


## 이용 가능성
해당 프로젝트는 군부대, 회사, 학교 등 여러 기관에서 이용이 가능하고 자료만 입력하면 대부분의 업무를 자동화하여 수행하므로 4차 산업혁명에 걸맞게 사업 전망 또한 매우 좋습니다.


실례로 부대에서 휴가 신청을 하게 되면 출타 비율과 빈도를 수기로 계산 후 엑셀 파일로 출타를 종합하고, 출력하여 문서로 공지하게 됩니다. 이를 근거로 상황판에 휴가 인원을 기재하고, 해당 날의 근무와 청소구역을 찾아 다시 교체하여 작성하는 등 여러 작업을 반복하는 비효율적인 면들이 존재합니다.  이런 상황에서 휴가 일정이 변경되기라도 하면 모든 문서를 다시 초기화해야 하며 기존 자료와 혼선이 발생하기도 합니다. 


여기에 스마트 국방업무처리 시스템을 이용하면 휴가자는 출타 관리 페이지에서 실시간 출타율을 보며 원하는 날짜에 휴가를 신청할 수 있습니다. 물론 훈련 등의 이유로 휴가 불가 기간을 지정해 두면 휴가 신청은 불가능합니다. 휴가를 신청하면 지휘관의 계정에 승인 요청이 뜨며 승인 시에 자동으로 출타 인원 현황이 종합되어 부대 일정과 부대일지에 등록이 됩니다. 또한 해당 일의 근무와 청소구역에 변경 표시가 활성화되어 교체 요청이나 자동 재편성이 가능해집니다. 필요시에는 휴가 행선지를 공유하여 카풀이나 배차를 이용할 수도 있습니다.


이러한 기능들은 군부대뿐만이 아니라 타 기관에서도 특성에 맞게 배치해 사용할 수 있으며 개인이 새로운 기능을 만들었을 경우에 깃허브의 Pull requests를 통해 commit을 하게 되면 프로그래밍 기술이 없지만 해당 기능이 필요한 다른 기관에서도 관리자 페이지의 GUI를 통해 손쉽게 추가하여 사용할 수 있는 강점이 있습니다.

## 기본 프로젝트 구조

1. 부대 업무


	- 출타 관리
	- 인원 현황
	- 부대 일정
	- 근무 관리


2. 부대 활동


	- 공지사항
	- 감사나눔 1·2·3 운동
	- 1·1·30·30 캠페인
	- 부대 밴드
	- 마음의 편지
	- **커스텀 페이지**


3. 연계 사이트


	- 나라사랑 포털
	- 국방부
	- 국방부 오픈소스아카데미
	- **커스텀 페이지**
