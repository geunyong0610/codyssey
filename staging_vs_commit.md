# 스테이징 영역과 커밋의 차이

## 1. 스테이징 영역 (Staging Area)

- 스테이징 영역은 Git에서 **"커밋할 준비가 된 파일 목록을 보관하는 중간 단계"**
- 파일을 수정하고 나면 Git은 변경 내용을 자동으로 커밋하지 않음,
  대신 사용자가 **`git add` 명령어를 통해 스테이징 영역에 추가**해야!!
- 스테이징 영역에 추가된 파일은 **"곧 커밋될 예정임"**을 의미함
- 이 단계에서 원하는 파일만 선택적으로 커밋할 수 있음

### 예시
```bash
git add main.py
```

→ `main.py` 파일을 스테이징 영역에 추가함

---

## 2. 커밋 (Commit)

- 커밋은 스테이징 영역에 있는 파일들의 변경 내용을 **Git 로컬 저장소에 영구적으로 기록하는 작업**
- 커밋을 하면 해당 시점의 코드 상태가 저장되며, 버전 관리를 할 수 있음
- 커밋 메시지를 통해 변경 내용을 설명할 수 있음

### 예시
```bash
git commit -m "Fix bug in main.py"
```

→ 스테이징된 파일을 로컬 저장소에 저장하고, 커밋 메시지를 남김

---

## 3. 요약 비교

| 구분           | 설명                                                  |
|----------------|-------------------------------------------------------|
| 스테이징 영역  | 수정된 파일을 **곧 커밋할 예정**이라고 표시하는 곳     |
| 커밋           | 스테이징된 내용을 **Git 로컬 저장소에 기록**하는 행위  |

---

## 4. 전체 흐름

1. 파일 수정 →  
2. `git add` → 스테이징 영역에 추가 →  
3. `git commit` → 로컬 저장소에 저장

이렇게 Git은 **2단계 저장 구조**를 통해 원하는 변경만 선택적으로 관리할 수 있게 해줌