"""
UDP_bone_send_ToGrasshopper.py

動画を再生し、MediaPipeで骨格データ（33点×xyz）を取得し、
UDPでGrasshopperに送信するスクリプト。

Requirements:
    pip install opencv-python mediapipe python-osc

Usage:
    1. MODEL_PATH に pose_landmarker_lite.task のパスを設定
    2. VIDEO_PATH に解析したい動画のパスを設定
    3. Grasshopper側でUDP Receiverを起動（Port: 12345）
    4. python UDP_bone_send_ToGrasshopper.py
"""

import cv2
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
from pythonosc import udp_client
import time

# ======================
# 設定
# ======================
UDP_IP   = "127.0.0.1"   # Grasshopper側のIPアドレス
UDP_PORT = 12345          # Grasshopper側のUDPポート番号

MODEL_PATH = r"./models/pose_landmarker_lite.task"  # MediaPipeモデルのパス
VIDEO_PATH = r"./video/input.mp4"                   # 解析する動画のパス

MAX_LOOPS = 3  # 動画の繰り返し再生回数

# ======================
# UDP クライアント初期化
# ======================
client = udp_client.SimpleUDPClient(UDP_IP, UDP_PORT)

# ======================
# MediaPipe PoseLandmarker 初期化
# ======================
base_options = python.BaseOptions(model_asset_path=MODEL_PATH)
options = vision.PoseLandmarkerOptions(
    base_options=base_options,
    running_mode=vision.RunningMode.VIDEO  # 動画モード
)
detector = vision.PoseLandmarker.create_from_options(options)

# ======================
# 動画キャプチャ初期化
# ======================
cap = cv2.VideoCapture(VIDEO_PATH)
fps = cap.get(cv2.CAP_PROP_FPS)
frame_interval = 1.0 / fps  # 1フレームあたりの時間（秒）

start_time = time.time()
loop_count = 0

# ======================
# メインループ
# ======================
while True:
    frame_start = time.time()

    ret, frame = cap.read()
    if not ret:
        # 動画の末尾に達したらループ
        loop_count += 1
        if loop_count >= MAX_LOOPS:
            print("再生完了（%d回）" % MAX_LOOPS)
            break
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)  # 先頭に戻す
        continue

    # BGRからRGBに変換（MediaPipe用）
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=frame_rgb)

    # タイムスタンプ（ミリ秒）
    timestamp_ms = int((time.time() - start_time) * 1000)

    # 骨格推定
    result = detector.detect_for_video(mp_image, timestamp_ms)

    if result.pose_landmarks:
        # 33点 × xyz = 99個の座標値をリストに格納
        coords = []
        for lm in result.pose_landmarks[0]:
            coords.append(float(lm.x))
            coords.append(float(lm.y))
            coords.append(float(lm.z))

        # UDPで送信（/pose アドレスに99個のfloat値）
        client.send_message("/pose", coords)
        print("sent %d values" % len(coords))

    # 動画プレビュー表示（qキーで終了）
    cv2.imshow("Pose", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    # FPSに合わせて待機（実時間に同期）
    elapsed = time.time() - frame_start
    wait = frame_interval - elapsed
    if wait > 0:
        time.sleep(wait)

# ======================
# 後処理
# ======================
cap.release()
cv2.destroyAllWindows()
