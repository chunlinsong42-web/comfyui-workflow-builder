# 自动修复循环（最多 5 轮）

借鉴 21Pdontno/comfyui-workflow-skills 的「协调者 + 专家」模式，结合本技能的离线校验器实现。
核心：**每轮只改一类问题，改完立刻重校验**；5 轮不收敛就停下来汇报，别无限重试。

## 循环

```
validate ──通过──> submit(小参数) ──成功──> 放大参数正式跑
   │                     │
   └─有错─> 分类 ─> 修 recipe ─┐
                              └──> 回到 validate
```

提交失败时从 `/history/<id>` 的 `status.messages` 或 `/prompt` 的 `node_errors` 取错误。

## 错误分类与修法

### A. 连接类（Connection Specialist）

| 症状 | 修法 |
|---|---|
| `required input 'x' is not connected` | 在 recipe 的 `links` 补 `"源.输出 -> 节点.x"` |
| `link type mismatch` | 源输出类型和目标输入类型不一致：换槽位（`CONDITIONING` 可能是 `positive`/`negative`） |
| slot out of range | 该节点输出槽数不对：用 `comfy.py nodes <类型>` 看 out 列表，改用输出名引用 |
| `return_type_mismatch` / `bad_linked_input` | 同类型问题；检查是否把 `LATENT` 接到 `IMAGE` 输入（需要 VAEDecode 中转） |

### B. 参数类（Parameter Specialist）

| 症状 | 修法 |
|---|---|
| `value_not_in_list`（COMBO 越界） | `comfy.py nodes <节点>` 查真实选项；模型名必须含子目录（如 `Zimage/z_image_turbo_bf16.safetensors`） |
| `required_input_missing`（widget） | 该控件没给值：在 `widgets` 补；若默认值类型不对，显式写正确类型 |
| 数值范围错（steps=0、cfg 越界） | 对照 `node-catalog.md` 的 min/max |
| 种子无效 | 用数字；`build` 会自动补 `control_after_generate` |

### C. 结构类（Structure Specialist）

| 症状 | 修法 |
|---|---|
| `unknown class_type` / Missing Node Types | 该节点未安装：换等价节点（查 catalog），或复制含该节点的既有工作流 |
| 缺输出节点 | 加 `SaveImage/SaveVideo/SaveAudio/SaveAnimatedWEBP` 等 |
| 循环依赖 | 拆环：用 `SetNode/GetNode`（改造既有）或把中间结果存成两个阶段 |
| autogrow / dynamic combo / 子图 | recipe 不支持，改走「复制既有工作流 + 改控件」路线 |

### D. 资源类（Resource Specialist）

| 症状 | 修法 |
|---|---|
| `CUDA out of memory` | 分辨率减半 → 帧数/批量减半 → 换 int8/fp8/GGUF → block swap / LowVRAMAttention → 最后才考虑换小模型 |
| 首次加载超时 | 正常（视频模型 2~5 分钟）；`--timeout` 加到 1800 以上 |
| 队列卡住 | `comfy.py queue` 看状态；`comfy.py interrupt` 中断 |
| 输出黑图/噪声 | cfg 与步数不匹配（turbo 必须 cfg=1）；VAE 用错（Zimage 用 z_image_vae，Krea2 用 qwen_image_vae） |

## 每轮动作模板

```powershell
# 1) 修完 recipe 后重建
python scripts\comfy.py build recipe.json -o wf.json
# 2) 只看错误（不提交）
python scripts\comfy.py validate wf.json
# 3) 小参数试跑
python scripts\comfy.py submit wf.json --wait --download .\out --timeout 1800
```

## 停止条件

- 连续 5 轮仍有错 → 停下来，把最后一轮错误原文、已尝试的修法、当前 recipe 送给用户，给出 2~3 个可选方案（换模型 / 换路线 / 降低目标）。
- 任何一次 `submit` 成功即退出循环，进入"正式参数 + 交付"。
