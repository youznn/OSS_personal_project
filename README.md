# Snake Eater 🎮🐍🍎
본 게임은 성균관대학교 오픈소스소프트웨어 실습 프로젝트의 일환으로 python과 pygame 라이브러리로 구현한 간단한 snake 게임입니다. rajatdiptabiswas의 snake-pygame을 기반으로 기능을 추가하여 업그레이드 했습니다. 해당하는  원본 소스는 [rajatdiptabiswas/snake-pygame](https://github.com/rajatdiptabiswas/snake-pygame)에서 확인하실 수 있습니다. 


# 구현 목표
본 프로젝트는 snake🐍가 가능한 많은 사과🍎를 먹어 최대한 높은 점수를 얻는 것을 목표로 합니다. 플레이어는 총 세 개의 목숨❤️으로 시작하며, 게임 오버 조건 충족 시마다 목숨이 하나씩 닳아 목숨이 모두 소진되면 게임이 종료됩니다.


# Features

## 기존 기능

1. snake의 머리가 먹이에 닿을 때마다 점수가 1씩 오르고 몸통이 길어집니다.
2. 게임 오버 조건 충족 시 프로그램이 종료됩니다.
	1) snake의 머리가 벽에 닿는 경우
    2) snake의 머리가 자신의 몸통에 닿는 경우

## 추가 기능
1. 시작 스크린 구현
	- 플레이어는 시작 전 EASY, MEDIUM, HARD, IMPOSSIBLE로 이루어진 네 가지의 난이도 중 한 가지를 선택할 수 있습니다.
    -  플레이어는 Enter 키를 입력하여 게임을 시작합니다.
  

2. 게임 추가 기능
	- 이미지 추가
    	- snake, food, lives의 이미지를 기존 pygame에서 제공하는 기본 선에서 이미지로 대체했습니다.
    - 목숨 시스템
    	- 플레이어는 3개의 목숨을 가지며, 게임오버 조건 달성 시 목숨을 하나씩 잃게 됩니다.
    - snake, food 크기 조정
    	- 기존 snake와 food의 두 배로 사이즈를 조정하여 가시성을 높였습니다.

3. 재시작 기능 추가 
목숨을 모두 잃을 경우, 재시작을 묻는 스크린으로 이동하여 Enter 키 입력 시 게임 재시작이 가능합니다.

# Reference
[1] https://github.com/pygame/pygame "pygame"

[2] https://www.dafont.com/retro-gaming.font "Retro Gaming Font"

[3] https://github.com/rajatdiptabiswas/snake-pygame "snake-pygame"

# 실행 예시

![mygame](https://github.com/youznn/oss_personal_project_phase1/assets/113789141/f92c626d-8f81-4ff9-9483-4d9752c592fe)

# 지원 OS 및 실행 방법
## 지원 OS
|OS|지원여부|
|---|---|
|Windows|⭕️|
|Linux||
|Mac|⭕️|

### Windows
1. python 3.12 버전을 설치합니다. https://www.python.org/downloads/
2. windows powershell에서 다음 명령어를 입력하여 pygame을 설치합니다.
 ```
 pip3 install pygame
 ```
3. 재부팅 이후 `python3 main.py`를 실행하면 게임이 시작됩니다.

### Linux
터미널을 열고 다음 과정을 차례로 수행합니다.
1. python 3.12 설치
  ```
  sudo apt-get update
  sudo apt-get install python3
  ```
2. pip 설치
  ```
  sudo apt-get install python3-pip
  ```
3. pygame 설치
  ```
  sudo apt-get install python3-pip
  ```
4. 프로젝트 최상위 디렉토리에서 `python3 main.py`를 실행하면 게임이 시작됩니다.

### Mac OS
터미널을 열고 다음 과정을 차례로 수행합니다.
1. pygame 설치
  ```
   pip3 install pygame
  ```
2. 프로젝트 최상위 디렉토리에서 `python3 main.py`를 실행하면 게임이 시작됩니다.

# 코드 설명


