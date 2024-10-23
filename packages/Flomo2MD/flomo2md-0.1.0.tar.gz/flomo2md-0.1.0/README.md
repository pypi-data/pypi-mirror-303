# Flomo2MD

## 简介

笔记理应当在各个平台自由传递。

Flomo2MD 是一个将 Flomo 导出的 HTML 转换成 Markdown 格式的工具。它可以帮助用户将 Flomo 中的笔记批量导出，并保存为 Markdown 文件，方便在其他平台或编辑器中使用。

## 特性

- 完整地导出图片附件链接，保持原有的相对路径不变
- 生成的 markdown 文件使用 UUID 命名，文件的首行采用创建时间作为标题
- 将文件的创建时间设置为笔记的创建时间，当前仅适配 macOS 系统

## 安装

```bash
pip install flomo2md
```

## 使用

```bash
flomo2md /path/to/flomo-html /path/to/output-dir
```

## 注意事项

- 当前对 flomo 的 html 样式没有完整地支持
