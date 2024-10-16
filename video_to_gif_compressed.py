import cv2
import imageio

# 비디오 파일 경로
video_path = r"D:\12304069_1080_1920_30fps.mp4"
output_gif_path = r"D:\12304069_1080_1920_30fps.mp4.gif"

# 비디오 로드
cap = cv2.VideoCapture(video_path)

# 비디오 파일 열렸는지 확인
if not cap.isOpened():
    print(f"Error: 비디오 파일을 열 수 없습니다. 경로를 확인하세요: {video_path}")
    exit()

# 프레임을 저장할 리스트
frames = []

# 프레임 크기 설정 (해상도 더 낮추기)
desired_width = 854 #640. 해상도를 더 줄여서 파일 크기를 낮춤
desired_height = 480 #360

# 프레임을 하나씩 처리
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # 해상도 변경 (원본 프레임을 줄임)
    frame_resized = cv2.resize(frame, (desired_width, desired_height))
    
    # OpenCV는 BGR로 이미지를 처리하므로 RGB로 변환
    frame_rgb = cv2.cvtColor(frame_resized, cv2.COLOR_BGR2RGB)
    
    # 프레임을 리스트에 추가
    frames.append(frame_rgb)

# 비디오 파일 해제
cap.release()

# 프레임 리스트를 확인
if len(frames) == 0:
    print("Error: 비디오에서 프레임을 읽어오지 못했습니다.")
else:
    # 프레임 리스트를 GIF로 저장 (무한 반복 설정)
    imageio.mimsave(output_gif_path, frames, fps=10, quantize=64, loop=0)  # loop=0으로 무한 반복 설정
    print(f"GIF 저장 완료: {output_gif_path}")


