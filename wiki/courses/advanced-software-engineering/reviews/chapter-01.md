---
id: ASE-REVIEW-01
title: "第1章期中複習測驗"
course: advanced-software-engineering
type: review
status: needs-review
created: '2026-11-06'
updated: '2026-11-06'
sources: [ASE-001, EXAM-001]
tags: [期中測驗, AI練習題]
---
# 第1章｜期中複習測驗

本題庫為依講義重新編寫的 AI 練習題，不代表教師正式考卷。英文敘述、術語填空與圖表判讀參考 EXAM-001 的可見題型。每題 pages 指本章講義 PDF 頁次。

單選與填空可自動批改；手寫、簡答與繪圖使用參考答案及 rubric 自評，不計入自動題分數。圖檔僅供參考解答，先在紙上作答再展開。

[回本章課程](../lessons/chapter-01.md) · [測驗索引](index.md)

## 題庫資料

以下 JSON 為唯一題庫來源；網站建置時解析此區塊。手動維護後執行 python3 scripts/build.py。

```json
[
  {
    "type": "choice",
    "prompt": "Which item is outside the software definition used in this course?",
    "options": [
      "部署與復原程序",
      "資料庫綱要",
      "CPU 實體晶片",
      "需求與操作文件"
    ],
    "answer": 2,
    "explanation": "軟體包含程式、資料、程序與文件；CPU 是實體硬體。",
    "pages": [
      14,
      18
    ],
    "level": "理解",
    "id": "ASE-C1-Q01",
    "source": "ASE-001"
  },
  {
    "type": "choice",
    "prompt": "系統程式通過單元測試，更新時卻因錯誤的部署步驟覆蓋資料。最直接缺失是哪一部分？",
    "options": [
      "Operational Procedures",
      "Programs 的語法",
      "CPU 設計",
      "螢幕效能"
    ],
    "answer": 0,
    "explanation": "描述焦點是部署程序；測試程式不會自動驗證所有維運步驟。",
    "pages": [
      14,
      15,
      16
    ],
    "level": "理解",
    "id": "ASE-C1-Q02",
    "source": "ASE-001"
  },
  {
    "type": "choice",
    "prompt": "軟體危機為何無法只靠更快的硬體解決？",
    "options": [
      "硬體更快一定會增加程式錯誤",
      "危機涉及需求、規模與團隊協作",
      "軟體不能使用新硬體",
      "只要改用高階語言即可解決"
    ],
    "answer": 1,
    "explanation": "系統複雜度及協作方式是核心問題，與單一機器速度不同。",
    "pages": [
      8,
      11
    ],
    "level": "理解",
    "id": "ASE-C1-Q03",
    "source": "ASE-001"
  },
  {
    "type": "choice",
    "prompt": "A third-party service fails and the whole application stops. Which quality attribute is most directly implicated?",
    "options": [
      "Portability / Installability",
      "Usability / Learnability",
      "Maintainability / Testability",
      "Reliability / Fault Tolerance"
    ],
    "answer": 3,
    "explanation": "故障時能否繼續提供服務是可靠性與容錯性；不是更換平台是否容易。",
    "pages": [
      43,
      44,
      45
    ],
    "level": "理解",
    "id": "ASE-C1-Q04",
    "source": "ASE-001"
  },
  {
    "type": "choice",
    "prompt": "模組彼此高度耦合，難以替資料庫建立測試替身。焦點是哪項品質？",
    "options": [
      "Compatibility",
      "Maintainability",
      "Portability",
      "Functional Suitability"
    ],
    "answer": 1,
    "explanation": "模組化與可測試性屬可維護性。相容性偏向共存及資訊交換。",
    "pages": [
      42,
      43,
      44
    ],
    "level": "理解",
    "id": "ASE-C1-Q05",
    "source": "ASE-001"
  },
  {
    "type": "choice",
    "prompt": "開發團隊將產品移至另一作業系統，安裝及替換十分困難。最直接對應？",
    "options": [
      "Security",
      "Reliability",
      "Portability",
      "Performance Efficiency"
    ],
    "answer": 2,
    "explanation": "安裝、適應與替換環境的容易程度屬可移植性。",
    "pages": [
      43,
      44
    ],
    "level": "理解",
    "id": "ASE-C1-Q06",
    "source": "ASE-001"
  },
  {
    "type": "choice",
    "prompt": "規格說每月產生報表，系統做到；但使用者真正需要每日風險警示。缺少哪個檢視？",
    "options": [
      "Validation",
      "只有編譯檢查",
      "只有效能調優",
      "只有程式格式檢查"
    ],
    "answer": 0,
    "explanation": "符合錯誤的規格不等於解決真正需求；Validation 要確認是否做對產品。",
    "pages": [
      26,
      28,
      69
    ],
    "level": "理解",
    "id": "ASE-C1-Q07",
    "source": "ASE-001"
  },
  {
    "type": "choice",
    "prompt": "雇主要求偽造合規測試結果，工程師應優先依據何者判斷？",
    "options": [
      "團隊當月提交次數",
      "主管的絕對命令",
      "個人的升遷利益",
      "Public 公眾利益與安全"
    ],
    "answer": 3,
    "explanation": "ACM/IEEE 倫理以公眾利益為最高考量，不能以服從雇主合理化造假。",
    "pages": [
      48,
      50,
      54
    ],
    "level": "理解",
    "id": "ASE-C1-Q08",
    "source": "ASE-001"
  },
  {
    "type": "choice",
    "prompt": "同一 AI 在沒有明確規格下產生程式與測試，所有測試都通過。主要風險？",
    "options": [
      "全部測試必然沒有執行",
      "測試與實作可能共用錯誤假設",
      "自動測試一定比人工慢",
      "只要改名測試函式就能消除問題"
    ],
    "answer": 1,
    "explanation": "Echo-Chamber Testing 指測試可能只證明自己的假設，而非真正需求。",
    "pages": [
      64,
      65,
      67
    ],
    "level": "理解",
    "id": "ASE-C1-Q09",
    "source": "ASE-001"
  },
  {
    "type": "choice",
    "prompt": "在已延期專案加入新人，卻讓資深成員花更多時間培訓與協調，對應哪個概念？",
    "options": [
      "YAGNI",
      "Dark Patterns",
      "Brooks’s Law",
      "Portability"
    ],
    "answer": 2,
    "explanation": "布魯克斯法則提醒加人存在培訓與溝通代價，不能當立即增加產能。",
    "pages": [
      34,
      36
    ],
    "level": "理解",
    "id": "ASE-C1-Q10",
    "source": "ASE-001"
  },
  {
    "type": "fill",
    "prompt": "Complete the fourth component: Programs, Data, Procedures, and _____.",
    "answers": [
      "Documentation"
    ],
    "explanation": "文件記錄需求、設計、操作等，是軟體構成的一部分。",
    "pages": [
      14
    ],
    "level": "識記",
    "id": "ASE-C1-Q11",
    "source": "ASE-001"
  },
  {
    "type": "fill",
    "prompt": "Software engineering applies systematic, disciplined and _____ approaches. 請填可量化的英文形容詞。",
    "answers": [
      "Quantifiable"
    ],
    "explanation": "工程要求可度量的方法，不能只靠主觀感覺。",
    "pages": [
      20,
      24
    ],
    "level": "識記",
    "id": "ASE-C1-Q12",
    "source": "ASE-001"
  },
  {
    "type": "fill",
    "prompt": "Are we building the product right? 這個檢查稱為 _____.",
    "answers": [
      "Verification"
    ],
    "explanation": "Verification 檢查是否符合規格；Validation 檢查是否解決真正需求。",
    "pages": [
      28
    ],
    "level": "識記",
    "id": "ASE-C1-Q13",
    "source": "ASE-001"
  },
  {
    "type": "fill",
    "prompt": "在四大活動中，因新需求持續調整既有系統稱為 Software _____.",
    "answers": [
      "Evolution"
    ],
    "explanation": "軟體演化包含上線後的修改與適應。",
    "pages": [
      29
    ],
    "level": "識記",
    "id": "ASE-C1-Q14",
    "source": "ASE-001"
  },
  {
    "type": "fill",
    "prompt": "只能靠提示詞生成且不理解實作，講義稱 Vibe _____（依題幹 Programming 用語填單字）。",
    "answers": [
      "Programming"
    ],
    "explanation": "講義使用 Vibe Programming 與 Vibe Coding；本題指定 Programming 用語。",
    "pages": [
      57
    ],
    "level": "識記",
    "id": "ASE-C1-Q15",
    "source": "ASE-001"
  },
  {
    "type": "fill",
    "prompt": "訂閱容易、取消困難的模式稱 Roach _____.",
    "answers": [
      "Motel"
    ],
    "explanation": "Roach Motel 藉退出流程障礙困住使用者。",
    "pages": [
      53
    ],
    "level": "識記",
    "id": "ASE-C1-Q16",
    "source": "ASE-001"
  },
  {
    "type": "written",
    "prompt": "用選課系統說明軟體四大組成，並解釋為何程式沒錯仍可能出事故。",
    "model": "程式檢查加選；資料保存名額與課表；程序負責部署及備份；文件定義業務與介面。若遷移或復原程序錯誤，仍可能破壞名額資料，即使單一函式測試正確。",
    "rubric": [
      "列出程式、資料、程序、文件",
      "四項各有具體例子",
      "指出程式測試無法代替其他部分驗證"
    ],
    "pages": [
      14,
      15,
      16,
      17
    ],
    "level": "應用",
    "id": "ASE-C1-Q17",
    "source": "ASE-001"
  },
  {
    "type": "written",
    "prompt": "用同一情境區分 Verification 與 Validation。",
    "model": "驗證選課系統依規格擋掉衝堂是 Verification；與學生確認此系統真的支援選課目標及實務流程是 Validation。兩者互補，符合規格不保證規格本身合適。",
    "rubric": [
      "兩個英文名詞正確",
      "分清規格符合與實際需求",
      "給出同一情境的不同檢視"
    ],
    "pages": [
      28
    ],
    "level": "應用",
    "id": "ASE-C1-Q18",
    "source": "ASE-001"
  },
  {
    "type": "written",
    "prompt": "兩週內做校園訂餐 MVP，說明一項合理工程權衡與不能省略的品質要求。",
    "model": "先交付菜單、下單與必要的付款處理，延後推薦功能以符合時程。仍保留付款正確性及必要驗證；權衡是減少範圍而非把未驗證系統當完成。",
    "rubric": [
      "明示時間／資源限制",
      "具體範圍取捨與價值",
      "保留重要品質要求並說明理由"
    ],
    "pages": [
      20,
      21,
      22,
      46
    ],
    "level": "應用",
    "id": "ASE-C1-Q19",
    "source": "ASE-001"
  },
  {
    "type": "written",
    "prompt": "發現 AI 產生的結帳程式通過兩個正常流程測試，是否能直接上線？列三個應檢視的事項。",
    "model": "不足以決定。應回到業務規格確認折扣與金額規則；測試失敗、重複送出、並行等邊界；審查安全與資料處理。生成程式與測試可能共用盲點，仍需人工及獨立驗證。",
    "rubric": [
      "明確指出證據不足",
      "至少三項具體檢視",
      "提及共同假設或人類責任"
    ],
    "pages": [
      64,
      65,
      67,
      68
    ],
    "level": "應用",
    "id": "ASE-C1-Q20",
    "source": "ASE-001"
  }
]
```
