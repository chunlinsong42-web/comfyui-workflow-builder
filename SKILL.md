---
name: comfyui-workflow-builder
description: 为远程 ComfyUI 实例制作、改造、校验并执行工作流。提供 recipe→UI JSON 生成器、离线校验、API 提交、SSH 隧道与 12 类管线模板（图像/视频/音频/放大/编辑）。当用户要求：做 ComfyUI 工作流、文生图/图生图/图生视频/文生视频/音频/放大/对口型 工作流、修改或调试 workflow JSON、把想法做成能在自己 ComfyUI 上跑的流程时使用。触发词：comfyui、工作流、workflow、文生图、图生视频、Wan2.2、LTX、Krea2、Zimage、MiniMax-H3、放大、超分、SeedVR2、TTS、口型、workflow json。
---

# ComfyUI 工作流制作

把「一句话需求」变成「能在你的 ComfyUI 上跑通、能继续改的 workflow JSON」。
技能内置一套离线工具链（recipe DSL、UI/API 互转、校验、提交、SSH 隧道），
并用一台真实机器（ComfyUI 0.44 / RTX 5090 / 150 个工作流）蒸馏出的 12 类管线模板作为起点。

## 安装（DeepSeek Harness）

```powershell
git clone <本仓库地址> "$env:USERPROFILE\.dsh\skills\comfyui-workflow-builder"
# 或直接把整个目录复制到 ~/.dsh/skills/comfyui-workflow-builder
```

其他支持 `SKILL.md` 的 agent（Claude Code / Codex / Cursor 等）同理：放进其 skills 目录即可。

## 配置（必做）

```powershell
cd "$env:USERPROFILE\.dsh\skills\comfyui-workflow-builder"
Copy-Item instance.example.json instance.json   # 填 host / port / user / password
python scripts\comfy.py tunnel                   # 本地 16006 -> 远端 127.0.0.1:6006
python scripts\comfy.py stats                    # 应打印 ComfyUI 版本 + GPU
python scripts\comfy.py catalog                  # 抓 /object_info 到 .cache
```

也支持环境变量（优先级更高）：`COMFY_SSH_HOST/PORT/USER/PASSWORD`、`COMFY_TUNNEL_PORT`、
`COMFY_REMOTE_PORT`、`COMFY_BASE_URL`。详见 `references/instance.md`。

## 铁律

1. **先配置、先隧道**：没有 `instance.json` 或隧道不通时，`submit/stats/catalog` 都会失败。
2. **先 validate 再 submit**；**先小参数跑通再放大**（图像 512×768、视频 480p/33 帧、音频 1 句）。
3. **节点名、模型文件名只能来自 `/object_info`**（`comfy.py nodes <关键词>`），禁止臆造。
4. **不手写 `widgets_values`**：用 recipe + `comfy.py build`（自动补种子后的 `control_after_generate`、算 slot/连线/布局）。
5. **不改** ComfyUI 启动脚本、`custom_nodes/` 源码、模型软链；只往 `user/default/workflows/` 写工作流。
6. 交付的 UI JSON 必须**在目标实例执行成功**过（或明确说明只做了静态校验）。

## 标准流程

1. **拆需求**：任务类型（图/视频/音频/放大/编辑/对口型）→ 模型族 → 分辨率/时长/批量 → 输出格式。
2. **选参考**：查 `references/workflow-index.md`（参考实例 150 个工作流的节点链）与 `references/patterns.md`，挑最接近的 1~2 个。
3. **写 recipe**：从 `templates/` 复制一份改（6 个起点），或按 patterns 里的链组装。
4. **build + validate**：
   ```powershell
   python scripts\comfy.py build recipe.json -o wf.json
   python scripts\comfy.py validate wf.json
   ```
5. **试跑**：`python scripts\comfy.py submit wf.json --wait --download .\out`（内部先 validate 再转 API）。
6. **修错**：按 `references/error-autofix.md` 分类（连接/参数/结构/资源）每轮只修一类，重校验，最多 5 轮。
7. **正式跑 + 交付**：确认产物 → 上传 UI JSON 到远端分类目录（`remote.py put`）→ 给出模型、参数、显存、耗时说明。

## 自动修复循环（最多 5 轮）

```
validate ─通过→ submit(小参数) ─成功→ 放大参数正式跑
   └─有错→ 分类 → 改 recipe → 重 validate（循环）
```

| 类别 | 典型错误 | 修法 |
|---|---|---|
| 连接 | `required input not connected`、类型不匹配 | 补 link / 换 output 槽 |
| 参数 | `value_not_in_list`、必填控件缺失 | `comfy.py nodes` 查真实选项 |
| 结构 | `unknown class_type`、autogrow/子图 | 换节点，或改走"复制既有工作流" |
| 资源 | OOM、超时、队列卡住 | 降分辨率/帧数 → 量化 → block swap |

细节见 `references/error-autofix.md`。不要在同一轮同时换模型、改参数、改链路。

## 命令速查

```powershell
python scripts\comfy.py tunnel               # SSH 隧道（后台常驻，带 keepalive/自动重连）
python scripts\comfy.py stats                # 版本/GPU
python scripts\comfy.py catalog              # 抓节点目录（首次或模型变更后）
python scripts\comfy.py nodes KSampler       # 节点签名与可选值；也支持关键词模糊搜
python scripts\comfy.py build recipe.json -o wf.json
python scripts\comfy.py validate wf.json
python scripts\comfy.py convert wf.json -o prompt.json
python scripts\comfy.py submit wf.json --wait --download .\out [--seed 123]
python scripts\comfy.py queue / interrupt

python scripts\remote.py run "ls /path/to/ComfyUI/user/default/workflows"
python scripts\remote.py get <远端文件> .\ref.json
python scripts\remote.py put .\wf.json "<远端分类>/name.json"
```

## 任务 → 模型选择（模板基于参考实例，按你的 catalog 替换模型名）

| 需求 | 首选 | 备选 | 关键参数 |
|---|---|---|---|
| 快速文生图 | Zimage Turbo | Krea2 Turbo | cfg=1，6~9 步，euler/simple |
| 写实人像 / 电商图 | Krea2 Turbo + 风格 LoRA | Qwen-Image 2512 | 见 patterns §2 |
| 中文复杂提示词 | Qwen-Image 2512 | Qwen-Image 2.1 | 8 步（Lightning LoRA） |
| 二次元 / SDXL LoRA 生态 | Illustrious / SDXL + 高清修复 | — | cfg 5~7，25~30 步 |
| 国风 / 插画 | FLUX2-Klein 9B | — | res_2s/bong_tangent，cfg=1，10 步 |
| 图生视频 | Wan2.2 原生 `WanImageToVideo` | WanVideoWrapper、LTX 2.5 | 480p 起，81 帧 |
| 音画同出 / 口播 | LTX 2.5 | H3（带音频 VAE） | 25fps，121~241 帧 |
| 多参考图生视频 | MiniMax-H3 ref2va | H3 Singularity turbo | 1344×768，124 帧 |
| 对口型数字人 | InfiniteTalk (Wan2.1) | LTX2.3 数字人 | 见 patterns §8 |
| 配音 / 克隆 / 音乐 | Qwen3-TTS | ACE-Step / MiniMax Music3 | 见 patterns §9 |
| 放大 / 去水印 | SeedVR2 / RTX VSR | FlashVSR / VOSR2 / RelayVSR | 见 patterns §10 |

## recipe 语法（唯一推荐的手写格式）

```json
{
  "title": "显示用标题",
  "annotate": true,
  "nodes": {
    "别名": {"type": "节点类型", "widgets": {"控件名": 值}}
  },
  "links": ["源别名.输出名 -> 目标别名.输入名", "源别名.LATENT -> 目标别名.samples"]
}
```

- 输出引用支持：输出名（`CONDITIONING`）、输出类型（`MODEL`/`IMAGE`）、槽位序号（`0`）。
- 输入名必须是目标节点真实输入名（见 `references/node-catalog.md` 或 `comfy.py nodes`）。
- 未写控件用 `/object_info` 默认值；种子类 INT 自动补 `control_after_generate=randomize`。
- `"annotate": true` 给每个节点生成 `[分类] 类型` 标题，便于阅读。
- 连线做类型检查；未连接的必填输入由 validate 抓出。
- **不支持**：子图、autogrow（如 H3 的 `ref_images`）、dynamic combo、bypass/mute、Set/Get 虚拟连线——这些场景复制既有工作流改控件。

示例：`templates/zimage-t2i.json`、`krea2-t2i.json`、`flux2-klein-t2i.json`、`sdxl-illustrious-t2i.json`、`zimage-i2i.json`、`wan22-native-i2v.json`。

## 改造既有工作流（最常用）

1. 下载：`python scripts\remote.py get "<远端绝对路径>" .\ref.json`
2. 只改控件，同时同步 `widgets_values` 与 `widgets_values_named`（旧前端没有 named 时按位置数组）。
3. 改完 `validate`，小参数 `submit --wait` 试跑；结构级改造（加 LoRA/放大链）建议回 recipe 重搭。

## 交付规范

- 远端路径：`user/default/workflows/<分类>/<前缀>-<主题>.json`，不覆盖既有文件。
- 本地保留 recipe，便于二次生成。
- 回复用户：工作流路径、模型、关键参数、显存/耗时、试跑结果（分辨率/步数/产物），附预览。
- 注意模型许可与生成内容合规。

## 文件地图

| 文件 | 内容 |
|---|---|
| `SKILL.md` | 本文件：流程、铁律、命令 |
| `instance.example.json` | 实例配置模板（复制为 `instance.json`） |
| `references/instance.md` | 配置、目录、参考实例、离线处理 |
| `references/workflow-format.md` | UI 0.4 与 API JSON 规范、控件/种子/连线规则 |
| `references/patterns.md` | 12 类管线模板（图像/视频/音频/放大/编辑/FLUX2-Klein） |
| `references/node-catalog.md` | 485 个常用节点签名（来自参考实例） |
| `references/workflow-index.md` | 参考实例 150 个工作流的分类索引 |
| `references/troubleshooting.md` | 错误对照表 |
| `references/error-autofix.md` | 5 轮自动修复循环 |
| `references/vram-and-samplers.md` | 显存预算与采样参数 |
| `references/github-digest.md` | 与上游技能的设计取舍 |
| `references/upstream/` | 上游文档存档（MIT，版权归原作者） |
| `templates/*.json` | 6 个 recipe 起点 |
| `scripts/comfy.py` | build / validate / convert / submit / tunnel / catalog |
| `scripts/remote.py` | SSH 执行、上传、下载 |

## 参考实例上的验证记录（2026-11）

- Zimage Turbo 512×768 / 6 步：success，48.6s（含首次加载）。
- Krea2 Turbo 768×1024 / 8 步：success，42.6s。
- 离线结构校验通过：Zimage 图生图、FLUX2-Klein、SDXL-Illustrious+4x、Wan2.2 原生 I2V。
- 参考实例：ComfyUI 0.44.0 / 前端 1.58.5 / RTX 5090 / 6,619 节点 / 150 工作流。

## 致谢

- [LingyiChen-AI/comfyui-workflow-skill](https://github.com/LingyiChen-AI/comfyui-workflow-skill)（MIT）
- [21Pdontno/comfyui-workflow-skills](https://github.com/21Pdontno/comfyui-workflow-skills)（MIT）

格式规则、模板思路与自动修复流程参考了它们；实现、实例细节与校验器为本项目原创。
