# 排错手册

## 连接层

| 现象 | 原因 / 处理 |
|---|---|
| `stats` 报 HTTP error / 连接被拒 | 隧道没开：先 `python scripts\comfy.py tunnel`（后台常驻）；或 16006 被占用，换 `--local-port 16007` 并设 `COMFY_BASE_URL=http://127.0.0.1:16007` |
| SSH `Authentication failed` | 密码/端口/env 不对；检查 `COMFY_SSH_*` |
| 隧道进程退出 | 长时间空闲被断；重新起 tunnel 即可，无需重启 ComfyUI |
| 首次请求很慢 | 模型冷加载（Zimage 首次 ~40s，H3/Wan 视频 2~5 分钟正常） |

## 提交/校验错误

提交 `/prompt` 返回 400 时，响应里有 `error` 与 `node_errors`：

```json
{"error": {"type": "prompt_outputs_failed_validation", "message": "Prompt outputs failed validation"},
 "node_errors": {"8": {"class_type": "KSampler", "errors": [{"type": "required_input_missing", "message": "Required input is missing", "details": "model"}]}}}
```

常见类型与修法：

| 错误 type | 含义 | 修法 |
|---|---|---|
| `value_not_in_list` | COMBO 值不在选项里（模型改名/子目录错） | `comfy.py nodes UNETLoader` 查真实文件名，或 `catalog` 后重跑 validate |
| `required_input_missing` | 必填输入既没连线也没控件值 | 补 link 或 widgets |
| `invalid_input_type` | 类型不匹配（MODEL 接到了 CONDITIONING） | 用 `comfy.py validate` 定位 link |
| `unknown_class_type` / 前端「Missing Node Types」 | 自定义节点缺失 | 对照 `custom_nodes/`；不要用未安装的节点 |
| `control_after_generate` 相关 | API 里混入了 UI 专用控件 | `comfy.py convert` 已自动剔除，不要手写 API |
| `prompt_no_outputs` | 没有输出节点 | 加 SaveImage/SaveVideo 等 |
| `bad_linked_input` / `return_type_mismatch` | 连线槽位/类型错 | 重建 link；参考 `workflow-format.md` |

本技能 `validate` 在本地就能抓到大部分：未连接输入、link slot 越界、type 不一致、COMBO 越界。

## 运行期

| 现象 | 处理 |
|---|---|
| `CUDA out of memory` | 降分辨率/批大小/帧数；换 int8/fp8/GGUF 模型；开 block swap（`WanVideoBlockSwap`、`UniBlockSwap`）、`MiniMaxLowVRAMAttention`、`VRAMCleanup` |
| 视频无声音 | H3/LTX 需要 `VAEDecodeAudio` + `CreateVideo(audio=...)` + `SaveVideo`；或 `LTXVConcatAVLatent` |
| 输出全黑/糊 | cfg 与步数不匹配（turbo 模型必须 cfg=1、6~9 步）；VAE 用错（Zimage 用 z_image_vae，Krea2 用 qwen/Krea2-HD vae） |
| 队列卡住 | `comfy.py queue` 查看；`comfy.py interrupt` 中断当前；重复排队会顺序执行 |
| `history` 里 status=error | 拉 `/history/<id>` 看 `status.messages`，通常含具体节点与异常 |
| 模型 not found（运行期） | 模型是符号链接，可能未挂载；`remote.py run "ls -l /root/ComfyUI/models/unet"` 检查 |

## 前端相关

- 工作流 JSON 放进 `user/default/workflows/<分类>/` 后，前端刷新即可在侧栏看到（文件名可中文）。
- 若打开后节点位置重叠：`build` 已按依赖深度排布；手改 pos 时保持 `[x,y]` 数值。
- 若控件值错位（改完 JSON 后 KSampler 的 steps 变成 sampler 名）：多半是漏了种子后的 `control_after_generate`，用 `comfy.py build` 重新生成，别手写 `widgets_values`。
- 不确定工作流是否有效，先 `comfy.py validate`，再 `comfy.py submit --wait`；宁可小分辨率跑通再放大参数。
