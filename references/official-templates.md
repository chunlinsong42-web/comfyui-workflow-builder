# 官方模板（Comfy-Org/workflow_templates）学习笔记

来源：<https://github.com/Comfy-Org/workflow_templates> · 抓取于 2026-11-16
索引 `templates/index.json` + 10 个代表性模板（展开子图后分析）。

## 1. 目录规模

| 分组 | 数量 | 分组 | 数量 |
|---|---:|---|---:|
| Foundation / Image | 226 | Foundation / Video | 227 |
| Foundation / Image Tools | 57 | Foundation / Video Tools | 59 |
| Foundation / Audio | 49 | Foundation / 3D Model | 51 |
| Foundation / LLM | 22 | Foundation / Vector | 9 |
| Foundation / Node Basics | 7 | Applied / Product & Ads | 16 |
| Applied / Character & Fashion | 28 | Applied / Brand & Design | 15 |

合计 **766** 个模板。标签统计：`API` 439（云模型，不适用本地）、`Video` 151、`Image Edit` 122、
`Text to Image` 116、`Image to Video` 88、`Text to Video` 58、`Int8` 47、`3D` 47、`ControlNet` 26。
模型覆盖：Nano Banana Pro 42、Wan 36、FLUX 33、MiniMax H3 29、Qwen-Image-Edit 16、LTX-2.3 15、Z-Image-Turbo 13…

## 2. 关键格式发现：官方模板是"子图包裹"的

官方新模板把主流程塞进 **subgraph**，顶层只剩 `SaveImage/SaveVideo` 和子图实例：

```json
{
  "nodes": [ {"type": "SaveImage"}, {"type": "7b34ab90-36f9-45ba-a665-71d418f0df18"} ],
  "definitions": { "subgraphs": [ { "id": "7b34ab90-...", "nodes": [...], "links": [...] } ] }
}
```

- 子图定义在 **`definitions.subgraphs`**（顶层），不是 `extra.subgraphs`（旧前端写法，少量老文件仍在 `extra` 下）。
- 子图实例节点 `type` = 子图 UUID；`inputs/outputs` 对应子图边界。
- 因此直接读顶层 `nodes` 只能看到 3~8 个节点，真实链路要展开。

本技能的 `comfy.py inspect <wf.json>` 会打印展开后的节点链与关键控件（只读，不改文件）。

## 3. 代表性模板展开后的链路

### Z-Image-Turbo（image_z_image_turbo）

```
CLIPLoader + UNETLoader + VAELoader
CLIPTextEncode → ConditioningZeroOut → KSampler
EmptySD3LatentImage → ModelSamplingAuraFlow → KSampler
VAEDecode → SaveImage
```

与参考实例 `C01` 的差异：官方用 `EmptySD3LatentImage` + `ModelSamplingAuraFlow`（shift 调节），
实例版用 `EmptyLatentImage` + 直接 KSampler；turbo 参数仍为 cfg=1、6~9 步、euler/simple。

### Krea2 Turbo（image_krea2_turbo_t2i）

```
UNETLoader + CLIPLoader + VAELoader
CLIPTextEncode → ConditioningZeroOut → KSampler
LoraLoaderModelOnly（可选）
TextGenerate + StringConcatenate + ComfySwitchNode（内置提示词改写开关）
ResolutionSelector → EmptyLatentImage → KSampler → VAEDecode → SaveImage
```

### Qwen-Image 2.1（image_qwen_image_2_1_t2i / _image_edit）

```
UNETLoader(qwen_image_2.1_int8_convrot) + CLIPLoader(qwen3vl_8b_int8_convrot, qwen_image)
VAELoader(qwen_image_2.1_vae_bf16)
TextEncodeQwenImage21(resolution=1024) → EmptyLatentImage(1024²)
QwenImage21Cache + KSampler(25 步, cfg=1, euler, simple) → VAEDecode → SaveImageAdvanced
```

编辑版额外：`LoadImage ×2 + BatchImagesNode + TextEncodeQwenImage21 + 提示词增强 LLM（TextGenerate）+ ComfySwitchNode`。

### FLUX.2 [Klein] 9B（image_flux2_text_to_image_9b）

```
UNETLoader + CLIPLoader + VAELoader
CLIPTextEncode ×2 → CFGGuider
KSamplerSelect + Flux2Scheduler + RandomNoise + EmptyFlux2LatentImage
SamplerCustomAdvanced → VAEDecode → SaveImage
```

注意：FLUX2 走 `Flux2Scheduler` + `CFGGuider` + `SamplerCustomAdvanced`，不是普通 KSampler。

### SDXL（image_sdxl_simple）

经典 8 节点：`CheckpointLoaderSimple + CLIPTextEncode ×2 + EmptyLatentImage(1024²) + KSampler(25 步, cfg=7, dpmpp_2m, karras) + VAEDecode + SaveImage`。

### Wan 2.2 14B I2V（video_wan2_2_14B_i2v）

```
UNETLoader ×2（high noise / low noise）+ VAELoader + CLIPLoader
LoraLoaderModelOnly ×2 + ModelSamplingSD3 ×2
CLIPTextEncode ×2 + WanImageToVideo + CreateVideo
KSamplerAdvanced ×2（高噪/低噪各一段）→ VAEDecode → SaveVideo
ComfySwitchNode 若干（开关：首帧/尾帧、LoRA、高低噪）
```

与我们 `patterns.md §5b` 的单模型简化版不同：**官方 14B 是双模型两段采样**。

### LTX-2.5 I2V（video_ltx2_5_i2v）

```
CLIPLoader + UNETLoader + VAELoader(video) + VAELoader(audio)
CLIPTextEncode ×2 + LTXVConditioning + LTXVImgToVideoInplace
ManualSigmas + RandomNoise + KSamplerSelect + LTXVDualCFGGuider + SamplerCustomAdvanced
LTXVLatentUpsampler → 第二段 ManualSigmas + SamplerCustomAdvanced（放大后重采样）
LTXVSeparateAVLatent / LTXVConcatAVLatent + VAEDecodeTiled + LTXVAudioVAEDecode + CreateVideo
```

两段式 + 音画双 VAE，节点多（展开约 47 个），适合直接复制模板再改参数。

### MiniMax-H3 R2V（video_minimax_h3_r2v）

```
UNETLoader(ref2va_int8) + CLIPLoader(qwen3vl_32b, minimax)
VAELoader(video int8) + VAELoader(audio fp32)
LoadImage ×N → MiniMaxH3ReferenceToVideo(1344×768, length=124, ref_image_size=match)
RandomNoise + KSamplerSelect(res_multistep) + BasicScheduler(simple, 20 步) + BasicGuider + SamplerCustomAdvanced
LoraLoaderModelOnly(turbo 4step) → VAEDecode + VAEDecodeAudio → CreateVideo(24fps) → SaveVideo
```

与参考实例 U01 几乎一致；官方默认 20 步 + 4 步 turbo LoRA 两条路径用 `ComfySwitchNode` 切换。

### SeedVR2 放大（utility_seedvr2_image_upscale）

```
LoadImage → SeedVR2LoadDiTModel + SeedVR2LoadVAEModel → SeedVR2VideoUpscaler
GetImageSize + SimpleMath+ + PrimitiveFloat + ImpactCompare + LayerUtility: If（按尺寸决定倍率）
→ SaveImage / ImageCompare（前后对比）
```

## 4. 官方 vs 参考实例：参数对照

| 模型 | 官方模板 | 参考实例（150 工作流统计） |
|---|---|---|
| Z-Image Turbo | cfg=1，6~9 步，euler/simple，ModelSamplingAuraFlow | cfg=1，8 步，euler/simple（median） |
| Krea2 Turbo | cfg=1，8~10 步 | 10 步，euler/simple |
| Qwen 2.1 | 25 步，cfg=1，euler/simple | 14 步（median），res_2s/beta57 与 euler/simple 混用 |
| FLUX2 Klein | Flux2Scheduler + CFGGuider | res_2s/bong_tangent，cfg=1，10 步 |
| SDXL | 25 步，cfg=7，dpmpp_2m/karras | 6 步（含 turbo 变体），euler/simple |
| Wan 2.2 I2V | 双模型两段，20~30 步，cfg 5~7 | 25 步，euler/normal，cfg=6 |
| LTX 2.5 | ManualSigmas 两段 + 音画 VAE | 手动 sigmas，4~8 段 |
| H3 R2V | 20 步 simple（或 4 步 turbo LoRA） | 10 步 median，beta/simple |

结论：**turbo/蒸馏模型统一 cfg=1**；步数差异来自是否挂 turbo LoRA；官方更倾向
`SamplerCustomAdvanced`（显式 scheduler/sigmas），实例更常用 `KSampler` 简版。

## 5. 怎么用这些模板

1. **直接复制**：官方模板依赖子图与大量自定义节点，复制到本地改参数最稳（`remote.py put` 到 workflows 目录）。
2. **拆开重建**：用 `comfy.py inspect` 看展开链，再按 `patterns.md` 的 recipe 语法重建；
   适合只需要主干（加载器→编码→采样→解码→保存）的情况。
3. **注意模型文件**：官方模板的模型名（`sd_xl_base_1.0`、`qwen_image_2.1_int8_convrot` 等）未必在你的机器上，
   `build/validate` 会报 `value_not_in_list`，换成你 `/object_info` 里的文件名。
4. **API 模板跳过**：439 个带 `API` 标签的模板调用云端模型（Nano Banana Pro、FLUX 3 API 等），
   本技能只处理本地节点工作流。
