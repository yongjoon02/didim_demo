import cv2
import time
from datetime import datetime

def record_video(duration=5):
    # 웹캠 초기화
    cap = cv2.VideoCapture(0)
    
    # 비디오 저장을 위한 설정
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = 20.0
    
    recording = False
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
            
        # 현재 화면 표시
        cv2.imshow('Camera', frame)
        
        # 키 입력 확인
        key = cv2.waitKey(1) & 0xFF
        
        # 's' 키를 누르면 녹화 시작
        if key == ord('s') and not recording:
            recording = True
            # 현재 시간을 파일명으로 사용
            filename = f"video_{datetime.now().strftime('%Y%m%d_%H%M%S')}.mp4"
            out = cv2.VideoWriter(filename, cv2.VideoWriter_fourcc(*'mp4v'), fps, (frame_width, frame_height))
            start_time = time.time()
            print(f"녹화를 시작합니다. {duration}초 동안 저장됩니다.")
        
        # 녹화 중이면 프레임 저장
        if recording:
            out.write(frame)
            # 지정된 시간이 지나면 녹화 종료
            if time.time() - start_time >= duration:
                recording = False
                out.release()
                print("녹화가 완료되었습니다.")
        
        # 'q' 키를 누르면 종료
        if key == ord('q'):
            break
    
    # 자원 해제
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    # 5초 동안 녹화하는 예제
    record_video(duration=5)
