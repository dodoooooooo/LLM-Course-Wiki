---
id: ASE-REVIEW-04
title: "第4章期中複習測驗"
course: advanced-software-engineering
type: review
status: needs-review
created: '2026-11-06'
updated: '2026-11-06'
sources: [ASE-004, EXAM-001]
tags: [期中測驗, AI練習題]
---
# 第4章｜期中複習測驗

本題庫為依講義重新編寫的 AI 練習題，不代表教師正式考卷。英文敘述、術語填空與圖表判讀參考 EXAM-001 的可見題型。每題 pages 指本章講義 PDF 頁次。

單選與填空可自動批改；手寫、簡答與繪圖使用參考答案及 rubric 自評，不計入自動題分數。圖檔僅供參考解答，先在紙上作答再展開。

[回本章課程](../lessons/chapter-04.md) · [測驗索引](index.md)

## 題庫資料

以下 JSON 為唯一題庫來源；網站建置時解析此區塊。手動維護後執行 python3 scripts/build.py。

```json
[
  {
    "type": "choice",
    "prompt": "Which perspective describes class relationships and static data organization?",
    "options": [
      "External",
      "Interaction",
      "Structural",
      "只限執行緒排程"
    ],
    "answer": 2,
    "explanation": "類別與資料的靜態關係屬 Structural；Sequence 則關注互動順序。",
    "pages": [
      6,
      7,
      8
    ],
    "level": "理解",
    "id": "ASE-C4-Q01",
    "source": "ASE-004"
  },
  {
    "type": "choice",
    "prompt": "每次下單都要驗證付款；使用優惠券為選用。正確關係？",
    "options": [
      "下單 include 付款；優惠券 extend 下單",
      "付款 extend 下單；下單 include 優惠券",
      "兩者都用繼承",
      "兩者都用資料流箭頭"
    ],
    "answer": 0,
    "explanation": "include 由基礎指被包含；extend 由擴充指基礎。",
    "pages": [
      20,
      28,
      30,
      31
    ],
    "level": "理解",
    "id": "ASE-C4-Q02",
    "source": "ASE-004"
  },
  {
    "type": "choice",
    "prompt": "Actor 在哪個位置？",
    "options": [
      "必須放資料庫內",
      "一定只能是人",
      "放任何位置都一樣",
      "本系統邊界之外"
    ],
    "answer": 3,
    "explanation": "Actor 是與系統互動的外部角色或外部系統，先定義系統邊界才可判斷。",
    "pages": [
      19,
      22,
      26,
      30
    ],
    "level": "理解",
    "id": "ASE-C4-Q03",
    "source": "ASE-004"
  },
  {
    "type": "choice",
    "prompt": "類別圖中實心菱形畫在 Order 端、連到 OrderItem，代表？",
    "options": [
      "OrderItem 是 Order 的父類別",
      "Order 是整體，組合管理其明細",
      "明細實現訂單介面",
      "兩者只有同步呼叫"
    ],
    "answer": 1,
    "explanation": "實心菱形表示 Composition 且位在整體端；三角才代表泛化或實現的指向端。",
    "pages": [
      41,
      43,
      47,
      51
    ],
    "level": "理解",
    "id": "ASE-C4-Q04",
    "source": "ASE-004"
  },
  {
    "type": "choice",
    "prompt": "Customer \"1\" -- \"0..*\" Order，哪個解讀正確？",
    "options": [
      "每筆訂單可無顧客",
      "每位顧客必須至少一筆訂單",
      "一位顧客可零到多筆訂單；每筆訂單恰一位顧客",
      "顧客一定只有一筆訂單"
    ],
    "answer": 2,
    "explanation": "看對端重數；Order 端 0..* 表示一位顧客可對應的訂單數。",
    "pages": [
      44,
      46,
      52
    ],
    "level": "理解",
    "id": "ASE-C4-Q05",
    "source": "ASE-004"
  },
  {
    "type": "choice",
    "prompt": "Which arrow points to a superclass in a class diagram?",
    "options": [
      "實線空心三角",
      "實線實心菱形",
      "虛線普通開放箭頭",
      "兩端黑點"
    ],
    "answer": 0,
    "explanation": "Generalization 使用實線空心三角，箭頭朝父類別。Realization 則是虛線空心三角朝介面。",
    "pages": [
      42,
      117
    ],
    "level": "理解",
    "id": "ASE-C4-Q06",
    "source": "ASE-004"
  },
  {
    "type": "choice",
    "prompt": "A sequence fragment has [APPROVED] and [else: DECLINED]. Which operator?",
    "options": [
      "loop",
      "opt",
      "par",
      "alt"
    ],
    "answer": 3,
    "explanation": "alt 表示條件替代分支；opt 只有單一選用分支；par 表示並行。",
    "pages": [
      62,
      63,
      64
    ],
    "level": "理解",
    "id": "ASE-C4-Q07",
    "source": "ASE-004"
  },
  {
    "type": "choice",
    "prompt": "活動圖中只有二選一的兩條付款路徑，重新匯合通常用？",
    "options": [
      "Join，等待兩者都到",
      "Merge，不等待兩條都到",
      "Fork，再啟動兩條",
      "類別繼承"
    ],
    "answer": 1,
    "explanation": "Merge 合併替代路徑；Join 常用來同步所有並行路徑，不能混用。",
    "pages": [
      77,
      78,
      83
    ],
    "level": "理解",
    "id": "ASE-C4-Q08",
    "source": "ASE-004"
  },
  {
    "type": "choice",
    "prompt": "狀態轉移 cancel [elapsed <= 120] / refund 中，中括號是？",
    "options": [
      "方法參數型別",
      "訊息回傳值",
      "Guard Condition",
      "類別可見度"
    ],
    "answer": 2,
    "explanation": "Guard 決定事件觸發時是否允許轉移；refund 是轉移效果。",
    "pages": [
      95,
      96
    ],
    "level": "理解",
    "id": "ASE-C4-Q09",
    "source": "ASE-004"
  },
  {
    "type": "choice",
    "prompt": "用 PlantUML 而非只保存二進位繪圖檔的主要工程優勢？",
    "options": [
      "可文字 diff、Git 審查與自動產圖",
      "保證所有 UML 語意都正確",
      "不再需要需求",
      "自動消除所有程式缺陷"
    ],
    "answer": 0,
    "explanation": "圖表即代碼改善維護與協作，但模型語意仍需審查。",
    "pages": [
      111,
      112,
      122
    ],
    "level": "理解",
    "id": "ASE-C4-Q10",
    "source": "ASE-004"
  },
  {
    "type": "fill",
    "prompt": "UML 的 private visibility 符號是 _____（只填一個符號）。",
    "answers": [
      "-"
    ],
    "explanation": "- 表私有；+ 公開；# 受保護；~ 套件。",
    "pages": [
      40,
      116
    ],
    "level": "識記",
    "id": "ASE-C4-Q11",
    "source": "ASE-004"
  },
  {
    "type": "fill",
    "prompt": "UML 的 protected visibility 符號是 _____（只填一個符號）。",
    "answers": [
      "#"
    ],
    "explanation": "# 是 protected，不是私有。",
    "pages": [
      40,
      116
    ],
    "level": "識記",
    "id": "ASE-C4-Q12",
    "source": "ASE-004"
  },
  {
    "type": "fill",
    "prompt": "Divide an activity diagram by responsible roles into _____ (or Partitions). 請填標準複數英文。",
    "answers": [
      "Swimlanes"
    ],
    "explanation": "泳道按角色、部門或系統責任分區，不表示一定有並行。",
    "pages": [
      79,
      80
    ],
    "level": "識記",
    "id": "ASE-C4-Q13",
    "source": "ASE-004"
  },
  {
    "type": "fill",
    "prompt": "基礎案例指向必要共用案例，關係名稱為 _____（填 include 或 extend）。",
    "answers": [
      "include",
      "<<include>>",
      "«include»"
    ],
    "explanation": "include 指向被納入的功能；extend 指向被擴充的基礎案例。",
    "pages": [
      20,
      28,
      31
    ],
    "level": "識記",
    "id": "ASE-C4-Q14",
    "source": "ASE-004"
  },
  {
    "type": "fill",
    "prompt": "Event [_____] / Action：填入守衛條件的英文單字。",
    "answers": [
      "Guard"
    ],
    "explanation": "事件與條件不能混淆；收到事件仍要檢查 guard。",
    "pages": [
      95,
      96
    ],
    "level": "識記",
    "id": "ASE-C4-Q15",
    "source": "ASE-004"
  },
  {
    "type": "fill",
    "prompt": "BCE 中負責協調業務流程的是 _____（填英文）。",
    "answers": [
      "Control"
    ],
    "explanation": "Boundary 處理外部互動；Control 協調；Entity 保存領域狀態。",
    "pages": [
      65,
      68,
      69
    ],
    "level": "識記",
    "id": "ASE-C4-Q16",
    "source": "ASE-004"
  },
  {
    "type": "written",
    "prompt": "紙筆畫使用案例圖：學生可加選；每次加選都檢查資格；額滿時可選擇加入候補。畫邊界、角色及兩種關係。",
    "model": "學生在選課系統外，連到加選課程；加選用 include 虛線箭頭指向檢查資格；加入候補以 extend 指向加選，標示額滿且願候補。必要與可選行為方向不能相反。",
    "rubric": [
      "Actor 在邊界外且案例在內",
      "include 由加選指向資格檢查",
      "extend 由候補指向加選並有條件"
    ],
    "pages": [
      19,
      20,
      26,
      27,
      30
    ],
    "level": "應用",
    "answerImage": "use-case.svg",
    "id": "ASE-C4-Q17",
    "source": "ASE-004"
  },
  {
    "type": "written",
    "prompt": "畫類別圖：一位顧客可有零到多張訂單；每張訂單恰一位顧客，且含至少一項不能獨立於該訂單存在的明細。補兩端重數與組合。",
    "model": "Customer 1 -- 0..* Order；Order 1 *-- 1..* OrderItem，實心菱形在 Order 端。各類別可列必要屬性與操作，例如私有 id、公開 calculateTotal。這是題設簡化模型。",
    "rubric": [
      "Customer／Order 兩端重數正確",
      "Order／OrderItem 兩端重數正確",
      "實心菱形位整體端",
      "列出合理屬性或操作及可見度"
    ],
    "pages": [
      39,
      40,
      43,
      44,
      51
    ],
    "level": "應用",
    "answerImage": "class-model.svg",
    "id": "ASE-C4-Q18",
    "source": "ASE-004"
  },
  {
    "type": "written",
    "prompt": "畫付款循序圖：UI 請求控制器，控制器請求金流；成功時儲存訂單後回成功，失敗時回錯誤。需用 alt。",
    "model": "UI 呼叫 Control；Control 呼叫 Gateway 並取得授權結果。alt 成功：Control 呼叫 Order 保存，再回覆 UI；else 失敗：回覆錯誤，不建立成功訂單。時間向下、回傳虛線、生命線與活化區間合理。",
    "rubric": [
      "UI 不越過控制器直接存資料",
      "alt 成功／失敗條件明確",
      "存成功後才回成功",
      "訊息方向與回傳合理"
    ],
    "pages": [
      60,
      61,
      62,
      67,
      68,
      69,
      70
    ],
    "level": "應用",
    "answerImage": "sequence.svg",
    "id": "ASE-C4-Q19",
    "source": "ASE-004"
  },
  {
    "type": "written",
    "prompt": "畫活動圖：檢查付款，失敗結束；成功後並行備餐與找外送員，兩者完成後交餐。用正確控制節點。",
    "model": "付款判斷用 Decision；失敗到終點；成功到 Fork 展開備餐與找外送員；Join 等兩者完成，再交餐及結束。不可把失敗分支也接入要求所有分支完成的 Join。",
    "rubric": [
      "付款選擇用菱形與 guard",
      "兩工作用 Fork 並行",
      "Join 同步後交餐",
      "失敗出口正確、不造成永久等待"
    ],
    "pages": [
      76,
      77,
      78,
      83,
      85
    ],
    "level": "應用",
    "answerImage": "activity.svg",
    "id": "ASE-C4-Q20",
    "source": "ASE-004"
  },
  {
    "type": "written",
    "prompt": "畫單一訂單狀態機：Paid 可開始備餐變 Preparing；Paid 只在120秒內可取消並退款；Preparing 完成後變 Ready，交付後 Delivered。",
    "model": "初始進 Paid；Paid → Preparing 標 startCooking；Paid → Cancelled 標 cancel [elapsed <= 120s] / refund；Preparing → Ready 標 mealReady；Ready → Delivered 標 deliver；Delivered 與 Cancelled 可進終點。沒有 Preparing 的一般取消路徑。",
    "rubric": [
      "狀態與事件分清",
      "取消有時間 guard 及退款效果",
      "必要路徑完整且終點無外出箭頭",
      "維持備餐後不可一般取消的不變量"
    ],
    "pages": [
      93,
      95,
      96,
      104,
      105,
      107
    ],
    "level": "應用",
    "answerImage": "state.svg",
    "id": "ASE-C4-Q21",
    "source": "ASE-004"
  }
]
```
