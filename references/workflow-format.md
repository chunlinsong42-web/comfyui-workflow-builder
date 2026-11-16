# ComfyUI 工作流 JSON 规范（参考实例：ComfyUI 0.44.0 / 前端 1.58.5）

本文件说明"前端 UI 格式"（LiteGraph，`version: 0.4`）和"API 提交格式"两种 JSON。
参考实例的 150 个既有工作流全部是 UI 格式；`scripts/comfy.py` 负责两者互转。

## 1. 顶层结构

```json
{
  "id": "0e6d...uuid",           // 工作流 id，前端用；任意 uuid 字符串即可
  "revision": 0,
  "last_node_id": 13,            // 必须 >= 所有 node.id 的最大值
  "last_link_id": 12,            // 必须 >= 所有 link 的最大 id
  "nodes": [ ... ],
  "links": [ [1, 2, 0, 5, 1, "MODEL"], ... ],
  "groups": [ ... ],             // 可选，视觉分组
  "config": {},
  "extra": {"ds": {"scale": 0.9, "offset": [0, 0]}, "frontendVersion": "1.58.5"},
  "version": 0.4
}
```

可选顶层键（既有工作流里常见，非必需）：`seed_widgets`（种子快照）、`extensions`、`extra.ue_links`（cg-use-everywhere 的虚拟连线）、`extra.subgraphs`（子图定义）。

## 2. 节点对象

```json
{
  "id": 7,
  "type": "KSampler",
  "pos": [1200, 400],
  "size": [300, 260],
  "flags": {},
  "order": 6,                       // 执行顺序提示，前端按连线重算，可随便填
  "mode": 0,                        // 0=正常 2=静音(不执行) 4=旁路(直通)
  "title": "采样-主",                // 可选，显示用
  "inputs": [
     {"name": "model", "type": "MODEL", "link": 3},
     {"name": "seed", "type": "INT", "widget": {"name": "seed"}, "link": null}
  ],
  "outputs": [
     {"name": "LATENT", "type": "LATENT", "slot_index": 0, "links": [8]}
  ],
  "properties": {"Node name for S&R": "KSampler", "cnr_id": "comfy-core"},
  "widgets_values": [42, "randomize", 8, 1, "euler", "simple", 1],
  "widgets_values_named": {"seed": 42, "control_after_generate": "randomize", "steps": 8, "cfg": 1,
                            "sampler_name": "euler", "scheduler": "simple", "denoise": 1}
}
```

要点：

- **inputs 里必须同时列出连线输入和控件输入**。控件输入要带 `"widget": {"name": ...}` 且 `"link": null`；否则前端不渲染该控件。
- **widgets_values 是位置数组**，顺序 = 节点类 INPUT_TYPES 中控件型输入的出现顺序（必填在前、可选在后）。
- **widgets_values_named** 是参考实例前端（≥1.41）额外写出的命名字典，API 转换用它最稳；旧前端不会写这个键，缺失时按位置映射。
- **种子类 INT 会多占一个位置**：object_info 中带 `"control_after_generate": true` 的 INT（KSampler.seed、RandomNoise.noise_seed 等），在 `widgets_values` 里紧跟着插入 `"randomize" / "fixed" / "increment" / "decrement"`，而 `widgets_values_named` 里多一个 `control_after_generate` 键。漏掉会让之后所有控件值错位。
- `localized_name` 可省略（参考实例是中文前端，会按 locale 自动补）；`label` 也可省略。
- 输出槽的 `slot_index` 建议写，方便阅读；`links` 必须包含所有以该输出为源的 link id。
- 节点的 `properties.cnr_id` 只是包标识，可省略；`"Node name for S&R"` 建议保留节点类型名。

## 3. links 数组

```json
[link_id, source_node_id, source_slot, target_node_id, target_slot, "TYPE"]
```

- `link_id` 全局自增，不得重复；
- 目标节点对应 `inputs[target_slot]` 的 `"link"` 必须等于该 id；
- 源节点对应 `outputs[source_slot].links` 必须包含该 id；
- `"TYPE"` 必须与输入槽 `type` 一致（或两边之一为 `*`）。

## 4. groups（可选）

```json
{"id": 20, "title": "加载器", "bounding": [-584, -60, 418, 586], "color": "#c47b30", "font_size": 24, "flags": {}}
```

`bounding = [x, y, width, height]`。分组只是视觉框，不影响执行；建议按"加载器/提示词/采样/解码/输出"分区，方便用户。

## 5. mode 与旁路

- `mode: 2`（mute）：提交 API 时该节点被丢弃（其下游若缺输入会报错，通常配合 `Any Switch`、`rgthree Fast Groups Muter` 使用）。
- `mode: 4`（bypass）：前端提交时会把输入透传到输出（按类型匹配的第一个输入）。**API 转换没有实现旁路透传**——本技能的 `ui_to_api` 直接跳过 mute/bypass 节点，所以自建工作流不要依赖 bypass，用开关节点（Any Switch / LazySwitch）更可靠。

## 6. SetNode / GetNode（rgthree 虚拟连线）

既有工作流大量使用 `SetNode` + `GetNode` 代替长连线：`SetNode` 的控件是变量名，`GetNode` 用同名变量取回，**JSON 里没有对应 link**。
自建工作流建议直接连真实 link（可校验、可转换）；只有在改造既有工作流并需要保持其结构时才用 Set/Get。

## 7. 子图（subgraph）

两种存放位置都要支持：

- **新格式（前端 1.5x / 官方模板）**：顶层 `definitions.subgraphs[]`；
- **旧格式**：`extra.subgraphs.subgraphs[]`（少量老文件还在用）。

子图对象含 `id / name / nodes / links / inputs / outputs / inputNode / outputNode / widgets`，
顶层/父级节点里出现 `type` 等于子图 `id` 的实例节点，`inputs/outputs` 就是子图边界槽。

官方 Comfy-Org 模板几乎全部是"子图包裹"：顶层只有 `SaveImage` + 一个子图实例，真实链路在
`definitions.subgraphs` 里（见 `references/official-templates.md`）。所以：

- 读别人的模板时，用 `python scripts/comfy.py inspect <wf.json>` 展开查看真实节点链；
- **不要手写子图**：需要复用逻辑时，复制既有子图工作流改参数，或把子图展开成普通节点重搭。

## 8. API 提交格式（/prompt）

```json
{
  "prompt": {
    "7": {"class_type": "KSampler",
           "inputs": {"model": ["1", 0], "positive": ["5", 0], "negative": ["6", 0],
                      "latent_image": ["4", 0], "seed": 42, "steps": 8,
                      "cfg": 1, "sampler_name": "euler", "scheduler": "simple", "denoise": 1}}
  },
  "client_id": "uuid"
}
```

- 键是节点 id 的**字符串**；连线输入的值是 `["上游id", 输出槽序号]`；
- 控件值直接放原始 JSON 值（数字/字符串/布尔）；
- `control_after_generate` 不是 API 输入，必须剔除（否则报 unexpected input）；
- 自动增长的输入（如 `MiniMaxH3ReferenceToVideo.ref_images` 的 `COMFY_AUTOGROW_V3`）在 API 里是多个平铺键（`ref_images.ref_image_0` …），本技能的转换器只处理普通输入，遇到这类节点请复制既有工作流再改控件。

## 9. 自检清单

1. 每个 required 输入要么有 link，要么有控件值；
2. 每个非控件输入都有 link（`comfy.py validate` 会检查）；
3. COMBO 值必须精确等于 object_info 给出的选项字符串（模型文件名大小写、子目录都要一致）；
4. `last_node_id` / `last_link_id` 不小于实际最大值；
5. link 的 type 与目标输入 type 一致；
6. 至少一个输出节点（SaveImage / SaveVideo / PreviewImage / SaveImageAdvanced / VHS_VideoCombine / ZealmanVideoOutput…）。
