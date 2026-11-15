# Changelog

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
