# 개발 환경 설정 및 Flask 설치 가이드

이 문서에서는 파이썬 설치부터 Flask 패키지 설치까지, 그리고 Visual Studio Code 설치와 확장 기능 설정까지의 과정을 안내합니다.

## 1. 파이썬 설치하기

파이썬 공식 홈페이지에서 **`.tgz`** 파일을 다운로드하여 설치합니다.

### 1.1. 다운로드 및 압축 해제

1. 파이썬 설치 파일을 다운로드합니다. (버전은 **3.13.5**로 예시)
2. 터미널에서 해당 폴더로 이동하여 아래 명령어로 압축을 해제합니다:

   ```zsh
   tar -xvzf Python-3.13.5.tgz
   ```

### 1.2. 파이썬 컴파일

압축을 해제한 디렉토리로 이동한 후, 파이썬을 컴파일합니다:

```zsh
cd Python-3.13.5
./configure --enable-optimizations
make
```

**권한 문제**로 `sudo` 명령어를 사용할 수 없을 경우, `--prefix` 옵션을 사용하여 사용자 권한이 있는 디렉토리로 설치할 수 있습니다:

```zsh
./configure --prefix=$HOME/python3.13 --enable-optimizations
make
make install
```

## 2. 파이썬과 파이썬 패키지 관리자를 환경 변수로 등록하기

### 2.1. 경로 확인

파이썬과 `pip3`의 경로를 확인한 후, 환경 변수에 추가합니다. `~/.zshrc` 파일을 열어 아래와 같이 경로를 추가합니다:

```zsh
export PATH="/usr/local/bin:$PATH"
```

### 2.2. 환경 변수 적용

`~/.zshrc` 파일을 수정한 후, 변경 사항을 적용하려면 아래 명령어를 입력합니다:

```zsh
source ~/.zshrc
```

## 3. 파이썬 패키지 관리자로 Flask 패키지 설치

파이썬의 패키지 관리자 `pip`를 사용하여 **Flask**를 설치합니다:

```zsh
pip3 install Flask
```

## 4. 터미널에서 파이썬 실행하여 "Hello" 반환하는 함수 작성하기

파이썬을 실행하고 `hello`라는 함수를 작성하여 `"Hello"`를 반환하게 합니다:

1. 터미널에서 파이썬 셸을 실행합니다:

   ```zsh
   python3
   ```

2. 파이썬 셸에서 다음과 같이 `hello` 함수를 작성합니다:

   ```python
   def hello():
       return "Hello"
   ```

3. 함수를 실행하여 `"Hello"`를 반환하는지 확인합니다:

   ```python
   hello()
   ```

4. `"Hello"`가 반환되는지 확인합니다.

## 5. Visual Studio Code 설치 및 Material Icon Theme 설치하기

### 5.1. Visual Studio Code 설치

1. Visual Studio Code 공식 홈페이지에서 **`.tar.gz`** 파일을 다운로드합니다. 예시:

   ```
   code-stable-x64-<version>.tar.gz
   ```

2. 다운로드한 파일을 압축 해제합니다:

   ```zsh
   tar -xvzf code-stable-x64-<version>.tar.gz
   ```

3. 압축 해제한 디렉토리로 이동합니다:

   ```zsh
   cd VSCode-directory
   ```

4. Visual Studio Code를 실행합니다:

   ```zsh
   ./code
   ```

### 5.2. Material Icon Theme 설치

1. Visual Studio Code가 실행되면, **확장 탭**을 엽니다.
2. **검색창에** `Material Icon Theme`을 입력한 후, 설치 버튼을 클릭하여 확장을 설치합니다.

## 6. 보너스 과제

1. **Vim**을 사용하여 터미널에서 `python_webframework.md` 파일을 작성합니다:

   ```zsh
   vim python_webframework.md
   ```

2. 파일 내용을 작성한 후 저장하고 종료합니다.

