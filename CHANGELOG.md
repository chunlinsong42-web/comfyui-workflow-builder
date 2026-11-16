# Changelog

## v1.1.0 — 2026-11-16

**新增**

- `comfy.py inspect`：展开 `definitions.subgraphs` / `extra.subgraphs`，打印真实节点链与控件（用于读官方/他人模板）。
- `references/official-templates.md`：学习 Comfy-Org/workflow_templates 的 766 个官方模板（12 个分组），
  记录子图格式、10 个代表模板的展开链路、官方 vs 参考实例参数对照。
- `requirements.txt`（paramiko）。
- `scripts/check_repo.py` + GitHub Actions CI（模板 JSON、SKILL frontmatter、文档链接、密钥扫描）。
- `CONTRIBUTING.md`、`SECURITY.md`。
- README 重制：Banner、徽章、目录、Mermaid 架构图、FAQ、Roadmap。

**修正**

- `workflow-format.md`：子图定义位置更正为 `definitions.subgraphs`（旧格式 `extra.subgraphs` 仍兼容）。
- `patterns.md`：新增官方模板对照（Wan 2.2 双模型两段采样、FLUX2 Flux2Scheduler、LTX 两段 ManualSigmas 等）。

## v1.0.0 — 2026-11-15

首个公开版本。

- `scripts/comfy.py`：`tunnel / stats / catalog / nodes / build / validate / convert / submit / queue / interrupt`
  - recipe DSL（别名、按输出名/类型/槽位连线、自动布局、`annotate` 节点标题）
  - 从 `/object_info` 自动取签名、默认值、COMBO 校验、种子后 `control_after_generate`
  - 离线校验缓存：`.cache/object_info.json`
  - SSH 隧道：keepalive 20s、断线自动重连
- `scripts/remote.py`：SSH 执行 / 上传 / 下载
- 配置：`instance.json` + 环境变量覆盖，仓库不含凭据
- 文档：格式规范、12 类管线模板、节点目录、排错、自动修复循环、显存与采样参数、上游技能取舍记录
- 模板：Zimage t2i / Krea2 t2i / Zimage i2i / FLUX2-Klein t2i / SDXL-Illustrious t2i+4x / Wan2.2 原生 i2v
- 验证：Zimage 512×768 6 步 48.6s；Krea2 768×1024 8 步 42.6s（RTX 5090）
