---
id: ASE-REVIEW-03
title: "第3章期中複習測驗"
course: advanced-software-engineering
type: review
status: needs-review
created: '2026-11-06'
updated: '2026-11-06'
sources: [ASE-003, EXAM-001]
tags: [期中測驗, AI練習題]
---
# 第3章｜期中複習測驗

本題庫為依講義重新編寫的 AI 練習題，不代表教師正式考卷。英文敘述、術語填空與圖表判讀參考 EXAM-001 的可見題型。每題 pages 指本章講義 PDF 頁次。

單選與填空可自動批改；手寫、簡答與繪圖使用參考答案及 rubric 自評，不計入自動題分數。圖檔僅供參考解答，先在紙上作答再展開。

[回本章課程](../lessons/chapter-03.md) · [測驗索引](index.md)

## 題庫資料

以下 JSON 為唯一題庫來源；網站建置時解析此區塊。手動維護後執行 python3 scripts/build.py。

```json
[
  {
    "type": "choice",
    "prompt": "「系統應每月提供藥品費用報表」與「最後工作日依指定格式、資料量與期限產製」主要差別？",
    "options": [
      "前者一定 FR，後者一定領域",
      "後者不用驗收",
      "前者較高階，後者是詳細系統規格",
      "只有後者才算需求"
    ],
    "answer": 2,
    "explanation": "使用者需求與系統需求按抽象與精確程度區分，不是簡單按功能／非功能區分。",
    "pages": [
      8,
      9,
      11
    ],
    "level": "理解",
    "id": "ASE-C3-Q01",
    "source": "ASE-003"
  },
  {
    "type": "choice",
    "prompt": "「使用者可送出取消申請」最直接指定？",
    "options": [
      "Functional Requirement",
      "只有儲存容量",
      "只有開發語言政策",
      "沒有任何需求"
    ],
    "answer": 0,
    "explanation": "描述系統應提供的服務或行為是 FR。取消是否合法、退款條件仍需另定。",
    "pages": [
      15,
      16
    ],
    "level": "理解",
    "id": "ASE-C3-Q02",
    "source": "ASE-003"
  },
  {
    "type": "choice",
    "prompt": "題目明說公司內規要求所有變更先經 PR 審查，依 NFR 來源分類是？",
    "options": [
      "Product",
      "External",
      "只有領域物理定律",
      "Organizational"
    ],
    "answer": 3,
    "explanation": "要求來自組織內部工程政策，因此是 Organizational。",
    "pages": [
      22,
      23,
      24
    ],
    "level": "理解",
    "id": "ASE-C3-Q03",
    "source": "ASE-003"
  },
  {
    "type": "choice",
    "prompt": "題目要求醫療系統符合 HIPAA 等外部法規，依 NFR 來源分類是？",
    "options": [
      "Product",
      "External",
      "Organizational",
      "只要有英文就不是需求"
    ],
    "answer": 1,
    "explanation": "題幹指向外部法規，因此選 External。本題不判斷實際法律適用。",
    "pages": [
      24
    ],
    "level": "理解",
    "id": "ASE-C3-Q04",
    "source": "ASE-003"
  },
  {
    "type": "choice",
    "prompt": "為何要到真實工作場所使用 Ethnography？",
    "options": [
      "可自動寫完整程式",
      "能保證需求不再變",
      "觀察習以為常而未說出的工作細節",
      "比所有其他方法永遠便宜"
    ],
    "answer": 2,
    "explanation": "民族誌補足訪談未能表達的內隱知識與非正式流程。",
    "pages": [
      38,
      42,
      45
    ],
    "level": "理解",
    "id": "ASE-C3-Q05",
    "source": "ASE-003"
  },
  {
    "type": "choice",
    "prompt": "客戶指定區塊鏈，但無法說明原因。訪談較應先做？",
    "options": [
      "直接開始寫合約",
      "以 5 Whys 問出真正的防竄改或稽核需求",
      "拒絕再談任何需求",
      "把該要求當作已驗證真理"
    ],
    "answer": 1,
    "explanation": "先問問題與業務原因，避免過早錨定特定技術。",
    "pages": [
      37,
      44
    ],
    "level": "理解",
    "id": "ASE-C3-Q06",
    "source": "ASE-003"
  },
  {
    "type": "choice",
    "prompt": "一條需求允許備餐後取消，另一條禁止同一條件取消。哪項檢查最直接？",
    "options": [
      "Consistency",
      "只有 Realism",
      "只有 Completeness",
      "只有字體一致"
    ],
    "answer": 0,
    "explanation": "同一條件的互相矛盾屬一致性問題；完整性則關心遺漏。",
    "pages": [
      16,
      54,
      56
    ],
    "level": "理解",
    "id": "ASE-C3-Q07",
    "source": "ASE-003"
  },
  {
    "type": "choice",
    "prompt": "「介面應極度直覺」主要欠缺哪一項？",
    "options": [
      "只有系統邊界",
      "只有 Stakeholder 名字",
      "只有資料表數量",
      "Verifiability"
    ],
    "answer": 3,
    "explanation": "沒有可觀察的成功條件或門檻，無法客觀驗收。",
    "pages": [
      25,
      27,
      54
    ],
    "level": "理解",
    "id": "ASE-C3-Q08",
    "source": "ASE-003"
  },
  {
    "type": "choice",
    "prompt": "哪一個 NFR 改寫最可驗證？",
    "options": [
      "任何網路下一律零延遲",
      "在指定資料量與負載下，95% 查詢兩秒內完成",
      "採用最多微服務",
      "讓使用者感到超級順"
    ],
    "answer": 1,
    "explanation": "同時有測試情境、指標與門檻；數值只是本題自編示例。",
    "pages": [
      25,
      27,
      28
    ],
    "level": "理解",
    "id": "ASE-C3-Q09",
    "source": "ASE-003"
  },
  {
    "type": "choice",
    "prompt": "變更一項需求前，先查哪些程式、設計與測試會受影響，最需要？",
    "options": [
      "只查程式行數",
      "只查設計師喜好",
      "Traceability 與 Impact Analysis",
      "刪除所有舊需求 ID"
    ],
    "answer": 2,
    "explanation": "唯一 ID 與追溯鏈支援評估變更影響；不能只改文字而不更新相依工件。",
    "pages": [
      57,
      58,
      59
    ],
    "level": "理解",
    "id": "ASE-C3-Q10",
    "source": "ASE-003"
  },
  {
    "type": "fill",
    "prompt": "Detailed technical specifications for engineers are _____ Requirements. Fill in one English word.",
    "answers": [
      "System"
    ],
    "explanation": "與使用者高階需求相較，系統需求提供精確的實作與驗收基準。",
    "pages": [
      8,
      9
    ],
    "level": "識記",
    "id": "ASE-C3-Q11",
    "source": "ASE-003"
  },
  {
    "type": "fill",
    "prompt": "Requirements checks: Validity, _____, Completeness, Realism, Verifiability. 填入「無互相矛盾」的英文。",
    "answers": [
      "Consistency"
    ],
    "explanation": "Consistency 關心條文相容；Completeness 關心是否遺漏。",
    "pages": [
      54
    ],
    "level": "識記",
    "id": "ASE-C3-Q12",
    "source": "ASE-003"
  },
  {
    "type": "fill",
    "prompt": "現場觀察挖掘習以為常的內隱知識，英文方法是 _____.",
    "answers": [
      "Ethnography"
    ],
    "explanation": "不是只靠訪談問題清單，而是觀察實際工作脈絡。",
    "pages": [
      38
    ],
    "level": "識記",
    "id": "ASE-C3-Q13",
    "source": "ASE-003"
  },
  {
    "type": "fill",
    "prompt": "User story 的驗收準則格式：Given–When–_____.",
    "answers": [
      "Then"
    ],
    "explanation": "Then 應描述可觀察結果，與前置情境及事件連接。",
    "pages": [
      39
    ],
    "level": "識記",
    "id": "ASE-C3-Q14",
    "source": "ASE-003"
  },
  {
    "type": "fill",
    "prompt": "Requirements Traceability Matrix 的縮寫為 _____.",
    "answers": [
      "RTM"
    ],
    "explanation": "追溯矩陣將需求連到實作與測試，支援覆蓋與影響分析。",
    "pages": [
      57,
      70
    ],
    "level": "識記",
    "id": "ASE-C3-Q15",
    "source": "ASE-003"
  },
  {
    "type": "fill",
    "prompt": "AI 提議後仍由人審核需求，稱 Human-in-the-_____.",
    "answers": [
      "Loop"
    ],
    "explanation": "人類應驗證規則、領域假設與例外，不能將模擬當成真實訪談。",
    "pages": [
      66,
      68
    ],
    "level": "識記",
    "id": "ASE-C3-Q16",
    "source": "ASE-003"
  },
  {
    "type": "written",
    "prompt": "為校園選課系統各寫一項 FR 與可驗證 NFR，並解釋為何不同。",
    "model": "FR：系統應允許學生依課號查詢剩餘名額。NFR：在指定資料集與 100 人並行負載、固定測試網路下，95% 查詢於兩秒內返回完整結果。前者定義服務，後者限制服務品質；數值是自訂示例。",
    "rubric": [
      "FR 是具體服務",
      "NFR 有條件、指標與門檻",
      "說明功能與品質的區別"
    ],
    "pages": [
      15,
      20,
      25,
      27
    ],
    "level": "應用",
    "id": "ASE-C3-Q17",
    "source": "ASE-003"
  },
  {
    "type": "written",
    "prompt": "審查「系統必須即時完成所有配送；外送員必須接單也可拒絕；任何天候都保證十分鐘到達」。至少指出三種問題。",
    "model": "即時沒有量測標準→可驗證性；同一條件必須接與可拒絕→一致性；任何天候十分鐘→現實性；也可指出未定義無人接單等例外→完整性。應具體釐清條件與例外。",
    "rubric": [
      "至少三種問題",
      "每種問題對到正確英文檢查項目",
      "指出需補充的條件或改寫方向"
    ],
    "pages": [
      54,
      56
    ],
    "level": "應用",
    "id": "ASE-C3-Q18",
    "source": "ASE-003"
  },
  {
    "type": "written",
    "prompt": "訪談發現使用者描述的流程與現場不同，如何補強需求擷取？",
    "model": "安排現場觀察或情境脈絡探詢，記錄實際行為與非正式捷徑，再以訪談詢問原因，必要時用原型共同確認。觀察可揭露內隱知識，但仍要和多方驗證，不能假設一人習慣代表全部規則。",
    "rubric": [
      "選擇觀察並說明價值",
      "說明與訪談或原型互補",
      "不把單一觀察當全面結論"
    ],
    "pages": [
      36,
      38,
      39,
      42
    ],
    "level": "應用",
    "id": "ASE-C3-Q19",
    "source": "ASE-003"
  },
  {
    "type": "written",
    "prompt": "需求變更「取消需退款」改為「僅特定時間可退款」，如何使用 RTM？",
    "model": "沿需求 ID 找出取消政策、狀態機、退款服務與測試。檢查時間邊界與例外、評估成本並核准，再同步改需求、圖、實作與正常／邊界／拒絕退款測試，保留追溯紀錄。",
    "rubric": [
      "以需求 ID 查設計／程式／測試",
      "先影響分析與核准",
      "同步更新並保留變更紀錄"
    ],
    "pages": [
      57,
      58
    ],
    "level": "應用",
    "id": "ASE-C3-Q20",
    "source": "ASE-003"
  }
]
```
