---
id: ASE-REVIEW-02
title: "第2章期中複習測驗"
course: advanced-software-engineering
type: review
status: needs-review
created: '2026-11-06'
updated: '2026-11-06'
sources: [ASE-002, EXAM-001]
tags: [期中測驗, AI練習題]
---
# 第2章｜期中複習測驗

本題庫為依講義重新編寫的 AI 練習題，不代表教師正式考卷。英文敘述、術語填空與圖表判讀參考 EXAM-001 的可見題型。每題 pages 指本章講義 PDF 頁次。

單選與填空可自動批改；手寫、簡答與繪圖使用參考答案及 rubric 自評，不計入自動題分數。圖檔僅供參考解答，先在紙上作答再展開。

[回本章課程](../lessons/chapter-02.md) · [測驗索引](index.md)

## 題庫資料

以下 JSON 為唯一題庫來源；網站建置時解析此區塊。手動維護後執行 python3 scripts/build.py。

```json
[
  {
    "type": "choice",
    "prompt": "依講義 p.19 的四層 V-Model，Architecture Design 對應哪個測試？",
    "options": [
      "Integration Testing",
      "Acceptance Testing",
      "只有語法檢查",
      "Unit Testing"
    ],
    "answer": 0,
    "explanation": "架構層重點是模組／子系統介面整合；詳細設計對應單元測試，系統規格對應系統測試。",
    "pages": [
      17,
      19
    ],
    "level": "理解",
    "id": "ASE-C2-Q01",
    "source": "ASE-002"
  },
  {
    "type": "choice",
    "prompt": "Waterfall 最容易讓哪個問題延遲到後期才被發現？",
    "options": [
      "程式語言是否有分號",
      "原始需求理解偏差",
      "團隊是否有姓名",
      "是否能建立資料夾"
    ],
    "answer": 1,
    "explanation": "客戶較晚看到可用軟體，需求誤解未能早期被回饋修正。",
    "pages": [
      12,
      14,
      16
    ],
    "level": "理解",
    "id": "ASE-C2-Q02",
    "source": "ASE-002"
  },
  {
    "type": "choice",
    "prompt": "第一版可查課，第二版再加入加選。這次擴充主要是？",
    "options": [
      "Verification",
      "Refactoring",
      "Incremental Development",
      "只有部署"
    ],
    "answer": 2,
    "explanation": "增加可用功能範圍是增量；反覆改善既有功能則偏疊代。",
    "pages": [
      25,
      26,
      33
    ],
    "level": "理解",
    "id": "ASE-C2-Q03",
    "source": "ASE-002"
  },
  {
    "type": "choice",
    "prompt": "哪個版本最符合垂直切片？",
    "options": [
      "先做全部資料表",
      "先做所有 API 但無可用介面",
      "只完成所有視覺稿",
      "完成可實際使用的查課介面、查詢邏輯與資料存取"
    ],
    "answer": 3,
    "explanation": "垂直切片貫穿必要層次，交付可端到端驗證的功能。",
    "pages": [
      26
    ],
    "level": "理解",
    "id": "ASE-C2-Q04",
    "source": "ASE-002"
  },
  {
    "type": "choice",
    "prompt": "Working software over comprehensive documentation 意味著？",
    "options": [
      "文件完全無價值",
      "更重視可運行成果，同時保留必要文件",
      "只看文件頁數驗收",
      "不需任何驗收條件"
    ],
    "answer": 1,
    "explanation": "敏捷偏重左項，但右項仍有價值；不是取消文件。",
    "pages": [
      40,
      42,
      43
    ],
    "level": "理解",
    "id": "ASE-C2-Q05",
    "source": "ASE-002"
  },
  {
    "type": "choice",
    "prompt": "Who orders the Product Backlog to maximize product value?",
    "options": [
      "Product Owner",
      "Scrum Master",
      "只有資料庫管理員",
      "自動編譯器"
    ],
    "answer": 0,
    "explanation": "PO 負責產品價值與待辦優先級；SM 支援流程，Developers 負責如何實作。",
    "pages": [
      48
    ],
    "level": "理解",
    "id": "ASE-C2-Q06",
    "source": "ASE-002"
  },
  {
    "type": "choice",
    "prompt": "團隊討論這次部署交接為何失敗、下次如何改善，最符合哪個事件？",
    "options": [
      "Sprint Review",
      "只做產品展示",
      "Sprint Retrospective",
      "使用者驗收"
    ],
    "answer": 2,
    "explanation": "Retrospective 檢視工作方式；Review 檢視產品成果及回饋。",
    "pages": [
      50,
      55
    ],
    "level": "理解",
    "id": "ASE-C2-Q07",
    "source": "ASE-002"
  },
  {
    "type": "choice",
    "prompt": "看板審查欄已達 WIP 上限。較合理的下一步是？",
    "options": [
      "繼續塞工作以增加忙碌度",
      "刪掉限制",
      "讓所有人同時開新任務",
      "協助完成審查、處理瓶頸後再拉工作"
    ],
    "answer": 3,
    "explanation": "WIP 上限促進先完成而非不斷開始，並暴露瓶頸。",
    "pages": [
      51,
      52,
      54
    ],
    "level": "理解",
    "id": "ASE-C2-Q08",
    "source": "ASE-002"
  },
  {
    "type": "choice",
    "prompt": "Which TDD step improves internal structure while keeping tests passing?",
    "options": [
      "Red",
      "Refactor",
      "取消全部測試",
      "新增未驗證功能"
    ],
    "answer": 1,
    "explanation": "Refactor 維持既有行為與測試通過，改善結構；Green 是先以最少實作通過測試。",
    "pages": [
      68,
      70,
      74
    ],
    "level": "理解",
    "id": "ASE-C2-Q09",
    "source": "ASE-002"
  },
  {
    "type": "choice",
    "prompt": "通過測試後仍由人決定是否發布正式環境，最符合？",
    "options": [
      "Continuous Deployment",
      "只做手動編譯",
      "Continuous Delivery",
      "完全沒有 CI"
    ],
    "answer": 2,
    "explanation": "Delivery 保持可發布並保留發布決策；Deployment 進一步自動發布。",
    "pages": [
      79,
      82
    ],
    "level": "理解",
    "id": "ASE-C2-Q10",
    "source": "ASE-002"
  },
  {
    "type": "fill",
    "prompt": "In a Kanban pull system, the three-letter abbreviation in _____ Limit is?",
    "answers": [
      "WIP"
    ],
    "explanation": "WIP 是 Work in Progress，限制同時進行工作以降低切換與瓶頸。",
    "pages": [
      51,
      54
    ],
    "level": "識記",
    "id": "ASE-C2-Q11",
    "source": "ASE-002"
  },
  {
    "type": "fill",
    "prompt": "請依序填完整循環：Red → Green → _____.",
    "answers": [
      "Refactor",
      "Refactoring"
    ],
    "explanation": "重構改善內部結構，同時維持測試通過。",
    "pages": [
      68,
      69
    ],
    "level": "識記",
    "id": "ASE-C2-Q12",
    "source": "ASE-002"
  },
  {
    "type": "fill",
    "prompt": "「改善內部結構、不改外部可觀察行為」稱 _____（英文）。",
    "answers": [
      "Refactoring"
    ],
    "explanation": "重構不是新增業務功能或修改驗收結果。",
    "pages": [
      70
    ],
    "level": "識記",
    "id": "ASE-C2-Q13",
    "source": "ASE-002"
  },
  {
    "type": "fill",
    "prompt": "固定開發週期的時間盒，在 Scrum 中稱 _____.",
    "answers": [
      "Sprint"
    ],
    "explanation": "Sprint 提供固定節奏；Kanban 則偏連續流。",
    "pages": [
      47,
      50
    ],
    "level": "識記",
    "id": "ASE-C2-Q14",
    "source": "ASE-002"
  },
  {
    "type": "fill",
    "prompt": "CI stands for Continuous _____.",
    "answers": [
      "Integration"
    ],
    "explanation": "持續整合強調頻繁合併、自動建置與測試。",
    "pages": [
      78
    ],
    "level": "識記",
    "id": "ASE-C2-Q15",
    "source": "ASE-002"
  },
  {
    "type": "fill",
    "prompt": "模型外的規格、沙盒與驗證保護機制，講義稱 Engineering _____.",
    "answers": [
      "Harness"
    ],
    "explanation": "Harness 將工程紀律落實為環境與檢查，而不是只加長提示詞。",
    "pages": [
      86,
      88,
      91
    ],
    "level": "識記",
    "id": "ASE-C2-Q16",
    "source": "ASE-002"
  },
  {
    "type": "written",
    "prompt": "畫出 V-Model 四層對應，並解釋測試左移。",
    "model": "使用者需求↔驗收；系統規格↔系統；架構設計↔整合；詳細設計↔單元。底部實作。左移是在各需求／設計形成時就規劃對應測試，不是等實作全部結束才想如何測。",
    "rubric": [
      "四組對應正確",
      "底部實作與兩側細化／整合方向合理",
      "說明提早規劃測試與追溯"
    ],
    "pages": [
      17,
      19
    ],
    "level": "應用",
    "answerImage": "v-model.svg",
    "id": "ASE-C2-Q17",
    "source": "ASE-002"
  },
  {
    "type": "written",
    "prompt": "同一功能持續改進與每版新增不同功能可否並用？以本複習網站為例。",
    "model": "可以。先提供一章課程與測驗，後續加入其他章節是增量；反覆改善第一章解說、題目難度與錯題回饋是疊代。每版須有可實際使用的價值，不只是孤立 UI 或資料庫。",
    "rubric": [
      "分清增加範圍與精煉",
      "同一專案各舉一例",
      "提到可用價值切片"
    ],
    "pages": [
      25,
      26,
      28,
      30
    ],
    "level": "應用",
    "id": "ASE-C2-Q18",
    "source": "ASE-002"
  },
  {
    "type": "written",
    "prompt": "新創需求尚不明確、三週內要取得使用者回饋。選擇流程並說明代價。",
    "model": "可採敏捷的增量與疊代，先交付能驗證核心服務的 MVP，依回饋調整需求。要管理架構演化、自動測試與技術債，避免只顧速度；嚴格一次凍結所有細節會延後學習。",
    "rubric": [
      "明示不確定性與早期回饋",
      "說明流程機制",
      "列出品質／技術債代價"
    ],
    "pages": [
      22,
      23,
      30,
      58,
      59
    ],
    "level": "應用",
    "id": "ASE-C2-Q19",
    "source": "ASE-002"
  },
  {
    "type": "written",
    "prompt": "Scrum 會議都正常，但每次改需求都引發大量回歸錯誤。診斷並提出兩項工程改善。",
    "model": "可能只有 Scrum 管理外殼而缺乏工程紀律，即 Flaccid Scrum。可建立自動回歸測試與 CI，並在測試保護下持續重構高耦合模組；單加會議不能解決技術債。",
    "rubric": [
      "辨識技術債／Flaccid Scrum",
      "兩項具體技術改善",
      "說明改善如何降低後續成本"
    ],
    "pages": [
      58,
      59,
      62,
      68,
      70,
      78
    ],
    "level": "應用",
    "id": "ASE-C2-Q20",
    "source": "ASE-002"
  }
]
```
