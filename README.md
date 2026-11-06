# LLM Course Wiki｜課程複習

## 線上使用

- [直接開啟課程 Wiki](https://dodoooooooo.github.io/LLM-Course-Wiki/)
- [GitHub 公開儲存庫](https://github.com/dodoooooooo/LLM-Course-Wiki)

網站由 main 分支的 GitHub Actions 建置並發布 dist/ 產物；[GitHub Actions 部署狀態](https://github.com/dodoooooooo/LLM-Course-Wiki/actions)可確認是否已完成。首次部署或重新發布尚未完成時，網站可能暫時顯示 404。後續修改 Markdown 後，先 build／check，再提交並推送，GitHub Pages 會更新網站。瀏覽器學習紀錄不會從本機檔案自動搬到線上站點；可先匯出 JSON，再於線上版匯入。

## 公開版本

本儲存庫依專案擁有人 2026-11-07 的明確授權公開，包含 `raw/` 原始講義與 Notebook。教師教材與第三方內容仍依原作者權利及原授權條件使用；本專案不替其另行授權。

## 在你的 Mac 使用

1. 在 Finder 開啟 `~/Desktop/TAICA_AI_work/LLM_Course_Wiki`。
2. 雙擊根目錄的 `index.html`，以 Chrome 或 Safari 開啟。
3. 課程、搜尋與測驗可離線使用，無須安裝套件或輸入 API key。

目前直接維護這份 Mac 桌面專案。搬移時請保留整個資料夾；`index.html` 是生成結果，正文仍以 `wiki/` Markdown 為準。

## 網頁分類

首頁與側欄自動掃描 `wiki/courses/*/index.md`，課程數隨資料增減。分類依各課程設定產生；以下為 2026-11-06 已整理內容的快照，不是數量限制。

所有課程 → ADVANCED SOFTWARE ENGINEERING → 課程／測驗 → 四章：

1. 軟體工程導論
2. 軟體流程與開發方法學
3. 需求工程
4. 系統塑模與 UML

硬體安全 → 課程／作業：課程包含七個主題，作業包含 SNR、CPA 兩份。論文報告日後提供資料再加入。

## 已整理內容

四章主題式筆記、五份跨章概念、六個重畫圖例與 81 題分章練習。軟工四份 PDF 共 374 頁；另匯入硬體安全七份 PDF 共 293 頁與作業一原始 Notebook，保存在 raw。網頁正文與題庫為重新整理／編寫，不是投影片檔案清單或整頁貼圖。

題型為 40 題單選、24 題英文填空、17 題簡答／繪圖。單選與填空自動批改；手寫另以要點自評，不混入自動分數。題型參考使用者分享對話可見題目，但這不是教師正式考卷。

硬體安全的七個主題為：導論與威脅模型、密碼學與 AES、IC 功耗、軌跡統計、DPA／CPA、模板、PQC。這是本站學習順序，不宣稱為教師章次。作業一附原 Notebook 保存的十六格 SNR 圖；未重算原 NPZ。作業二整理題意、兩類圖的讀法與結果紀錄框架，實際成果待補。

## 維護方式

先讀 [AGENTS.md](AGENTS.md)。
- 課程內容：`wiki/courses/advanced-software-engineering/lessons/chapter-*.md`
- 硬體安全內容：`wiki/courses/hardware-security/lessons/` 與 `assignments/`
- 各課程分類、順序與相容資訊：`wiki/courses/<課程代號>/course.json`；不另放正文或題庫。舊 `scripts/hardware-manifest.json` 僅保留歷史快照，建置不再讀取。
- 題庫唯一來源：`wiki/courses/advanced-software-engineering/reviews/chapter-*.md` 中的 JSON 區塊
- 其他筆記與追溯：[Wiki 首頁](wiki/index.md)
- 版面與互動：`web/template.html`；共用樣式：`web/styles.css`（建置時內嵌，離線不另載入 CSS）
- 重新產生網站：在專案根目錄執行 `python3 scripts/build.py`

建置僅需 Python 3.9+，Markdown 3.7 已附在 scripts/vendor，無須額外安裝或連網。其授權附於 vendor 的 dist-info 目錄。不要直接修改生成的 index.html，否則下次建置會被覆蓋。dist 是建置產物，不需手動維護。

## 增加課程

1. 建立 `wiki/courses/<穩定英文代號>/index.md`，YAML `title` 為顯示名稱。
2. 按需要建立各分類的 Markdown，使用 `course.json` 選擇分類名稱、目錄與功能。不同課程可使用不同分類，不必增加相同的空分類。
3. 來源摘要放在 `wiki/sources/`，以 YAML `course` 指定課程歸屬。更新 Wiki 索引、來源登錄與操作紀錄。
4. 執行 `python3 scripts/build.py`、`python3 scripts/check.py`。

首頁、側欄、搜尋、來源列表、學習紀錄、路由及各類數量自動更新；無須修改前端程式。題庫放在 Markdown 的 JSON 區塊，設定分類 `kind: quiz` 後即可使用共用單選／填空／手寫自評功能。詳見[課程設定說明](docs/course-configuration.md)。

## 學習紀錄

作答、錯題、閱讀與繪圖草稿只儲存在當前瀏覽器，沒有雲端同步。可在「學習紀錄」匯出 JSON 及匯入；匯入會取代既有紀錄。私人瀏覽、移動本機檔案、更換瀏覽器或清除網站資料可能使紀錄消失，因此建議定期匯出。

本專案沒有 LLM 線上問答服務，不傳送作答至外部 API。除了使用者主動開啟分享對話連結外，網頁沒有外部依賴。教材公開範圍已由專案擁有人確認；新增來源仍須個別確認公開權限。

## 目前限制

現有課程皆為主題式重點複習，非逐頁逐圖詳解。硬體安全課程已匯入，作業一只有保存證據，作業二未取得實測成果。部分外部研究主張與講義生成插圖有待查核，不作爭議題判分依據。正式期中日期、範圍與配分仍以教師公布為準。詳見 [待釐清問題](wiki/questions.md)。
