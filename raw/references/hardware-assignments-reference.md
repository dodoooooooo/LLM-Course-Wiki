# 硬體安全兩份作業：分享對話來源

URL：https://chatgpt.com/share/6aedb170-9494-83ec-964f-f6f801adf9bc

查閱日期：2026-11-06。已開啟並閱讀可見題目與相關上下文，以下為轉述，非逐字複製。部分歷史附件及可展開內容未完整取得。

## 作業一
在 ChipWhisperer Nano 執行 AES-128、使用隨機明文，記錄 51200 條功耗軌跡。對第一輪十六個 S-box 輸出的 HW 計算並繪製 SNR traces。原題指向 SCA101 Power and Hamming Weight Relationship Notebook 與 matplotlib。

## 作業二
沿用作業一資料，實作 CPA 恢復祕密金鑰。每個 key byte 都要有 correlation vs. sample point 與 maximum correlation vs. number of traces 兩類圖。原題說 200 條 traces 應足夠；後續中文補充要求涵蓋全部 16 bytes。

## 證據界線
使用者貼上的題目作為需求依據；歷史 AI 程式、預期圖形與成功說法均不當作實測證據。作業一狀態另外以原始 Notebook 核對。未取得正式截止日期、評分表、原 NPZ 或完成的 CPA Notebook。
