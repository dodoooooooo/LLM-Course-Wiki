---
id: hs-papers-index
title: 硬體安全｜論文報告
subtitle: Racing against the clock: side-channel leakage from crossing asynchronous clock domains
course: hardware-security
type: paper
status: verified
created: 2026-11-07
updated: 2026-11-07
sources: [HS-010, EXT-004, EXT-005]
tags: [論文報告, 時脈域, 側通道]
---

本次指定論文為 Martin Thompson、David Oswald 的 *Racing against the clock: side-channel leakage from crossing asynchronous clock domains*。

## 作者與期刊簡介

**Martin Thompson**：本篇第一作者。論文首頁同時列出英國杜倫大學（Durham University）與 ZF Automotive UK Ltd；致謝也提到雇主 ZF 的支持，呈現學術研究與汽車產業背景的連結。這裡只說明本文署名所列資訊，不推定未列出的職稱或作者分工。[HS-010，PDF p.1、19](../../../sources/hs-010.md)

**David Oswald**：本篇共同作者。杜倫大學官方介紹為電腦科學系的網路安全教授，研究重點包含嵌入式系統、可信執行，以及側通道、故障注入等實作安全問題；這與本文探討晶片實作如何洩漏資訊的方向相符。[EXT-004，杜倫大學官方簡介，2026-11-07 查閱](../../../sources/hs-011-authors-journal.md)

**TCHES 是什麼？** 全名為 *IACR Transactions on Cryptographic Hardware and Embedded Systems*，可理解為研究密碼硬體與嵌入式系統安全的學術期刊。它與 CHES 採期刊／研討會結合的開放取用發表模式：TCHES 是期刊，CHES 是對應的研討會，不是兩篇不同的研究。本篇刊於 **2026 年第 2 期、印刷頁 28–50**；報告可簡稱「TCHES 2026 第 2 期論文」。[HS-010，PDF p.1](../../../sources/hs-010.md) · [EXT-005，IACR 官方出版模式說明](../../../sources/hs-011-authors-journal.md)

## 閱讀入口

1. [報告導讀與討論](racing-against-the-clock.md)：研究問題、貢獻、證據界線、報告大綱與可能問答。
2. [各章重點](racing-against-the-clock-chapters.md)：依原文第 1–7 節及附錄整理，附 PDF 頁次與重要圖表讀法。
3. [名詞解釋](racing-against-the-clock-glossary.md)：時脈、硬體、統計與密碼學名詞，先讀白話再看論文用途。

這是閱讀整理，沒有執行作者程式或重現攻擊。報告時間、日期、格式與評分規範尚未提供。

[論文來源 HS-010](../../../sources/hs-010.md) · [回硬體安全](../index.md)
