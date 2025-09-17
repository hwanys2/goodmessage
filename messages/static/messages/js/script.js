// 현재 시간 표시
function updateTime() {
    const now = new Date();
    const timeString = now.toLocaleString('ko-KR', {
        year: 'numeric',
        month: 'long',
        day: 'numeric',
        hour: '2-digit',
        minute: '2-digit',
        second: '2-digit'
    });
    document.getElementById('currentTime').textContent = timeString;
}

// 새로운 메시지 가져오기
async function getNewMessage() {
    const refreshBtn = document.querySelector('.refresh-btn');
    const messageCard = document.getElementById('messageCard');
    const messageText = document.getElementById('messageText');
    const categoryBadge = document.querySelector('.category-badge');
    
    // 버튼 로딩 상태
    refreshBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> 새 메시지 가져오는 중...';
    refreshBtn.disabled = true;
    
    // 카드 페이드 아웃
    messageCard.style.opacity = '0.5';
    messageCard.style.transform = 'scale(0.95)';
    
    try {
        const response = await fetch('/api/random-message/');
        const data = await response.json();
        
        // 잠시 대기 (부드러운 전환을 위해)
        await new Promise(resolve => setTimeout(resolve, 500));
        
        // 메시지 업데이트
        messageText.textContent = data.message;
        categoryBadge.textContent = data.category;
        
        // 카드 페이드 인
        messageCard.style.opacity = '1';
        messageCard.style.transform = 'scale(1)';
        
        // 타이핑 애니메이션 효과
        messageText.style.animation = 'none';
        setTimeout(() => {
            messageText.style.animation = 'typeWriter 0.8s ease-out';
        }, 100);
        
    } catch (error) {
        console.error('메시지를 가져오는 중 오류 발생:', error);
        messageText.textContent = '메시지를 불러올 수 없습니다. 다시 시도해주세요.';
        categoryBadge.textContent = '오류';
    } finally {
        // 버튼 복원
        refreshBtn.innerHTML = '<i class="fas fa-sync-alt"></i> 새 메시지 보기';
        refreshBtn.disabled = false;
    }
}

// 메시지 공유하기
function shareMessage() {
    const messageText = document.getElementById('messageText').textContent;
    const shareText = `오늘의 좋은 메시지: "${messageText}"`;
    
    if (navigator.share) {
        // Web Share API 지원하는 경우
        navigator.share({
            title: '오늘의 좋은 메시지',
            text: shareText,
            url: window.location.href
        }).catch(err => console.log('공유 취소됨'));
    } else {
        // 클립보드에 복사
        navigator.clipboard.writeText(shareText).then(() => {
            showNotification('메시지가 클립보드에 복사되었습니다! 📋');
        }).catch(err => {
            console.error('클립보드 복사 실패:', err);
            showNotification('공유 기능을 사용할 수 없습니다.');
        });
    }
}

// 알림 표시
function showNotification(message) {
    const notification = document.createElement('div');
    notification.className = 'notification';
    notification.textContent = message;
    notification.style.cssText = `
        position: fixed;
        top: 20px;
        right: 20px;
        background: linear-gradient(45deg, #4facfe, #00f2fe);
        color: white;
        padding: 15px 25px;
        border-radius: 10px;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
        z-index: 1000;
        animation: slideInRight 0.3s ease-out;
        font-weight: 500;
    `;
    
    document.body.appendChild(notification);
    
    setTimeout(() => {
        notification.style.animation = 'slideOutRight 0.3s ease-out';
        setTimeout(() => {
            document.body.removeChild(notification);
        }, 300);
    }, 3000);
}

// 키보드 단축키
document.addEventListener('keydown', function(event) {
    if (event.key === ' ' || event.key === 'Enter') {
        event.preventDefault();
        getNewMessage();
    }
});

// 페이지 로드 시 실행
document.addEventListener('DOMContentLoaded', function() {
    updateTime();
    setInterval(updateTime, 1000);
    
    // 자동 새로고침 (선택사항 - 30초마다)
    // setInterval(getNewMessage, 30000);
});

// 추가 CSS 애니메이션
const additionalStyles = document.createElement('style');
additionalStyles.textContent = `
    @keyframes slideInRight {
        from {
            transform: translateX(100%);
            opacity: 0;
        }
        to {
            transform: translateX(0);
            opacity: 1;
        }
    }
    
    @keyframes slideOutRight {
        from {
            transform: translateX(0);
            opacity: 1;
        }
        to {
            transform: translateX(100%);
            opacity: 0;
        }
    }
`;
document.head.appendChild(additionalStyles);
