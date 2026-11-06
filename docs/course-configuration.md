# 新增課程與分類

Wiki Markdown 是正文與題庫的唯一來源。`course.json` 僅放導覽、順序、功能及相容性設定；不要寫課程總數、分類內容數量或複製題庫。

## 課程目錄

在 `wiki/courses/<穩定英文代號>/` 建立 `index.md`，依現有模板填入 YAML，至少以 `title` 指定顯示名稱。目錄代號是穩定識別碼；更改課名請修改 `title`，不要因改名或排序而改目錄代號。

同目錄的 `course.json` 可指定：

```json
{
  "order": 10,
  "sections": [
    {
      "id": "study",
      "label": "課程",
      "directory": "lessons",
      "kind": "lesson",
      "trackReading": true
    },
    {
      "id": "reports",
      "label": "論文報告",
      "directory": "papers",
      "kind": "paper",
      "trackReading": true
    }
  ]
}
```

以上只是設定示例，並非強制分類。可只選作業、加上測驗、使用其他顯示名稱或任意數量的分類；分類順序依 `sections`。`directory` 為相對於課程目錄的資料夾，必須在課程內。分類目錄可有或沒有 `index.md`，所有下層內容 Markdown 都會自動加入；分類索引不計入內容篇數。

省略 `course.json` 或 `sections` 時，建置會從課程子目錄 `*/index.md` 發現分類，使用其標題與類型。需要明確選擇分類、閱讀標記或互動測驗時，請提供設定；`sections: []` 代表不顯示主要分類。未選入主要分類的既有筆記仍可經 Wiki 連結與搜尋閱讀。

## 網址、顯示與順序

- 預設課程網址為 `#/courses/<課程代號>`，分類與內容網址依分類 ID、相對檔名自動產生，不需新增前端路由。
- 課程可選填 `route` 以保留既有網址。分類可選填 `route` 作為網址片段；顯示名稱用 `label`，兩者互不依賴。
- 課程 `order` 決定課程排序；同順位以穩定課程代號排序。頁面可在下述覆寫中設定 `order`，同順位以穩定路徑排序。
- 課名取自課程索引的 YAML `title`；內容標題取自各頁 `title` 或第一個標題，亦可覆寫 `short`。首頁與分類的篇數、題數及學習紀錄分母均從實際頁面計算。

可選的 `pages` 以課程相對檔案路徑為索引：

```json
{
  "pages": {
    "lessons/topic-a.md": {
      "short": "主題 A",
      "desc": "這篇的學習重點",
      "order": 10,
      "source": "COURSE-001",
      "pages": 20
    }
  }
}
```

`pages` 是 metadata 覆寫，不是內容清單。未寫在設定裡的新 Markdown 仍會加入分類。`pages` 數值是來源講義頁數，用來顯示與檢查引用，不是章節數上限。`file` 可記來源檔名；正文、來源限制與作業實際成果仍放 Markdown。

## 任一課程的測驗

分類設定 `kind: "quiz"`，每份測驗 Markdown 內放一個 JSON 陣列區塊，即可使用共用練習／測驗、錯題及自評功能。題型沿用 `choice`、`fill`、`written`；題目需有全站唯一且穩定的 `id`，以及 `prompt`、`source`、`pages`、對應答案與解析。格式可參考既有測驗 Markdown 或 `templates/review.md`。

題數從 JSON 陣列實際計算。單選不限定四個選項；簡答與繪圖只自評，不自動判斷語意。`answerImage` 可使用 `wiki/assets/` 相對圖檔路徑；既有唯一檔名仍相容。

測驗對應課程可在頁面覆寫設定 `lesson: "lessons/topic-a.md"`；未設定時，自動配對同課程中相同檔名且可標記閱讀的唯一頁面，否則回課程入口。

## 來源與學習紀錄

來源摘要放在 `wiki/sources/`，YAML `type: source`、`course: <課程代號>`；來源列表會按課程歸屬自動分組。不屬於現有課程的摘要列於共用與其他來源。登錄、已讀範圍與限制仍須維護在 Wiki 中。

閱讀內容由分類 `trackReading: true` 選定；預設不把作業點閱當作完成。紀錄統計依實際課程、所選閱讀頁與題目 ID 計算，不依課程名稱、序號或陣列位置。

新內容使用帶課程路徑的穩定紀錄識別碼。既有頁面設定中的 `readKey`、`quizKey`、`recordChapter`、`route` 是舊紀錄／書籤的相容資訊，請勿因排序或更名而修改。`recordChapter` 可保留舊數字型別，但其字串值必須等於 `quizKey`；這是舊資料識別碼，並非章節數限制。題目 ID 必須全站唯一，不因重新排序而變更。

瀏覽器儲存鍵仍為 `course-wiki-v1`，匯出版本仍為 1；舊閱讀、錯題、草稿、歷史與繪圖仍可載入和匯入。暫時移除課程時，未能對應到現有內容的紀錄會保留在匯出檔，不會在其他課程錯配。已移除題目的草稿無法直接續答時，重新進入該測驗會建立當前題庫的新草稿；原備份可留作歷史。

## 完成後

更新 Wiki 全域索引、來源登錄及 log，再於專案根目錄執行：

```sh
python3 scripts/build.py
python3 scripts/check.py
```

不修改前端課程清單或路由處理器。數量以建置結果為準；文件裡的既有內容快照不構成程式限制。

## 指定課程點綴色

可在 `course.json` 頂層加入 `"accent": "#52a9ff"` 指定亮藍色；使用六位十六進位色碼，建置會檢查與黑字的對比至少 4.5:1。未指定時沿用穩定課程 ID 的自動配色。設定會套用同課程所有內頁，不影響首頁亮黃主題；其他課程仍可使用桃紅等既有調色盤。
