# 오늘의 좋은 메시지 🌟

학생들을 위한 긍정적이고 따뜻한 메시지를 랜덤하게 표시하는 웹사이트입니다.  
교실 전자칠판에서 아침마다 새로운 메시지로 학생들에게 동기부여와 격려를 전할 수 있습니다.

## 주요 기능 ✨

- **랜덤 메시지 표시**: 새로고침할 때마다 다른 긍정적인 메시지
- **아름다운 UI**: 학생들이 좋아할 만한 현대적이고 아름다운 디자인
- **카테고리별 메시지**: 동기부여, 격려, 학습, 우정, 자신감 등 다양한 주제
- **반응형 디자인**: 데스크톱, 태블릿, 모바일 모든 기기에서 최적화
- **실시간 시간 표시**: 현재 날짜와 시간 표시
- **관리자 패널**: Django Admin을 통한 메시지 관리

## 포함된 메시지 카테고리 📝

- 🚀 **동기부여**: 학생들의 의욕을 북돋우는 메시지
- 💪 **격려**: 힘들 때 힘이 되는 응원 메시지  
- 📚 **학습**: 공부와 성장에 관한 메시지
- 👫 **우정**: 친구와 협력의 가치에 대한 메시지
- ⭐ **자신감**: 자존감과 자신감을 높이는 메시지
- 🙏 **감사**: 감사하는 마음에 대한 메시지
- 😊 **행복**: 긍정적인 마음가짐에 대한 메시지
- 🌱 **성장**: 개인적 성장과 발전에 대한 메시지

## 기술 스택 🛠️

- **Backend**: Django 5.2.6
- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **Database**: SQLite (개발), PostgreSQL (프로덕션)
- **Deployment**: Railway
- **Static Files**: WhiteNoise

## 로컬 개발 환경 설정 🔧

### 1. 프로젝트 클론
```bash
git clone <repository-url>
cd goodmessage
```

### 2. 가상환경 생성 및 활성화
```bash
conda create -n goodmessage python=3.12
conda activate goodmessage
```

### 3. 의존성 설치
```bash
pip install -r requirements.txt
```

### 4. 데이터베이스 마이그레이션
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. 샘플 메시지 추가
```bash
python add_sample_messages.py
```

### 6. 관리자 계정 생성
```bash
python manage.py createsuperuser
```

### 7. 개발 서버 실행
```bash
python manage.py runserver
```

이제 `http://127.0.0.1:8000`에서 웹사이트를 확인할 수 있습니다!

## Railway 배포 🚀

### 1. Railway 계정 생성
[Railway](https://railway.app)에서 계정을 생성합니다.

### 2. 프로젝트 연결
- GitHub 저장소를 Railway에 연결
- 자동으로 빌드 및 배포 시작

### 3. 환경 변수 설정 (선택사항)
Railway 대시보드에서 다음 환경 변수를 설정할 수 있습니다:
- `SECRET_KEY`: Django 비밀 키
- `DEBUG`: 디버그 모드 (False 권장)

### 4. 배포 완료
배포가 완료되면 Railway에서 제공하는 URL로 접속할 수 있습니다.

## 사용법 👩‍🏫

### 교실에서 사용하기
1. 전자칠판의 브라우저에서 웹사이트 접속
2. 전체화면 모드(F11)로 설정
3. 아침 시간이나 수업 시작 전에 새로고침하여 새로운 메시지 표시
4. 학생들과 함께 메시지를 읽고 하루를 시작

### 메시지 관리
1. `/admin/` URL로 관리자 페이지 접속
2. 관리자 계정으로 로그인
3. "좋은 메시지" 섹션에서 메시지 추가/수정/삭제
4. 카테고리별로 메시지 분류 및 관리

## 커스터마이징 🎨

### 새로운 메시지 추가
Django Admin 패널을 통해 쉽게 새로운 메시지를 추가할 수 있습니다:
1. 관리자 패널 접속
2. "Messages" → "Add" 클릭
3. 메시지 내용, 카테고리 입력
4. "Save" 클릭

### 디자인 수정
- CSS 파일: `good_messages/static/good_messages/css/style.css`
- HTML 템플릿: `good_messages/templates/good_messages/home.html`
- JavaScript: `good_messages/static/good_messages/js/script.js`

## 기여하기 🤝

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 라이선스 📄

이 프로젝트는 MIT 라이선스 하에 배포됩니다.

## 지원 및 문의 💬

문제가 발생하거나 새로운 기능을 제안하고 싶다면 Issues 탭에서 알려주세요!

---

**학생들의 하루를 더욱 밝게 만드는 작은 메시지의 힘을 믿습니다! 🌟**
