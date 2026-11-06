---
id: ASE-CH01
title: "第一章｜軟體工程導論"
course: advanced-software-engineering
type: lesson
status: needs-review
created: '2026-11-06'
updated: '2026-11-06'
sources: [ASE-001]
tags: [期中複習, 第1章]
---
# 第一章｜軟體工程導論

> 依講義重新整理；頁碼一律指 PDF 頁次。例子標為自編；整理稿尚待使用者複核。

## 先掌握本章的問題

程式可以執行，為什麼專案仍可能失敗？因為真正交付的系統還依賴資料、部署程序、文件、團隊協作與長期維護。讀完本章要能區分「軟體的組成」「工程的做法」「開發活動」與「品質特徵」，這四組分類不可混背。[ASE-001，PDF p.14–29]

## 1.1–1.2 軟體發展與軟體危機

大型主機將批次計算自動化；個人電腦帶來文書與試算表；網際網路串連資訊與交易；行動裝置與雲端提供隨時可用的服務；生成式 AI 則加入自然語言互動與內容生成。考試判讀時，要把技術演變連到使用方式改變，而非只背年代。[ASE-001，PDF p.3–6]

**軟體危機（Software Crisis）**是系統愈大，原本靠個人經驗寫程式的方法愈無法控制時程、預算與品質。症狀包含延期、超支、缺陷與難以維護；根因是複雜度與協作管理能力跟不上規模。1968 年 NATO 會議是講義強調的軟體工程發展節點。換更快的電腦，無法直接解決需求誤解或團隊溝通問題。[ASE-001，PDF p.8–11]

講義用飛行模式衝突、數值溢位、英制／公制不一致說明失效的不同來源。複習應抓「介面或假設沒有對齊」，事件數字並非本整理的核心背誦項目。[ASE-001，PDF p.10]

## 1.3 軟體四大組成：軟體冰山

| 組成 | 英文 | 自編例子：選課系統 |
| --- | --- | --- |
| 程式 | Programs | 檢查衝堂、提交加選的程式 |
| 資料與結構 | Data & Schemas | 名額、課程表、資料庫綱要 |
| 運作程序 | Operational Procedures | 部署、備份、故障回復步驟 |
| 文件 | Documentation | 需求規格、API 契約、操作說明 |

來源：[ASE-001，PDF p.14–17]。CPU、記憶體模組是硬體，不是以上的軟體組成。單元測試全通過，仍不能保證資料遷移、部署或備份程序正確。四大組成回答「軟體包含什麼」，四大活動則回答「工程過程做什麼」。

## 1.4 工程與軟體工程

**工程（Engineering）**是在現實約束與有限資源下，運用科學與經驗，設計可用方案。方法須系統化（Systematic）、紀律化（Disciplined）、可量測（Quantifiable / Measurable）。限制可來自期限、預算、平台與規範；資源則包含人力、工具與領域知識。[ASE-001，PDF p.20–24]

**權衡（Trade-off）**是說明選擇理由，而非單純選最先進的技術。**滿意化（Satisficing）**指在限制下找足以達成目標的方案。自編例：兩週內交付校內點餐系統，可先提供菜單與下單，再擴充推薦功能，但不能為了趕工捨棄必要的付款正確性。

## 1.5 四大核心活動與 V&V

| 活動 | 核心問題 | 典型產出 |
| --- | --- | --- |
| Specification 規格說明 | 系統要提供什麼？受哪些限制？ | SRS、使用者故事、驗收準則 |
| Design & Implementation 設計與實作 | 如何組織並實現系統？ | 架構、介面、資料模型、程式 |
| Validation 驗證與確認 | 是否符合規格與實際需求？ | 測試與審查結果 |
| Evolution 軟體演化 | 上線後如何修正與適應改變？ | 修補、遷移、版本更新 |

來源：[ASE-001，PDF p.26–29]。四個活動不代表只能線性各做一次；第二章的流程模型決定其順序與頻率。

| 術語 | 問句 | 判斷依據 |
| --- | --- | --- |
| Verification 驗證 | Are we building the product right? | 是否符合已定義規格 |
| Validation 確認 | Are we building the right product? | 是否解決真正需求 |

來源：[ASE-001，PDF p.28]。自編例：報表欄位符合規格是 Verification；主管確認這份報表確實支援決策則是 Validation。

維護可分：Corrective（修錯）、Adaptive（適應新環境）、Perfective（改善功能或品質）、Preventive（預防未來問題）。例如修登入崩潰、支援新版作業系統、改善查詢效能、重構高風險模組，依序對應四類。[ASE-001，PDF p.29]

## 1.5 延伸：工程原則與工具

**關注點分離（Separation of Concerns）**避免單一模組同時處理畫面、付款、資料查詢與郵件；**模組化（Modularity）**建立可理解的邊界；**DRY**避免重複知識；**KISS**維持簡單；**YAGNI**避免實作尚未需要的功能。[ASE-001，PDF p.32–38]

**布魯克斯法則（Brooks’s Law）**提醒：對已延期專案加人，可能因培訓、工作拆分與溝通而更慢。不能把人數與產能當成單純線性關係。講義中的溝通複雜度強調成長風險，不應推導成所有專案都必然指數成長。[ASE-001，PDF p.34–36；後句為整理提醒]

Git 支援版本與審查；CI/CD 將建置、測試與交付制度化；靜態分析找潛在問題；監控與可觀測性回饋營運狀態。工具的價值在於讓工程規則可持續執行。[ASE-001，PDF p.38]

## 1.6 ISO/IEC 25010 八大品質特徵

本課使用講義列出的**八大特徵模型**；講義參考文獻列 ISO/IEC 25010:2011。本頁按課內版本複習，不把它宣稱為所有後續版本都相同的分類。[ASE-001，PDF p.41–44、71]

| 特徵 | 英文 | 辨識線索 | 典型子特徵 |
| --- | --- | --- | --- |
| 功能適合性 | Functional Suitability | 做的功能對不對、齊不齊 | 完整性、正確性、適切性 |
| 效能效率 | Performance Efficiency | 快不快、耗多少資源 | 時間行為、資源利用、容量 |
| 相容性 | Compatibility | 能否共存或交換資訊 | Co-existence、Interoperability |
| 易用性 | Usability | 易學、易操作、防誤操作 | Learnability、Operability、Accessibility |
| 可靠性 | Reliability | 故障下是否維持或恢復服務 | Availability、Fault Tolerance、Recoverability |
| 資訊安全 | Security | 防未授權讀取或竄改 | Confidentiality、Integrity、Authenticity |
| 可維護性 | Maintainability | 易分析、修改與測試 | Modularity、Testability、Modifiability |
| 可攜／可移植性 | Portability | 更換環境、安裝或替換是否容易 | Adaptability、Installability、Replaceability |

來源：[ASE-001，PDF p.42–44]。

**考題辨識法**：先找題目描述的問題，不要被技術名詞吸走。外部服務故障造成系統停擺，焦點是 Reliability／Fault Tolerance；模組耦合導致測試困難是 Maintainability；換平台無法安裝是 Portability；查詢太慢是 Performance Efficiency。技術相同也可能改善不同品質，須看情境。[ASE-001，PDF p.44–45；辨識步驟為整理]

## 1.7 倫理與黑暗模式

倫理判斷先守住**公眾利益（Public）**，不能以雇主命令合理化危害或造假。其餘原則為 Client & Employer、Product、Judgment、Management、Profession、Colleagues、Self。[ASE-001，PDF p.48–54]

| 黑暗模式 | 英文 | 辨識線索 |
| --- | --- | --- |
| 訂閱容易退訂難 | Roach Motel | 用流程障礙困住使用者 |
| 確認羞辱 | Confirmshaming | 用拒絕文案羞辱使用者 |
| 偷塞購物車 | Sneak into Basket | 未主動選擇卻加入付費品項 |
| 偽造緊迫感 | Fabricated Urgency | 假倒數或假庫存壓力 |

來源：[ASE-001，PDF p.53]。手寫回答可用「行為 → 被損害的自主／安全利益 → 透明替代流程」三步說明。

## 1.8 AI 輔助開發的判斷

講義以 **Vibe Programming / Vibe Coding** 描述只靠自然語言生成、很少理解與檢查實作的開發方式。風險不是「用了 AI」，而是把能執行誤認為已符合規格、品質與安全要求。[ASE-001，PDF p.57–65]

- **Automation Bias 自動化偏誤**：因輸出流暢自信而不再檢查。
- **Echo-Chamber Testing 同溫層測試**：實作與測試沿用同一個錯誤假設，全部通過仍可能做錯需求。
- **Code Churn 程式碼流失／頻繁改寫**：短時間大量改寫可作為品質風險線索，不能單憑一項數值判定原因。

來源：[ASE-001，PDF p.58、64–67]。防護方式是先定義規格與驗收條件、獨立檢驗關鍵假設、執行測試與人工審查。AI 在需求、設計、編程、測試與維護都可協助，責任仍由工程團隊承擔。

**待查核提醒**：講義中的 AI 成效百分比、產業事故歸因與 Software 1.0／2.0／3.0 分期，未在本輪另查原始研究；不將它們改寫成已獨立驗證的普遍事實，也不作客觀題的唯一答案依據。[ASE-001，PDF p.58–61]

## 考前快速自問

能否不看表格寫出軟體四組成、工程四活動、八項品質？能否用同一個系統各舉出資料失誤、程序失誤與程式失誤？能否分清「可復原」與「可移植」？能否解釋為何全部測試通過仍要檢查需求？


## 來源與延伸

[ASE-001 原始講義](../../../../raw/advanced-software-engineering/lectures/slide01t_intro.pdf)。

[本章測驗](../reviews/chapter-01.md) · [課程首頁](../index.md)
