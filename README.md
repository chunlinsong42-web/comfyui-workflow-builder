# ComfyUI Workflow Builder（DSH / Agent Skill）

> 把「一句话需求」变成能在你的 ComfyUI 上跑通、能继续改的 workflow JSON。

一个面向 AI Agent 的 ComfyUI 工作流技能：内置 **recipe DSL**（约 20 行描述一个工作流）、
**离线校验器**、**UI ↔ API 转换**、**SSH 隧道 + 提交/下载**，以及从真实实例蒸馏出的 12 类管线模板。

- 🧱 生成 **ComfyUI UI 格式（0.4）** 工作流：可在前端打开、拖拽、继续编辑
- ✅ 离线 `build → validate → convert`：不连 GPU 也能改工作流
- 🚀 `submit --wait --download`：一条命令排队、等待、取回产物
- 🔌 SSH 隧道封装：远端 `127.0.0.1:6006` 的 ComfyUI 也能安全使用
- 📚 参考实例：150 个工作流 / 6,619 节点 / 12 类管线（图像、视频、音频、放大、对口型）

## 目录结构

```
comfyui-workflow-builder/
├── SKILL.md                  # Agent 的入口指令（DSH 会自动加载）
├── instance.example.json     # 实例配置模板（复制为 instance.json）
├── references/               # 格式规范、管线模板、节点目录、排错、显存参数
├── templates/                # 6 个 recipe 起点
├── scripts/comfy.py          # build/validate/convert/submit/tunnel/catalog
├── scripts/remote.py         # SSH 执行/上传/下载
└── docs/images/              # 示例产物
```

## 安装（DeepSeek Harness）

```bash
git clone <this-repo> ~/.dsh/skills/comfyui-workflow-builder
```

或直接把目录复制到 `~/.dsh/skills/`。Claude Code / Codex / Cursor 等支持 `SKILL.md` 的 agent 同理。

## 快速开始

```powershell
cd "$env:USERPROFILE\.dsh\skills\comfyui-workflow-builder"
Copy-Item instance.example.json instance.json   # 填 host/port/user/password
python scripts\comfy.py tunnel                   # 后台常驻：本地 16006 -> 远端 6006
python scripts\comfy.py stats                    # ComfyUI 0.44.0 | RTX 5090 | 33.7 GB
python scripts\comfy.py catalog                  # 抓节点目录（离线校验用）
```

第一个工作流：

```powershell
python scripts\comfy.py build templates\zimage-t2i.json -o wf.json
python scripts\comfy.py validate wf.json
python scripts\comfy.py submit wf.json --wait --download .\out
```

## 命令

| 命令 | 作用 |
|---|---|
| `tunnel` | SSH 本地端口转发（keepalive + 断线重连），常驻后台 |
| `stats` | ComfyUI 版本 / GPU / 显存 |
| `catalog` | 拉取 `/object_info` 到 `.cache/object_info.json` |
| `nodes <关键词>` | 查节点签名与可选模型名 |
| `build <recipe> -o wf.json` | recipe → UI 0.4 工作流（自动补 slot/link/widgets/布局） |
| `validate <wf.json>` | 类型、连线、必填输入、COMBO 合法性检查 |
| `convert <wf.json>` | UI → API prompt（提交用） |
| `submit <wf.json> --wait --download DIR` | 排队、等待、下载产物；`--seed` 统一改种子 |
| `queue` / `interrupt` | 查看队列 / 中断当前任务 |

## recipe 是什么

```json
{
  "title": "Zimage 文生图",
  "nodes": {
    "unet":   {"type": "UNETLoader", "widgets": {"unet_name": "Zimage/z_image_turbo_bf16.safetensors"}},
    "clip":   {"type": "CLIPLoader", "widgets": {"clip_name": "qwen_3_4b.safetensors", "type": "qwen_image"}},
    "vae":    {"type": "VAELoader", "widgets": {"vae_name": "z_image_vae.safetensors"}},
    "latent": {"type": "EmptyLatentImage", "widgets": {"width": 720, "height": 1280}},
    "pos":    {"type": "CLIPTextEncode", "widgets": {"text": "一名亚洲女生，晨光，写实人像"}},
    "neg":    {"type": "CLIPTextEncode", "widgets": {"text": "低分辨率，模糊"}},
    "sampler":{"type": "KSampler", "widgets": {"seed": 42, "steps": 8, "cfg": 1,
                                                "sampler_name": "euler", "scheduler": "simple", "denoise": 1}},
    "decode": {"type": "VAEDecode"},
    "save":   {"type": "SaveImage", "widgets": {"filename_prefix": "%date:yyyyMMdd%/image_"}}
  },
  "links": [
    "unet.MODEL -> sampler.model",
    "clip.CLIP -> pos.clip", "clip.CLIP -> neg.clip",
    "latent.LATENT -> sampler.latent_image",
    "pos.CONDITIONING -> sampler.positive", "neg.CONDITIONING -> sampler.negative",
    "sampler.LATENT -> decode.samples",
    "vae.VAE -> decode.vae", "decode.IMAGE -> save.images"
  ]
}
```

`build` 会从 `/object_info` 取节点签名，自动填默认值、补种子后的 `control_after_generate`、
计算 slot 与连线、按依赖分层布局，输出可直接导入前端的工作流。

## 示例产物

| Zimage Turbo | Krea2 Turbo |
|---|---|
| ![](docs/images/demo-zimage.png) | ![](docs/images/demo-krea2.png) |

（512×768 / 6 步 48.6s；768×1024 / 8 步 42.6s，RTX 5090）

## 设计

```
recipe.json ──build──> workflow(UI 0.4) ──validate──> convert ──> POST /prompt ──> /history ──> /view
                                      │
                                      └─ 离线校验：类型/连线/必填/COMBO（基于 .cache/object_info.json）
```

- **UI 0.4 为交付物**：用户能在 ComfyUI 前端继续编辑，而不是拿到只能提交的 API JSON。
- **以 `/object_info` 为唯一事实来源**：节点名、模型名、默认值、min/max、slot 全部实时读取。
- **自动修复循环**：连接/参数/结构/资源四类错误，最多 5 轮（见 `references/error-autofix.md`）。

## 兼容性

- 在 **ComfyUI 0.44.0 / 前端 1.58.5** 上实测；UI 0.4 格式对 0.3.x 以后版本基本通用。
- Python 3.9+（提交端仅用标准库；SSH 功能需要 `paramiko`）。
- 需要你的 ComfyUI 暴露 HTTP API（默认 6006），并通过 SSH 可达。

## 安全

- 仓库**不含**任何凭据；`instance.json` 与 `.cache/` 已被 `.gitignore` 排除。
- 密码建议用环境变量传入，或改用 SSH key。
- 只在你有权操作的实例上使用；模型与生成内容的许可由使用者负责。

## 致谢

格式规则、模板思路和自动修复流程参考了：

- [LingyiChen-AI/comfyui-workflow-skill](https://github.com/LingyiChen-AI/comfyui-workflow-skill)（MIT）
- [21Pdontno/comfyui-workflow-skills](https://github.com/21Pdontno/comfyui-workflow-skills)（MIT）

它们的原文存档在 `references/upstream/`，版权归原作者。

## English

A DeepSeek Harness / agent skill that builds **editable ComfyUI workflows** from a compact recipe DSL:
offline `build/validate/convert`, SSH-tunneled `submit --wait --download`, plus 12 pipeline templates
(image / video / audio / upscale / lipsync) distilled from a real 150-workflow ComfyUI instance.

Install: copy this folder into `~/.dsh/skills/`, copy `instance.example.json` to `instance.json`,
then run `python scripts/comfy.py tunnel` and `python scripts/comfy.py build templates/zimage-t2i.json -o wf.json`.

## License

MIT — see [LICENSE](LICENSE).
