import cv2
import imageio

# 비디오 파일 경로
video_path = 'H:/이채영/Flying_Bird_object_Dataset_in_Surveillance_Video/FBD-SV-2024/videos/output/bird_446_detected_split.mp4'
output_gif_path = 'H:/이채영/Flying_Bird_object_Dataset_in_Surveillance_Video/FBD-SV-2024/videos/output/bird_446_detected_split.gif'

# 비디오 로드
cap = cv2.VideoCapture(video_path)

# 비디오 파일 열렸는지 확인
if not cap.isOpened():
    print(f"Error: 비디오 파일을 열 수 없습니다. 경로를 확인하세요: {video_path}")
    exit()

# 프레임을 저장할 리스트
frames = []

# 프레임을 하나씩 처리
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # OpenCV는 BGR로 이미지를 처리하므로 RGB로 변환
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    # 프레임을 리스트에 추가
    frames.append(frame_rgb)

# 비디오 파일 해제
cap.release()

# 프레임 리스트를 확인
if len(frames) == 0:
    print("Error: 비디오에서 프레임을 읽어오지 못했습니다.")
else:
    # 프레임 리스트를 GIF로 저장
    imageio.mimsave(output_gif_path, frames, fps=10)  # fps 값을 조정 가능 (기본 10)
    print(f"GIF 저장 완료: {output_gif_path}")
