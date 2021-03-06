---
title: "Monospaced fonts for Visual Studio Code"
categories: [Editor, Visual Studio Code]
tags: [fonts, vscode]
---

To start with, a little background on how I started using Visual Studio Code:

Back in early 2016, I was using [Notepad++](https://notepad-plus-plus.org/) to write my daily work notes. For better readability, I thought to have different sections of the text (headings, paragraphs, lists, etc.) appear in different colors. Storing my notes in [Markdown](https://en.wikipedia.org/wiki/Markdown) format seemed to be an interesting option. Notepad++ has theming support, but it did not natively understand the Markdown syntax. I started with [Microsoft OneNote](https://www.onenote.com/) for first few days but having a text-based editor was always superior to an UI editor, since it does not require switching hands between keyboard and mouse for styling the text and aligning text-sections. In addition, if the text is stored in markdown format, I can switch to a better available text editor in future to view and edit the notes. Finally, I ended up on [Visual Studio Code](https://code.visualstudio.com/) since it supported markdown syntax highlighting and it featured HTML preview of the markdown text.

Visual Studio Code on Windows uses Consolas as the default font for text. In my opinion, Consolas is the best monospaced typeface available out-of-the-box in Windows. I have been using Consolas in VS Code for past 18 months and I never thought about changing the default font since Consolas (or any other font) gets rendered superbly in VS Code.

VS Code is built using [Electron](https://electronjs.org) framework that is maintained by GitHub. Electron allows for the development of desktop applications using web technologies i.e. HTML, JS, and CSS. It uses the [Chromium](https://www.chromium.org/) project, which is the bare metal of Google Chrome browser. Therefore, all Electron apps share the same rendering component ([Blink](https://www.chromium.org/blink)) and JavaScript engine (V8) with Chrome browser. Likewise, you get to experience the same crisp and clear text in VS Code, as on Chrome. Microsoft Edge browser also renders text quite nicely, but I do not know why Microsoft does not offer a similar high-quality text rendering on other Microsoft products like Word and Visual Studio IDE.

Here is how **Consolas** font looks like on VS Code:

<figure align="center">
  <img src="/assets/img/posts/consolas-font.png">
  <figcaption>Consolas Font</figcaption>
</figure>

Consolas and similarly a lot of monospaced fonts may work great for console applications like PowerShell, but they are not created specifically with programmers in mind. Instead, there are a selected set of fonts available for free on internet that are possibly better substitutes for Consolas if you are using VS Code primarily for coding. Here are the three fonts I find worth mentioning:

## Source Code Pro

<figure align="center">
  <img src="/assets/img/posts/source-code-pro-font.png">
  <figcaption>Source Code Pro Font</figcaption>
</figure>

Source Code Pro ([download link](https://www.fontsquirrel.com/fonts/download/source-code-pro)) makes quite a few changes to help with programming. For example, it makes it easy to distinguish between `I`, `l` and `1` characters. The single and double-quotes that are used heavily in programs are enlarged. Vertical placement of symbols like asterisk and hyphens that are used as mathematical operators, is adjusted to align them with nearby operands. It also optimizes shapes of greater-than and less-than symbols to ensure that characters within arrow-operators e.g. `->` and `=>` are not misaligned.

## Fira Code

<figure align="center">
  <img src="/assets/img/posts/fira-code-font.png">
  <figcaption>Fira Code Font</figcaption>
</figure>

Fira Code ([download link](https://www.fontsquirrel.com/fonts/download/fira-code)) adds support for programming-ligatures. For example, check how `=>` is printed in line 347 above. The font itself is quite beautiful. The complete list of supported ligatures can be found on Fira Code's [Github repository page](https://github.com/tonsky/FiraCode). They also have a [Wiki page](https://github.com/tonsky/FiraCode/wiki/VS-Code-Instructions) with instructions to enable ligatures in VS Code.

<figure align="center">
  <img src="https://raw.githubusercontent.com/tonsky/FiraCode/master/showcases/all_ligatures.png">
  <figcaption>All ligatures available in Fira Code</figcaption>
</figure>

## Luxi Mono

<figure align="center">
  <img src="/assets/img/posts/luxi-mono-font.png">
  <figcaption>Luxi Mono Font</figcaption>
</figure>

Luxi Mono ([download link](https://www.fontsquirrel.com/fonts/download/Luxi-Mono)) is unique in the sense that it is both monospaced and serif font. Moreover, it is quite elegant. Its italics style at line 362 feels better than those of Source Code Pro and Fira Code.

There are other font alternatives as well. Many of those are mentioned on [Fira Code's README page](https://github.com/tonsky/FiraCode#alternatives). One last font worth mentioning is [Operator Mono](https://www.typography.com/fonts/operator/styles/). It is a gem of all fonts though it is a paid one and far too heavy on the pocket. All in all, I was using Fira Code in my VS Code editor while I was awe-stricken with its ligatures. Once that phase was over, I switched to Source Code Pro. Having used these fonts, I do not think I will ever be going back to Consolas on VS Code.