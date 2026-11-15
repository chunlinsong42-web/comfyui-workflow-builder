> 说明：下文的工作流文件名/模型名来自**参考实例**；在别的机器上请把模型名替换为你自己 /object_info 中的选项，节点链本身通用。

# 常用管线模板（从本实例 150 个工作流提炼）

每条给出：**参考工作流**（直接下载复制最快）→ 关键节点链 → 必填控件 → 经验参数。
节点签名见 `node-catalog.md`；模型可选值以 `object_info` 为准。

## 1. 文生图 — Zimage Turbo（最快、最稳）

参考：`C图像-Zimage/C01-文生图-Zimage基础版.json`、`templates/zimage-t2i.json`（本技能已跑通，512×768/6 步 ≈ 1 分钟内含加载）

```
UNETLoader(Zimage/z_image_turbo_bf16.safetensors)
CLIPLoader(qwen_3_4b.safetensors, type=qwen_image)
VAELoader(z_image_vae.safetensors)
EmptyLatentImage → CLIPTextEncode(text) ─┐
CLIPTextEncode(negative) ────────────────┤
KSampler(euler, simple, cfg=1, steps 6-9) ← model / latent / pos / neg
VAEDecode → SaveImage(filename_prefix="%date:yyyyMMdd%/image_")
```

- Turbo 模型 **cfg 必须为 1**，步数 6~9；neg 可留空（cfg=1 时基本无效）。
- 加风格 LoRA：`LoraLoaderModelOnly` 串在 UNETLoader 与 KSampler 之间（如 `Zimage/AWPortrait-Z.safetensors`，strength 0.6~1.0）。

## 2. 文生图 — Krea2 Turbo（写实质感）

参考：`C图像-Krea2/T01-Krea2文生图超强写实质感.json`、`T15-krea2-MJ风格工作流-在下鱼酥.json`、`templates/krea2-t2i.json`（已跑通）

```
UNETLoader(krea2/krea2_turbo_int8_convrot.safetensors)
CLIPLoader(qwen3vl_4b_bf16.safetensors, type=krea2)
VAELoader(qwen_image_vae.safetensors 或 Krea2-HD-vae.safetensors)
CLIPTextEncode ×2 → KSampler(euler, simple, cfg=1, steps 8) → VAEDecode → SaveImage
```

- 风格 LoRA 放 `krea2/` 下（`Krea2-realism-V2`、`krea2_darkbrush` 等）。
- 角色三视图：`C图像-Krea2/T04`/`T10`（配 `Krea2_Character_Design_4-View_V1.safetensors`）。
- 图像编辑：`T07-Krea2图像编辑krea2edit版单图双图.json`，链为 `Krea2EditModelPatch + Krea2EditGroundedEncode + LoadImage + VAEEncode → KSampler`。

## 3. 文生图 — Qwen-Image 2512（中文提示词最听话）+ SeedVR2 高清

参考：`A图像-生成/A01-文生图-Qwen2512高清放大.json`

```
UNETLoader(qwen/qwen_image_2512_fp8_e4m3fn.safetensors)
CLIPLoader(qwen_2.5_vl_7b_fp8_scaled.safetensors, type=qwen_image)
VAELoader(qwen_image_vae.safetensors)
LoraLoaderModelOnly ×3（Lightning-4steps + 两个真实感 LoRA）
CR SDXL Aspect Ratio(width,height) → EmptyLatentImage
KSampler(res_2s / beta57, cfg=1, steps=8)
VAEDecode → ImageScaleBy(0.5) → SeedVR2VideoUpscaler(resolution=2048) → LayerColor: AutoAdjustV2 → SaveImage
```

- 先在 720×1280 出图，再 SeedVR2 放大，显存友好。
- 编辑版换 `qwen/qwen_image_2.1_int8_convrot.safetensors` + `TextEncodeQwenImage21`（参考 `B18`），或 Qwen-Image-Edit-2511（参考 `A08`）。

## 4. 文生图 — SDXL / Illustrious（4K 直出+高清修复）

参考：`E图像-SDXL-IL/E01-文生图-Illustrious.json`、`E02`、`E03`

```
CheckpointLoaderSimple(SDXL ckpt) → CLIPSetLastLayer(-2) → CLIPTextEncode ×2
EmptyLatentImage(832×1216) → KSampler(dpmpp_2m_sde / euler_a, cfg 5-7, steps 25-30)
VAEDecode → ImageUpscaleWithModelBatched(4x-UltraSharp) → ImageScaleBy(0.5) → SaveImage
```

## 5. 视频 — Wan2.2 图生视频（WanVideoWrapper，14 个 G 系列参考）

参考：`G视频-Wan-Ltx/G01-图生视频-Wan2.2万相基础版.json`、`G05-LightX2V最强动态`、`G06-首尾帧`

```
WanVideoModelLoader(high noise) ┐
WanVideoModelLoader(low noise)  ┤→ WanVideoSetBlockSwap → WanVideoSetLoRAs → WanVideoSampler(×2 高/低噪)
WanVideoVAELoader + LoadWanVideoT5TextEncoder → WanVideoTextEncode(pos,neg)
WanVideoImageToVideoEncode(LoadImage 起始帧)
WanVideoDecode → VHS_VideoCombine(frame_rate=16/25, format=video/h264-mp4)
```

- 显存：480p 起步；720p 需要 block swap（25~40）+ fp8 权重。`LightX2V` LoRA 可 4~6 步。
- 首尾帧：`G06`（两张 LoadImage + WanVideoImageToVideoEncode 的 first/last）。

### 5b. Wan2.2 原生节点路线（更短，推荐作为起点）

参考：`templates/wan22-native-i2v.json`（结构校验通过；12 节点）

```
UNETLoader(Wan/TurboWan2.2-I2V-A14B-high-720P.pth)
CLIPLoader(umt5_xxl_fp16.safetensors, type=wan) + VAELoader(wan_2.1_vae.safetensors)
CLIPVisionLoader(clip_vision_h.safetensors) + LoadImage → CLIPVisionEncode(crop=center)
CLIPTextEncode ×2 → WanImageToVideo(width, height, length=81, batch_size=1,
                                    start_image=LoadImage, clip_vision_output=CLIPVisionEncode)
KSampler(25 步, cfg 6, euler, normal) → VAEDecode → SaveAnimatedWEBP(fps=16)
```

原生链的 `WanImageToVideo` 输出 `positive/negative/latent` 三个槽，采样器直接从它取。没有 block swap/长视频能力；那些场景回退到 wrapper 链。

## 6. 视频 — LTX 2.5（音画同出）

参考：`H50-LTX2.5文生视频`、`H51-图生视频`、`H52-首尾帧`、`M19-视频去字幕`

```
UNETLoader(Ltx/ltx-2.5-22b-distilled-transformer-comfy-int8-convrot.safetensors)
CLIPLoader(gemma4-12b-with-proj-ltx-2.5-comfy-int8-convrot.safetensors, type=ltxv 或对应类型)
VAELoader(ltx-2.5-video-vae-bf16.safetensors) + VAELoader/音频 VAE(ltx-2.5-audio-vae-bf16.safetensors)
ManualSigmas + RandomNoise + KSamplerSelect(euler_ancestral) → SamplerCustomAdvanced
CLIPTextEncode / TextGenerateLTX2Prompt → LTXVConditioning
VAEDecode + LTXVSeparateAVLatent/LTXVConcatAVLatent（带音频）→ CreateVideo/SaveVideo
```

- 25fps、121~241 帧；分辨率 768×512 起。

## 7. 视频 — MiniMax-H3 参考/图生视频（U 系列 50 个，本机主力）

参考：`U01-minimax_h3_多图参考生视频基础版.json`、`U03-文生视频基础版`、`U30-Singularity超双采放大`

```
UNETLoader(minimax/minimax_h3_ref2va_pruned_int8_convrot.safetensors)
CLIPLoader(qwen3vl_32b_minimax_h3_nvfp4_awq.safetensors, type=minimax)
VAELoader(minimax_h3_video_vae_fp16.safetensors) + VAELoader(minimax_h3_audio_vae_fp32.safetensors)
LoadImage ×N（参考图）→ MiniMaxH3ReferenceToVideo(prompt, width, height, length=124, ref_image_size=match)
RandomNoise + KSamplerSelect(res_multistep) + BasicGuider + BasicScheduler(steps=25) → SamplerCustomAdvanced
MiniMaxLowVRAMAttention(head_chunks=4) + MiniMaxChunkFeedForward(chunks=4)
VAEDecode + VAEDecodeAudio → CreateVideo(fps=24) → SaveVideo(mp4)
```

- 加速版：换 `minimax/minimax_h3_fl2v_turbo_8step…` + `LoraLoaderModelOnly`（LoRA `minimax_h3_turbo_*`），步数 4~8。
- 提示词通常是 JSON（subject_definitions + shots），见 U01 的 `CR Prompt Text`。
- 二采/三采、双模型：参考 `U09`、`U30`（ExtendIntermediateSigmas / SplitSigmas / LatentUpscaler3D）。

## 8. 对口型数字人

参考：`J04-对口型-InfiniteTalk单人图像驱动.json`、`J03`（长视频无衰减）

```
WanVideoModelLoader(Wan2_1-I2V-14B-480p…) + WanVideoVAELoader + LoadWanVideoT5TextEncoder
CLIPVisionLoader(clip_vision_h.safetensors) → WanVideoClipVisionEncode
DownloadAndLoadWav2VecModel → MultiTalkWav2VecEmbeds(LoadAudio + AudioCrop)
MultiTalkModelLoader(Wan2_1-InfiniteTalk-Single…) → WanVideoImageToVideoMultiTalk
WanVideoSampler → WanVideoDecode → VHS_VideoCombine(+audio)
```

## 9. 音频

- **Qwen3-TTS 配音/克隆**（`N06-Qwen3TTS音频克隆` / `N06-音频创造`）
  `TDQwen3TTSModelLoader(Qwen/Qwen3-TTS-12Hz-1.7B-Base|VoiceDesign)` → `TDQwen3TTSVoiceClone`（需 LoadAudio + Apply Whisper 取参考文本）或 `TDQwen3TTSVoiceDesign(instruct)` → `SaveAudio`。
- **ACE-Step 音乐**（`N05`）：`UNETLoader(acestep_v1.5_xl_turbo_bf16)` + `DualCLIPLoader` + `VAELoader(ace_1.5_vae)` + `TextEncodeAceStepAudio1.5` + `EmptyAceStep1.5LatentAudio` + `KSampler` + `VAEDecodeAudio` + `SaveAudioMP3`。
- **MiniMax Music3**（`N08`）：`UNETLoader(minimax_music3_dit_*)` + `MiniMaxMusic3TextEncode` + `EmptyMiniMaxMusic3LatentAudio` + `KSampler` + `VAEDecodeAudioTiled`。

## 10. 放大 / 修复 / 去水印

- **SeedVR2 TTP 分块放大**（`M02`）：`SeedVR2LoadDiTModel` + `SeedVR2LoadVAEModel` → `TTP_Tile_image_size` + `TTP_Image_Tile_Batch` → `SeedVR2VideoUpscaler` → `TTP_Image_Assy` → SaveImage。
- **RTX VSR 快速放大**（`M07`，6 个节点）：`LoadImage → RTXVideoSuperResolution(resize_type=scale by multiplier, quality=ULTRA) → PreviewImage`。
- **视频超分**：FlashVSR（`M15`）、VOSR2（`M18`）、RelayVSR（`M20`）、LTX2.5 超分（`M16/H54`）。
- **视频去字幕/去水印**：`M19`（LTX 2.5 + `ltx2.3-ic-subtitles-remove-general` LoRA，prompt 写 "remove subtitles"）。

## 11. 编辑器与增强套路

- **二采/三采**：`SamplerCustomAdvanced`（第一遍）+ `SplitSigmas/ExtendIntermediateSigmas` + 第二遍 `SamplerCustomAdvanced`（手动改动 sigma、denoise），配合 `LatentUpscaleBy`/`MinimaxH3LatentUpscaler3D`。参考 `U30`、`C18`、`T03`。
- **本地 LLM 改写提示词**：`llama_cpp_model_loader(Qwen3-4b-Z-Image-Engineer…gguf)` + `llama_cpp_parameters` + `llama_cpp_instruct_adv` → 文本节点（参考 `C15`、`U00`）；视觉反推用 `Qwen3_VQA` / `Florence2Run` / `WD14Tagger`。
- **批量/循环**：`easy forLoopStart/forLoopEnd` + `easy batchAnything`；XY 图：`Z11-XY图表测试工作流`。
- **开关**：`Any Switch`、`LazySwitch2way`、`rgthree Fast Groups Muter/Bypasser`（分组开关）。

## 12. 文生图 — FLUX2-Klein 9B（国风/插画向）

参考：`templates/flux2-klein-t2i.json`（结构校验通过）、`C12-瑶光-动漫-MJ风格工作流`、`T16-krea2-MJ风格工作流V4`

```
UNETLoader(flux/flux-2-klein-9b-fp8.safetensors)
CLIPLoader(qwen_3_8b_fp8mixed.safetensors, type=flux2, device=default)
VAELoader(flux2-vae.safetensors)
EmptyFlux2LatentImage(1024×1024) → CLIPTextEncode ×2
KSampler(res_2s / bong_tangent, cfg=1, steps=10) → VAEDecode → SaveImage
```

- 参数取自 C12 实测；Klein 走 cfg=1 的蒸馏路线。
- 风格 LoRA 放 `flux/` 下（如 `Flux/Klein-yizhixing-lora.safetensors`，strength 0.6）。
- 也可用 `flux/flux-2-klein-4b*` 小模型省显存。
