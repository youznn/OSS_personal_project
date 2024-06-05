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
|Linux|⭕️|
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
## Functions
### restart_button()

- Description: 게임 오버 시 재시작 화면을 표시합니다.
	- 사용자가 Enter 키를 누르면 게임을 재시작하고, ESC 키를 누르면 게임을 종료합니다.
### game_over(snake_body)

- Description: 게임 오버 조건을 확인하고, 목숨이 남아 있는지 여부에 따라 게임을 재시작하거나 종료합니다.
	- 목숨이 남아 있을 경우 뱀을 중앙으로 이동시키고, 목숨이 모두 소진되면 재시작 버튼을 표시합니다.
### blink_snake(snake_body)
- Description: 목숨이 소진된 후 뱀의 몸을 깜박이게 하는 효과를 구현합니다.
	- 1초 동안 뱀의 몸을 깜박이게 합니다.

### start_screen()

- Description: 게임 시작 화면을 표시합니다.
	- 사용자가 난이도를 선택할 수 있도록 하고, Enter 키를 누르면 게임을 시작합니다.

### show_score(choice, color, font, size)

- Description: 현재 점수를 화면에 표시합니다. 점수와 남은 목숨(하트)을 화면에 표시합니다.

### main()
- Description: 게임의 메인 로직을 포함하는 함수입니다.
 	- 게임 변수 초기화, 뱀과 음식의 위치 설정, 게임 루프, 뱀의 움직임, 음식 생성, 게임 오버 조건 등을 포함합니다.

## Varients

- apple_image, heart_image, snake_head_image, snake_body_image: 게임에 사용되는 이미지들을 로드하고 크기를 조정합니다.

- font_path: 폰트 파일의 경로를 설정합니다.

- difficulty: 게임의 난이도를 설정합니다. 기본값은 25입니다.

- frame_size_x, frame_size_y: 게임 창의 크기를 설정합니다.

- black, white, yellow, orange, red, green, blue: 게임에 사용될 색상들을 정의합니다.

- score, lives: 점수와 목숨의 초기값을 설정합니다. 게임 오버 시 목숨이 줄어들고, 목숨이 모두 소진되면 게임이 종료됩니다.

## Flow
### 초기화
Pygame을 초기화하고 게임 창을 설정합니다. 이미지와 색상 등을 로드하고 초기화합니다.

### 시작 화면
start_screen() 함수가 호출되어 사용자가 난이도를 선택하고 게임을 시작할 수 있습니다.

### 게임 루프
main() 함수에서 게임 루프가 시작됩니다. 뱀의 위치와 음식의 위치를 설정하고, 뱀의 움직임을 처리합니다. 게임 오버 조건을 확인하고, 점수와 목숨을 화면에 표시합니다.

### 게임 오버

뱀이 벽에 부딪히거나 자신의 몸과 충돌하면 게임 오버가 됩니다.
목숨이 남아 있을 경우 게임을 재시작하고, 목숨이 모두 소진되면 재시작 버튼을 표시합니다.


---
# TODO
- 몸 깜박인 후 이전 위치가 사라지지 않는 오류 수정
- 테마 설정 기능
- 유저 입력 입력받고, 명예의 전당 기능 추가


