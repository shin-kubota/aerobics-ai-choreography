# aerobics-ai-choreography
**AI-powered aerobics choreography system for aging society**  
高齢化社会に向けたAIエアロビクスコリオ生成システム

---

## 🎯 Problem / 課題

Japan faces a serious shortage of aerobics instructors due to its aging society. Existing dance AI systems generate movements for "performance," but fail to model the **instructional structure** required for teaching: 8-count rhythm, bilateral symmetry, and safety.  This approach utilizes multiple LLMs and machine learning techniques, and in the future we will study modeling to generate aerobic choreography.

日本では少子高齢化により、エアロビクスインストラクターの不足と後継者問題が深刻化しています。既存のダンスAIは「見せるための動き」を生成しますが、**教えるための運動構造**（8カウント・左右対称・安全性）はモデル化されていません。このアプローチは複数のLLMや機械学習等を駆使し、将来的にはエアロビクスのコリオを生成するモデリングを研究します。

---

## 💡 Approach / アプローチ

| Feature | Status |
|---------|--------|
| Skeleton data acquisition via MediaPipe Pose (33 points) / MediaPipe Poseによる骨格データ取得（33点） | ✅ |
| UDP streaming from Python → Rhino/Grasshopper 3D visualization / PythonからUDP送信 → Grasshopper 3D可視化 | ✅ |
| LLM-based choreography generation with 8-count structure / LLMによる8カウント構造コリオ自動生成 | ✅ |
| Music BPM sync (MIDI-based) / 音楽BPMとの同期設計（MIDI基準） | 🚧 設計済み・未実装 |

---

## 🎬 Demo / デモ

▶️ [Instagram: 生成AIによるエアロビクスコリオ可視化](https://www.instagram.com/reel/DU6gtidk7Pi/)

---

## 📦 Demo Scripts / デモスクリプト配布

This repository includes demo scripts to extract skeleton (bone) data from video using MediaPipe and send it to Grasshopper via UDP.  
動画からMediaPipeで骨格データを取得し、UDPでGrasshopperに送信するデモスクリプトを配布しています。

| File | Description |
|------|-------------|
| `UDP_bone_send_ToGrasshopper.py` | Extract pose landmarks from video and send via UDP / 動画から骨格座標を取得してUDP送信 |
| `mediapipe_to_Point_Bone_Demo.gh` | Grasshopper receiver / Grasshopper側レシーバー |

> Anyone can visualize human motion data in Grasshopper using these scripts.  
> これらのスクリプトで誰でもGrasshopperで人体動作を可視化できます。

### ⚠️ Known Issue: Windows Defender Firewall / ファイアウォールの注意点

UDP communication between Python and Grasshopper may be blocked by Windows Defender Firewall.  
PythonとGrasshopperのUDP通信がWindows Defender Firewallにブロックされる場合があります。

- **Python** (sender / 送信側)
- **Rhino 7** (receiver / 受信側・GrasshopperはRhino7内で動作)
- Default: IP `127.0.0.1` / Port `12345`

---

## 🔧 Tools / 使用ツール

Gemini, ChatGPT, Claude, MediaPipe (Python), Grasshopper (Rhino 7)

---

## 🔧 System Architecture / システム構成
```
Video / Webカメラ
  ↓
MediaPipe Pose（Skeleton Estimation / 骨格推定）
  ↓
LLM（Choreography Modeling / コリオモデル化）
  ↓
UDP（Python）
  ↓
Grasshopper（3D Visualization / 3D可視化）
```

## 👤 Author / 著者

**Shin Kubota**

- Executive Officer & General Manager, Engineering Dept. / 執行役員 技術部長（東証プライム上場企業・医療機器メーカー）
- 27+ years in medical device development, production engineering & AI implementation / 27年以上の医療機器開発・生産技術・AI実装経験（眼光学・SaMD・QMS・自動化）
- M.Eng. Optical Engineering, Tokyo Polytechnic University / 東京工芸大学大学院 光工学専攻 修士（工学）
- M.Tech. Innovation & Design Engineering, AIIT / 東京都立産業技術大学院大学 修士（創造技術）
- Collaborative Researcher, Chiba University / 千葉大学大学院 研究員
- Researcher, Research Center for Health Design, AIIT / 東京都立産業技術大学院大学 健康デザイン研究所 研究員（介護予防・認知症予防・AI・IoT）
- [LinkedIn](https://www.linkedin.com/in/shinkubota/)

