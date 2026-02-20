# aerobics-ai-choreography

**AI-powered aerobics choreography system for aging society**  
高齢化社会に向けたAIエアロビクスコリオ生成システム

---

## 🎯 Problem / 課題

日本では少子高齢化により、エアロビクスインストラクターの不足と後継者問題が深刻化しています。既存のダンスAIは「見せるための動き」を生成しますが、**教えるための運動構造**（8カウント・左右対称・安全性）はモデル化されていません。

---

## 💡 Approach / アプローチ

- MediaPipe Poseによる骨格データ取得（33点）| ✅ 実装済み |
- PythonからUDP送信 → Rhinoceros/Grasshopperでリアルタイム3D可視化| ✅ 実装済み |
- LLMによる8カウント構造に基づくコリオ自動生成| ✅ 実装済み |
- 音楽BPMとの同期設計（MIDI基準）：未実装| 🚧 設計済み・未実装 |

---

## 🎬 Demo / デモ

▶️ [Instagram: 生成AIによるエアロビクスコリオ可視化](https://www.instagram.com/reel/DU6gtidk7Pi/)

---
## 🔧 Tools / 使用ツール

Tools used: Gemini, ChatGPT, Claude, MediaPipe(Python), Grasshopper(Rhino7)

---

## 🔧 System Architecture / システム構成
```
動画/Webカメラ
  ↓
MediaPipe Pose（骨格推定）
  ↓
LMM(モデル化)
  ↓
UDP送信（Python）
  ↓
Grasshopper（3D可視化）
```

---

## 👤 Author / 著者

**Shin Kubota**

- Executive Officer & General Manager, Engineering Dept.
  執行役員 技術部部長（東証プライム上場企業・医療機器メーカー）
- 27年以上の医療機器開発・生産技術開発・実装経験（眼光学・SaMD・QMS・生産技術・自動化・AI実装）
- 東京都立産業技術大学院大学 修士（創造技術）/ 東京工芸大学大学院 光工学専攻 修士（工学）
- 千葉大学大学院 研究員 / 東京都立産業技術大学院大学 健康デザイン研究所 研究員（介護予防・認知症予防・AI・IoT）
- [LinkedIn](https://www.linkedin.com/in/shinkubota/)
