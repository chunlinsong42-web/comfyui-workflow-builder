# 从 GitHub 同类技能里学到的东西（2026-11-15 调研）

调研对象：

- [LingyiChen-AI/comfyui-workflow-skill](https://github.com/LingyiChen-AI/comfyui-workflow-skill) — 自然语言→工作流 JSON，34 个模板 + 42 类节点文档
- [21Pdontno/comfyui-workflow-skills](https://github.com/21Pdontno/comfyui-workflow-skills) — 全生命周期（设计/校验/执行/自动修复），带 API 客户端与标注规范

本文件记录：**哪些做法被吸收进本技能、哪些被改写、哪些在本实例不适用**。读它能在改动本技能时知道设计取舍。

## 1. 已吸收并落地

| 来源 | 做法 | 在本技能中的落点 |
|---|---|---|
| 21Pdontno | 协调者 + 专家分工的自动修复循环（连接/参数/结构/资源），最多 5 轮 | `references/error-autofix.md`；`troubleshoot` → 分类 → 改 recipe → 重校验的流程写进 SKILL.md |
| 21Pdontno | 每个节点写可读标题（`[模块] 功能 - 说明`） | `comfy.py build` 支持 recipe 顶层 `"annotate": true`，自动给节点加 `[分类] 类型` 标题；`templates` 可按需开启 |
| 21Pdontno | VRAM 预算表、采样器/调度器速查、按模型给推荐参数 | `references/vram-and-samplers.md`（按本机 5090 33.7G 重算） |
| LingyiChen | 工作流 JSON 格式细则：UI 0.4 顶层字段、links 元组、widgets_values 顺序 | 已写入 `references/workflow-format.md`，并补了本实例特有的 `widgets_values_named` |
| LingyiChen | **种子后必须有 `control_after_generate`**，否则后续控件全部错位 | `comfy.py build` 自动补 `randomize`；`validate` 不做位置校验，但配方 DSL 从根本上避免手写数组 |
| LingyiChen | 二次元/SDXL/FLUX 的常见参数（CFG、步数、分辨率） | 合并进 `patterns.md` 与 `vram-and-samplers.md` |
| LingyiChen | Wan2.2 **原生节点**链（UNETLoader + CLIPLoader(wan) + WanImageToVideo + KSampler） | 新增 `templates/wan22-native-i2v.json`（已按本实例 object_info 校验；与 G 系列 WanVideoWrapper 方案并存） |
| 两者 | 交付时给模型说明与参数建议；先查环境再设计 | 写进 SKILL.md 标准流程第 1、7 步 |

## 2. 被改写/修正的部分

- **它们直接产出 API 格式**（`{id: {class_type, inputs}}`）。本实例用户要的是能在前端打开、继续改的 **UI 0.4 格式**，所以本技能以 UI JSON 为交付物、API 仅在提交时内部转换（`comfy.py convert`）。
- **LingyiChen 的 `models` 顶层数组**（缺失模型自动下载提示）在本机无意义——模型已挂载；本技能不发 `models` 字段，校验时直接对 `object_info` 组合框做真实文件名检查（更强）。
- **21Pdontno 的 `_meta.title`** 只对 API 格式有意义；本技能改用 UI 格式的节点 `title` 字段，并在 `build --annotate` 时生成。
- **节点名不能照抄**：两个仓库的节点表混有不同版本/自定义包。实测本实例：`QwenLoader`、`TextImageEncodeQwenVL`、`EmptyQwenImageLayeredLatentImage`、`WanTextToImageApi` 存在；但 `IPAdapterUnifiedLoader`/`IPAdapter` **不存在**（`models/ipadapter` 为空），照抄会直接报 unknown node。本技能一律以 `object_info` 为准（`comfy.py nodes`）。
- **它们的模板多用 SD1.5/SD3/Hunyuan/Mochi 等本机没有的模型**；本技能模板全部换成本机真实可用的 Zimage/Krea2/FLUX2-Klein/SDXL-IL/Wan2.2，并用离线 catalog 校验。

## 3. 本实例额外验证得到的结论（它们没有覆盖）

- `widgets_values_named` 是本机前端 1.41+ 的命名字典，比位置数组稳得多——`comfy.py convert` 优先用它。
- Wan2.2 有**两条路线**：`custom_nodes/ComfyUI-WanVideoWrapper`（G 系列 14 个）与**原生节点**（`WanImageToVideo` + `KSampler`，12 节点跑通结构校验）。原生链更短、依赖更少；wrapper 链功能多（block swap、LoRA、首尾帧、长视频）。
- H3 的 `ref_images` 是 `COMFY_AUTOGROW_V3` 自动增长输入，任何「JSON 模板生成器」都难正确生成——正确做法是复制 `U01` 之类既有工作流再改提示词。
- `RTXVideoSuperResolution` 的 `resize_type` 是 `COMFY_DYNAMICCOMBO_V3`（带子输入），recipe DSL 不支持，直接复制 `M07`。
- 子图（`extra.subgraphs`）与 Set/Get 虚拟连线同理：**改造而非重建**。

## 4. 不建议照搬的做法

- 直接用 API 格式交付：用户无法在前端继续编辑，且丢失分组/位置。
- 手写 `widgets_values` 位置数组：种子后的 `randomize` 一漏全错；用 `build`。
- 在 JSON 里塞 `models` 下载表：本机模型齐备，且容易指向不存在的 URL。
- 用未安装节点搭"万能模板"：本机 200 个 custom_nodes 覆盖面已很广，但名字版本差异大，必须查 catalog。
